# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
import json,csv,hashlib,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]; S=Path(__file__).resolve().parent
I={x['post_id']:x for x in map(json.loads,(R/'_raw/reddit-deep/aug-dec-2025-wave-v1/primary-index.jsonl').read_text().splitlines())}
T=list(csv.DictReader((R/'_raw/reddit-deep/triage/augdec-02.tsv').open(),delimiter='\t'))
L=R/'sources/reddit-augdec-02-reading.jsonl'
if sys.argv[1]=='freeze':
 assert not (S/'kept-chunks.json').exists()
 chunks=[]; ids=[]; text=''
 for t in T:
  if t['label']=='drop':continue
  i=I[t['post_id']]; raw=(R/i['raw_file']).read_text(); body=raw[raw.index('=== COMPLETE ORIGINAL POST TITLE ==='):]
  unit='\n\n######## READUNIT '+i['post_id']+' | '+i['subreddit']+' | '+i['post_date']+' ########\n'+body
  if len((text+unit).encode())>33000 and ids:
   chunks.append({'ids':ids,'file':f'kept-{len(chunks)+1:03d}.txt'}); (S/chunks[-1]['file']).write_text(text); text='';ids=[]
  text+=unit;ids.append(i['post_id'])
 if ids: chunks.append({'ids':ids,'file':f'kept-{len(chunks)+1:03d}.txt'});(S/chunks[-1]['file']).write_text(text)
 (S/'kept-chunks.json').write_text(json.dumps(chunks,indent=2));print('frozen',len(chunks),'chunks',sum(len(c['ids']) for c in chunks),'units')
elif sys.argv[1]=='show':
 c=json.loads((S/'kept-chunks.json').read_text())[int(sys.argv[2])-1]; print('READ CHUNK',sys.argv[2],len(c['ids']),'units',c['ids']);print((S/c['file']).read_text())
elif sys.argv[1]=='mark':
 c=json.loads((S/'kept-chunks.json').read_text())[int(sys.argv[2])-1]; exceptions={}
 for line in sys.stdin.read().splitlines():
  if not line.strip():continue
  pid,reason=line.split(' ',1);exceptions[pid]=reason
 assert set(exceptions)<=set(c['ids'])
 old={x['post_id'] for x in map(json.loads,L.read_text().splitlines())} if L.exists() else set();assert not old.intersection(c['ids'])
 with L.open('a') as f:
  for pid in c['ids']:
   i=I[pid];sha=hashlib.sha256((R/i['raw_file']).read_bytes()).hexdigest();assert sha==i['sha256']
   x=dict(post_id=pid,raw_file=i['raw_file'],post_body_read_complete=True,available_identifiable_OP_replies_read=i['OP_replies'],op_reply_ids_read=i['OP_comment_ids'],primary_unit_sha256=sha,status='read_pending_topic_review' if pid in exceptions else 'eligible',reason=exceptions.get(pid,'Complete native post and all available identifiable OP replies reviewed; ordinary practical task, with clinical and safety instructions retained as attributed evidence.'),quote_ids=[],reading_chunk=c['file'])
   f.write(json.dumps(x,ensure_ascii=False)+'\n')
 print('recorded',len(c['ids']),'total',len(old)+len(c['ids']))
elif sys.argv[1]=='select':
 with (S/'selections.jsonl').open('a') as f:
  for line in sys.stdin:
   if line.strip():
    x=json.loads(line);assert x['post_id'] in I;assert len(x['context'].split())<=25;f.write(json.dumps(x,ensure_ascii=False)+'\n')
 print('saved selections')
