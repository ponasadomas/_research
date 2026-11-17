#!/usr/bin/env python3
"""Freeze full source views for explicit manual checks. Never select or classify quotes."""
from pathlib import Path
import json,hashlib,sys
R=Path(__file__).resolve().parents[1]

def build(relative_dir,ids,max_bytes=15000):
 D=R/relative_dir;D.mkdir(parents=True,exist_ok=False)
 qs={q['id']:q for p in (R/'voice').glob('*.jsonl') for q in map(json.loads,p.read_text().splitlines())}
 groups={}
 for rid in ids:
  q=qs[rid];groups.setdefault(q['raw_file'],[]).append(rid)
 chunks=[];current=[];nbytes=0
 for raw,rids in groups.items():
  text=(R/raw).read_bytes().decode('utf-8');body=text.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1]
  title=text.split('=== COMPLETE ORIGINAL POST TITLE ===\n',1)[1].split('\n\n=== COMPLETE ORIGINAL POST BODY ===',1)[0] if '=== COMPLETE ORIGINAL POST TITLE ===' in text else '[See native raw header]'
  part='=== FULL SOURCE CONTEXT '+','.join(rids)+' ===\n'+json.dumps({'raw_file':raw,'post_id':qs[rids[0]]['post_id'],'title':title},ensure_ascii=False)+'\n'+body
  if current and nbytes+len(part.encode())>max_bytes:chunks.append(current);current=[];nbytes=0
  current.append({'raw_file':raw,'quote_ids':rids,'text':part,'raw_sha256':hashlib.sha256((R/raw).read_bytes()).hexdigest()});nbytes+=len(part.encode())
 if current:chunks.append(current)
 manifest=[]
 for i,items in enumerate(chunks,1):
  path=D/f'contexts-{i:02}.txt';path.write_bytes('\n\n'.join(x['text'] for x in items).encode());manifest.append({'chunk':i,'path':str(path.relative_to(R)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'sources':[{k:v for k,v in x.items() if k!='text'} for x in items]})
 (D/'manifest.json').write_text(json.dumps({'quote_ids':ids,'chunks':manifest},indent=2)+'\n');return manifest
if __name__=='__main__':
 result=build(sys.argv[1],sys.argv[2:]);print('Frozen views',len(result),'for explicit quote IDs',len(sys.argv)-2)
