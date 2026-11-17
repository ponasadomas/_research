from pathlib import Path
import json,sys,re
sys.path.insert(0,str(Path(__file__).parent))
from selections import selections
ROOT=Path(__file__).resolve().parents[2]
index={}
for p in sorted((ROOT/'_raw/reviews').glob('*-reviews.units.json')):
 j=json.loads(p.read_text())
 for q in j['reviews']:
  index[f"{j['app']}-{j['country']}-{q['id']}"]=(j,q)
rows=[]
for i,(key,text,speaker,stage,typ,themes,context) in enumerate(selections,1):
 j,q=index[key]
 # Whitespace and apostrophe normalization is solely validation; excerpt remains authored exact selection.
 if len(text.split())>25: print('LONG',key,len(text.split()))
 rows.append(dict(id=f'rev01-{i:04}',source='appstore-'+j['app']+'-'+j['country'],url=j['url'],date=q['date'][:10],speaker=speaker,stage=stage,type=typ,themes=themes,quote=text,context=context,raw_file=j['corpus_file'],source_class='app_review',evidence_kind='original_review',review_id=q['id'],rating=q['rating'],storefront=j['country']))
(ROOT/'voice/reviews-media-01.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
print(len(rows),'quotes')
