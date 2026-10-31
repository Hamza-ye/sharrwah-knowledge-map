# Held pass, Salla, batch SA-55: notes

80 entries (effort high), evidence at observed-sa@b0bd0b163, all of `settings-center` as rebuilt after SA-50 (one entry per node, every store's answer in it, with `if:`). Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-55`). Twelve sub-pages, all opened by items SA-48, SA-49 and SA-50 placed:
- 1 to 55, seven of the Products section's: Branch and warehouse priority order (`/products/products.branch_sorting`, 1, 2), Product filter settings (`/products/filters`, 3 to 14), Brand settings (`/products/brand_options`, 15 to 21), Exclude products from inventory sync (`/products/sync_ignore_sku`, 22 to 25), Product sorting options (`/products/products.product_sorting`, 26 to 35), Quick donation (`/products/quick_donation`, 36 to 43), Wishlist Notifications (`/products/wishlist-notifications`, 44 to 55);
- 56 to 65, three of Your profile's: Edit profile (56 to 61), Registered devices (`/profile/recent-access-devices`, 62), Quick access (`/profile/quick-login`, 63 to 65);
- 66 to 74, Shipping & delivery's Cash on delivery (`/shipping/shipping.cod`);
- 75 to 80, Customer wallet's Maximum Credit Usage Limit (`/wallet/max-credit-usage`).
- The twelve bodies are the same bytes on all five stores (sha256 of `<label>/<section>.json` compared: branch_sorting `6111160e…`, filters `74e7ecbd…`, brand_options `7d11eae1…`, sync_ignore_sku `a10bb136…`, product_sorting `45388de9…`, quick_donation `6bd821f7…`, wishlist-notifications `9ded678e…`, edit-profile `f5ddceb4…`, recent-access-devices `02b6f43e…`, quick-login `2d6fa288…`, shipping.cod `57791ca7…`, max-credit-usage `2024f0fe…`).

**Placed:** 75 entries on capabilities, none `new`, 5 `out`, in 94 lines: 86 `core`, 2 `extension-point` (CM-NTF-004, entry 53), 1 `shows` (CM-LOY-005, entry 44), 5 `out`. No `own-service` or `outside`, no filler.
- Lines by capability: CM-SFR-013 12, CM-MKT-017 11, CM-SFR-015 10, CM-SEL-007 8, CM-PAY-029 8, CM-CAT-005 7, CM-ACC-001 7, CM-LOY-001 6, CM-CNT-005 4, CM-INV-001 4, CM-TRU-001 4, CM-NTF-004 2, and one each on CM-INV-009, CM-CAT-002, CM-LOY-005, CM-PAY-016, CM-CUS-006, CM-TRU-008.
- Scope on 35 lines: `products-filters` (13), `brands` (11), `quick-donation` (8), `not sms-sender`, `not whatsapp-communication`, `multi-countries` (one each).
- Four qualities: the quick donation amounts (41), the wishlist reminder's 14 days (47), cash on delivery's SAR 20 minimum and SAR 1,000 maximum with Salla's shipping labels (69, 70).
- **The checker prints no `CHANGES` line: no cell changes.**

**Sources read:** the brief and what it names; the evidence map; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md` (its settings rows), `structures/README.md`, the register's rows for `settings-center` and `dashboard-settings-menu`; the selection rows; B-extent's "Cells and evidence" and conventions; the rulings, whole, with their last section; SA-48's to SA-54's notes, their rules S1 to S12, R1 to R9, T1 to T8, U1 to U8, V1 to V8, W1 to W8 and X1 to X4, and the coordinator's checks; the earlier lines `held_entries.py earlier` named (SA-33, SA-48, SA-49, SA-50, SA-51, and SA-52's and SA-54's channel selects).
- **The bodies.** I walked each of the twelve bodies once, with a script that prints each node, its key attributes and the conditions above it, and opened a body's code only where the walk left a column open. These are the entries the bodies settled:
  - 1, 62, 63, 64, 65: pages drawn by components that are no nodes (BranchSorter; DevicesSettingsTable; RegisterPasskeyButton and PasskeysSettingsTable), and 2's back link and its condition;
  - 5, 17, 24, 28, 38, 46, 55, 57, 61, 68, 74, 77, 80: which list an entry stands for, and whether the Save list's label is an unresolved array (V7) or a string;
  - 40 to 43, 50, 52, 79: shown only while a toggle is on, a form's value;
  - 53: the options' descriptions and disabled states, given under store features the entry leaves out (Y1);
  - 75 to 80: the page's two versions, by the store's markets (Y3).
- **To clarify only, each cited where a line rests on it:**
  - `dashboard-features/*@en/items.jsonl` for the eight features (demo lines: `quick-donation` 158, `customer-wallet` 187, `one-signal-push-notification` 301, `sms-sender` 385, `whatsapp-communication` 432, `brands` 501, `products-filters` 520, `multi-countries` 541), with the other three stores' lines;
  - three run pages: the Pro store's Quick donation page, 'Access restricted' (`20261009T033607Z-sweep-settings-demo-en/steps/062.text.txt`, lines 98, 99: entry 36); the Basic store's and the Pro store's Maximum Credit Usage Limit pages (`20261008T141131Z-sweep-merchant-en/steps/365.text.txt`, lines 58 to 60; `20261009T033607Z-sweep-settings-demo-en/steps/073.text.txt`, lines 145 to 150: entries 75 and 78), with `derived/plan-gates.tsv` rows 272 to 285 for the same addresses (only the public demo's home-page lines, so no plan gate);
  - `dashboard-translations/{en,ar}/settings.json` for the Arabic quotes and the keys no body uses (below);
  - `class_slice.py search` on the settings' labels, which found SA-S-0110 (CM-TRU-008) and SA-S-5145 (CM-PAY-028), and `merged/evidence.tsv` for the cells that cite them.

## The rules: S1 to S12 and R1 to X4, kept, and what I added where they don't reach

I kept the earlier rules as the coordinator's checks and rulings left them:
- S1 for each sub-page: the item that opens it (SA-48's, SA-49's, SA-50's) and the concern map's key, SA-S-1755 to SA-S-1766.
- W7 for the sections whose `flag:` gates their content (`products-filters`, `brands`, `quick-donation`), with S4 for the support: all three are released on the four held stores, so `core`, each store's `enabled` in `reading`.
- S7, R5 and U2 for the forms and lists; V7 for the Save lists whose label is an unresolved array (5, 17, 24, 28, 38 merge with their settings list; 74 stands alone, since the settings list's entry carries its own words, and is `out`); the Save lists with a string label stand alone and are `out` (55, 61, 80).
- U3 for the pages a component draws (1, 62, 63); S8 for the back link (2, `out`).
- T5 for the brands page's menu settings (19 to 21) and its list (17), as SA-51 placed the blog's (CM-CNT-005).
- S6's first refinement for the brands page's banner (18: brands, CM-CAT-005 alone).
- V4 and S7 for the channel select whose options name App Store providers (53).
- U5, U6 and V2 for the markets (75, 76).
- R9 for the profile's sign-in items (62 to 65 on CM-TRU-001; the sub-pages keep CM-ACC-001 by their keys).

For the coordinator to align with SA-56, I added:
- **Y1. An option's description or disabled state given under a store feature takes that condition as the scope of the line its words give** (X2, which is for an option's label; the ruling after SH-69). Entry 53's SMS option reads 'First, link your store to an SMS provider from the App Store…' only `if not useFeature sms-sender`, and its WhatsApp option '…to a WhatsApp provider from the App Store.' only `if not useFeature whatsapp-communication`; each is disabled under the same condition. So the two CM-NTF-004 `extension-point` lines take `not sms-sender` and `not whatsapp-communication`, and the select's own CM-MKT-017 line keeps none. `sms-sender` is enabled on the two Pro stores only, so the Basic stores are shown the App Store line; `whatsapp-communication` is enabled on all four, so none is. **The same conditions stand in `feedback~rating_message.json` (SA-52's 35, SA-E-b097937b) and `products~notify_availability.json` (SA-54's 77, SA-E-3db74e9f, whose SMS option's label is itself given under `useFeature sms-sender`), placed without them.** If the coordinator keeps Y1, those lines take the same scopes; if not, mine drop theirs. No support changes either way.
- **Y2. A sub-page's own section node governs its gate.** `/wallet/max-credit-usage` carries no `features`, unlike `/wallet` and `/wallet/notifications` (`customer-wallet`) and `/wallet/gift-card` (`wallet-gift-card`). The Basic store, without `customer-wallet`, is shown its form (`20261008T141131Z-sweep-merchant-en/steps/365.text.txt`, lines 58 to 60). So 75 to 80 take no `customer-wallet` scope, and the wallet section's feature stays the scope of the item that opens the page (SA-50's SA-E-e1aa2df5).
- **Y3. A page in two versions by the store's markets.** Maximum Credit Usage Limit shows its form while the store's active markets answer holds none, and in its place the component WalletScopeLimits (limits per market) when it holds markets. That answer is a query enabled by `getFeatureState multi-countries`, so the component's version takes `multi-countries` (U5), and the form's version takes none, the store's markets in `reading` (V2). The section's entry holds both versions' words in its `shows`, so it takes a line for each on CM-LOY-001, as W1 does for two versions: the container with no scope, and the per-market limits under `multi-countries`. The Pro store's page shows the second (step 073, above).
- **Y4. A cell that cites the entry's own statement by its term takes the entry's line, though no lead names it** (rule 2). Entry 68's checkbox `disable_cod_for_banned_customers` and its description 'Cash on delivery will be hidden for customers who are blocked from other Salla stores.' are SA-S-0110, which CM-TRU-008 cites as `core` (the coordinator, after batch 7), its terms holding the same control name. So 68 takes CM-TRU-008 `core` beside CM-PAY-029 (the list's rules) and CM-CUS-006 (the label's 'العملاء غير الجادين', that cell's own term).
- **Y5. A select's fixed options that are amounts the schema states are the setting's quality** (41, Quick donation options: '10 ر.س' to '1000 ر.س'), as W8 takes an input's stated bounds. A store's choice among them is its own data. If the coordinator reads the options as the setting's input (S7), the quality moves to `reading`.
- **Y6. A description that says where another thing named is managed is a statement about that thing** (14: 'You can customize product options from the categories & options page.'). It takes that thing's line, CM-CAT-002 `core`, by the ruling after SA-41 ('a statement about one of those things is placed on it'). If the coordinator reads such a pointer as named in passing, the line drops; CM-CAT-002 is `core` either way.
- **Y7. A filter's or a sort order's dimension is what the setting sets it by** (S5): brands, categories, tags, ratings, price and product options as filters (7, 8, 11 to 14), and sales, ratings, price, discount and Salla's suggestions as sort orders (29 to 35) take no line on the dimension's capability (the ruling after SA-41; U1's check). The filters stay on CM-SFR-013 alone (S6, which names filters), the sort orders on CM-SFR-015 (SA-48's item, kept by the coordinator).
- **Y8. Cash on delivery's sub-page takes CM-PAY-016 on its section only** (66), as SA-49 placed the item that opens it and the concern map cites the same setting (SA-S-1765) on both. Its form, list and settings name cash on delivery's own rules, so they stay on CM-PAY-029 alone (M-6 refined gives the parent's line where the words name the parent's thing). If the coordinator reads U2 as giving a form and a list every capability of their page, 67 and 68 take a CM-PAY-016 line each; no cell changes.

## `new` things

None. Each entry's thing is already a capability's: the sub-pages by the concern map's settings keys and the items that open them; the settings by the capability of what they set (S5, S7). Searched with `caps --terms`, besides the leads: price drop, تخفيض سعر, انخفاض, price alert; push notification, web push, إشعارات المتصفح, onesignal; store notification, إشعارات المتجر; sort, sorting, ترتيب المنتجات, merchandis; inventory sync, مزامنة, sync; blocked, محظور, حظر, blacklist, blocklist; passkey, مفاتيح المرور; device, الأجهزة, session; credit usage, استخدام الرصيد; brand page, banner, بانر; reminder, تذكير; cart weight, وزن السلة; donation amount; sender id, sender name, معرف المرسل. Beyond the cells placed, only CM-CUS-005 (blocking customers) and CM-TRU-008 answered for this batch's things; the rest matched words only (below). The concern map's search (`class_slice.py search`) on the labels found SA-S-0110 (CM-TRU-008, placed) and SA-S-5145 (CM-PAY-028, a lead).

## The `CHANGES` lines

None: every line falls on a cell that already holds its support.

## Entries I couldn't tell, and what would settle each

- **14, CM-CAT-002** (Y6): a pointer to the categories & options page, placed as a statement about product options. The coordinator's reading of pointers settles it.
- **41, the quality** (Y5).
- **53, the two scopes** (Y1), and their alignment with SA-52's 35 and SA-54's 77.
- **68, CM-CUS-005** (blocking customers): no line. The description's 'blocked from other Salla stores' names the other stores' blocking as the source of what Salla knows, which the model places on CM-TRU-008 (SA-S-0110). CM-CUS-005's note says what a blocked customer can't do isn't stated; this description states one consequence, other stores may hide cash on delivery from them. If the coordinator reads it as CM-CUS-005's statement, 68 takes a `core` line there; CM-CUS-005 is `core` already.
- **18, the brands page's banner, on CM-CAT-005 alone:** S6 names brands; CM-SFR-007's note keeps its bars and banners to those shown across the storefront. The brands page's own text, if held, would settle whether the banner is the brands' own image.
- **22 to 25, what the inventory sync is with:** not stated on the page. The concern map's SA-S-5145, 'مزامنة المخزون مع الخدمات الخارجية', a product's quantity changed by syncing the stock with carriers or accounting systems, is cited on CM-PAY-028 as `shows`, and SA-49's R1 placed carriers' stock sync on CM-INV-001 as `extension-point`. If the excluded products are left out of that sync, 22 takes a line there too; the page doesn't say, so it is a lead, not a line (M-12).
- **26 to 35, product sorting on CM-SFR-015,** as the coordinator kept after SA-48. The concern map holds two placed inventory entries no cell cites: SA-I-0983, the plan line 'ترتيب المنتجات' (plan-features), and SA-I-0759, Product sorting options (settings). Whether the plan line is the storefront's sort options or the admin's own product order would settle whether CM-SFR-015 takes it.
- **49, the availability notification for wishlist products, on CM-MKT-017 alone:** CM-MKT-016's note keeps wishlist notifications on CM-MKT-017. Its words are a back-in-stock alert to the buyers who saved the product; if the coordinator reads it as both, it takes a CM-MKT-016 `core` line, which changes nothing.
- **75, two lines on one capability** (Y3).

## A structure whose items and sources disagree

- **53:** the entry renders the control's name `channels` as the translation 'Sales channels' (قنوات البيع), a build fault SA-54 found in 77, and it shows the options' descriptions with neither their `if` nor the options' `disabled` conditions (`useFeature sms-sender`, `one-signal-push-notification`, `whatsapp-communication`). The body governs (Y1).
- **2:** the back link renders no address; the body's is `/inventory`, only under `from=inventory`.
- **64, 65:** render no label; the item is the component RegisterPasskeyButton.
- **75:** its `shows` holds the WalletScopeLimits component's props and the save toast as if the section's own text; the component shows only under the markets condition (Y3).
- **1, 62, 63:** drawn by components whose strings no node holds; their keys are in `settings.json` only (below).
- **46:** one entry for the form's four settings lists; **5, 17, 24, 28, 38:** one entry for a settings list and its Save list (V7), as known.

## For the second stage: what the sources state that no entry holds

The components' strings, in `structures/salla/dashboard-translations/en/settings.json` (and `ar/settings.json`), by key; no body node holds them:
- **CM-TRU-001:** `profile/recent-access-devices/detail#approve` 'Approve login', `#reject` 'Block access', `#desc` 'Manage devices connected to your account.', and the devices' statuses `profile/recent-access-devices#status.pending` 'Pending', `#status.blocked` 'Blocked', `#status.verified` 'Verified': the merchant approves or blocks a device's sign-in. `profile/quick-login#registration.description` 'Passkeys let you sign in quickly and securely without a password.' and `#registration.feature-secure` 'Protected by fingerprint or device passcode'.
- **CM-ACC-001 and CM-TRU-001:** `profile/edit-profile#mobile.description` 'This mobile number will be used to verify your account.'; `#email.description` 'Account notifications will be sent to this email address.'.
- **CM-INV-009 and CM-INV-005:** `products/products.branch_sorting#empty` 'No branches or warehouses found. Start by adding branches and warehouses to set their priority.'.
- **CM-LOY-001:** `wallet/max-credit-usage#per-scope.heading` 'Maximum credit usage per market'.
- **CM-PAY-029:** `shipping/shipping.cod#minimum_amount.error.greater_than_maximum` 'The minimum order value must be less than or equal to the maximum order value.'.

Other leads:
- **The browser push channel** of SA-52's and SA-54's notes, a channel to buyers no capability holds, is gated by `one-signal-push-notification`: type app, app_id 777872392, install address https://s.salla.sa/apps/install/777872392, not released (`structures/salla/dashboard-features/demo@en/items.jsonl`, line 301). The model already holds that flag on CM-MKT-007 as `shows` (SA-S-3260), with the released flag `one-signal` as `core`. A gate's feature gives no line of its own (S4), so 53 names it in `reading`; the coordinator may decide where web push to buyers belongs (CM-MKT-007's campaigns or CM-NTF-004's delivery).
- **CM-MKT-017's note** says no statement held defines what the notification says or when it is sent. This batch's 47 to 54 state when: 14 days after a product is added, when a saved product's price drops (by email), when it is available again, and when its stock drops below the merchant's threshold. The note can be revised at Salla's amendment.
- **CM-SEL-007:** quick donation is released for plus, pro and special and enabled on no held store; the Pro store's page reads 'Access restricted' (step 062 above).

## Leads set aside as no leads

- **The sections' common leads:** CM-ACC-006 (by `store_setting_browse`, the sections' permission: 1, 3, 15, 26, 36, 44); CM-AIA-003 (by product, text: 1, 3, 15, 26, 36, 42, 44).
- **By common words only:** CM-SHP-006, CM-SHP-008 (1, 2, by branch, order); CM-SHP-007 (6); CM-ANL-002 (8, 40, 51, 73, by categories, stock); CM-CNT-010 (8); CM-INV-010 (9, 29 to 35, 47 to 49, by product, حسب: the checker's first-lead notes on lines 35 to 41); CM-CNT-003 (10, 19 to 21, by page); CM-MKS-006, CM-TAX-001 (11, by price); CM-SHP-022 (12, 69, 70); CM-ORD-003 (14, by customize); CM-SFR-015 (7 to 14, by show: filters are CM-SFR-013's by S6); CM-ACC-003 (19 to 21, 54, by under, قايمة); CM-INV-003 (22 to 25, by inventory); CM-INV-009 (22 to 25); CM-INV-004 (32 to 35, by low; 51, kept apart by its note: the store's alerts); CM-CHK-008 (36 to 43, 63 to 65, by quick); CM-NTF-002 (44 to 46, 55, by notification: these are the buyers'); CM-API-009 (45 to 55, by notifications); CM-LOY-007 (47, 48, 54: reorder reminders, another thing); CM-LOY-008 (49, 51); CM-ACC-008 (50, 52, by available in); CM-MKT-016 (50, 52: its note); CM-API-013 (50, 52); CM-CHN-001 (53, by the build's Sales channels); CM-CUS-007, CM-API-004 (53, by email, SMS); CM-MKT-007, CM-NTF-004 (59, by email); CM-CUS-008 (59, by address); CM-TAX-003, CM-TAX-005 (60, by number); CM-API-003, CM-STF-005 (62 to 65, by access); CM-PLN-004 (66, by `shipping_options_management`); CM-SHP-019, CM-SHP-013 (66, 68); CM-SHP-015 (68, by carrier: the alert's rule of cash on delivery is CM-PAY-029's own, SA-S-0126, V8); CM-ACC-004 (69, 70, by شركة); CM-ORD-010 (69, 79, by limit: the store's minimum for every order is another setting, SA-48's); CM-SHP-001 (70); CM-CAT-001 (71, 72, 75, by المنتجات, add new); CM-SHP-020 (71, by weight); CM-LOY-004 (75, by markets); CM-ORD-001, CM-ORD-005 (75); CM-OPS-004 (76, by status); CM-PAY-025 (76 to 80, by credit: the merchant's business credit, not the buyer's wallet); CM-RET-002 (79).

## The checker's lines, read again

- **No `CHANGES`, no `NEW`.**
- **`NOTE` containers** (lines 2, 4, 17, 28, 32, 42, 43, 50, 52, 65, 73, 77, 79, 89, 91): each sub-page's section, and its form or list, placed on the capability of the item that opens it (S1, U2, U3); each one's settings are placed by their own entries.
- **`NOTE` first lead CM-INV-010** (lines 35 to 41, the sort toggles 29 to 35): matched by product and حسب only, set aside above.

## Problems with the brief or the script

- **The leads don't read a control's name as an identifier.** CM-TRU-008's terms hold `disable_cod_for_banned_customers`, and its evidence cites the same description (SA-S-0110), but entry 68, whose `controls:` names it, showed no lead to CM-TRU-008. Only `class_slice.py search` on the description found it (Y4). The leads could take a control's `name` where the model's terms hold it, as `earlier` sets common control names aside.
- **The build renders an option's `desc` without its `if`, and no option's `disabled`** (53), so store gates on options are read from the body (Y1). Three bodies hold them (`feedback~rating_message`, `products~notify_availability`, `products~wishlist-notifications`).
- **A sub-page whose content is in two versions by the store's data** (75 to 80) has its component's words rendered as the section's own (Y3). The rendering could mark them under the component.

## The coordinator's check (31 October 2026, after the batch)

- **No cell changes and no new things.** Y1 to Y8 stand for SA-56.
- **Y1 applies from this batch on.** SA-52's entry 35 and SA-54's entry 77 keep their one CM-NTF-004 line each, with no scope. They would split into one line each for SMS and for WhatsApp, under `not sms-sender` and `not whatsapp-communication`, and no support would change. The difference is noted here for the amendment.
- **Y2 stands:** `/wallet/max-credit-usage` takes no `customer-wallet` scope. The Basic store, without the feature, is shown its form.
- **Y4 stands:** entry 68 takes CM-TRU-008 `core` from SA-S-0110, which `class_slice.py search` found where no lead did.
- **Leads:**
  - the wishlist notifications' timing, for CM-MKT-017, whose note says no statement held it;
  - the component strings in `settings.json`, among them device approval, passkeys and the per-market limit.
- **Cost:** 19.5 million tokens over 89 requests, about 244,000 an entry.
