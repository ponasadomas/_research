#!/usr/bin/env python3
# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
"""Strict native capture, finite ownership, attribution and commercial-field audit."""
import collections,csv,datetime,gzip,hashlib,io,json,re,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent;W=R/'_raw/report-purchase-archive-wave03'
def jl(p):return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(t):return hashlib.sha256(t.encode()).hexdigest()
def norm(t):return re.sub(r'\s+',' ',t).strip()
def stamp(v):return datetime.datetime.fromtimestamp(int(v),datetime.timezone.utc).isoformat()
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def main():
 cap=json.loads((W/'capture-summary.json').read_text());idx=jl(W/'native-index.jsonl');ix={x['post_id']:x for x in idx};assert len(ix)==len(idx)==15226
 initial=jl(W/'commercial-candidates.jsonl');sup=jl(W/'supplement-v1/commercial-candidates.jsonl');assert len(initial)==72 and len(sup)==319
 iniids=[x['post_id'] for x in initial];supids=[x['post_id'] for x in sup];assert not set(iniids)&set(supids)
 ownass=json.loads((W/'supplement-v1/assignments/owner-first56.json').read_text());a4=json.loads((W/'supplement-v1/assignments/reader-04.json').read_text());a5=json.loads((W/'supplement-v1/assignments/reader-05.json').read_text())
 assert [len(x['post_ids']) for x in [ownass,a4,a5]]==[56,142,121]
 assert ownass['post_ids']+a4['post_ids']+a5['post_ids']==supids
 ti=list(csv.DictReader((S/'triage.tsv').open(),delimiter='\t'));ts=list(csv.DictReader((S/'supplement-v1/triage.tsv').open(),delimiter='\t'))
 assert [r['post_id'] for r in ti]==iniids and [r['post_id'] for r in ts]==ownass['post_ids']
 keeps=[r['post_id'] for r in ti+ts if r['label']=='keep'];drops=[r['post_id'] for r in ti+ts if r['label']=='drop'];assert len(keeps)==len(drops)==64
 assert [r['post_id'] for r in ts if r['label']=='keep']==ownass['kept_post_ids']
 for row in ti+ts:assert row['label'] in {'keep','drop'} and row['reason'].strip()
 card_views=0;full_views=0;viewby={}
 for base,count in [(S,72),(S/'supplement-v1',319)]:
  cm=json.loads((base/'card-views/manifest.json').read_text());assert len(cm['post_ids'])==count
  assert [p for c in cm['chunks'] for p in c['post_ids']]==cm['post_ids']
  for c in cm['chunks']:assert sha(R/c['file'])==c['sha256']
  card_views+=len(cm['chunks'])
 for x in initial+sup:assert sha(R/x['card_file'])==x['card_sha256']
 for base,want in [(S,[r['post_id'] for r in ti if r['label']=='keep']),(S/'supplement-own-full-v1',ownass['kept_post_ids'])]:
  m=json.loads((base/'full-views/manifest.json').read_text());assert m['post_ids']==want and [p for c in m['chunks'] for p in c['post_ids']]==want
  for c in m['chunks']:
   assert sha(R/c['file'])==c['sha256'] and (R/c['file']).stat().st_size<=25000
   for pid in c['post_ids']:viewby[pid]=c['file']
  full_views+=len(m['chunks'])
 rows=jl(R/'sources/report-purchase-archive-wave03-reading.jsonl');assert [r['post_id'] for r in rows]==keeps
 ledger={r['post_id']:r for r in rows};tx=jl(R/'sources/report-purchase-archive-wave03-transactions.jsonl');assert [r['post_id'] for r in tx]==keeps
 native={};stats=[];normgroups=collections.defaultdict(list)
 for dl in json.loads((W/'downloads.json').read_text()):
  p=R/dl['file'];assert dl['status']==200 and sha(p)==dl['sha256'] and p.stat().st_size==dl['bytes']==dl['manifest_bytes']
  check=subprocess.run(['zstd','-q','-t',str(p)],capture_output=True,text=True);assert check.returncode==0,check.stderr
  proc=subprocess.Popen(['zstd','-q','-d','-c',str(p)],stdout=subprocess.PIPE,stderr=subprocess.PIPE);full=0;window=0;statuses=collections.Counter();lo=None;hi=None;ids=set()
  for line in io.TextIOWrapper(proc.stdout,encoding='utf8'):
   if not line.strip():continue
   n=json.loads(line);full+=1;assert n['id'] not in ids;ids.add(n['id']);date=stamp(n['created_utc']);lo=date if lo is None else min(lo,date);hi=date if hi is None else max(hi,date)
   if not '2025-07-01T00:00:00+00:00'<=date<'2026-01-01T00:00:00+00:00':continue
   window+=1;pid=n['id'];u=ix[pid];assert pid not in native;native[pid]=n
   body=n.get('selftext','');status='removed' if body=='[removed]' else 'deleted' if body=='[deleted]' else 'empty' if not body.strip() else 'present';statuses[status]+=1
   assert u['date']==date and u['url']=='https://www.reddit.com'+n['permalink'] and u['title']==n['title'] and u['subreddit']==n['subreddit'] and u['body_status']==status
   assert u['native_author_sha256']==digest('report-purchase-wave03:'+str(n.get('author'))) and u['native_body_sha256']==digest(body)
   assert u['comment_source_available'] is False and u['source_comment_file'] is None and u['OP_replies']==0 and u['OP_comment_ids']==[]
   if status=='present':
    raw=R/u['raw_file'];assert sha(raw)==u['sha256'] and raw.stat().st_size==u['utf8_bytes'];text=raw.read_bytes().decode('utf8');title=text.split('=== COMPLETE ORIGINAL POST TITLE ===\n',1)[1].split('\n\n=== COMPLETE ORIGINAL POST BODY ===',1)[0];unitbody,rest=text.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)
    assert title==n['title'] and unitbody==body and 'publisher comment file is unavailable' in rest
    normgroups[digest(norm(body))].append(pid)
   else:assert u['raw_file'] is None
  err=proc.stderr.read().decode();assert proc.wait()==0,err
  recorded=next(x for x in cap['files'] if x['community']==dl['community']);assert full==recorded['native_records_all'] and window==recorded['window_records'] and dict(statuses)==recorded['window_text_status'] and lo==recorded['min_date'] and hi==recorded['max_date']
  assert sha(R/recorded['window_file'])==recorded['window_sha256'];windowids=[]
  with gzip.open(R/recorded['window_file'],'rt') as f:
   for line in f:
    n=json.loads(line);assert n==native[n['id']];windowids.append(n['id'])
  assert len(windowids)==window
  stats.append({'community':dl['community'],'full_records':full,'window_records':window,'min_date':lo,'max_date':hi,'status':dict(statuses),'compressed_sha256':dl['sha256'],'zstd_integrity_and_full_JSON_EOF':True})
 assert len(native)==15226 and sum(x['body_status']=='present' for x in idx)==15088
 for row in rows:
  u=ix[row['post_id']];assert row['post_body_read_complete'] is True and row['raw_file']==u['raw_file'] and row['primary_unit_sha256']==u['sha256']
  assert type(row['available_identifiable_OP_replies_read']) is int and row['available_identifiable_OP_replies_read']==0 and row['op_reply_ids_read']==[]
  assert row['comment_status']=='publisher_comment_file_unavailable' and row['comment_source_available'] is False and row['reading_chunk']==viewby[row['post_id']]
  assert row['date']==u['date'] and row['url']==u['url'] and row['source_archive']==u['archive_file'] and row['status'] in {'eligible','excluded_after_read','read_pending_topic_review'} and row['reason'].strip()
 for t in tx:
  assert t['raw_file']==ix[t['post_id']]['raw_file'] and t['primary_unit_sha256']==ix[t['post_id']]['sha256']
  assert t['payment_evidence'] and t['product_or_service'] and t['deliverable_format'] and t['use_or_outcome']
  assert t['standalone_customized_written_report_verified'] is False
  for k in ['trigger','actual_price','currency','personalization_inputs','personalization_output','support_bundle','qualifications_claimed','refund','affiliation']:assert k in t
 qs=jl(R/'voice/report-purchase-archive-wave03.jsonl');assert [q['id'] for q in qs]==[f'rpa03-{i:04d}' for i in range(1,len(qs)+1)] and len(qs)==21
 allquotes=[q for p in (R/'voice').glob('*.jsonl') for q in jl(p)];globalcounts=collections.Counter(q['id'] for q in allquotes)
 existing=[q for q in allquotes if not q['id'].startswith('rpa03-')];direct=[]
 for q in existing:
  match=re.search(r'/comments/([a-z0-9]+)',q.get('url',''));pid=q.get('post_id') or (match[1] if match else None)
  if pid in keeps:direct.append({'id':q['id'],'post_id':pid})
 assert not direct
 speakers={'expecting_mother','new_mother','experienced_mother','parent_unspecified','partner','relative_caregiver','recovered_parent','gave_up_parent','advisor','professional','reviewer','skeptic'};stages={'pregnancy_early','pregnancy_late','newborn_0_6_weeks','baby_6_16_weeks','baby_4_6_months','baby_6_12_months','toddler','return_to_work','looking_back','unknown'};types={'trigger_moment','pain','fear','tried_failed','desire','belief','question','objection','advice_given','success_story','failure_story','regret','others_said'}
 audit=[]
 for q in qs:
  n=native[q['post_id']];u=ix[q['post_id']];assert q['quote'] in n['selftext'] and q['date']==stamp(n['created_utc']) and q['url']=='https://www.reddit.com'+n['permalink'] and q['raw_file']==u['raw_file']
  assert q['speaker'] in speakers and q['stage'] in stages and q['type'] in types and len(q['context'].split())<=25 and globalcounts[q['id']]==1
  assert q['source_class']=='reddit_archive' and q['evidence_kind']=='archived_original' and q['archive_dataset']=='yikeee/reddit-subreddits25' and q['archive_commit']=='ea497c510aa68765c07ed744ec9f84d68bbedf7f' and q['read_scope']=='full_post_comment_source_unavailable'
  assert ledger[q['post_id']]['status']=='eligible'
  if q['speaker']=='new_mother':assert ('FTM' in n['selftext'] or 'motherhood' in n['selftext'])
  audit.append({'id':q['id'],'post_id':q['post_id'],'native_selftext_exact':True,'native_date_and_canonical_permalink':True,'speaker_stage_context_human_reviewed':True,'native_author_sha256':u['native_author_sha256'],'context_words':len(q['context'].split()),'raw_sha256':u['sha256']})
 for row in rows:assert row['quote_ids']==[q['id'] for q in qs if q['post_id']==row['post_id']]
 dump(S/'native-quote-audit.json',{'records':audit,'failed':0})
 groups=collections.defaultdict(list)
 for pid in keeps:groups[ix[pid]['native_author_sha256']].append(pid)
 dependence=[]
 for h,own in groups.items():
  related=[pid for pid,u in ix.items() if u['native_author_sha256']==h]
  if len(own)>1 or '1n2ffio' in related:dependence.append({'native_author_sha256':h,'own_full_read_post_ids':own,'related_window_post_ids_metadata_only':[p for p in related if p not in own],'quote_ids':[q['id'] for q in qs if q['post_id'] in own],'meaning':'one saved account label, not authenticated people or independent purchasers; outside own scope related bodies not read here'})
 targethash={digest(norm(native[p]['selftext'])):p for p in keeps};oldread=set(json.loads((R/'_raw/reddit-deep/continuation-v1/final-read-post-ids.json').read_text())['full_original_post_ids'])
 for p in (R/'sources').glob('*.jsonl'):
  if p.name.startswith('report-purchase-archive-wave03'):continue
  for row in jl(p):
   if row.get('post_body_read_complete') is True and row.get('post_id'):oldread.add(row['post_id'])
 oldquoted=set()
 for q in existing:
  match=re.search(r'/comments/([a-z0-9]+)',q.get('url',''));pid=q.get('post_id') or (match[1] if match else None)
  if pid:oldquoted.add(pid)
 bodyhits=[];scanned=0;priorworks=oldread|oldquoted
 for p in sorted((R/'_raw/reddit-deep/windows/2025-h2-v1').glob('*_submissions.jsonl.gz')):
  with gzip.open(p,'rt') as f:
   for line in f:
    n=json.loads(line);scanned+=1
    if n['id'] not in priorworks:continue
    h=digest(norm(n.get('selftext','')))
    if h in targethash:bodyhits.append({'own_post_id':targethash[h],'old_post_id':n['id'],'old_quoted':n['id'] in oldquoted,'old_read':n['id'] in oldread,'same_saved_author':ix[targethash[h]]['native_author_sha256']==digest('report-purchase-wave03:'+str(n.get('author'))),'existing_quote_ids':[q['id'] for q in existing if q.get('post_id')==n['id'] or '/'+n['id']+'/' in q.get('url','')]})
 assert [(x['own_post_id'],x['old_post_id']) for x in bodyhits]==[('1or3vij','1ow7gp3')],bodyhits
 assert all(x['same_saved_author'] and x['old_read'] and x['old_quoted'] for x in bodyhits)
 assert not {q['post_id'] for q in qs}&{x['own_post_id'] for x in bodyhits}
 touching=[v for v in normgroups.values() if len(v)>1 and set(v)&set(keeps)]
 dump(S/'dependence-and-work-check.json',{'repeated_saved_account_groups':dependence,'same_body_groups_touching_own_full_reads':touching,'existing_quote_records_checked':len(existing),'existing_quote_direct_work_hits':direct,'old_nine_community_native_records_machine_checked':scanned,'old_read_or_quoted_body_work_hits':bodyhits,'outside_own_human_full_read_count':0,'cross_reader_sequence_note':'1mclz85 Jul29 and1n6hnju Sep2 share saved account with reader04 own1n2ffio Aug28; latter metadata only inspected here; no independent buyer or separate corroboration claim.'})
 notes=R/'synthesis/reader-notes-report-purchase-archive-wave03.md';note=notes.read_text();refs=set(re.findall(r'rpa03-\d{4}',note));assert refs and refs<={q['id'] for q in qs}
 source=R/'sources/report-purchase-archive-wave03.md';documented=set(re.findall(r'`([a-z_]+)`',source.read_text()));assert {t for q in qs for t in q['themes']}<=documented
 run=subprocess.run([sys.executable,str(R/'_tools/verify_quotes.py'),str(R/'voice/report-purchase-archive-wave03.jsonl')],capture_output=True,text=True);assert run.returncode==0,run.stdout+run.stderr
 report={'date':'2026-10-24','independent_publisher':'yikeee/reddit-subreddits25','pinned_commit':'ea497c510aa68765c07ed744ec9f84d68bbedf7f','scope_separate_from_nine_community_ABC':True,'capture_files':stats,'whole_compressed_bytes':sum(x['bytes'] for x in json.loads((W/'downloads.json').read_text())),'window_originals':len(idx),'readable_original_units':15088,'unavailable_window_bodies':138,'initial_candidates':72,'supplement_candidates':319,'own_initial_triage':72,'own_initial_keeps':55,'own_initial_drops':17,'own_supplement_triage':56,'own_supplement_keeps':9,'own_supplement_drops':47,'supplement_delegated_to_existing_readers':{'04':142,'05':121},'all_own_full_reads':len(rows),'all_own_keeps_read':True,'partial_originals':0,'unread_own_keeps':[],'statuses':dict(collections.Counter(r['status'] for r in rows)),'own_card_drop_bodies_human_unread':64,'comments_and_identifiable_OP_replies_read':0,'comment_sources_unavailable':True,'human_extra_originals':0,'machine_validation_not_human_reading':True,'quotes':len(qs),'quoted_originals':len({q['post_id'] for q in qs}),'research_only_quote_ids':[q['id'] for q in qs if q.get('marketing_eligible') is False],'per_original_transaction_field_records':len(tx),'documented_standalone_customized_written_report_transactions':0,'native_readable_unit_title_body_metadata_hash_checks':15088,'full_source_JSON_records_scanned':sum(x['full_records'] for x in stats),'card_display_view_hash_checks':card_views,'human_card_views_read_initial':8,'human_card_views_read_supplement_own':5,'full_display_views_hash_checked':full_views,'native_body_date_canonical_URL_checks':len(qs),'global_own_ID_uniqueness':True,'note_quote_ids_checked':len(refs),'verify_quotes_stdout':run.stdout.strip(),'failed':0,'voice_sha256':sha(R/'voice/report-purchase-archive-wave03.jsonl'),'reading_sha256':sha(R/'sources/report-purchase-archive-wave03-reading.jsonl'),'transactions_sha256':sha(R/'sources/report-purchase-archive-wave03-transactions.jsonl'),'source_note_sha256':sha(source),'reader_notes_sha256':sha(notes),'limits':'Archived unverified self reports; no live completeness, authenticated independence, clinical efficacy, price acceptance for a custom report, causal outcomes or market prevalence. Other readers own remaining263supplement cards and their keeps.'}
 dump(R/'sources/report-purchase-archive-wave03-verification.json',report);dump(S/'completion-progress.json',{'own_candidates_triaged':128,'own_keeps':64,'own_full_originals':64,'own_card_drops':64,'eligible':53,'excluded_after_read':11,'quotes':21,'phase':'complete_native_audit_passed','failed':0})
 dump(S/'supplement-own-full-v1/reading-progress.json',{'supplement_originals_full':9,'supplement_keeps':9,'all_own_originals_full':64,'all_own_keeps':64,'phase':'complete'})
 print(json.dumps(report,indent=2))
if __name__=='__main__':main()
