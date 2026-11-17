from pathlib import Path
import json,csv,hashlib,gzip,datetime,collections,re,sys
R=Path(__file__).resolve().parents[2];S=R/'scratchpad/report-purchase-supplement-05';ERR=[]
def chk(ok,msg):
 if not ok:ERR.append(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p):return [json.loads(l) for l in p.read_text().splitlines()] if p.exists() else []
def ws(s):return re.sub(r'\s+',' ',s).strip()
A=json.loads((R/'_raw/report-purchase-archive-wave03/supplement-v1/assignments/reader-05.json').read_text());I={x['post_id']:x for x in rows(R/A['primary_index'])};T=list(csv.DictReader((R/'_raw/report-purchase-archive-wave03/supplement-v1/triage-05.tsv').open(),delimiter='\t'));RD=rows(R/'sources/report-purchase-supplement-05-reading.jsonl');Q=rows(R/'voice/report-purchase-supplement-05.jsonl');P=rows(R/'sources/report-purchase-supplement-05-purchase-evidence.jsonl');M=json.loads((S/'full-read-v1/manifest.json').read_text());CP=json.loads((R/'_raw/report-purchase-archive-wave03/capture-summary.json').read_text());assigned=set(A['post_ids']);kept={x['post_id'] for x in T if x['label']=='keep'};dropped=assigned-kept;quoted={q['post_id'] for q in Q};read={x['post_id'] for x in RD}
chk(len(A['post_ids'])==len(assigned)==121,'assignment IDs');chk(len(T)==len({x['post_id'] for x in T})==121 and {x['post_id'] for x in T}==assigned,'triage exact assignment');chk(len(RD)==len(read)==43 and read==kept,'all kept full-read exactly');chk(len(P)==43 and {x['post_id'] for x in P}==kept,'purchase ledger exact keep');chk(all(x['label'] in ['keep','drop'] and x['reason'] and x['card_file']==I[x['post_id']]['card_file'] for x in T),'triage schema');chk(not read&dropped,'card drops full-body unread');chk(all(x['post_body_read_complete'] and x['available_identifiable_OP_replies_read']==0 and x['op_reply_ids_read']==[] for x in RD),'all full and missing OP');chk(len(quoted)==len(Q)==22,'quote works unique');chk(quoted<=kept,'quotes within keep');chk({x['post_id'] for x in rows(S/'triage-reading.jsonl') if 'post_id' in x}==set(),'triage view log schema expectation')
for c in A['card_chunks']:chk(sha(R/c['file'])==c['sha256'],'original card view hash '+c['file'])
chk(len(rows(S/'triage-reading.jsonl'))==12,'12 original card views read');chk([p for c in rows(S/'triage-reading.jsonl') for p in c['post_ids']]==A['post_ids'],'card reading log exact ordered IDs')
for tid in assigned:
 x=I[tid];chk(sha(R/x['card_file'])==x['card_sha256'],'card hash '+tid)
chk(sha(R/M['triage_file'])==M['triage_sha256'],'frozen own triage hash');chk(set(M['kept_post_ids'])==kept,'frozen full scope');chk([p for c in M['views'] for p in c['post_ids']]==M['kept_post_ids'],'full view membership');chk(len(rows(S/'full-reading.jsonl'))==len(M['views'])==9,'9 full views read')
for c in M['views']:
 chk(sha(R/c['file'])==c['sha256'],'own full-view hash '+c['file'])
 for tid in c['post_ids']:
  unit=(R/I[tid]['raw_file']).read_text();b=unit.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0].strip();chk(b in (R/c['file']).read_text(),'complete body in own view '+tid)
for f in CP['files']:
 chk(sha(R/f['compressed_file'])==f['sha256'],'parent compressed hash '+f['community']);chk(sha(R/f['window_file'])==f['window_sha256'],'native window hash '+f['community'])
N={};native_counts={}
for p in sorted({I[t]['window_file'] for t in assigned}):
 n=0
 with gzip.open(R/p,'rt') as f:
  for l in f:
   x=json.loads(l);n+=1
   if x['id'] in assigned:N[x['id']]=x
 native_counts[p]=n
chk(set(N)==assigned,'all assigned native IDs found')
for tid in assigned:
 x=I[tid];n=N[tid];chk(x['title']==n['title'],'native title metadata '+tid);chk(x['subreddit']==n['subreddit'],'native subreddit '+tid);chk(x['url']=='https://www.reddit.com'+n['permalink'],'native URL '+tid);chk(datetime.datetime.fromtimestamp(n['created_utc'],datetime.timezone.utc).isoformat()==x['date'],'native date '+tid);chk(hashlib.sha256(('report-purchase-wave03:'+str(n.get('author'))).encode()).hexdigest()==x['native_author_sha256'],'native author '+tid);chk(hashlib.sha256(n['selftext'].encode()).hexdigest()==x['native_body_sha256'],'native body hash '+tid)
 if tid in kept:
  u=R/x['raw_file'];chk(sha(u)==x['sha256'],'unit hash '+tid);t=u.read_text();b=t.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0].strip();title=t.split('=== COMPLETE ORIGINAL POST TITLE ===\n',1)[1].split('\n=== COMPLETE ORIGINAL POST BODY ===',1)[0].strip();chk(b==n['selftext'].strip(),'kept complete native body '+tid);chk(title==n['title'],'kept complete native title '+tid)
speakers=set('expecting_mother new_mother experienced_mother parent_unspecified partner relative_caregiver recovered_parent gave_up_parent advisor professional reviewer skeptic'.split());stages=set('pregnancy_early pregnancy_late newborn_0_6_weeks baby_6_16_weeks baby_4_6_months baby_6_12_months toddler return_to_work looking_back unknown'.split());types=set('trigger_moment pain fear tried_failed desire belief question objection advice_given success_story failure_story regret others_said'.split());required=set('id source url date speaker stage type themes quote context raw_file'.split());qby=collections.defaultdict(list)
for q in Q:
 tid=q['post_id'];x=I[tid];n=N[tid];qby[tid].append(q['id']);chk(required<=set(q),'required fields '+q['id']);chk(q['speaker'] in speakers and q['stage'] in stages and q['type'] in types,'vocab '+q['id']);chk(len(q['context'].split())<=25,'context word count '+q['id']);chk(q['raw_file']==x['raw_file'],'quote source path '+q['id']);chk(q['url']=='https://www.reddit.com'+n['permalink'],'quote native permalink '+q['id']);chk(q['date']==datetime.datetime.fromtimestamp(n['created_utc'],datetime.timezone.utc).date().isoformat(),'quote native date '+q['id']);chk(q['source_class']=='reddit_archive' and q['evidence_kind']=='archived_original' and q['archive_dataset']=='yikeee/reddit-subreddits25' and q['archive_commit']=='ea497c510aa68765c07ed744ec9f84d68bbedf7f' and q['read_scope']=='full_post_comment_source_unavailable','provenance '+q['id'])
 # Whitespace only; no punctuation, apostrophe, case or Unicode normalization.
 for part in q['quote'].split(' […] '):chk(ws(part) in ws(n['selftext']),'strict whitespace-only native quote '+q['id'])
for r in RD:chk(r['quote_ids']==qby[r['post_id']],'reading quote attribution '+r['post_id']);chk(r['primary_unit_sha256']==I[r['post_id']]['sha256'],'reading hash '+r['post_id'])
allids=[];otherposts=[]
for f in (R/'voice').glob('*.jsonl'):
 for q in rows(f):
  allids.append(q['id'])
  if f.name!='report-purchase-supplement-05.jsonl' and q.get('post_id') in quoted:otherposts.append(dict(file=str(f.relative_to(R)),id=q['id'],post_id=q['post_id']))
chk(all(collections.Counter(allids)[q['id']]==1 for q in Q),'own quote IDs globally unique');chk(not otherposts,'quoted same works elsewhere')
MAN=json.loads((S/'manual-spotchecks-v1/manifest.json').read_text());MR=rows(S/'manual-spotchecks-reading.jsonl');chk(len(MR)==len(MAN['views'])==5,'manual spotcheck five full views');chk([q for v in MR for q in v['quote_ids']]==MAN['selected_quote_ids'],'manual exact 20 selected quote records');chk(len(MAN['selected_quote_ids'])==len(set(MAN['selected_quote_ids']))==20,'manual sample unique 20')
for v in MAN['views']:chk(sha(R/v['file'])==v['sha256'],'manual immutable full-context packet '+v['file'])
for v in MR:chk(v['all_full_source_contexts_read'],'manual full-context read '+str(v['view']))
DEP=json.loads((S/'dependence-audit.json').read_text());chk(not DEP['same_post_other_voice_records'],'dependence same works');chk(not DEP['exact_native_body_matches'],'dependence exact native body matches');chk(DEP['other_commercial_reader_shared_authors']==[],'other commercial shared authors')
C=dict(assigned_cards=len(assigned),triaged_cards=len(T),kept_cards=len(kept),dropped_cards_full_body_unread=len(dropped),full_originals_read=len(RD),partial_originals=0,OP_replies_read=0,comment_source_unavailable=len(RD),statuses=dict(collections.Counter(x['status'] for x in RD)),quotes=len(Q),quoted_post_ids=len(quoted),research_only_quotes=sum(q.get('marketing_eligible') is False for q in Q),actual_standalone_custom_report_purchases=sum(x['actual_standalone_custom_report_purchase'] for x in P),outside_assignment_human_body_inspections=0)
O=dict(counts=C,native_assigned_metadata_verified=len(N),native_full_bodies_verified=len(kept),native_whitespace_only_quotes_verified=len(Q),native_windows_scanned=native_counts,checks_failed=len(ERR),errors=ERR,verbatim_policy='Whitespace only; exact native case/punctuation/Unicode, no typographic normalization',other_voice_same_work_records=otherposts,utc=datetime.datetime.now(datetime.timezone.utc).isoformat());(R/'sources/report-purchase-supplement-05-verification.json').write_text(json.dumps(O,indent=2)+'\n');coverage=dict(assigned_ids=A['post_ids'],kept_full_read_ids=[x['post_id'] for x in RD],card_drop_full_body_unread_ids=[x['post_id'] for x in T if x['label']=='drop'],excluded_after_read_ids=[x['post_id'] for x in RD if x['status']=='excluded_after_read'],quoted_post_ids=sorted(quoted),kept_unread_ids=sorted(kept-read),counts=C);(S/'final-coverage.json').write_text(json.dumps(coverage,indent=2)+'\n');print(json.dumps(O,indent=2));sys.exit(bool(ERR))
