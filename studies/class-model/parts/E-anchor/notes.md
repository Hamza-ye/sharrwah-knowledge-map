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

