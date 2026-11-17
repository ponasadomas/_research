# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
"""Verify and finalize human decisions for the complete186-unit transfer06."""
import collections,csv,datetime,gzip,hashlib,html,json,re,subprocess,sys
from pathlib import Path
S=Path(__file__).resolve().parent;R=S.parents[1];W=R/'_raw/reddit-deep/aug-dec-2025-wave-v1'
def jl(p):return [json.loads(s) for s in p.read_text().splitlines() if s.strip()]
def save(p,a):p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in a))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+',' ',html.unescape(s).replace('\\n',' ')).strip()
def stamp(t):return datetime.datetime.fromtimestamp(int(t),datetime.timezone.utc).isoformat()
M=json.loads((S/'full-read-v1/manifest.json').read_text());P=json.loads((W/'assignments/root04-fullread-partitions-v1.json').read_text());own=next(x for x in P['partitions'] if x['number']=='06');assigned=set(M['post_ids']);I={x['post_id']:x for x in jl(W/'primary-index.jsonl')};L=jl(R/'sources/reddit-augdec-06-reading.jsonl');byid={x['post_id']:x for x in L};A=jl(S/'selections.jsonl');N={}
for f in sorted({I[p]['source_post_file'] for p in assigned}):
 with gzip.open(R/f,'rt') as stream:
  for line in stream:
   x=json.loads(line)
   if x['id'] in assigned:N[x['id']]=x
aux=R/'sources/reddit-augdec-06-auxiliary-read.jsonl'
if not aux.exists():aux.write_text('')
# Human reviewed allthree touching flags; assigned duplicates are still fully read.
reps={32:'1p3ysdn',57:'1mvi6h1',92:'1mzck9r'};D=[]
for number,g in enumerate(jl(W/'exact-body-duplicate-flags.jsonl'),1):
 ids={x['post_id'] for x in g['records']};scope=sorted(ids&assigned)
 if not scope:continue
 assert number in reps;rep=reps[number];selected=[a['post_id'] for a in A if a['post_id'] in ids];assert all(x==rep for x in selected)
 reason={32:'Earlier exact-body gifted-stroller post already selected as rad03-0040; remove own candidate and cite existing evidence, never an independent buyer.',57:'Earlier beyondthebump instance is representative; assigned full source read but no excerpt selected.',92:'Earlier same-community post thirteen seconds before repeat is sole selected representative; both assigned bodies fully read.'}[number]
 D.append(dict(flag_group=number,assigned_ids=scope,representative_post_id=rep,selected_post_ids=selected,reason=reason))
 for p in scope:byid[p].update(duplicate_body_group=number,duplicate_representative_post_id=rep,independent_body_representative=(p==rep))
byid['1p3ytwt'].update(status='excluded_after_read',reason='Fully read exact-body gifted-stroller crosspost; earlier instance1p3ysdn already selected as rad03-0040. No additional quote or independent buyer.')
byid['1pks3um']['native_body_ends_mid_sentence']=True
for p,other in [('1p0vdph','1p6erl4'),('1p6erl4','1p0vdph')]:byid[p]['same_author_followup_post_id']=other
save(S/'duplicate-review.jsonl',D)
Q=[]
for number,a in enumerate(A,1):
 p=a['post_id'];n=N[p];i=I[p]
 q=dict(id=f'rad06-{number:04d}',source=f'Reddit r/{n["subreddit"]} (frozen public archive)',url='https://www.reddit.com'+n['permalink'],date=stamp(n['created_utc']),author=n['author'],speaker=a.get('speaker','parent_unspecified'),stage=a['stage'],type=a['type'],themes=a['themes'],quote=a['quote'],context=a['context'],raw_file=i['raw_file'],source_class='reddit_archive',evidence_kind='archived_original',archive_dataset='yikeee/reddit-subreddits25',archive_commit='ea497c510aa68765c07ed744ec9f84d68bbedf7f',post_id=p,read_scope='full_post_comment_source_unavailable',paid_report_demand_proven=False)
 for k in ['authenticity_note']:
  if k in a:q[k]=a[k]
 Q.append(q)
voice=R/'voice/reddit-augdec-06.jsonl';ledger=R/'sources/reddit-augdec-06-reading.jsonl';save(voice,Q)
for l in L:l['quote_ids']=[q['id'] for q in Q if q['post_id']==l['post_id']]
save(ledger,L)
E=[];checks=collections.Counter()
def check(ok,kind,detail):
 checks[kind]+=1
 if not ok:E.append(dict(category=kind,detail=detail))
check(len(assigned)==len(M['post_ids'])==M['assigned_full_units']==186,'assignment186','complete exact own assignment')
check(M['post_ids']==own['post_ids'] and own['units']==186,'partition_IDs','frozen root partition')
check(M['all_human_triage_complete'] is True,'inherited_triage_complete','root completed all620 cards')
check(sha(R/P['triage_file'])==P['triage_sha256'],'inherited_triage_hash',P['triage_file'])
T=list(csv.DictReader((R/P['triage_file']).open(),delimiter='\t'));kept={x['post_id'] for x in T if x['label']!='drop'}
check(len(T)==620 and len(kept)==432 and sum(x['label']=='drop' for x in T)==188,'inherited_triage_counts','no new triage counted')
check(assigned<=kept,'assigned_kept','all assigned previously human kept')
parts=[set(x['post_ids']) for x in P['partitions']]
check(set.union(*parts)==kept and sum(map(len,parts))==len(kept),'partition_union_disjoint','60+186+186=432')
check(len(L)==len(byid)==186 and set(byid)==assigned,'exact_read_ID_set','every own original once')
check(len(N)==186,'native_original_count','all native originals located')
for f in ['reddit-augdec-01-reading.jsonl','reddit-augdec-02-reading.jsonl','reddit-augdec-03-reading.jsonl','reddit-augdec-04-reading.jsonl','reddit-augdec-05-reading.jsonl','reddit-augdec-07-reading.jsonl']:
 p=R/'sources'/f
 if p.exists():check(not assigned&{x['post_id'] for x in jl(p)},'disjoint_other_readers',f)
check(len(M['chunks'])==36,'chunks36','all frozen chunks')
chunkids=[]
for c in M['chunks']:
 check(sha(R/c['file'])==c['sha256'],'chunk_hash',c['file']);text=(R/c['file']).read_text();sections=text.split('=== SOURCE ===\n')[1:];chunkids+=c['post_ids']
 check(len(sections)==len(c['post_ids']),'chunk_unit_count',c['file'])
 for section,u in zip(sections,c['units']):
  p=u['post_id'];i=I[p];raw=(R/i['raw_file']).read_text();meta=json.loads(section.split('\n',1)[0]);body_and_OP=raw.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1];title=raw.split('=== COMPLETE ORIGINAL POST TITLE ===\n',1)[1].split('\n=== COMPLETE ORIGINAL POST BODY ===',1)[0].strip()
  check(meta['post_id']==p and meta['title']==title and meta['date']==i['post_date'],'lean_title_metadata',p)
  check(('=== COMPLETE ORIGINAL POST BODY ===\n'+body_and_OP).strip() in section.strip(),'lean_complete_body_OP',p)
  check(u['sha256']==i['sha256']==sha(R/u['raw_file']) and u['raw_file']==i['raw_file'],'manifest_unit_hash',p)
check(chunkids==M['post_ids'],'chunk_exact_order_IDs','all186 once')
for p,l in byid.items():
 i=I[p];n=N[p];raw=(R/i['raw_file']).read_text();body=raw.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0].strip();title=raw.split('=== COMPLETE ORIGINAL POST TITLE ===\n',1)[1].split('\n=== COMPLETE ORIGINAL POST BODY ===',1)[0].strip()
 check(body==n.get('selftext','').replace('\r\n','\n').strip(),'native_whole_body',p)
 check(title==n['title'].strip(),'native_title',p)
 check(l['post_body_read_complete'] is True,'full_read_boolean',p)
 check(l['raw_file']==i['raw_file'] and l['primary_unit_sha256']==i['sha256']==sha(R/i['raw_file']),'ledger_unit_hash',p)
 check(not i['source_comment_file'] and i['comment_source_available'] is False and i['OP_replies']==l['available_identifiable_OP_replies_read']==0 and i['OP_comment_ids']==l['op_reply_ids_read']==[],'native_OP_source_count_IDs',p)
 check('--- OP REPLY ---' not in raw,'no_hidden_OP_section',p)
check(N['1p0vdph']['author']==N['1p6erl4']['author'],'same_author_update','earlier success versus later inconsistent results')
check(len(jl(aux))==0,'auxiliary_empty','no missing OP parents or auxiliary reading needed')
manual=json.loads((S/'manual-quote-audit.json').read_text())
check(manual['all_44_selected_quotes_contexts_and_roles_reviewed'] is True and manual['names_or_usernames_in_quote_or_context']==0,'manual_all_quote_review','44 quotes with contexts and conservative roles')
check(len(set(manual['source_comparison_sample_ids']))==20 and set(manual['source_comparison_sample_ids'])<={q['id'] for q in Q},'manual20_own_body_spotcheck','exact displayed sample IDs')
pattern=re.compile(manual['safety_regex'],re.I)
check({q['id'] for q in Q if pattern.search(q['quote'])}=={x['id'] for x in manual['safety_quote_hits_reviewed']},'manual_safety_hit_ID_set','all quote safety-sweep hits reviewed')
readme=(R/'README.md').read_text()
def vocab(label):return set(re.findall(r'`([^`]+)`',readme.split(label+':',1)[1].split('\n\n',1)[0]))
speakers=vocab('Speakers');stages=vocab('Stages');types=vocab('Types');themes=vocab('Seed themes');globalids=[x['id'] for f in (R/'voice').glob('*.jsonl') for x in jl(f)]
for q in Q:
 p=q['post_id'];n=N[p];b=n.get('selftext','');check(globalids.count(q['id'])==1,'global_quote_ID',q['id']);check(q['speaker'] in speakers and q['stage'] in stages and q['type'] in types and set(q['themes'])<=themes,'README_vocabulary',q['id']);check(len(q['context'].split())<=25,'context_words',q['id']);check(q['author']==n['author'] and q['date']==stamp(n['created_utc']) and q['url']=='https://www.reddit.com'+n['permalink'],'native_quote_metadata',q['id']);check(q['raw_file']==I[p]['raw_file'] and q['id'] in byid[p]['quote_ids'],'quote_ledger_link',q['id']);check(byid[p]['post_body_read_complete'] is True,'restricted_quote',q['id']);pos=0
 for part in q['quote'].split(' […] '):
  part=norm(part);at=norm(b).find(part,pos);check(at>=0,'native_own_body_quote',q['id']);pos=at+len(part)
 check('u/' not in q['quote']+q['context'] and n['author'] not in q['quote']+q['context'],'no_username_in_selection',q['id']);check(q['paid_report_demand_proven'] is False,'no_purchase_inference',q['id'])
notes=R/'synthesis/reader-notes-reddit-augdec-06.md';source=R/'sources/reddit-augdec-06.md';noteids=[]
for p in [notes,source]:
 if not p.exists():E.append(dict(category='notes_pending',detail=p.name));continue
 for identifier in re.findall(r'rad06-\d{4}',p.read_text()):noteids.append(identifier);check(identifier in {q['id'] for q in Q},'notes_ID_lookup',p.name+':'+identifier)
strict=subprocess.run([sys.executable,str(R/'_tools/verify_quotes.py'),str(voice)],capture_output=True,text=True);check(strict.returncode==0,'strict_verify_quotes',strict.stdout+strict.stderr)
counts=dict(inherited_root_cards=620,inherited_root_keeps=432,inherited_root_drops=188,new_triage_cards=0,assigned_full_read_keeps=186,full_original_posts=len(L),partial_reads=0,eligible_after_read=sum(x['status']=='eligible' for x in L),excluded_after_read=sum(x['status']=='excluded_after_read' for x in L),identifiable_OP_replies=0,auxiliary_non_OP_comments=0,original_posts_comment_source_available=0,original_posts_comment_source_unavailable=186,selected_excerpts=len(Q),selected_original_posts=len({q['post_id'] for q in Q}),selected_original_body_excerpts=len(Q),selected_OP_reply_excerpts=0,research_only_excerpts=sum(q.get('marketing_eligible') is False for q in Q),duplicate_groups_touching_transfer=len(D),selected_flagged_groups=sum(bool(x['selected_post_ids']) for x in D),unique_notes_IDs_checked=len(set(noteids)),notes_ID_occurrences_checked=len(noteids))
audit=dict(date='2026-10-24',scope='All186 entirely unopened root04 keeps transferred to06; root triage inherited, no extra cards.',counts=counts,reading_by_subreddit=dict(collections.Counter(I[p]['subreddit'] for p in assigned)),quote_balance=dict(speakers=dict(collections.Counter(q['speaker'] for q in Q)),stages=dict(collections.Counter(q['stage'] for q in Q)),types=dict(collections.Counter(q['type'] for q in Q))),counts_are_not_independent_buyers_or_prevalence=True,verified_standalone_report_purchases=0,checks=dict(checks),failed=len(E),errors=E,strict_verify_quotes_exit_code=strict.returncode,strict_verify_quotes_output=strict.stdout.strip(),limitations=['Archive authenticity, provenance, rights/license and live completeness unverified.','Both assigned communities lack comment sources; zero OP replies is unavailable source, not a live-thread claim.','External pages, videos and images were not inspected; all saved original text read.','Historical prices, features, policies and clinical outcomes are unverified author accounts.'],output_sha256={str(p.relative_to(R)):sha(p) for p in [voice,ledger,aux,S/'duplicate-review.jsonl',S/'manual-quote-audit.json',S/'selection-review.json',source,notes] if p.exists()},frozen_manifest_sha256=sha(S/'full-read-v1/manifest.json'),frozen_chunk_hashes={c['file']:sha(R/c['file']) for c in M['chunks']})
(R/'sources/reddit-augdec-06-verification.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(counts=counts,failed=len(E),errors=E[:30],strict=strict.stdout.strip()),ensure_ascii=False,indent=2))
