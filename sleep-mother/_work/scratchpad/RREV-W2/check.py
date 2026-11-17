import json,glob,re
recs=[]
for n in (4,5,6): recs+=[json.loads(l)['id'] for l in open(f'voice/reddit-mr0{n}.jsonl')]
lab={}
for f in sorted(glob.glob('scratchpad/RREV-W2/b[0-9].txt')):
    for line in open(f):
        line=line.rstrip('\n')
        if line.startswith('N '):
            _,pre,*rs=line.split()
            for r in rs:
                a,_,b=r.partition('-'); a=int(a); b=int(b or a)
                for k in range(a,b+1):
                    i=f'{pre}-{k:04d}'
                    assert i not in lab,('dup',i); lab[i]=('false','')
        elif line.startswith('R '):
            _,i,reason=line.split(' ',2)
            assert i not in lab,('dup',i); assert len(reason.split())<=12,i; lab[i]=('true',reason)
miss=[i for i in recs if i not in lab]; extra=[i for i in lab if i not in set(recs)]
print(len(recs),len(lab),'missing',miss,'extra',extra)
if not miss and not extra:
    with open('synthesis/restricted-review-mr04-mr06.tsv','w') as o:
        o.write('id\trestricted\treason\n')
        for i in recs: o.write(f'{i}\t{lab[i][0]}\t{lab[i][1]}\n')
    for n in (4,5,6):
        before=set(open(f'scratchpad/RREV-W2/before{n}.txt').read().split())
        ids=[i for i in recs if i.startswith(f'sm0{n}-')]
        after={i for i in ids if lab[i][0]=='true'}
        print(n,len(ids),len(before),len(after),'newly restricted',sorted(after-before))
        open(f'scratchpad/RREV-W2/rel{n}.txt','w').write('\n'.join(sorted(before-after)))
