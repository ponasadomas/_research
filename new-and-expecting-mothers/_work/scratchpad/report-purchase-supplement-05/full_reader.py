from pathlib import Path
import json,hashlib,collections,datetime
R=Path(__file__).resolve().parents[2];S=R/'scratchpad/report-purchase-supplement-05';M=json.loads((S/'full-read-v1/manifest.json').read_text());A=json.loads((R/'_raw/report-purchase-archive-wave03/supplement-v1/assignments/reader-05.json').read_text());IDX={x['post_id']:x for x in map(json.loads,(R/A['primary_index']).read_text().splitlines())};READ=R/'sources/report-purchase-supplement-05-reading.jsonl';VOICE=R/'voice/report-purchase-supplement-05.jsonl';PUR=R/'sources/report-purchase-supplement-05-purchase-evidence.jsonl'
def records(p):return [json.loads(s) for s in p.read_text().splitlines()] if p.exists() else []
def body(tid):return (R/IDX[tid]['raw_file']).read_text().split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0].strip()
def span(tid,start,end):
 b=body(tid);a=b.index(start);z=b.index(end,a)+len(end);return b[a:z]
def quote(tid,text,context,type,themes,stage='unknown',speaker='parent_unspecified',**extra):
 assert text in body(tid) and len(context.split())<=25
 x=IDX[tid];return dict(source='Reddit — r/'+x['subreddit']+' (publisher archive)',url=x['url'],date=x['date'][:10],speaker=speaker,stage=stage,type=type,themes=themes,quote=text,context=context,raw_file=x['raw_file'],source_class='reddit_archive',evidence_kind='archived_original',archive_dataset='yikeee/reddit-subreddits25',archive_commit='ea497c510aa68765c07ed744ec9f84d68bbedf7f',post_id=tid,read_scope='full_post_comment_source_unavailable',**extra)
def finish(view,decisions,quotes=None,notes=''):
 quotes=quotes or [];c=M['views'][view-1];assert c['view']==view;assert hashlib.sha256((R/c['file']).read_bytes()).hexdigest()==c['sha256'];assert set(decisions)==set(c['post_ids']);old=records(READ);oldq=records(VOICE);assert not set(c['post_ids'])&{x['post_id'] for x in old};newq=[]
 for q in quotes:
  assert q['post_id'] in c['post_ids'] and decisions[q['post_id']]['status']=='eligible'
  newq.append(dict(id=f'rpa05-{len(oldq)+len(newq)+1:04d}',**q))
 rows=[];purchases=[]
 for tid in c['post_ids']:
  x=IDX[tid];d=decisions[tid];assert d['status'] in ['eligible','excluded_after_read'] and d['reason'] and d['classification'];assert x['comment_source_available'] is False and x['OP_replies']==0 and x['OP_comment_ids']==[];assert hashlib.sha256((R/x['raw_file']).read_bytes()).hexdigest()==x['sha256'];rows.append(dict(post_id=tid,raw_file=x['raw_file'],post_body_read_complete=True,available_identifiable_OP_replies_read=0,op_reply_ids_read=[],primary_unit_sha256=x['sha256'],status=d['status'],reason=d['reason'],purchase_classification=d['classification'],quote_ids=[q['id'] for q in newq if q['post_id']==tid],reading_view=view));purchases.append(dict(post_id=tid,raw_file=x['raw_file'],classification=d['classification'],actual_standalone_custom_report_purchase=False,assessment=d['reason'],**d.get('purchase',{})))
 for path,data in [(READ,rows),(VOICE,newq),(PUR,purchases)]:
  with path.open('a') as f:
   for x in data:f.write(json.dumps(x,ensure_ascii=False)+'\n')
 with (S/'full-reading.jsonl').open('a') as f:f.write(json.dumps(dict(view=view,file=c['file'],sha256=c['sha256'],all_units_human_read=True,post_ids=c['post_ids'],notes=notes,utc=datetime.datetime.now(datetime.timezone.utc).isoformat()),ensure_ascii=False)+'\n')
 cp=dict(assigned_cards=121,triaged_cards=121,kept_originals=43,full_originals_read=len(old+rows),remaining_kept=43-len(old+rows),OP_replies_read=0,statuses=dict(collections.Counter(x['status'] for x in old+rows)),quotes=len(oldq+newq),views_complete=view,views_total=len(M['views']));(S/'checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n');print(json.dumps(cp));print('QUOTES',[(q['id'],q['post_id']) for q in newq])
def d(classification,reason,excluded=False,**purchase):return dict(status='excluded_after_read' if excluded else 'eligible',classification=classification,reason=reason,purchase=purchase)
