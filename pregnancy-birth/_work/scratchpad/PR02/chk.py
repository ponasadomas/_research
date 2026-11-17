import json,re,html,sys
def norm(s): return re.sub(r"\s+"," ",html.unescape(s)).strip()
for l in open(sys.argv[1]):
    if not l.strip(): continue
    r=json.loads(l); t=norm(open(f"../_shared/_raw/reddit-2026/units/{r['u']}.txt").read()); pos=0
    for p in re.split(r"\s*\[…\]\s*",r['q']):
        p=norm(p); a=t.find(p,pos)
        if a<0: print("MISS",r['u'],p[:60])
        pos=a+len(p)
    if r.get('c') and ("COMMENT "+r['c']) not in t: print("NOC",r['u'],r['c'])
    if len(r['cx'].split())>25: print("CX",r['cx'])
print("ok")
