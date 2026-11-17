import json,re,sys,html
B='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/'
f=B+'voice/reddit-r35.jsonl'
ids=set(sys.argv[1:])
def canon(s): return s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('\\_','_')
out=[]
for l in open(f):
    r=json.loads(l)
    if r['id'] in ids:
        raw=open(B+r['raw_file']).read()
        raw=re.sub(r'\s+',' ',raw)
        pieces=r['quote'].split(' […] ')
        new=[]
        for p in pieces:
            p=re.sub(r'\s+',' ',p)
            # build regex: each char canon-compared
            cr=canon(raw); cp=canon(p)
            i=cr.find(cp)
            if i<0:
                # try escaped underscores in raw
                print('MISS',r['id'],p[:60]); new.append(p); continue
            # map back: canon only changes \\_ -> _ (length change), so do via regex on raw
            pat=''.join('(?:\\\\_|_)' if c=='_' else ("['’‘]" if c=="'" else ('["“”]' if c=='"' else re.escape(c))) for c in cp)
            m=re.search(pat,raw)
            new.append(m.group(0))
        r['quote']=' […] '.join(new)
    out.append(json.dumps(r,ensure_ascii=False))
open(f,'w').write('\n'.join(out)+'\n')
