# usage: python3 -I add.py batchfile.jsonl  -> appends to voice file, records restricted ids
import json,sys,re,os
B='/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/'
units={}
for l in open(B+'scratchpad/PR72/units.tsv'):
    n,c,p,s=l.rstrip('\n').split('\t'); units[int(n)]=p
V=B+'voice/reddit-pr72.jsonl'
n=sum(1 for l in open(V) if l.strip()) if os.path.exists(V) else 0
out=open(V,'a'); rf=open(B+'scratchpad/PR72/restricted.txt','a')
for line in open(sys.argv[1]):
    if not line.strip(): continue
    d=json.loads(line); p=units[d['u']]; txt=open(B+p,encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    rec={}
    if d.get('c'):
        mm=re.search(r'COMMENT '+d['c']+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
        date,url=mm.groups()
    n+=1; i='pb72-%04d'%n
    rec=dict(id=i,source='reddit r/'+sub,url=url,date=date,speaker=d['sp'],stage=d['st'],type=d['ty'],themes=d['th'],quote=d['q'],context=d['cx'],raw_file=p,source_class='reddit_archive',post_id=pid)
    if d.get('c'): rec['comment_id']=d['c']
    assert len(d['cx'].split())<=25, d['cx']
    out.write(json.dumps(rec,ensure_ascii=False)+'\n')
    if d.get('r'): rf.write(i+'\t'+str(d['u'])+'\n')
print('now',n)
