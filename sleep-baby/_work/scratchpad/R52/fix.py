import json,sys
f='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/voice/reddit-r52.jsonl'
ch=json.loads(sys.argv[1])  # {id:{field:val}}
L=[json.loads(l) for l in open(f)]
for r in L:
    if r['id'] in ch: r.update(ch[r['id']])
open(f,'w').write(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in L))
