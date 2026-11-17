import json,re,hashlib,collections
from pathlib import Path
R=Path(__file__).resolve().parents[2]
read=lambda p:[json.loads(x) for x in (R/p).read_text().splitlines()]
manifest=read('_raw/oblique-deep/geo-complete-context-v1/manifest.jsonl');chunks=read('_raw/oblique-deep/geo-complete-context-v1/chunks.jsonl');ledger=read('sources/geobaby-deep-reading.jsonl');v=read('voice/oblique-deep-02.jsonl')
m={x['thread_id']:x for x in manifest};l={x['thread_id']:x for x in ledger};err=[];budget=collections.Counter();ids=[];postcache={}
check=lambda b,*why:err.append(why) if not b else None
norm=lambda s:' '.join(s.split())
check(set(m)==set(l),'ledger manifest set mismatch');check(len(ledger)==len(l),'duplicate ledger threads')
check({t for c in chunks for t in c['thread_ids']}==set(m),'chunk manifest sets differ')
oldindex=read('_raw/oblique-deep/corpus/geo-chunks.jsonl')
check({t for c in oldindex for t in c['thread_ids']}==set(m),'original capture index ID set differs')
chunktext={t:(R/c['file']).read_text() for c in chunks for t in c['thread_ids']}
for c in chunks:check((R/c['file']).stat().st_size==c['bytes'],c['file'],'chunk byte count')
for t,x in m.items():
 data=(R/x['raw_file']).read_bytes();check(hashlib.sha256(data).hexdigest()==x['sha256'],t,'frozen unit hash')
 d=json.loads((R/x['thread_json']).read_text());postcache[t]={p['post_id']:p for p in d['posts']}
 check(x['posts']==len(d['posts'])==l[t]['posts'],t,'post counts');check(x['pages']==len(d['pages'])==l[t]['pages'],t,'page counts')
 check(l[t]['all_posts_and_op_followups_read'] and l[t]['quoted_context_read'],t,'incomplete read')
 for p in d['posts']:
  check(norm(p['body_with_quotes']) in norm(data.decode()),t,p['post_id'],'full quoted body missing from unit')
  check(norm(p['body_with_quotes']) in norm(chunktext[t]),t,p['post_id'],'full quoted body missing from assigned chunk')
for q in v:
 ids.append(q['id']);t=q['thread_id'];p=postcache[t][q['post_id']]
 check(norm(q['quote']) in norm(p['body']),q['id'],'not author-owned body')
 check(norm(q['quote']) in norm((R/q['raw_file']).read_text()),q['id'],'not frozen unit')
 check(q['raw_file']==m[t]['raw_file'],q['id'],'wrong unit')
 check(q['url']==p['url'] and q['date']==p['date'] and q['is_op']==p['is_op'] and q['author_id']==p['author_id'],q['id'],'provenance mismatch')
 check(l[t]['reading_status']=='read_complete',q['id'],'excluded thread quoted')
 check(len(q['context'].split())<=25,q['id'],'context word budget')
 check(q['source_class']=='forum_oblique' and q['evidence_kind']=='original_thread_post',q['id'],'classification')
 check(q['speaker'] in 'expecting_mother new_mother experienced_mother parent_unspecified partner relative_caregiver recovered_parent gave_up_parent advisor professional reviewer skeptic'.split(),q['id'],'speaker vocab')
 check(q['stage'] in 'pregnancy_early pregnancy_late newborn_0_6_weeks baby_6_16_weeks baby_4_6_months baby_6_12_months toddler return_to_work looking_back unknown'.split(),q['id'],'stage vocab')
 check(q['type'] in 'trigger_moment pain fear tried_failed desire belief question objection advice_given success_story failure_story regret others_said'.split(),q['id'],'type vocab')
check(len(ids)==len(set(ids)),'duplicate new ids')
all_ids=[]
for file in (R/'voice').glob('*.jsonl'):
 for line in file.read_text().splitlines():
  if not line.strip():continue
  q=json.loads(line);all_ids.append(q['id'])
  if 'archive.geoclicks.com/threads/' in q.get('url',''):
   budget[q['url']]+=len(re.sub(r'\s*\[(?:…|\.\.\.)\]\s*',' ',q['quote']).split())
check(len(all_ids)==len(set(all_ids)),'duplicate global ids')
for url,n in budget.items():check(n<=25,url,'aggregate post quotation budget',n)
notes=(R/'synthesis/reader-notes-geobaby-deep.md').read_text()
noteids=set(re.findall(r'odeep02-\d{4}',notes))
check(noteids<=set(ids),'reader note has unknown final record ID')
status=collections.Counter(x['reading_status'] for x in ledger)
excluded=[x for x in ledger if x['reading_status']!='read_complete']
result=dict(assigned_threads=len(m),read_captured_threads=len(ledger),read_captured_posts=sum(x['posts'] for x in ledger),read_captured_pages=sum(x['pages'] for x in ledger),chunks=len(chunks),eligible_threads=status['read_complete'],excluded_after_full_visible_read_threads=len(excluded),excluded_after_full_visible_read_posts=sum(x['posts'] for x in excluded),excluded_after_full_visible_read_pages=sum(x['pages'] for x in excluded),dispositions=dict(status),quotes=len(v),quoted_threads=len({q['thread_id'] for q in v}),unique_quoted_posts=len({q['url'] for q in v}),max_quoted_words_per_post=max(budget.values()),max_context_words=max(len(q['context'].split()) for q in v),uncertain_first_visible_threads=['166090','166302','166622'],uncertain_first_visible_thread_quotes=[q['id'] for q in v if q.get('source_role_uncertain')],unread_threads=[],partial_safety_inspections=[],failures=err,failed=len(err),voice_sha256=hashlib.sha256((R/'voice/oblique-deep-02.jsonl').read_bytes()).hexdigest(),ledger_sha256=hashlib.sha256((R/'sources/geobaby-deep-reading.jsonl').read_bytes()).hexdigest())
result['reader_note_final_ids_checked']=sorted(noteids)
result['reader_note_final_ids_checked_count']=len(noteids)
result['all_1422_full_quoted_bodies_matched_frozen_units_and_chunks']=not any('full quoted body missing' in str(e) for e in err)
(R/'sources/geobaby-deep-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));raise SystemExit(bool(err))
