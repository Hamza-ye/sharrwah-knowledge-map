# S-01, phase A: zid (ZD)

Subject: who holds the merchant's funds between the buyer's payment and the merchant's payout.

Agent run of 2026-10-12. An earlier run was interrupted before writing anything; this run started from an empty folder. That run left scratch files (page copies and scripts) in the session scratchpad; they were not used.

Counts: 145 statements, 4 absences, 9 gaps, 44 term rows, 365 citations.

## What was read

Q1 index, `studies/concern-map/platforms/zid/`: `concerns.tsv`, `statements.tsv`, `gaps.tsv`, `citations.tsv` (all rows of the concerns on Zid Pay, deposits, bank accounts, gateways, instalments, COD, bank transfer, wallets, Mazeed, financing, sales channels, POS and the contracting entity).

The brief's table gives zid no held material. `method/held_index.py` reports captures of several zid.sa and help.zid.sa pages under this repository's `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/`; they were not opened, because every page below was read live on 2026-10-12.

Read raw (HTML fetched; tags removed for reading; embedded page data searched for FAQ answers that open on click):
- https://zid.sa/ar/legal/zidpay-terms-conditions-sa/, https://zid.sa/en/legal/zidpay-terms-conditions-sa/
- https://zid.sa/ar/legal/zidpay-terms-conditions-kw/, https://zid.sa/en/legal/zidpay-terms-conditions-kw/
- https://zid.sa/ar/legal/terms-conditions/ (آخر تحديث اغسطس 2026, whole document, including its زد باي section, which reproduces the Saudi and Kuwait Zid Pay terms) and https://zid.sa/en/legal/terms-conditions/ (Last Updated January 2025)
- https://zid.sa/en/solutions/payments/, https://zid.sa/ar/solutions/payments/
- https://zid.sa/ar/legal/logistics-t-and-cs/, https://zid.sa/en/legal/domestic-shipping-terms/
- https://zid.sa/ar/paymob/, https://zid.sa/ar/mispay/ (landing pages for the partners' customers)
- https://zid.sa/en/pricing/ and https://zid.sa/_next/static/chunks/2501-f29c20b24ab64821.js (to re-check copied plan-line quotes)
- https://zid.sa/ar/legal/ (returned a page with no listing)

Read as `.md` endpoints: https://docs.zid.sa/llms.txt, overview-1340225m0.md, overview-1340608m0.md, overview-1341008m0.md, merchant-activation.md, payment-paid-event-17956148e0.md, webhooks.md.

Read rendered through `method/capture/page_text.mjs` (help.zid.sa): deposits_zidpay, about_zidpay, activate-online-payments, payment-requirements, nafath_verification, payment-gateways, tap-gateway, bnpl-2, zid-wallet, wallet-split, transactions, refund-requests, bank-accounts, zidpay-paymentpage, mazeed-financial-collection, mazeed-settlement-2, about-zid-financing, cod, gcc-merchants, jahez, connect-payment-device, about_zidpos, the sales-channels FAQ article (help.zid.sa/الأسئلة-الشائعة/), and the FAQ pages behind index citations ZD-S-0530, 0556, 0560, 0609, 0640, 0703, 0755, 0988, 0994. Every copied index quote was found again in today's copy of its source.

## What could not be read

- The store dashboard (https://web.zid.sa/): no account was used. The Zid Pay terms that the general Terms say are reached when activating the service (S01-ZD-005), the Nafath request that is stated to be in the provider's name (S01-ZD-046), the wallet's account details (S01-ZD-064) and the gateway and instalment activation forms are all behind it. These are the routes of gaps G01 to G07.
- Agreements the terms name as binding but do not identify or link: شروط وأحكام مقدم الخدمة for payment networks (S01-ZD-025), شروط وأحكام البنك for bank transfer (S01-ZD-075), الشروط والأحكام الخاصة بالطرف الثالث for خدمة الدفع عند التوصيل (S01-ZD-072), and Apple Pay Merchant Terms. No provider, bank or third party is named, so none could be read.
- zid.sa pages rendered through `page_text.mjs` return only an error message (عفواً! حدث خطأ. on https://zid.sa/ar/solutions/payments/), so zid.sa pages were read raw.

## Problems with the method

- The brief's table says zid has no held material, but `held_index.py` reports readable captures of zid pages from this morning's Q1 run. The pages were read live instead.
- The brief says copied citations keep their index commit; zid's index citations are live URLs with no commit, so they were copied with their source, locator, quote and dates unchanged.
- In raw zid.sa and WordPress HTML, a bold label sits before its colon (for example الدفع عند الاستلام (COD) on the logistics terms, Zid Pay in the English Kuwait definitions), and the items of some lists are separate elements with no text between them. A quote or statement crossing such a tag matches only if the checker replaces tags with a space, or only if it replaces them with nothing. Quotes and statements here were kept to text that matches both ways: label-and-value lines were recorded as values with the label in `identifier` (S01-ZD-124 to S01-ZD-128), and the payments page's activation list (متطلبات تحتاجها للتفعيل, which includes الجمعيات الخيرية) was not recorded, because its items cannot be quoted as one verbatim statement.
- Two statements rest on FAQ answers that exist only in the page's embedded data, inside a script, and open on click: S01-ZD-106 (https://zid.sa/ar/paymob/) and S01-ZD-113 (https://zid.sa/ar/solutions/payments/), which carries absence S01-ZD-N01. If the checker drops script content, these quotes will not be found. Index citation ZD-S-0743 quotes the same kind of data with JSON punctuation that today's raw page escapes (\",\"answer\":\"), so it was not copied.
- Sources differ and are recorded as found: Zid Pay deposit days in Saudi Arabia (Sunday, Tuesday, Thursday in S01-ZD-016, S01-ZD-032, S01-ZD-040; daily Sunday to Thursday in S01-ZD-038, S01-ZD-039); COD transfer timing (S01-ZD-069 twice a month to the wallet; S01-ZD-071, dated 2023, within two working weeks); Mazeed collections (S01-ZD-085 and S01-ZD-088 monthly with a 500 SAR minimum; S01-ZD-089 weekly on Tuesdays with no minimum). The English Terms (January 2025) are older than the Arabic Terms (August 2026), which state that the Arabic version prevails.
- The Kuwait Zid Pay text gives a period as x يوم (S01-ZD-022); recorded as found and as gap G08.
- Statement S01-ZD-072 (COD under تفعيل الحسابات, a third party's service) and S01-ZD-069 (COD under زد شب, collected by Zid) are two parts of the same Terms; both are recorded.

## Phase A2 (2026-10-13)

Brief `briefs/A2-close-gaps.md`, on the zid rows of `variants.tsv` marked gap (S01-VP-01, 02, 03, 04, 11, 12, 13, 15, 21, 22: gaps G01 to G09) or not covered (S01-VP-10). Added: statements S01-ZD-146 and S01-ZD-147, citations S01-ZD-C366 and S01-ZD-C367, one term row (بوابات الدفع), gaps S01-ZD-G10 to S01-ZD-G19, and `a2.tsv`. S01-ZD-146 was added to the `conditions` of S01-ZD-144. No absence was found. G01 to G09 are left unchanged; G10 to G18 restate them with the A2 reading, and G19 is the gap for S01-VP-10.

What was read is listed in each gap's `read` and in `a2.tsv`. Held copies were read from this repository's capture runs `20261012T045101Z-q1-zid-sources`, `20261012T104936Z-s01-sources` and `20261012T190225Z-s01-sources-zid` (raw HTML, tags removed for reading, because the zid.sa `text.txt` files hold only an error message). Pages not held were fetched raw on 2026-10-13 (help.zid.sa articles and FAQs found through https://help.zid.sa/sitemap_index.xml and its post and faqs sitemaps; zid.sa partner and campaign pages listed in the held zid.sa sitemap; docs.zid.sa payment-provider `.md` pages listed in the held llms.txt).

Problems:
- This repository is not a git checkout here, so held paths are cited as `sharrwah-knowledge-map:<path>` without a commit.
- S01-ZD-147 is cited from the held raw HTML of https://help.zid.sa/category/zid-pay/; the category page shows no date, so its source_date is the capture date.
- The step list on https://help.zid.sa/zid-pos-app/ (S01-ZD-146) appears twice in the raw HTML; one copy lies inside an HTML comment.

## Absence audit

Phase A3, 2026-10-13, brief `briefs/A3-absence-audit.md` (with the two additions sent during the run: record anything else the documents read state on the subject, and the result `partly contradicted`). Repository at `a920665d3307544df27207fd40905340d9eaadfe` when the run started; held files are cited at that commit. Rows are in `absence-audit.tsv`.

What was found:
- 23 claims audited: the 4 absences (N01 to N04) and the 19 gaps (G01 to G19; none is of kind `page not read`). All 23 are `confirmed`; none is contradicted or partly contradicted. No held document names Zid Pay's payment service provider or its licence, the bank or holder behind the wallet IBAN, the account or licence under which Zid holds COD amounts, the Mazeed gateway, who settles SurePay payments, who holds funds for Paymob, amwal pay or Tap, when the instalment providers pay, the Kuwait period (still x يوم), who holds Amazon proceeds, or any lien, رهن or set-off right; none offers Zid Pay, الاستقطاع للمحفظة or تمويل زد outside the lists in N01 to N04.
- Recorded under the added rule: S01-ZD-148 (store-language: مدفوعات زد متاحة لتجار السعودية و الكويت, and the buyer pays in the store's base currency), S01-ZD-149 (Egypt page, Starter plan: Basic payment methods (bank transfer, cash on delivery)), S01-ZD-150 (wallet withdrawal limit, fees, 2 to 5 working days, and amounts that cannot be withdrawn), with citations S01-ZD-C368 to S01-ZD-C377. S01-ZD-150 was added to the `conditions` of S01-ZD-121 and S01-ZD-122.
- Not recorded, because phase A's rule 12 stops recording past 150 statements and the folder now holds 150: the wallet page's note that تجار دول الخليج must zero the wallet before moving a store between countries; the Zid Pay terms' يجوز لزد باي ومزودو الخدمة باقتطاع رسوم رمزية على إجمالي العملية; activate-mazeed's ويتم إضافة اسم البنك ، اسم المستفيد، ورقم الايبان لتحويل المستحقات المالية; the plan data's الدفع بالتقسيط / Installment Payments line (launch, growth, pro; not starter); and the Trendyol FAQ's two lines on commission deducted from deposits (الإيداعات ستتضمن المبالغ بعد استقطاع العمولة, and commission on returned orders returned in the next deposit). All are in held files named in the rows' `read`.

Searches too broad to read in full, and how they were narrowed:
- Words that sit in every help page's menu (زد باي, تمويل زد, زد كاشير, نقاط البيع, زد لوجيستك, منصات البيع, مزيد) and words that are parts of other words (مدفوع in مدفوعات, إمكان in بإمكانك, COD in code, tap, lien in clients, offset in CSS, SAMA in osama) matched 78 to 174 documents. Each listing was narrowed to the documents that matched a more specific word of the same search (named in each row's note), to paragraphs naming both the arrangement and a country, or to the article text between آخر تحديث and the page footer.
- The docs.zid.sa order and coupon schemas match many names (Moyasar, Tabby, SurePay, Mazeed) only as code values; one copy (list-of-orders) was read for those lists.

Problems with the method:
- `corpus_search.py` does not search the zid.sa pages: their `text.txt` holds only the site's error message, so the Terms, the Zid Pay terms, the privacy policies, the payments, Paymob and Egypt pages and the shipping terms never match (for example مبلغ احتياطي returns no document). Their raw HTML was searched and read with a scratch script that strips tags, so those searches are not in the `searches` column; each row's note says so.
- The brief's rule 12 (150 statements) and the added rule conflict here: the folder held 147 statements before this phase, so only three could be added. The rest are listed above.
- The Zid Pay category page (held) lists an article المنتجات الرقمية و إيداع المبالغ that is not held and that no brief points to; it was not read.
- HEAD moved from a920665 to a041738 during the run (a change to STATE.md only); citations use a920665 as instructed.
