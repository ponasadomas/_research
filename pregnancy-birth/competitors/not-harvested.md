# Competitor sites not harvested — pregnancy-birth (2026-10-25)

robots.txt was fetched first for every domain (`scratchpad/mkt-preg/robots/`). No captcha, bot-wall or login workaround was attempted. Statuses are what `curl` with a browser User-Agent received on 2026-10-25.

| site | what it sells | status | why not harvested |
|---|---|---|---|
| kghypnobirthing.com | KG Hypnobirthing courses (UK) | robots 200: `Disallow: /` for ClaudeBot, anthropic-ai, GPTBot, CCBot, Claude-Web | AI-crawler ban respected |
| www.thebloommethod.com | Bloom Method main site | robots 200: `Disallow: /` for ClaudeBot, Claude-User, GPTBot, ChatGPT-User, CCBot | AI-crawler ban respected; shop.thebloommethod.com (robots allows) used instead, see `competitors/bloom-method.md` |
| stan.store | Stan Store creator storefronts | robots 200: `Disallow: /` for GPTBot | AI-crawler ban respected; no Stan Store pregnancy storefronts fetched |
| hypnobabies.com | Hypnobabies home-study course | 403 (bot wall on robots.txt and site) | blocked |
| labornursemama.com | Labor Nurse Mama marketing site | 403 | blocked; course host learn.labornursemama.com allowed and used |
| birthbootcamp.com | Birth Boot Camp online classes | 403 | blocked |
| classes.mother.ly | Motherly Birth Class | 403 | blocked |
| www.pullingcurls.com | Online Prenatal Class for Couples; Hypnobabies affiliate | 403 | blocked |
| bundlebirthnurses.com | Bundle Birth Nurses childbirth class | 403 | blocked |
| evidencebasedbirth.com | Evidence Based Birth classes | 403 | blocked |
| www.etsy.com | pregnancy planner / week-by-week printable listings (2 listings tried: /listing/1657566027, /listing/4476741281) | 403 (8-word block page) | blocked; robots allows listings but the site refuses the request |
| payhip.com | pregnancy planner printables (/b/Ekfoy, /b/LPFGy) | 403 "Just a moment..." (Cloudflare challenge) | blocked |
| elearn.lamaze.org | Lamaze course catalogue (old host) | curl 000 (no response) | unreachable; learn.lamaze.org used |
| get.pampers.com | Pampers free childbirth video series | curl 000 | unreachable |
| thehaywirehoney.gumroad.com/l/pregnancy-planner | Gumroad pregnancy planner | 404 | listing gone |
| hypnobirthingguide.gumroad.com, adelbook.gumroad.com | Gumroad hypnobirthing / pregnancy PDFs | 200 but 0 words (JavaScript) | JS shell; raw kept; tiny sellers (one shows "price":9.99 in page data), not torn down |
| birthfit.mykajabi.com/sales-page-1 | BIRTHFIT consumer program | 404 | page gone |
| the-calm-birth-school.teachable.com (store), mommysbundle.teachable.com (Postpartum Again), studiobloom.thebloommethod.com | course stores | 200 but products rendered by JavaScript | prices not in HTML: needs a browser walk |
