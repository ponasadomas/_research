import sys,re
t=open(sys.argv[1]).read()
for b in re.split(r'\n(?=ID )',t):
    m=re.match(r'ID (\S+) \| r/(\S+) \| (\S+) \| safety_flag=(\w+)\nTITLE: (.*)\nOPENING: (.*?)(?:\nMATCHES:.*)?$',b.strip(),re.S)
    if not m: print("??",b[:100].replace("\n"," ")); continue
    i,s,d,sf,ti,op=m.groups()
    op=re.sub(r'\s+',' ',op)[:230]
    print(f"{i}{' S' if sf=='True' else ''}|{ti[:90]}|{op}")
