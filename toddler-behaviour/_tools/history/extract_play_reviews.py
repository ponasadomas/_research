#!/usr/bin/env python3
"""RV1 2026-10-25: freeze the ~3 review bodies a public Google Play detail page exposes.
Reads _raw/reviews/_html/googleplay-<app>.html, writes _raw/reviews/googleplay-<app>.txt
(reviewer names omitted). Refuses to overwrite an existing corpus."""
import re, sys, html, json
from pathlib import Path
RAW = Path(__file__).resolve().parents[1] / '_raw/reviews'
out_units = []
for app in sys.argv[1:]:
    src = (RAW / f'_html/googleplay-{app}.html').read_text(errors='replace')
    blocks = re.split(r'<div class="EGFGHd"', src)[1:]
    corpus = RAW / f'googleplay-{app}.txt'
    if corpus.exists():
        raise SystemExit('refusing to overwrite ' + str(corpus))
    lines = []
    for i, b in enumerate(blocks, 1):
        rating = re.search(r'aria-label="Rated (\d) stars? out of five stars"', b)
        date = re.search(r'<span class="bp9Aid">([^<]*)</span>', b)
        body = re.search(r'class="h3YV2d">(.*?)</div>', b, re.S)
        helpful = re.search(r'<div class="AJTPZc"[^>]*>([^<]*)</div>', b)
        reply = re.search(r'class="ras4vb"[^>]*><div>(.*?)</div>', b, re.S)
        if not body:
            continue
        u = {'app': app, 'n': i, 'rating': rating and rating.group(1), 'date': date and date.group(1),
             'helpful': helpful and html.unescape(helpful.group(1)), 'body': html.unescape(body.group(1)),
             'developer_reply': reply and html.unescape(re.sub('<[^>]+>', ' ', reply.group(1)))}
        out_units.append(u)
        lines.append(f"REVIEW googleplay-{app}-{i} | {u['rating']} stars | {u['date']} | {u['helpful']}\n{u['body']}\n" + (f"DEVELOPER REPLY: {u['developer_reply']}\n" if u['developer_reply'] else '') + "\n")
    corpus.write_text(''.join(lines))
    print(app, len(lines))
(RAW / ('googleplay-review-units-' + '-'.join(sys.argv[1:]) + '.json')).write_text(json.dumps(out_units, ensure_ascii=False, indent=2))
