import sys
name=sys.argv[1]
keep={}
raw=sys.stdin.read(); open(f"in-{name}.txt","w").write(raw)
for l in raw.splitlines():
    l=l.strip()
    if not l: continue
    i,c,r=l.split(' ',2); keep[i]=(c,r)
out=[]
default=sys.argv[2]
for l in open(f'flat-{name}.txt'):
    i=l.split('|')[0].split()[0]
    c,r=keep.pop(i,('D',default))
    out.append(f"{i} {c} {r}")
assert not keep,keep
open(f'lab-{name}.txt','w').write("\n".join(out)+"\n")
print(len(out))
