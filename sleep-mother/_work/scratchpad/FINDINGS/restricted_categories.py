#!/usr/bin/env python3
"""Classify restricted ids by the category each reader gave it (reader-notes-mr0N.md 'Restricted ids' sections).
An id can sit in more than one category. Ids restricted only by the orchestrator are listed as 'orchestrator only'."""
import json, re, os
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
R={json.loads(l)['id'] for l in open(os.path.join(ROOT,'voice-merged','all.jsonl')) if json.loads(l).get('restricted')}
cats={'mental health':set(),'medication / supplement / medical':set(),'safe-sleep adjacent':set()}
for n in ('mr01','mr02','mr03'):
    t=open(os.path.join(ROOT,'synthesis',f'reader-notes-{n}.md')).read()
    sec=t.split('## Restricted ids',1)[1]
    cur=None
    for line in sec.splitlines():
        l=line.lower()
        if 'mental health' in l: cur='mental health'
        elif 'medication' in l or 'medical claim' in l: cur='medication / supplement / medical'
        elif 'safe-sleep' in l or 'safe sleep' in l: cur='safe-sleep adjacent'
        if l.startswith('unit ') or l.startswith('not quoted'): cur=None
        if cur:
            for a,b in re.findall(r'(sm\d{2}-\d{4})(?:[–-](\d{4}))?',line):
                if b:
                    p=a[:5]; 
                    for k in range(int(a[5:]),int(b)+1): cats[cur].add(f'{p}{k:04d}')
                else: cats[cur].add(a)
allc=set().union(*cats.values())
for k,v in cats.items(): print(f'{k}: {len(v & R)} (of which also in another category: {len((v&R) & set().union(*[w for kk,w in cats.items() if kk!=k]))})')
only=sorted(R-allc); print('orchestrator only (not in a reader category):',len(only),' '.join(only))
print('restricted total',len(R),'classified',len(allc&R))
print('in a reader category but not restricted:',sorted(allc-R))
