import sys,json,re,glob
ids=set(sys.argv[1:])
for f in glob.glob('/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/*.posts.jsonl'):
    for l in open(f):
        if not any(i in l for i in ids): continue
        d=json.loads(l)
        if d.get('id') in ids:
            t=(d.get('title','')+' . '+d.get('selftext','')).replace('\n',' ')
            ss=[s for s in re.split(r'(?<=[.!?]) ',t) if re.search(r'sleep|slept|tired|exhaust|insomnia|awake|night|nap|rest',s,re.I)]
            print(d['id'],len(t),'|',' '.join(ss)[:300]);print()
