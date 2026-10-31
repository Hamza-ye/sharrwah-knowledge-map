# Notes: held pass, Salla, batch SA-1 (`app-categories`, `app-store-tabs`; 81 entries; effort high)

**Sources read** (observed-sa at `b0bd0b163`): `structures/salla/app-categories/` (labels `api@ar`, `api@en`, `api-app-impact@ar`, `api-app-impact@en`, `apps-salla-sa`: items, meta.json, source); `structures/salla/app-store-tabs/merchant@ar/` (items, meta.json, `source.json`); the App Store page the tabs and the app_impact list were answered for, `raw/runs/20261008T122729Z-sweep-merchant-menus-ar/steps/078.text.txt` (step 78, `/apps`, 'سلة | متجر التطبيقات'). This is the first held batch on Salla, and no batch after it holds these structures, so there is nothing to align with.

**How the batch is placed.**
- **The categories** (entries 2 to 51) are the App Store's categories: B-extent's "app-store or marketplace category", `extension-point` on the capability whose thing the category is, as the model already places 12 of the same categories (SA-S-1188 to SA-S-1201, SA-S-1221 to SA-S-1228). The `api@ar` and `api-app-impact@ar` entries hold only Arabic names; their English names are in the `@en` items of the same structure, cited in `reading`, never in `terms`. The `apps-salla-sa` entries add a title and a description: each thing the description names as what the category's apps do takes its own line (rule 2).
- **The tabs' apps** (entries 52 to 81) are third parties' apps in the platform's own list to install (M-3, M-7): `extension-point` on what each description says the app does. `filler` is the item's `company.name`, and a venue the entry names (Instagram, AliExpress, Shein, Klaviyo, WhatsApp, Google Sheets, Power BI). `quality` is the app's listed price and trial. Reviews (`avg`, `count`) are the app's own data and aren't placed.
- **A tab's line** is given to an app only where its description names the tab's thing, or it is plainly one of it (rule 2, M-6 refined). Where not, the reading says "its description doesn't name the tab's ...".
- **No company named in the batch is in Salla's group**: none matches CM-ACC-002's companies or the checker's `GROUP`. So no line is `own-service`.

## New things

1. **`new:حوّل الزوار إلى مشترين`**, Convert visitors into buyers (`api-app-impact@en/items.jsonl`, line 3).
   - Entries: SA-E-7476fe50, the app_impact category; SA-E-9b00d3be, Noti Money's tab line, whose notifications help visitors decide to buy.
   - Place of its own: an app category of the App Store (type `app_impact`, id 2119052929). The dashboard's App Store tab of the same name, حول الزوار إلى مشترين (group 380443386), lists three apps.
   - Proposed: domain D, area MKT, parent CM-MKT-005.
   - Searched: conversion; convert; تحويل; visitor; زوار; مشترين. They found only CM-MKT-008, CM-MKT-009, CM-MKT-012, CM-MKT-022 and CM-CHK-001, none of them conversion.
   - WooCommerce's Marketplace has a parent category Conversion whose subcategories the model places (CM-MKT-001, CM-MKT-021, CM-MKT-022, CM-LOY-004); the parent itself has no capability. A possible join.
2. **`new:أتمت عملياتك اليومية`**, Automate daily operations (`api-app-impact@en/items.jsonl`, line 10).
   - Entries: SA-E-d458df84, the category; SA-E-9614fd57 (Social bot) and SA-E-d40da897 (Pop Auto), its tab's apps whose descriptions name automating.
   - Place of its own: an app category (type `app_impact`, id 1445340521), and the tab أتمت عملياتك اليومية (group 576261038, four apps).
   - Proposed: domain F, area AUT, as a sibling of CM-AUT-001 or under it.
   - I didn't place it on CM-AUT-001. Its thing is workflows the merchant builds from triggers and actions (Shopify Flow), and the category's apps automate given tasks: customer service, offers, prices. CM-AUT-001 on Salla still holds nothing.
   - Searched: automat; أتمت; workflow; operations; عمليات.
3. **`new:تتابع مهام فريقك، تنظّم مشاريعك`**, following the team's tasks and organizing projects.
   - Entry: SA-E-4426f98b, the app Work Table (ورك تيبل).
   - No place of its own: one app listing.
   - Proposed: domain A, area STF, parent CM-STF-001. Or out of the class's extent, as a general business tool sold in the App Store.
   - Searched: task; مهام; project; مشاريع; team; فريق; staff.

The new categories take `extension-point`, not M-13's `core` for a container that no capability names. B-extent says an app-store category is `extension-point`, and B-extent governs (the brief, "Read only").

## Entries I couldn't tell, and what would settle each

- **SA-E-b76230fe and SA-E-bd00e001 (Fulfillment / ادارة المخزون) are on CM-INV-001, not CM-SHP-011.**
  - The category's Arabic name is inventory management. Its description is 'essential inventory management Apps' for 'organizing and controlling your inventory' (`apps-salla-sa/items.jsonl`, line 5), and the description governs the title (B-extent).
  - CM-SHP-011's Salla cell rests only on this category's English name (SA-S-1192, "read as apps that fulfil the merchant's orders … no statement held defines the category"). That reading is now in doubt.
  - The category's `search_options` hold a Company Type 'Fulfillment' / 'شحن كلي/شامل' under Shipping and Delivery (see the second-stage leads), which may be what supports CM-SHP-011.
  - What would settle it: the coordinator's reading of the two together, or the apps listed under the category (apps.salla.sa/categories/fulfillment).
- **SA-E-e2b5ee3c and SA-E-e97fa216 (Site Optimization).**
  - The name-only entry follows the model, CM-CNT-007 (SA-S-1201). The dashboard's App Store tags SEO apps with it ('رانك سيو', 'ظهور - خبير السيو والوصف الذكي', `steps/078.text.txt`, lines 138 and 284).
  - The description names no search engine: it names the customer experience in the store, pop-up ads, hiring freelancers and gold and jewelry prices. So the `apps-salla-sa` entry goes on CM-SFR-005 (whose note holds Shopify's site optimization in Store design apps), CM-SFR-007, CM-CAT-013 and CM-PTN-005.
  - What would settle it: whether CM-CNT-007's Salla `extension-point` should rest on this category at all.
- **SA-E-e97fa216's CM-PTN-005 line ('hiring freelancers').** CM-PTN-005 is the platform's directory of partner services. The category says only that apps help hire freelancers, and who they are isn't stated. It may instead be no capability's.
- **The app_impact categories read from a goal, not a thing:**
  - SA-E-54e0a2a0, Attract new visitors: CM-MKT-005;
  - SA-E-e0b61b68, Reach customers wherever they are: CM-SUP-004, by its tab's AI customer-service apps;
  - SA-E-fe4a655b, Ship faster and cheaper: CM-SHP-001;
  - SA-E-0e57168d, Build trust after the sale: CM-SUP-003, by "trust" in its name. It has no tab, so what its apps do after the sale isn't held;
  - SA-E-cb23757b, Sell in more places: CM-CHN-001;
  - SA-E-726bef0c, Design without a developer: CM-SFR-001.

  What would settle each: the apps the App Store lists under it (not structured; I didn't look for a category's own answer in the runs. `marketplace/v2/apps/popular-apps` and `recommendations` are held in the same runs but not structured, REGISTER row 48).
- **Things a description names that I didn't give a line, each too thin to place:**
  - Email's 'send invoices' and Accounting's 'calculate bills': CM-ORD-008, order invoices;
  - Geolocation's 'calculate the distances between the shipping company and your customer': CM-SHP-004?;
  - Analytics' monitoring of 'advertising': CM-MKT-010;
  - Bosla's statistics 'لحظة بلحظة': CM-ANL-004, Live View, which holds nothing on Salla;
  - the Klaviyo app's 'تتبع مبيعاتك': CM-MKT-008, which holds nothing on Salla;
  - AlFinder and Atmet chat's AI, which serves buyers, not the merchant: not CM-AIA-001.
- **SA-E-48137ac0 (Wallet Plus), its CM-LOY-001 line, is `shows`.** The app's programmes are 'مرتبط بمحفظة العميل مباشرة': they link to the customer's wallet, the platform's, not one the app provides.
- **SA-E-6de0c72f ('All' / الكل) is `out`,** as a filter value that names nothing. If the coordinator reads it as the App Store's full list, it is CM-APP-002 `core`.
- **The `company` field.** Neither the API nor the page says what `company` is. I read it as the app's provider and gave it as `filler`. Step 78's page shows no company beside the apps (`steps/078.text.txt`). A maker gap only if the coordinator reads the field otherwise.

## The tabs (groups with no entry of their own), each with the capability its title names

| Tab (group id) | Capability, as a lead |
| --- | --- |
| حول الزوار إلى مشترين (380443386) | `new:حوّل الزوار إلى مشترين` |
| كبر قيمة كل سلة (13310252) | CM-MKT-021 |
| حول المشتري لعميل دائم (935729609) | CM-LOY-004 |
| البداية السريعة, "Quick start" (1289165728) | none: it names only a grouping, and no app_impact category matches it. Its apps (M5AZN, AliExpress, Shein) are dropshipping and logistics |
| وسع متجرك بالذكاء الاصطناعي (257821489) | CM-AIA-001 |
| أتمت عملياتك اليومية (576261038) | `new:أتمت عملياتك اليومية` |
| صمم متجرك بدون مطور (1791039590) | CM-SFR-001 |
| كلم عملاءك أينما كانوا (1480788116) | CM-SUP-004 |
| اعرف أرقامك و اتخذ قرار (433855235) | CM-ANL-001 |

The tabs as a whole are the App Store's (CM-APP-002), a container with no entry.

## Items against sources

- **The tabs' names and the app_impact categories differ:**
  - the tabs drop the categories' diacritics (حول against حوّل, كبر against كبّر, كلم against كلّم), and one adds a space (اعرف أرقامك و اتخذ قرار against اعرف أرقامك واتخذ قرار);
  - their ids differ;
  - five tab ids equal ids of `type: app` categories with other names: 1289165728 is ERP system, 433855235 AI-Driven Solutions, 257821489 Email, 576261038 Geolocation, 1480788116 Others. 1445340521, the app_impact category Automate daily operations, is also the company id of Social bot.

  READING.md says Salla's numbers recur across unrelated lists, so no line joins by id.
- **Step 78's page doesn't show the tabs' names.** It shows the app_impact list (`steps/078.text.txt`, lines 81 to 94), not the tabs' names (no match for حول الزوار إلى مشترين or البداية السريعة in the step's text). Where the dashboard shows the tabs isn't held.
- **The selection holds only the Arabic labels as entries.** `api@en` and `api-app-impact@en` are the same lists in English, so their names appear only in readings.
- **Items and sources agree.** For `api@ar`, `api@en`, `api-app-impact@ar` and `app-store-tabs`, I compared each item's id and name, and each tab's apps, against `source.json`: 19, 19, 15 and 30 items, all equal. I read `apps-salla-sa`'s items against the page's payload only through its `meta.json`, which states 141 equal pages.

## For the second stage: what the sources state that no entry holds

- **The Shipping and Delivery category's `search_options`** (`apps-salla-sa/items.jsonl`, line 3), dropped by the selection's rule `drop:search_options`:
  - Delivery Methods: 18 values, among them Same Day, Pickup, Heavy, Refrigerated, International, Next Day, Door to Door, Branch Pickup & Delivery, Smart Lockers, Pickup from Merchant Door & Delivery to Points;
  - Shipping Coverage Area: Domestic, International;
  - Company Type: 'Fulfillment' (شحن كلي/شامل), Shipment and Delivery;
  - Services: Packaging, Cash on Delivery, Warehousing, Express Shipping and others.

  These are leads for CM-SHP-011, CM-SHP-021 (packaging), CM-SHP-006/007 (pickup) and CM-SHP-020 (international).
- **`20261008T122729Z-sweep-merchant-menus-ar/steps/078.text.txt`:**
  - lines 52 and 80: 'اكتشف تطبيقات من سلة وشركائها الموثوقين' (apps from Salla and its trusted partners), a lead for CM-APP-011 on Salla, which holds nothing. No app in this batch names a Salla company;
  - lines 171 and 172: 'تطبيقات بين يدك...' and 'هذه التطبيقات مدمجة في لوحة التحكم لتستخدمها دون مغادرة متجرك.' (apps embedded in the dashboard), a lead for CM-APP-007;
  - lines 54 to 79: ready app bundles 'حزم جاهزة لانطلاقة متجرك' (باقة النمو 147.00, باقة زيادة المبيعات 286.00, باقة البداية 308.00), a lead for CM-APP-002 and CM-APP-003. Their answer, `marketplace/v2/apps/bundles`, isn't structured (REGISTER row 48).
- **Other answers held but not structured** (REGISTER row 48): `marketplace/v2/tags`, `recommendations` and `apps/popular-apps`, in the same runs.

## Problems with the brief or the script

- **A new app category's `supports`.** M-13 gives a new container `core`. B-extent gives an app-store category `extension-point`, and I followed B-extent.
- **Quotes from a sibling label.** The checker reads an entry's `terms` only from its own text. The English names of the `@ar` entries are held in the `@en` items of the same structure, so they can only be quoted in `reading`.

## The checker's notes on the new lines

Its NOTE lines 72, 109, 112 and 116 flag new things whose entries have leads. I read each lead. CM-MKS-009 matches the field name `data` (`list: data`), which every app entry holds. CM-ACC-004 and CM-ACC-002 match the words شركة, مؤسسة and معلومات in a company's name. CM-B2B-001, CM-B2B-003, CM-MKS-006 and CM-PLN-003 match price or wholesale words in the listing (سعر, جملة, منصة). CM-MKT-005 matches التسويق, which entry 52's description names; it has its own line there, and for Work Table it is only 'مديري التسويق', marketing managers. None of these leads is the new thing.

## The coordinator's check (30 October 2026, after the batch)

- **The weakest lines stand as readings.** 'Build trust after the sale' is CM-SUP-003's, social proof and social trust, beside the social-proof features and the UGC testimonials app the same batch names. 'Sell in more places' is CM-CHN-001's, sales channels.
- **Two of the model's Salla cells are read again at Salla's amendment:**
  - CM-SHP-011's, which rests on the Fulfillment category's English name alone, where its Arabic name and description say inventory management (ادارة المخزون);
  - CM-CNT-007's, which reads Site Optimization as SEO, where its description names no search engine, though the dashboard lists SEO apps under it.

  CM-CUS-009's note says what Salla's map services locate isn't stated. The Geolocation app's description now states it: shipping routes and distances.
- **App-store categories are `extension-point`, not M-13's `core`,** as the batch placed them: B-extent says so, and B-extent governs.
- **The three new things** (Convert visitors into buyers, Automate daily operations, Work Table's team tasks) are decided with Salla's others before its amendment.
