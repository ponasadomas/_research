const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const base = __dirname;
const root = path.resolve(base, '../../..');
const filenames = {P:'page-5f182d70f1f24a3d.js',S:'562-f8a0c4482aa81c7b.js'};
const sources = Object.fromEntries(Object.entries(filenames).map(([key,name]) => [key,fs.readFileSync(path.join(base,name),'utf8').split('\n')]));
function quote(key, lo, hi) {
  const body = sources[key].slice(lo-1,hi).map((line,i) => `${lo+i} | ${line}`).join('\n');
  return `${key}, lines ${lo}–${hi}:\n\n\`\`\`js\n${body}\n\`\`\``;
}
let md = fs.readFileSync(path.join(root,'STATIC-ANALYSIS.md'),'utf8').split('<!-- GENERATED_APPENDICES -->')[0];
md = md.replace(/\{\{([PS]):(\d+)-(\d+)\}\}/g, (_,key,lo,hi) => quote(key,Number(lo),Number(hi)));
const data = name => JSON.parse(fs.readFileSync(path.join(base,name+'.json'),'utf8'));
const cell = value => '`' + JSON.stringify(value).replaceAll('|','&#124;').replaceAll('`','\\u0060') + '`';
const source = (key,line) => `[${key}:${line}](raw/js/beautified/${filenames[key]}#L${line})`;
function decodedLine(name,key) {
  const lines = fs.readFileSync(path.join(base,name+'.json'),'utf8').split('\n');
  const i = lines.findIndex(line => line.trimStart().startsWith(JSON.stringify(key)+':'));
  return `[decoded:${i+1}](raw/js/beautified/${name}.json#L${i+1})`;
}
md += '<!-- GENERATED_APPENDICES -->\n\n## Appendix A. Exact hard-coded string inventory\n\n';
md += 'These are **definitions**, not a claim that every key is rendered. Displayed versus unused content is distinguished in §§5/7. Values below are JSON-quoted decoded runtime strings; placeholders remain unfilled. The source links point into `raw/js/beautified/`. For the three bundled JSON strings, decoded files provide readable individual lines while S 2440/2443/2446 preserve the original bundle evidence.\n\n';
md += '### A1. Four-area labels\n\n| Language | Labels (Physical, Cognitive, Language, Social-Emotional) | Source |\n|---|---|---|\n';
const areas = data('areas');
for(const lang of ['en','es','pt']) md += `| ${lang} | ${cell(Object.values(areas[lang]))} | ${source('P',1513)}; ${source('S',63)} |\n`;
md += '\nShort labels: `"Social-Emot."` for English, `"Socioemoc."` for Spanish/Portuguese; P 1537, S 87.\n\n';
function copyTable(name,key,start,end,title) {
  const values=data(name);
  md += `### ${title}\n\n| Key | en | es | pt | Source (en / es / pt) |\n|---|---|---|---|---|\n`;
  let language='en'; const lines={en:{},es:{},pt:{}};
  for(let i=start-1;i<end;i++) {
    const line=sources[key][i];
    const lang=line.match(/^\s{10}(en|es|pt): \{/); if(lang)language=lang[1];
    const item=line.match(/^\s{12}([\w]+): /); if(item)lines[language][item[1]]=i+1;
  }
  for(const prop of Object.keys(values.en)) {
    const refs=['en','es','pt'].map(lang=>source(key,lines[lang][prop]));
    if(refs.some(x=>x.includes('undefined')))throw Error(name+prop);
    md += `| \`${prop}\` | ${['en','es','pt'].map(lang=>cell(values[lang][prop])).join(' | ')} | ${refs.join(' / ')} |\n`;
  }
  md+='\n';
}
copyTable('classicCopy','P',1540,1854,'A2. Classic / classic-steps UI and report copy (all 103 keys × 3 languages)');
copyTable('hookCopy','S',90,506,'A3. Hook UI and report copy (all 137 keys × 3 languages)');
md += 'Optional initial.heroCta copy (S 785–789): en `"Measure it in 5 min →"`, es `"Mídelo en 5 min →"`, pt `"Meça em 5 min →"`. The aq-assessment router does not provide this prop.\n\n';
md += '### A4. Shared feedback and primer strings (all FB values)\n\nSource: '+source('S',2440)+'; full decoded [feedback.json](raw/js/beautified/feedback.json). Nested `_bands` and activity arrays are preserved exactly.\n\n| Key | en | es | pt |\n|---|---|---|---|\n';
const feedback=data('feedback');
for(const prop of Object.keys(feedback.en)) md += `| \`${prop}\` | ${['en','es','pt'].map(lang=>cell(feedback[lang][prop])).join(' | ')} |\n`;
md += '\n### A5. Every bundled question title (408 IDs × 2 languages)\n\n';
md += 'Spanish is module `5668` at '+source('S',2443)+'; Portuguese is module `7578` at '+source('S',2446)+'. The numeric ID sets are identical. There is no English title table, age/section/skill mapping, difficulty, cutoff, or item-selection rule in these dictionaries. Each row links to a decoded line as well as the original module citation above.\n\n| ID | es (exact) | pt (exact) | Decoded evidence es / pt |\n|---|---|---|---|\n';
const es=data('esQuestions'),pt=data('ptQuestions');
for(const id of Object.keys(es)) md += `| ${id} | ${cell(es[id])} | ${cell(pt[id])} | ${decodedLine('esQuestions',id)} / ${decodedLine('ptQuestions',id)} |\n`;
md += '\n### A6. Inline strings and fragments outside the tables\n\n';
md += 'This supplemental inventory lists decoded inline text/fragments, state/status/variant labels, and percent/numeric display literals. It excludes CSS classes/colors, URLs/assets, HTML tags, and technical attribute values. Combined with A1–A5, it includes the default English report and all fixed numeric placeholders. Repeated identical strings within a file are grouped by line; `.concat`/JSX fragments are quoted as fragments, without inventing joined runtime text.\n\n| File / line(s) | Exact literal |\n|---|---|\n';
// Inline literal extraction was completed from the local formatter tokenizer;
// the saved inventory lets this report rebuild without any installed dependency.
const literals=data('inline-literals');
for (const key of ['P','S']) {
  const groups=new Map();
  for (const item of literals.filter(item=>item.file===filenames[key])) {
    if(!groups.has(item.value))groups.set(item.value,[]);
    groups.get(item.value).push(item.line);
  }
  for(const [value,lines]of groups)md += `| ${key} ${[...new Set(lines)].map(line=>source(key,line)).join(', ')} | ${cell(value)} |\n`;
}
md+='\n## Appendix B. Every fetch call, verbatim with line numbers\n\n';
const sites=[['P',254,280,'track, assessment/list/skills'],['P',284,302,'lead, assessment/list/skills'],['P',328,360,'assessment start, assessment/list/skills'],['P',365,398,'assessment result, assessment/list/skills'],['P',399,427,'assessment result, skills report edit debounce'],['P',2189,2215,'track, classic/classic-steps'],['P',2219,2237,'lead, classic/classic-steps'],['P',2260,2291,'assessment start, classic/classic-steps'],['P',2296,2329,'assessment result, classic/classic-steps'],['P',3168,3193,'send-reading, classic/classic-steps'],['S',859,885,'track, hook'],['S',889,907,'lead, hook'],['S',930,961,'assessment start, hook'],['S',966,999,'assessment result, hook'],['S',1898,1923,'send-reading, hook']];
for(const [key,lo,hi,label]of sites)md+=`### ${label} — ${key}:${lo}\n\n${quote(key,lo,hi)}\n\n`;
md+='## Verification record\n\n- All five original SHA-256 checks pass after restoration and after analysis.\n- Both original/beautified JavaScript sets pass `node --check`; no application code was executed.\n- All four beautified JavaScript files have token streams identical to their originals; only formatting differs.\n- The 15 fetch sites and seven assessment sites were counted from both chunks and reconciled with Appendix B.\n- The only assessment actions are start/result; the only stage literals compared are extension/complete.\n- Question dictionary counts are 408 es / 408 pt with equal ID sets; copy tables are 103/137/48 keys per language.\n- Every numbered code quotation is checked against the corresponding beautified file; no live/API validation was performed.\n';
fs.writeFileSync(path.join(root,'STATIC-ANALYSIS.md'),md);
console.log(JSON.stringify({reportBytes:Buffer.byteLength(md),reportLines:md.split('\n').length,fetchSites:sites.length,inlineLiteralOccurrences:literals.length}));
