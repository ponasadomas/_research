// Step 2: raw cache -> corpus JSONL. No network. Reads cached Arctic Shift search
// responses and cached Mumsnet thread pages. Emits data/corpus/parenting.jsonl and
// baseline.jsonl, one doc per post/comment.

import { mkdir, readdir, readFile } from 'node:fs/promises';
import { createWriteStream } from 'node:fs';
import { createHash } from 'node:crypto';
import { once } from 'node:events';
import { join } from 'node:path';
import config from './config.mjs';
import { parseSearchUrl } from './lib/reddit.mjs';
import { cleanText, isBotText } from './lib/tokenize.mjs';
import { parseThreadPage, isThreadUrl, boardFromUrl } from './lib/mumsnet.mjs';

const subRegion = new Map(config.parentingSubs.map((s) => [s.name.toLowerCase(), s.region]));
const baselineNames = new Set(config.baselineSubs.map((s) => s.name.toLowerCase()));
const boardRegionCompare = new Map(config.mumsnet.boards.map((b) => [b.slug, b.regionCompare]));

// Corpora are hundreds of thousands of docs — stream to disk rather than buffering
// (a single joined JSONL string would blow past V8's ~512MB string cap).
const corpusDir = join(config.dataDir, 'corpus');
await mkdir(corpusDir, { recursive: true });
const streams = {
  parenting: createWriteStream(join(corpusDir, 'parenting.jsonl')),
  baseline: createWriteStream(join(corpusDir, 'baseline.jsonl')),
};

const tokenTally = new Map(); // source label -> rough word count
const stats = { parenting: { docs: 0, words: 0 }, baseline: { docs: 0, words: 0 } };
const seenIds = new Set();    // adjacent date windows can overlap on boundary items
let botsDropped = 0;

function addDoc(which, doc) {
  if (seenIds.has(doc.id)) return;
  seenIds.add(doc.id);
  if (isBotText(doc.text)) { botsDropped++; return; }
  doc.text = cleanText(doc.text);
  if (doc.text.length < 3) return;
  const words = doc.text.split(' ').length;
  tokenTally.set(doc.sub, (tokenTally.get(doc.sub) ?? 0) + words);
  stats[which].docs++;
  stats[which].words += words;
  streams[which].write(JSON.stringify(doc) + '\n');
}

// Let full write buffers flush between cache files. Gated on writableNeedDrain rather
// than on write()'s return value: the stream may already have drained by the time we
// get here, and a 'drain' listener attached after the fact would never fire.
async function flushBackpressure() {
  const waits = Object.values(streams).filter((s) => s.writableNeedDrain).map((s) => once(s, 'drain'));
  if (waits.length) await Promise.all(waits);
}

// --- Reddit (Arctic Shift) cache ---
const redditDir = config.cacheDirs.reddit;
let redditFiles = [];
try {
  redditFiles = await readdir(redditDir);
} catch {
  console.error('No reddit cache found — run npm run fetch:reddit first.');
  process.exit(1);
}

let pages = 0;
for (const file of redditFiles) {
  const envelope = JSON.parse(await readFile(join(redditDir, file), 'utf8'));
  const parsed = parseSearchUrl(envelope.url);
  if (!parsed) continue;
  const { type, sub } = parsed;
  const region = subRegion.get(sub.toLowerCase()) ?? 'US-leaning';
  const which = baselineNames.has(sub.toLowerCase()) ? 'baseline' : 'parenting';

  let rows;
  try {
    rows = JSON.parse(envelope.body)?.data;
  } catch {
    continue;
  }
  if (!Array.isArray(rows)) continue;
  pages++;
  await flushBackpressure();

  for (const row of rows) {
    if (type === 'posts') {
      if (row.selftext === '[removed]' || row.selftext === '[deleted]') continue;
      addDoc(which, {
        id: `t3_${row.id}`, source: 'reddit', sub, type: 'post', region, regionCompare: true,
        score: row.score ?? 0,
        url: `https://www.reddit.com/r/${sub}/comments/${row.id}/`,
        text: `${row.title ?? ''} ${row.selftext ?? ''}`,
      });
    } else {
      if (!row.body || row.body === '[removed]' || row.body === '[deleted]') continue;
      const threadId = (row.link_id ?? '').replace(/^t3_/, '');
      addDoc(which, {
        id: `t1_${row.id}`, source: 'reddit', sub, type: 'comment', region, regionCompare: true,
        score: row.score ?? 0,
        url: `https://www.reddit.com/r/${sub}/comments/${threadId}/comment/${row.id}/`,
        text: row.body,
      });
    }
  }
}
console.log(`Reddit: ${pages} cached search pages processed.`);

// --- Mumsnet cache (optional — may not exist yet) ---
const mumsnetDir = config.cacheDirs.mumsnet;
let mumsnetFiles = [];
try {
  mumsnetFiles = await readdir(mumsnetDir);
} catch { /* not fetched yet — fine */ }

let mnPosts = 0;
for (const file of mumsnetFiles) {
  const envelope = JSON.parse(await readFile(join(mumsnetDir, file), 'utf8'));
  if (!isThreadUrl(envelope.url)) continue;
  const board = boardFromUrl(envelope.url);
  await flushBackpressure();
  for (const p of parseThreadPage(envelope.body)) {
    mnPosts++;
    // Content-hashed id: a short thread's "?page=2" can echo page 1, and Mumsnet posts
    // carry no stable id in the markup, so identical text is the only dedup handle.
    const id = `mn_${board}_${createHash('sha1').update(p).digest('hex').slice(0, 16)}`;
    addDoc('parenting', {
      id, source: 'mumsnet', sub: `mumsnet/${board}`, type: 'post',
      region: 'UK', regionCompare: boardRegionCompare.get(board) ?? false,
      score: 0, url: envelope.url, text: p,
    });
  }
}
if (mumsnetFiles.length) console.log(`Mumsnet: ${mnPosts} posts from ${mumsnetFiles.length} cached pages.`);

// --- Close streams + sanity report ---
for (const s of Object.values(streams)) {
  s.end();
  await once(s, 'finish');
}

console.log('\nWords per source (approx):');
const sorted = [...tokenTally.entries()].sort((a, b) => b[1] - a[1]);
for (const [sub, n] of sorted) {
  const flag = n < 100_000 ? '  ⚠ under 100k' : '';
  console.log(`  ${sub.padEnd(28)} ${String(n).padStart(9)}${flag}`);
}
console.log(`\n${botsDropped} bot/automod docs dropped.`);
console.log(`parenting: ${stats.parenting.docs} docs / ~${stats.parenting.words} words`);
console.log(`baseline:  ${stats.baseline.docs} docs / ~${stats.baseline.words} words`);
// What matters for the log-odds prior is the baseline's absolute size (can it estimate
// general-Reddit word rates?), not parity with the parenting corpus — AskReddit posts are
// short titles, so it trails on word count while still being a large sample.
if (stats.baseline.words < 5_000_000 || stats.baseline.words < stats.parenting.words * 0.25) {
  console.log('⚠ baseline corpus is thin — consider more baseline subs or a longer date range.');
}
