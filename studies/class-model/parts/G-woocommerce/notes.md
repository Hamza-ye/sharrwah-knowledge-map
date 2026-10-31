# G-woocommerce: notes

**What this part is.** Domain G's mapping part for WooCommerce, onto G-anchor's model (7 capabilities: CM-MIG-001 to 005, CM-OPS-001 and 002). `scope.tsv` gives WooCommerce nine concerns of domain G: WC-C-034 (hosting), WC-C-036 (remote logging), WC-C-037 (store logs), WC-C-067 (product import and export), WC-C-083 (status and tools), WC-C-088 (feature settings), WC-C-090 (mobile app), WC-C-094 (Blueprint) and WC-C-109 (Store management extensions). Five concerns of other domains name G under `also`: WC-C-032, WC-C-035 and WC-C-043 (A), WC-C-033 (C) and WC-C-081 (A).

**What it holds.** 6 new capabilities (MIG 1, OPS 3, EVO 1, SRF 1), 9 landings, 13 cells (one per capability of the model, WooCommerce's), 44 evidence rows, 9 rulings, 1 quality, no slot fillers. Every statement of the nine concerns is cited, except WC-C-109's categories that aren't G's (see "Strained fits"). Each row below is a reading unless it quotes a statement.

## How I cut, and why

- **MIG.** WC-C-067 (Product Import, Product Export) lands in CM-MIG-001 by M-083, which holds it with Salla's SA-C-027. Blueprint (WC-C-094) gets a capability of its own, CM-MIG-006. It has a place of its own, the section Settings > Advanced > Blueprint (beta) (WC-S-0028), and an export route (WC-S-5451). Its object is the store's configuration: "Blueprint imports can change network-wide settings" (WC-S-5450). CM-MIG-001's objects are products, customers and orders. No statement puts Blueprint under import and export, so it has no parent. Nothing of WooCommerce's shows advanced import, export templates, an export log or a move into WooCommerce from another platform. Those four cells are `none-held`.
- **OPS.** Three new capabilities:
  - **CM-OPS-003, hosting of the store (WC-C-034).** Its place of its own is Shopify's plan line Unlimited web hosting (SH-C-036/decides/SH-S-7032), which SH-C-036 (E, naming G under `also`) lets G cite (convention 2). WooCommerce's own statements are a documentation page and a privacy clause. I kept it apart from CM-OPS-001 (reliability and continuity): no statement of WC-C-034 speaks of staying available or of failures.
  - **CM-OPS-004, store status (WC-C-083).** It has its own admin page, WooCommerce > Status, with System status and Tools, and its own REST APIs.
  - **CM-OPS-005, store logs (WC-C-037).** Its parent is CM-OPS-004, by WooCommerce's own grouping: "WooCommerce > Status > Logs" (WC-S-0920) and the Logs tab under Status (WC-S-0038). Neither anchor platform groups these, so WooCommerce's grouping is the only one.
  - **Remote Logging (WC-C-036)** is one feature flag (WC-S-5371), listed among the Features (WC-I-0335), with an endpoint (WC-S-0611). Convention 2 says a single feature flag isn't enough for a capability, so it lands in CM-OPS-005, strained.
- **EVO.** CM-EVO-001, feature settings (WC-C-088): its own section, Features, under Settings > Advanced (WC-S-5432), and WooCommerce's definition, "the WooCommerce features that can be enabled and disabled by admin users" (WC-S-5433). The anchor found no EVO capability: Shopify's betas and Salla's released flags scope the features they gate. Those flags are leads for the back-fill to read against this definition. Each Shopify or Salla flag gates one feature, and none of them is a section where the merchant turns features on or off. Unless a statement of theirs shows such a section, the back-fill's cells are likely `none-held` (an assumption).
- **SRF.** CM-SRF-001, the mobile app (WC-C-090): the onboarding task for it (WC-S-0422), its push notifications setting (WC-S-0939) and its wc-admin mobile-app routes (WC-S-0203, WC-S-0204). Push notifications are one feature flag (WC-S-5437), so they stay in this capability.
- **WC-C-109 (Store management extensions).** `scope.tsv`'s reason puts it in SRF, but no SRF capability fits a group of Marketplace categories, and the channel doesn't set the area. Only one of its categories is G's: Import and export (WC-S-0747). So it lands in CM-MIG-001 by terms, strained, as B's part landed the Merchandising group WC-C-104.
- **The 33 features listed under WC-C-088** (WC-I-0325 to WC-I-0356) are each another concern's subject (analytics, POS, cost of goods, HPOS and others) and aren't cited. Blueprint (beta) (WC-I-0339) and Push Notifications (WC-I-0348) are among them, and their concerns' statements are cited instead.

## Grains chosen

- **CM-MIG-001 stays one capability**, as the anchor left it. WooCommerce's cell is products only (M-083's granularity).
- **CM-OPS-005 is under CM-OPS-004** by WooCommerce's own grouping (above). CM-OPS-003 and CM-MIG-006 have no parent: no statement groups them under another capability.
- **Push notifications and Remote Logging** are single feature flags (convention 2), held in CM-SRF-001 and CM-OPS-005.

## Joins

- **By match:** WC-C-067 in CM-MIG-001 (M-083).
- **By terms:** WC-C-109 in CM-MIG-001, by import and export: WooCommerce's category Import and export (WC-C-109/where/WC-S-0747), Salla's Import & export (SA-C-027/where/SA-S-1805) and Shopify's Store data importer apps (SH-I-1878).
- **No join on role.**
- **The rest are `single`:** each makes a new capability that only WooCommerce shows so far, and WC-C-036 joins WC-C-037 in CM-OPS-005, a WooCommerce capability.
- **One ruling is `joined:` on a capability this part adds.** U-014 joins WC-C-034 with SH-C-036 in CM-OPS-003, by the term hosting (WC-S-0642, WC-S-0503; SH-S-7032). It holds once the back-fill writes Shopify's CM-OPS-003 cell with SH-C-036/decides/SH-S-7032. The checker flags it, as it should.

## Homonyms kept apart

- **Status:** WooCommerce's Status page (CM-OPS-004), the store's own system status report and tools, against Salla's status page (CM-OPS-002), which reports the platform's services ("Merchant APIs - Operational"). WooCommerce Tax's "If the status page shows Not connected to WordPress.com" (WC-C-055/boundary/WC-S-0638) reads as WooCommerce's own status page, a reading. It isn't cited, since WC-C-055 doesn't name G under `also`.
- **Log:** WooCommerce's Logs, "the entries created by the logger" (WC-S-0920), against the audit logs of Shopify (MerchantAuditLog, SH-C-012/where/SH-S-1581) and Salla (Activity history, SA-C-010/where/SA-S-1889), as Q1's U-044 says. Also against Salla's Export log (CM-MIG-004).
- **Export and import that aren't a store's data import and export**, none of them cited:
  - privacy exporters of a customer's personal data (WC-C-045/boundary/WC-S-0357 to WC-S-0360, and WC-C-066, WC-C-098, the same exporters);
  - analytics imports and report exports (WC-C-038/boundary/WC-S-0226, WC-S-0227, WC-S-0246, domain D);
  - customs import and export (WC-C-029/responsible/WC-S-0470, WC-C-058/responsible/WC-S-0485).
- **The none-held searches' other hits:**
  - "moving" finds "Removing checkout fields" (WC-C-087/boundary/WC-S-0796);
  - "switch to" finds an exchange rate (WC-C-053/decides/WC-S-0544);
  - "fallback" finds a fallback list of payment methods (WC-C-004/where/WC-S-0616);
  - "failed" finds failed orders (WC-C-076, WC-C-106);
  - "availability" finds Bookings' availability rules (WC-C-101/decides/WC-S-5352);
  - "operational" finds a table name and fees terms (WC-C-033/where/WC-S-5368, WC-S-0650).

## Strained fits

- **WC-C-036 (Remote Logging) in CM-OPS-005.** Its logs leave the store for WooCommerce's endpoint on public-api.wordpress.com (WC-S-0611), where CM-OPS-005's logs are viewed in the store's admin. It is allowed only when usage tracking is enabled (WC-S-5372), which is WC-C-035's, domain A. The reviewer may split it, or move it to sit with usage tracking in A. Its statements are cited only in CM-OPS-005.
- **WC-C-109 (Store management) in CM-MIG-001.** Only its Import and export category is cited in G. The others are other domains' subjects, all named under WC-C-109's `also` (A;C;D):
  - Business insights (WC-S-0746), analytics, D;
  - Order management (WC-S-0749), C;
  - Policy and security (WC-S-0750), A;
  - Accounting (WC-S-0754), with the Xero statements WC-S-5489 and WC-S-5491, C.

  The group itself (WC-S-0704) and Admin and notifications (WC-S-0752), which names nothing a statement defines, aren't cited.

## Concerns read under also

- **WC-C-032 (A):** I cited WC-S-0588 ("you're free to export all your content and take your site to any platform you choose") in CM-MIG-001 as `shows`. I left its HPOS and wp_options statements to A.
- **WC-C-035 (A), usage tracking:** I cited none of it. CM-OPS-005's reading names it as Remote Logging's condition, through WC-S-5372, which is WC-C-036's own statement.
- **WC-C-033 (C), WC-C-043 (A) and WC-C-081 (A):** I cited none of them. HPOS tables, transfers outside the EEA and UK, and the home and onboarding are those domains' subjects. The onboarding tasks I cite, Import your products (WC-S-0426) and Get the free WooCommerce mobile app (WC-S-0422), are placed in WC-C-067 and WC-C-090.
- **Outside also:** none cited.

## Placements

- **`core`:**
  - WooCommerce's own admin menus, sections, tabs and onboarding tasks;
  - its checks on user capabilities;
  - its own filters, classes and REST routes, for its own features (convention 1);
  - its released flags (push_notifications, not experimental and enabled by default, WC-S-5437; remote_logging, enabled by default, WC-S-5371).
- **`extension-point`:** the Marketplace category Import and export (WC-S-0747).
- **`outside`:** "your hosting provider", for a site not hosted by Automattic (WC-S-0503).
- **`own-service`, a reading, which the checker flags:** the same clause, WC-S-0503, names Automattic as the host of the sites it hosts ("if your site is not hosted by Automattic"). It names the company as providing hosting for some sites, but says nothing of what that hosting is. If the reviewer reads the clause as naming no service, the row goes and the cell keeps `outside` and `shows`.
- **`shows`:**
  - the merchant verifying their own hosting environment (WC-S-0642);
  - the readme on exporting all one's content (WC-S-0588);
  - Remote Logging's stated reason, "to help improve WooCommerce" (WC-C-036/reason/WC-S-0936).
- **Blueprint:** the section's own label says beta. The concern map holds no statement of Blueprint's feature flag, its released state or its default; only its name in the Features list (WC-I-0339). So `core` rests on the section, the route and the import checks, not on a flag (C6).

## Qualities and slot fillers

- **Quality:** store logs are kept for 30 days by default ("'retention_period_days' => 30,", WC-C-037/decides/WC-S-5373).
- **No slot filler.** WC-S-0503 names "your hosting provider" by its role, not by a name, so I recorded none.

## Gaps

- No statement names the maker of the WooCommerce mobile app. Its name carries the brand, and that doesn't name a maker, so the cell rests on the admin's and the API's own statements, as `core`.
- No statement names the company behind the remote logging endpoint on public-api.wordpress.com.
- No statement says what hosting Automattic provides, or on what terms (CM-OPS-003).
- No statement says what the system status items are (CM-OPS-004).
- Q1's gaps hold for every concern here. The responsible placement is stated only in general terms throughout. No reason was found for WC-C-034, WC-C-037, WC-C-067, WC-C-083, WC-C-088 or WC-C-090. No boundary was found for WC-C-034.

## Leads for the back-fill (Shopify and Salla on the new capabilities)

- **CM-OPS-003:** Shopify's Unlimited web hosting (SH-C-036/decides/SH-S-7032; also SH-I-1179, SH-I-1266). Shopify's subprocessor row "Cloud hosting and data processing" (SH-C-181/where/SH-S-0196) would bear on U-042's ruling if cited (see "Rulings"). Oxygen, "Shopify's global edge hosting platform" (SH-C-139/where/SH-S-0710), hosts Hydrogen apps, a storefront's, and is likely E's (an assumption).
- **CM-SRF-001:** Salla's تطبيق إدارة المتجر على أجهزة iOS و Android (SA-C-001/decides/SA-S-2082), and the anchor's lead SA-S-2083. SA-C-001 doesn't name G under `also`, so citing them is flagged as outside also.
- **CM-EVO-001:** Shopify's betas and Salla's released flags, read against the definition in WC-S-5433.

## Rulings

- **U-014:**
  - joined:CM-OPS-003 for SH-C-036 (pending the back-fill);
  - apart for SA-C-007 (E, not naming G).
- **U-042:**
  - apart for SH-C-181: its data hosting locations are A's, and G cites only its recovery sites. If the back-fill cites SH-S-0196 in CM-OPS-003, the merge re-tests this and it may become joined.
  - apart for SA-C-233, which has no statements.
- **U-044:** apart for SH-C-012 (A, not naming G) and for SA-C-010, the homonym log.
- **U-064:** apart for SH-C-191, SH-C-196 and SA-C-210. Accounting and security are C's and A's, and G cites neither side.
- **U-068:** apart for SA-C-001 (A, not naming G). The two read as the same thing, a store management app, a reading. If the coordinator names G under SA-C-001's `also`, the back-fill cites SA-S-2082 in CM-SRF-001 and the ruling becomes joined:CM-SRF-001.

## What the checker flagged, and my answers

- **own-service on WC-S-0503:** see "Placements". The clause names Automattic as a host ("not hosted by Automattic"). It is a reading, for the reviewer.
- **none-held on CM-MIG-004, CM-MIG-005, CM-OPS-001 and CM-OPS-002, with matching statements:** each hit is read and placed in "Homonyms kept apart". One of them is cited elsewhere in G: the readme's export statement (WC-S-0588, in CM-MIG-001). WooCommerce Tax's status page (WC-S-0638) reads as CM-OPS-004's homonym and is left uncited. The inventory entries in the flags (WC-I-0357 and after, WC-I-0591, WC-I-0297, WC-I-0298, WC-I-0323) are the same privacy exporters, checkout fields and failed orders. None of them shows the capability.
- **rulings line 2, joined:CM-OPS-003:** a capability this part adds; it holds once the back-fill writes Shopify's cell (above).

## Problems with the brief or the evidence

- **`scope.tsv` places WC-C-109 in SRF.** Its own categories go to A, C, D and G's MIG, and none is an admin surface. The coordinator may want its reason corrected, or the concern split.
- **U-068's pair is the same thing by both platforms' words** (the store management app), but `scope.tsv` gives SA-C-001 domain A without G under `also`, so the brief's rule makes the ruling apart.


## The coordinator's corrections (30 October)

- **U-068:** `scope.tsv` now names G under SA-C-001's `also`, as this part's notes asked, so the ruling is `joined:CM-SRF-001`, waiting for the back-fill to cite SA-S-2082 in CM-SRF-001's Salla cell.
