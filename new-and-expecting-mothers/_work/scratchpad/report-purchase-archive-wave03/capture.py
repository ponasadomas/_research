#!/usr/bin/env python3
"""New independent-publisher capture only; no old inventory writes."""
import collections,datetime,gzip,hashlib,io,json,re,subprocess,sys
from pathlib import Path
import requests
R=Path(__file__).resolve().parents[2]; S=Path(__file__).parent; W=R/'_raw/report-purchase-archive-wave03'
COMMIT='ea497c510aa68765c07ed744ec9f84d68bbedf7f'
FILES=[('sleeptrain','data/submissions/37/sleeptrain_submissions.jsonl.zst',55333761),('parentsnark','data/submissions/f0/parentsnark_submissions.jsonl.zst',435420)]
START=int(datetime.datetime(2025,7,1,tzinfo=datetime.timezone.utc).timestamp());END=int(datetime.datetime(2026,1,1,tzinfo=datetime.timezone.utc).timestamp())
PAY=re.compile(r'\b(?:paid|bought|purchas(?:e|ed|es|ing)|refund(?:s|ed|ing)?)\b',re.I)
ART=re.compile(r'\b(?:reports?|pdfs?|plans?|guides?|schedules?|customi[sz](?:ed|ation)|personali[sz](?:ed|ation)|tailored|huckleberry|baby\W*sleep\W*answers|taking\W*cara\W*babies|tcb|little\W*ones|moms?\W*on\W*call|moc|precious\W*little\W*sleep|pls|sleep\W*(?:sense|lady|science|wise|wave|consultant|coach)|happy\W*baby|hey\W*sleepy\W*baby|tinyhood|wee\W*bee\W*dreaming|wbd)\b',re.I)
def stamp(v):return datetime.datetime.fromtimestamp(int(v),datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def download():
 (W/'archive-files').mkdir(parents=True,exist_ok=True); assert not (W/'downloads.json').exists()
 saved=[]
 for community,path,expected in FILES:
  p=W/'archive-files'/Path(path).name; assert not p.exists(); u=f'https://huggingface.co/datasets/yikeee/reddit-subreddits25/resolve/{COMMIT}/{path}'
  response=requests.get(u,stream=True,timeout=(30,90))
  meta={'community':community,'source_url':u,'final_url':response.url,'status':response.status_code,'redirects':[{'status':h.status_code,'url':h.url} for h in response.history],'publisher_commit':COMMIT,'manifest_bytes':expected,'captured_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'headers':dict(response.headers)}
  if response.status_code!=200:
   saved.append(meta);dump(W/'downloads.json',saved);raise RuntimeError(f'Publisher denied or failed {community}: {response.status_code}; no alternate route attempted')
  with p.open('xb') as f:
   for b in response.iter_content(1024*1024):
    if b:f.write(b)
  meta.update(file=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p));saved.append(meta);dump(W/'downloads-progress.json',saved)
  assert meta['bytes']==expected,(community,meta['bytes'],expected)
  check=subprocess.run(['zstd','-q','-t',str(p)],capture_output=True,text=True);assert check.returncode==0,check.stderr
  print(json.dumps({k:meta[k] for k in ['community','status','bytes','sha256']}),flush=True)
 dump(W/'downloads.json',saved)
def build():
 assert not (W/'capture-summary.json').exists();(W/'window').mkdir(exist_ok=True);(W/'units').mkdir(exist_ok=True);(W/'cards').mkdir(exist_ok=True)
 idx=[];candidates=[];stats=[]
 for dl in json.loads((W/'downloads.json').read_text()):
  p=R/dl['file'];assert sha(p)==dl['sha256'];data=subprocess.Popen(['zstd','-q','-d','-c',str(p)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  full=0;windows=0;seen=set();wseen=set();lo=None;hi=None;last=None;inversions=0;months=collections.Counter();statuses=collections.Counter();wstatuses=collections.Counter();nativebytes=0
  wp=W/'window'/p.name.replace('.zst','.gz');assert not wp.exists()
  with gzip.open(wp,'wt',encoding='utf8') as out:
   for line in io.TextIOWrapper(data.stdout,encoding='utf8'):
    if not line.strip():continue
    n=json.loads(line);full+=1;pid=n['id'];assert pid not in seen;seen.add(pid);ts=int(n['created_utc']);assert n['subreddit'].lower()==dl['community'].lower()
    lo=ts if lo is None else min(lo,ts);hi=ts if hi is None else max(hi,ts);inversions+=int(last is not None and ts<last);last=ts;months[stamp(ts)[:7]]+=1
    body=n.get('selftext','');status='removed' if body=='[removed]' else 'deleted' if body=='[deleted]' else 'empty' if not body.strip() else 'present';statuses[status]+=1
    if not START<=ts<END:continue
    out.write(line);windows+=1;assert pid not in wseen;wseen.add(pid);wstatuses[status]+=1;nativebytes+=len(line.encode())
    meta={'post_id':pid,'subreddit':n['subreddit'],'date':stamp(ts),'url':'https://www.reddit.com'+n['permalink'],'title':n['title'],'body_status':status,'archive_file':dl['file'],'window_file':str(wp.relative_to(R)),'comment_source_available':False,'source_comment_file':None,'OP_replies':0,'OP_comment_ids':[],'archive_dataset':'yikeee/reddit-subreddits25','archive_commit':COMMIT,'native_author_sha256':hashlib.sha256(('report-purchase-wave03:'+str(n.get('author'))).encode()).hexdigest(),'native_body_sha256':hashlib.sha256(body.encode()).hexdigest(),'raw_file':None}
    if status=='present':
     unit=W/'units'/f'{n["subreddit"]}-{pid}.txt';assert not unit.exists();text='ARCHIVED ORIGINAL — ADDITIONAL COMMERCIAL COMMUNITIES\n'+json.dumps(meta,ensure_ascii=False,indent=2)+'\n\n=== COMPLETE ORIGINAL POST TITLE ===\n'+n['title']+'\n\n=== COMPLETE ORIGINAL POST BODY ===\n'+body+'\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===\nThe publisher comment file is unavailable; no live follow-up completeness is claimed.\n';unit.write_text(text);meta.update(raw_file=str(unit.relative_to(R)),sha256=sha(unit),utf8_bytes=unit.stat().st_size)
     combined=n['title']+'\n'+body;payments=list(PAY.finditer(combined));artifacts=list(ART.finditer(combined))
     if payments and artifacts:
      snippets=[]
      for match in payments+artifacts:
       snippet=combined[max(0,match.start()-85):min(len(combined),match.end()+100)].replace('\n',' ')
       if snippet not in snippets:snippets.append(snippet)
      card='ID '+pid+' | '+n['subreddit']+' | '+stamp(ts)+'\nTITLE '+n['title']+'\nOPENING '+body[:500].replace('\n',' ')+'\nPAYMENT_MATCHES '+json.dumps(sorted({m.group(0) for m in payments}),ensure_ascii=False)+'\nARTIFACT_MATCHES '+json.dumps(sorted({m.group(0) for m in artifacts}),ensure_ascii=False)+'\nMATCH_CONTEXTS\n'+'\n'.join(snippets)
      cardfile=W/'cards'/f'{pid}.txt';cardfile.write_text(card+'\n');candidates.append({**meta,'card_file':str(cardfile.relative_to(R)),'card_sha256':sha(cardfile),'payment_matches':sorted({m.group(0) for m in payments}),'artifact_matches':sorted({m.group(0) for m in artifacts})})
    idx.append(meta)
  err=data.stderr.read().decode();rc=data.wait();assert rc==0,err
  stats.append({'community':dl['community'],'compressed_file':dl['file'],'compressed_bytes':dl['bytes'],'sha256':dl['sha256'],'native_records_all':full,'json_errors':0,'missing_timestamps':0,'duplicate_ids':0,'timestamp_decreases':inversions,'min_date':stamp(lo),'max_date':stamp(hi),'months':dict(sorted(months.items())),'full_text_status':dict(statuses),'window_records':windows,'window_text_status':dict(wstatuses),'window_file':str(wp.relative_to(R)),'window_sha256':sha(wp),'window_native_utf8_bytes':nativebytes,'decompressed_complete_EOF':True})
  print(json.dumps({'community':dl['community'],'all_records':full,'window':windows,'text_status':dict(wstatuses)}),flush=True)
 (W/'native-index.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in idx));(W/'commercial-candidates.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in candidates));dump(W/'capture-summary.json',{'window_start':stamp(START),'window_end_exclusive':stamp(END),'files':stats,'window_records':len(idx),'readable_originals':sum(x['body_status']=='present' for x in idx),'commercial_candidates':len(candidates),'filter':'Exact saved PAY and ART regular expressions over same original title plus complete selftext; broad plans/guides/schedules retained for false-positive human review. Not a semantic keep or purchase proof.','payment_regex':PAY.pattern,'artifact_regex':ART.pattern,'comments_unavailable_for_both':True,'nine_community_inventory_membership':False});print('CANDIDATES',len(candidates),flush=True)
if __name__=='__main__':globals()[sys.argv[1]]()
