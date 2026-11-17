import sys,json,re,glob
sub=sys.argv[1]; ids=set(sys.argv[2:])
for l in open(f'../_shared/_raw/reddit-2026/{sub}.posts.jsonl'):
    d=json.loads(l)
    if d['id'] in ids:
        t=d.get('selftext','') or ''
        n=len(re.findall(r'sleep|nap|night|bedtime|wak',t,re.I))
        print(d['id'],len(t),'sl=',n,'|',' '.join(t.split())[:600]);print()
