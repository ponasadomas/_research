#!/usr/bin/env python3
"""Index Phase 7 Chrome exports and verify them offline; makes no requests."""

import base64
import hashlib
import json
import re
import struct
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'raw/browser2'
API = ROOT / 'raw/api/browser2'


def read(path):
    return json.loads(path.read_text())


def dump(name, value):
    (RAW / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def relative(path):
    return str(path.relative_to(ROOT)) if path else None


# Preserve body bytes, giving JSON bodies an appropriate extension.
for path in API.glob('*.body'):
    try:
        read(path)
    except (ValueError, UnicodeError):
        continue
    destination = path.with_suffix('.json')
    if destination.exists():
        raise RuntimeError(f'Unexpected existing destination: {destination}')
    path.rename(destination)


def body_file(reqid, kind):
    return next((p for ext in ('json', 'body')
                 if (p := API / f'{reqid}.{kind}.{ext}').exists()), None)


inventory = []
for line in (RAW / 'network-final.txt').read_text().splitlines():
    match = re.match(r'reqid=(\d+) (\S+) (.*?) \[([^]]+)\]$', line)
    if not match:
        continue
    reqid, method, listed_url, listed_status = match.groups()
    reqid = int(reqid)
    entry = dict(reqid=reqid, method=method, listed_url=listed_url,
                 listed_status=listed_status)
    metadata = RAW / f'{reqid}.network.txt'
    if metadata.exists():
        text = metadata.read_text()
        entry['metadata_file'] = relative(metadata)
        entry['url'] = re.search(r'^## Request (.*)$', text, re.M)[1]
        entry['status'] = re.search(r'^Status: (.*)$', text, re.M)[1]
        entry['response_body_unavailable'] = '<Response body not available anymore>' in text
        headers = re.search(r'### Request Headers\n(.*?)(?:\n### |\Z)', text, re.S)
        entry['request_headers_text'] = headers[1] if headers else None
    else:
        entry.update(url=listed_url, status=listed_status)
    parsed = urlparse(entry['url'])
    entry.update(host=parsed.netloc, path=parsed.path,
                 query=parse_qs(parsed.query, keep_blank_values=True),
                 fragment=parsed.fragment)
    entry['phase_by_request_order'] = ('assessment' if reqid < 58 else
                                     'paywall_or_back_boundary' if reqid < 84 else
                                     'return_from_paywall')
    for kind in ('request', 'response'):
        path = body_file(reqid, kind)
        entry[kind + '_body_file'] = relative(path)
        if path and kind == 'request':
            try:
                entry['request_json'] = read(path)
            except (ValueError, UnicodeError):
                entry['request_body_note'] = (
                    'Compressed Clarity body exported as lossy UTF-8; internal events unobserved.'
                    if 'clarity.ms' in parsed.netloc else 'Non-JSON body; see saved file.'
                )
    inventory.append(entry)

dump('network-inventory.json', {'first_reqid': 4, 'cutoff_reqid': 85, 'requests': inventory})
tracks = [e for e in inventory if e['path'] == '/api/track']
facebook = [e for e in inventory if e['host'] == 'www.facebook.com' and e['path'] == '/tr/']
trackers = [e for e in inventory if any(h in e['host'] for h in ('facebook', 'clarity', 'stripe'))]
dump('track-events.json', tracks)
dump('facebook-events.json', facebook)
dump('tracker-inventory.json', trackers)

stripe_path = body_file(82, 'request')
stripe = json.loads(unquote(base64.b64decode(stripe_path.read_text()).decode()))
dump('82.stripe-decoded.json', stripe)

start = read(API / 'start.response.json')
questions = []
for index, section in enumerate(start['sections']):
    group = ([section['anchor']] if section.get('anchor') else []) + section['items']
    if index < len(start['calibration']):
        group += [start['calibration'][index]]
    for area_index, item in enumerate(group, 1):
        position = len(questions) + 1
        snapshot = RAW / f'q{position:02}.snapshot.txt'
        text = snapshot.read_text()
        title = json.loads(re.search(r'heading (".*") level="2"', text)[1])
        skill = re.search(r'uid=\S+ "([A-Z][A-Z -]+)"', text)[1]
        questions.append(dict(position=position, display_area=section['area'],
                              area_position=area_index, area_count=len(group),
                              **item, answer='Yes' if item['rate'] >= .5 else 'Not yet',
                              on_screen_title=title, on_screen_skill=skill,
                              title_matches=title == item['title'], snapshot=relative(snapshot)))
dump('question-order.json', questions)

age12 = (ROOT / 'questions-by-age.md').read_text().split('## 12 months —')[1].split('\n## 13 months')[0]
expected = []
for line in age12.splitlines():
    match = re.match(r'- (?:\*\*anchor\*\* |\*calibration \([^)]*\)\* )?(\d+) · ([\d.]+) · (.*)', line)
    if match:
        expected.append((int(match[1]), float(match[2]), match[3]))

submitted = read(API / 'result.request.json')
result = read(API / 'result.response.json')
comparison = []
for kind in ('start', 'result'):
    for direction in ('request', 'response'):
        path = API / f'{kind}.{direction}.json'
        reference = ROOT / f'raw/api/browser/A-{kind}.{direction}.json'
        comparison.append(dict(file=relative(path), reference=relative(reference),
                               bytes_equal=path.read_bytes() == reference.read_bytes(),
                               byte_length=path.stat().st_size,
                               sha256=hashlib.sha256(path.read_bytes()).hexdigest()))

screenshots = []
for path in sorted((ROOT / 'screenshots/funnel2').glob('*.png')):
    data = path.read_bytes()
    width, height = struct.unpack('>II', data[16:24])
    screenshots.append(dict(file=relative(path), width=width, height=height,
                            sha256=hashlib.sha256(data).hexdigest()))

portrait = read(RAW / 'portrait.dom.json')
verification = dict(
    ageMonths=start['ageMonths'], corrected=start['corrected'],
    question_count=len(questions),
    age12_id_rate_title_order_equal=expected == [(q['id'], q['rate'], q['title']) for q in questions],
    all_on_screen_titles_match=all(q['title_matches'] for q in questions),
    answer_count=len(submitted['answers']), yes=sum(q['y'] for q in submitted['answers']),
    answers_follow_live_rates=submitted['answers'] == [dict(id=q['id'], y=int(q['rate'] >= .5)) for q in questions],
    extended=submitted['extended'], basic=result['basic'], detail=result['detail'],
    classic_comparisons=comparison, screenshots=screenshots,
    placeholder_count=len(portrait['placeholders']),
    placeholder_values=[n['node']['text'] for n in portrait['placeholders']],
    placeholder_filters=[n['node']['filter'] for n in portrait['placeholders']],
    other_hidden_report_nodes=portrait['hidden'],
    network_counts=dict(requests=len(inventory), tracks=len(tracks),
                        assessment=sum(e['path'] == '/api/assessment' for e in inventory),
                        lead=sum(e['path'] == '/api/lead' for e in inventory),
                        send_reading=sum(e['path'] == '/api/send-reading' for e in inventory),
                        facebook_events=len(facebook),
                        clarity_collect=sum('clarity.ms' in e['host'] and e['path'] == '/collect' for e in inventory)),
    hosts=dict(sorted(Counter(e['host'] for e in inventory).items())),
    paywall_navigation_url=next(e['url'] for e in inventory if e['reqid'] == 58),
    paywall_displayed_url=read(RAW / 'paywall.dom.json')['url'],
)
dump('verification.json', verification)

table = ['| # | Screen / counter | ID | API area | Rate | Answer | Skill label | Exact on-screen question |',
         '| --- | --- | --- | --- | --- | --- | --- | --- |']
for q in questions:
    table.append(f"| {q['position']} | {q['display_area']} {q['area_position']}/{q['area_count']} | {q['id']} | {q['area']} | {q['rate']:g} | {q['answer']} | {q['on_screen_skill']} | {q['on_screen_title']} |")
(RAW / 'question-comparison.md').write_text('\n'.join(table) + '\n')
print(json.dumps({k: verification[k] for k in ('network_counts', 'classic_comparisons',
                 'all_on_screen_titles_match', 'age12_id_rate_title_order_equal',
                 'answers_follow_live_rates', 'placeholder_count', 'hosts')}, indent=2))
