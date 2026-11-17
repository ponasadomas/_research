import json,sys
o=json.load(open('all.json'))
a,b=int(sys.argv[1]),int(sys.argv[2])
ov={}
for l in open(sys.argv[3]):
    p=l.rstrip('\n').split(' ',2)
    if len(p)>=2: ov[int(p[0])]=(p[1],p[2] if len(p)>2 else '')
for k in range(a,b):
    t=' '.join(o[k][5].split()[:11])
    lab,why=ov.get(k,('c',''))
    print(k,lab,why or t)
