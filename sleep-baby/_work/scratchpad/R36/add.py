import json,sys,re,os
base='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/'
out=base+'voice/reddit-r36.jsonl'
n=0
if os.path.exists(out):
    n=sum(1 for _ in open(out))
recs=[json.loads(l) for l in open(sys.argv[1]) if l.strip()]
outl=[]
if True:
    for r in recs:
        raw='../_shared/_raw/reddit-2026/units/%s.txt'%r['u']
        txt=open(base+raw).read()
        sub,pid=r['u'].rsplit('-',1)
        c=r.get('c')
        if c:
            m=re.search(r'^COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)'%c,txt,re.M)
        else:
            m=re.search(r'^POST %s \| r/\S+ \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)'%pid,txt,re.M)
        assert m,(r['u'],c)
        q=r['q']
        for part in q.split(' […] '):
            assert part in txt,(r['u'],part[:60])
        n+=1
        d={'id':'sb36-%04d'%n,'source':'reddit r/'+sub,'url':m.group(2),'date':m.group(1),
           'speaker':r['sp'],'stage':r['st'],'type':r['ty'],'themes':r['th'],'quote':q,
           'context':r['cx'],'raw_file':raw,'source_class':'reddit_archive','post_id':pid}
        if c: d['comment_id']=c
        assert len(d['context'].split())<=25,d['context']
        outl.append(json.dumps(d,ensure_ascii=False)+'\n')
        print(d['id'],r['u'],c or '')
open(out,'a').write(''.join(outl))
