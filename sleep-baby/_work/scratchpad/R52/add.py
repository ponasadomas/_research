# usage: python3 -I add.py recs.json  -> appends to voice/reddit-r52.jsonl
# rec: [unit_index, comment_id or "", speaker, stage, type, [themes], quote, context]
import json,sys,re,os
B='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/'
units=[l.rstrip('\n').split('\t')[1] for l in open(B+'scratchpad/R52/units.tsv')]
out=B+'voice/reddit-r52.jsonl'
n=sum(1 for l in open(out)) if os.path.exists(out) else 0
recs=json.load(open(sys.argv[1]))
with open(out,'a') as f:
  for rec in recs:
    u,cid,sp,st,ty,th,q,ctx=rec[:8]; rr=rec[8] if len(rec)>8 else ''
    rf=units[u-1]; t=open(B+rf,encoding='utf-8').read()
    m=re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)',t)
    pid,sub,date,url=m.groups()
    r={}
    if cid:
      mm=re.search(r'COMMENT '+cid+r' \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)',t); date,url=mm.groups()
    n+=1
    r=dict(id='sb52-%04d'%n,source='reddit r/'+sub,url=url,date=date,speaker=sp,stage=st,type=ty,themes=th,quote=q,context=ctx,raw_file=rf,source_class='reddit_archive',post_id=pid)
    if cid: r['comment_id']=cid
    f.write(json.dumps(r,ensure_ascii=False)+'\n')
    if rr: open(B+'scratchpad/R52/restricted.txt','a').write(r['id']+'\t'+rr+'\n')
print('total',n)
