from pathlib import Path
import json,csv,gzip,hashlib,re,datetime,collections,sys
from full_reader import ROOT,SCRATCH,PACKET,INDEX,records,READ,VOICE,original_body,MANIFEST
complete='--complete' in sys.argv
manifest=json.loads((PACKET/'assignments/batch-03-after-transfer.json').read_text())
triage=list(csv.DictReader((ROOT/'_raw/reddit-deep/triage/augdec-03.tsv').open(),delimiter='\t'))
read=records(READ);voice=records(VOICE);errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
norm=lambda x:re.sub(r'\s+',' ',x).strip()
check(len(triage)==len(set(x['post_id'] for x in triage))==1585,'Triage count/unique')
check({x['post_id'] for x in triage}==set(manifest['post_ids']),'Triage exact revised assignment')
cardlogs=records(SCRATCH/'triage-reading-ledger.jsonl')
check(len(cardlogs)==27,'Complete card file ledger count')
for c,log in zip(manifest['chunks'],cardlogs):
 check(log['cards_read_complete'] is True and log['card_file']==c['file'],'Card file completion '+c['file'])
 check(log['post_ids']==c['post_ids'] and log['card_count']==c['cards'],'Card file exact IDs '+c['file'])
 check(log['sha256']==c['sha256']==hashlib.sha256((ROOT/c['file']).read_bytes()).hexdigest(),'Card file immutable hash '+c['file'])
keep={x['post_id'] for x in triage if x['label']!='drop'};readids={x['post_id'] for x in read}
check(len(readids)==len(read),'Duplicate reading IDs');check(readids<=keep,'Unexpected read ID')
if complete:check(readids==keep,'Kept originals remain unread')
vby=collections.defaultdict(list)
for q in voice:vby[q['post_id']].append(q['id'])
for r in read:
 x=INDEX[r['post_id']]
 check(r['post_body_read_complete'] is True,'Body incomplete '+r['post_id'])
 check(r['primary_unit_sha256']==x['sha256']==hashlib.sha256((ROOT/r['raw_file']).read_bytes()).hexdigest(),'Raw hash '+r['post_id'])
 check(r['op_reply_ids_read']==x['OP_comment_ids'] and r['available_identifiable_OP_replies_read']==len(x['OP_comment_ids'])==x['OP_replies'],'OP replies '+r['post_id'])
 check(r['quote_ids']==vby[r['post_id']],'Quote ledger '+r['post_id'])
 check(not r['quote_ids'] or r['post_body_read_complete'] is True,'Excluded quote '+r['post_id'])
aux=records(ROOT/'sources/reddit-augdec-03-auxiliary-read.jsonl')
posts={};comments={};needed={q['post_id'] for q in voice};neededposts=needed|readids;neededcomments={tid for r in read for tid in r['op_reply_ids_read']}|{x['comment_id'] for x in aux}
for file in {INDEX[tid]['source_post_file'] for tid in neededposts}:
 with gzip.open(ROOT/file,'rt') as f:
  for line in f:
   x=json.loads(line)
   if x.get('id') in neededposts:posts[x['id']]=x
for file in {INDEX[r['post_id']]['source_comment_file'] for r in read if r['op_reply_ids_read']}:
 with gzip.open(ROOT/file,'rt') as f:
  for line in f:
   x=json.loads(line)
   if x.get('id') in neededcomments:comments[x['id']]=x
for r in read:
 check(norm(original_body(r['post_id']))==norm(posts[r['post_id']].get('selftext','')),'Complete native body '+r['post_id'])
 for tid in r['op_reply_ids_read']:
  c=comments.get(tid,{});p=posts[r['post_id']]
  check(c.get('link_id')=='t3_'+r['post_id'],'Native OP link '+tid)
  check(c.get('author')==p.get('author') and c.get('author') not in [None,'[deleted]','[removed]'],'Native identifiable OP author '+tid)
for x in aux:
 c=comments.get(x['comment_id'],{})
 check(x['body_read_complete'] is True,'Auxiliary incomplete '+x['comment_id'])
 check(hashlib.sha256(c.get('body','').encode()).hexdigest()==x['body_sha256'],'Auxiliary native body hash '+x['comment_id'])
 check(c.get('link_id')=='t3_'+x['post_id'],'Auxiliary native parent link '+x['comment_id'])
for chunk in MANIFEST['chunks']:
 path=ROOT/chunk['file'];view=path.read_text()
 check(hashlib.sha256(path.read_bytes()).hexdigest()==chunk['sha256'],'Frozen view hash '+str(chunk['chunk']))
 for tid in chunk['post_ids']:
  check(norm(original_body(tid)) in norm(view),'Displayed complete post body '+tid)
  for cid in INDEX[tid]['OP_comment_ids']:
   check(norm(comments[cid]['body']) in norm(view),'Displayed complete OP body '+cid)
speakers=set('expecting_mother new_mother experienced_mother parent_unspecified partner relative_caregiver recovered_parent gave_up_parent advisor professional reviewer skeptic'.split())
stages=set('pregnancy_early pregnancy_late newborn_0_6_weeks baby_6_16_weeks baby_4_6_months baby_6_12_months toddler return_to_work looking_back unknown'.split())
types=set('trigger_moment pain fear tried_failed desire belief question objection advice_given success_story failure_story regret others_said'.split())
for q in voice:
 check(q['post_id'] in readids,'Unread quote '+q['id'])
 x=comments[q['comment_id']] if q.get('comment_id') else posts[q['post_id']]
 body=x.get('body','') if q.get('comment_id') else x.get('selftext','')
 for part in q['quote'].split(' […] '):check(norm(part) in norm(body),'STRICT native-body quote '+q['id'])
 date=datetime.datetime.fromtimestamp(float(x['created_utc']),datetime.timezone.utc).date().isoformat()
 check(q['date']==date,'Native date '+q['id'])
 permalink=x.get('permalink','');url='https://www.reddit.com'+permalink if permalink.startswith('/') else permalink
 check(q['url'].rstrip('/')==url.rstrip('/'),'Native URL '+q['id'])
 check(q['speaker'] in speakers and q['stage'] in stages and q['type'] in types,'Vocabulary '+q['id'])
 check(len(q['context'].split())<=25,'Context length '+q['id'])
 check(q['raw_file']==INDEX[q['post_id']]['raw_file'],'Immutable raw path '+q['id'])
 check(q['read_scope']==('full_post_and_available_identifiable_OP_replies' if INDEX[q['post_id']]['comment_source_available'] else 'full_post_comment_source_unavailable'),'Read scope '+q['id'])
allids=[];otherpostrefs=collections.defaultdict(list)
for file in (ROOT/'voice').glob('*.jsonl'):
 for q in records(file):
  allids.append(q['id'])
  if file!=VOICE and q.get('post_id') in needed:otherpostrefs[q['post_id']].append(q['id'])
for q in voice:check(allids.count(q['id'])==1,'Global duplicate quote ID '+q['id'])
result=dict(complete=complete,original_assignment=2205,transferred_to_root=620,assigned_revised=len(triage),kept=len(keep),dropped=len(triage)-len(keep),full_originals_read=len(read),available_identifiable_OP_replies_read=sum(x['available_identifiable_OP_replies_read'] for x in read),unread_kept_ids=sorted(keep-readids),statuses=dict(collections.Counter(x['status'] for x in read)),quotes=len(voice),quoted_posts=len(needed),cross_wave_post_references=dict(otherpostrefs),strict_native_quote_failures=[x for x in errors if x.startswith('STRICT')],errors=errors,voice_sha256=hashlib.sha256(VOICE.read_bytes()).hexdigest(),triage_sha256=hashlib.sha256((ROOT/'_raw/reddit-deep/triage/augdec-03.tsv').read_bytes()).hexdigest(),reading_sha256=hashlib.sha256(READ.read_bytes()).hexdigest())
result.update(auxiliary_native_parent_comments_read=len(aux),available_non_OP_comments_unread=sum(INDEX[p]['non_OP_comments_unread'] for p in readids)-len(aux),kept_posts_comment_source_unavailable=sum(not INDEX[p]['comment_source_available'] for p in readids),frozen_full_read_views=len(MANIFEST['chunks']),post_body_excerpts=sum('comment_id' not in q for q in voice),OP_reply_excerpts=sum('comment_id' in q for q in voice),research_only_excerpts=sum(q.get('marketing_eligible') is False for q in voice))
(ROOT/'sources/reddit-augdec-03-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['unread_kept_ids']},indent=2));sys.exit(bool(errors))
