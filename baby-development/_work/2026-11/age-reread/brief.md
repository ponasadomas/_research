# Brief: read one share of a random sample, sort each post, cut the quotes

You are reader **{NN}**. Working directory: `~/GitHub/_research`. Other readers work on other
shares at the same time. Write only the three files named under "Your output". No network.
Do not use git. Do not spawn other agents. Never modify any other file.

## Why

This is a reading for the niche `baby-development`. Your share is part of a random sample of
every post with text in twelve parenting subreddits, April to October 2026. No keyword chose
them, so most posts are not about the niche. The purpose is to count how many posts show
each pattern and to keep what the parents say, word for word.

**Read with no product, brand or hypothesis in mind.** Read first, in the root `README.md`,
the sections "Research never censors" and "Conventions", and then
`baby-development/_work/2026-11/patterns/patterns.md` (thirteen numbered patterns, 0 to 12).
Open nothing else in `baby-development/` or the other niche folders.

## The niche

- **Subject:** The development of a child. The age range is not chosen yet.

A post belongs when it is about that: what a child does or does not do yet, how the child
behaves, plays and learns, and what is done with the child day to day. The child may be of
any age: record the age, do not judge by it. Who writes such posts and what their problems
are is not defined: that is what this reading finds.

## Your share

`{DIR}/reader-{NN}.tsv`: one row per post, with the path of its post file (the post and its
author's own replies in the thread).

## Task

Read every post file in your share, whole, one after another. Judge each post yourself from
its text; do not mark posts by keyword or by script. Every post gets one row.

For **every** post:

- `mark`:
  - `yes`: the post is about a child of any age (a son or daughter, not yet adult), and what
    it is mainly about is in the subject.
  - `near`: the post is about a child of any age, stated or not; **and** it says something
    about the child's development, abilities, behaviour, play or how the day is spent,
    although its main subject is something else. Give the reason in `border`. A post is
    never `near` or `no` because of the child's age.
  - `no`: everything else. That includes posts about pregnancy or about adults, and posts
    about a child that say nothing on those subjects (for example a post only about night
    waking, a rash, a pram, or the parents' relationship).
- `about`: what the post is about, 12 words of your own at most.

For **near** posts, `border` (one value): `sleep` (mainly about sleep), `feeding` (mainly
nutrition or feeding amounts), `parent_state` (mainly the parent's own exhaustion, mood,
work, relationship), `logistics` (equipment, travel, childcare arrangements), `other`.

For **yes** and **near** posts:

- `patterns`: the numbers of every pattern the post shows, separated by commas. Use `0` only
  when none fits, and then say what it is about in `other_what` (8 words at most).
- `main_pattern`: the one number the post is mostly about. Must be one of `patterns`.
- `ties_to_development`: `yes` if the author, in their own words, links the subject to the
  child's development, skills, milestones or a "regression" or "leap"; otherwise `no`.
- `speaker`: `new_mother`, `experienced_mother`, `parent_unspecified`, `partner`,
  `relative_caregiver`, `professional`, `other`. Use `parent_unspecified` unless the author
  says they are a mother.
- `stage`: the child's age as stated. `newborn_0_8_weeks`, `baby_2_4_months`,
  `baby_4_6_months`, `baby_6_9_months`, `baby_9_12_months`, `toddler_12_18_months`,
  `toddler_18_24_months`, `child_2_years`, `child_3_years`, `child_4_years`,
  `child_5_years`, `child_6_to_8_years`, `child_9_to_12_years`, `teen_13_to_17_years`,
  `looking_back`, `unknown` (age not stated). With several children, the one the post is
  mainly about.
- `wants`: what the author is asking for or wants, 15 words at most.
- `already_did`: what they say they already did or used about it, 15 words at most, or
  `nothing stated`.
- `paid`: `yes` if the author says they bought or paid for something for this (a product, a
  class, an app, a book, a professional); otherwise `no`. `paid_what`: what, 8 words at most.

**Quotes.** For every `yes` post, and every `near` post where `ties_to_development` is `yes`,
pull the quotes: every passage in which the author says, in their own words, what is
happening, what worries or pleases them, what they want, what they tried, what other people
told them, or what they bought or paid. Word for word. A long post gives several quotes; a
short one may give one. Take what is there, not what is expected.

Rules:

- State only what the author says. Do not infer the speaker's sex, age, country or income.
- Choose quotes for what they say, never for or against their subject. Illness, distress,
  anger, regret and harm are recorded like anything else.
- `themes` are your own short labels for what the quote is about (lowercase, underscores).
- Quote `type`: `trigger_moment`, `pain`, `fear`, `tried_failed`, `desire`, `belief`,
  `question`, `objection`, `advice_given`, `success_story`, `failure_story`, `regret`,
  `others_said`, `purchase`, `price_signal`.

## Your output

1. `{QUOTES}/reddit-{PREFIX}{NN}.jsonl`: one JSON object per line, per quote. Fields: `id`
   (`{PREFIX}{NN}-0001`, `{PREFIX}{NN}-0002`, ...), `post_id`, `source` (`reddit r/<sub>`),
   `url`, `date`, `speaker`, `stage`, `type`, `themes` (list), `quote`, `context` (25 words
   at most), `raw_file` (the post file path exactly as given in your share). Mark a cut
   inside a quote with ` […] `. No usernames.
2. `{DIR}/posts-{PREFIX}{NN}.tsv`: one row per post in your share, tab-separated, no tabs or
   line breaks inside a value, columns that do not apply left empty, header
   `post_id	mark	border	patterns	main_pattern	other_what	ties_to_development	about	speaker	stage	wants	already_did	paid	paid_what	quotes	note`
   (`quotes` is the number of quotes you pulled for the post; `note` is anything you were
   unsure of, 15 words at most).
3. `{DIR}/notes-{PREFIX}{NN}.md`: half a page: what came up again and again, what surprised
   you, what you were unsure how to mark. Counts of posts wherever you can.

## Check before you finish

- Every post in your share has exactly one row in the posts file, and no other post does.
- Confirm by a script of your own that every `quote` (each part between ` […] `) occurs word
  for word in its `raw_file`, that ids are unique, and that every record's `post_id` is in
  your share.
- Report: posts read, how many yes, near and no, quotes, and anything you were unsure of.
