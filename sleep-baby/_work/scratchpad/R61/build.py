#!/usr/bin/env python3
# Build reddit-r61.jsonl from q*.tsv: unit \t comment_id \t speaker \t stage \t type \t themes \t context \t quote
import json, re, glob, os
B='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/'
rows=[]
for f in sorted(glob.glob(B+'scratchpad/R61/q*.tsv')):
    for ln in open(f, encoding='utf-8'):
        if not ln.strip() or ln.startswith('#'): continue
        p=[x.strip() for x in ln.rstrip('\n').split(' ¦ ')]
        assert len(p)==8, (f, ln[:80])
        rows.append(p)
out=[]
for i,(u,cid,sp,st,ty,th,ctx,q) in enumerate(rows,1):
    rf='../_shared/_raw/reddit-2026/units/%s.txt'%u
    txt=open(B+rf,encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)',txt)
    pid,sub,date,url=m.groups()
    rec={'id':'sb61-%04d'%i,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':sp,'stage':st,'type':ty,
         'themes':[t.strip() for t in th.split(',') if t.strip()],'quote':q,'context':ctx,'raw_file':rf,
         'source_class':'reddit_archive','post_id':pid}
    if cid:
        cm=re.search(r'COMMENT %s \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)'%cid,txt)
        assert cm,(u,cid)
        rec['date'],rec['url']=cm.group(1),cm.group(2); rec['comment_id']=cid
    assert len(ctx.split())<=25,(ctx)
    out.append(rec)
open(B+'voice/reddit-r61.jsonl','w',encoding='utf-8').write(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in out))
print(len(out))
