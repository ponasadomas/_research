import json,sys,re,os,html
V='voice/reddit-pr04.jsonl'; RS='scratchpad/PR04/restricted.txt'
def norm(s): return re.sub(r"\s+"," ",html.unescape(s)).strip()
n=0
if os.path.exists(V): n=sum(1 for l in open(V) if l.strip())
buf=[]
for line in open(sys.argv[1]):
    if not line.strip(): continue
    r=json.loads(line)
    sub,pid=r['u'].split('-',1)
    rf=f"../_shared/_raw/reddit-2026/units/{r['u']}.txt"
    txt=open(rf).read()
    if r.get('c'):
        m=re.search(r"COMMENT "+r['c']+r" \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)",txt)
    else:
        m=re.search(r"POST "+pid+r" \| r/\S+ \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)",txt)
    assert m,(r['u'],r.get('c'))
    nt=norm(txt); pos=0
    for p in re.split(r"\s*\[…\]\s*",r['q']):
        p=norm(p); at=nt.find(p,pos); assert at>=0,(r['u'],p[:80]); pos=at+len(p)
    assert len(r['cx'].split())<=25,r['cx']
    n+=1; i=f"pb04-{n:04d}"
    rec={"id":i,"source":f"reddit r/{sub}","url":m.group(2),"date":m.group(1),"speaker":r['sp'],"stage":r['st'],"type":r['t'],"themes":r['th'],"quote":r['q'],"context":r['cx'],"raw_file":rf,"source_class":"reddit_archive","post_id":pid}
    if r.get('c'): rec["comment_id"]=r['c']
    buf.append((rec,r.get('r')))
out=open(V,'a'); rs=open(RS,'a')
for rec,rr in buf:
    out.write(json.dumps(rec,ensure_ascii=False)+"\n")
    if rr: rs.write(rec['id']+"\t"+rr+"\n")
    print(rec['id'],rec['post_id'])
