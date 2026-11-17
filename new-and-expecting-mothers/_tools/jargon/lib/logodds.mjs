// Log-odds ratio with informative Dirichlet prior (Monroe, Colaresi & Quinn 2008,
// "Fightin' Words"). Scores how distinctively a term belongs to corpus P vs corpus B.

/**
 * @param {Map<string,number>} countsP term counts in the target corpus
 * @param {Map<string,number>} countsB term counts in the baseline corpus
 * @param {number} alpha0 prior strength
 * @returns {Map<string,{z:number, delta:number, countP:number, countB:number}>}
 */
export function logOdds(countsP, countsB, alpha0) {
  const nP = sum(countsP);
  const nB = sum(countsB);

  // Background distribution over the union vocabulary
  const background = new Map();
  for (const [w, c] of countsP) background.set(w, c);
  for (const [w, c] of countsB) background.set(w, (background.get(w) ?? 0) + c);
  const B = nP + nB;

  const result = new Map();
  for (const [w, bw] of background) {
    const alphaW = (alpha0 * bw) / B;
    const yP = countsP.get(w) ?? 0;
    const yB = countsB.get(w) ?? 0;
    const delta =
      Math.log((yP + alphaW) / (nP + alpha0 - yP - alphaW)) -
      Math.log((yB + alphaW) / (nB + alpha0 - yB - alphaW));
    const variance = 1 / (yP + alphaW) + 1 / (yB + alphaW);
    result.set(w, { z: delta / Math.sqrt(variance), delta, countP: yP, countB: yB });
  }
  return result;
}

export function sum(counts) {
  let total = 0;
  for (const c of counts.values()) total += c;
  return total;
}

export function countInto(map, items) {
  for (const item of items) map.set(item, (map.get(item) ?? 0) + 1);
  return map;
}
