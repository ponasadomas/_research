import sys,json,glob
ids=set(sys.argv[1:])
for f in glob.glob('/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/*.posts.jsonl'):
    for l in open(f):
        if not any(i in l for i in ids): continue
        d=json.loads(l)
        if d.get('id') in ids:
            print(d['id'],'|',d.get('title'),'|',(d.get('selftext') or '')[:1100].replace('\n',' '),'\n')
