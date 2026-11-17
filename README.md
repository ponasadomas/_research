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
<listener>/<topic>-<yyyy>-<mm>/
├── README.md    required
└── ...          the raw files, in whatever layout they were collected in
```

- `<listener>` is the buyer and her problem, exactly as named in
  `~/GitHub/_home/library/avatars/` (for example `new-mother`, `stop-divorce`). Never a
  brand or a domain: those change.
- `<topic>` is the thing collected: a competitor, a product, a community.
- `<yyyy>-<mm>` is when it was collected.

## Every topic README says

1. What was collected, and from where.
2. When, and with which tool or script.
3. Which listener and which offer it was collected for.
4. The question it was meant to answer.
5. Where its findings page is.

## Three layers

Every topic that collects what people say has three layers. Name each for what it is.

| Layer | What it is | Where | Length |
|---|---|---|---|
| Quotes | Every quote as one record, with its source | the topic folder here | everything |
| Evidence file | The quotes sorted under themes, with what they show | the topic folder here | as long as it needs |
| Findings page | The conclusions, each with its strongest few quotes | `~/GitHub/_home/library/avatars/<listener>/findings/` | short: a person reads it in one sitting |

- Research is not finished until its findings page is filed and the avatar lists it.
  Agents read the findings page first and open the layers below only when asked or when
  checking a quote.
- A quote may be left out of a findings page **because it repeats** what others already
  show. It is never left out **because of its subject**. Whatever is left out stays in
  the evidence file, cited by id.
- A brief for research work says which layer it wants and who will read it. Asking for
  "the findings" without saying which produced a 940,000-word file in November 2026.

## Conventions

These came out of the November 2026 re-reading of five builds (41,000 posts). They cover
reading, quoting and merging. Conventions for the collecting step are still to be written.

**Records**

- A quote is one record with the same fields every time: id, source, link, date, speaker,
  stage, type, themes, and the quote word for word.
- Ids are unique across the topic and show who produced them: a prefix for the pass, the
  reader's number, a running number (`pbu07-0034`). Check for duplicates before each commit.
- Every post handed to a reader is accounted for in that reader's ledger: quoted,
  off-topic, or unavailable. Nothing is skipped silently.
- Raw material and finished quote files are never edited. New work is added as new files.

**Honesty about the evidence**

- Anything excluded is written down with the reason. Off-topic is a reason; subject is
  not (see "Research never censors").
- Counts are counts of quotes, never of people. Say how the posts were chosen, so the
  counts are not read as how common something is.
- Say what is still unread, and how much.
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
- The checking scripts live inside the topic folder, so the topic can be verified again
  after it is moved.
- Working figures (Codex, `gpt-6.1-sol`, xhigh): five agents at a time, 25 to 30 minutes
  per batch, about 2 to 2.5 percent of weekly usage per 1,000 posts.

## Material that fits several listeners

File it once, under the listener it was collected for. The other listeners' avatars get a
pointer line under "Also relevant research".

## Size

This repo is meant to be large. Videos, screenshots, saved sites and whole corpora belong
here when they were part of the research. Do not leave material out to save space.

The one hard limit is GitHub's: it rejects any single file over 100 MB. The commit hook
stops files over 95 MB. Split such a file into parts (as the Reddit archives here already
are), or keep it on disk and on the NAS backup and say so in the topic README.
After cloning, run: `git config core.hooksPath .githooks`
