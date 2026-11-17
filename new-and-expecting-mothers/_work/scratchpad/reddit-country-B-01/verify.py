#!/usr/bin/env python3
# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
"""Native attribution and finite-scope audit; writes country B01 outputs only."""
import collections,csv,datetime,gzip,hashlib,json,re,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]; S=Path(__file__).parent
P=R/'_raw/reddit-deep/next-july-country-B-v1/primary-v1'
def jl(p): return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(s): return hashlib.sha256(s.encode()).hexdigest()
def stamp(v): return datetime.datetime.fromtimestamp(int(v),datetime.timezone.utc).isoformat()
def url(n): return n['permalink'] if n['permalink'].startswith('https://') else 'https://www.reddit.com'+n['permalink']
def norm(s): return re.sub(r'\s+',' ',s).strip()
def dump(p,o): p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def main():
 a=json.loads((P/'assignments/batch-01.json').read_text()); ids=a['post_ids']; assert len(ids)==len(set(ids))==292
 ix={u['post_id']:u for u in jl(P/'primary-index.jsonl')}; assert len(ix)==847
 for c in a['chunks']:
  assert sha(R/c['file'])==c['sha256']
 assert [p for c in a['chunks'] for p in c['post_ids']]==ids
 cards=json.loads((S/'card-views/manifest.json').read_text()); flat=[]
 for c in cards['chunks']:
  assert sha(R/c['file'])==c['sha256']; assert (R/c['file']).stat().st_size<=15000
  flat.extend(c['post_ids'])
 assert flat==ids
 triage=list(csv.DictReader((R/'_raw/reddit-deep/triage/country-B-01.tsv').open(),delimiter='\t'))
 assert len(triage)==292 and [r['post_id'] for r in triage]==ids
 allowed={'keep_play','keep_solids','keep_pumping_work','keep_sleep','keep_postpartum','keep_pregnancy','keep_registry','keep_other','drop'}
 for row in triage:
  assert row['label'] in allowed and row['reason'].strip() and row['card_file']==cards['original_card_files'][row['post_id']]
 keeps=[r['post_id'] for r in triage if r['label'].startswith('keep_')]; drops=[r['post_id'] for r in triage if r['label']=='drop']; assert len(keeps)==224 and len(drops)==68
 m=json.loads((S/'full-views/manifest.json').read_text()); assert m['post_ids']==keeps
 assert [p for c in m['chunks'] for p in c['post_ids']]==keeps
 view_by_id={}
 for c in m['chunks']:
  assert sha(R/c['file'])==c['sha256'] and (R/c['file']).stat().st_size<=25000
  for pid in c['post_ids']: view_by_id[pid]=c['file']
 rows=jl(R/'sources/reddit-country-B-01-reading.jsonl'); assert [r['post_id'] for r in rows]==keeps
 ledger={r['post_id']:r for r in rows}; assert len(ledger)==224
 baseline_path=R/'_raw/reddit-deep/continuation-v1/final-read-post-ids.json'
 baseline=set(json.loads(baseline_path.read_text())['full_original_post_ids']); assert len(baseline)==5879 and not baseline&set(ids)
 tracked=subprocess.check_output(['git','ls-tree','-r','--name-only','34ec30af',str(R/'voice')],text=True).splitlines()
 old=[]
 for p in tracked:
  old.extend(json.loads(l) for l in subprocess.check_output(['git','show','34ec30af:'+p],text=True).splitlines() if l.strip())
 assert len(old)==1944
 oldids={q['id'] for q in old}; oldposts={q.get('post_id') for q in old}; assert not set(ids)&oldposts
 dump(S/'baseline-dedup-check.json',{'baseline_commit':'34ec30af','baseline_quotes':len(old),'baseline_read_posts':len(baseline),'read_inventory':str(baseline_path.relative_to(R)),'read_inventory_sha256':sha(baseline_path),'assigned_direct_read_or_quoted_overlap':[],'scope':'frozen 1944 quotes and authoritative 5879 complete original IDs; legacy final inventory not used'})
 groups=[g for g in jl(P/'duplicate-flags.jsonl') if set(ids)&{r['post_id'] for r in g['records']}]
 need=set(ids)|{r['post_id'] for g in groups for r in g['records']}; communities={ix[p]['subreddit'] for p in ids}|{r['subreddit'] for g in groups for r in g['records']}
 native={}; native_sources=[]
 for community in sorted(communities):
  p=R/f'_raw/reddit-deep/windows/2025-h2-v1/{community}_submissions.jsonl.gz'
  with gzip.open(p,'rt') as f:
   for l in f:
    n=json.loads(l)
    if n['id'] in need:
     assert n['id'] not in native; native[n['id']]=n
  native_sources.append({'file':str(p.relative_to(R)),'sha256':sha(p)})
 assert set(native)==need
 for pid in ids:
  u=ix[pid]; n=native[pid]; raw=R/u['raw_file']; assert sha(raw)==u['sha256'] and raw.stat().st_size==u['utf8_bytes']
  text=raw.read_text(); title=text.split('=== COMPLETE ORIGINAL POST TITLE ===\n',1)[1].split('\n\n=== COMPLETE ORIGINAL POST BODY ===',1)[0]
  body,rest=text.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)
  assert title==n['title'] and body==n['selftext'] and u['post_date']==stamp(n['created_utc']) and u['url']==url(n)
  assert u['subreddit']==n['subreddit'] and u['comment_source_available'] is False and u['source_comment_file'] is None
  assert u['OP_replies']==0 and u['OP_comment_ids']==[] and 'publisher comment file is unavailable' in rest
  if pid in ledger:
   r=ledger[pid]; assert r['post_body_read_complete'] is True
   assert type(r['available_identifiable_OP_replies_read']) is int and r['available_identifiable_OP_replies_read']==0 and r['op_reply_ids_read']==[]
   assert r['raw_file']==u['raw_file'] and r['primary_unit_sha256']==u['sha256'] and r['reading_chunk']==view_by_id[pid]
   assert r['status'] in {'eligible','excluded_after_read','read_pending_topic_review'} and r['reason'].strip()
 duplicate_reviews=[]
 for g in groups:
  ns=[native[r['post_id']] for r in g['records']]
  assert len({norm(n['selftext']) for n in ns})==1
  authors={n.get('author') for n in ns}; assert len(authors)==1 and not authors&{None,'[deleted]','[removed]'}
  groupids=[n['id'] for n in ns]
  duplicate_reviews.append({'post_ids':groupids,'assigned_ids':sorted(set(ids)&set(groupids)),'baseline_read_overlap':sorted(baseline&set(groupids)),'baseline_quote_ids':[q['id'] for q in old if q.get('post_id') in groupids],'same_native_author':True,'native_author_sha256':digest('country-b01-local-author-group-v1:'+next(iter(authors))),'same_whitespace_normalized_body':True,'earliest_native_id':min(ns,key=lambda n:n['created_utc'])['id'],'human_decision':'same dependent account, not independent people or fraud; all assigned keeps fully read, card drops remain card-only; no excerpt selected from flagged group','counterpart_scope':'machine body/author/date comparison only; not a human full-read credit'})
 assert len(duplicate_reviews)==8
 dump(S/'duplicate-review.json',{'reviews':duplicate_reviews,'additional_human_original_reads':0,'additional_human_comments':0,'semantic_reposts_and_followups':[{'post_ids':['1m85bdn','1m96cgn'],'reason':'Explicit next-day workplace accommodation followup; one dependent account.'},{'post_ids':['1mck70c','1mck87w'],'reason':'Explicit province-correction repost; both fully read and excluded.'}]})
 qs=jl(R/'voice/reddit-country-B-01.jsonl'); assert len(qs)==31 and [q['id'] for q in qs]==[f'rcb01-{i:04d}' for i in range(1,32)]
 counts=collections.Counter(q['id'] for p in (R/'voice').glob('*.jsonl') for q in jl(p))
 speakers={'expecting_mother','new_mother','experienced_mother','parent_unspecified','partner','relative_caregiver','recovered_parent','gave_up_parent','advisor','professional','reviewer','skeptic'}
 stages={'pregnancy_early','pregnancy_late','newborn_0_6_weeks','baby_6_16_weeks','baby_4_6_months','baby_6_12_months','toddler','return_to_work','looking_back','unknown'}
 types={'trigger_moment','pain','fear','tried_failed','desire','belief','question','objection','advice_given','success_story','failure_story','regret','others_said'}
 audit=[]
 role_anchors={'rcb01-0001':'FTM here','rcb01-0002':'mom-to-be','rcb01-0006':'My wife is currently 25 weeks pregnant','rcb01-0014':'As a first time mom','rcb01-0016':'like a bad mother','rcb01-0021':'My partner is breastfeeding','rcb01-0024':'My wife is on maternity leave','rcb01-0030':'Help a (new) mother out?'}
 for q in qs:
  pid=q['post_id']; n=native[pid]; assert q['quote'] in n['selftext']
  assert q['date']==stamp(n['created_utc']) and q['url']==url(n) and q['raw_file']==ledger[pid]['raw_file']
  assert q['speaker'] in speakers and q['stage'] in stages and q['type'] in types and len(q['context'].split())<=25
  assert counts[q['id']]==1 and q['id'] not in oldids and isinstance(q['themes'],list) and q['themes']
  assert q['source_class']=='reddit_archive' and q['evidence_kind']=='archived_original' and q['archive_dataset']=='yikeee/reddit-subreddits25'
  assert q['archive_commit']=='ea497c510aa68765c07ed744ec9f84d68bbedf7f' and q['read_scope']=='full_post_comment_source_unavailable'
  assert ledger[pid]['post_body_read_complete'] is True
  if q['speaker']!='parent_unspecified': assert q['id'] in role_anchors and role_anchors[q['id']] in n['title']+'\n'+n['selftext']
  assert not any(pid in d['post_ids'] for d in duplicate_reviews)
  audit.append({'quote_id':q['id'],'post_id':pid,'quote_in_native_selftext_exact':True,'canonical_permalink':url(n),'native_date':stamp(n['created_utc']),'native_author_sha256':digest('country-b01-local-author-group-v1:'+str(n.get('author'))),'speaker':q['speaker'],'stage':q['stage'],'speaker_basis':role_anchors.get(q['id'],'Conservative parent_unspecified; no gender, employment or diagnosis inferred from account metadata.'),'human_stage_and_context_review':'full original inspected; stage conservative and no named people in quote/context; context and payment claims reviewed','context_words':len(q['context'].split()),'primary_unit_sha256':ix[pid]['sha256']})
 for pid,r in ledger.items(): assert r['quote_ids']==[q['id'] for q in qs if q['post_id']==pid]
 dump(S/'native-quote-audit.json',{'records':audit,'failed':0,'native_files':native_sources,'notes':'Author hash groups saved publisher account labels only; identity, authenticity, rights and live completeness unverified.'})
 clusters=collections.defaultdict(list)
 for pid in keeps:
  author=native[pid].get('author')
  if author and author not in {'[deleted]','[removed]'}: clusters[digest('country-b01-local-author-group-v1:'+author)].append(pid)
 dump(S/'native-author-dependence.json',{'scope':'all 224 human full-read originals; saved account labels do not authenticate people','repeated_account_groups':[{'native_author_sha256':h,'post_ids':ps,'quote_ids':[q['id'] for q in qs if q['post_id'] in ps]} for h,ps in clusters.items() if len(ps)>1],'no_independent_buyer_count_claimed':True})
 source_note=(R/'sources/reddit-country-B-01.md').read_text()
 documented=set(re.findall(r'`([a-z_]+)`',source_note))
 assert {t for q in qs for t in q['themes']}<=documented
 notes=R/'synthesis/reader-notes-reddit-country-B-01.md'; note=notes.read_text(); refs=set(re.findall(r'rcb01-\d{4}',note)); assert refs and refs<={q['id'] for q in qs}
 namedposts=set(re.findall(r'`(1[a-z0-9]{5,8})`',note)); assert namedposts<=set(ids), namedposts-set(ids)
 run=subprocess.run([sys.executable,str(R/'_tools/verify_quotes.py'),str(R/'voice/reddit-country-B-01.jsonl')],capture_output=True,text=True); assert run.returncode==0,run.stdout+run.stderr
 report={'date':'2026-10-24','scope':'All292 assigned July country B cards manually triaged; all224 keeps fully read; comment source unavailable.',
 'parent_packet_cards':847,'assigned_cards':len(ids),'card_drops':len(drops),'triage_labels':dict(collections.Counter(r['label'] for r in triage)),
 'kept_originals':len(keeps),'fully_read_originals':len(rows),'partial_originals':0,'unread_kept_originals':[],'statuses':dict(collections.Counter(r['status'] for r in rows)),
 'saved_identifiable_OP_replies_read':0,'comment_source_unavailable_originals':len(keeps),'additional_human_original_reads':0,'additional_human_comment_reads':0,
 'card_drop_bodies_not_human_read':len(drops),'machine_native_validation_does_not_count_as_reading':True,
 'quotes':len(qs),'quoted_post_ids':len({q['post_id'] for q in qs}),'research_only_quote_ids':[q['id'] for q in qs if q.get('marketing_eligible') is False],
 'native_title_body_date_permalink_metadata_checks':len(ids),'native_full_originals_and_quote_attribution_passed':True,'quote_speaker_stage_context_semantics_reviewed':len(qs),'all_added_themes_documented':True,
 'original_card_chunks_hash_checked':len(a['chunks']),'complete_card_display_views_hash_checked':len(cards['chunks']),'kept_full_views_hash_checked':len(m['chunks']),
 'unit_bytes_all_full_reads':sum(ix[p]['utf8_bytes'] for p in keeps),'duplicate_groups_reviewed':len(groups),'baseline_quotes_checked':len(old),'baseline_full_original_ids_checked':len(baseline),
 'direct_baseline_overlap':[],'note_quote_ids_checked':len(refs),'note_post_ids_checked':len(namedposts),'global_own_quote_ID_uniqueness_passed':True,
 'verify_quotes_stdout':run.stdout.strip(),'failed':0,'assignment_sha256':sha(P/'assignments/batch-01.json'),'full_manifest_sha256':sha(S/'full-views/manifest.json'),
 'voice_sha256':sha(R/'voice/reddit-country-B-01.jsonl'),'reading_sha256':sha(R/'sources/reddit-country-B-01-reading.jsonl'),'triage_sha256':sha(R/'_raw/reddit-deep/triage/country-B-01.tsv'),
 'source_note_sha256':sha(R/'sources/reddit-country-B-01.md'),'reader_notes_sha256':sha(notes),'limitations':'Finite local archive evidence only; no verified real identities, rights, live completeness, clinical efficacy, prevalence, independent buyer total, accepted report price or customized-report sale established.'}
 dump(R/'sources/reddit-country-B-01-verification.json',report); print(json.dumps(report,indent=2))
if __name__=='__main__': main()
