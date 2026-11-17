#!/usr/bin/env python3
"""Append a manually selected original-post excerpt after exact source checks."""
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'_raw/oblique-deep'
DEST=ROOT/'voice/oblique-deep-01.jsonl'

def norm(s):return ' '.join(s.split())
def add(prefix,tid,pid,quote,themes,kind,context,stage='unknown',speaker='participant'):
 thread=json.loads((RAW/'threads'/f'{prefix}-{tid}.json').read_text())
 post=next(p for p in thread['posts'] if p['post_id']==pid)
 chunks=[json.loads(s) for s in (RAW/'corpus'/f'{prefix}-chunks.jsonl').read_text().splitlines()]
 chunk=next(c for c in chunks if tid in c['thread_ids'] and pid in (ROOT/c['file']).read_text())
 old=[json.loads(s) for s in DEST.read_text().splitlines()] if DEST.exists() else []
 if any(q['url']==post['url'] and q['quote']==quote for q in old):return
 pieces=quote.split(' […] ')
 assert all(norm(q) in norm(post['body']) for q in pieces),(tid,pid,quote)
 words=len(' '.join(pieces).split())
 assert words+sum(len(q['quote'].replace(' […] ',' ').split()) for q in old if q['url']==post['url'])<=25
 assert len(context.split())<=25
 rec={'id':f'odeep01-{len(old)+1:04}','source':'mse-forum' if prefix=='mse' else 'geobaby-publisher-archive','url':post['url'],'date':post['date'][:10],'speaker':speaker,'stage':stage,'type':kind,'themes':themes,'quote':quote,'context':context,'raw_file':chunk['file'],'source_class':'forum_oblique','evidence_kind':'original_thread_post','thread_id':tid,'post_id':pid,'author_id':post['author_id'],'is_op':post['is_op']}
 with DEST.open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
 print(rec['id'],words,tid,pid)

if __name__=='__main__':
 for line in sys.stdin:
  if line.strip():add(**json.loads(line))
