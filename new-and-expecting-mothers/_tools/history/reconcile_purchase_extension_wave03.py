#!/usr/bin/env python3
"""Reconcile all391 additional commercial cards, every keep and exact remaining IDs."""
from pathlib import Path
import json,csv,collections,hashlib
R=Path(__file__).resolve().parents[1];D=R/'_raw/report-purchase-archive-wave03';O=D/'final-v1';O.mkdir(exist_ok=True)
jl=lambda p:[json.loads(s) for s in p.read_text().splitlines() if s.strip()]
tsv=lambda p:list(csv.DictReader(p.open(),delimiter='\t'))
initial=jl(D/'commercial-candidates.jsonl');supp=jl(D/'supplement-v1/commercial-candidates.jsonl');initids={x['post_id'] for x in initial};suppids={x['post_id'] for x in supp};assert len(initids)==72 and len(suppids)==319 and not initids&suppids
tri03a=tsv(R/'scratchpad/report-purchase-archive-wave03/triage.tsv');tri03b=tsv(R/'scratchpad/report-purchase-archive-wave03/supplement-v1/triage.tsv');tri04=tsv(D/'supplement-v1/triage-04.tsv');tri05=tsv(D/'supplement-v1/triage-05.tsv');alltri=tri03a+tri03b+tri04+tri05
assert {x['post_id'] for x in tri03a}==initids
for n,rows in [(4,tri04),(5,tri05)]:assert {x['post_id'] for x in rows}==set(json.loads((D/f'supplement-v1/assignments/reader-{n:02}.json').read_text())['post_ids'])
assert {x['post_id'] for x in tri03b}==set(json.loads((D/'supplement-v1/assignments/owner-first56.json').read_text())['post_ids'])
assert len(alltri)==391==len({x['post_id'] for x in alltri}) and {x['post_id'] for x in alltri}==initids|suppids
ledgers={3:jl(R/'sources/report-purchase-archive-wave03-reading.jsonl'),4:jl(R/'sources/report-purchase-supplement-04-reading.jsonl'),5:jl(R/'sources/report-purchase-supplement-05-reading.jsonl')};triage={3:tri03a+tri03b,4:tri04,5:tri05};allreads=[];stats={}
for n,reads in ledgers.items():
 keep={x['post_id'] for x in triage[n] if x['label']!='drop'};assert keep=={x['post_id'] for x in reads} and len(reads)==len(keep)
 for x in reads:
  assert x['post_body_read_complete'] is True and x['available_identifiable_OP_replies_read']==0 and x['op_reply_ids_read']==[]
  assert hashlib.sha256((R/x['raw_file']).read_bytes()).hexdigest()==x['primary_unit_sha256']
  allreads.append(dict(x,reader=n))
 stats[n]={'cards':len(triage[n]),'kept_full':len(reads),'drops':len(triage[n])-len(reads),'eligible':sum(x['status']=='eligible' for x in reads),'excluded_after_read':sum(x['status']!='eligible' for x in reads),'quotes':len(jl(R/('voice/report-purchase-archive-wave03.jsonl' if n==3 else f'voice/report-purchase-supplement-{n:02}.jsonl')))}
readids={x['post_id'] for x in allreads};assert len(readids)==len(allreads)==122
main=json.loads((R/'_raw/reddit-deep/wave03-v1/final-read-post-ids.json').read_text());history=jl(R/'sources/reddit-purchase-followups-wave03-reading.jsonl')+jl(R/'sources/reddit-index-leads-wave03-reading.jsonl');histids={x['post_id'] for x in history};assert not readids&(set(main['full_original_post_ids'])|histids)
idx=jl(D/'native-index.jsonl');idxby={x['post_id']:x for x in idx};readable={x['post_id'] for x in idx if x['body_status']=='present'};assert len(idxby)==15226 and len(readable)==15088
unmatched=readable-(initids|suppids);drops={x['post_id'] for x in alltri if x['label']=='drop'};assert len(unmatched)==14697 and len(drops)==269 and not drops&readids
for name,ids in [('read-post-ids',readids),('card-drop-originals-unread',drops),('filter-unmatched-originals-unread',unmatched),('all-readable-originals-unread',readable-readids),('unavailable-original-bodies',set(idxby)-readable)]:
 (O/(name+'.json')).write_text(json.dumps(sorted(ids),indent=2)+'\n')
(O/'full-reading-inventory.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in allreads));(O/'all-card-decisions.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in alltri))
summary={'compiled_date':'2026-10-25','capture_date_UTC':'2026-10-24','published_files':2,'published_bytes':55769181,'whole_native_records_scanned':117713,'window_posts':15226,'readable_bodies':15088,'unavailable_bodies':138,'commercial_cards':391,'full_originals':122,'eligible':sum(x['status']=='eligible' for x in allreads),'excluded_after_read':sum(x['status']!='eligible' for x in allreads),'unread_keeps':0,'card_drop_bodies_unread':len(drops),'unmatched_bodies_unread':len(unmatched),'readable_bodies_unread':len(readable-readids),'OP_replies_read':0,'comments_source_unavailable_communities':2,'readers':stats}
(O/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
p=R/'synthesis/coverage.json';c=json.loads(p.read_text());c['date']='2026-10-25';c['reddit_purchase_extension']=summary|{'inventory':'_raw/report-purchase-archive-wave03/final-v1/'};c['all_reddit_full_original_post_ids_distinct']=len(set(main['full_original_post_ids'])|histids|readids);c['all_reddit_full_post_inventory']='_raw/audit/wave03-2026-10-24/all-reddit-full-post-ids-v2.json';(R/c['all_reddit_full_post_inventory']).write_text(json.dumps(sorted(set(main['full_original_post_ids'])|histids|readids),indent=2)+'\n');c.update(offer_pages_fully_read_total=73,competitor_notes=55,wave03_final_offer_followup_pages=15,wave03_seller_hosted_testimonials_read=22,wave03_partial_testimonial_previews=1,wave03_seller_process_illustrations_read=1);p.write_text(json.dumps(c,indent=2)+'\n');print(json.dumps(summary,indent=2));print('ALL DISTINCT FULL REDDIT POSTS',c['all_reddit_full_original_post_ids_distinct'])
