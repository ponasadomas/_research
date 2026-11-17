# usage: python3 -I check.py bNN.json -> reports quotes not found in unit text, and comment ids missing
import json,sys,re,html
B='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/'
units=[l.rstrip('\n').split('\t')[1] for l in open(B+'scratchpad/R53/units.tsv')]
def norm(s): return re.sub(r'\s+',' ',html.unescape(s).replace('\\n',' ')).strip()
bad=0
for k,rec in enumerate(json.load(open(sys.argv[1]))):
    u,cid=rec[0],rec[1]; t=open(B+units[u-1],encoding='utf-8').read(); nt=norm(t)
    if cid and ('COMMENT '+cid) not in t: print(k,'no comment',cid); bad+=1
    pos=0
    for p in rec[6].split(' […] '):
        i=nt.find(norm(p),pos)
        if i<0: print(k,'NOTFOUND u',u,repr(p[:80])); bad+=1; break
        pos=i+len(norm(p))
    if len(rec[7].split())>25: print(k,'context long')
print('recs',k+1,'bad',bad)
