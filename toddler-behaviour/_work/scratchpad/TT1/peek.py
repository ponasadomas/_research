import json,glob,sys
want=sys.argv[1:]
for f in glob.glob('*.posts.jsonl'):
    for l in open(f):
        d=json.loads(l)
        if d.get('id') in want:
            print(d['id'],d.get('title'),'|',(d.get('selftext') or '')[:600].replace('\n',' '),'\n')
