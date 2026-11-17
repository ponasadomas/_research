from pathlib import Path
import json,gzip,hashlib,re
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent
m=json.loads((S/'full-manifest.json').read_text()); ids={x['post_id'] for x in m['keeps']}
allc={x['post_id']:x for x in map(json.loads,(R/'_raw/report-purchase-archive-wave03/supplement-v1/commercial-candidates.jsonl').read_text().splitlines())}
allc.update({x['post_id']:x for x in map(json.loads,(R/'_raw/report-purchase-archive-wave03/commercial-candidates.jsonl').read_text().splitlines())})
native={}
for p in (R/'_raw/report-purchase-archive-wave03/window').glob('*.gz'):
 with gzip.open(p,'rt') as f:
  for l in f:
   x=json.loads(l)
   if x['id'] in allc:native[x['id']]=x
quotes=[]
for p in (R/'voice').glob('*.jsonl'):
 if p.name=='report-purchase-supplement-04.jsonl':continue
 for l in p.read_text().splitlines():
  if not l.strip():continue
  q=json.loads(l);q['_file']=str(p.relative_to(R));quotes.append(q)
records=[]
for k in m['keeps']:
 id=k['post_id'];n=native[id];a=n['author']
 samecards=[z for z,c in allc.items() if z!=id and c['native_author_sha256']==k['native_author_sha256']]
 samework=[];sameauthor=[];matching=[]
 for q in quotes:
  qid=q.get('post_id') or (re.search(r'/comments/([a-z0-9]+)/',q.get('url','')).group(1) if re.search(r'/comments/([a-z0-9]+)/',q.get('url','')) else None)
  if qid==id:samework.append(q['id'])
  if q.get('author')==a or (qid in native and native[qid]['author']==a):sameauthor.append(dict(id=q['id'],post_id=qid,file=q['_file']))
  qt=q.get('quote','')
  if len(qt)>30 and qt in n['selftext']:matching.append(q['id'])
 records.append(dict(post_id=id,same_author_candidate_ids=samecards,existing_same_work_quote_ids=samework,existing_same_author_quotes=sameauthor,existing_quote_exact_in_body=matching))
(S/'dependence-candidates.json').write_text(json.dumps(records,indent=2)+'\n')
for x in records:
 if any(v for k,v in x.items() if k!='post_id'):print(json.dumps(x))
