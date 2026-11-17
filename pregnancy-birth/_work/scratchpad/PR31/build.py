import json, re, sys
base='/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/'
units={}
for l in open(base+'scratchpad/PR31/units.txt'):
    ch,u=l.rstrip('\n').split('\t'); units[u.rsplit('/',1)[1][:-4]]=u
out=[];n=0;restricted=[]
for l in open(base+'scratchpad/PR31/drafts.jsonl'):
    d=json.loads(l); u=units[d['u']]
    txt=open(base+u,encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)',txt)
    pid,sub,date,url=m.groups()
    rec_url,rec_date=url,date
    if d['c']:
        mc=re.search(r'COMMENT '+re.escape(d['c'])+r' \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)',txt)
        rec_date,rec_url=mc.groups()
    n+=1; i='pb31-%04d'%n
    r={'id':i,'source':'reddit r/'+sub,'url':rec_url,'date':rec_date,'speaker':d['sp'],'stage':d['st'],'type':d['ty'],'themes':d['th'],'quote':d['q'],'context':d['cx'],'raw_file':u,'source_class':'reddit_archive','post_id':pid}
    if d['c']: r['comment_id']=d['c']
    if d.get('r'): restricted.append(i)
    if len(d['cx'].split())>25: print('long context',i,len(d['cx'].split()))
    out.append(r)
open(base+'voice/reddit-pr31.jsonl','w',encoding='utf-8').write(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in out))
open(base+'scratchpad/PR31/restricted.txt','w').write('\n'.join(restricted)+'\n')
print(n,len(restricted))
