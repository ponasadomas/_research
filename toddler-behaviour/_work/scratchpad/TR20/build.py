import json,re,sys,os
base=os.path.dirname(os.path.abspath(__file__))
root=os.path.join(base,'..','..')
out=[]
n=0
for line in open(os.path.join(base,'draft.jsonl')):
    if not line.strip(): continue
    d=json.loads(line)
    u=d['u']; rf='../_shared/_raw/reddit-2026/units/%s.txt'%u
    txt=open(os.path.join(root,rf),encoding='utf-8').read()
    m=re.search(r'^POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt,re.M)
    pid,sub,date,url=m.groups()
    rec_extra={}
    if d.get('c'):
        mc=re.search(r'^COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)'%d['c'],txt,re.M)
        date,url=mc.groups(); rec_extra['comment_id']=d['c']
    n+=1
    th=d['th'].split(',') if isinstance(d['th'],str) else d['th']
    if d.get('r') and 'restricted' not in th: th.append('restricted')
    rec={'id':'tb20-%04d'%n,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':d['sp'],'stage':d['st'],'type':d['ty'],'themes':th,'quote':d['q'],'context':d['cx'],'raw_file':rf,'source_class':'reddit_archive','post_id':pid}
    rec.update(rec_extra)
    if len(d['cx'].split())>25: print('LONG CONTEXT',n,file=sys.stderr)
    out.append(rec)
with open(os.path.join(root,'voice','reddit-tr20.jsonl'),'w') as f:
    for r in out: f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(out))
