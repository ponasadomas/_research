#!/usr/bin/env python3
"""Render manually researched offer records; never infer facts from downloaded pages.

Input lives in scratchpad/market/notes.json. All source pages were read by the
market reader before entering these records. Raw captures remain frozen.
"""
from pathlib import Path
import json,re,collections
ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'scratchpad/market/notes.json').read_text())
quotes=[]
for n,row in enumerate(rows,1):
 slug=row['slug']; raw=ROOT/'_raw/competitors'/(row.get('quote_raw',slug+'.txt'))
 text=raw.read_text()
 norm=lambda s:re.sub(r'\s+',' ',s).strip()
 if norm(row['quote']) not in norm(text):raise ValueError(f'{slug}: quote missing from source: '+row['quote'])
 url=re.search(r'^SOURCE: (.*)$',text,re.M).group(1)
 qid=f'mkt01-{n:04d}'
 record=dict(id=qid,source='market-'+slug,url=url,date='',captured_at='2026-10-24',speaker='advisor',stage='unknown',type='belief',themes=['personalization'],quote=row['quote'],context=f"Published offer statement: {row['name']}.",raw_file=str(raw.relative_to(ROOT)),segment=row['segment'],source_class='competitor',evidence_kind='seller_claim')
 if slug=='cdc-milestone-tracker':record['evidence_kind']='official_resource_description'
 quotes.append(record)
 srcs=sorted(p for p in (ROOT/'_raw/competitors').glob(slug+'*.txt') if p.stem==slug or p.stem.startswith(slug+'--'))
 srcs=[p for p in srcs if not p.name.startswith('discovery-')]
 lines=[f"# {row['name']}",'','Captured 2026-10-24; public first-party offer description, not a verified purchase or efficacy result.',f"Source: [{url}]({url}). Raw captures: "+', '.join('`'+str(p.relative_to(ROOT))+'`' for p in srcs)+'.','',f"Buyer/trigger: {row['buyer']}",f"Mechanism (≤8 words): {row['mechanism']}",f"Observed price/term: {row['price']}",f"Format: {row['format']}",f"Personalization: {row['inputs']}",f"Promise, seller description: {row['promise']}",f"Proof offered, not independent verification: {row['proof']}",f"Objections addressed: {row['objections']}",'',f"Verbatim excerpt [{qid}]:",'',f"> {row['quote']}",'','## Comparison with Mamivio — interpretation','',row['comparison'],'','## Gaps','',row['gaps'],'']
 (ROOT/'competitors'/(slug+'.md')).write_text('\n'.join(lines))
voice=ROOT/'voice/market-01.jsonl'
if voice.exists():
 old=[json.loads(l) for l in voice.read_text().splitlines() if l.strip()]
 if [r['id'] for r in old]!=[r['id'] for r in quotes]:raise RuntimeError('Refuse to renumber existing market ids')
voice.write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in quotes))
index=['# Competitors and substitutes — 2026-10-24','',f'{len(rows)} individual notes. This is a discovered-offer inventory, not a census of all global competitors. Prices are dated public observations, not verified transactions. No product was purchased. English-speaking markets are the initial-launch scope selected by the owner; Lithuanian offers remain format references.','',
'All excerpts are traceable to frozen captures and machine-checked. Seller copy is recorded in `voice/market-01.jsonl` as `evidence_kind=seller_claim`, never as customer voice. CDC is an official tool description. Notes distinguish price labels, hidden legacy markup, localized currencies, store SKUs and unverified checkout availability.','',
'| Note | Category | Price observed | Personalization mechanism |','|---|---|---|---|']
for row in rows:index.append(f"| [{row['name']}]({row['slug']}.md) | {row['segment']} | {row['price']} | {row['mechanism']} |")
index+=['','## Reading this market','',
'Development has unusually strong free substitutes: Pathways supplies daily recommendations, expert activity videos and caregiver sharing; CDC supplies corrected-age checklists and a PDF summary. Kinedu sells both a daily app and a separate assessment/profile. These observations establish competing features, not consumer preference or market share. [mkt01-0003] [mkt01-0004] [mkt01-0006] [mkt01-0008]','',
'Solids has distinct one-time guide and app offers. 101 Before One publishes a $29 first-month plan; Solid Starts and BLW Meals already describe meal personalization/diet options. Household-specific shopping, cooking and caregiver needs would have to provide additional utility. [mkt01-0014] [mkt01-0026] [mkt01-0027]','',
'Work-return plans and postpartum plans exist as professional services, often with a planning conversation and follow-up. Those prices cannot be transferred directly to unsupported automated reports. They reveal observable deliverables and inputs worth testing. [mkt01-0015] [mkt01-0016] [mkt01-0017] [mkt01-0018] [mkt01-0023] [mkt01-0024] [mkt01-0025]','',
'## Access and coverage gaps','',
'See `../sources/competitor-access.jsonl`, `competitor-access-extra.jsonl` and `competitors.md`. Original domains not harvested after robots/access failures: The Wonder Weeks, Little Ones, Solid Starts, BLW Meals, Exclusive Pumping, Empowered Motherhood and Postpartum Support International. Solid Starts and BLW SOCIAL were inspected through their permitted developer App Store listings. Mothersplan pricing URL returned 404 despite an indexed result; it is not a verified current offer.','',
'No paid contents, customer accounts, emails, consultation outcomes, precise conversion volumes or ad profitability were inspected. ClickBank, Digistore24 and BuyGoods marketplace inventories were not harvested. Follow-up candidates from the related-app lists (Starting Solids: BLW & Purees, Annabel Karmel, My Little Food Critic, BabyPlate, Little Lunches and others) are discovery leads, not completed teardowns. Original-domain access gaps and these candidates prevent a claim that every serious English-market offer is covered.','']
(ROOT/'competitors/README.md').write_text('\n'.join(index))
print(f'{len(rows)} notes; {len(quotes)} market excerpts; '+str(collections.Counter(r['segment'] for r in rows)))
if (ROOT/'scratchpad/market-wave2/notes.json').exists():
 import subprocess,sys
 subprocess.run([sys.executable,str(ROOT/'_tools/build_market_wave2.py')],check=True)
