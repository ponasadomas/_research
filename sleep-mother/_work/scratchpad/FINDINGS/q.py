#!/usr/bin/env python3
"""Lookup helper for findings. Usage:
 q.py id sb01-0001 ...            print records
 q.py grep REGEX [--type T] [--speaker S] [--theme TH] [--n N]   search quotes
 q.py restricted                  list historically marked ids (no effect on quotation)
 --norestr is accepted as a legacy option but never hides evidence.
"""
import json, re, sys, os
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
recs={}
for l in open(os.path.join(ROOT,'voice-merged','all.jsonl'),encoding='utf-8'):
    l=l.strip()
    if l: r=json.loads(l); recs[r['id']]=r
def restricted():
    # Historical labels are descriptive only, including review ids.
    t=open(os.path.join(ROOT,'synthesis/restricted-ids.md'),encoding='utf-8').read()
    return {i for line in t.splitlines() if line.startswith('|')
            for i in re.findall(r'\bsm(?:r)?\d{1,2}-\d{4}\b',line.split('|')[1])}
R=restricted()
def show(r):
    flag=' FORMERLY_MARKED (no effect)' if r['id'] in R else ''
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
if a[0]=='c':
    for i in a[1:]:
        r=recs.get(i)
        if not r: print('MISSING',i); continue
        print(f"{i} {r['speaker'][:8]} {r['stage'][:10]} {r['type']}: {r['quote'][:400]!r}")
