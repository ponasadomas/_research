# Competitors

Who sells to this buyer, what they sell and at what price.

- **Collected:** 2026-10-25, pages saved with `_tools/history/fetch_page.py`.
- **Question:** is anyone selling to her, and what is working?
- **Start with `overview.md`**: the list of all 21 sellers with a line each.
- **One note per seller** beside it (`kinedu-2026.md`, `babysparks-2026.md`, ...).
- **`raw/`:** the 57 saved pages the notes were written from (115 files with headers).
- **`not-harvested.md`:** sellers and pages that were found but not saved, and why.

The notes were written before the move and call the saved pages `../_raw/competitors/`;
they are now in `raw/`.

## `landing-pages-2026-11-05/`: how other sellers' pages look and what is reported to convert

- **Collected:** 2026-11-05. See its `README.md`.
- **What:** an audit of 43 seller URLs, two measured visual comparisons of current pages, recovered
  historical sales designs, and published conversion reports.
- Moved here on 2026-11-17 from the mamiVio site repo.

## `kinedu-aq-assessment/`: teardown of Kinedu's milestone quiz

- **Collected:** 2026-11-02 to 2026-11-10, by scripts in its own `scripts/` folder.
- **What:** how the quiz at `webpromo.kinedu.com/aq-assessment` works: its 408 questions, which
  ones each age gets, the extension round, and how the report is scored. Start with its `README.md`.
- **`raw/`:** 12,151 saved files, almost all of them the quiz server's answers (`raw/api/`).
- **Kept whole on purpose.** The mamiVio site's checking scripts read `raw/api/`, `quiz-spec/`,
  `scoring-table.csv` and `scripts/proxy_curl.sh` by path, so the inner layout must not change.
- Moved here on 2026-11-17 from `~/GitHub/mamiVio.com/research/`, where it was in no repo.
