import json,re,sys,os
B=os.path.dirname(os.path.abspath(__file__)); NICHE=os.path.join(B,'..','..')
units=[l.strip() for l in open(os.path.join(B,'units.txt')) if l.strip()]
bymap={os.path.basename(u)[:-4]:u for u in units}
out=[];n=0
for f in sorted(x for x in os.listdir(B) if x.startswith('rec-') and x.endswith('.jsonl')):
    for line in open(os.path.join(B,f)):
        if not line.strip(): continue
        r=json.loads(line); u=bymap[r['u']]; txt=open(os.path.join(NICHE,u),encoding='utf-8').read()
        sub,pid=r['u'].split('-',1)
        if r.get('c'):
            m=re.search(r'COMMENT '+r['c']+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
        else:
            m=re.search(r'POST '+pid+r' \| [^|]*\| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
        assert m,(r['u'],r.get('c'))
        n+=1
        d={'id':'sb16-%04d'%n,'source':'reddit r/'+sub,'url':m.group(2),'date':m.group(1),'speaker':r['sp'],'stage':r['st'],'type':r['ty'],'themes':r['th'],'quote':r['q'],'context':r['cx'],'raw_file':u,'source_class':'reddit_archive','post_id':pid}
        if r.get('c'): d['comment_id']=r['c']
        assert len(r['cx'].split())<=25,(n,r['cx'])
        out.append(d)
with open(os.path.join(NICHE,'voice','reddit-r16.jsonl'),'w') as fo:
    for d in out: fo.write(json.dumps(d,ensure_ascii=False)+'\n')
print(len(out))
