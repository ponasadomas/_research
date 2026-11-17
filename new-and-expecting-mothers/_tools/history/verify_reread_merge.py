#!/usr/bin/env python3
"""Verify recovery coverage, whole evidence quotations and preserved history.

Run with python3 -I. Does not edit source data, ledgers, digests or raw inventories.
The immutable merge manifest records the input hashes and previous citations.
"""
from pathlib import Path
import collections
import csv
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
WORK = ROOT / 'scratchpad/unfilter-reread'
manifest = json.loads((WORK / 'merge-2026-11-17.json').read_text())
coverage = json.loads((ROOT / 'synthesis/reread-coverage.json').read_text())
errors = []


def check(value, message):
    if not value:
        errors.append(message)


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


rows = [q for p in sorted((ROOT / 'voice').glob('*.jsonl')) for q in read_jsonl(p)]
by_id = {q['id']: q for q in rows}
new = {rid for rid in by_id if rid.startswith('glu')}
check(len(rows) == len(by_id) == 6991, 'Voice ids duplicated or total changed')
check(len(new) == manifest['total_new'] == 4829, 'Recovery quote total changed')

assignments = [q for p in sorted(WORK.glob('assign-ur*.tsv'))
               for q in csv.DictReader(p.open(), delimiter='\t')]
assigned = {q['unit_id'] for q in assignments}
queue = list(csv.DictReader((WORK / 'queue.tsv').open(), delimiter='\t'))
check(len(assignments) == len(assigned) == 3807, 'Assignment unit count/duplicates')
check(assigned == {q['unit_id'] for q in queue}, 'Queue/assignment coverage differs')
ledger = {}
reader_counts = collections.Counter()
for path in sorted((ROOT / 'sources').glob('reddit-reading-ur*.md')):
    for line in path.read_text().splitlines():
        if not line.startswith('|'):
            continue
        cells = [c.strip().strip('`') for c in line.split('|')[1:-1]]
        if len(cells) < 3 or cells[0] not in assigned:
            continue
        check(cells[0] not in ledger, 'Unit repeated in ledgers: ' + cells[0])
        count = int(cells[1])
        ledger[cells[0]] = count
        reader_counts[path.stem[-4:]] += count
check(set(ledger) == assigned, 'Unaccounted assignment units')
check(sum(ledger.values()) == 4829, 'Ledger quote total differs')
check(sum(n > 0 for n in ledger.values()) == 3747, 'Quoted-unit total differs')
for reader, count in reader_counts.items():
    check(len(read_jsonl(ROOT / ('voice/reddit-' + reader + '.jsonl'))) == count,
          'Reader ledger/voice total differs: ' + reader)

text = (ROOT / 'synthesis/evidence.md').read_text()
lines = text.splitlines()
blocks = []
locations = {}
current_theme = None
for n, line in enumerate(lines):
    anchor = re.fullmatch(r'<a id="reread-([a-z-]+)"></a>', line)
    if anchor:
        current_theme = anchor[1]
    match = re.fullmatch(r'\[([a-z][a-z0-9]*-\d+)\]', line)
    if not match or n + 1 >= len(lines) or not lines[n + 1].startswith('>'):
        continue
    rid = match[1]
    parts = []
    k = n + 1
    while k < len(lines) and lines[k].startswith('>'):
        parts.append(lines[k][2:] if lines[k].startswith('> ') else lines[k][1:])
        k += 1
    blocks.append(rid)
    locations[rid] = current_theme
    if rid in new:
        check('\n'.join(parts) == by_id[rid]['quote'],
              'Recovery block is not the exact complete field: ' + rid)
check(len(blocks) == len(set(blocks)) == 4970, 'Evidence duplicate/block count')
flagged = {q['id'] for q in rows if q.get('marketing_eligible') is False}
check(set(blocks) == new | flagged, 'Evidence missing recovered/restored ids')
check(set(manifest['assignment']) == new, 'Thematic assignment missing ids')
for rid in new:
    check(locations.get(rid) == manifest['assignment'][rid], 'Theme differs: ' + rid)
for kind in ['money', 'request']:
    expected = set(manifest['digest_' + kind + '_ids'])
    found = set()
    for line in lines:
        if re.match(r'- Digest \d+, ' + kind + r's?:', line):
            found.update(re.findall(r'\[(glu\d+-\d+)\]', line))
    check(found == expected, 'Missing/extra ' + kind + ' register ids')
    check(expected <= set(blocks), 'Unquoted ' + kind + ' items')

id_rx = r'\[([a-z][a-z0-9]*-\d+)\]'
conclusion_ids = set()
per_file = {}
anchors = set(re.findall(r'<a id="([^"]+)"', text))
for relative, previous in manifest['prior_conclusion_ids'].items():
    content = (REPO / relative).read_text()
    ids = set(re.findall(id_rx, content))
    per_file[relative] = {'distinct_ids': len(ids), 'new_ids': len(ids & new)}
    check(set(previous) <= ids, 'Previous citations dropped: ' + relative)
    check(ids <= set(by_id), 'Unresolved citations: ' + relative)
    check(ids & new <= set(blocks), 'Conclusion evidence missing: ' + relative)
    for target in re.findall(r'evidence\.md#(reread-[a-z-]+)', content):
        check(target in anchors, 'Evidence anchor missing: ' + target)
    conclusion_ids.update(ids)
counts = json.loads((ROOT / 'synthesis/counts.json').read_text())
check(counts['total'] == len(rows), 'Counts total stale')
check(counts['language_bank_entries'] == len(rows), 'Bank count stale')
check(counts['evidence_reproduced_quote_ids'] == len(set(blocks)), 'Evidence count stale')
check(counts['conclusion_distinct_quote_ids'] == len(conclusion_ids), 'Conclusion count stale')
check(counts['conclusion_new_reread_quote_ids'] == len(conclusion_ids & new), 'New citation count stale')
check(counts['source_class'] == dict(collections.Counter(q['source_class'] for q in rows)),
      'Source-class counts stale')
for relative, want in manifest['protected_sha256'].items():
    path = REPO / relative
    check(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == want,
          'Protected input changed: ' + relative)

native = {rid for rid in assigned if re.fullmatch('[a-z0-9]{5,10}', rid)}
old = set(json.loads((ROOT / '_raw/audit/wave03-2026-10-24/all-reddit-full-post-ids-v2.json').read_text()))
check(len(native | old) == coverage['reddit_full_post_ids_distinct_now'] == 8614,
      'Distinct Reddit original count differs')
for label, difference in coverage['reddit_body_inventory_differences'].items():
    before = set(json.loads((ROOT / difference['frozen_inventory']).read_text()))
    check(set(difference['read_in_recovery']) == before & native,
          'Recovered original ids differ: ' + label)
    check(set(difference['remaining_ids']) == before - native,
          'Unread original ids differ: ' + label)
    check(len(difference['remaining_ids']) == coverage['reddit_body_backlogs_remaining'][label],
          'Unread original count differs: ' + label)
check(coverage['assigned_saved_text_unread'] == 0 and coverage['previous_MSE_tail_posts_remaining'] == 0,
      'Recovery completion state differs')
result = {'quotes_read_in_recovery': len(new), 'voice_records': len(rows),
          'evidence_full_quote_ids': len(set(blocks)), 'new_full_evidence_quote_ids': len(new),
          'money_index_ids': len(manifest['digest_money_ids']),
          'request_index_ids': len(manifest['digest_request_ids']),
          'conclusion_distinct_ids': len(conclusion_ids),
          'conclusion_new_recovery_ids': len(conclusion_ids & new),
          'conclusion_files': per_file, 'assigned_units_accounted_for': len(ledger),
          'protected_files_unchanged': len(manifest['protected_sha256']),
          'duplicate_ids': len(rows) - len(by_id), 'failed': len(errors), 'errors': errors}
print(json.dumps(result, indent=2))
sys.exit(bool(errors))
