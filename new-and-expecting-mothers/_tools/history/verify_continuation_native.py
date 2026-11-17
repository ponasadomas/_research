#!/usr/bin/env python3
"""Independent native-body/metadata audit for all new reader ledgers. No source mutation."""
from pathlib import Path
import json,gzip,collections,datetime,hashlib,sys
R=Path(__file__).resolve().parents[1];OUT=R/'_raw/audit/continuation-2026-10-24';partial='--progress' in sys.argv
jl=lambda p:[json.loads(x) for x in p.read_text().splitlines() if x.strip()] if p.exists() else []
names=[f'reddit-augdec-{n:02}' for n in range(1,9)]+['reddit-july-B-solids']
read=[];aux=[];quotes=[];errors=[]
for name in names:
 read += [dict(x,_reader=name) for x in jl(R/f'sources/{name}-reading.jsonl')]
 aux += [dict(x,_reader=name) for x in jl(R/f'sources/{name}-auxiliary-read.jsonl')]
 quotes += [dict(x,_reader=name) for x in jl(R/f'voice/{name}.jsonl')]
check=lambda value,msg:None if value else errors.append(msg)
readids={x['post_id'] for x in read};check(len(readids)==len(read),'Duplicate continuation full-read post IDs')
inspections=jl(R/'sources/reddit-augdec-07-duplicate-inspections.jsonl');extra=[x for x in inspections if x['post_id'] not in readids];read+=extra;readids.update(x['post_id'] for x in extra)
posts={};comments={};by_post=collections.defaultdict(list)
for path in (R/'_raw/reddit-deep/windows/2025-h2-v1').glob('*_submissions.jsonl.gz'):
 with gzip.open(path,'rt') as f:
  for line in f:
   x=json.loads(line)
   if x['id'] in readids:posts[x['id']]=x
auxids={x['comment_id'] for x in aux}
for path in (R/'_raw/reddit-deep/windows/2025-h2-v1').glob('*_comments.jsonl.gz'):
 with gzip.open(path,'rt') as f:
  for line in f:
   x=json.loads(line);pid=x.get('link_id','').removeprefix('t3_')
   if pid in readids:comments[x['id']]=x;by_post[pid].append(x)
   elif x['id'] in auxids:comments[x['id']]=x
index={x['post_id']:x for folder in ['aug-dec-2025-wave-v1','july-B-solids-v1'] for x in jl(R/f'_raw/reddit-deep/{folder}/primary-index.jsonl')}
ledger={x['post_id']:x for x in read};nativeop=set()
for row in read:
 pid=row['post_id'];p=posts.get(pid);i=index[pid]
 check(bool(p),'Missing native post '+pid)
 if not p:continue
 author=p.get('author');ops=[x for x in by_post[pid] if author and author not in ['[removed]','[deleted]'] and x.get('author')==author];ids={x['id'] for x in ops};nativeop.update(ids)
 check(row['post_body_read_complete'] is True,'Body not marked complete '+pid)
 check(set(row['op_reply_ids_read'])==ids,'Incomplete/incorrect native OP IDs '+pid)
 check(row['available_identifiable_OP_replies_read']==len(ids),'Incorrect OP count '+pid)
 raw=R/row['raw_file'];text=raw.read_bytes().decode('utf-8');body=text.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0]
 check(body==p.get('selftext',''),'Full native original-body mismatch '+pid)
 check(hashlib.sha256(raw.read_bytes()).hexdigest()==row['primary_unit_sha256']==i['sha256'],'Full unit hash mismatch '+pid)
 check(row['raw_file']==i['raw_file'],'Full unit path mismatch '+pid)
 for x in ops:check(x.get('body','') in text,'OP body absent from full unit '+x['id'])
for q in quotes:
 pid=q['post_id'];rid=q['id'];row=ledger.get(pid);check(row is not None,'Quote without full read '+rid)
 if not row:continue
 n=comments.get(q['comment_id']) if q.get('comment_id') else posts.get(pid)
 check(n is not None,'Missing native quote body '+rid)
 if not n:continue
 if q.get('comment_id'):check(q['comment_id'] in row['op_reply_ids_read'],'Quote not own identifiable OP reply '+rid)
 body=n.get('body','') if q.get('comment_id') else n.get('selftext','')
 for part in q['quote'].split(' […] '):check(part in body,'Exact literal quote not in own native body '+rid)
 stamp=datetime.datetime.fromtimestamp(float(n['created_utc']),datetime.timezone.utc).isoformat()
 check(q['date'] in [stamp,stamp[:10]],'Native date mismatch '+rid)
 permalink=n.get('permalink','');url='https://www.reddit.com'+permalink if permalink.startswith('/') else permalink
 check(q['url'].rstrip('/')==url.rstrip('/'),'Native canonical permalink mismatch '+rid)
 check(q['raw_file']==row['raw_file'],'Quote raw unit mismatch '+rid)
 check(row['post_body_read_complete'] is True,'Quoted source body not completely read '+rid)
 check(len(q['context'].split())<=25,'Context over25words '+rid)
for row in aux:
 tid=row['comment_id'];n=comments.get(tid);check(bool(n),'Auxiliary comment missing '+tid)
 if not n:continue
 check(n.get('link_id')=='t3_'+row['post_id'],'Auxiliary parent-post mismatch '+tid)
 check(n.get('author')!=posts[row['post_id']].get('author'),'Auxiliary misclassified as nonOP '+tid)
 check(row.get('full_comment_read') is True or row.get('body_read_complete') is True,'Auxiliary not marked complete '+tid)
 if row.get('body_sha256'):check(hashlib.sha256(n['body'].encode()).hexdigest()==row['body_sha256'],'Auxiliary native body hash mismatch '+tid)
 if row.get('sha256'):
  p=R/row['raw_file'];check(hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],'Auxiliary raw hash mismatch '+tid);check(json.loads(p.read_text())==n,'Auxiliary saved native record mismatch '+tid)
base=json.loads((OUT/'baseline-voice-manifest.json').read_text())
for row in base:check(hashlib.sha256((R/row['path']).read_bytes()).hexdigest()==row['sha256'],'Committed baseline voice mutated '+row['path'])
result=dict(progress_only=partial,full_original_posts=len(read),additional_audit_inspections=len(inspections),additional_distinct_full_posts_from_inspection=len(extra),identifiable_OP_replies=len(nativeop),auxiliary_comments_distinct=len(auxids),selected_quotes=len(quotes),research_only_ids=[q['id'] for q in quotes if q.get('marketing_eligible') is False],errors=errors,failed=len(errors),voice_sha256={name:hashlib.sha256((R/f'voice/{name}.jsonl').read_bytes()).hexdigest() for name in names if (R/f'voice/{name}.jsonl').exists()})
(OUT/('native-audit-progress.json' if partial else 'final-native-audit.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));sys.exit(bool(errors))
