import sys,re
t=open(sys.argv[1]+'.txt').read().split('\n\n')
for b in t:
    L=b.strip().split('\n')
    if not L or not L[0].startswith('ID'):continue
    m=re.match(r'ID (\S+) \| r/\S+ \| (\S+) \| safety_flag=(\w+)',L[0])
    ti=L[1][7:] if len(L)>1 else ''
    op=' '.join(l for l in L[2:] if not l.startswith('MATCHES')).replace('OPENING: ','')
    print(m.group(1),'S' if m.group(3)=='True' else '', '|',ti[:90],'|',op[:230])
