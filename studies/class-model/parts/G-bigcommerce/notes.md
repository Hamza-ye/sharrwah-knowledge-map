# G-bigcommerce: notes

**What this part is.** Domain G's mapping part for BigCommerce, onto the model so far: G-anchor, G-woocommerce, G-backfill-woocommerce and G-zid (13 capabilities: CM-MIG-001 to 006, CM-OPS-001 to 005, CM-EVO-001, CM-SRF-001). `scope.tsv` gives BigCommerce two concerns of domain G, BC-C-060 (System logs and store logs) and BC-C-077 (BigCommerce mobile app). Five concerns of other domains name G under `also`, and I read them all: BC-C-052 (Native Hosting, E), BC-C-057 (API rate limits, F), BC-C-076 (Staging environments, F), BC-C-082 (Data transfer and storage location, A) and BC-C-083 (Subprocessors and hosting services, A).

**What it holds.** No new capability, 2 landings, 13 cells (one per capability, BigCommerce's), 19 evidence rows, 2 qualities, 1 slot filler, no ruling (BigCommerce has no unclear candidates). Each row below is a reading unless it quotes a statement. BigCommerce's statements are in English, so every search is in English only.

## How I cut, and why

- **BC-C-060 lands in CM-OPS-005 (Store logs), by terms and definition.** BigCommerce's Store logs is a control panel page, Settings > Advanced > Store logs (BC-C-060/where/BC-S-0332), with its own System Logs endpoint to "Retrieve and filter store logs ... access log entries for debugging, auditing, and monitoring store activity" (BC-C-060/where/BC-S-0331). WooCommerce's Logs is where "You can view the entries created by the logger" (WC-C-037/where/WC-S-0920). Both are the store's own log entries, viewed in the admin.
- **The parent.** CM-OPS-005's parent is CM-OPS-004 (system status), following WooCommerce's grouping (Status > Logs). BigCommerce puts its store logs under Settings > Advanced and holds no system status page, so its grouping differs. I keep the parent as it is: it is the only grouping stated for a system status, and BigCommerce's has no status page to put the logs under.
- **BC-C-077 lands in CM-SRF-001 (Mobile app for managing the store), by terms.** BigCommerce mobile app is a plan line (BC-C-077/decides/BC-S-0418). Commerce licenses it "solely in connection with your Account for so long as your Services subscription remains in effect" (BC-C-077/decides/BC-S-0419), so it is the merchant's app, not a shopper-facing one. What the app does isn't stated (Q1's gaps BC-C-077/boundary and BC-C-077/reason, searched, not found). The landing rests on the name and on the app being the merchant's. If the reviewer wants the fit marked strained because "managing the store" and push notifications aren't stated, nothing else in the model would take the concern.
- **No new capability.** Both concerns fit the model. Nothing in the `also` concerns has a place of its own that the model lacks in G:
  - rate limits (BC-C-057) and staging environments (BC-C-076) are domain F's;
  - data transfer (BC-C-082) and subprocessors (BC-C-083) are domain A's.

  Their G-bearing statements are cited in CM-OPS-001 and CM-OPS-003. So this part needs no back-fill.

## Cells

- **CM-OPS-001, statements.**
  - `core`: the product line Performance & reliability (BC-I-0539, placed in BC-C-083, C2), and the infrastructure "logically segmented and replicated throughout multiple availability zones" (BC-C-082/decides/BC-S-0450).
  - `shows`: the Cyber Week uptime record (BC-C-083/where/BC-S-0455, also the quality), and rate limits given as a safeguard for reliability (BC-C-057/reason/BC-S-0316, a reason).
- **CM-OPS-003, statements.**
  - `core`: Native Hosting for Catalyst projects and its own Infrastructure Hosting API (BC-C-052/where/BC-S-0288, BC-S-0287), and BigCommerce "as a shared hosting provider" in its PCI attestation (BC-C-028/responsible/BC-S-0169).
  - `outside`: the unnamed third parties "for hosting services that are essential to the Services" (BC-C-083/responsible/BC-S-0457), and Amazon hosting "customer / product catalog data, feed data, logs" (BC-C-082/where/BC-S-0447). Amazon is the slot filler, and its location, USA, is a quality.
  - Native Hosting covers Catalyst storefronts only and is in closed beta (BC-S-0289). Domain E's part may cite BC-S-0287 and BC-S-0288 as `core` for the headless storefront.
- **CM-OPS-005, statements, `core`:** BC-S-0331 and BC-S-0332. I don't cite BC-I-0061, the System Logs API resource, because the statement BC-S-0331 covers it.
- **CM-SRF-001, statements.**
  - `core`: the plan line (BC-S-0418). I don't cite BC-I-0398, which the statement covers.
  - `own-service`: Commerce's license of the Application (BC-S-0419).
  - `shows`: the Mobile App Terms (BC-S-0417), and the merchant's duty to have a compatible device (BC-S-0420).
- **CM-MIG-005, statements, `extension-point` only:** the App Marketplace category Data Transfer/Migration Services (BC-I-0484, placed in BC-C-059, F). What its apps move, and from which platforms, isn't stated.
- **The other eight cells are `none-held`.** Each lists its searched terms and reads its hits.

## Joins

- **By terms and definition:** BC-C-060 in CM-OPS-005, with keys BC-C-060/where/BC-S-0332 and BC-S-0331 against WC-C-037/where/WC-S-0038 and WC-S-0920.
- **By terms:** BC-C-077 in CM-SRF-001, with keys BC-C-077/decides/BC-S-0418 and BC-S-0419 against WC-C-090/where/WC-S-0422 and SA-C-001/decides/SA-S-2082.
- No join on role. BigCommerce was never matched by Q1.

## Homonyms kept apart

- **Blueprint.** WooCommerce's Blueprint is the export and import of store configuration (CM-MIG-006: WC-C-094/where/WC-S-0028, WC-C-094/boundary/WC-S-5451). BigCommerce's "non-Blueprint stores" (BC-C-044/where/BC-S-0248, E) names a kind of BigCommerce store, which the statement doesn't define. It isn't cited in CM-MIG-006.
- **Logs.** The landing rests on System Logs and Store logs. Two other logs are kept apart:
  - The same statement BC-S-0331 names a separate Staff Action Logs endpoint, "to audit the actions staff users performed in the store's control panel". That is an audit of staff actions, a different record from the store's log entries. A reading: it may belong to staff accounts (domain A). It is cited only as part of BC-S-0331's words, and "Staff Action Logs" isn't among the cell's terms.
  - Native Hosting's "worker logs" (BC-S-0287) are the hosting's logs, not the store's, so they are cited only in CM-OPS-003.
- **Status.** Storefront Status (BC-C-047/decides/BC-S-0265, A) is whether the storefront is open. Order, email, theme job and Partner statuses aren't CM-OPS-004's store status either.
- **Template.** Theme, widget and email templates aren't CM-MIG-003's export templates.
- **Export.** "Anti-Corruption, Export and Sanctions Compliance" (BC-C-080/where/BC-S-0435) is export control law, not a data export.
- **Mobile app.** BigCommerce's statements hold one mobile app, the merchant's (BC-C-077). No shopper-facing app of BigCommerce's own was found to keep apart.
- **Cloudflare.** The OpenNext Cloudflare adapter (BC-S-0290) is software that Native Hosting uses. Cloudflare as a subprocessor (BC-C-082/where/BC-S-0448) does DDoS mitigation and CDN. I don't cite the subprocessor row. A reading: CDN delivery and DDoS protection bear on hosting and reliability, but the row names security and delivery services, not the store's hosting. The reviewer may add it to CM-OPS-001 or CM-OPS-003 as `outside`.
- **Google.** In BC-C-082/where/BC-S-0446, Google's "Infrastructure hosting, document management, and communications" sits next to the purpose "Service delivery / product functionality for AI chatbots". Whether the hosting serves only the AI chatbots isn't clear from the row. Like G-zid with Google Cloud, I don't cite it in CM-OPS-003 and don't name Google as a slot filler.

## Strained fits

- None marked. See the note on BC-C-077 under "How I cut".

## What the checker flagged, and answers

- **BC-I-0484 (BC-C-059, F) in CM-MIG-005.** It is BigCommerce's only evidence of moving a store's data in from elsewhere, and it supports only `extension-point`, so no `core` is in two domains.
- **BC-C-028/responsible/BC-S-0169 (A) in CM-OPS-003, `core`.** It is the one statement naming BigCommerce as the host of stores in general: "including as a shared hosting provider". The others name only Native Hosting for Catalyst, or third parties. If domain A's part cites it as `core` for PCI compliance, the merge will flag it. The reviewer may lower it here to `shows`, which leaves Native Hosting as the cell's `core`.
- **`own-service` on BC-C-077/decides/BC-S-0419.** The statement names the company: "Commerce grants you a revocable, non-exclusive ... license to install and use the Application". Commerce is the licensor in BigCommerce's Mobile App Terms, the company that licenses the app. The app is separate from the control panel and installed on a device, so I read the statement as the company named as the app's provider. The plan line BC-S-0418 also supports `core`.
- **The `none-held` cells with matching statements.** I read every hit, and each cell's `reading` names them:
  - CM-EVO-001's hits are per-feature closed betas (BC-S-0077, scoped each time to one API), API groups marked Beta, unified billing's opt-in, and staging's "preview".
  - CM-MIG-001's are bulk pricing rules, bulk-create companies, export control law, and the migration category cited in CM-MIG-005.
  - CM-MIG-003's are theme, widget and email templates, and export control law.
  - CM-MIG-004's one hit is export control law.
  - CM-MIG-006's are theme backup and restore, the Settings APIs, the merchant's duty to back up, and "non-Blueprint stores".
  - CM-OPS-002's and CM-OPS-004's are statuses of other objects, HTTP 429 advice, the uptime record, and promotions "Tools".

  On CM-EVO-001: closed betas are BigCommerce's release model for single features, which is the subject of area EVO. The model's only EVO capability, though, is feature settings, a place where the merchant turns features on or off, and no BigCommerce statement shows one. The closed betas have no place of their own: no section, plan line or category for the beta programme. Each is a decides statement of one feature's API. So I add no capability. The reviewer may read BC-C-052/decides/BC-S-0289 (in an `also` concern) or BC-S-0077 as `shows` on CM-EVO-001, as Shopify's "Test new features before launch" is read there.

## Gaps and problems

- **BC-C-060/decides is a page Q1 didn't read.** What the store logs record, how long they are kept, and who can see them aren't stated, so CM-OPS-005 holds no retention quality for BigCommerce. BC-C-060/responsible is stated only in general terms.
- **BC-C-077/boundary and BC-C-077/reason were searched, not found.** No API, scope or push notification for the mobile app is held, and nothing says what the app does.
- **BigCommerce's store import and export** is unheld in the concern map: no control panel route, API resource or plan line. Whether BigCommerce has it isn't stated. A capture of its Help Center on import and export would settle it.
- **No status page** is held for BigCommerce. Q1 records no gap for it, since no concern covers it.
- **BC-I-0539, Performance & reliability,** is a product line name only. What the line covers isn't held.

## The coordinator's correction after E-bigcommerce batch 1 (30 October)

- **BC-S-0287 counts once:** `core` in E's CM-SFR-008, store domains, whose BigCommerce cell rests on it, and `shows` here. CM-OPS-003's BigCommerce cell stays `core` on BC-S-0288 and BC-S-0169. Native Hosting (BC-C-052) now lands here, through `G-amend`.
