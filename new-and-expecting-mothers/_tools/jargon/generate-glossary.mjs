// Step 5: merge terms + examples + Mumsnet acronym definitions into a glossary DRAFT
// (data/out/glossary-draft.md). Meanings/tone are judgment calls — the draft carries
// TODO placeholders that the curation pass fills before committing research/jargon-glossary.md.

import { readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import config from './config.mjs';
import { selectTopTerms } from './lib/select.mjs';

const outDir = join(config.dataDir, 'out');
const terms = JSON.parse(await readFile(join(outDir, 'terms.json'), 'utf8'));
const examples = JSON.parse(await readFile(join(outDir, 'examples.json'), 'utf8'));

let mumsnetAcronyms = new Map();
try {
  const raw = JSON.parse(await readFile(join(outDir, 'mumsnet-acronyms.json'), 'utf8'));
  mumsnetAcronyms = new Map(raw.map((a) => [a.term, a.meaning]));
} catch { /* Mumsnet glossary not fetched — meanings stay TODO */ }

const top = selectTopTerms(terms);

// An acronym entry supersedes its lowercase unigram twin (LO vs lo)
const acronymTerms = new Set(top.filter((t) => t.ngram === 'acr').map((t) => t.term));
const entries = top.filter((t) => !(t.ngram === 'uni' && acronymTerms.has(t.term.toUpperCase())));

const fmtQuote = (e) => `> "${e.snippet}" — ${e.sub}`;
const quotesFor = (term, n) => (examples[term]?.examples ?? []).slice(0, n).map(fmtQuote).join('\n');

const acronymRows = entries.filter((t) => t.ngram === 'acr');
const wordRows = entries.filter((t) => t.ngram !== 'acr');
const ukRows = entries.filter((t) => t.region_tag === 'UK' || t.z_uk_vs_us >= 3);

const today = new Date().toISOString().slice(0, 10);
const sources = [...config.parentingSubs.map((s) => 'r/' + s.name), 'Mumsnet'].join(', ');

let md = `# Mom-Community Jargon Glossary (for Vitaful copy) — DRAFT

> Provenance: ${sources}; sampled via Arctic Shift (weekly windows ending ${config.corpusDateRange.end})
> plus Mumsnet talk boards. Scored against a general-Reddit baseline (r/${config.baselineSubs.map((s) => s.name).join(', r/')})
> with log-odds w/ informative Dirichlet prior (Monroe et al. 2008). Generated ${today}.
> Rerun: see research/reddit-jargon/README.md. Fill every TODO during curation.

## 1. Acronyms & abbreviations

| Term | Meaning | Region | Tone note | Example |
|------|---------|--------|-----------|---------|
`;

for (const t of acronymRows) {
  const meaning = mumsnetAcronyms.get(t.term) ?? 'TODO';
  const ex = (examples[t.term]?.examples?.[0]?.snippet ?? '').replace(/\|/g, '\\|');
  md += `| **${t.term}** | ${meaning} | ${t.region_tag} | TODO | ${ex} |\n`;
}

md += `
## 2. Core vocabulary

<!-- Curation: group these into themes (Sleep / Feeding / Pregnancy & birth / Development / Community voice),
     fill MEANING + TONE, prune generic topical words that aren't actually jargon. -->

`;

for (const t of wordRows) {
  md += `**${t.term}** — MEANING: TODO · Region: ${t.region_tag} · Tone: TODO · z=${t.z_general}, n=${t.count_parenting}\n`;
  const q = quotesFor(t.term, 3);
  if (q) md += q + '\n';
  md += '\n';
}

md += `## 3. UK-specific terms

`;
if (ukRows.length) {
  for (const t of ukRows) {
    md += `**${t.term}** (${t.ngram}) — MEANING: TODO · UK rate ${t.rate_uk_per10k}/10k vs US ${t.rate_us_per10k}/10k\n`;
    const q = quotesFor(t.term, 2);
    if (q) md += q + '\n';
    md += '\n';
  }
} else {
  md += `_No UK-tagged terms — UK sources missing from corpus (fetch Mumsnet / r/UKParenting first)._\n`;
}

md += `
## 4. Copywriting notes

<!-- Human-written during curation: register dos/don'ts, which terms read native vs
     marketing-cringe, connotation warnings (e.g. is "crunchy" affectionate or barbed?). -->
TODO
`;

await writeFile(join(outDir, 'glossary-draft.md'), md);
console.log(`Draft written: data/out/glossary-draft.md (${acronymRows.length} acronyms, ${wordRows.length} words/phrases, ${ukRows.length} UK-tagged).`);
