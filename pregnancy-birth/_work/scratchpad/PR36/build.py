import json,re,sys
base='/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/'
units=[l.rstrip('\n').split('\t')[1] for l in open(base+'scratchpad/PR36/units.tsv')]
out=[];restricted=[]
for i,l in enumerate(open(base+'scratchpad/PR36/picks.jsonl'),1):
    p=json.loads(l)
    u=units[p['u']-1]
    t=open(base+u,encoding='utf-8').read()
    m=re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',t)
    pid,sub,date,url=m.groups()
    rec={'id':'pb36-%04d'%i,'source':'reddit r/'+sub}
    if p['c']:
        cm=re.search(r'COMMENT '+p['c']+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',t)
        date,url=cm.groups()
    rec.update(url=url,date=date,speaker=p['sp'],stage=p['st'],type=p['ty'],themes=p['th'],quote=p['q'],context=p['cx'],raw_file=u,source_class='reddit_archive',post_id=pid)
    if p['c']: rec['comment_id']=p['c']
    if len(p['cx'].split())>25: print('long ctx',rec['id'],file=sys.stderr)
    if p.get('r'): restricted.append(rec['id'])
    out.append(rec)
with open(base+'voice/reddit-pr36.jsonl','w',encoding='utf-8') as f:
    for r in out: f.write(json.dumps(r,ensure_ascii=False)+'\n')
open(base+'scratchpad/PR36/restricted.txt','w').write('\n'.join(restricted)+'\n')
print(len(out),'restricted',len(restricted))
