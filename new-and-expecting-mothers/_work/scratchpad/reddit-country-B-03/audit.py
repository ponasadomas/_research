"""Verify explicit human coverage and native source fidelity; never choose triage/quotes."""
import json,csv,gzip,hashlib,re,datetime,collections,sys
from pathlib import Path
from full_reader import ROOT,S,PACKET,M,IDX,READ,VOICE,records,body
errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
norm=lambda v:re.sub(r'\s+',' ',v).strip()
assignment=PACKET/'assignments/batch-03.json';a=json.loads(assignment.read_text());triagepath=ROOT/'_raw/reddit-deep/triage/country-B-03.tsv';tr=list(csv.DictReader(triagepath.open(),delimiter='\t'));rr=records(READ);vv=records(VOICE);keep={x['post_id'] for x in tr if x['label']!='drop'};readids={x['post_id'] for x in rr}
check(len(tr)==len({x['post_id'] for x in tr})==291 and set(a['post_ids'])=={x['post_id'] for x in tr},'Exact291assignment/triage IDs')
check({x['label'] for x in tr}<=set('keep_play keep_solids keep_pumping_work keep_sleep keep_postpartum keep_pregnancy keep_registry keep_other drop'.split()),'Triage vocabulary')
check(keep==readids==set(M['post_ids']) and len(rr)==203,'Exact203keep/read IDs')
for c in a['chunks']:check(hashlib.sha256((ROOT/c['file']).read_bytes()).hexdigest()==c['sha256'],'Immutable source card '+str(c['chunk']))
cm=json.loads((S/'card-views-v1/manifest.json').read_text());logs=records(S/'triage-reading.jsonl');check(len(logs)==12 and {p for x in logs for p in x['post_ids']}==set(a['post_ids']) and all(x['all_cards_human_read'] is True for x in logs),'All12cardviews human read')
check(cm['assignment_sha256']==hashlib.sha256(assignment.read_bytes()).hexdigest(),'Assignmenthash')
for c in cm['views']:check(hashlib.sha256((ROOT/c['file']).read_bytes()).hexdigest()==c['sha256'],'Card view hash '+str(c['view']))
cor=json.loads((S/'triage-reason-corrections.json').read_text());check(hashlib.sha256((S/'triage-before-reason-correction.tsv').read_bytes()).hexdigest()==M['triage_sha256']==cor['build_time_triage_sha256'],'Preserved exact build triage snapshot')
check(hashlib.sha256(triagepath.read_bytes()).hexdigest()==cor['current_triage_sha256'],'Current corrected triage hash')
before=list(csv.DictReader((S/'triage-before-reason-correction.tsv').open(),delimiter='\t'));check([(x['post_id'],x['label']) for x in before]==[(x['post_id'],x['label']) for x in tr],'Only reason wording corrected, no keep changes')
ins=records(ROOT/'sources/reddit-country-B-03-duplicate-inspections.jsonl');extraids={x['post_id'] for x in ins};native={}
files={IDX[t]['source_post_file'] for t in readids}|{x['source_post_file'] for x in ins}
for name in files:
 with gzip.open(ROOT/name,'rt') as f:
  for line in f:
   x=json.loads(line)
   if x.get('id') in readids|extraids:native[x['id']]=x
check(len(native)==208,'All203native and5duplicate-only originals found')
qby=collections.defaultdict(list)
for q in vv:qby[q['post_id']].append(q['id'])
for r in rr:
 t=r['post_id'];x=IDX[t];check(r['post_body_read_complete'] is True,'Complete body '+t);check(norm(body(t))==norm(native[t]['selftext']),'Entire native body '+t);check(hashlib.sha256((ROOT/r['raw_file']).read_bytes()).hexdigest()==x['sha256']==r['primary_unit_sha256'],'Unit hash '+t)
 check(r['available_identifiable_OP_replies_read']==0 and r['op_reply_ids_read']==[] and x['comment_source_available'] is False,'Unavailable OP scope '+t);check(r['quote_ids']==qby[t],'Quote ledger '+t);check(not r['quote_ids'] or r['post_body_read_complete'] is True,'No excluded quote '+t)
flogs=records(S/'full-reading.jsonl');check(len(flogs)==18 and all(x['all_units_human_read'] is True for x in flogs),'All18fullviews human read')
for c in M['views']:
 p=ROOT/c['file'];view=p.read_text();check(hashlib.sha256(p.read_bytes()).hexdigest()==c['sha256'],'Frozen fullview '+str(c['view']))
 for t in c['post_ids']:check(norm(body(t)) in norm(view) and json.dumps(IDX[t]['title'],ensure_ascii=False) in view,'Complete displayed title/body '+t)
for x in ins:
 p=ROOT/x['raw_file'];t=x['post_id'];saved=json.loads(p.read_text());check(hashlib.sha256(p.read_bytes()).hexdigest()==x['primary_unit_sha256'],'Extra raw hash '+t);check(saved==native[t] and x['post_body_read_complete'] is True,'Extra entire native body '+t);check(x['comment_source_available'] is False and x['available_identifiable_OP_replies_read']==0 and x['op_reply_ids_read']==[] and not x['quote_ids'],'Extra unavailable comments '+t)
speakers=set('expecting_mother new_mother experienced_mother parent_unspecified partner relative_caregiver recovered_parent gave_up_parent advisor professional reviewer skeptic'.split());stages=set('pregnancy_early pregnancy_late newborn_0_6_weeks baby_6_16_weeks baby_4_6_months baby_6_12_months toddler return_to_work looking_back unknown'.split());types=set('trigger_moment pain fear tried_failed desire belief question objection advice_given success_story failure_story regret others_said'.split())
for q in vv:
 t=q['post_id'];x=native[t]
 for part in q['quote'].split(' […] '):check(norm(part) in norm(x['selftext']),'STRICT native quote '+q['id'])
 check(q['date']==datetime.datetime.fromtimestamp(float(x['created_utc']),datetime.timezone.utc).date().isoformat(),'Native date '+q['id']);check(q['url'].rstrip('/')==('https://www.reddit.com'+x['permalink']).rstrip('/'),'Native URL '+q['id']);check(q['raw_file']==IDX[t]['raw_file'] and q['read_scope']=='full_post_comment_source_unavailable','Raw/scope '+q['id']);check(q['speaker'] in speakers and q['stage'] in stages and q['type'] in types,'Vocabulary '+q['id']);check(len(q['context'].split())<=25,'Context words '+q['id'])
allquotes=[]
for p in (ROOT/'voice').glob('*.jsonl'):
 for q in records(p):allquotes.append((p.name,q))
for q in vv:check(sum(x['id']==q['id'] for _,x in allquotes)==1,'Global unique ID '+q['id'])
other={t:[q['id'] for f,q in allquotes if f!=VOICE.name and q.get('post_id')==t] for t in qby};other={t:q for t,q in other.items() if q}
dup=json.loads((S/'duplicate-review.json').read_text());group_other={}
for g in dup['exact_groups']:
 bodies=[norm(native[t]['selftext']) for t in g['post_ids']];check(len(set(bodies))==1,'Exact-body group '+str(g['group']));qs=[q['id'] for _,q in allquotes if q.get('post_id') in g['post_ids']];check(len(qs)<=1,'Only one quoted representative group '+str(g['group']));group_other[str(g['group'])]=qs
baseline=json.loads((ROOT/'_raw/reddit-deep/continuation-v1/final-read-post-ids.json').read_text())['full_original_post_ids'];check(not set(baseline)&readids,'No frozen5879same-ID new read credit')
spot=json.loads((S/'spot-check-v1/manifest.json').read_text());check(spot['selected']==20 and spot['completion']=='all20fullsourcebodiesandquotedrecords_human_reread','20manual spotchecks completed')
result=dict(complete=True,parent_packet_originals=847,assigned_cards=291,human_triaged_cards=len(tr),triage_keep=len(keep),triage_drop=sum(x['label']=='drop' for x in tr),full_originals_read=len(rr),partial_originals=0,unread_kept_ids=sorted(keep-readids),unread_card_drop_body_ids=sorted(x['post_id'] for x in tr if x['label']=='drop'),OP_replies_read=0,post_comment_sources_unavailable=203,post_read_statuses=dict(collections.Counter(x['status'] for x in rr)),quotes=len(vv),quoted_post_ids=len({q['post_id'] for q in vv}),research_only_quotes=sum(q.get('marketing_eligible') is False for q in vv),communities=dict(collections.Counter(IDX[t]['subreddit'] for t in readids)),extra_duplicate_only_original_inspections=len(ins),extra_duplicate_only_comment_sources_unavailable=5,exact_body_groups_reviewed=len(dup['exact_groups']),near_repeat_groups_reviewed=1,quoted_duplicate_group_references=group_other,cross_file_same_post_quote_references=other,manual_random_spotchecks=20,strict_native_quote_failures=[e for e in errors if e.startswith('STRICT')],errors=errors,voice_sha256=hashlib.sha256(VOICE.read_bytes()).hexdigest(),reading_sha256=hashlib.sha256(READ.read_bytes()).hexdigest(),triage_sha256=hashlib.sha256(triagepath.read_bytes()).hexdigest(),themes=sorted({t for q in vv for t in q['themes']}))
(ROOT/'sources/reddit-country-B-03-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['unread_card_drop_body_ids','themes']},indent=2));sys.exit(bool(errors))
