import * as cheerio from 'cheerio';

// Mumsnet talk URLs look like /talk/<board>/<id>-<slug> (threads) and /talk/<board>
// with pagination for board indexes.

export const isThreadUrl = (url) => /\/talk\/[^/]+\/\d+-/.test(url);

export const boardFromUrl = (url) => url.match(/\/talk\/([^/]+)/)?.[1] ?? 'unknown';

export function looksBlocked(html) {
  return /just a moment|cf-challenge|challenge-platform|attention required/i.test(html.slice(0, 4000));
}

/** Thread URLs from a board index page. Pattern-based, resilient to class churn. */
export function parseBoardIndex(html, board) {
  const $ = cheerio.load(html);
  const urls = new Set();
  $('a[href]').each((_, el) => {
    const href = $(el).attr('href');
    const m = href?.match(new RegExp(`^(?:https://www\\.mumsnet\\.com)?(/talk/${board}/\\d+-[^?#]+)`));
    if (m) urls.add(`https://www.mumsnet.com${m[1]}`);
  });
  return [...urls];
}

/** Post bodies from a thread page. Primary selector pinned against live HTML 2026-07;
 *  older layouts kept as fallbacks in case of markup churn. */
export function parseThreadPage(html) {
  const $ = cheerio.load(html);
  const candidates = ['.post-body', 'div.talk-post div.mn-message', 'div[class*="talk-post"] p', '.message'];
  for (const sel of candidates) {
    const posts = $(sel)
      .map((_, el) => $(el).text().trim())
      .get()
      .filter((t) => t.length > 10);
    if (posts.length >= 1) return posts;
  }
  return [];
}

/** {term, meaning} pairs from the official acronym-list page.
 *  Current markup (2026): <h3>TERM</h3><p>meaning</p>; table/<strong> layouts kept as fallbacks. */
export function parseGlossary(html) {
  const $ = cheerio.load(html);

  const fromHeadings = $('h3')
    .map((_, h) => {
      const term = $(h).text().trim();
      if (!/^[A-Za-z]{2,10}$/.test(term)) return null;
      const meaning = $(h).next('p').text().trim();
      return meaning ? { term: term.toUpperCase(), meaning } : null;
    })
    .get()
    .filter(Boolean);
  if (fromHeadings.length > 50) return fromHeadings;

  const fromTables = $('table tr')
    .map((_, tr) => {
      const cells = $(tr).find('td, th').map((_, td) => $(td).text().trim()).get();
      return cells.length >= 2 && /^[A-Za-z]{2,10}$/.test(cells[0]) && cells[1]
        ? { term: cells[0].toUpperCase(), meaning: cells[1] }
        : null;
    })
    .get()
    .filter(Boolean);
  if (fromTables.length > 50) return fromTables;

  const fromStrong = $('p, li')
    .map((_, el) => {
      const bold = $(el).find('strong, b').first().text().trim();
      if (!/^[A-Za-z]{2,10}$/.test(bold)) return null;
      const meaning = $(el).text().replace(bold, '').replace(/^[\s:–—-]+/, '').trim();
      return meaning ? { term: bold.toUpperCase(), meaning } : null;
    })
    .get()
    .filter(Boolean);
  if (fromStrong.length > 50) return fromStrong;

  return fromTables.length >= fromStrong.length ? fromTables : fromStrong;
}
