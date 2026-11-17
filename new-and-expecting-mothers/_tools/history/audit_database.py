#!/usr/bin/env python3
"""Recount records and check structure; subject labels never exclude research."""
from pathlib import Path
import collections, datetime, json, random, re, sys

ROOT = Path(__file__).resolve().parents[1]
rows, errors = [], []
for p in sorted((ROOT / 'voice').glob('*.jsonl')):
    for n, line in enumerate(p.read_text().splitlines(), 1):
        if not line.strip(): continue
        try: q = json.loads(line)
        except Exception as e: errors.append(f'{p.name}:{n}: {e}'); continue
        q['_file'] = str(p.relative_to(ROOT)); rows.append(q)
        if len(q.get('context', '').split()) > 25: errors.append(f"{q.get('id')}: context exceeds 25 words")
        if not q.get('source_class'): errors.append(f"{q.get('id')}: missing source_class")
        if not q.get('evidence_kind'): errors.append(f"{q.get('id')}: missing evidence_kind")
        if not (ROOT / q.get('raw_file', 'MISSING')).is_file(): errors.append(f"{q.get('id')}: missing raw file")
ids = collections.Counter(q['id'] for q in rows)
errors += [f'duplicate id: {id}' for id, n in ids.items() if n > 1]
as_of = next((arg.split('=', 1)[1] for arg in sys.argv if arg.startswith('--as-of=')), datetime.date.today().isoformat())
datetime.date.fromisoformat(as_of)
counts = {'date': as_of, 'total': len(rows), 'files': {}, 'source_class': {}, 'evidence_kind': {}, 'speaker': {}, 'stage': {}, 'segment': {}, 'type': {}}
counts['files'] = dict(collections.Counter(q['_file'] for q in rows))
for k in ['source_class', 'evidence_kind', 'speaker', 'stage', 'segment', 'type']:
    counts[k] = dict(collections.Counter(q.get(k, 'not_tagged') for q in rows).most_common())
counts['themes'] = dict(collections.Counter(t for q in rows for t in q['themes']).most_common())
original_classes = {'reddit_archive','forum','forum_oblique','qa_community','app_review','book_review'}
counts['original_user_community_records'] = sum(q.get('source_class') in original_classes for q in rows)
counts['user_community_source_class_records'] = counts['original_user_community_records']
counts['original_user_community_records_definition'] = ('Legacy key: counts source-class tags, not authenticated independent original testimony. '
    'These collections also contain listing fragments, creator/commercial speech and second-hand accounts; evidence_kind and read_scope retain those distinctions.')
counts['historically_marked_records'] = sum(q.get('marketing_eligible') is False for q in rows)
counts['explicit_research_only_records'] = 0
index_path = ROOT / 'synthesis/quote-index.md'
counts['language_bank_entries'] = len(set(re.findall(r'\[([a-z0-9]+-\d+)\]', index_path.read_text()))) if index_path.exists() else 0
id_pattern = r'\[([a-z][a-z0-9]*-\d+)\]'
evidence = (ROOT / 'synthesis/evidence.md').read_text()
evidence_blocks = re.findall(r'^\[([a-z][a-z0-9]*-\d+)\]\n>', evidence, re.M)
conclusion_paths = [ROOT / 'synthesis' / name for name in
                    ['findings.md', 'niche-opportunities.md', 'purchase-evidence.md']]
conclusion_paths.append(ROOT.parent / 'main/synthesis/sub-niche-map.md')
conclusion_ids = {str(p.relative_to(ROOT.parent)): set(re.findall(id_pattern, p.read_text()))
                  for p in conclusion_paths}
combined_ids = set().union(*conclusion_ids.values())
counts['evidence_distinct_quote_ids'] = len(set(re.findall(id_pattern, evidence)))
counts['evidence_reproduced_quote_ids'] = len(set(evidence_blocks))
counts['conclusion_distinct_quote_ids'] = len(combined_ids)
counts['conclusion_new_reread_quote_ids'] = sum(i.startswith('glu') for i in combined_ids)
counts['conclusion_files'] = {name: {'distinct_ids': len(ids),
                           'new_reread_ids': sum(i.startswith('glu') for i in ids)}
                            for name, ids in conclusion_ids.items()}
coverage_path = ROOT / 'synthesis/reread-coverage.json'
if coverage_path.exists():
    recovery = json.loads(coverage_path.read_text())
    counts['rereading'] = {key: recovery[key] for key in
                          ['assignment_units', 'ledger_units', 'units_with_new_quotes',
                           'units_without_new_quotes', 'new_quote_records',
                           'assigned_saved_text_unread', 'full_discussions_unavailable',
                           'previous_MSE_tail_posts_remaining']}
out = [f'# Counts — {as_of}', '', 'Generated from files by `_tools/audit_database.py`. Counts are selected quote records, not people, prevalence, purchases or independent studies.', '', f"Total: {len(rows)} quote records."]
out += ['', f"Records in user/community source classes: {counts['user_community_source_class_records']}.",
        'Source classes identify collections, not independent original testimony: listing fragments, second-hand accounts and creator/commercial speech retain their evidence-kind and reading-scope labels.',
        f"Historically marked records: {counts['historically_marked_records']}; all are ordinary research records. Records excluded by subject: 0.", f"Distinct quote IDs in the generated language bank: {counts['language_bank_entries']}."]
out += ['', f"Evidence file: {counts['evidence_distinct_quote_ids']} distinct ids; {counts['evidence_reproduced_quote_ids']} reproduced quote fields.",
        f"Four conclusion files combined: {counts['conclusion_distinct_quote_ids']} distinct cited ids, including {counts['conclusion_new_reread_quote_ids']} from the re-reading.",
        'The recovered units were chosen because they had been excluded; they are not a sample of how common anything is. Completed assignments, partial-source limits and current unread bodies are recorded in `reread-coverage.json`.',
        '', '## Conclusion files', '', '| File | Distinct ids | New re-read ids |', '|---|---:|---:|']
out += [f"| {name} | {len(ids)} | {sum(i.startswith('glu') for i in ids)} |"
        for name, ids in conclusion_ids.items()]
if 'rereading' in counts:
    out += ['', '## Re-reading state', '']
    out += [f"- {key.replace('_', ' ')}: {value}" for key, value in counts['rereading'].items()]
for k, cc in counts.items():
    if not isinstance(cc, dict): continue
    if k in {'conclusion_files', 'rereading'}: continue
    out += ['', '## ' + k.replace('_', ' '), '', '| Value | Records |', '|---|---:|']
    out += [f'| {v} | {n} |' for v, n in cc.items()]
(ROOT / 'synthesis/counts.json').write_text(json.dumps(counts, indent=2))
(ROOT / 'synthesis/counts.md').write_text('\n'.join(out) + '\n')
pat = re.compile(r'kill myself|suicid|self.harm|hurt (?:myself|my baby)|abuse|hit me|shak(?:e|ing) (?:the|my) baby|miscarriage|stillbirth|infant death|bedshar|co.sleep|chok|allerg|reflux|tongue.tie|delay|prematur|eczema|low supply|milk supply|pain|bleed|seizure|depress|anxi|\b(?:1[0-7])\s*(?:f|m)\b', re.I)
hits = [{k:v for k,v in q.items() if k != '_file'} for q in rows if pat.search(q['quote'] + ' ' + q['context'])]
audit_arg = next((arg.split('=', 1)[1] for arg in sys.argv if arg.startswith('--audit-dir=')), 'scratchpad/database-audit')
if '_raw' in Path(audit_arg).parts:
    raise SystemExit('Audit output must be outside immutable _raw folders.')
audit = ROOT / audit_arg; audit.mkdir(exist_ok=True, parents=True)
if '--counts-only' not in sys.argv:
    (audit / 'safety-hits.jsonl').write_text(''.join(json.dumps(q, ensure_ascii=False) + '\n' for q in hits))
sample = random.Random(20261024).sample(rows, min(20,len(rows)))
if '--counts-only' not in sys.argv:
    (audit / 'spot-check.jsonl').write_text(''.join(json.dumps(q, ensure_ascii=False) + '\n' for q in sample))
(audit / 'structural-errors.json').write_text(json.dumps(errors, indent=2))
print(f"TOTAL {len(rows)} quotes; {len(errors)} structural errors; {len(hits)} safety hits in review queue; {len(sample)} spot-check records")
for e in errors: print(e)
sys.exit(bool(errors))
