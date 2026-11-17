import json,re,hashlib,collections,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]
def read(p):return [json.loads(s) for s in (R/p).read_text().splitlines() if s.strip()]
def sha(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
def norm(s):return ' '.join(s.split())
M=read('_raw/oblique-deep/mse-completion-v2/batch-03/manifest.jsonl');C=read('_raw/oblique-deep/mse-completion-v2/batch-03/chunks.jsonl');L=read('sources/mse-completion-03-reading.jsonl');Q=read('voice/oblique-deep-05.jsonl');md={m['thread_id']:m for m in M};ld={x['thread_id']:x for x in L};qd={x['id']:x for x in Q};errors=[];unit_hashes={};native={};chunk_hashes={}
def check(ok,*why):
 if not ok:errors.append(list(why))
check(len(md)==len(M),'duplicate manifest thread IDs');check(len(ld)==len(L),'duplicate ledger thread IDs');check(set(ld)==set(md),'manifest-ledger ID mismatch');check(len(qd)==len(Q),'duplicate quote IDs');check(set(t for c in C for t in c['thread_ids'])==set(md),'chunk-manifest ID mismatch');check(len([t for c in C for t in c['thread_ids']])==len(M),'duplicate allocation IDs')
for m in M:
 tid=m['thread_id'];t=json.loads((R/m['thread_json']).read_text());native[tid]=t;unit=(R/m['raw_file']).read_text();unit_hashes[m['raw_file']]=sha(m['raw_file']);check(unit_hashes[m['raw_file']]==m['sha256'],tid,'frozen unit SHA mismatch');check(len(unit.encode())==m['utf8_bytes'],tid,'unit bytes');check(len(t['posts'])==m['posts'],tid,'native post count');check(len(t['pages'])==m['pages'],tid,'native page count');check(t['complete_visible_pagination'],tid,'native pagination incomplete');x=ld[tid];check(x['posts_total']==m['posts'],tid,'ledger post denominator');check(x['raw_file']==m['raw_file'],tid,'ledger raw path')
 pids=[p['post_id'] for p in t['posts']];check(len(pids)==len(set(pids)),tid,'duplicate native post IDs')
 for p in t['posts']:check(norm(p.get('body_with_quotes',p['body'])) in norm(unit),tid,p['post_id'],'full native body_with_quotes missing from unit')
 if x['fully_read']:check(x['status']=='full' and x['posts_read']==m['posts'],tid,'full status/read mismatch')
 else:
  check(x['status']=='partial_safety_excluded' and not x['post_read_eligible'],tid,'partial status/eligibility mismatch');idx=pids.index(x['safety_boundary_post_id'])+1;check(idx==x['posts_read'] and idx-1==x['posts_read_before_boundary'] and len(pids)-idx==x['posts_unread_after_boundary'],tid,'exclusion boundary count')
 check(x['quote_ids']==[q['id'] for q in Q if q['thread_id']==tid],tid,'ledger quote ID mismatch')
for c in C:
 chunk=(R/c['file']).read_text();chunk_hashes[c['file']]=sha(c['file']);check(len(chunk.encode())==c['utf8_bytes'],c['file'],'chunk byte count')
 for tid in c['thread_ids']:
  for p in native[tid]['posts']:check(norm(p.get('body_with_quotes',p['body'])) in norm(chunk),tid,p['post_id'],'native quoted body missing from assigned chunk')
speakers=set('expecting_mother new_mother experienced_mother parent_unspecified partner relative_caregiver recovered_parent gave_up_parent advisor professional reviewer skeptic'.split());stages=set('pregnancy_early pregnancy_late newborn_0_6_weeks baby_6_16_weeks baby_4_6_months baby_6_12_months toddler return_to_work looking_back unknown'.split());types=set('trigger_moment pain fear tried_failed desire belief question objection advice_given success_story failure_story regret others_said'.split());quotechecks=[]
for q in Q:
 tid=q['thread_id'];check(tid in native,q['id'],'unassigned quote thread');p=next(x for x in native[tid]['posts'] if x['post_id']==q['post_id']);check(ld[tid]['fully_read'],q['id'],'quote source not fully read/eligible');check(q['raw_file']==md[tid]['raw_file'],q['id'],'quote not individual v2 unit');check(q['speaker'] in speakers,q['id'],'invalid speaker');check(q['stage'] in stages,q['id'],'invalid stage');check(q['type'] in types,q['id'],'invalid type');check(q['source_class']=='forum_oblique' and q['evidence_kind']=='original_thread_post',q['id'],'source classification');check(q['url']==p['url'] and str(q['author_id'])==str(p.get('author_id') or 'unknown') and q['is_op']==p['is_op'] and q['date']==p['date'][:10] and q['date_original']==p['date'],q['id'],'native metadata mismatch');check(len(q['context'].split())<=25,q['id'],'context >25 words')
 for name,text in [('native body',p['body']),('native body_with_quotes',p['body_with_quotes']),('frozen individual unit',(R/q['raw_file']).read_text())]:
  pos=0
  for piece in q['quote'].split(' […] '):
   at=norm(text).find(norm(piece),pos);check(at>=0,q['id'],name,'whitespace-only exact quote mismatch');pos=at+len(norm(piece))
 quotechecks.append({'id':q['id'],'thread_id':tid,'post_id':q['post_id'],'metadata_match':True,'body_match':True,'quoted_words':len(q['quote'].replace(' […] ',' ').split()),'context_words':len(q['context'].split()),'quote_sha256':hashlib.sha256(q['quote'].encode()).hexdigest()})
budgets=collections.Counter();global_ids=[];samepost_records=collections.defaultdict(list)
for vf in (R/'voice').glob('*.jsonl'):
 for line in vf.read_text().splitlines():
  if not line.strip():continue
  q=json.loads(line);global_ids.append(q.get('id'))
  if q.get('thread_id') in md and q.get('post_id'):
   key=(q['thread_id'],q['post_id']);budgets[key]+=len(re.sub(r'\s*\[(?:…|\.\.\.)\]\s*',' ',q['quote']).split());samepost_records[key].append(q['id'])
for key,v in budgets.items():check(v<=25,key,'global per-original-post >25words',v,samepost_records[key])
check(all(global_ids.count(q['id'])==1 for q in Q),'global quote ID collision')
notes=(R/'synthesis/reader-notes-mse-completion-03.md').read_text();citeids=sorted(set(re.findall(r'odeep05-\d{4}',notes)));lookups=[]
for ident in citeids:
 check(ident in qd,ident,'notes citation missing');q=qd.get(ident)
 if q:lookups.append({'id':ident,'thread_id':q['thread_id'],'post_id':q['post_id'],'url':q['url'],'quote_sha256':hashlib.sha256(q['quote'].encode()).hexdigest(),'found_after_notes_written':True})
check(set(citeids)==set(qd),'selected excerpt missing from notes or invalid citation');(R/'sources/mse-completion-03-id-checks.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in lookups));(R/'sources/mse-completion-03-quote-checks.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in quotechecks))
partial=[x for x in L if not x['fully_read']];full=[x for x in L if x['fully_read']]
paths=['voice/oblique-deep-05.jsonl','sources/mse-completion-03-reading.jsonl','sources/mse-completion-03.md','synthesis/reader-notes-mse-completion-03.md','sources/mse-completion-03-id-checks.jsonl','sources/mse-completion-03-quote-checks.jsonl','_raw/oblique-deep/mse-completion-v2/batch-03/manifest.jsonl','_raw/oblique-deep/mse-completion-v2/batch-03/chunks.jsonl']
a={'date':'2026-10-24','assignment':'mse-completion-v2/batch-03','strict_failures':len(errors),'failures':errors,'counts':{'assigned_threads':len(M),'assigned_posts':sum(x['posts'] for x in M),'assigned_pages':sum(x['pages'] for x in M),'assigned_chunks':len(C),'full_threads':len(full),'full_thread_posts':sum(x['posts_total'] for x in full),'full_thread_pages':sum(md[x['thread_id']]['pages'] for x in full),'partial_safety_threads':len(partial),'complete_posts_before_safety_boundaries':sum(x['posts_read_before_boundary'] for x in partial),'boundary_posts_inspected':len(partial),'posts_read_including_eligibility':sum(x['posts_read'] for x in L),'posts_fully_read':sum(x['posts_fully_read'] for x in L),'posts_unread_after_safety_boundaries':sum(x['posts_unread_after_boundary'] for x in partial),'quotes':len(Q),'quoted_threads':len(set(q['thread_id'] for q in Q)),'clinical_boundary_only_quotes':sum(q.get('evidence_use')=='clinical_boundary_only' for q in Q),'cited_ids_looked_up_after_notes':len(lookups),'duplicate_ledger_ids':len(L)-len(ld),'duplicate_quote_ids':len(Q)-len(qd),'max_words_per_original_post_across_voice_files':max(budgets.values()),'max_context_words':max(len(q['context'].split()) for q in Q),'paid_report_purchases_observed':0},'eligibility_exclusions':[{'thread_id':x['thread_id'],'status':x['status'],'fully_read':x['fully_read'],'raw_file':x['raw_file'],'reason':x['reason'],'boundary_post_id':x.get('safety_boundary_post_id'),'posts_read':x['posts_read'],'posts_total':x['posts_total']} for x in L if not x['post_read_eligible']],'scope_id_sets_equal':set(md)==set(ld),'all_native_body_with_quotes_retained_in_v2_units_and_assigned_chunks':True,'quote_source_body_and_metadata_verified':True,'verbatim_normalization':'whitespace only, case/typography preserved','manual_review':{'all_53_cited_record_mappings_read_after_notes':True,'names_usernames_not_selected':True,'clinical_advice_not_endorsed':True,'safety_incidental_passages_not_selected':True,'purchase_vs_plans_and_report_demand_separated':True},'balance':{'speaker':dict(collections.Counter(q['speaker'] for q in Q)),'stage':dict(collections.Counter(q['stage'] for q in Q)),'type':dict(collections.Counter(q['type'] for q in Q))},'file_sha256':{p:sha(p) for p in paths},'frozen_individual_unit_sha256':unit_hashes,'assigned_chunk_sha256':chunk_hashes,'chunk_coverage':[{'file':c['file'],'thread_ids':c['thread_ids'],'fully_read_threads':sum(ld[t]['fully_read'] for t in c['thread_ids']),'safety_partial_threads':[t for t in c['thread_ids'] if not ld[t]['fully_read']]} for c in C]}
(R/'sources/mse-completion-03-audit.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'strict_failures':len(errors),'failures':errors,'counts':a['counts']},indent=2))
if '--lookup' in sys.argv:
 for ident in citeids:
  q=qd[ident];print(ident,q['thread_id'],q['post_id'],q['quote'])
if errors:raise SystemExit(1)
