# Build voice file from scratch/q*.jsonl (compact records). Run from sleep-baby folder with python3 -I.
import json, re, glob, sys, os
os.chdir(sys.argv[1])
U='../_shared/_raw/reddit-2026/units/'
out=[]; n=0
for f in sorted(glob.glob('scratchpad/R24/q*.jsonl')):
    for line in open(f):
        if not line.strip(): continue
        r=json.loads(line)
        raw=U+r['u']+'.txt'
        txt=open(raw).read()
        m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)',txt)
        pid,sub,date,url=m.groups()
        rec={}
        if r.get('c'):
            mc=re.search(r'COMMENT '+r['c']+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
            date,url=mc.groups()
        n+=1
        rec={'id':'sb24-%04d'%n,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':r['sp'],'stage':r['st'],'type':r['ty'],'themes':r['th'],'quote':r['q'],'context':r['cx'],'raw_file':raw,'source_class':'reddit_archive','post_id':pid}
        if r.get('c'): rec['comment_id']=r['c']
        if len(r['cx'].split())>25: print('LONG CONTEXT',rec['id'])
        if r.get('R'): print('RESTRICT',rec['id'],r['R'])
        out.append(rec)
with open('voice/reddit-r24.jsonl','w') as w:
    for rec in out: w.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(n)
