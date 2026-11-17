import json,sys
o=json.load(open('all.json'))
a,b,w=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
for k,(f,i,fl,n,L,t,body) in enumerate(o[a:b],a):
    print(f"{k}|{i}|{'S' if fl=='True' else ''}|s{n}|L{L}|{t[:110]}|"+' '.join(body.split())[:w])
