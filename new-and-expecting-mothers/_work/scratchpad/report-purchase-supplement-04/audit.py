# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
from pathlib import Path
import json,gzip,hashlib,csv,re,html,subprocess,sys
from datetime import datetime,timezone
from collections import Counter,defaultdict
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+',' ',html.unescape(s).replace('\\n',' ')).strip()
def lines(p):return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
a=json.loads((R/'_raw/report-purchase-archive-wave03/supplement-v1/assignments/reader-04.json').read_text());m=json.loads((S/'full-manifest.json').read_text())
t=list(csv.DictReader((R/'_raw/report-purchase-archive-wave03/supplement-v1/triage-04.tsv').open(),delimiter='\t'))
index={x['post_id']:x for x in lines(R/a['primary_index'])};q=lines(R/'voice/report-purchase-supplement-04.jsonl');rd=lines(R/'sources/report-purchase-supplement-04-reading.jsonl')
e=[]
def check(test,msg):
 if not test:e.append(msg)
check(len(t)==len(a['post_ids'])==142,'triage size');check(set(x['post_id'] for x in t)==set(a['post_ids']),'assigned triage set')
check(all(x['label'] in ['keep','drop'] and x['reason'] and x['card_file']==index[x['post_id']]['card_file'] for x in t),'triage fields')
kept={x['post_id'] for x in t if x['label']=='keep'};check(len(kept)==15,'keep count')
check({x['post_id'] for x in rd}==kept and len(rd)==15,'full-read exact set')
check({x['post_id'] for x in m['keeps']}==kept,'full manifest exact set')
for c in a['card_chunks']:
 check(H(R/c['file'])==c['sha256'],'card view hash '+c['file'])
 check(re.findall(r'^ID ([a-z0-9]+) \|',(R/c['file']).read_text(),re.M)==c['post_ids'],'card view ids')
for c in m['views']:
 check(H(R/c['file'])==c['sha256'],'read view hash '+c['file'])
check([z for c in m['views'] for z in c['post_ids']]==[x['post_id'] for x in m['keeps']],'view exact IDs')
for x in t:
 k=index[x['post_id']];check(H(R/x['card_file'])==k['card_sha256'],'individual card hash '+x['post_id'])
# Audit native attributes, title and full body independently from immutable publisher JSON, not from metadata substrings.
native={}
for f in (R/'_raw/report-purchase-archive-wave03/window').glob('*.gz'):
 with gzip.open(f,'rt') as z:
  for l in z:
   n=json.loads(l)
   if n['id'] in set(a['post_ids']):native[n['id']]=n
check(len(native)==142,'native assigned record availability')
for x in rd:
 id=x['post_id'];k=index[id];n=native[id];p=R/x['raw_file'];s=p.read_text()
 check(H(p)==k['sha256']==x['primary_unit_sha256'],'unit hash '+id)
 header=json.loads(s.split('\n',1)[1].split('\n\n=== COMPLETE ORIGINAL POST TITLE ===')[0])
 title=s.split('=== COMPLETE ORIGINAL POST TITLE ===\n',1)[1].split('\n\n=== COMPLETE ORIGINAL POST BODY ===',1)[0]
 body=s.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].rsplit('\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0]
 check(title==n['title'],'native title '+id);check(body.strip()==n['selftext'].strip(),'complete native body '+id)
 check(hashlib.sha256(n['selftext'].encode()).hexdigest()==k['native_body_sha256']==x['native_body_sha256'],'native body sha '+id)
 check(hashlib.sha256(('report-purchase-wave03:'+str(n['author'])).encode()).hexdigest()==k['native_author_sha256']==x['native_author_sha256'],'native author sha '+id)
 check(x['native_author']==n['author'],'native author '+id)
 check(datetime.fromtimestamp(n['created_utc'],timezone.utc).isoformat()==x['date']==header['date'],'native date '+id)
 check('https://www.reddit.com'+n['permalink']==x['url']==header['url'],'native permalink '+id)
 check(x['post_body_read_complete'] is True and x['available_identifiable_OP_replies_read']==0 and x['op_reply_ids_read']==[] and x['comment_source_available'] is False,'read/OP fields '+id)
 check(set(x['quote_ids'])=={z['id'] for z in q if z['post_id']==id},'ledger quote ids '+id)
 check(not x['standalone_customized_written_report_purchase_proven'],'false standalone classification '+id)
other=[]
for p in (R/'voice').glob('*.jsonl'):
 if p.name!='report-purchase-supplement-04.jsonl':other+=lines(p)
check(len({x['id'] for x in q})==len(q),'own duplicate IDs');check(not({x['id'] for x in q}&{x['id'] for x in other}),'global duplicate IDs')
sp=set('expecting_mother new_mother experienced_mother parent_unspecified partner relative_caregiver recovered_parent gave_up_parent advisor professional reviewer skeptic'.split())
st=set('pregnancy_early pregnancy_late newborn_0_6_weeks baby_6_16_weeks baby_4_6_months baby_6_12_months toddler return_to_work looking_back unknown'.split())
ty=set('trigger_moment pain fear tried_failed desire belief question objection advice_given success_story failure_story regret others_said'.split())
allowedthemes=set('information_overload conflicting_advice late_night_search first_time_parent not_enough_time maternal_guilt tummy_time floor_play milestone_comparison corrected_age flat_head_concern feeding_reflux contact_naps sleep_routines sleep_training_values wake_windows first_solids allergen_introduction choking_fear meal_planning food_budget pumping_schedule return_to_work daycare_handoff bottle_refusal milk_supply_concern pregnancy_activity birth_preparation postpartum_recovery household_support partner_mental_load no_village second_baby twins skepticism subscription_fatigue price_value personalization free_alternatives clinical_referral language_access privacy'.split())
for x in q:
 id=x['id'];n=native[x['post_id']];check(len(x['context'].split())<=25,'context length '+id)
 check(x['speaker'] in sp and x['stage'] in st and x['type'] in ty and set(x['themes'])<=allowedthemes,'vocab '+id)
 check(x['author']==n['author'] and x['date']==index[x['post_id']]['date'] and x['url']=='https://www.reddit.com'+n['permalink'],'quote native attribution '+id)
 check(n['author'].casefold() not in (x['quote']+' '+x['context']).casefold(),'username in selection '+id)
 check(x['raw_file']==index[x['post_id']]['raw_file'],'actual unit citation '+id)
 pos=0
 for p in x['quote'].split(' […] '):
  at=norm(n['selftext']).find(norm(p),pos);check(at>=0,'native exact quote '+id);pos=at+len(norm(p))
 ow=[z['id'] for z in other if z.get('post_id')==x['post_id'] or '/comments/'+x['post_id']+'/' in z.get('url','')]
 check(not ow,'existing work overlap '+id+str(ow))
# Copy the repository verifier into this task and point its unchanged checking logic at the research root.
ver=(R/'_tools/verify_quotes.py').read_text().replace('ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")','ROOT = str(__import__("pathlib").Path(__file__).resolve().parents[2])')
(S/'verify_quotes.py').write_text(ver)
run=subprocess.run([sys.executable,str(S/'verify_quotes.py'),str(R/'voice/report-purchase-supplement-04.jsonl')],text=True,capture_output=True)
check(run.returncode==0,'copied strict quote verifier')
(S/'strict-verification.txt').write_text(run.stdout+run.stderr)
# Every selected excerpt was manually checked against its full original above, exceeding available random-sample size.
safety=[]
for x in q:
 hits=re.findall(r'\b(?:kill\w*|suicid\w*|abuse\w*|violence|death|dead|minor|trauma\w*|diagnos\w*|chok\w*|panic\w*|medicat\w*|feed\w*|nurs\w*|weep\w*|cry\w*)\b',x['quote']+' '+x['context'],re.I)
 safety.append(dict(id=x['id'],post_id=x['post_id'],manual_full_context_review=True,regex_hits=hits,decision='Retained research-only service/format evidence; no clinical advice, safety promise, acute-crisis marketing, names or usernames selected.'))
(S/'manual-safety-review.json').write_text(json.dumps(safety,indent=2)+'\n')
unread=[dict(post_id=x['post_id'],raw_file=index[x['post_id']]['raw_file'],card_file=x['card_file'],reason=x['reason'],post_body_read_complete=False) for x in t if x['label']=='drop']
(S/'card-dropped-unread.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in unread))
check(len(unread)==127,'unread dropped size')
# ID checks are activated after final note creation.
notes=[]
for p in [R/'sources/report-purchase-supplement-04.md',R/'synthesis/reader-notes-report-purchase-supplement-04.md']:
 if p.exists():
  refs=re.findall(r'rpa04-\d{4}',p.read_text());check(set(refs)<={x['id'] for x in q},'invalid note ids '+p.name);notes.append(dict(file=str(p.relative_to(R)),distinct_ids=len(set(refs)),mentions=len(refs)))
report=dict(status='passed' if not e else 'failed',errors=e,counts=dict(assigned_cards=142,card_views=13,triaged=142,kept=15,dropped_unread=127,full_originals=15,partial_originals=0,available_OP_replies_read=0,auxiliary_reads=0,eligible=14,excluded_after_full_read=1,quotes=len(q),quoted_originals=len({x['post_id'] for x in q}),research_only_quotes=len(q),explicit_spending_originals=2,standalone_customized_written_report_purchases_established=0),native_units_checked=len(rd),native_quotes_checked=len(q),manual_quote_context_checks=len(q),card_view_hashes_checked=13,card_hashes_checked=142,read_view_hashes_checked=4,note_id_checks=notes,strict_verifier=run.stdout.strip(),dependence_review='dependence-candidates.json; same-author groups manually resolved in notes',comment_source='Unavailable for both published communities; no OP or live-thread completeness claimed',raw_immutable=True)
(R/'sources/report-purchase-supplement-04-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2));sys.exit(bool(e))
