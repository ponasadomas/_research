import sys
# usage: save.py cardname outfile ; stdin: lines "id label reason" where label in keep_*/drop ; lines "id d reason" shorthand for drop
card,out=sys.argv[1:3]
ids=[l.split()[1] for l in open(f'../../_raw/reddit/filter-v1/wave1/cards/{card}.txt') if l.startswith('ID ')]
L={}
for l in sys.stdin.read().strip().split('\n'):
    i,lab,r=l.split(' ',2)
    if lab=='d': lab='drop'
    assert i not in L,i
    L[i]=(lab,r)
miss=[i for i in ids if i not in L]; extra=[i for i in L if i not in ids]
print('missing',miss,'extra',extra)
open(out,'w').write(''.join(f"{i}\t{L[i][0]}\t{L[i][1]}\n" for i in ids if i in L))
