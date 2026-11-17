# Books

Books sold to this buyer, and what readers say about them.

**Almost nothing was collected.** The October 2026 attempt looked for reader reviews of
nine books and came back with five reviews in total. Most files in `raw/` are empty or
hold only the store page, because that is what the stores returned.

- **Tried:** 2026-10-25, with `_tools/history/collect_apple_books.py` and
  `collect_barnes_reviews.py`. Nine titles, among them Brain Rules for Baby, The Montessori
  Baby, What to Expect the First Year and The Wonder Weeks.
- **Why so little:**
  - Barnes & Noble shows only a short, recent list of reviews; for six of the seven titles
    tried it was empty.
  - Apple Books shows star ratings but almost no written reviews (4 found).
  - Amazon and Goodreads, where book reviews actually are, were not fetched: both forbid
    automated collection in their robots rules.
- **What exists:** 5 reviews, giving 5 quotes, in `../quotes/reviews-rv1.jsonl`. Details
  per title are in `../reviews/reviews.md` and `../reviews/not-harvested.md`.
- **`raw/`:** 131 files: the saved store pages (`_html/`, 25 MB), the empty or near-empty
  review files, and the stores' robots rules.
- **Not done:** no notes on the books themselves (what each teaches, price, how it is
  sold). The question "what does she pay for, and was she satisfied?" is unanswered for books.
