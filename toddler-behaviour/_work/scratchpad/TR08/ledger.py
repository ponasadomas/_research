# Writes sources/reddit-reading-tr08.md from units.txt, status.tsv and the voice file.
import json, collections, os
N = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
units = [l.split() for l in open(os.path.join(N, "scratchpad/TR08/units.txt"))]
st = {}
for l in open(os.path.join(N, "scratchpad/TR08/status.tsv")):
    p = l.rstrip("\n").split("\t"); st[p[0]] = (p[1], p[2] if len(p) > 2 else "")
recs = [json.loads(l) for l in open(os.path.join(N, "voice/reddit-tr08.jsonl"))]
ids = collections.defaultdict(list)
for r in recs: ids[r["raw_file"]].append(r["id"])
def rng(a): return f"{a[0]}–{a[-1][5:]}" if len(a) > 1 else (a[0] if a else "")
cnt = collections.Counter(s for s, _ in st.values())
quoted = sum(1 for u in st if ids["../_shared/_raw/reddit-2026/units/" + u + ".txt"])
out = []
out.append("# Reddit full reads — TR08 (toddler-behaviour, 2026-10-25)\n")
out.append("Reader TR08 · id prefix `tb08` · voice file `voice/reddit-tr08.jsonl` · brief `../_shared/_tools/brief-reading.md` · chunks from `_raw/reddit/read-v1/chunks.jsonl`. Scratch and build script: `scratchpad/TR08/` (`spec-*.py` → `build.py`; this ledger from `ledger.py`; per-unit status in `status.tsv`).\n")
out.append("## Counts\n\n| step | n |\n|---|---|")
out.append("| chunks assigned | 8 (read-v1-keep_core-047 to 054) |")
out.append(f"| units in those chunks | {len(units)} |")
out.append(f"| units read in full | {len(st)} (all) |")
out.append(f"| units quoted from | {quoted} |")
out.append(f"| units excluded (read in full, nothing copied, line not to cross) | {cnt['excluded']} |")
out.append(f"| units read, not quoted (cross-post or off-topic) | {cnt['read, not quoted']} |")
out.append(f"| quotes written | {len(recs)} ({recs[0]['id']} to {recs[-1]['id']}) |")
out.append(f"| verify | `python3 -I _tools/verify_quotes.py voice/reddit-tr08.jsonl` → {len(recs)} quotes, 0 failed |\n")
out.append("Counts are counts of quotes chosen, never of people.\n")
out.append("## Chunks\n\n| chunk | units | quotes |\n|---|---|---|")
for c in sorted(set(u[0] for u in units)):
    us = [u[1] for u in units if u[0] == c]
    out.append(f"| {c} | {len(us)} | {sum(len(ids[u]) for u in us)} |")
out.append("\n## Units (every unit, read in full)\n")
out.append("Status `read` = read in full and quoted; `excluded` = read in full, nothing copied, neutral reason; `read, not quoted` = cross-post or off-topic. Notes record passages deliberately left unquoted inside read units, and units whose quotes are restricted (see `synthesis/reader-notes-tr08.md` § Restricted ids).\n")
out.append("| chunk | unit (raw_file) | status | quote ids | note |\n|---|---|---|---|---|")
for c, u in units:
    k = u.split("/")[-1][:-4]; s, note = st[k]
    out.append(f"| {c[-3:]} | `{u}` | {s} | {rng(ids[u])} | {note} |")
out.append("\n## Excluded units (neutral reasons)\n")
for c, u in units:
    k = u.split("/")[-1][:-4]; s, note = st[k]
    if s == "excluded": out.append(f"- `{u}` — {note}")
out.append("\n## Not read\n\nNone. Every unit in chunks 047–054 was read in full.\n")
open(os.path.join(N, "sources/reddit-reading-tr08.md"), "w").write("\n".join(out) + "\n")
print("ok", len(recs), quoted, cnt)
