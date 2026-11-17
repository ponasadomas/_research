import sys,json,glob,re
ids=set(sys.argv[2:]);n=int(sys.argv[1])
for f in glob.glob("/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/*.posts.jsonl"):
    for l in open(f):
        if not any(i in l[:400] for i in ids): continue
        d=json.loads(l)
        if d.get('id') in ids:
            print(d['id'],'::',re.sub(r'\s+',' ',d.get('selftext',''))[:n],'\n')
