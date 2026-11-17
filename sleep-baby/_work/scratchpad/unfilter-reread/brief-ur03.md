# Brief: re-read posts the filter kept out of the sleep-baby build

You are reader **UR03** of 24. Working directory: the `ads` repo.
Build: `mamivio.com/research/sleep-baby/` ("Mamivio — Baby and toddler sleep, 0–36 months").
Your assignment: `scratchpad/unfilter-reread/assign-ur03.tsv` (inside that build).
Other readers run at the same time on other assignments. Write only the two files named
under "Your output". Never modify `_raw/`, `synthesis/`, other readers' files, or shared
tools. No network. Do not use git.

## Why

The owner's ruling (2026-11-16): research never filters or censors. An earlier rule kept
these posts, or passages in them, out of the research because of their subject (medical
detail, diagnosis, loss, mental health, crisis, abuse, "safety"), at intake, at triage or
during reading. They are saved on disk. Read them now, in full, and extract what parents
actually say.

## How

1. Read `sleep-baby/README.md` (the niche, quote schema, vocabulary) and
   `_shared/_tools/brief-reading.md` (how a reader works). Follow them.
2. For every row in your assignment, find the full text. Unit files are in
   `mamivio.com/research/_shared/_raw/reddit-2026/units/<subreddit>-<postid>.txt`. If there
   is none, take the post from `_shared/_raw/reddit-2026/<subreddit>.posts.jsonl`. Read the
   whole thing.
3. **The only reason to take no quote is that the post says nothing about this niche**, as
   the build's README defines it. Subject matter is never a reason. Whatever is
   uncomfortable, medical, angry or raw is quoted like anything else.
4. If the build already holds quotes from the same post (the row says passages were left
   out, or `voice/*.jsonl` has records with the same `raw_file`), extract only what is not
   already quoted. Do not duplicate existing quotes.
5. Extract verbatim quotes in the build's schema. Ids: `sbu03-NNNN`, starting at 0001,
   never reused. `raw_file` must point at the exact file you read, relative to the build
   folder as the schema says. Quotes must match the raw text exactly.

## Your output (inside `mamivio.com/research/sleep-baby/`)

- `voice/reddit-ur03.jsonl`: your quotes, one JSON object per line.
- `sources/reddit-reading-ur03.md`: a ledger with one line per assigned row: the row's
  id exactly as written in the assignment, how many quotes, and if none, why (relevance
  only, or "nothing new beyond existing quotes"). Then a section, "What these posts add":
  the patterns you saw that `synthesis/findings.md` lacks or gets wrong, each with quote
  ids. Say plainly if much of your assignment was off-niche.
- If a row's text cannot be found, list it in the ledger as not found. Do not guess.

## Check before you finish

For every quote you wrote, confirm programmatically that its text occurs in its `raw_file`
(decode JSON when the raw file is `.jsonl`). Report the counts: rows assigned, read, not
found, quoted, quotes written, quotes verified.
