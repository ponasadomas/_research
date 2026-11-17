# Brief: remove the "restricted" filter from the development build

Working directory: the `ads` repo, branch `research-unfilter` (already checked out).
Scope: `mamivio.com/research/development/` and `mamivio.com/research/_shared/_tools/`.
Do not touch any other build, and never modify or delete anything under any `_raw/` folder.
No network access is needed. Do not push.

## Why

The owner's ruling (2026-11-16): research must never filter or censor. It records what
people actually say and do, in their words, whatever the subject. What is usable in copy is
the owner's decision, made later; it is never a research decision. An earlier agent added a
"restricted quote" rule to this research on its own initiative. The owner did not ask for
it, and it hid the rawest material from the findings. Undo it, without losing anything.

## What the filter did (verify, do not assume)

- `development/synthesis/restricted-ids.md` marks 218 of the build's quote ids.
- `development/synthesis/findings.md` cites some of them "(restricted)" but replaces their
  words with a description, and leaves the rest out.
- READMEs, reader prompts, briefs and scripts instruct future runs to do the same, and
  some scripts may enforce it (for example by failing when a restricted quote is quoted).
- The reading stage may also have skipped or withheld material before it reached
  `voice/*.jsonl`. Check the reader notes and reader prompts for this.

## Tasks

1. **Report first.** Write `development/synthesis/unfilter-report.md`: every place the
   filter acted, by stage (reading, quote extraction, marking, findings, tooling), with
   counts and file paths. Say plainly what was withheld at the reading stage that can only
   be recovered by re-reading raw units, and list those unit ids. Do not re-read them now.

2. **Findings.** Revise `development/synthesis/findings.md` so that it tells the whole truth:
   - Wherever a restricted id is cited, put the quote's exact words back, taken verbatim
     from `voice/*.jsonl`, in the same style as every other quote. Remove "(restricted)"
     and any sentence saying words may not be used or must not reach an ad.
   - Read every restricted quote that the findings never cited. Work them into the sections
     they belong to. Where they change or sharpen a conclusion, change the conclusion and
     say so. Do not bury them in an appendix.
   - Add a dated section at the end, "What the 2026-11-16 unfilter changed", listing the
     conclusions that moved and the ids behind each.
   - Every quote must be verbatim from the voice files. Invent nothing. Keep all existing ids.

3. **Markings.** Keep `restricted-ids.md` as a historical record, but retitle it and add a
   first paragraph: these ids were once marked restricted; the marking has no effect; they
   are ordinary quotes. Do not delete the list.

4. **Instructions and tools** (in `development/README.md`, `development/synthesis/` notes
   where they give instructions, and everything in `_shared/_tools/`):
   - Remove every instruction to restrict, withhold, exclude, soften or avoid quoting
     material because of its subject. Replace each "Lines not to cross" section with the
     principle in "Why" above, in two or three sentences.
   - Readers may still label a quote (for example with a theme), but nothing is withheld.
   - Change any script that enforces the old rule so that it no longer fails on, skips or
     hides restricted ids. Keep every other check (ids resolve, quotes match raw).
   - Leave historical run logs and reader notes as they are; they are records of what
     happened. Only change files that instruct or enforce.
   - List every file you changed in the report.

5. **Verify.** Run the build's own checks (`_shared/_tools/verify_findings_ids.py`,
   `check_ids.py`, `audit_niche.py` as applicable, with `python3 -I`) and include their
   output in the report. All cited ids must resolve and all quoted fragments must match.

6. **Commit** on `research-unfilter` with a clear message. One commit is fine.

## Report back

End with a short summary: counts restored, conclusions that changed, what could not be
restored without re-reading, files changed, check results, and anything you were unsure of.
