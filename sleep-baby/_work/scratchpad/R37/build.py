# usage: python3 -I build.py  -> reads entries_*.py (each defines E = [...]), writes voice file
import json, re, os, glob, sys
here=os.path.dirname(os.path.abspath(__file__)); sb=os.path.join(here,'..','..')
os.chdir(sb)
E=[]
for f in sorted(glob.glob(os.path.join(here,'entries_*.py'))):
    ns={}; exec(open(f).read(),ns); E+=ns['E']
out=[]
for n,e in enumerate(E,1):
    unit,cid,spk,stg,typ,th,q,ctx=e
    rf='../_shared/_raw/reddit-2026/units/%s.txt'%unit
    txt=open(rf,encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    r={"id":"sb37-%04d"%n,"source":"reddit r/"+sub,"url":url,"date":date,"speaker":spk,"stage":stg,"type":typ,"themes":th,"quote":q,"context":ctx,"raw_file":rf,"source_class":"reddit_archive","post_id":pid}
    if cid:
        cm=re.search(r'COMMENT %s \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)'%cid,txt)
        r["date"],r["url"]=cm.groups(); r["comment_id"]=cid
    assert len(ctx.split())<=25,(n,ctx)
    r["themes"]=["success_expectations" if t=="success_story" else t for t in r["themes"]]
    out.append(r)
with open('voice/reddit-r37.jsonl','w') as f:
    for r in out: f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(out))
