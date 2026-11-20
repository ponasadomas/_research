#!/usr/bin/env python3
"""covx.py -> rows of the sections' own Coverage tables whose 'Went to' is not one of that section's ### headings or 'section title' (exceptions worth reading)."""
import re,sys,os
sys.path.insert(0,os.path.dirname(__file__))
from sections import load,DIRS
s=load()
for (g,k),v in s.items():
    heads={h['head'] for h in v['heads'] if h['level']==3}
    t=open(v['file'],encoding='utf-8').read().split('\n## Coverage',1)[1]
    n=0
    for l in t.split('\n'):
        m=re.match(r'^\| (.+) \| (.+) \|\s*$',l)
        if not m or m.group(1) in('Digest heading','---'): continue
        n+=1
        w=m.group(2).strip()
        if w not in heads and w!='section title' and not set(w)<=set('-|'): print(g,k,'|',m.group(1),'=>',w)
    print(g,k,'rows',n)
