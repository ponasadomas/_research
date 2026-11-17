import json,sys,re,os
BASE='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby'
VOICE=BASE+'/voice/reddit-r32.jsonl'
units={os.path.basename(l.split('\t')[1].strip()):l.split('\t')[1].strip() for l in open(BASE+'/scratchpad/R32/units.txt')}
n=sum(1 for l in open(VOICE) if l.strip()) if os.path.exists(VOICE) else 0
out=open(VOICE,'a')
for rec in json.load(open(sys.argv[1])):
    u=rec['u']; 
    if not u.endswith('.txt'): u+='.txt'
    rf=units[u]; text=open(os.path.join(BASE,rf)).read()
    m=re.search(r'^POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)',text,re.M)
    pid,sub,date,url=m.groups()
    r={}
    if rec.get('c'):
        cm=re.search(r'^COMMENT '+rec['c']+r' \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)',text,re.M)
        date,url=cm.groups()
    n+=1
    r={'id':'sb32-%04d'%n,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':rec['sp'],'stage':rec['st'],'type':rec['ty'],'themes':rec['th'],'quote':rec['q'],'context':rec['cx'],'raw_file':rf,'source_class':'reddit_archive','post_id':pid}
    if rec.get('c'): r['comment_id']=rec['c']
    if len(rec['cx'].split())>25: print('LONG CONTEXT',r['id'])
    out.write(json.dumps(r,ensure_ascii=False)+'\n')
print('total',n)
