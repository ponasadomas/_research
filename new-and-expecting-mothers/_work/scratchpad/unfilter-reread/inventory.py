from pathlib import Path
import csv, json, re, collections

R=Path(__file__).resolve().parents[2]
O=R/'scratchpad/unfilter-reread'
O.mkdir(parents=True,exist_ok=True)
def jl(p):
    return [json.loads(s) for s in p.read_text().splitlines() if s.strip()]
subject=re.compile(r'clinic|medic|safety|unsafe|crisi|self.?harm|suicid|abus|coerci|violen|loss|bereave|death|miscar|stillbirth|minor|underage|vulnerab|distress|diagnos|treatment|therap|reflux|allerg|intimate|reproductive|pregnancy.continu|trauma|NICU|prematur|mental.health|depress|anxi|safeguard|custody',re.I)
provenance=re.compile(r'promot|affiliate|solicit|authentic|seeded|allegation|testimonial|spam',re.I)
duplicate=re.compile(r'duplic|cross.?post|same (?:author|body|text)|already (?:read|covered|quoted)',re.I)
paths={}
for name in ['_raw/reddit-deep/corpus-A-v1/index.jsonl','_raw/reddit-deep/july-2025-wave-v1/primary-index.jsonl','_raw/reddit-deep/aug-dec-2025-wave-v1/primary-index.jsonl','_raw/report-purchase-archive-wave03/commercial-candidates.jsonl']:
    for q in jl(R/name): paths[str(q['post_id'])]=q['raw_file']
# Only filenames and ledger/index fields are inspected; no source-unit body is read.
allpaths=list((R/'_raw').rglob('*'))
bybase=collections.defaultdict(list)
for p in allpaths:
    if p.is_file():
        bybase[p.stem].append(str(p.relative_to(R)))
        bybase[p.stem.split('-')[-1]].append(str(p.relative_to(R)))
def resolve(q,p):
    for k in ['raw_file','raw_thread_json']:
        if q.get(k):return q[k]
    i=str(q.get('post_id',q.get('question_id',q.get('thread_id',q.get('discussion_id',q.get('id',q.get('unit','')))))))
    if i in paths:return paths[i]
    if 'communities' in str(p):return '_raw/communities/corpus-index/'+str(q['unit']).zfill(3)+'.txt'
    if 'qa-deep' in str(p):return '_raw/qa-deep/threads/'+i+'.txt'
    for stem in [i,'mse-'+i,'geo-'+i,i.removeprefix('jp-')]:
        a=bybase[stem]
        pref=[x for x in a if '/units/' in x and x.endswith('.txt')]
        if pref:return pref[0]
        pref=[x for x in a if '/threads/' in x and x.endswith(('.txt','.json'))]
        if pref:return pref[0]
    if 'july-B-solids.tsv' in str(p):return '_raw/reddit-deep/windows/2025-h2-v1/BabyLedWeaning_submissions.jsonl.gz'
    if 'agent-geo-triage' in str(p):return '_raw/oblique-deep/geo-scoped-cards.jsonl'
    if 'triage' in p.name and 'oblique-deep' in str(p):return '_raw/oblique-deep/mse-filtered.jsonl'
    return ''
decisions=[]
def add(q,p,stage,reason=None):
    reason=reason or q.get('exclusion_reason') or q.get('reason') or q.get('note') or q.get('reader_note') or ''
    if isinstance(reason,(dict,list)):reason=json.dumps(reason,ensure_ascii=False)
    i=str(q.get('post_id',q.get('question_id',q.get('thread_id',q.get('discussion_id',q.get('id',q.get('unit','')))))))
    cat='subject_or_mixed' if subject.search(reason) or 'safety_excluded' in str(q.get('status','')) else 'duplicate' if duplicate.search(reason) else 'provenance_review' if provenance.search(reason) else 'off_topic_or_repetition'
    raw=resolve(q,p)
    if 'mse' in raw:i='mse-'+i.removeprefix('mse-')
    elif 'geo-' in raw or 'geo-' in p.name:i='geo-'+i.removeprefix('geo-')
    elif 'qa-deep' in raw:i='qa-'+i.removeprefix('qa-')
    elif 'communities/' in raw:i='extract-'+i.removeprefix('extract-').zfill(3)
    decisions.append(dict(unit_id=i,raw_file=raw,stage=stage,category=cat,reason=reason,ledger=str(p.relative_to(R))))

tri=list((R/'_raw/reddit-deep/triage').glob('*.tsv'))+list((R/'_raw/report-purchase-archive-wave03/supplement-v1').glob('triage-*.tsv'))
tri+=list((R/'_raw/communities').glob('triage-*.tsv'))+list((R/'_raw/oblique-deep').glob('*triage*.tsv'))+[R/'_raw/qa-deep/human-triage.tsv',R/'scratchpad/report-purchase-archive-wave03/triage.tsv',R/'scratchpad/report-purchase-archive-wave03/supplement-v1/triage.tsv']
for p in tri:
    for q in csv.DictReader(p.open(),delimiter='\t'):
        label=q.get('label',q.get('decision',''))
        if label and ('drop' in label or 'exclude' in label):add(q,p,'triage')
for p in (R/'sources').glob('forums-deep-*-triage.jsonl'):
    for q in jl(p):
        if q.get('disposition')=='drop':add(q,p,'triage')

read=list((R/'sources').glob('*reading.jsonl'))+[R/'sources/reddit-july-focused-post-read-exclusions.jsonl',R/'sources/reddit-july-pregnancy-fullread-outcomes.jsonl',R/'_raw/qa-deep/read-ledger-qdeep01.jsonl',R/'_raw/qa-deep/reconciliation-qdeep01.tsv',R/'_raw/reddit-deep/information-payment-v1/reading-ledger.jsonl',R/'scratchpad/reddit-july-newparents/reading-ledger.tsv',R/'_raw/oblique-deep/post-triage-exclusions.tsv']
for p in read:
    if not p.exists():continue
    rows=jl(p) if p.suffix=='.jsonl' else list(csv.DictReader(p.open(),delimiter='\t'))
    for q in rows:
        status=str(q.get('status',q.get('reading_status',q.get('final_status',q.get('read_status',q.get('final_outcome',q.get('outcome','')))))))
        if q.get('disposition')=='drop_after_read':status='excluded_after_read'
        if p.name=='reconciliation-qdeep01.tsv':
            if q.get('triage')=='drop':continue
            status=q.get('final_outcome','')
        excluded=any(x in status for x in ['exclud','drop','research_only','offscope']) or bool(q.get('exclusion_reason')) or q.get('post_read_eligible') is False or q.get('post_read_eligible')==0
        if excluded:add(q,p,'reading_partial' if 'partial' in status or q.get('fully_read') is False else 'reading')

# Thread-level prose records omitted passages as well as whole-thread exclusions.
omit=re.compile(r'(?:clinical|medical|safety|unsafe|loss|death|abusive|minor|trauma|treatment|diet|coercive|distress).{0,150}(?:not (?:selected|extracted|quoted|carried)|exclud|omitt)|(?:exclud|omitt|not (?:selected|extracted|quoted|carried)).{0,150}(?:clinical|medical|safety|unsafe|loss|death|abusive|minor|trauma|treatment)',re.I)
for p in (R/'sources').glob('*.md'):
    for line in p.read_text().splitlines():
        if not line.startswith('|') or not omit.search(line):continue
        m=re.match(r'\|\s*(?:`)?((?:jp-)?\d{3,8})\b',line)
        if m:
            raw=re.search(r'`(_raw/[^`]+)`',line)
            tid=m[1]
            if p.name=='mse-completion-01.md':
                t=re.match(r'\|\s*\d+\s*\|\s*(\d+)',line)
                if t:tid=t[1]
            q={'thread_id':tid}
            if raw:q['raw_file']=raw[1]
            add(q,p,'quote_extraction',line.strip('| ').replace('|',';'))
for p in [R/'sources/geobaby-deep-reading.jsonl',R/'_raw/qa-deep/read-ledger-qdeep01.jsonl',*sorted((R/'sources').glob('forums-deep-*-final.jsonl'))]:
    for q in jl(p):
        reason=' '.join(str(q.get(k,'')) for k in ['reason','note','reader_note'])
        if omit.search(reason):add(q,p,'quote_extraction',reason)
for q in jl(R/'sources/oblique-deep-reading-ledger.jsonl'):
    for tid,reason in q.get('excluded_from_marketing',{}).items():
        add({'thread_id':tid},R/'sources/oblique-deep-reading-ledger.jsonl','reading_partial' if str(tid)=='6189328' else 'reading',reason)
for q in jl(R/'_raw/oblique-deep/final-safety-unread-tails.jsonl'):
    add(q,R/'_raw/oblique-deep/final-safety-unread-tails.jsonl','reading_partial',q.get('reason') or 'Historical partial_safety_excluded: remaining replies deliberately unread.')

# Explicit passage omissions are also recorded in retained quote context.
voice=[q for p in (R/'voice').glob('*.jsonl') for q in jl(p)]
for q in voice:
    c=q.get('context','')
    if omit.search(c) and 'as clinical guidance' not in c:add(q,R/'voice'/next(p.name for p in (R/'voice').glob('*.jsonl') if q['id'] in p.read_text()),'quote_extraction',c)

unique={tuple(x.values()):x for x in decisions}
decisions=sorted(unique.values(),key=lambda x:(x['stage'],x['ledger'],x['unit_id']))
with (O/'decisions.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['unit_id','raw_file','stage','category','reason','ledger'],delimiter='\t');w.writeheader();w.writerows(decisions)
queue={}
for x in decisions:
    if x['category'] not in ['subject_or_mixed','provenance_review']:continue
    if not x['raw_file']:continue
    key=x['unit_id']
    row=queue.setdefault(key,dict(unit_id=x['unit_id'],raw_file=x['raw_file'],stage=set(),reason=[]))
    row['stage'].add(x['stage']);row['reason'].append(x['ledger']+': '+x['reason'])
with (O/'queue.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['unit_id','raw_file','stage','reason'],delimiter='\t');w.writeheader()
    for x in sorted(queue.values(),key=lambda x:(x['unit_id'],x['raw_file'])):
        w.writerow(dict(x,stage=';'.join(sorted(x['stage'])),reason=' | '.join(dict.fromkeys(x['reason']))))
stats=collections.defaultdict(collections.Counter)
for x in decisions:stats[(x['stage'],x['ledger'])][x['category']]+=1
missing=[x for x in decisions if x['category'] in ['subject_or_mixed','provenance_review'] and (not x['raw_file'] or not (R/x['raw_file']).is_file())]
(O/'unresolved-paths.json').write_text(json.dumps(missing,indent=2,ensure_ascii=False)+'\n')
summary={'decision_rows':len(decisions),'categories':dict(collections.Counter(x['category'] for x in decisions)),'queue_units':len(queue),'queue_stages':dict(collections.Counter(';'.join(sorted(x['stage'])) for x in queue.values())),'missing_paths':len(missing)}
(O/'inventory.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Global unfilter report — 2026-11-16 ruling; executed 2026-11-17','',
'Initial inventory written before changing instructions, tools, indices or findings. Scope: `global/` and `../main/`; no network, git, raw writes or source-unit re-reading. Historical source ledgers and reader notes are preserved. Counts describe selected quote records and logged decisions, never people or prevalence.','',
'## Verified baseline and where the filter acted','',
'- **Intake:** `_tools/reddit_deep_filter.py` assigns A/B/C by artifact/tool/friction regex and unavailable-body status; its safety regex only adds `safety_flag`. It emitted all 8,284 A cards, not a separate safety tier. Frozen B/C bodies remain a topic-selection backlog, not proven subject exclusions.','- **Triage:** `_tools/brief-reddit-deep-triage.md` says “Drop accounts centered on self-harm, violence/coercive control, infant death, pregnancy loss, minors or clinical crisis.” JustParents scripts additionally exclude clinical feeding, symptoms, injury, medication, atypical development, distress, and personal reproductive subjects as outside a practical report. The per-ledger table and exact decision reasons below distinguish subject/mixed reasons from ordinary scope/duplicate decisions.','- **Reading:** augmented reader briefs say “A crisis boundary may require stopping” and require `partial_safety`/`excluded_after_read` statuses. Fifteen MSE discussions have explicit partial boundaries and 231 unread tail posts; these were withheld, not full-read. Complete but excluded originals and incidentally omitted passages also remain outside the voice database.','- **Extraction:** clinical, safety, loss, coercion and other passages were withheld even inside otherwise quoted threads. The inventory records named omissions; general statements without unit ids cannot establish how many passages were lost. Raw re-reading is needed to recover their words.','- **Marking:** exactly **141** of **2,162** immutable voice records have `marketing_eligible=false`. Reasons mix subject restrictions with provenance/payment caution and ordinary adjacent topics. `evidence_use` is not a uniform category; every original reason is retained in the restoration manifest.','- **Language bank:** `_tools/build_index.py` explicitly skips `marketing_eligible=false`; `_tools/query.py --exclude-restricted` removes them and labels other query output “RESEARCH BOUNDARY ONLY”. The baseline bank contains **1,144** distinct ids, **zero** of the 141. The 80/section, 520-character, one/URL and source-balancing limits also omit ordinary records; removal of the subject filter alone would not ensure all 141 appear.','- **Findings:** `synthesis/findings.md` §13 says “No crisis, abuse, loss, infant death or minor-centered marketing” and repeats bank exclusion. Many marked ids were already cited, with summaries of their commercial relevance, but their words were largely withheld. `../main/synthesis/sub-niche-map.md` ranks clinical-adjacent jobs by compliance risk and calls some “not products”; that is an owner copy/product decision, not grounds to exclude research.','- **Tooling:** briefs repeat subject exclusions and marking rules; two native verifiers require a false eligibility flag to quote an excluded source. Renderers regenerate the bank-exclusion prose. Audit scripts count flags and search for sensitive terms; keyword hits alone are not errors. Structural/provenance checks must remain.','',
'## Decision inventory and recovery queue','',
'[Every logged drop/omission and the agent’s exact reason](../scratchpad/unfilter-reread/decisions.tsv) is grouped below. `subject_or_mixed` means the recorded reason names a sensitive/clinical subject, including mixed off-topic/duplicate reasons; it is a review set, not a claim that every such unit is on-topic. `off_topic_or_repetition` and `duplicate` are allowed decisions as recorded; no source bodies were rejudged. `provenance_review` records promotional/authenticity exclusions: provenance must be labelled, and relevant words retained. Broad mixed boilerplate prevents an honest exact count of censorship alone.','',
'**“Off-topic” did hide subjects:** forum defaults explicitly put “Clinical symptom/care, miscarriage/loss, surrogacy/adoption” outside household-report needs, and feeding defaults reject clinical topics as “unsuitable for report targeting/medical instructions”. These decisions cannot be accepted as ordinary irrelevant-topic drops without re-reading.','',
'The [queue](../scratchpad/unfilter-reread/queue.tsv) names units and raw paths for subject/mixed and provenance reassessment, including omitted passages in quoted units. Ordinary off-topic/duplicate decisions stay in the inventory. A queue row may have multiple historical stages/reasons; overlapping ledger entries are not independent units. No queued unit has been re-read in this pass. Missing words never reached `voice/*.jsonl`; restoring 141 stored records cannot recover them.','',
'| Stage | Ledger | Subject or mixed | Provenance review | Duplicate | Off-topic or repetition |','|---|---|---:|---:|---:|---:|']
for (stage,p),c in sorted(stats.items()):lines.append(f"| {stage} | `{p}` | {c['subject_or_mixed']} | {c['provenance_review']} | {c['duplicate']} | {c['off_topic_or_repetition']} |")
lines+=['', 'Inventory summary: `'+json.dumps(summary,sort_keys=True)+'`.','', '## Restoration, verification and changed files','', 'Pending. This initial report precedes restoration; the closing record will give final counts, conclusions, exact commands/output, limitations and all changed files.','']
# The initial report is historical; inventory rebuilds never overwrite it.
if not (R/'synthesis/unfilter-report.md').exists():
    (R/'synthesis/unfilter-report.md').write_text('\n'.join(lines))
print(json.dumps(summary,indent=2))
