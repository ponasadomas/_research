import json,re,sys,os,glob
B=os.path.dirname(os.path.abspath(__file__)); NB=os.path.abspath(os.path.join(B,'..','..'))
units=dict()
for l in open(os.path.join(B,'units.tsv')):
    c,u=l.strip().split('\t'); units[os.path.basename(u)[:-4]]=u
recs=[]
for f in sorted(glob.glob(os.path.join(B,'draft*.jsonl'))):
    for i,l in enumerate(open(f),1):
        if not l.strip(): continue
        try: d=json.loads(l)
        except Exception as e: sys.exit(f'{f}:{i} {e}')
        u=units[d['u']]; txt=open(os.path.join(NB,u),encoding='utf-8').read()
        m=re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)',txt)
        pid,sub,date,url=m.groups()
        r={'id':None,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':d['sp'],'stage':d['st'],'type':d['ty'],'themes':d['th'],'quote':d['q'],'context':d['cx'],'raw_file':u,'source_class':'reddit_archive','post_id':pid}
        if d.get('c'):
            m2=re.search(r'COMMENT '+d['c']+r' \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)',txt)
            if not m2: sys.exit('no comment '+d['c'])
            r['date'],r['url']=m2.groups(); r['comment_id']=d['c']
        r['_r']=d.get('r','')
        if len(d['cx'].split())>25: print('LONG CONTEXT',d['q'][:40])
        recs.append(r)
out=os.path.join(NB,'voice','reddit-pr38.jsonl')
restr=[]
with open(out,'w') as fo:
    for n,r in enumerate(recs,1):
        r['id']='pb38-%04d'%n; rr=r.pop('_r')
        if rr: restr.append((r['id'],rr))
        fo.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(recs),'written')
open(os.path.join(B,'restricted.tsv'),'w').write(''.join(a+'\t'+b+'\n' for a,b in restr))
print(len(restr),'restricted')
