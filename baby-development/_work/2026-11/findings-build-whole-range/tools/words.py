#!/usr/bin/env python3
"""words.py -> builds her-words.md from (a) every quote in spec/*.md of the findings page and (b) words-extra.txt ("id | phrase").
Each phrase is checked word for word against its record, filed under its post's main pattern and age (by the post's stage),
and given the count of the section form that cites that quote id. Capped at CAP phrases (longest dropped first)."""
import re,os,sys,glob,collections
sys.path.insert(0,os.path.dirname(__file__))
from common import *
from sections import load
S=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=R+'/her-words.md'; CAP=340
rec=records(); P=posts(); sec=load()
NAMES={'03':'Hard behaviour','01':'Is this normal, or is something wrong with my child?','04':'What should I get for this age?','02':'What do I do with the child all day?','09':'Classes, groups, other children, daycare as a place to grow','11':'Potty readiness and learning','05':"Am I harming the child's development by what I do?",'08':'Delight or pride in what the child now does','07':'Learning to eat and drink as a skill','06':'The child prefers someone else','12':'The child has a known delay or is in therapy','10':'Other people interfere','00':'None of these'}
ORDER=['03','01','04','02','09','11','05','08','07','06','12','10','00']
# id -> (n, m, part) from the sections; prefer On-niche
cite={}
PR={'On-niche posts':0,'Across the on-niche posts':1,'Near posts':2}
for (g,k),v in sec.items():
    for h in v['heads']:
        if h['level']!=3 or h['n'] is None: continue
        for i in h['ids']:
            c=(PR[h['part']],-h['n'],h['n'],h['m'],h['part'],g)
            if i not in cite or c<cite[i]: cite[i]=c
def tag(h):
    t=h.lower()
    if re.search(r'\bpay|paying|purchas|\bbuy|bought|spending|acquiring',t): return ' that name a purchase'
    if re.search(r'tried|\btry|\btries|tested|adjusting|practised|changed feeding|already acted',t): return ' that say what they tried'
    if re.search(r'\bother|receiv|\bhear|encounter|gets help',t): return ' that say what other people told them or did'
    return ' that name a feeling'
ACRLAB={}
for (g,k),v in sec.items():
    for h in v['heads']:
        if h['level']==3 and h['part']=='Across the on-niche posts':
            for i in h['ids']: ACRLAB.setdefault(i,tag(h['head']))
items=[]; seen=set(); problems=[]
def add(i,q,src):
    q=q.strip()
    if i not in rec: problems.append(f"id {i} missing"); return
    for part in [x for x in re.split(r'\s*\[…\]\s*',q) if x.strip()]:
        if not locate(rec[i]['quote'],part): problems.append(f"not word for word [{i}] {part[:60]}"); return
    key=(i,norm(q))
    if key in seen: return
    seen.add(key); items.append((i,q,src))
for f in sorted(glob.glob(S+'/spec/*.md')):
    for l in open(f,encoding='utf-8'):
        if l.startswith('- "'):
            m=re.match(r'^- "(.+)" \[([a-z]{2,}\d+-\d+)\]\s*$',l.rstrip())
            if m: add(m.group(2),m.group(1),'page')
        else:
            for q,i in re.findall(r'"([^"\n]+)" \[([a-z]{2,}\d+-\d+)\]',l): add(i,q,'page')
for l in open(S+'/words-extra.txt',encoding='utf-8'):
    if ' | ' in l:
        i,q=l.rstrip('\n').split(' | ',1); add(i.strip(),q,'extra')
# cap: drop the longest first
items.sort(key=lambda x:-len(x[1].split()))
dropped=[]
while len(items)>CAP: dropped.append(items.pop(0))
groups=collections.defaultdict(lambda:{'u2':[],'a23':[]}); nearg=[]
for i,q,src in items:
    p=P[rec[i]['post_id']]; b=band(p['stage'])
    c=cite.get(i)
    if c is None: note='not sorted into a form'
    else:
        _,_,n,m,part,g=c
        note='once' if n==1 else f"{n:,} of {m:,} posts"
        if part=='Across the on-niche posts': note+=ACRLAB[i]
    if p['mark']!='yes': nearg.append((i,q)); continue   # near posts are next to the niche: left out of her words
    age='a23' if b in('2y','3y') else 'u2'
    acr=1 if (c is not None and c[4]=='Across the on-niche posts') else 0   # lines cited only under an across tag go after the form-cited lines
    groups[f"{int(p['main_pattern']):02d}"][age].append(((acr,0 if c is None else -c[2]),i,q,note))
out=['# Baby development: her words','','**Written:** 2026-11-20. **Reviewed by the owner:** not yet','',
'Phrases and sentences, word for word, from the random sample of Reddit posts behind `findings/what-hurts-and-what-she-wants.md` (a child from birth to 48 months). Most writers do not say they are a mother (3,117 of 3,811 on-niche posts do not), so "her" means whoever wrote the post. The glossary of her vocabulary is not made yet, so this page has no "Her vocabulary" group.','',
'Grouped by pattern, and inside each pattern by the child\'s age: under 2, then 2 and 3. After each line: how many posts of that pattern and age say this kind of thing, taken from the form under which the pattern\'s section cites the post ("once" is a form of one post). Where the section cites the post only under what parents tried, were told, bought or feel, the count is of that and says so. Under 2 the counts are out of the first reading\'s posts of the pattern, at 2 and 3 out of the second reading\'s. Inside each age the lines run from the common to the rare; lines counted only under tried, told, bought or feel come last. Phrases from near posts are left out.','']
total=0
for k in ORDER:
    out+=[f"## {NAMES[k]}",'']
    for age,lab in (('u2','Under 2'),('a23','At 2 and 3')):
        L=sorted(groups[k][age],key=lambda x:(x[0],x[1]))
        if not L: continue
        out+=[f"### {lab}",'']
        for _,i,q,note in L: out.append(f'- "{q}" [{i}] ({note})'); total+=1
        out.append('')
open(OUT,'w',encoding='utf-8').write('\n'.join(out))
print('written',OUT,'phrases',total,'dropped for the cap',len(dropped),'words',len(' '.join(out).split()))
for k in ORDER: print(' ',k,len(groups[k]['u2']),len(groups[k]['a23']))
print('  near posts left out',len(nearg))
print('PROBLEMS' if problems else 'words checks OK'); [print('  ',p) for p in problems[:40]]
if not 250<=total<=350: print('COUNT OUT OF RANGE')
