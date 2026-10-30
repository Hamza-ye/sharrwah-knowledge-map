# E-anchor: notes

## Batch 1: area SFR (online store, themes and storefront)

Concerns landed: SH-C-029, SH-C-033, SH-C-035, SH-C-036, SH-C-139, SH-C-166, SH-C-193, SA-C-007, SA-C-082, SA-C-083. Capabilities CM-SFR-001 to CM-SFR-013, with a Shopify and a Salla cell each. Every reading below is a reading; the cells and landings cite the keys.

### How the area is cut, and the grains chosen

- **Two roots for the storefront's design, one for domains, one for headless, one for search.**
  - CM-SFR-001 (online store and its theme) holds CM-SFR-002 (theme editor and code), CM-SFR-003 (theme marketplace), CM-SFR-004 (app extensions in the storefront) and CM-SFR-005 (design elements beyond the theme), which holds CM-SFR-006 (landing pages and page builders) and CM-SFR-007 (announcement bars, banners and pop-ups). Both platforms' admin groupings put the theme, its editor and the theme market under one section: Shopify's Online Store (SH-I-0823; route editor in section OnlineStore, SH-S-5211) and Salla's Store design (/themes, /themes/editor, /themes/marketplace, /themes/landing-pages under @salla.sa/ui-merchant-themes, SA-S-3546).
  - SH-C-029 is coarser than the theme capabilities, so it lands in the parent CM-SFR-001; its statements cited in CM-SFR-002, -003 and -004 stay in that tree, so the fit is clean.
  - CM-SFR-008 (store domains) holds CM-SFR-009 (DNS records) and CM-SFR-010 (hosting and SSL). DNS records get a capability because Salla gives them an API group (DNS Records, SA-S-1064), a scope (SA-S-1556) and a plan line (SA-S-2041). SSL sits under domains because both platforms put it there (SA-S-2038, parent_code domyn-almtgr; SH-S-7465, Domain.sslEnabled). Hosting has no statement putting it under domains; it rides with SSL because Shopify's concern SH-C-036 holds both. A reviewer may prefer a root hosting capability; then SA-C-007's SSL line would be cited outside its tree and SA-C-007's fit would turn strained.
  - CM-SFR-011 (headless and custom storefronts) holds CM-SFR-012 (Storefront API). SH-C-139 is coarser (headless channel, Hydrogen, Oxygen, the plan row, and the Storefront API), so it lands in the parent. **The parent follows Shopify's grouping**, whose concern holds the Storefront API with the Headless channel (SH-S-6152). Salla's grouping differs: its storefront APIs are called by its Twilight themes through the Twilight JS SDK (SA-S-5140), not by a headless storefront. A reviewer may prefer CM-SFR-012 as a root; SH-C-139 would then be strained.
  - CM-SFR-013 (storefront search and filtering) is a root.
- **Parent of CM-SFR-007.** Shopify's Banner and Pop-up apps are App Store categories that Q1 placed in Store design add-ons (SH-C-193); Salla's Advertisements sit under /marketing (SA-S-3536), its staff permission in the group التسويق (SA-S-2357), and its plan line under أدوات التسويق (adoat-altsoyk, SA-S-2014). The groupings differ. I followed Shopify's, which keeps it a storefront element. Salla's landing-pages plan line is also under adoat-altsoyk (SA-S-2109), while its admin route is under themes (SA-S-1838).
- **SH-C-193** is Shopify's App Store category Store design apps and its subcategories. It lands in CM-SFR-005. Its children take Page builder apps (CM-SFR-006) and the Banner, Pop-up and Notification apps (CM-SFR-007). Its SEO apps (SH-I-1934) are left for area CNT, where SEO (SA-C-033) is. Its responsible statement SH-S-0058, a general clause on third-party services, and its decides statement SH-S-0755, on approving app scopes, are not cited: neither names store design.

### Joins on role (readings)

- CM-SFR-004: Shopify's theme app extensions, app embeds and app proxies (SH-S-0705) against Salla's App Snippets (SA-S-0209). Both are an installed app adding its code or elements to the merchant's storefront.
- CM-SFR-005: Shopify's Store design apps (SH-S-2662) against Salla's component bundles published in its Themes Marketplace (SA-S-5032, SA-S-1165, SA-S-1909). Both are third parties' design elements for a store, through the platform's market. No statement defines what a Salla bundle holds.
- CM-SFR-006: Salla's Landing pages (core) against Shopify's Page builder apps (SH-I-1938, an App Store category only). No Shopify statement defines what a page builder builds.
- CM-SFR-007: Salla's top-of-store bar, Advertisements (SA-S-2014), against Shopify's Banner apps and Pop-up apps.

### Homonyms

- "Advertisements" on Salla (SA-C-083, a top-of-store bar: شريط إعلاني أعلى المتجر, SA-S-2014; API folder Advertisements, SA-S-1067) is not Salla Ads (إعلانات سلة, SA-C-073, "Salla's product for simplifying the creation, management, and analysis of digital advertising campaigns", SA-S-0007). They are kept apart: SA-C-073 is not cited here.
- "Web Components": Shopify's Storefront Web Components (SH-I-0069, in SH-C-139) against Salla's Web Components (SA-C-091), Q1's U-050. Neither is defined in the statements. SH-I-0069 is not cited here; it is left to batch 2's ruling.

### Strained fits

None. Every landed concern's statements are cited only in its own capability's tree.

### Concerns read under `also`, and other domains' statements

- SA-C-020 (Products, domain B, naming E under also): its Product filter settings (SA-S-1756), its plan line for the filter options shown to the customer (SA-S-2135) and its flag products-filters (SA-S-3479) are cited in CM-SFR-013. U-013 is ruled joined:CM-SFR-013, with the basis naming domain B.
- SA-C-100 (Checkout APIs, domain C, not naming E): SA-S-5139 ("control cart and checkout-entry flows outside of the standard storefront") was found in the headless search. **It is not cited.** It is a lead for a Salla headless or custom-storefront cell, if a reviewer reads it as one.

### Statements of batch 2's concerns cited in my Salla cells

Batch 2 lands these concerns. Each one's statements are already cited here:
- **SA-C-090:** in CM-SFR-001 (Store design, plan lines, store_design_management), CM-SFR-002 (themes editor, customization flags and plan lines, Twilight Engine) and CM-SFR-003 (Theme Marketplace, theme-purchases, SA-S-5031, SA-S-0119). All three are in one tree, so SA-C-090 fits CM-SFR-001 by M-014.
- **SA-C-208:** in CM-SFR-003 (SA-S-5104, SA-S-1908), plus the quality on the minimum theme price (SA-S-5107).
- **SA-C-091:** in CM-SFR-005 (Component Bundle SA-S-1165, Bundles SA-S-1909, the bundle rule SA-S-5032) and CM-SFR-013 (the salla-filters and salla-search components, SA-S-1444, SA-S-1523). **These two capabilities are in different trees.** Wherever SA-C-091 lands, one of them is outside its tree: batch 2 should mark the fit strained, or move the citation.
- **SA-C-198:** in CM-SFR-004 (SA-S-0209, SA-S-1074).
- **SA-C-101:** in CM-SFR-012 (SA-S-0211, SA-S-5140, SA-S-5141).
- **SA-C-301:** not cited. Its Partners-portal domains (SA-S-5116, SA-S-5117) bear on CM-SFR-008, by M-017.

### Ruling pairs left for batch 2

Batch 2 lands the Salla side of each pair. My cells already cite both sides where noted, so the ruling follows them:
- U-049: SH-C-166 against SA-C-198. CM-SFR-004 cites both sides (SH-S-0705, SA-S-0209): joined:CM-SFR-004.
- U-050: SH-C-029 against SA-C-091, and SH-C-139 against SA-C-091. No capability here cites both sides on web components.
  - CM-SFR-005 cites SA-C-091's bundles and none of SH-C-029's statements. Its parent CM-SFR-001 cites SH-C-029, so where batch 2 reads the bundles as the candidate's subject, the ruling is nested:CM-SFR-005.
  - CM-SFR-013 cites SA-C-091's search components, against SH-C-035, not SH-C-139.
  - Batch 2 rules on what lands SA-C-091's web components.
- U-051: SH-C-029 against SA-C-208. CM-SFR-003 cites SH-C-029 (SH-S-0052, SH-S-0053) and SA-C-208 (SA-S-5104, SA-S-1908): joined:CM-SFR-003.
- U-063: SH-C-193 against SA-C-033 (SEO), which lands in area CNT. Shopify's SEO apps (SH-I-1934) are not cited here.

Rulings made in this batch: U-014 joined:CM-SFR-010; U-063 (SH-C-193 against SA-C-082) joined:CM-SFR-006; U-063 (SH-C-193 against SA-C-083) joined:CM-SFR-007; U-013 joined:CM-SFR-013.

### Matches written as terms

- SH-C-029 is in Q1's match M-014, and SH-C-139 in M-056. **Both landings are written as `terms`, citing both sides.** The other side of each match (SA-C-090, SA-C-101) lands in batch 2, and the checker refuses a match whose other concerns haven't landed. The terms are the ones Q1's basis names: "Themes and templates" against اختيار ثيم المتجر; "Storefront API" against "the Salla storefront APIs".
- SA-C-007 and SH-C-033 land together by M-017.

### Gaps that change what a cell can claim

- **CM-SFR-010, Salla:** no statement covers hosting of the store itself. Searching استضافة, الاستضافة and hosting finds only Salla hosting themes, apps and partner services (SA-S-0039, SA-S-0119, SA-S-0037, SA-S-0026, SA-S-0040). **The cell rests on the SSL plan line alone.**
- **CM-SFR-010, Shopify:** Q1's `where` gap is "observation needed".
- **CM-SFR-013, Shopify:** Q1's `decides` gap is "observation needed" (the Search & Discovery app's settings). No statement names that app's maker, so the cell holds no own-service.
- **CM-SFR-002, Shopify:** no statement names the Theme Access app's maker (SH-S-6301). It is cited as shows.
- **CM-SFR-006 and CM-SFR-007, Salla:** the `responsible` and `reason` gaps are "page not read".
- **CM-SFR-008, Shopify:** no statement names who registers the domains Shopify sells, and none names "the domain provider" of SH-S-7272. **No slot filler is recorded.**
- **CM-SFR-009, Shopify:** none-held for DNS. The definition is not stated on Shopify's side.
- **CM-SFR-011, Shopify:** Oxygen is "Shopify's global edge hosting platform" (SH-S-0710). I read it as core, part of the headless offer. A reviewer may read it as own-service, a separate product of Shopify's.

### What the checker flagged

- **cells.tsv line 23 (CM-SFR-011, Salla, none-held):** the 8 statements that match are these.
  - SA-S-2101 and SA-I-1101 (تصميم واجهة المتجر) and SA-S-2153: the theme's design, cited in CM-SFR-001's tree.
  - SA-S-5140 and SA-S-5141: the Twilight JS SDK for the storefront APIs, used by Salla's themes, cited in CM-SFR-012.
  - SA-S-5139: a domain C statement on checkout APIs, not cited (see above).
  - SA-S-2096 (inventory tracking) and SA-S-0147 (tax shown in invoices and the storefront): they match on the word واجهة only.

  None shows a storefront built apart from Salla's themes, so the cell stays none-held.
- **Fixed during the check:**
  - Four partner-requestable permissions cited as core were replaced by the staff permissions: SA-S-2411, SA-S-2397, SA-S-2357 and SA-S-2389, in place of SA-S-2628, SA-S-2614, SA-S-2574 and SA-S-2606.
  - The terms نطاق المتجر, تصميم المتجر, صفحات الهبوط and إدارة الإعلانات were dropped from the cells: no cited statement holds them.
  - The two match landings were rewritten as terms, as above.

## The coordinator's corrections after batch 1 (30 October)

- **Hosting is G's.** Domain G already holds CM-OPS-003, hosting of the store, whose Shopify cell rests on the plan row Unlimited web hosting (SH-S-7032) alone. Batch 1 cited the same row as `core` in CM-SFR-010, so it counted in two domains (the merge's flag, by convention 8). CM-SFR-010 is now the SSL certificate for the store's domains; SH-S-7032 is `shows` in it, and SH-C-036's landing is `strained`, its hosting row being G's.


## Batch 2: area SFR, Salla's SA-C-090, SA-C-091, SA-C-101, SA-C-198, SA-C-208, SA-C-301

All six concerns join batch 1's capabilities; no capability is added. Every reading below is a reading; the landings, cells and rulings cite the keys.

### Landings

- **SA-C-090** (Themes and store design) in CM-SFR-001, by M-014, beside SH-C-029. Coarser than CM-SFR-001: its statements are cited in CM-SFR-001, -002 and -003, one tree, so clean.
- **SA-C-091** (Storefront SDK and web components) in CM-SFR-002 (theme editor and theme code), a join on role, **strained**.
  - Why CM-SFR-002: Salla's docs navigation puts Twilight Engine (SA-S-1161, already cited in CM-SFR-002), Twilight SDK (SA-S-1162), Web Components (SA-S-1163) and Component Bundle (SA-S-1165) under one parent folder (01HNA8Q9YTZGTHZYF36EYDJEWD). The SDK and the components are what a Salla theme is written with. On Shopify, the theme's Ajax API (SH-I-0063) sits in SH-C-029 with Liquid and the Section Rendering API, which batch 1 cited in CM-SFR-002; I added it there as core.
  - Strained: salla-filters and salla-search (SA-S-1444, SA-S-1523) are cited in CM-SFR-013, a root. **I read that citation as right, not misplaced:** the two components show Salla's storefront having search and filters. Its Component Bundle statements (CM-SFR-005) and salla-advertisement (CM-SFR-007, as shows) are in CM-SFR-001's tree, the same as CM-SFR-002's.
  - **An alternative for the reviewer:** "Twilight comes with a JavaScript SDK for the Salla storefront APIs" (SA-S-5140, SA-C-101's) ties the Twilight SDK to CM-SFR-012. I didn't cite the SDK folder (SA-S-1162) there: SA-S-5140 already carries that tie, and SA-C-091 would then be cited in three trees. A reviewer may prefer a capability of its own for the storefront SDK and web components; Salla gives them docs folders of their own, so the convention allows one, and Shopify's side would then rest on the undefined Ajax API and Storefront Web Components titles.
- **SA-C-101** (Storefront API used by store pages) in CM-SFR-012, by M-056. SH-C-139 is in the parent CM-SFR-011. Clean.
- **SA-C-198** (App snippets) in CM-SFR-004, a join on role with SH-C-166 (U-049). Clean.
- **SA-C-208** (Theme publishing and sales by partners) in CM-SFR-003, a join on role with SH-C-029's Theme Store clauses (U-051). Clean: its Bundles link (SA-S-1909) is cited in CM-SFR-005, same tree.
- **SA-C-301** (Domains in the Partners portal) in CM-SFR-008, by M-017, with SH-C-033 and SA-C-007. Clean. Its three statements are cited as **shows**: they name a Domains Management section, a domain-purchase feature and a manage-domains permission in the Partners portal, but don't say whose stores the domains serve. Q1's responsible gap is "observation needed" and its reason gap "page not read". Read as partners buying domains for merchants' stores, they would be extension-point; no statement says so.

### Rulings

- U-049: joined:CM-SFR-004 (SH-C-166 against SA-C-198).
- U-050, two rows:
  - SH-C-029 against SA-C-091: joined:CM-SFR-002, on the Ajax API (SH-I-0063) against the Twilight SDK and Web Components (SA-S-1162, SA-S-1163). Batch 1's option nested:CM-SFR-005 rests on the bundles; I ruled on the keys that stand for what the candidate asks about, the web components and the theme's Ajax API.
  - SH-C-139 against SA-C-091: apart. Shopify's Storefront Web Components (SH-I-0069) is now cited in CM-SFR-011 as core, a title in Shopify's headless concern; Salla's Web Components in CM-SFR-002. Neither is defined in the statements, so the shared term doesn't join them. **This is the homonym question of U-050, left open:** a Shopify statement defining Storefront Web Components would settle it. SH-I-0060 ("Using web components") is Shopify's admin UI extensions concern (SH-C-164, domain F's), another use of the term; not cited.
- U-051: joined:CM-SFR-003 (SH-C-029 against SA-C-208).
- U-063's pair with SA-C-033 is batch 3's (area CNT).

### Evidence added to batch 1's cells

I appended evidence rows only; **the cells' `reading` and `terms` are batch 1's and don't mention them.** The coordinator may extend the readings:
- CM-SFR-001, Salla: the plan line حماية محتوى المتجر (SA-S-2035) and the released flags content-copyright, theme-versions-management and theme-version-screenshot as core; the unreleased flags remove-salla-copyright, theme-advanced-activation and theme-preview as shows.
- CM-SFR-002, Salla: the plan lines for CSS customization of all design elements (Pro, SA-S-2153) and full customization without code (Special, SA-S-2199), the released flag component-advanced-visibility, the Twilight docs folders Layouts, Hooks, Pages and Components (SA-S-1120, -1121, -1122, -1128), and SA-C-091's Twilight SDK, Web Components, Cart and salla-product-card, as core; canvas-mode, not released, as shows. Shopify: the Ajax API (SH-I-0063), core.
- CM-SFR-003, Salla: the Partners-portal links Theme Purchases and Theme Subscriptions Trials and the intermediary clause (SA-S-0039) as extension-point; Salla's review of every theme before publication (SA-S-5105) and the released flag theme-trial-versions as core; the commission, payout, freezing and pricing terms (SA-S-0040, -0041, -0042, -5107, -5106) and the unreleased ready-store-theme-purchase as shows. A quality: developers' dues paid after a warranty period, usually 15 days (SA-S-0041). The minimum theme price stays batch 1's quality; SA-S-5107 is cited here only as shows.
- CM-SFR-005, Salla: the bundle publish requirements' reason (SA-S-5033) as extension-point, the SDK folder Component Bundle (SA-S-1155) as shows.
- CM-SFR-007, Salla: the web component salla-advertisement (SA-S-1407) as shows. Its readme is empty; the tie to the top-of-store bar is by name only.
- CM-SFR-008, Salla: SA-C-301's three statements as shows (above).
- CM-SFR-011, Shopify: Storefront Web Components (SH-I-0069) as core.

### Statements not cited

- SA-C-090's flag products-layout-views (SA-S-3480): its name doesn't say whether it is a storefront layout or the dashboard's product list. Its partner permission store_design_management (SA-S-2628): the staff permission (SA-S-2411) carries core. The other Twilight theme docs folders (SA-S-1123 to -1127, -1129 to -1131): the four cited stand for them.
- SA-C-091's other SDK folders and web components (Auth, Wishlist, Loyalty, salla-loyalty-*, salla-reviews, salla-cart-*, and so on): they bear on capabilities of other domains (loyalty, reviews, cart). They are left to those domains' parts, which may cite them since SA-C-091's statements are the components' only record.

### For the coordinator

- **Two batch-1 landings can now be written as matches:** SH-C-029 by M-014 (SA-C-090 is in CM-SFR-001) and SH-C-139 by M-056 (SA-C-101 is in the child CM-SFR-012). Batch 1 wrote them as terms only because the other side hadn't landed.
- **Batch 1's ruling options in its notes:** I ruled U-050 (SH-C-029) joined:CM-SFR-002, not nested:CM-SFR-005; see above.
- No problem on batch 1's rows from the checker.

### What the checker flagged

`0 problems, 1 flags`. The flag is batch 1's: cells.tsv line 23, CM-SFR-011's Salla cell none-held, with 8 Salla statements matching. Batch 1's notes answer it. None of my rows changes it: the statements it lists are theme-design and storefront-API statements, none showing a storefront built apart from Salla's themes.

## The coordinator's corrections after batch 2 (30 October)

- **SH-C-029 and SH-C-139 are written as Q1's matches,** M-014 and M-056, now that batch 2 has landed their Salla sides. Batch 1 wrote them as `terms` only because the other side hadn't landed.
- **The cells batch 2 added evidence to** (Salla's CM-SFR-001, -002, -003, -005, -007 and -008; Shopify's CM-SFR-002 and -011) now name its rows at the end of their readings.



## Batch 3: area CNT, SH-C-027, SH-C-028, SH-C-030, SH-C-031, SH-C-034, SA-C-033, SA-C-081, SA-C-093

Capabilities CM-CNT-001 to CM-CNT-008 are new, with a Shopify and a Salla cell each. No concern joined an existing capability: area CNT had none. Every reading below is a reading; the landings, cells and rulings cite the keys.

### How the area is cut, and the grains chosen

- **No root for Shopify's Content section.** Shopify's admin section Content (content:parent, SH-S-5119, gated by metaobjects.enabled, SH-S-5120) holds Files, Metaobjects, Menus and Blog posts. Salla has no such grouping: its information pages are at /channel/pages (SA-S-1831), its blog at /blog and /marketing/blog (SA-S-1698, SA-S-3555), its custom URLs at /manage/custom-urls (SA-S-1833), its SEO at /marketing/seo (SA-S-1822). A section that groups capabilities isn't itself something a store has, so each is a root. SH-S-5120 is cited only in CM-CNT-002, the metaobjects entitlement it names.
- **CM-CNT-003 (store pages) holds CM-CNT-004 (blog).** Shopify's grouping puts them together: the staff permission Online store > Blog posts and pages (SH-I-0991), PAGES gating the blog's comments route (SH-S-5124), and read_online_store_pages on article events (SH-S-6062). Salla's differs: the blog is under marketing (SA-S-3555, plan line under أدوات التسويق, SA-S-2011), apart from information pages. I followed Shopify's, the one grouping that joins them. SH-C-030 (Pages and blog posts) is coarser, so it lands in the parent, clean.
- **CM-CNT-005 (menus), CM-CNT-006 (custom URLs) and CM-CNT-008 (store policies) are roots.**
  - SA-C-093 holds information pages, menus and custom URLs. It lands in CM-CNT-003, its first term, **strained**: its statements are cited in CM-CNT-005, -006 and -008 too.
  - **CM-CNT-008 is a root by Shopify's grouping** (Settings > Policies, SH-S-7087, not under Content). On Salla the policies are information pages (SA-S-2100, SA-S-5034). A reviewer may nest CM-CNT-008 under CM-CNT-003, following Salla's grouping. SA-C-093 would stay strained, by menus and custom URLs.
- **CM-CNT-006 is Salla's alone.** It has a place of its own on Salla: an admin link, an API folder (whose only operation, in the docs sidebar, is Import Custom URLs: context, not cited), a plan line, a staff permission and a flag. No statement defines a custom URL. Shopify's URL redirects aren't joined with it. Q1's M-015 note says the terms differ. Shopify's redirects have no statement of their own: they are named only in notes, SH-S-5123's routes redirects:list and redirects:new, and SH-S-6245's source page urlRedirectBulkDeleteAll. **This is a gap:** a Shopify statement keyed on its redirects routes or scope would let a reviewer place them, and a Salla statement defining custom URLs would settle whether they are the same thing.
- **CM-CNT-007 (SEO)** is a root. Salla builds it; Shopify's statements show only the App Store category SEO apps (SH-I-1934).
- **CM-CNT-001 (files) and CM-CNT-002 (custom data)** are Shopify's, with Salla none-held.

### Joins on role (readings)

- **CM-CNT-008:** Shopify's Policies (SH-S-7087; the merchant's refund, shipping and terms policies, SH-S-0014) against Salla's information pages that carry the store's policies (SA-S-2100) and the page marked as the return and exchange policy page (SA-S-5034). In both, it is the store's own policies, published to its buyers. U-012 is joined:CM-CNT-008.
- **CM-CNT-007 joins on the shared term SEO,** not on role. Neither side defines it: Salla's plan line names the store's visibility on search engines (SA-S-2141), and Shopify's side is an App Store category's name.

### Homonyms and terms kept apart

- **"Custom fields" (Salla) against "metafields" and "custom data" (Shopify), U-005.** They are not joined.
  - Salla's product custom fields (SA-S-2134, SA-C-020) and order custom fields (SA-S-1780, SA-S-2131, SA-C-042) are titles with no definition. scope.tsv reads SA-C-042's as fields the buyer fills at checkout.
  - Shopify's metafields are shown only as data attached to resources (SH-S-5915, SH-S-7257).
  - Both U-005 pairs are ruled apart.
  - Salla's Meta Data scope (SA-S-1562), Twilight SDK Metadata folder (SA-S-1143), salla-metadata component (SA-S-1470, with a prop entity) and customer-metadata flag (SA-S-3169) are also undefined. They are leads, not cited: a statement defining Salla's metadata would settle whether it is custom data.
- **"Custom URLs" (Salla) against "URL redirects" (Shopify):** kept apart (above).

### Strained fits

- **SA-C-093 in CM-CNT-003,** as above.
- **For the coordinator: batch 1's SH-C-193 in CM-SFR-005 now has a statement cited in another tree.** CM-CNT-007 cites its SEO apps (SH-I-1934). Batch 1 left the SEO apps for area CNT. The checker flags the row (landings.tsv line 9): by S1 it is now strained, with a reading naming CM-CNT-007.

### Rulings

- U-063 (SH-C-193 against SA-C-033): joined:CM-CNT-007.
- U-005 (SH-C-028 against SA-C-042; SH-C-028 against SA-C-020): apart, two rows. Both Salla concerns name E under also, so the ruling follows the cells, and CM-CNT-002's Salla cell is none-held.
- U-012 (SH-C-034 against SA-C-093): joined:CM-CNT-008. SH-C-034 against SA-C-066: apart, because scope.tsv gives SA-C-066 domain A, not naming E.
- No pair is left for a later batch: every candidate holding my concerns has both sides landed.

### Matches

- **M-015** holds SH-C-030, SH-C-031, SA-C-081 and SA-C-093. Its own granularity note says the platforms cut at different grains, so its concerns land in three trees:
  - SH-C-030 and SA-C-093 in CM-CNT-003;
  - SA-C-081 in its child CM-CNT-004;
  - SH-C-031 in CM-CNT-005, written as `terms` (Menus, SH-S-1526, against store-menu, SA-S-3343, the terms M-015's basis names), since none of the match's other concerns is in CM-CNT-005's tree.

### Concerns read under `also`, and other domains' statements

- **Cited only in none-held readings, not as evidence:** SA-C-020 (domain B, also E) for its product custom fields, and SA-C-042 (domain C, also E) for its order custom fields.
- **Not cited:**
  - SA-C-066 (privacy pages, domain A, not naming E);
  - SH-C-111's MarketWebPresence, "which defines its SEO strategy" (SH-S-7458). SH-C-111 is area MKS's, so it is left to the batch on MKS, which may cite it in CM-CNT-007's Shopify cell;
  - SA-C-091's salla-menu component (SA-S-1469), a lead for CM-CNT-005's Salla cell. SA-C-091 is landed in CM-SFR-002, already strained; I left it uncited, since its readme is empty and the store-menu flag carries the cell.

### Gaps that change what a cell can claim

- **CM-CNT-001 and CM-CNT-002, Salla:** none-held. Salla's definition of a file library and of custom data isn't stated.
- **CM-CNT-004, Salla:** Q1's boundary gap is "page not read". No blog API or webhook is held. The blog's flag store-blog is type app, with an install link in Salla's app store (SA-S-3389), but not released; no statement names the app's maker.
- **CM-CNT-006, Shopify:** none-held. Salla's custom URLs aren't defined.
- **CM-CNT-007, Shopify:** no statement shows SEO built into Shopify's admin, such as page titles or meta descriptions. The cell rests on the App Store category alone, so on Shopify's statements SEO is extension-point only.
- **SH-C-030 and SH-C-031:** Q1's reason gaps are "searched, not found", and the responsible gaps of SH-C-027, -028, -030 and -031 are "stated only in general terms".
- **SA-C-033, SA-C-081 and SA-C-093:** Q1's responsible gaps are "page not read".

### What the checker flagged

`0 problems, 8 flags`.
- **cells.tsv line 23 (CM-SFR-011, Salla):** batch 1's flag, answered in its notes.
- **cells.tsv line 29 (CM-CNT-001, Salla, none-held, 24 matches):** product images and GIF uploads (SA-C-020), review media (SA-C-030), marketing assets (SA-C-072), the storefront components salla-file-upload, salla-attachments and salla-attachment-view (SA-C-091), and the docs page Files and Folders Structure (SA-I-0135, a theme's files). None is a store's file library.
- **cells.tsv line 31 (CM-CNT-002, Salla, none-held, 26 matches):** the custom fields and metadata statements above, and permission lists that match on custom_fields (SA-C-010's export logs). Not cited, for the reasons under homonyms.
- **cells.tsv line 38 (CM-CNT-006, Shopify, none-held, 7 matches):** redirects in payments, billing, finance and agentic routes, and the help section on storefront redirection by market (SH-I-2152). None is a store's URLs.
- **SA-S-2100 cited in CM-CNT-003 and CM-CNT-008:** the plan line's title is information pages, and its description says they introduce the brand and the policies (from about us to the return policy). The description doesn't narrow the title to policies, so both cite it. See the alternative of nesting CM-CNT-008 under CM-CNT-003, above.
- **M-015's concerns in more than one tree:** a difference of grain (above).
- **landings.tsv line 9 (SH-C-193 clean in CM-SFR-005, cited in CM-CNT-007):** batch 1's row, for the coordinator (above).
- **CM-CNT-006 has no concern landed in its tree:** SA-C-093, the concern behind it, is coarser and lands in CM-CNT-003, strained. A reviewer may move SA-C-093 here; it would stay strained either way.

## The coordinator's correction after batch 3 (30 October)

- **SH-C-193 is `strained` in CM-SFR-005.** Batch 3 cites its SEO apps category (SH-I-1934) in CM-CNT-007, SEO, another tree, as batch 1's reading foresaw (S1).


## Batch 4: area CHN, SH-C-135, SH-C-136, SH-C-137, SH-C-138, SH-C-141, SH-C-195, SA-C-094, SA-C-096, SA-C-097, SA-C-174

Capabilities CM-CHN-001 to CM-CHN-006 are new, with a Shopify and a Salla cell each. Area CHN had none, so no concern joined an existing capability, and no evidence was added to batches 1 to 3's cells. Every reading below is a reading; the landings, cells and rulings cite the keys.

### How the area is cut, and the grains chosen

- **CM-CHN-001 (sales channels and publishing to them) is the root.** Both platforms give it an admin place: Shopify's Sales channels (SH-S-1534, SH-S-1496), Salla's Sales channels (/channels, SA-S-1687). SH-C-135 and SA-C-097 land in it by M-054.
- **Its children follow the grouping the platforms share:**
  - Shopify's help puts Shop, Marketplace Connect and Shopify Collective under online-sales-channels (the identifiers of SH-S-0723, SH-S-0727, SH-S-0729).
  - Salla's plan puts منصة محلي, صانع التطبيقات and سوق الجملة under its sales-channels group knoat-albyaa (SA-S-2067, SA-S-2068, SA-S-2069), and its routes for Mahally, the mobile app, Salla Point, the wholesale market and chat are all under /channel/ (SA-S-3551's path).
  - So: CM-CHN-002 (the platform's own shopping app or marketplace for buyers: Shop, Mahally), CM-CHN-003 (connecting external marketplaces and syncing their orders), CM-CHN-005 (Shopify Collective), CM-CHN-006 (the store's own branded mobile app).
- **CM-CHN-006's parent follows Salla's grouping.** Shopify's statements show only an App Store category and API scopes for mobile apps, with no grouping.
- **CM-CHN-004 (product listings and feeds for channels) is a root.** No held statement puts Shopify's Listings section or product feeds under sales channels. Salla's feed flags sit in its Pixels & feeds concern (SA-C-074), under marketing. scope.tsv's reason for SH-C-138 ("publishing products to sales channels") is a reading, not a statement. A reviewer may nest it under CM-CHN-001 if a statement ties product listings to sales channel apps.
- **SA-C-174 (App Maker publishing policy) lands in CM-CHN-006.** It is a legal page with no admin place, plan line or API of its own, so by the dry run's rule it isn't a capability. It is a finer part of App Maker. Its join is written as `definition`: the store's own app in Apple's and Google's stores (SA-S-5079 against SH-S-6059).
- **CM-CHN-003 and the qualities.** Shopify's plan rows on synced marketplace orders give two qualities: 50 a month free, and 1% up to $99/mo above that (SH-S-7050, SH-S-7051).

### Joins on role (readings)

- **CM-CHN-002:** Shop (SH-S-0723, SH-S-0057) against Mahally (SA-S-0005, SA-S-5044). In both, the platform runs a place where buyers find and buy merchants' products, and the order arrives in the merchant's store. Shop is also a delivery-tracking app; Mahally has its own coupons plan line (SA-S-2009) and a customer-wallet flag that isn't released.
- **CM-CHN-003:** Marketplace Connect (SH-S-0727, plan rows SH-S-7049 to SH-S-7051) against Salla's plan line الربط بمنصات التسوّق العالمية (SA-S-2195). **Salla's line has no description,** so which platforms it connects, and whether orders sync, aren't stated. A Salla help page on the line would settle it.

### Homonyms and terms kept apart

- **"Marketplace":** none of Salla's marketplaces is a sales channel. Its Theme Marketplace (SA-S-1829), Affiliate Marketplace (SA-S-1916), app marketplace (SA-C-194), expert-marketplace and influencer-marketplace flags are markets where partners or services are bought, not places to sell the store's products. None is cited here.
- **"Sales channel" on Shopify, against Salla's.** Shopify's channel is an app connecting the store to an outside surface (SH-S-0699). Salla's channels are its own channels (Mahally, the mobile app), with a column per channel on a product (SA-S-5046, product.channels.changed). They are joined at CM-CHN-001 by M-054, as the store's channels and the publishing of products to them. The difference is in the placements: extension-point on Shopify, core on Salla.

### Strained fits

- **SA-C-097 in CM-CHN-001.** Its dashboard app @salla.sa/ui-merchant-channel (SA-S-3551) serves /channel/ routes other than vendors, chat, mahally, sallapoint, whatsapp and mobile, which include the information pages at /channel/pages. Batch 3 cites the same statement, under SA-C-093's key, in CM-CNT-003. The checker doesn't flag it, because the two keys differ; I marked the fit strained by S1.
- Every other landing is clean.

### Concerns read under `also`, and other domains' statements

- **SA-C-074** (Pixels & feeds, domain D, naming E): its released flags google-merchant-feed, facebook-catalog-feed and snapchat-catalog-feed (SA-S-3201, SA-S-3203, SA-S-3205) are cited as core in CM-CHN-004. Domain D's notes leave them to domain E, and its CM-MKT-009 doesn't cite them. Its google-site-verification flag (SA-S-3202) isn't a feed, and isn't cited.
- **SA-C-098** (wholesale market, domain D, naming B and E): read for U-016, and not cited.
  - Salla's own grouping puts it among sales channels: plan line سوق الجملة under knoat-albyaa (SA-S-2069), route /channel/vendors (SA-S-3553). The seed lists it in CHN (Souq Eljomla).
  - Domain D's CM-B2B-001 holds its selling side, and domain B's CM-CAT-010 its buying side, both citing its plan line or permissions as core.
  - **A lead for the coordinator:** a child of CM-CHN-001 for the wholesale market would cite the same statements as core in a third domain. I left it to D.
- **SA-C-124** (settlements, domain C, not naming E): its Drop shipping app type (SA-S-1193) and settlement endpoint (SA-S-0179) matched CM-CHN-005's Salla search. They are not cited.
- **Not cited:**
  - SA-C-232 (domain A, not naming E): its publishing policy line for App Maker apps on Google and Apple (SA-S-5114, scope صانع التطبيقات). It is a lead for CM-CHN-006's Salla cell, if the coordinator adds E to SA-C-232's also.
  - SA-C-220's report_selling_channels permission (SA-S-2338, reports): a lead for a sales-channel report, which belongs to analytics.
  - SA-C-099's Salla Chat and WhatsApp routes under /channel/ (domain D).
  - Shopify's agentic channel (SH-C-140, domain F, naming E): "Sell in AI chats" is in Shopify's sales channels in the seed. It was not read here, since my concerns' statements don't name it. A lead for a child of CM-CHN-001.

### Rulings

- U-053: joined:CM-CHN-002 (SH-C-136 against SA-C-096).
- U-054, two rows:
  - SH-C-135 against SA-C-097: joined:CM-CHN-001.
  - SH-C-137 against SA-C-097: joined:CM-CHN-003.
  - WC-C-110's side is WooCommerce's part's.
- U-016, two rows:
  - SH-C-141 against SA-C-098: apart. SA-C-098 names E, so a capability here could cite it, but its role differs on its words: a wholesale sale to retail merchants (SA-S-5047), against stores selling each other's products (SH-S-0729).
  - SH-C-141 against SA-C-124: apart. scope.tsv gives SA-C-124 domain C, not naming E.
  - D-anchor ruled the first pair apart too, from its side.
- No pair is left for a later batch.

### For batches 5 to 7 (POS, In-person selling; MKS, Markets, currencies and languages)

- **POS:** Salla Point's route is /channel/sallapoint (SA-S-1836), one of the /channel/ routes with Mahally and the mobile app, and the seed lists POS among Shopify's sales channels. The POS batch may make its root a child of CM-CHN-001, if a statement places it there. Salla's knoat-albyaa plan group, as held, doesn't list Salla Point (search on knoat-albyaa: منصة محلي, صانع التطبيقات, سوق الجملة only).
- **MKS:** no pair of mine has a side in MKS.

### Gaps that change what a cell can claim

- **CM-CHN-003, Shopify:** no statement names Marketplace Connect's maker. Its route is an app's (extension-point), and the cell's core rests on the plan rows and Shopify's own API.
- **CM-CHN-003, Salla:** the plan line is a title only.
- **CM-CHN-004, Salla:** the feed flags are of type app with no app_id. No statement names who makes them.
- **CM-CHN-002, Shopify:** no admin route, plan row or permission for Shop is held, so the cell has no core.
- **CM-CHN-005, Salla:** none-held. Salla's definition of selling between stores is not stated.
- **CM-CHN-001, Salla:** Q1's responsible gap is "page not read". The reason gaps of SH-C-135, SH-C-136, SH-C-137, SH-C-141 and SH-C-195 are "searched, not found", and SH-C-138's responsible gap is "stated only in general terms".

### What the checker flagged

`0 problems, 13 flags`. Mine are six.
- **Five own-service flags: does the statement name the company?**
  - SH-S-0056: "Shop is a Shopify application", in Shopify's terms of service, which name Shopify as the party.
  - SH-S-2756: its scope names the publisher, Shopify Inc.
  - SH-S-0244: "Shopify Consumer Services, such as Shop ... Shopify is directly engaged by the customer".
  - SA-S-0002, twice (Mahally in CM-CHN-002, the app maker in CM-CHN-006): "Salla also offers connected products such as Salla Point, Salla Ads, Mahally, an app maker". I read "Salla" there as the company offering separate products. **A reviewer may read it as the platform's name only;** then it becomes shows. Domain F's CM-APP-002 cites it as shows, for the app marketplace.
- **cells.tsv line 53 (CM-CHN-005, Salla, none-held, 4 matches):** the wholesale market (SA-S-5047) and the Drop shipping app type and settlements (SA-S-1193, SA-S-0179, SA-I-0193). See U-016 above: neither is stores selling each other's products.
- **The other seven flags are batches 1 to 3's,** answered in their notes. No problem on earlier batches' rows.
- **Not flagged, for the merge:** SH-S-0729 and SH-S-7013 (Shopify Collective) are core in CM-CHN-005 and in domain B's CM-CAT-010. SH-C-141 is E's concern, and B cites it under also. On Shopify's plan row ("Sell and source"), the selling side is E's and the sourcing side is B's. The coordinator may make one of the two `shows`.

## Batch 5: area POS, SH-C-087, SH-C-142, SH-C-143, SH-C-144, SA-C-095

Capabilities CM-POS-001 to CM-POS-004 are new, with a Shopify and a Salla cell each. Area POS had none, so no concern joined an existing capability. No evidence was added to batches 1 to 4's cells: none of my concerns' statements bears on them. Every reading below is a reading; the landings, cells and rulings cite the keys.

### How the area is cut, and the grains chosen

- **CM-POS-001 (point of sale) is the area's root.** SH-C-142 and SA-C-095 land in it by M-057. Both give it a place of its own: Shopify's plan rows (SH-S-7017, SH-S-7018) and its terms' 9.3 POS Services; Salla's link /channel/sallapoint (SA-S-1836), its dashboard app (SA-S-3540), its plan line (SA-S-2094) and its permission group سلة بوينت.
- **Its children are Shopify's finer concerns,** which M-057's granularity names ("Shopify also splits POS hardware (SH-C-143) and POS UI extensions (SH-C-144)"), and cash management:
  - CM-POS-002, POS hardware and card-present payment devices (SH-C-143). Shopify gives it the Shopify Hardware Store (SH-S-7270) and its own agreement (SH-I-1398).
  - CM-POS-003, cash management (SH-C-087). Shopify gives it its own scope pair, read_cash_tracking and write_cash_tracking.
  - CM-POS-004, app extensions in the POS app (SH-C-144). Shopify gives it its own extension targets.
  - The parent of each is CM-POS-001 by Shopify's own words: "Extending Shopify POS with UI extensions" (SH-S-0713); the POS Services include Shopify's POS hardware (SH-S-7251); the cash query needs a POS retail role permission (SH-S-5941).

### CM-POS-001's parent: CM-CHN-001, sales channels (batch 4's lead)

A reading, and the weakest call in this batch. I put it under CM-CHN-001 by convention 6: the shared admin grouping. The reviewer may make it a root.
- **For:** both platforms' admin identifiers name the point of sale a channel.
  - Salla's route /channel/sallapoint (SA-S-1836, SA-S-3540) sits beside /channel/mahally and /channel/mobile, which batch 4 nested under CM-CHN-001.
  - Shopify's admin route is apps/point-of-sale-channel (SH-C-086/where/SH-S-6329, domain C naming E). Its retail role permission is view_payment_tracking_sessions_pos_channel (SH-S-5941).
- **Against:**
  - Shopify's help puts POS under manual/sell-in-person (SH-S-0436, SH-S-0585), apart from manual/online-sales-channels, where Shop, Marketplace Connect and Collective sit (SH-S-0723, SH-S-0727, SH-S-0729).
  - Shopify defines a sales channel as an app connecting "a merchant's online store to surfaces outside Shopify" (SH-S-0699).
  - Salla's plan group knoat-albyaa doesn't list Salla Point (batch 4's search).
  - Salla's /channel/ prefix also holds the information pages (/channel/pages, SA-S-1831). Its admin list 4 holds store design, domain, pages and custom URLs too (SA-S-1828, SA-S-1830, SA-S-1833), so it is "store and channels", not channels alone.
- No held statement lists Salla Point on Salla's Sales channels page (/channels).

### Joins on role (readings)

- **CM-POS-002 (U-074):** Shopify's POS Equipment against the payment terminal in Salla Point's card payment.
  - **Shopify:** the merchant may purchase POS Equipment from Shopify "that will allow you to accept Card Present Transactions and Keyed Transactions" (SH-S-7269), on the Shopify Hardware Store (SH-S-7270).
  - **Salla:** card payment in the Salla Point cashier starts by linking a Geidea account (SA-S-5040). Salla Point runs "مباشرة من جوالك أو جهازك اللوحي بدون الحاجة لأجهزة إضافية", directly from the phone or tablet, without additional devices (SA-S-2094). The terminal number is assigned to one device under the payment systems' and NearPay's requirements (SA-S-5042).
  - **The shared role:** the device that takes the card at the point of sale.
  - **The difference is in the placements:** Shopify's company sells the hardware (own-service); Salla's terminal comes from third parties on the merchant's own device (outside).
  - Q1's why_unclear calls them "Sub-parts", and the cut follows it: SA-C-095 lands in the parent.

### Homonyms and terms kept apart

- **"Retail stores" (Salla):** the seed lists it beside Salla Point. Its link goes to /products/branches/stock-management (SA-C-026/where/SA-S-1810), stock in branches, which B-anchor cites (domain B). It isn't the point of sale, and isn't cited here.
- **"Shift" against "cash tracking session":**
  - Salla Point's staff permissions بدء وإنهاء الشفت and عرض تقارير الشفتات (SA-S-2453, SA-S-2452) are core in CM-POS-001.
  - Shopify's cash tracking sessions are in CM-POS-003 (SH-S-5941).
  - Neither platform's statements define them, and no Salla statement says a shift counts cash, so I didn't join them: CM-POS-003's Salla cell is none-held.
  - A Salla help page on Salla Point shifts would settle it.
- **"quick sale" (Shopify) and quick_payment_direct (Salla):** neither is joined.
  - Q1 placed Shopify's quick-sale route and QUICK_SALE permission in SH-C-142, but their words don't name POS, so they are `shows` in CM-POS-001.
  - Salla's quick_payment_direct (الدفع السريع (المباشر)) sits in Salla Point's permission group, but Q1 holds it in SA-C-126 too (payment links, domain C), so it isn't cited.

### Strained fits

- None. SA-C-095's statements are cited in CM-POS-001 and in its child CM-POS-002: SA-S-2094 in both, and the Geidea and terminal statements in CM-POS-002. They are in one tree.

### Concerns read under `also`, and other domains' statements

- **SH-C-086** (in-person card payments, domain C, naming E): read for the parent and for CM-POS-002. Its route apps/point-of-sale-channel (SH-S-6329) is named in CM-POS-001's capability note, and is not cited in a cell. The card rates, offline payments and Shopify Payments rule (SH-S-0047, SH-S-7027, SH-S-0585) are domain C's.
  - **For domain C:** Salla's card payment in Salla Point through Geidea (SA-S-5038 to SA-S-5040) is cited here as `outside` in CM-POS-002, as the device's side. Domain C's in-person card payments may want them. scope.tsv gives SA-C-095 no `also`, so C can't cite them now.
- **SA-C-026 and SH-C-024** (branches and locations, domain B, naming E): read for "Retail stores", and not cited. salla_point_assign_branch (SA-S-2448), changing the branch, ties Salla Point to branches; it is cited in CM-POS-001 only.
- **Not cited:**
  - SH-C-184/responsible/SH-S-0089 (domain A, not naming E): "This P2PE Service is provided, managed, and processed exclusively by Stripe", in the POS Equipment terms. It is a lead for CM-POS-002's Shopify cell, and a slot filler (Stripe), if the coordinator adds E to SH-C-184's also.
  - SH-C-186/decides/SH-S-0593 (subscriptions on POS, domain C) and SH-C-018/decides/SH-S-0276 (no transaction fees on POS orders): payments and billing, not the point of sale itself.
  - SA-C-064/decides/SA-S-3237 (flag loyalty-free-product-pos, not released, domain D).
  - Shopify's POS notification templates (SH-I-2028 to SH-I-2032), inventory entries that my concerns don't hold: a lead for notifications, not for the point of sale itself.

### Rulings

- U-074: joined:CM-POS-002 (SH-C-143 against SA-C-095). WC-C-014's side is WooCommerce's part's.
- M-057 is a match, not a candidate: no ruling.
- No pair is left for batches 6 and 7. None of my concerns has a side in MKS.

### Gaps that change what a cell can claim

- **CM-POS-003, Shopify:** Q1's where and decides gaps on SH-C-087 are "observation needed": the POS screens and admin pages for cash drawer sessions, and the setting or permission that turns it on. The cell's core rests only on Shopify's own API scopes, by the dry run's convention on a platform's own API.
- **CM-POS-003, Salla:** none-held. Salla's definition of cash management at its point of sale is not stated.
- **CM-POS-004, Salla:** none-held. Salla's definition of extending Salla Point is not stated. The partner-requestable salla_point_* permissions (SA-S-2651 to SA-S-2664) give apps access to its data, and are cited in CM-POS-001.
- **CM-POS-002, Salla:** no statement names Salla's company selling or providing hardware. Geidea's and NearPay's parts are stated (slot fillers).
- **CM-POS-002, Shopify:** Q1's reason gap on SH-C-143 is "searched, not found".

### What the checker flagged

`0 problems, 20 flags`. Mine are five.
- **Four own-service flags: does the statement name the company?**
  - SH-S-2757: its scope names the publisher, Shopify Inc., as batch 4's SH-S-2756.
  - SH-S-7269: "purchase POS Equipment from Shopify", in the terms of service, whose party is Shopify.
  - SH-S-7251: "Shopify's POS hardware ("POS Equipment") and any updates thereto provided to you by Shopify", in the same terms.
  - SA-S-0006: "Salla Point (سلة بوينت) is Salla's point-of-sale product". I read "Salla's" as the company's product. **A reviewer may read it as the platform's name only,** as with batch 4's SA-S-0002; then it becomes shows, and CM-POS-001's Salla cell keeps its core.
- **Line 60 (CM-POS-003, Shopify): core rests only on boundary statements.** They are Shopify's own Admin API scopes and its own cash management query for its own feature, which the dry run's convention makes core. The admin place isn't held (the gaps above).
- **Lines 61 and 63 (none-held with matches):** answered in the cells' readings and above. CM-POS-003's matches are cash on delivery, cashback, the fund manager and others, plus Salla Point's shifts. CM-POS-004's matches are SA-C-095's own statements, cited in CM-POS-001.
- **The other flags are batches 1 to 4's,** answered in their notes. No problem on earlier batches' rows.

## The coordinator's corrections after batch 5 (30 October)

- **Stripe in CM-POS-002.** Batch 5's lead: Shopify's POS Equipment terms say "This P2PE Service is provided, managed, and processed exclusively by Stripe and is designed to encrypt cardholder data at the point of interaction" (SH-S-0089). Its concern SH-C-184 (domain A) now names E under `also`, and the statement is cited in CM-POS-002's Shopify cell as `outside`, with Stripe as a slot filler.
- **SA-C-095 names C under `also`,** so domain C's payment batches may cite Salla's Geidea card-present statements (SA-S-5038 to SA-S-5040), which are `outside` here.
- **CM-POS-001's parent** stays CM-CHN-001, by convention 6: both anchor platforms' admin identifiers name the point of sale a channel (Shopify's apps/point-of-sale-channel, Salla's /channel/sallapoint), though Shopify's help puts it under selling in person. The final review weighs it.
- **SH-C-144** (POS UI extensions, domain E naming F) is a lead for domain F's app-extension capabilities; F's cells don't cite it. Listed for the final review.


## Batch 6: area MKS, SH-C-032, SH-C-106, SH-C-107, SH-C-108, SH-C-109, SH-C-110, SH-C-111, SH-C-112, SH-C-113, SA-C-008

Capabilities CM-MKS-001 to CM-MKS-009 are new, with a Shopify and a Salla cell each. Area MKS had no capability, so no concern joined an existing one. Every reading below is a reading; the landings, cells and rulings cite the keys.

### How the area is cut, and the grains chosen

- **Markets is a root, CM-MKS-001,** with five children: CM-MKS-002 (rollouts), CM-MKS-003 (merchant of record for cross-border selling), CM-MKS-004 (local domains and visitor geolocation), CM-MKS-006 (prices in the buyer's currency), which holds CM-MKS-007 (currency conversion and exchange rates).
- **Prices in the buyer's currency are under Markets, by the grouping the two platforms share.**
  - Shopify sets a currency per market in Markets (SH-S-0547; admin route markets for SH-C-108 and SH-C-109, SH-S-6354, SH-S-6356).
  - Salla sets "the default currency and the other supported currencies for the market" (SA-S-0159), and its automatic exchange-rate option is in its markets product-price setting (the key markets/product_prices of SA-S-0117).
  - **Where the groupings differ:** Salla's Currencies settings are at general/currencies (SA-S-1724), not under Markets, and Shopify's help files multi-currency and conversion fees under store-currency (the paths of SH-S-0366 and SH-S-0363). A reviewer may prefer a root currency tree: CM-MKS-005 as the parent of CM-MKS-006 and -007.
- **The store currency, CM-MKS-005, is a root.** Shopify's admin keeps it apart from Markets (account setup, SH-S-0671; SH-C-107's where is its help on store currency). Salla's default currency is in the store's settings (SA-S-0154).
- **The store's languages, CM-MKS-008, are a root.** Both platforms give languages a settings section of their own (Shopify SH-S-1501, Salla SA-S-1723). Shopify's market customizations name languages (SH-S-0541) and Salla's market page names none, so they are not nested under Markets. Translation, the translation log and Salla's message translation are in the same capability: on both platforms they sit with the languages (Salla's /manage/languages/logs, SA-S-1896; Shopify's translations scopes beside the locales ones).
- **The backup region (SH-C-113) is not a capability.** It has no admin section, API group, plan line or app category of its own: it is set in Settings > General (SH-S-6358) and has a webhook topic. So it lands in CM-MKS-001, whose Shopify cell cites it.
- **CM-MKS-002 (rollouts) follows Shopify's grouping.** Its help is at manual/markets/rollouts (SH-S-0576), and its staff permissions are "Markets > Catalogs > View rollouts" and the like (SH-I-0967 to SH-I-0969, not cited). It is Shopify's own place: an admin route, an entitlement, a scope and webhooks. Salla's side is a store-design plan line (below).
- **CM-MKS-003 is under Markets by Shopify's grouping,** its routes managed and :id/managed being in section Markets (SH-S-7130, SH-S-7131). Salla's side is a partners page.
- **CM-MKS-004 is under Markets,** since a market has a web presence (SH-S-7458). **An alternative for the reviewer:** nest it under CM-SFR-008 (store domains), since Assign local domains is about domains. I kept one capability for local domains and geolocation, the grain of SH-C-111 and of Q1's M-087. A reviewer may split the Geolocation apps category off; SH-C-111 would then land in the parent.
- **The currency grain.** Q1's M-044 joins SH-C-107, SH-C-108 and SH-C-109 with SA-C-163, a match with three concerns on one side: a difference of grain. Shopify's three concerns land in three capabilities, CM-MKS-005, -006 and -007.
- **CM-MKS-009, countries, cities and districts reference data,** is added for SA-C-166, which batch 7 lands. It is Salla's alone: its own API folders and its countries scope.

### Joins on role (readings)

- **CM-MKS-002:** Shopify's rollout, "a scheduled set of changes to your online store's main theme, checkout and accounts pages, discounts, product catalogs" (SH-S-0576), against Salla's Plus plan line جدولة نشر النسخ, scheduling the publishing of theme versions (SA-S-2034). Both schedule a change to the live store's theme; Salla's is narrower.
- **CM-MKS-003:** Global-e becoming the merchant of record under Managed Markets (SH-S-0563), against Salla's المدفوعات و البيع بالنيابة (MoR) in the target market (SA-S-5129). In both, a party other than the merchant takes on the merchant of record's role for sales abroad. **Salla's statement doesn't say who that party is**, so its cell is shows and extension-point (SA-S-5130), not outside.
- **CM-MKS-004:** Shopify's country selector, so "your store displays their local currency" (SH-S-7288), against Salla's currency shown by the customer's geographic location (SA-S-0154). No Salla statement gives a market a domain.
- **CM-MKS-005:** Shopify's store currency (SH-S-0361) against Salla's default currency in the store's settings (SA-S-0154). Salla doesn't define it.

### Homonyms and terms kept apart

- **"Geolocation"** names different things on the two platforms:
  - Shopify's Geolocation apps (SH-S-2681; help "Using the Geolocation app", SH-I-2153) send buyers to their market;
  - Salla's app category Geolocation / الموقع الجغرافي (SA-S-1226, titled تحديد دقيق للمواقع), with its map services (google-maps-service and others), serves customer addresses. It is cited in domain D's CM-CUS-009 and not here. U-079 is ruled apart.
- **"Market selection"** (SA-S-1730, markets/browse_product_method) is cited in CM-MKS-001. It is also among SA-C-026's (branches, domain B) platform terms. No statement says what it selects.

### Strained fits

- **SH-C-111 in CM-MKS-004:** its MarketWebPresence (SH-S-7458), "which defines its SEO strategy", is also cited in CM-CNT-007 (SEO) as core: batch 3's lead.
- **SH-C-032 in CM-MKS-008, and SH-C-108 in CM-MKS-006:** Q1 placed the App Store category Currency and translation apps (SH-I-1916) in both concerns. It is cited in both capabilities, as extension-point, since the category names both.

### For the coordinator: earlier batches' rows

- **CM-CNT-007, Shopify (batch 3's cell):** I added SH-C-111/boundary/SH-S-7458 as core. The cell's derived placement is now core;extension-point. Its reading, and batch 3's gap note, still say that no statement shows SEO built into Shopify's admin. The added statement is an API object, not an admin setting; the reading should name it.
- **SA-C-090 in CM-SFR-001 (batch 2's row, landings.tsv line 12):** its plan line SA-S-2034 is now cited in CM-MKS-002. By S1 it is strained; the checker flags it.
- **U-076 has two rulings.** Domain F's part ruled SH-C-110 against SA-C-304 apart, on the basis that scope.tsv gives SH-C-110 domain E without F under also. Here, SA-C-304 names E under also, so CM-MKS-003 may cite it, and the ruling follows the cells: joined:CM-MKS-003. Each part ruled by its own rule. The coordinator reconciles; nothing in F's cells changes.
- No problem on earlier batches' rows from the checker.

### Concerns read under `also`, and other domains' statements

- **SA-C-304** (domain F, also E): SA-S-5129 is cited in CM-MKS-003 as shows and SA-S-5130 as extension-point. Domain F's CM-PTN-007 cites them as shows and extension-point too, so neither supports core in two domains. Q1's decides gap on SA-C-304 is "observation needed".
- **SA-C-065** (domain D, also E): read for U-079, and not cited.
- **SA-C-164** (domain C, also E): read for U-028, and not cited. SA-S-0067 says payments through Salla's gateway are received in riyals, which is the settlement currency, not a conversion.
- **SA-C-160** (domain C, not naming E): SA-S-0145 defines a market as "the country or region you target selling to", for its tax registration. **Not cited.** SA-S-0157 carries Salla's definition of Markets.
- **SA-C-090** (landed in CM-SFR-001): SA-S-2034, cited in CM-MKS-002.

### Rulings

- U-065:
  - SH-C-032 against SA-C-008: joined:CM-MKS-008.
  - SH-C-106 against SA-C-008: apart. Markets and languages are separate roots.
- U-076 (SH-C-110 against SA-C-304): joined:CM-MKS-003.
- U-079 (SH-C-111 against SA-C-065): apart.
- U-028 (SH-C-109 against SA-C-164): apart.

### For batch 7 (SA-C-163, SA-C-165, SA-C-166)

**Landings.** My Salla cells already cite these concerns' statements:
- **SA-C-165** in CM-MKS-001, by M-043. Its SA-S-0159 is cited in CM-MKS-006, in the same tree, so the fit is clean. SH-C-106's landing is written as a definition join only because SA-C-165 hadn't landed; it can then be rewritten as match:M-043.
- **SA-C-163** is coarser than my currency capabilities. Its statements are cited in four of them:
  - its default currency in CM-MKS-005, a root;
  - its Currencies settings, plan line, permission and flags in CM-MKS-006;
  - currency-exchange and the automatic exchange rate in CM-MKS-007;
  - the currency shown by location (SA-S-0154) in CM-MKS-004, and also in CM-MKS-005 and -006.
  
  By M-044 its natural place is CM-MKS-006. It is **strained** wherever it lands, since CM-MKS-005 is another tree. Once it lands, SH-C-107, SH-C-108 and SH-C-109 can be rewritten as match:M-044.
- **SA-C-166** in CM-MKS-009, single (Q1's M-082 is with WooCommerce only).

**Ruling pairs whose Salla side batch 7 lands:**
- U-033, SH-C-106 against SA-C-165: CM-MKS-001 cites both sides (SH-S-0540, SA-S-0157), so joined:CM-MKS-001.
- U-065, SH-C-106 against SA-C-165: joined:CM-MKS-001, the same keys.
- U-065, SH-C-032 against SA-C-165: apart on my cells. CM-MKS-008 cites SH-C-032 and none of SA-C-165, and CM-MKS-001's Salla cell names no language.

### Gaps that change what a cell can claim

- **CM-MKS-003, Salla:** no statement says who acts as merchant of record in Salla's programme, or whether Salla offers it in its admin.
- **CM-MKS-005, Salla:** the default currency isn't defined (what it prices or reports in).
- **CM-MKS-007, Salla:** no statement says whether a merchant can set a rate by hand, or who supplies the rate.
- **CM-MKS-008, Shopify:** no statement names the maker of the Translate & Adapt app (SH-I-2163), so it is shows.
- **CM-MKS-004, Shopify:** no statement names the maker of the Geolocation app (SH-I-2153).
- **CM-MKS-009:** SA-C-166's decides gap is "page not read": who keeps the lists isn't held. Shopify is none-held, so the definition isn't stated on Shopify's side.
- **Responsible and reason gaps:** SH-C-032, -107, -108, -111, -112 and -113 are "stated only in general terms" or "searched, not found"; SA-C-008, -163 and -165 are "page not read". Each cell's reading names its own.

### Qualities and slot fillers

- **Qualities:**
  - Salla: 40 languages (SA-S-2074), +33 currencies for payment (SA-S-1970), and more than 15 currencies in the payments integration (SA-S-0012). Q1's note records the difference between the two currency counts.
  - Shopify: "Add language (136 languages)" (SH-I-2098), a placed inventory entry no statement covers.
- **Slot fillers:**
  - Global-e, in CM-MKS-003: SH-S-0563, and SH-S-0127 with its Canada, UK and US scope.
  - Adyen, in CM-MKS-006: SH-S-0545.

### What the checker flagged

`0 problems, 29 flags`. Mine:
- **cells.tsv line 80 (CM-MKS-009, Shopify, none-held, 70 matches):** the matches are Shopify Payments', Balance's, Capital's and Tax's country eligibility, unsupported countries, regions in eligibility rules, and a legal entity's country code. None is a list of countries, cities or districts that the store reads.
- **SA-S-2034 in CM-MKS-002 and CM-SFR-001:** a join on role (above). SA-C-090's strain is for the coordinator.
- **SA-S-0154 in CM-MKS-004, -005 and -006:** one sentence names both the default currency in the settings and the currency shown by location. It is cited where each part bears; SA-C-163's strain is batch 7's.
- **SH-S-7458 in CM-CNT-007 and CM-MKS-004:** SH-C-111 is strained (above).
- **SH-I-1916 in CM-MKS-006 and CM-MKS-008:** SH-C-032 and SH-C-108 are strained (above).
- **M-044's concerns in more than one tree:** a difference of grain (above).
- **landings.tsv line 12 (SA-C-090):** batch 2's row, for the coordinator.
- **CM-MKS-009 has no concern landed in its tree:** SA-C-166 lands there in batch 7.

The other flags are batches 1 to 5's, answered in their notes.

## The coordinator's corrections after batch 6 (30 October)

- **SA-C-090 is `strained`:** batch 6 cites its plan line SA-S-2034 in CM-MKS-002 (S1).
- **CM-CNT-007's Shopify cell** now reads `core` as well as `extension-point`: batch 6 cites MarketWebPresence (SH-S-7458), Shopify's own API object that defines a market's SEO strategy. Batch 3's note that no statement shows Shopify's own SEO holds only for the admin's titles and meta descriptions.
- **U-076 is ruled differently** by F's part (`apart`, from F's cells) and by this batch (`joined:CM-MKS-003`, since SA-C-304 names E under `also`). Each domain rules from its own cells; the merge flags the pair for one answer at the final review.


## Batch 7: area MKS, SA-C-163, SA-C-165, SA-C-166 (the last batch)

No capability is added. The three concerns land in batch 6's capabilities, whose Salla cells already cited most of their statements. Every reading below is a reading; the landings, cells and rulings cite the keys.

### Landings

- **SA-C-165 in CM-MKS-001, match:M-043, clean.** Its market currencies (SA-S-0159) are cited in CM-MKS-006, a child of CM-MKS-001.
- **SA-C-163 in CM-MKS-006, match:M-044, strained.**
  - Q1's note on M-044 pairs SH-C-108 with SA-C-163, and the concern is the currencies a customer picks beside the cart (SA-S-0155).
  - It is coarser than CM-MKS-006: its exchange rate is cited in CM-MKS-007 (a child) and its currency shown by location in CM-MKS-004 (same tree).
  - **Strained:** SA-S-0154 is also cited in CM-MKS-005 (store currency), a root, where it is Salla's only evidence. A reviewer who makes CM-MKS-005 the parent of CM-MKS-006, the alternative batch 6 named, would make the fit clean.
- **SA-C-166 in CM-MKS-009, single, clean.** Q1's M-082 joins it with WooCommerce only.

### Evidence added to existing cells

All Salla, all statements of my concerns that batch 6 hadn't cited:
- CM-MKS-001: SA-C-165/boundary/SA-S-1055 (Store Scopes folder, boundary placement), core.
- CM-MKS-006: SA-C-163/boundary/SA-S-1060 (Currencies folder), core; SA-C-163/decides/SA-S-2605 (currency_setting_edit / إعدادات العملات as a partner's permission), shows, as batch 5 cited partner permissions; SA-C-163/boundary/SA-S-1562 (access scope Meta Data), shows.
- CM-MKS-009: SA-C-166/boundary/SA-S-1048 (Countries folder), core; SA-C-166/boundary/SA-S-1562 (Meta Data), shows.

The cells' readings, batch 6's rows, don't name these additions; the derived placements don't change (each cell already had core).

### Rulings

- **U-033, SH-C-106 against SA-C-165: joined:CM-MKS-001** (SH-S-0540, SA-S-0157).
- **U-065, SH-C-106 against SA-C-165: joined:CM-MKS-001** (SH-S-0541, which names languages among a market's customizations, and SA-S-0157).
- **U-065, SH-C-032 against SA-C-165: apart.**
  - Shopify's Localizations and Languages (SH-S-0778, SH-S-1501) are cited in CM-MKS-008 and Salla's Markets (SA-S-0157) in CM-MKS-001, two roots.
  - **For the reviewer:** one capability does cite both concerns. CM-MKS-006 cites SH-I-1916, the App Store category Currency and translation apps, which Q1 placed in both SH-C-032 and SH-C-108, beside SA-C-165's market currencies (SA-S-0159).
  - My reading: that co-citation is the category's currency half, SH-C-108's side, not Shopify's localizations against Salla's Markets. So the ruling's keys are the statements that stand for localization and for Markets.
  - If the reviewer reads SH-I-1916 as SH-C-032's key, the ruling becomes joined:CM-MKS-006. The checker tests the ruling on its keys, so it doesn't catch this.

With batch 6's rows, U-065's four Shopify–Salla pairs are all ruled.

### For the coordinator: earlier batches' rows

- **Joins that can now be written as Q1 matches.** Both sides have landed:
  - SH-C-106's landing (`definition`) can be rewritten as match:M-043;
  - SH-C-107 (`role`), SH-C-108 (`definition`) and SH-C-109 (`terms`) can be rewritten as match:M-044.
- **The access scope Meta Data (SA-S-1562) is read two ways in this part.** Batch 3 cites SA-C-033/boundary/SA-S-1562 as core in CM-CNT-007. Batch 6 (CM-MKS-008) and I (CM-MKS-006, CM-MKS-009) cite it as shows, since the statement names neither languages, currencies nor countries; only Q1's note ties the scope to each concern's operations. One reading should hold for all four.
- The whole part's check prints no problem on earlier batches' rows.

### Gaps that change what a cell can claim

- **SA-C-163 and SA-C-165:** Q1's responsible and reason gaps are "page not read".
- **SA-C-166:** the decides gap is "page not read", so who keeps the countries, cities and districts lists isn't held.
- **SA-C-166's inventory:** it holds the Partners portal's country list (SA-I-1705 onward, other:portal-countries). I don't cite it: it is a list, not a statement of the capability.

### What the whole part's check flagged

`0 problems, 27 flags for the reviewer` (`python3 -I method/check_class_part.py studies/class-model/parts/E-anchor`). My flags:
- **SA-C-163/decides/SA-S-0154 in CM-MKS-004, -005 and -006:** SA-C-163 is strained (above).
- **M-044's concerns land in more than one tree:** a difference of grain, batch 6's cut. SA-C-163 lands with SH-C-108, the pair Q1's note names.
- **SH-I-1916 in CM-MKS-006 and CM-MKS-008:** batch 6's; it bears on U-065 (above).

Batch 6's flag that CM-MKS-009 had no concern landed is answered: SA-C-166 lands there. The other flags are batches 1 to 6's, answered in their notes.

## The coordinator's corrections after batch 7 (30 October)

- **SH-C-106, SH-C-108 and SH-C-109 are written as Q1's matches** (M-043, M-044), now that their Salla sides have landed. SH-C-107 stays as batch 6 wrote it: it lands in CM-MKS-005, store currency, a root of its own, where none of M-044's other concerns landed.
- **The access scope Meta Data (SA-S-1562)** names no subject. It is `shows` in all four capabilities that cite it, CM-CNT-007 included, where batch 3 had it `core`. Salla's SEO cell stays `core` on its other rows.
- **U-065's pair SH-C-032 against SA-C-165** is `apart` on its keys, while CM-MKS-006 cites SH-I-1916, an entry Q1 placed in both SH-C-032 and SH-C-108. Batch 7 reads it as the category's currency half. The final review weighs it.
- **The part is complete:** 40 capabilities, 52 landings, 80 cells. Domain E's mapping parts follow: WooCommerce, Zid and BigCommerce.
- **SA-S-2133 counts once.** Salla's plan line for AI-generated SEO at extra fees is `core` in F's CM-AIA-003, whose Salla cell rests on it alone, and `shows` in CM-CNT-007, which stays `core` on its other rows.
