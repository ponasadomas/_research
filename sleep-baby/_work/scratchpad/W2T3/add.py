# usage: add.py < spec ; spec lines: "label: reason | id id id"
import sys
m={'c':'keep_core','p':'keep_purchase','s':'keep_success','o':'keep_otherside','d':'drop'}
out=open('labels.tsv','a')
for l in sys.stdin:
    l=l.strip()
    if not l: continue
    a,b=l.split('|'); lab,reason=a.split(':',1)
    for i in b.split(): out.write(f"{i}\t{m[lab.strip()]}\t{reason.strip()}\n")
