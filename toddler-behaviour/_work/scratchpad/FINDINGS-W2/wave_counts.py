#!/usr/bin/env python3
"""Counts of quotes by wave (wave 1 = tb01-tb09, wave 2 = tb10-tb17) from voice-merged/all.jsonl.
Counts of quotes chosen by readers, never of people."""
import json,re,os,collections
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
recs=[json.loads(l) for l in open(os.path.join(ROOT,'voice-merged','all.jsonl'),encoding='utf-8') if l.strip()]
def wave(i):
    if re.match(r'tb0\d-',i): return 1
    if re.match(r'tb1[0-7]-',i): return 2
    return 0
W={1:[r for r in recs if wave(r['id'])==1],2:[r for r in recs if wave(r['id'])==2]}
print('quotes: wave1',len(W[1]),'wave2',len(W[2]),'restricted wave2',sum(r.get('restricted',False) for r in W[2]))
print('wave2 dates',min(r['date'] for r in W[2]),max(r['date'] for r in W[2]))
TH=['daycare','daycare_behaviour','daycare_report','oh_crap','advice_ignores_household','only_with_me','only_at_home','parental_preference',
    'backing_off','backed_off','potty_method_3_day','big_little_feelings','good_inside','upairy','course_purchase','gear_purchase','possible_promo',
    'new_sibling','grandparent_undermining','partner_disagreement','maternal_rage','trained_but_own_child','trained_person_stuck','trained_parent','scripts','personalization','information_overload']
print('theme | wave1 | wave2')
for t in TH:
    a=sum(t in r.get('themes',[]) for r in W[1]); b=sum(t in r.get('themes',[]) for r in W[2])
    print(t,'|',a,'|',b)
for ty in ['purchase','price_signal','success_story']:
    print('type',ty,'|',sum(r['type']==ty for r in W[1]),'|',sum(r['type']==ty for r in W[2]))
for name,rx in [('Big Little Feelings / BLF',r'big little feelings|\bBLF\b'),('Good Inside',r'good inside'),('UpAiry',r'upairy'),('Oh Crap / Glowacki',r'oh crap|glowacki|\bjamie\b'),('consultant',r'consult'),('course',r'\bcourses?\b')]:
    print('quote mentions',name,'|',sum(bool(re.search(rx,r['quote'],re.I)) for r in W[1]),'|',sum(bool(re.search(rx,r['quote'],re.I)) for r in W[2]))
