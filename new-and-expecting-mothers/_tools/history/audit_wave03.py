#!/usr/bin/env python3
"""Recount, validate and freeze the third research wave's independent audit queues.

Run after all reader files are finalized. Does not rewrite voice/raw source files
or the first pass's frozen safety/spot-check samples. Queues still require human
context review; a zero structural count does not establish semantic accuracy.
"""
from pathlib import Path
import collections, datetime, hashlib, html, json, random, re, sys
from urllib.parse import urldefrag, urlsplit

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'_raw/audit/wave03-2026-10-24'
OUT.mkdir(parents=True,exist_ok=True)
INITIAL={Path(p).name for p in json.loads((OUT/'baseline-frozen-hashes.json').read_text()) if '/voice/' in p}
SPEAKERS=set('expecting_mother new_mother experienced_mother parent_unspecified partner relative_caregiver recovered_parent gave_up_parent advisor professional reviewer skeptic'.split())
STAGES=set('pregnancy_early pregnancy_late newborn_0_6_weeks baby_6_16_weeks baby_4_6_months baby_6_12_months toddler return_to_work looking_back unknown'.split())
TYPES=set('trigger_moment pain fear tried_failed desire belief question objection advice_given success_story failure_story regret others_said'.split())
REQUIRED='id source url date speaker stage type themes quote context raw_file source_class evidence_kind'.split()
rows=[];errors=[];file_hashes={}
for p in sorted((ROOT/'voice').glob('*.jsonl')):
    file_hashes[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    for number,line in enumerate(p.read_text().splitlines(),1):
        if not line.strip():continue
        try:q=json.loads(line)
        except Exception as e:errors.append(f'{p.name}:{number}: {e}');continue
        missing=set(REQUIRED)-q.keys()
        if missing:errors.append(f'{p.name}:{number}: missing {sorted(missing)}');continue
        q={**q,'_voice_file':p.name};rows.append(q)
        for key,allowed in [('speaker',SPEAKERS),('stage',STAGES),('type',TYPES)]:
            if q[key] not in allowed:errors.append(f"{q['id']}: invalid {key}={q[key]}")
        if not q['quote'].strip():errors.append(f"{q['id']}: empty quote")
        if len(q['context'].split())>25:errors.append(f"{q['id']}: long context")
        if not isinstance(q['themes'],list):errors.append(f"{q['id']}: themes not list")
        raw=(ROOT/q['raw_file']).resolve()
        if not raw.is_relative_to(ROOT.resolve()) or not raw.is_file():errors.append(f"{q['id']}: invalid raw path")
        if re.search(r'\bu/[A-Za-z0-9_-]{3,}',q['quote']+' '+q['context']):errors.append(f"{q['id']}: username in selected text")
ids=collections.Counter(q['id'] for q in rows)
errors += [f'duplicate quote id {key}' for key,n in ids.items() if n>1]

def work_key(q):
    host=urlsplit(q['url']).netloc.lower()
    if q.get('comment_id') is not None:return (host,'comment',str(q['comment_id']))
    if q.get('review_id') is not None:return (host,'review',str(q['review_id']))
    if q.get('review_local_key') is not None:return (urldefrag(q['url'])[0],'review_local',q['review_local_key'])
    if q.get('post_id') is not None:return (host,'post',str(q['post_id']))
    return (urldefrag(q['url'])[0],)

works=collections.defaultdict(list);duplicates=collections.defaultdict(list)
for q in rows:
    key=work_key(q)
    if q['source_class'] not in {'reddit_archive','community_index'}:works[key].append(q)
    norm=re.sub(r'\s+',' ',html.unescape(q['quote'])).strip()
    duplicates[(key,norm)].append(q['id'])
budgets=[]
for key,qs in works.items():
    words=sum(len(re.sub(r'\[(?:…|\.\.\.)\]',' ',q['quote']).split()) for q in qs)
    budgets.append({'work':key,'quoted_words':words,'ids':[q['id'] for q in qs]})
    if words>25:errors.append(f'non-Reddit work exceeds25words: {key}: {words}')
duplicate_excerpts=[{'work':key,'quote':quote,'ids':value} for (key,quote),value in duplicates.items() if len(value)>1]
new=[q for q in rows if q['_voice_file'] not in INITIAL]
pattern=re.compile(r'kill myself|suicid|self.harm|hurt (?:myself|my baby)|abuse|coerc|hit me|shak(?:e|ing) (?:the|my) baby|miscarriage|stillbirth|infant death|bedshar|co.sleep|chok|allerg|reflux|tongue.tie|delay|prematur|\bNICU\b|eczema|low supply|milk supply|pain|bleed|seizure|depress|anxi|vegan|vacci|medicat|dosage|diagnos|thrush|clinical|readiness|nutrition|airway|newborns are too young|\bGP\b|\b(?:1[0-7])\s*(?:f|m)\b',re.I)
hits=[q for q in new if pattern.search(q['quote']+' '+q['context'])]
(OUT/'final-safety-hits.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in hits))
(OUT/'non-reddit-work-budgets.json').write_text(json.dumps(budgets,ensure_ascii=False,indent=2))
(OUT/'duplicate-excerpts.json').write_text(json.dumps(duplicate_excerpts,ensure_ascii=False,indent=2))
# Reproducible continuation sample; committed baseline samples remain frozen.
later=new
rng=random.Random(2026102408);chosen=[]
for filename in sorted({q['_voice_file'] for q in later}):
    pool=[q for q in later if q['_voice_file']==filename]
    chosen+=rng.sample(pool,min(2,len(pool)))
remaining=[q for q in later if q['id'] not in {q['id'] for q in chosen}]
chosen+=rng.sample(remaining,min(max(0,20-len(chosen)),len(remaining)))
sample_path=OUT/'spot-check-wave03-originals.jsonl'
if not sample_path.exists():sample_path.write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in chosen))
# Preserve the initial random audit sample; later additions receive targeted checks.
chosen=[json.loads(s) for s in sample_path.read_text().splitlines() if s.strip()]
oversized=[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size} for p in (ROOT/'_raw').rglob('*') if p.is_file() and p.stat().st_size>=100_000_000]
if oversized:errors.append('raw files above100MB: '+str(oversized))
report={'date':'2026-10-25','total':len(rows),'initial':sum(q['_voice_file'] in INITIAL for q in rows),'new':len(new),'source_class':dict(collections.Counter(q['source_class'] for q in rows)),'voice_file_hashes':file_hashes,'non_reddit_works':len(works),'max_non_reddit_work_words':max((b['quoted_words'] for b in budgets),default=0),'duplicate_excerpt_groups':len(duplicate_excerpts),'new_safety_hits_requiring_human_review':len(hits),'later_spot_checks':len(chosen),'oversized_raw_files':oversized,'errors':errors,'failed':len(errors)}
(OUT/'final-structural-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(f"TOTAL {len(rows)} records; {len(new)} new; {len(errors)} structural/word-budget failures; {len(hits)} new safety hits need human review; {len(duplicate_excerpts)} duplicate-excerpt groups")
for e in errors:print(e)
sys.exit(bool(errors))
