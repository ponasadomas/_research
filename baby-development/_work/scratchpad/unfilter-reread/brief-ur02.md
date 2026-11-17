# Brief: re-read posts the filter kept out of the development build

You are reader **UR02**. Working directory: the `ads` repo, branch `research-unfilter`.
Build: `mamivio.com/research/development/`. Your assignment: `scratchpad/unfilter-reread/assign-ur02.tsv` (inside that build).
Four other readers run at the same time on other assignments. Write only the files named
under "Your output". Never modify `_raw/`, `synthesis/`, other readers' files, or shared
tools. No network. Do not use git.

## Why

The owner's ruling (2026-11-16): research never filters or censors. An earlier rule kept
these posts out of the research because of their subject (diagnosis, referral, therapy,
mental health, "safety"), before or during reading. They are saved on disk and were never
quoted. Read them now, in full, and extract what parents actually say.

## How

1. Read `development/README.md` (niche, quote schema, vocabulary) and
   `_shared/_tools/brief-reading.md` (how a reader works). Follow them.
2. For every row in your assignment, find the full text. Unit files are in
   `mamivio.com/research/_shared/_raw/reddit-2026/units/<subreddit>-<postid>.txt`. If there
   is none, take the post from `_shared/_raw/reddit-2026/<subreddit>.posts.jsonl` (a bare
   post id may need looking up across the subreddit files). Read the whole thing.
3. **The only reason to take no quote is that the post says nothing about this niche**
   (baby development and play, 0-24 months: milestones, comparison, worry about being
   behind, what to do with the baby, professionals, apps, products, money). Subject matter
   is never a reason. Diagnosis, referral, therapy, delay, medical detail, a parent's
   mental health, crisis, anger, or anything uncomfortable is quoted like anything else.
4. Extract verbatim quotes in the build's schema. Ids: `dv22-NNNN`, starting at 0001,
   never reused. `raw_file` must point at the exact file you read, relative to the build
   folder as the schema says. Quotes must match the raw text exactly.

## Your output (inside `mamivio.com/research/development/`)

- `voice/reddit-ur02.jsonl`: your quotes, one JSON object per line.
- `sources/reddit-reading-ur02.md`: a ledger with one line per assigned row: the id, how
  many quotes, and if none, why (relevance only). Then a short section, "What these posts
  add": the patterns you saw that the existing `synthesis/findings.md` lacks or gets
  wrong, each with quote ids. Say plainly if most of your assignment was off-niche.
- If a row's text cannot be found, list it in the ledger as not found. Do not guess.

## Check before you finish

For every quote you wrote, confirm programmatically that its text occurs in its `raw_file`.
Report the counts: rows assigned, read, not found, quoted, quotes written, quotes verified.
