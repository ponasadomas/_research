#!/usr/bin/env python3
"""Check one digest: quotes verbatim, ids real, share covered.  python3 -I unfilter_verify_digest.py <niche> <NN>"""
import json, os, re, sys
niche, nn = sys.argv[1], sys.argv[2]
T = os.path.dirname(os.path.abspath(__file__)); R = os.path.normpath(os.path.join(T, "..", "..", niche))
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()
share = {}
for f in open(os.path.join(R, "scratchpad", "unfilter-reread", f"digest-{nn}.files")).read().split():
    for l in open(os.path.join(R, f)):
        if l.strip(): r = json.loads(l); share[r["id"]] = r["quote"]
p = os.path.join(R, "synthesis", f"unfilter-digest-{nn}.md")
if not os.path.exists(p): print(f"{niche} digest {nn}: FAIL: no digest file"); sys.exit(1)
t = open(p).read(); IDR = r"([a-z]+\d{1,2}-\d{4})"
ids = set(re.findall(IDR, t)); foreign = [i for i in ids if i not in share and re.match(r"[a-z]+u\d\d-", i)]
def ok(q, i):
    parts = [x for x in re.split(r"\s*\[…\]\s*|\s*\[\.\.\.\]\s*|\s*…\s*", q) if len(x) > 8]
    src = norm(share[i].replace("\\", ""))
    return all(norm(x.replace("\\", "")).rstrip(".,;") in src for x in parts)
pairs = []; bad = 0; badids = []
for q, i in re.findall(r'["“]([^"”\n]{12,}?)["”]\s*`?\[?' + IDR + r"\]?", t):  # inline "quote" [id]
    if i in share:
        pairs.append(i)
        if not ok(q, i): bad += 1; badids.append(i)
L = t.split("\n"); n = 0   # blockquotes: "> text" with the id just before or just after
while n < len(L):
    if not L[n].startswith(">"): n += 1; continue
    a = n
    while n < len(L) and L[n].startswith(">"): n += 1
    q = " ".join(x.lstrip("> ").strip() for x in L[a:n]).strip().strip('"“”')
    q = re.sub(r"\s*[—–-]*\s*`?\[?" + IDR + r"\]?`?\s*$", "", q).strip().strip('"“”')
    before = [i for x in L[max(0, a - 6):a] for i in re.findall(IDR, x) if i in share][::-1]
    inside = [i for x in L[a:n] for i in re.findall(IDR, x) if i in share]
    after = [i for x in L[n:n + 4] for i in re.findall(IDR, x) if i in share]
    cands = inside + before[:1] + after[:1]
    if not cands or len(q) < 12: continue
    pairs.append(cands[0])
    if not any(ok(q, i) for i in cands): bad += 1; badids.append(cands[0])
n = 0   # fenced blocks: ```quote ... ``` with the id just before or just after
while n < len(L):
    m = re.match(r"\s*(`{3,}|~{3,})", L[n])
    if not m: n += 1; continue
    a = n + 1; n = a
    while n < len(L) and not L[n].strip().startswith(m.group(1)): n += 1
    q = " ".join(x.strip() for x in L[a:n]).strip().strip('"“”'); n += 1
    before = [i for x in L[max(0, a - 7):a - 1] for i in re.findall(IDR, x) if i in share][::-1]
    after = [i for x in L[n:n + 4] for i in re.findall(IDR, x) if i in share]
    cands = before[:1] + after[:1]
    if not cands or len(q) < 12: continue
    pairs.append(cands[0])
    if not any(ok(q, i) for i in cands): bad += 1; badids.append(cands[0])
cov = len(ids & set(share)); problems = []
if bad: problems.append(f"{bad} quotes not verbatim ({' '.join(badids[:8])})")
if cov < 0.6 * len(share): problems.append(f"only {cov} of {len(share)} ids mentioned")
if len(pairs) < 0.1 * len(share): problems.append(f"only {len(pairs)} quotes reproduced")
print(f"{niche} digest {nn}: share {len(share)}, ids mentioned {cov}, quotes reproduced {len(pairs)}, words {len(t.split())}; " + ("OK" if not problems else "FAIL: " + "; ".join(problems)))
sys.exit(1 if problems else 0)
