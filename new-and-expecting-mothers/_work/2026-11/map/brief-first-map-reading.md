# Brief: first map reading, one share of a random sample of a crowd

You are reader **{NN}**. Working directory: `~/GitHub/_research`. Other readers work on other
shares at the same time. Write only the two files named under "Your output". No network.
Do not use git. Do not spawn other agents. Never modify any other file.

## Why

A crowd has been collected whole: every post of 22 subreddits, 1 April to 24 October 2026.
Your share is part of a random sample of it. No keyword chose the posts and no subject is
being looked for. The purpose is a map: what this crowd writes about, in which situations,
and what the writers want, try and pay for.

**There is no niche, no subject and no kind of writer in mind. Do not look for one.** Every
post is described; none is marked as belonging or not belonging to anything. Read first, in
the root `README.md`, the sections "Research never censors" and "Conventions". Open nothing
in the niche folders.

## Your share

`{DIR}/reader-{NN}.tsv`: one row per post, with the path of its post file (the post and its
author's own replies in the thread).

## Task

Read every post file in your share, whole, one after another. Judge each post from its
text; do not describe posts by keyword or by script. Every post gets one row.

- `about`: what the post is about, 12 words of your own at most.
- `subject`: the area of life the post belongs to, as a label of 2 to 4 words of your own
  (lowercase). Reuse a label when the area is the same. Do not make labels fit any list.
- `does`: what the post does. One of: `asks` (asks what to do or whether something is all
  right), `tells` (tells what happened, with no question), `vents`, `shares_joy`,
  `advises` (gives advice or information unasked), `offers` (sells, promotes or recruits),
  `other`.
- `writer`: who is writing, only as they say it themselves, in their words shortened (for
  example "first time mom", "dad of two", "grandmother"). `not stated` if they do not say.
- `about_whom`: whom the post is about, only as stated (for example "my son", "myself",
  "my husband", "my mother in law"). `not stated` if unclear.
- `facts`: the facts of the situation that the writer states, each as `name: value`,
  separated by ` | `, 6 at most, the most specific first. Take whatever the writer gives:
  an age, a length of time, a number, a place, a diagnosis, a job, a family make-up. Name
  each fact in plain words of your own (for example `child's age: 14 months`). Do not
  infer a fact that is not stated. `none` if the post states none.
- `wants`: what the writer asks for or wants, 15 words at most; `nothing stated`.
- `tried`: what they say they already did or used about it, 15 words at most;
  `nothing stated`.
- `paid`: `yes` if the writer says they bought or paid for something to do with the post's
  subject; otherwise `no`. `paid_what`: what, 8 words at most.
- `note`: anything you were unsure of, 15 words at most.

Rules:

- State only what the writer says. Do not infer sex, age, country or income.
- Every subject is described like any other. Illness, distress, anger, regret and harm are
  recorded as they are.

## Your output

1. `{DIR}/posts-{PREFIX}{NN}.tsv`: one row per post in your share, tab-separated, no tabs or
   line breaks inside a value, header
   `post_id	about	subject	does	writer	about_whom	facts	wants	tried	paid	paid_what	note`
2. `{DIR}/notes-{PREFIX}{NN}.md`: half a page: which subjects came up most, which facts the
   writers state again and again, what surprised you, what was hard to describe. Counts of
   posts wherever you can.

## Check before you finish

- Every post in your share has exactly one row in the posts file, and no other post does.
- Report: posts read, your ten most frequent subject labels with counts, the five facts
  stated most often with counts.
