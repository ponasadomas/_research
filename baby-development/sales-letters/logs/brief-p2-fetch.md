# Phase 2 — fetch the sales letters from the Wayback Machine

You are a research agent working in `/home/thinkpad/GitHub/ads/mamivio.com/research/development/`. Read `sales-letters/README.md`, then `sales-letters/candidates-A.tsv`, `sales-letters/candidates-B.tsv` and the two `sales-letters/logs/p1*-report.md`. The owner wants at least ten long-form sales letters (one page, headline, ≥1,200 words of body, price or buy CTA, usually a guarantee) that were sold to mothers of 0–24-month babies on development, play, milestones, "what to do with your baby", tummy time, early stimulation, plus adjacent early-learning offers.

## Method
For each candidate, best first (the reports rank them):
1. `python3 -I _tools/wayback.py cdx '<domain or sales url>' --from 2005 --to 2024 --limit 40` to see the capture history. If the sales page lived at a path (e.g. `/index.html`, `/sales`, `/go`, `/letter`), query that path; use `--match prefix` with a trailing slash to see what paths exist. Ignore non-HTML.
2. Fetch **one** representative capture: `python3 -I _tools/wayback.py fetch <timestamp> '<url>' --out _raw/sales-letters/<slug>--<timestamp>.txt`. Check WORDS in the header. If under ~800 words, it is probably a redirect, a frame, a video-only page or a stub: try one other year, or a sub-path the page links to (look for the text of links in the saved file), then stop.
3. If it is a letter (≥1,200 words, headline + body + price/CTA), fetch **two more captures from different years** so we get split-tested headlines: `<slug>--<timestamp>.txt` each. Max four captures per letter.
4. Slug = short lowercase hyphenated product or domain name, stable across captures.
5. Append one row per fetch to `sources/sales-letters.md` (date, slug, source url, timestamp, http, words, letter? yes/no/landing, note).

## Hard limits
- Only `_tools/wayback.py` may touch web.archive.org (one request per 4 s; never run two copies at once). Cap: 220 Wayback requests this run; keep a running count and stop at the cap.
- Never edit a raw file. Never fetch live sites.
- Stop early once you have 12 confirmed letters with 2+ captures each, or at the cap.

## Output
`sales-letters/logs/p2-report.md`: table of every slug with letter? verdict, captures saved (file names, years, word counts), price seen, one-line description; the request count; candidates not reached. Then the full list of raw files for Phase 3.

## RANKED FETCH ORDER (set by the supervisor after reading both Phase 1 reports; work top to bottom)

Core development / play / milestones (do all of these first):
1. babydevelopmentnews.com — "A Practical Guide To Baby Milestones" (ClickBank, captures 2010–2016; try root and any /index or sales path)
2. babypillars.com — BabyPillars Baby Development System 0–24 months (start 20160504183614)
3. activebabiessmartkids.com.au — Active Babies Smart Kids (start 20160101144840; look for a /program or /shop path)
4. brightestbeginning.com/courses/play-develop-thrive/ — Play, Develop, Thrive (start 20220926061658)
5. all-gifted-children.com — How To Develop Your Child's Genius (ClickBank 2008–2012)
6. baby-massage.com — infant massage programme (2011+)
7. milestonesandmotherhood.com — tummy-time / milestone masterclasses (2021+; find the course sales path)
8. healthiest-baby.com — How To Play With Your Baby (2023; still fetch, late lead)
9. "Raising Smarter Babies" and "Your Child Development System" — domains unresolved in candidates-A.tsv; spend at most 6 requests trying the recorded hop targets / CDX on likely names, then drop.
10. mommyjingles.com — Mommy Jingles musical parenting (2016)

Early-learning, adjacent (next):
11. yourbabycanread.com (2008–2014) — fetch 2009 and 2012 captures
12. brillkids.com — find the Little Reader sales page path (2010–2014)
13. gentlerevolution.com — Doman "How To Teach Your Baby To Read"
14. childrenlearningreading.com (2012, 2015, 2018)
15. readingheadstart.com (2017, 2019)
16. winktolearn.com; intellectualbaby.com; babygenius.com; brainybaby.com (one capture each first)
17. signing4babies.com; babysignlanguage.com/basic-full-screen/ (2021); helpyourchildspeak.com

Sleep-adjacent (only after the above, same audience, lower priority; cap 5 letters):
18. babysleepmiracle.com (20170101164901 then 2022), sleepbabysleep.com (2012), babysleepsolution.com (2008–2012), babysleepanswers.com (2010+), fiveminutesleep.com (2017), sleeplady.com (2008)

Landing pages, captured not letters (one capture each, last, if budget remains): kinedu.com 2014 and 2018, babysparks.com 2014, lovevery.com 2018.
