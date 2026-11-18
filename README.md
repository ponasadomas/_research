# _research

Raw research material, and the rules for doing research. This file is the one place those
rules live; `AGENTS.md` and `CLAUDE.md` here are links to it, so agents working in this
repo load it automatically. `~/GitHub/_home/AGENTS.md` points here.

What is kept here: scrapes, saved pages, transcripts, screenshots, quote databases. It is
kept so it can be analysed again later with better tools.

## Research never censors

Research records what people actually say and do, in their own words, whatever the
subject. Nothing is dropped, withheld, softened or paraphrased away because it is
sensitive, unflattering, or might be unsuitable for an ad. A quote may be labelled, but it
is kept and quoted in full like any other.

What is used in copy is the owner's decision, made later, with everything in front of
him. It is never a research decision. If the owner wants the raw truth, that is his to
have. An agent that filters research "to be safe" has made the research wrong.

## Layout

```
_tools/                  scripts shared by every niche: draw a sample, build post files, check quotes and ids
<niche>/
├── README.md            overview: what exists per kind, the four questions, what is missing
├── brief.md             what this research set out to answer
├── ads/                 ads that are running (the swipe file)
├── books/
├── competitors/
├── forums/              parents' forums and communities other than Reddit
├── marketplaces/        marketplace listings and bestseller lists: what is for sale
├── official-guidance/   what the authorities she trusts say
├── reddit/
├── reviews/             of apps, books and courses
├── sales-letters/
├── statistics/          published figures about her
├── youtube/
├── quotes/              every quote pulled from the kinds above, one record each
├── evidence/            the quotes sorted under themes, counts, readers' notes
├── findings/            the short version of the evidence, one page per question
├── her-words.md         her phrases, word for word, for use in copy
├── _tools/              support: checks particular to this niche, and old rounds' scripts
└── _work/               support: reading ledgers, working files
```

- `<niche>` is the buyer and her problem (for example `baby-development`,
  `stop-divorce`), exactly as named in `~/GitHub/_home/library/niches.md`. Never a brand
  or a domain: those change.
- **One folder per kind of source**, so a person who needs the ads or the competitors
  opens that folder. Every kind folder always exists, even when empty, so it is plain
  what has not been collected yet. A new kind of source gets a new folder and a line here.
- **Inside a kind folder:** `README.md`, then the notes written about the material at the
  top, and the originals exactly as captured in `raw/`. Notes are what a person opens
  first. Originals are never edited.
- **A later round of research** goes into the same kind folder under a dated subfolder,
  `<yyyy>-<mm>/`.
- **What belongs here and what does not.** If it describes someone else (the buyer, a
  competitor, the market), it is research and lives here, including the scripts that
  collected it. If we made it (a site, a quiz, a design, a brand name), it lives with that
  product, in its repo's `_project/` folder when it is not code. A product repo has no
  `research` folder; its scripts that need research read it
  from this repo (`~/GitHub/_research`).
- **An underscore marks a folder that supports the others and is not one of them:**
  `_tools` and `_work` here, `_home` and `_research` among the project repos.

## READMEs

The niche README lists each kind: what was collected and from where, when, with which
tool or script, for which offer, the question it was meant to answer (see below), and
where its findings page is. A kind with nothing in it says "nothing collected yet". Each
kind folder's own README says the same for that kind in more detail.

## Four questions, each from a source that can answer it

A niche's research is complete when all four are answered. No source is required and
none is enough alone.

| Question | Sources that can answer it | Why |
|---|---|---|
| 1. Who is she, and what is her life like? | Our own data (quiz answers, buyers, email replies), ad platform audience data, the people who follow and comment on competitors, published surveys and statistics, communities | The other three questions are all about her. The avatar is written from this evidence, not imagined |
| 2. What hurts, what does she want, and how does she say it? | Reddit, forums, comment sections | Anonymous, long and unguarded. Includes the result she is really paying for |
| 3. What is she buying for this, what does she pay, and how did it go? | First: what she says she bought, bestseller lists and store charts, marketplaces. Then: reviews of what sells most | Only buyers know. Find where the money goes before choosing whose reviews to read |
| 4. Who is selling to her, and what is working? | Ads running now, competitor pages and funnels | An ad that runs for months is proof of money |

- **Question 3 has an order.** First map what she spends on: which kinds of thing (apps,
  books, courses, classes, a person), which products, what prices. Then read reviews of
  the ones that sell most: where they let her down and what delighted her. Reviews of
  products picked without the map may miss where the money is.
- Question 4 is the quick check (step 2 of `~/GitHub/_home/playbooks/new-niche.md`): it
  decides whether the niche is worth entering. The others are the deeper research.
- A community shows who posts there, not the market. Reddit is mostly American, younger
  and English-speaking, people post more when things are bad, and many who post never
  buy. Its counts never show how common a problem is.
- Sources close or change their access. Research that rests on one source ends when
  that source does.

## The chain: five steps, each made from the one before

| # | Name | What it is | Where | Length |
|---|---|---|---|---|
| 1 | Collected material | Posts, reviews and pages, saved as they were found | `<kind>/raw/` | everything |
| 2 | Quotes | The sentences worth keeping, cut out of that material, one record each with an id | `quotes/` | everything |
| 3 | Evidence file | All the quotes sorted into patterns and counted | `evidence/` | as long as it needs |
| 4 | Findings | The short version of an evidence file: each pattern with its count, its best quotes and what cuts against it. `her-words.md` is made alongside: her phrases, copied out for copy | `findings/`, `her-words.md` | short: a person reads a page in one sitting |
| 5 | Avatar | The centre of the findings, written as one person | `~/GitHub/_home/library/avatars/<niche>/avatar.md` | about a page |

Steps 1 to 4 are what they wrote, so they are research and live here. Step 5 is what we
made from it, so it lives in `_home`. Name each step for what it is.

Competitors have a shorter chain of their own, all here: saved pages in
`competitors/raw/`, one note per competitor, and `competitors/overview.md`. The overview is
already the short version, so it gets no findings page.

- Research is not finished until its findings are written and the owner has reviewed them.
  Agents read the findings first and open the steps before them only when asked or when
  checking a quote. Findings are written by the `write-findings` skill in `_home`.
- A quote may be left out of a findings page **because it repeats** what others already
  show. It is never left out **because of its subject**. Whatever is left out stays in
  the evidence file, cited by id.
- **Every niche's `evidence/` has a `jargon-glossary.md`:** the words she uses and how each
  one feels, with real usages. It answers "how does she say it" (question 2). Until it is
  made, `evidence/README.md` says "not made yet". The one that exists,
  `new-and-expecting-mothers/evidence/jargon-glossary.md`, covers mothers in general and is
  the starting point for a niche's own; its pipeline is `new-and-expecting-mothers/_tools/jargon/`.
- A brief for research work says which step it wants and who will read it. Asking for
  "the findings" without saying which produced a 940,000-word file in November 2026.

## Conventions

These came out of the November 2026 re-reading of five builds (41,000 posts). They cover
reading, quoting and merging. Conventions for the collecting step are still to be written.

**Records**

- A quote is one record with the same fields every time: id, source, link, date, speaker,
  stage, type, themes, and the quote word for word.
- Ids are unique across the niche and show who produced them: a prefix for the pass, the
  reader's number, a running number (`pbu07-0034`). Check for duplicates before each commit.
- Every post handed to a reader is accounted for in that reader's ledger: quoted,
  off-topic, or unavailable. Nothing is skipped silently.
- Raw material and finished quote files are never edited. New work is added as new files.

**Honesty about the evidence**

- Anything excluded is written down with the reason. Off-topic is a reason; subject is
  not (see "Research never censors").
- Count posts, not quotes: a pattern's count is the number of sampled posts that show it,
  and each post is tagged against one shared list of patterns. A post is not a person,
  but one eager poster cannot be counted ten times. Say how the posts were chosen. Only a
  random sample lets a count say how common something is among posts. The October 2026
  round counted quotes the readers chose; those counts show nothing about how common.
- Say what is still unread, and how much.
- An attempt that found little or nothing is recorded as that, with the reason, at the top
  of the kind folder's README. Saved pages and empty files are not research.
- When a script is turned away, do not stop there: follow
  `~/GitHub/_home/playbooks/collect-through-a-browser.md`.
- Keep and label provenance: commercial, fictional, second-hand or AI-written passages
  are marked, not removed.
- When a conclusion changes, record it with the date: what it said, what it says now,
  and the quote ids behind the change.

**Doing the work with agents**

- Split the reading: about 300 posts per reader.
- Merge in two steps: theme digests of about 1,200 quotes each, then one agent merges
  the digests. One agent given several thousand quotes directly used about a tenth.
- Agents write files; the supervisor checks and commits, one commit per batch. Every
  reproduced quote is compared with its source by a script before the commit.
- A piece that fails the check is redone whole, once. If it fails again, stop and have
  a person look.
- The brief fixes one layout for quotes in written files, so the checking script can
  read every agent's output.
- The scripts for sampling and checking live once, in `_tools/` at the top of this repo.
  A niche's own `_tools/` holds only checks particular to it.
- Working figures (Codex, `gpt-6.1-sol`, xhigh): five agents at a time, 25 to 30 minutes
  per batch, about 2 to 2.5 percent of weekly usage per 1,000 posts.

## Material that fits several niches

File it once, under the niche it was collected for. The other niches' avatars get a
pointer line under "Also relevant research".

## Size

This repo is meant to be large. Videos, screenshots, saved sites and whole corpora belong
here when they were part of the research. Do not leave material out to save space.

The one hard limit is GitHub's: it rejects any single file over 100 MB. The commit hook
stops files over 95 MB. Split such a file into parts (as the Reddit archives here already
are), or keep it on disk and on the NAS backup and say so in the niche README.
After cloning, run: `git config core.hooksPath .githooks`
