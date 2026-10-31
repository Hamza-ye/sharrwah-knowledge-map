# Q3's check, batch Q-03: notes

19 rows, the Knowledge Map's questions on the catalogue (CAT-01 to CAT-06), what is sold (SEL-01 to SEL-04), inventory (INV-01 to INV-05), languages (LNG-01, LNG-02) and operations (OPS-01, OPS-02). The check is in `check-Q-03.tsv`. `q3.py check` reports 0 problems.

## Count by result

- `covered`: 17 (CAT-01 to CAT-06, SEL-01 to SEL-04, INV-01 to INV-05, OPS-01, OPS-02)
- `partly`: 1 (LNG-02, the rest `candidate miss: not held`)
- `beyond the class`: 1 (LNG-01)
- `candidate miss: held`: 0
- `candidate miss: not held`: 0 whole rows; one rest (LNG-02)
- `unclear`: 0

## Rows that were hard to place

- **LNG-01** (a glossary: each platform's term and the term Sharrwah will use). Every cell already holds its platform's terms, Salla's in Arabic and English, so the platforms' half is in the model. But the glossary is not something the class does, and Sharrwah's own term is Sharrwah's design (`architecture/plan.md`, section 3: each part owns its model and its language). The checker doesn't accept `partly` without capabilities, or `beyond the class` with `model` among its answerers. So the row is `beyond the class`, answered by `engineering:build`, and its `what_would_settle_it` says where the platforms' terms already are. A reading.
- **LNG area.** `q3.py slice` shows LNG with 0 capabilities ("its domain may not be merged yet"), although the model is merged. The store's languages capability is `CM-MKS-008` in the Markets area (domain E), so LNG's rows land there. Either the seed's LNG area took no capabilities by design, or the slice's message is stale. The coordinator may want to check which.
- **INV-03** (what happens at zero stock: oversell, keep selling, hide). I read the out-of-stock policy as detail of `CM-INV-001`, not as a missing capability: it is a rule of inventory tracking, and its statements land there. Salla's `hide-out-of-stock-products` (SA-C-025/decides/SA-S-3482, SA-I-2482) lands in `CM-INV-001`, uncited. BigCommerce's guard against overselling (BC-C-004/reason/BC-S-0036) is cited in `CM-INV-001@bigcommerce`. Salla's "out-of-stock products shown at the page's end" (SA-C-020/decides/SA-S-1978) lands in `CM-CAT-001`. No statement held covers selling past zero (backorders, continue selling) for Shopify or WooCommerce: searched out of stock, out-of-stock, backorder(s), oversell(ing), continue selling, inventory policy, sell when, stock status, and for Salla and Zid نفاد, نفاذ, نفدت, غير متوفر, نفاد الكمية. If the coordinator reads the out-of-stock policy as a capability of its own, Salla's statements make it a held miss under `CM-INV-001`.
- **CAT-02** (manual or rule-based grouping). Read as detail of `CM-CAT-003`. But no statement on collections built from conditions is held on any platform: searched smart collection, automated collection, collection conditions, ruleSet, manual collection, dynamic; Salla and Zid ذكي, تلقائي, تصنيف تلقائي. The detail at that area will need Shopify's collection-conditions help page or the admin's collection form.
- **SEL-04** (deposits for bookings and pre-orders). Read as detail of `CM-SEL-004` and `CM-SEL-005`. No statement on deposits is held: searched deposit, partial payment, down payment, and for Salla and Zid عربون, العربون, دفعة مقدمة, دفع جزئي, مقدم.
- **OPS-01** (incident frequency and duration). Read as detail of `CM-OPS-001` and `CM-OPS-002`. No incident history is held, only Salla's status components (SA-S-0047) and BigCommerce's uptime claim (BC-S-0455). Delivered reliability is a measurement, not a capability.
- **OPS-02** (published limits, and which are product decisions and which engineering limits). Each limit is detail of its own capability. I added `engineering:detail` for the second half, since it is about the limits Sharrwah sets, which the class's evidence can show but not choose (a reading). Shopify's `maxProductVariants` and `maxProductOptions` (SH-I-2520, SH-I-2519) sit in Q1's out-of-scope list as unplaced keys. They belong in `CM-CAT-002`'s detail.
- **CAT-06** (catalogue capabilities found on only one platform: class feature or vendor choice). The model answers it with its counts (`CM-CAT-008`, `-009`, `-010`, `-011`, `-014` and `-015` at 1 of 5; option templates in `CM-CAT-002` at Salla and Zid; product SEO fields in `CM-CNT-007`). Whether each is a class feature is the plan's rule: `class` where the count is at least one (`PLAN.md`, Stage 4A, "the kind and the count"). So `plan` is among its answerers.

## Candidate misses and what was searched

- **LNG-02, its rest: `candidate miss: not held`.** The admin's own language, right-to-left layout, numerals, date formats and mixed-direction text. The Arabic storefront and its translation are `CM-MKS-008` (Salla's languages feature defaults to `ar`, SA-S-2973).
  - Searched in statements for Shopify, WooCommerce and BigCommerce: RTL, right-to-left, right to left, Arabic, admin language, language of the admin, numerals, date format, text direction, preferred language, account language, user language, interface language.
  - Searched for Salla and Zid: RTL, rtl, Arabic, العربية, اللغة العربية, عربي, من اليمين, اتجاه, لغة لوحة التحكم, لغة اللوحة, dashboard language, الأرقام, أرقام, هجري, التاريخ الهجري, hijri, numerals, ترجمة, الترجمة, لغة.
  - Searched `outscope` on all five for language, languages, locale, translation, rtl, arabic, لغة, اللغة, العربية.
  - Nothing found on the admin. Salla's captures are scoped `merchant@ar` and `merchant@en`, which suggests the admin runs in both languages, but no statement says so.
  - What would settle it: Shopify's help page on changing the admin's language, BigCommerce's control-panel language page, and a capture of Salla's and Zid's dashboard language switch with the admin shown in Arabic and in English. The coordinator routes it by `PLAN.md`, section 6, "Evidence".

## Time bombs

- **OPS-02:** `bundles` (its answerers' times differ: the model before build, `engineering:detail` at the area's build) and `wrong time` (`needed_by` `model` against `engineering:detail`'s time).
- No other row carries a time bomb.

## Problems with the brief or the evidence

- The checker doesn't accept `partly` without capabilities, or `beyond the class` with `model` among its answerers. A row like LNG-01, whose evidence half is spread across every cell rather than one capability, has to be `beyond the class`. The brief doesn't say how to place such a row.
- The slice reports the LNG area as unmerged (above).
