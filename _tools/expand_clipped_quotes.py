#!/usr/bin/env python3
"""Widen quotes that were clipped mid-sentence to the whole sentences they come from.
  python3 -I _tools/expand_clipped_quotes.py <quotes dir> <most words per quote> <page.md>...
  (run from ~/GitHub/_research)
Only bullet quotes of the form  - "<text>" [<id>]  that carry a cut mark […] are touched.
Each part is found in the record with that id and widened to its sentence; parts that then
touch are joined. A quote that cannot be found, or would pass the word limit, is left as it is.
The words stay the record's own. Run the page's checker afterwards."""
import glob, json, re, sys
qd, most, pages = sys.argv[1].rstrip("/"), int(sys.argv[2]), sys.argv[3:]
rec = {}
for f in glob.glob(f"{qd}/*.jsonl"):
    for l in open(f, encoding="utf-8"):
        if l.strip(): r = json.loads(l); rec[r["id"]] = r["quote"]
Q = "['’‘]"; DQ = '["“”]'
def pattern(part):
    out = []
    for w in part.split():
        w = re.escape(w); w = re.sub("['’‘]", lambda m: Q, w); w = re.sub('["“”]', lambda m: DQ, w); out.append(w)
    return r"\s+".join(out)
def widen(text, a, b):
    while a > 0 and not re.match(r"[.!?…]\s|\n", text[a - 2:a] if a >= 2 else "\n"): a -= 1
    m = re.search(r"[.!?…]+(?=\s|$)|\n", text[b - 1:] if b else text)
    b = (b - 1 + m.end()) if m and b else (m.end() if m else len(text))
    return a, min(b, len(text))
total = changed = 0
for page in pages:
    L = open(page, encoding="utf-8").read().split("\n")
    for i, l in enumerate(L):
        m = re.match(r'^- "(.*)" \[([a-z]{2,}[0-9]{1,3}-[0-9]{3,5})\]\s*$', l)
        if not m or "[…]" not in m.group(1) or m.group(2) not in rec: continue
        total += 1; text = rec[m.group(2)]; spans = []; pos = 0; okay = True
        for part in [p.strip() for p in m.group(1).split("[…]") if p.strip()]:
            f = re.compile(pattern(part)).search(text, pos) or re.compile(pattern(part.rstrip(".,;"))).search(text, pos)
            if not f: okay = False; break
            spans.append(widen(text, f.start(), f.end())); pos = f.end()
        if not okay or not spans: continue
        merged = [list(spans[0])]
        for a, b in spans[1:]:
            if a <= merged[-1][1] + 1 or not text[merged[-1][1]:a].strip(): merged[-1][1] = max(b, merged[-1][1])
            else: merged.append([a, b])
        new = " […] ".join(re.sub(r"\s+", " ", text[a:b]).strip() for a, b in merged)
        if merged[0][0] > 0 and text[:merged[0][0]].strip(): new = "[…] " + new
        if text[merged[-1][1]:].strip(): new = new + " […]"
        if len(new.split()) > most or '"' in new and '"' not in m.group(1): continue
        if new != m.group(1): L[i] = f'- "{new}" [{m.group(2)}]'; changed += 1
    open(page, "w", encoding="utf-8").write("\n".join(L))
print(f"quotes with a cut mark {total}, widened {changed}")
