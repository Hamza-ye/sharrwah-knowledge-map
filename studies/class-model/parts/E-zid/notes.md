# E-zid: notes

Domain E, Store presence and channels: Zid mapped onto the model of E-anchor and E-woocommerce. The part runs in two
batches. Read through `class_slice.py` only: `seed`, `model --areas`, `concerns --where`, `statements`, `gaps`,
`matches`, `key`, `search`, `caps` and `candidates`. Searches are in English and Arabic, singular and plural, with and
without ال. Every placement below is a reading of the statements cited. Nothing outside the concern map is cited.

## Batch 1: SFR, CNT and CHN

Concerns: ZD-C-075, ZD-C-076, ZD-C-096, ZD-C-113, ZD-C-039, ZD-C-093, ZD-C-102, ZD-C-109, ZD-C-110 and ZD-C-116. Zid's
cell is written for all 27 capabilities of the three areas (13 SFR, 8 CNT, 6 CHN) and for the one this batch adds
(CM-CNT-009): 28 cells, 19 citing statements, 9 `none-held` (CM-SFR-004, CM-SFR-007, CM-SFR-009,
CM-SFR-010, CM-SFR-011, CM-CNT-001, CM-CNT-006, CM-CHN-004, CM-CHN-005).

### How the concerns landed

| Concern | Lands in | Join | Fit |
|---|---|---|---|
| ZD-C-113 Online store and store design | CM-SFR-001 | terms | strained |
| ZD-C-076 Theme Market and themes | CM-SFR-003 | terms | clean |
| ZD-C-096 Domains | CM-SFR-008 | terms | clean |
| ZD-C-075 Storefront APIs | CM-SFR-012 | role | clean |
| ZD-C-039 Store legal pages | CM-CNT-008 | role | strained |
| ZD-C-093 Blogs | CM-CNT-004 | terms | clean |
| ZD-C-102 URL redirects | CM-CNT-009 (new) | single | clean |
| ZD-C-109 Mazeed marketplace | CM-CHN-002 | role | clean |
| ZD-C-110 Sales channels (marketplaces) | CM-CHN-003 | role | clean |
| ZD-C-116 Store mobile app | CM-CHN-006 | terms | clean |

Nine joined existing capabilities; one made a new one. None moved.

- **New capability CM-CNT-009, URL redirects.** Zid gives it a place of its own, a page in Settings (ZD-S-0967), so it
  meets the dry run's convention. No capability holds redirects: CM-CNT-006 (Salla's Custom URLs) is kept apart from
  redirects by its own note, since no Salla statement defines a custom URL; `caps --terms "redirect; إعادة توجيه; ..."`
  finds nothing in another domain (domain G's CM-MIG-001 is import and export, not redirects, though Zid's reason for
  redirects is a move from another platform, ZD-S-0968). Numbered past CM-CNT-008. A root: no statement puts it under
  another capability. **For the coordinator:** a back-fill (E-backfill-zid) needs Shopify's, Salla's and WooCommerce's
  cells for CM-CNT-009. The seed names Shopify redirects under CNT, but E-anchor found no Shopify statement of their own
  (CM-CNT-006's note).
- **ZD-C-075 in CM-SFR-012, not CM-SFR-011.** Zid's API's groups are customer-facing (the Role header Customer,
  ZD-S-0894); no Zid statement shows headless or custom storefronts, so the child, as WooCommerce's Store API.
- **ZD-C-110 in CM-CHN-003, not the parent CM-CHN-001.** Its statements are all about external marketplaces (Amazon,
  Trendyol, Jahez) and their sync. Its term منصات البيع names the dashboard section that also holds Mazeed; that
  section's route (ZD-S-0985, of ZD-C-109) is cited in CM-CHN-001.

### Grains chosen

- **ZD-C-113 is the whole Store Design plan group** (تصميم المتجر), coarser than CM-SFR-001. It lands in CM-SFR-001 and
  its lines go where each names: theme code and customization (ZD-S-1001, ZD-S-1002, ZD-S-1075, ZD-I-0329) in
  CM-SFR-002; Landing Page (ZD-I-0332) in CM-SFR-006; Search Bar, Filtering and Filter Criteria (ZD-I-0326, ZD-I-0330,
  ZD-I-0331) in CM-SFR-013; the main menu (ZD-S-1074) in CM-CNT-005; Manage additional pages (ZD-I-0539) in CM-CNT-003;
  API's > Storefront [Store Scripts] (ZD-S-0051) in CM-SFR-012.
- **The permission manage.store.front.customization** (Customize store front, ZD-S-0489) is cited in CM-SFR-001, as
  Salla's store_design_management is: its words name the storefront as a whole, not the theme's code.
- **API's > Storefront [Store Scripts]** (ZD-S-0051) is cited in CM-SFR-012 as a page of Zid's storefront API group, not
  in CM-SFR-004. A script tag is CM-SFR-004's on Shopify, but no Zid statement says apps or the merchant add the
  scripts; the statement is a page title only. A reviewer reading the page itself may move it.
- **API's > Storefront [Pages]** (ZD-S-0783) is cited in CM-CNT-003, not CM-CNT-008, though Q1 placed it in the legal
  pages concern: its words name pages.
- **The API groups API's > Products, Categories, Account and Countries** (ZD-I-0047, ZD-I-0048, ZD-I-0050, ZD-I-0052)
  are cited in CM-SFR-012: Q1 placed them in ZD-C-075 only, not in domain B's or the markets concerns, so they don't
  count a feature's own API twice (unlike WooCommerce's Store API routes, see E-woocommerce's notes).
- **The blog's API groups** (ZD-I-0036 to ZD-I-0041) are cited in CM-CNT-004, Blogs > Storefront > Posts among them,
  not in CM-SFR-012: they are under Merchant APIs > Blogs.
- **Mazeed** is CM-CHN-002, and its route under Sales platforms (ZD-S-0985) is cited in both CM-CHN-001 (the section)
  and CM-CHN-002 (activating Mazeed), one tree.

### Joins on role

- **CM-SFR-012 / ZD-C-075:** Zid's API's (customer role) with Salla's storefront APIs (SA-S-5140) and WooCommerce's
  Store API (WC-S-0914). No Zid statement calls them a storefront API.
- **CM-CNT-008 / ZD-C-039:** Zid's legal pages (ZD-S-0779, ZD-S-0780) with Shopify's Policies (SH-S-7087) and Salla's
  information pages carrying policies (SA-S-2100).
- **CM-CHN-002 / ZD-C-109:** Mazeed (ZD-S-0984, ZD-S-0989) with Salla's Mahally (SA-S-0005) and Shopify's Shop
  (SH-S-0723).
- **CM-CHN-003 / ZD-C-110:** Zid's Marketplaces (ZD-S-0458, ZD-S-1065) with Shopify's Marketplace Connect (SH-S-0727)
  and Salla's الربط بمنصات التسوّق العالمية (SA-S-2195).

### Homonyms

- **القائمة الرئيسية** names two things on Zid: a plan line under store design (ZD-S-1074), read as the store's main
  navigation menu and cited in CM-CNT-005; and the dashboard's own menu ("من القائمة الرئيسية ← الطلبات ← زد فويس",
  ZD-S-1067, domain C), not cited.
- **product.publish** (ZD-I-0062, a webhook topic of domain B): Salla's product.publish is "product published in a new
  sales channel" (SA-S-1606, CM-CHN-001); no Zid statement defines Zid's, so the same word isn't shown to name the same
  thing. Not cited in CM-CHN-001.
- **Store / Storefront.** Zid's API's > Storefront (ZD-I-0051) is one group of its customer-facing API's; it is not
  Shopify's Online Store or WooCommerce's Store API by name.

### Strained fits

- **ZD-C-113 in CM-SFR-001:** its lines are cited in other trees: CM-SFR-013 (ZD-I-0326, ZD-I-0330, ZD-I-0331),
  CM-CNT-005 (ZD-S-1074), CM-CNT-003 (ZD-I-0539), CM-SFR-012 in tree CM-SFR-011 (ZD-S-0051).
- **ZD-C-039 in CM-CNT-008:** its API's > Storefront [Pages] (ZD-S-0783) is cited in CM-CNT-003.

### Concerns read under `also`

- **ZD-C-024** (domain C, Mazeed collections and dues): its route لوحة التحكم > منصات البيع > مزيد (ZD-S-0702) is cited
  as `core` in CM-CHN-002, and Mazeed's own payment gateway (ZD-S-0703) as `shows`. Its collections, payout schedule
  and commission (ZD-S-0704 to ZD-S-0712) are domain C's subject, not cited.
- **ZD-C-103** (domain D, Google Maps) and **ZD-C-104** (domain C, working hours and closing the store, ZD-S-0970):
  read, not cited; neither bears on SFR, CNT or CHN as the statements stand. Batch 2 may weigh them.

### Statements of other domains cited (the checker's flags)

Cited only where the cell would otherwise be `none-held`, as B-zid and D-zid did:
- App Market categories of ZD-C-070 (domain F, no `also`), as `extension-point` in the capability each names:
  تحسين واجهة المتجر (ZD-I-0436) and المحتوى المرئي والقصص (ZD-I-0450) in CM-SFR-005; SEO وتحسين الظهور (ZD-I-0463)
  in CM-CNT-007; قنوات البيع (ZD-I-0452) in CM-CHN-001; تطبيقات الجوال للمتجر (ZD-I-0437) in CM-CHN-006. They support
  `extension-point`, never `core`, so they don't count a core placement in two domains. ZD-I-0450 is a reading: its
  name, visual content and stories, is read as a storefront addition like Shopify's Image and media apps; it is under
  the group زيادة المبيعات والتحويل (sales and conversion), and a reviewer may leave it out.
- **ZD-I-0300** (Store SEO Customization, ZD-C-106, domain D): D-zid's notes leave it to domain E. Cited as `core` in
  CM-CNT-007.
- **ZD-S-0963** (Custom Fields, ZD-C-100, domain C with `also` B): cited as `core` in CM-CNT-002, as WooCommerce's cell
  cites a domain-B concern's product custom fields. B-zid left it to domain C. **For the coordinator:** if domain C's
  parts cite it as `core` too, the merge will flag it; one domain should hold it.

### Other flags answered

- **own-service on ZD-S-0898** ("تمتلك زد حقوق الملكية الفكرية للثيمات التابعة لها"): it names Zid's company as owner
  of its own themes' intellectual property. Read as naming Zid the maker of the themes of its own that the Theme Market
  offers beside partners' themes (ZD-S-0897). A reading; ownership of IP is not stated to be making.
- **own-service on ZD-S-0989**: the merchant authorizes "زد متمثلة في منصة مزيد" as the seller's legal representative;
  it names Zid's company as the one that runs Mazeed. Mazeed's name doesn't carry Zid's brand, so the statement, not the
  name, places it.
- **none-held CM-SFR-004:** the matches are Zid's embedded apps (ZD-C-073, ZD-S-0885 to ZD-S-0887, ZD-S-0123,
  ZD-I-0125), which open inside the merchant dashboard, not the storefront; an embedded payment checkout (ZD-S-0598,
  domain C); and Store Scripts (ZD-S-0051), cited in CM-SFR-012 (above).
- **none-held CM-SFR-007:** the one match is the blog's reason (ZD-S-1044), naming paid advertisements, not a banner.
- **none-held CM-CNT-001:** the matches are files of other things: downloadable products' upload to S3 (ZD-S-0801),
  exported files (ZD-S-0804, ZD-S-0805), B2B tax invoices as attachments (ZD-S-0711), a file of customers to upload for
  abandoned-cart messages (ZD-S-1071), and the blog posts' Media (ZD-S-0936, ZD-I-0038, the blog's). None is a library
  of the store's files.
- **none-held CM-CHN-005:** the matches are the Dropshipping App Market category (ZD-I-0446, cited by B-zid in
  CM-CAT-010) and a payment-processing suppliers clause (ZD-S-0679); neither names Zid's other stores.

### Gaps

- **Maker statements:** the blog is reached on a separate "Blog platform" (ZD-S-1041) and called "the app" (ZD-S-1043);
  the sales channels connection app (تطبيق ربط قنوات البيع, ZD-S-1062); the mobile app built by عناقيد التطبيقات
  (ZD-S-1081). No statement names who makes the first two, or how عناقيد التطبيقات relates to Zid's company. Each cell
  is placed by what its statements show.
- **Definitions:** the Landing Page, Search Bar, Filtering and main menu lines (ZD-I-0332, ZD-I-0326, ZD-I-0330,
  ZD-I-0331, ZD-S-1074) are names only; Store Scripts and Pages (ZD-S-0051, ZD-S-0783) are page titles only.
- **Q1's gaps that bear on cells:** ZD-C-075/decides (what turns the storefront API's on, searched, not found);
  ZD-C-102/decides (`observation needed`) and ZD-C-102/boundary (no API); ZD-C-113, ZD-C-075, ZD-C-093, ZD-C-102 and
  ZD-C-110/responsible, stated only in general terms; no reason stated for ZD-C-113, ZD-C-075, ZD-C-076, ZD-C-096 and
  ZD-C-039.
- **Not cited:** the help-centre headings سوق الثيمات › الصفحات (ZD-I-0184) and سوق الثيمات › تحسين محركات البحث
  (ZD-I-0183), titles that show neither what pages nor what SEO; the product lines Themes, E-store's duplicate, Mazeed
  Marketplace and Marketplaces (ZD-I-0471, ZD-I-0464, ZD-I-0472, ZD-I-0475), covered by statements; the theme legal
  agreements (ZD-I-0418, ZD-I-0427, ZD-I-0428) and the Rise domain card (ZD-I-0379), covered by the statements cited.

### Proposed renames (for the coordinator)

- CM-SFR-003: add Zid's Theme Market / سوق الثيمات.
- CM-CHN-002: add Zid's Mazeed / مزيد.
- CM-CHN-003: add Zid's Marketplaces / منصات البيع.
- CM-CNT-008: add Zid's legal pages / الصفحات القانونية.

### Rulings

None. Q1's unclear candidates cover Shopify, Salla and WooCommerce only (`matches`); Zid has none. `rulings.tsv` holds its
header only.

### For batch 2 (areas POS and MKS)

- Your concerns: ZD-C-033 (countries and cities), ZD-C-034 (Markets / الأسواق), ZD-C-050 (languages and currencies),
  ZD-C-108 (Zid POS / زد كاشير). Read the model with `model --domain E --areas POS,MKS`.
- **API's > Countries** (ZD-I-0052, an entry of ZD-C-075) is cited `core` in CM-SFR-012 as a group of the
  customer-facing API. If an MKS cell needs it, cite it as `shows`, or say why in a note, so it isn't `core` in two
  trees; Merchant APIs > Countries and Cities (ZD-S-0035, ZD-C-033) is yours and uncited here.
- **Reports - Sales Channels** (ZD-S-1049, domain D) names POS among channels; D-zid cites it in CM-ANL-002. Not cited
  here.
- **ZD-C-104** (working hours, closing the store temporarily, ZD-S-0970) and **ZD-C-103** (Google Maps) name E under
  `also`; batch 1 cited neither.
- The POS staff permissions (pos.cashiers.page ZD-I-0490, pos.homepage ZD-I-0497) matched the store-pages search in
  batch 1 and were not cited.
- The last batch checks the whole part without `--concerns` and `--areas`.

## The coordinator's corrections after batch 1 (30 October)

- **scope.tsv:** ZD-C-070, Zid's App Market, names D and E under `also`, since its categories are cited as `extension-point` for the capabilities they name in both; ZD-C-100 (custom fields) and ZD-C-106 (its SEO plan line) name E. If domain C also counts ZD-S-0963 as `core`, the merge flags it, and it counts once.
- **CM-CNT-009, URL redirects,** is new: `E-backfill-zid` writes its Shopify, Salla and WooCommerce cells after batch 2.

