#!/usr/bin/env python3
"""Freeze a declared next comparison's CARDS only; no human triage/read claim."""
from pathlib import Path
import json,gzip,hashlib,collections
R=Path(__file__).resolve().parents[1];P=R/'_raw/reddit-deep/next-july-country-B-v1';P.mkdir(exist_ok=False)
jl=lambda p:[json.loads(x) for x in p.read_text().splitlines() if x.strip()]
rows=[x for x in jl(R/'_raw/reddit-deep/filter-v1/B-candidates.jsonl') if x['date'].startswith('2025-07-') and x['subreddit'] in ['BabyBumpsCanada','BabyBumpsandBeyondAu','BeyondTheBumpUK']];wanted={x['id'] for x in rows};native={}
for sub in sorted({x['subreddit'] for x in rows}):
 with gzip.open(R/f'_raw/reddit-deep/windows/2025-h2-v1/{sub}_submissions.jsonl.gz','rt') as f:
  for line in f:
   x=json.loads(line)
   if x['id'] in wanted:native[x['id']]=x
assert len(rows)==len(wanted)==len(native)==847
(P/'candidates.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows));C=P/'cards';C.mkdir();chunks=[];items=[];size=0

def flush():
 global items,size
 if not items:return
 n=len(chunks)+1;p=C/f'cards-{n:02}.txt';p.write_text('\n\n'.join(text for pid,text in items));chunks.append({'chunk':n,'file':str(p.relative_to(R)),'post_ids':[pid for pid,text in items],'utf8_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()});items=[];size=0
for x in rows:
 n=native[x['id']];card=f"ID {x['id']} | r/{x['subreddit']} | {x['date']} | {x['primary_topic']} | safety_flag={x['safety_flag']}\nTITLE: {n['title']}\nOPENING: {n.get('selftext','')[:350]}\nMATCHES: "+json.dumps({'friction_match':x['friction_match'],'matches':x['matches']},ensure_ascii=False)
 if items and size+len(card.encode())>40000:flush()
 items.append((x['id'],card));size+=len(card.encode())+2
flush();(P/'cards-index.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in chunks));report={'date':'2026-10-24','status':'Proposed NEXT reading scope; zero human cards triaged, zero original reads, zero quotes.','selection':'ALL July2025 B candidates inCanada/Australia/UK communities; no topic ranking/cap.','candidates':len(rows),'by_community':dict(collections.Counter(x['subreddit'] for x in rows)),'card_chunks':len(chunks),'card_bytes':sum(x['utf8_bytes'] for x in chunks),'OP_comment_sources_available':False,'source_file':'_raw/reddit-deep/filter-v1/B-candidates.jsonl','source_sha256':hashlib.sha256((R/'_raw/reddit-deep/filter-v1/B-candidates.jsonl').read_bytes()).hexdigest(),'plan':'Three readers share all cards; after human triage freeze and read EVERY keep, with actual count determined then. Current continuation B comparison was food/date-specific; this country/date comparison covers all topics.'};(P/'summary.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
