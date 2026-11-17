import json,sys
c=sys.argv[1]
for l in open('_raw/reddit/read-v1/chunks.jsonl'):
    d=json.loads(l)
    if d['chunk']==c:
        for u in d['units']:
            print('=====',u); print(open(u).read())
