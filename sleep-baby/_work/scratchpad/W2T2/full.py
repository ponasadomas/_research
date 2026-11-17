import sys,json,glob
want=set(sys.argv[1:])
for f in glob.glob('/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/*.posts.jsonl'):
    for l in open(f):
        if not any(w in l for w in want): continue
        d=json.loads(l)
        if d.get('id') in want:
            print('##',d['id'],d.get('title'),'\n',(d.get('selftext') or '')[:1100].replace('\n',' '),'\n')
