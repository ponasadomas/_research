import json,glob,re,sys
ids=set(sys.argv[1:])
for f in glob.glob('/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/*.posts.jsonl'):
    for l in open(f):
        if not any(i in l for i in ids): continue
        d=json.loads(l)
        if d['id'] in ids:
            t=(d.get('selftext') or '').replace('\n',' ')
            ms=[t[max(0,m.start()-150):m.end()+150] for m in re.finditer(r"sleep|insomnia|awake|slept|night",t)]
            print(d['id'],d['title'][:40],'||',' ... '.join(ms[:2]),'\n')
