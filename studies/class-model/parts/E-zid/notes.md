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


## Batch 2: POS and MKS

Concerns: ZD-C-108, ZD-C-033, ZD-C-034 and ZD-C-050. Zid's cell is written for all 13 capabilities of the two areas
(4 POS, 9 MKS): 9 cite statements, 4 are `none-held` (CM-POS-003, CM-POS-004, CM-MKS-002, CM-MKS-003). No capability
added. Read through `class_slice.py` only (`model --areas POS,MKS`, `statements`, `gaps`, `key`, `candidates`,
`search`, `caps`).

### How the concerns landed

| Concern | Lands in | Join | Fit |
|---|---|---|---|
| ZD-C-108 Zid POS / زد كاشير | CM-POS-001 | terms | clean |
| ZD-C-034 Markets / الأسواق | CM-MKS-001 | terms | clean |
| ZD-C-050 Store languages and currencies | CM-MKS-006 | terms | strained |
| ZD-C-033 Store country, operating countries and cities | CM-MKS-009 | terms | strained |

All four joined existing capabilities; none made a new one; none moved.

### Grains chosen

- **ZD-C-050 is coarser than any capability:** languages and currencies on one settings page (اللغات والعملات). It
  lands in CM-MKS-006, since most of its statements are about adding and showing other currencies (خاصية العملات,
  Salla's العملات). Its lines go where each names: the main currency (ZD-S-0806, ZD-S-0813, ZD-S-0808 as `shows`) in
  CM-MKS-005; languages (ZD-S-0813, ZD-I-0140) in CM-MKS-008; exchange rates (ZD-S-0809 to ZD-S-0812) in CM-MKS-007;
  Geo-Based Currency Settings (ZD-S-0807) in CM-MKS-004.
- **ZD-C-033** holds the countries API and the store's own country. The API (ZD-S-0035, ZD-S-0117, ZD-S-0744) is
  CM-MKS-009. Activating a country's currency turns on shipping to it (ZD-S-0745): cited in CM-MKS-001 as a
  per-country setting of where the store sells, a reading, as WooCommerce's Shipping location(s) there. **One thing, one
  domain:** changing the store's country in its settings (ZD-S-0746, with the wallet balance zeroed first) is the
  store's details, domain A's CM-ACC-006 (`caps --terms "store details; ..."`); "تحديد موقعك أو موقع المخزون"
  (ZD-S-0747, scope مستخدمي دول الخليج) is read as the store's or the stock's location, CM-ACC-006 or domain B's
  CM-INV-005. Neither is cited here; both are left to those domains' cells, and the landing's reading names them.
- **ZD-S-0744** (GET /v1/managers/countries, "countries where the store operates", with ID, name, ISO codes and flag)
  is cited in CM-MKS-009 as the countries API's endpoint, not in CM-MKS-001. A reviewer who reads "where the store
  operates" as the store's selling countries may add it to CM-MKS-001, as WooCommerce's selling locations.
- **ZD-S-0750** (عملة السوق, a market's currency for showing prices) is cited in CM-MKS-006, the child, as Shopify's
  "Set a currency for a market in Markets" is, not in CM-MKS-001.
- **ZD-S-0806's route** names languages and currencies, but its words narrow it to currencies (the dry run's title
  against description), so CM-MKS-008 cites the settings entry لغة وعملات المتجر (ZD-I-0140) for the page.
- **The POS permissions** pos.cashiers.page (ZD-I-0490), pos.homepage (ZD-I-0497), pos.cashier.usage (ZD-I-0495),
  pos.analytics (ZD-I-0528) and pos.payment.methods (ZD-S-0506) are cited `core` in CM-POS-001, as Salla's
  salla_point_* permissions are. pos.payment.methods is cited there, not in CM-POS-002: its words name payment methods,
  not devices.
- **The App Market category الربط مع الأنظمة (ERP/POS)** (ZD-I-0443, ZD-C-070, which now names E) is cited as
  `extension-point` in CM-POS-001, as Shopify's Selling in person apps, on its name only; not in CM-POS-004, which is
  apps inside the POS app.
- **Customer Display Screen** (ZD-I-0352), a plan line Q1 placed in Zid POS, is cited `core` in CM-POS-001 on its
  name only; nothing held says it is a device, so it is not cited in CM-POS-002.

### Joins on role

- **CM-MKS-004 / ZD-S-0807:** Zid's Geo-Based Currency Settings, "Automatically adjust currencies based on customer
  location", with Salla's currency shown by the customer's geographic location (موقع العميل الجغرافي). No Zid
  statement shows local domains or a country selector. The concern lands by terms in CM-MKS-006; this is a cell's join.

### Homonyms

- **السوق / Market:** Zid's الأسواق (Markets, ZD-C-034) is not its سوق التطبيقات (App Market, ZD-C-070) or سوق
  الثيمات (Theme Market, ZD-C-076), nor Mazeed Marketplace or Marketplaces (ZD-C-109, ZD-C-110). Only ZD-C-034's
  statements are cited in CM-MKS-001.
- **الكاشير:** Zid POS's cashier (ZD-C-108), not the cashback (الكاش باك) of the customer wallet (ZD-S-0667, domain D),
  which the POS-003 candidates found by the letters كاش.

### Strained fits

- **ZD-C-050 in CM-MKS-006:** ZD-S-0806, ZD-S-0808 and ZD-S-0813 are cited in CM-MKS-005, and ZD-S-0813 and ZD-I-0140
  in CM-MKS-008, both roots, other trees. The checker's three tree flags (ZD-S-0806, ZD-S-0808, ZD-S-0813) are this:
  Zid's one settings page and one API endpoint carry the store currency, the other currencies and the languages at
  once; the capabilities stay apart as the anchor cut them, and the statements are cited in each.
- **ZD-C-033 in CM-MKS-009:** ZD-S-0745 is cited in CM-MKS-001, another tree; ZD-S-0746 and ZD-S-0747 are left to
  domains A and B (above).

### Concerns read under `also`

- **ZD-C-070** (domain F, App Market): ZD-I-0443 cited as `extension-point` in CM-POS-001.
- **ZD-C-103** (domain D, Google Maps, ZD-S-0969): enabling Google Maps in the store, for addresses (CM-CUS-009);
  not MKS-004's geolocation of markets. Not cited.
- **ZD-C-104** (domain C, working hours): bears on no POS or MKS capability. Not cited.
- ZD-C-024, ZD-C-100, ZD-C-106: nothing for POS or MKS.

### Statements of other domains read, not cited

- ZD-S-1021 (ZD-C-085, domain B): on الباقة الاحترافية, with Zid Cashier on, one more warehouse per device.
- ZD-S-0620 (ZD-C-012, domain C): the payment methods API doesn't return the payment methods configured in POS.
- ZD-S-0828 (ZD-C-053, domain C): ZATCA e-invoicing "متاح الربط مع الكاشير".
- ZD-S-1049 (ZD-C-105, domain D): Reports - Sales Channels names POS; D-zid cites it.
- ZD-I-0256, Request Inventory via POS: Q1 placed it in ZD-C-108, but `candidates` marks it domain B; its subject is
  stock, left to domain B's inventory cells.
- Currency statements of Zid's wallet and fees (ZD-S-0654, ZD-S-0655, ZD-S-0673, domains A and C): not the store's
  selling currencies.

### Flags answered

- **own-service on ZD-S-0977** ("زد كاشير: هي خدمة تقدمها زد"): read as naming Zid's company as the provider of a
  service, its POS app, as batch 1 read ZD-S-0989 and Salla's cell reads SA-S-0006. "زد" may name the platform, not the
  company: a reviewer may make it `core`, which the plan lines and permissions already support.
- **none-held CM-POS-003:** ZD-S-0728 is the Kuwait Zid Pay contract's governing law, matched by a term's letters; no
  drawer, shift or till is held.
- **none-held CM-POS-004:** ZD-I-0540 to ZD-I-0543 are subscription and shipping app extension points.
- **none-held CM-MKS-002 and CM-MKS-003:** the matches are listed in the cells' readings; none is a scheduled store
  change or a merchant of record.
- The other flags are batch 1's, answered in its section.

### Qualities and slot fillers

- Qualities: Zid POS on Professional (ZD-S-0382); the e-invoicing approval "اعتماد من الهيئة" (ZD-S-0983, the
  Authority not named further); markets by plan (ZD-S-0749); Geo-Based Currency Settings by plan (ZD-S-0807, "1" on
  starter and launch, a count the statement doesn't explain); the payment currency with Zid Payments (ZD-S-0808).
- Slot fillers: الوكيل (the agent) for the devices' warranty (ZD-S-0981), a role, not a named company, so a reviewer may
  drop it; KNET (كي نت), paid in Kuwaiti dinars (ZD-S-0808, scope Zid Payments, Saudi Arabia and Kuwait).

### Gaps

- **ZD-C-108/responsible** (observation needed): which acquirer settles card payments on Zid POS devices. CM-POS-002
  names no card-present provider; nor does any statement name who sells the devices (the agent only warrants them).
- **ZD-C-108/reason, ZD-C-034/reason, ZD-C-033/reason, ZD-C-050/reason:** searched, not found.
- **ZD-C-034/boundary:** no API, scope or webhook for markets; no statement defines a market.
- **Translation:** none held; the languages cell shows only which languages the store supports.
- **Not cited, covered by statements cited:** ZD-I-0127 (ZD-S-0748), ZD-I-0357 (ZD-S-0807), ZD-I-0191 (ZD-S-0979),
  ZD-I-0399 (ZD-S-0382), ZD-I-0523 (ZD-S-0506), ZD-I-0035 and ZD-I-0119 (ZD-S-0035, ZD-S-0117); the help-centre
  headings ZD-I-0174 to ZD-I-0176. **Not cited, unexplained:** Merchant APIs > Account > Store (ZD-I-0002) and the
  scope third_store_details_read (ZD-I-0089), which Q1 placed in ZD-C-050; no statement ties them to the localization
  endpoint.
- **API's > Countries** (ZD-I-0052) stays `core` in CM-SFR-012 (batch 1), not cited in CM-MKS-009.

### Proposed renames (for the coordinator)

- CM-POS-001: add Zid's POS (Point of Sales) / زد كاشير.
- CM-MKS-001: add Zid's Markets / الأسواق.
- CM-MKS-004: add Zid's Geo-Based Currency Settings / ضبط العملات على الموقع الجغرافي.
- CM-MKS-006: add Zid's currencies / خاصية العملات.

### Rulings

None: Q1's unclear candidates cover Shopify, Salla and WooCommerce only, so none holds a Zid concern. `rulings.tsv`
keeps its header only.

### The whole part's check

`python3 -I method/check_class_part.py studies/class-model/parts/E-zid`: 0 problems, 14 flags for the reviewer
(14 landings, 41 cells, 136 evidence rows). No problem on batch 1's rows. The part still needs `E-backfill-zid` for
CM-CNT-009's Shopify, Salla and WooCommerce cells.
