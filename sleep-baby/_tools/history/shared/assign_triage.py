"""Split a wave's card files into triage assignments of ~target cards (round-robin by size).
Usage: python3 -I assign_triage.py <niche> <filter label> <wave> <prefix> <target cards>
Writes <niche>/_raw/reddit/<flab>/<wave>/assignments.txt; asserts every file assigned once."""
import os, re, sys
niche, flab, wave, pre, target = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5])
d = f"{niche}/_raw/reddit/{flab}/{wave}/cards"
files = sorted(f for f in os.listdir(d) if f.endswith(".txt"))
def ncards(f):
    t = open(os.path.join(d, f)).read()
    return max(1, len(re.findall(r"(?m)^ID [0-9a-z]{6,8} ", t)))
sizes = {f: ncards(f) for f in files}
total = sum(sizes.values()); k = max(1, round(total / target))
groups = [[] for _ in range(k)]; load = [0] * k
for f in sorted(files, key=lambda x: -sizes[x]):
    i = load.index(min(load)); groups[i].append(f); load[i] += sizes[f]
assert sorted(sum(groups, [])) == files
with open(f"{niche}/_raw/reddit/{flab}/{wave}/assignments.txt", "w") as o:
    for i, g in enumerate(groups):
        o.write(f"{pre}{i+1} " + " ".join(sorted(g)) + "\n")
print(niche, wave, "files", len(files), "cards~", total, "groups", k, "loads", load)
