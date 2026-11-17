import config from '../config.mjs';

/**
 * Pick the glossary candidate set using per-category quotas.
 * Ranking everything in one pool lets frequent topical unigrams ("baby", "sleep")
 * crowd out the multi-word phrases and acronyms where the actual jargon lives,
 * so each n-gram class gets its own slice.
 */
export function selectTopTerms(terms) {
  const { uni, bi, acr } = config.topTerms;
  const quota = { uni, bi, acr };
  const taken = { uni: 0, bi: 0, acr: 0 };
  return terms.filter((t) => (taken[t.ngram] < quota[t.ngram] ? (taken[t.ngram]++, true) : false));
}
