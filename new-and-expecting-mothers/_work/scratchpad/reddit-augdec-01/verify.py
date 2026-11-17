#!/usr/bin/env python3
# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
"""Strict finite-scope audit of human decisions and completed native-source reads."""
from pathlib import Path
import collections
import csv
import datetime
import gzip
import hashlib
import json
import re
import subprocess
import sys

R = Path(__file__).resolve().parents[2]
S = Path(__file__).resolve().parent
W = R / '_raw/reddit-deep/aug-dec-2025-wave-v1'


def jl(p):
    return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def stamp(value):
    return datetime.datetime.fromtimestamp(int(value), datetime.timezone.utc).isoformat()


def url(native):
    v = native['permalink']
    return v if v.startswith('https://') else 'https://www.reddit.com' + v


def main():
    assignment = json.loads((W / 'assignments/batch-01.json').read_text())
    triage = list(csv.DictReader((R / '_raw/reddit-deep/triage/augdec-01.tsv').open(), delimiter='\t'))
    assigned = assignment['post_ids']
    assert len(assigned) == len(set(assigned)) == len(triage) == 2199
    assert {x['post_id'] for x in triage} == set(assigned)
    assert [x['post_id'] for x in triage] == [pid for c in assignment['chunks'] for pid in c['post_ids']]
    labels = {'keep_play', 'keep_solids', 'keep_pumping_work', 'keep_sleep', 'keep_postpartum', 'keep_pregnancy', 'keep_registry', 'keep_other', 'drop'}
    card_by_id = {pid: c['file'] for c in assignment['chunks'] for pid in c['post_ids']}
    for c in assignment['chunks']:
        assert sha(R / c['file']) == c['sha256']
    for t in triage:
        assert t['label'] in labels and t['reason'].strip()
        assert t['card_file'] == card_by_id[t['post_id']]
    keep = {x['post_id'] for x in triage if x['label'].startswith('keep_')}
    assert len(keep) == 1646
    frozen = json.loads((S / 'kept-reading-manifest.json').read_text())
    transfer_path = W / 'assignments/fullread-transfer-to-05-v1.json'
    transfer = json.loads(transfer_path.read_text())
    assert sha(S / 'kept-reading-manifest.json') == transfer['source_manifest_sha256']
    assert len(frozen['chunks']) == 97
    for c in frozen['chunks']:
        assert sha(R / c['file']) == c['sha256']
    owned_ids = [pid for c in frozen['chunks'][:72] for pid in c['post_ids']]
    tail_ids = [pid for c in frozen['chunks'][72:] for pid in c['post_ids']]
    assert frozen['chunks'][72:] == transfer['chunks']
    assert set(tail_ids) == set(transfer['post_ids'])
    assert len(owned_ids) == len(set(owned_ids)) == 1292
    assert len(tail_ids) == len(set(tail_ids)) == 354
    assert not set(owned_ids) & set(tail_ids)
    assert set(owned_ids) | set(tail_ids) == keep
    reading = jl(R / 'sources/reddit-augdec-01-reading.jsonl')
    assert [x['post_id'] for x in reading] == owned_ids
    ledger = {x['post_id']: x for x in reading}
    index = {x['post_id']: x for x in jl(W / 'primary-index.jsonl')}
    posts, comments, by_comment = {}, collections.defaultdict(list), {}
    owned = set(owned_ids)
    for relative in sorted({index[p]['source_post_file'] for p in owned}):
        with gzip.open(R / relative, 'rt') as stream:
            for line in stream:
                n = json.loads(line)
                if n['id'] in owned:
                    assert n['id'] not in posts
                    posts[n['id']] = n
    for relative in sorted({index[p]['source_comment_file'] for p in owned if index[p]['comment_source_available']}):
        with gzip.open(R / relative, 'rt') as stream:
            for line in stream:
                n = json.loads(line)
                pid = n.get('link_id', '').removeprefix('t3_')
                if pid in owned:
                    comments[pid].append(n)
                    assert n['id'] not in by_comment
                    by_comment[n['id']] = n
    assert set(posts) == owned
    for p, row in ledger.items():
        unit = index[p]
        author = posts[p].get('author')
        op = [c for c in comments[p] if author and author not in {'[deleted]', '[removed]'} and c.get('author') == author]
        expected = {c['id'] for c in op}
        assert row['post_body_read_complete'] is True
        assert type(row['available_identifiable_OP_replies_read']) is int
        assert row['available_identifiable_OP_replies_read'] == len(expected) == unit['OP_replies']
        assert len(row['op_reply_ids_read']) == len(set(row['op_reply_ids_read']))
        assert set(row['op_reply_ids_read']) == expected == set(unit['OP_comment_ids'])
        assert row['raw_file'] == unit['raw_file']
        assert sha(R / row['raw_file']) == row['primary_unit_sha256'] == unit['sha256']
        text = (R / row['raw_file']).read_text()
        title = text.split('=== COMPLETE ORIGINAL POST TITLE ===\n', 1)[1].split('\n\n=== COMPLETE ORIGINAL POST BODY ===', 1)[0]
        body, reply_section = text.split('=== COMPLETE ORIGINAL POST BODY ===\n', 1)[1].split('\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===', 1)
        assert title == posts[p].get('title', '')
        assert body == posts[p].get('selftext', ''), p
        assert unit['post_date'] == stamp(posts[p]['created_utc']) and unit['url'] == url(posts[p])
        blocks = reply_section.split('\n--- OP REPLY ---\n')[1:]
        assert len(blocks) == len(op)
        seen = set()
        for block in blocks:
            header, actual_body = block.split('\n', 1)
            meta = json.loads(header)
            native = by_comment[meta['comment_id']]
            assert native in op
            assert actual_body.startswith(native.get('body', ''))
            assert not actual_body[len(native.get('body', '')):].strip()
            assert meta['date'] == stamp(native['created_utc'])
            assert meta['parent_id'] == native['parent_id']
            seen.add(meta['comment_id'])
        assert seen == expected
        assert row['status'] in {'eligible', 'excluded_after_read', 'read_pending_topic_review'} and row['reason'].strip()
    quotes = jl(R / 'voice/reddit-augdec-01.jsonl')
    assert [q['id'] for q in quotes] == [f'rad01-{i:04d}' for i in range(1, len(quotes) + 1)]
    speakers = {'expecting_mother', 'new_mother', 'experienced_mother', 'parent_unspecified', 'partner', 'relative_caregiver', 'recovered_parent', 'gave_up_parent', 'advisor', 'professional', 'reviewer', 'skeptic'}
    stages = {'pregnancy_early', 'pregnancy_late', 'newborn_0_6_weeks', 'baby_6_16_weeks', 'baby_4_6_months', 'baby_6_12_months', 'toddler', 'return_to_work', 'looking_back', 'unknown'}
    types = {'trigger_moment', 'pain', 'fear', 'tried_failed', 'desire', 'belief', 'question', 'objection', 'advice_given', 'success_story', 'failure_story', 'regret', 'others_said'}
    quote_ids = {q['id'] for q in quotes}
    global_counts = collections.Counter(q['id'] for path in (R / 'voice').glob('*.jsonl') for q in jl(path))
    for q in quotes:
        p = q['post_id']
        assert p in ledger
        native = by_comment[q['comment_id']] if q.get('comment_id') else posts[p]
        native_body = native.get('body', '') if q.get('comment_id') else native.get('selftext', '')
        assert q['quote'] in native_body, q['id']
        assert q['date'] == stamp(native['created_utc']) and q['url'] == url(native), q['id']
        if q.get('comment_id'):
            assert q['comment_id'] in ledger[p]['op_reply_ids_read']
        assert q['raw_file'] == ledger[p]['raw_file']
        assert q['speaker'] in speakers and q['stage'] in stages and q['type'] in types
        assert isinstance(q['themes'], list) and q['themes'] and all(isinstance(t, str) for t in q['themes'])
        assert len(q['context'].split()) <= 25
        assert q['source_class'] == 'reddit_archive' and q['evidence_kind'] == 'archived_original'
        assert q['archive_dataset'] == 'yikeee/reddit-subreddits25'
        assert q['archive_commit'] == 'ea497c510aa68765c07ed744ec9f84d68bbedf7f'
        assert q['read_scope'] == ('full_post_and_available_identifiable_OP_replies' if index[p]['comment_source_available'] else 'full_post_comment_source_unavailable')
        assert global_counts[q['id']] == 1
        assert ledger[p]['post_body_read_complete'] is True
    for p, row in ledger.items():
        assert row['quote_ids'] == [q['id'] for q in quotes if q['post_id'] == p]
    auxiliary = jl(R / 'sources/reddit-augdec-01-auxiliary-read.jsonl')
    assert len(auxiliary) == len({a['comment_id'] for a in auxiliary}) == 5
    for a in auxiliary:
        native = json.loads((R / a['raw_file']).read_text())
        assert native == by_comment[a['comment_id']]
        assert native['link_id'] == 't3_' + a['post_id']
        assert native.get('author') != posts[a['post_id']].get('author')
        assert a['full_comment_read'] is True and sha(R / a['raw_file']) == a['sha256']
    baseline = json.loads((R / '_raw/reddit-deep/final-read-post-ids.json').read_text())
    assert not owned & set(baseline['full_original_post_ids'])
    note = R / 'synthesis/reader-notes-reddit-augdec-01.md'
    note_refs = set(re.findall(r'rad01-\d{4}', note.read_text())) if note.exists() else set()
    assert note.exists() and note_refs and note_refs <= quote_ids
    result = subprocess.run([sys.executable, str(R / '_tools/verify_quotes.py'), str(R / 'voice/reddit-augdec-01.jsonl')], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    report = {
        'date': '2026-10-24', 'scope': 'all 2199 assigned cards; owned complete reading of frozen chunks001-072; chunks073-097 transferred unread to reader05',
        'assigned_and_triaged_cards': len(triage), 'triage_labels': dict(collections.Counter(x['label'] for x in triage)),
        'original_kept_batch_total': len(keep), 'card_drops_original_unread_by_this_reader': len(triage) - len(keep),
        'owned_full_original_posts': len(reading), 'owned_partial_original_posts': 0,
        'transferred_full_read_units': len(tail_ids), 'transfer_manifest': str(transfer_path.relative_to(R)),
        'transfer_manifest_sha256': sha(transfer_path), 'ownership_disjoint_union_equals_original_keeps': True,
        'owned_OP_replies_read': sum(x['available_identifiable_OP_replies_read'] for x in reading),
        'owned_auxiliary_comments_read': len(auxiliary), 'owned_statuses': dict(collections.Counter(x['status'] for x in reading)),
        'owned_source_communities': dict(collections.Counter(index[p]['subreddit'] for p in owned_ids)),
        'own_primary_unit_utf8_bytes': sum(index[p]['utf8_bytes'] for p in owned_ids),
        'own_primary_original_body_bytes': sum(index[p]['body_bytes'] for p in owned_ids),
        'quotes': len(quotes), 'quoted_post_ids': len({q['post_id'] for q in quotes}),
        'quoted_OP_replies': sum(bool(q.get('comment_id')) for q in quotes),
        'research_only_quote_ids': [q['id'] for q in quotes if q.get('marketing_eligible') is False],
        'reader_note_ids_checked': len(note_refs), 'native_body_dates_URLs_OP_attribution_hashes_and_global_own_ID_uniqueness': 'passed',
        'verify_quotes_stdout': result.stdout.strip(), 'voice_sha256': sha(R / 'voice/reddit-augdec-01.jsonl'),
        'reading_sha256': sha(R / 'sources/reddit-augdec-01-reading.jsonl'), 'failed': 0,
        'limitations': 'Machine checks substantiate finite saved-source coverage and excerpt attribution; human reading, safety judgment and truth of self-report are not established by substring checks. No live follow-up completeness, independent buyers, receipts, clinical efficacy or market prevalence claimed.'}
    (R / 'sources/reddit-augdec-01-verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
