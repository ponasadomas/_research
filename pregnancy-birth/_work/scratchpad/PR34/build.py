import json,re,sys
units=[l.rstrip('\n').split('\t')[1] for l in open('scratchpad/PR34/units.txt')]
def meta(u,c):
    t=open(units[u]).read()
    if c:
        m=re.search(r'^COMMENT '+c+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',t,re.M)
    else:
        m=re.search(r'^POST \S+ \| [^|]*\| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',t,re.M)
    assert m,(u,c)
    sub=re.search(r'^POST (\S+) \| r/(\S+)',t,re.M)
    return m.group(1),m.group(2),sub.group(1),sub.group(2)
out=open('voice/reddit-pr34.jsonl','w'); restricted=[]
n=0
for f in sorted(__import__('glob').glob('scratchpad/PR34/stage-*.jsonl')):
  for line in open(f):
    if not line.strip(): continue
    s=json.loads(line); n+=1
    d,url,pid,sub=meta(s['u'],s.get('c'))
    rid='pb34-%04d'%n
    rec={'id':rid,'source':'reddit r/'+sub,'url':url,'date':d,'speaker':s['sp'],'stage':s['st'],'type':s['ty'],'themes':s['th'],'quote':s['q'],'context':s['cx'],'raw_file':units[s['u']],'source_class':'reddit_archive','post_id':pid}
    if s.get('c'): rec['comment_id']=s['c']
    if s.get('r'): restricted.append(rid)
    out.write(json.dumps(rec,ensure_ascii=False)+'\n')
open('scratchpad/PR34/restricted.txt','w').write(', '.join(restricted))
print(n,'records;',len(restricted),'restricted')
