# usage: python3 -I add.py spec.jsonl   (run with cwd = sleep-mother folder)
# spec line: {"u":N,"c":"commentid or null","sp":..,"st":..,"ty":..,"th":[..],"q":..,"cx":..,"r":0/1}
import json,sys,re,os
base='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-mother/'
units=[l.rstrip('\n').split('\t') for l in open(base+'scratchpad/MR06/units.tsv')]
vf=base+'voice/reddit-mr06.jsonl'
rf=base+'scratchpad/MR06/restricted.txt'
n=0
if os.path.exists(vf): n=sum(1 for l in open(vf) if l.strip())
out=open(vf,'a'); rr=open(rf,'a')
for line in open(sys.argv[1]):
    if not line.strip(): continue
    s=json.loads(line)
    path=units[s['u']-1][1]
    txt=open(base+path,encoding='utf-8').read()
    m=re.search(r'^POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt,re.M)
    pid,sub,date,url=m.groups()
    c=s.get('c')
    rec={}
    if c:
        mc=re.search(r'^COMMENT '+c+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt,re.M)
        date,url=mc.groups()
    n+=1
    rid='sm06-%04d'%n
    rec={'id':rid,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':s['sp'],'stage':s['st'],'type':s['ty'],'themes':s['th'],'quote':s['q'],'context':s['cx'],'raw_file':path,'source_class':'reddit_archive','post_id':pid}
    if c: rec['comment_id']=c
    assert len(s['cx'].split())<=25, rid
    out.write(json.dumps(rec,ensure_ascii=False)+'\n')
    if s.get('r'): rr.write(rid+'\t'+s['r'] if isinstance(s['r'],str) else rid+'\n'); rr.write('\n') if isinstance(s['r'],str) else None
    print(rid, s['u'], c or '')
