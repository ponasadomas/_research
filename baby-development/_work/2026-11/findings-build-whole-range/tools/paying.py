#!/usr/bin/env python3
"""paying.py -> sorts the 138 paid-for rows of counts.md into kinds (the sorting is the findings writer's) and asserts the sums used in spec/16-paying.md."""
import re,os,sys,collections
sys.path.insert(0,os.path.dirname(__file__))
from common import *
C=R+'/evidence/2026-11/birth-to-48-months/counts.md'
rows=[]; on=False
for l in open(C,encoding='utf-8'):
    if l.startswith('| Post | Main pattern | Paid for'): on=True; continue
    if on:
        m=re.match(r'^\| (\w+) \| (\d+) \| (.+?) \|\s*$',l)
        if m: rows.append((m.group(1),int(m.group(2)),m.group(3)))
        elif l.startswith('##'): break
assert len(rows)==138,len(rows)
KIND={
'toys':'1v0a00t 1syfa0b 1stwdcq 1tw2tlw 1txfdav 1vp86gd 1xa2o4i 1s9u6xq 1sa1po2 1sq7837 1tnv5k3 1tt1o27 1vvcp57 1w99cso 1wk5egr 1sahmuz 1tc7cep 1tq4v8j 1sdhgk5 1vgnfdw 1uo6p1n 1vqdhtk 1u0s32s 1vcw6dp 1w1g4jy 1sdvgqm 1wxj6ta',
'cups':'1t9jr8x 1sk8eaq 1t8bdde 1v6om42 1vbg9yk 1vlah1k 1vpkj7c 1vhcytr',
'gear':'1uvdd0d 1sg8rkl 1t6z8il 1ulwa8x 1utc9ap 1u5mdfq 1v011zp 1v0v9i4 1se4rlf 1scxsow 1szzunh 1umex3n 1utml2h 1uzc9mr 1vwj2mt 1w5zvfo 1wqrgm5 1sj2uyu 1wstnpg 1tgp9hl 1sl3bv6 1ttxang 1twzxvr 1vhudbo 1tsl3du 1ukihsy 1v9m4u8 1vd1t7t 1w2x1ky 1t0dkmu 1vog6tn 1wi39yz',
'potty':'1vnbfze 1u3w3ne 1uesojn 1vdl60h 1sjqkiq 1ske27r 1slqua3 1t16tpw 1t6okrj 1tzhur4 1u4dkk3 1uismo4 1uw44bz 1uzx284 1v80xf6 1vkn5a6 1vokss7 1vnb4tm 1wks1w5',
'food':'1wid3te 1xec7s4 1t34i6o 1twrn3v 1vdrv6h 1vblk0k 1vtpizp 1whgihn 1wme7tq 1x0ivhz 1txu747',
'childcare':'1wmqdvl 1ssrp39 1vut2ci 1txrtdi 1upo5ms 1szeyo6 1vfr9o3 1xcp64c 1uuwsin 1v4r5ha 1wtw7zd 1tdub2p',
'therapy_medical':'1skwjsb 1snng3h 1sq6dyu 1t9dvtx 1unn3ko 1wnhdy9 1sdo5dq 1tlfjf4',
'classes':'1spy2kt 1sor6cd 1t2jfgy 1t6go8r 1tnq632 1tv1ejo 1wd83fq',
'outings':'1v7m2m3 1sxiopq 1vplly1 1ut20r0 1sqne3v',
'information':'1v04way 1stoi7a 1uz6uk3 1t9cls0 1tczob6',
'other':'1ve5iiz 1ud5ceu 1wfutpp 1ugnrq0'}
kind={p:k for k,v in KIND.items() for p in v.split()}
assert len(kind)==138 and set(kind)==set(r[0] for r in rows), set(r[0] for r in rows)^set(kind)
P=posts()
c=collections.Counter(kind[r[0]] for r in rows); print(dict(c))
things=c['toys']+c['cups']+c['gear']+c['potty']+c['food']; person=c['childcare']+c['therapy_medical']+c['classes']+c['outings']
assert (things,c['gear'],c['toys'],c['potty'],c['food'],c['cups'],person,c['childcare'],c['therapy_medical'],c['classes'],c['outings'],c['information'],c['other'])==(97,32,27,19,11,8,32,12,8,7,5,5,4)
by=collections.Counter((P[r[0]]['reader'][:2],kind[r[0]]) for r in rows)
first=sum(1 for r in rows if P[r[0]]['reader'].startswith('sr')); second=138-first
pp=lambda rd:sum(by[(rd,k)] for k in('childcare','therapy_medical','classes','outings'))
cf=lambda rd:by[(rd,'cups')]+by[(rd,'food')]
print('first reading',first,'second',second,'| potty',by[('sr','potty')],by[('ar','potty')],'| person or place',pp('sr'),pp('ar'),'| cups+food',cf('sr'),cf('ar'))
assert (first,second,by[('sr','potty')],by[('ar','potty')],pp('sr'),pp('ar'),cf('sr'),cf('ar'))==(82,56,4,15,15,17,17,2)
# are the quotes of the Paying group from posts among the 138?
rec=records()
page=open(R+'/findings/what-hurts-and-what-she-wants.md',encoding='utf-8').read()
g=page.split('\n## Paying')[1].split('\n## ')[0]
for i in re.findall(r'\[([a-z]{2,}\d+-\d+)\]',g): print(i,rec[i]['post_id'],'in the 138' if rec[i]['post_id'] in kind else 'NOT in the 138',kind.get(rec[i]['post_id']),'|',P[rec[i]['post_id']]['paid'],P[rec[i]['post_id']]['paid_what'])
print('paying checks OK')
