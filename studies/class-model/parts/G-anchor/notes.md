# G-anchor: notes

**What this part is.** Domain G's anchor, Cross-cutting, for Shopify and Salla. `scope.tsv` gives Shopify no concern of domain G and Salla four: SA-C-027 (import and export), SA-C-234 (platform security and service status), SA-C-235 (what happens when a partner is unavailable) and SA-C-302 (the store migration service). Nine concerns of other domains name G under `also`: Shopify's SH-C-036 (hosting and SSL, E), SH-C-171 (API conventions, F), SH-C-181 (where data is stored, A), SH-C-191 (accounting and ERP, C); Salla's SA-C-010 (activity and audit logs, A), SA-C-201 (rate limits, F), SA-C-202 (versioning and change log, F), SA-C-210 (accounting and ERP, C), SA-C-233 (where data is stored, A; no statements).

**What it holds.** 7 capabilities (MIG 5, OPS 2, and none in SRF, LNG or EVO), 4 landings, 14 cells, 60 evidence rows, 3 rulings, 1 quality, no slot fillers. Every statement of SA-C-027, SA-C-235 and SA-C-302 is cited; SA-C-234's five security statements are not (see "Strained fits"). Each row below is a reading unless it quotes a statement.

## How I cut, and why

- **MIG, import and export.** Salla holds its imports and exports in one concern (SA-C-027), under one staff permission (`import_export_management`, SA-S-2257), one flag (`impex`, SA-S-3224) and one Merchant API folder (Exports, SA-S-1057). Shopify has no such concern (M-083's note: "its export permissions sit in its products, orders and customers concerns"); its product import routes are in SH-C-020 and its Export permissions in SH-C-010 and each object's concern. CM-MIG-001 holds both. Salla gives three parts a place of their own (convention 2): Advanced import (link, route, dashboard app and permissions at `/importer`), Export templates (links at `/products/exports` and `/orders/exports`, and flags) and Export log (link at `/logs/export`, plan line, permission, flag). Each is a capability.
- **MIG, moving a store from another platform.** Salla's migration service has its own terms on partners.salla.com, with its own eligibility, benefits and company (SA-C-302), so it is a capability of its own (CM-MIG-005), apart from import and export.
- **OPS.** Two capabilities: the platform's reliability and continuity (CM-OPS-001: Salla's plan line استقرار المنصة وجاهزيتها للذروة, SA-I-1197; Shopify's pods and recovery sites, SH-C-181) and the service status page (CM-OPS-002: Salla's status page, SA-S-0047). What happens when a partner fails (SA-C-235) gets no capability of its own: no platform gives it a place of its own, neither an admin section or route, an API group, a plan line nor an app category (convention 2). So it lands in CM-OPS-001, strained.
- **SRF, LNG and EVO: no capability.** Neither platform has a concern of domain G in these areas, and their statements give none of them a place of its own:
  - **SRF:** the concern map holds no Shopify merchant mobile app. Searched in Shopify's statements: Shopify mobile app; Shopify app; mobile admin; merchant app; iOS; Android. Salla's iOS app is named only inside a billing plan line, إدارة الاشتراك في تطبيق سلة على iOS برصيد آيتونز (SA-C-004/decides/SA-S-2083, domain A). The admin router and Salla's dashboard links and apps are where every concern's `where` statements come from, not capabilities of their own. WooCommerce's WC-C-090 and WC-C-109 and BigCommerce's BC-C-077 are G's mobile app and store management concerns. Their parts add what they show, and their back-fills search Shopify and Salla; SA-S-2083 is a lead for those back-fills.
  - **LNG:** no statement of either platform names the language of its admin. Searched: arabic; right-to-left; RTL; admin language (Shopify); لغة لوحة التحكم; dashboard language; English; الإنجليزية (Salla). Salla's statements carry Arabic and English names, and Shopify's statements hold no Arabic. The vocabulary is in each cell's `terms`.
  - **EVO:** the statements that G may cite are all the API's. Shopify's Versioning and Feature previews (SH-C-171/where/SH-S-0793; SH-I-0038) are labels in its developer docs' navigation, in the group the citations' locator names "Core concepts" (context, not cited). Salla's Change Log (SA-C-202/where/SA-S-1167, SA-C-202/boundary/SA-S-1014) sits in its API docs' list under the same parent as Rate Limiting, Versioning and Security Considerations (SA-S-1001, SA-S-1002, SA-S-1006). `scope.tsv`'s rule gives the API's versioning to domain F, so I left them to F. Shopify's betas (the `betas` key of admin routes' eligibility) and Salla's `released` flags scope the features they gate (C6; the rulings' convention 11), so they aren't capabilities here. The seed's isBeta and isNewFeature flags aren't in the concern map: searched isBeta; isNewFeature; beta; تجريبي; تجريبية; ميزة جديدة. "beta" finds only App Functions being in beta (SA-C-196/decides/SA-S-0188, F), and the Arabic terms find test stores (SA-C-209, F). WooCommerce's WC-C-088 (opt-in features) is G's, and its part adds what it shows.
- **Limits.** The concern map holds no published store limits of either anchor platform that bear on G. Shopify's unplaced `maxProductOptions` and `maxProductVariants` (SH-I-2519, SH-I-2520) are about products, domain B. API rate limits (SH-C-171, SA-C-201) are F's by `scope.tsv`'s rule.

## Grains chosen

- **CM-MIG-001 isn't split by object.** Both platforms put each object's import or export in that object's own section: Salla's links are in the products, customers and orders lists (lists 2, 5 and 1), and Shopify's permissions are "Products > Export", "Customers > Export" and so on. Those sections are other domains' capabilities (B, C, D). So the capability is the mechanism, and the cells' readings name the objects: products, customers and orders on Salla, with order statuses imported; products imported and products, customers, orders, draft orders and gift cards exported on Shopify.
- **Parents (S2).** The platforms' own sections are other domains', so a parent within G can rest only on what the statements' names and routes show.
  - CM-MIG-002 (Advanced import) is under CM-MIG-001 by its own name. Its permissions are named إدارة الاستيراد المتقدم (advanced import management), and its link sits in the products list beside Import & export.
  - CM-MIG-003 (Export templates) is under CM-MIG-001 by its routes, the products' and orders' exports routes.
  - CM-MIG-004 (Export log) has no parent. Its route puts it under Salla's logs (`/logs/export`, list 11, beside Activity history at `/logs/audit`), the subject of SA-C-010, domain A. A parent in G would contradict that grouping.
  - CM-MIG-005 has no parent: no statement puts migration under import and export.
  - CM-OPS-002 has no parent either: no statement groups the status page with the stability plan line. Q1's SA-C-234 holds both, but that is Q1's grouping, not Salla's.

## Joins

- **No concern joins another.** Shopify has no concern of domain G, so all four landings are `single`. SA-C-027 is in Q1's M-083 with WooCommerce's WC-C-067; a `match:` landing here would sit with no other landed concern of the match, so the join is `single`, and WooCommerce's part lands WC-C-067 by M-083.
- **Capabilities that hold both platforms' statements:**
  - **CM-MIG-001, by terms.** Both use import and export for the same objects. Salla: Import & export, Import customers, تصدير الطلبات (SA-C-027/where/SA-S-1805, SA-S-1847, SA-C-027/decides/SA-S-1997). Shopify: products:imports, Products > Export, Customers > Export, Orders > Export (SH-C-020/decides/SH-S-5017, SH-I-0906, SH-I-0923, SH-I-0881).
  - **CM-MIG-005, on role, a reading.** Salla's service is "to ease moving from other e-commerce platforms" (SA-C-302/reason/SA-S-5123). Shopify's help-center section is "Migrating and integrating QuickBooks Desktop POS with Shopify POS" (SH-I-2302). Both move a merchant's data from another commerce system into the platform, but Shopify's is from a point-of-sale system and names no service.
  - **CM-OPS-001, on role, a reading.** Salla's plan line names platform stability and readiness for peak (SA-I-1197). Shopify's statements say each pod has an active data center and a recovery site, and each shard is isolated so a failure can't become a platform outage (SH-C-181/where/SH-S-0673, SH-C-181/reason/SH-S-0674). Both state the platform staying available under load and through failures, and neither defines the term.

## Homonyms kept apart

- **سجل / log:** Salla's Export log (سجل التصدير, CM-MIG-004) against its Activity history (سجل العمليات, SA-C-010/where/SA-S-1889, domain A). Q1's U-044 lists logs as audit logs against system logs (Shopify's SH-C-012, WooCommerce's WC-C-037); the export log is neither.
- **Import and export are not data import and export in these statements**, which stay out of CM-MIG-001:
  - customs: duties and import taxes (SH-C-105/responsible/SH-S-0618; SH-I-1327, SH-I-1341, SH-I-2156, SH-I-2318) and export control (SH-C-174/responsible/SH-S-0296);
  - a customer's personal data export, which is privacy (Salla's `customer-data-export`, SA-C-066/decides/SA-S-3175);
  - importing orders from marketplaces, which is a channel (SH-C-137/decides/SH-S-7049);
  - audiences exported to an ad account (SH-C-132/boundary/SH-S-0735);
  - exporting POS transactions for Germany's TSE (SH-C-142/reason/SH-S-7285);
  - exporting payout details (SH-I-2229) and the tax help section "Data Exporter" (SH-I-2323, SH-C-101).
- **Preview:** Shopify's Feature previews (SH-I-0038, developer docs) against Salla's `product-preview` and `theme-preview` flags (SA-C-020/decides/SA-S-3503, SA-C-090/decides/SA-S-3157), which preview a product or a theme. None is cited.
- **Switch:** "Switch to Shopify Payments" (SH-C-063/decides/SH-S-0369) came up in the migration search and is about payments, not moving a store.

## Strained fits

- **SA-C-027 in CM-MIG-001.** Its Export log link (SA-C-027/where/SA-S-1890) is cited in CM-MIG-004, another tree, which Salla's route puts under its logs. Its Advanced import and Export templates statements are cited in CM-MIG-002 and CM-MIG-003, inside its own tree.
- **SA-C-234 in CM-OPS-002.** Its plan line for platform stability (SA-I-1197) is cited in CM-OPS-001, another tree. Its other five statements aren't cited in G:
  - the API must use HTTPS (SA-C-234/decides/SA-S-0175), with TLS (SA-C-234/boundary/SA-S-0174) and OAuth 2.0 (SA-C-234/boundary/SA-S-0176), and the Security Considerations doc (SA-C-234/boundary/SA-S-1006): the API's conventions, domain F's by `scope.tsv`'s rule;
  - two-step verification made mandatory for dashboard sign-in (SA-C-234/reason/SA-S-5115): sign-in security, domain A's (U-006).

  Most of the concern is security. `scope.tsv` names A under `also`, but not F, so an F part citing them would be flagged. If the coordinator moves SA-C-234 to A, CM-OPS-002 can still cite its status page line, provided A names G.
- **SA-C-235 in CM-OPS-001.** Each of its statements is about one kind of partner whose subject is another domain's: carrier assignment by priority (SA-S-0162, shipping, C), a communication app's failure (SA-S-0194, apps, F) and the affiliate program's commissions (SA-S-0044). The carrier statement speaks of whether the first company delivers to the customer's area, so it is a fallback by coverage, not by outage. Q1's gaps (where, decides and reason: page not read) leave out where and how Salla handles an unavailable gateway or carrier.

## Concerns read under also

- **SH-C-181 (A):** I cited SH-S-0673 (recovery sites) and SH-S-0674 (failure isolation) in CM-OPS-001. I left its data-location statements to A: SH-S-0636 (storage rebalanced between Google Cloud regions), SH-S-0638 (Europe), SH-S-0672 (pods on isolated datastores, a `where` of data location as much as of reliability), the subprocessors and the transfer clauses. If A cites SH-S-0673 or SH-S-0674 as `core`, the merge flags them.
- **SA-C-010 (A):** I cited its export-log statements in CM-MIG-004 (SA-S-2122, SA-S-2423, SA-S-2640, SA-S-3234) and left its activity history to A (SA-S-1889, SA-S-2123, SA-S-2421, SA-S-2638, SA-S-2966, SA-S-5010, SA-S-3548). A shouldn't cite the export-log rows as `core` too.
- **SH-C-191 and SA-C-210 (C):** I cited only SH-I-2302 (migrating from QuickBooks Desktop POS, placed in SH-C-191 and SH-C-142) in CM-MIG-005. Their accounting apps, ERP apps, plan lines and flags are C's.
- **SH-C-171, SA-C-201 and SA-C-202 (F):** I cited none of them. Their versioning, change log, feature previews, rate limits and bulk operations are the API's conventions (see "How I cut"). The bulk operations statements (SH-S-0770, SH-S-1158; SH-I-0006, SH-I-0334, SH-I-0335, SH-I-0394) don't say that the operations import or export data, so they don't support CM-MIG-001.
- **SH-C-036 (E):** I cited none of it. Hosting and SSL are the storefront's (E). WooCommerce's hosting concern WC-C-034 is G's (OPS, also E) and U-014 holds it with SH-C-036 and SA-C-007; WooCommerce's part rules on it.
- **SA-C-233 (A):** it has no statements.
- **Outside also.** I cited Shopify statements of concerns that don't name G in CM-MIG-001 only: SH-C-020 (B) and the export permissions placed in SH-C-010 (A) with SH-C-020, SH-C-039, SH-C-054, SH-C-055 and SH-C-025 (B, C, D). The checker flags them; see the answers below. I didn't cite Salla's other exports, which belong to other domains' objects: `inventory::print_export` (SA-C-025/decides/SA-S-3094, which B's anchor left uncited), `coupon-export` (SA-C-070/decides/SA-S-3245), `special-offer-export` (SA-C-071/decides/SA-S-3311) and `export_special_opportunity` (SA-C-072/decides/SA-S-3411). They are leads, if the coordinator wants CM-MIG-001's objects counted in full. The status page's Store APIs line (SA-C-101/where/SA-S-0211, E) isn't cited either.

## Placements

- **`core`:**
  - Salla's own dashboard links, routes and apps; its staff permissions (S7); its plan lines; its released flags (C6); its Merchant API folder Exports and the exports scope (C1).
  - Shopify's admin routes for importing products, which are behind beta 78e33675. This follows B's anchor, which read routes behind a beta as `core` (CM-INV-002, CM-INV-003). The beta is named in the cell's reading, since the statements carry no scope field. Also Shopify's staff Export permissions (placed inventory entries, C2; S7).
  - The built-in behaviour Salla and Shopify state: carrier assignment, telling the store a communication failed, recovery sites, isolated shards.
- **`own-service`:** Salla's migration service. Its terms name شركة منصة سلة للاتصالات وتقنية المعلومات as owner of the platform that provides it (SA-S-5121, SA-S-5123), and it is a service under its own terms, apart from the dashboard.
- **`extension-point`:** Shopify's App Store category Store data importer apps (SH-I-1878).
- **`shows`:**
  - the partner permissions (S7) and Salla's flags that aren't released (C6);
  - the flag `update-products` and the plan line نقل البيانات بسلاسة, which don't say what they update or move;
  - the migration terms' place, eligibility and balance transfer;
  - Salla's liability clause (SA-S-0044);
  - Shopify's help-center section on QuickBooks POS (SH-I-2302), which names no one who does the migration.

## Qualities and slot fillers

- **Quality:** CM-MIG-005, Salla: the service's eligibility, sales of at least 20,000 SAR in the last 12 months (SA-C-302/decides/SA-S-5120).
- **Not qualities:** Shopify's "no guarantees ... availability or uptime of Shopify Tax" (SH-C-100/responsible/SH-S-0598) bears on Shopify Tax, domain C. Data hosting locations (SH-C-181) bear on A's capability.
- **No slot fillers.** No cited statement names a third party or a law as doing a capability of G or setting its terms. SA-S-0044 names payment gateways only in general. SA-S-5122 names "the previous platform" without naming one. The Google Cloud regions (SH-S-0636) are left to A.

## Gaps (statements a cell needs that the concern map doesn't hold)

- A Shopify status page, which the seed names as a lead, and any Shopify statement on its own uptime.
- Shopify's import of customers and orders. Shopify's own migration service, or a statement that its Store data importer apps move a store from another platform.
- What Salla's Advanced import imports, what an export template holds, what the export log records, what `update-products` updates and what نقل البيانات بسلاسة moves. The other platforms' `none-held` cells say these definitions aren't stated.
- Which platforms Salla's migration service covers, and which data it moves.
- Where and how Salla handles an unavailable payment gateway or carrier (Q1's gaps on SA-C-235).
- The partner agreements' clauses on an app or theme that fails or is withdrawn. Q1 places the titles of four agreements in SA-C-235: the app store's, the partners program's, the theme store's and the affiliate program's (SA-I-2615, SA-I-2616, SA-I-2617, SA-I-2619). Only the affiliate program's article 10 is held as a statement (SA-S-0044). The titles aren't cited, since they show nothing of the capability.
- Who answers for imports and exports (SA-C-027's responsible and reason: page not read), and who answers for account and data security (SA-C-234's responsible: page not read).
- **SA-I-1197's plan.** The inventory entry has no scope, so derived.tsv shows no plan. Its citation is a line of the Special plan's page (SA-S-2197, observed-sa@145f137); I read that as context and don't cite it.
- An API or webhook for Salla's export log (SA-C-010's boundary: page not read).
- A statement of what Shopify's bulk operations do.
- The seed's isBeta and isNewFeature flags and a Shopify merchant mobile app.

## What the checker flagged, and the answers

The final run reports 0 problems and 14 flags.

1. **Nine flags on CM-MIG-001's Shopify cell** (evidence lines 23 to 31): SH-C-020/where/SH-S-5011, SH-C-020/decides/SH-S-5012, SH-C-020/decides/SH-S-5017, SH-I-0906, SH-I-0923, SH-I-0881, SH-I-0898, SH-I-0916 and SH-I-1878 are statements of concerns that don't name G (SH-C-020, B; SH-C-010, A; SH-C-039 and SH-C-025, D; SH-C-054 and SH-C-055, C).
   - **Why they are cited:** Shopify has no import and export concern (M-083's note). Domain B's anchor left the product import routes to G (its notes, "import is domain G's (U-081)"; its U-081 basis) and listed the importer category among its gaps. No B part cites any of these keys: checked against every `B-*/evidence.tsv`. The export permissions are placed in the roles concern and each object's concern.
   - **What the coordinator could do:** name G under also for SH-C-020 and SH-C-010, as S6 did for SH-C-187.
2. **Two flags on `own-service`** (evidence lines 50 and 51).
   - **SA-S-5121** names the company: "منصة "سلة"، المملوكة لشركة منصة سلة للاتصالات وتقنية المعلومات (س.ت: 4031200589)".
   - **SA-S-5123**, in the same introduction, says the platform provides the service.
   - **The reading:** the service is separate, with its own terms, eligibility and benefits on partners.salla.com, and the company provides it. If the reviewer reads "the platform provides a service" as the platform itself doing it, both rows become `core`.
3. **CM-MIG-002's Shopify `none-held` matches SH-I-1878** (cells line 5). The searched term "importer" finds the Store data importer apps category, which is cited in CM-MIG-001. Nothing names an advanced or custom importer.
4. **CM-OPS-002's Shopify `none-held` matches five statements** (cells line 15). None is a status page: SH-S-0337 is a review criterion on operational patterns, SH-S-0598 the uptime Shopify doesn't guarantee for Shopify Tax, SH-S-0539 a tax engine moved with zero downtime, SH-S-0451 circuit breakers for local outages in payments, and SH-S-0674 isolated shards, cited in CM-OPS-001.
5. **CM-MIG-004 has no concern landed in its tree.** Two concerns hold it: SA-C-027, which lands in CM-MIG-001 as the coarser import-and-export concern, strained for this reason; and SA-C-010, which is domain A's. Salla's route puts the export log under its logs, so it has no parent in G (S2).

## Problems with the brief or the evidence

- **G's anchor is thin.** Shopify has no concern of domain G, and Salla four. SRF, LNG and EVO have no capability from the anchor. The seed's leads for them, Shopify's status page and published limits, and Salla's isBeta and isNewFeature flags have no statements in the concern map. The mapping parts (WooCommerce's nine G concerns, Zid's one and BigCommerce's two) will add most of G's capabilities, and their back-fills will write the anchor platforms' cells.
- **U-081 and the rule on other domains' concerns.** "Cite it only where the cell needs it" lets CM-MIG-001 cite SH-C-020's importer category, while "otherwise the ruling is apart" fixes U-081 as `apart`, because SH-C-020 doesn't name G. The two agree here only because I read the category as import, not migration. If the reviewer reads it as migration, the ruling would have to be `joined:CM-MIG-005`, which the brief allows only if SH-C-020 names G under also.
- **S2 in a cross-cutting domain.** The platforms put import, export, logs and migration inside other domains' sections. Following "the platforms' own grouping" strictly would leave G flat, so the parents here rest on names and routes, and each says so in the capabilities' notes.
- **SA-C-234 is mostly API and sign-in security,** which is F's and A's. Only its status page line and the stability plan line it holds are G's.
- **SA-C-235's statements don't show what the concern names.** Q1's own gaps say the pages that would show it weren't read.

## The coordinator's correction after A-anchor batch 6 (30 October)

- **SH-S-0672 is cited in CM-OPS-001.** This part left it to A and A-anchor left it to G, so no cell cited it. A pod as a set of shops on a fully isolated set of datastores is the isolation CM-OPS-001's Shopify cell already rests on (SH-S-0673, SH-S-0674).
