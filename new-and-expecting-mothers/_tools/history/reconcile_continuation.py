#!/usr/bin/env python3
"""Complete continuation inventory; preserves every committed baseline raw inventory."""
from pathlib import Path
import json,csv,collections,hashlib
R=Path(__file__).resolve().parents[1];RAW=R/'_raw/reddit-deep';W=RAW/'aug-dec-2025-wave-v1';O=RAW/'continuation-v1'
jl=lambda p:[json.loads(x) for x in p.read_text().splitlines() if x.strip()]
tsv=lambda p:list(csv.DictReader(p.open(),delimiter='\t'))
base=json.loads((RAW/'final-read-post-ids.json').read_text());coverage=json.loads((R/'_raw/audit/continuation-2026-10-24/baseline-synthesis/synthesis/coverage.json').read_text())
triage={n:tsv(R/f'_raw/reddit-deep/triage/augdec-{n:02}.tsv') for n in range(1,5)}
assignment={1:'batch-01.json',2:'batch-02.json',3:'batch-03-after-transfer.json',4:'batch-04.json'}
for n,rows in triage.items():
 assert len(rows)==len({x['post_id'] for x in rows})
 assert {x['post_id'] for x in rows}==set(json.loads((W/'assignments'/assignment[n]).read_text())['post_ids'])
keeps={n:{x['post_id'] for x in rows if x['label']!='drop'} for n,rows in triage.items()}
newtriage={x['post_id']:dict(x,triage_batch=n) for n,rows in triage.items() for x in rows};assert len(newtriage)==sum(map(len,triage.values()))==6597
assert set(newtriage)=={x['post_id'] for x in jl(RAW/'final-unhandled-A.jsonl')}
t05=set(json.loads((W/'assignments/fullread-transfer-to-05-v1.json').read_text())['post_ids'])
part=json.loads((W/'assignments/root04-fullread-partitions-v1.json').read_text())['partitions'];partition={int(x['number']):set(x['post_ids']) for x in part}
t08=set(json.loads((W/'assignments/fullread-transfer-07-to-08-v1.json').read_text())['post_ids'])
expected={1:keeps[1]-t05,2:keeps[2],3:keeps[3],4:partition[4],5:t05,6:partition[6],7:partition[7]-t08,8:t08}
readers={n:jl(R/f'sources/reddit-augdec-{n:02}-reading.jsonl') for n in range(1,9)}
for n,rows in readers.items():
 assert {x['post_id'] for x in rows}==expected[n],f'Reader{n} incomplete or wrong IDs'
 assert len(rows)==len(expected[n]) and all(x['post_body_read_complete'] is True for x in rows)
newreads={x['post_id']:dict(x,reader_batch=n) for n,rows in readers.items() for x in rows};assert len(newreads)==sum(map(len,readers.values()))==sum(map(len,keeps.values()))
assert not set(newreads)&set(base['full_original_post_ids'])
b=jl(R/'sources/reddit-july-B-solids-reading.jsonl');bids={x['post_id'] for x in b};assert len(bids)==len(b)==126 and not bids&(set(base['full_original_post_ids'])|set(newreads))
inspections=jl(R/'sources/reddit-augdec-07-duplicate-inspections.jsonl')
auditreads={x['post_id']:x for x in inspections}
assert len(inspections)==len(auditreads)==2 and all(x['post_body_read_complete'] is True for x in inspections)
allread=set(base['full_original_post_ids'])|set(newreads)|bids|set(auditreads)
auditextra=set(auditreads)-(set(base['full_original_post_ids'])|set(newreads)|bids)
assert auditextra=={'1nfmfl0'}
op=set(base['available_OP_comment_ids_read']);aux=set(base['non_OP_auxiliary_comment_ids_read'])
for rows in list(readers.values())+[b,inspections]:
 for x in rows:
  assert len(x['op_reply_ids_read'])==x['available_identifiable_OP_replies_read'];op.update(x['op_reply_ids_read'])
newaux=[]
for name in [f'reddit-augdec-{n:02}' for n in range(1,9)]+['reddit-july-B-solids']:
 for x in jl(R/f'sources/{name}-auxiliary-read.jsonl'):
  assert x.get('full_comment_read') is True or x.get('body_read_complete') is True
  aux.add(x['comment_id']);newaux.append(dict(x,reader=name))
tiers={n:{x['id']:x for x in jl(RAW/f'filter-v1/{n}-candidates.jsonl')} for n in ['A','B','C','unavailable']}
metadata={pid:x for tier in tiers.values() for pid,x in tier.items()}
oldinv={x['post_id']:x for x in jl(RAW/'final-A-reading-inventory.jsonl')};rows=[]
for pid,item in tiers['A'].items():
 old=oldinv[pid];new=newtriage.get(pid);full=pid in allread
 status='full_primary_read' if full else 'card_excluded_original_unread'
 assert full or old['july_card_triaged'] or (new and new['label']=='drop')
 rows.append(dict(post_id=pid,subreddit=item['subreddit'],july_card_triaged=old['july_card_triaged'],continuation_card_triaged=bool(new),full_original_primary_read=full,status=status,full_read_eligibility=newreads[pid]['status'] if pid in newreads else ('duplicate_audit_inspection' if pid in auditreads else 'see_baseline_ledger'),raw_file=newreads[pid]['raw_file'] if pid in newreads else (auditreads[pid]['raw_file'] if pid in auditreads else old['raw_file'])))
O.mkdir(exist_ok=True)
(O/'final-A-reading-inventory.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in rows))
(O/'final-unhandled-A.jsonl').write_text('')
(O/'final-read-post-ids.json').write_text(json.dumps(dict(full_original_post_ids=sorted(allread),available_OP_comment_ids_read=sorted(op),non_OP_auxiliary_comment_ids_read=sorted(aux)),indent=2)+'\n')
(O/'continuation-full-reading-inventory.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in newreads.values()))
(O/'continuation-auxiliary-comments-read.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in newaux))
for tier in ['A','B','C']:
 (O/f'unread-{tier}-post-ids.json').write_text(json.dumps(sorted(set(tiers[tier])-allread),indent=2)+'\n')
r=coverage['reddit'];r.update(full_original_posts_distinct_ids=len(allread),full_posts_by_subreddit=dict(collections.Counter(metadata[p]['subreddit'] for p in allread)),identifiable_OP_reply_records_read_distinct_ids=len(op),non_OP_comment_records_read=len(aux),outside_July_A_unhandled=0,A_original_bodies_unread=len(set(tiers['A'])-allread),B_bodies_unread=len(set(tiers['B'])-allread),C_bodies_unread=len(set(tiers['C'])-allread),B_read_ids=sorted(set(tiers['B'])&allread),C_read_ids=sorted(set(tiers['C'])&allread),six_month_card_chunks_with_unhandled_ids=0)
r.update(all_A_candidates_human_handled=len(tiers['A']),A_cards_human_triaged=1661+len(newtriage),A_other_full_source_handled=26,continuation_cards_triaged=len(newtriage),continuation_audit_inspections=len(inspections),continuation_audit_extra_full_posts=len(auditextra),continuation_card_drop_bodies_unread_after_audit=sum(x['label']=='drop' and pid not in allread for pid,x in newtriage.items()),continuation_card_drops=sum(x['label']=='drop' for x in newtriage.values()),continuation_initial_keeps=len(newreads),continuation_full_posts=len(newreads),continuation_full_read_eligible=sum(x['status']=='eligible' for x in newreads.values()),continuation_full_read_excluded=sum(x['status']!='eligible' for x in newreads.values()),continuation_OP_replies_read=sum(x['available_identifiable_OP_replies_read'] for x in newreads.values()),B_comparison_cards=178,B_comparison_full_posts=126,B_comparison_OP_replies_read=256,current_inventory='_raw/reddit-deep/continuation-v1/',baseline_inventory_immutable='_raw/reddit-deep/final-A-reading-inventory.jsonl',continuation_kept_unread=0,continuation_readers={str(n):dict(posts=len(v),OP_replies=sum(x['available_identifiable_OP_replies_read'] for x in v)) for n,v in readers.items()})
coverage['continuation']='All6597remaining A cards and every human keep complete; finite July BLW B comparison complete. Baseline raw inventories preserved.'
(R/'synthesis/coverage.json').write_text(json.dumps(coverage,indent=2)+'\n');print(json.dumps(r,indent=2))
