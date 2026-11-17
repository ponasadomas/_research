#!/usr/bin/env python3
"""Inspect and locally date-filter independently published Reddit JSONL.zst shards.

Use Python 3.12 with zstandard available. Raw compressed bytes stay untouched.
Publisher manifest/provenance captures and download hashes are separate source records.
No live Reddit requests, keyword ranking, proxies or credential handling occur here.
"""
from pathlib import Path
import argparse, collections, concurrent.futures, datetime, gzip, hashlib, io, json, os, shutil, sys
try:
    import zstandard
except ImportError:
    sys.path.insert(0,'/tmp/mamivio-reddit-packages')
    import zstandard

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'_raw/reddit-deep'

def records(path):
    with path.open('rb') as f, zstandard.ZstdDecompressor(max_window_size=2**31).stream_reader(f) as rd:
        for line in io.TextIOWrapper(rd,encoding='utf8'):
            if line.strip(): yield line

def date(ts):
    return datetime.datetime.fromtimestamp(int(ts),datetime.timezone.utc).isoformat()

def scan(path):
    stats={'file':str(path.relative_to(ROOT)),'records':0,'invalid_json':0,'missing_date':0,'months':{},'text_status':{},'subreddits':{},'timestamp_decreases':0}
    months=collections.Counter();statuses=collections.Counter();subs=collections.Counter();lo=None;hi=None;last=None;keys=None
    for line in records(path):
        try:q=json.loads(line)
        except Exception:stats['invalid_json']+=1;continue
        stats['records']+=1;keys=keys or list(q)
        text=q.get('selftext',q.get('body',''))
        statuses['removed' if text=='[removed]' else 'deleted' if text=='[deleted]' else 'empty' if not text else 'present']+=1
        subs[q.get('subreddit','MISSING')]+=1
        try:ts=int(q['created_utc'])
        except Exception:stats['missing_date']+=1;continue
        lo=ts if lo is None else min(lo,ts);hi=ts if hi is None else max(hi,ts)
        if last is not None and ts<last:stats['timestamp_decreases']+=1
        last=ts;months[date(ts)[:7]]+=1
    stats.update(months=dict(sorted(months.items())),text_status=dict(statuses),subreddits=dict(subs),min_created_utc=lo,max_created_utc=hi,min_date=date(lo) if lo else '',max_date=date(hi) if hi else '',schema_keys=keys)
    out=RAW/'file-stats';out.mkdir(exist_ok=True);(out/(path.name+'.json')).write_text(json.dumps(stats,indent=2)+'\n')
    print(json.dumps({k:v for k,v in stats.items() if k not in ['months','schema_keys']}),flush=True)
    return stats

def extract(path,start,end,label):
    outdir=RAW/'windows'/label;outdir.mkdir(parents=True,exist_ok=True)
    outpath=outdir/path.name.replace('.zst','.gz')
    if outpath.exists():raise RuntimeError(f'Frozen output exists; choose a new label: {outpath}')
    n=0;seen=set();dups=0;lo=None;hi=None;statuses=collections.Counter();source_scanned=0
    with gzip.open(outpath,'wt',encoding='utf8',compresslevel=6) as out:
        for line in records(path):
            q=json.loads(line);source_scanned+=1
            try:ts=int(q['created_utc'])
            except Exception:continue
            if not(start<=ts<end):continue
            # Preserve every original line, including duplicates; count them rather than silently deleting.
            out.write(line);n+=1;lo=ts if lo is None else min(lo,ts);hi=ts if hi is None else max(hi,ts)
            id=q.get('id','')
            if id in seen:dups+=1
            seen.add(id)
            body=q.get('selftext',q.get('body',''))
            statuses['removed' if body=='[removed]' else 'deleted' if body=='[deleted]' else 'empty' if not body else 'present']+=1
    m={'source_file':str(path.relative_to(ROOT)),'output':str(outpath.relative_to(ROOT)),'window_start':date(start),'window_end_exclusive':date(end),'source_records_scanned':source_scanned,'selected_records':n,'unique_ids':len(seen),'duplicate_ids':dups,'min_date':date(lo) if lo else '', 'max_date':date(hi) if hi else '', 'text_status':dict(statuses),'compressed_bytes':outpath.stat().st_size,'sha256':hashlib.sha256(outpath.read_bytes()).hexdigest()}
    (outdir/(path.name+'.manifest.json')).write_text(json.dumps(m,indent=2)+'\n');print(json.dumps(m),flush=True);return m

def split(path):
    # Lossless byte pieces remain <=95,000,000 bytes, so each can be committed if the owner requests.
    limit=95_000_000
    if path.stat().st_size<=100_000_000:return
    outdir=path.parent/(path.name+'.parts');outdir.mkdir(exist_ok=True)
    full=hashlib.sha256();pieces=[]
    with path.open('rb') as f:
        i=0
        while b:=f.read(limit):
            full.update(b);p=outdir/f'{i:04d}.part';p.write_bytes(b)
            pieces.append({'file':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()});i+=1
    m={'original_filename':path.name,'original_bytes':path.stat().st_size,'original_sha256':full.hexdigest(),'concatenation_order':[x['file'] for x in pieces],'pieces':pieces,'reassembly':'Concatenate the piece files in listed order as binary; resulting bytes reproduce the original JSONL.zst exactly.'}
    (outdir/'reassembly.json').write_text(json.dumps(m,indent=2)+'\n')
    # Keep the unsplit convenience copy outside the repository, after verifying every piece hash.
    tmp=Path('/tmp/mamivio-reddit-unsplit');tmp.mkdir(exist_ok=True)
    target=tmp/path.name
    shutil.move(str(path),str(target))
    m['temporary_unsplit_copy']=str(target);(outdir/'reassembly.json').write_text(json.dumps(m,indent=2)+'\n')
    print(json.dumps({'split':path.name,'pieces':len(pieces),'original_bytes':m['original_bytes'],'sha256':m['original_sha256'],'unsplit_temporary':str(target)}),flush=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('action',choices=['scan','extract','split']);ap.add_argument('paths',nargs='+');ap.add_argument('--start');ap.add_argument('--end');ap.add_argument('--label');ap.add_argument('--workers',type=int,default=2);a=ap.parse_args()
    paths=[Path(p).resolve() for p in a.paths]
    if a.action=='scan':
        with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:list(pool.map(scan,paths))
    elif a.action=='split':
        for p in paths:split(p)
    else:
        start=int(datetime.datetime.fromisoformat(a.start).replace(tzinfo=datetime.timezone.utc).timestamp());end=int(datetime.datetime.fromisoformat(a.end).replace(tzinfo=datetime.timezone.utc).timestamp())
        with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:list(pool.map(lambda p:extract(p,start,end,a.label),paths))

if __name__=='__main__':main()
