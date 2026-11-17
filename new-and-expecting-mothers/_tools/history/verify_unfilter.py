#!/usr/bin/env python3
"""Check the complete bank, restored evidence, untouched history and revised files.

Run python3 -I _tools/verify_unfilter.py. This reads stored records and metadata;
it does not re-read queued raw units or overwrite historical verification logs.
"""
from pathlib import Path
import ast, collections, csv, hashlib, json, re, subprocess, sys

R = Path(__file__).resolve().parents[1]
REPO = R.parents[2]
D = R / 'scratchpad/unfilter-reread'
baseline = json.loads((D / 'baseline-manifest.json').read_text())
errors = []
def check(value, message):
    if not value: errors.append(message)
def jl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
voice = [q for p in sorted((R / 'voice').glob('*.jsonl')) for q in jl(p)]
byid = {q['id']: q for q in voice}
flagged = {q['id'] for q in voice if q.get('marketing_eligible') is False}
recovery = json.loads((R / 'synthesis/reread-coverage.json').read_text())
new_ids = {q['id'] for q in voice if q['id'].startswith('glu')}
check(len(voice) == len(byid) == recovery['total_quote_records'], 'Voice count/duplicate mismatch')
check(len(new_ids) == recovery['new_quote_records'], 'Recovery quote count mismatch')
check(len(flagged) == 141, 'Historical marked count mismatch')
catalogue = jl(R / 'synthesis/quote-catalogue.jsonl')
check(len(catalogue) == len({q['id'] for q in catalogue}) == len(voice), 'Catalogue count/duplicate mismatch')
check({q['id'] for q in catalogue} == set(byid), 'Catalogue missing ids')
for q in catalogue:
    check(q == {k: v for k, v in byid[q['id']].items() if k not in {'marketing_eligible', 'evidence_use'}}, 'Catalogue record mismatch ' + q['id'])
bank = (R / 'synthesis/quote-index.md').read_text()
bank_ids = re.findall(r'^\[([a-z][a-z0-9]*-\d+)\]$', bank, re.M)
check(len(bank_ids) == len(set(bank_ids)) == len(voice) and set(bank_ids) == set(byid), 'Bank missing/duplicate ids')
restored = list(csv.DictReader((D / 'restored-records.tsv').open(), delimiter='\t'))
check(len(restored) == len({q['id'] for q in restored}) == 141, 'Restoration manifest duplicate/count mismatch')
check({q['id'] for q in restored} == flagged, 'Restoration manifest id mismatch')
evidence = (R / 'synthesis/evidence.md').read_text()
evidence_ids = re.findall(r'^\[([a-z][a-z0-9]*-\d+)\]$', evidence, re.M)
check(len(evidence_ids) == len(set(evidence_ids)) and set(evidence_ids) == flagged | new_ids,
      'Thematic evidence missing/duplicate restored or recovered ids')
normal = subprocess.run([sys.executable, '-I', str(R / '_tools/query.py'), '--id', *sorted(flagged), '--max', '200'], capture_output=True, text=True, check=True).stdout
compat = subprocess.run([sys.executable, '-I', str(R / '_tools/query.py'), '--exclude-restricted', '--id', *sorted(flagged), '--max', '200'], capture_output=True, text=True, check=True).stdout
check(normal == compat and normal.startswith('# 141 match\n'), 'Deprecated query switch hides records')
check('RESEARCH BOUNDARY ONLY:' not in normal, 'Query still applies a restriction label')

changed = []; preserved = collections.Counter(); markdown = []; syntax = 0
for root in [R, R.parent / 'main']:
    for p in sorted(root.rglob('*')):
        if not p.is_file() or '_raw' in p.parts: continue
        relative = str(p.relative_to(REPO)); digest = hashlib.sha256(p.read_bytes()).hexdigest()
        if relative in baseline and digest == baseline[relative]:
            if '/voice/' in relative: preserved['voice_files'] += 1
            if '/sources/' in relative: preserved['source_files'] += 1
            if p.name.startswith('reader-notes') or p.name.endswith('session-report.md') or p.name == 'STATE-deep-pass.md': preserved['reader_notes_and_run_logs'] += 1
            continue
        changed.append(relative)
        if p.suffix == '.md': markdown.append(p)
        if p.suffix == '.py':
            try: ast.parse(p.read_text(), filename=str(p)); syntax += 1
            except SyntaxError as e: errors.append(str(e))
for relative, want in baseline.items():
    p = REPO / relative
    check(p.is_file(), 'Baseline file deleted: ' + relative)
    if '/voice/' in relative or '/sources/' in relative or p.name.startswith('reader-notes') or p.name.endswith('session-report.md') or p.name in {'STATE-deep-pass.md', 'semantic20_audit.py'}:
        check(hashlib.sha256(p.read_bytes()).hexdigest() == want, 'Historical record changed: ' + relative)
# The existing verifier now checks the requested id-before-blockquote layout too.
proc = subprocess.run([sys.executable, '-I', str(R / '_tools/verify_findings.py'), *map(str, markdown)], capture_output=True, text=True)
check(proc.returncode == 0, 'Revised Markdown check failed: ' + proc.stdout)
queue = list(csv.DictReader((D / 'queue.tsv').open(), delimiter='\t'))
check(len(queue) == len({q['unit_id'] for q in queue}), 'Duplicate queued unit ids')
for q in queue:
    check(bool(q['reason']) and bool(q['stage']), 'Unexplained queue item: ' + q['unit_id'])
    check((R / q['raw_file']).is_file() and '_raw' in Path(q['raw_file']).parts, 'Missing/raw-invalid queue path: ' + q['unit_id'])
tails = jl(R / '_raw/oblique-deep/final-safety-unread-tails.jsonl')
check({q['unit_id'] for q in queue if 'reading_partial' in q['stage']} ==
      {'mse-' + str(q['thread_id']) for q in tails}, 'Partial MSE queue mismatch')
tail_posts = sum(q['posts_total'] - q['posts_read'] for q in tails)
check(len(tails) == 15 and tail_posts == 231, 'MSE partial/tail count mismatch')
# Check legacy inline fragments with exact punctuation as well as new blocks.
inline_pairs = 0
for p in markdown:
    for quote, rid in re.findall(r'["“]([^"”\n]{12,}?)["”][ \t]*`?\[([a-z][a-z0-9]*-\d+)\]`?', p.read_text()):
        inline_pairs += 1
        check(rid in byid and ' '.join(quote.split()) in ' '.join(byid[rid]['quote'].split()),
              'Exact inline fragment mismatch: ' + str(p.relative_to(REPO)) + ': ' + rid)
result = dict(records=len(voice), catalogue_records=len(catalogue), bank_ids=len(bank_ids), restored=141,
              themed_restored_quotes=len(set(evidence_ids) & flagged), themed_recovered_quotes=len(new_ids),
              themed_total_quotes=len(evidence_ids), query_compatibility='141 of 141; no exclusions',
              revised_markdown_check=proc.stdout.strip(), changed_python_syntax_checked=syntax,
              exact_inline_fragments=inline_pairs, historical_partial_MSE_units=len(tails),
              historical_MSE_tail_posts=tail_posts, unread_MSE_tail_posts=recovery['previous_MSE_tail_posts_remaining'],
              preserved=dict(preserved), queue_units=len(queue),
              queue_stage_combinations=dict(collections.Counter(q['stage'] for q in queue)),
              changed_files=changed, errors=errors, failed=len(errors))
out = D / 'checks-merge'; out.mkdir(exist_ok=True)
(out / 'unfilter-verification.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'changed_files'}, indent=2))
sys.exit(bool(errors))
