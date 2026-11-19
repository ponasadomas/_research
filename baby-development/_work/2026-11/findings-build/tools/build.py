#!/usr/bin/env python3
"""build.py -> assembles spec/*.md into the findings page, fills count lines, checks sums, builds Coverage."""
import re,os,sys,glob
sys.path.insert(0,os.path.dirname(__file__))
from sections import load
S=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.expanduser('~/GitHub/_research/baby-development/findings/what-hurts-and-what-she-wants.md')
if len(sys.argv)>1: OUT=sys.argv[1]
sec=load()
YES={k:[h for h in v['heads'] if h['level']==3 and h['part']=='On-niche posts'][0]['m'] for k,v in sec.items()}
NEAR={k:[h for h in v['heads'] if h['level']==3 and h['part']=='Near posts'][0]['m'] for k,v in sec.items()}
def find(k,part,head):
    hs=[h for h in sec[k]['heads'] if h['level']==3 and h['part']==part and h['head']==head]
    if len(hs)!=1: raise SystemExit(f"pattern {k} {part}: heading not found or not unique: {head!r}")
    return hs[0]
went={}  # (k,part,head) -> claim
acr={}; atag={}
errors=[]
out=[]; groupwords=[]
pat=None; claim=None
formsum={}
def setwent(k,part,head,c):
    key=(k,part,head)
    if key in went: errors.append(f"used twice: {key}")
    went[key]=c
files=sorted(glob.glob(S+'/spec/*.md'))
for f in files:
    L=open(f,encoding='utf-8').read().split('\n'); i=0; start=len(out)
    while i<len(L):
        l=L[i]
        if l.startswith('@pattern '): pat=l.split()[1]; i+=1; continue
        if l.startswith('### '): claim=l[4:].strip(); out.append(l); out.append(''); i+=1; continue
        if l.strip()=='@count pattern':
            out.append(f"{YES[pat]:,} of 2,471 posts."); i+=1; continue
        if l.startswith('@raw '): out.append(l[5:]); i+=1; continue
        if l.strip() in('@forms','@small'):
            kind=l.strip(); i+=1; tot=0; items=[]
            while L[i].strip()!='@end':
                if L[i].strip():
                    h,_,short=L[i].partition(' => ')
                    x=find(pat,'On-niche posts',h.strip()); tot+=x['n']; items.append((short.strip(),x['n'])); setwent(pat,'On-niche posts',h.strip(),claim)
                i+=1
            i+=1
            formsum[pat]=formsum.get(pat,0)+tot
            out.append(f"{tot:,} of {YES[pat]:,} posts.")
            if kind=='@small':
                out.append(''); out.append('Counted here: '+'; '.join(f"{s} ({n})" for s,n in items)+'.')
            continue
        if l.startswith('@across '):
            h=l[8:].strip(); x=find(pat,'Across the on-niche posts',h); setwent(pat,'Across the on-niche posts',h,claim)
            acr[pat]=acr.get(pat,0)+1; atag[claim]=['tried','others said','paid','how they feel'][acr[pat]-1]
            out.append(f"{x['n']:,} of {YES[pat]:,} posts."); i+=1; continue
        if l.startswith('@near '):
            k=l.split()[1]; i+=1; items=[]; assert L[i].strip()=='@list',L[i]; i+=1
            while L[i].strip()!='@end':
                if L[i].strip():
                    h,_,short=L[i].partition(' => ')
                    x=find(k,'Near posts',h.strip()); items.append((short.strip(),x['n']))
                i+=1
            i+=1
            for h in sec[k]['heads']:
                if h['level']==3 and h['part']=='Near posts': went[(k,'Near posts',h['head'])]=claim
            out.append(f"{NEAR[k]:,} of 5,534 posts."); out.append('')
            out.append('The largest forms: '+'; '.join(f"{s} ({n})" for s,n in items)+'.')
            continue
        if l.startswith('@'): errors.append(f"{os.path.basename(f)}: unknown directive {l}")
        out.append(l); i+=1
    groupwords.append((os.path.basename(f),len(' '.join(out[start:]).split())))
# checks
for k in sec:
    on=[h for h in sec[k]['heads'] if h['level']==3 and h['part']=='On-niche posts']
    miss=[h['head'] for h in on if (k,'On-niche posts',h['head']) not in went]
    if miss: errors.append(f"pattern {k}: {len(miss)} on-niche forms unused, e.g. {miss[:3]}")
    if formsum.get(k,0)!=YES[k]: errors.append(f"pattern {k}: forms sum {formsum.get(k,0)} != {YES[k]}")
    for h in sec[k]['heads']:
        if h['level']==3 and h['part']!='On-niche posts' and (k,h['part'],h['head']) not in went: errors.append(f"pattern {k}: {h['part']} heading unmapped: {h['head']}")
body='\n'.join(out).rstrip()+'\n'
above=len(body.split())
# coverage
cov=['','## Coverage','','<details>','<summary>Every heading of the evidence file, and where it went</summary>','','The evidence file is `counts.md` plus the thirteen sections. Headings are given section by section, because some repeat.','','| Evidence heading | Went to |','|---|---|']
SECT={'Limits':'Limits','On-niche posts':'section title','Near posts':'section title','Across the on-niche posts':'section title','Coverage':"not about her: the section's own coverage table"}
order=['01','03','04','02','05','07','06','08','12','09','10','11','00']
for k in order:
    cov.append(f"| **{sec[k]['title'].replace('baby-development: ','')} (pattern-{k}.md)** | section title |")
    for h in sec[k]['heads']:
        if h['level']==2: cov.append(f"| {h['head']} | {SECT[h['head']]} |")
        else: cov.append(f"| {h['head']} | {went.get((k,h['part'],h['head']),'UNMAPPED')} |")
extra=open(S+'/cov-counts.md',encoding='utf-8').read().strip().split('\n') if os.path.exists(S+'/cov-counts.md') else []
cov+=extra
cov+=['','</details>','']
open(OUT,'w',encoding='utf-8').write(body+'\n'.join(cov))
import json; json.dump([[k,part,h,c] for (k,part,h),c in went.items()],open(S+'/went.json','w'),ensure_ascii=False); json.dump(atag,open(S+'/atag.json','w'),ensure_ascii=False)
print('written',OUT); print('words above Coverage:',above)
for g,w in groupwords: print(f"  {g}: {w}")
print('ERRORS' if errors else 'build checks OK'); [print('  ',e) for e in errors[:40]]
