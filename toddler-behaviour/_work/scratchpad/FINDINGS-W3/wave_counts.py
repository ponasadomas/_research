#!/usr/bin/env python3
"""Counts of quotes by wave (1 = tb01-tb09, 2 = tb10-tb17, 3 = tb18-tb27) from voice-merged/all.jsonl.
Counts of quotes chosen by readers, never of people. possible_promo counted separately."""
import json,re,os,collections
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
recs=[json.loads(l) for l in open(os.path.join(ROOT,'voice-merged','all.jsonl'),encoding='utf-8') if l.strip()]
def wave(i):
    if re.match(r'tb0\d-',i): return 1
    if re.match(r'tb1[0-7]-',i): return 2
    if re.match(r'tb(1[89]|2\d)-',i): return 3
    return 0
W={k:[r for r in recs if wave(r['id'])==k] for k in (1,2,3)}
print('quotes:',{k:len(v) for k,v in W.items()},'reviews/other',sum(wave(r['id'])==0 for r in recs))
print('restricted by wave',{k:sum(r.get('restricted',False) for r in v) for k,v in W.items()})
print('wave3 dates',min(r['date'] for r in W[3]),max(r['date'] for r in W[3]))
print('wave3 quotes dated after 2026-06-24',sum(r['date']>'2026-06-24' for r in W[3]))
print('wave3 per reader',collections.Counter(r['id'][:4] for r in W[3]))
TH=['daycare','daycare_behaviour','daycare_report','oh_crap','advice_ignores_household','only_with_me','only_at_home','parental_preference',
    'backing_off','backed_off','holding_firm','held_firm','stopping_rule','naked_to_clothes','potty_method_3_day','big_little_feelings','good_inside','course_purchase','gear_purchase','possible_promo',
    'new_sibling','grandparent_undermining','partner_disagreement','maternal_rage','trained_but_own_child','professional_parent','scripts','personalization','information_overload','reassurance','reassurance_vs_plan','ai_adviser','online_judgement','isolation','working_parents','daycare_helps','deadline','restraint_collapse','consultant']
print('theme | wave1 | wave2 | wave3')
for t in TH:
    print(t,'|',' | '.join(str(sum(t in r.get('themes',[]) for r in W[k])) for k in (1,2,3)))
for ty in ['purchase','price_signal','success_story']:
    print('type',ty,'|',' | '.join(str(sum(r['type']==ty for r in W[k])) for k in (1,2,3)))
for name,rx in [('Big Little Feelings / BLF',r'big little feelings|\bBLF\b'),('Good Inside / Dr Becky',r'good inside|dr\.? ?becky|becky kennedy'),('UpAiry',r'upairy|U\*A\*\*y'),('Oh Crap',r'oh.?crap'),('consultant',r'consult'),('course',r'\bcourses?\b'),('chatgpt/AI',r'chat ?gpt|chat bot|chatbot|\bAI\b')]:
    print('quote mentions',name,'|',' | '.join(str(sum(bool(re.search(rx,r['quote'],re.I)) for r in W[k])) for k in (1,2,3)))
pp=[r['id'] for r in W[3] if 'possible_promo' in r.get('themes',[])]
print('wave3 possible_promo',len(pp),pp)
