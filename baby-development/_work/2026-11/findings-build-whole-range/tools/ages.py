#!/usr/bin/env python3
"""ages.py -> six age bands by main pattern, from posts.tsv (mark, stage, main_pattern). Prints the table used in spec/01-ages.md and writes ages.json."""
import sys,os,json,collections
sys.path.insert(0,os.path.dirname(__file__))
from common import *
P=posts(); yes=[p for p in P.values() if p['mark']=='yes']
assert len(yes)==3811
NAMES={0:'None of these',1:'Is this normal',2:'What to do all day',3:'Hard behaviour',4:'What to get',5:'Am I harming',6:'Prefers someone else',7:'Eating and drinking',8:'Delight or pride',9:'Daycare, classes, other children',10:'Other people interfere',11:'Potty',12:'Known delay or therapy'}
tab=collections.defaultdict(collections.Counter); tot=collections.Counter()
for p in yes:
    b=band(p['stage']); tab[b][int(p['main_pattern'])]+=1; tot[b]+=1
print('bands',dict(tot),'sum banded',sum(tot[b] for b in BANDS),'unbanded',tot['none'])
order=[3,1,4,2,9,11,5,8,7,6,12,10,0]
LAB={'0-6m':'0 to 6 months','6-12m':'6 to 12 months','12-18m':'12 to 18 months','18-24m':'18 to 24 months','2y':'2 years','3y':'3 years'}
lines=['| Pattern | '+' | '.join(LAB[b] for b in BANDS)+' |','|---|'+'---|'*6]
lines.append('| Posts | '+' | '.join(f"{tot[b]:,}" for b in BANDS)+' |')
for k in order:
    lines.append(f"| {NAMES[k]} | "+' | '.join(f"{tab[b][k]} ({round(100*tab[b][k]/tot[b])}%)" for b in BANDS)+' |')
print('\n'.join(lines))
json.dump({'tot':tot,'tab':{b:dict(tab[b]) for b in tab}},open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'ages.json'),'w'))
open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'ages-table.md'),'w').write('\n'.join(lines)+'\n')
# who
sp=collections.Counter(p['speaker'] for p in yes); print(sp.most_common())
for grp,name in ((lambda p:p['reader'].startswith('sr'),'first reading'),(lambda p:p['reader'].startswith('ar'),'re-read')):
    ys=[p for p in yes if grp(p)]; c=collections.Counter(p['speaker'] for p in ys); print(name,len(ys),c.most_common(4))
# subreddit by band
sub=collections.defaultdict(collections.Counter)
for p in yes: sub[p['subreddit']][band(p['stage'])]+=1
for s,c in sorted(sub.items(),key=lambda x:-sum(x[1].values())): print(s,sum(c.values()),{b:c[b] for b in BANDS})
# paid
paid=[p for p in yes if p['paid'].strip().lower() in('yes','true','1')]
print('paid yes posts',len(paid),collections.Counter(band(p['stage']) for p in paid),collections.Counter(p['reader'][:2] for p in paid))
print(collections.Counter(p['paid'] for p in yes))
# near
near=[p for p in P.values() if p['mark']=='near']
print('near',len(near),collections.Counter(p['border'] for p in near))
print('near tied',collections.Counter((p['reader'][:2],p['ties_to_development']) for p in near))
o48=[p for p in near if p['border']=='age_over_48']; print('over48 tied yes',sum(1 for p in o48 if p['ties_to_development']=='yes'),collections.Counter(p['main_pattern'] for p in o48 if p['ties_to_development']=='yes').most_common())
print('over48 main pattern all',collections.Counter(p['main_pattern'] for p in o48).most_common())
print('near tied by main pattern, by reading',collections.Counter((p['reader'][:2],p['main_pattern']) for p in near if p['ties_to_development']=='yes').most_common(40))

# keyword scan behind "in the first six months hard-behaviour posts are about crying and a baby who must be held"
import re
KW=r'cry|cries|scream|fuss|colic|whin|inconsolable|unsettled|witching|soothe|put.*down|held|holding|contact|clingy'
for bs in (('0-6m',),('6-12m',),('2y','3y')):
    a=[p for p in yes if p['main_pattern']=='3' and band(p['stage']) in bs]; c=[p for p in a if re.search(KW,(p['about']+' '+p['wants']).lower())]
    print('hard behaviour',bs,len(a),'summaries with a crying or holding word',len(c))
a=[p for p in yes if p['main_pattern']=='3' and band(p['stage'])=='0-6m']; assert (len(a),sum(1 for p in a if re.search(KW,(p['about']+' '+p['wants']).lower())))==(47,40)
