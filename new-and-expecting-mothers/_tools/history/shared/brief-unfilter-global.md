# Brief: remove the "research-only" filter from the global research set

Working directory: the `ads` repo, branch `research-unfilter` (already checked out).
Scope: `mamivio.com/research/global/` and `mamivio.com/research/main/`. Touch nothing
else. Never modify or delete anything under any `_raw/` folder. No network. Do not use
git; the supervisor commits.

## Why

The owner's ruling (2026-11-16): research must never filter or censor. It records what
people actually say and do, in their words, whatever the subject. What is usable in copy is
the owner's decision, made later; it is never a research decision. Earlier agents added
filtering rules to this research on their own initiative. The owner did not ask for them.
Undo them, without losing anything. The full rules are in `~/GitHub/_research/README.md`
(sections "Research never censors", "Three layers", "Conventions"); read them first.

The same job has been done on the five niche sets beside this one. See
`development/synthesis/unfilter-report.md` for a finished report. This set is older and its
filter worked differently, so verify everything below rather than assuming it.

## What is known (verify, do not assume)

- `global/README.md` and `global/synthesis/counts.md` say: 2,162 excerpts, a "language
  bank" of 1,144 entries, and **141 "research-only" records excluded** from the language bank.
- Reader notes say clinical and other excerpts were "marked research-only where needed".
- Reader notes also show triage: cards "dropped, bodies unread" and items "excluded after
  full read". Some drops are ordinary off-topic drops; some may be because of the subject.
- Briefs, READMEs and scripts in `global/_tools/` may instruct or enforce these rules.
- `main/` is the niche-selection write-up built on this set; it may repeat conclusions or
  rules that depend on the filter.

## Tasks

1. **Report first.** Write `global/synthesis/unfilter-report.md`: every place a filter
   acted, by stage (triage, reading, quote extraction, marking, language bank, findings,
   tooling), with counts and file paths. For each rule say in the agents' own words what it
   excluded and the reason given. Separate clearly:
   - material excluded **because of its subject** (sensitive, clinical, unsafe for an ad,
     and the like): this is what the ruling forbids;
   - material dropped as **off-topic or duplicate**: allowed, but say how many and how the
     decision was made, and whether "off-topic" was in practice used to drop a subject.
   Say plainly what was withheld before it reached `voice/*.jsonl` and can only be
   recovered by re-reading raw units. Write those units to
   `global/scratchpad/unfilter-reread/queue.tsv` (unit id, raw file path, stage that
   dropped it, reason). Do not re-read them now.

2. **Restore the 141.** Put every research-only record back as an ordinary record:
   into the language bank and any index built from the voice files (rebuild with the set's
   own tools), and into the synthesis documents where they belong, quoted verbatim with
   ids. Where they change or sharpen a conclusion, in `global/synthesis/` or in `main/`,
   change the conclusion and say so. Do not bury them in an appendix. Keep all existing ids.
   A label such as a theme may stay; a flag that hides or excludes may not.

3. **Instructions and tools.** In READMEs, briefs and scripts under `global/` and `main/`:
   remove every instruction to restrict, withhold, exclude, soften or avoid quoting material
   because of its subject, and replace each with the principle above in two or three
   sentences. Change any script that enforces the old rule so it no longer skips, hides or
   fails on those records. Keep every other check. Leave historical run logs and reader
   notes as they are: they are records of what happened.

4. **Dated record.** Add a closing section "What the 2026-11-16 unfilter changed" to the
   main findings document(s) you revised: each conclusion that moved, what it said, what it
   says now, and the ids behind it.

5. **Verify.** Run the set's own checks (see `global/_tools/` and `_shared/_tools/`, with
   `python3 -I`). All cited ids must resolve, every quoted fragment must match its source,
   no duplicate ids. Include the output in the report, and list every file you changed.

## Layout for quotes

When you reproduce a quote in a markdown file, use the style the document already uses.
Where you add a block of quotes, write each as a `> ` blockquote with its id in square
brackets on the line before it.

## Report back

End with a short summary to the console: records restored, conclusions that changed in one
line each, how many units are in the re-read queue and from which stages, files changed,
check results, and anything you were unsure of.
