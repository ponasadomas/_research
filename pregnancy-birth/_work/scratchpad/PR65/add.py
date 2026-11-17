# usage: python3 add.py batchfile.jsonl  -> appends to voice file with ids
# batch line: {"u":N,"c":"commentid or ''","sp":..,"st":..,"ty":..,"th":[..],"q":..,"cx":..,"r":0/1}
import json,sys,re,os
rows=[l.rstrip('\n').split('\t') for l in open('scratchpad/PR65/units.tsv')]
VF='voice/reddit-pr65.jsonl'
n=sum(1 for l in open(VF)) if os.path.exists(VF) else 0
restr=open('scratchpad/PR65/restricted.txt','a')
out=open(VF,'a')
for line in open(sys.argv[1]):
    if not line.strip(): continue
    b=json.loads(line)
    path=rows[b['u']][1]; txt=open(path).read()
    m=re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    rec={}
    n+=1
    rec['id']=f'pb65-{n:04d}'
    rec['source']=f'reddit r/{sub}'
    if b.get('c'):
        cm=re.search(r'COMMENT '+b['c']+r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)',txt)
        rec['url']=cm.group(2); rec['date']=cm.group(1)
    else:
        rec['url']=url; rec['date']=date
    rec.update(speaker=b['sp'],stage=b['st'],type=b['ty'],themes=b['th'],quote=b['q'],context=b['cx'],raw_file=path,source_class='reddit_archive',post_id=pid)
    if b.get('c'): rec['comment_id']=b['c']
    if b.get('r'): restr.write(rec['id']+'\n')
    out.write(json.dumps(rec,ensure_ascii=False)+'\n')
    print(rec['id'], b['u'], rec['quote'][:50])
