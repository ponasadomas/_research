# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
"""Build this reader's manually selected evidence and audit against frozen native records.

This performs no triage or semantic selection. Human decisions are in the TSV,
reading ledger, corrected selections, and explicit duplicate decisions below.
"""
import collections
import csv
import datetime
import gzip
import hashlib
import html
import json
import re
import subprocess
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
R = S.parents[1]
W = R / '_raw/reddit-deep/aug-dec-2025-wave-v1'
def jl(p):
    return [json.loads(line) for line in p.read_text().splitlines() if line.strip()]
def writejl(p, rows):
    p.write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in rows))
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):
    return re.sub(r'\s+', ' ', html.unescape(s).replace('\\n', ' ')).strip()
def stamp(t):
    return datetime.datetime.fromtimestamp(int(t), datetime.timezone.utc).isoformat()

manifest = json.loads((W / 'assignments/batch-02.json').read_text())
assigned = [p for c in manifest['chunks'] for p in c['post_ids']]
triage = list(csv.DictReader((R / '_raw/reddit-deep/triage/augdec-02.tsv').open(), delimiter='\t'))
triaged = {x['post_id']: x for x in triage}
ledger_path = R / 'sources/reddit-augdec-02-reading.jsonl'
ledger = jl(ledger_path)
read = {x['post_id']: x for x in ledger}
index = {x['post_id']: x for x in jl(W / 'primary-index.jsonl')}
selections = jl(S / 'selections-corrected.jsonl')
chunks = json.loads((S / 'kept-chunks.json').read_text())

# Explicit human decisions after inspecting all 101 flag groups. The names below
# are representatives for body-level deduplication, never authenticity findings.
representatives = {
    1:'1n7jklc', 2:'1npkqhb', 3:'1o1kw65', 4:'1o529je', 5:'1p1b1q0',
    6:'1pj1xjd', 7:'1mfaipx', 8:'1mihus3', 9:'1mjyh1i', 10:'1mlp2ll',
    11:'1mrftga', 12:'1mxgbln', 13:'1mzpkk2', 14:'1n4e914', 15:'1nbjaqx',
    25:'1otg7po', 29:'1oxc8r6', 31:'1p1kdpu', 32:'1p3ysdn', 34:'1ptar64',
    35:'1q08dgt', 36:'1pou59t', 40:'1n4965b', 42:'1n5mlol', 45:'1ngnfhp',
    46:'1odt3lv', 47:'1of6rxr', 48:'1pfz0ox', 54:'1mhwh2d', 55:'1mqzfuk',
    56:'1mtjiug', 58:'1na44u1', 59:'1nap6ec', 62:'1nnxxbs', 63:'1nnwhlz',
    64:'1noaua5', 74:'1oe3dbf', 77:'1oql6b9', 78:'1oqybt0', 79:'1osn9m8',
    81:'1penm6c', 82:'1pfwgrc', 84:'1phw8x5', 86:'1pm7hy9', 87:'1pyzmh4',
    88:'1pzbcra', 89:'1pzys8r', 90:'1mp8alu', 91:'1mswkev', 94:'1nutljq',
    96:'1pek399', 100:'1no1rfh',
}
duplicate_review = []
for number, group in enumerate(jl(W / 'exact-body-duplicate-flags.jsonl'), 1):
    members = group['records']
    own = [m['post_id'] for m in members if m['post_id'] in triaged]
    if not own:
        duplicate_review.append(dict(group=number, assigned_ids=[], decision='Outside assignment; flag metadata reviewed, no additional bodies claimed read.'))
        continue
    rep = representatives[number]
    assert rep in {m['post_id'] for m in members}
    reason = 'Earliest dated body instance represents this repeated body; no independent-buyer multiplication. All assigned keeps were still fully read.'
    if number == 13:
        reason = 'Earlier same-community copy selected; later copy already excluded after full reading. Only the earlier excerpt is retained.'
    elif number in {6,10}:
        reason = 'Repeated promotional or supplier guide/hack context remains unselected; earliest date is only the deduplication anchor, not a buyer.'
    elif all(triaged[p]['label'] == 'drop' for p in own):
        reason = 'All assigned cards independently dropped for their recorded scope or safety reasons; no original body read or quoted here. Earliest flag instance is the anchor.'
    elif all(read[p]['status'] == 'excluded_after_read' for p in own if p in read):
        reason = 'Read assigned keeps remain excluded for their recorded reasons. Earliest flag instance is the body anchor, with no selected purchase evidence.'
    duplicate_review.append(dict(group=number, assigned_ids=own, representative_post_id=rep,
                                 decision=reason, selected_ids=[x['post_id'] for x in selections if x['post_id'] in {m['post_id'] for m in members}],
                                 body_read_claim='Only IDs present in this reading ledger are claimed fully read.'))
    for p in own:
        if p in read:
            read[p].update(duplicate_body_group=number, duplicate_representative_post_id=rep,
                           independent_body_representative=(p == rep))
    for x in selections:
        if x['post_id'] in {m['post_id'] for m in members}:
            assert x['post_id'] == rep
writejl(S / 'duplicate-review.jsonl', duplicate_review)

# Retrieve original fields independently from the source window, not from titles,
# card openings, chunk headers, or primary-unit JSON metadata.
native = {}
for file in sorted({index[p]['source_post_file'] for p in read}):
    with gzip.open(R / file, 'rt') as stream:
        for line in stream:
            row = json.loads(line)
            if row['id'] in read:
                native[row['id']] = row
native_op = collections.defaultdict(list)
for file in sorted({index[p]['source_comment_file'] for p in read if index[p]['source_comment_file']}):
    with gzip.open(R / file, 'rt') as stream:
        for line in stream:
            row = json.loads(line)
            p = row.get('link_id', '').removeprefix('t3_')
            if p not in read:
                continue
            author = native[p].get('author')
            if author and author not in {'[deleted]', '[removed]'} and row.get('author') == author:
                native_op[p].append(row)
for rows in native_op.values():
    rows.sort(key=lambda x: (int(x['created_utc']), x['id']))

# Use README seed tags where applicable; the seven narrowly needed extensions
# are documented in this reader's source note, without editing global vocabulary.
theme_map = {
    'boundaries':'household_support', 'budget':'price_value', 'childcare':'daycare_handoff',
    'community':'no_village', 'decision_overload':'information_overload',
    'identity':'maternal_guilt', 'judgment':'maternal_guilt', 'meals':'meal_planning',
    'memories':'memory_keeping', 'mental_load':'household_mental_load', 'money':'price_value',
    'planning':'household_routines', 'play':'activity_planning', 'postpartum':'postpartum_recovery',
    'pumping':'pumping_schedule', 'purchase_decisions':'gear_selection', 'registry':'gear_selection',
    'routine':'household_routines', 'routines':'household_routines', 'self_care':'household_support',
    'simplicity':'household_routines', 'sleep':'sleep_routines', 'social_pressure':'maternal_guilt',
    'solids':'first_solids', 'support':'household_support', 'time':'not_enough_time',
    'time_management':'not_enough_time', 'tools':'digital_tools', 'tracking':'digital_tools',
    'travel':'travel_logistics', 'trust':'skepticism', 'value_for_money':'price_value',
    'work_life_balance':'return_to_work',
}
extensions = {'memory_keeping','household_mental_load','household_routines','activity_planning','gear_selection','digital_tools','travel_logistics'}
quotes = []
for number, selection in enumerate(selections, 1):
    p = selection['post_id']; n = native[p]; i = index[p]
    x = dict(id=f'rad02-{number:04d}', source=f'Reddit r/{n["subreddit"]} (frozen public archive)',
             url='https://www.reddit.com' + n['permalink'], date=stamp(n['created_utc']),
             author=n['author'], speaker='parent_unspecified', stage=selection['stage'],
             type=selection['type'], themes=list(dict.fromkeys(theme_map.get(t,t) for t in selection['themes'])),
             quote=selection['quote'], context=selection['context'], raw_file=i['raw_file'],
             source_class='reddit_archive', evidence_kind='archived_original',
             archive_dataset='yikeee/reddit-subreddits25',
             archive_commit='ea497c510aa68765c07ed744ec9f84d68bbedf7f', post_id=p,
             read_scope='full_post_and_available_identifiable_OP_replies' if i['comment_source_available'] else 'full_post_comment_source_unavailable',
             paid_report_demand_proven=False)
    if p in {'1mf67l2','1pt5em6','1my543p'}:
        x['stage'] = 'unknown'
    if p in {'1nksj37','1p4721n'}:
        x['speaker'] = 'partner'
    for k in ('authenticity_note'):
        if k in selection:
            x[k] = selection[k]
    # Earlier helper accepted a paid meal-kit success as tried_failed; corrected
    # selection explicitly preserves its actual positive reported outcome.
    quotes.append(x)
voice_path = R / 'voice/reddit-augdec-02.jsonl'
writejl(voice_path, quotes)
for row in ledger:
    row['quote_ids'] = [q['id'] for q in quotes if q['post_id'] == row['post_id']]
writejl(ledger_path, ledger)
aux_path = R / 'sources/reddit-augdec-02-auxiliary-read.jsonl'
if not aux_path.exists():
    aux_path.write_text('')

errors = []
checks = collections.Counter()
def check(condition, category, detail):
    checks[category] += 1
    if not condition:
        errors.append({'category':category, 'detail':detail})

check(len(assigned)==2193 and len(set(assigned))==2193, 'assignment', 'exact assigned count and uniqueness')
check(len(triage)==len(triaged)==2193 and set(assigned)==set(triaged), 'triage', 'exact assigned/triage sets')
check(len(manifest['chunks'])==37, 'assignment', '37 card chunks')
kept = {p for p,t in triaged.items() if t['label'] != 'drop'}
check(len(ledger)==len(read)==1490 and kept==set(read), 'reading', 'every keep exactly once')
check(len(native)==1490, 'native', 'all original records found')
for card in manifest['chunks']:
    check(sha(R/card['file'])==card['sha256'], 'card_hash', card['file'])
for t in triage:
    check(bool(t['reason'].strip()) and t['card_file'] in {c['file'] for c in manifest['chunks']}, 'triage', t['post_id'])
check(len(chunks)==80 and [p for c in chunks for p in c['ids']]==[x['post_id'] for x in ledger], 'reading_chunks', 'all frozen units accounted')
for c in chunks:
    chunk_text = (S / c['file']).read_text()
    for p in c['ids']:
        raw = (R / index[p]['raw_file']).read_text()
        complete = raw[raw.index('=== COMPLETE ORIGINAL POST TITLE ==='):]
        check(complete in chunk_text, 'frozen_complete_unit', p)
for p,l in read.items():
    i=index[p]; n=native[p]; raw=(R/i['raw_file']).read_text()
    check(l['post_body_read_complete'] is True, 'full_read_boolean', p)
    check(l['raw_file']==i['raw_file'] and l['primary_unit_sha256']==i['sha256']==sha(R/i['raw_file']), 'unit_hash', p)
    body=raw.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0].strip()
    check(body==n.get('selftext','').strip(), 'native_full_body', p)
    title=raw.split('=== COMPLETE ORIGINAL POST TITLE ===\n',1)[1].split('\n=== COMPLETE ORIGINAL POST BODY ===',1)[0].strip()
    check(title==n.get('title','').strip(), 'native_title', p)
    op=native_op[p]
    ids=[c['id'] for c in op]
    check(ids==i['OP_comment_ids']==l['op_reply_ids_read'] and len(ids)==i['OP_replies']==l['available_identifiable_OP_replies_read'], 'native_OP_identity_count', p)
    sections=raw.split('--- OP REPLY ---\n')[1:]
    check(len(sections)==len(op), 'native_OP_sections', p)
    for section, comment in zip(sections,op):
        metatext, b=section.split('\n',1); meta=json.loads(metatext)
        check(b.strip()==comment.get('body','').strip(), 'native_OP_full_body', comment['id'])
        check(meta['comment_id']==comment['id'] and meta['date']==stamp(comment['created_utc']) and meta['parent_id']==comment.get('parent_id'), 'native_OP_metadata', comment['id'])
        check(comment.get('author')==n.get('author') and n.get('author') not in {'[deleted]','[removed]'}, 'native_OP_author', comment['id'])

readme=(R/'README.md').read_text()
def tokens(label):
    return set(re.findall(r'`([^`]+)`', readme.split(label+':',1)[1].split('\n\n',1)[0]))
speakers=tokens('Speakers'); stages=tokens('Stages'); types=tokens('Types'); themes=tokens('Seed themes')|extensions
all_ids=[]
for file in (R/'voice').glob('*.jsonl'):
    all_ids.extend(q['id'] for q in jl(file))
for q in quotes:
    p=q['post_id']; n=native[p]; i=index[p]
    check(all_ids.count(q['id'])==1, 'global_quote_ID', q['id'])
    check(q['speaker'] in speakers and q['stage'] in stages and q['type'] in types and set(q['themes'])<=themes, 'vocabulary', q['id'])
    check(len(q['context'].split())<=25, 'context_words', q['id'])
    check(q['author']==n['author'] and q['date']==stamp(n['created_utc']) and q['url']=='https://www.reddit.com'+n['permalink'], 'native_quote_metadata', q['id'])
    check(q['raw_file']==i['raw_file'] and q['id'] in read[p]['quote_ids'], 'quote_ledger_link', q['id'])
    check(read[p]['post_body_read_complete'] is True, 'restricted_quote', q['id'])
    pos=0
    for piece in q['quote'].split(' […] '):
        body=norm(n['selftext']); piece=norm(piece); at=body.find(piece,pos)
        check(at>=0, 'native_own_body_quote', q['id'])
        pos=at+len(piece)
    check('u/' not in q['quote']+q['context'] and n['author'] not in q['quote']+q['context'], 'no_username_selected', q['id'])
    check(not q['paid_report_demand_proven'], 'no_report_purchase_inference', q['id'])

notes_path=R/'synthesis/reader-notes-reddit-augdec-02.md'
source_path=R/'sources/reddit-augdec-02.md'
note_ids=[]
if notes_path.exists() and source_path.exists():
    for path in [notes_path, source_path]:
        for identifier in re.findall(r'rad02-\d{4}',path.read_text()):
            note_ids.append(identifier)
            check(identifier in {q['id'] for q in quotes},'notes_ID_lookup',str(path.name)+':'+identifier)
else:
    errors.append({'category':'notes_pending','detail':'Final source note and reader findings must exist before final verification.'})
strict=subprocess.run([sys.executable,str(R/'_tools/verify_quotes.py'),str(voice_path)],capture_output=True,text=True)
check(strict.returncode==0,'strict_verify_quotes',strict.stdout+strict.stderr)
scope_groups=[g for g in duplicate_review if g['assigned_ids']]
counts=dict(assigned_cards=len(assigned),triaged_cards=len(triage),card_drops=sum(t['label']=='drop' for t in triage),
            triage_keeps=len(kept),full_original_posts=len(ledger),partial_reads=0,
            eligible_after_read=sum(l['status']=='eligible' for l in ledger),excluded_after_read=sum(l['status']=='excluded_after_read' for l in ledger),
            identifiable_OP_replies=sum(len(rows) for rows in native_op.values()),auxiliary_non_OP_comments=0,
            original_posts_comment_source_available=sum(index[p]['comment_source_available'] for p in read),
            original_posts_comment_source_unavailable=sum(not index[p]['comment_source_available'] for p in read),
            selected_excerpts=len(quotes),selected_original_posts=len({q['post_id'] for q in quotes}),
            selected_OP_comments=0,research_only_excerpts=sum(q.get('marketing_eligible') is False for q in quotes),
            duplicate_flag_groups_reviewed=len(duplicate_review),duplicate_groups_touching_assignment=len(scope_groups),
            selected_flagged_duplicate_groups=sum(bool(g.get('selected_ids')) for g in scope_groups),
            unique_notes_IDs_checked=len(set(note_ids)),notes_ID_occurrences_checked=len(note_ids))
audit=dict(date='2026-10-24',batch=2,scope='All assigned Aug–Dec tier-A cards and all human-kept original posts plus identifiable OP replies.',
           counts=counts,triage_labels=dict(collections.Counter(t['label'] for t in triage)),
           reading_by_subreddit=dict(collections.Counter(index[p]['subreddit'] for p in read)),
           counts_are_not_people_or_prevalence=True,paid_standalone_report_purchases_verified=0,
           known_limitations=['Publisher authenticity, rights/license/provenance and live completeness unverified.',
                              'Seven community comment files absent; full live threads and all non-OP comments not claimed.',
                              '703 card-dropped original bodies remain unread here; no drop-body inspection claimed.',
                              'Prices, employment rules, benefit availability and product capabilities are historical author claims, not current advice.'],
           declared_theme_extensions=sorted(extensions),checks=dict(checks),errors=errors,failed=len(errors),
           strict_verify_quotes_output=strict.stdout.strip(),strict_verify_quotes_exit_code=strict.returncode,
           output_sha256={str(p.relative_to(R)):sha(p) for p in [voice_path,ledger_path,aux_path,S/'duplicate-review.jsonl',notes_path,source_path,R/'_raw/reddit-deep/triage/augdec-02.tsv'] if p.exists()},
           frozen_reading_chunk_hashes={c['file']:sha(S/c['file']) for c in chunks})
(R/'sources/reddit-augdec-02-verification.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'counts':counts,'failed':len(errors),'errors':errors[:12],'strict':strict.stdout.strip()},ensure_ascii=False,indent=2))
