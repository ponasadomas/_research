# Current competitor visual comparison B

Checked 5 November 2026 using rendered browser DOM and computed styles at desktop 1440 × 1000 and mobile 390 × 844. Seven current first-party brands were measurable. The Brainy Store was attempted twice but remained blank in this browser; no palette or layout was inferred for it. Original supplied paths and redirects are recorded in the [full URL audit](COMPETITOR-AUDIT.md).

The raw measurements are in [raw-visual](raw/raw-visual). Styles were read after allowing responsive layouts to settle. Primary marketing actions were checked separately where text was nested in spans or divs; automatic selection of all links can otherwise mistake login, curriculum and footer links for the sales CTA.

## Desktop comparison

| Brand and current page | Canvas and brand colors | Main action | Heading treatment | Hero and information structure |
| --- | --- | --- | --- | --- |
| [Gentle Revolution](https://www.gentlerevolution.com/) | White, with blue `#215F8E` header/footer and link color. | Product-level blue text links; this is a store, with no single filled hero purchase button. | Montserrat sans serif; featured-products heading 52 px. | Promotion banner followed by a product grid and extensive shopping navigation. This is catalog evidence, not a single-offer funnel. |
| [Healthiest Baby ebook](https://www.healthiest-baby.com/how-to-play-with-your-baby) | White and pale blue `#F1FAFB`; ink `#161E2A`. | Turquoise `#3DDAD7`, black text, 4 px radius, 53 px tall; purchase label includes the price. | Playfair Display serif, 56 px; supporting text Poppins. | Two-column copy/photo hero, followed by benefits, audience recognition and reassurance; the same purchase action repeats. |
| [Milestones and Motherhood courses](https://milestonesandmotherhood.com/courses) | Cream `#F6F0E6`, off-white `#FBFAF7`, peach `#FDEBDA`, charcoal `#26292B`. | Several pale peach/pink stage-selection pills with dark text. These are navigation choices, not one purchase CTA. | Editors Notes serif, 66 px headline; Poppins supporting text. | Centered title on a panel over a wide home photo, followed by stage choices and separate course sections. |
| [Montessori Notebook workshop](https://courses.themontessorinotebook.com/p/montessori-for-babies-from-conception-through-the-first-year) | Full-width room photograph behind white hero text; pale grey/white content below. | Blue `#0D7BFC`, white text, 25 px radius, 52 px tall. | Palatino serif, 48 px; this page also uses serif supporting type. | Centered title, age, format, price and enrollment over the photograph; outcomes, access, curriculum and parent accounts follow. |
| [Reading Head Start](https://www.readingheadstart.com/) | White, blue `#276BAE` section headings, pale blue/green pricing accents. | Bright green `#00B54D`, white text, 10 px radius, about 55 px tall on desktop. | Roboto sans serif for content headings; main content H1 appears below the video/pricing area. | Centered video first, then three pricing options and repeated offer/guarantee sections. This is a direct-response sales funnel. |
| [The Sleep Lady](https://sleeplady.com/) | White page/navigation, sage `#89B6A5` hero, blue `#253688` later headings. | Purple `#904E99`, near-white text, 5 px radius; main consultation action about 478 × 58 px. | Roboto sans serif, bold uppercase white 57.6 px hero headline. | Centered promise and consultation action, then package/age routes, authority and supporting content. A separate embedded form was also present. |
| [BabyPillars](https://www.babypillars.com/) | Pale paper `#FDFCF9`, dark text and green accents. | Green `#54A388`, white text, pill shape, 64 px tall in the hero; secondary free tracker action. | Instrument Serif, 68 px; sans serif body and controls. | Copy-left/photo-right hero; practical benefits, method, inclusions, age bands, proof, recurring prices and questions. |

The main action colors span turquoise, peach/pink navigation, blue, green and purple. A green button appears on two of these seven brands, while one of those brands uses a blue/white sales design around it. Button color and the overall page palette must be counted separately.

Four of these seven brands use a serif main title; three use sans serif content headings. Combined figures belong in the cross-audit synthesis, rather than treating this subset as the entire supplied sample.

## Mobile ordering and action position

Positions below are document y coordinates after rendering at 390 × 844; height is the actual control height. They describe observed geometry, not conversion performance. Cookie prompts and form overlays can affect what a visitor can use, even when an element falls inside the viewport.

| Brand | Mobile first action or choice | Observed implication |
| --- | --- | --- |
| Gentle Revolution | Product text links around y623; a cookie notice covers part of the lower viewport. | A catalog and its overlays are a poor model for a one-action quiz entry. |
| Healthiest Baby | Purchase y666, height48; the baby photograph precedes the title on mobile. | The purchase still fits in this viewport, but the photo consumes the first260px of content. |
| Milestones and Motherhood | First stage label around y529; purchase action is much later. | Immediate relevance comes from stage navigation; it is not a one-action purchase hero. |
| Montessori Notebook | Enrollment y615, height52, with centered photo-overlay copy. | The complete initial offer and action fit before scrolling in this viewport. |
| Reading Head Start | Trial y623, height93; other pricing actions below y1150. | The responsive arrangement gives the trial offer early placement even though desktop pricing buttons begin around y1130. |
| The Sleep Lady | Consultation y611, height75; additional announcement link at the top. | A wide action appears early, alongside other package and navigation routes. |
| BabyPillars | Hero action y719, height60, full available content width. | Text and action precede the large photo; no hero photo appears in the first mobile viewport. |

## Lessons for the quiz description

The recurring useful relationship is a readable promise, an explicit next action and a strong visual distinction between that action and the surrounding page. The sources do not converge on a green site theme. Several combine a cool blue/teal or pale neutral base with a separate action hue.

For the current bounded quiz entry, retain one action and put it before a large photo on mobile. Use a light canvas, dark readable headline and a filled action with clear contrast. A proposed navy/white/orange combination is supported as a synthesis of observed visual roles; its precise shades and conversion performance are not measured by these observations.

Commercial testing evidence is documented separately in [CONVERSION-EVIDENCE.md](CONVERSION-EVIDENCE.md). In particular, Reading Head Start reports mobile form improvements; its current green action cannot be identified as the cause of those reported gains.
