import sys,re
t=open('/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-mother/_raw/reddit/filter-v1/wave2/cards/'+sys.argv[1]).read()
cards=re.split(r'\n(?=ID )',t.strip())
a,b=int(sys.argv[2]),int(sys.argv[3])
print(len(cards))
for c in cards[a:b]:
    m=re.match(r'ID (\S+) \| r/\S+ \| (\S+) \| safety_flag=(\w+)\nTITLE: (.*)\nOPENING: (.*?)\nMATCHES: (.*)',c,re.S)
    if not m: print('??',c[:200]);continue
    i,d,s,ti,op,ma=m.groups()
    top=re.search(r'"topic": "([^"]*)"',ma)
    print(i,'S' if s=='True' else '','|',ti[:110],'|',re.sub(r'\s+',' ',op)[:270],'| T:',top.group(1) if top else '')
