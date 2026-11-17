#!/usr/bin/env python3
"""Verify the completed finite B comparison against native saved post/reply bodies."""
from pathlib import Path
import collections
import csv
import datetime
import gzip
import hashlib
import json

R = Path(__file__).resolve().parents[1]
P = R / '_raw/reddit-deep/july-B-solids-v1'


def jl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def stamp(value):
    return datetime.datetime.fromtimestamp(int(value), datetime.timezone.utc).isoformat()


def main():
    candidates = {row['id'] for row in jl(P / 'candidates.jsonl')}
    all_b = {row['id'] for row in jl(R / '_raw/reddit-deep/filter-v1/B-candidates.jsonl')
             if row['subreddit'] == 'BabyLedWeaning' and row['date'].startswith('2025-07-')}
    assert candidates == all_b and len(candidates) == 178
    triage = list(csv.DictReader((R / '_raw/reddit-deep/triage/july-B-solids.tsv').open(), delimiter='\t'))
    assert len(triage) == len({row['post_id'] for row in triage}) == 178
    assert {row['post_id'] for row in triage} == candidates
    kept = {row['post_id'] for row in triage if row['label'].startswith('keep_')}
    reading = jl(R / 'sources/reddit-july-B-solids-reading.jsonl')
    assert len(reading) == len({row['post_id'] for row in reading}) == 126
    assert {row['post_id'] for row in reading} == kept
    ledger = {row['post_id']: row for row in reading}
    index = {row['post_id']: row for row in jl(P / 'primary-index.jsonl')}
    posts = {}
    comments = collections.defaultdict(list)
    by_comment = {}
    with gzip.open(R / '_raw/reddit-deep/windows/2025-h2-v1/BabyLedWeaning_submissions.jsonl.gz', 'rt') as stream:
        for line in stream:
            row = json.loads(line)
            if row['id'] in candidates:
                posts[row['id']] = row
    with gzip.open(R / '_raw/reddit-deep/windows/2025-h2-v1/BabyLedWeaning_comments.jsonl.gz', 'rt') as stream:
        for line in stream:
            row = json.loads(line)
            pid = row.get('link_id', '').removeprefix('t3_')
            if pid in candidates:
                comments[pid].append(row)
                by_comment[row['id']] = row
    for row in reading:
        pid = row['post_id']
        post = posts[pid]
        author = post.get('author')
        op = [comment for comment in comments[pid]
              if author and author not in {'[deleted]', '[removed]'} and comment.get('author') == author]
        expected = {comment['id'] for comment in op}
        assert row['post_body_read_complete'] is True
        assert set(row['op_reply_ids_read']) == expected
        assert row['available_identifiable_OP_replies_read'] == len(expected)
        path = R / row['raw_file']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row['primary_unit_sha256'] == index[pid]['sha256']
        text = path.read_text()
        body = text.split('=== COMPLETE ORIGINAL POST BODY ===\n', 1)[1].split('\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===', 1)[0]
        assert body == post.get('selftext', ''), pid
        for comment in op:
            assert comment.get('body', '') in text
    quotes = jl(R / 'voice/reddit-july-B-solids.jsonl')
    assert len(quotes) == len({row['id'] for row in quotes}) == 47
    for row in quotes:
        pid = row['post_id']
        assert pid in ledger
        native = by_comment[row['comment_id']] if row.get('comment_id') else posts[pid]
        body = native.get('body', '') if row.get('comment_id') else native.get('selftext', '')
        assert row['quote'] in body, row['id']
        assert row['date'] == stamp(native['created_utc'])
        if row.get('comment_id'):
            assert row['comment_id'] in ledger[pid]['op_reply_ids_read']
            expected_url = native['permalink'] if native['permalink'].startswith('https://') else 'https://www.reddit.com' + native['permalink']
        else:
            expected_url = 'https://www.reddit.com' + native['permalink']
        assert row['url'] == expected_url, row['id']
        assert row['raw_file'] == ledger[pid]['raw_file']
        assert len(row['context'].split()) <= 25
        assert ledger[pid]['post_body_read_complete'] is True
    auxiliary = jl(R / 'sources/reddit-july-B-solids-auxiliary-read.jsonl')
    assert len(auxiliary) == len({row['comment_id'] for row in auxiliary}) == 5
    for row in auxiliary:
        raw = R / row['raw_file']
        native = json.loads(raw.read_text())
        assert native == by_comment[row['comment_id']]
        assert native['link_id'] == 't3_' + row['post_id']
        assert hashlib.sha256(raw.read_bytes()).hexdigest() == row['sha256']
        assert native.get('author') != posts[row['post_id']].get('author')
        assert row['full_comment_read'] is True
    baseline = json.loads((R / '_raw/reddit-deep/final-read-post-ids.json').read_text())
    assert not kept.intersection(baseline['full_original_post_ids'])
    report = {'date': '2026-10-24', 'scope': 'all July2025 BabyLedWeaning B cards, then all human keeps',
              'cards': 178, 'initially_kept': len(kept), 'card_exclusions_original_unread': 178 - len(kept),
              'full_original_posts': len(reading),
              'OP_replies_read': sum(row['available_identifiable_OP_replies_read'] for row in reading),
              'auxiliary_comments_read': len(auxiliary),
              'excluded_after_full_read': sum(row['status'] != 'eligible' for row in reading),
              'eligible_after_full_read': sum(row['status'] == 'eligible' for row in reading),
              'quotes': len(quotes), 'quoted_post_ids': len({row['post_id'] for row in quotes}),
              'research_only_quote_ids': [row['id'] for row in quotes if row.get('marketing_eligible') is False],
              'native_body_date_URL_OP_attribution_and_hash_checks': 'passed',
              'voice_sha256': hashlib.sha256((R / 'voice/reddit-july-B-solids.jsonl').read_bytes()).hexdigest(),
              'failed': 0}
    (R / 'sources/reddit-july-B-solids-verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
