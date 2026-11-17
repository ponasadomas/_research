#!/usr/bin/env python3
"""Wave 1/2/3 quote counts (run from pregnancy-birth/): python3 -I scratchpad/FINDINGS-W3/w3counts.py"""
import json,re,collections
R=[json.loads(l) for l in open('voice-merged/all.jsonl',encoding='utf-8') if l.strip()]
def wave(r):
    m=re.match(r'pb(\d\d)-',r['id'])
    if not m: return None
    n=int(m.group(1)); return 1 if n<=22 else 2 if n<=45 else 3 if n<=72 else None
W=collections.defaultdict(list)
for r in R:
    w=wave(r)
    if w: W[w].append(r)
for w in (1,2,3):
    print('wave',w,'quotes',len(W[w]),'historically_marked',sum(bool(r['formerly_restricted']) for r in W[w]))
print('all quotes',len(R),'historically_marked',sum(bool(r['formerly_restricted']) for r in R))
print('\nper reader (wave 3): quotes historically_marked share')
pr=collections.defaultdict(lambda:[0,0])
for r in W[3]:
    p=r['id'][:4]; pr[p][0]+=1; pr[p][1]+=bool(r['formerly_restricted'])
for p in sorted(pr): print(p,pr[p][0],pr[p][1],f"{100*pr[p][1]/pr[p][0]:.0f}%")
sh=sorted((100*b/a,p) for p,(a,b) in pr.items()); print('min',sh[0],'max',sh[-1])
TH=['work_in_pregnancy','maternity_leave','partner_role','partner_leave','partner_leave_gap','visitors','mother_in_law','own_mother','pregnancy_with_toddler','older_child_care','who_minds_older_child','first_two_weeks','information_overload','week_by_week','stock_lines','guide_request','sugar_coated','ob_prepayment','hospital_prepayment','care_navigation','us_insurance','uk_nhs','birth_course','hypnobirthing','doula','what_to_buy','registry','dated_plan','overseas_family_visit','no_village','not_listened_to','dismissed_by_provider','comparison_other_pregnancies','second_pregnancy','first_pregnancy']
print('\ntheme | w1 | w2 | w3')
for t in TH: print(t,*[sum(t in r['themes'] for r in W[w]) for w in (1,2,3)])
for w in (1,2,3): print('any theme containing heat, wave',w,sum(any('heat' in t for t in r['themes']) for r in W[w]))
ai=lambda ws:[r['id'] for r in ws if re.search(r'(?i:chat ?gpt|claude|chatbot|gemini|copilot)|\bAI\b',r['quote'])]
for w in (1,2,3): print('AI wording wave',w,len(ai(W[w])))
print(ai(W[3]))
st=collections.Counter(r['stage'] for r in W[3]); print('\nwave3 stage',st.most_common())
sp=collections.Counter(r['speaker'] for r in W[3]); print('wave3 speaker',sp.most_common())
tot={w:len(W[w]) for w in (1,2,3)}
print('\nshares of each wave (w1/w2/w3)')
for t in ['work_in_pregnancy','maternity_leave','partner_role','pregnancy_with_toddler','visitors','mother_in_law','own_mother','first_two_weeks','information_overload','week_by_week','ob_prepayment']:
    print(t,' / '.join(f"{100*sum(t in r['themes'] for r in W[w])/tot[w]:.1f}%" for w in (1,2,3)))
print('ob_prepayment by reader, wave 3',collections.Counter(r['id'][:4] for r in W[3] if 'ob_prepayment' in r['themes']))
for w in (1,2,3):
    s=collections.Counter(r['stage'] for r in W[w]); print('wave',w,'first_trimester',s['first_trimester'],'second_trimester',s['second_trimester'],'third_trimester',s['third_trimester'],'birth',s['birth'])
import re as _re
d=collections.defaultdict(list)
for r in W[3]:
    if len(r['quote'])>=40: d[_re.sub(r'\W+','',r['quote'].lower())[:120]].append(r['id'])
print('identical-text pairs across wave-3 readers',[v for v in d.values() if len({x[:4] for x in v})>1])
