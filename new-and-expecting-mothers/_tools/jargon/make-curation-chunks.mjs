// Step 5b: split the candidate terms (+ their usage examples and Mumsnet definitions)
// into review-sized JSON chunks under data/out/curation/. Curation is a judgment task —
// meanings and connotation can't be derived statistically — so each chunk is a
// self-contained packet a human or LLM reviewer can work through without the corpus.
// Usage: node make-curation-chunks.mjs [--size=60]

import { mkdir, readFile, writeFile, rm } from 'node:fs/promises';
import { join } from 'node:path';
import config from './config.mjs';
import { selectTopTerms } from './lib/select.mjs';

const size = Number(
  process.argv.slice(2).find((a) => a.startsWith('--size='))?.split('=')[1] ?? 60
);

const outDir = join(config.dataDir, 'out');
const terms = JSON.parse(await readFile(join(outDir, 'terms.json'), 'utf8'));
const examples = JSON.parse(await readFile(join(outDir, 'examples.json'), 'utf8'));

let definitions = new Map();
try {
  const raw = JSON.parse(await readFile(join(outDir, 'mumsnet-acronyms.json'), 'utf8'));
  definitions = new Map(raw.map((a) => [a.term, a.meaning]));
} catch { /* glossary not fetched */ }

const selected = selectTopTerms(terms);
// An acronym entry supersedes its lowercase unigram twin (LO vs lo)
const acronymTerms = new Set(selected.filter((t) => t.ngram === 'acr').map((t) => t.term));
const candidates = selected.filter((t) => !(t.ngram === 'uni' && acronymTerms.has(t.term.toUpperCase())));

const packets = candidates.map((t) => ({
  term: t.term,
  kind: t.ngram,
  region_tag: t.region_tag,
  z: t.z_general,
  count: t.count_parenting,
  uk_per10k: t.rate_uk_per10k,
  us_per10k: t.rate_us_per10k,
  known_meaning: definitions.get(t.term) ?? null,
  sources: t.sources.split('|'),
  examples: (examples[t.term]?.examples ?? []).slice(0, 6).map((e) => `[${e.sub}] ${e.snippet}`),
}));

const curationDir = join(outDir, 'curation');
await rm(curationDir, { recursive: true, force: true });
await mkdir(curationDir, { recursive: true });

const chunks = [];
for (let i = 0; i < packets.length; i += size) chunks.push(packets.slice(i, i + size));
await Promise.all(
  chunks.map((chunk, i) =>
    writeFile(join(curationDir, `chunk-${String(i + 1).padStart(2, '0')}.json`), JSON.stringify(chunk, null, 1))
  )
);

console.log(`${packets.length} candidates -> ${chunks.length} chunks of <=${size} in data/out/curation/`);
