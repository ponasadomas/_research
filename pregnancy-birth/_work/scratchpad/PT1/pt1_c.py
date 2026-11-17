import sys,re
t=open(sys.argv[1]).read()
for b in t.split('\n\nID '):
    b=b if b.startswith('ID ') else 'ID '+b
    m=re.match(r'ID (\S+) \| r/(\S+) \| (\S+) \| safety_flag=(\w+)\nTITLE: (.*)\nOPENING: (.*)',b,re.S)
    if not m: print("??",b[:100]);continue
    i,s,d,f,ti,o=m.groups()
    o=re.sub(r'\s+',' ',o.split('\nMATCHES')[0])[:int(sys.argv[2])]
    print(f"{i}{'*' if f=='True' else ''}|{ti[:90]}|{o}")
