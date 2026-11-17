#!/usr/bin/env python3
"""Restricted set for wave-3 checks: merged flag + restricted-ids.md (q.py parser) + every id in the
'## Restricted ids' section of reader-notes-tr18..tr27 + ids written '(restricted)' / ', restricted]' in those notes.
Prints coverage of the merged flag against the readers' lists."""
import json,re,os,glob
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
recs={}
for l in open(os.path.join(ROOT,'voice-merged','all.jsonl'),encoding='utf-8'):
    if l.strip(): r=json.loads(l); recs[r['id']]=r
merged={i for i,r in recs.items() if r.get('restricted')}
md=set()
for line in open(os.path.join(ROOT,'synthesis','restricted-ids.md'),encoding='utf-8'):
    if not line.startswith('|'): continue
    cell=line.split('|')[1]; pref=None
    for tok in re.findall(r'tb[a-z0-9]{2}-\d{4}|\b\d{4}\b',cell):
        if tok.startswith('tb'): pref=tok[:5]; md.add(tok)
        elif pref: md.add(pref+tok)
reader=set(); inline=set()
for f in sorted(glob.glob(os.path.join(ROOT,'synthesis','reader-notes-tr*.md'))):
    mm0=re.search(r'tr(\d+)\.md$',f)
    if not mm0: continue
    n=int(mm0.group(1))
    if n<18: continue
    t=open(f,encoding='utf-8').read()
    m=re.search(r'## Restricted ids(.*?)(\n## |\Z)',t,re.S)
    if m:
        sec=m.group(1)
        # TR19 table and others; skip the 'Units carrying...not restricted' paragraph
        sec=sec.split('**Units carrying')[0]
        reader|=set(re.findall(r'tb\d\d-\d{4}',sec))
    for mm in re.finditer(r'(tb\d\d-\d{4})(?:,? ?tb\d\d-\d{4})*[,\s]*\(?restricted',t):
        pass
    for mm in re.finditer(r'(tb\d\d-\d{4})\s*\(restricted\)|(tb\d\d-\d{4}), restricted\]',t):
        inline.add(mm.group(1) or mm.group(2))
    for mm in re.finditer(r'\[((?:tb\d\d-\d{4}, )+tb\d\d-\d{4}), restricted\]',t):
        inline|=set(re.findall(r'tb\d\d-\d{4}',mm.group(1)))
ALL=merged|md|reader|inline
if __name__=='__main__':
    w3m={i for i in merged if re.match(r'tb(1[89]|2\d)-',i)}
    print('merged total',len(merged),'| md',len(md),'| md not merged',len(md-merged))
    print('wave3 merged',len(w3m),'| reader-section ids',len(reader),'| reader not merged',sorted(reader-merged))
    print('inline (restricted) ids not merged',sorted(inline-merged))
    print('merged wave3 not in reader lists',len(w3m-reader))
