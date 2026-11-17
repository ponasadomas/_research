import sys
lines=[l.rstrip('\n').split('\t') for l in open('scratchpad/PR34/units.txt')]
a,b=int(sys.argv[1]),int(sys.argv[2])
for i in range(a,min(b,len(lines))):
    print(f"\n######## U{i} {lines[i][1].split('/')[-1]}")
    print(open(lines[i][1]).read())
