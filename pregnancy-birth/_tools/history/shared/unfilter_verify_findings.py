#!/usr/bin/env python3
"""Supervisor's independent check of a build's findings after the unfilter pass.
python3 -I unfilter_verify_findings.py <niche> [git-ref-to-compare=HEAD]"""
import glob, json, os, re, subprocess, sys
niche = sys.argv[1]; ref = sys.argv[2] if len(sys.argv) > 2 else "HEAD"
T = os.path.dirname(os.path.abspath(__file__)); R = os.path.normpath(os.path.join(T, "..", "..", niche))
repo = subprocess.run(["git", "-C", T, "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()
voice = {}
for f in glob.glob(os.path.join(R, "voice", "*.jsonl")):
    for l in open(f):
        try: r = json.loads(l); voice[r["id"]] = r["quote"]
        except Exception: pass
IDR = r"([a-z]+\d{1,2}-\d{4})"
t = open(os.path.join(R, "synthesis", "findings.md")).read()
old = subprocess.run(["git", "-C", repo, "show", f"{ref}:mamivio.com/research/{niche}/synthesis/findings.md"], capture_output=True, text=True).stdout
cited = set(re.findall(r"\[" + IDR + r"\]", t)); was = set(re.findall(r"\[" + IDR + r"\]", old))
ur = {i for i in voice if re.match(r"[a-z]+u\d\d-|dv2[1-5]-", i)}
pairs = re.findall(r'["“]([^"”\n]{12,}?)["”]\s*`?\[' + IDR + r"\]", t); bad = []
for q, i in pairs:
    if i not in voice: continue
    parts = [p for p in re.split(r"\s*\[…\]\s*|\s*\[\.\.\.\]\s*|\s*…\s*", q) if len(p) > 8]
    if not all(norm(p).rstrip(".,;") in norm(voice[i]) for p in parts): bad.append(i)
unres = [i for i in cited if i not in voice]
print(f"{niche}: words {len(old.split())} -> {len(t.split())} | cited {len(was)} -> {len(cited)} | earlier citations dropped {len(was - cited)} | "
      f"unresolved {len(unres)} | re-read ids cited {len(ur & cited)} of {len(ur)} | pairs {len(pairs)}, mismatches {len(bad)} {bad[:5]}")
sys.exit(1 if (bad or unres or was - cited) else 0)
