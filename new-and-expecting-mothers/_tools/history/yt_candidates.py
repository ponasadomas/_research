#!/usr/bin/env python3
"""Rank comments per video for manual reading. Reads only _raw/youtube/*.txt.
usage: python3 -I yt_candidates.py <txt-dir> <out.txt> [per_video=20] [cap=700]
Each candidate is printed as: K<n> <video-id> likes=<n> len=<n> / text (display-capped; quote from the raw file).
A key map (K<n> -> video id, comment id, likes, age) is written to <out>.keys.tsv."""
import sys, os, re, glob, math
src, out = sys.argv[1], sys.argv[2]
per = int(sys.argv[3]) if len(sys.argv) > 3 else 20
cap = int(sys.argv[4]) if len(sys.argv) > 4 else 700
POS = [r"\bmy (baby|child|daughter|son|partner|husband|wife)", r"\b(first.time|new) (mom|mum|mother|parent)",
       r"tummy time|floor (time|play)|milestone", r"solids|wean|puree|purée|grocery|meal plan",
       r"pump|breastfeed|return.{0,8}work|daycare|childcare|caregiver", r"postpartum|pregnan|trimester",
       r"sleep|nap|wake window", r"i tried|i've tried|i did", r"overwhelm|confus|guilt",
       r"too much|not enough time|couldn.t|didn.t|wish|free|pay|subscription|cancel", r"what (do|should|can) i", r"\?"]

SPAM = re.compile(r"whatsapp|spell ?cast|love spell|@gmail|\bdr\.? ?[a-z]+ (on|via|helped)|herbal|priest|\+\d{6,}|instagram|telegram|hacker|crypto|contact (him|her) (on|via|at)", re.I)
hdr = re.compile(r"^\[c:(\S+) likes:(\d+) age:(.*?) reply:(\d)\]$")
k = 0
with open(out, "w", encoding="utf-8") as o, open(out + ".keys.tsv", "w", encoding="utf-8") as kf:
    for f in sorted(glob.glob(os.path.join(src, "*.txt"))):
        vid = os.path.basename(f)[:-4]
        lines = open(f, encoding="utf-8").read().split("\n")
        o.write(f"\n===== {vid} :: {lines[0][2:120]}\n")
        cands = []
        i = 1
        while i < len(lines):
            m = hdr.match(lines[i])
            if m and i + 1 < len(lines):
                t = lines[i + 1]
                if 140 <= len(t) <= 4000 and not SPAM.search(t):
                    low = t.lower()
                    s = sum(1 for p in POS if re.search(p, low))
                    s += min(3, math.log10(int(m.group(2)) + 1))
                    s += min(2, len(t) / 600)
                    if re.search(r"\b(i|my|me)\b", low) is None: s -= 4
                    cands.append((s, m.group(1), int(m.group(2)), m.group(3), t))
                i += 2
            else:
                i += 1
        cands.sort(key=lambda x: -x[0])
        for s, cid, likes, age, t in cands[:per]:
            k += 1
            shown = t if len(t) <= cap else t[:cap] + f" …[+{len(t)-cap}]"
            o.write(f"K{k} likes={likes} len={len(t)}\n{shown}\n")
            kf.write(f"K{k}\t{vid}\t{cid}\t{likes}\t{age}\n")
print(k)
