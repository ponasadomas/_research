# usage: python3 -I build.py <nicheroot>  ; reads scratchpad/PR20/draft-*.py (each defines Q = list of tuples)
import json,os,re,sys,glob
root=sys.argv[1]; os.chdir(root)
paths={os.path.basename(l.split('\t')[1])[:-4]:l.split('\t')[1] for l in open('scratchpad/PR20/units.txt')}
recs=[];restricted=[]
for f in sorted(glob.glob('scratchpad/PR20/draft-*.py')):
    ns={}; exec(open(f).read(),ns)
    for t in ns['Q']:
        unit,cid,speaker,stage,typ,themes,quote,context,r=t
        p=paths[unit]; txt=open(p,encoding='utf-8').read()
        m=re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)',txt)
        pid,sub,date,url=m.groups()
        if cid:
            mm=re.search(r'COMMENT '+cid+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt); date,url=mm.groups()
        n=len(recs)+1; id='pb20-%04d'%n
        assert len(context.split())<=25, (id,context)
        d={"id":id,"source":"reddit r/"+sub,"url":url,"date":date,"speaker":speaker,"stage":stage,"type":typ,"themes":themes,"quote":quote,"context":context,"raw_file":p,"source_class":"reddit_archive","post_id":pid}
        if cid: d["comment_id"]=cid
        recs.append(d)
        if r: restricted.append((id,r))
with open('voice/reddit-pr20.jsonl','w',encoding='utf-8') as o:
    for d in recs: o.write(json.dumps(d,ensure_ascii=False)+'\n')
with open('scratchpad/PR20/restricted.tsv','w') as o:
    for i,r in restricted: o.write(i+'\t'+r+'\n')
print(len(recs),'records',len(restricted),'restricted')
