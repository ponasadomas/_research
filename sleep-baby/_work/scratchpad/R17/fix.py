import json,sys
V='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/voice/reddit-r17.jsonl'
fix=json.loads(sys.argv[1])  # {"id":{"field":value}} or {"post:<unit>":{...}}
rs=[json.loads(l) for l in open(V) if l.strip()]
for r in rs:
    for k,v in fix.items():
        if r['id']==k or (k.startswith('unit:') and r['raw_file'].endswith(k[5:]+'.txt')): r.update(v)
open(V,'w').write(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rs))
