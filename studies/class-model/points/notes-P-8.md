# Notes: batch P-8 (S-02, points 77, 80 to 83, 85 to 92)

These are the drafter's notes for the coordinator (`briefs/P-points.md`, "Notes"). The model is the merge at a11d4727. Every placement and slot filler below is the model's cell as `land_points.py cell` printed it. Every "reading" is marked as one.

**Count:** 13 points.
- 7 are `landed`: S02-VP-77, S02-VP-83, S02-VP-85, S02-VP-86, S02-VP-87, S02-VP-91, S02-VP-92.
- 6 are `conflict`: S02-VP-80, S02-VP-81, S02-VP-82, S02-VP-88, S02-VP-89, S02-VP-90. They hold 8 conflicts: 5 `count`, 2 `placement`, 1 `structure`.

No conflict is under a founder's decision. They rest on:
- S02-D6, engineering's ruling, under which the founder entered no veto;
- S02-F7 and S02-F10, rows that follow by rule (RD3);
- the model alone, for the `structure` conflict.

The checker's final line: `# 13 points in P-8, 0 problems`. It printed no `lead:` lines.

## Points that were hard to land

- **S02-VP-77 and S02-VP-91: no lead offered the store's settings.**
  - The only leads were CM-SEL-004 (Salla's bookings, through its help page) and, for S02-VP-91, CM-ACC-004 and CM-TRU-010 (through Zid's store-info page). No capability is named for a time zone or for units. `caps --terms "time zone;timezone;weight unit;units"` finds only CM-SHP-020, for a product's weight in customs data.
  - I landed on CM-ACC-006 by `search`. Four platforms hold these values in their general settings:
    - Shopify: Store defaults in Settings > General (S02-SH-246);
    - Zid: the time zone in Business address (S02-ZD-465);
    - BigCommerce: localization settings, with BC-C-047/where/BC-S-0262 returning "status, domain, and timezone";
    - WooCommerce: its measurement settings (S02-WC-289).
  - Salla holds no store time zone. Each of its answers belongs to one flow, so I named that flow's capability:
    - bookings use Saudi time only (S02-SA-431, S02-SA-432): CM-SEL-004;
    - the order prep list's "Use Saudi Arabia time zone" (S02-SA-433): CM-ORD-009. This is a reading: the prep list is a printed order document, and the model doesn't hold the prep list itself.
  - In S02-VP-91, WooCommerce's units are set from the store's location by its onboarding (S02-WC-292, S02-WC-244), so I added CM-ONB-004.
  - Not landed: Salla's weight unit per product (S02-SA-435, "Product weight and weight unit"). It is a lead for CM-CAT-001, the product's own fields. It also sits beside S02-F7's "one set of units are held for the whole store". That is a matter inside the subject, not a conflict with the model.
- **S02-VP-80 and S02-VP-81: three capabilities for one setting.**
  - Salla's and Zid's answers land on CM-ACC-007.
  - WooCommerce's coming soon mode lands on CM-ACC-009.
  - BigCommerce's storefront status (S02-BC-314) is the setting Storefront Status, which CM-ACC-006 holds (BC-C-047/decides/BC-S-0265). The subject's statements don't give its values, so whether it is a maintenance mode isn't stated: a lead for CM-ACC-007 or CM-ACC-009 on BigCommerce, not a conflict.
  - Set aside:
    - Shopify's Pause and Build plan (S02-SH-752, S02-SH-756, S02-SH-758). It keeps the store online and turns off checkout, so it isn't a maintenance mode. It is a lead for the plans capabilities.
    - Zid's "stop receiving orders" (S02-ZD-343). CM-ORD-010 already holds it (Zid core).
- **S02-VP-82 and S02-VP-83: the key is broader than its word.** التذكير is Salla's abandoned-cart reminder, but the point's key is "messages to buyers" (`variation-points.tsv`). So I named four capabilities, five and six in S02-VP-83:
  - the abandoned-cart reminder itself: CM-MKT-022;
  - the store's notifications: CM-NTF-001;
  - sender and delivery: CM-NTF-004;
  - SMS marketing: CM-MKT-007;
  - in S02-VP-83 only, WooCommerce's own review-request and restock flows: CM-SUP-002 and CM-MKT-016, both core on WooCommerce.

  Zid's buyers stopping WhatsApp messages (S02-ZD-337) can also be read as CM-CUS-007's (marketing consent), where Zid holds nothing. I read it as a setting of Zid's own WhatsApp product, CM-NTF-004 (Zid core), with the buyer as who sets it. So it raises no conflict. If the coordinator reads it as consent, S02-ZD-337 and S02-ZD-338 would place Zid core in CM-CUS-007: a `count`.
- **S02-VP-85: reach.** I read it as `cross-cutting: markets and the seller's country`, as S02-VP-01 landed. BigCommerce's per-storefront country (S02-BC-109) is a value of the same setting, keyed on its storefront. Its store_country is global only (S02-BC-100).
- **S02-VP-89: WooCommerce's inbox notes.** WooCommerce shows notes to the merchant, keyed on:
  - the store's base country (S02-WC-433, S02-WC-434);
  - whether it sells to the EU (S02-WC-278, S02-WC-279, S02-WC-510).

  Some notes come from WooCommerce.com (S02-WC-435). I landed them on CM-NTF-002, notices to the store's own people, which is core on WooCommerce. This is a reading. The model holds WooCommerce's admin notes resource (WC-C-081/boundary/WC-S-0206) in no cell: `q3.py where` says "cited in no cell", its concern landing in CM-ONB-004. Notes from the platform to the merchant could be read as a thing of their own. If so, that would be a `structure` matter, which I didn't raise.

## Each conflict, with both sides

1. **S02-VP-80, `count` (rows: S02-D6, model). Shopify's private mode.**
   - The model: CM-ACC-009's Shopify cell is none-held. CM-ACC-007's is none-held too, after searching maintenance, password page, password protection, Store password and storefront password.
   - The subject:
     - S02-SH-719 manages access to the online store through private mode;
     - S02-SH-726 is the Admin API field OnlineStorePasswordProtection.enabled;
     - S02-SH-720, S02-SH-759 and S02-SH-775: private mode is on by default until launch and during the trial;
     - S02-SH-749: the store closes temporarily, with no vacation setting.
   - A reading: core by the model's rules, in CM-ACC-009 (before launch) and CM-ACC-007 (a temporary closing). None of these statements is in the concern map, so an amendment would cite them.
2. **S02-VP-80, `structure` (rows: model). CM-ACC-007 and CM-ACC-009 may be one thing.**
   - The model: CM-ACC-009's note keeps them apart. No held statement defines what Salla's maintenance mode does to the storefront. The reviewer "may join them on role if a definition of Salla's mode is held".
   - The subject:
     - WooCommerce's coming soon mode also "temporarily make[s] your site invisible to the public while you work on it" (S02-WC-497);
     - it syncs with "a maintenance mode plugin" (S02-WC-499);
     - Shopify's private mode serves both before launch (S02-SH-720) and a temporary closing (S02-SH-749).

     S02-SA-063 and S02-SA-064 (Salla's maintenance per market) don't define it either.
   - What would settle it: a definition of Salla's maintenance mode, meaning what a buyer sees. A Salla run could capture that page. If they join, conflict 1 falls on one capability.
3. **S02-VP-81, `count` (rows: S02-F7, model).** This is conflict 1 again, on the "who sets" point: the seller sets Shopify's own private mode. One amendment settles both.
4. **S02-VP-81, `placement` (rows: S02-F10, model). Third parties and WooCommerce's coming soon mode.**
   - The model: CM-ACC-009 on WooCommerce is core only (WC-C-082/where/WC-S-0009, WC-C-082/decides/WC-S-0891, WC-C-082/decides/WC-S-5421, WC-C-082/boundary/WC-S-5423).
   - The subject:
     - S02-WC-496 is a guide "for third-party developers and hosting providers on how to integrate their systems with WooCommerce's coming soon mode";
     - S02-WC-498, S02-WC-499 and S02-WC-501 sync the mode from another plugin, a maintenance mode plugin among them, through the option woocommerce_coming_soon;
     - S02-WC-500 covers a hosting provider's coming soon mode;
     - S02-WC-503 and S02-WC-508 let developers add exclusions through the filter woocommerce_coming_soon_exclude.
   - A reading: extension-point beside core, through WooCommerce's option and filter.
5. **S02-VP-82, `count` (rows: S02-D6, model). Shopify's SMS Sender ID.**
   - The model: CM-NTF-004's Shopify cell is none-held. Its reading says "No statement says how Shopify delivers its notifications". Zid's sender name is core in the same capability (ZD-C-098/decides/ZD-S-0957).
   - The subject:
     - S02-SH-871: the SMS Sender ID is based on the store name in Store contact details;
     - S02-SH-872: some countries don't support dynamic Sender IDs, so the store's number shows instead.
   - A reading: core on Shopify. The other reading is that the Sender ID belongs to CM-NTF-001, where Shopify is core already, and then the conflict falls. The coordinator chooses.
6. **S02-VP-88, `placement` (rows: S02-F10, model). The visitors' consent interface on WooCommerce.**
   - The model: CM-TRU-006 on WooCommerce is core only, resting on the Accounts and Privacy notices (WC-C-045/decides/WC-S-0881). Its reading says no cookie banner or consent setting is held.
   - The subject:
     - S02-WC-415: Google Analytics for WooCommerce "does not provide any UI, like a cookie banner", and is "integrated with WP Consent API, so you can pick another extension that provides a user interface";
     - S02-WC-402 and S02-WC-448: order attribution reads consent through the WP Consent API.
   - A reading: a third party's extension provides the consent banner. That is extension-point, or outside if the WP Consent API isn't read as the platform's interface.
   - It bears on S02-VP-84 (who sets cookie preferences), which is batch P-7's. The coordinator may want to read the two together.
7. **S02-VP-89, `count` (rows: S02-D6, model). BigCommerce's internal notifications.**
   - The model: CM-NTF-002's BigCommerce cell is none-held, after searching staff notification, staff notifications, staff, new order, order notification and admin notification.
   - The subject: S02-BC-144: "you can do all of this within the control panel: [...] Configure storefront settings and internal notifications for each storefront".
   - A reading: core. What an internal notification is isn't stated: a gap the amendment would carry.
8. **S02-VP-90, `count` (rows: S02-F7, model).** This is conflict 7 again, on the "who sets" point. One amendment settles both.

## The checker's leads

The checker printed no `lead:` lines. Leads from `show` that I set aside, and why:
- S02-VP-77 and S02-VP-91: CM-ACC-004 and CM-TRU-010 come only through Zid's store-info page (`page`). The time zone isn't the business entity's or the seller's legal compliance.
- S02-VP-80: CM-ANL-001 and CM-ANL-004 come only by the term Live.
- S02-VP-81:
  - CM-ORD-010 (Zid's working-hours page) holds the closing beside order receiving. CM-ACC-007 already cites Zid's closing (ZD-C-104/where/ZD-S-0970).
  - CM-CNT-008 and CM-TRU-010 come through Zid's Terms page, which only states terms.
- S02-VP-82 and S02-VP-83: CM-CUS-007, by "SMS marketing" (see Zid's opt-out above), and CM-CUS-013, by "WhatsApp marketing". They are a buyer's consent and sign-in codes, not messages.
- S02-VP-85: set aside because the point asks the store's country, not the markets or the currency:
  - CM-MKS-001 and CM-MKS-005 (through WC-S-0880, which CM-ACC-006 also cites);
  - CM-ONB-001, the country at sign-up;
  - CM-CHN-007, by the term country.
- S02-VP-86 and S02-VP-92: set aside because none is the installed app:
  - CM-APP-002 (the app store), CM-APP-009 (custom apps) and CM-CHN-006 (the store's mobile app);
  - CM-ACC-005 (Shopify's multiple entities, which carries S02-SH-1149's page) and CM-AIA-005.
- S02-VP-87 and S02-VP-88: CM-TRU-021 (WooCommerce's usage tracking to Automattic) is the platform's telemetry, not the store's analytics. CM-CUS-007 comes by the term pixels.
- S02-VP-89 and S02-VP-90: CM-MKT-022 (term emails), CM-ORD-003 (term order_statuses), CM-ACC-001, CM-APP-002 and CM-CHK-007 come through Zid's pages.

Leads for the model's cells that are not conflicts. The subject holds statements a cell lacks, but they would place the platform `extension-point`, and a `count` needs `core` or `own-service`:
- **CM-MKT-009 on Zid** is none-held. The subject's S02-ZD-293 to S02-ZD-298, S02-ZD-453, S02-ZD-454 and S02-ZD-456 show Google Analytics, Google Tag Manager, Facebook pixel and TikTok Pixel as apps in Zid's App Market category تتبع الحملات. Each is activated with the merchant's account code.
- **CM-MKT-009 on WooCommerce** is none-held. Google Analytics for WooCommerce (S02-WC-412 to S02-WC-415) is an extension configured under WooCommerce > Settings > Integration. Its maker isn't stated, a gap, so it gives no own-service.
- **S02-WC-409** ("connect your store to our service") is the same text as WC-S-0573, which the model reads as naming no company. It gives nothing new for CM-ANL-001.

## Slot fillers named by the subject and not listed

These cover the landings on a `slot` capability or one with `outside` cells: CM-CHK-004 (slot), CM-NTF-004 (Zid outside) and CM-MKS-006 (Shopify outside).
- CM-CHK-004: Shopify's post-purchase and cross-sell apps (S02-SH-091, S02-SH-1149) are named only as a kind, with no third party by name.
- CM-NTF-004:
  - Salla's default communication apps for local and international SMS (S02-SA-413 to S02-SA-415) and the SMS apps a market's sign-in draws its OTP provider from (S02-SA-461) name no provider.
  - Zid's sender-name documents for the UAE, Kuwait and Oman (S02-ZD-163 to S02-ZD-166) name each country's commercial register or licence, and no authority.
- CM-MKS-006: WooCommerce's "multi-currency extension/plugin" (S02-WC-025) is named only as a kind.

Leads on capabilities without outside cells, for the coordinator's reading:
- CM-MKT-007 on Shopify:
  - the Privacy and Electronic Communications Regulations, a law for SMS marketing to or from the United Kingdom (S02-SH-954);
  - Meta, with which stores in Brazil or Indonesia verify their account for WhatsApp marketing (S02-SH-965, S02-SH-966).

  Its listed fillers are SendGrid and Twilio.
- CM-MKT-009 on Salla:
  - Google, through the Google Analytics and Tag Manager apps (S02-SA-401, S02-SA-405);
  - Meta, whose pixel and Conversions API Salla connects (S02-SA-407).

  The cell lists no slot filler.
- CM-TRU-006 on WooCommerce: the WP Consent API and "another extension" for the consent banner (S02-WC-415), as conflict 6.

## Problems with the brief or the script

- None that blocked the work.
- At first I separated `--terms` with commas, which `class_slice.py` reads as one phrase. Its separator is `;`. The single-term searches I ran cover the same ground, so nothing was missed.
- One cross-batch matter for the coordinator: conflict 6 (CM-TRU-006 on WooCommerce) is the thing that P-7's S02-VP-84 (who sets cookie preferences) asks about.
