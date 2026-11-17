import json,re,sys,os,glob,html
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
U='../_shared/_raw/reddit-2026/units/'
out=[];n=0;restr=[]
def norm(s): return re.sub(r'\s+',' ',html.unescape(s)).strip()
fails=0
for f in sorted(glob.glob('scratchpad/R59/b*.jsonl')):
  for line in open(f):
    if not line.strip(): continue
    e=json.loads(line)
    path=U+e['u']+'.txt'
    txt=open(path,encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    rec={}
    if e.get('c'):
      cm=re.search(r'COMMENT '+e['c']+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
      date,url=cm.groups()
    if norm(e['q'].split(' […] ')[0]) not in norm(txt): print('FAIL',f,e['q'][:60]); fails+=1
    n+=1
    rec={'id':'sb59-%04d'%n,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':e['sp'],'stage':e['st'],'type':e['ty'],'themes':e['th'],'quote':e['q'],'context':e['cx'],'raw_file':path,'source_class':'reddit_archive','post_id':pid}
    if e.get('c'): rec['comment_id']=e['c']
    if len(e['cx'].split())>25: print('LONGCX',rec['id'])
    out.append(rec)
    if e.get('r'): restr.append((rec['id'],e['r']))
with open('voice/reddit-r59.jsonl','w') as fo:
  for r in out: fo.write(json.dumps(r,ensure_ascii=False)+'\n')
print(n,'records',fails,'quick-fails')
open('scratchpad/R59/restricted.txt','w').write(''.join(f'- {i} ({r})\n' for i,r in restr))
print(len(restr),'restricted')
