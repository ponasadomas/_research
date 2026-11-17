# Reader notes — triage (agents' reports as they arrive)

## T1 (wave 1, 850 cards: keep 459, drop 391)
- Named in purchase keeps: Taking Cara Babies (several; also the swaddle), 12 Hours by 12 Weeks (compared with TCB), Happy Little Sleeper, Sleep Wave, Merlin sleep suit, Owlet, Huckleberry, Napper; SNOO often; a $180 nursing glider called wasted.
- Paid sleep consultants have a visible failure theme: "they're stubborn" said of a 20-month-old, a dispute over wake windows, "gentle" training that still ended in sobbing.
- r/workingmoms (~65/69) and r/daddit (21/23) cards are almost all drops for this niche; r/sleeptrain nearly all keep_core.
- Dropped: sick-baby nights, children 4+, mother-sleep-only posts, reposts (~9), promotions (wake-clock app, surveys, lead-gen).

## T4 (wave 1, 671 cards: keep 449, drop 222)
- About 170 drops are posts in Parenting, Mommit, NewParents, beyondthebump where sleep is a passing mention (agent opened full posts for ambiguous cards).
- 11 exact cross-posts dropped as "duplicate repost of <id>"; cross-reader duplicates not checked yet (orchestrator to dedupe before units).
- Purchase set names: Taking Cara Babies (program and book), Possums Sleep, Precious Little Sleep, Huckleberry (incl. a paid schedule), Napper, SNOO, Cradlewise, Owlet Dream Sock, Magic Merlin (one says it worked), Woolino; consultants incl. one quoted near $1,000 and declined, a $500 search, one funded by a disability-association scholarship.
- Success stories few (9); recurring pattern: trained successfully, then a regression, travel or illness setback.
- Age edge: children nearing 4 dropped (3 ids); ordinary 3-year-olds kept.

## T2 (wave 1, 834 cards: keep 446, drop 388)
- Recurring names: Taking Cara Babies (~8 posts, incl. parents who followed it and still had bad sleep), Huckleberry, SNOO, Owlet, Nara Baby, Woolino, Merlin suit. A parent says they spent "thousands of dollars" on consultants without help (verify in full read).
- **Nara Baby** (free tracker) announced $6.99/month or $69.99 lifetime; three posts react, some asking for a free alternative. Price-reaction posts labelled keep_purchase.
- Jargon: wake-window notation "3/3.5/4", "2 nap to 1 nap", "split nights"; sleep-training "success story" is its own post genre ("3 weeks of Ferber: our success story").
- ~30 drops are postpartum/burnout vents where baby sleep is a passing mention (candidates for sleep-mother). Seller promoting a 30-page newborn sleep guide, tracker promo, automod tests dropped.

## T3 (wave 1, 790 cards: keep 441, drop 349)
- Names: Taking Cara Babies (one parent also paid for a consult), Precious Little Sleep, Moms on Call; Huckleberry (one says tracking made her anxious), Napper; SNOO, Owlet, Love to Dream, Halo, Najell, Snuzpod; consultants, a night nanny; "Actually Sleeping" asked about as "real or a scam?".
- Other side: daycare and caregiver naps (baby "disruptive" at daycare nap, naps collapse after daycare starts, grandparents' schedule clashes); parents content to cosleep and refuse sleep training; a "highly skeptical" mother reporting Ferber success.
- Copy patterns to check in full reads: "have we messed up / broken our baby's sleep?"; slept through until a regression, illness, teething, trip or swaddle drop undid it; re-sleep-training; nap transitions 3→2, 2→1 dominate.
- 9 safety drops with neutral reasons; ~15 cross-post duplicates dropped.

## T5 (wave 1, 689 cards: keep 414, drop 275)
- Purchase names: Taking Cara Babies (course and plans), Huckleberry (app, SweetSpot, sleep plan), SNOO, Owlet, Love to Dream, Woolino. People ask for virtual or "no-cry" consultants, weigh a night nanny; some "on a budget but will pay".
- Partner split as the other side: a husband who won't back Ferber, a partner wary of CIO, a husband who won't take the night shift, a father who rocks to sleep while the mother wants change.
- Re-training after illness, move, teething or daycare start recurs (now noted by T2, T3, T5).
- Safety drops (neutral): an infant breathing emergency while cosleeping, a caregiver in distress at night crying, a caregiver conflict incident. Kept: ordinary unsafe-sleep slips and a fall off a bed as parent worry.

## T6 (wave 1, 743 cards: keep 416, drop 327)
- Names: Taking Cara Babies (a dad "panic bought" it after a failed Ferber nap), Sleep Wave ("day 7... trying not to sound like marketing"), SNOO vs Cradlewise, Huckleberry/SweetSpot, Napper, Nara, Glow Baby; "Sleep coach worth it?"; a Huckleberry data-privacy post.
- Method switching after failure: "total extinction caused sleep anxiety"; "CIO didn't work, what gentle method?".
- Other side: a husband sleep-training after nine months of split nights while his wife refused; grandmothers letting babies sleep late, overdressing, ignoring naps; pushback on "don't hold your baby too much" and "drowsy but awake".
- **Age inconsistency:** T6 dropped plain "3 years old" posts; T1–T5 kept ordinary 3-year-olds. Five sleep posts restored in `_raw/reddit/triage/wave1-corrections-orchestrator.tsv` (1wt8f67, 1wmuts6, 1w0r2n1, 1w4x2nb, 1xcg5lx). 1x61527 (paediatrician disagreement) left dropped.

## Totals after wave-1 triage
4,577 cards → keep_core 2,216 · keep_purchase 239 · keep_otherside 95 · keep_success 75 · drop 1,952 (before the 5 corrections). Cross-reader reposts not yet deduped; readers will flag them.

## Reading so far (orchestrator log)
- R01 purchase: 141 units, 328 quotes, 0 failed. R03 core: 127 units, 327 quotes. R04 core: 128 units, 314 quotes. All verified by the orchestrator; ids unique across the niche.
- R04: almost no purchases in core posts (one sound machine; "money for night nurse" out of reach); most problems ended with a free nap tweak from the thread. Doctors are often the push or the brush-off ("toddlers will be toddlers"). AI chatbots used for tracking and reassurance (sb04-0085, sb04-0298). "Only mum can settle" told by dads (sb04-0159, -0160, -0313, -0239). The temperament ask: "looking for advice from someone who has a baby with a similar temperament" (sb04-0020). Self-identified mothers 129 of 314 quotes.
- R02 success + other side: 73 units, 294 quotes, 0 failed. **Speaker convention set by orchestrator 2026-10-25:** a father (or any author who says they are not the birth mother) writing about the family's nights = `partner`. R01 used `parent_unspecified` for some r/daddit fathers: fix at merge (relabel in a merged copy, never in the reader's file).
- R02 patterns: the personalized plan is what got a full trial ("I didn't have confidence that my random internet schedule would work so I never fully tried", sb02-0007); what turned it was often small and sticking with one method for a set week mattered more than which method; method fit is per baby (check-ins worse → full CIO; Ferber vomiting → chair); partner conflict runs both ways; MIL napping the baby before bedtime recurs; daycare both "just works" and breaks sleep; sceptic voice ("overpriced PDFs and courses", "stop googling wake windows"); relief doesn't last; one mother's own body still wakes hourly after the baby sleeps through (sleep-mother overlap).
- **Night buying, revised (R14):** a mother bought from a Facebook ad half asleep during a 1:45am feed and regretted it (sb14-0204/0205), plus a "sleep deprivation-influenced splurge" (sb14-0206). R05/R07/R08 found no night panic-buying of courses; the night feed is when parents scroll and sometimes buy products. Treat as a small, real pattern.
