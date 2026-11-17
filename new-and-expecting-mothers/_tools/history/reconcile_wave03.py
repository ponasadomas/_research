#!/usr/bin/env python3
"""Reconcile completed country/commercial readings into a fresh cumulative ID inventory.
Requires every declared country keep; never rewrites older raw inventories.
"""
from pathlib import Path
import json,csv,collections,hashlib
R=Path(__file__).resolve().parents[1];D=R/'_raw/reddit-deep';O=D/'wave03-v1'
jl=lambda p:[json.loads(s) for s in p.read_text().splitlines() if s.strip()]
base=json.loads((D/'continuation-v1/final-read-post-ids.json').read_text());coverage=json.loads((R/'_raw/audit/wave03-2026-10-24/baseline34ec30af/synthesis/coverage.json').read_text())
packet=D/'next-july-country-B-v1/primary-v1';allcandidate={x['id'] for x in jl(D/'next-july-country-B-v1/candidates.jsonl')};triaged=set();newread={};readerstats={};countryledger=[]
for n in range(1,4):
 tri=list(csv.DictReader((D/f'triage/country-B-{n:02}.tsv').open(),delimiter='\t'));assigned=set(json.loads((packet/f'assignments/batch-{n:02}.json').read_text())['post_ids']);ids={x['post_id'] for x in tri}
 assert len(ids)==len(tri) and ids==assigned and not ids&triaged;triaged|=ids
 keep={x['post_id'] for x in tri if x['label']!='drop'};reads=jl(R/f'sources/reddit-country-B-{n:02}-reading.jsonl');assert {x['post_id'] for x in reads}==keep and len(reads)==len(keep)
 assert not keep&(set(base['full_original_post_ids'])|set(newread))
 for x in reads:
  assert x['post_body_read_complete'] is True;assert hashlib.sha256((R/x['raw_file']).read_bytes()).hexdigest()==x['primary_unit_sha256'];assert len(x['op_reply_ids_read'])==x['available_identifiable_OP_replies_read'];newread[x['post_id']]=x;countryledger.append(dict(x,reader=n))
 readerstats[n]={'cards':len(tri),'keep':len(keep),'drop':len(tri)-len(keep),'complete':len(reads),'eligible':sum(x['status']=='eligible' for x in reads),'excluded_after_read':sum(x['status']!='eligible' for x in reads)}
assert triaged==allcandidate and len(allcandidate)==847
root=jl(R/'sources/reddit-report-purchases-v2-reading.jsonl');extras=[]
for n in range(1,4):
 p=R/f'sources/reddit-country-B-{n:02}-extra-inspections.jsonl'
 if p.exists():extras+=jl(p)
 p=R/f'sources/reddit-country-B-{n:02}-duplicate-inspections.jsonl'
 if p.exists():extras+=jl(p)
full=set(base['full_original_post_ids'])|set(newread);op=set(base['available_OP_comment_ids_read']);aux=set(base['non_OP_auxiliary_comment_ids_read'])
for x in countryledger+root+extras:
 assert x['post_body_read_complete'] is True;full.add(x['post_id']);op.update(x['op_reply_ids_read'])
for n in range(1,4):
 p=R/f'sources/reddit-country-B-{n:02}-auxiliary-read.jsonl'
 if p.exists():
  for x in jl(p):assert x.get('full_comment_read') is True or x.get('body_read_complete') is True;aux.add(x['comment_id'])
tiers={t:{x['id']:x for x in jl(D/f'filter-v1/{t}-candidates.jsonl')} for t in ['A','B','C','unavailable']};meta={k:v for t in tiers.values() for k,v in t.items()};assert full<=set(meta)
O.mkdir(exist_ok=True);(O/'final-read-post-ids.json').write_text(json.dumps({'full_original_post_ids':sorted(full),'available_OP_comment_ids_read':sorted(op),'non_OP_auxiliary_comment_ids_read':sorted(aux)},indent=2)+'\n')
for t in ['A','B','C']:(O/f'unread-{t}-post-ids.json').write_text(json.dumps(sorted(set(tiers[t])-full),indent=2)+'\n')
unreadcomments=set(json.loads((D/'continuation-v1/unread-available-comment-ids.json').read_text()))-(op|aux);(O/'unread-available-comment-ids.json').write_text(json.dumps(sorted(unreadcomments),indent=2)+'\n')
(O/'country-B-full-reading-inventory.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in countryledger));(O/'root-commercial-reading-inventory.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in root));(O/'country-B-extra-reading-inventory.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in extras))
# Preserve A metadata while updating only the current snapshot's full-read fields.
A=[]
for x in jl(D/'continuation-v1/final-A-reading-inventory.jsonl'):
 if x['post_id'] in full and not x['full_original_primary_read']:
  hit=next(y for y in root+extras if y['post_id']==x['post_id']);x=dict(x,full_original_primary_read=True,status='full_primary_read',full_read_eligibility=hit['status'],raw_file=hit['raw_file'],wave03_full_reinspection=True)
 A.append(x)
(O/'final-A-reading-inventory.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in A))
r=coverage['reddit'];r.update(full_original_posts_distinct_ids=len(full),full_posts_by_subreddit=dict(collections.Counter(meta[p]['subreddit'] for p in full)),identifiable_OP_reply_records_read_distinct_ids=len(op),non_OP_comment_records_read=len(aux),A_original_bodies_unread=len(set(tiers['A'])-full),B_bodies_unread=len(set(tiers['B'])-full),C_bodies_unread=len(set(tiers['C'])-full),B_read_ids=sorted(set(tiers['B'])&full),C_read_ids=sorted(set(tiers['C'])&full),current_inventory='_raw/reddit-deep/wave03-v1/',available_comment_records_human_read_distinct=len(op|aux),available_comment_records_unread=len(unreadcomments),unread_available_comment_inventory='_raw/reddit-deep/wave03-v1/unread-available-comment-ids.json')
r['wave03']={'country_cards':len(triaged),'country_keeps':len(newread),'country_drops':len(triaged)-len(newread),'kept_unread':0,'readers':readerstats,'country_extra_inspections':len(extras),'root_commercial_cards':136,'root_full_read_occurrences':len(root),'root_full_distinct_ids':len({x['post_id'] for x in root}),'new_full_distinct_ids_total':len(full-set(base['full_original_post_ids'])),'new_OP_ids':len(op-set(base['available_OP_comment_ids_read'])),'country_full_reads_by_subreddit':dict(collections.Counter(meta[p]['subreddit'] for p in newread)),'country_post_read_status':dict(collections.Counter(x['status'] for x in countryledger))}
coverage.update(review_units_fully_read=219+80,app_review_units_fully_read=204+80,book_review_units_fully_read=15,competitor_notes=len(list((R/'competitors').glob('*.md')))-1,offer_pages_fully_read_total=48+6+4,wave03_report_buyer_seller_pages_fully_read=4,wave03_affiliate_review_articles_fully_read=1,wave03_seller_hosted_testimonials_read=18,wave03_public_offer_read_occurrences=8,wave03_reviews={'pages':8,'full_review_units':80,'unique_native_ids':80,'quoted_records':22,'unread_visible_reviews':0})
coverage['supplemental_historical_reddit_posts']=2
coverage['supplemental_historical_reddit_ledger']='sources/reddit-purchase-followups-wave03-reading.jsonl'
coverage['continuation']='All A candidates handled previously; all847preparedcountryBcards triaged and every584keep fully read, plus two complete commercial-purchase cohorts. Larger card-drop/B/C queues and source gaps remain.'
(R/'synthesis/coverage.json').write_text(json.dumps(coverage,indent=2)+'\n');summary={'reddit_full':len(full),'OP':len(op),'aux':len(aux),'unread_comments':len(unreadcomments),'unread_bodies':{t:len(set(tiers[t])-full) for t in ['A','B','C']},'wave03':r['wave03'],'reviews_full':coverage['review_units_fully_read']};(O/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
