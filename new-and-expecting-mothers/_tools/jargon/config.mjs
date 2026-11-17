// All tuning knobs for the jargon-mining pipeline. Scripts read only from here.

export default {
  userAgent: 'mamivio-jargon-research/1.0 (contact: adomas.kontautas@gmail.com)',

  // --- Reddit ---
  // region: used for UK-vs-US tagging. US-heavy subs are "US-leaning", not "US" —
  // they have plenty of non-US posters, so tagging needs a strong skew (see analyze).
  parentingSubs: [
    { name: 'Mommit', region: 'US-leaning' },
    { name: 'beyondthebump', region: 'US-leaning' },
    { name: 'NewParents', region: 'US-leaning' },
    { name: 'pregnant', region: 'US-leaning' },
    { name: 'BabyBumps', region: 'US-leaning' },
    { name: 'UKParenting', region: 'UK', yearsBack: 3 }, // small sub — sample a longer period
  ],
  // yearsBack 3: only 2 baseline subs vs 6 parenting — longer period keeps the
  // baseline corpus at a comparable size (analysis warns if < 50% of parenting).
  baselineSubs: [
    { name: 'CasualConversation', yearsBack: 3 },
    { name: 'AskReddit', yearsBack: 3 },
  ],
  // Fixed sampling period (stable dates → stable cache URLs across days).
  // Weekly windows over this range; one auto-page (~500-600 rows) of posts and of
  // comments per window per sub via Arctic Shift.
  corpusDateRange: { end: '2026-07-01' },

  // --- Mumsnet ---
  mumsnet: {
    base: 'https://www.mumsnet.com',
    glossaryUrl: 'https://www.mumsnet.com/i/acronyms', // canonical as of 2026-07 (/info/acronyms redirects here)
    // regionCompare: false = general-chat board. Still mined for mum-voice vocabulary,
    // but excluded from UK-vs-US rate math — every US source is a parenting sub, so
    // comparing general chat against them turns topic differences into fake region signal.
    boards: [
      { slug: 'am_i_being_unreasonable', regionCompare: false },
      { slug: '_chat', regionCompare: false },
      { slug: 'pregnancy', regionCompare: true },
      { slug: 'parenting', regionCompare: true },
    ],
    indexPagesPerBoard: 5,
    threadsPerBoard: 120,
    pagesPerThread: 2,
  },

  // --- Fetch politeness ---
  requestDelayMs: 6500, // default (Mumsnet): slow and polite
  arcticDelayMs: 1200,  // Arctic Shift is a bulk-access API with generous limits
  requestJitterMs: 1500,

  // --- Analysis ---
  minTermCount: 10,   // min occurrences in parenting corpus
  minSourceSpread: 3, // must appear in >= N distinct subs/boards
  // Dirichlet prior strength (Monroe et al.). Must scale with corpus size: alpha_w =
  // alpha0 * b_w / B, so on a 60M-token corpus the textbook alpha0=1000 leaves terms
  // absent from the baseline with a prior weight near zero, and the 1/(y+alpha) variance
  // term then explodes — scoring perfectly corpus-exclusive jargon as insignificant.
  alpha0: 100_000,
  // Per-n-gram-class quotas for the glossary candidate set (see lib/select.mjs).
  // Bigrams get the largest slice — that's where phrasal jargon lives.
  topTerms: { uni: 200, bi: 500, acr: 80 },
  examplesPerTerm: 10,

  // UK/US tagging: >= ratioX rate skew (per 10k tokens) and >= minCount on the high side.
  // minExpectedForAbsence guards the "US" tag, which is an argument from absence in the
  // (much smaller) UK corpus — require enough expected UK occurrences to trust the silence.
  regionTag: { ratio: 3, minCount: 5, minExpectedForAbsence: 15 },

  // Working files (corpus/, out/) live in the niche's _work/jargon/. corpus/ is rebuilt
  // from the caches by `npm run corpus` and is not stored in git.
  dataDir: new URL('../../_work/jargon/', import.meta.url).pathname,
  // The saved responses are the originals, kept by kind of source.
  cacheDirs: {
    reddit: new URL('../../reddit/raw/jargon-2026-07/', import.meta.url).pathname,
    mumsnet: new URL('../../forums/raw/mumsnet-jargon-2026-07/', import.meta.url).pathname,
  },
};
