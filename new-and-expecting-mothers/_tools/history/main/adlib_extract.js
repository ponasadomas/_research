() => {
  const html = document.documentElement.innerHTML;
  const out = {url: location.href, captured: new Date().toISOString(), count: null, ads: []};
  const cm = html.match(/"search_results_connection":\{"count":(\d+)/);
  if (cm) out.count = +cm[1];
  const seen = new Set();
  const re = /"ad_archive_id":"(\d+)"[\s\S]{0,4000}?"page_id":"(\d+)"[\s\S]{0,3000}?"page_name":"((?:[^"\\]|\\.)*)"/g;
  let m;
  while ((m = re.exec(html)) && out.ads.length < 60) {
    if (seen.has(m[1])) continue; seen.add(m[1]);
    const seg = html.slice(m.index, m.index + 9000);
    const g = (rx) => { const x = seg.match(rx); return x ? x[1] : null; };
    out.ads.push({
      ad_archive_id: m[1], page_id: m[2], page_name: JSON.parse('"' + m[3] + '"'),
      start_date: g(/"start_date":(\d+)/), is_active: g(/"is_active":(true|false)/),
      title: g(/"title":"((?:[^"\\]|\\.){0,200})"/), link_url: g(/"link_url":"((?:[^"\\]|\\.){0,300})"/),
      body: g(/"body":\{"text":"((?:[^"\\]|\\.){0,600})"/)
    });
  }
  out.visible_text = document.body.innerText.slice(0, 3000);
  return out;
}
