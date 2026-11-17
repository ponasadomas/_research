#!/usr/bin/env python3
"""Independent joins/counts/native-body checks for the bounded ad research.

Machine verification cannot establish human interpretation, delivery or profit.
The separate independent audit records the source-context spot checks.
"""
from pathlib import Path
import collections, csv, datetime, hashlib, json, re
from derive_advertiser_wave04 import ads, value, INVALID

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '_raw/advertiser-census-wave04-2026-10-25'
OUT = BASE / 'audit'
OUT.mkdir(exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()
native, source_hashes, queries = {}, {}, []
for p in sorted((BASE / 'queries').glob('*.json')):
    rel = str(p.relative_to(ROOT))
    source_hashes[rel] = sha(p.read_bytes())
    d = json.loads(p.read_text())
    v = value(d)
    if not v:
        continue
    aa = ads(v)
    queries.append((rel, d, v, aa))
    for a in aa:
        key = (rel, str(a['ad_archive_id']))
        assert key not in native, ('duplicate capture/ad key', key)
        native[key] = a

ledgers, read_rows, checked_occurrences, individually_read = {}, [], 0, set()
for p in sorted((ROOT / 'sources').glob('advertiser04-*-reading.jsonl')):
    rows = [json.loads(s) for s in p.read_text().splitlines() if s.strip()]
    ledgers[p.name] = len(rows)
    for q in rows:
        identity = str(q['ad_id'])
        assert (q.get('native_body_and_all_card_text_read_complete') is True
                or q.get('body_and_all_loaded_card_headline_text_read') is True
                or q.get('body_and_all_loaded_text_read') is True
                or q.get('full_available_body_and_card_text_read') is True
                or q.get('read_status') == 'full_loaded_text_read'), (p, identity, 'read flag')
        occurrences = q.get('source_occurrences')
        if not occurrences:
            source = next((q.get(k) for k in ['capture_file', 'raw_file', 'source_file', 'capture'] if q.get(k)), None)
            occurrences = [{'capture_file': source}]
        for occurrence in occurrences:
            source = occurrence.get('capture_file') or occurrence.get('raw_file')
            assert source and Path(source).stem not in INVALID, (identity, source, 'invalid capture')
            a = native[(source, identity)]
            individually_read.add((source, identity))
            assert a.get('is_active') is True, identity
            expected_page = str(q.get('advertiser_page_id') or q.get('page_id'))
            assert str(a.get('page_id')) == expected_page, (identity, 'outer Page')
            claimed_hash = occurrence.get('capture_sha256') or occurrence.get('sha256')
            if claimed_hash:
                assert source_hashes[source] == claimed_hash, (identity, 'capture hash')
            text = ((a.get('snapshot') or {}).get('body') or {}).get('text', '')
            claimed_body = occurrence.get('native_body_text_sha256') or q.get('native_body_text_sha256') or q.get('body_sha256') or q.get('native_body_sha256')
            assert claimed_body == sha(text.encode()), (identity, source, 'own-body hash')
            checked_occurrences += 1
        read_rows.append(q)

read_ids = [str(q['ad_id']) for q in read_rows]
assert len(read_ids) == len(set(read_ids)) == 604
pages = [json.loads(s) for s in (ROOT / 'sources/advertiser-wave04-page-census.jsonl').read_text().splitlines()]
page_ids = {x['page_id'] for x in pages}
assert len(pages) == len(page_ids) == 43
page_ad_ids = {str(a['ad_archive_id']) for row in pages for a in [a for rel, _, _, aa in queries if rel == row['capture'] for a in aa]}
assert len(page_ad_ids) == sum(x['loaded_native_ads'] for x in pages) == 603
assert set(read_ids) - page_ad_ids == {'1762465444948789'}
assert not page_ad_ids - set(read_ids)

unread, not_individually_read = [], []
for rel, d, v, aa in queries:
    if d.get('kind') not in {'keyword_discovery', 'category_discovery'}:
        continue
    for a in aa:
        identity = str(a['ad_archive_id'])
        if (rel, identity) not in individually_read:
            not_individually_read.append({'capture': rel, 'ad_id': identity, 'advertiser_page_id': str(a.get('page_id')), 'displayed_name': (a.get('snapshot') or {}).get('page_name'), 'same_id_fully_text_read_elsewhere': identity in set(read_ids), 'status': 'discovery_snapshot_not_individually_full_read; no new read credit'})
        if identity not in set(read_ids):
            unread.append({'capture': rel, 'ad_id': identity, 'advertiser_page_id': str(a.get('page_id')), 'displayed_name': (a.get('snapshot') or {}).get('page_name'), 'status': 'discovery_metadata_only_body_and_media_unread'})
(OUT / 'unread-discovery-ad-occurrences.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in unread))
(OUT / 'discovery-occurrences-not-individually-read.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in not_individually_read))

old = list(csv.DictReader((ROOT / 'sources/ad-body-reading-ledger.tsv').open(), delimiter='\t'))
old_read = {x['id'] for x in old if x['read_status'] == 'full_body_read' and sha((ROOT / x['raw_file']).read_bytes()) == x['body_sha256']}
old_hash_verified = set(old_read)
# The previous five visible-text continuation reads used full query captures,
# not the first63-body TSV. All five IDs are independently read natively now.
old_additional = {'1889792095496859', '3262395007292940', '1804441577549614', '1124475943769660', '2527356304342424'}
assert old_additional <= set(read_ids)
old_read |= old_additional
assert len(old_read) == 68
baseline = json.loads((ROOT / '_raw/audit/wave03-2026-10-24/final-structural-audit.json').read_text())
assert all(sha((ROOT / 'voice' / p).read_bytes()) == h for p, h in baseline['voice_file_hashes'].items())
old_inventory = json.loads((ROOT / '_raw/audit/wave03-2026-10-24/baseline-frozen-hashes.json').read_text())
for p, h in old_inventory.items():
    path = Path(p)
    if not path.is_absolute():
        path = (ROOT.parents[2] if p.startswith('mamivio.com/') else ROOT) / path
    assert sha(path.read_bytes()) == h, (p, 'baseline inventory')

independent = json.loads((ROOT / 'scratchpad/advertiser04-independent-audit/audit.json').read_text())
oversized = [str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and p.stat().st_size >= 100_000_000]
assert not oversized
report = {
    'compiled_date': '2026-10-25', 'browser': 'Chrome DevTools MCP, user-visible browser, port9225',
    'valid_distinct_advertiser_pages': len(pages),
    'pages_with_active_results': sum((x['reported_active_results'] or 0) > 0 for x in pages),
    'pages_with_zero_results': sum(x['reported_active_results'] == 0 for x in pages),
    'excluded_superseded_page_captures': INVALID,
    'fully_read_page_native_ad_ids': len(page_ad_ids), 'additional_discovery_only_full_read_ids': ['1762465444948789'],
    'full_read_distinct_ad_ids': len(read_ids), 'full_read_native_occurrences_checked': checked_occurrences,
    'full_read_ledgers': ledgers, 'retained_unread_ad_ids': [],
    'discovery_body_unread_occurrences': len(unread), 'discovery_body_unread_distinct_ids': len({x['ad_id'] for x in unread}),
    'unretained_discovery_snapshots_not_individually_full_read': len(not_individually_read),
    'explicitly_full_read_discovery_occurrences': sum((rel, str(a['ad_archive_id'])) in individually_read for rel, d, _, aa in queries if d.get('kind') in {'keyword_discovery', 'category_discovery'} for a in aa),
    'prior_body_TSV_hash_verified_ids': len(old_hash_verified),
    'prior_additional_declared_query_text_read_ids_now_natively_verified': sorted(old_additional),
    'prior_total_full_body_read_ids': len(old_read), 'overlap_prior_and_wave04': len(old_read & set(read_ids)),
    'cumulative_visible_body_read_distinct_ids': len(old_read | set(read_ids)),
    'unchanged_committed_voice_files': len(baseline['voice_file_hashes']), 'unchanged_baseline_voice_inventory_hashes': len(old_inventory),
    'voice_quotes': baseline['total'], 'new_voice_quotes': 0, 'media_viewed': 0,
    'independent_context_audit_path': 'scratchpad/advertiser04-independent-audit/audit.json',
    'oversized_files': oversized, 'failed': 0, 'errors': [],
    'limits': ['Active-result count is not a budget, unique concept count or customer count.',
               'No evidence of uninterrupted delivery, profit, ad-attributed sales or accepted prices.',
               'Whole libraries/creative media/variants uninspected beyond stated captures.',
               'Remaining canonical Google checks ended with Chrome connection refusal; no zero-spend inference.'],
}
(OUT / 'native-and-coverage-verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
(OUT / 'query-capture-hashes.json').write_text(json.dumps(source_hashes, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False, indent=2))
