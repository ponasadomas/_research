from pathlib import Path
import json,csv,gzip,hashlib,datetime,collections,re
R=Path(__file__).resolve().parents[2];P=Path(__file__).resolve().parent;RAW=R/'_raw/reddit-deep/aug-dec-2025-wave-v1'
jl=lambda p:[json.loads(x) for x in p.read_text().splitlines() if x.strip()]
triage=list(csv.DictReader((R/'_raw/reddit-deep/triage/augdec-04.tsv').open(),delimiter='\t'))
assigned=json.loads((RAW/'assignments/batch-04.json').read_text());parts=json.loads((RAW/'assignments/root04-fullread-partitions-v1.json').read_text());own=json.loads((P/'full-read-v1/manifest.json').read_text())
assert len(triage)==len({x['post_id'] for x in triage})==620
assert {x['post_id'] for x in triage}==set(assigned['post_ids'])
kept={x['post_id'] for x in triage if x['label']!='drop'}
assert len(kept)==432 and set.union(*(set(x['post_ids']) for x in parts['partitions']))==kept
assert sum(len(x['post_ids']) for x in parts['partitions'])==len(kept)
read=jl(R/'sources/reddit-augdec-04-reading.jsonl');voice=jl(R/'voice/reddit-augdec-04.jsonl')
assert len(read)==len({x['post_id'] for x in read})==60 and {x['post_id'] for x in read}==set(own['post_ids'])
index={x['post_id']:x for x in jl(RAW/'primary-index.jsonl')};native={}
for f in {index[x['post_id']]['source_post_file'] for x in read}:
 with gzip.open(R/f,'rt') as stream:
  for line in stream:
   x=json.loads(line)
   if x['id'] in set(own['post_ids']):native[x['id']]=x
ledger={x['post_id']:x for x in read}
for x in read:
 pid=x['post_id'];i=index[pid];p=R/x['raw_file'];text=p.read_text();body=text.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0]
 assert body==native[pid]['selftext'],pid
 assert hashlib.sha256(p.read_bytes()).hexdigest()==x['primary_unit_sha256']==i['sha256']
 assert x['post_body_read_complete'] is True and i['comment_source_available'] is False
 assert x['op_reply_ids_read']==[] and x['available_identifiable_OP_replies_read']==i['OP_replies']==0
 assert x['quote_ids']==[q['id'] for q in voice if q['post_id']==pid]
for chunk in own['chunks']:assert hashlib.sha256((R/chunk['file']).read_bytes()).hexdigest()==chunk['sha256']
for q in voice:
 n=native[q['post_id']];assert q['quote'] in n['selftext'],q['id'];assert q['date']==datetime.datetime.fromtimestamp(float(n['created_utc']),datetime.timezone.utc).date().isoformat()
 assert q['url']=='https://www.reddit.com'+n['permalink'];assert len(q['context'].split())<=25
 assert q['raw_file']==index[q['post_id']]['raw_file'] and ledger[q['post_id']]['status']=='eligible'
 assert q['read_scope']=='full_post_comment_source_unavailable'
allq=[q for p in (R/'voice').glob('*.jsonl') for q in jl(p)];allids=collections.Counter(q['id'] for q in allq)
assert all(allids[q['id']]==1 for q in voice)
report=dict(reader='root04',triage_cards=620,triage_kept=432,triage_dropped=188,full_read_own=60,transferred_06=186,transferred_07_original=186,transferred_07=126,transferred_08=60,OP_replies_read=0,auxiliary_comments_read=0,statuses=dict(collections.Counter(x['status'] for x in read)),quotes=len(voice),quoted_post_ids=len({q['post_id'] for q in voice}),duplicate_groups_human_reviewed=3,voice_sha256=hashlib.sha256((R/'voice/reddit-augdec-04.jsonl').read_bytes()).hexdigest(),native_fullbody_date_permalink_attribution_hash_idset_checks='passed',failed=0)
(R/'sources/reddit-augdec-04-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
