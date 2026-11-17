from pathlib import Path
import json,hashlib,collections,datetime,re
ROOT=Path(__file__).resolve().parents[2];S=ROOT/'scratchpad/reddit-country-B-03';PACKET=ROOT/'_raw/reddit-deep/next-july-country-B-v1/primary-v1';M=json.loads((S/'full-read-v2/manifest.json').read_text());IDX={x['post_id']:x for x in map(json.loads,(PACKET/'primary-index.jsonl').read_text().splitlines())};READ=ROOT/'sources/reddit-country-B-03-reading.jsonl';VOICE=ROOT/'voice/reddit-country-B-03.jsonl'
def records(p):return [json.loads(s) for s in p.read_text().splitlines()] if p.exists() else []
def body(tid):return (ROOT/IDX[tid]['raw_file']).read_text().split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0].strip()
def span(tid,start,end):
 b=body(tid);a=b.index(start);z=b.index(end,a)+len(end);return b[a:z]
def quote(tid,text,context,type,themes,stage='unknown',speaker='parent_unspecified',**extra):
 assert text in body(tid) and len(context.split())<=25
 x=IDX[tid];return dict(source='Reddit — r/'+x['subreddit']+' (publisher archive)',url=x['url'],date=x['post_date'][:10],speaker=speaker,stage=stage,type=type,themes=themes,quote=text,context=context,raw_file=x['raw_file'],source_class='reddit_archive',evidence_kind='archived_original',archive_dataset='yikeee/reddit-subreddits25',archive_commit='ea497c510aa68765c07ed744ec9f84d68bbedf7f',post_id=tid,read_scope='full_post_comment_source_unavailable',**extra)
def finish(view,exclusions=None,quotes=None,notes='',reasons=None):
 exclusions=exclusions or {};quotes=quotes or [];reasons=reasons or {};c=M['views'][view-1];assert c['view']==view;assert hashlib.sha256((ROOT/c['file']).read_bytes()).hexdigest()==c['sha256'];old=records(READ);oldq=records(VOICE);assert not set(c['post_ids'])&{x['post_id'] for x in old};assert set(exclusions)<=set(c['post_ids']) and set(reasons)<=set(c['post_ids']);newq=[]
 for q in quotes:
  assert q['post_id'] in c['post_ids'] and q['post_id'] not in exclusions
  newq.append(dict(id=f'rcb03-{len(oldq)+len(newq)+1:04d}',**q))
 rows=[]
 for tid in c['post_ids']:
  x=IDX[tid];assert x['comment_source_available'] is False and x['OP_replies']==0 and x['OP_comment_ids']==[];assert hashlib.sha256((ROOT/x['raw_file']).read_bytes()).hexdigest()==x['sha256'];rows.append(dict(post_id=tid,raw_file=x['raw_file'],post_body_read_complete=True,available_identifiable_OP_replies_read=0,op_reply_ids_read=[],primary_unit_sha256=x['sha256'],status='read_pending_topic_review' if tid in exclusions else 'eligible',reason=exclusions.get(tid,reasons.get(tid,'Full title and complete original body read; retained bounded ordinary parent/consumer context. Publisher comment source unavailable, no followups inferred.')),quote_ids=[q['id'] for q in newq if q['post_id']==tid],reading_view=view))
 for path,data in [(READ,rows),(VOICE,newq)]:
  with path.open('a') as f:
   for x in data:f.write(json.dumps(x,ensure_ascii=False)+'\n')
 with (S/'full-reading.jsonl').open('a') as f:f.write(json.dumps(dict(view=view,file=c['file'],sha256=c['sha256'],all_units_human_read=True,post_ids=c['post_ids'],notes=notes,utc=datetime.datetime.now(datetime.timezone.utc).isoformat()),ensure_ascii=False)+'\n')
 checkpoint=dict(assigned_cards=291,triaged_cards=291,kept_originals=203,full_originals_read=len(old+rows),remaining_kept=203-len(old+rows),OP_replies_read=0,comment_sources_unavailable=len(old+rows),statuses=dict(collections.Counter(x['status'] for x in old+rows)),quotes=len(oldq+newq),views_complete=view,views_total=len(M['views']),next_view=view+1 if view<len(M['views']) else None)
 (S/'checkpoint.json').write_text(json.dumps(checkpoint,indent=2)+'\n');print(json.dumps(checkpoint));print('QUOTES',[(x['id'],x['post_id']) for x in newq])
