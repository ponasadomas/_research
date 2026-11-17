// Smoke test: known mom-jargon should rank highly; junk should not.
// Heuristic pass/fail table — informational, no exit(1).

import { readFile } from 'node:fs/promises';
import { join } from 'node:path';
import config from './config.mjs';
import { selectTopTerms } from './lib/select.mjs';

const terms = JSON.parse(await readFile(join(config.dataDir, 'out', 'terms.json'), 'utf8'));
const key = (t) => (t.ngram === 'acr' ? t.term : t.term.toLowerCase());
const tag = new Map(terms.map((t) => [key(t), t.region_tag]));
// "Selected" = made the per-category quota, i.e. reached the glossary draft.
const selected = new Set(selectTopTerms(terms).map(key));

const inTop = (term) => selected.has(term);
const results = [];
const check = (label, ok) => results.push([ok ? 'PASS' : 'FAIL', label]);

// Known jargon expected to reach the glossary draft (any of the listed variants)
const expectTop = [
  ['LO', 'lo'], ['FTM', 'ftm'], ['wake windows', 'wake window'], ['cluster feeding', 'cluster feed'],
  ['sleep regression'], ['contact naps', 'contact nap'], ['DH', 'dh'], ['CIO', 'cio'], ['EBF', 'ebf'],
];
for (const variants of expectTop) {
  check(`glossary includes ${variants[0]}`, variants.some(inTop));
}

// Region tags (only meaningful when UK sources are present)
const hasUK = terms.some((t) => t.region_tag !== 'both');
if (hasUK) {
  for (const [term, want] of [['health visitor', 'UK'], ['AIBU', 'UK'], ['HV', 'UK'], ['nappy', 'UK'],
    ['diaper', 'US'], ['stroller', 'US']]) {
    check(`${term} tagged ${want}`, tag.get(term) === want);
  }
} else {
  results.push(['SKIP', 'region-tag checks (no UK sources in corpus)']);
}

// Junk and bot boilerplate must not reach the glossary
for (const junk of ['the', 'and', 'reddit', 'edit', 'post', 'upvote',
  'performed automatically', 'please contact', 'action performed']) {
  check(`glossary free of "${junk}"`, !inTop(junk));
}

let fails = 0;
for (const [status, label] of results) {
  if (status === 'FAIL') fails++;
  console.log(`  ${status}  ${label}`);
}
console.log(fails ? `\n${fails} check(s) failed — inspect terms.json / tune config.` : '\nAll checks passed.');
