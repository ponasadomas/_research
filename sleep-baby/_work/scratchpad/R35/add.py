# usage: python3 -I add.py batch.json  -> appends records to voice file
import json,sys,re,os
B='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/'
units=[l.rstrip('\n').split('\t')[1] for l in open(B+'scratchpad/R35/units.tsv')]
out=B+'voice/reddit-r35.jsonl'
n=sum(1 for l in open(out)) if os.path.exists(out) else 0
recs=json.load(open(sys.argv[1]))
with open(out,'a') as f:
  for r in recs:
    ui,cid,sp,st,ty,th,q,ctx=r
    u=units[ui-1]; txt=open(B+u).read()
    m=re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    rec={}
    if cid:
      mm=re.search(r'COMMENT '+cid+r' \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)',txt)
      date,url=mm.groups()
    n+=1
    rec=dict(id='sb35-%04d'%n,source='reddit r/'+sub,url=url,date=date,speaker=sp,stage=st,type=ty,themes=th,quote=q,context=ctx,raw_file=u,source_class='reddit_archive',post_id=pid)
    if cid: rec['comment_id']=cid
    assert len(ctx.split())<=25, ctx
    f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print('total',n)
