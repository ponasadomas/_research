import json,sys,glob
recs=[]
for n in (4,5,6):
    recs+= [json.loads(l) for l in open(f'voice/reddit-mr0{n}.jsonl')]
a,b=int(sys.argv[1]),int(sys.argv[2])
for i,r in enumerate(recs[a:b],a):
    print(f"{r['id']}|{r['source'][14:]}|{r['quote']}")
