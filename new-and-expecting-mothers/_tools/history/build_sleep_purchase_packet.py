#!/usr/bin/env python3
"""Explicit-format plus transaction-language census in saved native originals/available OPs."""
from pathlib import Path
import json,gzip,re,collections,hashlib,datetime
R=Path(__file__).resolve().parents[1];O=R/'_raw/reddit-deep/sleep-purchases-v3';O.mkdir(exist_ok=False);(O/'units').mkdir();(O/'cards').mkdir()
fmt=re.compile(r'\bsleep\s+plans?\b|baby\s*sleep\s*answers|huckleberry|taking cara babies|little ones',re.I)
pay=re.compile(r'\bpaid\b|\bbought\b|purchas|refund',re.I)
posts={};replies=collections.defaultdict(list);nativeposts={}
for path in (R/'_raw/reddit-deep/windows/2025-h2-v1').glob('*_submissions.jsonl.gz'):
 with gzip.open(path,'rt') as f:
  for line in f:
   q=json.loads(line)
   if q.get('selftext','').strip() and q.get('selftext') not in ['[removed]','[deleted]']:posts[q['id']]=q;nativeposts[q['id']]=path
commentsources={}
for path in (R/'_raw/reddit-deep/windows/2025-h2-v1').glob('*_comments.jsonl.gz'):
 commentsources[path.name.split('_comments')[0]]=path
 with gzip.open(path,'rt') as f:
  for line in f:
   c=json.loads(line);pid=c.get('link_id','').removeprefix('t3_');p=posts.get(pid)
   if p and p.get('author') and p.get('author') not in ['[deleted]','[removed]'] and c.get('author')==p['author']:replies[pid].append(c)
previous=set(json.loads((R/'_raw/reddit-deep/continuation-v1/final-read-post-ids.json').read_text())['full_original_post_ids']);country={json.loads(x)['id'] for x in (R/'_raw/reddit-deep/next-july-country-B-v1/candidates.jsonl').read_text().splitlines()}
index=[];cards=[]
for pid,q in posts.items():
 op=sorted(replies[pid],key=lambda x:(int(x['created_utc']),x['id']));texts=[q.get('title','')+'\n'+q['selftext']]+[c['body'] for c in op];matches=[i for i,text in enumerate(texts) if fmt.search(text) and pay.search(text)]
 if not matches:continue
 sub=q['subreddit'];permalink=q['permalink'];url='https://www.reddit.com'+permalink if permalink.startswith('/') else permalink;date=datetime.datetime.fromtimestamp(int(q['created_utc']),datetime.timezone.utc).isoformat();meta={'post_id':pid,'subreddit':sub,'url':url,'post_date':date,'title':q['title'],'source_post_file':str(nativeposts[pid].relative_to(R)),'source_comment_file':str(commentsources[sub].relative_to(R)) if sub in commentsources else None,'comment_source_available':sub in commentsources,'OP_replies':len(op),'OP_comment_ids':[c['id'] for c in op],'prior_full_read':pid in previous,'country_current_assignment':pid in country,'matched_original_body':0 in matches,'matched_OP_comment_ids':[op[i-1]['id'] for i in matches if i>0],'provenance':'independentpublisherarchive, pinnedcommit ea497c510aa68765c07ed744ec9f84d68bbedf7f, authenticity/license/livecompletenessunverified'}
 text='REPORT-PURCHASE DISCOVERY CANDIDATE — NOT A HUMAN PURCHASE CLASSIFICATION\n'+json.dumps(meta,ensure_ascii=False,indent=2)+'\n\n=== COMPLETE ORIGINAL POST TITLE ===\n'+q['title']+'\n\n=== COMPLETE ORIGINAL POST BODY ===\n'+q['selftext']+'\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===\n'
 if sub not in commentsources:text+='The publisher comment file is unavailable; no live follow-up completeness is claimed.\n'
 elif not op:text+='No identifiable OP replies in available frozen archive; not proof none existed live.\n'
 for c in op:
  u=c['permalink'];u='https://www.reddit.com'+u if u.startswith('/') else u;m={'comment_id':c['id'],'date':datetime.datetime.fromtimestamp(int(c['created_utc']),datetime.timezone.utc).isoformat(),'parent_id':c.get('parent_id'),'url':u};text+='\n--- OP REPLY ---\n'+json.dumps(m,ensure_ascii=False)+'\n'+c['body']+'\n'
 p=O/f'units/{sub}-{pid}.txt';p.write_bytes(text.encode());row={**meta,'raw_file':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'utf8_bytes':p.stat().st_size};index.append(row)
 excerpt=q['selftext'][:350]
 if not 0 in matches:excerpt+='\nMATCHED OP OPENING: '+op[matches[0]-1]['body'][:350]
 cards.append((pid,f"ID {pid} | r/{sub} | {date} | prior_full_read={pid in previous} | in_current_country_assignment={pid in country}\nTITLE: {q['title']}\nOPENING: {excerpt}\nFORMAT MATCH: {fmt.search(texts[matches[0]]).group(0)}\nTRANSACTION MATCH: {pay.search(texts[matches[0]]).group(0)}"))
index.sort(key=lambda x:(x['subreddit'],x['post_date'],x['post_id']));cardby=dict(cards);chunks=[];parts=[];size=0
for row in index:
 t=cardby[row['post_id']]
 if parts and size+len(t.encode())>14000:
  n=len(chunks)+1;p=O/f'cards/cards-{n:02}.txt';p.write_text('\n\n'.join(x[1] for x in parts));chunks.append({'chunk':n,'file':str(p.relative_to(R)),'post_ids':[x[0] for x in parts],'sha256':hashlib.sha256(p.read_bytes()).hexdigest()});parts=[];size=0
 parts.append((row['post_id'],t));size+=len(t.encode())+2
if parts:
 n=len(chunks)+1;p=O/f'cards/cards-{n:02}.txt';p.write_text('\n\n'.join(x[1] for x in parts));chunks.append({'chunk':n,'file':str(p.relative_to(R)),'post_ids':[x[0] for x in parts],'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(O/'primary-index.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in index));(O/'cards-index.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in chunks));summary={'scope':'All98000readableH2nativeposts and identifiableOPreplies in availabletwofiles; named sleepbrands OR sleep-plan terms AND explicit paid/bought/purchase/refund in same author body; candidate not proof.','post_candidates':len(index),'prior_full_read':sum(x['prior_full_read'] for x in index),'overlap_current_country_assignment':sum(x['country_current_assignment'] for x in index),'OP_replies_in_packet':sum(x['OP_replies'] for x in index),'card_chunks':len(chunks),'format_regex':fmt.pattern,'transaction_regex':pay.pattern,'human_triage':0,'human_full_reads':0};(O/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
