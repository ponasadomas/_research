#!/usr/bin/env python3
"""Validate the final integrated continuation without modifying source evidence."""
from pathlib import Path
import json,re,hashlib,collections,subprocess,sys
R=Path(__file__).resolve().parents[1];repo=R.parents[2];D=R/'_raw/audit/continuation-2026-10-24';errors=[]
jl=lambda p:[json.loads(x) for x in p.read_text().splitlines() if x.strip()]
check=lambda value,msg:None if value else errors.append(msg)
qs=[q for p in (R/'voice').glob('*.jsonl') for q in jl(p)];byid={q['id']:q for q in qs};C=json.loads((R/'synthesis/counts.json').read_text());V=json.loads((R/'synthesis/coverage.json').read_text());r=V['reddit'];native=json.loads((D/'final-native-audit.json').read_text());structure=json.loads((D/'final-structural-audit.json').read_text())
check(len(qs)==len(byid)==C['total']==1944,'Whole quote count/unique ID mismatch')
check(C['source_class']==dict(collections.Counter(q['source_class'] for q in qs)),'Source class recount mismatch')
restricted={q['id'] for q in qs if q.get('marketing_eligible') is False}
check(len(restricted)==C['historically_marked_records'],'Historical label recount mismatch')
lines=(R/'synthesis/quote-index.md').read_text().splitlines();bank=[]
for n,line in enumerate(lines):
 match=re.fullmatch(r'\[([a-z0-9]+-\d+)\]',line)
 if not match:continue
 rid=match.group(1);bank.append(rid);q=byid.get(rid);check(q is not None,'Unknown bank ID '+rid)
 if not q:continue
 quote_lines=q['quote'].split('\n')
 check(lines[n+1:n+1+len(quote_lines)]==['> '+part for part in quote_lines],'Bank quote mismatch '+rid)
 expected=f"Context: {q['context']} [Original source]({q['url']}) · [Frozen source](../{q['raw_file']})"
 check(lines[n+len(quote_lines)+3]==expected,'Bank context/source links mismatch '+rid)
 role=lines[n+len(quote_lines)+2]
 check(q['speaker'].replace('_',' ') in role and q['stage'].replace('_',' ') in role,'Bank role/stage mismatch '+rid)
check(len(bank)==len(set(bank))==C['language_bank_entries']==len(qs),'Bank duplicate/recount mismatch')
for file,want in structure['voice_file_hashes'].items():check(hashlib.sha256((R/'voice'/file).read_bytes()).hexdigest()==want,'Stale global structure hash '+file)
for file,want in native['voice_sha256'].items():check(hashlib.sha256((R/f'voice/{file}.jsonl').read_bytes()).hexdigest()==want,'Stale native hash '+file)
check(native['failed']==structure['failed']==0,'Global audit has failures')
check(native['full_original_posts']==4816 and native['identifiable_OP_replies']==1700 and native['selected_quotes']==648,'Continuation native denominator mismatch')
base=json.loads((D/'baseline-voice-manifest.json').read_text())
for b in base:check(hashlib.sha256((R/b['path']).read_bytes()).hexdigest()==b['sha256'],'Baseline voice mutated '+b['path'])
for name in ['_raw/reddit-deep/final-A-reading-inventory.jsonl','_raw/reddit-deep/final-unhandled-A.jsonl','_raw/reddit-deep/final-read-post-ids.json','_raw/oblique-deep/final-mse-reading-inventory.jsonl','_raw/oblique-deep/final-safety-unread-tails.jsonl']:
 relative=str((R/name).relative_to(repo));old=subprocess.check_output(['git','show','2613feb3:'+relative],cwd=repo);check((R/name).read_bytes()==old,'Baseline inventory mutated '+name)
inv=R/'_raw/reddit-deep/continuation-v1';read=json.loads((inv/'final-read-post-ids.json').read_text());a=json.loads((inv/'unread-A-post-ids.json').read_text());b=json.loads((inv/'unread-B-post-ids.json').read_text());c=json.loads((inv/'unread-C-post-ids.json').read_text());comments=json.loads((inv/'unread-available-comment-ids.json').read_text())
check(len(set(read['full_original_post_ids']))==r['full_original_posts_distinct_ids']==5879,'Cumulative post-ID count')
check(len(a)==r['A_original_bodies_unread']==2532 and len(b)==r['B_bodies_unread']==51126 and len(c)==r['C_bodies_unread']==38463,'Unread body inventories')
check(r['continuation_card_drop_bodies_unread_after_audit']==1907 and r['continuation_audit_extra_full_posts']==1,'Audit inspection accounting')
check(len(read['available_OP_comment_ids_read'])==r['identifiable_OP_reply_records_read_distinct_ids']==2149,'Cumulative OP IDs')
check(len(read['non_OP_auxiliary_comment_ids_read'])==r['non_OP_comment_records_read']==43,'Cumulative auxiliary IDs')
check(len(set(comments))==len(comments)==r['available_comment_records_unread']==145387,'Unread available comment inventory')
check(set(comments).isdisjoint(read['available_OP_comment_ids_read']) and set(comments).isdisjoint(read['non_OP_auxiliary_comment_ids_read']),'Read comments marked unread')
check(145387+2149+43==147579,'Available comment denominator')
check(r['all_A_candidates_human_handled']==8284 and r['A_cards_human_triaged']==8258 and r['continuation_full_posts']==4689 and r['outside_July_A_unhandled']==0 and r['continuation_kept_unread']==0,'A completion scope')
hits={q['id'] for q in jl(D/'final-safety-hits.jsonl')};reviews=jl(D/'final-safety-review.jsonl');check(hits=={x['quote_id'] for x in reviews} and len(hits)==len(reviews)==68,'Safety hit/review exact ID set')
random1=jl(D/'independent-semantic20/results.jsonl');random2=jl(D/'parent-random20-results.jsonl');check(len(random1)==len(random2)==20,'Manual random samples incomplete')
check({x['quote_id'] for x in random2}=={q['id'] for q in jl(D/'spot-check-continuation-originals.jsonl')},'Root random-sample ID set')
check(len(jl(D/'parent-targeted-semantic-results.jsonl'))==23,'Targeted manual audit incomplete')
qposts=collections.defaultdict(list)
for q in qs:
 if q.get('source_class')=='reddit_archive' and q.get('post_id'):qposts[q['post_id']].append(q['id'])
bodygroups=[]
for n,g in enumerate(jl(R/'_raw/reddit-deep/aug-dec-2025-wave-v1/exact-body-duplicate-flags.jsonl'),1):
 selected=[m['post_id'] for m in g['records'] if qposts[m['post_id']]]
 check(len(selected)<=1,'Multiple quoted exact-body copies group'+str(n))
 if selected:bodygroups.append({'group':n,'quoted_representative_post_id':selected[0],'quote_ids':qposts[selected[0]],'all_flagged_post_ids':[m['post_id'] for m in g['records']]})
(D/'final-selected-body-duplicate-groups.json').write_text(json.dumps(bodygroups,indent=2)+'\n')
for n in range(1,9):
 report=json.loads((R/f'sources/reddit-augdec-{n:02}-verification.json').read_text());check(not report.get('failed',0) and not report.get('errors',[]),'Reader audit incomplete '+str(n))
 check((R/f'synthesis/reader-notes-reddit-augdec-{n:02}.md').is_file(),'Reader notes missing '+str(n))
rawfiles=[p for p in (R/'_raw').rglob('*') if p.is_file()];large=[str(p.relative_to(R)) for p in rawfiles if p.stat().st_size>=100000000];check(not large,'Oversized raw files '+str(large[:4]))
inputpaths=''.join(str(p.relative_to(repo))+'\n' for p in rawfiles);ignore=subprocess.run(['git','check-ignore','--no-index','--stdin'],cwd=repo,input=inputpaths,text=True,capture_output=True);check(ignore.returncode in [0,1] and not ignore.stdout,'Raw files ignored: '+ignore.stdout[:1000])
changed=subprocess.check_output(['git','diff','--name-only','--',str(R/'_raw')],cwd=repo,text=True).splitlines();check(not changed,'Committed raw files changed '+str(changed[:4]))
result=dict(date='2026-10-24',total_quotes=len(qs),new_quotes=648,bank_ids=len(bank),research_only=len(restricted),full_Reddit_posts=5879,OP_replies=2149,auxiliary_comments=43,body_unread=dict(A=2532,B=51126,C=38463),available_comments_unread=len(comments),manual_safety_reviewed=len(reviews),manual_random_samples=[20,20],distinct_random_IDs=len({x['id'] for x in random1}|{x['quote_id'] for x in random2}),targeted_record_checks=23,selected_exactbody_groups=len(bodygroups),baseline_voice_files_unchanged=len(base),baseline_raw_inventories_unchanged=5,raw_files=len(rawfiles),oversized_raw=large,ignored_raw=ignore.stdout.splitlines(),errors=errors,failed=len(errors))
(D/'final-state-consistency.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));sys.exit(bool(errors))
