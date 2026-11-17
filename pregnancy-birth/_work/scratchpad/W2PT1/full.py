import sys,re,glob
base='/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/'
import json
ids=set(sys.argv[1:])
for f in glob.glob(base+'*.posts.jsonl'):
    for l in open(f):
        if any(i in l[:200] for i in ids):
            d=json.loads(l)
            if d.get('id') in ids: print(d['id'],'|',d.get('title'),'|',re.sub(r'\s+',' ',d.get('selftext',''))[:int(900)],'\n')
