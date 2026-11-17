import sys,re
t=open(sys.argv[1]).read().split('\n\nID ')
for i,b in enumerate(t):
    if i==0 and b.startswith('ID '): b=b[3:]
    L=b.split('\n')
    h=L[0].split(' | ')
    rest=' '.join(L[1:])
    rest=re.sub(r'\s+',' ',rest)
    rest=re.sub(r'TITLE: ','T: ',rest); rest=re.sub(r' OPENING: ',' | ',rest)
    m=re.search(r'MATCHES: (.*)$',rest)
    rest=rest[:m.start()] if m else rest
    tp=re.search(r'"topic": "([^"]*)"',m.group(1)).group(1) if m else ''
    sf='' if 'False' in h[-1] else ' SAFE'
    print(h[0]+' '+h[1].replace('r/','')+sf+' ['+tp+'] '+rest.strip()[:330])
