# Held pass, Salla, batch SA-57: notes

67 entries (effort high), evidence at observed-sa@b0bd0b16, the last of Salla's held pass. Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-57`):
- 1 to 25 `shipping-carriers`: the shipping companies a store is offered, GET `api.salla.dev/admin/v2/shipping/carriers`, on the public demo (giftshop2024, 16 of 17: `public-demo@en`, run `20261009T022751Z-sweep-public-demo-en` step 68) and the real store (dandye-dandy-ksa, 15: `real-merchant@en`, run `20261012T010906Z-sweep-real-merchant-full-en` step 269). An entry held under both labels (7 to 11, 15) has the same item on both stores.
- 26 to 41 `theme-design-components`: `data.blocks`, the 16 section types the theme editor offers for the demo store's theme رائد (`raed@demo-en`, run `20261008T200413Z-journey-themes-demo` step 9).
- 42 to 49 `theme-marketplace` `all-page1@demo-en`: page 1 (8 themes) of the Theme Marketplace's list of 287; 50 to 67 `tags@demo-en`: its 18 tags (run `20261008T201238Z-journey-theme-marketplace-demo` step 1).

**Placed:** all 67 entries on capabilities; one (7, Prolo) also takes a new thing. None `out`. 139 lines: 138 on capabilities, 1 `new`; 76 `core`, 58 `extension-point`, 5 `shows`; no `own-service` or `outside`. Fillers on 79 lines (the carriers and the theme developers), qualities on 40 (the carriers' prices, durations and reach; the themes' prices), scope on the 89 carrier lines (the store: `giftshop2024`, `dandye-dandy-ksa`, or both).

**Sources read:** the brief and what it names; the evidence map; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's rows for the three structures and `index/ledger-summary.tsv`; the selection rows; B-extent's "Cells and evidence" and conventions; the rulings to their last section; `show --meta`; each structure's `meta.json`, `source.json` and `items.jsonl`. To clarify only, each cited where a line rests on it: the two stores' shipping pages (`20261009T022751Z-sweep-public-demo-en/steps/068.text.txt`, `20261012T010906Z-sweep-real-merchant-full-en/steps/269.text.txt`); the App Store listing, `structures/salla/marketplace-apps/api@ar/items.jsonl`, for the carriers' `app_id` (lines 518, 521, 573, 580, 718, 761, 765, 773, 804); the themes journey's steps 001, 009 and 010 (text and tree); the marketplace journey's step 001; the locale `structures/salla/dashboard-translations/en/themes-marketplace-monorepo.json` (one JSON line, cited by key); the cells of every capability placed on.

## The run decisions

A run of one kind is decided once and each entry read for a difference (the brief's "How to work"):

- **C1. A carrier of Salla's labels** (`type: salla`, `supports_salla_awb: true`; 1 to 9, 17 to 22): `core` on CM-SHP-015, the carrier its filler. The page sets each under 'Salla Shipping Labels' and says 'integrate your store with the best shipping companies' (step 068 line 21; step 269 line 22): the platform's own list of the carriers it integrates (M-4), as the cell's flags and plan lines naming carriers are `core` with the carriers as fillers. `type: salla` is no maker statement (the brief). The App Store lists the apps of four of them with company 'سلة' (Aramex, Smsa, Aymakan, Redbox): Salla's own apps connecting them. **For the coordinator:** the ruling after SA-17 makes an app of Salla's that connects a third party, who does the thing, `extension-point`, with the third party as filler. Applied to the carrier rows themselves, the CM-SHP-015 lines of 1, 2, 4, 5, 17, 18, 20 and 21 become `extension-point`. No cell changes either way (CM-SHP-015 is `core;extension-point`). I kept `core`, since the entry is the dashboard's own list under Salla's labels, not the App Store's listing.
- **C2. A carrier by its own app** (`type: app`; 10 to 16, 23 to 25): `extension-point` on CM-SHP-015, as SA-27 placed Mrsool, SPL and Sent Express (SA-27:47 to 49). The App Store's company for the app is the carrier's own: Naqel Express, SPL, Sent, Logistiq, AJEX. For مرسول and أفق السرعة the app isn't in the held listing, so the maker is a gap. أفق السرعة (13) and إيجكس on the real store (25) show 'Carrier app', not 'Salla Shipping Labels'.
- **C3. `supports_salla_awb: true`, shown as 'Salla Shipping Labels'** (the page shows it beside every carrier whose field is true, and 'Carrier app' beside the two whose field is false): `core` on CM-SHP-002, the carrier as filler. Each shipping type's price and duration are the line's quality ('Starting cost', 'Delivery time' on the page; no currency is stated). For the type-app carriers I kept SA-2:51, which placed Salla's changelog naming Naqel, Ajax, Sent and Logistiq among its labels' carriers on CM-SHP-002 `core`. Where the field is false (13, 25), no CM-SHP-002 line.
- **C4. `supports_ratings: true`**: `core` on CM-SHP-022, the ratings of the carriers. The page shows each carrier's rating and count, and 'Rate now' wherever the store's `review.status` is `need_review`. So the merchant rates the carriers, which CM-SHP-022's note leaves open ('Who rates the carriers isn't stated'). Prolo, شيبا and iMile have `supports_ratings: false`, so no line.
- **C5. The carrier's own services and types beyond its shipping** (M-8; SA-49's R1, kept: the provider's line `core` with the carriers as fillers, and the thing they do `extension-point` on its own capability, with the same fillers):
  - the international type, دولي, of Aramex, Smsa and Dhl: CM-SHP-020;
  - Aramex's insured type, مؤمن: CM-SHP-003;
  - cash on delivery, الدفع عند الاستلام, in Aramex's and Smsa's services: CM-PAY-029;
  - Aramex's free packaging materials, مواد تغليف مجانية: CM-SHP-021;
  - Aymakan's storage, preparation and shipping in its description: CM-SHP-011;
  - Redbox's smart lockers: CM-SHP-019;
  - Prolo's refrigerated type, cold / مبرد: the new thing below.

  Regular and economy shipping (عادي, اقتصادي) and door-to-door delivery are the carrier's shipping itself, CM-SHP-015's own thing. The concern map keeps the plan lines on regular and economy shipping through named carriers on CM-SHP-015 and CM-SHP-002, so they take no line of their own: their terms are on CM-SHP-015, their prices on CM-SHP-002. Aramex's 'الاستلام و التسليم من مختلف فروعنا' stays on CM-SHP-015, as the model keeps collection at a carrier's branch there (CM-SHP-019's reading of SA-S-2020). Redbox's lockers go to CM-SHP-019, because the App Store's Redbox app says the buyer collects orders from them by a code (line 521).
- **D1. A section type of the theme editor** (26 to 41): `core` on CM-SFR-002. Each is listed under 'Add new section' in the editor of the theme رائد (step 010, lines 19 and 24 to 39), as SA-40 placed a theme's custom components on CM-SFR-002 `core`. A section whose name names another capability's thing takes a `shows` line there, since what it draws on isn't stated: Brands on CM-CAT-005, the two testimonials sections on CM-SUP-001, and Promotion on CM-MKT-001. A section of images, sliders, products, links, a banner or a video is layout and takes no second line.
- **T1. A theme of the marketplace** (42 to 49): `extension-point` on CM-SFR-003, its developer as filler and its price and sale price as quality, as SA-40's rule 2 placed the themes developers publish.
  - The `developer` field is shown to merchants: the locale labels it 'Developer' and 'More themes by {{developer}}' on a theme's details page (`marketplace.details.developer`, `.developer_themes`). So it is a maker statement, as the App Store's company is (the ruling after SA-17, and the ruling after WC-4 that a maker field must be one merchants are shown).
  - None of the eight names Salla.
- **T2. A theme's key features take their own lines** where a capability holds the thing (M-8): Hamsa Nabd's offer bar, social proof and trust badges, sticky purchase bar and editable settings.
  - Carmela's list of what its 49 components make is named in passing, so it takes no line (the ruling after SA-41).
  - The theme's layout of the store's own content takes none either: the mega menu, the category icons, the hero banners and the brand grid. The alternative is lines on CM-CNT-005, CM-CAT-003, CM-SFR-007 and CM-CAT-005, each of which would change a cell.
- **T3. A tag of the marketplace** (50 to 67): `extension-point` on CM-SFR-003. A tag is a category of the platform's marketplace of themes, listed under 'Discover themes for your industry' (step 001, lines 73 to 92), as SA-1 placed the App Store's categories (SA-1:20). An industry names whom the themes are for, not a capability, as the ruling after SA-2 and SA-5 reads a sector's link. So Digital products (CM-SEL-002), Charity (CM-SEL-007), Services and Accessories and gifts (CM-LOY-006) take no second line.

**Earlier lines kept to:**
- SA-13:4 and SA-18:61: CM-SHP-015 `core`, the carriers' page and link.
- SA-27:47 to 49: CM-SHP-015 `extension-point`, the type-app carriers.
- SA-2:51: CM-SHP-002 `core`, the carriers within Salla's labels.
- SA-49's R1.
- SA-1:20: a marketplace's category is `extension-point`.
- SA-40's rule 2 and its SA-E-2557cc9e: developers' themes on CM-SFR-003; a theme's custom components on CM-SFR-002 `core`.
- The ruling after SA-17, applied to read the carriers' apps' makers and the themes' `developer` field.

SA-2:82's `core` for SPL on CM-SHP-015 rests on Salla's changelog post. Entries 12 and 23 show SPL's own app, so I placed them `extension-point`, as SA-27:48 did. The ruling after SH-53 (the platform's own themes are `core`) applies to no entry here: none is stated to be Salla's.

## `new` things

- **Refrigerated shipping** (entry 7, SA-E-e0239281, Prolo, both stores; one line, `shows`, Prolo its filler):
  - **What it is:** the carrier's one shipping type, `name: cold; label: مبرد`, within Salla's labels (price 24, 'الشحن 1 - 5 ايام عمل'). Both stores' shipping pages name it in their filter 'Refrigerated shipping' (step 068 line 49; step 269 line 47).
  - **Place of its own:** none. It is a type in a carrier's list and an option of a page's filter.
  - **Proposed:** domain C, area SHP, parent CM-SHP-015 (or CM-SHP-001).
  - **Names:** 'Refrigerated shipping' in English, 'مبرد' in Arabic (the type's label); key `cold`.
  - **Searched:** refrigerated; cold; مبرد; تبريد; chilled; cold chain (`caps --terms`); `held/new.tsv`: nothing. SA-2:82's reading records that SPL's changelog post names no refrigerated shipping.
  - **Leads:** the entry's only lead, CM-MKS-006, comes by 'salla' and 'عمل', words every carrier entry holds: no lead (the checker's NOTE on line 29).

## The `CHANGES` lines, and what I decided on each

1. **CM-SHP-020 gains `extension-point`** (lines 5, 12, 17, 59, 66, 71: the international type of Aramex, Smsa and Dhl on both stores).
   - The carrier ships abroad within Salla's labels, its own service named in the platform's list (C5). The cell already holds the readiness page and Salla's fee on international shipping, and its note keeps Shopify's help section International shipping here.
   - Kept. The alternative reads the type as a grain of CM-SHP-002, like regular and economy shipping: no line, and no change.
2. **CM-SHP-003 becomes held, `extension-point`** (lines 6, 60: Aramex's insured type, both stores).
   - `name: insured; label: مؤمن`, price 24, in Salla's labels: insurance on a shipment sent with the platform's labels, the capability's own definition. The cell's homonym (تأمين as securing packaging) doesn't apply: the key is `insured`.
   - Kept. Who insures, and for what cover, isn't stated. If Salla's labels sell the insurance themselves, the line is `core`.
   - What would settle it: the label creation screen's insured option, or a help article on Salla's insured shipping.
3. **CM-PAY-029 gains `extension-point`** (lines 7, 13, 61, 67: cash on delivery in Aramex's and Smsa's services).
   - The carrier collects through the platform's carriers list (C5; SA-49's R1).
   - The cell's split puts Salla's settlement from its labels' carriers in `core` (SA-S-0122) and the merchant's own carrier in `outside`. These carriers are Salla's labels', and nothing here says who settles.
   - Kept. The alternative is `core` with the carrier as filler, which changes nothing.
4. **CM-SHP-021 gains `extension-point`** (lines 8, 62: Aramex's free packaging materials).
   - The carrier supplies them, its own service named in the platform's list. The request goes through the platform's Packaging page ('Packaging materials', step 068 line 39).
   - The cell reads the approved carriers' supply as `outside` (SA-S-5069). Here the platform's interface is named.
   - Kept.
5. **CM-SHP-019 becomes held, `extension-point`** (lines 25, 79: Redbox's smart lockers).
   - 'خزائن ذكية لإستلام و شحن الطرود', and the App Store's Redbox app (company 'سلة'): 'الخزائن الذكية التي يستطيع عميلك استلام طلباته منها عبر رمز يرسل إلى جواله'.
   - This is shipping to pickup points, which the cell's note leaves undefined. A reading.
   - Kept. What would settle it: a checkout offering a Redbox locker as the buyer's delivery option.
6. **CM-SUP-003 becomes held, `extension-point`** (line 113: Hamsa Nabd's 'Instagram gallery to build social proof with your customers' and 'Trust badges (fast shipping, free returns, secure payment) displayed below the header').
   - A third party's theme sold in the platform's marketplace offers the capability's own two words, social proof and trust (M-8).
   - Kept. The capability is undefined on both platforms (its note), and the cell's note also names Salla's own component salla-trust-badges, not cited.
7. **CM-SFR-007 gains `extension-point`** (line 112: Hamsa Nabd's 'Fully customizable scrolling offer bar with discount codes').
   - A bar across the storefront, the cell's top bar, offered by a theme. Kept.
8. **CM-CHK-008 gains `extension-point`** (line 114: Hamsa Nabd's 'Sticky mobile purchase bar to streamline the checkout process').
   - Read by its role: it shortens the buyer's way to buying, as the cell's quick purchase does. The weakest of the theme's four.
   - What would settle it: the theme's preview, showing whether the bar adds to the cart or buys directly. Without it, the alternative is no line.
9. **CM-SFR-002 gains `extension-point`** (line 115: Hamsa Nabd's 'Fully editable colors, fonts, and text via the control panel—no coding required.').
   - The theme's own settings, edited in the platform's editor without code: a developer's settings through the editor. The editor itself stays `core`.
   - Kept.

## The checker's `NOTE` lines

- **Line 29:** a new thing whose entry has leads (CM-MKS-006). Read and set aside (above).
- **Line 104 (entry 36, Store Features):** the first lead CM-EVO-001 holds nothing. It comes by 'features' and is a homonym: WooCommerce's feature settings, which the merchant enables or disables, against a homepage section showing the store's features. No line.
- **Line 117 (entry 44, carmeela):** the first lead CM-B2B-007 holds nothing. It comes by 'storefront' in 'create rich and flexible storefronts', and is a homonym (BigCommerce's buyer portal), as CM-CHN-007, by 'storefronts', is too. No line.

## Entries I couldn't tell, and what would settle each

- **C1's support** on the eight carriers whose apps are Salla's (above). The coordinator's reading of the ruling after SA-17 for carriers of Salla's labels would settle it.
- **31 and 35, the testimonials sections, `shows` on CM-SUP-001** (reviews and ratings, whose cell holds store-rating). CM-SUP-003 (social proof) is the alternative, a CHANGES line. The section's form, or the storefront's rendering, would say whether it shows the store's ratings or text the merchant enters.
- **41, Promotion, `shows` on CM-MKT-001.** It may show an offer (CM-MKT-003), a code (CM-MKT-002) or only a banner. The section's form would settle it.
- **36, Store Features:** no second line. If the section shows trust badges (free shipping, secure payment), it is CM-SUP-003's too. The section's form would settle it.
- **The six `custom_component` sections (26 to 31):** custom components of the theme. Neither their maker nor Raed's is stated in these sources, so `core` rests on the editor offering them. A statement of who makes رائد would settle it: the marketplace's summary (`theme-marketplace-summary`, held, not selected), or the theme's page.
- **50 to 67, the tags:** `extension-point`, as an app category is. Some themes are Salla's (below), so a tag holds both kinds. `core` is the alternative. No cell changes either way.

## A structure whose items and sources disagree

- **`shipping-carriers` `public-demo@en`:** the source's pagination says `total: 17`, `totalPages: 2`. Page 2's one carrier isn't held, a gap. The real store's list is whole (15 of 15): it lacks أفق السرعة and holds no carrier the public demo lacks.
- **The rendering leaves out item keys:** a carrier's `id` and `logo`; a theme's `id`, `image`, `version`, `customizable_message` (null), `components` (empty), `template_preview_url` (null) and `position`. No statement is lost.
- **The marketplace page against the source:** the page shows 'Try for free' beside each theme (step 001, lines 93 to 140), while each theme's `has_trial_version` is false. The source governs.
- **`theme-design-components` holds only `data.blocks`.** Its `store_blocks` and `bundles` reach no entry (below).

## What sources state that no entry holds (for the second stage)

- **The editor's bundles,** `theme-design-components/raed@demo-en/source.json`, `data.bundles`: six ready-made sets of sections with their blocks, which step 010 lists at lines 40 to 75 with Arabic names such as بنر إعلاني متحرك, عداد تنازلي and الأسئلة الشائعة:
  - Bedaya (`is_landing_page_template: true`);
  - Creative & Visual Excellence;
  - Attraction and impact bundle;
  - Trust & Professionalism;
  - Recommended by Mushammir;
  - Ai Generated Bundle (1).

  These are leads for CM-SFR-005 (Component Bundle), CM-SFR-006 (a landing page template) and CM-AIA-001 (Mushammir, an AI-generated bundle).
- **The editor's placed section,** `data.store_blocks`: 'Products on Your Taste' / منتجات على ذوقك, slug `bundle_component`, with `is_visible`, `can_be_deleted`, `allowed_copies: 0` and `can_be_sorted`. Leads for CM-SFR-002 and CM-SFR-005.
- **The editor itself,** step 010:
  - 'Buy bundles' (line 20): CM-SFR-005;
  - 'ميز متجرك' and 'إنشاء عنصر بالذكاء الإصطناعي' (lines 22, 23): creating a section with AI, CM-AIA-001;
  - 'Beta' beside 'Homepage' (lines 4, 5).
- **The shipping page,** step 068:
  - lines 27 to 34: 'Create shipping labels in one click', 'Discounted shipping rates', 'Local, GCC, and global reach', 'Track shipments in real-time', 'Instant setup, no fees', 'Simplified returns handling', 'One unified dashboard', 'Advanced shipping performance reports'. Leads for CM-SHP-002, CM-SHP-017, CM-RET-003 and the shipping reports;
  - the filters 'Express shipping' and 'Freight shipping' (lines 46, 50), which no held carrier's type holds.
- **The marketplace page,** step 001:
  - 'Suggested themes', 'Popular themes', 'Latest themes', 'Discounts', 'Free themes' (lines 19 to 23);
  - 'Discover section bundles that give you more control over your store design.' (line 143), with eight bundles priced (lines 146 to 185): CM-SFR-005;
  - 'Themes created by Salla partners' (line 186): CM-SFR-003.
- **The marketplace's locale,** `dashboard-translations/en/themes-marketplace-monorepo.json`:
  - `faqs.question2` 'Are all themes developed by Salla?' and `faqs.answer2` 'Some themes are developed by Salla, and others by Salla partners.';
  - the filter `filters.developer`: 'Developed by', with 'Salla' and 'Salla Partners'.

  This is maker evidence for Salla's own themes, `core` on CM-SFR-001 by the ruling after SH-53, and for partners' themes, `extension-point` on CM-SFR-003.
- **The App Store's carrier apps,** `marketplace-apps/api@ar/items.jsonl`:
  - Aramex's 'أسعار حصرية لتجار سلة' (line 804);
  - Logistiq's 'رسوم شحن تنافسية تبدأ من 25 ريال سعودي' (line 573);
  - Naqel's 'تغطي جميع أنحاء المملكة' (line 518).

  These are qualities of the carriers. The four apps with company 'سلة' (Aramex 1311345502, Smsa 1683195908, Aymakan 944213936, Redbox 1910472440) are leads for CM-APP-011, the platform's own apps, as the ruling after SA-17 says of the 83.
- **The carriers' fields** `is_special_price`, `is_recommended`, `activate_kyc_policy` and `is_unified`: false on every carrier held. They name things the platform can mark on a carrier (a special price, a recommendation, a KYC policy on activation), and no held value is true. Leads.

## Problems with the brief or the script

- **The checker's quote finder reads a plural possessive's apostrophe as a quote mark.** In 'the carriers' ratings', following a quote, it took the text between the quote and the possessive as a quote and reported it found nowhere. I rephrased the readings ('the ratings of the carriers').
- **No rule of this brief reads differently from B-extent.md here.**
