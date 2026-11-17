import json,sys,re
o=json.load(open('all.json'))
sl=re.compile(r'sleep|nap|bedtime|night|wake|waking|crib|cot\b|bassinet|cosleep|co-sleep|bed.?shar',re.I)
for k in map(int,sys.argv[1:]):
    f,i,fl,n,L,t,body=o[k]
    ss=re.split(r'(?<=[.!?])\s+',' '.join(body.split()))
    hits=[s for s in ss if sl.search(s)]
    print(f"## {k} {t[:70]}")
    print(' // '.join(h[:200] for h in hits[:5])[:700])
