# Brief: read one share of a random sample of posts

You are reader **{NN}** of 2. Working directory: the `_research` repo, niche
`baby-development/`. The other reader works on the other share at the same time. Write
only the three files named under "Your output". No network. Do not use git. Never modify
anything under `quotes/` (other than your own new file), any `raw/` folder or `evidence/`.

## Why

Earlier readings of this niche chose their posts by filters, so their counts cannot show
what is common. This reading is of 600 posts drawn at random from every post that a broad
keyword filter matched to this niche, April to October 2026. Its purpose is to record what
these parents actually write about, in their words, and in what proportion.

**Read with no product, brand or hypothesis in mind.** Do not open `brief.md`,
`evidence/`, `findings/`, `competitors/` or the older quote files: they carry an earlier
framing and would steer what you notice. Read first: the root `README.md` sections
"Research never censors" and "Conventions", and the "Quote schema" and "Vocabulary"
paragraphs of `baby-development/README.md`.

## The niche

Parents of babies and toddlers from birth to 24 months, writing about the child's
development and their days together: what the child can or cannot do yet, whether that is
all right, what to do with the child, play, movement, speech, and how the parent feels
about it. A post is **on topic** when its author is such a parent (or someone caring for
such a child) and the post is about any of that. Everything else is **off topic**: other
ages, pregnancy, sleep or feeding alone, sales posts, and so on. The keyword filter was
broad, so expect many off-topic posts; marking them is part of the result.

## Your share

`baby-development/_work/reddit-selection/random-2026-11/reader-{NN}.tsv`: one row per
post, with the path of its unit file (the post plus its author's own replies).

## Task

1. Read **every** unit in your share, whole. Do not sample and do not skim long ones.
2. Give every post one line in your ledger (see "Your output"), on topic or not.
3. For each on-topic post, fill the post record and pull its quotes.
   - **Post record:** who is speaking and the child's age, as stated; then, in plain words
     of your own (15 words at most each): what the post is mainly about, what the author
     is asking for or wants, and what they say they already did, used or paid for about
     it (or "nothing stated").
   - **Quotes:** every passage in which the author says, in their own words, what is
     happening, what worries or pleases them, what they want, what they tried, what other
     people told them, or what they bought or paid. Word for word. A long post gives
     several quotes; a short one may give one. Take what is there, not what is expected.
4. Rules:
   - State only what the author says. "Unknown" is a value: do not infer the speaker's
     sex, age, country or income.
   - Choose quotes for what they say, never for or against their subject. Illness,
     distress, anger, regret and harm are recorded like anything else.
   - Themes are your own short labels for what the quote is about (lowercase, underscores).
     Reuse a label when the subject is the same.

## Your output

1. `baby-development/quotes/reddit-rs{NN}.jsonl`: one JSON object per line, per quote.
   Fields: `id` (`rs{NN}-0001`, `rs{NN}-0002`, ...), `post_id`, `source` (`reddit r/<sub>`),
   `url`, `date`, `speaker`, `stage`, `type` (values from the README vocabulary),
   `themes` (list), `quote`, `context` (25 words at most), `raw_file` (the unit path as
   given in your share, relative to `baby-development/`). Mark a cut inside a quote with ` […] `.
2. `baby-development/_work/reddit-selection/random-2026-11/posts-rs{NN}.tsv`: one row per
   post in your share, tab-separated, header
   `post_id	on_topic	off_topic_reason	speaker	stage	about	wants	already_did_or_paid	quotes`
   (`on_topic` is `yes` or `no`; `quotes` is the number of quotes you pulled).
3. `baby-development/_work/reading-ledgers/reddit-reading-rs{NN}.md`: what you noticed
   while reading, in a page: what came up again and again, what surprised you, what you
   were unsure how to classify. Counts of posts, not impressions, wherever you can.

## Check before you finish

- Every post in your share has exactly one row in the posts file.
- Confirm by a script of your own that every `quote` (each part between ` […] `) occurs
  word for word in its `raw_file`, that ids are unique, and that every record's `post_id`
  is in your share.
- Report: posts read, on topic, off topic (by reason), quotes, and anything you were unsure of.
