import json,sys,re,collections
for f in sys.argv[1:]:
    s=open(f).read()
    # unescape layers
    for _ in range(3):
        s=s.replace('\\/','/').replace('\\"','"')
    c=collections.Counter()
    for m in re.finditer(r'"link_url":"([^"]+)"',s):
        c[m.group(1)]+=1
    names=collections.Counter(re.findall(r'"page_name":"([^"]+)"',s))
    print("==",f.split('/')[-1][:60]); 
    for u,n in c.most_common(12): print(" ",n,u[:150])
    for u,n in names.most_common(15): print("   page:",n,u)
