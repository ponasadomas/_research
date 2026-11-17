#!/usr/bin/env python3
"""Flag local July duplicate bodies; flags are not automatic human exclusions."""
from pathlib import Path
import json,re,hashlib,collections
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'_raw/reddit-deep/july-2025-wave-v1'
ASSIGNED={'beyondthebump','ExclusivelyPumping','workingmoms','BabyLedWeaning','BeyondTheBumpUK'}
def main():
 candidates=list(map(json.loads,(P/'candidates.jsonl').read_text().splitlines()));docs=[];byhash=collections.defaultdict(list);inverted=collections.defaultdict(list)
 for r in candidates:
  text=(P/'primary-units'/f"{r['subreddit']}-{r['id']}.txt").read_text()
  body=text.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0].strip()
  normalized=' '.join(body.lower().split());tokens=re.findall(r'\w+',normalized);shingles={tuple(tokens[i:i+5]) for i in range(max(0,len(tokens)-4))}
  i=len(docs);docs.append({'id':r['id'],'subreddit':r['subreddit'],'title':r['title'],'body':normalized,'shingles':shingles})
  byhash[hashlib.sha256(normalized.encode()).hexdigest()].append(i)
  for sh in shingles:inverted[sh].append(i)
 exact=[[{k:docs[i][k] for k in ['id','subreddit','title']} for i in g] for g in byhash.values() if len(g)>1 and any(docs[i]['subreddit'] in ASSIGNED for i in g)]
 near=[];seen=set()
 for i,d in enumerate(docs):
  if d['subreddit'] not in ASSIGNED or len(d['shingles'])<10:continue
  shared=collections.Counter(j for sh in d['shingles'] for j in inverted[sh] if j!=i and len(inverted[sh])<=30)
  for j,count in shared.items():
   pair=tuple(sorted([i,j]))
   if pair in seen or count<.3*min(len(d['shingles']),len(docs[j]['shingles'])):continue
   seen.add(pair);other=docs[j]
   if d['body']==other['body']:continue
   similarity=len(d['shingles']&other['shingles'])/len(d['shingles']|other['shingles'])
   if similarity>=.60:near.append({'jaccard_5word':round(similarity,4),'records':[{k:docs[x][k] for k in ['id','subreddit','title']} for x in pair]})
 report={'scope':'all July primary original-post bodies; machine flags require manual inspection; no read-completeness claim','scanned_posts':len(docs),'exact_body_groups_touching_assigned':exact,'near_body_pairs_touching_assigned':near}
 out=ROOT/'sources/reddit-july-focused-duplicate-flags.json';out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print('Scanned',len(docs),'exact groups',len(exact),'near pairs',len(near))
 for g in exact:print('EXACT',[(r['subreddit'],r['id'],r['title']) for r in g])
 for g in near:print('NEAR',g['jaccard_5word'],[(r['subreddit'],r['id'],r['title']) for r in g['records']])
if __name__=='__main__':main()
