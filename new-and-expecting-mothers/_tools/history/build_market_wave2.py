#!/usr/bin/env python3
"""Render the manually read second market wave without changing market-01 ids."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'scratchpad/market-wave2/notes.json').read_text())
qs=[]
def addq(slug,quote,rawname,context):
 raw=ROOT/'_raw/competitors'/rawname;text=raw.read_text()
 norm=lambda s:re.sub(r'\s+',' ',s).strip()
 assert norm(quote) in norm(text),(slug,quote)
 qid=f'mkt02-{len(qs)+1:04d}'
 url=re.search(r'^SOURCE: (.*)$',text,re.M).group(1)
 qs.append(dict(id=qid,source='market-'+slug,url=url,date='',captured_at='2026-10-24',speaker='advisor',stage='unknown',type='belief',themes=['first_solids','personalization','meal_planning'],quote=quote,context=context,raw_file=str(raw.relative_to(ROOT)),segment='solids',source_class='competitor',evidence_kind='seller_claim'))
 return qid,url
for row in rows:
 slug=row['slug'];qid,url=addq(slug,row['quote'],row.get('quote_raw',slug+'.txt'),'Published offer description: '+row['name']+'.')
 srcs=sorted(p for p in (ROOT/'_raw/competitors').glob(slug+'*.txt') if p.stem==slug or p.stem.startswith(slug+'--'))
 body=[f"# {row['name']}",'','Captured 2026-10-24, follow-up market wave. First-party seller description; no purchase, generated-plan evaluation or efficacy verification.',f"Source: [{url}]({url}). Raw text: "+', '.join('`'+str(p.relative_to(ROOT))+'`' for p in srcs)+'.','',f"Buyer/trigger: {row['buyer']}",f"Mechanism (≤8 words): {row['mechanism']}",f"Observed price/term: {row['price']}",f"Format: {row['format']}",f"Personalization: {row['inputs']}",f"Promise, seller description: {row['promise']}",f"Proof offered, not independent verification: {row['proof']}",f"Objections addressed: {row['objections']}",'',f"Verbatim excerpt [{qid}]:",'',f"> {row['quote']}",'','## Comparison with Mamivio — interpretation','',row['comparison'],'','## Gaps','',row['gaps'],'']
 (ROOT/'competitors'/(slug+'.md')).write_text('\n'.join(body))
extras=[
('little-lunches','$49.99/year ($4.17/mo).','little-lunches--pricing.txt','Published web pricing; checkout and location-specific terms untested.'),
('little-lunches','Reuse pantry ingredients','little-lunches.txt','The provider describes pantry-ingredient reuse among planning benefits.'),
('little-lunches','Add another parent or caregiver to plan together','little-lunches--appstore.txt','Developer describes shared household planning.'),
('babyplate',"Ideas adapt based on what you've already introduced",'babyplate.txt','Developer describes weekly ideas adapting to prior foods.'),
('babyplate','Kosher filtering','babyplate.txt','Developer lists another dietary framework; compliance not independently checked.'),
('orango-blw-recipes','grocery buy list','orango-blw-recipes.txt','Developer describes turning a selected date range into groceries.'),
('annabel-karmel','Plan your family’s mealtimes with custom Meal Planners','annabel-karmel--appstore.txt','Developer describes family meal planning.'),
('my-little-food-critic','MLFC Monthly $3.99','my-little-food-critic--appstore.txt','US App Store purchase listing; differs from website price copy.'),
('orango-blw-recipes',"family's diet",'orango-blw-recipes.txt','Developer describes fitting generated plans to the family diet.')]
for x in extras:addq(*x)
voice=ROOT/'voice/market-02.jsonl'
if voice.exists():
 old=[json.loads(l) for l in voice.read_text().splitlines() if l.strip()]
 assert [q['id'] for q in old]==[q['id'] for q in qs],'Refuse to renumber existing second-wave ids'
voice.write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in qs))
index=ROOT/'competitors/README.md';s=index.read_text()
s=re.sub(r'^\d+ individual notes\.', '34 individual notes (27 original, 7 follow-up).', s, count=1,flags=re.M)
s=s.replace('`voice/market-01.jsonl` as','`voice/market-01.jsonl` and `voice/market-02.jsonl` as')
marker='## Follow-up wave — first-solids planning substitutes'
if marker in s:s=s.split(marker)[0].rstrip()+'\n'
old='Follow-up candidates from the related-app lists (Starting Solids: BLW & Purees, Annabel Karmel, My Little Food Critic, BabyPlate, Little Lunches and others) are discovery leads, not completed teardowns.'
s=s.replace(old,'The five named first-solids follow-ups are now inspected below; the broader related-app universe remains non-exhaustive.')
s+='\n'+marker+'\n\nAll five named follow-ups have notes. My Little Food Critic’s 28-Day Meal Plan and Orango’s generated-plan app are two additional direct substitutes. Eleven successful new page captures were read; Annabel’s original domain was excluded by robots, and its permitted App Store listing used. The market excerpt files now contain 43 records, all labeled as offer evidence.\n\n'
s+='| Note | Observed price | Relevant personalization |\n|---|---|---|\n'
for row in rows:s+=f"| [{row['name']}]({row['slug']}.md) | {row['price']} | {row['inputs']} |\n"
s+='\nThe proposed household-specific first-30-days solids report is not a feature gap established by this research. Little Lunches already describes family ages/preferences, selected meals, grocery automation, ingredient reuse and caregiver access; BabyPlate describes cultural-diet filters and food-history adaptation; Orango explicitly generates 1–100-day plans. The untested proposition is whether some parents prefer a finite, portable report over these apps. [mkt02-0005] [mkt02-0006] [mkt02-0007] [mkt02-0009] [mkt02-0010] [mkt02-0011] [mkt02-0013] [mkt02-0016]\n\n'
s+='My Little Food Critic also sells a 28-day guide: duration is not an unoccupied format. Existing advertised prices do not establish Mamivio’s demand or willingness to pay. [mkt02-0004]\n\nSee `../synthesis/reader-notes-market-wave2.md` and `../sources/marketplaces.md` for changed interpretation and actual marketplace access probes.\n'
index.write_text(s)
print(f'{len(rows)} new notes; {len(qs)} new offer excerpts; market-01 unchanged')
