"""Save explicit human semantic decisions after reading every frozen sample/context."""
from pathlib import Path
import collections
import hashlib
import json

R = Path(__file__).resolve().parents[2]
P = R / '_raw/audit/continuation-2026-10-24/independent-semantic20'
sample = json.loads((P / 'sample.json').read_text())
manifest = json.loads((P / 'manifest.json').read_text())

# Every note below was written after inspecting the full quote metadata and full
# source view, including all eight available OP replies across the sample.
decisions = [
    ('rad02-0081', 'pass', 'Seven-month-old and three daycare days are explicit. Seeks affordable activities, sign language and recommendations; limited conditional willingness, no curriculum or report transaction. No clinical or crisis content in selected use.', None),
    ('rad02-0032', 'pass', 'Thirty weeks pregnant establishes late pregnancy. Director role, absent employer policy and proposed remote or part-time return are explicit; family help is planned. Workplace precedent and legal entitlement remain separate, with no purchased plan.', None),
    ('rad03-0171', 'pass', 'First-time parents of a five-week-old, UK location and long leave are explicit. Contentment without tracking is personal and work-context dependent; no universal sleep claim or purchase. Conservative speaker label is appropriate.', None),
    ('rad03-0022', 'pass', 'At thirty-six weeks with a second child, repeated provider and receptionist contact has not supplied a date. Childcare and leave coordination depend on an external decision. Research-only restriction appropriately avoids a procedure recommendation.', None),
    ('rad04-0018', 'pass', 'Three-month-old, existing rhythm, desired morning outings and downloaded unnamed guide are explicit. The source does not say it was bought. Logistical excerpt preserves dissatisfaction with fit; feeding timing and sleep totals are not clinical recommendations.', None),
    ('rad04-0014', 'pass', 'Twelve weeks is explicit. The author objects to course sales pitches and describes conflicting advice and failed implementation. No course bought, remedy established or acute harm disclosed; quoted wording is the author own complaint.', None),
    ('rad05-0005', 'pass', 'Parent already has the hybrid carrier-bag, has called the airline twice and faces allowance uncertainty. Teenage son is incidental to bag capacity, not the central safety topic or author. No current airline rule, accepted price or report purchase inferred.', None),
    ('rad05-0026', 'pass', 'Two-month-old is current age; upcoming program and future childcare timing explain the title. Enrollment aims at employee tuition and student childcare benefits, but evening attendance was unexpected. No general institutional policy or report transaction is established.', None),
    ('rbc01-0025', 'pass', 'Baby turns five months this week; successful prior postpartum freezer preparation is explicit. All four OP replies read, including SLP involvement, salt uncertainty and desire for variety despite repeated adult meals. Selected quote remains practical preparation, not clinical feeding advice or app purchase.', None),
    ('rbc01-0024', 'pass', 'Fourteen months is explicit and toddler label is appropriate. Parent plans new recipes and asks a fallback question; not a demonstrated rejection event or behavioral-treatment finding. Available comment source contains no identifiable OP reply. No purchase.', None),
    ('rad03-0094', 'pass', 'Baby just turned six months, so six-month boundary of stage label is supported. Initial meal and desire for a repeatable loose plan are explicit, alongside a downloaded app lacking expected guidance. No payment stated and quoted desire does not validate food safety or nutritional prescriptions.', None),
    ('rad02-0048', 'pass', 'Author explicitly bought an earlier pump, stopped early under setup constraints and now cannot inspect the covered model. Current 300-dollar alternative is considered and resisted, not purchased. Unknown stage is conservative because due month alone does not establish gestational stage. Clinical supply efficacy not inferred.', None),
    ('rad03-0014', 'pass', 'Second-time mom self-identification supports experienced_mother; exact gestational stage is absent. Doula and clinician-readable contingency document are explicit. Research-only restriction correctly separates usability from personalized treatment or guaranteed emergency preferences.', None),
    ('rad02-0070', 'pass', 'Almost three months supports stage. Stopped wake-window schedule, less fuss and easier settling are explicit personal reports; initial attempts and anxiety remain visible in full context. No causal proof, clinical recommendation, payment or independent buyer count.', None),
    ('rad05-0009', 'pass', 'Five-month-old and explicit paid Huckleberry version support use and dissatisfaction. Source also says prior Snoo helped a different child and existing Nara tracking was incomplete. Research-only and causality limitations preserve this mixed context; no app-caused worsening or report transaction proven.', None),
    ('rad03-0081', 'pass', 'Almost eight months, Ontario, ordinary grocery access, existing app and adults repeated meals are explicit. Original asks about fish, but selected excerpt is the ordinary menu-planning constraint; no allergen, mercury or feeding-safety instruction extracted. App payment unknown.', None),
    ('rad05-0035', 'pass', 'Original describes a reported 210-dollar registration payment and rejected app submissions. All four OP replies read: care already started, receipt date still requested and balance issue remains unresolved. Context accurately keeps administrative friction separate from tax eligibility or report buying.', None),
    ('rad05-0028', 'needs_context_correction', 'Ten months and regular varied non-puree meals are explicit; hotel trip, pouches and concern about restaurant salt drive the logistical question. The source does not establish overall clinical health, so Healthy is unsupported. Payment and nutritional prescription are not established.', 'Replace context with: Parent of a ten-month-old who eats varied solids needs hotel-trip meal access. Sodium limits and nutrition prescriptions are outside selected use.'),
    ('rad03-0155', 'pass', 'Current infant age is ten weeks; 4.5 months is the future handoff deadline. Grandmother already watches a two-year-old and contact naps would strain capacity. Context preserves this timing and constraint, with no purchase, clinical sleep advice or safety crisis inferred.', None),
    ('rad02-0060', 'pass', 'Author self-identifies mother and current single parent; stopped pumping around seven months and now looks back at eleven-and-a-half months. Formula brought relief while old routines now evoke affection. Excerpt and context preserve mixed feelings without relapse, restart intent or paid-demand inference.', None),
]
assert [x[0] for x in decisions] == sample['quote_ids'] == manifest['quote_ids']
records = {q['id']: q for q in sample['source_quote_records']}
scope = {}
hashes = []
for view in manifest['chunks']:
    path = R / view['path']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == view['sha256']
    hashes.append((view['path'], view['sha256']))
    for source in view['sources']:
        raw = R / source['raw_file']
        assert hashlib.sha256(raw.read_bytes()).hexdigest() == source['raw_sha256']
        text = raw.read_text()
        replies = text.count('\n--- OP REPLY ---\n')
        for qid in source['quote_ids']:
            assert records[qid]['raw_file'] == source['raw_file']
            scope[qid] = {'complete_original_title_and_selftext': True,
                          'all_available_identifiable_OP_replies': True,
                          'available_identifiable_OP_replies_read': replies,
                          'comment_source_available': records[qid]['read_scope'] == 'full_post_and_available_identifiable_OP_replies',
                          'raw_file': source['raw_file'], 'raw_sha256': source['raw_sha256'],
                          'view': view['path'], 'view_sha256': view['sha256']}
results = []
correction_log_path = P.parent / 'parent-metadata-corrections-05.json'
correction_log = json.loads(correction_log_path.read_text())
correction = next(x for x in correction_log if x['id'] == 'rad05-0028')
current05 = {q['id']: q for q in map(json.loads, (R / 'voice/reddit-augdec-05.jsonl').read_text().splitlines())}
assert current05['rad05-0028']['context'] == correction['after']
for qid, decision, note, correction in decisions:
    results.append({'id': qid, 'decision': decision, 'source_scope_read': scope[qid],
                    'literal_supported': True, 'speaker_supported': True, 'stage_supported': True,
                    'context_supported': decision == 'pass',
                    'claimant_and_purchases_preserved': True, 'safety_restrictions_supported': True,
                    'evidence_limits': note, 'proposed_correction': correction,
                    'duplicate_or_repeat_author_limit': 'No duplicate independent-buyer claim is made. This finite sample alone cannot establish unique authors across the corpus.',
                    'new_auxiliary_comment_ids_read': [], 'voice_changed': False})
    if qid == 'rad05-0028':
        results[-1]['correction_status'] = 'applied_by_root_and_current_context_checked'
        results[-1]['correction_log'] = str(correction_log_path.relative_to(R))
(P / 'results.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in results))
rows = '\n'.join(f'| `{s["raw_file"]}` | `{s["raw_sha256"]}` |' for c in manifest['chunks'] for s in c['sources'])
summary = f'''# Independent semantic/context audit of twenty frozen records

Auditor: reader 01, after completing and freezing own 01 outputs. Fixed seed `{sample['seed']}`; two random records per frozen other-reader file 02/03/04/05/B, plus ten random remaining records. Own 01 and unfinished 06/07 excluded. Every full sampled quote/context/metadata record and both intact full source views were manually read, including all eight available identifiable OP replies. This is a finite stratified sample, not the whole continuation or a population estimate.

Results against the frozen sample: **20 checked; 19 supported as written; 1 minor context correction identified; 0 literal, speaker, stage, transaction-attribution or new safety failures; 0 auditor voice edits.** Root has applied the one correction, leaving **0 unresolved findings**. Per-ID decisions and qualifications are in `results.jsonl`.

`rad05-0028`: the source establishes a ten-month-old eating varied solids well, but does not establish general clinical health. Remove the unsupported word “Healthy”. Proposed replacement: “Parent of a ten-month-old who eats varied solids needs hotel-trip meal access. Sodium limits and nutrition prescriptions are outside selected use.” The quote, age and practical meal-access selection remain supported. This is a wording correction, not evidence that the child is unwell.

Root's applied correction is recorded in [parent-metadata-corrections-05.json](../parent-metadata-corrections-05.json). The current reader-05 context was checked against that log and contains no general-health assertion. Frozen sample/context files remain unchanged, preserving the wording that triggered the finding.

The other records preserve conditional affordability versus buying, prior gear purchase versus current consideration, free/nontracking successes, mixed paid-app experiences, provider and benefit dependencies, infant current age versus future handoff age, and qualified-care boundaries. Three sample records already carry research-only restrictions, which are appropriate. No sampled post centers an acute crisis, abuse, loss/death or minor author; the incidental teenage traveler in `rad05-0005` does not turn its airline allowance question into minor-centered material. No independent-buyer total or corpus-wide duplicate clearance was inferred.

No exact parent comment needed additional inspection for the selected claims. Newly read auxiliary comments: **0**. The eight supplied OP replies are context reinspection only and must not be added again to aggregate source coverage. Native byte/date/URL audits are root's separate check; the hashes here fix what was inspected. Rights, author authenticity, self-report truth, live completeness, clinical efficacy and policy currency remain unverified. No sources fetched, outgoing messages or extraction appenders rerun.

Frozen sample SHA-256: `{hashlib.sha256((P / 'sample.json').read_bytes()).hexdigest()}`.
Frozen context manifest SHA-256: `{hashlib.sha256((P / 'manifest.json').read_bytes()).hexdigest()}`.

| Full view | SHA-256 |
| --- | --- |
''' + '\n'.join(f'| `{path}` | `{digest}` |' for path, digest in hashes) + '''

| Inspected individual source | SHA-256 |
| --- | --- |
''' + rows + '\n'
(P / 'summary.md').write_text(summary)
print(json.dumps({'records': len(results), 'decisions': dict(collections.Counter(x['decision'] for x in results)),
                  'OP_replies_reinspected': sum(x['source_scope_read']['available_identifiable_OP_replies_read'] for x in results),
                  'new_auxiliary_comments': 0, 'voice_edits': 0}))
