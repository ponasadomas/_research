import sys
name=sys.argv[1]; ov={}
for l in open(f'O-{name}.txt'):
    l=l.rstrip('\n')
    if not l.strip(): continue
    p=l.split('|',2); ov[p[0]]=(p[1],p[2] if len(p)>2 else None)
out=[];seen=set()
for l in open(f'A-{name}.txt',errors='replace'):
    i,t,_=l.split('|',2); i=i.rstrip('S')
    code,r=ov.get(i,('c',None)); seen.add(i)
    if r is None: r=' '.join(t.split()[:12])
    out.append(f'{i}|{code}|{r}')
assert set(ov)<=seen, set(ov)-seen
open(f'L-{name}.txt','w').write('\n'.join(out)+'\n')
