# Phase 9 — Compare Kinedu's "share doing it" numbers with CDC milestone norms

Context: Kinedu's quiz sends a `rate` with every question (we read it as the share of babies of that age who already do it).
We have those rates for every month at which each question is asked: questions.csv (column rate_by_age_months, plus
raw_observations) and questions-by-age.md. We want to know whether Kinedu's shares are honest, inflated (more babies said to do
things than reality → parents look "behind") or deflated (→ parents look "ahead").

Yardstick: CDC "Learn the Signs. Act Early." milestone checklists, 2022 revision. Each CDC milestone is listed at the age by which
**75% or more** of children do it (CDC changed from 50% to 75% in 2022). So for a milestone CDC places at age X months, an honest
share at age X should be roughly 0.75 or higher (and lower at earlier ages).

Network: use `scripts/proxy_curl.sh` for all HTTP (it takes normal curl args). Save every fetched page under raw/cdc/.
Work only in this folder. No browser.

Steps:
1. Fetch the CDC checklists for 2 months, 4, 6, 9, 12 (1 year), 15, 18, 24 (2 years), 30, 36 (3 years), 48 (4 years):
   https://www.cdc.gov/ncbddd/actearly/milestones/milestones-2mo.html (and -4mo, -6mo, -9mo, -1yr, -15mo, -18mo, -2yr, -30mo, -3yr, -4yr).
   If a URL has moved, find the current one on https://www.cdc.gov/ncbddd/actearly/milestones/index.html. Extract every milestone
   sentence with its CDC age and domain (Social/Emotional, Language/Communication, Cognitive, Movement/Physical). Save as raw/cdc/cdc-milestones.csv.
2. Match CDC milestones to Kinedu questions by meaning (same behaviour, same difficulty). Be strict: only pair items that describe
   the same skill at the same level (e.g. CDC 12 mo "Pulls up to stand" ↔ Kinedu "Pulls up to a standing position"). Record a
   confidence (exact / close / loose) and the reason. Aim for as many strict matches as the data allows (expect 40–80).
3. For each matched pair: list Kinedu's shares by month, then the share AT the CDC age if asked that month; otherwise the nearest
   asked month(s) on each side with their shares, and a linear interpolation between them if both sides exist (mark interpolated).
   Verdict per pair: Kinedu share at CDC age ≥ 0.75 = consistent; 0.5–0.75 = Kinedu stricter/later (fewer babies said to do it →
   parents look better); < 0.5 = clearly later than CDC; > 0.95 = Kinedu says nearly all do it earlier than CDC (parents look worse).
4. Write CDC-COMPARISON.md: method, the matched-pairs table (CDC milestone, CDC age, Kinedu question id + text, shares by month,
   share at CDC age, verdict, match confidence), a summary (counts per verdict, median share at CDC age, split by domain and by
   age band 0–12 / 13–24 / 25–48), the unmatched CDC milestones list, and a plain-words conclusion: do Kinedu's numbers make
   babies look behind, ahead, or about right compared with CDC? Separate observed from inferred; note that CDC's 75% is a floor,
   and that "share doing it" is our reading of the rate field. Finish with a 12-line summary.
