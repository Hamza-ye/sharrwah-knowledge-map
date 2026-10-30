# E-woocommerce: notes

WooCommerce's concerns of domain E, mapped onto the model E-anchor built. The part runs in two batches. Read through
`class_slice.py` only: `seed`, `model --areas`, `concerns --where`, `statements`, `gaps`, `matches`, `key`, `search` and
`candidates`. Searches are in English, WooCommerce's only language in the concern map. Every placement below is a reading
of the statements cited. Context read in the WooCommerce release at `/home/user/woocommerce-release/11.2.1` informs
readings and is never cited.

## Batch 1: SFR, CNT and CHN

Three concerns: WC-C-079, WC-C-107 and WC-C-111. WooCommerce's cell is written for all 27 capabilities of the three
areas: 13 SFR, 8 CNT, 6 CHN. 14 cells cite statements, 13 are `none-held`.

### How I cut

| Concern | Lands in | Join | Fit |
|---|---|---|---|
| WC-C-079 Store API | CM-SFR-012 | match:M-056 | strained |
| WC-C-107 Store content and customization extensions | CM-SFR-005 | role | strained |
| WC-C-111 Storefront design (themes and block patterns) | CM-SFR-001 | match:M-014 | clean |

All three joined existing capabilities; none made a new one. No capability is added: every WooCommerce statement of the
three areas found a capability of the model, or belongs to another domain (below).

- **WC-C-079 in CM-SFR-012, not CM-SFR-011.** M-056 holds Shopify's SH-C-139 (landed in CM-SFR-011, headless storefronts
  as a whole) and Salla's SA-C-101 (landed in CM-SFR-012, the storefront API). Q1's granularity note says Salla's and
  WooCommerce's concerns are the storefront API only, so WooCommerce's goes with Salla's, in the child. Same tree, so the
  match isn't split.
- **WC-C-079 is strained** (S1): the Store API's routes are the same statements as other concerns' own APIs, already
  cited in B's CM-CAT-001 to CM-CAT-006 (products, attributes, categories, brands, tags), D's CM-LOY-005 (shopper lists),
  CM-MKT-002 (cart coupons) and CM-SUP-001 (product reviews). CM-SFR-012 cites the API as a whole (WC-S-0914, WC-S-0941,
  WC-S-0081, WC-S-0915), the one route no other concern holds (/batch, WC-S-0148), and its extension points. I didn't cite
  the cart and checkout routes (WC-S-0149 to WC-S-0163, held also by WC-C-072, WC-C-073, WC-C-074, WC-C-075, WC-C-087):
  they are domain C's features' own API, and citing them as `core` here would count them in two domains.
- **WC-C-107 joins CM-SFR-005 on role.** Its Marketplace category Store content and customizations (WC-S-0703) holds
  third parties' additions to the storefront, the role of Shopify's Store design apps (SH-S-2662) and Salla's Component
  Bundle (SA-S-1165). Its subcategories go where Shopify's matching App Store categories go: Search and navigation
  (WC-S-0743) to CM-SFR-013, as Shopify's Search and navigation apps; Product images and media (WC-S-0742) and Store page
  enhancements (WC-S-0744) to CM-SFR-005, as Shopify's Image and media apps and Product display apps. Strained: WC-S-0743
  is in another tree (CM-SFR-013), and WC-S-0742 is also cited in domain B's CM-CAT-007.
- **WC-C-111 is clean.** Its statements sit in CM-SFR-001 and its children CM-SFR-002 (Customize your store, WC-S-0419),
  CM-SFR-003 (Marketplace category Themes, WC-S-0695) and CM-SFR-005 (the patterns route, WC-S-0178). The patterns route
  goes to CM-SFR-005, design elements beyond the theme, because WC-C-111's own name calls them block patterns; read in the
  release, the route fetches patterns and registers them as block patterns (context).

### WordPress, not WooCommerce

The task asks to say where WordPress does a thing. In each case the cell places by WooCommerce's own statements only; no
statement held says what WordPress does, so each is a reading.
- **Themes and their editing** (CM-SFR-001, CM-SFR-002): the theme and the Site Editor or Customizer are WordPress's.
  WooCommerce's statements show its onboarding tasks Choose your theme and Customize your store and its admin API around
  them. In the release, the Choose your theme task is actioned on WordPress's theme-install.php, and Customize your store
  completes when WordPress's global styles, templates or Customizer are saved (context).
- **Pages, blog, menus, files** (CM-CNT-003, CM-CNT-004, CM-CNT-005, CM-CNT-001): WordPress's pages, posts, menus and
  media library. CM-CNT-003 cites WooCommerce's settings section Page setup (WC-S-0022) as `shows`: what it does to pages
  isn't stated.
- **Domains, DNS, SSL** (CM-SFR-008 to CM-SFR-010): the site's address belongs to WordPress and its host; nothing held.

### Concerns read under `also`, and statements cited from concerns without it

Cited under `also` (they name E): WC-C-017 (F: WC-S-0923, WC-S-0834 in CM-SFR-003), WC-C-064 (B: WC-S-0675 in
CM-CNT-002), WC-C-087 (C: WC-S-5466 in CM-SFR-004), WC-C-110 (D: WC-S-0760 and WC-I-0617 in CM-CNT-007, WC-S-0759 in
CM-CHN-001, WC-S-5492 and WC-S-5494 in CM-CHN-004). Read, not cited: WC-C-014, WC-C-034, WC-C-058, WC-C-082.

Cited from concerns that don't name E, each flagged by the checker:
- **WC-C-050/responsible/WC-S-0644** (F) in CM-SFR-003 as `own-service`: "Some of our Services are offered for a fee,
  like certain WordPress.com plans or Woo themes or extensions". "Our" is Automattic's, which its terms define to include
  WooCommerce, Inc. (WC-C-023/responsible/WC-S-0461). It is the only maker statement for Woo themes. F's CM-APP-011 cites it as `own-service` too, so the
  merge will flag it in two domains: the coordinator decides which counts. Proposal: add E to WC-C-050's `also`.
- **WC-C-072/where/WC-S-0022** (C) in CM-CNT-003 as `shows`: the settings section Advanced > Page setup is WooCommerce's
  only statement on store pages. `shows` keeps it from counting as `core` here and in C.
- **WC-C-071/responsible/WC-S-5408** (C) in CM-CNT-008 as `shows`: the merchant must maintain return and refund policies,
  WooCommerce's only statement on a store's own policies.

### Statements of the batch's concerns left uncited, and why

- **WC-C-107:** Cart and checkout features (WC-S-0740) and the Checkout Field Editor (WC-S-5484, WC-S-5486, WC-S-5487,
  WC-S-5488) are about checkout and its fields, domain C's subject; no capability of E holds them. Proposal: add C to
  WC-C-107's `also`, so domain C's part can cite them. WC-S-5487 (a field's name is used as the meta key) bears on custom
  data, but it is an extension's own field store, so CM-CNT-002 doesn't cite it.
- **WC-C-079:** the routes held by other concerns (above); the guides WC-S-0774 to WC-S-0779 repeat WC-S-0773.
- **WC-C-111:** none.
- **WC-C-110 (read under `also`):** Social (WC-S-0762) is undefined: no statement shows it is selling on social channels
  rather than marketing there, so CM-CHN-001 doesn't cite it.

### Homonyms

- **Marketplace.** WooCommerce's Marketplace (WC-S-0923) is the WooCommerce.com store of extensions and themes for
  merchants. Shopify's Marketplace Connect (CM-CHN-003) and Salla's الربط بمنصات التسوّق العالمية are external sales
  marketplaces. They stay apart; CM-CHN-002 and CM-CHN-003 are `none-held` for WooCommerce.
- **Channel.** WooCommerce's marketing API marketing/channels (WC-S-0189, cited in D's CM-MKT-005) names marketing
  channels, not sales channels; CM-CHN-001 doesn't cite it.
- **Publish.** WooCommerce's webhook topic product.published (WC-S-0269) is not shown to mean publishing to a channel, as
  Salla's product.publish does in CM-CHN-001. A reading: on WordPress, published is a post's status. Not cited.

### Rulings

U-013, U-051 and U-063, for WC-C-107 and WC-C-111 against each Shopify and Salla concern:
- U-013: WC-C-107 joined:CM-SFR-013 with SH-C-035 and with SA-C-020 (domain B, which names E under also).
- U-051: WC-C-111 joined:CM-SFR-003 with SH-C-029 (on theme sales, what the candidate asks; M-014 already joins them in
  CM-SFR-001) and with SA-C-208.
- U-063: WC-C-107 joined:CM-SFR-005 with SH-C-193; apart from SA-C-033 (SEO is WC-C-110's, in CM-CNT-007);
  nested:CM-SFR-006 with SA-C-082 and nested:CM-SFR-007 with SA-C-083. The nested rulings are readings: WooCommerce's
  category is coarser and has no subcategory held for landing pages or bars, so it sits in the parent, as the anchor nests
  Shopify's Page builder apps and Banner apps under Store design apps.

### Earlier rows of other parts that no longer hold

The cells here cite keys that turn rulings of other parts from `apart` to joined. For the coordinator:
- **D-woocommerce, U-063, WC-C-110 against SA-C-033** (rulings.tsv line 34, `apart`): CM-CNT-007 now cites WC-C-110's SEO
  and SEM (WC-S-0760) and SA-C-033's keys: joined:CM-CNT-007. Against SH-C-193 (line 33): CM-CNT-007 cites Shopify's SEO
  apps by inventory id SH-I-1934, an entry Q1 placed in SH-C-193; a ruling's keys must be statements, so the coordinator
  decides whether it becomes joined.
- **D-woocommerce, U-054, WC-C-110 against SH-C-135 and SA-C-097** (lines 14 and 15, `apart`): CM-CHN-001 now cites
  WC-C-110's Sales channels (WC-S-0759) with both: joined:CM-CHN-001. Against SH-C-137 (line 13) it still holds:
  WooCommerce's CM-CHN-003 is `none-held`.
- **F-woocommerce, U-051, WC-C-017 against SH-C-029 and SA-C-208** (lines 7 and 8, `apart`): CM-SFR-003 now cites
  WC-C-017's WC-S-0923 and WC-S-0834 with SH-C-029's and SA-C-208's keys: joined:CM-SFR-003, if the coordinator keeps them
  here.

### Gaps

- WC-C-111/decides (searched, not found): nothing held says what turns a theme on or limits it.
- No WooCommerce statement held defines its Marketplace categories (Store content and customizations and its
  subcategories, Themes, Sales channels, SEO and SEM): every placement on them rests on the category's name.
- Google for WooCommerce (CM-CHN-004): no statement held names its maker; the concern's note that it is listed under
  Developed by Woo is a note and never counts. So its cell supports no placement (`not-stated`).
- WC-C-079/responsible is stated only in general terms, and WC-C-079/reason was searched and not found.

### Names (proposals for the coordinator)

- CM-SFR-001: add "WooCommerce: Themes, Choose your theme".
- CM-SFR-005: add "WooCommerce: Store content and customizations".
- CM-SFR-012: add "WooCommerce: Store API".

### What the checker flagged

`check_class_part.py ... --concerns WC-C-079,WC-C-107,WC-C-111 --areas SFR,CNT,CHN`: 0 problems, 19 flags.
- **Statements of concerns without E under `also`** (WC-S-0644, WC-S-0022, WC-S-5408): above.
- **own-service on WC-S-0644:** it names Automattic's Paid Services, "Woo themes or extensions": the company as provider.
- **core resting only on boundary statements** (CM-SFR-005: the route wc/private > /patterns, WC-S-0178; CM-CNT-002:
  the product custom fields API, WC-S-0675): each is WooCommerce's own API for its own feature, `core` by the dry run's
  convention. In CM-SFR-005 the rest of the cell is `extension-point`.
- **none-held with matching statements:** each cell's reading names the hits and why none shows the capability. In
  short: CM-SFR-007 (legal and admin notices), CM-SFR-008 (a WordPress.com account, WC-S-5335), CM-SFR-009 (HPOS text),
  CM-SFR-010 (https URLs), CM-SFR-011 (WC-S-5466 and WC-I-0612, cited in CM-SFR-004 and CM-SFR-001), CM-CNT-001 (fees
  and download settings), CM-CNT-004 (WordPress post types, HPOS), CM-CNT-005 (admin menus), CM-CNT-006 (payment
  redirects, slugs, URLs), CM-CHN-002 and CM-CHN-003 (shop_* post types, the extensions Marketplace, Amazon Pay),
  CM-CHN-005 (Automattic's terms, WC-S-0461, WC-S-0647 and WC-S-0644, which say who Automattic is and what it sells, and
  the dropshipping category WC-S-0713), CM-CHN-006 (the merchant's mobile app and its POS mode).

### For batch 2 (POS and MKS)

- **Your concerns:** WC-C-030, WC-C-046, WC-C-051, WC-C-052, WC-C-053, WC-C-089, WC-C-099 and WC-C-108; WC-C-014 (C)
  names E under `also`. Your unclear candidates: U-028, U-033, U-065, U-074 (WC-C-014's, not yours to rule), U-079.
- **The files:** all eight exist with their headers. `capabilities.tsv` is empty: batch 1 added no capability, so number
  new ones from the anchor's highest in each area. Append; don't rewrite these rows.
- **WC-C-108's category** International and localization sits under Extensions > Store content and customizations, the
  category WC-C-107 lands in CM-SFR-005 (WC-S-0703). If you land WC-C-108 in an MKS capability, it is in another tree
  from its parent category: say so, as the batch's reading.
- **WooCommerce's mobile app:** POS mode (WC-C-089) runs in the WooCommerce mobile app, the merchant's app (WC-C-090,
  domain G). CM-CHN-006, the store's branded app for buyers, is `none-held`: don't cite POS there.
- **The last batch checks the whole part,** without `--concerns` and `--areas`.

## The coordinator's corrections after batch 1 (30 October)

- **The pairs this batch's cells join, which other parts ruled apart from their own cells,** now have E's side in `rulings.tsv`: U-063 (WC-C-110 against SA-C-033, joined:CM-CNT-007), U-054 (WC-C-110 against SH-C-135 and SA-C-097, joined:CM-CHN-001) and U-051 (WC-C-017 against SH-C-029 and SA-C-208, joined:CM-SFR-003). Each domain rules from its own cells; the merge flags each pair ruled differently, for one answer at the final review.
- **scope.tsv:** WC-C-107 names C under `also` (its cart and checkout categories, for domain C), and WC-C-050, WC-C-072 and WC-C-071 name E.
- **WC-S-0644 counts once:** `own-service` in CM-SFR-003, where WooCommerce's cell rests on it, and `shows` in F's CM-APP-011.


## Batch 2: POS and MKS

Eight concerns: WC-C-089, WC-C-030, WC-C-046, WC-C-051, WC-C-052, WC-C-053, WC-C-099 and WC-C-108; WC-C-014 (C) read
under `also`. WooCommerce's cell is written for all 13 capabilities of the two areas: 4 POS, 9 MKS. 8 cells cite
statements, 5 are `none-held` (CM-POS-003, CM-POS-004, CM-MKS-002, CM-MKS-003, CM-MKS-008). All eight concerns joined
existing capabilities; none made a new one, so `capabilities.tsv` stays empty. Before deciding that, I searched every
domain's capabilities (`caps`) for selling and shipping locations, geolocation, currency, translation, point of sale and
cash: nothing outside E holds them, and no capability of the model fits selling countries better than CM-MKS-001.

### How I cut

| Concern | Lands in | Join | Fit |
|---|---|---|---|
| WC-C-089 Point of Sale in the mobile app | CM-POS-001 | match:M-057 | strained |
| WC-C-030 Selling and shipping locations | CM-MKS-001 | role | strained |
| WC-C-046 Customer geolocation | CM-MKS-004 | match:M-087 | strained |
| WC-C-051 WooPayments payout currency and conversion | CM-MKS-007 | match:M-044 | strained |
| WC-C-052 Store currency | CM-MKS-005 | match:M-044 | clean |
| WC-C-053 Multi-currency | CM-MKS-006 | match:M-044 | clean |
| WC-C-099 Reference data | CM-MKS-009 | match:M-082 | clean |
| WC-C-108 International and localization extensions | CM-MKS-001 | role | strained |

- **M-044's finer pairs** decide the currency landings: WC-C-052 with SH-C-107 (CM-MKS-005), WC-C-053 with SH-C-108 and
  SA-C-163 (CM-MKS-006), WC-C-051 with SH-C-109 (CM-MKS-007). The checker flags M-044 in more than one tree: the anchor's
  CM-MKS-005 has no parent, so the match spans two trees on every platform; that is the anchor's cut, not this batch's.
- **WC-C-030 in CM-MKS-001, on role, strained.** Selling location(s) limits the countries the store sells to (WC-S-5354,
  WC-S-0600): the location part of Shopify's markets (SH-S-0541, product availability by market) and Salla's (SA-S-0157,
  versions of the store per country it targets). What doesn't fit: WooCommerce's is one store-wide list, with no version
  of the store per country (currency, language, domain); Shipping location(s) (WC-S-5355, WC-S-5357) is shipping's, cited
  as `shows`; WC-S-0880 is cited also in CM-MKS-005, another tree (the checker's flag), for the currency it selects. It
  is not its own capability: WooCommerce gives it two options under General and two filters, no section, route, API
  group, plan line or category of its own (the dry run's convention). The reviewer may split selling countries from
  markets as a child of CM-MKS-001; the anchors would then need back-filling there.
- **WC-C-046 in CM-MKS-004, strained.** M-087 joins it with Shopify's Geolocation apps. WooCommerce's stated purpose is to
  "display tax rates and shipping methods specific to their location" (WC-S-0641); nothing held sends buyers to a market's
  domain or currency, the capability's other half.
- **WC-C-051 in CM-MKS-007, strained.** Its conversion statements are here; its payout statements (WC-S-0536, WC-S-5314:
  payout currency eligibility and the default bank account) are payouts, domain C's subject, where Shopify's Supported
  payout currencies sits (SH-C-069, C). They stay uncited in E. Proposal: add C to WC-C-051's `also`, so C's payouts can
  cite them.
- **WC-C-089 in CM-POS-001, strained** only because its POS order emails (WC-S-0308, WC-S-0309), cited here as `shows`,
  are cited as `core` in D's CM-NTF-001 under WC-C-076. Its category Official payments > In-person payments (WC-S-0711)
  goes to CM-POS-002, its child.
- **WC-C-108 in CM-MKS-001, on role, strained.** International and localization (WC-S-0741) is where third parties'
  extensions for international selling sit, the role of Shopify's Internationalization apps (SH-I-1914), which the anchor
  cites in CM-MKS-001. As batch 1 said, WooCommerce's own grouping puts it under Store content and customizations, which
  WC-C-107 lands in CM-SFR-005: another tree. The category is undefined, so CM-MKS-006 and CM-MKS-008 don't cite it,
  though Shopify's Currency and translation apps sit there; if the reviewer reads "localization" as translation, it moves.
- **WC-C-099 clean.** WooCommerce holds countries and continents, Salla countries, cities and districts: a difference of
  grain inside one capability (Q1's note).

### WordPress, not WooCommerce

Each a reading; no statement held says what WordPress does.
- **Store languages and translation** (CM-MKS-008, `none-held`): the site's language and translations are WordPress's.
  WooCommerce's only statements near it are country names (i18n/countries.php, per locale, cited in CM-MKS-009) and an
  undefined Marketplace category.
- **Local domains** (CM-MKS-004): the site's address is WordPress's and its host's, as batch 1 said for CM-SFR-008 to 010.
- **POS access** (CM-POS-001): the per-user capabilities are WordPress's authorization primitive, which WC-S-5435 itself
  says; WooCommerce defines the woocommerce_pos_* ones.
- **The POS app** is the WooCommerce mobile app (WC-C-090, domain G), not WordPress: the plugin's own feature point_of_sale
  enables POS "in the WooCommerce mobile apps" (WC-S-0937). Read in the release, the flag is not experimental, on by
  default and, since 11.0.0, always on (context); so it is cited as a released flag, `core`.

### Maker statements: WooPayments and the mobile app

- **WooPayments** carries multi-currency (CM-MKS-006), exchange rates and conversion fees (CM-MKS-007) and in-person
  payments (CM-POS-002). No statement of E's concerns names its maker. The one held is in Automattic's terms, "As part of
  WooPayments, we may use certain third parties to fulfill our obligations to you" (WC-C-006/responsible/WC-S-0476),
  where "we" is Automattic, WooCommerce, Inc. included (WC-S-0461). WC-C-006 is domain C and doesn't name E, so the
  checker flags it three times; I cite it `own-service` in the three cells because each cell needs it for its placement,
  as batch 1 did with WC-S-0644. Domain C will surely cite it for WooPayments itself, so the merge will flag it in two
  domains: the coordinator decides where it counts. Without it, the three cells are `not-stated` on that side: CM-MKS-007
  then derives `not-stated`, CM-MKS-006 `extension-point` only, CM-POS-002 `outside;extension-point`. Proposal: add E to
  WC-C-006's `also`. Also held, and not cited: "WooPayments is the only payment gateway designed by Woo for Woo"
  (WC-S-0557, WC-C-006): Woo is a brand, not a company the terms name.
- **The WooCommerce mobile app:** no statement held names its maker, so POS mode (WC-S-0892) is `shows`; CM-POS-001's
  `core` rests on the plugin's settings tab, released flag and staff capabilities. Gap.

### Concerns read under `also`, and statements cited from concerns without it

- **WC-C-014** (C, names E): WC-S-0868, WC-S-0481, WC-S-0850, WC-S-0869, WC-S-0870 in CM-POS-002.
- **WC-C-006** (C, without E): WC-S-0476, above.
- Statements of my concerns held also by other concerns: WC-S-0711 (also WC-C-005, C), cited as `extension-point`, and
  WC-S-0308, WC-S-0309 (also WC-C-076, D), cited as `shows`: neither counts as `core` here.

### Rulings

- **U-033:** WC-C-030 joined:CM-MKS-001 with SH-C-106 and with SA-C-165 (on role, strained).
- **U-065:** WC-C-108 joined:CM-MKS-001 with SH-C-106 and with SA-C-165; apart from SH-C-032 and SA-C-008 (CM-MKS-008
  is its own tree, and WooCommerce's cell there is `none-held`).
- **U-079:** WC-C-046 joined:CM-MKS-004 with SH-C-111 (M-087 already joins them); apart from SA-C-065 (domain D, names E
  under `also`; no capability of E cites its keys: its Geolocation apps are D's CM-CUS-009, map services for addresses).
  The pair WC-C-046 against WC-C-047, both WooCommerce's, isn't ruled: the checker takes one row per pair across
  platforms, and scope.tsv gives WC-C-047 domain C.
- **U-028:** WC-C-051 joined:CM-MKS-007 with SH-C-109; apart from SH-C-069 (domain C) and SA-C-164 (domain C, names E;
  no capability of E cites its keys; its settlement currency is what WC-C-051's uncited payout statements are about).
- **U-074** is WC-C-014's (domain C): not ruled here. For C's part: CM-POS-002 cites WC-C-014's keys with Shopify's
  SH-C-143 and Salla's SA-C-095, so from E's cells the pairs would be joined:CM-POS-002.

### Homonyms

- **Localization.** WooCommerce's International and localization is a Marketplace category of extensions; Shopify's
  Localizations (SH-C-032) is its core translation API. Kept apart (U-065).
- **Register.** "digital cash register" (WC-S-0892) is POS mode; the Store API's and blocks' register functions are code.
  CM-POS-003 cites neither.
- **Geolocation.** WooCommerce's (WC-C-046) is the visitor's location for taxes and shipping; Salla's Geolocation apps
  (SA-C-065) are map services for addresses (D's CM-CUS-009).

### Gaps

- WC-C-089/responsible stated only in general terms; no maker statement for the WooCommerce mobile app.
- WC-C-046/responsible searched, not found.
- WC-C-051/where observation needed; WC-C-051/responsible page not read.
- WC-C-030, WC-C-052, WC-C-053, WC-C-099 /reason searched, not found; WC-C-052, WC-C-053, WC-C-099 /responsible stated
  only in general terms.
- WC-C-108: decides and responsible stated only in general terms, boundary and reason searched and not found; no
  statement defines the category.
- No statement held says who sells WooPayments' card readers (CM-POS-002), or gives a conversion fee's value (CM-MKS-007).

### Names (proposals for the coordinator)

- CM-POS-001: add "WooCommerce: Point of Sale, POS mode".
- CM-MKS-001: add "WooCommerce: Selling location(s)", if it stays there.
- CM-MKS-004: add "WooCommerce: MaxMind Geolocation, Default customer location".
- CM-MKS-005: add "WooCommerce: base currency".
- CM-MKS-009: add "WooCommerce: data/countries, data/continents" and "continents" to the name.

### What the checker flagged (the whole part)

`check_class_part.py studies/class-model/parts/E-woocommerce`: 0 problems, 30 flags. One problem in my own rows on the
batch check (a ruling of two WooCommerce concerns, WC-C-046 against WC-C-047) is fixed by removing the row. This batch's
flags:
- **WC-S-0476** (three cells): a statement of WC-C-006 (C) without E under `also`, `own-service`, and cited in more than
  one tree (CM-POS-002, CM-MKS-006, CM-MKS-007). Above: it names Automattic as WooPayments' provider; it is a maker
  statement, so it bears on every cell WooPayments does, not on one capability.
- **WC-S-0880 in two trees** (CM-MKS-001 `core`, CM-MKS-005 `shows`): the general settings page's one sentence names both
  the regions sold to and the currency; WC-C-030 is `strained` for it.
- **M-044 in more than one tree:** the anchor's cut, above.
- **none-held with matching statements:** CM-POS-003 (WC-S-0892, the Store API's register, Cash on delivery), CM-POS-004
  (the POS capabilities, emails and terminals, cited elsewhere), CM-MKS-002 (Action Scheduler's background work),
  CM-MKS-003 (customs data, WC-S-5386), CM-MKS-008 (country names, the readme, the undefined category): each cell's
  reading names the hits and why none shows the capability.
- The other flags are batch 1's, answered in its section.

### For the coordinator: batch 1's rows

- **WC-C-111/boundary/WC-S-0082** (the namespace wc/private) is uncited, though batch 1's notes say WC-C-111 leaves none
  uncited. CM-SFR-005 cites the route under it (WC-S-0178); the namespace could be cited there as `shows`.
- No problem on batch 1's rows in the whole part's check.

## The coordinator's corrections after batch 2 (30 October)

- **U-074 has E's side:** joined:CM-POS-002 for WC-C-014 against SH-C-143 and SA-C-095, since CM-POS-002's cells cite all three. Domain C's WooCommerce part rules the pair from C's cells, and the merge flags any difference.
- **scope.tsv:** WC-C-051 names C under `also`, for its payout currencies; WC-C-006 names E, since its statement naming WooPayments' provider (WC-S-0476) supports `own-service` in CM-POS-002, CM-MKS-006 and CM-MKS-007.
- **A maker statement may count for each feature of its service.** WC-S-0476 says who provides WooPayments; each cell that cites it as `own-service` shows a different feature of WooPayments by its own statements. If domain C counts it too, the merge flags it, and the final review weighs it as maker evidence, not as a feature counted twice.
- **The part is complete,** with no capability added: domain E needs no WooCommerce back-fill. Zid and BigCommerce map next.
- **Counted once (the coordinator, at E's merge):** WC-C-046/where/WC-S-0008 is `shows` in CM-MKS-004: core in F's CM-APP-010, whose WooCommerce cell rests on it.
