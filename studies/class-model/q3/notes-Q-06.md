# Q3's check, batch Q-06: notes

The rows: km:CUS-01 to CUS-04, B2B-01, B2B-02, MKT-01 to MKT-04, LOY-01, SUP-01 to SUP-03, ANL-01, ANL-02, NTF-01 to NTF-03 (19). The placements are in `check-Q-06.tsv`. `q3.py check` printed: "19 of 19 rows placed; 0 problems".

Count by result: covered 17; partly 1 (NTF-03); beyond the class 1 (ANL-02). There are no candidate misses, held or not held.

## Rows that were hard to place

- **km:B2B-01, quantity rules.** Every other part has a capability: companies, locations and contacts (CM-B2B-002), price lists (CM-B2B-003) and payment terms (CM-PAY-008). For quantity rules, the cells hold two things:
  - Shopify's store-wide add-to-cart limit (SH-S-7483, cited in CM-CHK-002@shopify);
  - BigCommerce's bulk pricing rules (BC-S-0017, cited in CM-CAT-013@bigcommerce).

  So I placed the row `covered`, and named per-buyer minimums, maximums and increments as detail. No held statement names quantity rules per B2B catalog or company. Searched:
  - English, on Shopify, BigCommerce and WooCommerce: quantity rules, quantityRules, volume pricing, quantity price breaks, minimum quantity, increment, minimum purchase quantity, maximum purchase quantity, bulk pricing, quantity;
  - Arabic, on Salla and Zid: الحد الأدنى للطلب, الحد الأدنى للكمية, حد أدنى, الكمية القصوى, أقصى كمية, خصم الكمية, خصومات الكمية, التسعير حسب الكمية, كمية الجملة, أقل كمية, الكمية الدنيا, حد الكمية, كميات, الجملة, كمية.

  `outscope` finds only Shopify's store feature `volumePricingEnabled` (SH-I-2603), which is unplaced. A reading: if the coordinator wants per-catalog quantity rules to be a capability of their own, that would be a not-held miss, settled by capturing Shopify's B2B quantity rules and volume pricing pages and BigCommerce's minimum and maximum purchase quantity.
- **km:ANL-01, "can merchants build their own?"** CM-ANL-006 holds custom reports built by developers and apps: Salla's Report Creator (SA-S-5146) and Shopify's ShopifyQL for apps (SH-S-5905). No held statement shows a merchant building a report in the admin. Searched:
  - English, on every platform: custom report(s), report builder, exploration;
  - Arabic, on Salla and Zid: تقارير مخصصة, تقرير مخصص, منشئ التقارير.

  `outscope` finds only Shopify's store features `reports` and `reportsEditing` (SH-I-2592, SH-I-2593), both unplaced. I placed the row `covered`, since the cells say who builds custom reports on each platform, and named merchant-built reports as detail. A reading: `reportsEditing` suggests Shopify lets merchants edit reports. If the coordinator reads that as a capability of its own, it is a not-held miss, settled by Shopify's help pages on custom reports.
- **km:MKT-01.** No held statement names buy X get Y or tiered discounts. Searched:
  - English: buy x get y, BOGO, free shipping, tiered, combine, combinations, stack;
  - Arabic: شحن مجاني, الشحن المجاني, خصم متدرج, الحزم, حزمة, دمج الخصومات, الجمع بين.

  The discount types are in the cells as capabilities: codes (CM-MKT-002), automatic offers (CM-MKT-003), Shopify's function targets for order, product and shipping discounts (CM-MKT-004) and bundles (CM-SEL-006). I placed the row `covered`, with the types and how discounts combine as detail. It carries `bundles` because CM-MKT-004 is a slot and the others are class.
- **km:MKT-04, conversion APIs.** The only held matches are Salla's flags `facebook-conversion`, `snapchat-conversion` and `tiktok-conversion` (SA-S-3216 to SA-S-3218). Each is an app, cited in CM-MKT-009@salla. That they carry conversions is a reading from their names. No held statement names a conversion API that runs on the server. Searched: conversion API, Conversions API, server-side, CAPI, Meta Pixel, TikTok Pixel, Snapchat Pixel, conversion(s), التحويلات, تتبع التحويلات. I placed the row `covered`, with server-side versus browser conversions as detail.
- **km:CUS-03, shipping keyed on a group.** Groups key prices (BC-S-0048, BC-S-0050), promotions and product access (BC-S-0209), and payment methods (CM-PAY-019: Salla by customer, BigCommerce by company). For shipping, the cells hold only shipping restrictions in general (CM-SHP-001: SA-S-2112, ZD-S-0855). No held statement keys a shipping rate on a customer group, so I named it as detail.
- **km:CUS-04, "under what consent".** I read this as the platforms' consent mechanism: CM-TRU-006, and SH-S-0707 and SH-S-0067 in CM-MKT-009. What consent a market's law requires is not asked as such. No subject covers consent law: S-08 covers where data lives.
- **km:ANL-02** asks what data architecture serves analytics at scale. The references' evidence holds what their analytics show, not the architecture behind it, so I placed the row `beyond the class`, answered by `engineering:build`. Its words name neither the platforms nor Sharrwah. By the brief's rule, such a row asks the model, which can't answer it, so it carries `wrong party`. It also carries `wrong time`: its `needed_by` is `later`, but engineering's architecture decision is `before build`.
- **km:NTF-03** is `partly`:
  - The channels and the slot for their providers are CM-NTF-004.
  - Each market's sender rules (SMS sender registration, WhatsApp Business) are a market's fact, and no subject in `subjects.tsv` covers them. So the answerer is `subject:none`; the subject it needs is one on messaging channels and sender rules in each market, for Stage 3's list. The regulators and providers are `outside`.
  - Which providers Sharrwah partners with is the founder's (commercial agreements and partners: `founder-decisions` 2026-10-29, Intent (standing)).

  It carries `bundles`: the model's part is due before build, the founder's and outside parts before release.

## The subjects' registers

S-01's and S-02's registers answer none of these rows. S02-D4 is an engineering ruling, not vetoed. It keeps a group of customers as a dimension beside markets, which a setting such as a price may key on, and it lets a market be of the business-customer kind. That bears on CUS-03 and B2B-02, but neither row asks a choice of Sharrwah's own, so I didn't add engineering to them. S02-M9, the number of catalogs across B2B markets set by plan, is plans and prices. No row here asks it.

## Problems with the brief or the evidence

None that stopped the work. A reading of a recurring borderline: the brief counts a capability that holds the thing on some platform, through an app or a store-wide setting, as covering it. So per-buyer quantity rules (B2B-01) and merchant-built reports (ANL-01) are `covered` with their gaps as detail, not misses. In both, the only evidence of the narrower thing is an unplaced Shopify store feature in `outscope`. The coordinator may read either as a not-held miss instead; the material that would settle each is named above.
