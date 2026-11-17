# Build voice jsonl from q*.txt files. Line format (sep " ||| "):
# unit_basename ||| comment_id or - ||| speaker ||| stage ||| type ||| themes,comma ||| R or - ||| quote ||| context
import json,re,glob,os,sys
base='/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth'
rawpre='../_shared/_raw/reddit-2026/units/'
out=[];restr=[];n=0
for fn in sorted(glob.glob(base+'/scratchpad/PR63/q*.txt')):
  for line in open(fn,encoding='utf-8'):
    line=line.rstrip('\n')
    if not line.strip() or line.startswith('#'): continue
    if line.startswith('DROP '):
      n+=1; continue
    p=line.split(' ||| ')
    assert len(p)==9,(fn,line[:80],len(p))
    ub,cid,sp,st,ty,th,r,q,ctx=p
    rf=rawpre+ub+'.txt'
    txt=open(os.path.join(base,rf),encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    if cid!='-':
      mm=re.search(r'COMMENT '+cid+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
      assert mm,(ub,cid); date,url=mm.groups()
    assert len(ctx.split())<=25,(ctx)
    n+=1; i='pb63-%04d'%n
    d={'id':i,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':sp,'stage':st,'type':ty,'themes':[t.strip() for t in th.split(',') if t.strip()],'quote':q,'context':ctx,'raw_file':rf,'source_class':'reddit_archive','post_id':pid}
    if cid!='-': d['comment_id']=cid
    out.append(d)
    if r=='R': restr.append(i)
with open(base+'/voice/reddit-pr63.jsonl','w',encoding='utf-8') as f:
  for d in out: f.write(json.dumps(d,ensure_ascii=False)+'\n')
open(base+'/scratchpad/PR63/restricted.txt','w').write('\n'.join(restr)+'\n')
print(n,'records',len(restr),'restricted')
