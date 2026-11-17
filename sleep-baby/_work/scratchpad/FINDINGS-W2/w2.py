#!/usr/bin/env python3
"""Wave-2 helper. Usage:
 w2.py money            quotes in sb22..sb40 with a currency amount
 w2.py grep REGEX       wave-2 quotes matching REGEX
 w2.py theme T1,T2..    count wave-2 quotes carrying any of the themes
 w2.py dup              identical quote text across different ids in wave 2
"""
import json,re,sys,os
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
recs=[json.loads(l) for l in open(os.path.join(ROOT,'voice-merged','all.jsonl'),encoding='utf-8') if l.strip()]
W2=[r for r in recs if re.match(r'sb(2[2-9]|3\d|40)-',r['id'])]
MONEY=re.compile(r'[$£€]\s?\d|\d\s?[$£€]|\d\s?(k|K)\b|\d+\s?(dollars|pounds|euros|bucks)|thousands? of dollars|hundreds of dollars|\$\$',re.I)
def show(r): print(f"[{r['id']}]{' R' if r.get('restricted') else ''} {r['date']} {r['post_id']} | {r['quote'][:300]!r}")
a=sys.argv[1:]
if a[0]=='money':
    n=0
    for r in W2:
        if MONEY.search(r['quote']): show(r); n+=1
    print('count',n,'of',len(W2))
elif a[0]=='grep':
    rx=re.compile(a[1],re.I); n=0
    for r in W2:
        if rx.search(r['quote']): show(r); n+=1
    print('count',n)
elif a[0]=='theme':
    ts=set(a[1].split(',')); m=[r for r in W2 if ts & set(r.get('themes',[]))]
    print('wave-2 quotes with',sorted(ts),':',len(m),'of',len(W2),'| restricted among them:',sum(1 for r in m if r.get('restricted')))
elif a[0]=='dup':
    d={}
    for r in W2: d.setdefault(r['quote'].strip(),[]).append(r['id'])
    for q,ids in d.items():
        if len(ids)>1: print(ids, q[:80])
elif a[0]=='stats':
    print('wave-2 quotes',len(W2),'restricted',sum(1 for r in W2 if r.get('restricted')))
    from collections import Counter
    print(Counter(r['speaker'] for r in W2)); print(min(r['date'] for r in W2), max(r['date'] for r in W2))
