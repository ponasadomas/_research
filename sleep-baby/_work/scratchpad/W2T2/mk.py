import sys,re
# usage: mk.py outname idsfile ; exceptions from stdin lines "id TEXT"
out=sys.argv[1]
ids=open(sys.argv[2]).read().split()
ex={}
for l in sys.stdin:
    l=l.strip()
    if l:
        k,v=l.split(' ',1); ex[k]=v
bad=[k for k in ex if k not in ids]
assert not bad,bad
open(out,'w').write('\n'.join(i+' '+ex.get(i,'C') for i in ids)+'\n')
print(out,len(ids),len(ex))
