# _tools

Scripts shared by every niche. Run them from `~/GitHub/_research`.

| Script | What it does |
|---|---|
| `draw_sample.py` | Draws a random sample of Reddit posts for a niche from the shared archive, with no keyword; `--only-ids` narrows the pool to posts a word list matched |
| `build_post_files.py` | Makes one reading file per sampled post (the post and the poster's own replies) and deals the sample out to readers |
| `verify_quotes.py` | Checks every quote, word for word, against the file it cites |
| `check_ids.py` | Checks that no quote id is used twice in a niche |

A niche's own `_tools/` holds only what is particular to that niche: the checks for its
October 2026 round and, under `history/`, the scripts and briefs that round used.
