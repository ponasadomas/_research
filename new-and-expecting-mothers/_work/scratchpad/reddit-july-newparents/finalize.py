from work import R,W,M,P
import json,csv,collections,hashlib
T=list(csv.DictReader((R/'_raw/reddit-deep/triage/july-newparents.tsv').open(),delimiter='\t'))
manifest=[z for z in map(json.loads,(P/'triage-cards-index.jsonl').read_text().splitlines()) if z['subreddit']=='NewParents']
expected=[p for z in manifest for p in z['post_ids']]
assert len(T)==len(expected)==len(set(x['post_id'] for x in T))
assert set(expected)==set(x['post_id'] for x in T)
E={
'1m14kxp':'Potential promotional/market-research Welcome Baby cluster; independence unverified; excerpt withdrawn',
'1lpzjlb':'Unsafe infant sleep modifications central after full read; equipment excerpt withdrawn',
'1makl4z':'Individualized restraint change and infant transport safety question',
'1lplqvf':'Individualized sleep difficulties tied to ongoing clinical symptoms; no ordinary logistics excerpt retained',
'1lrh0x1':'Feeding decline and stagnant weight make clinical assessment central',
'1ltba0i':'Post-read severe mental-health and disorientation focus',
'1ltq48s':'Self-promotional channel recommendation; not independent parent demand',
'1lu2zvf':'Severe mental-health distress and sedating-medication context',
'1luaia8':'Individual milk intake, weight and physiological feeding assessment',
'1luybaw':'Severe parental mental-health distress is central',
'1lwdca2':'Mental-health and relationship vent without concrete report-sized job after full read',
'1lwh177':'Prevention of clinical postpartum mental-health condition rather than concrete household preparation',
'1lzf7c5':'Formula substitution contrary to existing clinician plan; individualized nutrition question',
'1m01p15':'Maker solicits demand for own proposed commercial app; not independent customer evidence',
'1m03mjm':'Prior loss context excluded from marketing-language use',
'1m1j8ey':'Sleep-plan DM solicitation and unverified rapid-outcome claim',
'1m21ckt':'Severe mental-health distress and inability-to-cope focus',
'1m3nhul':'Acute exhaustion-related clinical safety concern',
'1m4jg4q':'Severe distress with clinically linked feeding/sleep treatment narrative; paid-service excerpts withdrawn',
'1m4xvhb':'High-distress inability-to-cope account; paid-service excerpt withdrawn',
'1m7l9xg':'Known neurological history makes individualized sleep assessment central',
'1m7tode':'Child injury/neglect and safeguarding complaint; not marketing material',
'1m9zdi0':'Maker promoting own data-based clothing planner; not independent customer evidence',
'1maarlx':'High-distress clinically intensive sleep-program account; service-failure excerpts withdrawn',
'1mblnrh':'Memory/bonding symptoms and mental-health concern central despite positive framing on card',
'1mbn9yc':'Severe distress and exhausted caregiver safety concerns',
'1mbahgg':'Severe ongoing infant/parent distress; clinical routing precedes ordinary report support',
'1mbbug8':'Unsafe infant sleep scenario without separate ordinary artifact/tool decision',
'1mcsczv':'Proposed swaddling continuation raises individualized infant sleep safety issue',
'1mdy5xg':'Clinical body-image and severe mental-health distress central after full read',
}
assert set(E)<=set(x['post_id'] for x in T if x['label']!='drop')
Q=list(map(json.loads,(R/'voice/reddit-july-newparents.jsonl').read_text().splitlines()))
removed=[x for x in Q if x['post_id'] in E]
# Withdrawal ids are not reused; preserve a neutral audit without republishing removed text.
prior_withdrawals=json.loads((W/'withdrawn-quote-ids.json').read_text()) if (W/'withdrawn-quote-ids.json').exists() else []
withdrawals={x['id']:x for x in prior_withdrawals}
withdrawals.update({x['id']:{'id':x['id'],'post_id':x['post_id'],'reason':E[x['post_id']]} for x in removed})
(W/'withdrawn-quote-ids.json').write_text(json.dumps(list(withdrawals.values()),indent=2)+'\n')
Q=[x for x in Q if x['post_id'] not in E]
for x in Q:
    if x['post_id']=='1ltgsu5':x['stage']='unknown'
    if x['post_id'] in {'1m14kxp','1m1othf','1md8uu1'}:x['speaker']='parent_unspecified'
    if x['post_id']=='1mcx8xp':x['speaker']='experienced_mother'
    if x['post_id']=='1mef23j':x['themes']=['free_alternatives','format_preference','simple_tracking']
assert len({x['id'] for x in Q})==len(Q)
existing={}
for f in sorted((R/'voice').glob('*.jsonl')):
    if f.name=='reddit-july-newparents.jsonl':continue
    for s in f.read_text().splitlines():
        if not s.strip():continue
        x=json.loads(s); existing.setdefault(x.get('quote',''),[]).append((f.name,x.get('id')))
D=[{'id':x['id'],'other':existing[x['quote']]} for x in Q if x['quote'] in existing]
prior_duplicates=json.loads((W/'duplicate-excerpts.json').read_text()) if (W/'duplicate-excerpts.json').exists() else []
duplicate_history={x['id']:x for x in prior_duplicates};duplicate_history.update({x['id']:x for x in D})
(W/'duplicate-excerpts.json').write_text(json.dumps(list(duplicate_history.values()),indent=2)+'\n')
# Avoid exact repeat excerpts from already-saved readers; all source reads still remain in ledger.
dupids={x['id'] for x in D};Q=[x for x in Q if x['id'] not in dupids]
(R/'voice/reddit-july-newparents.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in Q))
qby=collections.defaultdict(list)
for x in Q:
    pid=x['post_id'];meta=M[pid]
    assert x['quote'] in (R/meta['raw_file']).read_text(),x['id']
    assert x['url']==meta['url'] and x['date']==meta['post_date']
    assert x['raw_file']==meta['raw_file'] and x['read_scope']=='full_post'
    assert len(x['context'].split())<=25
    qby[pid].append(x['id'])
with (W/'reading-ledger.tsv').open('w') as out:
    wr=csv.writer(out,delimiter='\t',lineterminator='\n');wr.writerow(['post_id','card_file','triage_label','reading_status','fully_read','read_scope','reason','raw_file','quote_ids'])
    for x in T:
        pid=x['post_id'];card=next(z['file'] for z in manifest if pid in z['post_ids'])
        status='not-selected' if x['label']=='drop' else ('excluded' if pid in E else 'read')
        wr.writerow([pid,card,x['label'],status,int(x['label']!='drop'),'full_post' if x['label']!='drop' else 'card_only',E.get(pid,x['reason']),M[pid]['raw_file'],','.join(qby[pid])])
with (W/'unread-primary-paths.tsv').open('w') as out:
    wr=csv.writer(out,delimiter='\t',lineterminator='\n');wr.writerow(['post_id','reason','path'])
    for x in T:
        if x['label']=='drop':wr.writerow([x['post_id'],'not-selected after full card triage',M[x['post_id']]['raw_file']])
other=[x for x in map(json.loads,(R/'_raw/reddit-deep/corpus-A-v1/index.jsonl').read_text().splitlines()) if x['subreddit']=='NewParents' and x['post_id'] not in M]
with (W/'outside-july-A-paths.tsv').open('w') as out:
    wr=csv.writer(out,delimiter='\t',lineterminator='\n');wr.writerow(['post_id','status_for_this_reader','path'])
    for x in other:wr.writerow([x['post_id'],'outside assignment; not read by this reader',x.get('raw_file',x.get('unit_file',f"_raw/reddit-deep/corpus-A-v1/units/NewParents-{x['post_id']}.txt"))])
summary={'candidates':len(T),'cards':len(manifest),'triage_labels':dict(collections.Counter(x['label'] for x in T)),'initial_kept':sum(x['label']!='drop' for x in T),'fully_read_posts':sum(x['label']!='drop' for x in T),'post_read_excluded':len(E),'retained_read_posts':sum(x['label']!='drop' for x in T)-len(E),'quotes':len(Q),'quoted_posts':sum(bool(v) for v in qby.values()),'withdrawn_quote_ids':list(withdrawals),'duplicate_excerpt_ids_removed':list(duplicate_history),'unread_selected_kept_posts':0,'unread_not_selected_posts':sum(x['label']=='drop' for x in T),'outside_july_A_posts_not_read_by_this_reader':len(other),'primary_unit_utf8_bytes_read':sum(M[x['post_id']]['utf8_bytes'] for x in T if x['label']!='drop'),'post_body_bytes_read':sum(M[x['post_id']]['post_body_bytes'] for x in T if x['label']!='drop'),'OP_replies_read':0,'other_comments_read':0,'candidate_safety_flags':sum(M[x['post_id']]['safety_flag'] for x in T),'all_quote_ids_unique':True,'all_quotes_literal_substrings':True,'all_contexts_at_most_25_words':True,'all_metadata_matches_frozen_index':True,'triage_id_set_missing':0,'triage_id_set_unexpected':0,'triage_duplicate_ids':0}
(W/'audit.json').write_text(json.dumps(summary,indent=2)+'\n')
(W/'post-read-exclusions.json').write_text(json.dumps(E,indent=2)+'\n')
print(json.dumps(summary,indent=2))
