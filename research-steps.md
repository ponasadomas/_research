# Research steps: what was done, and how to repeat it

Written 2026-11-20, after the first full run (the mothers' crowd, niche `baby-development`).
Words are used as in `glossary.md`. The rule these steps follow is "The five steps of
research" in `~/GitHub/_home/playbooks/new-niche.md`. The commands for each step are in
`_tools/README.md`.

## The steps

"Done this time?" is about the first run. "On command" says what has to exist so that the
step is started with one command and can go wrong in fewer ways.

| # | Step | Purpose | Done this time? | Who | How it becomes repeatable on command |
|---|---|---|---|---|---|
| **1** | **Pick the crowd** | | | | |
| 1a | Name the crowd and list its places | Fix where people gather, with nothing else decided | Yes: 22 subreddits | Owner | A short form the owner fills in: the crowd's name and its places. Nothing else is asked |
| 1b | Collect each place whole | Have everything on disk, so nothing is ever chosen by a keyword | Yes, through the archive's API (slow) | Script | Skill `collect-source`: one command per source, from downloaded dump files. Ends with a count of posts and replies per place |
| **2** | **Map reading** | | | | |
| 2a | Draw a random sample | A fair, repeatable set of posts | Skipped | Script | `draw_sample.py`, already general. The command records pool size and seed |
| 2b | First small map reading | Find out what this crowd keeps stating, in free words | Skipped | Readers | Brief exists as a draft (`new-and-expecting-mothers/_work/2026-11/map/`). Needs a checker and to be run once |
| 2c | Agree the columns and a subject list | Turn free words into fixed values, so many readers can be counted together | Skipped | Supervisor drafts, owner agrees | A script that lists the most frequent free labels and stated facts; the owner strikes and adds |
| 2d | Large map reading | Describe every post of a large sample | Skipped | Readers | The reading runner with the map brief and map checker |
| **3** | **The map** | Show what the crowd writes about, in which situations, how often, where paying shows up | Skipped | Script | One counting script that makes the map page from the map reading |
| **4** | **Choose a niche** | Put a subject and its range in one line, with counts behind it | Done without a map: the subject was named first and the range was set by the owner afterwards | Owner | The owner writes the line in `library/niches.md`; `check_definition.py` then refuses any brief that does not carry it |
| **5** | **Deep reading** | | | | |
| 5a | First reading | See what on-niche posts look like before fixing any list | Yes: 1,500 posts | Readers | Runner and checker exist. The brief must take the definition from `niches.md`, not from its own text |
| 5b | Draft the pattern list | Name what on-niche posts are about | Yes: 12 patterns and "none" | Supervisor drafts, owner agrees | A brief for one agent that drafts the list from the first reading's one-line descriptions |
| 5c | Test the pattern list | Know how well two agents agree, and how many posts fit none | Yes: three coders, 30 shared posts | Coders | Runner and checker exist |
| 5d | Trial of the main brief | Catch a brief that marks too much or too little, and choose the effort | Yes | Readers | Built into the reading runner as "first block is the trial"; the runner prints the trial's shares and waits |
| 5e | Main reading | Mark, tag and quote a large random sample | Yes: 20,000 posts, then 12,534 read again | Readers | `run_pass.sh`, general. Blocks are cut in shuffled order, so it can stop anywhere |
| 5f | Counts page | Posts per pattern, per stage, per border | Yes | Script | `count_patterns.py`, general |
| 5g | Digests | Find the forms inside each pattern | Yes: 34 | Digest readers | `make_digest_shares.py`, `run_digests.sh`; the brief still names the niche in its text |
| 5h | Sections | One short page per pattern | Yes: 26 | Section writers | `run_sections.sh`; same remark on the brief |
| 5i | Findings page and her words | The whole range in one sitting | Yes | Findings writer | Skill `write-findings`. Next time: one writer per pattern group, then one to join (see the post-mortem) |
| 5j | Owner reviews | Nothing counts as known until the owner has read it | Not yet | Owner | A line on the page: "Reviewed by the owner: <date>" |
| | **After research: the avatar** | Who she is, from the reviewed findings | Not yet | Avatar writer | Skill `write-avatar` |

### What "on command" needs overall

| Piece | State |
|---|---|
| Skill `collect-source` | Planned, not built |
| Skill for the map (steps 2 and 3) | Not built; one draft brief |
| Skill `continue-research`: runs the next unfinished job of a niche until done or usage runs out | Planned, not built; the runners under it exist |
| Briefs as templates that take the definition, the pattern list and the stage list as inputs | Not done: every brief still has the mothers' crowd written into it |
| One queue file per niche that says which step is next and how far it is | Not built |
| A second crowd run through all of it | Not done. Until then nothing here is proven general |

## Post-mortem of the first run

What went wrong, what it cost, and what stops it next time. "In place" means the fix exists
today; "to do" means it does not.

### Mistakes in the order of the work

| # | Mistake | What it cost | What stops it next time | State |
|---|---|---|---|---|
| 1 | The niche was named before any map existed, in October even with a product in mind | The October round was unusable for conclusions | The five steps: a niche is chosen from a map | Rule in place; steps 2 and 3 not built |
| 2 | A keyword list, written by us, decided which posts anyone read | Same | Samples are random. No keyword chooses what is read | In place |
| 3 | The age limit (24 months) was copied from an old brief into the new one; the owner meant 48 | 12,534 posts read twice; a day | The definition lives in one place, the owner confirms it, the runner checks it | In place |
| 4 | Each "definition" I wrote added things only the research can know (her problem, who she is) | Three rounds of correction | A definition is the subject and its range, nothing else | In place |
| 5 | No run-book was kept while running | The owner could not see where we were | The run-book and this page are updated as part of each step | In place |

### Mistakes in sampling and counting

| # | Mistake | What it cost | What stops it next time | State |
|---|---|---|---|---|
| 6 | A "random" check sample was drawn from the already filtered pool and presented as a fix | A wrong reassurance | Every sample states its pool; the pool is the whole crowd | In place |
| 7 | Shares were dealt in date order | 4,500 posts read that cannot be used for counts | Blocks are cut in shuffled order | In place |
| 8 | Quotes were counted instead of posts (October) | Counts that showed nothing | Counts are of posts | In place |
| 9 | "Paid for something" is counted in two places that disagree (138 and 173) | An unclear number on the findings page | One place counts it: the reader's `paid` column. Digest readers do not count it again | To do |
| 10 | Promotional, fictional and AI-written posts sit in the counts | Slightly inflated counts | A column for what kind of post it is, filled by the reader | To do |
| 11 | The same text posted to two subreddits is counted twice | Slightly inflated counts | Drop repeats when the sample is drawn (same author and title) | To do |
| 12 | The two halves of the range were read under two briefs by different readers | A jump at 24 months may partly come from that | One brief for the whole range from the start, which mistake 3 prevented | Follows from 3 |
| 13 | Posts were read without the poster's later replies, because fetching them was slow | Thinner material for most posts | Collect replies in bulk before any reading starts | Rule in place |

### Mistakes in sending agents

| # | Mistake | What it cost | What stops it next time | State |
|---|---|---|---|---|
| 14 | Model and effort were written into a script | Would have sent agents nobody agreed to | Runners take them as arguments; the owner is asked each time | In place |
| 15 | A checker was tested only on a made-up short example; it failed on quotes that run over several lines | 14 digests redone for nothing | Test every checker on real output of the step before | Rule in place |
| 16 | A page-wide word limit made section writers clip quotes to fragments | 416 quotes repaired by script | A limit per finding, and "fewer quotes, not shorter ones" | In the brief |
| 17 | I said "about 9" agents before cutting the shares; it was 14 | One extra question | Cut the shares first, then ask with the exact number | Rule: to write into the runner |
| 18 | A new brief made "near" cover two thirds of all posts | Caught in the trial | The first block of every reading is a trial | In place |
| 19 | One findings writer was given 26 sections; it read 2 whole and skimmed 24 through a script | A thinner findings page than asked for | One writer per pattern group, each reading only its own sections whole; then one writer joins | To do |
| 20 | A finding used a keyword scan for one number | One sentence to remove | The brief says: no number that is not a count of tags | To do |
| 21 | `git add -A` swept a large download into a commit | Cleaned up before pushing | Commit by path | In place |

### Mistakes in how I reported

| # | Mistake | What it cost | What stops it next time | State |
|---|---|---|---|---|
| 22 | Long prose answers | The owner could not follow | Short bullets and tables; one question at a time | In place |
| 23 | Many words for the same thing, and the same word for different things | The owner could not follow | `glossary.md`: one word, one meaning | In place |
| 24 | Work in the background with only status lines | The owner could not tell whether anything was happening | One agent is always shown live in a side pane | In place |
| 25 | A column of free "her words" was counted by exact match and I concluded "she has no fixed words" | A wrong conclusion, withdrawn | No counting of free text; her words come from the quotes | In place |

### What the next run should do differently, in order

1. Run steps 2 and 3 for real: a map reading and a map, before any niche line is written.
2. Turn the briefs into templates that take the definition, the pattern list and the stage list as inputs.
3. Fix the three "to do" counting items (9, 10, 11) in the reading brief and the sample draw.
4. Split the findings step: one writer per pattern group.
5. Build `continue-research` on the runners, with the queue file.
6. Run a second, different crowd through all of it. Only that shows whether this is general.
