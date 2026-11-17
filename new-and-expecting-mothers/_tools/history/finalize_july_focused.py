"""Finalize reader-owned metadata and precise additive source inventories; never alter raw capture."""
from july_focused_reader import *
import gzip,collections

rows=[json.loads(x) for x in VOICE.read_text().splitlines()]
flags=json.loads((ROOT/'sources/reddit-july-focused-duplicate-flags.json').read_text())
groups=[]
for n,g in enumerate(flags['exact_body_groups_touching_assigned'],1):
 groups.append({'group_id':f'focused-exact-{n:02}','kind':'exact_normalized_body','post_ids':[x['id'] for x in g]})
for n,g in enumerate(flags['near_body_pairs_touching_assigned'],1):
 groups.append({'group_id':f'focused-near-{n:02}','kind':'near_body_machine_flag_human_triaged','post_ids':[x['id'] for x in g['records']],'jaccard_5word':g['jaccard_5word']})
groups += [
 {'group_id':'focused-manual-pump-near','kind':'same_author_near_duplicate_human_read','post_ids':['1m9a034','1m9aewx'],'selected_representative':'1m9a034','excluded_later':'1m9aewx'},
 {'group_id':'focused-teacher-related','kind':'same_author_related_question_not_independent_person','post_ids':['1m1ljot','1m1lsou']},
 {'group_id':'focused-career-related','kind':'same_author_related_followup_not_independent_person','post_ids':['1lzzqlk','1m5412d']},
 {'group_id':'focused-happysleeper-followup','kind':'same_author_changed_question_and_later_outcome','post_ids':['1lp19lb','1lscc4q'],'note':'Later source reports sleep improved after4days but spouse opposed method; earlier outing constraint not a claim of overall failure.'}
]
corrections=[]
for r in rows:
 r['Mamivio_report_purchase_proven']=False
 r['population_inference']='Purposive archived testimony; not representative prevalence or verified independent customer sample.'
 r['related_body_groups']=[g['group_id'] for g in groups if r['post_id'] in g['post_ids']]
 if r['related_body_groups']:r['independent_voice_limit']='Related crossposts/replies describe one account/body, not additional independent customers; cross-reader reconciliation required.'
 if r['id']=='rjfc01-0090':r['payment_signal']='explicit_competitor_personalized_sleep_analysis_purchase'
 elif r.get('reported_purchase'):r['payment_signal']='reported_adjacent_'+r.get('purchase_category','purchase')
 elif r.get('purchase_status'):r['payment_signal']='qualified_'+r['purchase_status']
 else:r['payment_signal']='no_explicit_transaction_in_selected_excerpt'
 if r['id']=='rjfc01-0071':r['later_same_author_context']='1lscc4q reports improved sleep after4days but spouse concerns; no independently verified efficacy.'
 if r['id']=='rjfc01-0083':
  corrections.append({'id':r['id'],'field':'speaker','before':r['speaker'],'after':'parent_unspecified','reason':'First-time parents and future breastfeeding do not explicitly establish mother self-identification.'});r['speaker']='parent_unspecified'
 if r['id']=='rjfc01-0075':
  corrections.append({'id':r['id'],'field':'stage','before':r['stage'],'after':'unknown','reason':'Expecting soon does not establish gestational week.'});r['stage']='unknown'
VOICE.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
(ROOT/'sources/reddit-july-focused-metadata-corrections.json').write_text(json.dumps(corrections,ensure_ascii=False,indent=2)+'\n')
with (ROOT/'_raw/reddit-deep/triage/july-focused.tsv').open() as f:tri=list(csv.DictReader(f,delimiter='\t'))
triidx={r['post_id']:r for r in tri};kept={r['post_id'] for r in tri if r['label']!='drop'}
ledger=[json.loads(x) for x in LEDGER.read_text().splitlines()];li={r['post_id']:r for r in ledger}
promotion=[r for r in tri if any(s in r['reason'].lower() for s in ['promo','seller','recruit','market-research','creator','medium','amalma','watchwise','thrive'])]
(ROOT/'sources/reddit-july-focused-promotion-review.json').write_text(json.dumps({'basis':'Human card readings plus separately logged complete-source eligibility inspections; original wording preserved in triage reasons. Linked pages/media not followed. Suspicion does not prove seller affiliation.','screening_records':promotion,'retained_cautions':[{'post_id':'1lzp6af','finding':'Prospective product auto-off question; no explicit seller affiliation or purchase; not automatically promotional.'},{'post_id':'1m9x8ft','finding':'Detailed enthusiastic pump review, no exposed affiliate marker. Independence unverified; not excluded solely for tone.'},{'post_id':'1m8l9o5','finding':'FamilyAlbum member-display support question; no memorybook seller pitch in body.'}],'memorybook_cluster':'No retained photo/AI memorybook seller body was identified within assigned five-community originals. This is a bounded inspection, not a claim of no promotion in Reddit.'},ensure_ascii=False,indent=2)+'\n')
(ROOT/'sources/reddit-july-focused-duplicate-review.json').write_text(json.dumps({'groups':groups,'scope':'All1661 July bodies machine-screened, human card/source decisions only for assigned scope. Exact/near group is not automatically malicious or fraudulent.','within_assignment':'At card stage kept earliest eligible representative of repeated body; new full-read pump near-duplicate excluded later. Distinct later OP replies are not independent people.','cross_reader_quote_overlap':[{'this_quote':'rjfc01-0078','other_quote':'rjnp01-0058','post_ids':['1lx2kpy','1lwzwe9'],'finding':'Same body/account; two excerpts are not two independent buyers. Gifted Lovevery, not author purchase.'}]},ensure_ascii=False,indent=2)+'\n')
final=[]
for tid in sorted(kept):
 x=li[tid].copy();x['card_decision']=triidx[tid]['label'];x['quote_ids']=[r['id'] for r in rows if r['post_id']==tid];x['related_body_groups']=[g['group_id'] for g in groups if tid in g['post_ids']];final.append(x)
(ROOT/'sources/reddit-july-focused-final-status.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in final))
(ROOT/'sources/reddit-july-focused-post-read-exclusions.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in final if r['read_status']!='read_complete'))
auxread=[json.loads(x) for x in (ROOT/'sources/reddit-july-focused-auxiliary-read.jsonl').read_text().splitlines()]
readpairs={(r['post_id'],r['comment_id']) for r in auxread};unread=[]
for tid in sorted(kept):
 u=unit(tid);p=PACKET/'auxiliary-comments'/f"{u['meta']['subreddit']}-{tid}.jsonl.gz"
 if not p.exists():continue
 with gzip.open(p,'rt') as f:comments=[json.loads(x) for x in f]
 ids=[r['id'] for r in comments];notread=[cid for cid in ids if (tid,cid) not in readpairs]
 unread.append({'post_id':tid,'raw_file':str(p.relative_to(ROOT)),'archived_nonOP_comments':len(ids),'human_read_exact_parent_ids':[cid for cid in ids if (tid,cid) in readpairs],'unread_comment_ids':notread,'unread_count':len(notread),'scope':'No entire nonOP comment list read. Exact parent reads only.'})
(ROOT/'sources/reddit-july-focused-unread-auxiliary-index.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in unread))
print('Finalized',len(rows),'quotes;',len(final),'post outcomes;',len(auxread),'exact auxiliary reads;',sum(r['unread_count'] for r in unread),'unread nonOP comments')
