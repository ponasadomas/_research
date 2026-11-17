#!/usr/bin/env python3
"""Freeze ALL July BabyLedWeaning B posts as a declared filter-bias comparison."""
from pathlib import Path
import collections
import datetime
import gzip
import hashlib
import json

R = Path(__file__).resolve().parents[1]
RAW = R / '_raw/reddit-deep'
OUT = RAW / 'july-B-solids-v1'


def rel(path):
    return str(path.relative_to(R))


def stamp(value):
    return datetime.datetime.fromtimestamp(int(value), datetime.timezone.utc).isoformat()


def jl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main():
    if OUT.exists():
        raise SystemExit('Frozen comparison exists; do not rebuild.')
    selected = {row['id']: row for row in jl(RAW / 'filter-v1/B-candidates.jsonl')
                if row['subreddit'] == 'BabyLedWeaning' and row['date'].startswith('2025-07-')}
    assert len(selected) == 178
    prior = json.loads((RAW / 'final-read-post-ids.json').read_text())
    assert not set(selected).intersection(prior['full_original_post_ids'])
    posts = {}
    native = RAW / 'windows/2025-h2-v1/BabyLedWeaning_submissions.jsonl.gz'
    with gzip.open(native, 'rt') as stream:
        for line in stream:
            row = json.loads(line)
            if row['id'] in selected:
                posts[row['id']] = row
    assert set(posts) == set(selected)
    comments = collections.defaultdict(list)
    native_comments = RAW / 'windows/2025-h2-v1/BabyLedWeaning_comments.jsonl.gz'
    with gzip.open(native_comments, 'rt') as stream:
        for line in stream:
            row = json.loads(line)
            pid = row.get('link_id', '').removeprefix('t3_')
            if pid in selected:
                comments[pid].append(row)
    OUT.mkdir()
    for folder in ['primary-units', 'cards']:
        (OUT / folder).mkdir()
    index = []
    cards = []
    for pid in sorted(selected, key=lambda p: (int(selected[p]['created_utc']), p)):
        post = posts[pid]
        author = post.get('author')
        known = bool(author and author not in {'[deleted]', '[removed]'})
        op = sorted([row for row in comments[pid] if known and row.get('author') == author],
                    key=lambda row: (int(row['created_utc']), row['id']))
        aux = [row for row in comments[pid] if row['id'] not in {reply['id'] for reply in op}]
        meta = {'post_id': pid, 'subreddit': 'BabyLedWeaning', 'url': selected[pid]['url'],
                'date': stamp(post['created_utc']), 'title': post.get('title', ''),
                'source_post_file': rel(native), 'source_comment_file': rel(native_comments),
                'read_scope': 'complete_original_post_plus_all_available_identifiable_OP_replies',
                'OP_replies': len(op), 'OP_comment_ids': [row['id'] for row in op],
                'non_OP_comments_unread': len(aux), 'source_window_end_exclusive': '2026-01-01T00:00:00+00:00',
                'selection': 'every July2025 BabyLedWeaning B record; no rank, cap or human keep yet',
                'publisher_provenance_license_and_live_completeness': 'unverified'}
        text = 'ARCHIVED ORIGINAL — JULY B FILTER-BIAS COMPARISON\n' + json.dumps(meta, ensure_ascii=False, indent=2)
        text += '\n\n=== COMPLETE ORIGINAL POST TITLE ===\n' + post.get('title', '')
        text += '\n\n=== COMPLETE ORIGINAL POST BODY ===\n' + post.get('selftext', '')
        text += '\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===\n'
        if not op:
            text += 'No identifiable OP replies in saved archive; not proof none existed live.\n'
        for row in op:
            cm = {'comment_id': row['id'], 'date': stamp(row['created_utc']), 'parent_id': row.get('parent_id'),
                  'url': f"https://www.reddit.com/r/BabyLedWeaning/comments/{pid}/_/{row['id']}/"}
            text += '\n--- OP REPLY ---\n' + json.dumps(cm, ensure_ascii=False) + '\n' + row.get('body', '') + '\n'
        path = OUT / 'primary-units' / f'BabyLedWeaning-{pid}.txt'
        path.write_text(text)
        index.append({**meta, 'raw_file': rel(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                      'utf8_bytes': path.stat().st_size, 'non_OP_comment_ids': [row['id'] for row in aux]})
        body = post.get('selftext', '')
        cards.append((pid, f"ID {pid} | {meta['date']} | safety_flag={selected[pid]['safety_flag']}\nTITLE: {post.get('title','')}\nOPENING: {body[:350]}\n\n"))
    card_index = []
    buffer = ''
    ids = []
    def flush():
        path = OUT / 'cards' / f'cards-{len(card_index)+1:02}.txt'
        path.write_text(buffer)
        card_index.append({'file': rel(path), 'post_ids': list(ids), 'utf8_bytes': path.stat().st_size})
    for pid, card in cards:
        if buffer and len((buffer + card).encode()) > 18000:
            flush()
            buffer = ''
            ids = []
        buffer += card
        ids.append(pid)
    if buffer:
        flush()
    for name, rows in [('candidates.jsonl', list(selected.values())), ('primary-index.jsonl', index), ('cards-index.jsonl', card_index)]:
        (OUT / name).write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows))
    summary = {'scope': 'all July2025 BabyLedWeaning B records, not selected for asking for a report',
               'baseline_commit': '2613feb3', 'candidates': len(selected), 'card_chunks': len(card_index),
               'primary_bytes': sum(row['utf8_bytes'] for row in index),
               'OP_replies': sum(row['OP_replies'] for row in index),
               'non_OP_comments_unread': sum(row['non_OP_comments_unread'] for row in index),
               'human_triaged': 0, 'human_kept': 0, 'primary_reads': 0}
    (OUT / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
