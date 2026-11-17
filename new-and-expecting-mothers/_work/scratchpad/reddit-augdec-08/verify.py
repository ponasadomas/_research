#!/usr/bin/env python3
# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
"""Audit the exact transferred helper08 scope against saved native records."""
from pathlib import Path
import collections,csv,datetime,gzip,hashlib,json,re,subprocess,sys
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent
W=R/'_raw/reddit-deep/aug-dec-2025-wave-v1'
def jl(p):return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def stamp(v):return datetime.datetime.fromtimestamp(int(v),datetime.timezone.utc).isoformat()
def url(n):return n['permalink'] if n['permalink'].startswith('https://') else 'https://www.reddit.com'+n['permalink']
def main():
 m=json.loads((S/'full-read-v1/manifest.json').read_text());ids=m['post_ids'];assert len(ids)==len(set(ids))==60
 transfer_path=W/'assignments/fullread-transfer-07-to-08-v1.json';t=json.loads(transfer_path.read_text())
 assert t['donor_confirmed_all_tail_unread'] is True and t['post_ids']==ids
 assert sha(R/t['source_manifest'])==t['source_manifest_sha256']
 donor=json.loads((R/t['source_manifest']).read_text());assert donor['assigned_full_units']==186
 first=[p for c in donor['chunks'][:40] for p in c['post_ids']];tail=[p for c in donor['chunks'][40:] for p in c['post_ids']]
 assert len(first)==126 and tail==ids and not set(first)&set(ids)
 assert donor['chunks'][40:]==t['source_chunks']
 assert len(m['chunks'])==20
 for c,d in zip(m['chunks'],t['source_chunks']):
  assert c['file']==d['file'] and c['post_ids']==d['post_ids'] and c['units']==d['units']
  assert sha(R/c['file'])==c['sha256']==d['sha256']
 triage=list(csv.DictReader((R/m['inherited_triage']).open(),delimiter='\t'))
 assert len(triage)==len({x['post_id'] for x in triage})==620
 kept={x['post_id'] for x in triage if x['label'].startswith('keep_')};assert len(kept)==432
 root04=json.loads((R/'scratchpad/reddit-augdec-04/full-read-v1/manifest.json').read_text())
 helper06=json.loads((R/'scratchpad/reddit-augdec-06/full-read-v1/manifest.json').read_text())
 sets=[set(root04['post_ids']),set(helper06['post_ids']),set(first),set(ids)]
 assert [len(s) for s in sets]==[60,186,126,60]
 assert set.union(*sets)==kept and sum(map(len,sets))==len(kept)
 rows=jl(R/'sources/reddit-augdec-08-reading.jsonl');assert [x['post_id'] for x in rows]==[p for c in m['chunks'] for p in c['post_ids']]
 ledger={x['post_id']:x for x in rows};assert set(ledger)==set(ids)
 ix={u['post_id']:u for u in jl(W/'primary-index.jsonl')};posts={};comments=collections.defaultdict(list);bycomment={}
 with gzip.open(R/'_raw/reddit-deep/windows/2025-h2-v1/workingmoms_submissions.jsonl.gz','rt') as f:
  for line in f:
   n=json.loads(line)
   if n['id'] in ledger:assert n['id'] not in posts;posts[n['id']]=n
 with gzip.open(R/'_raw/reddit-deep/windows/2025-h2-v1/workingmoms_comments.jsonl.gz','rt') as f:
  for line in f:
   n=json.loads(line);pid=n.get('link_id','').removeprefix('t3_')
   if pid in ledger:comments[pid].append(n);assert n['id'] not in bycomment;bycomment[n['id']]=n
 assert set(posts)==set(ids)
 for pid,row in ledger.items():
  u=ix[pid];post=posts[pid];author=post.get('author')
  op=[c for c in comments[pid] if author and author not in {'[deleted]','[removed]'} and c.get('author')==author]
  expected={c['id'] for c in op};assert row['post_body_read_complete'] is True
  assert type(row['available_identifiable_OP_replies_read']) is int and row['available_identifiable_OP_replies_read']==len(expected)==u['OP_replies']
  assert len(row['op_reply_ids_read'])==len(expected) and set(row['op_reply_ids_read'])==expected==set(u['OP_comment_ids'])
  assert row['raw_file']==u['raw_file'] and sha(R/row['raw_file'])==row['primary_unit_sha256']==u['sha256']
  text=(R/row['raw_file']).read_text();title=text.split('=== COMPLETE ORIGINAL POST TITLE ===\n',1)[1].split('\n\n=== COMPLETE ORIGINAL POST BODY ===',1)[0]
  body,rest=text.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)
  assert title==post.get('title','') and body==post.get('selftext','')
  assert u['post_date']==stamp(post['created_utc']) and u['url']==url(post)
  blocks=rest.split('\n--- OP REPLY ---\n')[1:];assert len(blocks)==len(op);seen=set()
  for block in blocks:
   head,actual=block.split('\n',1);meta=json.loads(head);native=bycomment[meta['comment_id']]
   assert native in op and actual.startswith(native.get('body','')) and not actual[len(native.get('body','')):].strip()
   assert meta['date']==stamp(native['created_utc']) and meta['parent_id']==native['parent_id'];seen.add(meta['comment_id'])
  assert seen==expected and row['status'] in {'eligible','excluded_after_read','read_pending_topic_review'} and row['reason'].strip()
 quotes=jl(R/'voice/reddit-augdec-08.jsonl');assert [q['id'] for q in quotes]==[f'rad08-{i:04d}' for i in range(1,len(quotes)+1)]
 counts=collections.Counter(q['id'] for p in (R/'voice').glob('*.jsonl') for q in jl(p))
 speakers={'expecting_mother','new_mother','experienced_mother','parent_unspecified','partner','relative_caregiver','recovered_parent','gave_up_parent','advisor','professional','reviewer','skeptic'}
 stages={'pregnancy_early','pregnancy_late','newborn_0_6_weeks','baby_6_16_weeks','baby_4_6_months','baby_6_12_months','toddler','return_to_work','looking_back','unknown'}
 types={'trigger_moment','pain','fear','tried_failed','desire','belief','question','objection','advice_given','success_story','failure_story','regret','others_said'}
 for q in quotes:
  pid=q['post_id'];native=bycomment[q['comment_id']] if q.get('comment_id') else posts[pid]
  assert q['quote'] in native.get('body' if q.get('comment_id') else 'selftext','')
  assert q['date']==stamp(native['created_utc']) and q['url']==url(native)
  assert q['raw_file']==ledger[pid]['raw_file'] and counts[q['id']]==1
  if q.get('comment_id'):assert q['comment_id'] in ledger[pid]['op_reply_ids_read']
  assert q['speaker'] in speakers and q['stage'] in stages and q['type'] in types
  assert len(q['context'].split())<=25 and isinstance(q['themes'],list) and q['themes']
  assert q['source_class']=='reddit_archive' and q['evidence_kind']=='archived_original'
  assert q['archive_dataset']=='yikeee/reddit-subreddits25' and q['archive_commit']=='ea497c510aa68765c07ed744ec9f84d68bbedf7f'
  assert q['read_scope']=='full_post_and_available_identifiable_OP_replies'
  assert ledger[pid]['post_body_read_complete'] is True
 for pid,row in ledger.items():assert row['quote_ids']==[q['id'] for q in quotes if q['post_id']==pid]
 aux=jl(R/'sources/reddit-augdec-08-auxiliary-read.jsonl');assert not aux
 baseline=json.loads((R/'_raw/reddit-deep/final-read-post-ids.json').read_text());assert not set(ids)&set(baseline['full_original_post_ids'])
 for other in ['01','02','03','04','05','06','07']:
  p=R/f'sources/reddit-augdec-{other}-reading.jsonl'
  if p.exists():assert not set(ids)&{x['post_id'] for x in jl(p)},other
 notes=R/'synthesis/reader-notes-reddit-augdec-08.md';refs=set(re.findall(r'rad08-\d{4}',notes.read_text()));assert refs and refs<={q['id'] for q in quotes}
 run=subprocess.run([sys.executable,str(R/'_tools/verify_quotes.py'),str(R/'voice/reddit-augdec-08.jsonl')],capture_output=True,text=True);assert run.returncode==0,run.stdout+run.stderr
 report={'date':'2026-10-24','scope':'all60 transferred unstarted originals in original07 frozen views041-060; inherited root04 triage, no additional cards',
  'inherited_cards':len(triage),'inherited_keeps':len(kept),'partition_counts_root04_helper06_current07_helper08':[60,186,126,60],
  'exact_partition_disjoint_union_passed':True,'full_original_posts':len(rows),'partial_original_posts':0,
  'OP_replies_read':sum(r['available_identifiable_OP_replies_read'] for r in rows),'auxiliary_comments_read':len(aux),
  'statuses':dict(collections.Counter(r['status'] for r in rows)),'quotes':len(quotes),'quoted_post_ids':len({q['post_id'] for q in quotes}),
  'quoted_OP_replies':sum(bool(q.get('comment_id')) for q in quotes),'research_only_quote_ids':[q['id'] for q in quotes if q.get('marketing_eligible') is False],
  'primary_unit_utf8_bytes':sum(ix[p]['utf8_bytes'] for p in ids),'original_body_bytes':sum(ix[p]['body_bytes'] for p in ids),
  'frozen_source_views_checked':len(m['chunks']),'note_quote_ids_checked':len(refs),'native_original_OP_quote_bodies_dates_canonical_URLs_hashes_and_global_own_ID_uniqueness':'passed',
  'baseline_and_other_reader_ID_nonoverlap':'passed','verify_quotes_stdout':run.stdout.strip(),
  'manifest_sha256':sha(S/'full-read-v1/manifest.json'),'transfer_manifest':str(transfer_path.relative_to(R)),'transfer_sha256':sha(transfer_path),
  'voice_sha256':sha(R/'voice/reddit-augdec-08.jsonl'),'reading_sha256':sha(R/'sources/reddit-augdec-08-reading.jsonl'),'failed':0,
  'limits':'Finite local archive attribution and coverage only; no live completeness, verified purchases, clinical efficacy, independent buyer count or market prevalence established.'}
 (R/'sources/reddit-augdec-08-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
