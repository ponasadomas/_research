#!/usr/bin/env python3
"""Join completed source ledgers by original ids; never infer reads from downloads."""
from pathlib import Path
import collections, csv, hashlib, json

R=Path(__file__).resolve().parents[1]
OUT=R/'synthesis'
def jl(name):return [json.loads(l) for l in (R/name).read_text().splitlines() if l.strip()]
def tsv(name):return list(csv.DictReader((R/name).open(),delimiter='\t'))
def dump(name,obj):(R/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

july=jl('_raw/reddit-deep/july-2025-wave-v1/candidates.jsonl')
np=tsv('scratchpad/reddit-july-newparents/reading-ledger.tsv')
pg=tsv('sources/reddit-july-pregnancy-per-id.tsv')
fc=jl('sources/reddit-july-focused-final-status.jsonl')
pay=jl('_raw/reddit-deep/information-payment-v1/reading-ledger.jsonl')
np_read={x['post_id'] for x in np if x['fully_read']=='1'}
pg_read={x['post_id'] for x in pg if x['full_original_read'].lower()=='true'}
fc_read={x['post_id'] for x in fc if x['post_body_read_complete']}
pay_read={x['id'] for x in pay if x['status']=='fully_read'}
assert (len(np),len(pg),len(fc),len(np_read),len(pg_read),len(fc_read))==(469,495,406,352,273,406)
# Focused final-status is intentionally the human-kept primary queue, not all697 cards.
fc_triage=tsv('_raw/reddit-deep/triage/july-focused.tsv')
all_card_ids={x['post_id'] for x in np}|{x['post_id'] for x in pg}|{x['post_id'] for x in fc_triage}
july_ids={x['id'] for x in july}
assert len(all_card_ids)==1661 and all_card_ids==july_ids
july_read=np_read|pg_read|fc_read
all_read=july_read|pay_read
metadata={x['id']:x for x in july}
metadata.update({x['id']:x for x in pay})
op_ids=set()
for row in fc:
    text=(R/row['raw_file']).read_text();meta,_=json.JSONDecoder().raw_decode(text[text.index('{'):])
    assert len(meta['OP_comment_ids'])==row['available_identifiable_OP_replies_read']
    op_ids.update(meta['OP_comment_ids'])
for row in pay:
    native=json.loads((R/f"_raw/reddit-deep/information-payment-v1/units/{row['id']}.json").read_text())
    op_ids.update(x['id'] for x in native['available_identifiable_OP_replies'])
aux=jl('sources/reddit-july-focused-auxiliary-read.jsonl')
aux_ids={str(x.get('comment_id',x.get('id'))) for x in aux}
assert len(aux_ids)==7
tiers={tier:{x['id']:x for x in jl(f'_raw/reddit-deep/filter-v1/{tier}-candidates.jsonl')} for tier in ['A','B','C','unavailable']}
A=set(tiers['A'])
handled=july_ids|pay_read
unhandled=A-handled
assert len(unhandled)==6597
rows=[]
for pid,item in tiers['A'].items():
    rows.append({'post_id':pid,'subreddit':item['subreddit'],'july_card_triaged':pid in july_ids,'full_original_primary_read':pid in all_read,'handled_in_payment_cohort':pid in pay_read,'status':'full_primary_read' if pid in all_read else ('card_excluded_original_unread' if pid in july_ids else 'unhandled_machine_candidate'),'raw_file':f"_raw/reddit-deep/corpus-A-v1/units/{item['subreddit']}-{pid}.txt"})
(R/'_raw/reddit-deep/final-A-reading-inventory.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in rows))
(R/'_raw/reddit-deep/final-unhandled-A.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in rows if x['post_id'] in unhandled))
dump('_raw/reddit-deep/final-read-post-ids.json',{'full_original_post_ids':sorted(all_read),'available_OP_comment_ids_read':sorted(op_ids),'non_OP_auxiliary_comment_ids_read':sorted(aux_ids),'payment_overlap_with_July_primary_reads':sorted(pay_read&july_read)})
reddit={'window_post_records':112665,'available_text_bodies':98000,'window_comment_records':147579,'communities':9,'A_candidates':8284,'B_candidates':51253,'C_candidates':38463,'unavailable_bodies':14665,'July_cards_triaged':1661,'July_initial_kept_primary_units_fully_read':len(july_read),'July_final_eligible_contexts':322+241+370,'July_post_read_exclusions':30+32+36,'July_initial_card_drops':1661-len(july_read),'payment_cohort_full_posts':39,'payment_overlap_with_July_full_reads':len(pay_read&july_read),'full_original_posts_distinct_ids':len(all_read),'full_posts_by_subreddit':dict(collections.Counter(metadata[pid]['subreddit'] for pid in all_read)),'identifiable_OP_reply_records_read_distinct_ids':len(op_ids),'non_OP_comment_records_read':len(aux_ids),'outside_July_A_unhandled':len(unhandled),'A_original_bodies_unread':len(A-all_read),'July_card_dropped_bodies_unread_after_payment_overlap':len(july_ids-all_read),'B_bodies_unread':len(set(tiers['B'])-all_read),'C_bodies_unread':len(set(tiers['C'])-all_read),'B_read_ids':sorted(set(tiers['B'])&all_read),'C_read_ids':sorted(set(tiers['C'])&all_read),'six_month_card_chunks_with_unhandled_ids':110}

# MSE: first reader, one eligibility exclusion, then all313 disjoint completion rows.
captured={}
for p in (R/'_raw/oblique-deep/threads').glob('mse-*.json'):
    if p.name.endswith('.http.json'):continue
    x=json.loads(p.read_text());captured[x['discussion_id']]=x
first={x.removeprefix('mse-') for x in (R/'_raw/oblique-deep/read-thread-ids.txt').read_text().split()}
mse=[]
for tid in first:
    x=captured[tid];mse.append({'thread_id':tid,'fully_read':True,'posts_read':len(x['posts']),'posts_total':len(x['posts']),'status':'full_with_quoted_context_supplement','raw_file':f'_raw/oblique-deep/threads/mse-{tid}.json'})
mse.append({'thread_id':'6189328','fully_read':False,'posts_read':1,'posts_total':27,'status':'partial_safety_excluded','raw_file':'_raw/oblique-deep/threads/mse-6189328.json'})
for n in range(1,4):mse+=jl(f'sources/mse-completion-{n:02}-reading.jsonl')
assert len(mse)==len({x['thread_id'] for x in mse})==343 and {x['thread_id'] for x in mse}==set(captured)
for x in mse:assert x['posts_total']==len(captured[x['thread_id']]['posts'])
full=[x for x in mse if x['fully_read']];partial=[x for x in mse if not x['fully_read']]
mse_stats={'captured_threads':343,'captured_pages':sum(len(x['pages']) for x in captured.values()),'captured_posts':sum(len(x['posts']) for x in captured.values()),'full_visible_threads_read':len(full),'posts_in_full_threads_read':sum(x['posts_total'] for x in full),'partial_safety_excluded_threads':len(partial),'posts_inspected_or_read_in_partials':sum(x['posts_read'] for x in partial),'later_posts_deliberately_unread':sum(x['posts_total']-x['posts_read'] for x in partial),'eligible_kept_unread':0}
(R/'_raw/oblique-deep/final-mse-reading-inventory.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in sorted(mse,key=lambda x:x['thread_id'])))
(R/'_raw/oblique-deep/final-safety-unread-tails.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in partial))
jp=json.loads((R/'sources/forums-deep-effective-kept-manifest.json').read_text())['stats']
geo=jl('sources/geobaby-deep-reading.jsonl')
assert len(geo)==183 and all(x['all_posts_and_op_followups_read'] and x['quoted_context_read'] for x in geo)
geo_stats={'captured_threads':183,'captured_pages':sum(x['pages'] for x in geo),'captured_posts':sum(x['posts'] for x in geo),'full_visible_threads_read':len(geo),'posts_in_full_threads_read':sum(x['posts'] for x in geo),'post_read_excluded_threads':sum('excluded' in x['reading_status'] for x in geo),'eligible_kept_unread':0}
forums={'captured_threads':jp['unique_captured_threads']+343+183,'captured_posts':jp['captured_original_posts_and_responses']+mse_stats['captured_posts']+geo_stats['captured_posts'],'initial_kept_for_reading':jp['initially_retained_threads']+343+183,'full_visible_threads_read':jp['provisional_threads_fully_read']+len(full)+183,'posts_in_fully_read_threads':jp['initially_retained_posts']+mse_stats['posts_in_full_threads_read']+geo_stats['captured_posts'],'partial_safety_inspections':len(partial),'posts_inspected_or_read_in_partials':mse_stats['posts_inspected_or_read_in_partials'],'unread_posts_in_card_dropped_JP_threads':jp['captured_original_posts_and_responses']-jp['initially_retained_posts'],'deliberately_unread_MSE_safety_tail_posts':mse_stats['later_posts_deliberately_unread'],'eligible_kept_unread':0}
qa=json.loads((R/'synthesis/qa-deep-verification.json').read_text())
report={'date':'2026-10-24','reddit':reddit,'JustParents':jp,'MSE':mse_stats,'GeoBaby':geo_stats,'forums_combined':forums,'Parenting_API':qa,'review_units_fully_read':219,'app_review_units_fully_read':204,'book_review_units_fully_read':15,'competitor_notes':41,'new_offer_pages_fully_read':7,'initial_offer_pages_fully_read':41,'offer_pages_fully_read_total':48,'ad_queries':20,'retained_ad_ids_visible_text_read':68}
dump('synthesis/coverage.json',report)
print(json.dumps({'reddit':reddit,'MSE':mse_stats,'GeoBaby':geo_stats,'forums_combined':forums},indent=2))
