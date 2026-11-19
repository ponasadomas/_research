#!/usr/bin/env python3
"""Within each pattern group of the findings page: the form findings' counts (all but the first and the last four) must sum to the pattern's yes posts."""
import re,sys
t=open(sys.argv[1],encoding='utf-8').read().split('\n## Coverage')[0]
ok=True; n=0
for g in re.split(r'^## ',t,flags=re.M)[1:]:
    name=g.split('\n')[0].strip(); blocks=re.split(r'^### ',g,flags=re.M)[1:]
    cs=[re.search(r'^(\d[\d,]*) of ([\d,]+) posts\.',b,re.M) for b in blocks]
    if not blocks or not cs[0] or cs[0].group(2)!='2,471' or len(blocks)<6 or name in('Who writes, and about what age','Paying'): continue
    val=lambda m:(int(m.group(1).replace(',','')),int(m.group(2).replace(',','')))
    pat=val(cs[0])[0]; forms=[val(c) for c in cs[1:-4]]; across=[val(c) for c in cs[-4:]]
    s=sum(a for a,_ in forms); good=(s==pat and all(m==pat for _,m in forms) and all(m==pat for _,m in across))
    ok&=good; n+=1
    print(f"{'OK  ' if good else 'FAIL'} {name}: pattern {pat}, {len(forms)} form findings sum {s}, across {[a for a,_ in across]}")
print(f"{n} pattern groups;", 'ALL SUMS OK' if ok and n==13 else 'PROBLEM')
