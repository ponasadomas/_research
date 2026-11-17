# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
import json,hashlib,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]; S=Path(__file__).resolve().parent
M=json.loads((R/'_raw/reddit-deep/aug-dec-2025-wave-v1/assignments/fullread-transfer-to-05-v1.json').read_text())
I={x['post_id']:x for x in map(json.loads,(R/'_raw/reddit-deep/aug-dec-2025-wave-v1/primary-index.jsonl').read_text().splitlines())}
L=R/'sources/reddit-augdec-05-reading.jsonl'
if sys.argv[1]=='freeze':
 assert not (S/'kept-chunks.json').exists()
 assert hashlib.sha256((R/M['source_kept_manifest']).read_bytes()).hexdigest()==M['source_manifest_sha256']
 assert M['donor_confirmed_unread'] is True and len(set(M['post_ids']))==354
 assert not set(M['post_ids'])&{json.loads(x)['post_id'] for x in (R/'sources/reddit-augdec-02-reading.jsonl').read_text().splitlines()}
 chunks=[]
 for c in M['chunks']:
  assert hashlib.sha256((R/c['file']).read_bytes()).hexdigest()==c['sha256']
  out='';number=int(Path(c['file']).stem)
  for pid in c['post_ids']:
   i=I[pid];p=R/i['raw_file'];assert hashlib.sha256(p.read_bytes()).hexdigest()==i['sha256']
   raw=p.read_text();body=raw[raw.index('=== COMPLETE ORIGINAL POST TITLE ==='):]
   out+='\n\n######## READUNIT '+pid+' | '+i['subreddit']+' | '+i['post_date']+' ########\n'+body
  f=f'kept-{number:03d}.txt';(S/f).write_text(out);chunks.append(dict(number=number,ids=c['post_ids'],file=f,sha256=hashlib.sha256(out.encode()).hexdigest()))
 (S/'kept-chunks.json').write_text(json.dumps(chunks,indent=2));print('frozen',len(chunks),'chunks',sum(len(c['ids']) for c in chunks),'units')
elif sys.argv[1]=='show':
 c=next(c for c in json.loads((S/'kept-chunks.json').read_text()) if c['number']==int(sys.argv[2]));print('READ CHUNK',sys.argv[2],len(c['ids']),'units',c['ids']);print((S/c['file']).read_text())
elif sys.argv[1]=='mark':
 c=next(c for c in json.loads((S/'kept-chunks.json').read_text()) if c['number']==int(sys.argv[2]));exceptions={}
 for line in sys.stdin.read().splitlines():
  if line.strip():pid,reason=line.split(' ',1);exceptions[pid]=reason
 assert set(exceptions)<=set(c['ids'])
 old={x['post_id'] for x in map(json.loads,L.read_text().splitlines())} if L.exists() else set();assert not old.intersection(c['ids'])
 with L.open('a') as f:
  for pid in c['ids']:
   i=I[pid];sha=hashlib.sha256((R/i['raw_file']).read_bytes()).hexdigest();assert sha==i['sha256']
   x=dict(post_id=pid,raw_file=i['raw_file'],post_body_read_complete=True,available_identifiable_OP_replies_read=i['OP_replies'],op_reply_ids_read=i['OP_comment_ids'],primary_unit_sha256=sha,status='read_pending_topic_review' if pid in exceptions else 'eligible',reason=exceptions.get(pid,'Complete native post and all available identifiable OP replies reviewed; bounded ordinary practical context, including clinical or safety instructions as attributed speech.'),quote_ids=[],reading_chunk=c['file'],fullreading_transfer=5)
   f.write(json.dumps(x,ensure_ascii=False)+'\n')
 print('recorded',len(c['ids']),'total',len(old)+len(c['ids']))
elif sys.argv[1]=='select':
 with (S/'selections.jsonl').open('a') as f:
  for line in sys.stdin:
   if line.strip():
    x=json.loads(line);assert x['post_id'] in set(M['post_ids']);assert len(x['context'].split())<=25;f.write(json.dumps(x,ensure_ascii=False)+'\n')
 print('saved selections')
