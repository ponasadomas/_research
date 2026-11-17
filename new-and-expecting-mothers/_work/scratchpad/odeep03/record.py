import json,pathlib,re,sys
R=pathlib.Path('mamivio.com/research/global')
MAN=[json.loads(x) for x in (R/'_raw/oblique-deep/mse-completion-v2/batch-01/manifest.jsonl').read_text().splitlines()]
M={x['thread_id']:x for x in MAN}
V=R/'voice/oblique-deep-03.jsonl'; L=R/'sources/mse-completion-01-reading.jsonl'; N=R/'scratchpad/odeep03/thread-notes.jsonl'
def save(tid, selections, note, partial=None):
 tid=str(tid);m=M[tid];d=json.loads((R/m['thread_json']).read_text());existing=[json.loads(x) for x in V.read_text().splitlines()] if V.exists() else []
 ids=[]
 for post_id,quote,speaker,stage,typ,themes,context in selections:
  p=next(x for x in d['posts'] if x['post_id']==post_id)
  assert re.sub(r'\s+',' ',quote).strip() in re.sub(r'\s+',' ',p['body']).strip(),(tid,post_id,quote)
  assert len(context.split())<=25
  id=f'odeep03-{len(existing)+1:04d}';ids.append(id)
  e=dict(id=id,source='MoneySavingExpert',url=p['url'],date=p['date'],speaker=speaker,stage=stage,type=typ,themes=themes.split(','),quote=quote,context=context,raw_file=m['raw_file'],source_class='forum_oblique',evidence_kind='original_thread_post',thread_id=tid,post_id=post_id,is_op=p['is_op'],author_id=p.get('author_id') or 'unknown')
  existing.append(e)
 V.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in existing))
 prior=[json.loads(x) for x in L.read_text().splitlines()] if L.exists() else []
 assert tid not in [x['thread_id'] for x in prior]
 count=partial[0] if partial else len(d['posts'])
 e=dict(thread_id=tid,status='partial_safety_excluded' if partial else 'full',fully_read=not bool(partial),posts_read=count,posts_total=len(d['posts']),post_read_eligible=False if partial else True,reason=partial[1] if partial else 'Whole v2 unit read, including quoted context and every visible OP follow-up.',raw_file=m['raw_file'],quote_ids=ids)
 with L.open('a') as f:f.write(json.dumps(e,ensure_ascii=False)+'\n')
 with N.open('a') as f:f.write(json.dumps(dict(thread_id=tid,note=note,quote_ids=ids),ensure_ascii=False)+'\n')
 print(tid,ids)
