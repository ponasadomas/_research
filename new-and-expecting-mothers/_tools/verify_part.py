#!/usr/bin/env python3
"""Check a document that reproduces quotes: every reproduced quote is word for word from the
record with that id, and every id belongs to the given quote files.
Layout expected: the id in square brackets on its own line, then the quote as a "> " blockquote
(an inline "quote" [id] is also read).
python3 -I _tools/verify_part.py <files-list or quotes dir> <markdown> [min-share-mentioned=0.15]
Run from the niche folder."""
import glob, json, os, re, sys
src, p = sys.argv[1], sys.argv[2]; need = float(sys.argv[3]) if len(sys.argv) > 3 else 0.15
files = sorted(glob.glob(os.path.join(src, "*.jsonl"))) if os.path.isdir(src) else open(src).read().split()
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("\\", "")).strip().lower()
share = {}
for f in files:
    for l in open(f):
        if l.strip(): r = json.loads(l); share[r["id"]] = r["quote"]
if not os.path.exists(p): print(f"{p}: FAIL: no file"); sys.exit(1)
t = open(p).read(); IDR = r"([a-z]+\d{1,2}-\d{4})"
ids = set(re.findall(IDR, t)); foreign = sorted(i for i in ids if i not in share)
def ok(q, i):
    parts = [x for x in re.split(r"\s*\[…\]\s*|\s*\[\.\.\.\]\s*|\s*…\s*", q) if len(x) > 8]
    return all(norm(x).rstrip(".,;") in norm(share[i]) for x in parts)
pairs = []; badids = []
for q, i in re.findall(r'["“]([^"”\n]{12,}?)["”][ \t]*`?\[?' + IDR + r"\]?", t):
    if i in share:
        pairs.append(i)
        if not ok(q, i): badids.append(i)
L = t.split("\n"); n = 0
while n < len(L):
    if not L[n].lstrip().startswith(">"): n += 1; continue
    a = n
    while n < len(L) and L[n].lstrip().startswith(">"): n += 1
    q = " ".join(x.lstrip().lstrip(">").strip() for x in L[a:n]).strip().strip('"“”')
    q = re.sub(r"\s*[—–-]*\s*`?\[?" + IDR + r"\]?`?\s*$", "", q).strip().strip('"“”')
    before = [i for x in L[max(0, a - 6):a] for i in re.findall(IDR, x) if i in share][::-1]
    inside = [i for x in L[a:n] for i in re.findall(IDR, x) if i in share]
    after = [i for x in L[n:n + 4] for i in re.findall(IDR, x) if i in share]
    cands = inside + before[:1] + after[:1]
    if not cands or len(q) < 12: continue
    pairs.append(cands[0])
    if not any(ok(q, i) for i in cands): badids.append(cands[0])
cov = len(ids & set(share)); problems = []
if badids: problems.append(f"{len(badids)} quotes not word for word ({' '.join(badids[:8])})")
if foreign: problems.append(f"{len(foreign)} ids not in these quote files ({' '.join(foreign[:8])})")
if cov < need * len(share): problems.append(f"only {cov} of {len(share)} ids mentioned")
if not pairs: problems.append("no quotes reproduced in the expected layout")
print(f"{os.path.basename(p)}: quotes available {len(share)}, ids mentioned {cov}, quotes reproduced {len(pairs)}, words {len(t.split())}; " + ("OK" if not problems else "FAIL: " + "; ".join(problems)))
sys.exit(1 if problems else 0)
