#!/usr/bin/env python3
"""q.py ids...  -> print id, H(historically marked), speaker, stage, type, quote.  q.py -g REGEX [-u] -> grep quotes (-u retained for compatibility; no exclusions)."""
import json,sys,re
P='/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/voice-merged/all.jsonl'
recs={}
for l in open(P,encoding='utf-8'):
    l=l.strip()
    if l:
        r=json.loads(l); recs[r['id']]=r
def show(r):
    print(f"{r['id']} {'H' if r.get('formerly_restricted') else '-'} {r['speaker']}/{r['stage']}/{r['type']} :: {r['quote'][:400].replace(chr(10),' ')}")
a=sys.argv[1:]
if a and a[0]=='-g':
    rx=re.compile(a[1],re.I); u='-u' in a
    n=0
    for r in recs.values():
        if rx.search(r['quote']):
            show(r); n+=1
    print('N',n)
else:
    for i in a:
        if '-' not in i: continue
        r=recs.get(i)
        if r: show(r)
        else: print(i,'MISSING')
