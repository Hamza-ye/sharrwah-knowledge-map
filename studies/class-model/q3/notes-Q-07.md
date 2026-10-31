# Q3's check, batch Q-07: notes

Rows: 23. These are the Knowledge Map's questions on the storefront (SFR-01 to SFR-07), content (CNT-01 to CNT-04), channels (CHN-01 to CHN-05), point of sale (POS-01 to POS-03) and markets (MKS-01 to MKS-04). The results are in `check-Q-07.tsv`. `q3.py check --batch Q-07` reports 23 of 23 rows placed and 0 problems.

## Count by result

- covered: 21
- beyond the class: 2 (SFR-07, POS-03)
- partly, candidate miss (held or not held), unclear: 0

## Rows that were hard to place, and why

- **SFR-07 (rendering architecture: caching, CDN, edge rendering, theme sandboxing).** The row asks for a design: which architecture serves many stores fast and cheaply. It doesn't ask what the platforms do, so I placed it `beyond the class`, answered by `engineering:build`. The class's evidence holds only fragments, and they are a reading, not a design:
  - Shopify's Oxygen edge hosting (SH-S-0710);
  - BigCommerce's subprocessor Cloudflare, used for its CDN (BC-S-0448);
  - WooCommerce's coming-soon pages, which CDNs cache for 60 seconds (WC-S-5424);
  - WooCommerce's API response caching (CM-API-012).

  The founder's order of qualities and the "scale numbers come later" line (founder-decisions 2026-10-29 Quality) bear on this decision, but they don't answer it. I didn't add `founder:decided`.
- **POS-03 (which hardware and in-person payment providers are available "in the market").** This is a market's fact, so it is `beyond the class`.
  - In-person payment providers and card readers belong to S-04, plus `outside` for each provider's own terms. S02-M2 moved the providers to S-04.
  - Printers and scanners are covered by no subject. I gave them `subject:none`. They would need a subject on in-store hardware supply in each market, or the coordinator could rule them cheap and leave them to the build (a reading).
  - Time bombs: `bundles`, because S-04 answers before build and `outside` before release. `wrong time`, because the row's `needed_by` is `later`, against S-04's before build.
- **Where S-02's rulings answer a part (MKS-01, MKS-02, MKS-03, MKS-04, CHN-02).** These rows name neither "Sharrwah" nor "should", so their wording gives engineering no part. But each one's thing is S-02's subject: which settings bind per market, and what is keyed on the seller's country. So I named `subject:S-02` among the answerers, with the rulings in `basis` as `S-02 <row id>` and "ruled". This follows the brief's rule that a subject answers wherever the row's thing is one it holds, and Q-04's ACC-04 handled it the same way. The rulings used:
  - MKS-01: D4, D5, D6, E1, E3 and M2.
  - MKS-02: D7, E4 and D9, plus `subject:S-09`, which hasn't run, for the currency of orders and records in each market.
  - MKS-03: D6 and F8.
  - MKS-04: D3 and E2.
  - CHN-02: D4 makes a channel a kind of market, and D6 makes the products offered a per-market setting.

  Every one of these is before build, the same time as the model, so none raises a time bomb. If the coordinator reads these rulings as engineering's (`engineering:build`) rather than the subject's, the `when` and the time bombs stay the same.
- **CHN-03 and CHN-04 (the platform's own marketplace or buyer app; a branded app built by the platform).** Whether Sharrwah's own company runs a marketplace or a buyer app is on the founder's list (Intent (standing), line 2). But both rows, as worded, ask what the class does. So they are answered by `model` alone, and the founder's part is mentioned only as context. POS-03 is handled the same way for point of sale and hardware.
- **CNT-04 (the policies a platform requires or generates; needed by launch).** The cells answer this: the platforms either require policies or make the merchant responsible for them. Which policies a market's law requires is a different question, one the row only touches. It is a market's fact that no subject covers: Salla's cell names Saudi Arabia's E-commerce System as a filler (SA-S-5034). I didn't add it as an answerer. The coordinator may want it on Stage 3's list.
- **POS-01 (registers, cash, receipts, staff PINs, hardware, offline mode).** Placed as `covered`. Point of sale, hardware, cash management and in-person card payments each have a capability. I read registers, receipts, staff PINs and offline mode as detail of those capabilities, not as capabilities missing from the model. Offline mode is SH-S-0585, cited in CM-PAY-021@shopify. Registers and shifts are Salla's permissions (SA-S-2452, SA-S-2453) and WooCommerce's description of POS mode as a digital cash register (WC-S-0892). Staff PINs are held on no platform: I searched PIN, passcode and staff PIN, and for Salla and Zid رمز الدخول and الرمز السري.
- **SFR-06 (password protection).** No platform holds a storefront password page. CM-ACC-009@shopify's own search list covers password page, storefront password, password protect and similar terms. Shopify's private mode, which hides the store from visitors and search engines (S02-SH-719), is the class's form. So the row is covered by CM-ACC-009, CM-ACC-007 and CM-CNT-007, with the password itself as detail.

## Candidate misses

None. What I searched before ruling each one out:
- **POS staff PINs and offline mode:** PIN, passcode, offline checkout, offline mode (Shopify, WooCommerce, BigCommerce); for Salla and Zid PIN, رمز الدخول, الرمز السري, وضع عدم الاتصال, بدون إنترنت, offline, إيصال, الإيصالات, الوردية, ورديات, shift, درج النقود, cash drawer. Offline payments is cited in CM-PAY-021. Salla's shift permissions are cited in CM-POS-001@salla.
- **Receipts and registers:** Shopify's POS extension targets SH-I-1692, SH-I-1693, SH-I-1694 and SH-I-1695 are held but cited by no cell. Their concern, SH-C-144, lands in CM-POS-004, which is the same thing at its own grain. So they are detail, not a miss.
- **Sitemaps and structured data (CNT-03):** sitemap, structured data, schema.org, robots.txt, meta description, page title; for Salla and Zid خريطة الموقع, البيانات المنظمة, وصف الصفحة, عنوان الصفحة. Nothing is held on sitemaps or structured data. BigCommerce's setting Storefront Robots.txt (BC-I-0391) is held but cited by no cell, and its concern BC-C-047 lands in CM-ACC-006. My reading is that it belongs in CM-CNT-007@bigcommerce, the SEO capability. That is a placement for the coordinator, not a miss, since the SEO capability exists.
- **Prices per channel (CHN-02):** BigCommerce's price lists assigned to a channel (BC-S-0050) are cited in CM-B2B-003@bigcommerce.
- **Price rounding (MKS-02):** Shopify's Rounding prices (SH-I-2170) is held but cited by no cell. Its concern, SH-C-108, lands in CM-MKS-006, the capability it belongs to, so it is detail. I found nothing on rounding for Salla, Zid or BigCommerce (searched تقريب and rounding).
- **CDN, caching and edge rendering (SFR-07):** CDN, edge, page cache, caching and render, on all five platforms. These are the fragments listed above, and the row is beyond the class in any case.

## Time bombs

- POS-03: `bundles`; `wrong time`.
- No other row has one. Every other row is answered by the model, alone or with S-02 or S-09, all before build.

## Problems with the brief or the evidence

- **Which answerer carries S-02's rulings.** The brief lists engineering rulings under `engineering`. The message for this batch said "ruled" as the brief says. Q-04 named `subject:S-02` for the same kind of row, and Q-03's PLN-06 named `engineering:build`. I followed Q-04. The coordinator may want one convention across batches. Since both are before build, nothing computed changes.
- **SFR-03 and CM-SFR-001.** Salla's theme copies and scheduled publishing are terms of CM-SFR-001, and CM-MKS-002 (Rollouts) sits under Markets. My reading is that previewing and scheduling theme changes is a storefront concern placed under Markets because of Shopify's naming. This doesn't affect any result.
