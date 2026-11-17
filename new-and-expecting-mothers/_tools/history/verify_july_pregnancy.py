#!/usr/bin/env python3
"""Verify frozen selected originals, lossless human reading views, per-ID outcomes, and exact quote/schema provenance."""
from pathlib import Path
import json,csv,re,hashlib,collections
r=Path(__file__).resolve().parents[1];d=r/'scratchpad/reddit-july-pregnancy';m=json.loads((d/'kept-manifest.json').read_text());idx={x['post_id']:x for x in m['units']};tri=list(csv.DictReader((r/'_raw/reddit-deep/triage/july-pregnancy.tsv').open(),delimiter='\t'));out=[json.loads(x) for x in (r/'sources/reddit-july-pregnancy-fullread-outcomes.jsonl').read_text().splitlines()]; oi={x['post_id']:x for x in out};q=[json.loads(x) for x in (r/'voice/reddit-july-pregnancy.jsonl').read_text().splitlines()]; fail=[]
def check(ok,msg):
 if not ok:fail.append(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assigned=[]
for x in map(json.loads,(r/'_raw/reddit-deep/july-2025-wave-v1/triage-cards-index.jsonl').read_text().splitlines()):
 if x['subreddit'] in {'BabyBumps','BabyBumpsCanada','BabyBumpsandBeyondAu'}:assigned+=x['post_ids']
check(len(tri)==len({x['post_id'] for x in tri})==len(assigned)==495,'495 unique card IDs');check({x['post_id'] for x in tri}==set(assigned),'Exact assigned card ID set');check({x['post_id'] for x in tri if x['label']!='drop'}==set(idx),'Frozen keep IDs equal human card decisions');check(len(out)==len(oi)==len(idx)==273,'273 exact full-read outcomes');check(set(oi)==set(idx),'Exact outcome ID set');check(all(x['complete_archived_original_read'] and x['read_scope']=='full_post' and x['comments_available']==False and x['OP_followups_available']==False for x in out),'Full-post/no-comments scope');
reads=[json.loads(x) for x in (d/'fullreading-ledger.jsonl').read_text().splitlines()];check(len(reads)==len({x['chunk'] for x in reads})==17,'17 unique complete chunk reads');check({x['chunk'] for x in reads}=={x['file'] for x in m['chunks']},'Exact chunk read set')
for u in idx.values():
 check(sha(r/u['raw_file'])==u['sha256'],'Raw hash '+u['post_id']);check(oi[u['post_id']]['sha256']==u['sha256'],'Outcome hash '+u['post_id'])
for c in m['chunks']:check(sha(r/c['file'])==c['sha256'],'Frozen chunk hash '+c['file'])
views=json.loads((d/'fulltext-views-manifest.json').read_text())
for v,c in zip(views,m['chunks']):
 check(sha(r/v['file'])==v['sha256'],'Reading view hash '+v['file']);blocks=[]
 for i in c['post_ids']:
  u=idx[i];raw=(r/u['raw_file']).read_text();text=raw[raw.index('=== COMPLETE ORIGINAL POST TITLE ==='):];blocks.append(f"\nID {i} | r/{u['subreddit']} | {u['post_date']} | reported_comments={u['post_reported_num_comments']} | scope=full_post_no_comments\nURL {u['url']}\n"+text)
 check((r/v['file']).read_text()=='\n'.join(blocks),'Lossless complete original title/body/followup text '+v['file'])
cardreads=[json.loads(x) for x in (d/'triage-reading-ledger.jsonl').read_text().splitlines()];check(len(cardreads)==9,'Nine card chunk reads')
for cr in cardreads:
 p=r/cr['file'];check(sha(p)==cr['sha256'],'Card read hash '+cr['file'])
speakers=set('expecting_mother,new_mother,experienced_mother,parent_unspecified,partner,relative_caregiver,recovered_parent,gave_up_parent,advisor,professional,reviewer,skeptic'.split(','));stages=set('pregnancy_early,pregnancy_late,newborn_0_6_weeks,baby_6_16_weeks,baby_4_6_months,baby_6_12_months,toddler,return_to_work,looking_back,unknown'.split(','));types=set('trigger_moment,pain,fear,tried_failed,desire,belief,question,objection,advice_given,success_story,failure_story,regret,others_said'.split(','));seen=set()
for x in q:
 check(x['id'] not in seen,'Unique quote ID '+x['id']);seen.add(x['id']);check(x['speaker'] in speakers and x['stage'] in stages and x['type'] in types,'README vocabulary '+x['id']);check(len(x['context'].split())<=25,'Context length '+x['id']);u=idx[x['post_id']];check(oi[x['post_id']]['final_status']=='retain','Quote not dropped '+x['id']);check(x['raw_file']==u['raw_file'] and x['url']==u['url'] and x['date']==u['post_date'],'Quote source metadata '+x['id']);check(x['paid_report_demand_proven']==False,'No unsupported paid report demand '+x['id']);raw=(r/x['raw_file']).read_text();body=raw.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0];pos=0
 for piece in x['quote'].split(' […] '):
  at=body.find(piece,pos);check(at>=0,'Exact own body substring '+x['id']);pos=max(pos,at+len(piece))
stats={'assigned_cards':len(tri),'card_chunks_fully_read':len(cardreads),'initial_card_drops':sum(x['label']=='drop' for x in tri),'provisional_retained_originals':len(idx),'provisional_originals_fully_read':len(out),'post_read_drops':sum(x['final_status']=='drop' for x in out),'final_retained_originals':sum(x['final_status']=='retain' for x in out),'final_retained_originals_fully_read':sum(x['final_status']=='retain' and x['complete_archived_original_read'] for x in out),'kept_originals_unread':0,'retained_reading_chunks':len(m['chunks']),'retained_chunks_fully_read':len(reads),'quote_count':len(q),'comments_read':0,'OP_followups_read':0,'linked_media_read':0,'complete_live_Reddit_threads_read':0,'by_community':dict(collections.Counter(idx[x['post_id']]['subreddit'] for x in out if x['final_status']=='retain')),'quote_payment_signal_counts':dict(collections.Counter(x['payment_signal'] for x in q))}
report={'failed':len(fail),'failures':fail,'stats':stats,'checks':'Exact495 assigned cards; human keep manifest;273 raw hashes;17 frozen chunks and17 lossless original-text views;17 human read ledger entries; per-ID outcomes; exact own-body quotes; README vocabulary; context<=25words; no dropped quote source; provenance/date/URL; no report-payment inference.'};(r/'synthesis/reddit-july-pregnancy-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));raise SystemExit(bool(fail))
