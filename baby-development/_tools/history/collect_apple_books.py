#!/usr/bin/env python3
"""(development copy, RV1 2026-10-25; titles adapted, KNOWN ids skip the US storefront.) Apple Books public product pages (us, gb, ca, au) -> visible customer reviews.
Resolves https://books.apple.com/us/book/isbn<EAN> (public product route; robots disallows only
/WebObjects/* and /v1/catalog/*), then fetches the same id in gb/ca/au. Apple shows ~3 reviews
per storefront page; reviewer names are not written to the corpus. Never overwrites."""
import re, subprocess, json, html, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / '_raw/books'; H = RAW / '_html'
BOOKS = {  # development RV1; ebook ISBNs first
 'brain-rules-baby': ['9780983263395', '9780983263388'],
 'aap-your-babys-first-year': ['9780593983874', '9780593158289'],
 'montessori-toddler': ['9781523507900', '9781523506897'],
 'baby-play-gymboree': ['9780865734340'],
 'amazing-child-montessori': ['9781465462305', '9780241286265'],
 'what-to-expect-first-year': ['9780761183174', '9780761181507'],
 'montessori-baby': [], 'wonder-weeks': [], 'simplest-baby-book': [],
}
# global/ already holds the US Apple Books page of these three (global/_raw/books/*.txt SOURCE lines): only gb/ca/au here
KNOWN = {'montessori-baby': '6443052178', 'wonder-weeks': '1451744965', 'simplest-baby-book': '1597514453'}
def curl(url, out):
    r = subprocess.run(['curl','-sS','-L','--max-time','40','-D',str(out.with_suffix('.headers.txt')),'-o',str(out),'-w','%{http_code} %{url_effective}',url],capture_output=True,text=True)
    return r.stdout.strip().split(' ',1)
def reviews(src):
    out=[]
    for m in re.finditer(r'<div aria-labelledby="(we-customer-review-\d+)" class="we-customer-review lockup">(.*?)(?=<div aria-labelledby="we-customer-review-|<h2 class="section__headline|</section>)', src, re.S):
        b=m.group(2)
        rating=re.search(r'aria-label="(\d) out of 5"',b); date=re.search(r'class="we-customer-review__date"[^>]*>([^<]*)<',b)
        title=re.search(r'<h3[^>]*>(.*?)</h3>',b,re.S); body=re.search(r'<blockquote[^>]*>(.*?)</blockquote>',b,re.S)
        clean=lambda x: re.sub(r'\s+',' ',html.unescape(re.sub(r'<br\s*/?>','\n',re.sub(r'<(?!br)[^>]+>','',x)))).strip() if x else None
        out.append({'review_id':m.group(1),'rating':rating and int(rating.group(1)),'date':date and date.group(1).strip(),'title':clean(title and title.group(1)),'contents':clean(body and body.group(1))})
    return out
ALT = {'good-inside-2': {'gb': '9780008505554'}}  # storefront edition with its own Apple id
import sys
def main():
    H.mkdir(parents=True,exist_ok=True); manifest=[]
    for slug,eans in BOOKS.items():
        if sys.argv[1:] and slug not in sys.argv[1:]: continue
        bid=KNOWN.get(slug); fronts=['gb','ca','au'] if bid else ['us','gb','ca','au']
        for e in ([] if bid else eans):
            out=H/f'apple-{slug}-isbn{e}.html'
            if out.exists(): raise SystemExit('refusing to overwrite '+str(out))
            code,final=curl(f'https://books.apple.com/us/book/isbn{e}',out)
            manifest.append({'book':slug,'storefront':'us','url':f'https://books.apple.com/us/book/isbn{e}','final':final,'http_status':code,'raw_file':str(out.relative_to(ROOT))})
            m=re.search(r'/id(\d+)',final)
            if code=='200' and m: bid=m.group(1); usfile=out; break
            out.unlink(missing_ok=True)
        if not bid: print(slug,'not found'); continue
        units=[]
        for cc in fronts:
            if cc=='us': out=usfile; code='200'; url=manifest[-1]['final']
            else:
                out=H/f'apple-{slug}-{cc}-id{bid}.html'
                if out.exists(): raise SystemExit('refusing to overwrite '+str(out))
                url=f'https://books.apple.com/{cc}/book/isbn{ALT[slug][cc]}' if cc in ALT.get(slug,{}) else f'https://books.apple.com/{cc}/book/id{bid}'; code,final=curl(url,out); time.sleep(1)
                manifest.append({'book':slug,'storefront':cc,'url':url,'final':final,'http_status':code,'raw_file':str(out.relative_to(ROOT))})
            for r in reviews(out.read_text(errors='replace')) if code=='200' else []:
                r.update(storefront=cc,url=url,html_file=str(out.relative_to(ROOT))); units.append(r)
        corpus=RAW/f'apple-{slug}-corpus.txt'
        if corpus.exists(): raise SystemExit('refusing to overwrite '+str(corpus))
        seen=set()
        with corpus.open('w') as f:
            for u in units:
                k=(u['title'],u['contents'])
                if k in seen: u['duplicate']=True; continue
                seen.add(k)
                f.write(f"REVIEW apple-{u['storefront']}-{u['review_id']} | {u['rating']} stars | {u['date']} | {u['url']}\nTITLE: {u['title']}\n{u['contents']}\n\n")
        (RAW/f'apple-{slug}-review-units.json').write_text(json.dumps(units,ensure_ascii=False,indent=2))
        print(slug,'id',bid,'units',len(units),'unique',len(seen),flush=True)
    (RAW/('apple-books-manifest'+('-'+'-'.join(sys.argv[1:]) if sys.argv[1:] else '')+'.json')).write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
main()
