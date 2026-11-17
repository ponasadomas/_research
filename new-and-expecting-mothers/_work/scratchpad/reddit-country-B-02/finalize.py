# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
"""Finalize explicit human triage/full reads; no machine semantic classification."""
import collections,csv,datetime,gzip,hashlib,html,json,re,subprocess,sys
from pathlib import Path
S=Path(__file__).resolve().parent;R=S.parents[1];W=R/'_raw/reddit-deep/next-july-country-B-v1';P=W/'primary-v1';M=json.loads((P/'assignments/batch-02.json').read_text());C=json.loads((S/'card-views.json').read_text());K=json.loads((S/'kept-manifest.json').read_text());I={x['post_id']:x for x in map(json.loads,(P/'primary-index.jsonl').read_text().splitlines())}
def jl(p):return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
def save(p,a):p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in a))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def stamp(t):return datetime.datetime.fromtimestamp(int(t),datetime.timezone.utc).isoformat()
def norm(s):return re.sub(r'\s+',' ',html.unescape(s).replace('\\n',' ')).strip()
Tpath=R/'_raw/reddit-deep/triage/country-B-02.tsv';T=list(csv.DictReader(Tpath.open(),delimiter='\t'));Lpath=R/'sources/reddit-country-B-02-reading.jsonl';L=jl(Lpath);byid={x['post_id']:x for x in L};assigned=set(M['post_ids']);kept={x['post_id'] for x in T if x['label']!='drop'};N={};A=jl(S/'selections.jsonl')
for source in {I[p]['source_post_file'] for p in kept}:
 with gzip.open(R/source,'rt') as f:
  for line in f:
   n=json.loads(line)
   if n['id'] in kept:N[n['id']]=n
D=[];reps={11:'1lxxg7n',17:'1lynnxs'}
for number,g in enumerate(jl(P/'duplicate-flags.jsonl'),1):
 ids={x['post_id'] for x in g['records']};own=sorted(ids&kept)
 if not own:continue
 rep=reps[number];selected=[a['post_id'] for a in A if a['post_id'] in ids];assert not selected
 reason='Earlier assigned country-community body is representative. Every assigned keep fully read; no quote chosen, no independent buyer from repetition.'
 if number==17:reason+=' Assigned source remains excluded for its individually recorded feeding/safe-eating reason.'
 D.append(dict(flag_group=number,assigned_ids=own,representative_post_id=rep,selected_post_ids=selected,reason=reason))
 for p in own:byid[p].update(duplicate_body_group=number,duplicate_representative_post_id=rep,independent_body_representative=(p==rep))
for a,b in [('1m0bn9h','1m0dm42'),('1m0dm42','1m0bn9h')]:byid[a]['near_duplicate_same_native_author_post_id']=b
for a,b in [('1mcneqd','1mclx71'),('1mclx71','1mcneqd')]:byid[a]['related_same_native_author_post_id']=b
save(S/'duplicate-review.jsonl',D)
aux=R/'sources/reddit-country-B-02-auxiliary-read.jsonl';extra=R/'sources/reddit-country-B-02-extra-inspections.jsonl'
for p in [aux,extra]:
 if not p.exists():p.write_text('')
Q=[]
for number,a in enumerate(A,1):
 p=a['post_id'];n=N[p];q=dict(id=f'rcb02-{number:04d}',source=f'Reddit r/{n["subreddit"]} (frozen public archive)',url='https://www.reddit.com'+n['permalink'],date=stamp(n['created_utc']),author=n['author'],speaker=a.get('speaker','parent_unspecified'),stage=a['stage'],type=a['type'],themes=a['themes'],quote=a['quote'],context=a['context'],raw_file=I[p]['raw_file'],source_class='reddit_archive',evidence_kind='archived_original',archive_dataset='yikeee/reddit-subreddits25',archive_commit='ea497c510aa68765c07ed744ec9f84d68bbedf7f',post_id=p,read_scope='full_post_comment_source_unavailable',paid_customized_report_purchase_proven=False)
 for k in ['authenticity_note']:
  if k in a:q[k]=a[k]
 Q.append(q)
voice=R/'voice/reddit-country-B-02.jsonl';save(voice,Q)
for l in L:l['quote_ids']=[q['id'] for q in Q if q['post_id']==l['post_id']]
save(Lpath,L)
E=[];checks=collections.Counter()
def check(ok,kind,detail):
 checks[kind]+=1
 if not ok:E.append(dict(category=kind,detail=detail))
check(len(assigned)==M['cards']==264 and len(M['post_ids'])==264,'assigned264','exact own card set')
check(len(T)==264 and {x['post_id'] for x in T}==assigned,'triage_exact_ID_set','all cards once')
check(len(L)==len(byid)==len(kept)==157 and set(byid)==kept,'kept_read_exact_ID_set','every keep once')
check(len(N)==157,'native157','all kept native originals located')
check(sha(Tpath)==K['triage_sha256'],'triage_hash','frozen prior to full reads')
for c in M['chunks']:check(sha(R/c['file'])==c['sha256'],'original_card_chunk_hash',c['file'])
viewtext=''.join((S/c['file']).read_text() for c in C)
for c in C:check(sha(S/c['file'])==c['sha256'],'card_view_hash',c['file'])
for c in M['chunks']:
 for card in re.split(r'\n\n(?=ID )',(R/c['file']).read_text()):check(card.strip() in viewtext,'complete_card_view',re.match(r'ID (\S+)',card).group(1))
check([p for c in C for p in c['ids']]==M['post_ids'],'card_view_exact_order','264cards')
for t in T:check(t['card_file']==next(c['file'] for c in M['chunks'] if t['post_id'] in c['post_ids']) and bool(t['reason']),'triage_card_link',t['post_id'])
for c in K['chunks']:
 check(sha(S/c['file'])==c['sha256'],'kept_view_hash',c['file']);text=(S/c['file']).read_text()
 for p in c['ids']:
  raw=(R/I[p]['raw_file']).read_text();check(raw[raw.index('=== COMPLETE ORIGINAL POST TITLE ==='):] in text,'complete_unit_in_view',p)
check([p for c in K['chunks'] for p in c['ids']]==K['post_ids'] and set(K['post_ids'])==kept,'kept_views_exact_IDs','14frozenchunks')
for p,l in byid.items():
 i=I[p];n=N[p];raw=(R/i['raw_file']).read_text();body=raw.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0].strip();title=raw.split('=== COMPLETE ORIGINAL POST TITLE ===\n',1)[1].split('\n=== COMPLETE ORIGINAL POST BODY ===',1)[0].strip()
 check(l['post_body_read_complete'] is True,'full_read_boolean',p);check(l['raw_file']==i['raw_file'] and l['primary_unit_sha256']==i['sha256']==sha(R/i['raw_file']),'primary_unit_hash',p);check(body==n.get('selftext','').replace('\r\n','\n').strip(),'native_whole_body',p);check(title==n['title'].strip(),'native_title',p);check(i['url']=='https://www.reddit.com'+n['permalink'] and i['post_date']==stamp(n['created_utc']),'native_unit_date_URL',p);check(i['comment_source_available'] is False and not i['source_comment_file'] and i['OP_replies']==l['available_identifiable_OP_replies_read']==0 and i['OP_comment_ids']==l['op_reply_ids_read']==[] and '--- OP REPLY ---' not in raw,'unavailable_OP_source_count_IDs',p)
baseline_path=R/'_raw/reddit-deep/continuation-v1/final-read-post-ids.json';baseline=set(json.loads(baseline_path.read_text())['full_original_post_ids']);check(len(baseline)==5879 and not assigned&baseline,'baseline5879_disjoint','authoritative baseline ID set')
for f in (R/'sources').glob('*reading.jsonl'):
 if f==Lpath:continue
 rows=jl(f);overlap=kept&{x.get('post_id') for x in rows if x.get('post_body_read_complete') is True};check(not overlap,'other_complete_read_disjoint',f.name+':'+str(sorted(overlap)))
for a,b in [('1m0bn9h','1m0dm42'),('1mcneqd','1mclx71')]:check(N[a]['author']==N[b]['author'] and N[a]['author'] not in {'[deleted]','[removed]'},'native_author_dependence',a+':'+b)
readme=(R/'README.md').read_text()
def vocab(label):return set(re.findall(r'`([^`]+)`',readme.split(label+':',1)[1].split('\n\n',1)[0]))
speakers=vocab('Speakers');stages=vocab('Stages');types=vocab('Types');themes=vocab('Seed themes');allq=[x for f in (R/'voice').glob('*.jsonl') for x in jl(f)];ids=[x['id'] for x in allq]
for q in Q:
 p=q['post_id'];n=N[p];check(ids.count(q['id'])==1,'global_quote_ID',q['id']);check(q['speaker'] in speakers and q['stage'] in stages and q['type'] in types and set(q['themes'])<=themes,'README_vocab',q['id']);check(len(q['context'].split())<=25,'context_words',q['id']);check(q['author']==n['author'] and q['url']=='https://www.reddit.com'+n['permalink'] and q['date']==stamp(n['created_utc']),'native_quote_metadata',q['id']);check(q['raw_file']==I[p]['raw_file'] and q['id'] in byid[p]['quote_ids'],'quote_ledger_link',q['id']);check(byid[p]['post_body_read_complete'] is True,'restricted_status',q['id']);check('u/' not in q['quote']+q['context'] and n['author'] not in q['quote']+q['context'],'no_username_selection',q['id']);pos=0
 for part in q['quote'].split(' […] '):
  part=norm(part);at=norm(n['selftext']).find(part,pos);check(at>=0,'native_own_body_quote',q['id']);pos=at+len(part)
 check(not any(x.get('post_id')==p and not x['id'].startswith('rcb02-') for x in allq),'no_existing_work_quote',q['id'])
check(not jl(aux) and not jl(extra),'no_unclaimed_extra_inspections','no card-drop body or nonOP comment opened')
notes=R/'synthesis/reader-notes-reddit-country-B-02.md';source=R/'sources/reddit-country-B-02.md';noteids=[]
for p in [notes,source]:
 if not p.exists():E.append(dict(category='notes_pending',detail=p.name));continue
 for identifier in re.findall(r'rcb02-\d{4}',p.read_text()):noteids.append(identifier);check(identifier in {q['id'] for q in Q},'notes_ID_lookup',p.name+':'+identifier)
manual=S/'manual-quote-audit.json'
if manual.exists():
 a=json.loads(manual.read_text());check(len(set(a['spotcheck_ids']))==20 and set(a['spotcheck_ids'])<={q['id'] for q in Q},'manual20_IDs','actual displayed own-body sample');check(a['all_quotes_contexts_roles_reviewed'] is True,'manual_all_review','47selectedexcerpts');check({q['id'] for q in Q if re.search(a['safety_regex'],q['quote'],re.I)}==set(a['safety_hits_reviewed']),'manual_safety_hit_set','every quote regex hit inspected')
else:E.append(dict(category='manual_audit_pending',detail=manual.name))
strict=subprocess.run([sys.executable,str(R/'_tools/verify_quotes.py'),str(voice)],capture_output=True,text=True);check(strict.returncode==0,'strict_verify_quotes',strict.stdout+strict.stderr)
counts=dict(parent_prepared_cards=847,assigned_cards=264,triaged_cards=len(T),card_drops=sum(x['label']=='drop' for x in T),kept_originals=len(kept),full_original_posts=len(L),partial_reads=0,eligible_after_read=sum(x['status']=='eligible' for x in L),excluded_after_read=sum(x['status']=='excluded_after_read' for x in L),available_identifiable_OP_replies=0,auxiliary_non_OP_reads=0,extra_card_drop_body_reads=0,selected_excerpts=len(Q),selected_original_posts=len({q['post_id'] for q in Q}),research_only_excerpts=sum(q.get('marketing_eligible') is False for q in Q),duplicate_groups_touching_keeps=len(D),duplicate_groups_selected=0,unique_notes_IDs=len(set(noteids)),notes_ID_occurrences=len(noteids))
audit=dict(date='2026-10-24',counts=counts,triage_by_label=dict(collections.Counter(x['label'] for x in T)),assigned_by_subreddit=dict(collections.Counter(I[p]['subreddit'] for p in assigned)),full_reads_by_subreddit=dict(collections.Counter(I[p]['subreddit'] for p in kept)),quote_balance=dict(speakers=dict(collections.Counter(q['speaker'] for q in Q)),stages=dict(collections.Counter(q['stage'] for q in Q))),verified_standalone_customized_report_purchases=0,counts_are_not_people_independent_buyers_or_prevalence=True,checks=dict(checks),failed=len(E),errors=E,strict_exit_code=strict.returncode,strict_output=strict.stdout.strip(),baseline5879_sha256=sha(baseline_path),output_sha256={str(p.relative_to(R)):sha(p) for p in [voice,Lpath,Tpath,aux,extra,S/'duplicate-review.jsonl',source,notes,manual] if p.exists()},frozen_card_views={c['file']:sha(S/c['file']) for c in C},frozen_kept_views={c['file']:sha(S/c['file']) for c in K['chunks']},limitations=['Public archive rights/provenance, author authenticity and live completeness unverified.','Country comment files unavailable; zero saved OP replies is absence of source, not live followup completeness.','Linked images and external pages not inspected; every assigned kept saved original read completely.','Historical policy, price, feature and clinical claims not current advice.'])
(R/'sources/reddit-country-B-02-verification.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(counts=counts,failed=len(E),errors=E[:20],strict=strict.stdout.strip()),ensure_ascii=False,indent=2))
