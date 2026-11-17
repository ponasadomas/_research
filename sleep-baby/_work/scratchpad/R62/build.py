import json,re,glob,os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
units={}
for l in open('scratchpad/R62/units.txt'):
    ch,p=l.strip().split('\t'); pid=os.path.basename(p)[:-4].split('-')[-1]; units[pid]=p
out=[];restricted=[];n=0
for f in sorted(glob.glob('scratchpad/R62/q*.jsonl')):
    for line in open(f):
        if not line.strip(): continue
        pid,cid,sp,st,ty,th,q,ctx,r=json.loads(line)
        p=units[pid]; txt=open(p,encoding='utf-8').read()
        m=re.search(r'^POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)$',txt,re.M)
        sub=m.group(2); url=m.group(4); date=m.group(3)
        if cid:
            mc=re.search(r'^COMMENT '+cid+r' \| (\d{4}-\d\d-\d\d) .*?\| (\S+)$',txt,re.M)
            date=mc.group(1); url=mc.group(2)
        n+=1; i='sb62-%04d'%n
        rec=dict(id=i,source='reddit r/'+sub,url=url,date=date,speaker=sp,stage=st,type=ty,themes=th,quote=q,context=ctx,raw_file=p,source_class='reddit_archive',post_id=pid)
        if cid: rec['comment_id']=cid
        assert len(ctx.split())<=25,(i,ctx)
        out.append(rec)
        if r: restricted.append(i)
with open('voice/reddit-r62.jsonl','w') as w:
    for r in out: w.write(json.dumps(r,ensure_ascii=False)+'\n')
open('scratchpad/R62/restricted.txt','w').write('\n'.join(restricted)+'\n')
print(n,'quotes',len(restricted),'restricted')
