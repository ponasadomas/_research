import collections, hashlib, json, random, re, subprocess, sys
from pathlib import Path
from reader import ROOT, WORK

def rows(path):return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+',' ',s).strip()
def contains(quote,body):
 pos=0
 for piece in re.split(r'\s*\[(?:…|\.\.\.)\]\s*',quote):
  piece=norm(piece)
  at=norm(body).find(piece,pos)
  if at<0:return False
  pos=at+len(piece)
 return True

voice=ROOT/'voice/oblique-deep-04.jsonl'
ledger_path=ROOT/'sources/mse-completion-02-reading.jsonl'
base=ROOT/'_raw/oblique-deep/mse-completion-v2/batch-02'
manifest=rows(base/'manifest.jsonl');chunks=rows(base/'chunks.jsonl')
quotes=rows(voice);ledger=rows(ledger_path)
failures=[]
def ck(condition,label,extra=None):
 if not condition:failures.append({'check':label,'detail':extra})

mc=collections.Counter(m['thread_id'] for m in manifest)
lc=collections.Counter(l['thread_id'] for l in ledger)
ck(mc==lc,'exact_manifest_ledger_id_multiset')
ck(all(n==1 for n in lc.values()),'no_duplicate_ledger_ids')
ck(len(quotes)==len(set(q['id'] for q in quotes)),'no_duplicate_quote_ids')
md={m['thread_id']:m for m in manifest};ld={l['thread_id']:l for l in ledger}
native={i:json.loads((ROOT/m['thread_json']).read_text()) for i,m in md.items()}
for m in manifest:
 p=ROOT/m['raw_file']
 ck(sha(p)==m['sha256'],'frozen_individual_unit_hash',m['thread_id'])
 ck(len(p.read_bytes())==m['utf8_bytes'],'frozen_unit_bytes',m['thread_id'])
 t=native[m['thread_id']]
 ck(len(t['posts'])==m['posts'],'native_post_count',m['thread_id'])
 ck(t['complete_visible_pagination'] and len(t['pages'])==m['pages'],'native_full_pagination',m['thread_id'])
 l=ld[m['thread_id']]
 ck(l['posts_total']==m['posts'],'ledger_denominator',m['thread_id'])
 ck(l['raw_file']==m['raw_file'],'ledger_individual_unit',m['thread_id'])
 ck(l['fully_read']==(l['status']=='full'),'ledger_status_boolean',m['thread_id'])
 ck(0<=l['post_read_eligible']<=l['posts_read']<=l['posts_total'],'ledger_read_bounds',m['thread_id'])
 if l['fully_read']:ck(l['posts_read']==l['posts_total'],'full_is_all_posts',m['thread_id'])
 else:ck(not l['quote_ids'] and l['posts_read']<l['posts_total'],'partial_exclusion_no_quotes',m['thread_id'])
 ck(l['quote_ids']==[q['id'] for q in quotes if q['thread_id']==m['thread_id']],'ledger_quote_link',m['thread_id'])

chunk_ids=[]
for c in chunks:
 p=ROOT/c['file'];ct=p.read_text();ids=re.findall(r'^THREAD MSE-(\d+):',ct,re.M)
 ck(ids==c['thread_ids'],'chunk_thread_order',c['file'])
 ck(len(p.read_bytes())==c['utf8_bytes'],'chunk_bytes',c['file'])
 chunk_ids.extend(c['thread_ids'])
ck(collections.Counter(chunk_ids)==mc,'exact_chunks_manifest_id_multiset')

readme=(ROOT/'README.md').read_text()
vocab={}
for key,label in [('speaker','Speakers'),('stage','Stages'),('type','Types')]:
 line=next(x for x in readme.splitlines() if x.startswith(label+':'))
 vocab[key]=set(re.findall(r'`([^`]+)`',line))

selected_keys=set();word_totals=collections.Counter()
for q in quotes:
 i=q['thread_id'];p=next(p for p in native[i]['posts'] if p['post_id']==q['post_id'])
 key=(i,q['post_id']);selected_keys.add(key)
 ck(contains(q['quote'],p['body']),'strict_actual_author_body',q['id'])
 ck(contains(q['quote'],p['body_with_quotes']),'strict_full_context_body',q['id'])
 ck(contains(q['quote'],(ROOT/q['raw_file']).read_text()),'strict_frozen_unit_containment',q['id'])
 ck(q['raw_file']==md[i]['raw_file'],'quote_individual_raw',q['id'])
 ck(q['url']==p['url'],'exact_post_url',q['id'])
 ck(q['date']==p['date'][:10],'exact_original_date',q['id'])
 ck(q['is_op']==p['is_op'],'exact_is_op',q['id'])
 ck(q['author_id']==(p.get('author_id') or 'unknown'),'actual_source_author_id',q['id'])
 ck(q['source_class']=='forum_oblique' and q['evidence_kind']=='original_thread_post','source_class_kind',q['id'])
 ck(ld[i]['fully_read'],'quoted_thread_full_and_eligible',q['id'])
 ck(len(q['context'].split())<=25,'context_25_words',q['id'])
 for field in vocab:ck(q[field] in vocab[field],'readme_'+field,q['id'])
 word_totals[key]+=len(re.sub(r'\[(?:…|\.\.\.)\]','',q['quote']).split())

# The copyright ceiling applies across every retained excerpt from each original
# post, including any other reader file, not just this new voice file.
global_words=collections.Counter();global_ids=[]
for p in sorted((ROOT/'voice').glob('*.jsonl')):
 for q in rows(p):
  global_ids.append(q['id'])
  key=(str(q.get('thread_id','')),str(q.get('post_id','')))
  if key in selected_keys:
   global_words[key]+=len(re.sub(r'\[(?:…|\.\.\.)\]','',q['quote']).split())
for key,n in global_words.items():ck(n<=25,'aggregate_post_25_words',{'post':key,'words':n})
for q in quotes:ck(global_ids.count(q['id'])==1,'globally_unique_new_quote_id',q['id'])

notes=ROOT/'synthesis/reader-notes-mse-completion-02.md'
cited=sorted(set(re.findall(r'\[(odeep04-\d{4})\]',notes.read_text())))
byid={q['id']:q for q in quotes}
for i in cited:ck(i in byid,'notes_id_exists',i)
lookup=[{k:byid[i][k] for k in ['id','thread_id','post_id','speaker','stage','type','quote','context']} for i in cited if i in byid]
(WORK/'notes-id-lookups.json').write_text(json.dumps(lookup,ensure_ascii=False,indent=2)+'\n')

# Direct source-author linkage, rather than a remembered display name.
p1=native['4936780']['posts'][0];p2=native['5015478']['posts'][0]
ck(p1['author_id']==p2['author_id']=='276311','cross_thread_author_identity')
ck(native['5782171']['posts'][33]['post_id']=='Comment_73774772','partial_5782171_final_post')

r=subprocess.run([sys.executable,str(ROOT/'_tools/verify_quotes.py'),str(voice)],capture_output=True,text=True)
ck(r.returncode==0,'copied_verifier',r.stdout+r.stderr)
(WORK/'verify-quotes.txt').write_text(r.stdout+r.stderr)

sample=random.Random(20261024).sample(quotes,20)
(WORK/'spot-check-20.json').write_text(json.dumps([{**q,'native_body':next(p['body'] for p in native[q['thread_id']]['posts'] if p['post_id']==q['post_id'])} for q in sample],ensure_ascii=False,indent=2)+'\n')
counts=json.loads((WORK/'counts.json').read_text())
result={
 'completed_on':'2026-10-24','assignment':'mse-completion-v2/batch-02',
 'counts':counts,'strict_failures':len(failures),'failures':failures,
 'copied_verifier':r.stdout.strip(),
 'ledger_id_duplicates':sum(v-1 for v in lc.values() if v>1),
 'assigned_missing_from_ledger':sorted(set(mc)-set(lc)),
 'unassigned_in_ledger':sorted(set(lc)-set(mc)),
 'quoted_posts_over_25_words':sum(v>25 for v in global_words.values()),
 'max_aggregate_words_per_selected_original_post':max(global_words.values()),
 'max_context_words':max(len(q['context'].split()) for q in quotes),
 'notes_cited_unique_ids':len(cited),'notes_id_lookup_file':'scratchpad/mse-completion-02/notes-id-lookups.json',
 'source_author_containment':'All excerpts match native body without blockquotes, as well as full body_with_quotes and frozen individual unit.',
 'manual_review':'Reader reviewed all selected excerpts and read complete assigned eligible threads; twenty deterministic source/body/metadata spot checks recorded separately. No names/usernames retained in excerpts or contexts. No selected passage supplies medical, safety or benefits advice.',
 'speakers':dict(collections.Counter(q['speaker'] for q in quotes)),
 'stages':dict(collections.Counter(q['stage'] for q in quotes)),
 'types':dict(collections.Counter(q['type'] for q in quotes)),
 'sha256':{str(p.relative_to(ROOT)):sha(p) for p in [voice,ledger_path,ROOT/'sources/mse-completion-02.md',notes,base/'manifest.jsonl',base/'chunks.jsonl',WORK/'notes-id-lookups.json',WORK/'spot-check-20.json',WORK/'verify-quotes.txt']},
 'individual_units_sha256':{m['raw_file']:sha(ROOT/m['raw_file']) for m in manifest},
 'chunks_sha256':{c['file']:sha(ROOT/c['file']) for c in chunks},
}
(ROOT/'sources/mse-completion-02-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'counts':counts,'strict_failures':len(failures),'failures':failures,'notes_ids':len(cited),'copied_verifier':r.stdout.strip()},ensure_ascii=False,indent=2))
sys.exit(bool(failures))
