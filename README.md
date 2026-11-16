# _research

Raw research material only: scrapes, saved pages, transcripts, screenshots. It is kept so
it can be analysed again later with better tools. Findings do not live here; they are in
`~/GitHub/_home/library/avatars/<listener>/findings/`.

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

## Large files

Files over 50 MB are not committed (GitHub rejects files over 100 MB). The commit hook
blocks them. They are covered by the NAS backup.
After cloning, run: `git config core.hooksPath .githooks`
