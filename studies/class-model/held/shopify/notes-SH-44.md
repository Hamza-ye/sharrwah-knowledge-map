# SH-44: notes

**Batch:** Shopify, `merchant-changelog`, 130 posts from June 11, 2021 back to June 19, 2020 (`SH-E-866d4b86` to `SH-E-da2a321a`), effort `high`. Every entry is one post of `structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl` (observed-sh at `e38dc17e3`). Four of the posts carry a type tag (Changed, Feature, Improvement twice); the rest have none, so their readings begin with the date alone (digest, rule 3).

**What I read:** the brief; the digest `held/rules/merchant-changelog.md`, whole, its section 6 included; the last section of `held/review-H-rulings.md`; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, and the structure's rows in `structures/REGISTER.tsv` and `held/selection.tsv`; the evidence map; B-extent's "Cells and evidence" and "Conventions from the dry run"; the structure's `--meta`. Of the earlier batches' notes, only the lines the digest sent me to, by `grep`: `notes-SH-42.md` for C42.1, C42.5, C42.7, C42.8 and C42.9, and `notes-SH-43.md` for Oberlo, C43.7 and C43.8. `earlier` found no earlier line on any key of these posts, and no twin. So for precedents of the same kind of post I searched the earlier placements files by phrase: the Shopify mobile app, card readers, Shop's app, Geolocation, the Store Importer, backup rates, PayPal, CAPTCHA, checkout.liquid, transit times, Launchpad, Scripts, order tags and YouTube media. Each line I followed is named in the reading that keeps to it. I read no post's page: each post's own text left no column open, and none of its links is a page this pass reads.

**Placements:** 205 lines for 130 entries. 125 entries take capability lines only, 2 take a `new` line only, and 3 are `out`. By support: `core` 146, `own-service` 35, `extension-point` 11, `shows` 6, `core;own-service` 2, `core;extension-point` 2.

## New things

1. **Planet** (`SH-E-fa9039af`), `core;own-service`, under the name SH-43 gave this thing. November 13, 2020, 'Carbon-neutral BFCM shopping':
   - `core`: 'Shopify is paying to offset all carbon emissions from the delivery of every single order placed on our platform during the BFCM weekend', 'at no cost to you'. The platform does it itself, and 'This initiative ends after BFCM' (C44.3).
   - `own-service`: 'Shopify always offsets the carbon emissions of all orders made with Shop Pay' (its link Shop's help, rule 17). And 'the Offset app', whose maker a held post names: SH-E-39234b62's title, 'Offset your store's shipping emissions with Offset (by Shopify)!' (`makers`).
   - **A reading:** the Offset app and Shop Pay's offsets are the same thing as the Planet app's carbon-neutral shipping, which offsets or removes the emissions of the store's deliveries. So I named them `new:Planet`, as the brief has entries of one new thing named alike. The coordinator may prefer a name for the capability rather than the app, such as "Carbon-neutral shipping".
   - **Place of its own:** the Offset app's App Store listing (`apps.shopify.com/offset`, the post's link) is a listing, not one of B-extent's kinds. SH-43 named the Planet app's listing and admin page (`apps/planet-1`). The BFCM initiative has none.
   - **Proposed:** domain C, area SHP, parent CM-SHP-001 (shipping and delivery), since what it offsets is the store's deliveries (a reading).
   - **Names:** Offset, Planet. No Arabic name is held, since the admin in Arabic isn't captured (`docs/GAPS.md`).
   - **Searched:** `carbon; emissions; sustainability; offset` (caps: none).
   - **The checker refuses two lines on one new thing for one entry,** so the two supports share one line.
2. **Rich text editor** (`SH-E-1c4f7a67`), `shows`. September 29, 2020: “We've made improvements to the rich text editor for Blogs posts, Pages, Products and Collections”, with a color picker for RGB/HEX codes.
   - **Place of its own:** none. It is a field inside the editing pages of products, collections, pages and blog posts, so `shows` (the brief's `new`). Its help page sits under `shopify-admin/productivity-tools/rich-text-editor`, beside bulk actions and file uploads.
   - **Proposed:** domain E, area CNT, with no parent. Or no capability at all: the coordinator may read the post as changing those four records' text, and give it lines on CM-CAT-001, CM-CAT-003, CM-CNT-003 and CM-CNT-004 instead. I left those four out because the digest's rule 6 gives no line to a list of places.
   - **Searched:** `rich text editor; text editor; WYSIWYG; content editor; description editor; text formatting; color picker; product description`. The only hit was CM-AIA-003 (AI content generation), which isn't this. The held lines on "Rich text" are a metafield type (CM-CNT-002) and a theme editor setting (CM-SFR-002).

## Rules I followed that the digest doesn't state (for the coordinator)

- **C44.1:** a feature a first-party app opens to one of its own plans takes `own-service`, the app's plan as its scope.
  - The case is `SH-E-fd0a444a`: 'The variant mapping feature is now available on the Explorer Oberlo plan'.
  - The app's plan is the separate product's own offer. C43.10's `core` is for the platform's own plans that include an app (Flow on Shopify's plans).
- **C44.2:** a page a post's new action or view appears on takes a `core` line on that page's capability. I read rule 5's "each list page it changes" as each page it changes.
  - The pages: the customer page (`SH-E-28464afb`, CM-CUS-001); the product details page (`SH-E-3f21b808` and `SH-E-d81abd04`, CM-CAT-001); the Orders page (`SH-E-0e555755`, CM-ORD-001); the orders list (`SH-E-721a5733` and `SH-E-5dc59886`, CM-ORD-001); and the gift card issue page (`SH-E-da2a321a`, CM-LOY-002).
  - If rule 5 is for list pages only, the lines on the customer page and the product details page go. Each is `core` on a cell that is already `core`, so no cell changes either way.
- **C44.3:** a time-limited initiative that the platform runs itself for every store is `core` while it lasts, its end in `reading`. The case is the BFCM weekend's carbon offsets (`SH-E-fa9039af`).
- **C44.4:** a public page of the platform's own figures across all its stores is `out`. It is not something merchants, buyers, partners or developers use in a store. The case is the BFCM Live Map (`SH-E-4472e2ad`): sales and orders per minute across 'more than 1 million independent businesses powered by Shopify'. It is not the store's own Live View (CM-ANL-004).
- **C44.5:** the organization admin's own address is its frame and takes no line, as C42.5 reads admin.shopify.com. The post is `out` where it names nothing else. The case is `SH-E-a3d9c4ef`: the Shopify.Plus URL now carries the organization's name.
- **C44.6:** an identity provider the platform's sign-in integrates with takes `extension-point` on CM-TRU-001, the providers named as its fillers, beside the platform's own SAML (`core`).
  - The case is `SH-E-0a013352`: 'First-party integrations are available for Okta and Azure Active Directory'.
  - 'First-party' names who built the integration, which is a means. It is not a separate product that signs users in, so no `own-service` (rule 14).
- **C44.7:** users added and removed through SCIM by an identity provider take CM-STF-001 `core;extension-point`, beside the platform's SCIM on CM-TRU-001 `core`. This is C42.9 for users rather than roles. The case is `SH-E-55ea61f3`; no provider is named, so no filler.

Rule applications the digest covers, named so they can be checked:
- **App Store collections:** a new App Store collection that 'we' introduce is CM-APP-002 `core` (rule 8), beside the apps' own capability as `extension-point`. The cases are post-purchase upsells (`SH-E-b68bec1a`: CM-MKT-021 and CM-CHK-004) and subscriptions (`SH-E-b579c03f`: CM-SEL-001).
- **A theme editor section a third party ended:** the Instagram feed section stopped when 'Instagram has discontinued its legacy API', with apps named as the way. The line supports the replacement, apps adding the feed to the storefront: CM-SFR-005 `extension-point` (rules 30, 31 and 33; C43.1). The case is `SH-E-ba9af7cc`.
- **New POS permissions with manager approval:** the access level Approval required is over permissions themselves, so it takes CM-STF-002. Each permission named takes a line on what it gates (rule 46; C43.9): CM-POS-001 for ship to customer and custom sales, CM-MKT-001, CM-TAX-001, CM-RET-002 and CM-RET-003. The case is `SH-E-b81a9e8f`.
- **Bulk action lists on mobile:** each action takes its own capability (rule 5). The cases are `SH-E-40429011` (CM-ORD-009, CM-ORD-011 and CM-APP-008) and `SH-E-1d43f378` (CM-SHP-009, CM-PAY-020, and CM-SHP-002 under its own countries).
- **Address form changes by country:** each change takes its own CM-CUS-008 line with its countries, and CM-CHK-001 takes their union (rules 24 and 42). The case is `SH-E-855cff2e`.

## Makers settled by `makers` that the digest's table lacks

- **Own-service:**
  - Oberlo: SH-E-945c828e, SH-43's line;
  - Offset: SH-E-39234b62, 'Offset (by Shopify)';
  - Shopify Ping: SH-E-7da656d8, “We've released the Android version of Shopify Ping”;
  - Shopify Chat: SH-E-48a67270 and SH-E-5bf6fdbc, 'Today we released SMS support in Shopify Chat';
  - Launchpad: SH-E-bd544a27, “We’ve made creating discount events in Shopify Launchpad easier!”. I kept the earlier batches' capability for it, CM-MKS-002 (SH-E-8f59733c's line);
  - the Shopify Local Delivery app: SH-E-bddc1876, 'we built tools', the post itself.
- **None held,** so `shows` (rule 13):
  - the Theme Kit Access app;
  - the Shipping Manifests app;
  - the Store Importer app (C43.5).

## Entries I couldn't tell, and what would settle each

- **`SH-E-a3d9c4ef`** (organization admin URLs): `out` by C44.5. If the coordinator reads the post as naming the organization admin as a feature, it takes CM-ACC-003 `core`, the cell whose reading cites the organization admin.
- **`SH-E-4472e2ad`** (BFCM Live Map): `out` by C44.4. The other reading is `shows` on CM-ANL-004, if a public page of platform-wide figures counts as live analytics for merchants.
- **`SH-E-1c4f7a67`** (rich text editor): new thing 2 above. The alternatives are lines on the four records' capabilities, or `out` as the admin's own tooling.
- **`SH-E-1d43f378`:** the list of bulk order actions reads 'Archive products' and 'Unarchive products'. I kept them in the CM-ORD-001 line, as order actions. The post's page or the help page it links (`fulfill-your-own#fulfill-multiple-orders-at-the-same-time`) would settle whether orders or products are meant. If products, they take CM-CAT-001 (product statuses, as `SH-E-5192577b`).
- **`SH-E-137fad08`** (China, Italy and South Korea): I placed the 'additional field in the checkout' on CM-CUS-008 and CM-CHK-001 by rule 42, its uses ('customs, shipping labels, or invoices') being a list (rule 6).
  - The post doesn't say the field is in the address form. The help page it links (`understanding-shipping-labels#international-considerations`) would settle it.
  - If the field isn't an address field, the line is CM-CHK-001 alone, perhaps with CM-SHP-020 for customs. `SH-E-72b8d9b9` (Brazil's CPF/CNPJ) names a tax ID, so it takes CM-TAX-005 by rule 40.
- **`SH-E-1b2dc5f9`** (app developers issue app refunds): CM-APP-003 `extension-point`. The developers do the refund through the platform's app billing, which the help link (`your-invoice/apps#request-an-app-refund-or-credit`) names. If the coordinator reads it as the platform's own billing gaining a feature, it is `core`, and the cell changes nothing.
- **`SH-E-3f21b808`** (open the original AliExpress product page): the post names no app, so I read the action as the admin's own. That gives CM-CAT-010 `core`, which changes its cell, with AliExpress, the marketplace the product came from, as its filler.
  - Whether the action comes from Oberlo is not stated. If it does, the line is `own-service` on Oberlo's maker statement.
  - If AliExpress is read as named with no role, the filler goes (rule 51).
- **`SH-E-5abc763e`** (Theme Kit Access): CM-SFR-002 `shows`, as the cell reads the Theme Access app, and a second line on CM-STF-005 `shows` for the access granted to 'developer partners'. The second line could go if theme-only access is read as CM-SFR-002's alone.
- **`SH-E-866d4b86`** (Shop Pay Installments in the Shop App): CM-PAY-015 `own-service`, since Shop provides the buyer's management of their instalments (rule 14), and CM-CHN-002 `own-service`. If managing instalments in Shop is read as Shop's channel only, the CM-PAY-015 line goes, and its `own-service` with it.
- **`SH-E-083d7c50`** (POS analytics reports): the 'Staff report to see top-performing staff by net sales' reads staff attribution. I gave it no `new:Staff sales attribution` line, since it credits no sale.
- **`SH-E-bddc1876`** (local delivery and the Shopify Local Delivery app): I read the post as the app's launch, which gives it CM-APP-011 `own-service` (C42.6). If it isn't the launch, that line goes (rule 15).
- **`SH-E-e04031b0`** (reCAPTCHA v3 on contact forms and blog comments): CM-CUS-012 by the digest's rule 42 ('the storefront's CAPTCHA'), as SH-E-a275a8ff's line reads it on the storefront's protected forms. That cell's name and note are about sign-in and registration only, so the coordinator may want its name widened.
- **`SH-E-d38d6bba`** (Vimeo-hosted product videos): no filler, as SH-E-be338d5c's line holds YouTube Shorts. If the video's host counts as doing the media, Vimeo is the filler, and so is YouTube on that line.
- **The two speed report posts** (`SH-E-ee3c12d4`, `SH-E-85bec81d`): CM-ANL-002, as a kind of report (its note), since no capability holds storefront speed. Only the second names Google Lighthouse, which is its filler.

## The CHANGES lines, and what I decided

Each was read again against its post.

| Line | Change | Decision |
| --- | --- | --- |
| 33 | CM-ANL-001 gains `own-service` | Shop's metrics on its own channel (C42.7). Kept. |
| 4 | CM-APP-003 gains `extension-point` | App developers' refunds; see above. Kept. |
| 70 and on | CM-AUT-001 gains `own-service` (12 lines) | Flow's features, on the digest's maker statements. Kept. |
| 35 | CM-CAT-010 gains `core` | The admin's own action to the AliExpress page; see above. Kept, with doubt. |
| 5, 30, 69 | CM-CAT-010 gains `own-service` | Oberlo's features, on SH-E-945c828e. Kept. |
| 60, 196 | CM-CUS-012 gains `core` and becomes held | reCAPTCHA at customer login, and on contact forms and blog comments (rule 42). Kept. |
| 189 | CM-DVT-004 gains `core` | 'all newly created development stores will be password protected': the platform's own development stores. Kept. |
| 132, 155 | CM-MKS-002 gains `own-service` | Launchpad, as earlier batches placed it. Kept. |
| 31, 56 | CM-MKS-004 gains `own-service` | The Geolocation app, on the platform's possessive (the check after SH-43). Kept. |
| 28 | CM-MKS-009 gains `core` and becomes held | The UK's constituent countries in shipping zones (rule 38; C42.8). Kept. |
| 75 | CM-MKT-003 gains `core` and becomes held | Automatic discounts on POS (rule 43). Kept. |
| 54 | CM-MKT-007 gains `own-service` | Shopify Email's editor, on its maker statements. Kept. |
| 112, 173 | CM-MKT-023 gains `core` and `extension-point`, and becomes held | Shopify-powered recommendations in POS Pro (rule 43), and the earlier recommendations by app partners' POS extensions. Kept. |
| 65 | CM-ORD-011 gains `core` and becomes held | Tags added to and removed from orders in bulk, as SH-E-d9b7f517 reads draft orders' tags. Kept. |
| 2 | CM-PAY-015 gains `own-service` | Instalments managed in the Shop App; see above. Kept, with doubt. |
| 160 | CM-PAY-032 gains `core` and becomes held | 'checkout links for draft orders' shared by SMS, 'making it easier for you to collect payments': a link to pay. The cell's reading lacked one. Kept. |
| 192 | CM-SHP-008 gains `own-service` | The Shopify Local Delivery app, 'we built tools'. Kept. |
| 11 | CM-SHP-012 gains `own-service` | The Fulfillment Network (the digest's table). Kept. |
| 137 | CM-SHP-017 gains `own-service` | Tracking through the Shop app, which Shop provides. Kept. |
| 151 | CM-STF-001 gains `extension-point` | SCIM users from an identity provider (C44.7). Kept. |
| 204 | CM-TRU-001 gains `extension-point` | Okta and Azure Active Directory through SAML (C44.6). Kept. |

The checker's other NOTEs I read again:
- Eighteen lines name a product with the platform's brand as `core`. Each is the platform's own (rule 8): the Shopify App Store (3), Shopify Payments (3), Shopify POS (5), Shopify Checkout (2), the Shopify Mobile app (2), the Shopify Theme Store and the Shopify Plus organization admin. The eighteenth is the Shopify Local Delivery app's line, whose `core` rests on local delivery set up at checkout and its `own-service` on the app.
- Its first lead holds nothing on Shopify for five lines. Three are CM-OPS-004, WooCommerce's system status report (`SH-E-696538bd`, `SH-E-f2a9be20`, `SH-E-1b3e9d14`). Two are CM-MKS-009, reference lists of countries (`SH-E-183f6d18`, `SH-E-72b8d9b9`). Neither is those posts' thing, and each line's reading says so.
- The two new things' leads: I read their cells, and none is the thing.

## What no entry holds, and the structure

I read no source beyond the entries, so I have no lead for the second stage from a source's other text. No item disagreed with what I read of it.

## Problems with the brief or the script

- **`check`** refuses two lines on one new thing for an entry, even with different supports. The brief's rule allows a second line on one capability, under its own condition. So a new thing with two supports takes one line, `core;own-service` (`SH-E-fa9039af`).
- **`check`'s NOTE on an empty first lead** stays after the line's reading sets the lead aside, since it reads only the lines' `cap_id`. It costs nothing, but it repeats on every run.
- **`earlier`** found nothing for this batch's posts: no key cited, no twin. For these older posts the precedents are posts of the same kind, which only a search of the placements by phrase finds.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 130 of 130 entries, no problem.
- **The `CHANGES` stand,** each on the digest's table, its rules or a maker statement `makers` found. The new makers join the digest's table:
  - **`own-service`:** Oberlo, Offset ('Offset (by Shopify)', read as Planet's forerunner and kept under SH-43's name, Planet), Shopify Ping, Shopify Chat, Launchpad and the Local Delivery app;
  - **`shows`** (no maker held): the Theme Kit Access, Shipping Manifests and Store Importer apps.

  The two kept with doubt stay as placed. The admin's own AliExpress action is `core`, naming no app. Shop Pay Installments managed in the Shop app is `own-service`, as Shop's things are.
- **The new things:**
  - Planet's two supports share one line: the BFCM offsets Shopify paid for are `core` while they last, and the Offset app is `own-service`.
  - Rich text editor is `shows`, with no place of its own, as the brief writes such a thing.
- **For the amendment:** CM-CUS-012 is 'reCAPTCHA verification at buyers' sign-in and registration'. Shopify's one reCAPTCHA setting also covers the storefront's contact and comment forms, which rule 42's lines place there. The cell's definition may widen.
- **The rules C44.1 to C44.7 stand** and join the digest's section 6.
- **Cost:** 30.2 million tokens over 107 requests, about 232,000 an entry. The context reached about 511,000 tokens: `earlier` finds no keys in these older posts, so the agent searched by phrase.
