#!/usr/bin/env python3
"""Materialize root's completed human readings and manually selected evidence; no classifier."""
from pathlib import Path
import json,hashlib,csv,re,collections,gzip
R=Path(__file__).resolve().parents[1]
notes={
'1md0k6z':('promotional_resource','Labor experience introduces PDF by direct message; no purchase, price, individualization or independent affiliation established. Clinical claims remain attributed evidence.'),
'1n0ltxj':('gear_decision_payment_unknown','First-time parent compares stroller compatibility, one-hand use, infant-to-toddler seat and physical size. Consumer Reports referenced, no subscription purchase stated.'),
'1nblwu7':('paid_course','Fear of birth leads to self-reported course purchase; videos and printouts, self-paced learning praised, effort/network limitations noted. No price or customized report.'),
'1nxmb0i':('paid_clinical_service_bundle','Reports $200 per physiotherapy session and generic PDF breathing handout, inadequate instruction and progress. Dollar currency unspecified, clinical care only; not report-only payment.'),
'1mjz79m':('seller_hypothetical','Student seeks hypothetical demand for a 35-page first-aid/checklist PDF. No parent transaction, price or personalization. Clinical instructions not reproduced.'),
'1n54u11':('unconfirmed_pdf_purchase','Objects to successive sleep/pumping/bottle PDFs, shares logins. Hundreds-of-dollars estimate explicitly guessed; no named purchased deliverable, personalization or actual price.'),
'1nu9wzp':('paid_sleep_resources_unspecified','Self-reports buying many sleep resources after poor sleep and later distrusts programs. No specific PDF transaction, price or individualization. Claimed sleep causality unverified.'),
'1o1ieko':('promotional_app_payment_unknown','Long parenting narrative endorses personalized general-learning app; no payment. Near-identical cross-community text is dependent promotional-looking material, affiliation unverified.'),
'1p3nte6':('paid_app_feature','Explicit Huckleberry SweetSpot purchase at two months, followed by tracking stress. No price, paid expert analysis or report stated.'),
'1pei9n5':('free_resource_request','Seeks free recovery workout PDF/YouTube after seeing $200 programs/memberships. No purchase, current recovery is a clinical boundary.'),
'1o3uj2j':('dependent_promotional_app','Near-identical 1o1ieko narrative and learning-app endorsement; no payment. Separate native post, not independent corroborating buyer.'),
'1o70lus':('gear_decision_payment_unknown','Due date approaching; asks community to resolve safety/ease/aesthetics and mixed-brand system choices. Hardware spending intent, no paid report.'),
'1nsrvoc':('resume_document_not_parent_report','PDF is own resume sent to connections. Recommends a resume proofer but no explicit payment for proofreading and no new-parent custom report.'),
'1pi3suw':('paid_consultation','Single parent reports paying sleep consultant, little improvement despite attempted timing advice. No price, written plan or refund. Clinical/health-visitor context retained.'),
'1m1fp76':('paid_app_feature','Annual Plus membership paid; alleged lost records and entitlement. No amount, report or subsequent resolution.'),
'1mbdqhf':('paid_app_feature','Subscribed after recommendations for Huckleberry/Nanit; surprised by recurring charges. No amounts or report deliverable.'),
'1mcom5n':('paid_course','Newborn sleep difficulty triggered Taking Cara Babies program purchase. Later regrets environmental rigidity with daycare naps. No price or customization, causality unverified.'),
'1mr0vor':('paid_app_subscription','Year subscription called a panic purchase on hospital return. Meticulous tracking later questioned. Tier, price and custom-report delivery absent.'),
'1mrt9i2':('paid_app_book_clinical_context','Self-reports sleep-guide and paid-app use amid active infant treatment and severe postpartum mental-health context. No personalized report. Research boundary only.'),
'1nb7wfo':('prepurchase_question','Asks whether newborn course worth buying after pediatrician recommended free content. No transaction by author.'),
'1ow7gp3':('payment_unknown_app_question','Questions paid AI prediction value and log complexity. No author purchase.'),
'1m7uosu':('paid_app_bundled_expert_plan','Explicit Huckleberry Premium purchase for expert analysis, gradual plan delivered. First-night implementation prolonged settling, partner opposed crying; price, PDF and later outcome absent. Existing rjfc01-0090, not a new buyer.'),
'1nid2y8':('paid_app_feature','Paid Huckleberry user seeks alternative after worse perceived sleep with SweetSpot. No price, expert report or proven causality.'),
'1okasr2':('paid_app_clinical_boundary','Premium paid after second birth; describes severe distress, compulsive tracking and later deleting app. No custom written plan. Retain the complete account as attributed evidence.'),
'1pot5mn':('physical_purchase_not_app','Purchase is pre-baby gaming headset, not Huckleberry. Seeks noise reduction while holding distressed infant. No report purchase.'),
'1pwhvcq':('paid_app_feature','Just purchased Huckleberry for five-month-old nap timing; intends to try suggestions. Price/tier/written report and later outcome absent.')}
rootquotes=[]
selections=[('1n0ltxj','compatible with Nuna Pipa, has a one hand fold, includes a seat for newborn through toddler','Parent needs compatible physical gear and manageable size; references rankings, no paid report or ranking subscription stated.','registry_gear'),('1o70lus','My head is swimming and I just want my trusted reddit community to tell me what to do.','Expecting parent asks community to resolve travel-system decisions; spending intent concerns hardware, not paid information.','registry_gear'),('1pwhvcq','We just purchased huckleberry and it recommended some different nap times that we’ll be trying.','Parent reports app purchase and planned schedule changes. Tier, price, written report and later satisfaction are unknown.','sleep_routines')]
indices={}
for name in ['report-purchases-v2','sleep-purchases-v3']:
 for l in (R/f'_raw/reddit-deep/{name}/primary-index.jsonl').read_text().splitlines():
  x=json.loads(l);indices.setdefault(x['post_id'],x)
for pid,quote,context,theme in selections:
 x=indices[pid];assert quote in (R/x['raw_file']).read_text();assert len(context.split())<=25
 rootquotes.append({'id':f'rba01-{len(rootquotes)+1:04}','source':f'Reddit — r/{x["subreddit"]} (publisher archive)','url':x['url'],'date':x['post_date'],'speaker':'parent_unspecified','stage':'unknown','type':'question','themes':[theme,'personalization','decision_fatigue'],'quote':quote,'context':context,'raw_file':x['raw_file'],'source_class':'reddit_archive','evidence_kind':'archived_original','archive_dataset':'yikeee/reddit-subreddits25','archive_commit':'ea497c510aa68765c07ed744ec9f84d68bbedf7f','post_id':pid,'read_scope':'full_post_comment_source_unavailable','paid_report_demand_proven':False})
(R/'voice/reddit-report-purchases-v2.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rootquotes))
ledger=[]
for name in ['report-purchases-v2','sleep-purchases-v3']:
 tri=list(csv.DictReader((R/f'_raw/reddit-deep/triage/{name}.tsv').open(),delimiter='\t'))
 for t in tri:
  if t['decision']!='keep':continue
  pid=t['post_id'];x=next(json.loads(l) for l in (R/f'_raw/reddit-deep/{name}/primary-index.jsonl').read_text().splitlines() if json.loads(l)['post_id']==pid)
  assert pid in notes
  ledger.append({'post_id':pid,'cohort':name,'raw_file':x['raw_file'],'post_body_read_complete':True,'available_identifiable_OP_replies_read':x['OP_replies'],'op_reply_ids_read':x['OP_comment_ids'],'primary_unit_sha256':x['sha256'],'status':'eligible','reason':notes[pid][1],'purchase_class':notes[pid][0],'actual_standalone_custom_report_purchase':False,'prior_full_read':x['prior_full_read'],'quote_ids':[q['id'] for q in rootquotes if q['post_id']==pid]})
(R/'sources/reddit-report-purchases-v2-reading.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in ledger))
verification={'cards_read':136,'retained_read_occurrences':len(ledger),'retained_distinct_post_ids':len({x['post_id'] for x in ledger}),'unique_new_post_ids_vs_5879_baseline':len({x['post_id'] for x in ledger if not x['prior_full_read']}),'OP_comment_ids_read':sorted({i for x in ledger for i in x['op_reply_ids_read']}),'partial_keeps':0,'new_standalone_report_purchases_established':0,'native_audit_failures':[]}
native={}
for p in (R/'_raw/reddit-deep/windows/2025-h2-v1').glob('*_submissions.jsonl.gz'):
 with gzip.open(p,'rt') as f:
  for l in f:
   q=json.loads(l)
   if q['id'] in notes:native[q['id']]=q
for x in ledger:
 p=R/x['raw_file'];n=native[x['post_id']];txt=p.read_text();
 assert hashlib.sha256(p.read_bytes()).hexdigest()==x['primary_unit_sha256'];assert n['title'] in txt and n['selftext'] in txt
for q in rootquotes:assert q['quote'] in native[q['post_id']]['selftext'];assert q['url']=='https://www.reddit.com'+native[q['post_id']]['permalink']
(R/'sources/reddit-report-purchases-v2-verification.json').write_text(json.dumps(verification,indent=2)+'\n');print(verification)
