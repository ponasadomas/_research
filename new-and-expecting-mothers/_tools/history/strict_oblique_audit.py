#!/usr/bin/env python3
"""Whitespace-only fidelity, original-post word budget, read provenance and hashes."""
import json,re,collections,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def norm(s):return ' '.join(s.split())
def main():
 voice=ROOT/'voice/oblique-deep-01.jsonl';quotes=[json.loads(s) for s in voice.read_text().splitlines()]
 read={r['thread_id'] for r in map(json.loads,(ROOT/'_raw/oblique-deep/thread-reading-inventory.jsonl').read_text().splitlines()) if r['reading_status']=='read_complete'}
 errors=[];budget=collections.Counter();ids=[]
 for q in quotes:
  ids.append(q['id']);prefix='mse' if q['source']=='mse-forum' else 'geo'
  thread=json.loads((ROOT/'_raw/oblique-deep/threads'/f"{prefix}-{q['thread_id']}.json").read_text())
  post=next(r for r in thread['posts'] if r['post_id']==q['post_id'])
  for label,raw in [('frozen corpus',(ROOT/q['raw_file']).read_text()),('actual original post',post['body'])]:
   pos=0;haystack=norm(raw)
   for piece in re.split(r'\s*\[(?:…|\.\.\.)\]\s*',q['quote']):
    found=haystack.find(norm(piece),pos)
    if found<0:errors.append([q['id'],label,'whitespace-only exact containment'])
    else:pos=found+len(norm(piece))
  key=(prefix,q['thread_id'],q['post_id']);budget[key]+=len(q['quote'].replace(' […] ',' ').split())
  if q['thread_id'] not in read:errors.append([q['id'],'discussion not fully read'])
  if q['url']!=post['url']:errors.append([q['id'],'original post URL mismatch'])
  if len(q['context'].split())>25:errors.append([q['id'],'context exceeds25words'])
  if q['source_class']!='forum_oblique' or q['evidence_kind']!='original_thread_post':errors.append([q['id'],'source classification'])
 for key,count in budget.items():
  if count>25:errors.append([key,'quote budget exceeds25words',count])
 if len(set(ids))!=len(ids):errors.append(['duplicate ids'])
 print(json.dumps({'quotes':len(quotes),'failures':errors,'voice_sha256':hashlib.sha256(voice.read_bytes()).hexdigest()},indent=2))
 if errors:raise SystemExit(1)
if __name__=='__main__':main()
