// Step 1a: fetch Reddit posts + comments for all configured subreddits via Arctic Shift,
// one auto-page of each per weekly window. Disk-cached, so re-runs fast-forward.
// Usage: node fetch-reddit.mjs [--subs=Mommit,CasualConversation] [--windows=4]

import config from './config.mjs';
import { dateWindows, fetchWindow } from './lib/reddit.mjs';

const args = Object.fromEntries(
  process.argv.slice(2).filter((a) => a.startsWith('--')).map((a) => a.replace(/^--/, '').split('='))
);

const allSubs = [...config.parentingSubs, ...config.baselineSubs];
const onlySubs = args.subs ? args.subs.split(',') : null;
const subs = onlySubs ? allSubs.filter((s) => onlySubs.some((n) => n.toLowerCase() === s.name.toLowerCase())) : allSubs;
const windowCap = args.windows ? Number(args.windows) : null;

if (onlySubs && subs.length !== onlySubs.length) {
  console.error(`Unknown sub in --subs (known: ${allSubs.map((s) => s.name).join(', ')})`);
  process.exit(1);
}

for (const sub of subs) {
  let windows = dateWindows(sub.yearsBack ?? 1);
  if (windowCap) windows = windows.slice(-windowCap); // most recent N windows for smoke runs
  console.log(`[${sub.name}] ${windows.length} weekly windows...`);

  let posts = 0, comments = 0;
  const started = Date.now();
  for (const [i, w] of windows.entries()) {
    posts += (await fetchWindow('posts', sub.name, w)).length;
    comments += (await fetchWindow('comments', sub.name, w)).length;
    if ((i + 1) % 10 === 0 || i + 1 === windows.length) {
      const perWindow = (Date.now() - started) / (i + 1);
      const eta = Math.round(((windows.length - i - 1) * perWindow) / 60_000);
      console.log(`[${sub.name}] ${i + 1}/${windows.length} windows — ${posts} posts, ${comments} comments (ETA ~${eta}m)`);
    }
  }
  console.log(`[${sub.name}] done: ${posts} posts, ${comments} comments.\n`);
}

console.log('Fetch complete. Next: npm run pipeline');
