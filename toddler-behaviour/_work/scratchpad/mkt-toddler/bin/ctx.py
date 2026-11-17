import sys,re
pat=re.compile(sys.argv[1],re.I); w=int(sys.argv[2])
for f in sys.argv[3:]:
    t=open(f,encoding='utf-8',errors='replace').read()
    seen=set()
    for m in pat.finditer(t):
        s=t[max(0,m.start()-w):m.end()+w].replace('\n',' | ')
        if s in seen: continue
        seen.add(s); print(f.split('/')[-1],'::',s)
