// Step 4: for the top-scored terms, pull real usage examples from the parenting corpus.
// Single streaming pass over the corpus testing all terms per doc (the corpus is far
// too large to hold in memory, and re-scanning it per term would take hours).
// Prefers source diversity, then high score; snippets are sentence-bounded.

import { createReadStream } from 'node:fs';
import { createInterface } from 'node:readline';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import config from './config.mjs';
import { selectTopTerms } from './lib/select.mjs';

const terms = JSON.parse(await readFile(join(config.dataDir, 'out', 'terms.json'), 'utf8'));
const top = selectTopTerms(terms);

// Acronyms must match case-sensitively ("LO" not "lo"); other terms case-insensitively.
const probes = top.map((t) => {
  const escaped = t.term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return {
    term: t.term,
    ngram: t.ngram,
    cheap: t.ngram === 'acr' ? t.term : t.term.toLowerCase(), // substring prefilter
    caseSensitive: t.ngram === 'acr',
    re: t.ngram === 'acr' ? new RegExp(`\\b${escaped}s?\\b`) : new RegExp(`\\b${escaped}\\b`, 'i'),
    hits: new Map(), // sub -> candidate snippets (capped)
    total: 0,
  };
});

const PER_SUB_CAP = 20;

function snippet(text, re) {
  for (const sentence of text.split(/(?<=[.!?])\s+/)) {
    if (re.test(sentence)) {
      return sentence.length > 240 ? sentence.slice(0, 237).replace(/\s+\S*$/, '') + '…' : sentence;
    }
  }
  return null;
}

const rl = createInterface({
  input: createReadStream(join(config.dataDir, 'corpus', 'parenting.jsonl')),
  crlfDelay: Infinity,
});

let scanned = 0;
for await (const line of rl) {
  if (!line) continue;
  const doc = JSON.parse(line);
  const lower = doc.text.toLowerCase();
  scanned++;

  for (const p of probes) {
    if (!(p.caseSensitive ? doc.text : lower).includes(p.cheap)) continue;
    if (!p.re.test(doc.text)) continue;
    const s = snippet(doc.text, p.re);
    if (!s) continue;
    p.total++;
    let bucket = p.hits.get(doc.sub);
    if (!bucket) p.hits.set(doc.sub, (bucket = []));
    if (bucket.length < PER_SUB_CAP) {
      bucket.push({ snippet: s, sub: doc.sub, score: doc.score, url: doc.url });
    } else {
      // keep the highest-scored candidates per source
      let minIdx = 0;
      for (let i = 1; i < bucket.length; i++) if (bucket[i].score < bucket[minIdx].score) minIdx = i;
      if (doc.score > bucket[minIdx].score) {
        bucket[minIdx] = { snippet: s, sub: doc.sub, score: doc.score, url: doc.url };
      }
    }
  }
}

// Round-robin across sources so each term's examples span the communities that use it.
const examples = {};
for (const p of probes) {
  const queues = [...p.hits.values()].map((b) => b.sort((a, b2) => b2.score - a.score));
  const picked = [];
  while (picked.length < config.examplesPerTerm && queues.some((q) => q.length)) {
    for (const q of queues) {
      if (q.length && picked.length < config.examplesPerTerm) picked.push(q.shift());
    }
  }
  examples[p.term] = { ngram: p.ngram, totalHits: p.total, examples: picked };
}

const outDir = join(config.dataDir, 'out');
await mkdir(outDir, { recursive: true });
await writeFile(join(outDir, 'examples.json'), JSON.stringify(examples, null, 1));
console.log(`Examples extracted for ${probes.length} terms from ${scanned} docs.`);
