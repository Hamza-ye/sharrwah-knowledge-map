# Held pass, Salla, batch SA-50: notes

92 entries (effort high), evidence at observed-sa@b0bd0b16, all of `settings-center` as rebuilt after SA-48 (`nodes:section`: one entry per node, every store's answer in it). Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-50`). The seven sections after SA-49's twelve:
- 1 to 12 Customers (`/customers`); 13 to 40 Marketing (`/coupons`); 41 to 46 Customer wallet (`/wallet`); 47 to 53 Loyalty program (`/loyalty-program`); 54 to 59 Gifting (`/gift-system`); 60 to 66 Blog (`/blog`); 67 to 92 Reviews (`/feedback`).
- The seven bodies are the same bytes on all five stores (sha256 of `<label>/<section>.json` compared: customers `98db4969…`, coupons `2a3f40ef…`, wallet `1997e970…`, loyalty-program `7cf09b83…`, gift-system `b2a740fe…`, blog `029dbcac…`, feedback `1ee82d59…`).

**Placed:** 83 entries on capabilities, none `new`, 9 `out`, in 107 lines: 88 `core`, 1 `core;extension-point` (CM-MKT-023, entry 30), 1 `extension-point` (CM-PTN-009, entry 23), 8 `shows`, 9 `out`. No `own-service` or `outside`. One filler (Apple Pay, entry 10); one quality (the Recommended tag's threshold, entry 88). Scope on 38 lines (below, T1 to T3).
- `shows`: CM-CUS-010 (4, behind auth-v2; 6, behind custom-customer-fields), CM-CUS-013 (9, behind whatsapp-otp), CM-MKT-002 (19, behind multi_coupon), CM-LOY-002 and CM-LOY-001 (45, behind wallet-gift-card): features no held store has released; CM-NTF-004 (8, the SMS balance named); CM-SUP-005 (87, the store's support channels named).
- **The checker prints one `CHANGES` line:** CM-MKT-023 gains `extension-point` (entry 30, below).

**Sources read:** the brief and what it names; the evidence map; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's row for `settings-center`, `index/ledger-summary.tsv`; the selection row; B-extent's "Cells and evidence" and conventions; the rulings to their last section (the three after SA-49); SA-48's and SA-49's notes, their rules S1 to S12 and R1 to R9 and the coordinator's checks.
- **The entries carried most of what governs them.** I read the seven bodies only for what the entries leave out, with one walk that prints each node and the `if` conditions above it (below, "A structure whose items and sources disagree"). That walk settled the scope of entries 5, 6, 9, 19, 27 to 31 and 45, and the support of 6 and 19, which the entries alone left open. I read 30 and 31's nodes in the body for the suggestions' source request, and 43's for its hidden input.
- **To clarify only, each cited where a line rests on it:** the stores' settings panels, which show which items each store's panel displayed: the Pro store, `20261008T133523Z-sweep-demo-store-en` steps 102 to 108; the Basic store, `20261008T141131Z-sweep-merchant-en` steps 104 to 110; for Marketing also the real store (`20261012T010906Z-sweep-real-merchant-full-en/steps/293.text.txt`) and the public demo (`20261009T022751Z-sweep-public-demo-en/steps/106.text.txt`). Also `dashboard-features/*@en/items.jsonl` for each gate, with `demo@en/meta.json` for its date, and `dashboard-translations/{en,ar}/settings.json` for the Arabic quotes. The concern map's settings keys (SA-S-1703 to SA-S-1734, SA-S-1766 to SA-S-1768) gave each sub-page's cell (S1, S10). I read the earlier batches' lines named by `held_entries.py earlier` (SA-8, SA-11, SA-16, SA-21, SA-23, SA-33, SA-48).

## The rules: S1 to S12 and R1 to R9, kept, and what I added for the kinds they don't cover

I kept S1 to S12 and R1 to R9 as the coordinator's checks left them, with the three rulings after SA-49: the gate node's scope, the `s:redirect`, which none of my sections holds, and the admin's language, which none holds either. For the coordinator to align with SA-51 to SA-56:

- **T1. A section with `features` is a gate node over its content.** This covers Customer wallet `customer-wallet`, Loyalty program `loyalty-system` and Gifting `buy-as-gift`. On the Basic store each page shows only 'This feature isn’t available on your plan' and the upgrade line, while the Pro store shows the settings (steps 106 to 108 against 104 to 106).
  - So the feature is the scope of the section's own line (S4) and of every node inside it. The ruling after SA-49 names "an `s:plan-gate` or a gated list"; I read a gated section as the same kind of node.
  - A node's own gate is added: `customer-wallet;wallet-gift-card` (45), `loyalty-system;multi-countries` (53), `buy-as-gift;multi-countries` (57).
  - If the coordinator keeps the ruling to plan gates and lists, the inner nodes' scope (42 to 46, 48 to 53, 55 to 59) moves to their readings, and only 41, 47 and 54 keep it.
- **T2. An `if` on a store feature, which the rendering leaves out, is the node's gate on the store, so its scope** (S4), in the body's identifiers:
  - 5 and 9 show only where `auth-v2` is off (`not getFeatureState auth-v2`), so the scope is `not auth-v2`, as SA-49 wrote `plan not basic`;
  - 6 shows only under `useFeature custom-customer-fields`;
  - 19 shows only under `getFeatureVisibility multi_coupon`.

  The feature then sets the support by S4: none of `auth-v2`, `custom-customer-fields`, `multi_coupon` or `whatsapp-otp` is released on a held store, and no held panel shows 4, 6, 9 or 19.
  - A condition on the store's own stored data goes in `reading` (R8). Examples are `useVars /$query/data/marketing_settings.basket_gap/slug` and the same test for `checkout_xsell` and `checkout_xsell_source` (29 to 31), and the wallet's status for gift cards (45).
  - A condition on a staff permission (`usePermission reviews_management` around 80's card) is a gate on the user (S3).
- **T3. An `if` on the store's plan around a list makes a gated list.** Smart recommendations is wrapped in `getStorePlan` equal to `plus`, `pro`, `team` or `special`. Its plans are the scope of its header and of each field in it (27 to 31), written `plus;pro;team;special` in the body's identifiers (the ruling after SA-49; R6). The Pro and the real store's panels show the list, and the Basic store's doesn't.
- **T4. 'Powered by Mushammir' / 'Powered by Meshmar' (يدعمه مشمر) in a tooltip** (28 to 30) takes a CM-AIA-001 `core` line, as SA-16 placed Mushammir's product suggestions (SA-E-0a249719). It is a product's name, not a maker statement, so not `own-service`.
- **T5. A setting that puts a page in the store's navigation menu takes CM-CNT-005 `core` beside its own capability** (S5). The cases are 64, 'Show the blog in the main navigation menu and set its label.', and 20, the Discounts tab 'in the store navigation'. CM-CNT-005's Salla cell holds only the flag `store-menu`, and its reading says no admin link, permission or plan line names menus.
- **T6. A display option shown in the store's own app takes that app's capability** (72, App Maker, CM-CHN-006), by S6's second refinement: the app is a place outside the web storefront. A storefront page where a feature shows goes in `reading`, as S6 keeps the product page: the information pages (86, not CM-CNT-003), the category page (70) and the checkout (30).
- **T7. A section's untitled lists** (S2, R4):
  - `out` where the section's cards hold several capabilities' settings: Customers (3), Marketing (16), Customer wallet (42: the wallet and the gift cards), Blog (62: the blog, its menu item and its SEO) and Reviews (69);
  - a container on the one capability where every setting in them is that capability's: Loyalty program (48) and Gifting (55), with the section's gate as scope.
- **T8. An item whose link is an admin page, not a settings sub-page** (80, `/feedback/settings/factors`), takes the line SA-8 gave that page, a one-thing page, so one line (R2).

## `new` things

None. Each entry's thing is already a capability's:
- **the sub-pages:** each is the cell of its concern-map key (SA-S-1703 to SA-S-1734, SA-S-1766 to SA-S-1768);
- **the fields:** each is the capability of what it sets (S5, S6).

Searched with `caps --terms`, besides the leads:
- require login, login to view, password protect, private store, members only, فرض تسجيل الدخول, تسجيل الدخول قبل, sign in required, login required, store access, restrict access;
- guest cart, merge cart, دمج السلة, Safari, apple pay;
- Mushammir, Meshmar, مشمر, frequently bought together, cross-sell, upsell;
- donation reminder, تذكير;
- discounted products, التخفيضات, sale price, compare at, navigation menu, store menu, قائمة التنقل, footer, popup.

## The `CHANGES` line, and what I decided

- **Line 37 (entry 30): CM-MKT-023, product recommendations, gains `extension-point`.**
  - **What the entry states:** 'Product suggestions at checkout' / 'اقتراح منتجات في صفحة الدفع': 'Show products suggested by AI or by your store's apps' (an ASCII apostrophe, so quoted here, not in the row) and 'اعرض منتجات يقترحها الذكاء الاصطناعي أو تطبيقات متجرك'. Its sibling 'Source' (31) lets the merchant 'Choose where the product suggestions for your customers come from.', from the request `marketing-integration/checkout-xsell/sources`.
  - **How I read it:** the store's apps fill the platform's own checkout suggestions, so third parties do the recommending through something the platform provides. The apps are unnamed, so the line has no filler (S7, M-8). Kept.
  - **What would settle it:** the sources' answer, which isn't held, would say which apps or providers the suggestions come from, and whether any of them is Salla's own (the ruling after SA-17: an app of Salla's is `own-service`).
  - **A limit of the evidence:** no held store's panel shows the field (29 to 31 need the store's settings to hold the key, R8), so this line rests on the schema and its translations alone.

## Entries I couldn't tell, and what would settle each

- **6, 'Require login to view store' / 'فرض تسجيل الدخول قبل تصفُّح المتجر', on CM-CUS-010 `shows`.** No capability holds a store closed to buyers who aren't signed in. I read it as a rule of the buyer's sign-in, a toggle with no place of its own. A new thing is the alternative, a members-only store, or B2B's buyer portal (CM-B2B-007). The unused `customers#login-access-settings.description`, 'Control sign-in options and store access requirements.', groups it with sign-in (below). No cell changes either way.
- **20, 'Show discounts tab', on CM-MKT-001** (the discounted products are the store's price reductions, S6) **and CM-CNT-005** (T5). CM-SFR-015, storefront display, is the alternative for the first line. No cell changes.
- **38, 'Auto donation reminders' / 'تذكيرات التبرع التلقائية', on CM-SEL-007.** 'Enable automated reminders for donation.' doesn't say who is reminded, of what, or by which channel. CM-LOY-007 (reorder reminders) and SA-49's new تبرع سلة عن كل طلب (Salla's own donation per order) are the alternatives. The help article on donations, or the reminder's message in the notifications' settings, would settle it.
- **23, the Salla Partners store page, `extension-point` on CM-PTN-009,** read with the cell's reading of the partners' side (its Affiliate Marketplace). If the coordinator reads the store page as the merchant's own side, the line is `core`. No cell changes either way.
- **46, 'Wallet & Cashback Notifications', on CM-LOY-001 (the cell's settings route, SA-S-1768), CM-LOY-003 (the cashback named in the label) and CM-NTF-001** (the settings of automatic notices to customers, which CM-NTF-001's reading says no statement lists). If the coordinator reads the notices as only the wallet's, the CM-LOY-003 and CM-NTF-001 lines go. No cell changes.
- **78, 'Request shipping review', on CM-SUP-002 and CM-SHP-022** (the carriers' ratings). CM-SHP-022 is defined for the carriers of Salla's own labels; the entry says only 'the shipping carrier for their order'. A statement of which carriers the buyers rate would settle it. No cell changes.
- **87, 'Allow customers to contact support about their reviews':** CM-SUP-001 `core` and CM-SUP-005 `shows` (the store's customer service reached by email or WhatsApp, 'قنوات خدمة العملاء'). If the coordinator reads it as a review form's option only, the second line goes.
- **89, 'Hide customer name', on CM-SUP-001 alone.** The masked name is the buyer's, but CM-TRU-005 holds the merchant's privacy duties (privacy settings, consent, data requests), and a line there would make its `not-stated` cell `core`. I didn't take it. The checker's footnote note on this line is the masking's asterisks ('M* A****'), not a footnote mark.
- **88, 'Customer recommendations', on CM-SUP-001,** not CM-MKT-023: the "Recommended" tag rests on buyers' ratings, a homonym of the lead. Its threshold, 'rated 3 stars or higher', is written as a quality, the platform's own limit. If the coordinator keeps qualities to maxima, rates, fees, prices and durations, the quality goes.
- **12, 'Merge cart after login', on CM-CHK-002 alone;** the sign-in (CM-CUS-010) is when it happens. If the coordinator reads the 'account cart' as the customer account's own, a CM-CUS-010 line is added. No cell changes.

## A structure whose items and sources disagree

- **The entries leave out each node's `if` conditions:**
  - on a store feature: `not getFeatureState auth-v2` (5, 9), `useFeature custom-customer-fields` (6), `getFeatureVisibility multi_coupon` (19);
  - on the store's plan: `getStorePlan` in plus, pro, team, special (27 to 31);
  - on the store's data: the `useVars /$query/data/…/slug` tests (29 to 31), the wallet's status (45);
  - on the user: `usePermission reviews_management` (80's card).

  These decide a scope or a support, so every section's body still needs reading for them. The entry could carry them as it carries `features`.
- **One entry, several nodes:** 14 holds Marketing's two fetchers, and the untitled `s:list` entries hold every card of their section (3, 16, 42, 48, 55, 62, 69). 16's cards are of several capabilities, one of them holding only the donation reminders.
- **Ids resolved as translation keys,** as SA-49 found for its entry 35. 46's id `notifications` renders as 'Notifications (الإشعارات) [notifications]', the section Notifications' title; 50's id `general` renders as 'General (عام) [general]'. The items' own words are their labels.
- **Keys of another namespace in `shows`:** `utils:form.submit_button.saved` (41, 47, 54) and `utils:form.submit_button.error` (54), the toast after saving, unresolved.
- **10 has no description in the body,** while the locale holds one no body uses (below).

## For the second stage: what the sources state that no entry holds

- **`dashboard-translations/en/settings.json` (and `ar`), keys no held body uses,** each a lead for the cell named:
  - CM-PAY-012: `customers#browser_notification_for_applepay.description`, 'Display a prompt directing customers to use Safari to pay with Apple Pay.' (entry 10's field has no description in the body);
  - CM-CUS-010: `customers#login-access-settings.*` ('Login & access', 'Control sign-in options and store access requirements.'), `customers#registration-form.*` ('Set required registration fields for customers.'), `customers#profile.*` ('Control which fields are shown on the customer profile.'), and `customers#upgrade.description`, 'Unlock this feature by upgrading to the Special plan to access advanced customer settings.' The last is the plan of `custom-customer-fields`, which gates 6;
  - CM-CHK-002: `customers#cart-management.*`, 'Manage the customer cart experience throughout the store.'; CM-CHK-001: `customers#payment-notifications.*`, 'Control checkout notices to keep the payment flow smooth.';
  - CM-LOY-001: `wallet#balance-validity.*`, 'Balance expiry', 'Set how long the balance is valid after it’s added to the wallet.';
  - CM-SUP-001: `feedback#allow_attach_images.*`, 'Allow customers to upload up to 3 images with their review.', a limit for its qualities;
  - CM-LOY-007: `coupons#repurchase-reminders`, 'Repurchase reminders';
  - CM-MKT-001 to CM-MKT-003: `coupons#coupons-settings.label`, 'Coupon settings'; `coupons#offers.label`, 'Discount settings'; `coupons#offers_settings_rules.label`, 'Offer settings rules'; `coupons#panel.enable_coupons` and `coupons#panel.show_discounts`;
  - CM-MKT-023: `coupons#bought-together.ai-feature-1` to `-3` ('Personalized for each customer', 'Ready in one click') and `coupons#basket-gap.ai-feature-*`.
- **CM-MKT-023:** the checkout suggestions' sources, `marketing-integration/checkout-xsell/sources` (`structures/salla/settings-center/demo@en/coupons.json`, the `$sourcesQuery` of the field `checkout-xsell-source`), aren't held. They would name the apps behind entry 30's `extension-point`.
- **The settings panels' later state:** the Pro store's panels are of 8 October and its features answer of 9 October (`structures/salla/dashboard-features/demo@en/meta.json`). The loyalty and gifting items behind `multi-countries` (53, 57) aren't shown on 8 October, and no later panel of `/loyalty-program` or `/gift-system` is held.

## Leads set aside as no leads

- **Customers:** CM-ACC-006 (1, by `store_setting_edit_setting`); CM-STF-002, CM-ACC-001 (1, by permissions, store owner: the permission message); CM-ONB-002, CM-TRU-017 (1, by access, restricted, request); CM-LOY-008 (2 to 12, by customer); CM-MKS-009 (4, by countries); CM-CUS-007 (4, 9, by email, SMS, WhatsApp: no consent named); CM-MKT-007, CM-API-004, CM-MKS-006 (5, 7, by email, اتاحة); CM-PAY-003 (6, by before); CM-TRU-001 (8, by security: that cell is the admin's sign-in, and CM-CUS-012 is the buyer's); CM-MKT-007, CM-NTF-003 (8, 9, by SMS, sent); CM-PAY-015, CM-PTN-008 (10, by pay, under); CM-B2B-002, CM-INV-005, CM-SHP-015 (11, by addresses, location, shipping); CM-ACC-001, CM-PAY-029 (12, by account, when).
- **Marketing:** CM-ANL-002 (13 to 19, by coupons); CM-MKT-014, CM-MKT-015 (13 to 16, 27, by name: marketing); CM-LOY-008, CM-PTN-008 (17 to 40, by code, under, تسويق); CM-ACC-005 (19, by multiple); CM-CAT-001, CM-INV-010 (20, 30, 31, by products); CM-MKT-013 (21, by name); CM-ACC-001 (22, 23, 30, by your store); CM-MKT-005, CM-LOY-004 (22, 25, by التسويق, program); CM-CNT-003, CM-PTN-001, CM-CAT-007 (23, by page, partner, image); CM-PAY-032 (24, by link); CM-ORD-003, CM-ORD-015 (25, by order status: what it sets it by, S5); CM-PTN-009 (26, by commission: the store's own commission period); CM-PTN-010 (28, by powered by: the checker's note, a partners' service, not Mushammir); CM-AIA-003 (28 to 30, by text, product: the AI recommends products, it writes no text); CM-CHK-002, CM-CHK-007, CM-CUS-001 (29, by cart, carts); CM-CHK-001 (30, by checkout, in reading); CM-MKT-001, CM-SFR-015, CM-CAT-012 (33, by promotion, show); CM-API-010, CM-MKT-016 (34, 37, by conditions, available); CM-MKT-018 (35, by offer); CM-LOY-007 (38, by reminder); CM-INV-009 (39, by priority).
- **Wallet, loyalty, gifting:** CM-PLN-006, CM-MKT-020 (41 to 43, by wallet: the store's own balance with Salla and the ads wallet, homonyms CM-LOY-001's note keeps apart); CM-SHP-017, CM-ORD-015, CM-ORD-003 (43, 44, by can, status, order); CM-PAY-025 (44, by credit); CM-CHK-008 (45, by buy); CM-API-009, CM-NTF-002, CM-AIA-003 (46, by notifications, such: staff notices and webhooks aren't these); CM-ANL-002 (47 to 53, by the id `loyalty-program`); CM-MKT-014 (47, by `loyalty_system_management`); CM-PTN-001, CM-OPS-001, CM-TRU-005 (47 to 53, by program, available, بيان); CM-SHP-014 (51, by how, set); CM-MKS-001, CM-ACC-008, CM-MKS-006 (53, 57, by markets, available: what it sets it by, S5); CM-INV-005, CM-STF-005, CM-SUP-005 (54, by `gift_system_management`, system); CM-B2B-007, CM-SFR-013 (56, by storefront); CM-CAT-001, CM-ORD-003 (58, by products, which); CM-API-003, CM-ORD-013, CM-SHP-015, CM-API-013 (59, by write, messages, own).
- **Blog and reviews:** CM-AIA-003 (60, 66, by blog, description); CM-ACC-001, CM-SHP-015 (63, by your store, whether); CM-ACC-003 (64, by under); CM-CUS-001, CM-STF-002, CM-ORD-013, CM-MKS-006 (65, 70, 71, 81, by customer, comment); CM-SFR-013 (66, by search: search results, not the store's search); CM-SHP-015 (67, 78, by carrier: the carriers' ratings are CM-SHP-022's); CM-ONB-002 (67, by access, restricted); CM-CNT-003 (70, 71, 75, 85, 86, 88, by page, pages); CM-CUS-002, CM-APP-011 (70, by تصنيف, category); CM-SFR-015, CM-INV-010 (71 to 73, 88, by display, product); CM-APP-002 (72, by app); CM-CAT-001 (74, 75, 83, 84, by products, add new); CM-ACC-003 (75, by مرتبطة); CM-ACC-001, CM-TRU-005 (76, 86, by your store, request); CM-ORD-007, CM-RET-004 (77, by طلب, request); CM-ACC-004, CM-SHP-004 (78, by شركة, rate); CM-SHP-022, CM-AIA-003 (80, by quality, rating, text); CM-PLN-002, CM-CAT-012 (82, 83, by متجر, value); CM-B2B-002, CM-API-013 (84, by users, control); CM-NTF-004, CM-MKT-007, CM-CUS-007 (87, by email, WhatsApp: the buyer contacts the store, no message is delivered); CM-MKT-023 (88, by customer recommendations, a homonym); CM-SFR-013 (89, by خيار); CM-CAT-007, CM-MKT-016 (90, by media, when); CM-CNT-004 (91, by comments: the reviews' likes, not the blog's).

## The checker's lines, read again

- **`CHANGES` line 37:** above; kept.
- **`NOTE` line 105: a footnote mark.** The asterisks of 'M* A****' are the masking's example, not a footnote.
- **`NOTE` line 33: entry 28's first lead CM-PTN-010 (by powered by) holds nothing.** Set aside: 'Powered by Mushammir' names Salla's AI (T4), not a partners' commerce service.
- **`NOTE` lines 2, 16, 49, 58, 65, 71 and 80: the containers** `/customers`, `/coupons`, `/wallet`, `/loyalty-program`, `/gift-system`, `/blog` and `/feedback`. Each section is placed on the capability its title names, as SA-23 placed the same settings links (S1), and its settings by their own entries. The checker doesn't flag the titled list headers (15, 21, 27, 32), which go on the capability their titles name (S2's second exception).
- No `NEW`.

## Problems with the brief or the script

- **The `if` conditions** (above) are the one thing the rebuilt entries still leave out that decides a placement. Five of this batch's scopes and two of its supports rest on them. A node's enclosing conditions, rendered as `if:` beside `features`, would spare every settings batch its bodies.
- **The checker's quotes:** a typographic apostrophe (’) inside a quote closes it, as an ASCII one does. 'the product’s average 5-star rating' and 'your store’s information pages' made a false NOTE, which I fixed by quoting the Arabic. Labels and descriptions with ’ ('You don’t have', 'store’s', 'it’s') can be quoted only around it.
- **`held_entries.py earlier` matches an id resolved as a translation key:** 46's `Notifications` printed the partners portal's and the notifications' lines, and 50's `General` printed CM-PTN-002's and CM-APP-002's. They are no lead.

The checker's last line for SA-50, after this file was written: `92 of 92 entries placed; 0 problems`.

## The coordinator's check (31 October 2026, after the batch)

- **One cell change, kept:** CM-MKT-023 gains `extension-point`. Products 'suggested by AI or by your store's apps' fill the platform's own checkout slot. The suggestions' sources are a lead.
- **The rules T1 to T8 stand,** and T1 and T2 are made a ruling (after SA-50): a section or list gated by a feature is a gate node, and an `if` on a store's feature or plan is a gate.
- **The build now renders those gates.** Each settings entry carries `if:`, the store gates of the `if`s it sits under, in the answer's identifiers ('not multi-countries-basic', 'plan plus or plan pro or plan team or plan special'). An `else` branch carries its condition's negation. A form's value or a query's state is not rendered.
  - **Ids changed:** 10 entries, re-keyed in SA-49 (2), SA-50 (8), SA-51 and SA-54.
  - **One entry split in two.** This batch's untitled Marketing list now stands apart from its plan-gated twin, the smart recommendations' list (SA-E-a4b5a6c6). The coordinator placed the twin on CM-MKT-023, `core`, with scope `plus;pro;team;special` (T3, T7).
  - **SA-51** takes the split twin of its own entry: Guest checkout's item under `multi-countries`.
- **The other open cases stand as placed:** 6, 20, 23, 38, 46, 78, 87, 88, 89 and 12.
- **The checker's notes:** the typographic apostrophe inside a quote and the masked name's asterisks are set aside. Node ids that render as translation keys (46, 50) are cosmetic.
- **Cost:** 22.8 million tokens over 104 requests, about 248,000 an entry. That is less than half SA-49's, with the prompt that narrowed what the agent reads. With the gates now rendered, the bodies are needed less still.
