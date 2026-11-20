#!/usr/bin/env python3
"""menu.py u2|a23 NN [part-prefix] -> for each ### of that section, each cited quote widened to whole sentences, with the post's stage."""
import sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from common import *
from sections import DIRS
rec=records(); P=posts()
g,k=sys.argv[1],sys.argv[2]; only=sys.argv[3] if len(sys.argv)>3 else None
part=None
for l in open(f"{DIRS[g]}/pattern-{k}.md",encoding='utf-8'):
    l=l.rstrip('\n')
    if l.startswith('## '):
        part=l[3:]
        if part=='Coverage': break
        if not only or part.startswith(only): print('\n=== '+part)
        continue
    if only and not (part or '').startswith(only): continue
    if l.startswith('### '): print('\n'+l); continue
    m=re.match(r'^(\d+) of (\d+) posts',l)
    if m: print(l); continue
    if l.strip() and not re.search(r'\[[a-z]{2,}\d+-\d+\]',l) and not l.startswith('**Written') and not l.startswith('**Reviewed') and not l.startswith('# '): print('  ~ '+l)
    if l.startswith('**But') and re.search(r'\[[a-z]{2,}\d+-\d+\]',l):
        lab=re.sub(r'"[^"\n]+" \[[a-z0-9-]+\]','',l).replace('**But:**','').strip()
        if lab: print('  ~ But: '+lab)
    if part=='Near posts' and os.environ.get('NEARQ')!='1': continue
    for q,i in re.findall(r'"([^"\n]+)" \[([a-z]{2,}\d+-\d+)\]',l):
        r=rec[i]; p=P.get(r['post_id'],{})
        tag='B ' if l.startswith('**But') else ''
        st=p.get('stage','').replace('toddler_','t').replace('baby_','b').replace('_months','m').replace('newborn_0_8_weeks','nb').replace('child_','')
        outs=[]
        for part_ in [x for x in re.split(r'\s*\[…\]\s*',q) if x.strip()]:
            loc=locate(r['quote'],part_)
            outs.append(widen(r['quote'],*loc) if loc else '??'+part_)
        ex=' […] '.join(dict.fromkeys(outs))
        if len(ex.split())>40: ex=' '.join(ex.split()[:40])+' ~~'
        print(f"{tag}[{i}] {st}/{p.get('mark','')}{p.get('border','')}/m{p.get('main_pattern','')}: {ex}")
