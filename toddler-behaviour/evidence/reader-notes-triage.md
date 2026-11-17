# Reader notes — triage (agents' reports as they arrive)

## TT1 (wave 1, 713 cards: keep 347, drop 366)
- Over half dropped as sleep, weaning or baby posts: the toddler filter pulls in a lot of non-behaviour material, especially r/AttachmentParenting and r/NewParents.
- Potty cards are dominated by Oh Crap! method posts: withholding, accidents only at daycare, regression, daycare rules (a handbook requiring potty training before the 3–5 room). Only 2 success stories, 1 quit.
- Daycare and preschool adjustment is a big cluster: separation anxiety, biting/hitting reports, daycare notes ("work on listening ears") → keep_otherside.
- Other side: critical or involved grandparents ("this isn't normal", worse around Nana), a spouse with lower tolerance for an intense toddler.
- Only 3 keep_purchase in 713: buying is much rarer in toddler posts than in sleep posts (sleep T1–T6: 239 of 4,577).
- Diagnosis questions kept and marked; safety drops neutral.

## TT2 (wave 1, 607 cards: keep 309, drop 298)
- keep_purchase almost all potty: Oh Crap! (book and method, dominant), UpAiry undies, which potty to buy, what to switch to after Oh Crap. Real spending signals rare.
- Small fixes reported: a potty success with a laxative (medical; quote only as belief), a method "sustainable for the parent"; finger toothbrush, a recipe site for fussy eaters.
- About half drops are sleep, SAHM burnout or marriage vents with a toddler in passing.
- Orchestrator override: 1wmjy6e (parent shoved a 2-year-old) kept by TT2, changed to safety drop in `_raw/reddit/triage/wave1-corrections-orchestrator.tsv`.
- Reposts: originals may sit in another reader's cards; dedupe before units.

## TT3 (wave 1, 681 cards: keep 399, drop 282)
- Sleep-only posts (bedtime refusal, night waking) were the largest drop group; kept when the bedtime post was a behaviour fight.
- Oh Crap! in dozens of potty posts: keep_purchase only where the method or book is judged or bought; plain "following Oh Crap" is keep_core with "Oh Crap" in the reason (grep-able).
- Paid help named: Big Little Feelings course (one says it helped with potty; one took it for a 3-year-old and is considering quitting), Brandi Brucks audiobook method, Good Inside, toilet-training consultants, an OT for poop issues, a portable potty "worth it?".
- **New sub-theme: preschool or daycare policy pressure** (keep_otherside): an ultimatum over a 3-year-old's daily accidents, a 23-month-old dismissed after 4 days, a 2.5-year-old expelled for wanting mom, sent home without underwear; parents asking whether to pull the child out.
- Countervoices: a dad pushing back on gentle parenting ("dad gives in"); a post rejecting "militant potty culture".
- 8 cross-sub reposts dropped; later copies may sit in other readers' files: dedupe by title at the merge step.
