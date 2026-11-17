import sys,re
base='/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/_raw/reddit/filter-v1/wave2/cards/'
t=open(base+sys.argv[1]).read()
cards=re.split(r'\n(?=ID )',t.strip())
for c in cards:
    m=re.match(r'ID (\S+) \| r/(\S+) \| (\S+) \| safety_flag=(\w+)',c)
    ti=re.search(r'TITLE: (.*)',c); 
    op=re.search(r'OPENING: (.*?)\nMATCHES:',c,re.S)
    o=re.sub(r'\s+',' ',op.group(1) if op else '')[:int(sys.argv[2])]
    print(m.group(1),'S' if m.group(4)=='True' else '', '|',ti.group(1)[:110] if ti else '','|',o)
