import json,sys
# usage: fix.py unit speaker  -> sets speaker for all drafts of unit
u,sp=sys.argv[1],sys.argv[2]
L=[json.loads(l) for l in open('draft.jsonl') if l.strip()]
for d in L:
    if d['u']==u: d['sp']=sp
open('draft.jsonl','w').write(''.join(json.dumps(d,ensure_ascii=False)+'\n' for d in L))
