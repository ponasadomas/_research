import sys,json
sub=sys.argv[1]; ids=set(sys.argv[2:])
for l in open(f'/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/{sub}.posts.jsonl'):
    d=json.loads(l)
    if d['id'] in ids: print('##',d['id'],d['title'],'|',d['selftext'][:600].replace('\n',' '));print()
