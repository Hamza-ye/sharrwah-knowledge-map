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
