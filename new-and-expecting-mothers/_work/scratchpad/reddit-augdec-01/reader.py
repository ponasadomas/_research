import collections,csv,hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
WORK=Path(__file__).parent
WAVE=ROOT/'_raw/reddit-deep/aug-dec-2025-wave-v1'
MANIFEST=json.loads((WAVE/'assignments/batch-01.json').read_text())
INDEX={x['post_id']:x for x in map(json.loads,(WAVE/'primary-index.jsonl').read_text().splitlines())}
TRIAGE=ROOT/'_raw/reddit-deep/triage/augdec-01.tsv'
CODES={'r':'keep_registry','p':'keep_pregnancy','o':'keep_other','w':'keep_pumping_work','s':'keep_sleep','f':'keep_solids','h':'keep_postpartum','a':'keep_play','d':'drop'}
def card(n,start=0,stop=None):
 c=MANIFEST['chunks'][n-1]
 cards=re.split(r'(?=^ID )',(ROOT/c['file']).read_text(),flags=re.M)
 cards=[x for x in cards if x.strip()]
 print(''.join(cards[start:stop]))
def save(n,text):
 c=MANIFEST['chunks'][n-1]
 updates=[]
 for line in text.strip().splitlines():
  i,code,reason=line.split('|',2)
  updates.append(dict(post_id=i,label=CODES[code],reason=reason,card_file=c['file']))
 assert [x['post_id'] for x in updates]==c['post_ids'],('Order/count mismatch',n,len(updates),len(c['post_ids']))
 old=list(csv.DictReader(TRIAGE.open(),delimiter='\t')) if TRIAGE.exists() else []
 assert not (set(x['post_id'] for x in old)&set(c['post_ids'])), 'Already triaged; do not overwrite'
 TRIAGE.parent.mkdir(parents=True,exist_ok=True)
 with TRIAGE.open('a',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['post_id','label','reason','card_file'],delimiter='\t')
  if not old:w.writeheader()
  w.writerows(updates)
 allrows=old+updates
 (WORK/'triage-progress.json').write_text(json.dumps({'completed_cards':len(allrows),'label_counts':dict(collections.Counter(x['label'] for x in allrows)),'last_chunk':n},indent=2)+'\n')
 print(json.dumps({'saved_chunk':n,'cards':len(updates),'completed_cards':len(allrows),'label_counts':dict(collections.Counter(x['label'] for x in allrows))}))
if __name__=='__main__':
 if sys.argv[1]=='card':card(int(sys.argv[2]),int(sys.argv[3]) if len(sys.argv)>3 else 0,int(sys.argv[4]) if len(sys.argv)>4 else None)
 if sys.argv[1]=='save':save(int(sys.argv[2]),sys.stdin.read())
