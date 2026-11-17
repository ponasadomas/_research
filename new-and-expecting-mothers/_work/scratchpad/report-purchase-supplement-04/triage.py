import csv,json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]
a=json.loads((R/'_raw/report-purchase-archive-wave03/supplement-v1/assignments/reader-04.json').read_text())
index={x['post_id']:x for x in map(json.loads,(R/a['primary_index']).read_text().splitlines())}
p=R/'_raw/report-purchase-archive-wave03/supplement-v1/triage-04.tsv'
old=list(csv.DictReader(p.open(),delimiter='\t')) if p.exists() else []
ids={x['post_id'] for x in old}
new=[]
for line in sys.stdin:
 if not line.strip():continue
 id,label,reason=line.rstrip('\n').split('\t')
 assert id in a['post_ids'] and id not in ids
 ids.add(id)
 x=index[id]
 new.append(dict(post_id=id,label=label,reason=reason,card_file=x['card_file']))
with p.open('w') as f:
 w=csv.DictWriter(f,fieldnames=['post_id','label','reason','card_file'],delimiter='\t');w.writeheader();w.writerows(old+new)
print('triaged',len(old+new),'keeps',sum(x['label']=='keep' for x in old+new))
