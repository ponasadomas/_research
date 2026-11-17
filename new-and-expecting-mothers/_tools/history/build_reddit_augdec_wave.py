#!/usr/bin/env python3
"""Freeze every remaining outside-July A card and full post/OP-reply unit.

Local existing sources only. Does not make human keep/read decisions. Existing
corpora and the committed baseline inventories are never rewritten.
"""
from pathlib import Path
import collections
import datetime
import gzip
import hashlib
import json
import re

R = Path(__file__).resolve().parents[1]
RAW = R / '_raw/reddit-deep'
OUT = RAW / 'aug-dec-2025-wave-v1'


def jl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def rel(path):
    return str(path.relative_to(R))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stamp(value):
    return datetime.datetime.fromtimestamp(int(value), datetime.timezone.utc).isoformat()


def savejl(name, rows):
    (OUT / name).write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows))


def main():
    if OUT.exists():
        raise SystemExit('Frozen packet already exists; do not rebuild.')
    frozen = [RAW / name for name in ['final-unhandled-A.jsonl', 'final-read-post-ids.json',
              'outside-july-card-queue-v1.jsonl', 'filter-v1/A-candidates.jsonl',
              'corpus-A-v1/index.jsonl']]
    hashes = {rel(path): digest(path) for path in frozen}
    selected = {row['post_id'] for row in jl(RAW / 'final-unhandled-A.jsonl')}
    previous = json.loads((RAW / 'final-read-post-ids.json').read_text())
    assert len(selected) == 6597 and not selected.intersection(previous['full_original_post_ids'])
    candidates = {row['id']: row for row in jl(RAW / 'filter-v1/A-candidates.jsonl') if row['id'] in selected}
    queue = jl(RAW / 'outside-july-card-queue-v1.jsonl')
    assert set(candidates) == selected == {pid for row in queue for pid in row['untriaged_outside_july_ids']}
    OUT.mkdir()
    for folder in ['triage-cards', 'primary-units', 'assignments']:
        (OUT / folder).mkdir()
    cards = []
    for row in queue:
        source = R / row['file']
        segments = re.split(r'(?m)(?=^ID [a-z0-9]+ \| r/)', source.read_text())
        wanted = set(row['untriaged_outside_july_ids'])
        found = {}
        for segment in segments:
            match = re.match(r'ID ([a-z0-9]+) \| r/', segment)
            if match and match.group(1) in wanted:
                found[match.group(1)] = segment
        assert set(found) == wanted
        path = OUT / 'triage-cards' / source.name
        path.write_text(''.join(found[pid] for pid in row['untriaged_outside_july_ids']))
        cards.append({'file': rel(path), 'source_card_file': row['file'],
                      'post_ids': row['untriaged_outside_july_ids'], 'cards': len(wanted),
                      'utf8_bytes': path.stat().st_size, 'sha256': digest(path)})
    # Greedy byte-balanced assignment keeps every card exactly once. No topic or
    # score ranking is used to remove candidates.
    batches = [[] for _ in range(3)]
    loads = [0, 0, 0]
    for card in sorted(cards, key=lambda row: (-row['utf8_bytes'], row['file'])):
        index = min(range(3), key=lambda i: (loads[i], len(batches[i]), i))
        batches[index].append(card)
        loads[index] += card['utf8_bytes']
    ownership = {}
    for number, batch in enumerate(batches, 1):
        batch.sort(key=lambda row: row['file'])
        for card in batch:
            for pid in card['post_ids']:
                assert pid not in ownership
                ownership[pid] = number
        manifest = {'batch': number, 'selection': 'all remaining outside-July A IDs; no ranking or cap',
                    'cards': sum(row['cards'] for row in batch), 'card_chunks': len(batch),
                    'card_bytes': sum(row['utf8_bytes'] for row in batch), 'chunks': batch,
                    'post_ids': sorted(pid for card in batch for pid in card['post_ids'])}
        (OUT / 'assignments' / f'batch-{number:02}.json').write_text(json.dumps(manifest, indent=2) + '\n')
    posts = {}
    body_groups = collections.defaultdict(list)
    for path in sorted((RAW / 'windows/2025-h2-v1').glob('*_submissions.jsonl.gz')):
        with gzip.open(path, 'rt') as stream:
            for line in stream:
                post = json.loads(line)
                body = post.get('selftext', '')
                if len(body.strip()) >= 100:
                    key = hashlib.sha256(' '.join(body.lower().split()).encode()).hexdigest()
                    body_groups[key].append({'post_id': post['id'], 'subreddit': post['subreddit'],
                                             'date': stamp(post['created_utc']), 'title': post.get('title', '')})
                if post['id'] in selected:
                    posts[post['id']] = (post, path)
    assert set(posts) == selected
    replies = collections.defaultdict(list)
    comments = collections.defaultdict(list)
    comment_sources = {}
    for path in sorted((RAW / 'windows/2025-h2-v1').glob('*_comments.jsonl.gz')):
        sub = path.name.split('_comments')[0]
        comment_sources[sub] = path
        with gzip.open(path, 'rt') as stream:
            for line in stream:
                comment = json.loads(line)
                pid = comment.get('link_id', '').removeprefix('t3_')
                if pid in selected:
                    comments[pid].append(comment)
                    author = posts[pid][0].get('author')
                    if author and author not in {'[deleted]', '[removed]'} and comment.get('author') == author:
                        replies[pid].append(comment)
    index = []
    for pid in sorted(selected, key=lambda p: (candidates[p]['subreddit'], int(candidates[p]['created_utc']), p)):
        post, native = posts[pid]
        candidate = candidates[pid]
        sub = candidate['subreddit']
        available = sub in comment_sources
        op = sorted(replies[pid], key=lambda row: (int(row['created_utc']), row['id']))
        aux = [row for row in comments[pid] if row['id'] not in {reply['id'] for reply in op}]
        meta = {'post_id': pid, 'subreddit': sub, 'url': candidate['url'],
                'post_date': stamp(post['created_utc']), 'title': post.get('title', ''),
                'batch': ownership[pid], 'source_post_file': rel(native),
                'source_comment_file': rel(comment_sources[sub]) if available else None,
                'comment_source_available': available,
                'primary_read_scope': 'complete_original_post_plus_all_available_identifiable_OP_replies' if available else 'complete_original_post_only_comment_source_unavailable',
                'source_window_end_exclusive': '2026-01-01T00:00:00+00:00',
                'OP_replies': len(op), 'OP_comment_ids': [reply['id'] for reply in op],
                'non_OP_comments_unread': len(aux), 'non_OP_comment_ids': [row['id'] for row in aux],
                'post_reported_num_comments': post.get('num_comments'),
                'primary_topic': candidate['primary_topic'], 'topics': candidate['topics'],
                'safety_flag': candidate['safety_flag'],
                'publisher_provenance_license_and_live_completeness': 'unverified'}
        text = 'ARCHIVED ORIGINAL — AUGUST–DECEMBER PRIMARY UNIT\n' + json.dumps(meta, ensure_ascii=False, indent=2)
        text += '\n\n=== COMPLETE ORIGINAL POST TITLE ===\n' + post.get('title', '')
        text += '\n\n=== COMPLETE ORIGINAL POST BODY ===\n' + post.get('selftext', '')
        text += '\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===\n'
        if not available:
            text += 'The publisher comment file is unavailable; no live follow-up completeness is claimed.\n'
        elif not op:
            text += 'No identifiable OP replies in the available frozen archive; not proof none existed live.\n'
        for reply in op:
            cm = {'comment_id': reply['id'], 'date': stamp(reply['created_utc']),
                  'parent_id': reply.get('parent_id'),
                  'url': f"https://www.reddit.com/r/{sub}/comments/{pid}/_/{reply['id']}/"}
            text += '\n--- OP REPLY ---\n' + json.dumps(cm, ensure_ascii=False) + '\n' + reply.get('body', '') + '\n'
        path = OUT / 'primary-units' / f'{sub}-{pid}.txt'
        path.write_text(text)
        index.append({**meta, 'raw_file': rel(path), 'utf8_bytes': path.stat().st_size,
                      'body_bytes': len(post.get('selftext', '').encode()), 'sha256': digest(path)})
    duplicates = [group for group in body_groups.values() if len(group) > 1 and any(row['post_id'] in selected for row in group)]
    savejl('candidates.jsonl', [candidates[pid] for pid in sorted(selected)])
    savejl('cards-index.jsonl', cards)
    savejl('primary-index.jsonl', index)
    savejl('exact-body-duplicate-flags.jsonl', [{'records': group, 'human_review_required': True} for group in duplicates])
    summary = {'date': '2026-10-24', 'baseline_commit': '2613feb3', 'candidates': len(selected),
               'card_chunks': len(cards), 'by_subreddit': dict(collections.Counter(row['subreddit'] for row in index)),
               'primary_units': len(index), 'primary_bytes': sum(row['utf8_bytes'] for row in index),
               'OP_replies': sum(row['OP_replies'] for row in index),
               'non_OP_comments_separate_unread': sum(row['non_OP_comments_unread'] for row in index),
               'duplicate_body_groups_for_human_review': len(duplicates),
               'card_triaged': 0, 'human_kept': 0, 'full_primary_reads': 0,
               'batch_cards': [sum(row['cards'] for row in batch) for batch in batches],
               'batch_chunks': [len(batch) for batch in batches], 'baseline_hashes': hashes}
    assert all(digest(R / path) == value for path, value in hashes.items())
    (OUT / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
