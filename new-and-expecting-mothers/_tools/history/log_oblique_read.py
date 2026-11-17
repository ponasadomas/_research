#!/usr/bin/env python3
"""Log a completed manual chunk read; does not infer read status from capture.

Research retains every subject in the speaker’s own words. The owner decides
later what to use in copy; unselected units only record scope/duplicate decisions."""
import sys,json,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];RAW=ROOT/'_raw/oblique-deep'
def log(prefix,number,note,unselected_threads=None):
 target=f'_raw/oblique-deep/corpus/{prefix}-chunk-{number:03}.txt'
 dest=ROOT/'sources/oblique-deep-reading-ledger.jsonl'
 old=[json.loads(s) for s in dest.read_text().splitlines()] if dest.exists() else []
 assert not any(r['file']==target for r in old),'Already logged'
 c=next(json.loads(s) for s in (RAW/'corpus'/f'{prefix}-chunks.jsonl').read_text().splitlines() if json.loads(s)['file']==target)
 threads=[json.loads((RAW/'threads'/f'{prefix}-{tid}.json').read_text()) for tid in c['thread_ids']]
 quotes=[json.loads(s)['id'] for s in (ROOT/'voice/oblique-deep-01.jsonl').read_text().splitlines() if json.loads(s)['raw_file']==target]
 rec={'file':target,'reader':'reviews_media','status':'read_complete','thread_ids':c['thread_ids'],'threads':len(threads),'pages':sum(len(t['pages']) for t in threads),'posts':sum(t['post_count'] for t in threads),'bytes':c['bytes'],'parts':c['parts'],'read_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'quotes':quotes,'unselected_units':unselected_threads or {},'note':note}
 with dest.open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
 print(target,rec['threads'],rec['posts'])
if __name__=='__main__':log(sys.argv[1],int(sys.argv[2]),sys.argv[3])
