# SH-46: notes

Shopify's `merchant-changelog`, its oldest 86 posts, from 4 April 2019 back to 3 August 2018 (`changelog.shopify.com@posts`, observed-sh at `e38dc17e3`). Effort `high`.

## What I read

- The brief; the rules digest (`held/rules/merchant-changelog.md`) whole, section 6 included; the rulings' last section (`review-H-rulings.md`, "After the batches under version 3").
- observed-sh's guides: `README.md`, `docs/READING.md`, `structures/README.md`, `docs/GAPS.md` (no line on the changelog), the register's `shopify/merchant-changelog` row (`index/ledger-summary.tsv` has no changelog row); the evidence map's introduction, coverage and faults; B-extent's "Cells and evidence" and "Conventions from the dry run"; the structure's `show --meta` and `selection.tsv` row.
- No earlier batch's notes: the digest, and one grep of the earlier placements per chunk by its posts' distinctive words, gave every precedent I used. `earlier` found no key in any of the 86 entries, as for SH-44.
- No post's page: each entry's own text settled its capability, support and scope, so no archive record is cited, and I found no item that disagrees with its source.
- No rule of the brief read differently from B-extent.md in these entries.
- **The digest changed on disk during the batch** (SH-45's rules C45.1 to C45.10, and the table's rows for the Google app and the Buy Button channel, after the rulings' "Corrections after SH-45"). I read its section 6, its table and those corrections again. My lines already kept C45.1, C45.2, C45.3, C45.5, C45.7 and C45.9. Two lines had rested on the table's earlier `extension-point` row for the Google channel, which the corrections overturn; I rewrote them by rule 13 (C46.3 below): SH-E-d7c259a2 (Pinterest) and SH-E-20ac6905 (Instagram).

## Counts

86 entries, 142 lines: 138 on capabilities, 4 `new` (4 entries also take a capability line); none `out`. Supports: `core` 123, `own-service` 11, `shows` 11, `extension-point` 7.

## Rules I followed that the digest doesn't hold (for the coordinator)

- **C46.1:** the Shopify Plus wholesale channel is a sales channel the Plus plan includes, so its features are `core` on their capabilities (SH-E-dbcffeff: CM-B2B-003 for its volume pricing, CM-B2B-001 for the channel), as SH-42 placed its order confirmation setting (SH-E-60a6640f). `makers` holds no statement for 'wholesale channel', and no held words call it an app. If the coordinator reads it as an app with no maker held, rule 13 makes those two lines `shows`.
- **C46.2:** an app's own interface languages (the Shopify app's, the POS app's) take `new:Admin languages` `core` beside the app's line (CM-SRF-001, CM-POS-001): the interface language the merchant or the staff work in (the ruling after SA-49), as SH-E-c4c8d76b's line placed the admin's. The list of languages itself takes no line (market data). Entries: SH-E-8d8e59b8, SH-E-ff9a1b45.
- **C46.3:** a sales channel named for a third party, with no maker statement held (`makers`: none for Pinterest or for the Instagram channel), takes one line `shows;extension-point` on its capability: the channel's own work `shows`, the maker a gap (rule 13); the third party's own feature the post names `extension-point` (M-8), the third party the venue as filler. Entries: SH-E-d7c259a2 (Pinterest's Product Pins, CM-CHN-004), SH-E-20ac6905 (Instagram's shopping stickers and product tags, CM-CHN-001). Since the corrections after SH-45 made the Google channel `own-service` on its maker statements, its earlier `extension-point` row is no precedent for such channels.
- **C46.4:** a setting of the payment service that no capability holds and that has no place of its own (3D Secure, a setting inside Shopify Payments) goes on CM-PAY-002 `core`, and the effect the post states on chargebacks takes CM-PAY-009 `core` (rule 5). Entry: SH-E-747ee5be. A lead for a capability, if another platform gives 3D Secure a place of its own.
- **C46.5:** a maker statement for a retired app doesn't pass to the app that replaces it: 'The original Barcode Printer app, created by Shopify' names the retired app's maker only, and 'the new Retail Barcode Labels app', with no maker held, is `shows` (rule 13). Entry: SH-E-a5195d34.

## New things

- **`new:Quantity rules`** (the Editions' name, SH-50; kept by SH-41 and SH-42's SH-E-cc191d02): SH-E-dbcffeff, `shows`, scope Shopify Plus. Its words: 'the minimum order quantity, maximum order quantity, and volume is calculated based on the total quantity of all of the variants for each product', the wholesale channel's pricing requirements. Place of its own: none in this entry, a rule inside the channel's price lists; the Editions' entries decide it. Proposed: domain D, area B2B, parent CM-B2B-003 (catalogs, which hold wholesale prices). No Arabic name held. Searched (`caps --terms`): 'wholesale; volume pricing; minimum order quantity' (only CM-B2B-001, CM-B2B-003 and CM-CAT-010 hold 'wholesale', none a quantity limit) and 'quantity rule; maximum order quantity; volume pricing' (none). Its leads (CM-CAT-002, CM-ACC-004, CM-CAT-013, CM-LOY-008, CM-CHK-010) came by a field's word and none is a quantity limit.
- **`new:Admin languages`** (the digest's name, SH-34; the ruling after SA-49): SH-E-8d8e59b8 (POS app 5.2 for iOS and 3.2 for Android) and SH-E-ff9a1b45 (Shopify app 8.0), `core` (C46.2). Place of its own: none in these posts, an app version's feature; it is decided with the other platforms' language menus. Proposed: as decided for SH-34's line, the admin's interface. No Arabic name held. Searched: 'interface language; admin language; display language' (none). Their leads (CM-APP-002, by the app stores' links; CM-CAT-001, CM-ONB-003, CM-RET-003, CM-CNT-008, CM-MKT-005, CM-SUP-005) aren't an interface language; CM-MKS-008 is the store's languages for its buyers.
- **`new:Tipping`** (the digest's name, SH-35's Tips): SH-E-2d8ad8cf, `core`, beside CM-POS-001: 'Add tipping to the checkout for in-person orders processed with the credit payment method', with tips collected, tracked and refunded. Its support is decided with SH-35's `shows` and SH-41's `core` (the digest, section 4). Place of its own: none in this post. Proposed: domain C, parent CM-POS-001. Searched: 'tipping; gratuity; tip' (none). Its leads (CM-PAY-021, CM-POS-001, CM-TAX-009, CM-PAY-022, CM-CHK-009) aren't tipping.

## Entries I couldn't tell, and what would settle each

1. **SH-E-9856c63d and SH-E-a5195d34, the Retail Barcode Labels app** (CM-CAT-015 `shows`, the cell's first lines): “You've been asking for it, and we heard you loud and clear. Introducing a new way to assign and print barcode labels” names no app (its link opens the app's help page, digest rule 7), and 'we heard you' names no maker; `makers` holds none. If the coordinator reads 'Introducing' after 'we heard you' as Shopify shipping it (the ruling after SH-35), both lines become `own-service`.
2. **SH-E-5a2bdb81, Shopify Pay without an SMS** (CM-PAY-014 `core;own-service`): `core` for the store's checkout (C45.3), `own-service` for 'the new pay.shopify.com landing page', read as Shop Pay's own site apart from the store (digest rule 17; SH-S-0411, SH-S-0413). If that page counts as inside the checkout, the line is `core` only.
3. **CM-MKT-010 gains `core`** (SH-E-34389903, SH-E-ff9a1b45, SH-E-c8bc4e01): the admin's own ad tools, Facebook dynamic ads set up in the marketing section, ad campaigns from the Shopify app's Marketing tab, and 'our first Shopify-built marketing tools for advertising on Google and Facebook' in the Marketing section. The cell's reading puts Shopify's own advertising tools in CM-MKT-011 (Audiences) and CM-MKT-012 (Shop Campaigns), which these aren't. 'Shopify-built' names Shopify their maker, but they are tools of the admin's Marketing section, not a separate product (the correction on Shopify Balance), so `core`.
4. **SH-E-78436754, the Share on Facebook button retired** (CM-MKT-005 `shows;extension-point`): no capability holds the merchant's own posts to social networks. CM-MKT-005 holds marketing activities and the App Store's Marketing apps, which the post links (social media marketing); CM-SFR-016 is the storefront's share buttons for buyers. A capability for social posting would settle it.
5. **SH-E-32ab9331, Postmates removed** (CM-SHP-008 `shows;extension-point`): the App Store search the post links is 'local delivery'. An on-demand courier delivers for the store; if CM-SHP-008 stays the store's own delivery only, CM-SHP-006 (local pickup and local delivery) is the other place.
6. **SH-E-dd57261c, Fraud Protect** (CM-PAY-010 `shows`, United States): 'currently available only to select merchants' (digest rule 29). That Fraud Protect is Shopify Protect's forerunner is a reading: both protect eligible Shopify Payments orders against fraudulent chargebacks, and no held statement joins them.
7. **SH-E-f9ebb4dd's first lead, CM-MKT-023** (product recommendations, which holds nothing): 'use their order history to make personalized product recommendations' is a use staff make of a customer's profile in POS (digest rule 6), not the platform's or the merchant's curated recommendations: no line.
8. **Lines that rest on rule 5 or C44.2, which the coordinator may judge named in passing:** SH-E-ef21b30b's CM-ORD-001 (the order details page shows POS receipt numbers) beside CM-ORD-009 and CM-POS-001; SH-E-7adceca7's CM-ORD-001 (orders reach the admin later, with a banner on the orders list); SH-E-10713924's CM-SHP-002 (packing slips printed with labels bought in bulk); SH-E-3b20c617's CM-ORD-001 (orders assigned to locations); SH-E-84aa1409's CM-APP-001 and CM-MKT-005 (the Apps page and the Marketing page the Google Shopping app's features moved to).
9. **Kept in `reading`, not a line:** the delay to order confirmation emails during high volume (SH-E-7adceca7, CM-NTF-001); 'Plus stores will get this feature as a part of the next checkout upgrade' (SH-E-06db618f, SH-E-8807a82a: the same thing, later); the merchant's custom checkout translations updated to match renamed card fields (SH-E-39d85613, CM-MKS-008); the Tap, Chip, and Swipe reader the store uses (SH-E-345a22e5).
10. **The Buy Button channel** is `own-service` by C45.2 (SH-E-39b19e37, SH-E-2e0b3cfe). Earlier batches' lines on the Help Center's answers placed 'Buy Button sales channel' `core` on CM-CHN-001 (SH-E-737a2561, SH-E-728858eb, SH-E-f35bf9c2); the corrections after SH-45 keep only the pricing pages' rows `core`, so those lines may need aligning.

## What a source states that no entry holds

Nothing read: I opened no post's page or run step.

## Problems with the brief or the script

- `earlier` found no key in these posts, as the coordinator expected; one grep of the earlier placements per chunk found every precedent.
- The checker's note 'core on a product named with the platform's brand' fires on the platform's own surfaces named with its brand (Shopify POS, Shopify Shipping, Shopify Payments, the Shopify Themes Store and App Store, Shopify Plus stores, the Shopify app, Shopify Capital, Shopify Community): each is `core` by digest rule 8, rule 9 or the table; so are the Customer View app (part of POS, the table), Shopify Pay in the store's checkout (C45.3) and the Plus wholesale channel (C46.1).

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 86 of 86 entries, no problem. With this batch the changelog is placed whole (SH-34 to SH-46, 1,646 posts).
- **CM-MKT-010's `core` stands.** The cell is 'Advertising on ad platforms', and its Salla side is the platform's own product for making ad campaigns (Salla Ads). The admin's own tools for advertising on Google and Facebook ('our first Shopify-built marketing tools'), and ads made from the admin or the Shopify app, are that thing, built in. CM-MKT-011 (Audiences) and CM-MKT-012 (Shop Campaigns) are other things.
- **The other `CHANGES` stand,** each on the digest's rules and the corrections after SH-45:
  - Flow `own-service`, its connectors' apps `extension-point`;
  - the Buy Button's and the Google app's features `own-service`;
  - the cost API and the shipping apps reading customs data `extension-point`;
  - the Retail Barcode Labels app `shows`, with no maker held. 'Introducing a new way …' in the platform's voice isn't a maker statement (the ruling after SH-43), and C46.5 holds.
- **The Buy Button's plan rows** (SH-E-737a2561, SH-E-728858eb, SH-E-f35bf9c2) stay `core`, as plan lines (the corrections after SH-45).
- **The rules C46.1 to C46.5 stand** and join the digest's section 6.
- **The new things** keep their names: Quantity rules, Admin languages and Tipping. Their supports are decided with each thing.
- **Cost:** 17.2 million tokens over 75 requests, about 200,000 an entry. The context reached about 397,000 tokens.
