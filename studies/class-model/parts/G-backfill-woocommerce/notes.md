# G-backfill-woocommerce: notes

## What this part did

G-woocommerce added six capabilities to domain G: CM-MIG-006 (export and import of store configuration), CM-OPS-003 (hosting of the store), CM-OPS-004 (store status), CM-OPS-005 (store logs, under CM-OPS-004), CM-EVO-001 (feature settings) and CM-SRF-001 (mobile app for managing the store). This part writes their twelve cells for Shopify and Salla. It adds no capabilities, lands no concerns, and writes no rulings, qualities or slot fillers.

For each platform I ran `candidates --domain G`, read the leads with `key`, and searched further with `search`: Salla in English and in Arabic, each Arabic term in its singular and its plural, with and without ال. The terms are in each cell's `searched`. Four cells hold statements, eight are `none-held`. `none-held` means only that the concern map holds nothing found by those terms; it never means the platform lacks the capability. Each row is a reading unless it quotes a statement.

| Capability | Shopify | Salla |
|---|---|---|
| CM-MIG-006 store configuration | none-held | none-held |
| CM-OPS-003 hosting | core: SH-C-036/decides/SH-S-7032 | none-held |
| CM-OPS-004 store status | none-held | none-held |
| CM-OPS-005 store logs | none-held | none-held |
| CM-EVO-001 feature settings | core, a reading: SH-I-1235, SH-I-1308 | none-held |
| CM-SRF-001 mobile app | core, a reading: SH-C-079/decides/SH-S-5144, SH-C-118/decides/SH-S-5145, SH-C-043/decides/SH-S-5149 | core: SA-C-001/decides/SA-S-2082 |

## The readings

- **CM-OPS-003, hosting.** Shopify: the plan line Unlimited web hosting, Included on all four plans (SH-S-7032). SH-C-036 is E and names G under `also`. This is G-woocommerce's lead. U-014's `joined:CM-OPS-003` for SH-C-036 now holds. I left two things uncited:
  - the subprocessor row "Cloud hosting and data processing" (SH-C-181/where/SH-S-0196). It names Google Cloud Canada Corporation as a supplier of Shopify's own, and its subject, where data is processed, is A's (a reading). Citing it as `outside` would say a third party hosts the store in the merchant's place, which no statement says. So U-042 stays `apart` for SH-C-181.
  - Oxygen (SH-C-139, E, not naming G), which hosts Hydrogen storefronts.

  Salla: its hosting hits are its hosting of themes and partners' apps and services (SA-C-090, SA-C-194, SA-C-195, SA-C-208) and App Functions' serverless runtime (SA-C-145, SA-C-196). Neither hosts the store, so the cell is `none-held`.
- **CM-EVO-001, feature settings.** Shopify: the plan line Test new features before launch, which its citations show as included on Plus only (SH-S-1999, SH-S-2072, context). It exists only as inventory entries placed in SH-C-015 (domain A, not naming G), so the cell cites SH-I-1235 and SH-I-1308 by id (C2). Placing them as `core` is a reading on two counts:
  - that "new features before launch" are the platform's experimental features, which WooCommerce's definition includes (WC-S-5433);
  - that a plan line including them is the capability, though no statement shows a section where the merchant enables or disables them.

  G-woocommerce's notes expected `none-held` unless such a section were shown, an assumption. This line is the one thing the search adds. **The reviewer may read it otherwise:** as the merchant testing their own changes, or as too far from "enables or disables". Then the evidence rows go and the cell is `none-held`.

  Salla: its `released` flags each gate one feature (C6; the anchor's EVO note). Nothing is a section where the merchant turns features on or off, so the cell is `none-held`.
- **CM-SRF-001, mobile app.**
  - Salla: the plan line تطبيق إدارة المتجر على أجهزة iOS و Android (SA-S-2082, Salla Plus). `scope.tsv` now names G under SA-C-001's `also` for it, so U-068's `joined:CM-SRF-001` holds. SA-C-004's iOS subscription line (SA-S-2083, A, not naming G) isn't needed and isn't cited.
  - Shopify: the anchor's searches found no merchant mobile app. This search finds Shopify's own admin routes named for mobile, whose eligibility is `"clients":["native"]`: order:mobile:record-payment, order:mobile:release-fulfillment-holds and customer:mobile:edit-marketing-status. Reading a native client served by routes for managing orders and customers as a mobile app for managing the store is a reading. No statement names the app. The routes' concerns are of C and D and don't name G, and the cell cites them because nothing else holds it. If the reviewer finds "native" too thin, the cell becomes `none-held` or `shows`.
- **CM-MIG-006, CM-OPS-004 and CM-OPS-005, `none-held` on both platforms.** Each cell's reading names the hits and why they aren't the capability.

## Homonyms kept apart

- **Mobile app:** Salla's channel Mobile app (SA-C-094, App Maker's branded commerce app for buyers, with the store-ios-app and store-android-app flags) and Shopify's Shop app and Mobile app builder apps (SH-C-136, SH-C-195) are buyers' apps, not the merchant's app of CM-SRF-001.
- **Log:** Shopify's staff audit log (SH-C-012) and Salla's Activity history and Export log (SA-C-010; U-044), and Salla's per-feature logs: translation, SMS, inventory, digital cards, shipments, webhooks, e-payments, and the API's Change Log. None is the logger's entries of CM-OPS-005.
- **Status:** Salla's platform status page (SA-C-101/where/SA-S-0211, SA-C-234/where/SA-S-0047; CM-OPS-002), and the order, refund and coupon statuses of both platforms. None is the store's system status of CM-OPS-004.
- **Hosting:** Salla's hosting of themes and of partners' apps, and Shopify's subprocessors' cloud hosting, both against hosting the store.
- **Restore:** Salla's restore of deleted data (restore_data_management, restore-data) and Shopify's backup region in Markets, both against exporting a store's configuration.

## Leads not cited

Salla's Plus plan line تفريغ الكاش, clearing the cache (SA-C-002/decides/SA-S-2092, A, not naming G), is one tool. WooCommerce's statements don't say what its Tools are, so no statement shows the two as the same thing, and the line stays out of CM-OPS-004 (a reading).

## Gaps

- No statement says what Shopify's hosting consists of (CM-OPS-003).
- No statement names the maker of either platform's merchant mobile app, or its push notifications (CM-SRF-001).
- Shopify's Test new features before launch has no statement beyond the plan line's label. Nothing says which features, or how they are turned on (CM-EVO-001).
- WooCommerce's definitions of system status, Tools, Logs and Blueprint aren't stated by Shopify or Salla. Their cells are `none-held`.

## What the checker flagged, and my answers

The final run prints 0 problems and 13 flags.
- **Outside also (5 flags), evidence lines 3 to 7:**
  - SH-I-1235 and SH-I-1308 (SH-C-015, A), for CM-EVO-001;
  - SH-C-079/decides/SH-S-5144 and SH-C-118/decides/SH-S-5145 (C) and SH-C-043/decides/SH-S-5149 (D), for CM-SRF-001.

  Each cell needs them, as nothing of a G concern or a concern naming G holds it, and each cell's reading says why (see "The readings"). None of them is cited in its own domain for a G capability, so the merge's check on `core` in two domains may flag them too. The reviewer decides.
- **none-held with matching statements (8 flags), on cells.tsv lines 2, 3, 5 to 9 and 11:** each cell's reading names its hits by concern and says why none is the capability. Salla's CM-EVO-001 matches 1,311 statements, mostly through the other platforms' term Features and the flags' `released` and `enabled` keys. Salla's CM-OPS-004 matches 174, mostly order statuses and plan lines. Neither shows a section of the capability.

## Problems

- None with the brief. The Shopify readings on CM-EVO-001 and CM-SRF-001 rest on statements of other domains. The reviewer may prefer `none-held` there.
