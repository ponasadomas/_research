# usage: python3 -I add.py batchfile.py  (batch = list of dicts with u, c(optional), speaker, stage, type, themes, quote, context)
import json, re, sys, os
NICHE='/home/thinkpad/GitHub/ads/mamivio.com/research/toddler-behaviour'
OUT=NICHE+'/voice/reddit-tr02.jsonl'
recs=eval(open(sys.argv[1]).read())
existing=[json.loads(l) for l in open(OUT)] if os.path.exists(OUT) else []
n=len(existing)
with open(OUT,'a') as f:
    for r in recs:
        raw=f"../_shared/_raw/reddit-2026/units/{r['u']}.txt"
        text=open(os.path.join(NICHE,raw)).read()
        sub,pid=r['u'].rsplit('-',1)
        m=re.search(r'^POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)',text,re.M)
        url,date=m.group(4),m.group(3)
        rec={}
        if r.get('c'):
            mc=re.search(r'^COMMENT '+r['c']+r' \| (\d{4}-\d\d-\d\d) .*?\| (\S+)',text,re.M)
            url,date=mc.group(2),mc.group(1)
        n+=1
        rec=dict(id=f"tb02-{n:04d}",source=f"reddit r/{m.group(2)}",url=url,date=date,speaker=r['speaker'],stage=r['stage'],type=r['type'],themes=r['themes'],quote=r['quote'],context=r['context'],raw_file=raw,source_class="reddit_archive",post_id=pid)
        if r.get('c'): rec['comment_id']=r['c']
        assert len(rec['context'].split())<=25, rec['context']
        f.write(json.dumps(rec,ensure_ascii=False)+'\n')
        print(rec['id'], r['u'], r.get('c',''))
