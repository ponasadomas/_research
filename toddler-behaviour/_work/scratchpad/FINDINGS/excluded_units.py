#!/usr/bin/env python3
"""Tally units excluded (read in full, nothing quoted) in the reader ledgers, by first-matching reason keyword."""
import re,glob,os,collections
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
rows={}
for f in sorted(glob.glob(os.path.join(ROOT,'sources','reddit-reading-tr0*.md'))):
    insec=False
    for line in open(f):
        if line.startswith('## '):
            insec=bool(re.match(r'## (Units excluded|Excluded units)',line))
            continue
        if not line.startswith('|'): continue
        status=re.search(r'\|\s*excluded(-restricted)?\s*\|',line,re.I)
        if not (insec or status): continue
        m=re.search(r'([A-Za-z]+-1[0-9a-z]{5,7})(\.txt)?',line)
        if not m: continue
        rows[(os.path.basename(f),m.group(1))]=line.strip().strip('|').split('|')[-1].strip().lower()
def cls(r):
    if re.search(r'yell|shout|harsh|hit(ting)? the child|tapping|restrain|holding the child|hold(ing)? (him|her|the child) down|force|forcing|physically|grabb|lock|shutting|spank|smack|threat|punish|handling|physical act|same author as pottytraining-1wg3jw2',r): return 'parent or relative harshness / force toward a child'
    if re.search(r'medic|dosing|laxative|scan|treatment|bowel|gi\b',r): return 'medical treatment detail'
    if re.search(r'autis|adhd|diagnos|assess|delay|neuro|evaluat|therap',r): return 'diagnosis-centred'
    if re.search(r'body|privacy|undress|urinat|smear',r): return 'child body / privacy'
    return 'other (adult conflict, self-injury, violence between children, parent mental health, duplicates)'
c=collections.Counter(cls(r) for r in rows.values())
print('excluded units found in ledgers:',len(rows))
per=collections.Counter(k[0] for k in rows); print(dict(per))
for k,v in c.most_common(): print(v,'|',k)
if os.environ.get('V'):
    for k,r in sorted(rows.items()): print(k,cls(r),'::',r[:120])
