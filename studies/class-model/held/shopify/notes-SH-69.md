# Held pass, Shopify, batch SH-69: notes

83 entries of `pricing-page-data` (effort high), evidence at observed-sh@e38dc17e3, in `structures/shopify/pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl`. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-69`).
- **1 to 28:** the rest of www.shopify.com/ae-ar's plans page (items.jsonl line 2):
  - the comparison table from 'تقدير الرسوم والضرائب وتحصيلها' to its end (rows 68 and 70 to 84 of 84, counted from 1; row 69, the note '*يتطلب Shopify Payments', is SH-68's SH-E-94cbf0aa);
  - the eight FAQs (`accordionItems`);
  - the disclaimer `apyDisclaimer` with its three footnotes.
- **29 to 83:** www.shopify.com/ae-ar's POS page (line 3):
  - its terms entry;
  - the six plan summaries with their features (`mainPlans`, `alternatePlans`);
  - the two sections 'متضمن في كل باقة' (`sideBySideGridContent`) and 'ما هو POS Pro؟' (`posLiteVsProContent`), with their six items each;
  - the casual in-person selling and POS Pro lists (`posLiteVsProContent.plans`).

  SH-70 begins with `loaderData.*.posLiteVsProPlans` (its 1 to 4 and on: `name: PosLite`, then PosPro). These are the same two lists, in the same words, that my 71 to 83 hold under `posLiteVsProContent.plans`: they can take the same lines, for the coordinator to align.

**Placed:** 83 entries in 179 lines: 82 entries on capabilities, 1 `out` (the Finance heading), no `new`; 54 entries take more than one line. Supports: 158 `core`, 15 `shows`, 5 `outside`; no `own-service` or `extension-point`. Five filler lines (the disclaimer's providers). 64 lines carry qualities.

**Sources read:**
- the brief and what it names: the evidence map; the rulings, the last section most; B-extent.md's "Cells and evidence" and "Conventions from the dry run"; observed-sh's `README.md`, `docs/READING.md` (fetch runs, structures, indexes), `docs/GAPS.md` (nothing on these pages), `structures/README.md`;
- `structures/REGISTER.tsv` row 141; `index/ledger-summary.tsv`'s shopify-com-sitemaps rows; `selection.tsv`'s row; `show --meta`;
- SH-68's notes and placements first, as the batch before mine on this structure, and kept to their R0 to R11 as the coordinator's check left them;
- items.jsonl lines 2 and 3 (the ae-ar plans and POS pages) by the parts my entries are cut from, and the English twins on www.shopify.com/ae (its plans page's rows 68 to 84 and disclaimer, its POS page's sections and summaries), to clarify only. Every line's terms and quotes are the Arabic entry's own, but for one English quote in 66's reading, cited at its page.
- The model: `earlier` (no earlier line on my entries' keys, but for `online_store`, below); `cells` for every capability placed on; `land_points.py cell` for CM-PAY-023 to CM-PAY-027 and CM-INV-004; `caps --terms` and `search` for the rows and items (below). The cells cite the 30 September table's twin rows: SH-S-7062 to SH-S-7065 (Finance), SH-S-7070 to SH-S-7079 (Plus rows and duties), SH-S-7195 to SH-S-7200 (the disclaimer), SH-S-7202 (the PCI FAQ), SH-I-1235 (Test new features before launch, CM-EVO-001).

## Rules followed

**SH-68's rules, as kept.**
- R0 (the coordinator's check): a line on every read site of its language takes no site in scope.
  - Of mine, every entry labelled with the three Arabic sites takes none, but SH-E-e4bfb392 (28). R0 lists it among the five that keep their labels.
  - Entries labelled with www.shopify.com/ae-ar alone take it after their plans: 18, 25 to 27, the six plan summaries and 75.
- R1: the POS page's terms entry (29), three `core` lines.
- R3: the table rows, the Finance heading `out`, Just for Plus CM-PLN-001 `shows` (scope Plus).
- R4: the POS page.
- R6: the FAQs.
- R7: the qualities.
- R9: the disclaimer's providers, `outside` with fillers, as the cells hold the 30 September page's same footnote.

**Rules for kinds R0 to R11 don't cover, for the coordinator to align with SH-70 to SH-79:**
1. **A footnote of the disclaimer's list** (`apyDisclaimer.list`) is `shows` on its row's capability, its rates and fees as qualities, as R3 has the note row. The row's own reading quotes it.
   - The list's order (Balance, Credit, Capital) isn't the marks' order (¹ Balance, ² Capital, ³ Credit).
   - I joined each footnote to its row by its words (26 to 3, 27 to 5, 28 to 4). The English page's list has the same order.
   - Whether the page renders the list numbered isn't held in the loader data.
2. **A provider named for one country takes that country in its scope.**
   - The disclaimer's 'تُصدر جميع التمويلات المقدمة عبر Shopify Capital في الولايات المتحدة من قِبل WebBank' gives CM-PAY-026 the scope `www.shopify.com/ae-ar;الولايات المتحدة`. The disclaimer's other lines take the site alone.
   - This departs from rule 5's 'An entry's lines share one scope'. A filler's market comes from its statement's scope (B-extent, slot fillers), and without the United States, WebBank would read as the UAE site's lender.
   - The same holds for 19's CM-PLN-002 line, scoped Plus: the answer states the annual or 3-year commitment for Plus only, and its other line (cancelling the account) for every plan.
3. **The POS page's two sections.**
   - **The items under 'متضمن في كل باقة' (58 to 63)** take the header's scope, Basic;Grow;Advanced;Plus, as R4 gives the header. Each also takes CM-POS-001 beside its own capability, since the page lists the point of sale's features (R4's summaries). The exceptions are an item whose own capability is CM-POS-001's child (CM-POS-002) and in-person card payments (CM-PAY-021), as R3 has them.
   - **The items under 'ما هو POS Pro؟' (65 to 70)** take 'POS Pro' and CM-POS-001, as R2 and R8 have the POS Pro card.
4. **A plan summary's description** (`description_long`) goes in reading, as R4 has it. Each thing it names takes its own line too, as rule 2 has what a description names:
   - Basic's selling online (CM-SFR-001);
   - Grow's shipping discount (CM-SHP-002, 'خصم شحن يصل إلى 87%' as quality);
   - Advanced's enhanced support, more markets and advanced analytics (CM-ONB-003, CM-MKS-001, CM-ANL-001);
   - Starter's selling on social media (CM-CHN-001).

   Each cell is already `core`, so these lines change nothing. If R4 meant the descriptions to give no lines, they can go.
5. **A list ending in 'والمزيد' or 'وغيرها' (and more)** names examples, which take no line: 60's draft orders, gift cards and analytics; 70's BOPIS and endless aisle. This is R3's rule for tooltips and the ruling after SA-41. A list without it states what the item does, and each thing takes its line:
   - 65's staff accounts and permissions;
   - 66's inventory counts, purchase orders and low stock alerts;
   - 68's lifetime value reports and loyalty insights.
6. **A plan summary's POS Pro add-on stated unavailable** (Starter's `is_available: false`) is `shows` on CM-POS-001, as the ruling after WC-5 has an offer listed but stated unavailable. Starter's own point of sale ('1 تسجيل دخول لـ POS', 52) is `core`.
7. **Customer loyalty insights** (47, 79, and 68's 'إحصاءات الولاء') are CM-ANL-001's: analytics on customers, which Salla's cell also holds there (customers' analytics). They aren't CM-LOY-004, loyalty programmes. CM-CUS-001 is the other reading, since 68 puts them in the customer profile in POS.

## New things

None. Each row, FAQ, summary and item had a capability. Searched with `caps --terms`:
- the Plus rows by their English twins;
- for the FAQs: closing and cancelling, the countries, setup fee, bandwidth, TLS, Buy Button, embed;
- for the POS page: purchase order, low stock, stock alert, staff performance, staff target, customer preferences, clienteling, lifetime value, loyalty insights, endless aisle, ship to customer, pickup, BOPIS, locations, draft order, retail analytics, retail reports, customer profile, social media, AI channels, online store.

## Entries I couldn't tell, and what would settle each

- **17 (pricing-faq-0), what Shopify is, on CM-CHN-001 `core`:** its answer's own statement is selling across channels 'من لوحة تحكم واحدة'. What it lists after that is in passing. The alternative is `out`: a description of the whole platform, which no capability holds, as the ruling after SA-21 has a container over the whole admin.
- **19's account cancellation on CM-ONB-002 `shows`:** 'إلغاء حسابك' read as the merchant closing the store. CM-PLN-002 alone is the other reading, the question being about the subscription.
- **26 to 28, the footnotes, `shows`:** they give the products' terms. 26's 'مكافأة مقدمة من Shopify' and its daily accrual could read as `core`. The cell is `core` either way.
- **59's CM-INV-005 line:** the back office 'يدعم أكثر من 1,000 موقع' read as the store's own locations. The figure stays on CM-POS-001, as R1 has posRetailLocations.
- **61 on CM-PAY-021 alone:** in-person payments 'باستخدام Shopify Payments', which CM-PAY-021's name holds (Shopify Payments for POS). A CM-PAY-002 line is the other reading.
- **62 on CM-POS-002 `core`** (a CHANGES line, below).
- **63 on CM-POS-001 `core` and CM-POS-004 `shows`:** 'قابل للتوسيع وسهل التخصيص', with low-code and no-code options.
  - It names neither apps nor extension targets, nor who extends the POS app.
  - `core` on CM-POS-004 would change the cell (`extension-point` only), on a reading of the smart grid that the item doesn't name.
  - Shopify's own statements of what merchants customize in POS without code would settle it. The cell cites shopify.dev's POS UI extensions pages (SH-S-0713) for apps only.
- **47, 68, 79 on CM-ANL-001:** rule 7 above.

## A structure whose items and sources disagree

- **Plus's POS Pro add-on** (42) is titled 'يشتمل على POS Pro' (includes POS Pro) with `included_in_plan: false`. Retail's has the same title with `true`. The plans page's POS Pro row states 'يتضمن 20 من المواقع.' on Plus (SH-68's SH-E-ff61aa7e). The line quotes the title and names the flag; which holds isn't stated.
- **The Basic annual price** (SH-68's notes): the ae-ar POS summary gives `annual_monthly_price` 29 and `annual_price` 348, while the same page's terms entry (29) gives 'basicAnnualPrice: <span>$24.00 USD</span>'. Each line quotes its own entry.
- **The footnotes' order:** rule 1 above.
- **The items and the entries agree:** the entries are the items' decoded loader data. I didn't print the WARC records.

## What the sources state that no entry holds, and leads (for the second stage)

- **POS Pro's 'وتتبع الأداء' (track performance, 65)** of staff has no capability.
  - CM-STF-004, staff targets (Salla's /users/targets), holds nothing on Shopify. Its definition isn't stated, and tracking performance isn't targets, as worded, so I gave it no line.
  - Shopify's POS staff reports, if held, would settle whether it is CM-STF-004's or CM-ANL-002's.
- **The endless aisle (70's 'التسوق من ممرات افتراضية لا نهائية (endless aisle)')** has no capability. It is named as an example, so it has no line.
- **The Balance footnote's 'شروط المكافآت'** links help.shopify.com/manual/finance/shopify-balance/rewards/earning-rewards. **The Credit footnote and the disclaimer** link /ae-ar/legal/shopify-credit-program-terms and /ae-ar/legal/shopify-credit-issuing-bank-terms. These are leads for CM-PAY-023 and CM-PAY-025's terms; the cells already cite Shopify Credit's Program Terms.
- **The POS page's** `sideBySideProps.image.alt` 'امرأة تستخدم جهاز POS' is pruned (`image`): `out` in any case.

## The checker's lines, read again

- **`CHANGES CM-INV-004@shopify gains core` and `holds nothing: becomes held`, by line 146 (66, SH-E-59c14ea0):** kept.
  - The item of 'ما هو POS Pro؟' states, as what POS Pro includes, 'واحصل على تنبيهات انخفاض المخزون من مكان واحد'. Its English twin on www.shopify.com/ae's POS page is 'Perform inventory counts, complete purchase orders, and get low stock alerts from a single place.'
  - Low stock alerts to the merchant are CM-INV-004's thing (its note: 'Salla's alert to the store when a product's quantity is low'). The buyers' back-in-stock alerts, the cell's one earlier hit, are domain D's.
  - It is a feature of the add-on, so its scope is POS Pro (R8).
- **`CHANGES CM-POS-002@shopify gains core`, by line 136 (62, SH-E-f744fe44):** kept.
  - Every plan includes 'وصول إلى أجهزة POS حديثة وموثوقة', with hardware staff use at the counter or on the floor. It names no seller, so it is placed by what it shows.
  - SH-68's line 122 (its 84) gives the same cell `core` from the plan line on phones and card readers, which the coordinator's check kept. With it, this line changes nothing.
  - `shows` is the alternative, if 'access to hardware' is read as the merchant's own purchase. The cell's `own-service` rests on Shopify's sale of the equipment (SH-S-7269), which this item doesn't name.
- **`NOTE` on a product named with the platform's brand** (lines 4 to 7, 10, 33, 130, 135): each line is `core` by its cell's place, not by its name:
  - Shopify Balance, Capital, Credit and Bill Pay: their admin sections, routes and plan rows (SH-68's R9);
  - Shopify Combined Listings: its plan row SH-S-7071 and API object;
  - Shopify Checkout: its settings route;
  - Shopify POS: its plan rows and POS app;
  - Shopify Payments for POS: CM-PAY-021's plan rows In-person card rates.
- **`NOTE line 130`: its first lead CM-PTN-008 holds nothing.** The lead is by name only ('برنامج' is the POS software here, not a programme). It is not the entry's thing.
- **The other name-only leads to cells that hold nothing were read too, and are not the entries' things:**
  - CM-CUS-006 (24, 68);
  - CM-PTN-006 (25);
  - CM-PLN-006 (26): the footnote's 'رصيد يُضاف إلى حساب Balance' is a credit to the money account. CM-PAY-023's note keeps it apart from CM-PLN-006.
  - CM-SFR-013 (8, 11): التصفية is the flash sale there, not filtering;
  - CM-AIA-003 (53, 56): AI channels are CM-AIA-005's.
- **The checker's last line:** '83 of 83 entries placed; 0 problems'.

## Problems with the brief or the script

- **`earlier`** keyed the summaries' feature `name` `online_store` (53, 56) to SH-8's admin routes visited as the Online Store app (SH-8:29, :56), a different thing. My lines place the summaries' 'متجر إلكتروني محدود' on CM-SFR-001.
- **`check`** printed 'SH-E-d9f8d2b2 has no placement' twice while it was unplaced; the batch list holds it once (`held/batches/SH-69.txt`, line 83).
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief states (qualities wider than B-extent's list; the rulings). Rule 2 above departs from the brief's own rule 5, for B-extent's slot fillers.

## The coordinator's check (31 October 2026, after the batch)

- **One cell changes, kept:** CM-INV-004 is `core`, scope POS Pro. POS Pro's item 'واحصل على تنبيهات انخفاض المخزون من مكان واحد' is the low-stock alert, as its English twin, 'get low stock alerts from a single place', is. CM-POS-002's `core` repeats SH-68's.
- **The rules 1 to 7 stand for SH-70 to SH-79, with R0 to R11:**
  - rule 2 is made a ruling (after SH-69): a line takes its own scope where its thing is stated under its own condition;
  - rule 4 stands, since a plan's description states what the plan includes (M-9), unlike a list's examples, which rule 5 gives no line.
- **SH-70 opens with `posLiteVsProPlans`.** Its two lists are in the same words as this batch's entries 71 to 83, so SH-70's prompt says to take these lines.
- **The source's disagreement** (Plus's 'يشتمل على POS Pro' with `included_in_plan: false`) is in `reading`.
- **Lead:** POS Pro's staff performance tracking and 'endless aisle' have no capability. CM-STF-004 (staff targets) is the lead for the first.
- **Cost:** 13.4 million tokens over 65 requests, about 161,000 an entry.
