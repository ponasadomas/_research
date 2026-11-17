import sys,re
C="/home/thinkpad/GitHub/ads/mamivio.com/research/toddler-behaviour/_raw/reddit/filter-v1/wave3/cards/"
f,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
n=int(sys.argv[4]) if len(sys.argv)>4 else 230
t=[x for x in re.split(r"(?m)^(?=ID \S+ \| r/)",open(C+f).read()) if x.startswith("ID ")]
for x in t[a:b]:
    L=x.strip().split("\n")
    i=L[0].split()[1]; sf=L[0].split("safety_flag=")[1][0]
    o=" ".join(L[2:]).split("MATCHES:")[0][9:n]
    print(i,sf,"|",L[1][6:],"|",o)
