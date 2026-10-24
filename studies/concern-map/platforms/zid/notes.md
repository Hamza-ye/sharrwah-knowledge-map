# Zid: notes on the Q1 concern map run

Run of 12 October 2026, at declaration level only. The sources were:

- docs.zid.sa: the developer docs, read as `.md` pages through its `llms.txt`;
- help.zid.sa: the merchant help centre, in Arabic, rendered with `page_text.mjs`;
- zid.sa: product, pricing, legal and country pages, plus `zid.sa/llms.txt`;
- zid.eg;
- apps.zid.sa, read through the public categories endpoint it calls;
- help-partner.zid.sa.

No account was used. Every quote was copied from a file fetched with curl or rendered with `page_text.mjs`. The fetch log is in `fetched/log.tsv`.

## Files

| File | Rows |
| --- | --- |
| inventory.tsv | 543 |
| concerns.tsv | 96 |
| citations.tsv | 1087 |
| statements.tsv | 654 |
| gaps.tsv | 156 |
| not-reached.tsv | 4 |

Citations come from 202 web sources.

Concern ids are not consecutive (ZD-C-001 to ZD-C-116, with numbers left free between groups). There is no `placements.tsv`: this platform started from the reshaped placement step.

## Lists used and their sizes

| List | Entries | Source, as the platform organizes it |
| --- | --- | --- |
| api-resources | 56 | docs.zid.sa `llms.txt`, section "## API Docs": one entry per navigation group (the crumb before each page). |
| webhook-topics | 31 | Three sources: 16 merchant event topics from Webhooks Overview; 12 `app.market.*` events from App Management > Events; and 3 Zid Payments event types (`merchant_linked`, `payment_paid`, `refund_status_changed`) from the Zid Payments overview. |
| access-scopes | 38 | Scope identifiers named in the "🔑Scopes" blocks of the endpoint pages (338 endpoint `.md` pages read), plus scopes named in narrative pages (e.g. `embedded_apps_tokens_write`). |
| settings | 28 | Help centre category الإعدادات, groups عام / التواصل / المتجر. |
| other:help-centre-zid-products | 32 | Help centre sidebar "منتجات وخدمات زد". |
| plan-features | 182 | The compare-plans data of the pricing page (script chunk `2501-f29c20b24ab64821.js`), in groups, with keys starter, launch, growth, pro. |
| other:plan-cards | 38 | The plan cards of zid.sa/en/pricing. |
| legal-agreements | 23 | 7 `/legal/` pages in zid.sa/sitemap.xml; the footer link "Zid Stores' Customer Complaints"; 11 service sections of the Arabic Terms; the Zid App Activation & OAuth Policy; and 3 agreements named in the developer pages (App Partner terms, Theme Partner terms, Theme commercial policy). |
| other:app-market-categories | 35 | `api.zid.sa/v1/market/public/categories`, categories and subcategories. |
| other:product-lines | 14 | zid.sa header menu, Solutions. |
| other:countries | 5 | zid.sa/llms.txt, "Other countries". |
| other:staff-permissions | 57 | docs.zid.sa User Roles and Permissions, List of Available Permissions. |
| extension-points | 4 | docs.zid.sa Overview, "App Types": Public apps, Private apps, and the two kinds of shipping apps. |

Eight entries are out of scope, each with its reason:

- six plan lines for generic dashboard tools (Universal Search Center, Bulk Actions, Bulk Printing, Data Filtering, Delete All, Disable All);
- the permissions `view.zid.academy` and `view.store.home`.

ZD-C-011 (other payment gateways, بوابات الدفع الأُخرى) is in none of these lists. It comes from its own help article.

The admin-navigation list was not taken, because the merchant dashboard needs an account. The help centre's guide (دليل استخدام منصة التاجر) is organized in sections whose names match the dashboard paths its articles give (for example لوحة التحكم > الطلبات). Only its settings section was taken as a list, as the brief asks.

## Where the inventory stops

- **API reference.** Taken at group level, not endpoint by endpoint. Endpoint pages were read for their scopes. Two endpoint pages have a "/" in their slug (publish/unpublish-a-category, import-products-via-csv/xlsx-file). They were fetched late under flattened file names and name only `products.read_write`, which is already listed.
- **Storefront JavaScript events and theme development docs** (Vitrin, templates, presets) were not taken as lists.
- **Help centre.** Categories other than الإعدادات were read article by article, only where a concern needed them: 136 help pages were rendered, out of about 526 URLs in its sitemaps. The Zid FAQ pages (zid-faqs) were read only where a concern needed them.
- **App Market.** Categories only. Individual app listings were not inventoried; the apps page (apps.zid.sa/en-sa/apps) was rendered once.
- **Partner help centre** (help-partner.zid.sa): pages on payouts and shipping apps were read. So were four collection pages (Getting Started, FAQs, App Support, Theme Support) and two articles, read to look for the partner agreements. It was not taken as a list.
- **Country pages** (Egypt, UAE, Kuwait, Oman, Syria) on zid.sa were read, and zid.eg for Egypt. No Gulf-country page names a separate entity.

## What couldn't be shown

On the seven architecture concerns:

1. **Holding money.** No page names any of these:
   - the licensed entity, bank or provider that holds collected Zid Pay funds before deposit;
   - who holds the funds behind the Zid Wallet's IBAN;
   - who holds cash-on-delivery amounts that Zid collects for the merchant;
   - the payment service providers behind Zid Pay;
   - the financing entity (جهة التمويل);
   - the third-party processor for purchases from Zid.
   
   These are gaps (observation needed, or searched, not found).
2. **Licences.** No page states Zid's own payment or e-money licence. The Zid Pay terms name ساما for Saudi Arabia and the Central Bank of Kuwait for Kuwait.
3. **Entities.** No Gulf entities are stated. For Egypt, Zid Egypt's registration is stated, but zid.eg serves the same Terms naming the Saudi company. Which entity contracts with Egyptian merchants is not stated.
4. **Sanctions.** Countries and sanctions lists are named. Who screens, and how, is not.
5. **Where data lives.** No page states a country or cloud region for merchant or customer data, for Zid Agent's Google Cloud Vertex AI processing, or for the Amazon S3 storage of digital products.
6. **Partners.** No page names any of these:
   - the carriers behind the 35-carrier contract;
   - the company behind Zid Voice;
   - the providers and terms of Zid Growth services;
   - the acquirer for Zid POS card payments.
   
   The partnership agreement for app partners sits behind the partner dashboard login.
7. **Currency and tax.** Stated in detail. No gap is specific to it beyond the plan lines.

Elsewhere:

- **Which plan or staff role turns on a setting.** For several settings (checkout, gifting, URL redirects, Google Maps, working hours, custom shipping methods, the customer portal) this would need the dashboard; these are observation gaps for the founder.
- **Stated reasons.** Most commerce concerns state none. The help articles describe features and their benefits; a benefit was not recorded as a reason for a placement unless the text gives one for where the concern sits or who sets it.

## Sources that disagree (each is recorded with its citation; none is resolved)

- **Saudi Zid Pay deposits.** The sources give three schedules:
  - Sunday, Tuesday and Thursday (Zid Pay terms, Saudi Arabia);
  - daily from Sunday to Thursday (help article on activating online payments);
  - "every 2-3 days" (zid.sa/en/solutions/payments).
- **Mazeed payouts.** Two help articles of the same date disagree. One says weekly on Tuesday with no minimum (help.zid.sa/mazeed-settlement-2/). The other says monthly, for sales of 500 SAR or more (help.zid.sa/mazeed-financial-collection/). The Arabic Terms say the 30th of each month, with a 500 SAR minimum.
- **Cash-on-delivery transfer to the merchant.** Twice a month (Arabic Terms, August 2026), against "within two working weeks" (help-centre FAQ, July 2023).
- **Zid Egypt tax ID.** 711-549-443 in the English text and 711-459-443 in the Arabic text of the same help article (help.zid.sa/about-zid-egypt/).
- **Zid's legal name.** The English Privacy Policy gives "Al Qudrah Technical for Information and Communication Technology Company L.L.C"; the Terms and the site footer give "Al-Qudrah Al-Taqniyah for Technology and Communication Company".
- **Terms versions.** The English Terms show January 2025 and the Arabic Terms August 2026; the Terms say the Arabic version prevails. The Arabic Terms repeat the cash-on-delivery sentence under خدمة التحويل البنكي.
- **Countries served.** A help-centre FAQ dated August 2023 says Zid serves merchants in Saudi Arabia and the Gulf only. The 2026 Egypt and Syria pages present Zid in those countries. Syria is also in the Saudi Zid Pay list of sanctioned countries.
- **Amazon.** The sales-channels FAQ says Amazon is available in Saudi Arabia and the UAE, and gives seller registration links for Saudi Arabia, the UAE and Egypt.
- **Reports.** The help article says reports are only for باقة الأعمال الكبيره، النخبة، الإحترافية. The compare-plans data shows the line "Reports - Sales Channels" on launch, growth and pro.

## Plan names, as each source gives them (not mapped to one another)

| Source | Names |
| --- | --- |
| Pricing cards | Starter (free), Rise (99 SAR/month), Growth (299 SAR/month), Pro ("Let's talk") |
| Compare-plans keys | starter, launch, growth, pro |
| zid.sa/llms.txt | البداية (free), الانطلاقة (99), النمو (299), الاحترافية (custom price) |
| Terms | باقة لايت، باقة نمو، باقة الاحترافية |
| Help centre | باقة زد لايت، باقة النمو، الباقة الاحترافية، باقة الأعمال الكبيرة، النخبة، الباقات المجانية، الباقة المجانية |
| Sales-channels article | النمو، الانطلاقة، الاحترافية |
| Docs | "Professional or Enterprise plan" |

## Problems with method

- **zid.sa in a headless browser.** Every zid.sa HTML page renders an error page, both when read and in the capture: "Oops! Something went wrong." in English, "عفواً! حدث خطأ." in Arabic. A script chunk returns 404 (ChunkLoadError), so the rendered text holds only the error. This is a deployment fault, not a bot check. The full text is in the served HTML, including the Next.js payload (`self.__next_f.push`). zid.sa quotes were taken from the raw HTML.
  - Some FAQ answers on product pages exist only in that embedded data. They match with markup removed.
- **The compare-plans data.** It is only in the script chunk `2501-f29c20b24ab64821.js`, served as `application/javascript`. The capture tool saves such a file as `raw.bin`, which the checker does not read, so the plan-line quotes resolve through the browser's rendering of the script as text.
- **Scopes on the Authorization page.** The page shows its scope list only as an image. Scopes were taken from the endpoint pages instead.
- **help.zid.sa in English.** Its robots.txt disallows `/en/`, and the help centre was read in Arabic, its default. Help articles marked "( لوحة التحكم الجديدة )" describe the new dashboard.
- **Dates.**
  - Help articles: the "آخر تحديث" date each article shows.
  - docs.zid.sa pages: undated, so recorded with the day read. The exception is the OAuth policy, dated 2026-09-09.
  - zid.sa pages: the date shown on the page, or else the sitemap lastmod.
  - The script chunk: its HTTP Last-Modified header (2026-10-11).
- **The App Market.** apps.zid.sa is a client-rendered app, so its categories were taken from the public JSON endpoint it calls.
- **Fetch rate.** Own fetches ran at about one request per second per host. No host refused a request.
- **Pages behind a login.** partner.zid.sa/partnership-details renders the partner dashboard login. It is listed in not-reached.tsv and was not attempted further.

## Capture and check

All 202 cited web sources were captured with `method/capture/run.sh` (CAPTURE_LANG `en,ar;q=0.8`) into `capture/20261012T045101Z-q1-zid-sources`. Every source returned HTTP 200 and rendered.

The checker found 0 errors. All 1087 citation quotes were found (3 of them with markup removed), and all 654 statements were found verbatim in their first citation's captured source. One review item remains: ZD-C-011 is in none of the lists.

## Facts about the sites

| Host | robots.txt |
| --- | --- |
| docs.zid.sa | allows all |
| zid.sa and zid.eg | disallow /private/, /en/testing, /ar/testing |
| help.zid.sa | disallows /en/ |
| help-partner.zid.sa | sets Crawl-delay 1 |
| apps.zid.sa | allows all |

These were recorded as facts and did not limit what was read.

Both `zid.sa/llms.txt` (Arabic, then English) and `docs.zid.sa/llms.txt` exist. They were used as page indexes.

Four pages address AI agents or assistants:

- docs: "Zid AI Agent Skill" (a skill for AI coding agents);
- docs: "Our custom MCP server";
- docs: "Moving to Vitrin Using LLMs";
- partner help centre: "Connect your Zid partner account to your AI assistant with Partner MCP" (seen only as a title in a collection list).

They were noted and not followed.

## Inference (not counted as statements)

- Inference: the API reference's example file URLs point to S3 buckets in eu-west-1 (for example a bucket named zid-testing). These are examples, and they do not show where Zid stores production data.
- Inference: zid.eg serves the zid.sa site with the Saudi company in its footer, which may mean Egyptian merchants contract with the Saudi company; no page states it.
- Inference: الانطلاقة (99 SAR in zid.sa/llms.txt), the card Rise (99 SAR) and the compare-plans key launch may name the same plan; no page maps them.
