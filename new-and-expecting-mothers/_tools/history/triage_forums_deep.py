#!/usr/bin/env python3
"""Manual card dispositions; separate all-board raw capture from kept reading corpus."""
import importlib.util,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('harvest',ROOT/'_tools/harvest_justparents_deep.py');h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
KEEP={
'11006':'Ordinary return-to-work pumping logistics question; no response, no payment evidence.',
'10762':'12-hour day/night work handoff and expressing/pump constraints; retain logistics and OP pushback, no clinical advice.',
'10899':'Freelance time-zone work and feeding/sleep workload; no treatment claims.',
'9955':'Expressed-milk storage workflow and equipment; retain operational question, retain all reply instructions as attributed speech.',
'10094':'Weaning meaning/decision confusion; adjacent counterevidence, cessation is not necessarily first-solids need.',
'4091':'Breast-pump choice confusion; purchases sought, not report demand.',
'9629':'Next-baby feeding expectations and preparation; experience-only, no clinical recommendations.',
'9037':'Returning-to-work bottle transition and caregiver preparation; retain practical constraints.',
'8844':'16month jarred-food convenience versus homemade pressure; adjacent household-meal counterevidence.',
'8915':'Public-feeding confidence and peer support; counterevidence to information-only solution.',
'9121':'Expecting first mother choosing feeding; emotional preference not a medical diagnosis.',
'8987':'Public-feeding lived experience; counterevidence to universal distress.',
'8970':'Travel/public-feeding practical experience; no legal assertions adopted.',
'8050':'Expecting-parent soother purchase/preparation tradeoff.',
'8634':'Near12month stopping/continuing breastfeeding planning; adjacent, not early-solids inferred.',
'8593':'Direct BLW concept and food-format confusion.',
'8076':'Father doing daytime feeds after mother returns to work; original caregiver handoff voice.',
'6817':'Preparing another feeding attempt after earlier difficulty; read for practical support expectations, retain clinical instructions as attributed speech.',
'1770':'Feeding-goal guilt and lived constraints; counterevidence to report fixing emotional/social pressure.',
'6489':'Firsthand purchased feeding accessory; equipment spend not report willingness.',
'6465':'Expecting mother planning partner feeds and expressing workflow.',
'5496':'First weeks of solids confusion around integrating milk and meals; question evidence only.',
'4514':'Expecting return-to-work at4months and pumping/grocery workflow planning.',
'4483':'Manual pump dissatisfaction and seeking dual/electric purchase; price/infrastructure constraints.',
'1646':'Expecting first mother overwhelmed by conflicting information.',
'3774':'Bottle purchase to combine breast/other-caregiver feeds.',
'2967':'First purees and recipe sources; dated age advice not adopted.',
'2170':'Expecting/planning additional child with3children; available time constraint.',
'2432':'10month breastfeeding social-pressure decision; adjacent counterevidence.',
'2256':'Late-pregnancy feeding preference/guilt; no crisis implied, no emotional-pressure marketing.',
'2118':'Bottle format purchase confusion; practical product-choice question.',
}
SPAM={'10872','10182','5954','9171','2503'}
OUT={'9863','10432','9992','9421','9920','9017','8948','8860','8648','8064','8100','7613','6526','7157','2499','2500','2719'}
if __name__=='__main__':
    b=json.loads((ROOT/'_raw/forums-deep/justparents/boards/feeding.json').read_text());triage=[];kept=[]
    for card in b['topics']:
        tid=card['url'].strip('/').split('topic-')[-1]
        t=json.loads((ROOT/f'_raw/forums-deep/justparents/threads/{tid}.json').read_text())
        # Historical defaults mixed topic decisions with subject censorship.
        # Research keeps every subject; the owner decides later what goes in copy.
        # Unreviewed cards require human topic/duplicate review, not a subject drop.
        keep=True
        reason=KEEP.get(tid) or 'Pending complete human topic/duplicate review; retain all subjects and label commercial provenance.'
        triage.append({'thread_id':t['thread_id'],'board':'feeding','title':t['title'],'url':t['url'],'disposition':'keep' if keep else 'drop','reason':reason,'card_read_scope':'Complete title and first240characters of original post; keep provisional until complete thread read. Earlier all-corpus001–002 also read, separately logged.','raw_thread_json':f'_raw/forums-deep/justparents/threads/{tid}.json','posts':len(t['posts'])})
        if keep:kept.append(t)
    (ROOT/'sources/forums-deep-feeding-triage.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in triage))
    h.freeze_board('kept-feeding',kept)
    print({'triaged':len(triage),'kept':len(kept),'dropped':len(triage)-len(kept),'posts_kept':sum(len(t['posts']) for t in kept)})
