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

## Findings

Research is not finished until its findings are filed. A findings page per topic goes in
`~/GitHub/_home/library/avatars/<listener>/findings/`, and the avatar lists it. Agents
read findings first and open raw material only when asked or when checking a quote.

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
