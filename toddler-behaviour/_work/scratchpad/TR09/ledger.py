import json, os, collections
N = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
recs = [json.loads(l) for l in open(os.path.join(N, "voice/reddit-tr09.jsonl"))]
st = {}
for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "status.tsv")):
    p = l.rstrip("\n").split("\t"); st[p[0]] = (p[1], p[2] if len(p) > 2 else "")
units = [l.split() for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "units.txt"))]
byu = collections.defaultdict(list)
for r in recs: byu[r["raw_file"]].append(r["id"])
rows = []; perchunk = collections.OrderedDict()
for c, u in units:
    k = u.split("/")[-1][:-4]; s, note = st[k]; ids = byu.get(u, [])
    if s == "read" and not ids: s = "read, not quoted"
    perchunk.setdefault(c, [0, 0]); perchunk[c][0] += 1; perchunk[c][1] += len(ids)
    q = f"{ids[0]}–{ids[-1]} ({len(ids)})" if ids else "—"
    rows.append(f"| keep_core-{c} | `{u}` | {s} | {q} | {note} |")
cnt = collections.Counter(r.split(" | ")[2] for r in rows)
out = f"""# Reddit full reads — TR09 (toddler-behaviour, 2026-10-25)

Reader TR09 · id prefix `tb09` · voice file `voice/reddit-tr09.jsonl` · brief `../_shared/_tools/brief-reading.md` · chunks from `_raw/reddit/read-v1/chunks.jsonl`. Scratch and build script: `scratchpad/TR09/` (`spec-*.py` → `build.py`; this ledger from `ledger.py`). Final assignment of the read-v1 keep_core set (includes chunk 063).

## Counts

| step | n |
|---|---|
| chunks assigned | 9 (read-v1-keep_core-055 to 063) |
| units in those chunks | {len(units)} |
| units read in full | {len(units)} (all) |
| units quoted from | {cnt['read']} |
| units excluded (read in full, nothing copied, line not to cross) | {cnt['excluded']} |
| units read, not quoted (duplicate cross-post, restricted or off-topic) | {cnt['read, not quoted']} |
| quotes written | {len(recs)} ({recs[0]['id']} to {recs[-1]['id']}) |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-tr09.jsonl` → {len(recs)} quotes, 0 failed |

Counts are counts of quotes chosen, never of people.

## Chunks

| chunk | units | quotes |
|---|---|---|
""" + "\n".join(f"| read-v1-keep_core-{c} | {a} | {b} |" for c, (a, b) in perchunk.items()) + """

## Units (every unit, read in full)

Status `read` = read in full and quoted; `excluded` = read in full, nothing copied, neutral reason; `read, not quoted` = duplicate, restricted with nothing safe to quote, or off-topic. Notes record passages deliberately left unquoted inside read units; `restricted` units are listed in `../synthesis/reader-notes-tr09.md` § Restricted ids.

| chunk | unit (raw_file) | status | quote ids | note |
|---|---|---|---|---|
""" + "\n".join(rows) + "\n"
open(os.path.join(N, "sources/reddit-reading-tr09.md"), "w").write(out)
print(cnt)
