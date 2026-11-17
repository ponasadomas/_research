# usage: python3 -I add.py batchfile.tsv  ; appends records to voice file
# batch line format (tab-separated): unit|comment_id|speaker|stage|type|themes(comma)|context|quote
import json, sys, re, os, html
def norm(s):
    s=html.unescape(s).replace('\\n',' ')
    return re.sub(r'\s+',' ',s).strip()
TYPES='trigger_moment pain fear tried_failed desire belief question objection advice_given success_story failure_story regret others_said purchase price_signal'.split()
B=os.path.dirname(os.path.abspath(__file__))+'/../..'
V=B+'/voice/reddit-r20.jsonl'
n=0
if os.path.exists(V): n=sum(1 for l in open(V) if l.strip())
out=[]
for line in open(sys.argv[1],encoding='utf-8'):
    line=line.rstrip('\n')
    if not line.strip() or line.startswith('#'): continue
    unit,cid,sp,st,ty,th,ctx,q=[x.strip() for x in line.split('¦')]
    raw='../_shared/_raw/reddit-2026/units/'+unit+'.txt'
    txt=open(B+'/'+raw,encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\S+) .*?\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    rec={}
    if cid:
        cm=re.search(r'COMMENT '+cid+r' \| (\S+) .*?\| (\S+)',txt)
        date,url=cm.groups()
    n+=1
    rec={"id":"sb20-%04d"%n,"source":"reddit r/"+sub,"url":url,"date":date,"speaker":sp,"stage":st,"type":ty,"themes":th.split(','),"quote":q,"context":ctx,"raw_file":raw,"source_class":"reddit_archive","post_id":pid}
    if cid: rec["comment_id"]=cid
    assert len(ctx.split())<=25, ctx
    assert ty in TYPES, ty
    T=norm(txt); pos=0
    for piece in re.split(r'\s*\[(?:…|\.\.\.)\]\s*', q):
        piece=norm(piece)
        at=T.find(piece,pos)
        if at<0: sys.exit('MISSING '+unit+': '+piece[:80])
        pos=at+len(piece)
    out.append(json.dumps(rec,ensure_ascii=False)+'\n')
open(V,'a').writelines(out); print(n)
