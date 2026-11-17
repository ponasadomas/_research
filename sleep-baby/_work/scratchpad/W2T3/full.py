import sys,json,glob
want=set(sys.argv[1:]); n=int(0)
for f in glob.glob('/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/*.posts.jsonl'):
    for l in open(f):
        if not any(w in l for w in want): continue
        r=json.loads(l)
        if r.get('id') in want:
            print('##',r['id'],r.get('title','')[:80],'\n',(r.get('selftext') or '')[:700].replace('\n',' '),'\n')
