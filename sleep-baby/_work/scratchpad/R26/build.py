import json, re, sys, os, glob
SB='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby'
SC=SB+'/scratchpad/R26'
units={}
for l in open(SC+'/units.txt'):
    ch,p=l.rstrip('\n').split('\t'); units[os.path.basename(p)[:-4]]=p
out=[];restr=[];n=0;errs=0
for f in sorted(glob.glob(SC+'/q*.jsonl')):
    for line in open(f):
        if not line.strip(): continue
        s=json.loads(line); u=s['u']; p=units[u]
        txt=open(os.path.join(SB,p),encoding='utf-8').read()
        m=re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
        pid,sub,date,url=m.groups()
        c=s.get('c') or ''
        if c:
            mm=re.search(r'COMMENT '+c+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
            if not mm: print('NO COMMENT',u,c); errs+=1; continue
            date,url=mm.groups()
        n+=1; rid='sb26-%04d'%n
        if len(s['cx'].split())>25: print('LONG CTX',rid,u)
        r={'id':rid,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':s['sp'],'stage':s['st'],'type':s['t'],'themes':s['th'],'quote':s['q'],'context':s['cx'],'raw_file':p,'source_class':'reddit_archive','post_id':pid}
        if c: r['comment_id']=c
        out.append(r)
        if s.get('r'): restr.append((rid,s['r']))
        print(rid, f.split('/')[-1], u, file=open(SC+'/idmap.txt','a') if False else sys.stderr) if False else None
with open(SB+'/voice/reddit-r26.jsonl','w') as fo:
    for r in out: fo.write(json.dumps(r,ensure_ascii=False)+'\n')
with open(SC+'/restricted.txt','w') as fo:
    for a,b in restr: fo.write(a+'\t'+b+'\n')
print('records',n,'restricted',len(restr),'errs',errs)
