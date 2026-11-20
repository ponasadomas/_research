#!/usr/bin/env python3
"""check_sums.py [page] -> in each pattern group of the findings page: the under-2 form findings must sum to that pattern's under-2 yes posts,
the 2-and-3 form findings to its 2-and-3 yes posts (both totals taken from the sections' "On-niche posts" count lines, not from the page),
the group's first count must be their sum out of 3,811, and the four across findings must be out of that sum and equal the two sections' tag counts added."""
import re,sys,os
sys.path.insert(0,os.path.dirname(__file__))
from sections import load
from common import R
page=sys.argv[1] if len(sys.argv)>1 else R+'/findings/what-hurts-and-what-she-wants.md'
sec=load()
YES={k:[h for h in v['heads'] if h['level']==3 and h['part']=='On-niche posts'][0]['m'] for k,v in sec.items()}
ACR={k:sorted(h['n'] for h in v['heads'] if h['level']==3 and h['part']=='Across the on-niche posts') for k,v in sec.items()}
NAME={re.sub(r'^baby-development: pattern \d+, ','',v['title']):k for (g,k),v in sec.items() if g=='u2'}
t=open(page,encoding='utf-8').read().split('\n## Coverage')[0]
val=lambda m:(int(m.group(1).replace(',','')),int(m.group(2).replace(',','')))
ok=True; n=0; grand=0
for g in re.split(r'^## ',t,flags=re.M)[1:]:
    name=g.split('\n')[0].strip()
    if name not in NAME: continue
    k=NAME[name]; n+=1
    parts=re.split(r'^\*\*(Under 2|At 2 and 3)\*\* \(([\d,]+) posts\)\s*$',g,flags=re.M)
    if len(parts)!=7: print('FAIL',name,'runs not found'); ok=False; continue
    first=val(re.search(r'^(\d[\d,]*) of ([\d,]+) posts\.',parts[0],re.M))
    def blocks(x): return [val(re.search(r'^(\d[\d,]*) of ([\d,]+) posts\.',b,re.M)) for b in re.split(r'^### ',x,flags=re.M)[1:]]
    u2=blocks(parts[3]); rest=blocks(parts[6]); a23=rest[:-4]; across=rest[-4:]
    mu,ma=YES[('u2',k)],YES[('a23',k)]
    wantacr=sorted(a+b for a,b in zip(ACR[('u2',k)],ACR[('a23',k)]))  # only a sanity bound; exact pairing is by tag in build.py
    good=(sum(a for a,_ in u2)==mu and all(m==mu for _,m in u2) and sum(a for a,_ in a23)==ma and all(m==ma for _,m in a23)
          and first==(mu+ma,3811) and all(m==mu+ma for _,m in across) and int(parts[2].replace(',',''))==mu and int(parts[5].replace(',',''))==ma
          and 3<=len(u2)<=6 and 3<=len(a23)<=6 and sum(a for a,_ in across)==sum(ACR[('u2',k)])+sum(ACR[('a23',k)]))
    ok&=good; grand+=first[0]
    print(f"{'OK  ' if good else 'FAIL'} {name[:44]:44} total {first[0]:>4} | under 2: {len(u2)} findings {[a for a,_ in u2]} = {sum(a for a,_ in u2)} of {mu} | 2 and 3: {len(a23)} findings {[a for a,_ in a23]} = {sum(a for a,_ in a23)} of {ma} | across {[a for a,_ in across]}")
print(f"{n} pattern groups; pattern totals sum to {grand};", 'ALL SUMS OK' if ok and n==13 and grand==3811 else 'PROBLEM')
