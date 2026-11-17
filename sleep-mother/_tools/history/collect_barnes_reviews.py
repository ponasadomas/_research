#!/usr/bin/env python3
"""RV1 2026-10-25 (sleep-mother copy of toddler-behaviour/_tools; First Forty Days left out, global/ holds its B&N list): Barnes & Noble public edition pages -> public Yotpo storefront review lists.
Route as in global/sources/reviews-followups.md: product page (robots-permitted /w/), then
https://api-cdn.yotpo.com/v3/storefront/store/<appKey>/product/<shopify id>/reviews?page=N&perPage=8
(api-cdn robots allows /v3/storefront/store/*). Each format (paperback, ebook, ...) is its own
Shopify product and review list. Never overwrites a saved capture or corpus."""
import json, re, subprocess, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / '_raw/books'; HTML = RAW / '_html'
SEEDS = {
 'say-good-night-insomnia': ['9780805089585'],
 'hello-sleep': ['9781250828408', '9781250347428'],
 'sleep-solution': ['9780399583612'],
 'fourth-trimester': ['9781611804003'],
 'sleep-deprived-no-more': ['9780738215044'],
}
Q = '\\\\"'  # escaped quote inside the page's serialized JSON

def curl(url, out):
    r = subprocess.run(['curl', '-sS', '-L', '--max-time', '40', '-D', str(out.with_suffix('.headers.txt')), '-o', str(out), '-w', '%{http_code} %{url_effective}', url], capture_output=True, text=True)
    return r.stdout.strip()

def main():
    HTML.mkdir(parents=True, exist_ok=True)
    manifest = []
    for slug, eans in SEEDS.items():
        products = {}
        for ean in eans:
            page = HTML / f'barnes-{slug}-{ean}.html'
            if page.exists(): raise SystemExit('refusing to overwrite ' + str(page))
            st = curl(f'https://www.barnesandnoble.com/w/?ean={ean}', page)
            code, final = st.split(' ', 1)
            src = page.read_text(errors='replace')
            m = re.search(r'data-yotpo-product-id="(\d+)"', src)
            key = re.search(r'yotpoAppKey' + Q + ',' + Q + r'([A-Za-z0-9]+)', src)
            title = re.search(r'data-yotpo-name="([^"]*)"', src)
            manifest.append({'title_slug': slug, 'seed_ean': ean, 'url': final, 'http_status': code, 'raw_file': str(page.relative_to(ROOT)), 'yotpo_product_id': m and m.group(1), 'name': title and title.group(1)})
            if code != '200' or not m: continue
            appkey = key.group(1)
            products[m.group(1)] = {'ean': ean, 'format': 'page edition', 'name': title.group(1)}
            for gid, name, handle, ptype in re.findall(Q + 'id' + Q + ',' + Q + r'gid://shopify/Product/(\d+)' + Q + ',' + Q + 'title' + Q + ',' + Q + r'([^\\]*)' + Q + ',' + Q + 'handle' + Q + ',' + Q + r'(\d{13})' + Q + ',' + Q + 'productType' + Q + ',' + Q + r'([^\\]*)', src):
                if name.split(':')[0].lower().strip() == title.group(1).split(':')[0].lower().strip():
                    products.setdefault(gid, {'ean': handle, 'format': ptype, 'name': name})
            time.sleep(1)
        units = []
        for pid, info in products.items():
            pg = 1
            while True:
                out = RAW / f'barnes-{slug}-{pid}-p{pg}-yotpo-reviews.json'
                if out.exists(): raise SystemExit('refusing to overwrite ' + str(out))
                st = curl(f'https://api-cdn.yotpo.com/v3/storefront/store/{appkey}/product/{pid}/reviews?page={pg}&perPage=8', out)
                d = json.loads(out.read_text())
                tot = d.get('pagination', {}).get('total', 0)
                for r in d.get('reviews', []):
                    units.append({'review_id': r['id'], 'product_id': pid, 'ean': info['ean'], 'format': info['format'], 'score': r['score'], 'date': r['createdAt'][:10], 'title': r['title'], 'content': r['content'], 'verifiedBuyer': r.get('verifiedBuyer'), 'syndicated': bool(r.get('syndicationData')), 'raw_json': str(out.relative_to(ROOT))})
                manifest.append({'title_slug': slug, 'yotpo_product_id': pid, 'ean': info['ean'], 'format': info['format'], 'name': info['name'], 'http_status': st.split(' ')[0], 'raw_file': str(out.relative_to(ROOT)), 'page': pg, 'total': tot})
                if pg * 8 >= tot: break
                pg += 1; time.sleep(0.5)
        corpus = RAW / f'barnes-{slug}-corpus.txt'
        if corpus.exists(): raise SystemExit('refusing to overwrite ' + str(corpus))
        seen = set()
        with corpus.open('w') as f:
            for u in units:
                if u['review_id'] in seen: continue
                seen.add(u['review_id'])
                f.write(f"REVIEW barnes-{u['review_id']} | {u['score']} stars | {u['date']} | {u['format']} {u['ean']} | verifiedBuyer={u['verifiedBuyer']} syndicated={u['syndicated']}\nTITLE: {u['title']}\n{u['content']}\n\n")
        (RAW / f'barnes-{slug}-review-units.json').write_text(json.dumps(units, ensure_ascii=False, indent=2))
        print(slug, 'products', len(products), 'units', len(seen), flush=True)
    (RAW / 'barnes-collection-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
