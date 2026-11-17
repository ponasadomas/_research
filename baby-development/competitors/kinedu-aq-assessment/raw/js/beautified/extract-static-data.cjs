// Static data only: evaluates isolated object/string literals, never application modules.
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const base = __dirname;
const pageName = 'page-5f182d70f1f24a3d.js';
const sharedName = '562-f8a0c4482aa81c7b.js';
const page = fs.readFileSync(path.join(base, pageName), 'utf8');
const shared = fs.readFileSync(path.join(base, sharedName), 'utf8');
function objectAt(source, marker) {
  let start = source.indexOf(marker);
  if (start < 0) throw new Error(marker);
  start = source.indexOf('{', start + marker.length);
  let depth = 0, quote = '';
  for (let end = start; end < source.length; end++) {
    const c = source[end];
    if (quote) { if (c === '\\') end++; else if (c === quote) quote = ''; continue; }
    if (c === '"' || c === "'") { quote = c; continue; }
    if (c === '{') depth++;
    if (c === '}' && --depth === 0) return vm.runInNewContext('(' + source.slice(start, end + 1) + ')', Object.create(null), {timeout:1000});
  }
  throw new Error('unbalanced literal');
}
const jsonLines = shared.split('\n').flatMap((line, index) => {
  const m = line.match(/e\.exports = JSON\.parse\((.*)\)$/);
  return m ? [{line:index + 1, value:JSON.parse(vm.runInNewContext(m[1], Object.create(null), {timeout:1000}))}] : [];
});
if (jsonLines.length !== 3) throw new Error('expected FB, es and pt data');
const data = {
  areas: objectAt(page, 'let A ='),
  classicCopy: objectAt(page, 'q ='),
  hookCopy: objectAt(shared, '_ ='),
  feedback: jsonLines[0].value.FB,
  esQuestions: jsonLines[1].value,
  ptQuestions: jsonLines[2].value,
  sourceLines: jsonLines.map(e => e.line)
};
for (const [key,value] of Object.entries(data)) {
  fs.writeFileSync(path.join(base, key + '.json'), JSON.stringify(value, null, 2) + '\n');
}
console.log(JSON.stringify({questionCounts:{es:Object.keys(data.esQuestions).length,pt:Object.keys(data.ptQuestions).length},sameIds:JSON.stringify(Object.keys(data.esQuestions)) === JSON.stringify(Object.keys(data.ptQuestions)),classicKeys:Object.keys(data.classicCopy.en).length,hookKeys:Object.keys(data.hookCopy.en).length,sourceLines:data.sourceLines},null,2));
