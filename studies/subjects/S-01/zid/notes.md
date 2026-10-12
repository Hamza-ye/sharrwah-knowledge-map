# S-01, phase A: zid (ZD)

Subject: who holds the merchant's funds between the buyer's payment and the merchant's payout.

Agent run of 2026-10-12. An earlier run was interrupted before writing anything; this run started from an empty folder. That run left scratch files (page copies and scripts) in the session scratchpad; they were not used.

Counts: 144 statements, 4 absences, 9 gaps, 44 term rows, 364 citations.

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
