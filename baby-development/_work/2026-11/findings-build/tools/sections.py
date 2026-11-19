import re,os,json
D=os.path.expanduser('~/GitHub/_research/baby-development/findings/2026-11/patterns')
def load():
    out={}
    for n in range(13):
        k=f"{n:02d}"; part=None; heads=[]; cur=None
        title=None
        for l in open(f"{D}/pattern-{k}.md",encoding='utf-8'):
            l=l.rstrip('\n')
            if l.startswith('# ') and title is None: title=l[2:]
            if re.match(r'^## ',l):
                part=l[3:].strip(); heads.append({'level':2,'part':part,'head':part}); cur=None
            elif re.match(r'^### ',l):
                cur={'level':3,'part':part,'head':l[4:].strip(),'n':None,'m':None,'ids':[]}; heads.append(cur)
            elif cur is not None:
                m=re.match(r'^(\d[\d,]*) of ([\d,]+) posts\.',l)
                if m and cur['n'] is None: cur['n']=int(m.group(1).replace(',','')); cur['m']=int(m.group(2).replace(',',''))
                cur['ids']+=re.findall(r'\[(sr\d+-\d+)\]',l)
        out[k]={'title':title,'heads':heads}
    return out
if __name__=='__main__':
    s=load()
    for k,v in s.items():
        on=[h for h in v['heads'] if h['level']==3 and h['part']=='On-niche posts']
        ne=[h for h in v['heads'] if h['level']==3 and h['part']=='Near posts']
        ac=[h for h in v['heads'] if h['level']==3 and h['part']=='Across the on-niche posts']
        print(k,v['title'][:60],'| on',len(on),sum(h['n'] for h in on),set(h['m'] for h in on),'| near',len(ne),sum(h['n'] for h in ne),set(h['m'] for h in ne),'| across',[(h['n']) for h in ac], '| parts',[h['head'] for h in v['heads'] if h['level']==2])
        dup=[h['head'] for h in v['heads'] if h['level']==3]
        d=set(x for x in dup if dup.count(x)>1)
        if d: print('   DUP',d)
    print(sum(1 for v in s.values() for h in v['heads']))
