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
