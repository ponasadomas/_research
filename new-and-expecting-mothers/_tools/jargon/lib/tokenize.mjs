// Tokenization for the jargon analysis. Two streams per document:
//  - lowercased tokens for the unigram/bigram passes
//  - case-preserved tokens for the acronym pass (LO, DH, AIBU...)

const STOPWORDS = new Set(`a about above after again against all am an and any are aren't as at be because been
before being below between both but by can can't cannot could couldn't did didn't do does doesn't doing don't
down during each few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here
here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's
me more most mustn't my myself no nor not of off on once only or other ought our ours ourselves out over own
same shan't she she'd she'll she's should shouldn't so some such than that that's the their theirs them
themselves then there there's these they they'd they'll they're they've this those through to too under until
up very was wasn't we we'd we'll we're we've were weren't what what's when when's where where's which while
who who's whom why why's with won't would wouldn't you you'd you'll you're you've your yours yourself
yourselves also just really like get got one even go going still much well know think see way lot bit thing
things something anything everything someone anyone people time day now back always never actually maybe
probably definitely honestly literally though yeah yes okay ok right sure want wanted need needed make made
making take took getting said say says tell told feel felt look looked come came around every im ive dont
didnt cant wont youre theyre isnt wasnt id ill thats hes shes whats us new first last long good great better
best bad little big many two three able try trying tried keep kept put use used etc`.split(/\s+/));

// Bot/automod boilerplate. Arctic Shift responses don't carry the author field, so
// bots are identified by their signature text rather than by username.
const BOT_TEXT = /this action was performed automatically|i am a bot|^welcome to r\/|has been removed because|please contact the moderators of this subreddit/i;

export const isBotText = (raw) => BOT_TEXT.test(raw ?? '');

/** Clean raw post/comment text: strip markdown, URLs, quoted lines, entities. */
export function cleanText(raw) {
  return (raw ?? '')
    .replace(/^&gt;.*$|^>.*$/gm, ' ')            // quoted lines (avoid double-counting)
    .replace(/&(amp|lt|gt|quot|#39|nbsp);/g, (m) => ({ '&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"', '&#39;': "'", '&nbsp;': ' ' }[m]))
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')     // markdown links -> anchor text
    .replace(/https?:\/\/\S+/g, ' ')
    .replace(/[*_~^`|\\]/g, ' ')                 // markdown decoration
    .replace(/[‘’]/g, "'")
    .replace(/\s+/g, ' ')
    .trim();
}

// Letters plus optional internal apostrophes/hyphens/digits: don't, co-sleeping, 4mo, 18mo.
const TOKEN_RE = /[a-z0-9](?:[a-z0-9'-]*[a-z0-9])?/gi;
const HAS_LETTER_RE = /[a-z]/i;

/** Case-preserved token stream (for the acronym pass). */
export function tokens(text) {
  return (text.match(TOKEN_RE) ?? []).filter((t) => HAS_LETTER_RE.test(t));
}

/** Lowercased token stream (for n-gram passes). */
export function tokensLower(text) {
  return tokens(text).map((t) => t.toLowerCase());
}

// Bigrams use a much narrower filter: only true function words. The unigram list above
// drops generic content nouns ("time", "day", "night"), which is right on their own but
// destroys real phrasal jargon — "tummy time", "screen time", "wake window".
// Verb particles (out/up/down/off/over) are deliberately NOT listed: they carry the
// meaning in "touched out", "spit up", "blow out", "melt down". Their noisy combinations
// ("out of", "up to") are already killed by the other half of the pair being a function word.
const FUNCTION_WORDS = new Set(`a about above after again against all am an and any are aren't as at be
because been before being below between both but by can can't cannot could couldn't did didn't do does
doesn't doing don't during each few for from further had hadn't has hasn't have haven't having he he'd
he'll he's her here here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it
it's its itself let's me more most mustn't my myself no nor not of on once only or other ought our ours
ourselves own same shan't she she'd she'll she's should shouldn't so some such than that that's the
their theirs them themselves then there there's these they they'd they'll they're they've this those through
to too under until very was wasn't we we'd we'll we're we've were weren't what what's when when's where
where's which while who who's whom why why's with won't would wouldn't you you'd you'll you're you've your
yours yourself yourselves im ive dont didnt cant wont youre theyre isnt wasnt id ill thats hes shes whats
just really like get got even go going still much well also us`.split(/\s+/));

export const isStopword = (t) => STOPWORDS.has(t);

/** Unigrams: lowercased, stopwords excluded. */
export function unigrams(toks) {
  return toks.filter((t) => !STOPWORDS.has(t) && t.length > 1);
}

// Particles only ever trail their verb in English ("spit up", "touched out"), so allowing
// them in first position just harvests sentence noise ("up around", "over weeks").
const PARTICLES = new Set(['out', 'up', 'down', 'off', 'over']);

/** Bigrams over the FULL stream (real adjacency), then drop any containing a function word. */
export function bigrams(toks) {
  const out = [];
  for (let i = 0; i < toks.length - 1; i++) {
    const a = toks[i], b = toks[i + 1];
    if (FUNCTION_WORDS.has(a) || FUNCTION_WORDS.has(b)) continue;
    if (PARTICLES.has(a)) continue;
    if (a.length > 1 && b.length > 1) out.push(`${a} ${b}`);
  }
  return out;
}

const ACRONYM_RE = /^[A-Z]{2,6}s?$/;

// Ordinary words people write in caps for emphasis — not acronyms.
const SHOUTY = new Set(`NOT AND THE ALL ARE WAS HIS HER SHE HIM YOU ANY THIS THAT VERY NEVER EVER WHY HOW
WHAT WHEN ONE TWO DAY ONLY JUST REALLY STOP PLEASE LOVE HATE NEED WANT WILL CAN CANT DONT EVERY SAME NOW
HAD HAS HAVE DID DOES DO SO NO YES BUT FOR OUT GET GOT MORE MUCH BOTH THEY THEM WITH LOT TOO ALWAYS THEN
THERE HERE MUST MY ME WE IS IT BE ANYTHING EVERYTHING NOTHING SOME YOUR OUR THEIR WERE BEEN AM MOM DAD
BABY KNOW THINK SAID SAYS TELL TOLD ASK ASKED GO GOING WENT COME BACK OFF ON IN AT BY UP OF TO`.split(/\s+/));

/** Acronym tokens from the case-preserved stream, normalized to singular uppercase. */
export function acronyms(caseTokens) {
  return caseTokens
    .filter((t) => ACRONYM_RE.test(t))
    .map((t) => t.replace(/s$/, ''))
    .filter((t) => !SHOUTY.has(t));
}
