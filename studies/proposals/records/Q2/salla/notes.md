# Notes: Q2 on Salla

## Selection
- 38 rows set to `copy` (37 concerns and S-01). The other 56 are set aside: their terms and statements name a feature or setting of Salla's own, with no place's law, sanction or licence, and no partner or provider chosen by the platform. No concern was added.

## What was read (all held, read 2026-10-18)
- observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3 held pages:
  - `structures/salla/com-policies/terms/text.txt` (https://salla.com/terms), read in full: articles 1 to 33, the subscriptions and refund policy, and the footer;
  - `structures/salla/com-policies/privacy/text.txt` (https://salla.com/privacy);
  - `structures/salla/com-policies/policies-selling/text.txt`;
  - `structures/salla/com-policies/payments/text.txt`;
  - `structures/salla/com-policies/policies-nd96/text.txt`: the terms of the National Day 96 campaign. Nothing was recorded from it.
- Fetch archive records:
  - `raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz` at 3700206 (https://salla.com/ar-ae/terms). Compared with salla.com/terms, it differs only in whitespace and line breaks;
  - the same archive at 20448927 (https://salla.com/en-ae/terms) and at 14913731 (https://salla.com/gcc-ecommerce);
  - the same archive at 15293952 (https://salla.com/salla-crossborder): a partner recruitment page. It does not say who answers for customs duties, so Q2-SA-G0148 stays open;
  - `raw/runs/20261008T121631Z-com-pages/fetch.warc.gz` at 7464352 (https://salla.com/ar-ae/blog/paylink), 17880198 (a blog page; not relevant), and `raw/runs/20261005T234928Z-docs-md/fetch.warc.gz` at 1434946 (developer advice; not relevant).
- `structures/salla/kyc-schema/demo@en/source.json`: its translations hold no payment services contract text. Q2-SA-G0176 to Q2-SA-G0178 stay open. Its Arabic strings are stored as \u escapes, so the statements cite its English strings.
- Help map: categories in Arabic; category lists asqsa2licbq3qbaigkvepipo, f9tgx9usfvxntfgbbo7qet7g, mf82baozc2wsgf5fxv1oq6vg and nlmrfbvrh4bdalrikuwpvai0.
  - Articles read: g0cbvwqncrfmptexs580y6f7, huvvumstnafaadcw6abpol14, brz9k255mdsfjeuty7ojte37 and ndz1k0tts5p7gfnqqxcubspl.
  - Articles scanned for licence and law terms: c7kvq9bm0bxjtef4yf5us13q, q70uv78qn8jm2wuxf8305qy4, di3p4uro9bna3ezsld2fjznr and vrufpnifa23qqdof8u71355o.
  - huvv… and brz9… added nothing beyond the copies.
- Corpus searches (`--max 10`):
  - (a) availability and sanctions wording;
  - (b) sanctions, OFAC and AML terms: no document matched;
  - (c) data-centre and residency terms: hits not relevant;
  - (d) regulators and licences.

## Live pages
- None read.

## Gaps
- Pages the gaps name as held but not read have now been read:
  - The privacy policy does not state where data is stored or transferred, nor its controller beyond the companies named. Q2-SA-G0218 to Q2-SA-G0222 stay open.
  - https://salla.com/payments names no processor or licence. Q2-SA-G0113, Q2-SA-G0114 and Q2-SA-G0116 stay open.
  - https://salla.com/gcc-ecommerce lists no countries and no entity per country. Q2-SA-G0160 stays open.
- Statements that close copied gaps, as noted in their `note`:
  - Q2-SA-032 closes Q2-SA-G0161 for ar-ae/terms;
  - Q2-SA-028 closes Q2-SA-G0164;
  - Q2-SA-029 closes Q2-SA-G0163;
  - Q2-SA-041 closes Q2-SA-G0217 and Q2-SA-G0171.

## Copies
- Q2-SA-K2510 cites CR 7011845513 for شركة منصة سلة للاتصالات وتقنية المعلومات, and Q2-SA-K2511 cites CR 4031200589 for the same company name. The usage agreement gives 7011845513 for شركة تطبيق سلّة لتقنية المعلومات. These are recorded as the sources give them; I found no copy wrong.

## Method
- The brief caps the account at about 1,500 words. It is at about that length.
- Statements longer than 300 characters are cited by consecutive quotes, each up to 300 characters, from the same line.

## Re-check against the observed runs, 19 October 2026

### What was read
- Guides of observed-sa at 4ca2e896a729215f422a137a364e7e9488610ba3: `README.md` and `docs/READING.md`, whole. Also `index/rest-endpoints.tsv` and `index/runs.tsv` (run names only).
- Corpus searches (`python3 -I method/corpus_search.py salla … --max 10`):
  - (r1) "sanction" "OFAC" "embargo" "العقوبات" "قوائم العقوبات" "blacklist" "محظور" "غسل الأموال": for Q2-SA-N01;
  - (r2) "عقد خدمات الدفع" "payment services contract" "البنك المركزي السعودي" "Saudi Central Bank" "مرخصة من" "licensed by" "SAMA": for Q2-SA-G0113, G0114, G0116, H0002, G0176, G0177. No run document listed; hits are help articles, fetch archives and structures already read or about carriers;
  - (r3) "noon" "نون للمدفوعات" "noon payments" "بوابة نون": after the gateways answer;
  - (r4) "مراكز البيانات" "مركز بيانات" "data center" "data residency" "تخزين البيانات" "داخل المملكة" "stored in" "hosted in": sentence 2, and G0218, G0221, G0222. The run documents listed matched only داخل المملكة, in orders, offers, shipping and community answers. None was about data;
  - (r5) "اتفاقية خدمات الدفع" "عقد خدمات الدفع" "Payment Services Agreement" "payment services contract" "شركة منصة سلة" "شركة تطبيق سلة" "Salla Holding": G0176, G0177, G0213, G0214, G0216;
  - (r6) "eu-central-1" "me-south-1" "me-central-1" "amazonaws.com" "data stored" "تُحفظ البيانات": sentence 2;
  - (r7) "غير متاحة لدولتك" "غير متاح في دولتك" "not available in your country" "country_not_supported" "للمتاجر في السعودية فقط" "only available for stores in" "المتطلبات القانونية": sentence 1. country_not_supported is already copied.
- Run files opened (all at 4ca2e896a729215f422a137a364e7e9488610ba3):
  - `raw/runs/20261012T010906Z-sweep-real-merchant-full-en/`: `run.json`, `responses.jsonl`, `responses/1488.json` (GET /admin/v2/gateways/payment, step 42), `steps/042.text.txt`, `responses/10106.json` (GET /admin/v2/store-wallet/payment-method, step 279), `responses/12135.json` (payment-restrictions, step 335: a settings section only, nothing recorded);
  - `raw/runs/20261008T122729Z-sweep-merchant-menus-ar/`: `run.json`, `responses.jsonl`, `responses/1683.json` (gateways, step 71). The same slug salla with label noon; the methods blocked_by requires_paid_plan. Not recorded again. The search lists the same label in runs 20261008T141131Z-sweep-merchant-en (2443.json) and 20261009T022751Z-sweep-public-demo-en (2864.json); not opened;
  - `raw/runs/20261008T125139Z-sweep-merchant-routes-ar/`: `run.json`, `actions.jsonl`, `responses.jsonl`, `responses/0535.json` (GET /admin/v2/onboarding/persona-country, step 23), `responses/0013.json` (GET /admin/v2/domain, step 1), `steps/023.text.txt`;
  - `raw/runs/20261008T131847Z-sweep-merchant-routes-ar/`: `run.json`, `responses.jsonl`, `actions.jsonl` line 14, `responses/0344.json` (checkout translations, step 14);
  - `raw/runs/20261008T211326Z-journey-reports-demo/`: `run.json`, `actions.jsonl` line 6, `steps/006.text.txt`, `steps/006.aria.yaml`.
- Store names: run 20261008T125139Z-sweep-merchant-routes-ar has no `extra` in its `run.json`. Its store is named by `"username":"store-1-da"` in its own GET /admin/v2/domain answer (`responses/0013.json`, Q2-SA-C077), cited with Q2-SA-061 to 063. The others name their store in `run.json` `extra.store`: real-merchant, merchant, demo.
- Arabic in the saved responses 1488.json, 0535.json and 10106.json is stored as \u escapes. The statements from them hold only their ASCII parts, and the persona question is recorded from the step's page text.

### Open items
- Q2-SA-N01: unchanged. Search r1 added to `searched`; no run document opened, none named sanctions in its title or snippet.
- Q2-SA-G0113, G0114, H0002: open. Q2-SA-064 records the gateway's slug and label, and names the gaps in its note; it shows no licence or contracting party.
- Q2-SA-G0116: unchanged.
- Q2-SA-G0176, G0177: unchanged. No run document opened from r2 or r5 showed the contract or its parties.
- Q2-SA-G0213: open. Q2-SA-065 records the bank account owner names, and names the gap in its note; it is not a party clause.
- Q2-SA-G0214, G0216: unchanged.
- Q2-SA-G0218: open. Q2-SA-066 and Q2-SA-067 record storage addresses, and name the gap in their notes; the privacy policy statement it asks for was not read.
- Q2-SA-G0221, G0222: unchanged.
- Coordinator's phrases: none were listed.

### Wording check (step 4)
- Q2-SA-N01: CheckSallaBlacklisted and 'ID suspended due to compliance or terms violations' are in Q2-SA-059 and its citation Q2-SA-C074. Salla Payments is in the records. The row is unchanged.

### New statements
- Q2-SA-061 to Q2-SA-067, cited by Q2-SA-C076 to Q2-SA-C085. The options list on the persona page has 7 items, recorded in full.

### Not read
- The KYC schema saved responses (GET api.aws.salla.dev/kyc/api/kyc/schema) in the runs: the folder already read `structures/salla/kyc-schema/demo@en/source.json`.
- The persona translations (`responses/0527.json` of run 20261008T125139Z-sweep-merchant-routes-ar), and the later persona steps 24 to 27.
- The other run documents listed by r4 and r6 (logos, apps, shipping companies in eu-central-1 addresses).

### Problems
- None with the tools. The corpus search lists the persona translations' store as "-", matching `run.json`.
