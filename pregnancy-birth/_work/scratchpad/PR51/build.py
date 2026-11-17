import json,re,os,sys
B=os.path.dirname(os.path.abspath(__file__))
NB=os.path.join(B,'..','..')
out=[];restr=[];n=0
for line in open(os.path.join(B,'q.jsonl'),encoding='utf-8'):
    if not line.strip(): continue
    r=json.loads(line)
    rf='../_shared/_raw/reddit-2026/units/%s.txt'%r['u']
    txt=open(os.path.join(NB,rf),encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\S+) .*?\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    c=r.get('c')
    if c:
        mm=re.search(r'COMMENT %s \| (\S+) .*?\| (\S+)'%c,txt)
        date,url=mm.groups()
    n+=1
    rec={'id':'pb51-%04d'%n,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':r['sp'],'stage':r['st'],'type':r['ty'],'themes':r['th'],'quote':r['q'],'context':r['cx'],'raw_file':rf,'source_class':'reddit_archive','post_id':pid}
    if c: rec['comment_id']=c
    assert len(r['cx'].split())<=25, r['cx']
    out.append(rec)
    if r.get('r'): restr.append(rec['id'])
with open(os.path.join(NB,'voice','reddit-pr51.jsonl'),'w',encoding='utf-8') as f:
    for rec in out: f.write(json.dumps(rec,ensure_ascii=False)+'\n')
open(os.path.join(B,'restricted.txt'),'w').write('\n'.join(restr)+'\n')
print(n,'quotes',len(restr),'restricted')
