#!/usr/bin/env python3
"""Resolve full-body read status against the saved per-id ledger and body hashes."""
from pathlib import Path
import csv,hashlib,json
ROOT=Path(__file__).resolve().parents[1]

def body_read_ids(rows,initially_selected=()):
    ledger=ROOT/'sources/ad-body-reading-ledger.tsv'
    if not ledger.exists():
        return {str(a['id']) for a in initially_selected}
    entries=list(csv.DictReader(ledger.open(),delimiter='\t'))
    ids=[e['id'] for e in entries]
    if len(ids)!=len(set(ids)):
        raise ValueError('Duplicate ids in ad-body reading ledger')
    by_id={str(a['id']):a for a in rows};read=set()
    for e in entries:
        a=by_id.get(e['id'])
        if not a or e['read_status']!='full_body_read' or a['raw_file']!=e['raw_file']:
            continue
        raw=ROOT/e['raw_file']
        if raw.exists() and hashlib.sha256(raw.read_bytes()).hexdigest()==e['body_sha256']:
            read.add(e['id'])
    return read

if __name__=='__main__':
    rows=[json.loads(l) for l in (ROOT/'_raw/ads-running/on-topic-ads.jsonl').read_text().splitlines() if l]
    read=body_read_ids(rows)
    print(f'{len(read)} retained bodies read; {len(rows)-len(read)} retained bodies unread; {len(rows)} retained ids')
