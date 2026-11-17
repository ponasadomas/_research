# usage: python3 -I add.py specfile ; spec lines: unit|cid or -|speaker|stage|type|themes,comma|quote|context
import json,sys,re,os
B='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/'
V=B+'voice/reddit-r17.jsonl'
n=0
if os.path.exists(V): n=sum(1 for l in open(V) if l.strip())
out=open(V,'a')
for line in open(sys.argv[1],encoding='utf-8'):
    line=line.rstrip('\n')
    if not line.strip() or line.startswith('#'): continue
    p=line.split('|')
    assert len(p)==8,(len(p),line[:80])
    unit,cid,sp,st,ty,th,q,c=p
    rf='../_shared/_raw/reddit-2026/units/'+unit+'.txt'
    txt=open(B+rf,encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    if cid!='-':
        mm=re.search(r'COMMENT '+cid+r' \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)',txt)
        date,url=mm.groups()
    assert len(c.split())<=25,c
    n+=1
    r={'id':'sb17-%04d'%n,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':sp,'stage':st,'type':ty,'themes':th.split(','),'quote':q,'context':c,'raw_file':rf,'source_class':'reddit_archive','post_id':pid}
    if cid!='-': r['comment_id']=cid
    out.write(json.dumps(r,ensure_ascii=False)+'\n')
print('total',n)
