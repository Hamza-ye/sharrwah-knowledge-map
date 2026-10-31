# SH-43: notes

**Batch:** Shopify, `merchant-changelog`, 130 posts from July 06, 2022 back to June 15, 2021 (`SH-E-d9089fea` to `SH-E-5e0c439f`), effort `high`. Every entry is one post of `structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl` (observed-sh at `e38dc17e3`). The 34 posts from 2021 have no type tag, so their readings begin with the date alone (digest, rule 3).

**What I read:** the brief; the digest `held/rules/merchant-changelog.md`, whole, its section 6 included; the last section of `held/review-H-rulings.md`; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md` and its register row; the evidence map; B-extent's "Cells and evidence" and "Conventions from the dry run"; the structure's selection row and `--meta`. Of the earlier batches' notes, only the two cases behind the digest's rule 31: `notes-SH-38.md`, lines 39 and 40, and `notes-SH-40.md`, lines 33 and 34. I aligned with earlier batches' placements by `earlier` and by grepping their placement files for the same kind of post (Shopify Payments for POS by country, Shopify Shipping by country, local methods, Flow's plan lines, Saved views, free themes, the bulk editor, the mobile app, tax liability insights).

**Placements:** 190 lines for 130 entries. 127 entries take capability lines only, 3 also take a `new` line, and none is `out`. By support: `core` 137, `own-service` 34, `extension-point` 10, `shows` 7, `core;extension-point` 2.

## New things

1. **Try before you buy** (`SH-E-75f13f01`), `shows`. June 21, 2022: 'try before you buy apps are now integrated with Shopify Checkout', installed from the App Store category the post links (`apps.shopify.com/categories/merchandising-purchase-options`).
   - **Place of its own:** none held. The held App Store taxonomy (`structures/shopify/app-store-taxonomy/apps.shopify.com_categories/`, `menu.jsonl` and `pages.jsonl`) has no try-before-you-buy or purchase-options category. Today's Pre-orders category sits under Upsell and bundles. So the line is `shows` (the brief's `new`). The apps' role would be `extension-point` if a capability is made.
   - **Proposed:** domain SEL (B), beside CM-SEL-005 (Pre-orders), which the same post's other line takes. Another possible home is CM-SEL-001 (subscriptions and selling plans) if purchase options are read as selling plans; the post doesn't say so.
   - **Name:** "try before you buy". No Arabic name is held (the admin in Arabic isn't captured).
   - **Searched:** `try before; trial period; deferred payment; pay later; purchase option; selling plan`. The only hit was CM-PAY-015 (instalments and buy now, pay later: "the buyer pays for an order later"). That is financing, not a trial before purchase, so I didn't use it.
2. **Planet** (`SH-E-41c88730`), `own-service`, under the digest's name: “we're releasing the Planet app”. It has a place of its own: the app's App Store listing (`apps.shopify.com/planet`) and its admin page (`apps/planet-1`, SH-E-1a4f382c's line). The same post takes CM-APP-011 (C42.6).
3. **Saved views** (`SH-E-ff74c33a`), `shows`, under SH-35's name, as SH-E-c79d0322's and SH-E-9c2e557d's lines have it: 'save your column arrangements within each order view'. The orders list itself takes CM-ORD-001.

## Rules I followed that the digest doesn't state (for the coordinator)

- **C43.1:** a customer notification option retired, with third-party apps named as the way to keep it (SH-E-920d26f3, SMS shipping notifications).
  - The platform's changed notification is `core` on CM-NTF-001, with the retired option ('SMS or Email') in `reading` (rule 30).
  - The SMS partners' apps are `extension-point` on CM-NTF-004, message delivery by SMS through communication apps (rule 31's pattern).
- **C43.2:** a refund paid as a gift card (SH-E-ae26b891) is `core` on CM-LOY-002 and `shows` on CM-RET-002. CM-RET-002's note does the same for a refund to store credit (core on CM-LOY-001, shows here).
- **C43.3:** Handshake's posts (SH-E-ecfff693, SH-E-db352cbb, SH-E-f72e3a23, SH-E-a07c488b). No maker statement is held (`makers`: none), so each is `core` by what the post shows, the maker a gap, with no filler: a named company that no held statement places in or out of the group isn't a third party for that reason.
  - The suppliers' side is CM-B2B-001, as its note reads Salla's wholesale market.
  - The retailers' side is CM-CAT-010, where CM-B2B-001's note puts Salla's buying side.
  - Product information made only for Handshake is CM-CHN-004.
  - Its automatic discounts are CM-MKT-003 (rule 43).
  - Shopify's help centre files Handshake under `online-sales-channels/wholesale/handshake` (the posts' links).
- **C43.4:** a feature stated as available only 'on some stores', with no reason given (SH-E-301ede63, PayPal Express for subscriptions), is `shows` (rule 29). The words go in `reading`, not in `scope` (rule 22, as with 'eligible merchants').
- **C43.5:** an app the post names in the App Store, with no maker held, that does the post's thing, is `core` by what the post shows, the maker a gap. The cases are the Store Importer app (SH-E-b1ede873), the Customer Privacy app (SH-E-4021ea27) and the Geolocation app (SH-E-d449ad6a). This extends rule 13 and the brief's catalog-card rule to apps not named with Shopify's brand.
- **C43.6:** third-party financial apps that reach the merchant's Balance account through a connection the platform offers by a partner (SH-E-c6505fda: 'through our partnership with Plaid', Venmo and Wise) take one line, CM-PAY-023 `core;extension-point`. The partner and the apps are the fillers. This extends the check after SH-42 (QuickBooks syncing through the platform's sign-in).
- **C43.7:** a free theme's launch or a version of one (Colorblock and Ride; Taste and Studio; Sense, Craft and Crave; Dawn; Dawn 2.1.0; Dawn 3.0.0) is CM-SFR-001 `core` (the ruling after SH-53). Its theme settings and sections are listed in passing (rule 6). Support for app blocks in a theme section is CM-SFR-004 `extension-point` (SH-E-659467fc).
- **C43.8:** card networks that Shopify Payments starts taking in a country (SH-E-f7c99683: Discover and Diners Club in the United Kingdom) are CM-PAY-002 `core`, the networks its fillers, as rule 35 has for POS. A local card scheme (Cartes Bancaires, SH-E-8758dc6f) is CM-PAY-017 (C42.1), as SH-42 placed Bancontact.
- **C43.9:** a post of new staff permissions that names only some of the tasks they delegate (SH-E-79bfcd63: 'responding to GDPR requests and enabling private apps') gives each named permission a `core` line on what it gates (CM-TRU-007, CM-APP-009). The 'newly categorized sensitive permissions', a category over permissions themselves, go on CM-STF-002 (rule 46). The other nine permissions aren't named, so they take no line. SH-E-2c111db8 (per-app and app-charge permissions) is read the same way: CM-APP-001 and CM-APP-003.
- **C43.10:** a post making Flow available on more plans (SH-E-870e830c, SH-E-6fbb7205) is a plan line, `core`, as SH-41's SH-E-2bff15c9 and SH-50's SH-E-10b07c1b are. Flow's own features are `own-service` (the digest's table).

## Entries I couldn't fully tell, and what would settle each

- **SH-E-d449ad6a**, Geolocation: “Shopify's Geolocation app”. `makers` finds no maker's cue, so I placed it `core`, the maker a gap (C43.5). If the coordinator reads the possessive as a maker statement (like 'from Shopify', rule 10), the line becomes `own-service`.
- **The Handshake posts** (C43.3): a held statement naming Handshake's owner would settle them. If Shopify owns it, they become `own-service`, possibly on CM-CHN-002, the platform's own marketplace. If a third party owns it, they become `extension-point` or `outside`.
- **SH-E-920d26f3:** the place of the admin's 'Customer Contact Method section' is open; the post doesn't name it. The help centre's `manual/checkout-settings/checkout-form-options.md` (help-center structure, `help.shopify.com@en-ar/md/en/`) names customer contact method among the checkout settings, a lead for a CM-CHK-001 line. Reading that page is beyond the entry's sources.
- **SH-E-fabd8e90**, order archiving 'in your Order Processing settings': I placed it on CM-ORD-001 only. CM-ORD-010's Shopify cell cites the help section 'Set up order processing and archiving' as `shows`, but CM-ORD-010's thing is receiving orders, not archiving them. The coordinator may decide whether Shopify's Order processing settings belong to CM-ORD-010.
- **SH-E-c35bf309**, the Twitter sales channel: `extension-point`, Twitter the filler, by analogy with the digest's Google & YouTube app row. No maker statement is held (`makers`: none).
- **SH-E-dc73c4db**, Google local inventory sync: `extension-point` on CM-CHN-004 and CM-CHN-001, Google the venue. Its twin label, SH-50's SH-E-1f273f67, is `shows`, because the Edition's highlight names the feature by brand only. This post names 'the Shopify Google channel', which the digest's table reads as the channel app's `extension-point`.
- **SH-E-2ee1a831**, Shopify Protect: `shows`. The title says 'early access' and the text 'eligible US merchants' (rule 29). If the coordinator reads 'We’ve just released … to eligible US merchants' as a release, the line becomes `core`, scope US.
- **SH-E-516a5bee**, unique SKUs: I placed it on CM-INV-001, since the post sets SKUs 'in your inventory' and shows the warning on the 'inventory card'. CM-CAT-002 (variants) is the alternative.
- **SH-E-301ede63**, PayPal Express: CM-PAY-011 (third-party providers: PayPal), not CM-PAY-012 (wallets), whose terms don't hold PayPal.
- **SH-E-c6505fda** (C43.6): the alternative is `core` alone, Plaid the filler (rule 20).

## The `CHANGES` lines

- **CM-AUT-001 gains `own-service`** (Flow's features, six lines): the digest's table makes Flow's own features `own-service`. Its plan lines stay `core` (C43.10).
- **CM-MKT-007 gains `own-service`:** Shopify Email's features, per the digest's table.
- **CM-MKT-011 gains `own-service`:** SH-E-f2d95634 says 'Shopify Audiences is an app built by Shopify', a maker statement in the entry itself (the digest's table).
- **CM-SHP-012 gains `own-service`:** the Fulfillment Network, per the digest's table (E16, SH-51).
- **CM-ANL-001 gains `own-service`:** Inbox's conversation metrics (C42.7).
- **CM-CAT-010 gains `own-service`:** Oberlo, “we've added the new Replace order item feature … on all Oberlo plans” (rule 10). `makers` holds no other statement.
- **CM-CAT-010 gains `core`, and CM-MKT-003 gains `core` and becomes held:** the Handshake posts (C43.3).
  - CM-MKT-003 holds nothing on Shopify in the merged model. The earlier batches' rule-43 lines aren't amended yet, so it would become held once they are anyway.
- **CM-MIG-005 gains `core`:** the Store Importer app migrating from Lightspeed (C43.5).
- **CM-SHP-020 gains `core`:** the 'customs forms' printed with labels and packing slips (rule 40; rule 5).
- **CM-NTF-004 gains `extension-point`:** the SMS partners' apps (C43.1).
- **CM-PAY-023 gains `extension-point`:** Venmo and Wise through Plaid (C43.6).
- **CM-CUS-007 gains `extension-point`:** consents obtained 'through features enabled by 3rd party apps' (SH-E-f0757c26).

## Leads for the second stage (stated, but by no line of mine)

- **CM-ORD-013,** notes on an order, holds nothing on Shopify. SH-E-0917b3fd states 'order notes are now displayed in the shipping label flow'. That is the data the label flow shows (rule 6), so it takes no line, but it shows that Shopify keeps order notes.
- **First leads set aside after reading their cells:**
  - CM-ORD-003 (order statuses), led by 'processing', 'failed' and 'on hold' in SH-E-510bdd58, SH-E-ec318148 and SH-E-dd2cdf1a: a fulfilment hold is the fulfilment's (CM-SHP-009);
  - CM-APP-010 (app settings), led by 'integration' in SH-E-17d61c89 and SH-E-f768ce89;
  - CM-MKT-023, which is the platform's recommendations on the storefront, not Inbox's product cards (SH-E-84265957).
- **Two posts carry broken links,** the bytes as held: the WisePad 3 links of SH-E-8081c233 (`https://changelog.shopify.com/posts/WisePad%203`) and SH-E-4e2a638f (`WisePad%203`). Neither link is read (rule 7).
- **SH-E-d0858e55** names 'the following regions' with no countries in its text (a '?' stands there). Its link is to Shopify Payments' supported countries, so the line has no scope.

## Problems with the brief or the script

- The checker's note 'core on a product named with the platform's brand' fires on 30 lines that rest on the admin's own services: Shopify Payments, Shopify Shipping, Shopify Balance, Shopify Markets, Shopify POS, Flow's plan lines. Each is `core` by the digest's rules 8, 9 and 11, or by the corrections.
- No other problem.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 130 of 130 entries, no problem.
- **A ruling from this batch** (the ruling after SH-43): an app or a separate product with no maker statement held is `shows` on its feature's capability, the maker a gap, whatever its name. B-extent's `shows` is what such a statement supports: it shows the platform has the capability and supports no placement. The admin's page, route or section for it, and a plan line that includes it, stay `core`.
  - So C43.3 (Handshake) and C43.5 (the Store Importer and Customer Privacy apps) are `shows`, and their eight lines are aligned.
  - The `CHANGES` they raised on CM-MIG-005, CM-CAT-010 and CM-MKT-003 fall away. CM-MKT-003 becomes held from the Editions' lines anyway.
- **The Geolocation app is `own-service`:** two held posts say 'Shopify's Geolocation app', and the platform's possessive names it as the provider, as SH-70's rule 4 reads 'Shopify's flexible iPad stand'. Line 180 is aligned. `makers` now counts the possessive as a cue.
- **The other `CHANGES` stand,** each on the digest's table or rules:
  - Flow, Shopify Email, Audiences, the Fulfillment Network and Oberlo are `own-service` ('we've added … on all Oberlo plans').
  - The customs forms are CM-SHP-020.
  - The SMS partners, the financial apps through Plaid and third parties' consents are `extension-point`.
- **The rules C43.1 to C43.10 stand,** with C43.3 and C43.5 as the ruling restates them, and join the digest's section 6.
- **The open cases stay as placed:** the Customer Contact Method section, order archiving, Shopify Protect's early access, the Twitter channel and the SKU warning.
- **Cost:** 22.4 million tokens over 96 requests, about 172,000 an entry. The context reached about 420,000 tokens.
