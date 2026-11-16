# _research

Raw research material only: scrapes, saved pages, transcripts, screenshots. It is kept so
it can be analysed again later with better tools. Findings do not live here; they are in
`~/GitHub/_home/library/avatars/<listener>/findings/`.

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
blocks them and `.gitignore` lists the usual types. They are covered by the NAS backup.
After cloning, run: `git config core.hooksPath .githooks`
