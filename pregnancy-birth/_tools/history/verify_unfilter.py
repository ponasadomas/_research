#!/usr/bin/env python3
"""Check the unfilter restoration against original voice records and its queue.

Run with python3 -I. This never opens source bodies or changes any file.
Historical subject labels do not affect evidence eligibility.
"""
from pathlib import Path
import csv
import json
import re
import sys

BUILD = Path(__file__).resolve().parent.parent
ID = re.compile(r'\bpb(?:\d{2}|r1)-\d{4}\b')


def norm(text):
    # Only whitespace changes are allowed; retain spelling, case and punctuation.
    return ' '.join(text.split())


def main():
    voice = {}
    for path in sorted((BUILD / 'voice').glob('*.jsonl')):
        for line in path.read_text().splitlines():
            if line.strip():
                rec = json.loads(line)
                voice[rec['id']] = rec
    text = (BUILD / 'synthesis/findings.md').read_text()
    normalized = norm(text)
    marked = set(ID.findall((BUILD / 'synthesis/restricted-ids.md').read_text()))
    cited = set(ID.findall(text))
    unresolved = cited - voice.keys()
    absent = [qid for qid in sorted(marked)
              if qid not in voice or norm('"' + voice[qid]['quote'] + '" [' + qid + ']') not in normalized]
    print(f'{len(cited)} explicit ids, {len(unresolved)} unresolved; '
          f'{len(marked)} historically marked full quotes, {len(absent)} missing or changed')
    for qid in sorted(unresolved):
        print('UNRESOLVED', qid)
    for qid in absent:
        print('FULL QUOTE MISSING OR CHANGED', qid)
    rows = list(csv.DictReader((BUILD / 'scratchpad/unfilter-reread/queue.tsv').open(), delimiter='\t'))
    expected_header = ['kind', 'id', 'why_it_was_dropped']
    problems = sum(list(row) != expected_header or row['kind'] not in {'unit', 'post'}
                   or not row['why_it_was_dropped'].strip() or not row['id'].strip() for row in rows)
    keys = [row['id'] for row in rows]
    duplicates = len(keys) - len(set(keys))
    queue_keys = set(keys)
    safety = set()
    for path in (BUILD / '_raw/reddit').glob('filter-*/safety-candidates.jsonl'):
        for line in path.read_text().splitlines():
            if line.strip():
                rec = json.loads(line)
                safety.add(rec['subreddit'] + '-' + rec['id'])
    omitted_safety = safety - queue_keys
    merged = [json.loads(line) for line in (BUILD / 'voice-merged/all.jsonl').read_text().splitlines() if line.strip()]
    active = sum(rec.get('restricted') is True for rec in merged)
    legacy_labels = '(restricted)' in text
    print(f'{len(rows)} queue rows, {duplicates} duplicate ids, {problems} malformed rows; '
          f'{len(safety)} safety-routed posts, {len(omitted_safety)} absent from queue')
    print(f'{active} active merged restrictions; {int(legacy_labels)} old findings labels')
    return bool(unresolved or absent or duplicates or problems or omitted_safety or active or legacy_labels)


if __name__ == '__main__':
    sys.exit(main())
