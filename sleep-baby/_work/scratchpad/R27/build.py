import json,glob,re,os,sys
base='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/'
units=[l.split('\t')[1].strip() for l in open(base+'scratchpad/R27/units.txt')]
def meta(u,c):
    t=open(base+u,encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)',t)
    pid,sub,date,url=m.groups()
    if c:
        mm=re.search(r'COMMENT '+c+r' \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)',t)
        date,url=mm.groups()
    return pid,sub,date,url
out=[];restricted=[];n=0
for f in sorted(glob.glob(base+'scratchpad/R27/recs-b*.jsonl')):
    for line in open(f):
        if not line.strip(): continue
        r=json.loads(line); n+=1
        u=units[r['u']-1]; pid,sub,date,url=meta(u,r.get('c'))
        rid='sb27-%04d'%n
        rec={'id':rid,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':r['sp'],'stage':r['st'],'type':r['ty'],'themes':r['th'],'quote':r['q'],'context':r['cx'],'raw_file':u,'source_class':'reddit_archive','post_id':pid}
        if r.get('c'): rec['comment_id']=r['c']
        if len(r['cx'].split())>25: print('LONG CONTEXT',rid)
        if r.get('r'): restricted.append((rid,r['r']))
        out.append(rec)
with open(base+'voice/reddit-r27.jsonl','w') as fo:
    for rec in out: fo.write(json.dumps(rec,ensure_ascii=False)+'\n')
with open(base+'scratchpad/R27/restricted.tsv','w') as fo:
    for a,b in restricted: fo.write(a+'\t'+b+'\n')
print(n,'records',len(restricted),'restricted')
