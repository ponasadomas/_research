import json,sys,re,os
# usage: add.py staging.jsonl  -> appends to voice file
units=[l.rstrip('\n').split('\t')[1] for l in open('scratchpad/PR33/units.tsv')]
vf='voice/reddit-pr33.jsonl'
n=0
if os.path.exists(vf):
    n=sum(1 for l in open(vf) if l.strip())
out=open(vf,'a')
for line in open(sys.argv[1]):
    if not line.strip(): continue
    r=json.loads(line)
    u=units[r.pop('n')-1]
    txt=open(u,encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d)',txt)
    pid,sub,pdate=m.groups()
    cid=r.pop('cid','')
    if cid:
        mm=re.search(r'COMMENT '+cid+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
        date,url=mm.groups()
    else:
        date=pdate; url=re.search(r'\| (https://\S+)',txt.split('\n')[0]).group(1)
    n+=1
    rec={'id':'pb33-%04d'%n,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':r['speaker'],'stage':r['stage'],'type':r['type'],'themes':r['themes'],'quote':r['quote'],'context':r['context'],'raw_file':u,'source_class':'reddit_archive','post_id':pid}
    if cid: rec['comment_id']=cid
    if r.get('restricted'): open('scratchpad/PR33/restricted.txt','a').write(rec['id']+'\n')
    out.write(json.dumps(rec,ensure_ascii=False)+'\n')
print('total',n)
