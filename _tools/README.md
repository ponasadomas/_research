# _tools: how a research round is run

Scripts shared by every niche, and the order to run them in. This is the method as it was
run by hand for `baby-development` in November 2026. The skills (`collect-source`,
`continue-research`, the reading skills) will be written from this page; until then, follow
it. Why each rule exists: `~/GitHub/_home/playbooks/new-niche.md`, "Lessons".

Run everything from `~/GitHub/_research`. `<W>` is `<niche>/_work/<yyyy-mm>`.

## Rules that hold for every step

- **Agents:** before any step marked "agents", ask the owner provider, model, effort, how
  many and how many at a time, and wait for a yes. The runners take model and effort as
  arguments and write what was sent to `sent.txt`.
- **Runners** (`run_*.sh`) are started in a terminal pane the owner can watch. They show one
  agent live, check every output, redo a failed one whole once, commit each checked group,
  stop by themselves when usage runs out, and carry on when the same command is run again.
- **Test a checker on real output before sending agents.** A fake short example is not
  enough (see "What went wrong").
- **Commit by path, never `git add -A`.** The owner pushes `_research`.

## The steps

| # | Step | Agents? | Command | Output | Done when |
|---|---|---|---|---|---|
| 0 | Define the niche with the owner: the subject and its range, in one line. Never who she is or her problem; the research finds those. Then write the brief around that definition, copied word for word; no product, price or brand | no | by hand; `check_definition.py <niche> <brief>...` | `~/GitHub/_home/library/niches.md` "Definitions"; `<niche>/brief.md` | owner has confirmed the definition; the check prints OK. `run_pass.sh` refuses to start otherwise |
| 1 | Collect each place whole, no keyword | no | Reddit replies: `fetch_sub_comments.py <first day> <last day> <subs> 8` then `index_own_replies.py <subs>`. Posts and larger amounts: see the playbook, "Planned, not built" | shared archive `new-and-expecting-mothers/reddit/raw/reddit-2026/` | every state file says done |
| 2 | Draw a random sample; count the pool; record the seed | no | `draw_sample.py <niche> <round> <label> <size> <seed> --subs A,B [--exclude-samples ...]` | `<W>/<label>/sample.tsv`, `pool.json` | pool counted, posts with text gone counted |
| 3 | First reading: a small sample (1,500), marks yes / near / no, free quotes | agents | `run_readers.sh` (uses `build_post_files.py`, `verify_reading.py`) | `<W>/first-reading/` | every post has a row |
| 4 | Draft the pattern list from the first reading's on-niche posts; owner looks at it | no | by hand | `<W>/patterns/patterns.md` | owner agrees |
| 5 | Test the list: three coders tag the first reading's posts, 30 posts shared | agents | `run_coders.sh` (`verify_coding.py`) | `<W>/patterns/coded-*.tsv` | agreement counted; few posts fit none |
| 6 | Test the effort level: the same 150 posts at two efforts | agents | `<W>/effort-test/run.sh` | yes posts found by each | owner picks the effort |
| 7 | Main reading: read and sort a large random sample in one pass | agents | `run_pass.sh <niche> <dir> <quotes dir> <prefix> <top pattern> <model> <effort> 150 5 <seed>` (`make_block.py`, `verify_pass.py`) | `<dir>/posts-*.tsv`, `<niche>/quotes/reddit-<prefix>NNN.jsonl` | PASS-DONE |
| 8 | Count posts per pattern | no | `count_patterns.py <niche> <round> <out label> <top pattern> <patterns.md> <reading>:<prefix>...` (a later reading replaces an earlier one for the posts it read again) | `<niche>/evidence/<round>/<label>/counts.md`, `pattern-NN.md`, `posts.tsv` | prints COUNTED; read `counts.md` |
| 9 | Digest each pattern into its forms | agents | `make_digest_shares.py <evidence dir> <W>/digests 315`, then `run_digests.sh <niche> <W>/digests <evidence dir> <model> <effort> 5` (`verify_digest.py`) | `<evidence dir>/digest-NN.md` | DIGESTS-DONE |
| 10 | One findings section per pattern, merging its digests | agents | `run_sections.sh <niche> <W>/sections <W>/digests <evidence dir> <niche>/findings/<round>/patterns <niche>/quotes <model> <effort> 5` (`verify_section.py`, `check_findings.py`), then `expand_clipped_quotes.py <niche>/quotes 70 <pages>` | `<niche>/findings/<round>/patterns/pattern-NN.md` | SECTIONS-DONE, checks OK after widening |
| 11 | The findings page and her words, from the sections | agents | `/write-findings <niche>` in `~/GitHub/_home` | `<niche>/findings/`, `her-words.md` | checker OK; owner reviews |
| 12 | The avatar | agents | `/write-avatar <niche>` | `~/GitHub/_home/library/avatars/<niche>/avatar.md` | owner reviews |

The briefs each agent step used are kept beside its output and are the starting point for
the next niche: `baby-development/_work/2026-11/brief-read-and-sort.md` (step 7),
`digests/brief-digest.md` (9), `sections/brief-section.md` (10), `first-reading/brief-reader.md`
(3), `patterns/brief-coder.md` (5). They still name the niche in their text.

## What it took (Codex, `gpt-6.1-sol`, high, November 2026)

| Step | Size | Agents | Time |
|---|---|---|---|
| 1 Replies of 12 subreddits, 7.5 months | 4.19 million replies | none | 7.5 hours |
| 3 First reading | 1,500 posts | 5 | about 45 minutes |
| 7 Main reading | 24,500 posts (150 per reader) | 164, 10 at a time | 4 hours; used up what was left of one usage |
| 9 Digests | 4,388 posts in 20 shares | 20, 5 at a time | 9 to 15 minutes each |
| 10 Sections | 13 patterns | 13, 5 at a time | 32 minutes |

About 12% of the posts were on the niche, so 20,000 posts gave 2,471 on-niche posts.

## What went wrong, and what the next run does instead

| What happened | Do instead |
|---|---|
| `make_block.py` dealt shares in date order; the stopped third reading had read only 1 to 9 April and could not be used for counts | Fixed 2026-11-20: blocks are cut from a shuffled order. `<dir>/order.txt` says how many leading rows were already dealt by date (third reading: 4,500); everything read after them is a fair sample of the rest |
| The digest checker read only the first line of a quote; it rejected 14 good digests and each was redone | Test every checker on real output of the step before it, including a quote that runs over lines |
| A 2,500-word limit made section writers clip quotes to fragments | Give a limit per finding, not per page; or widen afterwards with `expand_clipped_quotes.py` |
| The age limit (24 months) came from an older brief; the owner meant 48. 12,534 posts had to be read again | Step 0: the definition is agreed with the owner and kept in `library/niches.md`; briefs copy it; the runner checks it |
| The combined brief first made "near" cover two thirds of all posts | Try a new brief on 150 posts before the main reading (step 6 does this) |
| Fetching replies post by post was too slow to keep up with readers | Download replies in bulk before the reading starts |
| `git add -A` swept the bulk download into a commit | Commit by path; large downloads are in `.gitignore` |
| A free-form "her words" column was counted by exact match and showed nothing | Do not count vocabulary from free-form columns; her words come from the quotes |

## Scripts

| Script | What it does |
|---|---|
| `draw_sample.py` | Draws a random sample of posts from the shared archive, with no keyword |
| `build_post_files.py`, `fetch_replies.py` | First reading only: one file per post, replies fetched post by post (slow; superseded by the bulk download) |
| `fetch_sub_comments.py`, `index_own_replies.py` | Bulk download of every reply of named subreddits; index of each poster's own replies |
| `make_block.py`, `run_pass.sh`, `verify_pass.py` | Main reading: deal a block of shares, run the readers, check one reader |
| `run_readers.sh`, `verify_reading.py` | First reading: run and check |
| `run_coders.sh`, `verify_coding.py` | Pattern test: run and check |
| `count_patterns.py` | Merge a reading and count posts per pattern |
| `make_digest_shares.py`, `run_digests.sh`, `verify_digest.py` | Digests: cut shares, run, check |
| `run_sections.sh`, `verify_section.py`, `expand_clipped_quotes.py` | Findings sections: run, check counts, widen clipped quotes |
| `verify_quotes.py`, `check_ids.py` | Any quotes file: word for word against its source; no id used twice |

A niche's own `_tools/` holds only what is particular to that niche.
