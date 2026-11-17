// Reddit data via the Arctic Shift API (arctic-shift.photon-reddit.com).
// Direct reddit.com/*.json access 403s from this network, and Arctic Shift is both
// faster (no thread-by-thread fetching) and kinder: bulk posts/comments per date window.
// No score sort/filter server-side, so we sample the whole period and rank locally.

import { cachedFetchJson } from './http.mjs';
import config from '../config.mjs';

const API = 'https://arctic-shift.photon-reddit.com/api';
const POST_FIELDS = 'id,title,selftext,score,created_utc,subreddit';
const COMMENT_FIELDS = 'id,body,score,created_utc,subreddit,link_id';
const FETCH_OPTS = { kind: 'reddit', delayMs: config.arcticDelayMs };

/** Weekly [after, before) ISO-date windows covering config.corpusDateRange (fixed dates → stable cache URLs). */
export function dateWindows(yearsBack = 1) {
  const end = new Date(config.corpusDateRange.end + 'T00:00:00Z');
  const start = new Date(end);
  start.setUTCFullYear(end.getUTCFullYear() - yearsBack);
  const windows = [];
  for (let t = start.getTime(); t < end.getTime(); t += 7 * 86_400_000) {
    windows.push({
      after: new Date(t).toISOString().slice(0, 10),
      before: new Date(Math.min(t + 7 * 86_400_000, end.getTime())).toISOString().slice(0, 10),
    });
  }
  return windows;
}

function searchUrl(type, sub, { after, before }) {
  const fields = type === 'posts' ? POST_FIELDS : COMMENT_FIELDS;
  return `${API}/${type}/search?subreddit=${sub}&after=${after}&before=${before}&limit=auto&sort=asc&fields=${fields}`;
}

/** One auto-page (~500-600 rows) of posts or comments for a sub in a date window. */
export async function fetchWindow(type, sub, window) {
  const res = await cachedFetchJson(searchUrl(type, sub, window), FETCH_OPTS);
  return res?.data ?? [];
}

export const isSearchUrl = (url) => url.startsWith(API);
export const parseSearchUrl = (url) => {
  const m = url.match(/\/api\/(posts|comments)\/search\?subreddit=([^&]+)/);
  return m ? { type: m[1], sub: m[2] } : null;
};
