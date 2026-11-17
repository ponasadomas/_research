import { createHash } from 'node:crypto';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import config from '../config.mjs';

// Single global throttle gate: every network request (any host) waits its turn,
// so total request rate stays polite regardless of call sites.
let gate = Promise.resolve();
let lastRequestAt = 0;

function throttled(fn, delayMs = config.requestDelayMs) {
  const run = gate.then(async () => {
    const wait = lastRequestAt + delayMs + Math.random() * config.requestJitterMs - Date.now();
    if (wait > 0) await new Promise((r) => setTimeout(r, wait));
    try {
      return await fn();
    } finally {
      lastRequestAt = Date.now();
    }
  });
  gate = run.catch(() => {});
  return run;
}

const cacheDir = (kind) => config.cacheDirs?.[kind] ?? join(config.dataDir, 'cache', kind);
const cacheKey = (url) => createHash('sha1').update(url).digest('hex');

export async function readCache(kind, url) {
  try {
    const raw = await readFile(join(cacheDir(kind), cacheKey(url) + '.json'), 'utf8');
    return JSON.parse(raw);
  } catch {
    return null;
  }
}

async function writeCache(kind, url, envelope) {
  const dir = cacheDir(kind);
  await mkdir(dir, { recursive: true });
  await writeFile(join(dir, cacheKey(url) + '.json'), JSON.stringify(envelope));
}

const BACKOFFS_MS = [60_000, 120_000, 240_000];

/**
 * Fetch with disk cache, global throttle, and 429/5xx backoff.
 * Returns { url, fetchedAt, status, body } — body is the response text.
 * Only HTTP 200 responses are cached; a null return means "gave up on this URL".
 */
export async function cachedFetch(url, { kind, headers = {}, delayMs } = {}) {
  const cached = await readCache(kind, url);
  if (cached) return cached;

  const attempt = (target) =>
    throttled(() =>
      fetch(target, { headers: { 'User-Agent': config.userAgent, ...headers } }),
      delayMs
    );

  for (let i = 0; i <= BACKOFFS_MS.length; i++) {
    let res;
    try {
      res = await attempt(url);
    } catch (err) {
      console.warn(`  network error on ${url}: ${err.message}`);
      if (i < BACKOFFS_MS.length) await new Promise((r) => setTimeout(r, BACKOFFS_MS[i]));
      continue;
    }

    if (res.status === 200) {
      const body = await res.text();
      const envelope = { url, fetchedAt: new Date().toISOString(), status: 200, body };
      await writeCache(kind, url, envelope);
      return envelope;
    }

    if (res.status === 404) {
      console.warn(`  404: ${url}`);
      return null;
    }

    if (i < BACKOFFS_MS.length) {
      const retryAfter = Number(res.headers.get('retry-after')) * 1000 || BACKOFFS_MS[i];
      console.warn(`  HTTP ${res.status} on ${url} — backing off ${Math.round(retryAfter / 1000)}s`);
      await new Promise((r) => setTimeout(r, retryAfter));
    }
  }

  console.warn(`  giving up on ${url}`);
  return null;
}

export async function cachedFetchJson(url, opts) {
  const envelope = await cachedFetch(url, opts);
  if (!envelope) return null;
  try {
    return JSON.parse(envelope.body);
  } catch {
    console.warn(`  unparseable JSON from ${url}`);
    return null;
  }
}
