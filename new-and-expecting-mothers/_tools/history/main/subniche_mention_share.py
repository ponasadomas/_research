#!/usr/bin/env python3
"""Mention share per sub-niche across the harvested Reddit windows.

Reads every ``*_submissions.jsonl.gz`` in the global research window folder,
applies one wide regex per sub-niche to title+selftext, and writes a CSV and a
Markdown table. This is a *width proxy*: the share of posts whose text matches a
regex, not the prevalence of people or problems. One post can match several
sub-niches. Regexes are deliberately wide (recall over precision); they are
listed in the output so the reader can judge them.

Usage:
    python3 -I subniche_mention_share.py [--windows DIR] [--out DIR]
"""
import argparse
import csv
import gzip
import json
import os
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_WINDOWS = os.path.normpath(os.path.join(
    HERE, "..", "..", "global", "_raw", "reddit-deep", "windows", "2025-h2-v1"))
DEFAULT_OUT = os.path.normpath(os.path.join(HERE, "..", "synthesis"))

# sub-niche -> regex (case-insensitive). Keep the order: it is the output order.
PATTERNS = [
    ("sleep", r"\b(sleep regress\w*|sleep[- ]train\w*|naps?\b|napping|wake windows?|bedtime|night ?wak\w*|contact naps?|won'?t sleep|cry it out|ferber|sleep schedule|short naps?|false start|split nights?)"),
    ("breastfeeding_supply", r"\b(breast ?fe\w+|nursing|latch\w*|milk supply|low supply|oversupply|mastitis|clogged duct|nipples?|wean\w*)\b"),
    ("pumping", r"\b(pump(s|ed|ing)?|exclusive(ly)? pump\w*|freezer stash|haakaa|flange)\b"),
    ("formula_bottle", r"\b(formula|bottle[- ]refus\w*|bottle[- ]fe\w+|combo[- ]fe\w+|paced feed\w*|how (much|many) (oz|ounces|ml))\b"),
    ("reflux_colic_fussy", r"\b(reflux|colic\w*|gassy|gas pain|spit(s|ting)? up|weight gain|not gaining|percentiles?|witching hour|fussy|screaming)\b"),
    ("solids", r"\b(solids?|baby[- ]led weaning|blw|pur[eé]es?|first foods?|allergens?|starting solids|finger foods?|picky eat\w*)\b"),
    ("milestones_development", r"\b(milestones?|tummy time|roll(s|ed|ing)? over|crawl(s|ed|ing)?|sit(s|ting)? up (on|un|by)|pull(s|ing)? (himself|herself|themselves|up)|development(al)?|early intervention|motor skills?|head control|head lag)\b"),
    ("speech_language", r"\b(babbl\w*|first words?|speech|not talking|talking yet|say(s|ing)? (mama|dada)|language delay|words? yet|speech therap\w*)\b"),
    ("social_eye_contact", r"\b(eye contact|autis\w*|respond(s|ing)? to (his|her|their) name|social smile|not smiling|pointing|wav(e|es|ing) bye|red flags?)\b"),
    ("toddler_behaviour", r"\b(tantrums?|meltdowns?|hitting|biting|discipline|time[- ]?outs?|gentle parenting|terrible twos|whining|defian\w*|big feelings)\b"),
    ("potty", r"\b(potty|toilet[- ]train\w*|pull-?ups|diaper[- ]free)\b"),
    ("pregnancy_symptoms", r"\b(nausea|morning sickness|hyperemesis|heartburn|braxton|contractions?|weeks pregnant|trimesters?|ultrasound|anatomy scan|glucose test|gestational|round ligament|swelling)\b"),
    ("birth_prep_labour", r"\b(birth plan|hospital bag|induction|induced|c-?sections?|epidural|labou?r\b|due date|doula|midwi(fe|ves)|birth(ing)? class|hypnobirth\w*|delivery)\b"),
    ("postpartum_body", r"\b(postpartum|post-?partum|pelvic floor|diastasis|stitches|tear(ing)?|incontinen\w*|leak(ing|s)? (pee|urine)|hair loss|night sweats|lochia|bleeding after)\b"),
    ("maternal_mental_health", r"\b(ppd|ppa|postpartum (depression|anxiety|rage)|baby blues|intrusive thoughts|touched out|lost myself|identity|lonely|isolat\w*|mom guilt|guilt|overwhelm\w*|burn(t|ed)? ?out)\b"),
    ("partner_mental_load", r"\b(mental load|my husband|my partner|my wife|resent\w*|default parent|division of labou?r|he doesn'?t|doesn'?t help)\b"),
    ("family_inlaws_visitors", r"\b(in-?laws?|mother-?in-?law|\bmil\b|\bfil\b|grandparents?|grandmas?|grandmothers?|visitors?|boundar(y|ies)|unsolicited)\b"),
    ("return_to_work_childcare", r"\b(maternity leave|parental leave|mat leave|return(ing)? to work|back to work|daycare|day care|nursery|childcare|child care|nann(y|ies)|fmla|pump(ing)? at work)\b"),
    ("gear_registry_money", r"\b(registry|strollers?|car seats?|cribs?|bassinets?|snoo|baby monitors?|budget\w*|afford\w*|expensive|cost(s|ly)?|worth it|babylist|must[- ]haves?)\b"),
    ("travel_outings", r"\b(flights?|flying|airplane|plane|road trips?|travel\w*|vacation|holiday|restaurants?|outings?|leave the house|getting out of the house)\b"),
    ("baby_names", r"\b(baby names?|name (ideas|suggestions|help)|middle names?|first names?)\b"),
    ("memory_keeping", r"\b(baby book|photo ?books?|albums?|keepsakes?|newborn (photos?|shoot|session)|milestone (cards|photos?)|scrapbook\w*)\b"),
    ("second_baby_twins_prem", r"\b(second baby|baby #? ?2|age gap|two under (two|2)|twins?|nicu|premature|preemie|corrected age|adjusted age|siblings?)\b"),
    ("mom_fitness_weight", r"\b(lose (the )?weight|baby weight|work ?outs?|exercis\w*|gym|running|prenatal (yoga|pilates)|bounce back|body after)\b"),
    ("relationship_intimacy", r"\b(sex|intimacy|libido|marriage|relationship)\b"),
    ("baby_minor_health", r"\b(rash|eczema|cradle cap|baby acne|fever|sick|a cold|teething|vaccin\w*|pediatrician|paediatrician|gp\b|doctor)\b"),
    ("what_to_do_all_day", r"\b(what (do|should) (i|we|you) do with|all day|bored|entertain\w*|activities|play ideas|screen time|\btv\b|overstimulat\w*)\b"),
    ("information_overload", r"\b(conflicting (advice|info\w*)|so much (advice|information)|googl\w*|2 ?am|3 ?am|overwhelm\w* (by|with) (advice|info)|every(one|body) says|too much information)\b"),
]
COMPILED = [(k, re.compile(p, re.I)) for k, p in PATTERNS]


def iter_posts(path):
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--windows", default=DEFAULT_WINDOWS)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    files = sorted(f for f in os.listdir(args.windows) if f.endswith("_submissions.jsonl.gz"))
    totals = Counter()
    available = Counter()
    hits = defaultdict(Counter)
    months = defaultdict(set)
    anyhit = Counter()
    for f in files:
        sub = f.split("_submissions")[0]
        for p in iter_posts(os.path.join(args.windows, f)):
            totals[sub] += 1
            text = (p.get("title") or "") + "\n" + (p.get("selftext") or "")
            st = p.get("selftext") or ""
            if st in ("[removed]", "[deleted]") or not text.strip():
                continue
            available[sub] += 1
            ts = p.get("created_utc")
            if ts:
                months[sub].add(datetime.fromtimestamp(float(ts), tz=timezone.utc).strftime("%Y-%m"))
            matched = False
            for k, rx in COMPILED:
                if rx.search(text):
                    hits[sub][k] += 1
                    matched = True
            if matched:
                anyhit[sub] += 1

    subs = [f.split("_submissions")[0] for f in files]
    os.makedirs(args.out, exist_ok=True)
    csv_path = os.path.join(args.out, "width-reddit-mention-share.csv")
    md_path = os.path.join(args.out, "width-reddit-mention-share.md")

    all_avail = sum(available.values())
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["sub_niche", "all_subs_posts", "all_subs_share"] + [f"{s}_posts" for s in subs] + [f"{s}_share" for s in subs])
        for k, _ in PATTERNS:
            tot = sum(hits[s][k] for s in subs)
            row = [k, tot, f"{tot / all_avail:.4f}"]
            row += [hits[s][k] for s in subs]
            row += [f"{hits[s][k] / available[s]:.4f}" if available[s] else "" for s in subs]
            w.writerow(row)

    lines = []
    lines.append("# Width proxy — share of harvested Reddit posts mentioning each sub-niche\n")
    lines.append(f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by `_tools/subniche_mention_share.py` over `global/_raw/reddit-deep/windows/2025-h2-v1/` (July–December 2025 submissions, nine communities). "
                 "**Read this as the share of available post bodies whose title+text matches a wide regex, not as the prevalence of people or problems.** One post can match several rows. Removed/deleted/empty bodies are excluded from the denominator. Regexes favour recall; each is printed at the bottom so you can judge the noise.\n")
    lines.append("## Posts per community\n")
    lines.append("| community | downloaded | available bodies | months | any sub-niche match |")
    lines.append("|---|---:|---:|---:|---:|")
    for s in subs:
        lines.append(f"| r/{s} | {totals[s]:,} | {available[s]:,} | {len(months[s])} | {anyhit[s]:,} ({anyhit[s] / available[s]:.0%}) |" if available[s] else f"| r/{s} | {totals[s]:,} | 0 | 0 | 0 |")
    lines.append(f"| **all** | **{sum(totals.values()):,}** | **{all_avail:,}** | | **{sum(anyhit.values()):,}** |\n")

    lines.append("## Mention share by sub-niche (all nine communities), sorted\n")
    lines.append("| sub-niche | posts matching | share of available | top communities by share |")
    lines.append("|---|---:|---:|---|")
    ranked = sorted(PATTERNS, key=lambda kp: -sum(hits[s][kp[0]] for s in subs))
    for k, _ in ranked:
        tot = sum(hits[s][k] for s in subs)
        top = sorted(((hits[s][k] / available[s], s) for s in subs if available[s]), reverse=True)[:3]
        lines.append(f"| {k} | {tot:,} | {tot / all_avail:.1%} | " + ", ".join(f"r/{s} {sh:.0%}" for sh, s in top) + " |")
    lines.append("")

    lines.append("## Share by community (rows = sub-niche, columns = community)\n")
    lines.append("| sub-niche | " + " | ".join(f"r/{s}" for s in subs) + " |")
    lines.append("|---|" + "---:|" * len(subs))
    for k, _ in ranked:
        lines.append(f"| {k} | " + " | ".join(f"{hits[s][k] / available[s]:.1%}" if available[s] else "" for s in subs) + " |")
    lines.append("")

    lines.append("## Regexes used\n")
    for k, p in PATTERNS:
        lines.append(f"- `{k}`: `{p}`")
    lines.append("")
    lines.append("Caveats: r/ExclusivelyPumping, r/BabyLedWeaning and r/workingmoms are topic communities, so their own topic dominates their column and inflates the all-communities total for pumping, solids and work return. Pregnancy communities (r/BabyBumps, r/BabyBumpsCanada, r/BabyBumpsandBeyondAu, r/BeyondTheBumpUK in part) inflate pregnancy rows. The useful comparison is within the general communities r/NewParents and r/beyondthebump. No sleep, breastfeeding, toddler, potty or mental-health community was harvested; those rows are therefore lower bounds for width.")

    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"wrote {csv_path}\nwrote {md_path}")
    print(f"posts {sum(totals.values()):,} available {all_avail:,}")
    for k, _ in ranked:
        tot = sum(hits[s][k] for s in subs)
        print(f"{k:28s} {tot:7,} {tot / all_avail:6.1%}")


if __name__ == "__main__":
    main()
