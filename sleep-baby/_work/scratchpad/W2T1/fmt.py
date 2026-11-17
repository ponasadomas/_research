import sys,re,json
subs={}
def sl(sub,i):
    if sub not in subs:
        subs[sub]={}
        for l in open(f'../../../_shared/_raw/reddit-2026/{sub}.posts.jsonl'):
            d=json.loads(l); t=(d.get('selftext') or '')
            subs[sub][d['id']]=(len(t),len(re.findall(r'sleep|nap|night|bedtime|wak',t,re.I)))
    return subs[sub].get(i,(0,0))
for f in sys.argv[1:]:
    sub=re.match(r'A-(.*)-\d+\.txt',f).group(1)
    t=open('../../_raw/reddit/filter-v1/wave2/cards/'+f).read()
    for c in t.strip().split('\n\nID '):
        c=c if c.startswith('ID ') else 'ID '+c
        m=re.match(r'ID (\S+) \| r/(\S+) \| (\S+) \| safety_flag=(\w+)\nTITLE: (.*)\nOPENING: (.*?)\nMATCHES:',c,re.S)
        if not m: print('??',c[:200]);continue
        i,s,d,sf,ti,op=m.groups()
        op=' '.join(op.split())[:200]
        L,n=sl(sub,i)
        print(f"{i}|{'S' if sf=='True' else ''}|{n}/{L}|{ti[:100]}|{op}")
