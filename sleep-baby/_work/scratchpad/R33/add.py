import json,sys,re,os
V='voice/reddit-r33.jsonl'
units=[l.split('\t')[1].strip() for l in open('scratchpad/R33/units.tsv')]
def find(u):
    m=[x for x in units if x.endswith('-'+u+'.txt')]
    assert len(m)==1,u
    return m[0]
n=sum(1 for l in open(V)) if os.path.exists(V) else 0
recs=json.load(open(sys.argv[1]))
out=open(V,'a')
for r in recs:
    rf=find(r['u']); txt=open(rf,encoding='utf-8').read()
    h=txt.split('\n',1)[0]
    m=re.match(r'POST (\w+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*\| (https\S+)',h)
    pid,sub,date,url=m.groups()
    rec={}
    c=r.get('c')
    if c:
        cm=re.search(r'COMMENT '+c+r' \| (\d{4}-\d\d-\d\d) \S+ UTC \| (https\S+)',txt)
        date,url=cm.groups()
    n+=1
    rec=dict(id='sb33-%04d'%n,source='reddit r/'+sub,url=url,date=date,speaker=r['sp'],stage=r['st'],type=r['ty'],themes=r['th'],quote=r['q'],context=r['cx'],raw_file=rf,source_class='reddit_archive',post_id=pid)
    if c: rec['comment_id']=c
    if r.get('restricted'): pass
    out.write(json.dumps(rec,ensure_ascii=False)+'\n')
    print(rec['id'],r['u'],r.get('restricted',''))
