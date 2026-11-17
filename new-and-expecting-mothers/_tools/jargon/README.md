# reddit-jargon

Mines the distinctive vocabulary of mother communities (6 subreddits + Mumsnet) so Vitaful
copy can sound native. Output: `../../evidence/jargon-glossary.md`.

**Where things are (moved here 2026-11-17 from the mamiVio site repo):**

- saved Reddit responses: `../../reddit/raw/jargon-2026-07/` (1,480 files)
- saved Mumsnet pages: `../../forums/raw/mumsnet-jargon-2026-07/` (746 files)
- working output: `../../_work/jargon/out/` (scored terms, examples, the draft, the curation chunks)
- `../../_work/jargon/corpus/` is rebuilt by `npm run corpus` in about four minutes and is not stored in git

Below, "`data/cache/`" means the two saved-response folders and "`data/out/`" means
`_work/jargon/out/`. The paths are set in `config.mjs` (`dataDir`, `cacheDirs`).

## Run it

```sh
npm install
npm run fetch:reddit     # ~40 min, Arctic Shift API (bulk Reddit archive)
npm run fetch:mumsnet    # ~2.5 h, deliberately slow/polite HTML scrape
npm run pipeline         # seconds: corpus -> analyze -> examples -> glossary -> verify
```

Every HTTP response is cached under `data/cache/`, so re-running a fetch costs nothing and an
interrupted fetch resumes where it stopped. `pipeline` never touches the network — iterate on
tokenization/scoring freely by editing `config.mjs` and re-running it.

Smoke run before committing to a full fetch:
`node fetch-reddit.mjs --subs=Mommit,CasualConversation --windows=4 && npm run pipeline`

## How it works

Distinctiveness, not raw frequency: terms are scored against a general-Reddit baseline
(r/CasualConversation, r/AskReddit) with log-odds ratio + informative Dirichlet prior
(Monroe, Colaresi & Quinn 2008, "Fightin' Words"), separately for unigrams, bigrams, and
case-preserved acronyms, then merged by z-score. A second log-odds pass compares UK sources
(Mumsnet, r/UKParenting) against US-leaning ones to tag region.

Reddit data comes from the Arctic Shift API — reddit.com's own `.json` endpoints 403 this
network, and Arctic Shift serves bulk posts/comments per date window instead of one request
per thread. It has no server-side score sort, so we sample whole weekly windows and rank locally.

The glossary is `../../evidence/jargon-glossary.md`; the terms it was cut from are
`../../evidence/jargon-terms.csv`. Rerunning the pipeline on 2026-11-17 from this folder reproduced
`terms.csv`, `terms.json` and `examples.json` byte for byte.

## Curation step

`generate-glossary.mjs` emits `data/out/glossary-draft.md` with `TODO` placeholders for meaning
and tone plus real quotes. A script can't judge whether "crunchy" is affectionate or barbed —
a human (or an LLM reading `examples.json`) fills those in, prunes non-jargon, and groups terms
into themes to produce the committed glossary.
