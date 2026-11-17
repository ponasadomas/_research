import json,re,sys
U='../_shared/_raw/reddit-2026/units/'
out=[];n=0;R=[]
for line in open('scratchpad/DR05/q.jsonl',encoding='utf-8'):
    if not line.strip(): continue
    q=json.loads(line)
    path=U+q['u']+'.txt'
    txt=open(path,encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    rec={}
    n+=1
    rec['id']='dv05-%04d'%n
    rec['source']='reddit r/'+sub
    if q.get('c'):
        cm=re.search(r'COMMENT '+q['c']+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
        if not cm: sys.exit('no comment '+q['c'])
        date,url=cm.groups()
    rec['url']=url;rec['date']=date
    rec['speaker']=q['sp'];rec['stage']=q['st'];rec['type']=q['ty'];rec['themes']=q['th']
    rec['quote']=q['q'];rec['context']=q['cx'];rec['raw_file']=path
    rec['source_class']='reddit_archive';rec['post_id']=pid
    if q.get('c'): rec['comment_id']=q['c']
    if q.get('seg'): rec['segment']=q['seg']
    if q.get('r'): R.append(rec['id'])
    if len(q['cx'].split())>25: print('long ctx',rec['id'])
    out.append(rec)
with open('voice/reddit-dr05.jsonl','w',encoding='utf-8') as f:
    for r in out: f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(out),'restricted',len(R),', '.join(R))
