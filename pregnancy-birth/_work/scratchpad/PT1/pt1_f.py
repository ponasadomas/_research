import sys,json,glob,re
ids=set(sys.argv[1:])
for fn in glob.glob('/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/*.posts.jsonl'):
    for l in open(fn):
        if not any(i in l for i in ids): continue
        d=json.loads(l)
        if d.get('id') in ids:
            print(d['id'],'|',d.get('title'),'|',re.sub(r'\s+',' ',d.get('selftext',''))[:700],'\n')
