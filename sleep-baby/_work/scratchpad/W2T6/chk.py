import json,re,glob,sys
want=set(sys.argv[1:])
for f in glob.glob("_shared/_raw/reddit-2026/*.posts.jsonl"):
    for l in open(f):
        try:d=json.loads(l)
        except: continue
        if d.get("id") in want:
            t=re.sub(r'\s+',' ',d.get("selftext") or "")
            ss=re.split(r'(?<=[.!?]) ',t)
            hit=[s[:160] for s in ss if re.search(r'sleep|nap\b|naps|bedtime|wak(e|ing)|night|crib|cosleep',s,re.I)]
            print(d["id"],"::"," // ".join(hit[:4])[:520]); 
