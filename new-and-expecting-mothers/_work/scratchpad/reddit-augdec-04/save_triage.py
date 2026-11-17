"""Persist explicit human decisions and reject missing/duplicate display IDs."""
from pathlib import Path
import csv
import json

R = Path(__file__).resolve().parents[2]
P = Path(__file__).resolve().parent


def save(parts, text):
    views = [json.loads(line) for line in (P / 'card-views-index.jsonl').read_text().splitlines()]
    wanted = {pid for number in parts for pid in views[number - 1]['post_ids']}
    source = {pid: row['source_card_file'] for row in views for pid in row['post_ids']}
    rows = []
    for line in text.strip().splitlines():
        pid, label, reason = line.split('\t', 2)
        rows.append({'post_id': pid, 'label': label, 'reason': reason, 'card_file': source[pid]})
    assert len(rows) == len(wanted) == len({row['post_id'] for row in rows})
    assert {row['post_id'] for row in rows} == wanted
    path = R / '_raw/reddit-deep/triage/augdec-04.tsv'
    prior = list(csv.DictReader(path.open(), delimiter='\t')) if path.exists() else []
    assert not {row['post_id'] for row in prior}.intersection(wanted)
    with path.open('a') as stream:
        writer = csv.DictWriter(stream, fieldnames=['post_id', 'label', 'reason', 'card_file'], delimiter='\t')
        if not prior:
            writer.writeheader()
        writer.writerows(rows)
    print('Human decisions saved:', len(rows), '; cumulative', len(prior) + len(rows), '/620')
