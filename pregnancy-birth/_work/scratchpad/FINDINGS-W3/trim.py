import sys,re
skip=False
for l in open(sys.argv[1]):
    if l.startswith('#'):
        skip=bool(re.search(r'(?i)jargon|new them|theme tag|new tags|tags used|products and services|products named',l))
    if not skip: sys.stdout.write(l)
