import json,sys,hashlib,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
MAN={x['thread_id']:x for x in map(json.loads,(ROOT/'_raw/oblique-deep/geo-complete-context-v1/manifest.jsonl').read_text().splitlines())}
LEDGER=ROOT/'sources/geobaby-deep-reading.jsonl';VOICE=ROOT/'voice/oblique-deep-02.jsonl'
def add(notes,quotes):
 existing=[json.loads(x) for x in LEDGER.read_text().splitlines()] if LEDGER.exists() else []
 existingq=[json.loads(x) for x in VOICE.read_text().splitlines()] if VOICE.exists() else []
 ids={x['thread_id'] for x in existing};newq=[]
 for q in quotes:
  tid,pid,speaker,stage,typ,themes,quote,context=q
  m=MAN[tid]; t=json.loads((ROOT/m['thread_json']).read_text()); p=next(p for p in t['posts'] if p['post_id']==pid)
  assert ' '.join(quote.split()) in ' '.join(p['body'].split()),(tid,pid,quote)
  assert len(quote.split())<=25 and len(context.split())<=25
  rid='odeep02-%04d'%(len(existingq)+len(newq)+1)
  newq.append(dict(id=rid,source='geobaby-forum',url=p['url'],date=p['date'],speaker=speaker,stage=stage,type=typ,themes=themes.split(','),quote=quote,context=context,raw_file=m['raw_file'],source_class='forum_oblique',evidence_kind='original_thread_post',thread_id=tid,post_id=pid,is_op=p['is_op'],author_id=p['author_id']))
 new=[]
 for tid,status,note in notes:
  assert tid not in ids;ids.add(tid);m=MAN[tid]
  new.append(dict(thread_id=tid,title=m['title'],url=m['url'],raw_file=m['raw_file'],thread_json=m['thread_json'],pages=m['pages'],posts=m['posts'],sha256=m['sha256'],reading_status=status,all_posts_and_op_followups_read=True,quoted_context_read=True,note=note,quote_ids=[q['id'] for q in newq if q['thread_id']==tid]))
 assert {q['thread_id'] for q in newq} <= {n['thread_id'] for n in new}
 with VOICE.open('a') as f:
  for q in newq:f.write(json.dumps(q,ensure_ascii=False)+'\n')
 with LEDGER.open('a') as f:
  for n in new:f.write(json.dumps(n,ensure_ascii=False)+'\n')
 print('Saved threads',len(new),'quotes',len(newq),'total',len(existing)+len(new),len(existingq)+len(newq))
def read_chunk(n):
 ch=[json.loads(x) for x in (ROOT/'_raw/oblique-deep/geo-complete-context-v1/chunks.jsonl').read_text().splitlines()][n-1]
 for tid in ch['thread_ids']:
  m=MAN[tid];t=json.loads((ROOT/m['thread_json']).read_text());print('\nTHREAD',tid,m['title'])
  for p in t['posts']:
   print('\n',p['post_id'], 'OP' if p['is_op'] else 'reply','A'+p['author_id'],p['date'],'\n'+p['body_with_quotes'])
if __name__=='__main__':read_chunk(int(sys.argv[1]))
