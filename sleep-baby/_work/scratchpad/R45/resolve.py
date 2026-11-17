# Replace {{substring}} in a template with the sb45 id whose quote contains it (must be unique).
import json,re,sys
R=[json.loads(l) for l in open(sys.argv[3])]
t=open(sys.argv[1],encoding='utf-8').read()
def f(m):
    s=m.group(1)
    h=[r['id'] for r in R if s in r['quote']]
    if len(h)!=1: sys.exit(f"{len(h)} hits for {s!r}: {h}")
    return h[0]
open(sys.argv[2],'w',encoding='utf-8').write(re.sub(r'\{\{(.+?)\}\}',f,t))
