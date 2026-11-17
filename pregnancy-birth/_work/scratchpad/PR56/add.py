# usage: python3 -I add.py staged.tsv  -> rebuilds voice file from all staged tsv files in order
# TSV cols: unitid(sub-postid) commentid|- speaker stage type themes(comma) R|- quote context
import json,sys,re,glob,os
base='/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth'
units={}
for l in open(base+'/scratchpad/PR56/units.tsv'):
    c,u=l.rstrip('\n').split('\t'); units[os.path.basename(u)[:-4]]=u
out=[];restr=[];n=0;seen=set()
for f in sorted(glob.glob(base+'/scratchpad/PR56/staged-*.tsv')):
  for line in open(f,encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    p=line.rstrip('\n').split('\t')
    assert len(p)==9,(f,line[:80],len(p))
    uid,cid,sp,st,ty,th,R,q,ctx=p
    u=units[uid]; txt=open(os.path.join(base,u),encoding='utf-8').read()
    m=re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    rec={'id':None,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':sp,'stage':st,'type':ty,'themes':th.split(','),'quote':q,'context':ctx,'raw_file':u,'source_class':'reddit_archive','post_id':pid}
    if cid!='-':
        mm=re.search(r'COMMENT '+cid+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
        assert mm,(uid,cid)
        rec['date'],rec['url']=mm.groups(); rec['comment_id']=cid
    assert len(ctx.split())<=25,ctx
    n+=1; rec['id']='pb56-%04d'%n
    if R=='R': restr.append(rec['id'])
    out.append(rec)
with open(base+'/voice/reddit-pr56.jsonl','w',encoding='utf-8') as o:
    for r in out:
        r={k:v for k,v in r.items()}
        o.write(json.dumps(r,ensure_ascii=False)+'\n')
open(base+'/scratchpad/PR56/restricted.txt','w').write(', '.join(restr)+'\n')
print(n,'records;',len(restr),'restricted')
