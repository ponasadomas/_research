# Brief: fold the re-read quotes into the sleep-baby findings

Working directory: the `ads` repo, branch `research-unfilter`.
Build: `mamivio.com/research/sleep-baby/`. No network. Do not use git. Never modify
anything under `_raw/` or any `voice/reddit-*.jsonl` or `sources/reddit-reading-*.md` file.

## Background

The owner's ruling (2026-11-16): research never filters or censors. An earlier rule kept
7122 posts, or passages in them, out of this build because of their subject. 24 readers have now
read all of them and written 8772 verified quotes:

- quotes: `voice/reddit-ur*.jsonl` (ids start `sbu`)
- ledgers, each ending in "What these posts add": `sources/reddit-reading-ur*.md`
- what was filtered and why: `synthesis/unfilter-report.md`

`synthesis/findings.md` does not include any of this yet.

## Task

The new quotes are too many for one agent to weigh at once, so digest agents have each read
a share of them in full and written `synthesis/unfilter-digest-NN.md`: the patterns in
that share, the quotes behind each, where each belongs in the findings, and whether it
confirms, extends or contradicts a current conclusion.

1. Read `synthesis/findings.md` in full and every `synthesis/unfilter-digest-*.md` in full.
   Read the digests side by side: a pattern that looks minor in each share may be large
   across all of them. Open the voice files whenever you need the full quote or more of
   the same pattern; they are the source, the digests are a guide.
2. Revise `synthesis/findings.md` so it tells the whole truth about this buyer:
   - Put the new evidence into the sections it belongs to, quoted verbatim with ids, in
     the same style as the existing quotes. Add sections where a pattern has no home.
   - Where the new evidence changes, sharpen or contradicts a conclusion, rewrite the
     conclusion. Do not leave an old conclusion standing beside evidence that undercuts it.
   - Carry over every money item and every outright request the digests list.
   - Keep every id the findings already cite. Soften, omit or paraphrase nothing because
     of its subject. Describe what parents say as they say it.
   - Be exact about what the evidence is. These posts were chosen because they had been
     excluded; they are not a sample of prevalence. Say so once, where counts are discussed,
     and keep the document's rule that counts are counts of quotes, never of people.
   - Add a dated section at the end, "What the 2026-11-16 re-reading changed": each
     conclusion that moved, what it was, what it is now, and the ids behind it.
3. Bring the build's records up to date so they agree with the findings: the state line and
   counts in `README.md`, `synthesis/counts.md`, `sources/reddit.md` or the source ledger,
   and `voice-merged/all.jsonl` (rebuild it the way the build's own tools do; check
   `sleep-baby/_tools/` and `_shared/_tools/`; do not edit shared scripts). Add a short closing
   section to `synthesis/unfilter-report.md` saying the re-reading is done and what, if
   anything, is still unread.
4. Verify with the build's own checks (`python3 -I _shared/_tools/verify_findings_ids.py <findings> sleep-baby`,
   `check_ids.py`, `audit_niche.py` as applicable). All cited ids must resolve and every
   quoted fragment must match its source. Fix what fails. Do not modify the digests.

## Report back

Counts (quotes read, quotes cited in the findings, new sections), the conclusions that
changed in one line each, files changed, check output, and anything you were unsure of.

## Also

- Other agents are working in other builds at the same time. Touch only `sleep-baby/`.
- The finished example of this job is the development build: its
  `synthesis/findings.md` (see the closing section "What the 2026-11-16 re-reading
  changed") and `synthesis/unfilter-report.md`.
- Write your final report to the console only; the supervisor commits.
