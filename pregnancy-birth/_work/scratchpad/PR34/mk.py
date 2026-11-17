import json,sys,runpy
name=sys.argv[1]
R=runpy.run_path(name+'.py')['R']
with open('stage-'+name+'.jsonl','w') as f:
    for r in R:
        u,c,sp,st,ty,th,q,cx=r[:8]
        f.write(json.dumps(dict(u=u,c=c,sp=sp,st=st,ty=ty,th=th,q=q,cx=cx,r=len(r)>8 and r[8]),ensure_ascii=False)+'\n')
print(len(R))
