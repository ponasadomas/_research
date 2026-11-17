# Brief: who is she? Read one share of the baby-development quotes

You are reader **{NN}** of 3. Working directory: the `_research` repo.
Niche: `baby-development/` (mothers of babies 0 to 24 months who want to know what to do
with the baby at this age and whether the baby is on track). Other readers work on other
shares at the same time. Write only the one file named under "Your output". No network.
Do not use git. Never modify anything under `quotes/`, any `raw/` folder or `evidence/`.

## Why

Research here answers four questions (`README.md` in the repo root, "Four questions").
This niche has 2,970 quotes that were collected for question 2, what hurts. Nobody has
read them for **question 1: who is she, and what is her life like?** People describe
themselves when they post, so the answer is scattered through the quotes. You collect it
from your share. A final agent merges the three shares, and the avatar (the portrait of
the buyer) is then written from that evidence instead of being imagined.

## Your share ({COUNT} quotes)

{FILES}

## Task

1. Read `baby-development/README.md` (the niche, the quote fields, the vocabulary) and the
   root `README.md` sections "Research never censors", "Four questions" and "Conventions".
2. Read **every** record in your share: the `quote`, its `context`, `speaker`, `stage`,
   `themes` and `source`. Do not sample. When a quote hints at her situation but cuts off,
   open the post it came from (`raw_file`, relative to `baby-development/`) and read the
   rest; you may reproduce words from the stored `quote` only.
3. Collect what the quotes say about who she is, under these headings. Add a heading when
   something does not fit.
   - **Her situation:** first child or not; her age where she states it; working, on
     leave or at home, and when she goes back; partner, alone, or other adults in the
     house; country or health system where it shows; money where she mentions it.
   - **Her day:** what the day with the baby looks like; when she has time and when she
     does not; when she searches, reads or posts; sleep and tiredness as they shape the day.
   - **Who else has a say:** partner, her mother and in-laws, the doctor or health
     visitor, daycare, friends and other mothers, people online. What each says to her and
     how she takes it.
   - **What she already follows and believes:** the accounts, apps, books, methods and
     rules she names; what she takes for granted about babies and about a good mother.
   - **What she has already tried or bought** for this, in her own account of it.
   - **How she sees herself:** what she calls herself, what she is proud of, what she
     feels guilty or ashamed about, who she compares herself with.
   - **Who is speaking who is not her:** partners, grandparents, reviewers. What differs.
4. For each pattern under a heading write:
   - one plain line stating the pattern;
   - the quotes behind it, word for word, with ids. Quote every strong or distinctive one;
     list further supporting ids after them;
   - how many quotes in your share show it;
   - the quotes that cut against it.
5. Rules for this reading:
   - State only what people say about themselves. Do not infer age, income, education or
     anything else she did not say. "Unknown" is a finding: say how many quotes give no
     sign of something (for example, how many say nothing about work).
   - Counts are counts of quotes, never of people, and never how common something is.
     These are people who post on Reddit or review an app; say so once at the top.
   - Leave nothing out, and soften nothing, because of its subject.
6. **Layout for quotes, exactly:** the id in square brackets on its own line, then the
   quote as a blockquote (each line starting with a greater-than sign and a space) on the
   following lines. No other layout, no code fences. Example:

   [dv03-0073]
   > the quote, word for word

## Your output

`baby-development/_work/who-she-is/part-{NN}.md`

End it with a coverage line: quotes in the share, quotes reproduced, further ids listed,
and how many quotes said nothing about who she is.

## Check before you finish

Confirm programmatically that every quote you reproduce is word for word from the `quote`
field of the record with that id, and that every id you mention is in your share.
