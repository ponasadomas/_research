# Source map — sleep-mother

Written 2026-10-25 (Phase 2). Volume figures are probe counts, not harvest totals; harvest totals go in each source note's ledger. Shared Reddit harvest: `../../_shared/_raw/reddit-2026/` (2026-04-01 → 2026-10-25). Not harvested and why: `not-harvested.md`.

## Communities and bulk sources

| source | class | volume | access | priority | plan |
|---|---|---|---|---|---|
| r/sleeptrain | the parent's exhaustion inside baby-sleep posts | 86/day | Arctic Shift API, 200 on 2026-10-25 | high | filter mother's own sleep |
| r/pregnant, r/BabyBumps | pregnancy insomnia | ~400/day | Arctic Shift API, 200 on 2026-10-25 | high | filter insomnia, can't sleep, pregnancy pillow |
| r/postpartumprogress, r/Postpartum_Depression | postpartum sleep and mood | 15/day + probe cap | Arctic Shift API, 200 on 2026-10-25 | medium | filter sleep only; crisis posts dropped by rule |
| r/insomnia | adult insomnia, oblique | probe cap hit | Arctic Shift API, 200 on 2026-10-25 | medium | harvest later; filter baby, postpartum, newborn, pregnant |
| r/NewParents, r/beyondthebump, r/beyondthebumpUK, r/FirstTimeMom | main subreddits (shared) | ~240 posts/day together | Arctic Shift API, 200 on 2026-10-25 | high | filter `../_shared/_raw/reddit-2026/` with this niche's regex |
| r/Mommit, r/Parenting, r/sahm, r/workingmoms | wide subreddits (shared) | ~300 posts/day | Arctic Shift API | high | same filter; these hold the experienced-mother voice |
| r/daddit | the partner's side (shared) | ~100/14 days probe cap hit | Arctic Shift API | medium | filter for this niche's problem told from the partner's side |
| OP replies on kept posts | thread follow-ups | per kept post | Arctic Shift comments endpoint | high | fetch only for kept posts, after triage |
| global/ Reddit archive files, Jul–Dec 2025 | older window, frozen | 112,665 posts, 9 subs | on disk | medium | filter by id; quotes cite `../global/_raw/...` raw files; read only items global/ left unread |
| global/ forums: JustParents (505 threads), MSE (343), GeoBaby (183) | niche forums, frozen | 1,031 threads | on disk | medium | filter for this niche; read unread matches |
| Parenting Stack Exchange official API | Q&A | 1,155 questions in global/ | API | low | re-query by this niche's tags |
| App Store / Google Play public pages | app reviews | 10 per storefront (Apple), 3 per app (Play) | public pages only; continuation restricted by robots | medium | every competing app below, all storefronts US/GB/CA/AU |
| Trustpilot | competitor reviews | unknown | Solid Starts page 403 on 2026-10-24 | low | probe once per competitor; log status |
| Barnes & Noble edition review lists | book reviews | few reviews per edition | 200 in global/ | medium | every adjacent bestseller below |
| Meta Ad Library | ads running | see `../main/ads-running/` | Chrome MCP, owner watching | high | 10+ searches for this niche, announced before running |
| ClickBank snapshots | marketplace | monthly snapshots on disk | on disk | low | list every offer in this niche |
| Competitor sites | competitors | see list below | public pages; robots checked first | high | save every sales, quiz and order page; teardown each |

## Market

- **Competitors to tear down:** Sleepio, Stellar Sleep, Calm and Headspace sleep content, CBT-I Coach, night nannies and postpartum doula services, Hatch (adult), pregnancy pillows (light touch); any seller found in the Ad Library under mother-sleep phrases.
- **Adjacent books (Barnes & Noble reviews; Goodreads and Amazon are robots-restricted):** Say Good Night to Insomnia, Hello Sleep, The Sleep Solution, The Fourth Trimester (sleep chapters), The First Forty Days.
- **Apps (public review pages):** Sleepio, Stellar Sleep, Calm, Headspace, BetterSleep, Slumber.
- **Ad Library searches planned (exact phrases unless noted):** "postpartum insomnia" · "can't sleep when baby sleeps" · "sleep deprived mom" · "pregnancy insomnia" · "exhausted mom" · "mom sleep" · "new mom sleep" · "cbt-i" · "night nanny" · "postpartum doula".

## Sent to the owner

2026-10-25, with `../../PLAN-2026-10-25.md`. Owner tips go here when they arrive.
