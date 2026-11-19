#!/usr/bin/env python3
"""Check one digest against its share.
  python3 -I _tools/verify_digest.py <work dir> <evidence dir> <NN>
  (run from ~/GitHub/_research)
Checks: the three sections exist; every post of the share is in exactly one "Posts:" line
of its section and no other post is; each form's count line matches its "Posts:" line and
the counts sum to the section's posts; every form has a quote and a But line; every quote
is word for word inside the quote with that id in the share."""
import collections, html, os, re, sys
wd, ev, nn = sys.argv[1].rstrip("/"), sys.argv[2].rstrip("/"), sys.argv[3]
sf, df = f"{wd}/share-{nn}.md", f"{ev}/digest-{nn}.md"
if not os.path.isfile(df): print(f"digest {nn}: FAIL: missing {df}"); sys.exit(1)
norm = lambda s: re.sub(r"\s+", " ", html.unescape(s).replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()
ID = r"[a-z]{2,}[0-9]{1,3}-[0-9]{3,5}"
share = [s for s in re.split(r"^## .*$", open(sf, encoding="utf-8").read(), flags=re.M)[1:]]
ids = [re.findall(r"^### (\S+) \|", s, flags=re.M) for s in share]
# a quote may run over several lines: it ends at the next quote, the next post or the next section
quotes = {m.group(1): norm(m.group(2)) for m in re.finditer(r"^- `(" + ID + r")` \([a-z_]+\) (.*?)(?=^- `|^### |^## |\Z)", "\n".join(share), flags=re.M | re.S)}
t = open(df, encoding="utf-8").read(); problems = []
secs = re.split(r"^## (.*)$", t, flags=re.M); sec = {secs[i].strip(): secs[i + 1] for i in range(1, len(secs) - 1, 2)}
def find(word): return next((b for h, b in sec.items() if h.endswith(word)), None)
for which, word in ((0, "yes posts"), (1, "near posts")):
    body = find(word)
    if body is None: problems.append(f'no section ending "{word}"'); continue
    seen = collections.Counter(); total = 0
    for b in re.split(r"^### ", body, flags=re.M)[1:]:
        name = b.split("\n")[0].strip()[:60]
        m = re.search(r"^(\d[\d,]*) of (\d[\d,]*) posts\.", b, re.M); pl = re.search(r"^Posts: (.*)$", b, re.M)
        if not m: problems.append(f'"{name}": no count line'); continue
        if not pl: problems.append(f'"{name}": no Posts line'); continue
        got = pl.group(1).split(); seen.update(got); total += len(got)
        if int(m.group(1).replace(",", "")) != len(got): problems.append(f'"{name}": count {m.group(1)} but {len(got)} posts listed')
        if int(m.group(2).replace(",", "")) != len(ids[which]): problems.append(f'"{name}": M is {m.group(2)}, share has {len(ids[which])}')
        if not re.search(r'" \[' + ID + r"\]", b): problems.append(f'"{name}": no quote')
        if "**But:**" not in b: problems.append(f'"{name}": no But line')
    miss = [i for i in ids[which] if seen[i] != 1]; extra = [i for i in seen if i not in ids[which]]
    if miss: problems.append(f"{word}: {len(miss)} posts not in exactly one form, e.g. {miss[:3]}")
    if extra: problems.append(f"{word}: {len(extra)} listed posts not in the share, e.g. {extra[:3]}")
if find("across the yes posts") is None: problems.append('no section ending "across the yes posts"')
pairs = re.findall(r'"([^"\n]+)" \[(' + ID + r")\]", t.replace("“", '"').replace("”", '"'))
for q, i in pairs:
    if i not in quotes: problems.append(f"quote id {i} is not in the share"); continue
    parts = [x for x in re.split(r"\s*\[…\]\s*|\s*\[\.\.\.\]\s*", q) if x.strip()]
    if not all(norm(x).rstrip(".,;") in quotes[i] for x in parts): problems.append(f"not word for word from {i}: {q[:50]}")
print(f"digest {nn}: quotes checked {len(pairs)}, words {len(t.split())}; " + ("OK" if not problems else "FAIL"))
for p in problems[:20]: print("  " + p)
sys.exit(1 if problems else 0)
