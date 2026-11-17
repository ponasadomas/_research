// Step 1b: fetch Mumsnet — robots.txt gate, official acronym glossary, then talk boards.
// Slow by design (default 6.5s delay + jitter). All responses disk-cached.
// Usage: node fetch-mumsnet.mjs [--boards=pregnancy] [--threads=10]

import { mkdir, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import config from './config.mjs';
import { cachedFetch } from './lib/http.mjs';
import { parseBoardIndex, parseThreadPage, parseGlossary, looksBlocked } from './lib/mumsnet.mjs';

const args = Object.fromEntries(
  process.argv.slice(2).filter((a) => a.startsWith('--')).map((a) => a.replace(/^--/, '').split('='))
);
const mn = config.mumsnet;
const allBoards = mn.boards.map((b) => b.slug);
const boards = args.boards ? args.boards.split(',') : allBoards;
const threadsPerBoard = args.threads ? Number(args.threads) : mn.threadsPerBoard;
const OPTS = { kind: 'mumsnet', headers: { 'Accept-Language': 'en-GB' } };

function guard(envelope, what) {
  if (envelope && looksBlocked(envelope.body)) {
    console.error(`Anti-bot challenge detected on ${what} — aborting rather than caching garbage.`);
    process.exit(1);
  }
  return envelope;
}

// --- robots.txt gate ---
const robots = await cachedFetch(`${mn.base}/robots.txt`, OPTS);
const generalBlock = robots?.body.match(/User-agent: \*\n(?:(?:Disallow|Allow):[^\n]*\n?)+/i)?.[0] ?? '';
if (/^Disallow: \/talk\/?\s*$/m.test(generalBlock)) {
  console.error('robots.txt disallows /talk for * — skipping board scrape (glossary only).');
  boards.length = 0;
}

// --- official acronym glossary ---
const glossaryPage = guard(await cachedFetch(mn.glossaryUrl, OPTS), 'glossary page');
if (glossaryPage) {
  const acronyms = parseGlossary(glossaryPage.body);
  const outDir = join(config.dataDir, 'out');
  await mkdir(outDir, { recursive: true });
  await writeFile(join(outDir, 'mumsnet-acronyms.json'), JSON.stringify(acronyms, null, 1));
  console.log(`Glossary: ${acronyms.length} acronym definitions saved.`);
  if (acronyms.length < 50) console.warn('⚠ suspiciously few glossary entries — markup may have changed.');
}

// --- boards ---
for (const board of boards) {
  console.log(`[${board}] fetching ${mn.indexPagesPerBoard} index pages...`);
  const threadUrls = new Set();
  for (let p = 1; p <= mn.indexPagesPerBoard; p++) {
    const url = p === 1 ? `${mn.base}/talk/${board}` : `${mn.base}/talk/${board}?page=${p}`;
    const page = guard(await cachedFetch(url, OPTS), url);
    if (!page) continue;
    for (const t of parseBoardIndex(page.body, board)) threadUrls.add(t);
  }
  const threads = [...threadUrls].slice(0, threadsPerBoard);
  console.log(`[${board}] ${threadUrls.size} threads found, fetching ${threads.length} × ${mn.pagesPerThread} pages...`);

  let posts = 0;
  const started = Date.now();
  for (const [i, threadUrl] of threads.entries()) {
    for (let p = 1; p <= mn.pagesPerThread; p++) {
      const url = p === 1 ? threadUrl : `${threadUrl}?page=${p}`;
      const page = guard(await cachedFetch(url, OPTS), url);
      if (!page) continue;
      const extracted = parseThreadPage(page.body).length;
      posts += extracted;
      if (p === 1 && extracted === 0) {
        console.warn(`  extracted 0 posts from ${url} — selectors stale?`);
        break; // don't waste a request on page 2 of an unparseable thread
      }
      if (extracted < 20) break; // short thread — no page 2
    }
    if ((i + 1) % 20 === 0 || i + 1 === threads.length) {
      const eta = Math.round(((threads.length - i - 1) * (Date.now() - started)) / (i + 1) / 60_000);
      console.log(`[${board}] ${i + 1}/${threads.length} threads, ${posts} posts (ETA ~${eta}m)`);
    }
  }
  console.log(`[${board}] done: ${posts} posts.\n`);
}

console.log('Mumsnet fetch complete.');
