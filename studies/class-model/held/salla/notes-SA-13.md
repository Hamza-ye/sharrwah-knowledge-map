# Held pass, Salla, batch SA-13: notes

87 entries of `dashboard-app-routes` (items at items.jsonl lines 2866 to 3092: the apps shipping, starter-kit, themes, ticketing-system, users, utils, whatsapp, widgets, platform and billing). Evidence at observed-sa@b0bd0b163.

**Placed:** 82 entries on capabilities or new things, in 97 lines; 5 `out`, in 5 lines. 102 lines in all.
- 77 entries only on capabilities, 4 only on new things (32, 33, 65, 66), and 1 on both (64). The 5 `out` are 41 (the themes app's `/`), 52 (the themes app's 404 catch-all), 67 (the WhatsApp app's `/`), 68 (a VML shape's path) and 75 (engine.io's client options).
- 15 entries take two lines: 5, 14, 31, 34, 46, 51, 58, 59, 64, 69, 77, 79, 81, 84, 86.
- 73 lines support `core` and 24 `shows`. There is no `own-service`, `extension-point`, filler or quality.
- Scope on 35 entries, each a store feature the route's own guard names, read from the page's chunk: `shipping-routes`, `shipping-profiles`, `shipping-new-pages`, `shipping-ticket-system`, `delivery-promises`, `shipping-carrier-pickup`, `shipping-fulfillment-centers`, `landing-pages`, `user-advance-management`, `app_pos`, `settings-control-panel` and `billing-native`. Staff permissions are named in `reading` only.

Entry numbers below are the batch's order (`held_entries.py show --batch SA-13`). Bundles are cited by their record. The app bundles are in `raw/runs/20261008T120306Z-dashboard-bundles-chunks1/fetch.warc.gz`: shipping @37241188, starter-kit @37312399, themes @37423558, ticketing @37545861, users @39272890, utils @39521943, whatsapp @40133643 and widgets @42163022. The page chunks are in `raw/runs/20261008T121539Z-dashboard-bundles-chunks2/fetch.warc.gz`, at the offsets the readings give.

## How I read the entries

I kept SA-7's eight rules and the coordinator's checks after SA-8 to SA-12. I decided from `show --code 300`. Where the router gave only a lazy element (`Dd`, `Pl`, `$G`), I read its import in the app bundle, then that chunk's guard and API calls (`held_index.py` for each chunk's record, `warc_text.py` to print it).
- **A guard of the page's own chunk is the route's gate.** Most apps here wrap each page in `guard({feature, permission, mode:"page"})`. Its `feature` is the scope; its `permission` goes in `reading`.
- **A guard on an unreleased feature makes the route `shows`.** The features list (`structures/salla/dashboard-features/*@en/items.jsonl`) gives these released false on every store held: `shipping-profiles` (8 to 10), `delivery-promises` (25 to 27), `shipping-carrier-pickup` (28 to 30) and `shipping-fulfillment-centers` (34). The page isn't offered, so the line is `shows`, as the flag rule reads, with the feature as scope.
- **A feature named on a button or a field, not on the page, isn't the route's scope.** Examples: free shipping's route and customer-group fields (13), the themes page's buy button `theme-purchases` (42), the staff list's add button `user-advance-management` (56).
- **A plan read only from a run step or a locale goes in `reading`** (SA-7's rule 7). Examples: the rules page's 'upgrade to Special or Pro' (18), and the profiles' 'Available for Pro and Special plans'.
- **Leads set aside as common words:** CM-B2B-002 (`companies`, `users`), CM-PTN-003 and CM-PAY-020 (`transactions`), CM-SHP-023 (`rule`), CM-OPS-005 (`logs`), CM-SHP-007, CM-SHP-019 and CM-SHP-004 (`pickup`, `carrier`, `delivery`), CM-ANL-006 (`reports`), CM-CNT-003 (`pages`), CM-SUP-002 (`review requests`, against `preview-requests`), CM-APP-002 and CM-CHN-003 (`marketplace`), CM-STF-003 (`roles`), CM-PAY-025 (`credit`), CM-PAY-030 and CM-PAY-016 (`bank-transfers`: Salla's bills, not the buyer's payment), CM-TAX-005 (`vat-invoices`: Salla's tax invoices to the store, not the store's to its buyers), and CM-CHK-007 and CM-CHK-002 (the WhatsApp app's abandoned carts).

## The new things

1. **Bullet Delivery** (التوصيل السريع; the locale calls it Express Delivery), entries 32 and 33, `core`, no scope. SA-22 and SA-32 named the same address `new:Bullet Delivery`, so I named it the same way.
   - **Its place of its own:** the route `/shipping/bullet-delivery` and its settings `/update`, and the nav entry.
   - **What the locale says it is** (`structures/salla/dashboard-translations/en/shipping.json`, `express_delivery.*`): delivery from the store's branches within a radius, by Salla-approved providers or the store's own couriers. Examples: 'Deliver customer orders within two hours across 23 cities — Salla automatically selects the best provider for each order.' and 'Choose an external carrier, your in-house couriers, or both.'
   - **Proposed:** domain C, area SHP, parent CM-SHP-006, since SA-32 proposed CM-SHP-001. CM-SHP-008, the store's own delivery from its locations, is the nearest capability, but the platform's providers do this delivery.
   - **Its guard:** each entry stands for two route objects. One sits inside `expressDeliveryGuard-Ce41uYPh.js` (@14131274), which sends the store to /shipping unless its express statistics say it is activated, a condition on the store's own data. The other sits outside it. The page chunks name no feature. SA-32's gate `shipping-routes` comes from the derived plan-gates table, not from the bundle.
   - **Searched:** express; bullet; same-day; سريع; التوصيل السريع; delivery promise; local delivery.
2. **Custom Product Fields** (الحقول المخصصة), entries 64, 65 and 66, `core`. I used the same name as SA-32.
   - **What the routes are:** the routes of the custom fields component of the shared app `ui-merchant-utils`, exported as `cc` (@39521943). Its entity is `product` by default, its fields are read from `/metadata/?entity=`, and its paths are relative to the basePath of the app that uses it.
   - **Its place of its own:** `/products/options/custom-fields/*` (SA-32), which the products app routes at the constant `T.options.customFields` (items.jsonl line 2378).
   - **Unsure:** another app may pass another entity. The orders' custom fields are CM-CHK-009's, from the orders app (SA-11). Whether the products and orders apps use this component would settle it.

The carrier pickup, which I first drafted as new, is CM-SHP-009's: its cell cites the flag `shipping-carrier-pickup` as `shows`, and SA-32 placed the address there.

## Entries I couldn't tell, and what would settle each

- **64, the utils app's `/`.** It is two routes: the custom fields' empty pane, which has no guard, and the settings pane's root, which is guarded by `settings-control-panel` (as `Guarded_SettingsPane`, or as `SettingsModal` behind the flag). The brief says an entry's lines share one scope, so both lines carry `settings-control-panel`. That is right for CM-ACC-006 only. See "Problems" below.
- **14, `/shipping/operations` (Shipping performance).** Two lines, `core`: CM-SHP-002, since the page tracks shipping through Salla's labels, and CM-ANL-001, as SA-22 and SA-32 placed the address.
- **16, `/shipping/reports`.** Placed on CM-ANL-002, since the cell's note keeps kinds of report there and its cell holds a payments-and-shipments report. SA-22 and SA-32 placed the address on CM-ANL-001. The coordinator may want one of the two.
- **24, `/shipping/awb-proposals`.** Its chunk only posts to `shipping/awb-proposals` and returns to /shipping with the answer's message. Placed on CM-SHP-002 (labels, AWB). What a proposal is isn't stated: a run that opens it with a store that ships would settle it.
- **5, 31, `/shipping/old` and `/old/*`.** These are the older carriers' page of Salla's labels (`shipping-CDeD49Hl.js`; `20261008T131847Z-sweep-merchant-routes-ar/steps/101.text.txt`). Each takes two lines, CM-SHP-015 and CM-SHP-002. Whether the registry still sends merchants there isn't held.
- **25, the delivery promises' list.** Its guard gates by the plans the flag `delivery-promises` lists, where it lists some (pro, special), and by the feature otherwise (`deliveryPromises-CkhCCMzL.js`, @14067897). The flag is unreleased, so I placed it `shows`, with the scope `delivery-promises`. SA-32 wrote the scope `pro;special`. `core` with `pro;special` is the alternative, if the plan gate lets a Pro store in. A Pro store's run at the address would settle it.
- **34, `/shipping/fulfillment-centers`.** 'Salla warehouses', 'You sell—we store, pack, and deliver your products.'. Two `shows` lines:
  - CM-SHP-012, the platform's own fulfilment network, whose cell held nothing (a CHANGES line);
  - CM-SHP-011, whose cell cites the same flag, as SA-32 placed it.

  The locale's 'Booking will be available when the fulfillment backend is connected.' says it isn't finished.
- **35 to 40, `ui-merchant-starter-kit` v0.1.3-beta-39.** The import map names it and the registry doesn't serve it. Its pages copy the staff pages (UsersPage, UserRoles, CreateUser, `users:` keys). I placed it `shows` on CM-STF-001 and CM-STF-002, as SA-7 placed the beta `marketing-camping` and SA-9 an unserved module. `out`, as a scaffold like `ui-merchant-{app-name}`, is the alternative: a starter kit for apps, by its name.
- **46, `/themes/preview-requests`.** 'Custom theme requests': an outside theme developer asks to preview its theme on the store, and the store accepts or rejects (`allow_preview_requests`). Two lines:
  - CM-SFR-001 `core`, the store's own page and setting;
  - CM-SFR-002 `shows`, what a partner asks of a merchant (the ruling on S7).

  CM-SFR-003 `extension-point` is the alternative for the second line, if these developers' themes are the marketplace's.
- **45, `/themes/orders-center`.** It reads `marketplace/themes/orders-center`, so I read it as the store's orders from the Theme Marketplace, on CM-SFR-003. It isn't the partners' Orders Center (CM-PTN-005).
- **51, `/themes/marketplace/:id/new`.** It creates a version of the store's theme from a marketplace theme ('Error creating version:') and returns to /themes. Two lines: CM-SFR-001 (the theme's versions, its plan line إنشاء نسخ متعددة من الثيم) and CM-SFR-003.
- **69 to 73, the WhatsApp ads app** (`/marketing/ads/whatsapp`, served). I placed them `shows`, as the coordinator kept SA-11's engage app: the page shows its keys untranslated ('content-design.engage-design', `20261008T133523Z-sweep-demo-store-en/steps/282.text.txt`).
  - 69 takes CM-MKT-022, since it is an abandoned-cart message with a discount, and CM-MKT-007.
  - 70 to 73 are breadcrumb labels with no page, placed with the app's own thing, as SA-7 and SA-11 placed the same labels.
- **79, 84, the billing app's tax invoices.** 'Access tax invoices for all your Salla purchases. Invoices are issued automatically on the 15th of each month.' These are Salla's own invoices for the tax on its charges, so `core` on CM-PLN-007 (a CHANGES line). `shows` is the alternative, if the coordinator reads CM-PLN-007 as the tax itself, which the page doesn't state.
- **77, 81, 86, the payment schedule and the bank transfers** take CM-PLN-005 beside CM-PLN-004, as SA-10's notes read the same locale.
- **63, `/users/targets`.** Its guard names `app_pos` and the permission `order_management`. Placed on CM-STF-004, with `app_pos` as scope. SA-32's rule 7 gave the gate its own CM-POS-001 line; I gave none, since the brief makes the gate a scope. 61 and 62 (`user-advance-management`) are the same case against SA-32's CM-STF-001 line. The coordinator may align them.
- **58, 59, a staff member's registered devices and passkeys.** CM-STF-001 and CM-TRU-001, as SA-7's rule 8 places passkeys. CM-ACC-001's Registered devices is the owner's own profile page.

## The CHANGES lines

- **CM-PLN-007@salla gains core** (79, 84). Kept, a reading, above.
- **CM-SHP-012@salla becomes held** (34), by a `shows` line only, so the cell stays without a placement. Kept.

## Checker notes I read again

- **Containers by path** (`shipping`, `shipping/setting`, `shipping/setting/routes` and `/profiles`, `shipping/old`, `shipping/delivery-promises`, `shipping/carrier-pickup`, `themes/marketplace`, `users/edit/:userId`, `users/roles`). Each is placed on the capability of its own page, which is its children's too, or theirs one by one.
- **First leads whose cell holds nothing.** CM-B2B-002 (8 lines) is the word `users` or `companies`: staff and carriers, not business buyers. CM-SHP-023 (18) is the word `rule`: the page is shipping restrictions, and nothing names a rules engine. CM-PAY-025 (80, 85) is credit notes on Salla's bills, not business credit. No line.
- **New things whose entries have leads.** Bullet Delivery's leads (CM-SHP-001, CM-SHP-018, CM-SHP-019) were read: none holds a delivery by the platform's providers from the branches.

## What a source or run step states that no entry holds (for the second stage)

- **CM-SHP-005 (order routing, holds nothing):** the shipping settings' 'تحديد المستودع تلقائيًا حسب مدينة العميل' (`20261008T131847Z-sweep-merchant-routes-ar/steps/107.text.txt`), which chooses the warehouse by the customer's city.
- **CM-SHP-001, CM-SHP-015, CM-INV-001, CM-ORD-001:** the same page's other lines, cut off in the print:
  - 'التحقق من رقم جوال المستلم حسب دولة الشحن';
  - 'السماح لشركات الشحن بتغيير حالة الطلب', 'تتيح بعض شركات الشحن مثل فاستلو وسلاسة خاصية تحديث حالة الطلبات تلقائيًا حسب حالة الشحنة.';
  - 'السماح لشركات الشحن بمزامنة المخزون', naming ديجيباكس، إسناد، وتراك;
  - 'عرض مندوب واحد عند تطابق رسوم الشحن';
  - 'إرسال تفاصيل المنتجات ضمن مجموعة منتجات'.

  The carriers named are fillers, if placed.
- **CM-SHP-016 (what a route is, which its cell says isn't stated):** the profiles' locale ties routes, rules and profiles together (`shipping.json`, `ShippingProfilesPage.*`):
  - 'Activate shipping routes to disable shipping rules and apply the routes defined below in your store.';
  - 'Shipping rules will be discontinued soon. Shipping profiles are the improved system to manage shipping rules in your store.';
  - 'Automatically assign the right shipping carrier to each order.';
  - 'Set order limits for each carrier, by file or by store.';
  - 'Upgrade to the Special plan to use priority-based shipping profiles.'
- **CM-PAY-029, CM-SHP-002:** 'Cash on delivery is available for SAR 20–1,000 orders with Salla Shipping Labels.' (`ShippingProfilesPage.cod-fee-note`), a quality.
- **CM-SHP-002, CM-PLN-005, CM-PLN-006:** the postpaid labels' terms (`awb-postpaid.terms-*`):
  - 'Salla grants you a specific limit for issuing AWBs; exceeding it requires payment to continue.';
  - 'Outstanding amounts are automatically deducted from your store wallet or upcoming sales via (Salla Pay).';
  - 'Issued AWBs are subject to the return policy of the contracted shipping companies.'
- **CM-SHP-008, CM-APP-007:** the couriers' and express delivery's promotion of Tayaar, 'Manage your courier fleet with Tayaar' and 'Exclusive offer: 50 SAR free credit' (`CouriersPage.tayar-banner.promo-title`, `express_delivery.dashboard.tayar_offer_badge`). The shipping app's constant `TAYAR_EMBEDDED_APP` is `tayar-embedded-app`. Tayaar's maker isn't stated: a gap.
- **Bullet Delivery and CM-SHP-018:**
  - 'This duration is preset to support the express delivery promise for Salla Shipping Labels and can’t be changed.' (`express_delivery.form.delivery_time_locked_hint`);
  - '7 in 10 similar Salla stores have enabled express delivery across all their branches — join them.';
  - 'This delivery promise is managed in express delivery settings'.
- **CM-SHP-012:** 'For a monthly cost estimate, contact <sales>sales</sales> for real-time demand insights and better accuracy.' and 'Booking will be available when the fulfillment backend is connected.' (`fulfillment-centers.*`).
- **CM-TAX-001, CM-TAX-007:** the shipping app also routes `/payments/taxes` and `/payments/taxes/:id` at the constant `Ro` (taxRecordTable, taxRecordManagement; bundle @37241188), which are not entries here. The locale has 'Install ZATCA Integration app' (`tax.title`), and the app's constants include `tax-profiles` and `tax-profiles-disable-usa-country`.
- **CM-PLN-004:** tax invoices 'issued automatically on the 15th of each month' (`billing.json`, `invoices.vat_invoices.description`), a quality, and the late instalment's 'We couldn’t collect the scheduled installment for your {{planName}} plan, and you’ve lost access to the following features:' (`plans.downgrade.late_installment_desc`).
- **CM-PTN-005 or CM-SFR-002:** 'Request a custom theme through trusted developers' (`themes-marketplace-monorepo.json`, `preview_requests.placeholder.description`).

## A structure whose items and sources disagree

None in the values. Three observations:
- Entries 32 and 33 each stand for two route objects with one element (lines 2899 and 2901, 2900 and 2902), one inside a layout guard and one outside. The router lists both.
- The themes app's `/` (41) and the WhatsApp app's `/` (67) hold only cookie-library objects. The starter kit's `/` (35) holds one of them and a route.
- The shipping app's `/payments/taxes` routes have a constant path, so they reach no entry (above).

## Problems with the brief or the script

- **"An entry's lines share one scope"** doesn't fit an entry that stands for two routes with different gates (64): the custom fields' route has none, and the settings pane's has `settings-control-panel`. I gave both lines the second and said so in the reading. The coordinator may want a route's own gate to rule where an entry stands for several routes.
- **`show --code 300`** shows a lazy element's name, not the guard inside its chunk. Here most gates sit in the chunk (`guard({feature,…})(page)`), so I opened about 45 chunks, each once, in one or two commands per app. If `show` printed each element's import and its chunk's guard, most of these lookups would be spared.

## The coordinator's check (31 October 2026, after the batch)

- **The cells this batch changes stand:**
  - CM-PLN-007 gains `core`: the billing app's tax invoices, 'Access tax invoices for all your Salla purchases…', Salla's invoices for the tax on its own charges;
  - CM-SHP-012 is held by a `shows` line: 'Salla warehouses', 'You sell—we store, pack, and deliver your products.', behind an unreleased feature.
- **`/shipping/reports` is CM-ANL-002's,** reports being the child CM-ANL-001 holds (M-6). SA-22's and SA-32's lines for the address move there too. `/shipping/operations` stays on CM-ANL-001 in all three.
- **Entry 64's lines take each its own item's scope.** It stands for two routes with different gates. The custom fields route has none, and the settings pane's root keeps `settings-control-panel` on its CM-ACC-006 line. The brief now allows a line its own item's scope where an entry stands for several items whose conditions differ.
- **The other differences with SA-22 and SA-32 stand,** each by its own structure:
  - a route's gate is its scope, where a plan gate's row places the gate itself;
  - the delivery promises route takes its guard's feature, where the plan gate's row takes its plans.
- **New things:** Bullet Delivery and Custom Product Fields, under SA-32's names.
- **Cost:** 22.0 million tokens over 91 requests, about 253,000 an entry. Most of the gates sit in the routes' lazy page chunks, which `show --code` doesn't reach, so the agent opened about 45 chunks. SA-14 is the last batch of the dashboard's routes.
