# Brief: findings section for one pattern

You are section writer for **pattern {P}: {PNAME}**. Working directory: `~/GitHub/_research`.
Other writers work on other patterns at the same time. Write only the one file named under
"Your output". No network. Do not use git. Do not spawn other agents. Never modify any
other file.

## Why

Niche `baby-development`. A random sample of 20,000 Reddit posts (twelve parenting
subreddits, 1 April to 24 October 2026, no keyword) was read; 2,471 were on the niche and
each got one main pattern. Digest readers then sorted each pattern's posts into forms.
A pattern with many posts was dealt over two or three digest readers, who named their
forms independently. You merge this pattern's digests into one short findings section
that the owner can read in a few minutes.

Read first, in the root `README.md`, "Research never censors" and "Conventions".

## Your input

The digests of this pattern, read each whole: {DIGESTS}

Totals for this pattern: **{YES} on-niche (yes) posts, {NEAR} near posts.**

## Task

1. Merge the yes forms. Forms from different digests that say the same thing become one
   finding, and their counts are added. A form that stands alone stays a finding, however
   few posts it has. Every yes form of every digest goes into exactly one finding, whole:
   never split a form's count. The findings' counts sum to {YES}.
2. Do the same for the near forms, apart from the yes forms. Their counts sum to {NEAR}.
3. Add up the four tags (tried, others, bought, feeling) over the digests and write the
   four cross findings from the digests' quote lists.
4. Word each finding as one plain claim about the parent, from their side, readable alone.
   Order findings by count, highest first; "Other" last.
5. Each finding: the count line, one to three sentences, two or three quotes that show its
   range, and what cuts against it. Copy quotes and ids exactly from the digests.
   Choose quotes for what they say, never for or against their subject.

## Your output

`baby-development/findings/2026-11/patterns/pattern-{PP}.md`, exactly this layout:

```
# baby-development: pattern {P}, {PNAME}

**Written:** 2026-11-20 from {DIGESTS}
**Reviewed by the owner:** not yet

## Limits

<Two or three sentences: where the posts come from, how they were chosen, how many are in
this pattern, that each count is a number of posts tagged by one reader, and that forms
from different digest readers were merged by judgement.>

## On-niche posts

### <The finding, as one plain claim>

<N> of {YES} posts.

<One to three sentences.>

- "<quote, word for word>" [<id>]
- "<quote, word for word>" [<id>]

**But:** <what cuts against it, with a quote and id; or "nothing found against it.">

## Near posts

### <finding>

<N> of {NEAR} posts.

(same layout)

## Across the on-niche posts

### <What they already tried, as one claim>

<n> of {YES} posts.

(same layout; then the same for what other people told them or did, what they bought or
paid for, and how they say they feel: four findings)

## Coverage

<details>
<summary>Every heading of the digests, and where it went</summary>

| Digest heading | Went to |
|---|---|
| <heading text, exactly as in the digest> | <the finding's claim> |

</details>
```

Rules:

- The Coverage table has one row for every `##` and `###` heading of every digest, with
  the heading text copied exactly. A heading that is a section title and not a form goes to
  "section title".
- Keep the page short: 2,500 words at most above "## Coverage".
- Quotes are bullets: a straight double quote, the words exactly, a straight double quote,
  a space, the id in square brackets. Mark a cut with `[…]`.
- A quote stays on one line with its id. Where a digest's quote runs over several lines,
  join the lines with a space.
- State only what the digests say. "unknown" is a value.

## Check before you finish

Run both; each must print OK:

```
python3 -I ~/GitHub/_home/.agents/skills/write-findings/check_findings.py baby-development/findings/2026-11/patterns/pattern-{PP}.md --quotes baby-development/quotes {EVARGS}
python3 -I _tools/verify_section.py baby-development/findings/2026-11/patterns/pattern-{PP}.md {YES} {NEAR}
```

Report: findings written, and anything you were unsure of when merging.
