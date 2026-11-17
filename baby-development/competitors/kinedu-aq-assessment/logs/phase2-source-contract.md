# Phase 2 source contract

Read-only analysis of the saved first-party bundles, 2026-11-02. No network requests or browser were used for this note. Offsets below are zero-based Unicode character offsets in the original minified source; snippets make the claims verifiable even if a reader opens a formatted copy.

Sources:

- [page-5f182d70f1f24a3d.js](../raw/js/page-5f182d70f1f24a3d.js): SHA-256 `9f8f06a76dd4c261c2a406040077939b5a42ea87ee77c38c8b5deb0514a1092c`.
- [562-f8a0c4482aa81c7b.js](../raw/js/562-f8a0c4482aa81c7b.js): SHA-256 `00391c90805fc2171c9ff2f686480a4273d76a6dbf24cc7802d4a3c4384791b9`.

## Start request and dates

Observed: all three components (default, classic, and hook) POST to `/api/assessment` with `Content-Type: application/json`. Their start bodies contain exactly `action`, `birthdate`, and `gestationalWeeks`. No language, UI variant, name, cookie header, or session field is explicitly added to this request body. Native same-origin fetch can of course send ambient browser cookies; the saved code alone does not establish whether the API requires any.

Default component ([page bundle](../raw/js/page-5f182d70f1f24a3d.js)):

Zero-based character offset `6838`:

```javascript
fetch("/api/assessment",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({action:"start",birthdate:S,gestationalWeeks:F?E:null})}),l=await s.json();if(422===s.status&&(null==l?void 0:l.error
```

Classic component ([page bundle](../raw/js/page-5f182d70f1f24a3d.js)):

Zero-based character offset `58478`:

```javascript
action:"start",birthdate:$,gestationalWeeks:X?ee:null})}),a=await t.json();if(422===t.status&&(null=
```

Hook component ([shared bundle](../raw/js/562-f8a0c4482aa81c7b.js)):

Zero-based character offset `33226`:

```javascript
action:"start",birthdate:et,gestationalWeeks:ei?ed:null})}),o=await a.json();if(422===a.status&&(nul
```

Observed: the default component uses `input type="date"` and sends its value unchanged. Classic explicitly concatenates year, zero-padded month (zero-based month plus one), and zero-padded day. This establishes the `YYYY-MM-DD` request format. The preterm checkbox controls whether a numeric gestational week value or `null` is sent.

Zero-based character offset `11751`:

```javascript
type:"date",value:S,max:e,onChange:e=>D(e.target.value),className:"mt-1 w-full rounded-xl border bg-white px-4 py-3 text-[16px]",style:{borderColor:d.line}
```
Zero-based character offset `57270`:

```javascript
$=""!==A&&""!==P&&""!==G?"".concat(G,"-").concat(String(Number(A)+1).padStart(2,"0"),"-").concat(String(P).padStart(2,"0")):"",[X,Z]=(0,l.useState)(!1),[ee,et]=(0,l.useState)(34),[ea,es]=(0,l.useState)(nul
```

Observed: the classic date picker disables future dates. Consequently the requested day-15 sweep sample for nominal age zero on 2026-11-02 is 2026-11-15, which is future and cannot be chosen in the UI. Preserve any such probe, but use an actual newborn DOB to establish age-zero behavior. This observation does not predict whether the server will reject the future date.

Zero-based character offset `52848`:

```javascript
b=e=>new Date(d,u,e)>i,g=e=>""!==a&&Number(a)===d&&Number(n)===u&&Number(r)===e,
```

## Response contract and question order

Observed: start success reads `ageMonths`, `corrected`, `sections`, and optional `calibration` (default `[]`). The 422 branch requires both status 422 and JSON `error === "age_range"`; the default component also reads `ageMonths` in this failure case.

Zero-based character offset `7016`:

```javascript
if(422===s.status&&(null==l?void 0:l.error)==="age_range"){n({s:"age_range",months:null!==(t=l.ageMonths)&&void 0!==t?t:49});return}if(!s.ok){ea("Please check the birthdate.");return}T(l.ageMonths),z(l.corrected),O(l.sections),U(null!==(a=l.calibration)&&void 0!==a?a:[]),e("quiz_started","child"),n({s:"area",idx:0,q:0})}catch(e){ea("Connection hiccup — try again.")}finally{ee(!1)}},ei=async t=>{ee(!0);try{var a;let s=await fetch("/api/assessment",{method:"POST",headers:{
```

Observed: preserve API section order. For each section at index i, the rendered order is the optional `anchor`, all `items` in returned order, then `calibration[i]` if i is in bounds. Calibration is interleaved by section index rather than appended once at the end. The calibration association is positional in this code. A calibration array longer than the sections array would leave its tail undisplayed by this construction.

Zero-based character offset `6654`:

```javascript
er=(0,l.useMemo)(()=>L.map((e,t)=>{let a=[];return e.anchor&&a.push(e.anchor),a.push(...e.items),t<B.length&&a.push(B[t]),a}),[L,B]),eo=async()=>{ee(!0),ea("");try{var t,a;let s=awai
```
Zero-based character offset `58187`:

```javascript
eT=(0,l.useMemo)(()=>er.map((e,t)=>{let a=[];return e.anchor&&a.push(e.anchor),a.push(...e.items),t<ei.length&&a.push(ei[t]),a}),[er,ei]),eM=async()=>{eD(!0),eA("");try{var e;let t=await 
```

Observed: classic uses `section.area` as its section heading and looks up presentation colors/images by that value. Do not assume a separate `section.id` exists unless the live API supplies it. Per-question rendered text falls back to `question.title`; question answers are stored by `question.id`. CSV `kind` should be derived from the location in `anchor`, `items`, or `calibration` if the API does not return such a field.

Zero-based character offset `67179`:

```javascript
m=l?"":null!==(a=null===(e=er[r])||void 0===e?void 0:e.area)&&void 0!==a?a:"",h=l?C.brand:null!==(n=w[m])&&void 0!==n?n:C.brand,g=l?"/aq-classic/kined
```
Zero-based character offset `72729`:

```javascript
em.current.set(e.id,0),_(e=>e+1)},className:"rounded-full border-[1.5p
```
Zero-based character offset `73128`:

```javascript
em.current.set(e.id,1),_(e=>e+1)},className:"rounded-full border-[1.5p
```

Inference: the initial list has no client-side answer-dependent filtering in the observed construction. This does not rule out API selection by age or an additional result-driven extension. Ordered ID lists, rather than unordered sets, match what the client displays.

## Language handling

Observed: classic selects locale from the URL `lang`, accepting prefixes `es` and `pt`, otherwise defaulting to `en`. Question translations are client-side lookups keyed by `String(question.id)` in modules 5668 (Spanish) and 7578 (Portuguese); missing translations fall back to the API `title`. Section area titles have a separate local translation map. The default component renders English directly; the hook component also uses local translation dictionaries.

Zero-based character offset `31167`:

```javascript
var v=a(5668),j=a(7578);a(8487),a(1121);
```
Zero-based character offset `31797`:

```javascript
function D(){try{let e=(new URLSearchParams(location.search).get("lang")||"").toLowerCase();if(e.startsWith("es"))return"es";if(e.startsWith("pt"))return"pt"}catch(e){}return"en"}function F(e,t){var a,s;return"es"===t?null!==(a=v[String(e.id)])&&void 0!==a?a:e.title:"pt"===t&&null!==(s=j[String(e.id)])&&void 0!==s?s:e.title}let A={en:{Physical:"Physical"
```
Zero-based character offset `32123`:

```javascript
let A={en:{Physical:"Physical",Cognitive:"Cognitive",Language:"Language","Social-Emotional":"Social-Emotional"},es:{Physical:"F\xedsica",Cognitive:"Cognitiva",Language:"Lenguaje","Social-Emotional":"Socioemocional"},pt:{Physical:"F\xedsica",Cognitive:"Cognitiva",Language:"Linguagem","Social-Emotional":"Socioemocional"}},E=function(e,t){var a;let s=arguments.length>2&&void 0!==arguments[2]&&arguments[2],l=null!==(a=A[t][e])&&void 0!==a?a:e;return s&&"Social-Emotional"===e?"en"===t?"Social-Emot.":"Socioemoc.":l},q={en:{hero_h1:"See what your baby is building right n
```

The saved [shared bundle](../raw/js/562-f8a0c4482aa81c7b.js) exports exactly **408** Spanish and **408** Portuguese question entries from modules 5668 and 7578. Their ID sets are identical, spanning numeric IDs 1 through 1152 with gaps. Module starts are at offsets `75689` and `100710`. These dictionaries provide an independent static inventory for comparison with the API bank; presence in a dictionary does not prove an ID is reachable from the observed endpoint or ages.

Inference for the requested language step: skip invented language parameters to `/api/assessment`. The captured client contract has no such field and localizes displayed questions client-side. This is evidence about this client, not proof that the server would reject every unobserved language parameter.

## Extension and completeness caveat

Observed: `result` requests contain `action:"result"`, API `ageMonths`, `extended`, and `answers:[{id,y}, ...]`. Answers seen in the UI are numeric zero and one. When a result response has `stage:"extension"` and the request was not already extended, the client stores response `items` and moves to an extension screen. The extension list is rendered separately from start sections. This branch exists in default, classic, and hook components.

Zero-based character offset `7547`:

```javascript
action:"result",ageMonths:P,extended:t,answers:[...R.current.entries()].map(e=>{let[t,a]=e;return{id:t,y:a}})})}),l=await s.json();if("extension"===l.stage&&!t){K(l.items),e("extension_started","extension"),n({s:"extension",q:0});return}I(l.basic),V(null!==(a=l.skills)&&void 0!==a?a:[]),e("funnel_completed","celebrate"),n({s:"celebrate"})}catch(e){
```
Zero-based character offset `59182`:

```javascript
if("extension"===r.stage&&!e){eu(r.items),b("extension_started","extension"),f({s:"extension",q:0});return}ep(r.basic),eb(null!==(t=r.detail)&&void 0!==t?t:null),ey(null!==(a=r.skills)&&void 0!==a?a:[]),e_(null!==(s=r.activity)&&void 0!==s?s:null),ej(null!==(l=r.floorActivities)&&void 0!==l?l:[]),b("funnel_completed","celebrate"
```
Zero-based character offset `67138`:

```javascript
u=l?ec:null!==(t=eT[r])&&void 0!==t?t:[],m=l?"":null!==(a=null===(e=er[r])||void 0===e?void 0:e.area)&&void 0!==a?a:"",h=l?C.brand:null!==(n=w[m])&&void 0!==n?n:C.brand,g=l?"/aq-classic/kinedu.png":k[m],j=u.fil
```

Observed: the classic/hook completion path additionally reads `basic`, `detail`, `skills`, `activity`, and `floorActivities`. Default completion reads `basic` and `skills`; its 800 ms debounced result request uses `extended:true` and accepts `stage:"complete"`. The source does not disclose the server's rules for when an extension is selected, which questions it contains, or how scores are computed.

Zero-based character offset `59289`:

```javascript
ep(r.basic),eb(null!==(t=r.detail)&&void 0!==t?t:null),ey(null!==(a=r.skills)&&void 0!==a?a:[]),e_(null!==(s=r.activity)&&void 0!==s?s:null),ej(null!==(l=r.floorActivities)&&void 0!==l?l:[]),b("funnel_completed","celebrate"),f({s:"celebrate"})}catch(e){eA(T(p,"conn_error"))}finally{eD(!1)}};if("hero"===y.s)return(0,s.jsxs)(W,{children:[(0,s.jsx)(K,{}),(0,s.j
```
Zero-based character offset `8163`:

```javascript
action:"result",ageMonths:P,extended:!0,answers:[...R.current.entries()].map(e=>{let[t,a]=e;return{id:t,y:a}})})}),a=await t.json();if("complete"===a.stage){var e;I(a.basic),V(null!==(e=a.skills)&&void 0!==e?e:[])}}catch(e){}},800)},[P]),ec=(e,t,a)=>{R.current.set(e.id,t),a()};if("hero"===a.s)return(0,s.jsxs)(h,{children:[(0,s.j
```

Inference: enumerating every start age proves the observed initial question bank and age-to-initial-list mapping. It alone cannot prove that every possible question used by the complete assessment has been recovered. Additional result probes can measure observed extension items, but a finite collection of answer patterns should not be described as an exhaustive proof over all answer combinations unless the API behavior independently supports that conclusion.

## Corrected age and range copy are not server formulas

Observed: the client says correction is used “until age 2” and says the assessment is built for ages 0 to 48 months. These are copy strings, not a server implementation of the correction formula or range check. Derive both from raw live responses and distinguish the returned age from the nominal month-subtraction sweep label.

Zero-based character offset `34285`:

```javascript
aap_note:"We’ll use their corrected age, as the American Academy of Pediatrics recommends, until age 2 — and we’ll say so.",check_date:"Please check the birthdate.",conn_error:"Connection hiccup — try
```
Zero-based character offset `34588`:

```javascript
over48_body:"This assessment is built and validated for ages 0 to 48 months, so we can’t give {name} a fair reading here. Kinedu still has activity plans and expert content for the whole family.",over48_cta:"Explore Kinedu →",assessment_for:"Ass
```
