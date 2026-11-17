# Affiliate marketplaces — actual access probes, 2026-10-24

These probes establish access limits. **No complete parenting inventory was harvested from any of the three networks.** A marketing page, login screen, empty sitemap or category shell is not a product census. No credentials/accounts were supplied or created, and no session cookies, captcha solving or access workarounds were used.

| Network / requested URL | Observed result | What that establishes | Saved evidence |
|---|---|---|---|
| ClickBank: `https://www.clickbank.com/marketplace/` | HTTP 200 after redirect to `https://accounts.clickbank.com/marketplace.htm`; page requests login after session expiry | Public route resolves to account-gated marketplace; no product/category result set | `_raw/marketplaces/clickbank.txt`, `_html/clickbank.html` |
| ClickBank account robots: `https://accounts.clickbank.com/robots.txt` | HTTP 403, CloudFront request blocked | Direct account-host harvesting not attempted further | `_raw/marketplaces/accounts.clickbank.com-robots.txt` |
| ClickBank public robots: `https://www.clickbank.com/robots.txt` | HTTP 200, allows public root | Public marketing route was permitted; does not grant account access | `_raw/marketplaces/www.clickbank.com-robots.txt` |
| Digistore24: `https://www.digistore24.com/marketplace` | HTTP 404 | This candidate route did not expose listings | `_raw/marketplaces/digistore24.txt`, matching HTML |
| Digistore24: `https://www.digistore24.com/v2/marketplace` | HTTP 404 | Second public route did not expose listings | `_raw/marketplaces/digistore24-v2.txt`, matching HTML |
| Digistore24 robots-linked sitemap: `https://www.digistore24.com/v2/marketplace/sitemaps.xml` | HTTP 200; empty sitemap index | No public listing URLs supplied by this current sitemap response | `_raw/marketplaces/digistore24-sitemaps.xml` |
| Digistore24 public robots: `https://www.digistore24.com/robots.txt` | HTTP 200; public allow plus restricted application paths | Public probes permitted; private application paths left alone | `_raw/marketplaces/www.digistore24.com-robots.txt` |
| BuyGoods: `https://go.buygoods.com/marketplace` | HTTP 200; affiliate marketing/filter shell linking Browse All Products to back office | No complete campaign inventory or parenting filter/result set in captured text | `_raw/marketplaces/buygoods.txt`, matching HTML |
| BuyGoods linked browse URL: `https://backoffice.buygoods.com/campaigns` | Web provider returned a 28-line category/navigation shell, HTTP status not exposed by tool | Lists categories but provides no product inventory in returned text; do not interpret this as zero parenting offers | `_raw/marketplaces/marketplace-buygoods-browse-web.txt` |
| BuyGoods back-office robots: `https://backoffice.buygoods.com/robots.txt` | HTTP 403, error code 1010 | No subsequent direct harvest of back-office content | `_raw/marketplaces/backoffice.buygoods.com-robots.txt` |
| BuyGoods public robots: `https://go.buygoods.com/robots.txt` | HTTP 200, empty body | No explicit public-root disallow in response; marketing page inspected | `_raw/marketplaces/go.buygoods.com-robots.txt` |

ClickBank's official category guide does list Parenting & Families, including Parenting and Pregnancy & Childbirth; its official search instructions direct the user to log in and open Affiliate Marketplace. Those are facts about organization/access, not the current contents of that category. Sources: [ClickBank categories](https://support.clickbank.com/en/articles/10535276-what-categories-and-subcategories-are-clickbank-products-sorted-into), [search instructions](https://support.clickbank.com/en/articles/10535272-how-do-i-search-the-clickbank-marketplace). Saved discovery response: `_raw/competitors/followup-discovery-4.txt`.

Digistore24's official [Find products to promote](https://help.digistore24.com/hc/en-us/articles/24001244509073-Find-products-to-promote) instructions also begin with account login and affiliate Marketplace. Saved primary-description capture: `_raw/marketplaces/digistore-discovery-web.txt`. No claim that all possible public aliases were exhausted is intended; the tested routes, empty official sitemap and documented account route are the evidence.

## Ledger and continuation

| Network | Complete inventories downloaded | Relevant products locally filtered | Kept product records | Full product reads | Product quotes |
|---|---:|---:|---:|---:|---:|
| ClickBank parenting/pregnancy | 0 | 0 | 0 | 0 | 0 |
| Digistore24 parenting/family | 0 | 0 | 0 | 0 | 0 |
| BuyGoods parenting/family | 0 | 0 | 0 | 0 | 0 |

The saved marketing/error/navigation responses were inspected for access only and are excluded from competitor full-read/quote totals. Continuation requires a legitimate account/export or newly available public listing endpoint. No credentials are requested as a prerequisite to the current public-source synthesis, and no conclusion about market absence or network profitability follows from these failures.
