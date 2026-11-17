import json,sys,glob
want=set(sys.argv[2:]); n=int(sys.argv[1])
for f in glob.glob('/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/*.posts.jsonl'):
    for l in open(f):
        if '"id": "' in l:
            d=json.loads(l)
            if d['id'] in want:
                print(d['id'],'|',d['title'][:80],'|',' '.join(d['selftext'].split())[:n]);print()
