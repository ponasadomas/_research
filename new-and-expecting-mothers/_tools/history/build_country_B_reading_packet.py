#!/usr/bin/env python3
"""Add frozen full-source units/assignments to the prepared847-card scope; no keep decisions."""
from pathlib import Path
import json,gzip,hashlib,collections,datetime
R=Path(__file__).resolve().parents[1];P=R/'_raw/reddit-deep/next-july-country-B-v1';O=P/'primary-v1';O.mkdir(exist_ok=False);(O/'units').mkdir();(O/'assignments').mkdir()
jl=lambda p:[json.loads(x) for x in p.read_text().splitlines() if x.strip()]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=jl(P/'candidates.jsonl');selected={x['id'] for x in rows};old=json.loads((R/'_raw/reddit-deep/continuation-v1/final-read-post-ids.json').read_text());assert len(selected)==847 and not selected&set(old['full_original_post_ids'])
cards=jl(P/'cards-index.jsonl');assert set.union(*(set(x['post_ids']) for x in cards))==selected
batches=[[] for _ in range(3)];loads=[0]*3
for card in sorted(cards,key=lambda x:(-x['utf8_bytes'],x['chunk'])):
 i=min(range(3),key=lambda n:(loads[n],len(batches[n]),n));batches[i].append(card);loads[i]+=card['utf8_bytes']
ownership={}
for number,batch in enumerate(batches,1):
 batch.sort(key=lambda x:x['chunk']);ids=[pid for c in batch for pid in c['post_ids']]
 for pid in ids:assert pid not in ownership;ownership[pid]=number
 m={'reader':number,'scope':'ALL inherited candidate cards; manual triage then EVERY keep in full, all topics','cards':len(ids),'card_chunks':len(batch),'post_ids':ids,'chunks':batch}
 (O/f'assignments/batch-{number:02}.json').write_text(json.dumps(m,indent=2)+'\n')
posts={};groups=collections.defaultdict(list)
for path in sorted((R/'_raw/reddit-deep/windows/2025-h2-v1').glob('*_submissions.jsonl.gz')):
 with gzip.open(path,'rt') as f:
  for line in f:
   q=json.loads(line);body=q.get('selftext','');stamp=datetime.datetime.fromtimestamp(int(q['created_utc']),datetime.timezone.utc).isoformat()
   if len(body.strip())>=100:groups[hashlib.sha256(' '.join(body.split()).encode()).hexdigest()].append({'post_id':q['id'],'subreddit':q['subreddit'],'date':stamp,'title':q.get('title','')})
   if q['id'] in selected:posts[q['id']]=(q,path)
assert set(posts)==selected
index=[]
for pid in sorted(selected):
 q,native=posts[pid];sub=q['subreddit'];assert sub in ['BabyBumpsCanada','BabyBumpsandBeyondAu','BeyondTheBumpUK'];assert not (R/f'_raw/reddit-deep/windows/2025-h2-v1/{sub}_comments.jsonl.gz').exists()
 permalink=q['permalink'];url='https://www.reddit.com'+permalink if permalink.startswith('/') else permalink
 meta={'post_id':pid,'subreddit':sub,'url':url,'post_date':datetime.datetime.fromtimestamp(int(q['created_utc']),datetime.timezone.utc).isoformat(),'title':q.get('title',''),'reader_batch':ownership[pid],'source_post_file':str(native.relative_to(R)),'source_comment_file':None,'comment_source_available':False,'OP_replies':0,'OP_comment_ids':[],'primary_read_scope':'complete_original_post_only_comment_source_unavailable','source_window_end_exclusive':'2026-01-01T00:00:00+00:00','publisher_provenance_license_and_live_completeness':'unverified'}
 text='ARCHIVED ORIGINAL — JULY COUNTRY B COMPARISON\n'+json.dumps(meta,ensure_ascii=False,indent=2)+'\n\n=== COMPLETE ORIGINAL POST TITLE ===\n'+q.get('title','')+'\n\n=== COMPLETE ORIGINAL POST BODY ===\n'+q.get('selftext','')+'\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===\nThe publisher comment file is unavailable; no live follow-up completeness is claimed.\n'
 p=O/f'units/{sub}-{pid}.txt';p.write_bytes(text.encode());index.append({**meta,'raw_file':str(p.relative_to(R)),'sha256':sha(p),'utf8_bytes':p.stat().st_size})
(O/'primary-index.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in index));dups=[{'records':g,'human_review_required':True,'comparison':'Exact case-preserving body after whitespace collapse, across all nine native H2 submission files.'} for g in groups.values() if len(g)>1 and any(x['post_id'] in selected for x in g)];(O/'duplicate-flags.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in dups));summary={'scope':'ALL847preparedJulycountryBcards, no topics/ranking/cap','captured_primary_units':847,'primary_bytes':sum(x['utf8_bytes'] for x in index),'OP_comment_sources_available':False,'human_triage':0,'human_full_reads':0,'duplicate_groups_for_human_review':len(dups),'assignments':[{'reader':n,'cards':sum(len(c['post_ids']) for c in b),'card_chunks':len(b)} for n,b in enumerate(batches,1)],'baseline_read_ID_manifest_sha256':sha(R/'_raw/reddit-deep/continuation-v1/final-read-post-ids.json')};(O/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
