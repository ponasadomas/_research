"""Record explicit completed human reads and selected exact excerpts, never classify sources."""
from pathlib import Path
import json,hashlib,datetime,collections,re
ROOT=Path(__file__).resolve().parents[2]
SCRATCH=ROOT/'scratchpad/reddit-augdec-03'
PACKET=ROOT/'_raw/reddit-deep/aug-dec-2025-wave-v1'
MANIFEST=json.loads((SCRATCH/'full-read-v1/manifest.json').read_text())
INDEX={x['post_id']:x for x in map(json.loads,(PACKET/'primary-index.jsonl').read_text().splitlines())}
READ=ROOT/'sources/reddit-augdec-03-reading.jsonl'
VOICE=ROOT/'voice/reddit-augdec-03.jsonl'
def records(path):return list(map(json.loads,path.read_text().splitlines())) if path.exists() else []
def original_body(post_id):
 s=(ROOT/INDEX[post_id]['raw_file']).read_text()
 return s.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0].strip()
def span(post_id,start,end):
 """Copy a manually selected exact source span without retyping its punctuation/spacing."""
 b=original_body(post_id);a=b.index(start);z=b.index(end,a)+len(end);return b[a:z]
def quote(post_id,text,context,type,themes,stage='unknown',speaker='parent_unspecified',**extra):
 assert text in original_body(post_id),'Must copy exact original post-body substring'
 assert len(context.split())<=25
 x=INDEX[post_id]
 return dict(source='Reddit — r/'+x['subreddit']+' (publisher archive)',url=x['url'],date=x['post_date'][:10],speaker=speaker,stage=stage,type=type,themes=themes,quote=text,context=context,raw_file=x['raw_file'],source_class='reddit_archive',evidence_kind='archived_original',archive_dataset='yikeee/reddit-subreddits25',archive_commit='ea497c510aa68765c07ed744ec9f84d68bbedf7f',post_id=post_id,read_scope='full_post_and_available_identifiable_OP_replies' if x['comment_source_available'] else 'full_post_comment_source_unavailable',**extra)
def comment_quote(post_id,comment_id,text,context,type,themes,stage='unknown',speaker='parent_unspecified',**extra):
 x=INDEX[post_id];assert comment_id in x['OP_comment_ids']
 s=(ROOT/x['raw_file']).read_text();matched=None
 for unit in s.split('\n--- OP REPLY ---\n')[1:]:
  header,body=unit.strip().split('\n',1);meta=json.loads(header)
  if meta['comment_id']==comment_id:matched=(meta,body);break
 assert matched and text in matched[1]
 meta,body=matched;assert len(context.split())<=25
 meta['url']=x['url'].rstrip('/')+'/'+comment_id+'/'
 return dict(source='Reddit — r/'+x['subreddit']+' (publisher archive, OP reply)',url=meta['url'],date=meta['date'][:10],speaker=speaker,stage=stage,type=type,themes=themes,quote=text,context=context,raw_file=x['raw_file'],source_class='reddit_archive',evidence_kind='archived_original',archive_dataset='yikeee/reddit-subreddits25',archive_commit='ea497c510aa68765c07ed744ec9f84d68bbedf7f',post_id=post_id,comment_id=comment_id,read_scope='full_post_and_available_identifiable_OP_replies',**extra)
def finish(chunk,exclusions=None,quotes=None,notes='',reasons=None):
 """Invoke only after every displayed unit in this exact chunk has actually been read."""
 exclusions=exclusions or {};quotes=quotes or [];reasons=reasons or {}
 c=MANIFEST['chunks'][chunk-1];assert c['chunk']==chunk
 assert hashlib.sha256((ROOT/c['file']).read_bytes()).hexdigest()==c['sha256']
 old=records(READ);assert not {x['post_id'] for x in old}&set(c['post_ids'])
 assert set(exclusions)<=set(c['post_ids']) and set(reasons)<=set(c['post_ids'])
 oldq=records(VOICE);newq=[]
 for q in quotes:
  assert q['post_id'] in c['post_ids'] and q['post_id'] not in exclusions
  q={'id':f'rad03-{len(oldq)+len(newq)+1:04d}',**q};newq.append(q)
 rows=[]
 for u in c['units']:
  tid=u['post_id'];x=INDEX[tid];assert hashlib.sha256((ROOT/x['raw_file']).read_bytes()).hexdigest()==u['sha256']
  rows.append(dict(post_id=tid,raw_file=x['raw_file'],post_body_read_complete=True,available_identifiable_OP_replies_read=x['OP_replies'],op_reply_ids_read=x['OP_comment_ids'],primary_unit_sha256=x['sha256'],status='read_pending_topic_review' if tid in exclusions else 'eligible',reason=exclusions.get(tid,reasons.get(tid,'Full title and original body plus every available identifiable OP reply read; retained as bounded ordinary consumer or household context, without endorsing health or safety instructions.')),quote_ids=[q['id'] for q in newq if q['post_id']==tid],reading_chunk=chunk))
 with VOICE.open('a') as f:
  for q in newq:f.write(json.dumps(q,ensure_ascii=False)+'\n')
 with READ.open('a') as f:
  for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 with (SCRATCH/'full-reading-chunks.jsonl').open('a') as f:f.write(json.dumps(dict(chunk=chunk,file=c['file'],sha256=c['sha256'],all_units_fully_read=True,post_ids=c['post_ids'],notes=notes,read_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()),ensure_ascii=False)+'\n')
 checkpoint=dict(assigned_cards=1585,assigned_card_files=27,cards_fully_read_and_triaged=1585,triage_kept=1121,triage_dropped=464,kept_full_originals_read=len(old)+len(rows),remaining_kept=len(MANIFEST['chunks']) and 1121-len(old)-len(rows),OP_replies_read=sum(x['available_identifiable_OP_replies_read'] for x in old+rows),statuses=dict(collections.Counter(x['status'] for x in old+rows)),quotes=len(oldq)+len(newq),completed_reading_chunks=chunk,total_reading_chunks=len(MANIFEST['chunks']),next_reading_chunk=chunk+1)
 (SCRATCH/'checkpoint.json').write_text(json.dumps(checkpoint,indent=2)+'\n')
 p=ROOT/'sources/reddit-augdec-03.md';s=p.read_text();s=re.sub(r'Current exact checkpoint: .*?\n',lambda _: 'Current exact checkpoint: '+json.dumps(checkpoint)+'\n',s,count=1);p.write_text(s)
 print(json.dumps(checkpoint));print('NEW QUOTES',[(q['id'],q['post_id']) for q in newq])
