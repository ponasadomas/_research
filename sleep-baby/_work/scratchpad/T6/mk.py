import sys,re
# usage: mk.py start end outfile ; overrides read from ov.txt (id<TAB>label<TAB>reason); default keep_core with auto reason from title
start,end,out=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
ov={}
for l in open('ov.txt'):
    p=l.rstrip('\n').split('\t')
    if len(p)==3: ov[p[0]]=(p[1],p[2])
lines=open('all.txt').read().splitlines()[start-1:end]
with open(out,'w') as f:
    for l in lines:
        p=l.split('|'); i=p[0]
        t=p[2] if p[1]=='SF' else p[1]
        lab,r=ov.get(i,('keep_core','baby/toddler sleep problem: '+t[:60]))
        f.write(f"{i}\t{lab}\t{r}\n")
