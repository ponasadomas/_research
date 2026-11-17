#!/usr/bin/env python3
"""Check cited ids and same-line quoted fragments. Historical subject markings have no effect.
Run with python3 -I and optionally a findings/draft path.
"""
import json,re,sys,os
B=os.path.dirname(os.path.abspath(__file__))+'/../..'
R={}
for l in open(B+'/voice-merged/all.jsonl',encoding='utf-8'):
    if l.strip():
        r=json.loads(l); R[r['id']]=r
f=sys.argv[1] if len(sys.argv)>1 else B+'/synthesis/findings.md'
t=open(f,encoding='utf-8').read()
i=t.find('## 17. What wave 3 added')
if i>=0: t=t[i:]
def n(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace(' ',' ')
    return re.sub(r'\s+',' ',s).strip()
ID=re.compile(r'\b(pb[r0-9]\d?-\d{4})\b')
bad=0; ids=set()
for k,line in enumerate(t.split('\n'),1):
    lids=ID.findall(line); ids.update(lids)
    for x in lids:
        if x not in R: print('UNRESOLVED',k,x); bad+=1; continue
    frags=[x for x in line.split('"')[1::2] if len(x)>=12]
    for fr in frags:
        if '`' in fr: continue
        nf=n(fr).strip(' .')
        cands=[x for x in lids if x in R]
        if not cands: continue
        if not any(nf in n(R[x]['quote']) for x in cands):
            print('FRAG?',k,repr(fr[:90]),cands[:4]); bad+=1
print('ids', len(ids), 'problems', bad)
sys.exit(1 if bad else 0)
