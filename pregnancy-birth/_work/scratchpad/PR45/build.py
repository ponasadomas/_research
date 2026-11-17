import json,re,sys
base='../_shared/_raw/reddit-2026/units/'
out=[];restricted=[];n=0
for line in open('scratchpad/PR45/q.tsv',encoding='utf-8'):
    line=line.rstrip('\n')
    if not line.strip(): continue
    f=line.split('\t')
    assert len(f)==9,(len(f),line[:80])
    unit,cid,spk,stg,typ,th,R,q,ctx=f
    raw=base+unit+'.txt'
    txt=open(raw,encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    rec={}
    if cid!='-':
        mc=re.search(r'COMMENT '+cid+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
        date,url=mc.groups()
    n+=1
    rid='pb45-%04d'%n
    assert len(ctx.split())<=25,(rid,len(ctx.split()))
    rec=dict(id=rid,source='reddit r/'+sub,url=url,date=date,speaker=spk,stage=stg,type=typ,themes=th.split(','),quote=q,context=ctx,raw_file=raw,source_class='reddit_archive',post_id=pid)
    if cid!='-': rec['comment_id']=cid
    out.append(rec)
    if R=='R': restricted.append(rid)
with open('voice/reddit-pr45.jsonl','w',encoding='utf-8') as fo:
    for r in out: fo.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(out)); print(' '.join(restricted))
