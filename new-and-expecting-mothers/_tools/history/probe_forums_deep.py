#!/usr/bin/env python3
"""Ordinary public HTTP policy/landing inspection; no identity switching or wall bypass."""
import concurrent.futures, datetime, hashlib, json, pathlib, re, urllib.parse
import requests

ROOT=pathlib.Path(__file__).resolve().parents[1]
RAW=ROOT/'_raw/forums-deep/access'
RAW.mkdir(parents=True, exist_ok=True)
SITES=[
('babyandbump','https://forums.babyandbump.com/'),
('thebump','https://forums.thebump.com/'),
('parentingforums','https://www.parentingforums.org/'),
('babyforum','https://www.babyforum.com/'),
('pregnantcommunity','https://www.pregnantcommunity.com/'),
('bellybelly','https://www.bellybelly.com.au/forum/'),
('essentialbaby','https://www.essentialbaby.com.au/'),
('essentialkids','https://www.essentialkids.com.au/'),
('fertilethoughts','https://www.fertilethoughts.com/forums/'),
('fertilityfriends','https://www.fertilityfriends.co.uk/'),
('mumschat','https://mums.chat/'),
('babycentreuk','https://community.babycentre.co.uk/'),
('babycenterindia','https://www.babycenter.in/community'),
('babycenteraustralia','https://www.babycenter.com.au/community'),
('healthboards','https://www.healthboards.com/boards/pregnancy/'),
('madeformums','https://forum.madeformums.com/'),
('pregnancyforum','https://www.pregnancyforum.org.uk/'),
('hellobee','https://boards.hellobee.com/'),
('mumsnet','https://www.mumsnet.com/talk/'),
('netmums','https://www.netmums.com/coffeehouse/'),
('babyforumuk','https://www.babyforum.co.uk/'),
('pregnancyinfo','https://www.pregnancy-info.net/forums/'),
('babyexpert','https://www.babyexpert.com/'),
('babywhisperer','https://www.babywhispererforums.com/'),
('babyledweaning','https://www.babyledweaning.com/forum/'),
('babyledweaningforum','https://www.babyledweaningforum.com/'),
('mothering','https://www.mothering.com/forums/'),
('justmommies','https://www.justmommies.com/forums/'),
('pregnancyorg','https://www.pregnancy.org/bulletinboards/'),
('diaperswappers','https://www.diaperswappers.com/forums/'),
('clothdiapernation','https://www.clothdiapernation.com/'),
('countdowntopregnancy','https://www.countdowntopregnancy.com/forum/'),
('babycenterus','https://community.babycenter.com/'),
('whattoexpect','https://community.whattoexpect.com/'),
('pregnancychat','https://www.pregnancychat.com/forum/'),
('mumsforum','https://www.mumsforum.co.uk/'),
]

def fetch(slug,kind,url):
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    out={'slug':slug,'kind':kind,'requested_url':url,'fetched_at':started}
    try:
        r=requests.get(url,timeout=22)
        path=RAW/f'{slug}-{kind}.bin'
        path.write_bytes(r.content)
        out.update(status=r.status_code,final_url=r.url,headers=dict(r.headers),bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest(),raw_file=str(path.relative_to(ROOT)),redirects=[{'status':h.status_code,'url':h.url,'location':h.headers.get('Location')} for h in r.history])
        body=r.text
        t=re.search(r'(?is)<title[^>]*>(.*?)</title>',body)
        out['title']=re.sub('<[^>]+>','',t.group(1)).strip() if t else ''
        out['policy_excerpt']=body[:1800] if kind=='robots' else ''
    except Exception as e:
        out.update(status=None,error=repr(e))
    (RAW/f'{slug}-{kind}.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
    return out

def probe(site):
    slug,url=site
    u=urllib.parse.urlsplit(url)
    robots=fetch(slug,'robots',urllib.parse.urlunsplit((u.scheme,u.netloc,'/robots.txt','','')))
    # Landing inspection is independent of bulk access. Do not crawl any discovered pages here.
    landing=fetch(slug,'landing',url)
    print(json.dumps({'slug':slug,'robots':robots.get('status'),'landing':landing.get('status'),'url':landing.get('final_url'),'title':landing.get('title'),'bytes':landing.get('bytes'),'error':landing.get('error')},ensure_ascii=False),flush=True)
    return [robots,landing]

if __name__=='__main__':
    allrows=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for rows in pool.map(probe,SITES): allrows.extend(rows)
    ledger=ROOT/'sources/forums-deep-access.jsonl'
    ledger.parent.mkdir(parents=True,exist_ok=True)
    ledger.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in allrows))
