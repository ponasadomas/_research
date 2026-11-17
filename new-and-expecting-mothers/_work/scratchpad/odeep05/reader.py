import json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]
M=[json.loads(s) for s in (R/'_raw/oblique-deep/mse-completion-v2/batch-03/manifest.jsonl').read_text().splitlines()]
C=[json.loads(s) for s in (R/'_raw/oblique-deep/mse-completion-v2/batch-03/chunks.jsonl').read_text().splitlines()]
def thread(tid):return json.loads((R/f'_raw/oblique-deep/threads/mse-{tid}.json').read_text())
def show(c,part=1):
 ts=C[c-1]['thread_ids'];pages=[];buf=''
 for tid in ts:
  t=thread(tid)
  for i,p in enumerate(t['posts'],1):
   s=f"\nTHREAD {tid} {t['title']} POST {i}/{len(t['posts'])} {p['post_id']} {'OP' if p['is_op'] else 'reply'}\n{p.get('body_with_quotes',p['body'])}\n"
   if len(buf)+len(s)>24000 and buf:pages.append(buf);buf=''
   buf+=s
 if buf:pages.append(buf)
 print(f'CHUNK {c} DISPLAY PART {part}/{len(pages)}')
 print(pages[part-1])
def quote(tid,pid,quote,themes,kind,context,stage='unknown',speaker='parent_unspecified'):
 dest=R/'voice/oblique-deep-05.jsonl';old=[json.loads(s) for s in dest.read_text().splitlines()] if dest.exists() else []
 t=thread(tid);p=next(x for x in t['posts'] if x['post_id']==pid)
 norm=lambda s:' '.join(s.split())
 assert all(norm(x) in norm(p['body']) for x in quote.split(' […] ')),(tid,pid,quote)
 assert len(quote.replace(' […] ',' ').split())+sum(len(x['quote'].replace(' […] ',' ').split()) for x in old if x['post_id']==pid and x['thread_id']==tid)<=25
 assert len(context.split())<=25
 row=dict(id=f'odeep05-{len(old)+1:04}',source='mse-forum',url=p['url'],date=p['date'][:10],speaker=speaker,stage=stage,type=kind,themes=themes,quote=quote,context=context,raw_file=f'_raw/oblique-deep/mse-completion-v2/units/mse-{tid}.txt',source_class='forum_oblique',evidence_kind='original_thread_post',thread_id=tid,post_id=pid,author_id=p.get('author_id') or 'unknown',is_op=p['is_op'])
 with dest.open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 print(row['id'],tid,pid)
def note(tid,note,excluded_at=None,reason=None):
 t=thread(tid);ps=t['posts'];read=len(ps) if excluded_at is None else next(i for i,p in enumerate(ps,1) if p['post_id']==excluded_at)
 row=dict(thread_id=tid,status='full' if excluded_at is None else 'partial_safety_excluded',fully_read=excluded_at is None,posts_read=read,posts_total=len(ps),post_read_eligible=excluded_at is None,reason=reason or 'All visible posts and quoted context read; historical peer discussion.',raw_file=f'_raw/oblique-deep/mse-completion-v2/units/mse-{tid}.txt',quote_ids=[],reader_note=note)
 if excluded_at:row.update(safety_boundary_post_id=excluded_at,posts_read_before_boundary=read-1,posts_unread_after_boundary=len(ps)-read)
 dest=R/'scratchpad/odeep05/progress.jsonl'
 old=[json.loads(s) for s in dest.read_text().splitlines()] if dest.exists() else []
 assert tid not in [x['thread_id'] for x in old],tid
 with dest.open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 print('logged',tid,row['status'],read)
if __name__=='__main__':
 if sys.argv[1]=='show':show(int(sys.argv[2]),int(sys.argv[3]) if len(sys.argv)>3 else 1)
 else:
  for line in sys.stdin:
   if line.strip():
    x=json.loads(line);(quote if x.pop('action')=='quote' else note)(**x)
