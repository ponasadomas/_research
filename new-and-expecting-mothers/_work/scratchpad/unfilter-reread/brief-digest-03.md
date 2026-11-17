# Brief: digest one share of the re-read quotes for the global research set

You are digest agent **03** of 4. Working directory: the `ads` repo.
Build: `mamivio.com/research/global/`. Other agents work on other shares at the same time.
Write only the one file named under "Your output". No network. Do not use git.

## Background

The owner's ruling (2026-11-16): research never filters or censors. An earlier rule kept
thousands of posts out of this build because of their subject. Readers have now read them
and extracted verified quotes. There are too many for one agent to weigh, so the new quotes
are split into 4 shares. You digest one share. A final agent will then rewrite
`synthesis/findings.md` and the evidence file from all the digests.

## Your share (1124 quotes)

- `voice/reddit-ur09.jsonl` (356 quotes) and its ledger `sources/reddit-reading-ur09.md`
- `voice/reddit-ur12.jsonl` (368 quotes) and its ledger `sources/reddit-reading-ur12.md`
- `voice/reddit-ur13.jsonl` (400 quotes) and its ledger `sources/reddit-reading-ur13.md`

## Task

1. Read `global/README.md`, `synthesis/findings.md` and `synthesis/niche-opportunities.md`,
   so you know what the set is for, the current sections and the current conclusions.
2. Read **every** quote in your share, and each ledger's "What these posts add" section.
   Do not sample. If you work in passes, make sure no file and no part of a file is skipped.
3. Write the digest. For each pattern you find:
   - a plain one-line statement of the pattern;
   - the quotes behind it, verbatim with their ids. Quote generously: every strong or
     distinctive quote, not one example. List further supporting ids after them;
   - which section of the current findings it belongs in;
   - whether it **confirms**, **extends** or **contradicts** a current conclusion. Where it
     extends or contradicts, quote the current conclusion and say what should change.
   Then:
   - **Outliers and counter-examples**: quotes that cut against the main patterns.
   - **What fits nowhere**: material the current findings have no section for.
   - **Money**: every price, purchase, refund, cost or willingness to pay, each with its id.
   - **Requests**: every place a parent asks outright for a product, plan, list or service.
4. Soften, omit or paraphrase nothing because of its subject. Describe what parents say as
   they say it. Counts are counts of quotes, never of people; these posts were chosen
   because they had been excluded, so they are not a sample of prevalence.
5. **Layout for quotes, exactly:** the id in square brackets on its own line, then the quote
   as a `> ` blockquote on the following lines. No other layout, no code fences.

   ```
   [glu03-0042]
   > the quote, word for word
   ```

## Your output

`mamivio.com/research/global/synthesis/unfilter-digest-03.md`

End it with a coverage line: quotes in the share, quotes reproduced verbatim, further ids
listed, ids not mentioned at all (aim for none; if any, say why).

## Check before you finish

Confirm programmatically that every quote you reproduce is verbatim from the `quote` field
of the record with that id, and that every id you mention exists in your share.
