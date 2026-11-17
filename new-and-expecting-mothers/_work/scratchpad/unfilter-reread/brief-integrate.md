# Brief: fold the re-read quotes into the global research set

Working directory: the `ads` repo, branch `research-unfilter`.
Research set: `mamivio.com/research/global/`, and the niche map in `mamivio.com/research/main/`.
No network. Do not use git. Never modify anything under `_raw/`, any `voice/*.jsonl`,
any `sources/reddit-reading-*.md` or any `synthesis/unfilter-digest-*.md`.

## Background

The owner's ruling (2026-11-16): research never filters or censors. Earlier rules kept
3807 posts and threads, or passages in them, out of this set because of their subject.
13 readers have now read them and written 4829 verified quotes
(`voice/reddit-ur*.jsonl`, ids start `glu`; ledgers `sources/reddit-reading-ur*.md`).
Digest agents then wrote `synthesis/unfilter-digest-NN.md`: the patterns in each share, the
quotes behind them, and whether each confirms, extends or contradicts a current conclusion.
Read `~/GitHub/_research/README.md`, sections "Three layers" and "Conventions", first.

## Task: three layers, kept apart

1. Read `synthesis/findings.md`, `synthesis/niche-opportunities.md`,
   `synthesis/purchase-evidence.md`, `synthesis/evidence.md`, `../main/synthesis/sub-niche-map.md`
   and every digest in full. Read the digests side by side: a pattern that looks minor in
   each share may be large across all of them. Open the voice files when you need more.
2. **Evidence file: `synthesis/evidence.md`.** Add the new quotes here, sorted under
   themes, verbatim with ids. This file is complete, not short: every new quote is either
   reproduced or cited by id under the theme it supports. Carry over every money item and
   every outright request the digests list.
3. **Conclusions: `synthesis/findings.md`, `synthesis/niche-opportunities.md`,
   `synthesis/purchase-evidence.md` and `../main/synthesis/sub-niche-map.md`.** Keep these
   readable. Where the new evidence changes, sharpen or contradicts a conclusion or a
   ranking, rewrite it, and support it with the strongest few quotes and a pointer to the
   theme in `evidence.md`. Do not paste quotes in bulk here. Do not leave an old conclusion
   standing beside evidence that undercuts it. Keep every id these files already cite.
   A quote may be left out of these files because it repeats what others show, never
   because of its subject.
4. Add a dated section to the end of `synthesis/findings.md`, "What the 2026-11-17
   re-reading changed": each conclusion or ranking that moved, what it said, what it says
   now, and the ids behind it. Say once, where counts are discussed, that these units were
   chosen because they had been excluded and are not a sample of how common anything is.
5. Bring the set's records up to date: the state lines and counts in `README.md`,
   `synthesis/counts.md` and its JSON, the quote catalogue and language bank (rebuild with
   the set's own tools in `_tools/`), and a closing section in
   `synthesis/unfilter-report.md` saying the re-reading is done and what is still unread
   or unavailable.
6. Verify with the set's own checks (`python3 -I`): all cited ids resolve, every quoted
   fragment matches its source, no duplicate ids. Fix what fails.

## Layout for quotes you add

The id in square brackets on its own line, then the quote as a `> ` blockquote. In running
text, use the style the document already uses.

## Report back (console only; the supervisor commits)

Counts (quotes read, quotes in the evidence file, quotes cited in the conclusion files),
the conclusions and rankings that changed in one line each, files changed, check output,
and anything you were unsure of.
