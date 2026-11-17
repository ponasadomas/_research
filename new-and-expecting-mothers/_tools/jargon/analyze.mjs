// Step 3: corpus JSONL -> scored term lists (data/out/terms.json + terms.csv).
// Three passes (unigram, bigram, acronym) scored vs baseline with Monroe log-odds,
// merged by z-score; plus a UK-vs-US pass within the parenting corpus.

import { createReadStream } from 'node:fs';
import { createInterface } from 'node:readline';
import { mkdir, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import config from './config.mjs';
import { tokens, tokensLower, unigrams, bigrams, acronyms } from './lib/tokenize.mjs';
import { logOdds, countInto } from './lib/logodds.mjs';

const KINDS = ['uni', 'bi', 'acr'];

/** Stream a corpus JSONL, yielding parsed docs (corpora are too large to hold in memory). */
async function* readJsonl(name) {
  const rl = createInterface({ input: createReadStream(join(config.dataDir, 'corpus', name)), crlfDelay: Infinity });
  for await (const line of rl) {
    if (line) yield JSON.parse(line);
  }
}

// Source membership is a bitmask, not a Set per term: with millions of distinct
// bigrams, one Set object per term costs gigabytes.
const sourceBit = new Map();
const bitFor = (sub) => {
  if (!sourceBit.has(sub)) {
    if (sourceBit.size >= 31) throw new Error('More than 31 sources — source mask needs a wider representation.');
    sourceBit.set(sub, 1 << sourceBit.size);
  }
  return sourceBit.get(sub);
};
const popcount = (n) => { let c = 0; while (n) { n &= n - 1; c++; } return c; };

function makeCounters() {
  const blank = () => Object.fromEntries(KINDS.map((k) => [k, new Map()]));
  return {
    counts: blank(),
    sourceMask: blank(),
    ukCounts: blank(),
    usCounts: blank(),
    regionTokens: { UK: 0, 'US-leaning': 0 },
  };
}

function countDoc(c, doc, trackRegion) {
  const lower = tokensLower(doc.text);
  const streams = { uni: unigrams(lower), bi: bigrams(lower), acr: acronyms(tokens(doc.text)) };
  // Region math uses parenting-topic sources only (see config.mumsnet.boards)
  const countsForRegion = trackRegion && doc.regionCompare !== false;
  if (countsForRegion) c.regionTokens[doc.region] += lower.length;
  const bit = bitFor(doc.sub);
  const isUK = doc.region === 'UK';
  for (const kind of KINDS) {
    const terms = streams[kind];
    countInto(c.counts[kind], terms);
    const masks = c.sourceMask[kind];
    const region = countsForRegion ? (isUK ? c.ukCounts[kind] : c.usCounts[kind]) : null;
    for (const t of terms) {
      masks.set(t, (masks.get(t) ?? 0) | bit);
      if (region) region.set(t, (region.get(t) ?? 0) + 1);
    }
  }
}

const P = makeCounters();
const B = makeCounters();
for await (const doc of readJsonl('parenting.jsonl')) countDoc(P, doc, true);
// Spread filter counts parenting sources only, so snapshot before the baseline pass
const sourcesPresent = sourceBit.size;
for await (const doc of readJsonl('baseline.jsonl')) countDoc(B, doc, false);

// Spread filter can't exceed the number of parenting sources actually present (mini runs use 1 sub)
const minSpread = Math.min(config.minSourceSpread, sourcesPresent);
if (minSpread < config.minSourceSpread) {
  console.log(`note: only ${sourcesPresent} source(s) in corpus — spread filter lowered to ${minSpread}`);
}

const hasUK = P.regionTokens.UK > 0;
const per10k = (count, tokens) => (tokens > 0 ? (count / tokens) * 10_000 : 0);

// --- Score each pass, apply filters ---
const results = [];
const subForBit = new Map([...sourceBit].map(([sub, bit]) => [bit, sub]));
const subsFromMask = (mask) =>
  [...subForBit].filter(([bit]) => mask & bit).map(([, sub]) => sub).sort().join('|');

for (const kind of KINDS) {
  const scored = logOdds(P.counts[kind], B.counts[kind], config.alpha0);
  // UK-vs-US pass within parenting (only meaningful once UK sources are in the corpus)
  const ukScored = hasUK ? logOdds(P.ukCounts[kind], P.usCounts[kind], config.alpha0) : new Map();

  for (const [term, s] of scored) {
    if (s.countP < config.minTermCount) continue;
    const mask = P.sourceMask[kind].get(term) ?? 0;
    if (popcount(mask) < minSpread) continue;
    if (s.z <= 0) continue;

    const ukCount = P.ukCounts[kind].get(term) ?? 0;
    const usCount = P.usCounts[kind].get(term) ?? 0;
    const rateUK = per10k(ukCount, P.regionTokens.UK);
    const rateUS = per10k(usCount, P.regionTokens['US-leaning']);
    let regionTag = 'both';
    if (hasUK) {
      const { ratio, minCount, minExpectedForAbsence } = config.regionTag;
      // A "US" tag rests on the term being ABSENT from UK sources, which is only
      // meaningful if the UK corpus is large enough that we'd expect to see it there.
      const expectedInUK = (usCount / (P.regionTokens['US-leaning'] || 1)) * P.regionTokens.UK;
      if (rateUK >= rateUS * ratio && ukCount >= minCount) regionTag = 'UK';
      else if (rateUS >= rateUK * ratio && usCount >= minCount && expectedInUK >= minExpectedForAbsence) {
        regionTag = 'US';
      }
    }

    results.push({
      term, ngram: kind,
      z_general: round(s.z), count_parenting: s.countP, count_baseline: s.countB,
      rate_uk_per10k: round(rateUK), rate_us_per10k: round(rateUS),
      region_tag: regionTag, z_uk_vs_us: round(ukScored.get(term)?.z ?? 0),
      sources: subsFromMask(mask),
    });
  }
}

function round(x) { return Math.round(x * 100) / 100; }

// --- Dedupe: suppress a unigram when >=70% of its occurrences sit inside one top bigram ---
const uniByTerm = new Map(results.filter((r) => r.ngram === 'uni').map((r) => [r.term, r]));
const suppressed = new Set();
for (const bi of results.filter((r) => r.ngram === 'bi')) {
  for (const word of bi.term.split(' ')) {
    const uni = uniByTerm.get(word);
    if (uni && bi.count_parenting / uni.count_parenting >= 0.7 && bi.z_general >= uni.z_general * 0.5) {
      suppressed.add(word);
    }
  }
}
const finalResults = results
  .filter((r) => !(r.ngram === 'uni' && suppressed.has(r.term)))
  .sort((a, b) => b.z_general - a.z_general);

// --- Write outputs ---
const outDir = join(config.dataDir, 'out');
await mkdir(outDir, { recursive: true });
await writeFile(join(outDir, 'terms.json'), JSON.stringify(finalResults, null, 1));

const cols = ['term', 'ngram', 'z_general', 'count_parenting', 'count_baseline',
  'rate_uk_per10k', 'rate_us_per10k', 'region_tag', 'z_uk_vs_us', 'sources'];
const csv = [cols.join(','), ...finalResults.map((r) =>
  cols.map((c) => {
    const v = String(r[c]);
    return /[",]/.test(v) ? `"${v.replace(/"/g, '""')}"` : v;
  }).join(','))].join('\n');
await writeFile(join(outDir, 'terms.csv'), csv + '\n');

console.log(`Scored ${finalResults.length} terms (${suppressed.size} unigrams folded into bigrams).`);
console.log(`UK sources present: ${hasUK ? 'yes' : 'no — region tags disabled'}`);
console.log('\nTop 30 by z:');
for (const r of finalResults.slice(0, 30)) {
  console.log(`  ${String(round(r.z_general)).padStart(7)}  ${r.ngram.padEnd(3)}  ${r.term.padEnd(24)} ${r.region_tag}`);
}
