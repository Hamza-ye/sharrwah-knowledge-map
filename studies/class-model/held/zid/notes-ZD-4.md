# Held pass, Zid, batch ZD-4: notes

195 entries, all of Zid's `dashboard-route-manifest`: the six routes outside a store that ZD-1 left (email confirmation, the registration's location, complete, details and mobile steps, the one-time login), the store's own route `$lang.stores.$storeId`, and 188 of its child routes (channels, services, catalog, marketing, settings, customers, analytics, finance, support). Evidence at other-product-class@0d79b794f.

**Placed:** 194 entries on capabilities (in 222 lines: 28 entries take two lines), 1 entry `new`, 0 `out`. Every line supports `core`, except entry 107's second line (`extension-point`, CM-SFR-003) and entry 163 (`core;extension-point`, CM-SHP-015). No `own-service`: no entry names Zid's company as a maker. Slot fillers, each named in the route's own path: Jahez (13), Mokafaa (54, 122), Qitaf (144), Nafath (99) and WhatsApp (28, 58, 64, 65, 76, 142, 171), the last as ZD-1 gave it to `services/whatsapp`.

Entry numbers below are the batch's order (`held_entries.py show --batch ZD-4`).

## How I read the entries

A route entry gives only its id, parent, path and index flag. Where the path left the thing unclear, I read, as ZD-1 did:
- the route's item in `zid/structures/dashboard-route-manifest/items.jsonl`, for its `module` and `imports`, which the rendering leaves out (the brief's known case). Readings cite them as "module imports ...";
- the page as a run opened it, through `zid/index/ledger/dashboard-routes.tsv`, cited as "page text <run>#<step>", meaning `zid/raw/runs/<run>/steps/<NNN>.text.txt`. The run labels are ZD-1's (`rest-en`, `gaps-en`, `en-2`, `api-en`), and also:
  - `en`: 20261028T144855Z-dashboard-routes-en;
  - `devstore-markets-en`: 20261028T170107Z-devstore-markets-en;
- for a route that showed only "This feature is unavailable", two strings of `zid/structures/dashboard-locales/items.jsonl`, cited by namespace and key (entries 67 and 80).

Every route was placed one by one (the brief's rule for routes). Where ZD-1 placed the same page (its page-index entry with the same path), I kept to its capability, its second lines and its filler, and say so in the reading ("ZD-1's ...").

**Leads.** No entry of this batch printed a lead. `candidates()` drops an entry's `id`, `path` and `parentId` fields (`values_of`, `ID_FIELDS`), so a route's own words reach no term or name lead, and its tokens matched no cited statement. Every placement here comes from the rule 2 lookups: ZD-1's placements of the same paths, `class_slice.py caps --terms` and the cells (`land_points.py cell`). See "Problems" below.

**Scope.** Only three lines take a scope, entries 67, 80 and 177 (`channels/online-store/settings`, its `location` and `badges`). Each imports `new-zones-feature-guard`, and each opened as "This feature is unavailable". I took the module's name as the condition, as M-11 says for a condition with no name of its own: `new-zones-feature-guard`, marked as a reading. ZD-1's page-index line for the same page (`channels/online-store/settings`) has `showNewZones`, from `source.js`, which isn't this entry's source. The coordinator may want to align the two names.

I left three other gates out of `scope`, since the entry's sources name no condition:
- `use-is-ngo-store`, imported by almost every store route's module;
- `with-feature` and `use-feature-flag`, imported by many;
- the store conditions ZD-1 took from `source.js` (`hasPos or subscription.is_trial` for POS, `customerWallets` for cashback, `mustUseMarketsPricing` for Markets, `not an NGO store`).

Reading what any of them gates would mean tracing the modules, which the brief rules out.

## The new thing

**`new:Similar products`.** Its entry is 75, ZD-E-58ea454e, `catalog/products/:id/similar-products`.
- **What it is:** a product's similar products, which the merchant chooses: the module `products_._id_.similar-products` imports `select-products-dialog`. Not opened (ledger `not opened`), so what the storefront shows of them isn't held.
- **Its place of its own:** an admin route, the manifest's own path.
- **Proposed home:** domain D, area MKT, parent CM-MKT-021 (Upsell and cross-sell offers). The alternatives:
  - CM-MKT-023, product recommendations, but those are the platform's own, chosen by an engine;
  - a part of CM-CAT-001 (the product's page), if the coordinator reads it as one of the product's fields.
- **Names:**
  - English: Similar products (the path);
  - Arabic: not read. The locales would give it, but no entry holds it.
- **Searched** with `class_slice.py caps --terms`: similar products; related products; similar; upsell; cross-sell; recommend; منتجات مشابهة; مشابهة; ذات صلة. The searches found CM-MKT-021 and CM-MKT-023 (and CM-SEL-006 by upsell), and none of them names similar or related products. I read CM-MKT-021's and CM-MKT-023's notes too: MKT-021 rests on app categories only, and MKT-023 is BigCommerce's recommendations engine.

## Entries I couldn't tell, and what would settle each

- **5, `login/otl/:token`.** Placed on CM-TRU-001, keeping to ZD-1's `login/impersonate/:token`. Its page wasn't opened as a route, but the partner dashboard's one-time link to the development store landed on it (`devstore-markets-en`, `actions.jsonl`). It is a sign-in by a one-time token. The alternatives:
  - CM-ACC-001, the account;
  - CM-PTN-002, the partner account, if the coordinator reads the route as the partner's way into a development store.
- **7, `$lang.stores.$storeId`, the store's own route.** A container, the parent of 188 entries of this batch. Its children:
  - `channels`: online store, legal pages, blog, SEO, themes, landing pages, mobile app, marketplaces (connect, Mazeed), POS;
  - `services`: logistics, payments, WhatsApp, financing, growth;
  - `catalog`: products, categories, brands, inventories, custom fields, preorder campaigns;
  - `marketing`, `customers`, `analytics`, `finance`, `support` and `settings`.

  Its title names nothing, so I placed it on the capability whose page its own path opens: the store's home, "Welcome back, Zid Demo Store", with the last 90 days' figures and quick access (page text en#2). That is CM-ANL-003, Overview dashboards. `new:<its title>` is the alternative, but it has no title of its own.
- **13, `connect/settings/jahez-branches`.** A second line on CM-INV-005 (branches), since the module joins Jahez's branches to the store's inventories (`inventories-details-table`). The page opened empty (rest-en#18). The coordinator may read Jahez's branches as Jahez's own, which would leave only CM-CHN-003.
- **32, `services/logistics/settings/bank-account/:id`.** Placed on CM-PAY-029 (cash on delivery), read as the bank account that the shipments' COD settlement pays. The module imports `select-bank` and `ibantools`, and the shipments' transactions page shows a "COD settlement" (rest-en#32). Not opened. Its page, or the logistics settings page that lists it, would settle it. CM-SHP-002 (labels paid through the platform) is the alternative.
- **46, `services/logistics/settings/sender-profile`.** Placed on CM-SHP-002, since its page names the sender details "for shipping labels and contacts" (rest-en#31). CM-SHP-001 is the alternative.
- **64, 142, WhatsApp `store-widget` and `tags`.** Placed on CM-SUP-004 with ZD-1's WhatsApp chat pages. Both pages broke ("Oops! Something broke"). The widget may also be a storefront element (CM-SFR-005). The tags may be customer tags (CM-CUS-002). A run that opens them would settle it.
- **83, `channels/mobile-app/push-notifications`.** Two lines: CM-CHN-006 (the store's app) and CM-MKT-007, because a notification the merchant sends to the app's users is the kind of campaign that MKT-007's Salla term (حملات تسويقية عبر ... إشعارات التطبيق) names. No capability names push notifications to buyers (`caps --terms "push notification"` finds only CM-NTF-002 and CM-SRF-001, the merchant's own app).
- **109, WhatsApp `opt-out`.** Placed on CM-CUS-007, the customers' marketing consent, which names WhatsApp. This changes a cell that holds nothing, and it rests only on the path's word: the page broke (rest-en#72). A run that opens it would settle it.
- **119, `settings/information/business-kyc`.** Two lines: CM-ACC-004 (the business data, as the cell's Store data page) and CM-PAY-003 (KYC). Both cells hold the term "KYC (Know Your Customer)", so the coordinator may keep one.
- **130, `services/payments/settings/:tab?`.** Placed on CM-PAY-002 (Zid Pay's settings). Not opened, and the module's imports (`use-user-roles`, `get-benificary-name`) don't settle which settings. A run on its tabs would.
- **155, `support/chargeback-dispute/:id`.** Placed on CM-PAY-009 with `core`. Its module imports `use-get-payment-charge-back` and `add-uploader`, read as the merchant contesting a chargeback with uploaded files. Not opened. This changes CM-PAY-009's Zid cell from `not-stated` to `core`, against its readings that 'Zid Pay assumes no responsibility for disputes or chargebacks'. The route shows Zid's own place for a dispute, not who carries its loss, so the two don't conflict.
- **169, `settings/notification-settings`.** Placed on CM-NTF-001. The page broke (gaps-en#48), and the settings sidebar doesn't list it. CM-NTF-002 is the alternative.
- **Local delivery and pickup** (21, 37, 77, 100, 131, 162). Each takes its narrower capability: CM-SHP-008 for local delivery, CM-SHP-007 for pickup in store. The two list pages (131, 162) also take the parent, CM-SHP-006, whose own name holds both words. The tier routes (22, 37, 47) also take CM-SHP-001, since a tier is a price by countries and cities (module imports `price-zone-form-pricing-options`, `tier-countries-cities-selector`).
- **Auto restock** (62, 71, 153). Placed on CM-INV-006, transfers, since "Automatically creates a transfer request when products reach their minimum stock level" (rest-en#94). The minimum stock level may also bear on CM-INV-004 (low stock).
- **The marketplace connection's sub-pages** (9, 12, 20, 24, 35, 84, 85, 105): inventory, prices, settings, products, orders. Each is placed on CM-CHN-003 alone, as a part of the connection. I gave them no line on CM-INV-001 or CM-CAT-013, whose things they apply only to the marketplaces.
- **The legal pages** (8, 10, 11, 19, 45). Each is placed on CM-CNT-008, whose Zid cell already names the five kinds. I gave no second line to the subjects they are about (CM-SUP-008 for complaints, CM-RET-003 for returns, CM-TRU-005 for privacy, CM-TRU-010 for licences): a page of the store's policy text doesn't show the platform doing those things.
- **Markets** (86, 156, 180). Placed on CM-MKS-001. 86 `price-managing` may also be CM-MKS-006. GAPS.md says prices per market aren't held, since the flag `must_use_markets_pricing` is false.

## A structure whose items and sources disagree

None in this batch. Every route's item holds its `module` and `imports`, which the entry's rendering leaves out, as the brief says.

## What a source or run step states that no entry holds (for the second stage)

- **CM-NTF-004, the sender name:** the provider and prices. Run 20261028T160128Z-dashboard-routes-rest-en, `steps/063.text.txt` states:
  - 'Service activation requires Zid team review and may be delayed due to regulatory checks by the provider (Unifonic).';
  - 'The sender's name is a service that is renewed annually.';
  - the prices by region, such as 'SMS Sender Id - KSA only | SAR 530.00' and 'SMS Sender Id -UAE only | SAR 2,599.00'.
- **CM-INV-004:** a "Low Product Stock" setting in the marketplace connection's inventory settings (rest-en, `steps/017.text.txt`).
- **CM-POS-003:** the POS sessions history has Cash and Credit card columns per session, with who started and closed it (rest-en, `steps/052.text.txt`).
- **CM-STF-002, CM-POS-001:** 'Enable location-based POS access': 'Restrict staff access to POS data and registers based on their assigned locations.' (rest-en, `steps/049.text.txt`).
- **CM-STF-003, a quality:** the group page counts 'POS app permissions (ZidPOS)', "0 of 195", and a user given dashboard permissions 'will count as a seated user' (gaps-en, `steps/030.text.txt`).
- **CM-PAY-015:** the module of `services/payments/other-payment-providers/:id` imports `madfu_logo` and `emkanpay` (its item in `items.jsonl`). This is a lead for providers of instalments, whose role no held statement of this batch gives (M-5).
- **CM-CHN-003:** Amazon's acceptable use policy, a dialog the activation route imports (`amazon-acceptable-use-policy-dialog`). Also, 'Price changes are sent to marketplaces instantly, but they may take up to 6 hours to appear on Zid.' (rest-en, `steps/026.text.txt`), a duration.
- **CM-CHN-002:** 'Your first 5 orders are commission-free!' for Mazeed (rest-en, `steps/036.text.txt`), a quality. Mazeed's settlements 'moved to Zid Wallet' (rest-en, `steps/045.text.txt`), a lead for CM-PLN-006.
- **CM-CUS-008, CM-SHP-001:** 'The national address is now required for all domestic shipments in Saudi.' (gaps-en, `steps/007.text.txt`), scope Saudi Arabia.
- **CM-ACC-004, CM-TAX-003:** 'Vat Registration Certificate (Income greater than 375K SAR)' (gaps-en, `steps/053.text.txt`), a threshold.
- **CM-PAY-026:** the financing activation's 'your store sales within 12 months qualifies you' (rest-en, `steps/106.text.txt`), against ZD-1's note of "sales over 40,000 in 3 months".
- **CM-SFR-003, CM-SFR-006:** the landing page themes' makers and prices, such as Sigma, 'By: Small Details', 1,300 (rest-en, `steps/070.text.txt`), and the theme market's '1 - 13 of 94 themes' (rest-en, `steps/067.text.txt`).
- **CM-SHP-007, CM-CAT-014:** the online store's badges 'Pickup only' and 'Quick delivery' (dashboard-locales, `online-store-settings:badges.pickup.title`, `badges.quickDelivery.title`).
- **CM-MKT-016:** the stock notification's sending time and channels (email, WhatsApp; rest-en, `steps/048.text.txt` and `109.text.txt`).
- **CM-SUP-002:** 'Specify how many hours after order completion customers should receive a review request Email.' (en-2, `steps/005.text.txt`).

## Problems with the brief or the script

- **No leads for routes.** `held_entries.py`'s `values_of` drops the fields `id`, `path` and `parentId`, so a route entry's own words never reach the term or name leads, and none of this batch's 195 entries printed one. The brief expects about a quarter to have none. For a route manifest, all have none, so rule 2's lookups carry the whole batch. Leading routes by their path's words, minus the words every route holds, would help ZD-5 and ZD-6.
- **The checker's container note** sees only `$lang.stores.$storeId` (entry 7) as a container, since every store route has it as its `parentId`. Paths such as `services/logistics` hold others by path, not by parent, and the checker doesn't see them. None of them is an entry of this batch on its own.
- **`ZD-5` and `ZD-6` haven't run.** They hold the rest of the manifest. Where they place the same sections (`services/logistics/*`, `channels/marketplaces/*`, `services/whatsapp/*`), the coordinator aligns them with these lines.
- **The checker** printed no problem besides the missing notes, which this file supplies.

## The coordinator's check (30 October 2026, after the batch)

- **The leads.** The batch ran with no leads: the term and name leads read an entry's values, and a route's `path` had been left out of them with its identifiers. A route's path is the platform's own words for its place, so the leads now read its segments, without parameters (`held_entries.py`). With them, 176 of the batch's 195 entries have leads, and the checker's notes on this batch were read again: each line stands. Mobile app push notifications are the branded app's (CM-CHN-006), not the merchant's own app's (CM-SRF-001), whose Zid cell names the homonym. Payments onboarding is CM-PAY-003's, not the store's onboarding (CM-ONB-004). WhatsApp's settings are no app's developer settings (CM-APP-010).
- **Two readings settled by the dashboard's own strings** (`dashboard-locales`, the platform's locales for routes no run opened):
  - WhatsApp's opt-out page sets 'Unsubscribe keywords' and an 'Unsubscribe confirmation message', 'You have been unsubscribed and will no longer receive automated messages.': the customers' consent to the store's messages, CM-CUS-007, no longer unsure;
  - the chargeback dispute page is titled 'Chargeback dispute response': the merchant contests the dispute, CM-PAY-009.
- **Similar products** is decided as CM-MKT-023, product recommendations (`held/new.tsv`): 'Customize similar products' and a 'Similar products preview', the products shown beside a product on the storefront, which the merchant may choose. Not CM-MKT-021's offers.

**The coordinator, after SA-2 (30 October 2026):** this batch's llms.txt line on CM-AIA-005 is `shows` now, and the entry takes CM-CNT-007 `core`. A store's llms.txt is a file the platform writes for AI platforms to read the store; it gives buyers no channel and no purchase, and Zid keeps it in its SEO section (`review-H-rulings.md`, the ruling after SA-2).
