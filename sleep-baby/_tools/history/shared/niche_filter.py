#!/usr/bin/env python3
"""Tier every harvested post for one niche and write triage cards for tier A.

    python3 -I niche_filter.py <niche> [--label filter-v1] [--dry]

Reads ../_raw/reddit-2026/*.posts.jsonl (2026-04-01 -> 2026-10-25). Writes
<niche>/_raw/reddit/<label>/{index.jsonl, A|B|C|unavailable|safety-candidates.jsonl, cards/*.txt, cards-index.jsonl, summary.json}.
Filters choose what to read; they never replace reading. No ranking, no top-N cap.
Frozen: refuses to overwrite an existing label.
"""
import collections, datetime, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESEARCH = os.path.normpath(os.path.join(HERE, "..", ".."))
RAW = os.path.join(RESEARCH, "_shared", "_raw", "reddit-2026")

PURCHASE = r"\b(?:paid|pay(?:ing)? for|bought|buy(?:ing)? (?:a|the|her|his|their)|purchas\w*|refund\w*|subscri\w*|worth (?:it|the money)|waste of money|expensive|overpriced|courses?|program(?:me)?s?|consultants?|coach(?:es|ing)?|ebook|pdf|\$\s?\d+|£\s?\d+|€\s?\d+|taking cara|huckleberry|sweet ?spot|napper|good inside|big little feelings|lovevery|kinedu|babysparks|oh crap|hypnobirth\w*|birth (?:course|class)|antenatal class\w*|prenatal class\w*|sleepio|calm app|headspace|night nanny|postpartum doula)\b"
TOOLWORD = r"\b(?:plan|method|guide|book|app|class|schedule|routine)s?\b"
PAIN = r"\b(?:exhaust\w*|desperate\w*|losing my mind|wits.? end|breaking point|can.?t (?:do|take) (?:this|it)|sob(?:bing|bed)?|crying|cried|resent\w*|rage|snapp(?:ed|ing)|terrified|scared|panic\w*|overwhelm\w*|hopeless|failing|failure|guilt\w*|asham\w*|embarrass\w*|zombie|sanity|please help|at a loss|nothing (?:works|is working|has worked)|tried everything|dread\w*|miserable|drowning|burn(?:ed|t)? out|defeated|frustrat\w*|so tired)\b"
HELP = r"\b(?:any (?:advice|tips|ideas)|what (?:do|should|can) (?:i|we)|how (?:do|did|can|should) (?:i|we|you)|is (?:this|it) normal|anyone else|help\b|advice)\b"
BABY = r"\b(?:baby|babies|newborn|infant|toddler|LO|son|daughter|kid|\d{1,2}\s?(?:mo|mos|months?|m)\b|\d{1,2}\s?(?:wk|wks|weeks?)\s?old|month.?old|year.?old|\d\s?(?:yo|y/o|yr|yrs))\b"
TODDLER = r"\b(?:toddler\w*|preschool\w*|daycare|nursery|\b[1-4]\s?(?:yo|y/o|yr|yrs|years? old)|(?:1[2-9]|[2-4]\d)\s?(?:mo|mos|months?)\b|two.year.old|three.year.old|threenager)\b"
SAFETY_COMMON = r"kill myself|suicid\w*|self.?harm|want to die|hurt (?:myself|my baby|him|her)|shak(?:e|ing|en) (?:the|my) baby|abus\w*|domestic violence|\b(?:1[0-7])\s?(?:f|m)\b|\bi(?:'| a)?m 1[3-7]\b|cps\b"
LOSS = r"miscarr\w*|stillb\w*|still.?born|pregnancy loss|lost (?:the|my|our) baby|\bmmc\b|chemical pregnancy|\btfmr\b|no heartbeat|ectopic|\bd&c\b|angel baby|infant loss|\bsids\b death|passed away|funeral"

N = {
 "sleep-baby": dict(
  core={"sleeptrain"},
  subs={"sleeptrain","toddlers","NewParents","beyondthebump","beyondthebumpUK","FirstTimeMom","Mommit","Parenting","sahm","workingmoms","GentleParenting","AttachmentParenting","ScienceBasedParenting","daddit"},
  topic=r"\b(?:sleep\w*|naps?|napp\w*|wake windows?|bedtime|night ?wak\w*|wakes? (?:up )?(?:every|at|\d)|regression|ferber\w*|\bcio\b|cry(?:ing)? it out|contact naps?|self.?settl\w*|drowsy but awake|early (?:riser|waking|wakeup)|crib|cot\b|bassinet|co.?sleep\w*|bed.?shar\w*|room.?shar\w*|night wean\w*|dream ?feed|huckleberry|sweet ?spot|taking cara|precious little sleep|napper|sleep consultant)\b",
  need=BABY, safety=SAFETY_COMMON + "|" + LOSS),
 "sleep-mother": dict(
  core=set(),
  subs={"sleeptrain","pregnant","BabyBumps","PregnancyUK","NewParents","beyondthebump","beyondthebumpUK","FirstTimeMom","Mommit","Parenting","sahm","workingmoms","postpartumprogress","Postpartum_Depression","daddit"},
  topic=r"(?:\b(?:insomnia|sleep deprivation|sleep.?deprived|can.?t (?:fall )?(?:back )?(?:to )?sleep|cannot sleep|unable to sleep|lie awake|lay awake|lying awake|awake (?:all night|at \d|for hours)|haven.?t slept|running on (?:\d|no|zero|little) (?:hours?|sleep)|\d+ hours? of sleep|my sleep|i (?:barely|never|don.?t|can.?t) sleep|sleep when (?:the )?baby sleeps|take (?:night )?shifts|split (?:the )?nights?|night shifts?|(?:husband|partner|he|spouse) (?:sleeps|slept) (?:through|all night|in)|doesn.?t wake up (?:for|to)|pregnancy pillow|night sweats|racing (?:mind|thoughts) at night|hear(?:ing)? (?:the )?baby (?:cry|crying) (?:when|even)|phantom cr(?:y|ies|ying))\b)",
  need=r"\b(?:i|i.?m|i.?ve|my|me)\b", safety=SAFETY_COMMON + "|" + LOSS + r"|psychosis|intrusive thoughts? (?:of|about) (?:hurting|harming)"),
 "development": dict(
  core={"Montessori"},
  subs={"Montessori","toddlers","NewParents","beyondthebump","beyondthebumpUK","FirstTimeMom","Mommit","Parenting","sahm","workingmoms","ScienceBasedParenting","daddit"},
  topic=r"\b(?:tummy time|milestones?|roll(?:s|ing|ed)? over|rolling|sit(?:s|ting)? up|sitting unassisted|crawl\w*|pull(?:s|ing)? (?:up|to stand)|cruis\w*|first steps|walk(?:ing|s)? yet|not walking|babbl\w*|first words?|no words|saying words|words yet|fine motor|gross motor|activit(?:y|ies)|play ?(?:ideas|time|mat|gym)|what (?:do you|to|do i) do (?:with|all day)|entertain\w*|awake time|floor time|toys?|montessori|wonder weeks|leaps?|development\w*|delay\w*|behind|on track|corrected age|early intervention|physio\w*|occupational therap\w*|speech therap\w*|screen time|kinedu|lovevery|babysparks|pathways)\b",
  need=BABY, safety=SAFETY_COMMON + "|" + LOSS),
 "development-v2": dict(
  core={"Montessori"},
  subs={"Montessori","toddlers","NewParents","beyondthebump","beyondthebumpUK","FirstTimeMom","Mommit","Parenting","sahm","workingmoms","ScienceBasedParenting","daddit"},
  topic=r"\b(?:tummy time|milestones?|roll(?:s|ing|ed)? over|sit(?:s|ting)? up|sitting unassisted|crawl(?:ing|s|ed)?|pull(?:s|ing)? (?:up|to stand)|cruis(?:ing|es)|first steps|walk(?:ing|s)? yet|not walking|babbl\w*|first words?|no words|saying words|words yet|fine motor|gross motor|play ?(?:ideas|mat|gym)|what (?:do you|to|do i) do (?:with (?:a|my|your|the) (?:baby|\d+ ?(?:mo|month|week))|all day)|awake time|floor time|montessori|wonder weeks|leaps?|development(?:al)? (?:activit|play|stage|leap|milestone)\w*|on track (?:developmentally|for)|corrected age|screen time|ms rachel|independent play|play (?:alone|independently|on (?:her|his) own)|kinedu|lovevery|babysparks|pathways)\b",
  need=r"\b(?:baby|babies|newborn|infant|LO|\d{1,2}\s?(?:mo|mos|months?|m)\b|\d{1,2}\s?(?:wk|wks|weeks?)\s?old|month.?old|(?:1[0-9]|2[0-4])\s?(?:mo|months?))\b", safety=SAFETY_COMMON + "|" + LOSS),
 "toddler-behaviour": dict(
  core={"toddlers","pottytraining","GentleParenting"},
  subs={"toddlers","pottytraining","GentleParenting","AttachmentParenting","ScienceBasedParenting","Mommit","Parenting","sahm","workingmoms","FirstTimeMom","NewParents","daddit"},
  topic=r"\b(?:tantrum\w*|meltdowns?|hit(?:s|ting)?|bit(?:e|es|ing)|throw(?:s|ing)|scream\w*|kick\w*|(?:won.?t|doesn.?t|not) listen\w*|defian\w*|boundar\w*|disciplin\w*|time.?outs?|consequences?|gentle parenting|big little feelings|good inside|transitions?|potty|toilet\w*|poop\w*|pee\w*|accidents?|pull.?ups|underwear|oh crap|3.day method|withhold\w*|picky eat\w*|new sibling|jealous\w*|behavio(?:u)?r\w*|clingy|separation anxiety|whin\w*|negotiat\w*|power struggles?|no phase|threenager)\b",
  need=TODDLER, safety=SAFETY_COMMON + "|" + LOSS),
 "pregnancy-birth": dict(
  core={"pregnant","BabyBumps","PregnancyUK","Doulas"},
  subs={"pregnant","BabyBumps","PregnancyUK","Doulas","beyondthebump","beyondthebumpUK","NewParents","FirstTimeMom","Mommit","daddit"},
  topic=r"\b(?:pregnan\w*|trimester|\d{1,2}\s?w(?:ee)?ks?\s?(?:pregnant|\+\d)|\d{1,2}w\d\b|birth\w*|labou?r\w*|induc\w*|epidural|c.?section|csection|vbac|hypnobirth\w*|doula\w*|midwi\w*|\bob\b|ob.?gyn|contractions?|due date|hospital bag|nausea|morning sickness|prenatal|antenatal|perine\w*|pelvic floor|first (?:two|2) weeks|fourth trimester|postpartum recovery|second baby|second pregnancy|third pregnancy)\b",
  need=r".", safety=SAFETY_COMMON + "|" + LOSS + r"|abortion|termination"),
}


def card(rec, body):
    return (f"ID {rec['id']} | r/{rec['subreddit']} | {rec['date'][:10]} | safety_flag={rec['safety_flag']}\n"
            f"TITLE: {rec['title']}\nOPENING: {body[:350]}\nMATCHES: {json.dumps(rec['matches'], ensure_ascii=False)}\n\n")


def main():
    niche = sys.argv[1]
    label = sys.argv[sys.argv.index("--label") + 1] if "--label" in sys.argv else "filter-v1"
    dry = "--dry" in sys.argv
    c = N[niche]
    folder = niche[:-3] if niche.endswith("-v2") else niche
    out = os.path.join(RESEARCH, folder, "_raw", "reddit", label)
    if not dry:
        if os.path.exists(out):
            raise SystemExit(f"frozen output exists: {out}; choose a new --label")
        os.makedirs(os.path.join(out, "cards"))
    topic, need, safety = re.compile(c["topic"], re.I), re.compile(c["need"], re.I), re.compile(c["safety"], re.I)
    purchase, pain, helpq, toolw = re.compile(PURCHASE, re.I), re.compile(PAIN, re.I), re.compile(HELP, re.I), re.compile(TOOLWORD, re.I)
    totals = collections.Counter(); by_sub = collections.defaultdict(collections.Counter)
    files = {} if dry else {t: open(os.path.join(out, f"{t}-candidates.jsonl"), "w") for t in ["A", "B", "C", "unavailable", "safety"]}
    index = None if dry else open(os.path.join(out, "index.jsonl"), "w")
    cards = collections.defaultdict(list)
    for sub in sorted(c["subs"]):
        path = os.path.join(RAW, f"{sub}.posts.jsonl")
        if not os.path.exists(path):
            print("MISSING harvest:", sub); totals["missing_sub"] += 1; continue
        for line in open(path, encoding="utf-8"):
            q = json.loads(line)
            title, body = q.get("title") or "", q.get("selftext") or ""
            text = title + "\n" + body
            totals["scanned"] += 1; by_sub[sub]["scanned"] += 1
            tm = topic.search(text)
            if not tm or (sub not in c["core"] and not need.search(text)):
                continue
            unavailable = body.strip() in ("", "[removed]", "[deleted]")
            pms = sorted({m.group(0).lower() for m in purchase.finditer(text)})
            pns = sorted({m.group(0).lower() for m in pain.finditer(text)})
            hm = helpq.search(text)
            sf = safety.search(text)
            if unavailable: tier = "unavailable"
            elif pms or len(pns) >= 2: tier = "A"
            elif pns or hm or toolw.search(text): tier = "B"
            else: tier = "C"
            date = datetime.datetime.fromtimestamp(int(q["created_utc"]), datetime.timezone.utc).isoformat()
            rec = {"id": q["id"], "subreddit": sub, "created_utc": q["created_utc"], "date": date, "title": title,
                   "body_chars": len(body), "tier": tier, "matches": {"topic": tm.group(0), "purchase": pms[:6], "pain": pns[:6], "help": hm.group(0) if hm else ""},
                   "safety_flag": bool(sf), "safety_match": sf.group(0) if sf else "", "num_comments": q.get("num_comments"),
                   "url": f"https://www.reddit.com/r/{sub}/comments/{q['id']}/", "source_file": f"../_shared/_raw/reddit-2026/{sub}.posts.jsonl"}
            totals[tier] += 1; by_sub[sub][tier] += 1
            if not dry:
                index.write(json.dumps(rec, ensure_ascii=False) + "\n"); files[tier].write(json.dumps(rec, ensure_ascii=False) + "\n")
                if tier == "A": cards[sub].append(card(rec, body))
    chunks = []
    if not dry:
        for sub in sorted(cards):
            buf, n, i = "", 0, 1
            for cd in cards[sub]:
                if buf and len((buf + cd).encode()) > 40000:
                    name = f"A-{sub}-{i:03d}.txt"; open(os.path.join(out, "cards", name), "w").write(buf)
                    chunks.append({"file": f"_raw/reddit/{label}/cards/{name}", "cards": n}); buf, n, i = "", 0, i + 1
                buf += cd; n += 1
            if buf:
                name = f"A-{sub}-{i:03d}.txt"; open(os.path.join(out, "cards", name), "w").write(buf)
                chunks.append({"file": f"_raw/reddit/{label}/cards/{name}", "cards": n})
        open(os.path.join(out, "cards-index.jsonl"), "w").write("".join(json.dumps(x) + "\n" for x in chunks))
    summary = {"niche": niche, "label": label, "window": "2026-04-01 to 2026-10-25 (harvest)", "totals": dict(totals),
               "by_subreddit": {k: dict(v) for k, v in sorted(by_sub.items())}, "card_chunks": len(chunks),
               "tier_rule": "A = topic + explicit purchase/paid-tool/brand signal or 2+ distinct pain words; B = topic + one pain word, a help question or a generic tool word (plan, method, guide, book, app, class, schedule, routine); C = topic only; safety_flag = descriptive regex label only, never changes A/B/C routing; non-core subs also need the niche's person regex",
               "triaged": 0, "kept": 0, "read": 0, "quoted": 0}
    if not dry:
        open(os.path.join(out, "summary.json"), "w").write(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({k: summary[k] for k in ["niche", "totals", "card_chunks"]}))


if __name__ == "__main__":
    main()
