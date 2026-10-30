# E-bigcommerce: notes

The mapping part for BigCommerce in domain E (Store presence and channels). It runs in two batches. Every row below is a reading unless it quotes a statement.

## Batch 1: areas SFR and CNT

**Concerns landed (13):** BC-C-011, BC-C-040, BC-C-041, BC-C-042, BC-C-043, BC-C-044, BC-C-045, BC-C-049, BC-C-050, BC-C-051, BC-C-052, BC-C-053, BC-C-078.
- 11 joined existing capabilities: BC-C-011 (CM-SFR-013), BC-C-041 (CM-CNT-009), BC-C-042 (CM-SFR-001), BC-C-043 (CM-SFR-005), BC-C-044 (CM-SFR-004), BC-C-045 (CM-CNT-003), BC-C-049 (CM-CNT-002), BC-C-050 (CM-SFR-011), BC-C-051 (CM-SFR-006), BC-C-053 (CM-SFR-012), BC-C-078 (CM-SFR-010).
- 1 made a new capability: BC-C-040, Sites and routes, CM-SFR-014 (parent CM-SFR-011).
- 1 moved: BC-C-052, Native Hosting, `moved:G`.

**Cells:** BigCommerce's cell for all 22 capabilities of SFR and CNT, and for CM-SFR-014: 23 cells, 19 `statements`, 4 `none-held` (CM-SFR-009, CM-CNT-001, CM-CNT-005, CM-CNT-006). Qualities: 3. Slot fillers: none (no statement of these cells names a third party by name or a law doing the capability; "the designer licensor" and "external developers" in BC-S-0240 and BC-S-0241 name no one).

**Rulings:** none. Q1 never matched BigCommerce, so no unclear candidate holds a BigCommerce concern (`concerns --platform bigcommerce --domain E` lists no match or candidate); `rulings.tsv` holds only its header.

### How I cut, and the grains

- **CM-SFR-014, Sites and routes (new).** BigCommerce gives it an API group of its own (Sites, BC-S-0231), an access scope (store_sites, BC-S-0232) and webhook topics (BC-S-0233, BC-I-0263), so it is a capability by the dry run's convention (a place of its own). Parent CM-SFR-011: BC-S-0231 puts sites and routes with "headless storefront sales channels". Not CM-SFR-008, the store's domain: no statement of BC-C-040 speaks of a domain. Not CM-CNT-006 (Custom URLs): no statement defines a route further. The back-fill part writes the other platforms' cells.
- **BC-C-052, Native Hosting, moved to G.** "BigCommerce provides hosting for your Catalyst projects" (BC-S-0288) and the Infrastructure Hosting API group (BC-S-0287) are hosting of the store, G's CM-OPS-003, whose BigCommerce cell already cites both as core (BC-C-052 names G under also). One thing, one domain: I added no hosting capability under CM-SFR-011, though Shopify's CM-SFR-011 cell cites Oxygen (SH-S-0710), Shopify's hosting for Hydrogen, which the coordinator may want to weigh against CM-OPS-003 the same way. BC-S-0287 also says "add custom domains": I cite it once more, in CM-SFR-008, for the custom domains only (see the flags).
- **BC-C-042, Themes, lands in the parent CM-SFR-001.** It is coarser than the theme's children: its Stencil engine and custom templates are cited in CM-SFR-002, its design-theme licence terms in CM-SFR-003. All three are under CM-SFR-001, so the fit is clean.
- **BC-C-045, Pages and store content, lands in CM-CNT-003.** It holds pages and the built-in blog (CM-CNT-004, the child), and its Content API also manages redirects (BC-S-0252), cited in CM-CNT-009 too. The GraphQL Storefront API's site content (BC-S-0256) and the reason for it (BC-S-0257) are cited in CM-CNT-003, not CM-SFR-012, to keep the concern in one tree where the statement's subject is the content.
- **BC-C-049, Metafields, lands in CM-CNT-002.** BigCommerce's statements hold metafields only (searched: metaobject;metaobjects;definition;custom data;custom fields: no hit), so the cell claims metafields, not metaobjects.
- **BC-C-050, Catalyst, lands in CM-SFR-011** as `core`: "BigCommerce's ... headless ecommerce storefront framework" (BC-S-0281), the place Shopify's Hydrogen has. Its statement that Catalyst implements the GraphQL Storefront API (BC-S-0283) goes to CM-SFR-012, CM-SFR-011's child.

### Joins on role

- **BC-C-043, Widgets, in CM-SFR-005.** BigCommerce's Widgets API (widget templates, widgets, regions, placements, BC-S-0244) and page widgets (BC-S-0245) add elements to the storefront's pages besides the theme, the role of Shopify's Store design apps (SH-S-2662) and Salla's Component Bundle (SA-S-1165). BigCommerce builds them itself (`core`), where the anchor's statements show apps and partners (`extension-point`).
- **BC-C-044, Scripts, in CM-SFR-004.** An app's scripts in the storefront (BC-S-0249), the role of Shopify's script tags (SH-S-6291) and Salla's App Snippet (SA-S-0209). Strained (below).

### Homonyms

None kept apart in this batch. Two terms to watch:
- **Storefront API.** BigCommerce has a GraphQL Storefront API (BC-C-053, cited in CM-SFR-012) and a REST Storefront API authenticated by CORS headers (BC-S-0054 in BC-C-008, BC-S-0218 in BC-C-037, domains B and A), for BigCommerce-hosted storefronts. Neither REST statement is cited here; the CM-SFR-012 cell rests on the GraphQL API only.
- **Content.** BigCommerce's Content API (store_v2_content, BC-S-0254) manages blog posts, pages and redirects; Shopify's admin section Content holds metaobjects, files, menus and blogs. They are not the same grouping; no join rests on the word.

### Strained fits

- **BC-C-044 in CM-SFR-004.** CM-SFR-004 is an installed app's code in the storefront. BigCommerce's Script Manager is also the merchant's own place to add and inspect scripts in a storefront's channel settings (BC-S-0248, BC-S-0249). A proposal for the coordinator: rename CM-SFR-004 "App and custom code in the storefront (… BigCommerce: Scripts, Script Manager)", or split the merchant's own scripts out.
- **BC-C-045 in CM-CNT-003.** BC-S-0252 ("Manage blog posts, blog tags, content pages, and redirects") is cited in CM-CNT-003, CM-CNT-004 and CM-CNT-009; CM-CNT-009 is not under CM-CNT-003.
- **BC-C-051 in CM-SFR-006.** CM-SFR-006 sits under CM-SFR-005 and CM-SFR-001, the theme's storefront; BigCommerce's statements put Makeswift with Catalyst, its headless framework (BC-S-0284, BC-S-0286), which is CM-SFR-011's tree. The reviewer may prefer CM-SFR-006 without a theme parent, or a page-builder capability under CM-SFR-011.
- **BC-C-078 in CM-SFR-010.** The concern is wider than the SSL certificate: its Storefront Security settings (BC-S-0422) don't say what they set, and its Tier 1 certifications (ISO, SOC, PCI, FIPS, RH-ISAC, GDPR, CCPA, BC-S-0421) bear on the platform's security and compliance as a whole. No capability of any domain holds that (`caps --terms "PCI; ISO; SOC; compliance; certifications; security; …"` finds none). I record BC-S-0421 as a quality of CM-SFR-010 and cite it as `shows`, so it isn't left uncited; the coordinator may move it to a platform-security capability in A or G.

### Concerns read under `also`, and other domains' statements

- **BC-C-010** (domain D, Marketing): BC-S-0062, "Create coupons, banners, and gift certificates programmatically through the BigCommerce Marketing APIs", cited as `core` in CM-SFR-007 for the banners. D already cites it as `core` in CM-MKT-002 (coupons) and CM-LOY-002 (gift certificates): one statement naming three objects. The merge will flag it as core in two domains; I keep it, since it is BigCommerce's only statement held on banners.
- **BC-C-047** (domain A, Store profile and storefront settings): BC-S-0266 (Storefront SEO settings) and BC-S-0263 (Settings APIs, "SEO settings, and search filters") in CM-CNT-007; BC-S-0263 also in CM-SFR-013; BC-S-0262 (store information's domain) in CM-SFR-008 as `shows`. A-bigcommerce hasn't run, so A cites none of them yet; the merge may flag BC-S-0263 and BC-S-0266 as core in two domains if A cites them as core.
- **BC-C-086** (domain A, without E under also): BC-S-0472, the merchant's privacy policy "readily accessible to Your Users", cited as `shows` in CM-CNT-008, because it is BigCommerce's only statement held on the store's own policies, as WooCommerce's CM-CNT-008 cell cites WC-S-5408 from domain C.
- **BC-C-038** (domain E, batch 2's concern): BC-S-0221, the plan line Online storefront, cited as `core` in CM-SFR-001.
- **BC-C-052** (moved to G): BC-S-0287 cited in CM-SFR-008 for "add custom domains".

### Gaps that change what a cell claims

- CM-SFR-003: no statement held names a theme marketplace, theme store or theme-partner programme of BigCommerce's (searched: theme marketplace;theme store;Themes Marketplace;Theme Marketplace;theme partner;design theme). The cell shows licensed third-party design themes (`shows`, `outside`) and claims no marketplace.
- CM-SFR-006: Makeswift's maker. BC-S-0285 is a row of BigCommerce's list of contracting entities naming "Makeswift, Inc." for the "Makeswift visual editor / builder", and BC-S-0284 calls Makeswift "BigCommerce's visual page builder". No statement held says in words that Makeswift, Inc. is a company of BigCommerce's group: the `own-service` placement rests on the contracting-entity list being BigCommerce's own, a reading. What enables Makeswift: searched, not found (BC-C-051/decides).
- CM-SFR-013: BC-S-0068's Q1 note infers that Product filtering is included from Scale up; the note never counts, so the cell claims no plan for the line.
- CM-SFR-014 and CM-CNT-009: what turns sites or redirects on or limits them: page not read (BC-C-040/decides, BC-C-041/decides).
- CM-SFR-011, CM-SFR-012, CM-CNT-002: what enables Catalyst, the Storefront API or metafields: searched, not found.
- Every concern of this batch: who is legally responsible is stated only in general terms (each concern's `responsible` gap), except BC-C-042 (the designer licensor, BC-S-0240) and BC-C-051 (Makeswift, Inc., BC-S-0285).

### What the checker flagged, and my answers

The batch check ends "0 problems" after this file was written (the one problem before it was notes.md missing). Its 8 flags:
1. **own-service on BC-S-0285 and BC-S-0284 (Makeswift).** Answered above (Gaps, CM-SFR-006): BC-S-0284 says "BigCommerce's visual page builder" and BC-S-0285 names Makeswift, Inc. in BigCommerce's own list of contracting entities as the provider of the Makeswift visual editor / builder. That Makeswift, Inc. is of BigCommerce's group is a reading; if the reviewer reads the list as not naming the group, both rows become `shows` and the cell `not-stated`.
2. **BC-S-0472 is BC-C-086's (domain A, no E under also).** Answered above: it is the only statement held on the store's own policies, and it supports `shows` only.
3. **CM-CNT-001 none-held with 9 matches.** Every hit is named in the cell's reading and none is a library of the store's files (digital products' files, file storage on the plan line, hosting artifacts, segment files, a carrier's specification file, SFTP to Feedonomics, a payment method on file, the merchant's backups).
4. **CM-CNT-005 none-held with 2 matches.** BC-S-0303 is the control panel's Settings menu for API accounts; BC-I-0289 is social media links. Neither is a storefront menu.
5. **CM-CNT-006 none-held with 2 matches.** BC-S-0286 is the Makeswift site URL (cited in CM-SFR-006), BC-S-0382 a shipping provider's Quote URL. Neither is a custom URL for the store's pages.
6. **BC-S-0252 in CM-CNT-003, CM-CNT-004 and CM-CNT-009, more than one tree.** The statement names three things: content pages and blog posts (CM-CNT-003 and its child CM-CNT-004) and redirects (CM-CNT-009). URL redirects are not a part of store pages on any platform's grouping held, so I keep CM-CNT-009 apart and mark BC-C-045's landing strained.
7. **BC-S-0263 in CM-CNT-007 and CM-SFR-013, more than one tree.** The statement lists settings the Settings APIs manage, "SEO settings, and search filters": two things, one in each capability. BC-C-047 isn't landed here (domain A), so no fit rests on it.
8. Not a separate flag line, but the merge will raise it: BC-S-0062 (CM-SFR-007, and D's CM-MKT-002 and CM-LOY-002) and BC-S-0287 (CM-SFR-008, and G's CM-OPS-003) support `core` in two domains. Each names two or three objects, one per capability; answered under "Concerns read under also" and "How I cut".

### Problems with the brief or the evidence

- The batch message says "rule on the unclear candidates that hold your concerns"; the brief says Zid and BigCommerce have none, and the slice confirms it. No rulings.
- The brief says "22 in all" for the two areas; with the new CM-SFR-014 the batch writes 23 cells.

## For batch 2 (areas CHN, POS and MKS)

- **Your concerns:** BC-C-038 (Channels), BC-C-039 (Multi-Storefront), BC-C-048 (Locales and translations), BC-C-067 (Feedonomics), BC-C-068 (Marketplaces and social channels), BC-C-069 (Point of sale), BC-C-074 (Currencies), BC-C-075 (Geography). None of them is landed yet.
- **Already cited by batch 1:** BC-C-038/decides/BC-S-0221 (plan line Online storefront) in CM-SFR-001 as core. If BC-C-038 lands in a CHN capability, cite its other statements there; BC-S-0221 stays in CM-SFR-001 (the online storefront is the theme's store), and the landing's reading should say so, or mark the fit strained.
- **Sites belong to channels.** BC-C-040 (CM-SFR-014) speaks of "headless storefront sales channels" and a site "associated with the specified channel" (BC-S-0233). If batch 2 builds a channel capability from BC-C-038 ("A channel is anywhere a merchant sells their products. This encompasses headless storefronts, marketplaces, POS systems", BC-S-0220), check whether CM-SFR-014's parent should stay CM-SFR-011; leave a note for the coordinator rather than changing batch 1's row.
- **Multi-Storefront (BC-C-039)** may bear on CM-SFR-001 and CM-SFR-014 (several storefronts on one backend; Redirects already says "one or more storefronts powered by a single BigCommerce backend", BC-S-0234). Add evidence to batch 1's cells by appending rows, not by rewriting them.
- **Feedonomics (BC-C-067):** BC-S-0367 (SFTP to Feedonomics Holdings LLC) is named, not cited, in CM-CNT-001's reading. Feedonomics Holdings LLC is also in BigCommerce's contracting-entity list (BC-I-0458 is its privacy policy), the same maker question as Makeswift's: use the same reading or note why not.
- **Locales and translations (BC-C-048):** BC-S-0270 ("available on any storefront type – Stencil, Catalyst or any other headless") isn't cited by batch 1.
- **Domains:** CM-SFR-008's BigCommerce cell rests on BC-S-0287 (hosting projects' custom domains) and BC-S-0262; nothing in batch 2's areas should need it.
- **The last batch checks the whole part** without `--concerns` and `--areas`.

## The coordinator's corrections after batch 1 (30 October)

- **BC-C-052, Native Hosting, is G's:** scope.tsv gives it domain G with E under `also`, and `G-amend` lands it in CM-OPS-003, hosting of the store.
- **BC-S-0287 counts once:** `core` here in CM-SFR-008, whose BigCommerce cell rests on it, and `shows` in G's CM-OPS-003.
- **CM-SFR-014, sites and routes of a headless storefront channel,** is new: `E-backfill-bigcommerce` writes its cells for the other four platforms after batch 2.
- **The Tier 1 certifications (BC-S-0421),** recorded as a quality of CM-SFR-010, bear on platform-wide security and compliance: domain A's TRU batches and A's BigCommerce part weigh where they belong.

## Batch 2: areas CHN, POS and MKS

**Concerns landed (8):** BC-C-038, BC-C-039, BC-C-048, BC-C-067, BC-C-068, BC-C-069, BC-C-074, BC-C-075.
- 7 joined existing capabilities: BC-C-038 (CM-CHN-001, terms, strained), BC-C-067 (CM-CHN-004, role), BC-C-068 (CM-CHN-003, definition, strained), BC-C-069 (CM-POS-001, terms, strained), BC-C-048 (CM-MKS-008, terms), BC-C-074 (CM-MKS-006, terms, strained), BC-C-075 (CM-MKS-009, terms).
- 1 made a new capability: BC-C-039, Multi-Storefront, CM-CHN-007 (parent CM-CHN-001).
- None moved.

**Cells:** BigCommerce's cell for all 19 capabilities of CHN, POS and MKS, and for CM-CHN-007: 20 cells, 11 `statements`, 9 `none-held` (CM-CHN-002, CM-CHN-005, CM-CHN-006, CM-MKS-001, CM-MKS-002, CM-MKS-003, CM-POS-002, CM-POS-003, CM-POS-004). One evidence row added to batch 1's CM-SFR-014 (BC-S-0219, the Channels API manages a channel's sites); batch 1's reading of that cell is unchanged. Qualities: 4. Slot fillers: 9 (Amazon, Walmart, eBay in CM-CHN-003; Square, Vend, Clover, Heartland Retail in CM-POS-001; Stripe in CM-MKS-006 and CM-MKS-007). `uncited --domain E --platform bigcommerce` prints 0.

**Rulings:** none. No match or unclear candidate holds a BigCommerce concern (`concerns --platform bigcommerce --domain E` lists none); `rulings.tsv` still holds only its header.

### How I cut, and the grains

- **CM-CHN-007, Several storefronts in one store (new).** Multi-Storefront has a plan line of its own with a price and a maximum per plan (BC-S-0228) and a definition (BC-S-0227), so it is a capability by the dry run's convention. It is not Markets (CM-MKS-001): the anchor defines a market by the buyers' place, and no statement of BC-C-039 ties a storefront to a place. It is not domain A's CM-ACC-003, several stores under one owner: MSF is several storefronts "within one Store". Area CHN, parent CM-CHN-001, a reading: BigCommerce counts headless storefronts as channels (BC-S-0220) and names multi-storefront beside multi-channel (BC-S-0229). The coordinator may prefer area SFR, under CM-SFR-001, since the thing multiplied is the storefront. `E-backfill-bigcommerce` writes its cells for the other four platforms.
- **Multi-Storefront and batch 1's cells.** I added no MSF statement to CM-SFR-001 or CM-SFR-014: CM-CHN-007 holds them all, and none of BC-C-039's statements speaks of a theme, a site or a route. The MSF-enabled control panel (BC-S-0401) is cited in CM-MKS-006, where its subject, transactional currencies, is.
- **BC-C-038, Channels, in CM-CHN-001.** The concern is BigCommerce's channel object as a whole: the channel's sites (CM-SFR-014), its product listings (CM-CHN-004) and the plan line Online storefront (BC-S-0221, batch 1's CM-SFR-001). BC-S-0221 stays in CM-SFR-001, as batch 1 left it; with BC-S-0219 in CM-SFR-014 and CM-CHN-004, the fit is strained.
- **BC-C-074, Currencies, in CM-MKS-006,** the parent of conversion (CM-MKS-007); currency by the shopper's country (BC-S-0402) is also cited in CM-MKS-004. The default currency (BC-S-0404) goes to CM-MKS-005, which is not under CM-MKS-001: strained.
- **BC-C-068, Marketplaces and social channels, in CM-CHN-003.** Its words are about marketplaces (BC-S-0368, BC-S-0369). Its product lines Social channels and Google Shopping are names only: cited as `shows` in CM-CHN-001 and CM-CHN-004. Strained for CM-CHN-004.
- **BC-C-075, Geography, in CM-MKS-009.** BigCommerce's list holds countries, states and provinces; cities and districts are Salla's. The capability's name could add "states and provinces" (a proposal).

### Joins on role

- **BC-C-067, Feedonomics, in CM-CHN-004.** Feedonomics Surface "connects your store to ad channels and keeps product listings accurate as your catalog changes" (BC-S-0365): the role of Shopify's product feeds (SH-S-6093) and Salla's catalog feeds (SA-S-3201), the store's products kept listed on another channel.

### Homonyms

None kept apart. To watch:
- **Marketplace.** BigCommerce's App Marketplace (or Commerce Marketplace, BC-S-0172, BC-S-0173, BC-S-0325, domain F) sells apps to merchants; its Marketplaces product line (BC-S-0368) is Amazon, Walmart and eBay as sales channels. Only the second is cited here (CM-CHN-003); CM-CHN-002's `none-held` names the first.
- **Mobile app.** The BigCommerce mobile app (BC-S-0417, BC-S-0418, domain G) is the merchant's app for running the store, not a store's branded app for buyers (CM-CHN-006).
- **Conversion.** BigCommerce's "conversion rate" (BC-S-0405, BC-S-0406) is a currency conversion; the reason statement's "encourages conversions" (BC-S-0410) is sales conversion.

### Strained fits

- **BC-C-038 in CM-CHN-001:** BC-S-0221 in CM-SFR-001 (batch 1), BC-S-0219 also in CM-SFR-014 and CM-CHN-004, two other trees.
- **BC-C-068 in CM-CHN-003:** BC-I-0522 (Google Shopping) in CM-CHN-004, another tree.
- **BC-C-069 in CM-POS-001:** CM-POS-001 is in-person selling from the platform's own POS app; BigCommerce's statements show only POS integrations to Square, Vend, Clover and Heartland Retail (BC-S-0372), and no POS app of its own. The cell is `extension-point` only. A proposal: rename CM-POS-001 "Point of sale: in-person selling, from the platform's own POS app or connected POS systems", or split connected POS systems into a child.
- **BC-C-074 in CM-MKS-006:** BC-S-0404 in CM-MKS-005, another tree.

### For the coordinator: CM-SFR-014's parent

BigCommerce's Channels API manages "sales channels, their sites, and their product listings" (BC-S-0219), and a site is "associated with the specified channel" (BC-S-0233). Sites belong to every BigCommerce channel by that statement, not only to headless storefronts, though BC-S-0231 names headless storefront channels. CM-SFR-014's parent CM-SFR-011 follows BC-S-0231; CM-CHN-001 would follow BC-S-0219. I leave batch 1's row as it is; BC-S-0219's citation in CM-SFR-014 is the flag on it below.

### Concerns read under `also`, and other domains' statements

- None of the ten concerns naming E under `also` is cited by this batch. Inventory entries cited: BC-I-0259, BC-I-0260, BC-I-0494, BC-I-0519, BC-I-0521 (CM-CHN-001), BC-I-0522 (CM-CHN-004), BC-I-0491 (CM-POS-001), all among the entries Q1 placed in this batch's concerns, cited where no statement covers them.
- Read and not cited, named in the cells' readings: BC-S-0385 (geolocation for a guest shopper's tax zone, BC-C-072, domain C), BC-S-0387 (the Tax Settings API's cross-border prices, domain C), BC-S-0413 (Staging environments, domain F, F's CM-DVT-006), BC-S-0347 (Agentic checkout, domain F), BC-S-0417 and BC-S-0418 (the BigCommerce mobile app, domain G), BC-S-0234 (batch 1's redirects for several storefronts).

### Gaps that change what a cell claims

- **CM-CHN-004 and CM-CHN-007's makers.** Feedonomics: BC-S-0366 is a row of BigCommerce's list of contracting entities naming Feedonomics Holdings, LLC for the Feedonomics Platform (BC-I-0547 is the same row; BC-I-0458 is its own privacy policy). No statement held says in words that Feedonomics Holdings is of BigCommerce's group. The `own-service` placement rests on the list being BigCommerce's own, the same reading batch 1 made of Makeswift, Inc.; if the reviewer reads it otherwise, the row becomes `shows` and the cell stays `core` on BC-S-0219, BC-S-0224 and BC-S-0365.
- **CM-CHN-003:** who builds the marketplace connections, BigCommerce, Feedonomics or an app, is not held (searched: Amazon;eBay;Walmart;marketplace;Marketplaces). Q1's responsible gap on BC-C-068 is stated only in general terms.
- **CM-CHN-007:** the "additional requirements" for a Multi-Storefront enabled store (BC-S-0227) are not held. Responsible: stated only in general terms.
- **CM-MKS-004:** how the shopper's country is found for a transactional currency (BC-S-0402) is not held.
- **CM-MKS-005:** where the default currency is set, and whether it changes, are not held.
- **CM-MKS-007:** where the BigCommerce conversion rate comes from is not held.
- **CM-MKS-009:** who sets the list of countries, and how it meets the rest: searched, not found (BC-C-075/decides, BC-C-075/boundary).
- **CM-MKS-008:** why translations are placed as they are: searched, not found (BC-C-048/reason).
- **CM-POS-001:** responsible stated only in general terms, reason searched, not found (BC-C-069).

### What the checker flagged, and my answers

The whole part's check, `python3 -I method/check_class_part.py studies/class-model/parts/E-bigcommerce`, ends "0 problems, 20 flags for the reviewer". Batch 1's flags (Makeswift's own-service, BC-S-0472, CM-CNT-001, CM-CNT-005, CM-CNT-006, BC-S-0252, BC-S-0263) are answered in batch 1's section. This batch's:
1. **own-service on BC-S-0366 (Feedonomics).** Answered under Gaps: a reading resting on BigCommerce's contracting-entity list, as for Makeswift.
2. **CM-CHN-002 none-held, 33 matches.** They hold "marketplace" or "Shop": the App Marketplace for merchants (BC-C-029, BC-C-059, domain F), other companies' marketplaces (BC-S-0368, BC-S-0369, BC-S-0370, cited in CM-CHN-003), the channel's definition (BC-S-0220) and "shop" in other senses. None is a shopping app or marketplace BigCommerce runs for buyers.
3. **CM-CHN-005 none-held, 3 matches.** App Marketplace categories Product Sourcing and B2B/Wholesale (names only) and the subprocessor Microsourcing: none is selling between BigCommerce's stores.
4. **CM-CHN-006 none-held, 4 matches.** The BigCommerce mobile app and its terms, the merchant's app (domain G).
5. **CM-MKS-001 none-held, 14 matches.** Named in the cell's reading: marketing, regions of widgets and payments, email templates, global settings, metafields, shipping zones, tax regions, data-transfer regions. None is a version of the store for a place's buyers.
6. **CM-MKS-002 none-held, 6 matches.** StagingPro and Staging environments (domain F, CM-DVT-006) and a tax rate schedule (BC-S-0383): no scheduled change to the live store.
7. **CM-MKS-003 none-held, 2 matches.** BC-S-0347 is the merchant remaining merchant of record in agentic checkout; BC-S-0387 is the Tax Settings API's cross-border prices. Neither is a third party as merchant of record.
8. **CM-POS-002 none-held, 2 matches.** A persistent cart across devices and the mobile app's compatible device.
9. **CM-POS-003 none-held, 5 matches.** Offline payment methods not exposed by the Payments API, and things being registered (webhooks, carriers, tax providers).
10. **CM-POS-004 none-held, 14 matches.** In-store pickup, checkout extensions, control-panel app extensions, contracting entities naming "Extensions", and BigCommerce's POS integrations (cited in CM-POS-001): none an extension point inside a POS app.
11. **BC-S-0219 in CM-CHN-001, CM-CHN-004 and CM-SFR-014, more than one tree.** The statement names three things: sales channels (CM-CHN-001), their sites (CM-SFR-014) and their product listings (CM-CHN-004). BC-C-038's landing is strained for it; see "CM-SFR-014's parent" and the next point.
12. **BC-S-0404 in CM-MKS-005 and CM-MKS-006, more than one tree.** One sentence holds the multi-currency gateway requirement (CM-MKS-006) and, in its parenthesis, the store's default currency (CM-MKS-005). BC-C-074's landing is strained for it. The coordinator may weigh putting CM-MKS-005 under CM-MKS-006 or CM-MKS-001; the anchor left it a root.
- CM-CHN-004 has no parent, though CM-CHN-002, -003, -005 and -006 sit under CM-CHN-001: the coordinator may weigh giving CM-CHN-004 the parent CM-CHN-001, which would put BC-S-0219's CM-CHN-004 citation in CM-CHN-001's tree (point 11) and clear BC-C-068's strain.

### Problems on batch 1's rows

The whole part's check prints no problem on any row. Two observations for the coordinator, neither a checker problem:
- CM-SFR-014's parent (above).
- Batch 1 cited BC-C-038's plan line Online storefront (BC-S-0221) in CM-SFR-001. That citation still holds, and BC-C-038's landing names it as one reason it is strained.

### Problems with the brief or the evidence

- The batch message's "rule on the unclear candidates that hold your concerns": none hold a BigCommerce concern, as the brief says for Zid and BigCommerce. No rulings.
- The message says 19 capabilities; with the new CM-CHN-007 this batch writes 20 cells.
