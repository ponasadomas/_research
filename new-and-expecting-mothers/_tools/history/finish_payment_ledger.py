"""Research retains every subject; copy decisions belong to the owner.
Unquoted units remain pending human topic/duplicate review, rather than being
excluded for clinical, emotional or reproductive subject matter.
"""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
D=R/'_raw/reddit-deep/information-payment-v1'
ix=[json.loads(l) for l in (D/'index.jsonl').read_text().splitlines()]
qs=[json.loads(l) for l in (R/'voice/reddit-payment-01.jsonl').read_text().splitlines()]
quoted_here={q['post_id'] for q in qs}
# Cross-reader context review: fatigue alone did not establish an acute crisis.
# The bounded purchase/implementation excerpt is retained in the focused cohort.
quoted_elsewhere={'1m7uosu'}
kept=quoted_here|quoted_elsewhere
reasons={
'1mnob2r':'Emergency formula-fund solicitation.',
'1ocsgre':'Monitor-security concern; no planning-report job.',
'1p6mz2j':'Severe sleep-related distress; retain as attributed evidence.',
'1p9ujvu':'Proposed photo-app market-research pitch.',
'1lwbm2y':'Broad career direction, no infant planning artifact.',
'1lyj703':'Older-child and eldercare phone boundaries.',
'1mib7zp':'Seller tester-recruitment promotion.',
'1mxsz3z':'General corporate-expense reimbursement.',
'1mzlxvl':'Older-toddler schooling and career choice.',
'1o1owwn':'Employment-charge dispute requiring policy interpretation.',
'1p0jwzy':'Older-child school-hours career choice.',
'1pyjn37':'Personal pregnancy-continuation decision; retain as attributed evidence.',
'1m54wgk':'Serious pregnancy complication; retain as attributed evidence.',
'1p62zpr':'Supplement dosing device request.',
'1m3ggbo':'Severe pregnancy/work physical distress; retain as attributed evidence.',
'1luj5pl':'Feeding-injury treatment advice.',
'1oy22jm':'Mental-health vulnerability centered; retain as attributed evidence.',
'1pi3suw':'Severe sleep-related distress; retain as attributed evidence.',
'1pwsqea':'Older-child career discussion.',
'1luvib8':'Bereavement-centered family conflict.',
'1ot2aoj':'Severe sleep-related distress; retain as attributed evidence.',
'1m1othf':'Travel comfort expenditure, no information-purchase signal.'}
assert {x['id'] for x in ix}==kept|set(reasons)
rows=[{**x,'status':'fully_read','OP_replies_fully_read':x['OP_replies'],'disposition':'keep_quoted_elsewhere' if x['id'] in quoted_elsewhere else ('keep' if x['id'] in kept else 'read_pending_topic_review'),'reason':'Retained after cross-reader boundary review; ordinary fatigue and paid-plan implementation testimony, quoted in focused cohort without instructions.' if x['id'] in quoted_elsewhere else ('Ordinary constraints/tool decision or countervoice.' if x['id'] in kept else reasons[x['id']])} for x in ix]
(D/'reading-ledger.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in rows))
print(len(rows),'originals fully read;',sum(x['OP_replies'] for x in rows),'OP replies;',len(kept),'retained;',len(reasons),'pending topic review;',len(qs),'quotes')
