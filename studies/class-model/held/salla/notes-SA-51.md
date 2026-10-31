# Held pass, Salla, batch SA-51: notes

92 entries (effort high), evidence at observed-sa@b0bd0b16, all of `settings-center` as rebuilt after SA-50 (one entry per node, every store's answer in it, with `if:`). Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-51`). Two top-level sections and the sub-pages that follow SA-50's sections:
- 1 to 22 Notifications (`/notifications`); 23 to 25 Installed apps (`/apps`);
- 26 to 43 the Blog's three sub-pages (`/blog/blogs.show_in_menu`, `blogs.allow_likes`, `blogs.homepage_title`); 44 to 50 the Checkout's Guest checkout (`/checkout/guest-checkout`);
- 51 to 76 the Marketing section's sub-pages: Multiple coupons (51 to 57), Marketing assets (58), Automatic welcome message (59 to 65), Status settings (66), Commission period (67), Offer priority (68 to 70), Cashback eligibility (71 to 76);
- 77 to 92 the Customers section's Login & registration options (`/customers/login_methods`).
- The fourteen bodies are the same bytes on all five stores (sha256 of `<label>/<section>.json` compared: notifications `13fcc71a…`, apps `0c4aaea4…`, the blog's `08eeb663…`, `12aba2cd…`, `14adcd4d…`, guest checkout `bbe4e95f…`, multiple coupons `ae9fef05…`, marketer assets `d90ae034…`, welcome email `15a59e13…`, status settings `3f014b09…`, commission period `cc753861…`, discount priorities `7c4216e2…`, cashback eligibility `687e3a8f…`, login methods `b78e1a39…`).

**Placed:** 71 entries on capabilities, none `new`, 21 `out`, in 122 lines: 62 `core`, 39 `shows`, 21 `out`. No `own-service`, `extension-point` or `outside`. One filler line (Google, Apple, X, Facebook, entry 89); four qualities (the coupons and offers allowed on a cart, 51, 55, 69, 70). Scope on 37 lines: `auth-v2` (16), `auth-v2;multi-countries` (8), `multi_coupon` (9), `multi-countries` (4).
- `shows`: every line of Multiple coupons (behind `multi_coupon`) and of Login & registration options (behind `auth-v2`), neither released on any held store; and the subjects the merchant's notices name (U1).
- **The checker prints no `CHANGES` line: no cell changes.**

**Sources read:** the brief and what it names; the evidence map; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's row for `settings-center`, `index/ledger-summary.tsv` and `index/ledger/settings-field.tsv`'s header; the selection row; B-extent's "Cells and evidence" and conventions; the rulings to their last section (read again when the file changed during the batch: the new ruling after SH-35 doesn't touch this structure); SA-48's, SA-49's and SA-50's notes, their rules S1 to S12, R1 to R9 and T1 to T8, and the coordinator's checks.
- **The bodies, read only where an entry left a column open:** `notifications.json` (one list or several, 2); `apps.json` (the header's radios, 24); the three blog sub-pages (which list holds the settings and which the Save button, 28, 31, 34, 37, 40, 43); `checkout~guest-checkout.json` (the conditions of 47 to 49); `coupons~multiple-coupons.json` (its whole content under `getFeatureVisibility multi_coupon`, which no entry renders, 51 to 57); `coupons~marketer-assets.json`, `~status-settings.json`, `~commission-period.json` (drawn by components, 58, 66, 67); `coupons~welcome-email.json` (63's disabled title, 64's request); `coupons~discount-priorities.json` (the two forms' conditions, 68 to 70); `coupons~cashback-eligibility.json` (74's statuses request); `customers~login_methods.json` (the market conditions, 78, 79, 91, 92).
- **To clarify only, each cited where a line rests on it:** `dashboard-features/*@en/items.jsonl` for `multi-countries` (line 541 on the demo store), `multi_coupon` (365), `auth-v2` (218) and `customize-login-for-multi-markets`; `dashboard-translations/{en,ar}/settings.json` for the Arabic quotes and the placeholders the entries leave out (63). The earlier batches' lines named by `held_entries.py earlier` (SA-7, SA-13, SA-14, SA-18, SA-23, SA-28, SA-33, SA-49, SA-50). No run page was needed: SA-33's plan gates already hold the stores' pages of `customers/login_methods`.

## The rules: S1 to S12, R1 to R9 and T1 to T8, kept, and what I added where they don't reach

I kept the earlier rules as the coordinator's checks and rulings left them: T1 for the login options' `features: auth-v2` (a section with features is a gate node over its content), T2 for `if: multi-countries`, S11 for sub-pages whose link is gated, S7 and R5 for the forms, S2, R4 and T7 for the lists. For the coordinator to align with SA-52 to SA-56:

- **U1. The store's own notifications** (the Notifications section, 1 to 22). Its ten toggles have the control `in_app`, each saved by `PATCH …/notifications/v1/inbox/preferences/<id>`: the notices the store receives in the dashboard's inbox ('Turn all store notifications on or off.', 'Get notified when a new order is placed.').
  - Each toggle is CM-NTF-002 `core`, notices to the store's staff, not CM-NTF-001's messages to customers. The section keeps its title's CM-NTF-001 (S1), and its one list, whose settings are all CM-NTF-002's, is a container there (S2's first exception).
  - What a notice is about takes a `shows` line on its capability, where the toggle's label or description names it: the cart (CM-CHK-002), the wishlist (CM-LOY-005), Salla Community and the platform's updates (CM-ONB-003), Salla Partners (CM-PTN-001), Salla Chat (CM-SUP-004). The notice itself is CM-NTF-002's, so the subject only shows.
  - Where the notice is itself the subject's thing, it takes that capability's `core`: 'Out of stock', an alert to the store on a product's quantity, is CM-INV-004's (its note: Salla's alert to the store when a product's quantity is low). 'New order' is CM-NTF-002's own example and takes no second line.
  - CM-NTF-002's note says Salla gives it no place of its own (a staff permission only). This section's page holds only the store's own notices, so the coordinator may revise the note. No cell changes.
- **U2. A sub-page's form and lists** (the blog's, guest checkout's, cashback's, the welcome message's, the login options'). The form is placed by S7 on the page's capability, or capabilities where the page is itself two things (blogs.show_in_menu: CM-CNT-004 and CM-CNT-005, as SA-50's T5 placed its link; blogs.homepage_title: CM-CNT-004 and CM-CNT-007, as SA-50 placed its link). The list holding the settings is a container on the same capabilities (S2's first exception, T7). The list that holds only the Save button (`utils:form.submit_button.save`, or 'Save changes') is `out`, a UI string.
- **U3. A sub-page drawn whole by a component that is no node** (58 Marketing assets, `MarketingAssetsComponent`; 66 Status settings, `AttributionStatusComponent`; 67 Commission period, `AttributionTimeComponent`, all of `@salla.sa/ui-merchant-partner-marketing`; 23's list `apps:installed-list`): a container on its title's capability, as the item that links to it was placed, with the component in `reading`.
- **U4. An `if` the rendering leaves out:** `getFeatureVisibility multi_coupon` wraps the whole Multiple coupons sub-page (51 to 57), and no entry carries it (the rebuilt `if:` renders `useFeature`, as 47 and 49 show, and plan conditions, but not this). By T2 it is the nodes' gate, so `multi_coupon` is their scope; it isn't released on any held store, so `shows` (S4), as SA-50 placed the item that links to the page (SA-E-00033b7e).
- **U5. A query gated by a store feature.** The markets list is read by `scopes?…`, a query whose `enabled` is `getFeatureState multi-countries`, and a node that shows only when that query returns the store's markets can't show without the feature:
  - these are 70 (Offer priority's per-market form) and 78, 79, 91, 92 (the login options' market select, revert form and per-market form);
  - I read the feature as their gate, so `multi-countries` is in their scope (T2), and the store's having active markets is in `reading` (M-11);
  - if the coordinator keeps T2 to an `if` node, the scope moves to `reading` and these lines keep `auth-v2` alone (78, 79, 91, 92) or none (70).
- **U6. A per-market version of a setting:** the markets are what it sets it by (S5), so no CM-MKS-001 line (47, 49, 68, 70, as SA-50 placed the loyalty programme's Markets).
  - The exception is where CM-MKS-001's cell already names the same per-market thing: its flag `customize-login-for-multi-markets` (released, plans pro and special) is the login options set per market.
  - So 78, 79, 91 and 92 take a CM-MKS-001 line, `shows` behind `auth-v2` (rule 2: a cell's term names the same thing).
- **U7. A form whose key names another capability's thing** (S7's 'unless'): Offer priority's `marketing_settings.offers_settings_rules` sets the number of special offers on a cart ('Create a special offer first…'), so 69 and 70 take CM-MKT-003 `core` beside the page's CM-MKT-001. The limit, 1 to 5, is CM-MKT-003's quality.
- **U8. An item that names a market's toggle by the control's name** (49, `name: markets`) is read from the body: each toggle is labelled by a market's name from the scopes answer, which isn't held.

## `new` things

None. Each entry's thing is already a capability's: the sub-pages by the concern map's settings keys (SA-S-1703 to SA-S-1714) and the items SA-49 and SA-50 placed on them; the notices by CM-NTF-002; the login methods by CM-CUS-010, CM-CUS-011 and CM-CUS-013. Searched with `caps --terms`, besides the leads:
- inbox, notification center, in-app, مركز الإشعارات, push notification, low stock, stock alert, out of stock, نفاد المخزون, تنبيه, platform updates, التحديثات, required actions, الإجراءات المطلوبة;
- moderation, comment, تعليق, meta description, وصف الصفحة, installed, status filter;
- combine, combination, stacking, multiple coupons, تعدد الكوبونات, دمج, discount priority, أولوية, voucher, القسائم, loyalty coupon, كوبون الولاء;
- social login, تسجيل الدخول عبر الحسابات الاجتماعية, OTP, رمز تحقق, one-time, identity provider, Google, Facebook, email login, welcome message, رسالة ترحيبية, marketing assets, المرفقات التسويقية, attribution, commission period, offers limit.

## The checker's lines, read again

- **No `CHANGES`:** every line falls on a cell that already holds its support. Two lines bear on cells that are thin on Salla, without changing them:
  - **89, CM-CUS-011 (not-stated):** 'Let customers sign in with Google, Apple, X, or Facebook. Providers are configured at platform level; this switch controls availability.' This is the first statement held that names the buyers' identity providers, where the cell held only the unreleased flag `sso-login`. It is `shows`, behind `auth-v2`, so the cell stays not-stated. Google, Apple, X and Facebook are its fillers, the parties its words name as signing buyers in. If `auth-v2` is released to a held store, this line becomes `core` and the cell changes.
  - **85, CM-CUS-013:** 'إرسال رمز تحقق لمرة واحدة (OTP) إلى رقم جوال العميل عبر واتساب.' is the first held statement that describes the cell's thing, which its reading had from its names alone. It is `shows`, behind `auth-v2`.
- **`NOTE` lines 12, 20, 23: `core` on a product named with the platform's brand** (Salla Community, Salla Partners, Salla Chat, on CM-NTF-002). Each line's thing is the notice, the platform's own setting, and the brand names the notice's subject, which takes its own `shows` line (U1). No maker is stated or needed.
- **`NOTE` on the containers:**
  - the sub-pages `/blog/blogs.show_in_menu` and `/blog/blogs.allow_likes`, Guest checkout, Multiple coupons, Automatic welcome message, Offer priority, Cashback eligibility and Login & registration options, each placed on the capability of the item that links to it (S1);
  - their forms, placed by the key they save under (S7, R5, U7).

  The checker's 'holds 1 other entries' on each field of the Notifications section is its `s:base-url`, which is `out`.
- No `NEW`.

## Entries I couldn't tell, and what would settle each

- **5, 7, 9, 15, 17, 21: the notices' subjects as `shows` lines** (U1). If the coordinator reads a notice as CM-NTF-002's alone, the six `shows` lines go. No cell changes. What the Salla Partners and Salla Chat notices announce isn't stated (no description); an inbox's notices would settle it.
- **13, 'Out of stock', `core` on CM-INV-004** beside CM-NTF-002. The cell is low stock, and this notice is sent when a product runs out. If the coordinator keeps CM-INV-004 to a low-stock threshold, the line goes. No cell changes. The unused key `notifications#low-stock.label`, 'Low stock notification', suggests both kinds are among the store's notices (below).
- **2, the Notifications list, on CM-NTF-002** (S2's first exception), where the section is CM-NTF-001's by its title. If the coordinator reads the one list as standing for the section, it takes CM-NTF-001.
- **24, the Installed apps header, `out`:** a search box and radios of the apps' statuses from `marketplace/v2/apps/installed/statuses`, whose answer isn't held. As SA-49 placed the Manage stores header (S8). If the statuses name something (a trial, a subscription), the answer would show it.
- **58, 66, 67 on CM-MKT-014 alone:**
  - they are drawn by components of `@salla.sa/ui-merchant-partner-marketing`, the app CM-PTN-009's note names as 'the merchant's side' of the partners' affiliates, and the marketing assets 'appear on your Salla Partners store page' (SA-50's item, SA-E-e7471cab);
  - I kept CM-MKT-014 alone, as SA-50 placed the items and the concern map the keys (SA-S-1708, SA-S-1710, SA-S-1711), since CM-PTN-009's cell cites the app's other pages (marketing/affiliates, influencers, experts, marketplace), not these;
  - a CM-PTN-009 line on 58 is the alternative. No cell changes either way;
  - CM-MKT-008, sales attribution, which the components' names suggest, keeps `affiliates-attribution-settings` in CM-MKT-014 by its own reading, so it takes no line.
- **69, 70: CM-MKT-003 beside CM-MKT-001** (U7). The rules the forms show also name coupons, 'Coupons are applied first in the cart, except fixed-price offers, which take priority.', which I read as the discounts ordered among themselves, CM-MKT-001's. A CM-MKT-002 line is the alternative. No cell changes.
- **51, the Multiple coupons page's application order:** vouchers, abandoned-cart coupons ('Only one abandoned-cart coupon per cart', written as a quality), general coupons, and loyalty coupons ('calculated from the cart subtotal'). I read them as what the rule orders, in `reading`, and gave the abandoned-cart and loyalty coupons their lines only where a setting sets them (56: CM-LOY-004; 57: CM-MKT-022). What the 'Vouchers' / 'القسائم' are isn't stated: they show only where the store's rules hold some.
- **U5's scopes** (70, 78, 79, 91, 92) and **U6's CM-MKS-001 lines** (78, 79, 91, 92): above, with what each alternative changes. No cell changes.
- **30 and 41, 42: the second lines** (CM-CNT-004 on the menu title; CM-CNT-004 on the blog homepage's SEO title and description). Each field is the blog's own and the second capability's (menu, SEO). If the coordinator keeps one line per field, the CM-CNT-004 lines go.

## A structure whose items and sources disagree

- **`if:` leaves out two kinds of store gate:**
  - `getFeatureVisibility`, which wraps the whole Multiple coupons page (51 to 57), as it gates SA-50's item SA-E-00033b7e;
  - a query's `enabled: getFeatureState multi-countries`, which decides whether the market nodes can show (70, 78, 79, 91, 92).

  The checker can't see either. The build could render the first as it renders `useFeature`, and the second as `if: multi-countries` on the nodes that read the query's data.
- **A control's name rendered as a translation:** 49's toggle `name: markets` renders as 'Markets (الأسواق المتعددة) [markets]', as SA-49 and SA-50 found ids resolved as keys. The toggle's own label is each market's name, from an answer not held.
- **One entry, several nodes:**
  - 53 holds both lists of the Multiple coupons page;
  - 81 holds the SMS and email lists of both login forms (the store-wide and the per-market one);
  - 82 to 90 each hold the same method's node in both forms. Their scope is the one condition both share (`auth-v2`), the per-market twin named in `reading`.
- **Pages drawn by components that are no node** (U3): `apps:installed-list`, `MarketingAssetsComponent`, `AttributionStatusComponent`, `AttributionTimeComponent`, and `coupons:scope-view` in Offer priority. Their strings are in `settings.json` under keys no body uses (below).
- **Keys of another namespace:** `utils:form.submit_button.save`, `.saved` and `.error` (31, 37, 43, 50, 59, 76, 77, 90), unresolved.

## For the second stage: what the sources state that no entry holds

- **`dashboard-translations/en/settings.json` (and `ar`), keys no held body uses,** each a lead for the cell named:
  - **CM-NTF-002:** a table of the store's notices by channel, `notifications#table.header.notification`, `.email` and `.in_app` ('Notification type', 'Email', 'App notifications'), with notice types no body holds: `notifications#cod-payments.label` 'Cash on delivery', `#electronic-payments.label` 'Online payments', `#customer-question.label` 'Customer question', `#product-rating.label` 'Product review', `#store-rating.label` 'Store review', `#shipping-rating.label` 'Carrier review', `#staff-activation.label` 'Staff account activation';
  - **CM-INV-004:** `notifications#low-stock.label`, 'Low stock notification';
  - **CM-APP-001:** the installed apps' list, `apps#table.app`, `.rating`, `.rating_empty` ('Not rated'), `.details`, and `apps#list.empty` ('No apps installed');
  - **CM-MKT-014:** the marketing assets' limits, `coupons/marketer-assets#attachments.description`, 'Supported files: jpg, png, gif, pdf, max 2 MB.', with `#error.size` and `#error.type`; and `#youtube.add`, 'Or add a YouTube link', for its qualities;
  - **CM-MKT-002:** `coupons/multiple-coupons#order.tooltip`, 'A fixed order that cannot be changed, so every cart gives the customer the same result.';
  - **CM-MKT-003:** `coupons/discount-priorities#max-discounts.label`, 'Maximum number of offers applied'; **CM-LOY-003:** `coupons/cashback-eligibility#max-discounts.label`, 'Select order statuses for cashback eligibility'.
- **Answers the bodies request and no structure holds:**
  - `marketplace/v2/apps/installed/statuses` (24), which would name the installed apps' statuses;
  - `/admin/v2/marketing/cashback_statuses` (74), which would name the order statuses that grant cashback;
  - `settings/fields/customers.login_methods`, whose `whatsapp_available` and `social_available` say whether a store's WhatsApp service and the platform's social providers are set up (84, 88);
  - `scopes?…` (47, 49, 70, 78), the store's markets;
  - the notifications' inbox preferences (1 to 22), each store's own values.
- **The Multiple coupons and Login & registration options pages on a store that has their features:** no held store has `multi_coupon` or `auth-v2` released. A store that has them would make lines 51 to 57 and 77 to 92 `core`, and CM-CUS-011's cell would then be held from 89.

## Leads set aside as no leads

- **Notifications:** CM-API-009 (1 to 22, by notifications: webhooks to other services, not the store's inbox); CM-API-013 (3, by all, control); CM-APP-012 (5, by platform, receive, update); CM-MKT-016 (7, 13: the buyers' back-in-stock alerts, not the store's); CM-MKT-017 (8, 13, 21, 22: the buyers' wishlist notifications, not the store's); CM-LOY-008 (7, 11, 21, by get, when); CM-PAY-029 (11, by order, when, استلام); CM-INV-001 and CM-ANL-002 (13, 14, by stock: CM-INV-004, its child, is the alert); CM-PTN-008 (17, by salla, under).
- **Installed apps:** CM-APP-004 (23 to 25, by app, installed: lifecycle events to apps); CM-SFR-013 and CM-CNT-007 (24, by search, بحث).
- **Blog:** CM-AIA-003 (26, 30, 31, 38 to 43, by blog, text, seo); CM-ACC-003 (29, by under, قايمة); CM-SUP-001 and CM-ORD-013 (32 to 37, by comments: the blog's comments are the blog's); CM-CNT-003 (41, 42, by page: the blog's homepage isn't a store page).
- **Guest checkout:** CM-SFR-012 (44 to 50, by checkout); CM-CHK-008 (44 to 50, by checkout, شراء); CM-MKS-001 (47 to 49, by markets, multi-countries: what it sets it by, U6); CM-ACC-001, CM-MKS-006, CM-SFR-015 (48, by your store, market, how); CM-LOY-004 (49, by markets).
- **Marketing's sub-pages:** CM-CHK-002 (51, 55, 57, by cart, السلات); CM-ACC-006 (51, by general); CM-ACC-005 (51, 55, by multiple, one); CM-ANL-002 (51 to 76, by coupons); CM-PTN-001 (54, by support: Salla's support named to turn it off, in reading); CM-EVO-001, CM-API-013 (54 to 57, by enable, control); CM-API-005 (55, by limit); CM-POS-001 and CM-CHK-010 (56, by point, cart); CM-PAY-029 (57, by own, when); CM-MKT-005, CM-MKT-007 (58, by marketing); CM-PAY-032 and CM-LOY-008 (62, by link, each); CM-CNT-003, CM-AIA-003 (64, by content); CM-PAY-014 (65, by save); CM-ORD-015 (66, by status); CM-PLN-003, CM-PTN-008 (67, by commission: the store's commission period to its affiliates); CM-MKT-018 (68, by offer: bank offers aren't named); CM-API-010, CM-ORD-010, CM-API-013 (69, 70, by conditions, how many); CM-ORD-003, CM-ORD-010, CM-LOY-008 (74, by order statuses: what it sets it by, S5).
- **Login options:** CM-ACC-006 (77, 79, 91, by store_setting_edit_setting, اعدادات المتجر: the permission and the store's defaults); CM-NTF-004, CM-NTF-003, CM-MKT-007 (77, 79, 82, 85, 87, by SMS, email, WhatsApp: sign-in codes are CM-CUS-010's, as CM-NTF-004's note says); CM-CUS-007 (77, 79, 84, by email, WhatsApp: no consent named); CM-TRU-017 (77, by access, request); CM-TAX-003 (78 to 92, by registration, تسجيل); CM-CUS-001, CM-CUS-003 (80, 92, by customers); CM-MKS-004, CM-MKS-009, CM-ONB-001 (83, 86, by countries, country selector: what it sets the method by, S5); CM-ACC-001 (84, 87, by your store, account); CM-TRU-001 (84, 87, by login, sign: the admin's sign-in, not the buyer's); CM-CHK-001, CM-SFR-012 (88, by checkout).

## Problems with the brief or the script

- **`if:`** leaves out `getFeatureVisibility` and a query's `enabled` (above). The scope and support of nine lines (entries 51 to 57) rest on the first, and the scope of ten lines (entries 70, 78, 79, 91, 92) on the second.
- **`held_entries.py earlier` matches control and node names that are common words:** `market`, `limit`, `scopes`, `statuses`, and the ids `updates`, `community`, `partners`, `actions`. They printed 73 lines of reports, the partners' portal and the order statuses, none of them leads.

The checker's last line for SA-51, after this file was written: `92 of 92 entries placed; 0 problems`.

## The coordinator's check (31 October 2026, after the batch)

- **No cell changes and no new things.** U1 to U8 stand for SA-52 to SA-56.
- **U1's six `shows` lines on what each notice is about are dropped:** platform updates, the cart, Salla Community, Salla Partners, Salla Chat and the wishlist. A toggle's own thing is the notice (CM-NTF-002), and the rest is named in passing (the ruling after SA-41). 'Out of stock' keeps CM-INV-004 `core`, because its notice is the stock alert itself.
- **U4 and U5 stand.** `getFeatureVisibility`, and a query enabled by a store feature, are gates on the store (the ruling after SA-50).
- **Leads:**
  - CM-CUS-011 (the buyers' identity providers) and CM-CUS-013 (a one-time code over WhatsApp) have their first held statements, behind `auth-v2`, which no held store has.
  - CM-NTF-002's note says Salla gives the merchant's notices no place of their own, but this section suggests otherwise. It is read again at Salla's amendment.
- **`held_entries.py earlier`** no longer takes common words (`market`, `limit`, `scopes`, `statuses` and the like) as an entry's keys.
- **Cost:** 17.1 million tokens over 80 requests, about 186,000 an entry.
