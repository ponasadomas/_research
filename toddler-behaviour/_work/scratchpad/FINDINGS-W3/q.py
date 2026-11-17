#!/usr/bin/env python3
"""Lookup helper for findings. Usage:
 q.py id sb01-0001 ...            print records
 q.py grep REGEX [--type T] [--speaker S] [--theme TH] [--n N]   search quotes
 q.py restricted                  list historical markings (no effect on quotation)
 Legacy --norestr is a no-op: markings never exclude research records.
"""
import json, re, sys, os
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
recs={}
for l in open(os.path.join(ROOT,'voice-merged','all.jsonl'),encoding='utf-8'):
    l=l.strip()
    if l: r=json.loads(l); recs[r['id']]=r
def restricted():
    s={i for i,r in recs.items() if r.get('restricted')}
    t=open(os.path.join(ROOT,'synthesis','restricted-ids.md'),encoding='utf-8').read()
    for line in t.splitlines():
        if line.startswith('Reviewed and left usable'): continue
        cell=line.split('|')[1] if line.startswith('|') else ''
        pref=None
        for tok in re.findall(r'tb\d{2}-\d{4}|\b\d{4}\b',cell):
            if tok.startswith('tb'): pref=tok[:5]; s.add(tok)
            elif pref: s.add(pref+tok)
    return s
R=restricted()
def show(r):
    flag=' FORMERLY MARKED (no effect)' if r['id'] in R else ''
    print(f"[{r['id']}]{flag} {r['speaker']} | {r['stage']} | {r['type']} | {','.join(r.get('themes',[]))} | {r['source']}\n   Q: {r['quote']}\n   C: {r.get('context','')}")
a=sys.argv[1:]
if a[0]=='id':
    for i in a[1:]:
        show(recs[i]) if i in recs else print('MISSING',i)
elif a[0]=='restricted':
    print(len(R)); print(' '.join(sorted(R)))
elif a[0]=='grep':
    rx=re.compile(a[1],re.I); opts=dict(zip(a[2::2],a[3::2])); n=int(opts.get('--n',40)); c=0
    for r in recs.values():
        if not rx.search(r['quote']): continue
        if '--type' in opts and r['type']!=opts['--type']: continue
        if '--speaker' in opts and r['speaker']!=opts['--speaker']: continue
        if '--theme' in opts and opts['--theme'] not in r.get('themes',[]): continue
        show(r); c+=1
        if c>=n: break
    print('shown',c)
if a[0]=='th':
    th=a[1]; ty=a[2] if len(a)>2 else None
    for r in recs.values():
        if th!='*' and th not in r.get('themes',[]): continue
        if ty and r['type']!=ty: continue
        print(f"{r['id']}{' (formerly marked; no effect)' if r['id'] in R else ''} {r['speaker'][:8]} {r['stage'][:10]} {r['type']} [{','.join(r.get('themes',[]))}]: {r['quote'][:int(os.environ.get('W','260'))]!r}")
if a[0]=='c':
    for i in a[1:]:
        r=recs.get(i)
        if not r: print('MISSING',i); continue
        print(f"{i}{' **R**' if i in R else ''} {r['speaker'][:8]} {r['stage'][:10]} {r['type']}: {r['quote'][:400]!r}")
