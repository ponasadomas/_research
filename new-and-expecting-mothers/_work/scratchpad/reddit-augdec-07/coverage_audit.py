"""Check explicit final scope/duplicate coverage; never classify or substitute for human reading."""
import sys,json,gzip,hashlib,re,collections,datetime
from pathlib import Path
from full_reader import ROOT,SCRATCH,PACKET,INDEX,MANIFEST,READ,VOICE,records,original_body
errors=[]
def check(ok,label):
 if not ok:errors.append(label)
cov=json.loads((SCRATCH/'final-coverage.json').read_text());read=records(READ);voice=records(VOICE);aux=records(ROOT/'sources/reddit-augdec-07-auxiliary-read.jsonl');inspections=records(ROOT/'sources/reddit-augdec-07-duplicate-inspections.jsonl');dup=json.loads((SCRATCH/'duplicate-review.json').read_text());checkpoint=json.loads((SCRATCH/'checkpoint.json').read_text())
assigned=set(MANIFEST['post_ids']);old=json.loads((SCRATCH/'full-read-v1/manifest.json').read_text());transferred=set(old['post_ids'])-assigned
check(len(assigned)==126 and len(transferred)==60,'126 own /60 transferred')
check(set(cov['assigned_original_ids'])==set(cov['full_original_ids'])==assigned,'Exact final coverage original set')
check(not cov['partial_original_ids'] and not cov['unread_assigned_original_ids'] and not cov['unread_available_OP_reply_ids'],'No assigned partial/unread units')
check(set(cov['transferred_to08_original_ids'])==transferred,'Exact transferred metadata IDs')
check(not assigned&transferred and set(r['post_id'] for r in read)==assigned,'Read set excludes transferred units')
expectedop=[c for r in read for c in INDEX[r['post_id']]['OP_comment_ids']]
check(cov['available_OP_reply_ids_read']==expectedop and len(expectedop)==338 and len(set(expectedop))==338,'Exact338 OP replies')
auxids={x['comment_id'] for x in aux};check(len(auxids)==len(aux)==7 and set(cov['auxiliary_non_OP_comment_ids_read'])==auxids,'Exact7 auxiliary comments')
expectednonop={r['post_id']:[c for c in INDEX[r['post_id']]['non_OP_comment_ids'] if c not in auxids] for r in read if INDEX[r['post_id']]['non_OP_comment_ids']}
check(cov['available_non_OP_comment_ids_unread_by_post']==expectednonop and sum(map(len,expectednonop.values()))==2053,'Exact2053 unread assigned nonOP comments')
missing={r['post_id'] for r in read if not INDEX[r['post_id']]['comment_source_available']}
check(set(cov['comment_source_unavailable_post_ids'])==missing and len(missing)==37,'Exact37 comment-source-unavailable originals')
extraids={x['post_id'] for x in inspections};check(extraids=={'1pyzonc','1nfmfl0'} and not extraids&assigned,'Two duplicate-only extra inspections')
check(cov['duplicate_audit_inspection_non_OP_comment_ids_unread_by_post']=={t:INDEX[t]['non_OP_comment_ids'] for t in extraids},'Exact outside-inspection nonOP IDs')
check(cov['duplicate_audit_inspection_comment_source_unavailable_post_ids']==['1pyzonc'],'Outside-inspection unavailable comment source')
check(len(INDEX['1nfmfl0']['non_OP_comment_ids'])==16,'16 outside-inspection nonOP comments remain unread')
native={}
for name in {INDEX[t]['source_post_file'] for t in assigned|extraids}:
 with gzip.open(ROOT/name,'rt') as f:
  for s in f:
   p=json.loads(s)
   if p.get('id') in assigned|extraids:native[p['id']]=p
for r in inspections:
 t=r['post_id'];x=INDEX[t]
 check(r['primary_unit_sha256']==x['sha256']==hashlib.sha256((ROOT/r['raw_file']).read_bytes()).hexdigest(),'Extra-inspection immutable unit '+t)
 check(r['post_body_read_complete'] is True and original_body(t)==native[t]['selftext'].strip(),'Extra-inspection complete native body '+t)
 check(r['available_identifiable_OP_replies_read']==x['OP_replies']==0 and r['op_reply_ids_read']==x['OP_comment_ids']==[],'Extra-inspection all available OP replies0 '+t)
 check(r['comment_source_available']==x['comment_source_available'] and not r['quote_ids'],'Extra-inspection scope '+t)
externalOP=[]
with gzip.open(ROOT/INDEX['1nfmfl0']['source_comment_file'],'rt') as f:
 for s in f:
  c=json.loads(s)
  if c.get('link_id')=='t3_1nfmfl0' and c.get('author')==native['1nfmfl0'].get('author') and c.get('author') not in [None,'[deleted]','[removed]']:externalOP.append(c['id'])
check(externalOP==[],'Native 1nfmfl0 identifiable OP availability0')
flags=records(PACKET/'exact-body-duplicate-flags.jsonl');touching=[(i,g) for i,g in enumerate(flags,1) if {x['post_id'] for x in g['records']}&assigned]
check([i for i,g in touching]==[87,99] and dup['machine_flags_touching_assigned']==2,'All2 touching duplicate flags reviewed')
for g in dup['groups']:
 a,b=g['post_ids'];rep=g['representative_post_id']
 check(original_body(a)==original_body(b),'Duplicate native full bodies agree '+str(g['duplicate_body_group']))
 check(hashlib.sha256(original_body(a).encode()).hexdigest()==g['body_sha256'],'Duplicate comparison body hash')
 check(rep==min([a,b],key=lambda t:float(native[t]['created_utc'])),'Duplicate earliest timestamp representative')
 for q in voice:
  if q['post_id'] in [a,b]:check(q['post_id']==rep and q.get('duplicate_body_group')==g['duplicate_body_group'] and q.get('duplicate_representative_post_id')==rep and q.get('independent_body_representative') is True,'Duplicate quoted representative metadata')
check(checkpoint['scope_complete'] is True and checkpoint['next_reading_chunk'] is None and checkpoint['remaining_kept']==0,'Complete checkpoint has no next transferred view')
notes=(ROOT/'synthesis/reader-notes-reddit-augdec-07.md').read_text();refs=set(re.findall(r'rad07-\d{4}',notes));check(refs<={q['id'] for q in voice},'Reader notes cite only existing own quote IDs')
result=dict(complete=True,errors=errors,assigned_originals=126,assigned_full_originals=126,assigned_identifiable_OP_replies_read=338,auxiliary_non_OP_comments_read=7,assigned_non_OP_comments_unread=2053,assigned_post_comment_sources_unavailable=37,outside_assignment_duplicate_inspection_originals=2,outside_assignment_duplicate_inspection_OP_replies=0,outside_assignment_duplicate_inspection_non_OP_comments_unread=16,outside_assignment_duplicate_inspection_missing_comment_sources=1,duplicate_body_groups_reviewed=2,all_reviewed_groups_one_representative=True,main_counts_do_not_include_extra_inspections=True,transferred_originals_not_in_reader_coverage=60,transferred_OP_replies_not_in_reader_coverage=197,quoted_post_ids=len({q['post_id'] for q in voice}),quote_ids=len(voice),read_ledger_statuses=dict(collections.Counter(r['status'] for r in read)),reader_notes_referenced_quote_ids=sorted(refs))
(SCRATCH/'coverage-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));sys.exit(bool(errors))
