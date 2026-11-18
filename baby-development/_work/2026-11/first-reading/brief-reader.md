# Brief: first reading, one share of a random sample of posts

You are reader **{NN}** of 5. Working directory: `~/GitHub/_research`. Four other readers
work on the other shares at the same time. Write only the three files named under "Your
output". No network. Do not use git. Do not spawn other agents. Never modify any other file.

## Why

This is the first reading for the niche `baby-development`. The sample is 1,500 posts drawn
at random from every post with text in twelve parenting subreddits, April to October 2026.
No keyword chose them. Its purpose is to find out what share of what parents write is about
this niche, what they write when it is, and which words they use for it.

**Read with no product, brand or hypothesis in mind.** Read first, in the root `README.md`,
the sections "Research never censors" and "Conventions". Open nothing else in
`baby-development/` or the other niche folders: older files carry an earlier framing and
would steer what you notice.

## The niche, as a starting description

Mothers of babies from birth to 24 months who want to know what to do with the baby at this
age and whether the baby is on track: what the child can or cannot do yet, whether that is
all right, how to spend the day with the child, play, movement, speech, and how she feels
about all of it.

This description is ours and may be wrong at the edges. So every post gets one of three marks:

- **yes**: the author cares for a child of 0 to 24 months and the post is about the above.
- **near**: the author cares for a child of 0 to 24 months and the post touches the above
  without being about it, or you cannot tell whether it belongs. When unsure between yes
  and near, choose near and say why.
- **no**: everything else. Most posts will be "no"; marking them is part of the result.

## Your share

`baby-development/_work/2026-11/first-reading/reader-{NN}.tsv`: one row per post, with the
path of its post file (the post and its author's own replies in the thread).

## Task

1. Read **every** post file in your share, whole. Do not sample and do not skim long ones.
2. Give every post one row in your posts file, whatever its mark.
   - For **every** post: `about`, in 12 words of your own at most (for example "toddler
     bedtime fights", "husband does not help at night", "is this rash normal").
   - For **yes** and **near** posts also: who is speaking and the child's age as stated;
     what the author is asking for or wants; what they say they already did, used or paid
     for about it (or "nothing stated"); and `her_words`: the words and short phrases, copied
     exactly, with which the author names the thing the post is about (for example
     "tummy time", "behind", "not crawling yet"), separated by ` | `.
3. For each **yes** and **near** post, pull its quotes: every passage in which the author
   says, in their own words, what is happening, what worries or pleases them, what they
   want, what they tried, what other people told them, or what they bought or paid. Word for
   word. A long post gives several quotes; a short one may give one. Take what is there, not
   what is expected.
4. Rules:
   - State only what the author says. "unknown" is a value: do not infer the speaker's sex,
     age, country or income.
   - Choose quotes for what they say, never for or against their subject. Illness, distress,
     anger, regret and harm are recorded like anything else.
   - `themes` are your own short labels for what the quote is about (lowercase,
     underscores). Reuse a label when the subject is the same.

## Allowed values

- `speaker`: `new_mother`, `experienced_mother`, `parent_unspecified`, `partner`,
  `relative_caregiver`, `professional`, `other`. Use `parent_unspecified` unless the author
  says they are a mother.
- `stage`: `newborn_0_8_weeks`, `baby_2_4_months`, `baby_4_6_months`, `baby_6_9_months`,
  `baby_9_12_months`, `toddler_12_18_months`, `toddler_18_24_months`, `looking_back`, `unknown`.
- `type`: `trigger_moment`, `pain`, `fear`, `tried_failed`, `desire`, `belief`, `question`,
  `objection`, `advice_given`, `success_story`, `failure_story`, `regret`, `others_said`,
  `purchase` (the author says they bought or paid for something), `price_signal` (what
  they say it was worth).

## Your output

1. `baby-development/quotes/reddit-fr{NN}.jsonl`: one JSON object per line, per quote.
   Fields: `id` (`fr{NN}-0001`, `fr{NN}-0002`, ...), `post_id`, `source` (`reddit r/<sub>`),
   `url`, `date`, `speaker`, `stage`, `type`, `themes` (list), `quote`, `context` (25 words
   at most), `raw_file` (the post file path exactly as given in your share). Mark a cut
   inside a quote with ` […] `. No usernames.
2. `baby-development/_work/2026-11/first-reading/posts-fr{NN}.tsv`: one row per post in
   your share, tab-separated, no tabs or line breaks inside a value, header
   `post_id	mark	about	speaker	stage	wants	already_did_or_paid	her_words	quotes	unsure_why`
   (`mark` is `yes`, `near` or `no`; `quotes` is the number of quotes you pulled; leave the
   columns that do not apply empty).
3. `baby-development/_work/2026-11/first-reading/notes-fr{NN}.md`: one page on what you
   noticed: what came up again and again among the yes and near posts, what the "no" posts
   were mostly about, what surprised you, what you were unsure how to mark. Counts of
   posts, not impressions, wherever you can.

## Check before you finish

- Every post in your share has exactly one row in the posts file, and no other post does.
- Confirm by a script of your own that every `quote` (each part between ` […] `) occurs
  word for word in its `raw_file`, that ids are unique, and that every record's `post_id`
  is in your share and marked yes or near.
- Report: posts read, how many yes, near and no, quotes, and anything you were unsure of.
