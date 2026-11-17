import json,glob,os,re,sys
base=os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(base,'..','..'))
units=[l.rstrip('\n').split('\t') for l in open(os.path.join(base,'units.tsv'))]
upath={os.path.basename(u)[:-4]:(c,u) for c,u,s in units}
recs=[];S={}
for f in sorted(glob.glob(os.path.join(base,'recs','b*.py'))):
    ns={};exec(open(f).read(),ns);recs+=ns['R'];S.update(ns.get('S',{}))
out=[];restr=[];bad=0
for i,r in enumerate(recs,1):
    unit,cid,date,sp,st,ty,th,q,ctx,rr=r
    if unit not in upath: print('UNKNOWN UNIT',unit);bad+=1;continue
    c,u=upath[unit]; sub,pid=unit.split('-',1)
    txt=open(u).read()
    if cid and cid not in txt: print('cid missing',unit,cid)
    m=re.search((r'COMMENT '+cid if cid else r'POST '+pid)+r' \| (?:r/\S+ \| )?(\d{4}-\d\d-\d\d)',txt)
    if m and m.group(1)!=date: print('date fix',i,date,m.group(1)); date=m.group(1)
    url=f"https://www.reddit.com/r/{sub}/comments/{pid}/"+(f"comment/{cid}/" if cid else "")
    if url not in txt: print('url missing',url)
    if len(ctx.split())>25: print('ctx long',i,len(ctx.split()))
    d={"id":f"pb16-{i:04d}","source":f"reddit r/{sub}","url":url,"date":date,"speaker":sp,"stage":st,"type":ty,"themes":th,"quote":q,"context":ctx,"raw_file":u,"source_class":"reddit_archive","post_id":pid}
    if cid: d["comment_id"]=cid
    out.append(d)
    if rr: restr.append((d["id"],rr))
with open('voice/reddit-pr16.jsonl','w') as f:
    for d in out: f.write(json.dumps(d,ensure_ascii=False)+"\n")
json.dump({"restricted":restr,"S":S},open(os.path.join(base,'meta.json'),'w'),ensure_ascii=False,indent=0)
print(len(out),'records',len(restr),'restricted')
