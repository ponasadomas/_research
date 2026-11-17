# usage: python3 -I add.py batchfile.tsv-like json lines
# each input line: {"u":"pregnant-1shl25r","c":"ofdv1c5"(opt),"sp":..,"st":..,"ty":..,"th":[..],"q":..,"cx":..,"r":true(opt)}
import json,sys,re,os,html
B='/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/'
V=B+'voice/reddit-pr50.jsonl'; R=B+'scratchpad/PR50/restricted.txt'
n=sum(1 for l in open(V) if l.strip()) if os.path.exists(V) else 0
def norm(s): return re.sub(r'\s+',' ',html.unescape(s).replace('\\n',' ')).strip()
recs=[]
for line in open(sys.argv[1]):
    if not line.strip(): continue
    d=json.loads(line)
    rawp='../_shared/_raw/reddit-2026/units/%s.txt'%d['u']
    txt=open(B+rawp,encoding='utf-8').read()
    sub,pid=d['u'].rsplit('-',1)
    if d.get('c'):
        m=re.search(r'COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)'%d['c'],txt)
    else:
        m=re.search(r'POST %s \| r/\S+ \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)'%pid,txt)
    assert m,(d['u'],d.get('c'))
    nt=norm(txt)
    pos=0
    for piece in d['q'].split(' […] '):
        i=nt.find(norm(piece),pos)
        assert i>=0,('QUOTE NOT FOUND',d['u'],piece[:60])
        pos=i+len(norm(piece))
    assert len(d['cx'].split())<=25,('ctx long',d['cx'])
    n+=1; iid='pb50-%04d'%n
    rec={"id":iid,"source":"reddit r/"+sub,"url":m.group(2),"date":m.group(1),"speaker":d['sp'],"stage":d['st'],"type":d['ty'],"themes":d['th'],"quote":d['q'],"context":d['cx'],"raw_file":rawp,"source_class":"reddit_archive","post_id":pid}
    if d.get('c'): rec['comment_id']=d['c']
    recs.append((rec,d.get('r')))
out=open(V,'a'); rf=open(R,'a')
for rec,r in recs:
    out.write(json.dumps(rec,ensure_ascii=False)+'\n')
    if r: rf.write(rec['id']+'\n')
    print(rec['id'],rec['post_id'],rec['type'])
