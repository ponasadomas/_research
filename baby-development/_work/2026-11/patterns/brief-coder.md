# Brief: sort posts under a list of patterns

You are coder **{NN}** of 3. Working directory: `~/GitHub/_research`. Write only the one
file named under "Your output". No network. Do not use git. Do not spawn other agents.

## Why

A first reading of 1,500 random posts from parenting subreddits found 524 that are on or
near the niche `baby-development`. They now need to be sorted the same way by everyone, so
that posts can be counted per pattern. Read with no product, brand or hypothesis in mind.
Open nothing in `baby-development/` except the three files this brief names.

## The niche

Parents of babies from birth to 24 months, writing about the child's development and their
days together: what the child can or cannot do yet, whether that is all right, behaviour,
play, how to spend the day, and how the parent feels about all of it.

## Read first

`baby-development/_work/2026-11/patterns/patterns.md`: thirteen numbered patterns (0 to 12).

## Your share

`baby-development/_work/2026-11/patterns/coder-{NN}.tsv`: one row per post with the path of
its post file (the post and its author's own replies).

## Task

Read every post file in your share, whole, one after another. Judge each post yourself from
its text; do not mark posts by keyword or by script. For each post fill one row:

- `mark`:
  - `yes`: the author cares for a child of 0 to 24 months, and what the post is mainly about
    is in the niche.
  - `near`: anything else that still touches the niche. Give the reason in `border`.
  - `no`: does not touch the niche at all.
- `border` (for `near` only, one value): `sleep` (mainly about sleep), `feeding` (mainly about
  nutrition or feeding amounts), `parent_state` (mainly about the parent's own exhaustion,
  mood, work, relationship), `age_unknown` (child's age not stated), `age_over_24` (child is
  or may be older than 24 months; "two years old" with no months counts here), `logistics`
  (equipment, travel, childcare arrangements), `other`.
- `patterns`: the numbers of every pattern the post shows, separated by commas, for `yes` and
  `near` posts. Use `0` only when none fits, and then say what it is about in `other_what`
  (8 words at most). Leave empty for `no`.
- `main_pattern`: the one number the post is mostly about. Must be one of `patterns`.
- `ties_to_development`: `yes` if the author, in their own words, links the subject to the
  child's development, skills, milestones or a "regression" or "leap"; otherwise `no`.
- `paid`: `yes` if the author says they bought or paid for something for this (a product, a
  class, an app, a book, a professional); otherwise `no`. `paid_what`: what, 8 words at most.
- `note`: anything you were unsure of, 15 words at most; otherwise empty.

State only what the author says. Do not infer sex, age, country or income.

## Your output

`baby-development/_work/2026-11/patterns/coded-pc{NN}.tsv`: tab-separated, no tabs or line
breaks inside a value, one row per post in your share, header
`post_id	mark	border	patterns	main_pattern	other_what	ties_to_development	paid	paid_what	note`

## Check before you finish

Every post in your share has exactly one row and no other post does; every value is one of
the allowed ones. Report: posts read, how many yes, near and no, and what you were unsure of.
