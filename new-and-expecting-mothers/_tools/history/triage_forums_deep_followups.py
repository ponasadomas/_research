#!/usr/bin/env python3
"""Full selected board-card triage; provisional kept threads require complete reading."""
import importlib.util,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('h',ROOT/'_tools/harvest_justparents_deep.py');h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
KEEP={
'baby':{'12170','10929','8980','10503','10592','10171','10184','9482','10027','9877','10012','9997','9952','9780','9172','9000','9219','9026','8268','7835','7461','7232','5903','4216','2726','2079','1762'},
'work-childcare':{'8081','3051','10545','9889','9858','9862','10002','5414','4309','8660','7103','4332','2433'},
'third-trimester':{'9382','10008','9894','10061','9996','9954','8327'},
'second-trimester':{'9608'},
'first-trimester':{'9791','9773'},
'birth-labour':{'9960'},
'activities':{'9878','8662','8555','8027','6995','1789','1307','1157','707','918','100','1130'},
}
CLINICAL_BABY={'11963','10713','10945','9843','10718','9660','9977','8796','9917','9868','8875','9564','8890','9519','9494','7741','9271','8743','8357','7954','7727','7680','7167','6856','4143','3260'}
DISTRESS_BABY={'9809','9564','6507','5279','1308','10817','7467','7443','7366','2642','4013'}
PROMO_BABY={'11323','10306'}
REASONS={
'baby':'Practical baby-care, purchases, activity/meal ideas, caregiver support or a normal positive counterexample; provisional until full thread read. Retain every subject as attributed evidence; copy decisions belong to the owner.',
'work-childcare':'Firsthand work/home/caregiving constraints or work choice after baby. Read for structural/cost alternatives, not job recruitment or an assumed report market.',
'third-trimester':'Late-pregnancy household/sibling preparation, bag/checklist, support choices or purchases; include ordinary confidence as counterevidence.',
'second-trimester':'Expecting twins parent seeks people to chat with; human community is an alternative, not assumed report demand.',
'first-trimester':'Information overload or newborn gadget-choice confusion; inspect for research solicitation or commercial self-promotion before quoting.',
'birth-labour':'Information consumed before birth versus actual experience; context-only counterevidence, all birth stories retained as attributed evidence.',
'activities':'Infant trip/packing logistics, affordable local activities, free library support or explicit adjacent toddler space constraints. Historical policy advice not adopted.',
}
if __name__=='__main__':
    triage=[];groups={};totals={}
    for board,keepids in KEEP.items():
        b=json.loads((ROOT/f'_raw/forums-deep/justparents/boards/{board}.json').read_text());kept=[]
        for card in b['topics']:
            tid=card['url'].strip('/').split('topic-')[-1];t=json.loads((ROOT/f'_raw/forums-deep/justparents/threads/{tid}.json').read_text())
            # Research retains every subject; copy decisions belong to the owner.
            # Historical default drops mixed subjects and scope: review them fully.
            keep=True
            if keep:reason=REASONS[board] if tid in keepids else 'Pending complete human topic/duplicate review; retain every subject and label provenance.'
            row={'thread_id':t['thread_id'],'board':board,'title':t['title'],'url':t['url'],'disposition':'keep_provisional' if keep else 'drop','reason':reason,'card_read_scope':'Complete title and original-post preview (190characters Baby;160characters otherboards). Not a full thread read.','raw_thread_json':f'_raw/forums-deep/justparents/threads/{tid}.json','posts':len(t['posts'])}
            triage.append(row)
            if keep:kept.append(t)
        group='baby' if board=='baby' else 'work' if board=='work-childcare' else 'activities' if board=='activities' else 'preparation'
        groups.setdefault(group,[]).extend(kept);totals[board]={'cards_triaged':len(b['topics']),'provisional_kept':len(kept),'dropped':len(b['topics'])-len(kept)}
    (ROOT/'sources/forums-deep-followup-triage.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in triage))
    for group,threads in groups.items():
        brief=ROOT/f'_tools/brief-forum-kept-{group}.md'
        brief.write_text(f'''# JustParents retained {group} reading wave\n\nThe complete board-card inventories have been triaged locally; see sources/forums-deep-followup-triage.jsonl. Read every post and all saved pages for every thread in scratchpad/forums-deep/justparents-kept-{group}-manifest.json. The prior all-board corpus stays frozen and is not automatically retained.\n\nRead all chunks before calling a multi-chunk thread fullread. Append only to your own hash-based chunk reading ledger. Produce per-thread final disposition and reader notes. Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; record off-topic/duplicate/unavailable decisions and label commercial provenance. Unknown author age is not invented. Original-post/response IDs, page URL and raw HTML path are in each block. Repeated quoted content is not another voice.\n\nFocus on ordinary caregiver coordination, constraints, purchases actually made/tried, price objections, free alternatives, OP followups and counterevidence to customized report demand. Do not repeat medical or historical policy advice as fact. A question or equipment purchase is not paid-report demand. Fresh wave quote file/prefix must be agreed with parent/market to avoid collisions; do not append fdeep01. Exact <=25words per original post/author work, context <=25words, source_class=forum, evidence_kind=original_thread_post, raw_file required, 0failed verification. No outreach, accounts, new harvesting or global synthesis edits in this reading task.\n''')
        h.freeze_board('kept-'+group,threads)
    print(json.dumps(totals,indent=2))
