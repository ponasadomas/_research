import json, re, html, sys, glob, os
B='/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/'
def norm(s): return re.sub(r"\s+"," ",html.unescape(s)).strip()
units={l.split('\t')[1].strip().split('/')[-1][:-4]:l.split('\t')[1].strip() for l in open(B+'scratchpad/PR43/units.txt')}
def segs(path):
    txt=open(B+path,encoding='utf-8').read()
    out=[];cur=None
    for line in txt.split('\n'):
        m=re.match(r'^POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [\d:]+ UTC \| (\S+)',line)
        c=re.match(r'^COMMENT (\w+) \| (\d{4}-\d\d-\d\d) [\d:]+ UTC \| (\S+)',line)
        if m: sub=m.group(2); pid=m.group(1); cur={'cid':None,'date':m.group(3),'url':m.group(4),'t':[]}; out.append(cur)
        elif c: cur={'cid':c.group(1),'date':c.group(2),'url':c.group(3),'t':[]}; out.append(cur)
        elif cur: cur['t'].append(line)
    for s in out: s['t']=norm('\n'.join(s['t']))
    return sub,pid,out
recs=[];n=0;rest=[]
for f in sorted(glob.glob(B+'scratchpad/PR43/spec*.txt'), key=lambda x:int(re.search(r'spec(\d+)',x).group(1))):
    for line in open(f,encoding='utf-8'):
        line=line.rstrip('\n')
        if not line.strip(): continue
        u,sp,st,ty,th,r,ctx,q=line.split('|',7)
        path=units[u]; sub,pid,ss=segs(path)
        first=norm(re.split(r"\s*\[(?:…|\.\.\.)\]\s*",q)[0])
        hit=[s for s in ss if first in s['t']]
        if not hit: print('NOTFOUND',u,q[:60]); hit=[ss[0]]
        s=hit[0]; n+=1
        rid='pb43-%04d'%n
        d={'id':rid,'source':'reddit r/'+sub,'url':s['url'],'date':s['date'],'speaker':sp,'stage':st,'type':ty,'themes':th.split(','),'quote':q,'context':ctx,'raw_file':path,'source_class':'reddit_archive','post_id':pid}
        if s['cid']: d['comment_id']=s['cid']
        if len(ctx.split())>25: print('LONGCTX',rid)
        recs.append(d)
        if r=='R': rest.append(rid)
with open(B+'voice/reddit-pr43.jsonl','w',encoding='utf-8') as o:
    for d in recs: o.write(json.dumps(d,ensure_ascii=False)+'\n')
open(B+'scratchpad/PR43/restricted.txt','w').write('\n'.join(rest)+'\n')
print(len(recs),'records',len(rest),'restricted')
