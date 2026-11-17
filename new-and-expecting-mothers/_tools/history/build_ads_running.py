#!/usr/bin/env python3
"""Adapted from SYD build_ads_running.py for frozen browser/embedded-JSON captures.
Retains off-topic records in raw; never equates active status or longevity with profit.
"""
from pathlib import Path
import collections,datetime,json,re,urllib.request,concurrent.futures
from ad_body_reads import body_read_ids
ROOT=Path(__file__).resolve().parents[1]
ALLOW={'Kinedu','BabySparks','Huckleberry','Solid Starts','Lovevery'}

def connections(x):
    if isinstance(x,dict):
        if 'search_results_connection' in x: yield x['search_results_connection']
        for v in x.values():yield from connections(v)
    elif isinstance(x,list):
        for v in x:yield from connections(v)

def unpack(d):
    ss='\n'.join(x['text'] for x in d['result'].get('content',[]) if x['type']=='text')
    m=re.search(r'```json\n(.*)\n```',ss,re.S)
    return json.loads(m.group(1)) if m else {}

def slug(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')

def date(ts):
    return datetime.datetime.fromtimestamp(ts,datetime.timezone.utc).date().isoformat() if ts else ''

ads={};queries=[]
for p in sorted((ROOT/'_raw/ads-running').glob('*.json')):
    d=json.loads(p.read_text())
    if not isinstance(d,dict) or 'result' not in d or 'query' not in d:continue
    v=unpack(d)
    if not v:continue
    p.with_suffix('.txt').write_text(v['text'])
    cc=[c for s in v.get('scripts',[]) for c in connections(json.loads(s))]
    aa=[a for c in cc for e in c.get('edges',[]) for a in e.get('node',{}).get('collated_results',[])]
    queries.append({'query':d['query'],'date':d['captured'],'url':v.get('url',''),'count':cc[0].get('count') if cc else None,'captured':len(aa),'raw':str(p.relative_to(ROOT))})
    for a in aa:
        id=a.get('ad_archive_id')
        if not id:continue
        if id in ads:ads[id]['queries'].append(d['query']);continue
        ads[id]={'record':a,'queries':[d['query']],'capture':str(p.relative_to(ROOT))}
kept={k:v for k,v in ads.items() if v['record'].get('snapshot',{}).get('page_name') in ALLOW}
records=ROOT/'_raw/ads-running/records';records.mkdir(exist_ok=True)
rows=[]
for id,v in kept.items():
    a=v['record'];s=a.get('snapshot',{});body=(s.get('body') or {}).get('text','')
    (records/(id+'.json')).write_text(json.dumps(v,ensure_ascii=False,indent=2))
    (records/(id+'.txt')).write_text(body)
    rows.append(dict(id=id,advertiser=s.get('page_name'),page_id=a.get('page_id'),url='https://www.facebook.com/ads/library/?id='+id,start=date(a.get('start_date')),active=a.get('is_active'),body=body,link=s.get('link_url'),queries=v['queries'],capture=v['capture'],raw_file=str((records/(id+'.txt')).relative_to(ROOT))))
(ROOT/'_raw/ads-running/query-ledger.json').write_text(json.dumps(queries,ensure_ascii=False,indent=2))
(ROOT/'_raw/ads-running/on-topic-ads.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
# One short excerpt per advertiser; full body is preserved and reviewed separately.
quotes=[];selected=[]
for brand in sorted(ALLOW):
    candidates=[a for a in rows if a['advertiser']==brand and a['body']]
    if not candidates:continue
    a=candidates[0];selected.append(a)
    if a['body'].startswith('{{'):continue  # unresolved dynamic creative is not meaningful language
    q=' '.join(a['body'].split()[:20])
    # Exact substring preserves original whitespace, punctuation and line breaks.
    words=list(re.finditer(r'\S+',a['body']));q=a['body'][:words[min(20,len(words))-1].end()]
    i=len(quotes)+1
    quotes.append(dict(id=f'ads01-{i:03}',source='adlibrary-'+slug(brand),source_class='advertisement',evidence_kind='seller_claim',url=a['url'],date='',speaker='advisor',stage='unknown',type='belief',themes=['personalization'],quote=q,context='Advertiser offer language; active status is not evidence of buyer outcomes or profitability.',raw_file=a['raw_file'],advertiser=brand))
(ROOT/'voice/ads-01.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in quotes))
(ROOT/'_raw/ads-running/selected-for-full-read.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in selected))
fully_read=body_read_ids(rows,selected)
idx=['# Active advertising evidence — 2026-10-24','',f'{len(queries)} real-browser searches; {len(ads)} unique library ids captured, including off-topic results; {len(rows)} ids from five explicitly selected on-niche advertisers. This is the first loaded result page of each search, not an exhaustive ad census.','', 'Country filter: ALL. The material includes English and other languages; it is not a US-only advertising sample. Broad search terms produce substantial noise. Zero keyword results do not prove that a brand has no ads. Longevity and active status do not establish spend, conversion, revenue, profitability or effectiveness. No impressions or budgets were available.','', '## Search ledger','', '| Query | Result count reported by embedded data | Loaded entries | Date | Raw |','|---|---:|---:|---|---|']
for q in queries:idx.append(f"| {q['query']} | {q['count'] if q['count'] is not None else 'unavailable'} | {q['captured']} | {q['date']} | `{q['raw']}` |")
idx+=['','## Selected advertisers','', '| Advertiser | Captured distinct ids | Earliest observed active start (UTC) | Note |','|---|---:|---|---|']
for b in sorted(ALLOW):
    rr=[a for a in rows if a['advertiser']==b];starts=[a['start'] for a in rr if a['start']]
    idx.append(f"| {b} | {len(rr)} | {min(starts) if starts else ''} | [{slug(b)}]({slug(b)}.md) |")
    out=[f'# {b} — captured ads','', 'Source: Meta Ad Library, ALL countries, active search, 2026-10-24. Raw record bodies and original capture pointers are in `_raw/ads-running/records/`. Counts are distinct library ids, not unique creative concepts.','', '| Library id | Start date UTC | Destination |','|---|---|---|']
    out += [f"| [{a['id']}]({a['url']}) | {a['start']} | {a['link'] or 'not exposed'} |" for a in rr]
    read_count=sum(str(a['id']) in fully_read for a in rr)
    out += ['',f'{read_count} of {len(rr)} retained body texts fully read, as recorded in `sources/ad-body-reading-ledger.tsv`; {len(rr)-read_count} retained body texts unread. The initial five-body snapshot in `selected-for-full-read.jsonl` is preserved separately. Full creative images/videos and alternate variants were not inspected. Active status is not proof of profitability.']
    (ROOT/'ads-running'/(slug(b)+'.md')).write_text('\n'.join(out)+'\n')
idx+=['','## Coverage and continuation','',f"Retained body texts fully read: {len(fully_read)} of {len(rows)}; retained body texts unread: {len(rows)-len(fully_read)}; quotes: {len(quotes)}. Per-id status and body hashes are in `sources/ad-body-reading-ledger.tsv`. The initial {len(selected)}-body snapshot and its four-quote selection remain preserved; `_raw/ads-running/unread-bodies.txt` is a historical pre-completion list, not current read status. Lovevery's captured body is an unresolved template placeholder; reading it does not reveal its actual creative message. Full images/videos and alternate creative variants remain unviewed. All off-topic ads remain only in raw captures. Brand-name/domain searches did not verify owner ads: Mamivio domain returned one unrelated advertiser; Pirmi Žingsniai domain returned no entries. A later search by the actual owning Page id is needed.",'','No new ads or customer-facing copy were drafted. To extend, page through allowed Library results or inspect a known advertiser Page in a browser, preserve captures under new filenames, and maintain a separate media-viewing ledger.']
(ROOT/'ads-running/README.md').write_text('\n'.join(idx)+'\n')
# Preserve one preview per selected advertiser now; remote media URLs can expire.
assets=ROOT/'_raw/ads-running/assets';assets.mkdir(exist_ok=True)
assetlog=[]
for a in selected:
    s=kept[a['id']]['record'].get('snapshot',{});media=s.get('images') or s.get('videos') or []
    m=media[0] if media else {};u=m.get('original_image_url') or m.get('video_preview_image_url')
    if not u:assetlog.append({'ad':a['id'],'status':'no image preview exposed'});continue
    p=assets/(a['id']+'.jpg')
    try:
        with urllib.request.urlopen(u,timeout=20) as resp:p.write_bytes(resp.read());code=resp.status
        assetlog.append({'ad':a['id'],'url':u,'status':code,'file':str(p.relative_to(ROOT))})
    except Exception as e:assetlog.append({'ad':a['id'],'url':u,'status':str(e)})
(ROOT/'_raw/ads-running/asset-log.json').write_text(json.dumps(assetlog,indent=2))
print(f'{len(queries)} searches; {len(ads)} unique ids; {len(rows)} on-topic ids; {len(selected)} selected bodies; {len(quotes)} quotes')
