# Notes on batch P-7 (S-02: S02-VP-69 to S02-VP-76, S02-VP-78, S02-VP-79, S02-VP-84)

The drafter's notes for the coordinator (`briefs/P-points.md`). The model is read merged, at a11d4727; `show` printed no warning that a domain's files changed after the merge. Every landing and every side of a conflict below is a reading unless it quotes a key.

Count: 11 points. 6 landed (S02-VP-70, S02-VP-74, S02-VP-75, S02-VP-76, S02-VP-78, S02-VP-79). 5 have conflicts (S02-VP-69, S02-VP-71, S02-VP-72, S02-VP-73, S02-VP-84), 6 conflicts in all: 4 `count`, 2 `placement`, no `structure`, no `premise`.

## Points that were hard to land

- **S02-VP-69, the checkout's address form.** No capability is "the address form". CM-CUS-008 (customer addresses) is the closest thing: its Salla cell holds the setting itself (`settings.address.form`, the national address for buyers in Saudi Arabia, SA-C-065), and its WooCommerce cell holds the addresses typed at checkout (WC-S-0919). But Shopify's Customer information section (S02-SH-652) and Zid's طريقة تحديد عنوان العميل (S02-ZD-142) are inside their checkout settings, so CM-CHK-001 is the second capability. I did not count this as a `structure` conflict. The model holds the buyer's address in CUS-008 and the checkout's settings in CHK-001, and the platforms answer in both. But the same setting, a national address required at checkout, sits in CUS-008 on Salla and in no cell on Zid. The Zid `count` asks the coordinator to settle where it belongs.
- **S02-VP-70, who sets address autocompletion.** I found CM-CUS-009 (map and location services for addresses) with `caps --terms autocomplet`: no lead offered it. Its WooCommerce cell holds the Address autocomplete setting (WC-S-5379, WC-S-5380). Only Shopify's variants are about autocompletion itself (S02-SH-240, S02-V-663). The other four answer who sets the address fields' requirements, which is CUS-008's thing, so both capabilities are named. This is a "who sets" point, so no `count` is drafted (see the leads below).
- **S02-VP-71 and S02-VP-72, staff permissions.** I read their reach as `cross-cutting: identity and permissions`. CM-STF-002's note says the permissions each capability cites are evidence for that capability, so the permission system is held in every area. S02-VP-72 also names CM-MKS-001, because the Markets permission is cited there (SH-C-106/decides/SH-S-5203, VIEW_MARKETS), found by search.
- **S02-VP-73 and S02-VP-74, a customer's market.** Matching a buyer to a market is CM-MKS-004's thing: local domains and visitor geolocation, "sending each market's buyers to its domain, country and currency". Shopify's backup region (SH-C-113) and Salla's Market selection (SA-S-1730) are cited in CM-MKS-001, so both are named.
- **S02-VP-75, customer privacy.** Zid's only answer is its store's privacy-policy page (S02-ZD-462, an admin route under pages/legal). The model holds Zid's legal pages in CM-CNT-008 (ZD-C-039/where/ZD-S-0779, found by search), not in CM-TRU-006. So CNT-008 is the second capability and there is no conflict on Zid. The model holds the privacy policy in two places: WooCommerce's privacy notices in TRU-006, and Zid's and Shopify's policy pages in CNT-008. I read them as two different things, notices against the page, so I raised no `structure` conflict.
- **S02-VP-76, the business address.** I read its reach as `capability`. The store's country it carries belongs to the cross-cutting decision "markets and the seller's country", but the address itself isn't held in every area. CM-ACC-004 is named for Shopify, whose address comes in its business entity's form (S02-SH-324). I found it by search; the key cited is SH-C-004/where/SH-S-6306.
- **S02-VP-79, the customer service details.** I found CM-ACC-006 by search; it holds the details (SA-C-231/boundary/SA-S-5147, BC-C-047/where/BC-S-0263). CM-TRU-010 holds the law that each store must add them (SA-S-0160) and Zid showing them at the foot of the store page (ZD-S-0763). That is where Salla's and Zid's "the platform" answers sit.

## The conflicts, with both sides

1. **S02-VP-69, `count`, WooCommerce (rows: S02-F7, S02-F10, model).**
   - The subject's side: S02-WC-142, -143, -145, -151, -156 and -159 are WooCommerce's shipped `WC_Countries` code: address formats per country, a locale per country that makes fields required or hidden, and its own filters. By B-extent that is core.
   - The model's side: CUS-008's WooCommerce cell is `not-stated`, with WC-C-047/where/WC-S-0919 as shows.
   - Reading: the statements bear out core. The concern map holds the same release file under WC-C-099 at other locators (the `page` lead).
2. **S02-VP-69, `count`, Zid (rows: S02-F7, model).**
   - The subject's side: S02-ZD-142 to -144 are Zid's own checkout-page setting for customer addresses, with the national address option and fields by country.
   - The model's side: CUS-008's Zid cell is none-held, while Salla's like setting is CUS-008's core (SA-C-065/decides/SA-S-3031, SA-C-065/reason/SA-S-5021). CHK-001's Zid cell (ZD-C-099/where/ZD-S-0961) holds the page and names no address setting.
   - What settles it: which capability holds an address-form setting.
3. **S02-VP-71, `count`, BigCommerce (rows: S02-D6, model).**
   - The subject's side: S02-BC-345 to -348 are BigCommerce's team permissions and user permissions at Settings › Users.
   - The model's side: CM-STF-002's BigCommerce cell is none-held.
   - Reading: the statements bear out core. None of them traces to the concern map.
4. **S02-VP-72, `placement`, WooCommerce (rows: S02-F10, model).**
   - The subject's side: S02-WC-463 and -464 have third parties' plugins changing what roles can do (User Roles Editor for WooCommerce).
   - The model's side: CM-STF-002's WooCommerce cell is core only (WC-C-080/where/WC-S-0883, WC-C-080/boundary/WC-S-5418).
   - What settles it: whether the plugins work through an interface WooCommerce provides (`extension-point`) or not (`outside`).
5. **S02-VP-73, `count`, BigCommerce (rows: S02-D5, model).**
   - The subject's side: S02-BC-327 to -329 are BigCommerce's per-channel setting Allow global logins, which decides which storefronts a customer may enter.
   - The model's side: CM-MKS-001's BigCommerce cell is none-held, and CM-MKS-004's is core on transactional currency only (BC-C-074/decides/BC-S-0402).
   - This conflict holds only if BigCommerce's channels are its markets in the model (the subject's S02-VP-26, batch P-4). If they aren't, the setting is customer accounts' (CM-CUS-010, core) and the conflict should be dismissed. The coordinator should settle it with S02-VP-26.
6. **S02-VP-84, `placement`, WooCommerce (rows: S02-F10, model).**
   - The subject's side: S02-WC-415 says another extension provides the cookie banner, through WP Consent API. S02-WC-448 has WooCommerce's order attribution reading consent through `wp_has_consent`, and S02-WC-450 asks extensions to secure consent.
   - The model's side: CM-TRU-006's WooCommerce cell is core only (WC-C-045/decides/WC-S-0881) and says no cookie banner or consent setting is held.
   - What settles it: whether WP Consent API is an interface WooCommerce provides (`extension-point`) or WordPress's alone (`outside`).
   - S02-VP-75's WooCommerce variant rests on S02-WC-413, the same extension's statement that visitors in the EEA, UK and Switzerland must consent before tracking. It shows the rule, not a third party doing the work, so S02-VP-75 carries no conflict. Settling this conflict settles S02-VP-75's cell too.

No `premise` conflict: no register row naming these points claims anything about the references that a cell contradicts.
- S02-F7 says the address form follows the buyer's country on all five. The cells say nothing about markets.
- S02-F8 names Shopify's and BigCommerce's address form per market. The cells are silent on that too.

## The checker's leads, and what I made of them

- **S02-VP-71, BigCommerce:** answered by conflict 3.
- **S02-VP-72, BigCommerce:** the same statements (S02-BC-348). This is a "who sets" point, and a staff member setting the platform's own permission is core, so no conflict here. Conflict 3 carries the missing cell.
- **S02-VP-78, WooCommerce:** CM-INV-005's WooCommerce cell is none-held.
  - The subject's statements are about Local Pickup: pickup locations offered to customers (S02-WC-389, -390, -395, -396), and its save route guarded by `manage_woocommerce` (S02-WC-394).
  - The cell's reading already rules local pickup a different kind of location from where stock is held (WC-S-0292).
  - This is a "who sets" point, so no conflict. If the coordinator reads pickup locations as الفروع, the WooCommerce cell would gain them.
- **S02-VP-84, Zid:** CM-TRU-006's Zid cell is none-held.
  - The subject's Zid statements are not about cookies: the merchant's privacy policy applies, not Zid's (S02-ZD-334, -335, -338); a buyer may opt out of targeted advertising on the merchant's site (S02-ZD-335); WhatsApp opt-out words are fixed (S02-ZD-337, -339), a marketing messages setting.
  - No Zid statement names a cookie setting. Whether Zid has one is the subject's gap S02-ZD-G19. No conflict.

Leads the checker doesn't print, because a landing cell on the platform holds statements:
- **S02-VP-70, Shopify:** CM-CUS-009's Shopify cell is none-held, though S02-SH-240 and S02-V-663 state Shopify's own default address autocompletion, active by default and turned off in its checkout and accounts editor. That would be core.
- **S02-VP-70, BigCommerce:** CUS-009's BigCommerce cell is none-held, though S02-BC-304's heading is Google Autocomplete for Addresses, under its checkout settings and the Manage Settings permission.
- Both are drafted without a conflict because the brief limits a "who sets" point to `placement`. The coordinator may add them as `count` conflicts "(the coordinator)", or amend CUS-009 under S02-VP-69's settling.
- **S02-VP-73 and S02-VP-74, Salla:** CM-MKS-004's Salla cell says "No Salla statement gives a market its own domain", but S02-SA-102 states the redirect of a visitor from the UAE to the market's own domain (ae.example.com). The cell is already core, so it is no `count`. Its reading would change.

## Third parties and laws the subject names that `cell` doesn't list as slot fillers

None of the landing capabilities is of the kind `slot`. Those with `outside` cells are CM-MKS-004 (WooCommerce) and CM-INV-005 (Zid, BigCommerce). Each name below is a lead, not a conflict.
- CM-CUS-008 (S02-VP-69, S02-VP-70):
  - SPL's National Address (S02-SA-303, S02-ZD-143);
  - Saudi Cabinet Decision No. 252, قرار مجلس الوزراء رقم (252), which Zid gives as the basis for requiring the short national address (S02-ZD-182);
  - the shipping companies whose acceptance the setting ensures (S02-SA-022, S02-ZD-182).
  - The cell lists only الهيئة العامة للنقل.
- CM-CUS-009 (S02-VP-70): Google, in BigCommerce's Google Autocomplete for Addresses (S02-BC-304), a feature's name and not a statement that Google does it.
- CM-MKS-004 (S02-VP-74): Shopify's Geolocation app (S02-SH-230). No statement names its maker, and the cell's Geolocation apps category (SH-C-111/where/SH-S-2681) is already `extension-point`.
- CM-INV-005 (S02-VP-78): third-party apps that use FulfillmentService and create their own locations (S02-SH-910, S02-SH-913). The Shopify cell's `extension-point` (SH-C-024/boundary/SH-S-6206) already holds them.
- CM-TRU-006 (S02-VP-75, S02-VP-84):
  - the privacy laws behind consent in the EEA, the UK and Switzerland (S02-WC-413);
  - Google's tags and consent mode (S02-WC-413);
  - WP Consent API (S02-WC-415).
  - The cell lists the GDPR and the CCPA, both on BigCommerce.

## Problems with the brief or the script

- The brief allows only `placement` on a "who sets" point. So when a who-sets point and its "takes its value per" twin are in different batches, or rest on different statements, a cell the subject shows to be missing goes unrecorded on the who-sets side. Here that is CUS-009's Shopify and BigCommerce autocompletion.
- The checker requires the register rows in `show`'s order. That order is not always the row ids' order: S02-VP-78's is S02-M7 first.
