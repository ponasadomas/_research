# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
import json,hashlib,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]; S=Path(__file__).resolve().parent
M=json.loads((S/'full-read-v1/manifest.json').read_text())
I={x['post_id']:x for x in map(json.loads,(R/'_raw/reddit-deep/aug-dec-2025-wave-v1/primary-index.jsonl').read_text().splitlines())}
L=R/'sources/reddit-augdec-06-reading.jsonl'
if sys.argv[1]=='show':
 c=next(c for c in M['chunks'] if c['chunk']==int(sys.argv[2]));print('READ CHUNK',sys.argv[2],len(c['post_ids']),'units',c['post_ids']);print((R/c['file']).read_text())
elif sys.argv[1]=='mark':
 c=next(c for c in M['chunks'] if c['chunk']==int(sys.argv[2]));exceptions={}
 for line in sys.stdin.read().splitlines():
  if line.strip():pid,reason=line.split(' ',1);exceptions[pid]=reason
 assert set(exceptions)<=set(c['post_ids'])
 old={x['post_id'] for x in map(json.loads,L.read_text().splitlines())} if L.exists() else set();assert not old.intersection(c['post_ids'])
 with L.open('a') as f:
  for pid in c['post_ids']:
   i=I[pid];sha=hashlib.sha256((R/i['raw_file']).read_bytes()).hexdigest();assert sha==i['sha256']
   x=dict(post_id=pid,raw_file=i['raw_file'],post_body_read_complete=True,available_identifiable_OP_replies_read=i['OP_replies'],op_reply_ids_read=i['OP_comment_ids'],primary_unit_sha256=sha,status='read_pending_topic_review' if pid in exceptions else 'eligible',reason=exceptions.get(pid,'Complete native post and all available identifiable OP replies reviewed; bounded ordinary practical context, including clinical or safety instructions as attributed speech.'),quote_ids=[],reading_chunk=c['file'],fullreading_transfer=6)
   f.write(json.dumps(x,ensure_ascii=False)+'\n')
 print('recorded',len(c['post_ids']),'total',len(old)+len(c['post_ids']))
elif sys.argv[1]=='select':
 with (S/'selections.jsonl').open('a') as f:
  for line in sys.stdin:
   if line.strip():
    x=json.loads(line);assert x['post_id'] in set(M['post_ids']);assert len(x['context'].split())<=25;f.write(json.dumps(x,ensure_ascii=False)+'\n')
 print('saved selections')
