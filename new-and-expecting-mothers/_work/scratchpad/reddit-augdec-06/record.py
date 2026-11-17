# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
import json,hashlib,sys
from pathlib import Path
S=Path(__file__).resolve().parent;R=S.parents[1];M=json.loads((S/'full-read-v1/manifest.json').read_text());I={x['post_id']:x for x in map(json.loads,(R/'_raw/reddit-deep/aug-dec-2025-wave-v1/primary-index.jsonl').read_text().splitlines())};c=next(c for c in M['chunks'] if c['chunk']==int(sys.argv[1]));a=json.load(sys.stdin);ex=a.get('excluded',{});assert set(ex)<=set(c['post_ids']);p=R/'sources/reddit-augdec-06-reading.jsonl';old={x['post_id'] for x in map(json.loads,p.read_text().splitlines())} if p.exists() else set();assert not old&set(c['post_ids'])
with p.open('a') as f:
 for pid in c['post_ids']:
  i=I[pid];h=hashlib.sha256((R/i['raw_file']).read_bytes()).hexdigest();assert h==i['sha256']
  x=dict(post_id=pid,raw_file=i['raw_file'],post_body_read_complete=True,available_identifiable_OP_replies_read=i['OP_replies'],op_reply_ids_read=i['OP_comment_ids'],primary_unit_sha256=h,status='read_pending_topic_review' if pid in ex else 'eligible',reason=ex.get(pid,'Entire saved original read; bounded ordinary practical context, including clinical or unsafe peer instructions as attributed speech.'),quote_ids=[],reading_chunk=c['file'],fullreading_transfer=6)
  f.write(json.dumps(x,ensure_ascii=False)+'\n')
with (S/'selections.jsonl').open('a') as f:
 for x in a.get('selections',[]):
  assert x['post_id'] in c['post_ids'];assert len(x['context'].split())<=25;f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('Recorded',len(c['post_ids']),'total',len(old)+len(c['post_ids']))
