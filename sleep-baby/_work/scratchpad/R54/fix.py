import json
B='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/'
units=[l.rstrip('\n').split('\t')[1] for l in open(B+'scratchpad/R54/units.tsv')]
idx={u:i+1 for i,u in enumerate(units)}
f=B+'voice/reddit-r54.jsonl'
recs=[json.loads(l) for l in open(f)]
for r in recs:
    u=idx[r['raw_file']]
    if u==30: r['speaker']='new_mother'; r['stage']='unknown'
    if u==74: r['speaker']='parent_unspecified'; r['context']=r['context'].replace('Mother of','Parent of').replace('Same mother','Same parent')
    if u==87 and r['type']=='pre_empting_replies': r['type']='objection'
    if u==115: r['themes']=[t for t in r['themes'] if t!='fear']
    if u==137 and r.get('comment_id')=='om3bzhf': r['themes']=[t for t in r['themes'] if t!='relative_caregiver_conflict']
    if u==151: r['themes']=[t for t in r['themes'] if t!='cosleeping']
open(f,'w').write(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in recs))
print(len(recs), len({r['id'] for r in recs}))
