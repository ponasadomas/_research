import json,sys,glob
ids=set(sys.argv[1:])
for f in glob.glob('_shared/_raw/reddit-2026/*.posts.jsonl'):
    for l in open(f):
        d=json.loads(l)
        if d.get('id') in ids:
            t=(d.get('selftext') or '').replace('\n',' ')
            print('##',d['id'],t[300:1000],'\n')
