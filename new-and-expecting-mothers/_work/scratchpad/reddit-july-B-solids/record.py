# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
"""Record explicit human-read chunks and manually selected quotations only."""
from pathlib import Path
import hashlib
import json
import sys

R = Path(__file__).resolve().parents[2]
P = Path(__file__).resolve().parent
RAW = R / '_raw/reddit-deep/july-B-solids-v1'


def jl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()] if path.exists() else []


def read_chunks(numbers, exclusions=None):
    exclusions = exclusions or {}
    index = {row['post_id']: row for row in jl(RAW / 'primary-index.jsonl')}
    chunks = jl(P / 'kept-reading-chunks.jsonl')
    output = R / 'sources/reddit-july-B-solids-reading.jsonl'
    old = jl(output)
    done = {row['post_id'] for row in old}
    new = []
    for number in numbers:
        for pid in chunks[number - 1]['post_ids']:
            assert pid not in done, 'Never repeat a read ledger entry'
            done.add(pid)
            row = index[pid]
            assert hashlib.sha256((R / row['raw_file']).read_bytes()).hexdigest() == row['sha256']
            new.append({'post_id': pid, 'raw_file': row['raw_file'],
                        'post_body_read_complete': True,
                        'available_identifiable_OP_replies_read': row['OP_replies'],
                        'op_reply_ids_read': row['OP_comment_ids'],
                        'primary_unit_sha256': row['sha256'],
                        'status': 'read_pending_topic_review' if pid in exclusions else 'eligible',
                        'reason': exclusions.get(pid, 'Ordinary comparison context; no individualized health advice or purchase inferred.'),
                        'read_chunk': number, 'reader': 'root'})
    with output.open('a') as stream:
        for row in new:
            stream.write(json.dumps(row, ensure_ascii=False) + '\n')
    print('Recorded', len(new), 'complete primary units; cumulative', len(old) + len(new))


def quotes(items):
    index = {row['post_id']: row for row in jl(RAW / 'primary-index.jsonl')}
    ledger = {row['post_id']: row for row in jl(R / 'sources/reddit-july-B-solids-reading.jsonl')}
    output = R / 'voice/reddit-july-B-solids.jsonl'
    previous = jl(output)
    new = []
    for item in items:
        row = index[item['post_id']]
        assert ledger[item['post_id']]['post_body_read_complete'] is True
        text = (R / row['raw_file']).read_text()
        body = text.split('=== COMPLETE ORIGINAL POST BODY ===\n', 1)[1].split('\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===', 1)[0]
        meta = {'url': row['url'], 'date': row['date']}
        if item.get('comment_id'):
            for part in text.split('\n--- OP REPLY ---\n')[1:]:
                first, content = part.split('\n', 1)
                m = json.loads(first)
                if m['comment_id'] == item['comment_id']:
                    body = content
                    meta = m
                    break
            else:
                raise AssertionError('Comment must be an identifiable OP reply')
        assert item['quote'] in body, item['quote']
        assert len(item['context'].split()) <= 25
        quote = {'id': f'rbc01-{len(previous) + len(new) + 1:04}',
                 'source': 'Reddit r/BabyLedWeaning — July B comparison',
                 'url': meta['url'], 'date': meta['date'],
                 'speaker': item['speaker'], 'stage': item['stage'], 'type': item['type'],
                 'themes': item['themes'], 'quote': item['quote'], 'context': item['context'],
                 'raw_file': row['raw_file'], 'source_class': 'reddit_archive',
                 'evidence_kind': 'archived_original', 'archive_dataset': 'yikeee/reddit-subreddits25',
                 'archive_commit': 'ea497c510aa68765c07ed744ec9f84d68bbedf7f',
                 'post_id': row['post_id'], 'read_scope': 'full_post_and_available_identifiable_OP_replies',
                 'selection_scope': 'all July2025 BabyLedWeaning B cards, then human kept full reads'}
        if item.get('comment_id'):
            quote['comment_id'] = item['comment_id']
        for key in ['related_post_ids']:
            if key in item:
                quote[key] = item[key]
        new.append(quote)
    with output.open('a') as stream:
        for row in new:
            stream.write(json.dumps(row, ensure_ascii=False) + '\n')
            print(row['id'], row['post_id'], row.get('comment_id', 'OP'))


if __name__ == '__main__':
    raise SystemExit('Import and pass explicit human decisions; no automatic read/quote selection.')
