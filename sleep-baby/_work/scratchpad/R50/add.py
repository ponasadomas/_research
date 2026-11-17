# usage: python3 -I add.py batchfile  ; batch lines: unit|comment_id|speaker|stage|type|themes(comma)|quote|context
import json,sys,re,os
SB='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby'
OUT=SB+'/voice/reddit-r50.jsonl'
n=0
if os.path.exists(OUT):
    n=sum(1 for l in open(OUT) if l.strip())
out=open(OUT,'a')
for line in open(sys.argv[1],encoding='utf-8'):
    line=line.rstrip('\n')
    if not line.strip() or line.startswith('#'): continue
    p=line.split('|')
    assert len(p)==8,line
    unit,cid,sp,st,ty,th,q,ctx=p
    rf='../_shared/_raw/reddit-2026/units/%s.txt'%unit
    txt=open(os.path.join(SB,rf),encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    rec={}
    if cid:
        mm=re.search(r'COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)'%re.escape(cid),txt)
        assert mm,(unit,cid)
        date,url=mm.groups()
    assert len(ctx.split())<=25,ctx
    n+=1
    rec=dict(id='sb50-%04d'%n,source='reddit r/'+sub,url=url,date=date,speaker=sp,stage=st,type=ty,themes=[t for t in th.split(',') if t],quote=q,context=ctx,raw_file=rf,source_class='reddit_archive',post_id=pid)
    if cid: rec['comment_id']=cid
    out.write(json.dumps(rec,ensure_ascii=False)+'\n')
print('total',n)
