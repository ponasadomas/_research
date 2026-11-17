#!/usr/bin/env python3
"""Persist human decisions after each entire assigned July card file is read."""
import json,csv,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];PACKET=ROOT/'_raw/reddit-deep/july-2025-wave-v1';OUT=ROOT/'_raw/reddit-deep/triage/july-focused.tsv'
ASSIGNED={'beyondthebump','ExclusivelyPumping','workingmoms','BabyLedWeaning','BeyondTheBumpUK'}
def save(subreddit,number,decisions,inspections=None):
 filename=f'July-A-{subreddit}-{number:03}.txt'
 card=next(r for r in map(json.loads,(PACKET/'triage-cards-index.jsonl').read_text().splitlines()) if r['file'].endswith('/'+filename))
 assert subreddit in ASSIGNED
 assert set(decisions)==set(range(1,len(card['post_ids'])+1)),('Missing card decisions',set(range(1,len(card['post_ids'])+1))-set(decisions))
 old=[]
 if OUT.exists():
  with OUT.open() as f:old=list(csv.DictReader(f,delimiter='\t'))
 assert not set(card['post_ids'])&{r['post_id'] for r in old},'Already saved file or duplicate ids'
 OUT.parent.mkdir(exist_ok=True)
 with OUT.open('a') as f:
  w=csv.writer(f,delimiter='\t')
  if not old:w.writerow(['post_id','label','reason'])
  for i,tid in enumerate(card['post_ids'],1):
   label,reason=decisions[i];assert label=='drop' or label.startswith('keep_');w.writerow([tid,label,reason])
 ledger=ROOT/'sources/reddit-july-focused-card-ledger.jsonl'
 with ledger.open('a') as f:f.write(json.dumps({'file':card['file'],'cards':card['cards'],'status':'all_cards_read_and_human_triaged','full_source_eligibility_inspections':inspections or [],'kept_primary_units_read':0,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})+'\n')
 print(filename,len(decisions),'cards',sum(v[0]!='drop' for v in decisions.values()),'kept')
def audit():
 cards=[r for r in map(json.loads,(PACKET/'triage-cards-index.jsonl').read_text().splitlines()) if r['subreddit'] in ASSIGNED]
 expected={tid for r in cards for tid in r['post_ids']}
 with OUT.open() as f:rows=list(csv.DictReader(f,delimiter='\t'))
 actual=[r['post_id'] for r in rows]
 print({'expected':len(expected),'actual':len(actual),'missing':sorted(expected-set(actual)),'unexpected':sorted(set(actual)-expected),'duplicate_count':len(actual)-len(set(actual))})
if __name__=='__main__':audit()
