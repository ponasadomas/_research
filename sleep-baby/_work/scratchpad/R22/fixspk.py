import json,sys
p='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/voice/reddit-r22.jsonl'
fix=dict(a.split('=') for a in sys.argv[1:])
L=[json.loads(l) for l in open(p) if l.strip()]
c=0
for d in L:
    if d['post_id'] in fix: d['speaker']=fix[d['post_id']]; c+=1
open(p,'w').write(''.join(json.dumps(d,ensure_ascii=False)+'\n' for d in L)); print('fixed',c)
