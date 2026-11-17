import sys
S='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-mother/scratchpad/MT1/'
C='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-mother/_raw/reddit/filter-v1/wave1/cards/'
k={}
for l in open(S+'k8.txt'):
    p=l.rstrip('\n').split('|'); k[p[0]]=(p[1],p[2])
out=[]
for f in ['A-sleeptrain-001.txt','A-sleeptrain-003.txt']:
    for l in open(C+f):
        if l.startswith('ID '):
            i=l.split()[1]
            lab,r=k.get(i,('drop','baby sleep question, parent own sleep not described'))
            out.append(f'{i}|{lab}|{r}')
open(S+'l8.txt','w').write('\n'.join(out)+'\n')
