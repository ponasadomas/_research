# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
"""Finalize explicitly human-selected transfer05 evidence; no automatic triage."""
import collections,csv,datetime,gzip,hashlib,html,json,re,subprocess,sys
from pathlib import Path
S=Path(__file__).resolve().parent; R=S.parents[1]; W=R/'_raw/reddit-deep/aug-dec-2025-wave-v1'
def jl(p):return [json.loads(s) for s in p.read_text().splitlines() if s.strip()]
def save(p,a):p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in a))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+',' ',html.unescape(s).replace('\\n',' ')).strip()
def stamp(t):return datetime.datetime.fromtimestamp(int(t),datetime.timezone.utc).isoformat()
M=json.loads((W/'assignments/fullread-transfer-to-05-v1.json').read_text()); assigned=set(M['post_ids'])
I={x['post_id']:x for x in jl(W/'primary-index.jsonl')}; ledger_path=R/'sources/reddit-augdec-05-reading.jsonl'
L=jl(ledger_path); byid={x['post_id']:x for x in L}; A=jl(S/'selections.jsonl'); C=json.loads((S/'kept-chunks.json').read_text())
N={}
for f in sorted({I[p]['source_post_file'] for p in assigned}):
 with gzip.open(R/f,'rt') as stream:
  for line in stream:
   x=json.loads(line)
   if x['id'] in assigned:N[x['id']]=x
OP=collections.defaultdict(list); aux_path=R/'sources/reddit-augdec-05-auxiliary-read.jsonl'
if not aux_path.exists():aux_path.write_text('')
aux=jl(aux_path); aux_native={}
for f in sorted({I[p]['source_comment_file'] for p in assigned if I[p]['source_comment_file']}):
 with gzip.open(R/f,'rt') as stream:
  for line in stream:
   x=json.loads(line); p=x.get('link_id','').removeprefix('t3_')
   if x['id'] in {a['comment_id'] for a in aux}:aux_native[x['id']]=x
   if p not in assigned:continue
   author=N[p].get('author')
   if author and author not in {'[deleted]','[removed]'} and x.get('author')==author:OP[p].append(x)
for rows in OP.values():rows.sort(key=lambda x:(int(x['created_utc']),x['id']))
comment_byid={x['id']:x for rows in OP.values() for x in rows}

# All 13 touching groups were reviewed explicitly after full source reading.
reps={28:'1ovgli7',30:'1p0fkw8',43:'1ngovl6',60:'1ngjhqh',62:'1nnxxbs',63:'1nnwhlz',
      64:'1noaua5',69:'1o29z07',86:'1pm7hy9',93:'1n5kdk2',94:'1nutljq',95:'1ny0wj7',98:'1pqfadk'}
dup=[]
for number,g in enumerate(jl(W/'exact-body-duplicate-flags.jsonl'),1):
 ids={x['post_id'] for x in g['records']}; own=sorted(ids&assigned)
 if not own:continue
 rep=reps[number]; assert rep in ids
 selected=[x['post_id'] for x in A if x['post_id'] in ids]
 assert all(p==rep for p in selected)
 reason='Earliest dated body instance is the comparison representative; all assigned originals were still read, and repetitions cannot create independent buyers.'
 if number==63:reason='Earlier birthday-planning body selected; later reposts in other scopes do not add independent demand.'
 if number in {30,43,62,64,69,93,95}:reason+=' Historical clinical, safety or vulnerability reason is retained; the unit now needs ordinary topic review.'
 dup.append(dict(flag_group=number,assigned_ids=own,representative_post_id=rep,selected_post_ids=selected,reason=reason))
 for p in own:byid[p].update(duplicate_body_group=number,duplicate_representative_post_id=rep,independent_body_representative=(p==rep))
byid['1no3i3m']['near_duplicate_context_post_id']='1no3dzl'
byid['1p5qmvg']['native_body_ends_mid_sentence']=True
save(S/'duplicate-review.jsonl',dup)

Q=[]
for number,a in enumerate(A,1):
 p=a['post_id']; i=I[p]; original=N[p]; c=a.get('comment_id'); n=comment_byid[c] if c else original
 q=dict(id=f'rad05-{number:04d}',source=f'Reddit r/{original["subreddit"]} (frozen public archive)',
        url='https://www.reddit.com'+n['permalink'],date=stamp(n['created_utc']),author=n['author'],
        speaker='parent_unspecified',stage=a['stage'],type=a['type'],themes=a['themes'],quote=a['quote'],context=a['context'],
        raw_file=i['raw_file'],source_class='reddit_archive',evidence_kind='archived_original',
        archive_dataset='yikeee/reddit-subreddits25',archive_commit='ea497c510aa68765c07ed744ec9f84d68bbedf7f',post_id=p,
        read_scope='full_post_and_available_identifiable_OP_replies' if i['comment_source_available'] else 'full_post_comment_source_unavailable',
        paid_report_demand_proven=False)
 if c:q['comment_id']=c
 for k in ['authenticity_note']:
  if k in a:q[k]=a[k]
 Q.append(q)
voice_path=R/'voice/reddit-augdec-05.jsonl'; save(voice_path,Q)
for row in L:row['quote_ids']=[q['id'] for q in Q if q['post_id']==row['post_id']]
save(ledger_path,L)

E=[];checks=collections.Counter()
def check(ok,kind,detail):
 checks[kind]+=1
 if not ok:E.append(dict(category=kind,detail=detail))
check(len(assigned)==354 and len(M['post_ids'])==354,'assignment','354 unique transferred originals')
check(len(L)==len(byid)==354 and set(byid)==assigned,'exact_read_ID_set','Every transferred keep once')
check(len(M['chunks'])==len(C)==25,'frozen_chunks','all25chunks073–097')
check(sha(R/M['source_kept_manifest'])==M['source_manifest_sha256'],'source_manifest_hash','donor frozen manifest')
check(len(N)==354,'native_posts','all original submissions located')
units={u['post_id']:u for u in M['units']}
other02={x['post_id'] for x in jl(R/'sources/reddit-augdec-02-reading.jsonl')}
check(not assigned&other02,'disjoint_reading','no original batch02 overlap')
donor=R/'sources/reddit-augdec-01-reading.jsonl'
if donor.exists():check(not assigned&{x['post_id'] for x in jl(donor)},'disjoint_reading','no donor01 original read overlap')
for dc,c in zip(M['chunks'],C):
 check(sha(R/dc['file'])==dc['sha256'],'donor_chunk_hash',dc['file'])
 check(sha(S/c['file'])==c['sha256'],'lean_chunk_hash',c['file'])
 check(dc['post_ids']==c['ids'],'lean_chunk_IDs',c['file'])
 text=(S/c['file']).read_text()
 for p in c['ids']:
  raw=(R/I[p]['raw_file']).read_text(); complete=raw[raw.index('=== COMPLETE ORIGINAL POST TITLE ==='):]
  check(complete in text,'lean_complete_unit',p)
for p,l in byid.items():
 i=I[p];n=N[p];raw=(R/i['raw_file']).read_text()
 check(l['post_body_read_complete'] is True,'full_read_boolean',p)
 check(l['raw_file']==i['raw_file'] and l['primary_unit_sha256']==i['sha256']==units[p]['sha256']==sha(R/i['raw_file']),'unit_hash',p)
 body=raw.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0].strip()
 title=raw.split('=== COMPLETE ORIGINAL POST TITLE ===\n',1)[1].split('\n=== COMPLETE ORIGINAL POST BODY ===',1)[0].strip()
 # Path.read_text normalizes CRLF; normalize that exact transport distinction only.
 check(body==n.get('selftext','').replace('\r\n','\n').strip(),'native_whole_body',p)
 check(title==n.get('title','').strip(),'native_title',p)
 ids=[x['id'] for x in OP[p]]
 check(ids==l['op_reply_ids_read']==i['OP_comment_ids'] and len(ids)==l['available_identifiable_OP_replies_read']==i['OP_replies'],'native_OP_ID_count',p)
 sections=raw.split('--- OP REPLY ---\n')[1:];check(len(sections)==len(ids),'native_OP_sections',p)
 for section,c in zip(sections,OP[p]):
  meta,b=section.split('\n',1); meta=json.loads(meta)
  check(b.strip()==c.get('body','').strip(),'native_OP_whole_body',c['id'])
  check(meta['comment_id']==c['id'] and meta['date']==stamp(c['created_utc']) and meta['parent_id']==c.get('parent_id'),'native_OP_metadata',c['id'])
  check(c['author']==n['author'] and n['author'] not in {'[deleted]','[removed]'},'native_OP_author',c['id'])
for a in aux:
 n=aux_native.get(a['comment_id']);check(n is not None,'aux_native_ID',a['comment_id'])
 if n:
  check(a['body_read_complete'] is True and a['date']==stamp(n['created_utc']) and a['url']=='https://www.reddit.com'+n['permalink'] and a['parent_id']==n.get('parent_id'),'aux_metadata',a['comment_id'])
  check(n['author']!=N[a['post_id']]['author'],'aux_non_OP',a['comment_id'])
readme=(R/'README.md').read_text()
def vocab(label):return set(re.findall(r'`([^`]+)`',readme.split(label+':',1)[1].split('\n\n',1)[0]))
speakers=vocab('Speakers');stages=vocab('Stages');types=vocab('Types');themes=vocab('Seed themes')
globalids=[x['id'] for f in (R/'voice').glob('*.jsonl') for x in jl(f)]
for q in Q:
 p=q['post_id'];n=comment_byid[q['comment_id']] if q.get('comment_id') else N[p];body=n.get('body','') if q.get('comment_id') else n.get('selftext','')
 check(globalids.count(q['id'])==1,'global_quote_ID',q['id'])
 check(q['speaker'] in speakers and q['stage'] in stages and q['type'] in types and set(q['themes'])<=themes,'README_vocabulary',q['id'])
 check(len(q['context'].split())<=25,'context_words',q['id'])
 check(q['author']==n['author'] and q['date']==stamp(n['created_utc']) and q['url']=='https://www.reddit.com'+n['permalink'],'native_quote_metadata',q['id'])
 check(q['raw_file']==I[p]['raw_file'] and q['id'] in byid[p]['quote_ids'],'quote_ledger_link',q['id'])
 check(byid[p]['post_body_read_complete'] is True,'restricted_quote',q['id'])
 pos=0
 for part in q['quote'].split(' […] '):
  part=norm(part);at=norm(body).find(part,pos);check(at>=0,'native_own_body_quote',q['id']+': '+part[:80]);pos=at+len(part)
 check('u/' not in q['quote']+q['context'] and n['author'] not in q['quote']+q['context'],'no_username_in_selection',q['id'])
 check(not q['paid_report_demand_proven'],'no_purchase_inference',q['id'])
source=R/'sources/reddit-augdec-05.md';notes=R/'synthesis/reader-notes-reddit-augdec-05.md';noteids=[]
for p in [source,notes]:
 if not p.exists():E.append(dict(category='notes_pending',detail=p.name));continue
 for identifier in re.findall(r'rad05-\d{4}',p.read_text()):
  noteids.append(identifier);check(identifier in {q['id'] for q in Q},'notes_ID_lookup',p.name+':'+identifier)
strict=subprocess.run([sys.executable,str(R/'_tools/verify_quotes.py'),str(voice_path)],capture_output=True,text=True)
check(strict.returncode==0,'strict_verify_quotes',strict.stdout+strict.stderr)
counts=dict(transferred_keeps=354,new_triage_cards=0,full_original_posts=len(L),partial_reads=0,
            eligible_after_read=sum(x['status']=='eligible' for x in L),excluded_after_read=sum(x['status']=='excluded_after_read' for x in L),
            identifiable_OP_replies=sum(len(x) for x in OP.values()),auxiliary_non_OP_comments=len(aux),
            original_posts_comment_source_available=sum(I[p]['comment_source_available'] for p in assigned),
            original_posts_comment_source_unavailable=sum(not I[p]['comment_source_available'] for p in assigned),
            selected_excerpts=len(Q),selected_original_posts=len({q['post_id'] for q in Q}),
            selected_original_body_excerpts=sum(not q.get('comment_id') for q in Q),selected_OP_reply_excerpts=sum(bool(q.get('comment_id')) for q in Q),
            research_only_excerpts=sum(q.get('marketing_eligible') is False for q in Q),duplicate_groups_touching_transfer=len(dup),
            selected_flagged_groups=sum(bool(x['selected_post_ids']) for x in dup),unique_notes_IDs_checked=len(set(noteids)),notes_ID_occurrences_checked=len(noteids))
audit=dict(date='2026-10-24',scope='All354 transferred already-triaged donor01 keeps in073–097; no extra triage cards.',counts=counts,
           reading_by_subreddit=dict(collections.Counter(I[p]['subreddit'] for p in assigned)),
           counts_are_not_independent_buyers_or_prevalence=True,verified_standalone_report_purchases=0,
           checks=dict(checks),failed=len(E),errors=E,strict_verify_quotes_exit_code=strict.returncode,strict_verify_quotes_output=strict.stdout.strip(),
           limitations=['Archive author authenticity, rights/provenance/license and live completeness unverified.',
                        'No all-live-thread or all-non-OP-comment reading claimed; only exact auxiliary parent nqm8v8h was added.',
                        'Linked external images, videos and product pages were not inspected; all available native post/reply text was read.',
                        'Historical prices, institutional policies, benefits and app features are author claims, not current advice.'],
           output_sha256={str(p.relative_to(R)):sha(p) for p in [voice_path,ledger_path,aux_path,S/'duplicate-review.jsonl',source,notes] if p.exists()},
           frozen_chunk_hashes={c['file']:sha(S/c['file']) for c in C})
(R/'sources/reddit-augdec-05-verification.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(counts=counts,failed=len(E),errors=E[:20],strict=strict.stdout.strip()),ensure_ascii=False,indent=2))
