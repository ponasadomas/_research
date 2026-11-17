import sys,json,glob
for i in sys.argv[1:]:
    for f in glob.glob("/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/*.posts.jsonl"):
        for l in open(f):
            if '"%s"'%i in l[:400]:
                d=json.loads(l)
                if d.get("id")==i: print(i,d.get("title"),"::",(d.get("selftext") or "")[:700].replace("\n"," "),"\n");break
