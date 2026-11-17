import sys,glob,json
want=set(sys.argv[2:]);n=int(sys.argv[1])
for f in glob.glob('/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/*.posts.jsonl'):
    for l in open(f):
        if not any(w in l for w in want):continue
        d=json.loads(l)
        if d.get('id') in want:
            print(d['id'],'|',d.get('title','')[:80],'|',(d.get('selftext') or '').replace('\n',' ')[:n]);print()
