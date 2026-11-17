# Brief: re-read material the filter kept out of the global research set

You are reader **UR07** of 13. Working directory: the `ads` repo.
Research set: `mamivio.com/research/global/` (mother-and-baby research across niches).
Your assignment (293 units): `scratchpad/unfilter-reread/assign-ur07.tsv` inside that
folder. Columns: stage that dropped it, unit id, raw file, the reason recorded then.
Other readers run at the same time on other assignments. Write only the two files named
under "Your output". Never modify `_raw/`, `synthesis/`, other readers' files, or any
script. No network. Do not use git.

## Why

The owner's ruling (2026-11-16): research never filters or censors. Earlier rules kept
these posts and threads, or passages in them, out of the research because of their subject
(clinical detail, loss, mental health, crisis, coercion, minors, "safety"), at triage,
during reading or when quotes were pulled. They are saved on disk. Read them now, in full,
and extract what people actually say. The rules are in `~/GitHub/_research/README.md`
("Research never censors", "Conventions") and `global/synthesis/unfilter-report.md`.

## How

1. Read `global/README.md`: what the set is for, the quote schema, the vocabulary of
   speakers, stages, types and themes. Follow it. Look at an existing file in
   `global/voice/` from the same kind of source to see which extra fields that source
   carries (`source_class`, `evidence_kind`, `post_id` and so on) and fill them the same way.
2. For every row, open the raw file (path is relative to `global/`) and read the unit in
   full. Most raw files hold one unit. A few are bundles shared by many rows (`.gz` and
   `.jsonl` files): find the unit inside by its unit id. Forum threads are `.json`: read
   every post in the thread. Where a row says reading stopped partway, read the rest.
3. **The only reason to take no quote is that the unit says nothing about mothers, babies,
   pregnancy, or what parents need, buy or struggle with.** Subject matter is never a
   reason. Whatever is clinical, uncomfortable, angry or raw is quoted like anything else.
   The reason recorded in your assignment is history, not an instruction.
4. If the set already holds quotes from the same unit (`voice/*.jsonl` records with the
   same `raw_file`, or the row says passages were left out), extract only what is not
   already quoted.
5. Extract verbatim quotes in the set's schema. Ids: `glu07-NNNN`, starting at 0001,
   never reused. `raw_file` is the exact file you read, relative to `global/`. Quotes must
   match the raw text exactly; trim only with ` […] `. Do not add `marketing_eligible`,
   `research_only` or any field that marks a quote as restricted. Label provenance where
   it matters (commercial, second-hand, fictional, AI-written) in `context` or
   `evidence_kind`; never drop a quote for it.

## Your output (inside `mamivio.com/research/global/`)

- `voice/reddit-ur07.jsonl`: your quotes, one JSON object per line. (The file name says
  reddit for the scripts' sake; it holds your quotes from every kind of source.)
- `sources/reddit-reading-ur07.md`: a ledger with one line per assigned row: the unit id
  exactly as written in the assignment, how many quotes, and if none, why (says nothing
  about the subject, "nothing new beyond existing quotes", or text not available). Then a
  section, "What these units add": the patterns you saw that `synthesis/findings.md` and
  `synthesis/niche-opportunities.md` lack or get wrong, each with quote ids. Say plainly
  if much of your assignment had nothing to quote.
- If a unit's text cannot be found or is incomplete on disk, say so in the ledger. Do not guess.

## Check before you finish

For every quote you wrote, confirm programmatically that its text occurs in its `raw_file`
(decompress `.gz`, decode JSON for `.json` and `.jsonl`). Report the counts: rows assigned,
read, not found, quoted, quotes written, quotes verified.
