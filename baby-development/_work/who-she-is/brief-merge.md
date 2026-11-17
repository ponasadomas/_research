# Brief: who is she? Merge the three readings into one evidence page

Working directory: the `_research` repo. Niche: `baby-development/`. No network. Do not
use git. Write only the file named under "Your output". Never modify anything under
`quotes/`, any `raw/` folder, `_work/` or the other files in `evidence/`.

## Background

Research here answers four questions (root `README.md`, "Four questions"). Question 1 is
**who is she, and what is her life like?** Three readers each read a third of this niche's
2,970 quotes for that question and wrote `baby-development/_work/who-she-is/part-01.md`,
`part-02.md` and `part-03.md`. You merge them into the evidence page that the avatar (the
portrait of the buyer, in another repo) will be written from. Read the root `README.md`
sections "Research never censors", "Three layers" and "Conventions" first.

## Task

1. Read `baby-development/README.md`, all three parts in full, and
   `baby-development/brief.md`. Read the parts side by side: a pattern that is small in
   each share may be large across all three, and a pattern in one share may be
   contradicted in another. Open the quote files (`baby-development/quotes/*.jsonl`) when
   you need more of a pattern.
2. Write one page under these headings, in this order, adding a heading where the parts
   found something that fits nowhere:
   - Her situation
   - Her day
   - Who else has a say
   - What she already follows and believes
   - What she has already tried or bought
   - How she sees herself
   - Who is speaking who is not her
3. Under each heading, for each pattern:
   - one plain line stating it;
   - the strongest quotes, word for word, with ids: enough to show the range, not every
     one. List the further supporting ids after them, so nothing found is lost;
   - the number of quotes across all three parts;
   - what cuts against it, quoted.
   A quote may be left out of the reproduced ones because it repeats what others show,
   never because of its subject. Every id the parts cite for a pattern stays listed.
4. Open the page with:
   - **What this is and its limit**, in three or four sentences: 2,970 quotes from people
     who posted on Reddit between April and October 2026 or reviewed an app; collected for
     a different question; counts are counts of quotes, never of people, and never how
     common something is.
   - **What the quotes cannot tell us**: each thing about her that the quotes are silent
     or nearly silent on, with the count (for example how many quotes say anything about
     her work, her age, her income, her country). This list is as important as the patterns.
5. If `baby-development/statistics/us-first-time-mothers.md` exists, add a last section,
   "Beside the public figures": for each figure in that file, one line on whether the
   quotes agree, disagree or say nothing. Keep the two kinds of evidence visibly apart;
   do not blend a statistic into a pattern drawn from quotes.
6. State only what people say about themselves. Infer nothing about age, income or
   education that was not said. Soften nothing because of its subject.
7. **Layout for quotes, exactly:** the id in square brackets on its own line, then the
   quote as a blockquote (each line starting with a greater-than sign and a space). No
   other layout, no code fences.

## Your output

`baby-development/evidence/who-she-is.md`. Aim for a page a person can read in one
sitting: the patterns and their best quotes, with the long lists of supporting ids kept
compact.

## Check before you finish

Run from `baby-development/`:
`python3 -I _tools/verify_part.py quotes evidence/who-she-is.md 0.05`
It must end in OK. Report: patterns per heading, quotes reproduced, ids cited, the list of
what the quotes cannot tell us, and anything you were unsure of.
