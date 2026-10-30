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
