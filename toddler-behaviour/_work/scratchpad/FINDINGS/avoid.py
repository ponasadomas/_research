#!/usr/bin/env python3
"""Extended avoid set: merged restricted flag + restricted-ids.md + every id/range in readers' '## Restricted ids' sections."""
import json,re,glob,os
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
recs={}
for l in open(os.path.join(ROOT,'voice-merged','all.jsonl')):
    l=l.strip()
    if l: r=json.loads(l); recs[r['id']]=r
flag={i for i,r in recs.items() if r['restricted']}
ext=set()
for f in sorted(glob.glob(os.path.join(ROOT,'synthesis','reader-notes-tr*.md'))):
    t=open(f).read()
    m=re.search(r'## Restricted ids(.*?)(\n## |\Z)',t,re.S)
    if not m: continue
    sec=m.group(1)
    for line in sec.splitlines():
        pref=None
        for tok in re.finditer(r'(tb\d{2}-)?(\d{4})(\s*[–-]\s*(tb\d{2}-)?(\d{4}))?',line):
            if tok.group(1): pref=tok.group(1)
            if not pref: continue
            a=int(tok.group(2)); b=int(tok.group(5)) if tok.group(5) else a
            if b<a or b-a>20: b=a
            for n in range(a,b+1): ext.add(f'{pref}{n:04d}')
ext&=set(recs)
print('flag',len(flag),'ext',len(ext),'ext-not-flag',len(ext-flag))
open(os.path.join(H,'avoid.txt'),'w').write('\n'.join(sorted(ext|flag)))
print(' '.join(sorted(ext-flag)))
