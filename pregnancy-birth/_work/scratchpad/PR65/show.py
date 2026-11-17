import sys
rows=[l.rstrip('\n').split('\t') for l in open('scratchpad/PR65/units.tsv')]
a,b=int(sys.argv[1]),int(sys.argv[2])
for i in range(a,min(b,len(rows))):
    print(f'\n######## U{i} {rows[i][1]}')
    print(open(rows[i][1]).read())
