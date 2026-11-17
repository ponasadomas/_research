"""Group a read-<label>/chunks.jsonl into reader assignments of ~target units.
Usage: python3 -I assign_readers.py <niche> <label> <first reader number> <reader letter prefix> [target]
Writes <niche>/_raw/reddit/<label>/assignments.txt; asserts every chunk is assigned exactly once.
A last group under 40% of target is folded into the one before."""
import json, sys
niche, label, first, pre = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
target = int(sys.argv[5]) if len(sys.argv) > 5 else 125
p = f"{niche}/_raw/reddit/{label}/"
chunks = [json.loads(l) for l in open(p + "chunks.jsonl")]
order = {"keep_purchase": 0, "keep_success": 1, "keep_otherside": 2, "keep_core": 3}
chunks.sort(key=lambda c: (order.get(c["label"], 9), c["chunk"]))
groups, cur, n = [], [], 0
for c in chunks:
    cur.append(c); n += len(c["units"])
    if n >= target: groups.append(cur); cur, n = [], 0
if cur:
    if groups and n < 0.4 * target: groups[-1].extend(cur)
    else: groups.append(cur)
names = [c["chunk"] for g in groups for c in g]
assert sorted(names) == sorted(c["chunk"] for c in chunks) and len(set(names)) == len(names)
with open(p + "assignments.txt", "w") as f:
    for i, g in enumerate(groups):
        f.write(f"{pre}{first + i:02d} " + " ".join(c["chunk"] for c in g) + f" {sum(len(c['units']) for c in g)}\n")
print(open(p + "assignments.txt").read())
