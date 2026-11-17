# Brief: fold the re-read quotes into the development findings

Working directory: the `ads` repo, branch `research-unfilter`.
Build: `mamivio.com/research/development/`. No network. Do not use git. Never modify
anything under `_raw/` or any `voice/reddit-*.jsonl` or `sources/reddit-reading-*.md` file.

## Background

The owner's ruling (2026-11-16): research never filters or censors. An earlier rule kept
1,169 posts out of this build because of their subject. Five readers (UR01-UR05) have now
read all of them and written 1,182 verified quotes:

- quotes: `voice/reddit-ur01.jsonl` ... `voice/reddit-ur05.jsonl` (ids `dv21-` to `dv25-`)
- ledgers, each ending in "What these posts add": `sources/reddit-reading-ur01.md` ... `ur05.md`
- what was filtered and why: `synthesis/unfilter-report.md`

`synthesis/findings.md` does not include any of this yet.

## Task

1. Read `synthesis/findings.md` in full, the five "What these posts add" sections, and
   every one of the 1,182 quotes. Do not sample.
2. Revise `synthesis/findings.md` so it tells the whole truth about this buyer:
   - Put the new evidence into the sections it belongs to, quoted verbatim with ids, in
     the same style as the existing quotes. Add sections where a pattern has no home.
   - Where the new evidence changes, sharpens or contradicts a conclusion, rewrite the
     conclusion. Do not leave an old conclusion standing beside evidence that undercuts it.
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
   `development/_tools/` and `_shared/_tools/`). Add a short closing section to
   `synthesis/unfilter-report.md` saying the re-reading is done and what, if anything,
   is still unread.
4. Verify with the build's own checks (`python3 -I _shared/_tools/verify_findings_ids.py`,
   `check_ids.py`, `audit_niche.py` as applicable). All cited ids must resolve and every
   quoted fragment must match its source. Fix what fails.

## Report back

Counts (quotes read, quotes cited in the findings, new sections), the conclusions that
changed in one line each, files changed, check output, and anything you were unsure of.
