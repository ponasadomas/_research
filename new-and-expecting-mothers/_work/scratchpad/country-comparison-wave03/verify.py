# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
from pathlib import Path
import json,csv,collections,hashlib,re,gzip,datetime
R=Path(__file__).resolve().parents[2];S=R/'scratchpad/country-comparison-wave03';P=R/'_raw/reddit-deep/next-july-country-B-v1/primary-v1';I={x['post_id']:x for x in map(json.loads,(P/'primary-index.jsonl').read_text().splitlines())};m=json.loads((S/'manifest.json').read_text());errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
norm=lambda x:re.sub(r'\s+',' ',x).strip()
alltr=[];allread=[];allquotes=[];summaries=[];inputs={}
for n in [1,2,3]:
 stem=f'reddit-country-B-0{n}';t=R/f'_raw/reddit-deep/triage/country-B-0{n}.tsv';rd=R/f'sources/{stem}-reading.jsonl';v=R/f'voice/{stem}.jsonl';note=R/f'synthesis/reader-notes-{stem}.md';source=R/f'sources/{stem}.md'
 tr=list(csv.DictReader(t.open(),delimiter='\t'));rows=[json.loads(x) for x in rd.read_text().splitlines()];qs=[json.loads(x) for x in v.read_text().splitlines()];check({x['post_id'] for x in rows}=={x['post_id'] for x in tr if x['label']!='drop'},f'Reader{n}exact keep/read');check(all(x['post_body_read_complete'] is True and x['available_identifiable_OP_replies_read']==0 and x['op_reply_ids_read']==[] for x in rows),'All full/missing-comments scope')
 summaries.append(dict(reader=n,triaged=len(tr),kept=len(rows),dropped=sum(x['label']=='drop' for x in tr),statuses=dict(collections.Counter(x['status'] for x in rows)),quotes=len(qs),research_only=sum(x.get('marketing_eligible') is False for x in qs)));alltr+=tr;allread+=rows;allquotes+=qs
 for p in [t,rd,v,note,source]:inputs[str(p.relative_to(R))]=hashlib.sha256(p.read_bytes()).hexdigest()
check(len(alltr)==len({x['post_id'] for x in alltr})==847 and {x['post_id'] for x in alltr}==set(I),'All847assigned/triaged IDs exactly once');check(len(allread)==len({x['post_id'] for x in allread})==584,'All584full IDs distinct');check(len(allquotes)==len({x['id'] for x in allquotes})==117,'117unique own quote IDs');check(sum(x['status']=='eligible' for x in allread)==478 and sum(x['status']=='excluded_after_read' for x in allread)==106,'478eligible106excluded');

communities={k:dict(triaged=sum(I[x['post_id']]['subreddit']==k for x in alltr),read=sum(I[x['post_id']]['subreddit']==k for x in allread)) for k in ['BabyBumpsCanada','BabyBumpsandBeyondAu','BeyondTheBumpUK']}
for x in communities.values():x['card_drops']=x['triaged']-x['read']
qmap={x['id']:x for x in allquotes};doc=R/'synthesis/country-comparison-wave03.md';refs=set(re.findall(r'rcb0[123]-\d{4}',doc.read_text()));check(refs<=set(m['lookup_ids'])<=set(qmap),'Every cited ID looked up');native={};wanted={qmap[q]['post_id'] for q in m['lookup_ids']}
for name in {I[t]['source_post_file'] for t in wanted}:
 with gzip.open(R/name,'rt') as f:
  for s in f:
   x=json.loads(s)
   if x.get('id') in wanted:native[x['id']]=x
for qid in m['lookup_ids']:
 q=qmap[qid];n=native[q['post_id']]
 for part in q['quote'].split(' […] '):check(norm(part) in norm(n['selftext']),'Native exact quote '+qid)
 check(q['date'][:10]==datetime.datetime.fromtimestamp(float(n['created_utc']),datetime.timezone.utc).date().isoformat() and (len(q['date'])==10 or abs(datetime.datetime.fromisoformat(q['date'].replace('Z','+00:00')).timestamp()-float(n['created_utc']))<1),'Native date/timestamp '+qid);check(q['url'].rstrip('/')==('https://www.reddit.com'+n['permalink']).rstrip('/'),'Native URL '+qid)
for v in m['views']:check(hashlib.sha256((R/v['file']).read_bytes()).hexdigest()==v['sha256'],'Lookup view hash')
for x in m['lookups']:check(hashlib.sha256(native[x['post_id']]['selftext'].encode()).hexdigest()==x['native_body_sha256'] and hashlib.sha256((R/x['raw_unit']).read_bytes()).hexdigest()==x['raw_unit_sha256'],'Lookup source hash '+x['quote_id'])
check(m.get('human_reread_complete') is True and len(m['lookup_ids'])==31 and m['new_original_reading_credit']==0,'31manual native-context rereads,zero newcredit')
result=dict(complete=True,readers=summaries,communities=communities,triaged=847,kept_full_originals=584,card_drop_bodies_unread=263,eligible_contexts=478,excluded_after_read=106,quotes=117,research_only=26,missing_comment_sources=584,OP_replies_read=0,extra_duplicate_only_bodies_separate=5,comparison_native_context_rereads=31,new_original_reading_credit=0,new_quotes=0,cited_quote_ids=sorted(refs),errors=errors,inputs_sha256=inputs,comparison_sha256=hashlib.sha256(doc.read_bytes()).hexdigest());(S/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['inputs_sha256','cited_quote_ids']},indent=2));raise SystemExit(bool(errors))
