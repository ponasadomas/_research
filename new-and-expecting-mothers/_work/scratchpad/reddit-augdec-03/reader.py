"""Save only explicit human card decisions; exact-scope checks, no automatic classifier."""
from pathlib import Path
import json,csv,re,hashlib,datetime,collections
ROOT=Path(__file__).resolve().parents[2]
PACKET=ROOT/'_raw/reddit-deep/aug-dec-2025-wave-v1'
MANIFEST=json.loads((PACKET/'assignments/batch-03-after-transfer.json').read_text())
TRIAGE=ROOT/'_raw/reddit-deep/triage/augdec-03.tsv'
SCRATCH=ROOT/'scratchpad/reddit-augdec-03'
LABELS=set('keep_play keep_solids keep_pumping_work keep_sleep keep_postpartum keep_pregnancy keep_registry keep_other drop'.split())
def cards(number):
 c=MANIFEST['chunks'][number-1];s=(ROOT/c['file']).read_text();parts=[x for x in re.split(r'(?=^ID )',s,flags=re.M) if x.startswith('ID ')]
 assert [x.split()[1] for x in parts]==c['post_ids']
 return c,parts
def show(number):
 c,parts=cards(number)
 for n,p in enumerate(parts,1):print(f'\nCARD {n}\n{p}')
def save(number,decisions,note=''):
 c,parts=cards(number);parsed={}
 for line in decisions.strip().splitlines():
  num,label,reason=line.split('|',2);num=int(num);assert num not in parsed and label in LABELS and reason.strip();parsed[num]=(label,reason.strip())
 assert set(parsed)==set(range(1,len(parts)+1)),('Exact explicit decisions required',number,sorted(set(range(1,len(parts)+1))-set(parsed)))
 old=list(csv.DictReader(TRIAGE.open(),delimiter='\t')) if TRIAGE.exists() else []
 assert not set(c['post_ids'])&{r['post_id'] for r in old},'Do not rerun an appended card batch'
 exists=TRIAGE.exists()
 with TRIAGE.open('a') as f:
  w=csv.writer(f,delimiter='\t');
  if not exists:w.writerow(['post_id','label','reason','card_file'])
  for n,tid in enumerate(c['post_ids'],1):w.writerow([tid,*parsed[n],c['file']])
 rec={'assignment_chunk':number,'card_file':c['file'],'sha256':hashlib.sha256((ROOT/c['file']).read_bytes()).hexdigest(),'post_ids':c['post_ids'],'cards_read_complete':True,'card_count':len(parts),'note':note,'read_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 with (SCRATCH/'triage-reading-ledger.jsonl').open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
 allrows=list(csv.DictReader(TRIAGE.open(),delimiter='\t'))
 state={'assigned_cards':MANIFEST['cards'],'assigned_card_files':MANIFEST['card_chunks'],'cards_fully_read_and_triaged':len(allrows),'completed_card_files':len({x['card_file'] for x in allrows}),'keep_so_far':sum(x['label']!='drop' for x in allrows),'drop_so_far':sum(x['label']=='drop' for x in allrows),'labels':dict(collections.Counter(x['label'] for x in allrows)),'primary_originals_read':0,'quotes':0,'next_assignment_chunk':number+1}
 (SCRATCH/'checkpoint.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
 source=ROOT/'sources/reddit-augdec-03.md'
 if source.exists():source.write_text(re.sub(r'Current exact checkpoint: .*?\n',lambda _: 'Current exact checkpoint: '+json.dumps(state,ensure_ascii=False)+'\n',source.read_text(),count=1))
 print('Saved',number,len(parts),'cards',dict(collections.Counter(x[0] for x in parsed.values())))
