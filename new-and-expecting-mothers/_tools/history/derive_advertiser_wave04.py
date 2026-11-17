#!/usr/bin/env python3
"""Derive Page/query ledgers from immutable, ordinary Chrome MCP captures.

Does not collect data or alter existing captures/voice files. Root text-pool
views are audit derivatives, not a reading declaration or quotation corpus.
"""
from pathlib import Path
import collections, datetime, hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '_raw/advertiser-census-wave04-2026-10-25'
OUT = ROOT / 'scratchpad/advertiser-wave04-root'
INVALID = {
    '008-nesting-notes-page': 'Unresolved public profile ID; replaced by 055.',
    '013-master-maternity-page': 'Public profile ID, not advertiser Page; replaced by 022.',
    '017-baby-sleep-answers-page-ui': 'Stale embedded data after SPA transition; replaced by 018.',
    '047-myregistry-page': 'Previous Busy Toddler Page after selection race; replaced by 047c.',
}

def value(d):
    text = '\n'.join(x.get('text', '') for x in d.get('browser_response', {}).get('content', []) if x.get('type') == 'text')
    match = re.search(r'```json\n(.*)\n```', text, re.S)
    return json.loads(match[1]) if match else None

def ads(v):
    return [a for c in v.get('connections', []) for e in c.get('edges', []) for a in e.get('node', {}).get('collated_results', [])]

def iso(ts):
    return datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).date().isoformat() if ts else None

if __name__ == '__main__':
    queries, pages = [], []
    for p in sorted((BASE / 'queries').glob('*.json')):
        d = json.loads(p.read_text())
        row = {'capture': str(p.relative_to(ROOT)), 'query': d.get('query'), 'kind': d.get('kind'), 'captured_at': d.get('captured_at'), 'capture_error': d.get('browser_response', {}).get('isError', False)}
        v = value(d)
        if v:
            row.update(url=v.get('url'), captured_at=v.get('captured_at'))
            if 'advertiser_page' in d.get('kind', '') or d.get('kind') in {'category_discovery', 'keyword_discovery'}:
                cs, aa, text = v.get('connections', []), ads(v), v.get('text', '')
                header = text.split('Ads\nAbout')[0].split('Search by keyword or advertiser')[-1].replace('\u200b', '').strip()
                dates = [iso(a['start_date']) for a in aa if a.get('start_date')]
                label = re.search(r'(?:~[\d,]+|>[\d,]+) results?', text)
                row.update(reported_active_results=cs[0].get('count') if cs else None,
                           visible_result_label=label[0] if label else '', loaded_native_ads=len(aa),
                           distinct_loaded_ids=len({str(a.get('ad_archive_id')) for a in aa}),
                           niches=d.get('niches'), page_id=d.get('expected_page_id'), page_header=header,
                           oldest_observed_active_start=min(dates) if dates else None,
                           newest_observed_active_start=max(dates) if dates else None,
                           has_next_page=[c.get('page_info', {}).get('has_next_page') for c in cs],
                           invalid_reason=INVALID.get(p.stem))
                if 'advertiser_page' in d.get('kind', '') and not row['invalid_reason']:
                    assert header, (p, 'empty Page identity')
                    assert row['distinct_loaded_ids'] == len(aa), (p, 'duplicate native IDs')
                    assert all(str(a.get('page_id')) == str(d.get('expected_page_id')) for a in aa), (p, 'outer Page mismatch')
                    assert all(a.get('is_active') is True for a in aa), (p, 'non-active record')
                    pages.append(row)
        queries.append(row)

    def jsonl(p, rows):
        p.write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in rows))

    jsonl(ROOT / 'sources/advertiser-wave04-query-ledger.jsonl', queries)
    jsonl(ROOT / 'sources/advertiser-wave04-page-census.jsonl', pages)
    print('Verified advertiser Pages:', len(pages), 'positive:', sum((x['reported_active_results'] or 0) > 0 for x in pages), 'zero:', sum(x['reported_active_results'] == 0 for x in pages))
    for x in pages:
        print(x['page_header'], x['reported_active_results'], 'loaded', x['loaded_native_ads'], 'oldest', x['oldest_observed_active_start'])

    # Present duplicate field strings once with exact SHA-256 and per-native-ID maps.
    retained = OUT / 'root-retained-ad-reads.json'
    if retained.exists():
        rows, pool, mapping = json.loads(retained.read_text()), {}, []
        for a in rows:
            rec, texts = a['record'], []
            def add(field, item):
                if isinstance(item, dict):
                    item = item.get('text')
                if not isinstance(item, str) or not item:
                    return
                digest = hashlib.sha256(item.encode()).hexdigest()
                if digest not in pool:
                    pool[digest] = {'text_id': f'rt{len(pool) + 1:03}', 'sha256': digest, 'text': item}
                texts.append({'field': field, 'text_id': pool[digest]['text_id'], 'sha256': digest})
            for key in ['body', 'title', 'caption', 'link_description', 'cta_text']:
                add(key, rec.get(key))
            for j, card in enumerate(rec.get('cards') or []):
                for key in ['body', 'title', 'caption', 'link_description', 'cta_text']:
                    add(f'cards[{j}].{key}', card.get(key))
            mapping.append({'ad_id': a['ad_id'], 'page_id': a['page_id'], 'start': rec['start_date'], 'link_url': rec['link_url'], 'format': rec['display_format'], 'texts': texts})
        jsonl(OUT / 'root-text-unit-map.jsonl', mapping)
        units = list(pool.values())
        jsonl(OUT / 'root-unique-ad-texts.jsonl', units)
        parts, current, size = [], [], 0
        for unit in units:
            line = json.dumps(unit, ensure_ascii=False)
            if current and size + len(line) > 14000:
                parts.append(current)
                current, size = [], 0
            current.append(line)
            size += len(line)
        if current:
            parts.append(current)
        for i, part in enumerate(parts, 1):
            (OUT / f'root-text-pool-{i:02}.jsonl').write_text('\n'.join(part) + '\n')
        print('Root retained native IDs:', len(rows), 'unique complete field texts:', len(units), 'human view parts:', len(parts))
