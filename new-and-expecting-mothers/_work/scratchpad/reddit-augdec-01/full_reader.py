import collections,csv,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; WORK=Path(__file__).parent
WAVE=ROOT/'_raw/reddit-deep/aug-dec-2025-wave-v1'
INDEX={x['post_id']:x for x in map(json.loads,(WAVE/'primary-index.jsonl').read_text().splitlines())}
MAN=WORK/'kept-reading-manifest.json'
LED=ROOT/'sources/reddit-augdec-01-reading.jsonl'; VOICE=ROOT/'voice/reddit-augdec-01.jsonl'
def jl(p):return [json.loads(x) for x in p.read_text().splitlines() if x.strip()] if p.exists() else []
def build():
 assert not MAN.exists()
 rows=list(csv.DictReader((ROOT/'_raw/reddit-deep/triage/augdec-01.tsv').open(),delimiter='\t')); keep=[x['post_id'] for x in rows if x['label'].startswith('keep_')];keep.remove('1n1yo2d'); keep.insert(0,'1n1yo2d')
 flags=jl(WAVE/'exact-body-duplicate-flags.jsonl'); byid=collections.defaultdict(list)
 for g in flags:
  for a in g['records']:byid[a['post_id']].append(g['records'])
 chunks=[];units=[];parts=[];ids=[];size=0
 out=WORK/'kept-chunks';out.mkdir(exist_ok=True)
 def flush():
  nonlocal parts,ids,size
  if not ids:return
  p=out/f'{len(chunks)+1:03d}.txt';body='\n\n'.join(parts)+'\n';p.write_text(body);chunks.append({'file':str(p.relative_to(ROOT)),'post_ids':ids,'utf8_bytes':len(body.encode()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()});parts=[];ids=[];size=0
 for pid in keep:
  u=INDEX[pid];p=ROOT/u['raw_file'];t=p.read_text();content=t[t.index('=== COMPLETE ORIGINAL POST TITLE ==='):];meta={k:u[k] for k in ['post_id','subreddit','url','post_date','raw_file','comment_source_available','OP_replies','OP_comment_ids']}; view='PRIMARY UNIT '+json.dumps(meta,ensure_ascii=False)+'\n'+('EXACT BODY REPEAT FLAGS '+json.dumps(byid[pid],ensure_ascii=False)+'\n' if byid[pid] else '')+content
  if size+len(view.encode())>35000:flush()
  parts.append(view);ids.append(pid);size+=len(view.encode());units.append(u)
 flush();MAN.write_text(json.dumps({'scope':'all 1646 human keeps from 2199 assigned cards; complete title/body and all available identifiable OP replies','units':units,'chunks':chunks},ensure_ascii=False,indent=2)+'\n'); print({'units':len(units),'chunks':len(chunks),'view_bytes':sum(x['utf8_bytes'] for x in chunks)})
def view(n):
 assert 1 <= n <= 72, 'Own frozen scope is chunks 001-072; tail transferred to reader 05'
 c=json.loads(MAN.read_text())['chunks'][n-1];p=ROOT/c['file'];assert hashlib.sha256(p.read_bytes()).hexdigest()==c['sha256'];print(p.read_text(),end='')
def save(n,decisions):
 assert 1 <= n <= 72, 'Own frozen scope is chunks 001-072; tail transferred to reader 05'
 m=json.loads(MAN.read_text());c=m['chunks'][n-1]; ds=[]
 for l in decisions.strip().splitlines():
  pid,status,reason=l.split('|',2);assert status in {'e','x'};ds.append((pid,status,reason))
 assert [d[0] for d in ds]==c['post_ids'],('decision mismatch',n,[d[0] for d in ds],c['post_ids'])
 prev=jl(LED);assert not {x['post_id'] for x in prev}&set(c['post_ids'])
 qs=jl(VOICE)
 with LED.open('a') as f:
  for pid,status,reason in ds:
   u=INDEX[pid];p=ROOT/u['raw_file'];assert hashlib.sha256(p.read_bytes()).hexdigest()==u['sha256']
   row={'post_id':pid,'raw_file':u['raw_file'],'post_body_read_complete':True,'available_identifiable_OP_replies_read':u['OP_replies'],'op_reply_ids_read':u['OP_comment_ids'],'primary_unit_sha256':u['sha256'],'status':'eligible' if status=='e' else 'read_pending_topic_review','reason':reason,'quote_ids':[q['id'] for q in qs if q['post_id']==pid],'reading_chunk':c['file']};f.write(json.dumps(row,ensure_ascii=False)+'\n')
 now=jl(LED);(WORK/'reading-progress.json').write_text(json.dumps({'completed_units':len(now),'OP_replies_read':sum(x['available_identifiable_OP_replies_read'] for x in now),'statuses':dict(collections.Counter(x['status'] for x in now)),'last_chunk':n},indent=2)+'\n');print({'saved_chunk':n,'units':len(ds),'completed_units':len(now),'total':sum(len(c['post_ids']) for c in m['chunks'][:72])})
def quotes(specs):
 prev=jl(VOICE)
 with VOICE.open('a') as f:
  for s in specs:
   u=INDEX[s['post_id']];s={'id':f'rad01-{len(prev)+1:04d}','source':'Reddit r/'+u['subreddit']+' — August–December continuation','url':u['url'],'date':u['post_date'],'speaker':'parent_unspecified','stage':'unknown',**s,'raw_file':u['raw_file'],'source_class':'reddit_archive','evidence_kind':'archived_original','archive_dataset':'yikeee/reddit-subreddits25','archive_commit':'ea497c510aa68765c07ed744ec9f84d68bbedf7f','read_scope':'full_post_and_available_identifiable_OP_replies' if u['comment_source_available'] else 'full_post_comment_source_unavailable'}
   assert len(s['context'].split())<=25;assert s['quote'] in (ROOT/u['raw_file']).read_text();f.write(json.dumps(s,ensure_ascii=False)+'\n');prev.append(s); print(s['id'],s['post_id'])
if __name__=='__main__':
 cmd=sys.argv[1]
 if cmd=='build':build()
 if cmd=='view':view(int(sys.argv[2]))
 if cmd=='save':save(int(sys.argv[2]),sys.stdin.read())
 if cmd=='quotes':quotes(json.load(sys.stdin))
