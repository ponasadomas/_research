#!/usr/bin/env python3
"""Phase 2 source maps for the five niche folders, 2026-10-25. Overwrites source-map.md only if --force."""
import os, sys
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
FORCE = "--force" in sys.argv

COMMON = [
 ("r/NewParents, r/beyondthebump, r/beyondthebumpUK, r/FirstTimeMom", "main subreddits (shared)", "~240 posts/day together", "Arctic Shift API, 200 on 2026-10-25", "high", "filter `../_shared/_raw/reddit-2026/` with this niche's regex"),
 ("r/Mommit, r/Parenting, r/sahm, r/workingmoms", "wide subreddits (shared)", "~300 posts/day", "Arctic Shift API", "high", "same filter; these hold the experienced-mother voice"),
 ("r/daddit", "the partner's side (shared)", "~100/14 days probe cap hit", "Arctic Shift API", "medium", "filter for this niche's problem told from the partner's side"),
 ("OP replies on kept posts", "thread follow-ups", "per kept post", "Arctic Shift comments endpoint", "high", "fetch only for kept posts, after triage"),
 ("global/ Reddit archive files, Jul–Dec 2025", "older window, frozen", "112,665 posts, 9 subs", "on disk", "medium", "filter by id; quotes cite `../global/_raw/...` raw files; read only items global/ left unread"),
 ("global/ forums: JustParents (505 threads), MSE (343), GeoBaby (183)", "niche forums, frozen", "1,031 threads", "on disk", "medium", "filter for this niche; read unread matches"),
 ("Parenting Stack Exchange official API", "Q&A", "1,155 questions in global/", "API", "low", "re-query by this niche's tags"),
 ("App Store / Google Play public pages", "app reviews", "10 per storefront (Apple), 3 per app (Play)", "public pages only; continuation restricted by robots", "medium", "every competing app below, all storefronts US/GB/CA/AU"),
 ("Trustpilot", "competitor reviews", "unknown", "Solid Starts page 403 on 2026-10-24", "low", "probe once per competitor; log status"),
 ("Barnes & Noble edition review lists", "book reviews", "few reviews per edition", "200 in global/", "medium", "every adjacent bestseller below"),
 ("Meta Ad Library", "ads running", "see `../main/ads-running/`", "Chrome MCP, owner watching", "high", "10+ searches for this niche, announced before running"),
 ("ClickBank snapshots", "marketplace", "monthly snapshots on disk", "on disk", "low", "list every offer in this niche"),
 ("Competitor sites", "competitors", "see list below", "public pages; robots checked first", "high", "save every sales, quiz and order page; teardown each"),
]
NOT = [
 ("Goodreads", "robots bans GPTBot (global/ 2026-10-24)"),
 ("Amazon reviews", "robots bans GPTBot and ChatGPT-User"),
 ("BabyCenter, What to Expect, BabyandBump, Mothering", "robots/terms restrict automated collection"),
 ("Mumsnet, Netmums, HealthUnlocked", "robots/403"),
 ("YouTube search and comments", "robots disallows search and comment routes; channel pages only"),
 ("Facebook groups, TikTok and Instagram comments, Discord", "private or no permitted public route; owner may grant access"),
]

S = {
 "sleep-baby": dict(
  subs=[("r/sleeptrain", "core subreddit", "86 posts on 2026-09-02", "high", "every post 2026-04-01 → 2026-10-25; filter only to drop off-topic"),
        ("r/toddlers", "toddler sleep", "115/day", "high", "filter sleep"),
        ("r/GentleParenting, r/AttachmentParenting, r/ScienceBasedParenting", "the values side of sleep training", "≤100/14 days probe cap", "medium", "filter sleep; the people who refuse sleep training")],
  comp="Betteroo (quiz.betteroo.ai, walk the quiz), Let's Sleep (SamCart), Taking Cara Babies, Just Chill Baby Sleep, Good Inside Baby sleep program, Smart Starts, Sleep Nanny, Little Slumber Stars, Baby Sleep Consultant (.co), Happy Sleep Co, Huckleberry SweetSpot, Napper, Smart Sleep Coach, BedtimeCoach, Dawnly, Precious Little Sleep, Cradlewise/Nanit (hardware, light touch)",
  books="Precious Little Sleep, Taking Cara Babies (no book; course), The Happy Sleeper, Cribsheet (sleep chapters), On Becoming Babywise, Healthy Sleep Habits Happy Child, The No-Cry Sleep Solution, 12 Hours' Sleep by 12 Weeks Old",
  apps="Huckleberry, Napper, Smart Sleep Coach (Owlet), Baby Daybook, Betteroo app if any",
  ads="\"sleep training\" course · \"self settling\" · \"wake windows\" · \"sleep regression\" · \"4 month sleep regression\" · \"contact naps\" · \"baby sleep\" quiz · \"sleep plan\" personalized · \"toddler sleep\" · \"early waking\" · brand Pages: Betteroo, Let's Sleep, Taking Cara, Just Chill, Good Inside, Huckleberry"),
 "sleep-mother": dict(
  subs=[("r/sleeptrain", "the parent's exhaustion inside baby-sleep posts", "86/day", "high", "filter mother's own sleep"),
        ("r/pregnant, r/BabyBumps", "pregnancy insomnia", "~400/day", "high", "filter insomnia, can't sleep, pregnancy pillow"),
        ("r/postpartumprogress, r/Postpartum_Depression", "postpartum sleep and mood", "15/day + probe cap", "medium", "filter for sleep relevance; retain crisis material"),
        ("r/insomnia", "adult insomnia, oblique", "probe cap hit", "medium", "harvest later; filter baby, postpartum, newborn, pregnant")],
  comp="Sleepio, Stellar Sleep, Calm and Headspace sleep content, CBT-I Coach, night nannies and postpartum doula services, Hatch (adult), pregnancy pillows (light touch); any seller found in the Ad Library under mother-sleep phrases",
  books="Say Good Night to Insomnia, Hello Sleep, The Sleep Solution, The Fourth Trimester (sleep chapters), The First Forty Days",
  apps="Sleepio, Stellar Sleep, Calm, Headspace, BetterSleep, Slumber",
  ads="\"postpartum insomnia\" · \"can't sleep when baby sleeps\" · \"sleep deprived mom\" · \"pregnancy insomnia\" · \"exhausted mom\" · \"mom sleep\" · \"new mom sleep\" · \"cbt-i\" · \"night nanny\" · \"postpartum doula\""),
 "development": dict(
  subs=[("r/Montessori", "play at home", "~4/day", "high", "every post; filter infant/toddler"),
        ("r/toddlers", "12–24 month development", "115/day", "medium", "filter development"),
        ("r/ScienceBasedParenting", "evidence-seeking parents", "probe cap", "medium", "filter development"),
        ("r/NICUParents", "corrected age", "probe cap", "low", "not harvested yet; filter corrected age, milestones; retain all relevant evidence")],
  comp="Pirmi Žingsniai and the HU clone (already read in `../main/ads-running/`), Kinedu, BabySparks, Pathways, Wonder Weeks, Lovevery (play kits + app), Bloom Baby Classes, Baby Acrobatics, First Step Method, CDC Milestone Tracker, Tadpoles/Kinderling-style curriculum sellers, Etsy age-by-month activity printables",
  books="The Montessori Baby, The Wonder Weeks, What to Expect the First Year, Simplest Baby Book, Brain Rules for Baby, Your Baby's First Year (AAP)",
  apps="Kinedu, BabySparks, Pathways, Wonder Weeks, Lovevery, CDC Milestone Tracker",
  ads="\"baby activities\" · \"what to do with baby\" · \"tummy time\" · \"baby development\" guide · \"milestones\" · \"month by month\" baby · \"play ideas\" · \"montessori baby\" · \"Babafejlődési\" (HU) · brand Pages: Kinedu, BabySparks, Lovevery, Pathways"),
 "toddler-behaviour": dict(
  subs=[("r/toddlers", "core subreddit", "115/day", "high", "every post 2026-04-01 → 2026-10-25"),
        ("r/pottytraining", "core potty subreddit", "20/day", "high", "every post"),
        ("r/GentleParenting, r/AttachmentParenting", "method communities", "≤100/14 days probe cap", "high", "every post"),
        ("r/ScienceBasedParenting", "evidence-seeking", "probe cap", "medium", "filter toddler behaviour")],
  comp="Big Little Feelings (Potty Training Made Simple, Winning the Toddler Stage, Big Feelers), Good Inside, UpAiry (method page), Potty Training Consultant, Oh Crap! Potty Training, Just Chill potty guide, MindNest / bloomlittle.com, parentPRO, Parenting with Rishika, Jackie Black, Positive Parenting Solutions, Janet Lansbury (Unruffled)",
  books="Oh Crap! Potty Training, Good Inside, How to Talk So Little Kids Will Listen, No Bad Kids, The Whole-Brain Child, The Happiest Toddler on the Block, Hunt Gather Parent",
  apps="Good Inside app, Big Little Feelings (if any), Potty training apps (Pull-Ups, potty timers)",
  ads="\"potty training\" course · \"potty train\" · \"3 day potty training\" · \"toddler tantrums\" · \"toddler hitting\" · \"gentle parenting\" · \"toddler behavior\" · \"big feelings\" · \"how to get your toddler to listen\" · brand Pages: Big Little Feelings, Good Inside, UpAiry, Oh Crap"),
 "pregnancy-birth": dict(
  subs=[("r/pregnant", "core subreddit", "291/day", "high", "every post; largest single source in the plan"),
        ("r/BabyBumps", "core subreddit", "103/day", "high", "every post"),
        ("r/PregnancyUK", "UK maternity care", "probe cap", "medium", "every post"),
        ("r/Doulas", "the professional side", "~2/day", "medium", "every post"),
        ("r/GestationalDiabetes, r/HyperemesisGravidarum", "condition subs", "probe cap", "low", "not harvested yet; assess research relevance without subject-based exclusions"),
        ("global/ BabyBumps, BabyBumpsCanada, BabyBumpsandBeyondAu, Jul–Dec 2025", "older window", "on disk", "medium", "global/ left most B/C tiers unread")],
  comp="Pirmi pregnancy guide (LT + HU, already read), hypnobirthing courses (The Positive Birth Company, Hypnobirthing Australia, KG Hypnobirthing, Mongan Method), birth courses (Mommy Labor Nurse, Bump Academy, Birth It Up, Pulling Down the Moon), prenatal fitness (Every Mother, Expecting Empowered, BirthFit, Moms Into Fitness), Expectful, Flo, BabyCenter, Ovia, What to Expect app, Rooted Birth, Beyond Birthing (global/ teardowns)",
  books="Expecting Better, Ina May's Guide to Childbirth, The Positive Birth Book, Mama Natural Week-by-Week, Real Food for Pregnancy, The Birth Partner, What to Expect When You're Expecting, The First Forty Days",
  apps="Flo, BabyCenter, What to Expect, Ovia, Pregnancy+, Expectful, The Bump",
  ads="\"birth course\" · \"hypnobirthing\" · \"labor prep\" · \"birth preparation\" · \"pregnancy workout\" · \"prenatal course\" · \"second pregnancy\" · \"pregnancy guide\" · \"Várandóssági\" (HU) · brand Pages: Positive Birth Company, Mommy Labor Nurse, Every Mother, Expecting Empowered"),
}

def table(rows):
    out = ["| source | class | volume | access | priority | plan |", "|---|---|---|---|---|---|"]
    out += [f"| {' | '.join(r)} |" for r in rows]
    return "\n".join(out)

for slug, s in S.items():
    d = os.path.join(ROOT, slug, "sources")
    rows = [(a, b, c, "Arctic Shift API, 200 on 2026-10-25" if a.startswith("r/") else "on disk", p, e) for a, b, c, p, e in s["subs"]] + COMMON
    p = os.path.join(d, "source-map.md")
    if os.path.exists(p) and not FORCE:
        print("exists, kept:", p); continue
    open(p, "w").write(f"""# Source map — {slug}

Written 2026-10-25 (Phase 2). Volume figures are probe counts, not harvest totals; harvest totals go in each source note's ledger. Shared Reddit harvest: `../../_shared/_raw/reddit-2026/` (2026-04-01 → 2026-10-25). Not harvested and why: `not-harvested.md`.

## Communities and bulk sources

{table(rows)}

## Market

- **Competitors to tear down:** {s['comp']}.
- **Adjacent books (Barnes & Noble reviews; Goodreads and Amazon are robots-restricted):** {s['books']}.
- **Apps (public review pages):** {s['apps']}.
- **Ad Library searches planned (exact phrases unless noted):** {s['ads']}.

## Sent to the owner

2026-10-25, with `../../PLAN-2026-10-25.md`. Owner tips go here when they arrive.
""")
    open(os.path.join(d, "not-harvested.md"), "w").write("# Not harvested\n\n2026-10-25. Inherited from `../../global/sources/not-harvested.md`; re-probe only if a finding needs it.\n\n| source | why |\n|---|---|\n" + "\n".join(f"| {a} | {b} |" for a, b in NOT) + "\n| Subreddits with 0 posts in the 2026-09 probe: PostpartumAnxiety, toddlerpottytraining, Hypnobirthing, BirthStories, speechdelays, CSectionMoms, Postpartum, PPDsupport, BabyBumpsUK, Mumsnet | 0 in probe window; name may be wrong or the sub private/banned. Unresolved, not nonexistent |\n")
    print("wrote", slug)
