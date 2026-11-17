#!/usr/bin/env python3
"""Wave-1 vs wave-2 quote counts by theme (run from pregnancy-birth/)."""
import json,re,collections
R=[json.loads(l) for l in open('voice-merged/all.jsonl') if l.strip()]
def wave(r):
    m=re.match(r'pb(\d\d)-',r['id'])
    if not m: return None
    n=int(m.group(1)); return 1 if n<=22 else 2 if n<=45 else None
W=collections.defaultdict(list)
for r in R:
    w=wave(r)
    if w: W[w].append(r)
for w in (1,2):
    print('wave',w,'quotes',len(W[w]),'historically_marked',sum(r['formerly_restricted'] for r in W[w]))
TH=['work_in_pregnancy','maternity_leave','partner_role','partner_leave','partner_leave_gap','paternity_leave','visitors','mother_in_law','own_mother','pregnancy_with_toddler','older_child_care','who_minds_older_child','first_two_weeks','information_overload','week_by_week','heat','heat_in_pregnancy','stock_lines','stock_phrases','guide_request','sugar_coated','sugar_coated_info','overseas_family_visit','ob_prepayment','global_fee','global_ob_fee','us_insurance','uk_nhs']
print('theme | wave1 | wave2')
for t in TH:
    print(t, sum(t in r['themes'] for r in W[1]), sum(t in r['themes'] for r in W[2]))
heat2=[r for r in W[2] if any('heat' in t for t in r['themes'])]
heat1=[r for r in W[1] if any('heat' in t for t in r['themes'])]
print('any theme containing "heat": w1',len(heat1),'w2',len(heat2))
sm=lambda ws:[r['id'] for r in ws if re.search(r'wildfire|smoke from|air quality|\bAQI?\b',r['quote'],re.I)]
print('smoke/air-quality wording w1',sm(W[1]),'w2',sm(W[2]))
ai=lambda ws:[r['id'] for r in ws if re.search(r'chat ?gpt|\bAI\b|claude|chatbot|gemini',r['quote'])]
print('AI wording w1',len(ai(W[1])),ai(W[1]),'\nw2',len(ai(W[2])),ai(W[2]))
ai2=lambda ws:[r['id'] for r in ws if re.search(r'(?i:chat ?gpt|claude|chatbot|gemini|copilot)|\bAI\b',r['quote'])]
print('AI wording (fixed) w1',len(ai2(W[1])),'w2',len(ai2(W[2])),ai2(W[2]))
