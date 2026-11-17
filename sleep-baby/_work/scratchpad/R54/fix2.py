import json
B='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/'
units=[l.rstrip('\n').split('\t')[1] for l in open(B+'scratchpad/R54/units.tsv')]
idx={u:i+1 for i,u in enumerate(units)}
f=B+'voice/reddit-r54.jsonl'
recs=[json.loads(l) for l in open(f)]
for r in recs:
    u=idx[r['raw_file']]
    if u in (23,142):
        r['speaker']='parent_unspecified'
        r['context']=r['context'].replace('Mother of','Parent of').replace('Same mother','Same parent').replace('Breastfeeding parent','Parent')
    if u in (47,121):
        r['context']=r['context'].replace('Breastfeeding parent','Breastfeeding mother').replace('Same parent','Same mother')
open(f,'w').write(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in recs))
import collections; print(collections.Counter(r['speaker'] for r in recs))
