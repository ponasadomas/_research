#!/usr/bin/env python3
"""Reconcile captured, card-triaged, finally retained, and actually read forum units."""
import collections,hashlib,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
RAW=ROOT/'_raw/forums-deep/justparents'
SCRATCH=ROOT/'scratchpad/forums-deep'
boardrows=[json.loads(p.read_text()) for p in (RAW/'boards').glob('*.json')]
threads={t['thread_id']:t for t in [json.loads(p.read_text()) for p in (RAW/'threads').glob('*.json')]}
triage=[]
for f in ['forums-deep-feeding-triage.jsonl','forums-deep-followup-triage.jsonl']:
    p=ROOT/'sources'/f
    if p.exists():triage.extend(json.loads(l) for l in p.read_text().splitlines())
final={}
for p in (ROOT/'sources').glob('forums-deep-*-final.jsonl'):
    for l in p.read_text().splitlines():
        x=json.loads(l);final[x['thread_id']]=x
read_chunks={}
for p in (ROOT/'sources').glob('forums-deep-reading-*.jsonl'):
    for l in p.read_text().splitlines():
        x=json.loads(l)
        if x.get('read_status')=='full' and (ROOT/x['file']).exists() and hashlib.sha256((ROOT/x['file']).read_bytes()).hexdigest()==x['sha256']:read_chunks[x['file']]=x
needed=collections.defaultdict(set);chunkrows=[]
for p in SCRATCH.glob('justparents-kept-*-manifest.json'):
    m=json.loads(p.read_text());chunkrows.extend(m['chunks'])
    for c in m['chunks']:
        for tid in c['thread_ids']:needed[tid].add(c['file'])
readthreads={tid for tid,files in needed.items() if files.issubset(read_chunks)}
effective=[]
for x in triage:
    if x['disposition'].startswith('keep'):
        f=final.get(x['thread_id'],{});d=f.get('disposition','keep_provisional')
        effective.append({**x,'final_disposition':d,'final_reason':f.get('reason','Full reading/final disposition pending.'),'read_status':'full' if x['thread_id'] in readthreads else 'unread','required_chunks':sorted(needed[x['thread_id']]),'quotes':f.get('quote_ids',[])})
retained=[x for x in effective if not x['final_disposition'].startswith('drop')]
read_kept=[x for x in retained if x['read_status']=='full'];unread=[x for x in retained if x['read_status']!='full']
quote_files=sorted((ROOT/'voice').glob('forums-deep-*.jsonl'));quotes=[json.loads(l) for p in quote_files for l in p.read_text().splitlines()]
stats={'board_inventory_count':len(boardrows),'board_listing_pages':sum(len(b['pages']) for b in boardrows),'listed_thread_cards':sum(b['unique_topics'] for b in boardrows),'unique_captured_threads':len(threads),'captured_thread_pages':sum(t['visible_pages_fetched'] for t in threads.values()),'captured_original_posts_and_responses':sum(t['visible_post_count'] for t in threads.values()),'listing_count_mismatches':sum(b['unique_topics']!=b['expected_displayed_topics'] for b in boardrows),'thread_count_mismatches':sum(not t['listed_count_matches'] for t in threads.values()),'triaged_cards':len(triage),'initially_retained_threads':len(effective),'post_read_drops':len(effective)-len(retained),'effective_retained_threads':len(retained),'retained_threads_fully_read':len(read_kept),'retained_threads_unread':len(unread),'frozen_retained_chunks':len(chunkrows),'retained_chunks_fully_read':sum(c['file'] in read_chunks for c in chunkrows),'retained_chunks_unread':sum(c['file'] not in read_chunks for c in chunkrows),'quotes':len(quotes)}
stats.update(initially_retained_posts=sum(threads[x['thread_id']]['visible_post_count'] for x in effective),effective_retained_posts=sum(threads[x['thread_id']]['visible_post_count'] for x in retained),provisional_threads_fully_read=sum(x['read_status']=='full' for x in effective),initial_card_drops=len(triage)-len(effective),total_dropped_threads=len(triage)-len(retained))
(ROOT/'sources/forums-deep-effective-kept-manifest.json').write_text(json.dumps({'stats':stats,'threads':effective,'reading_ledgers':[str(p.relative_to(ROOT)) for p in (ROOT/'sources').glob('forums-deep-reading-*.jsonl')]},ensure_ascii=False,indent=2))
(ROOT/'sources/forums-deep-thread-registry.jsonl').write_text(''.join(json.dumps({'thread_id':tid,'title':t['title'],'board':t['board'],'url':t['url'],'pages':t['visible_pages_fetched'],'posts':t['visible_post_count'],'pagination_complete':t['pagination_complete'],'listed_count_matches':t['listed_count_matches'],'raw_thread_json':f"_raw/forums-deep/justparents/threads/{tid[3:]}.json"},ensure_ascii=False)+'\n' for tid,t in sorted(threads.items())))
lines=['# Primary parenting forums — expanded wave','', 'See [discovery/access ledger](forums-deep-discovery.md) for 54 candidate host/URL variants (51 after www collapse), actual canonical policy/content outcomes, and untouched responses. One core forum, JustParents, supported this full capture; that is not 51 usable forums. No account, outreach, identity switching, proxy, challenge bypass or private access.','',
'The finite board inventory was chosen by ordinary pregnancy/infant/caregiving topics, then **every listing page and every visible paginated thread page** was saved before local card triage. No search-picked top 10 or arbitrary per-board thread cap. Full inventory collection does not imply automatic retention. All original raw threads and the earlier all-board reading corpus remain preserved after drops.','',
'|Board|Listing pages|Displayed/unique topics|Captured posts|','|---|---:|---:|---:|']
for b in sorted(boardrows,key=lambda x:x['board']):
    ts=[t for t in threads.values() if t['board']==b['board']]
    lines.append(f"|{b['board']}|{len(b['pages'])}|{b['expected_displayed_topics']}/{b['unique_topics']}|{sum(t['visible_post_count'] for t in ts)}|")
lines.extend(['',f"Captured **{stats['unique_captured_threads']} unique full visible threads, {stats['captured_thread_pages']} thread pages, {stats['captured_original_posts_and_responses']} original posts/responses**. Board count mismatches:{stats['listing_count_mismatches']}; expected-post count mismatches:{stats['thread_count_mismatches']}. 'Complete' describes visible pagination, not deleted/private content, independently verified authorship, all historical site topics, or a representative population.",'',
f"Local triage covers **{stats['triaged_cards']} cards**, with **{stats['initially_retained_threads']} initially retained**, **{stats['post_read_drops']} later drops**, **{stats['effective_retained_threads']} effective retained**. **{stats['retained_threads_fully_read']} effective retained threads fully read; {stats['retained_threads_unread']} unread**. Frozen retained chunks:{stats['frozen_retained_chunks']}; actually fullread:{stats['retained_chunks_fully_read']}; unread:{stats['retained_chunks_unread']}. Individual dispositions and required chunks: `forums-deep-effective-kept-manifest.json`. The frozen original manifests show the initial unread snapshot; actual read state comes only from SHA256-validated reading ledgers.",'',
f"Quotes:{stats['quotes']} across fresh `voice/forums-deep-*.jsonl`; see per-wave strict verification artifacts. Original HTML `raw_file`, original post/response ID, thread JSON and original-post linkage accompany each excerpt. Repeated quoted prior posts are not independent voices. Quote contexts<=25 words and quotations<=25 words per original post/author work; factual claims in replies remain peer claims.",'',
'Limitations: this is one self-selected public forum archive, with many original discussions roughly 2007–2018 despite later replies. Dates are retained **as displayed** (often relative), not invented as exact calendar dates. No current segment prevalence, success rate, saturation, TAM or report willingness-to-pay is inferred. Work/childcare is largely an old work-at-home business board; promotional/recruitment cards are excluded. Research records what people actually say and do, in their own words, whatever the subject. The owner decides later what to use in copy; research never makes that decision. Free support and equipment spending are not paid-report demand.','',
'Full reader findings and counterevidence: `synthesis/reader-notes-forums-deep.md`. All-card triage: `forums-deep-feeding-triage.jsonl` and `forums-deep-followup-triage.jsonl`. Raw thread registry: `forums-deep-thread-registry.jsonl`. The reading scripts and reusable group briefs are in `_tools/`; page responses are never executed by the parser.',''])
(ROOT/'sources/forums-deep.md').write_text('\n'.join(lines))
print(json.dumps(stats,indent=2))
