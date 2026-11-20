# Brief: digest of one share of one pattern's posts

You are digest reader **{NN}**. Working directory: `~/GitHub/_research`. Other readers work
on other shares at the same time. Write only the one file named under "Your output". No
network. Do not use git. Do not spawn other agents. Never modify any other file.

## Why

Niche `baby-development`: the development of a child from birth to 48 months. A random
sample of 20,000 Reddit posts was read; each on-niche post was tagged with one main
pattern. The posts in this share are almost all about children of 2 and 3 years; the
younger children were digested earlier, apart from these. Your share is posts of
**pattern {P}: {PNAME}**.
The pattern says what the posts are about. Your digest says what the forms inside it are:
the distinct situations, worries, wants and attempts, and how many posts show each.

Read first, in the root `README.md`, "Research never censors" and "Conventions". Read with
no product, brand or hypothesis in mind. Open nothing else in `baby-development/`.

## Your share

`{SHARE}`: posts of the pattern, each a `###` line (post id, subreddit, date, child's
stage, speaker), one line on what it is about, then its quotes with their ids. Two
sections: "On-niche posts (yes)" and "Near posts tied to development". Keep them apart.

## Task

1. Read **every** post in your share, whole.
2. Sort the **yes** posts into forms. A form is one plain claim about the parent, worded
   from their side (for example "She compares her child with another child the same age
   and asks if hers is late"). Let the forms come from the posts. 8 to 20 forms is usual.
   - Every yes post goes into exactly one form: the one it is mostly about. A post that
     fits none goes into the form "Other", with a few words on what it is.
   - Besides the forms, tag every yes post for four things, each `yes` or `no`: `tried`
     (says what they already did about it), `others` (says what other people told them or
     did), `bought` (names something bought or paid for), `feeling` (names how they feel).
3. Do the same for the **near** posts, as their own list of forms. Reuse a yes form's
   exact wording where a near post shows the same thing.

## Your output

`baby-development/evidence/2026-11/age-reread/digest-{NN}.md`, exactly this layout:

```
# Digest {NN}: pattern {P}, {PNAME}

Share: <file>. Yes posts: <n>. Near posts: <n>.

## Pattern {P}, share {NN}: yes posts

### <The form, as one plain claim>

<N> of <M> posts.

<Two to four sentences: what these posts say, the range inside the form, the ages. Only
what the posts say.>

- "<quote, word for word>" [<quote id>]
- "<quote, word for word>" [<quote id>]

**But:** <what in these posts cuts against the claim, with a quote and id; or "nothing found against it.">

Posts: <every post id of this form, separated by spaces>

## Pattern {P}, share {NN}: near posts

(same layout)

## Pattern {P}, share {NN}: across the yes posts

| Tag | Posts |
|---|---|
| tried | <n> of <M> |
| others | <n> of <M> |
| bought | <n> of <M> |
| feeling | <n> of <M> |

### What they tried, in their words
### What other people told them or did
### What they bought or paid for
### How they say they feel

(under each: 5 to 12 quotes, as bullets in the layout above, covering the range)
```

Rules:

- M is the number of yes posts (or near posts) in your share. The forms' counts sum to M.
- Give each form 3 to 8 quotes that show its range, most telling first. Quotes are copied
  from the share exactly, with the id that stands before them. Mark a cut with `[…]`.
- Choose quotes for what they say, never for or against their subject. Illness, distress,
  anger, regret and harm are recorded like anything else.
- "unknown" is a value: do not infer the speaker's sex, age, country or income.

## Check before you finish

- By a script of your own: every post id of your share is in exactly one "Posts:" line of
  its section; the counts match the "Posts:" lines and sum to M; every quoted passage
  (each part between `[…]`) is word for word in the share under the id given.
- Report: posts read, forms found, and anything you were unsure of.
