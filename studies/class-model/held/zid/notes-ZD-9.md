# Notes on ZD-9 (Zid: the last of `store-permissions`, then the first of `store-plan-policies`)

**What the batch holds:** 130 entries, at `high` effort. All evidence is at other-product-class@0d79b794f.
- Entries 1 to 28: the last 28 of `store-permissions`' 215 items (`zid/structures/store-permissions/items.jsonl`, lines 188 to 215).
- Entry 29: the structure's one role, `meta.json`'s `roles` (`store.owner`, Store Owner), read as an entry by the `meta:roles` rule.
- Entries 30 to 130: the first 101 of `store-plan-policies`' 633 items (`zid/structures/store-plan-policies/items.jsonl`, lines 1 to 101, `abandoned_carts_analytics` to `coupons.filter`).

**Where the rest is.** ZD-7 and ZD-8 placed the other 187 permissions. I read their lines and the coordinator's checks first, and kept to them (below). No batch had placed `store-plan-policies` before this one. `ZD-10` to `ZD-13` hold the rest of it, from `coupons.multiple_coupons` (items line 102) on, and haven't run. The coordinator aligns them with these lines. `coupons.*` is split between this batch and ZD-10.

**Count:** 130 entries, all on a capability: 0 `new`, 0 `out`. That is 153 lines, all `capability`: 121 `core` and 32 `shows`. There are no `own-service`, `extension-point` or `outside` lines, no filler and no quality.

## How the entries were read

### The permissions (entries 1 to 28)

I kept ZD-7's and ZD-8's rules, as the coordinator corrected them, now the brief's rule 5:
- Each permission is `core` on the capability of what it gates. None of these is over the staff's permissions, so none is on CM-STF-002.
- Every `Export` permission also takes a CM-MIG-001 line (entries 15, 16, 17).
- `relies_on` takes no line. It is named in `reading`.
- `package_restrictions` are the plans the permission is open to, as `scope`, in package keys (entry 14, `customers.edit`).
- **No line comes from a page's gate in `dashboard-page-index/source.js`.** I didn't read it. Each permission takes only the lines its own words name.

Lines beyond the permission's main capability:
- **`orders.request.due.payment` (entry 4)** names a payment link and an order edit in its description. It takes CM-PAY-032 and CM-ORD-002, as ZD-7's flag `order_due` does.
- **`export.store.abandonedcarts` (entry 15)** takes CM-CHK-007 and CM-MIG-001, as ZD-7's `abandoned.carts.export` does.
- **`zam.app.subscriptions`, Subscribe to Apps (entry 1),** takes CM-APP-003, whose cell holds Zid's App Subscription Events and Subscription Details. It also takes CM-APP-001, the store's apps (see "Entries I couldn't tell").
- **`working.times.manage` (entry 5)** takes CM-ORD-010, the cell's أوقات العمل, ZD-1's Hours of operation. It takes no CM-ACC-007 line: ZD-1 gave that line for the page's 'Close store completely', which the permission's words don't name.

**The eleven `(virtual)` permissions (entries 18 to 28).** These are `list.store.orders`, `list.store.products`, `list.store.customers`, `view.store.dashboard`, `manage.store.account.settings`, `manage.store.coupons`, `manage.store.settings`, `manage.store.subscription`, `manage.store.front.customization`, `create.store.orders` and `edit.store.orders`. Each has:
- the name '(virtual)';
- the id `00000000-0000-0000-0000-000000000000`;
- order 999.

Each slug is a staff permission that the model's Zid cell already cites from the concern map (by the leads, such as ZD-S-0518 `edit.store.orders`, ZD-S-0477 `view.store.dashboard`, ZD-S-0516 `manage.store.account.settings`). Each is `core` on that cell, and its only term is the slug. '(virtual)' isn't a term.

**The role (entry 29).** Store Owner is the signed-in user's role. It takes two lines:
- CM-STF-002, as one of Zid's roles, to which 'all permissions are tied' (the cell's ZD-S-0940);
- CM-ACC-001, as the store's owner.

The cell CM-STF-002 says no statement held names Zid's list of roles. This is the only role held, so that list is still not held.

**Scope.** As ZD-7 and ZD-8, the permissions and the role have no scope except `package_restrictions`. The structure's `of` names the store they were read for: Demo Store, 127604, on `new_professional.yearly`.

### The plan policies (entries 30 to 130)

**What an item states.** Each item has:
- a `key`, `<feature>` or `<feature>.<part>`;
- `enabled`;
- `config`;
- `available_in`, the plan it is available in, `{ar, en, package_key}`, or `[]`;
- `policies`, the older boolean.

They are the policies of the Demo Store's plan, `new_professional.yearly` (`meta.json` `of`). No item has a label or description. The dashboard's locales key no string on a policy key: I grepped `dashboard-locales/items.jsonl` for 22 of the keys and found none. So each line is a reading from its key's words, and says so.

**Supports and scope.** I followed the brief's rule for a plan policy or entitlement listed for a store:
- **Enabled** (`enabled: true`, a plan in `available_in`, `policies: true`): `core`. The `scope` is the plan it is available in, as its `package_key` (`new_starter`, `rise`, `new_growth`, `new_professional`, `elite`), the source's identifier, as ZD-7 and ZD-8 wrote the permissions' plans. The `reading` gives the plan's English and Arabic names, and the store's value.
- **Disabled** (`enabled: false`, `available_in: []`, `policies: null`; 33 of these 101): `shows`, as a store's flag with the value false. There is no plan to scope it, so the scope is the store, `Demo Store (store_id 127604)`, as ZD-7's flags.
- **No `config` holds a limit.** The two that hold anything give a value, which goes in `reading`, not `quality`:
  - `automatic_messages.sms_campaigns`: `enable_special_prices: true`;
  - `checkout_page_options.geolocation_service`: `implementation: opensource`.

**Where I kept to the model and to earlier batches:**
- **`abandoned_carts_analytics` and its 19 parts (entries 30 to 49):** these are on CM-ANL-001. CM-CHK-007's own reading says of Zid's abandoned-cart plan lines (Abandoned Cart Value, Count, Stage, Sales Over Time): 'are measures, domain D's analytics, and not cited', and CM-ANL-001 holds Zid's other measures (Top Customers, Returning Customer Rate, Top-Selling Cities). `.export` also takes CM-MIG-001, as ZD-8's `analytics.exports` does.
- **`abandoned_carts.*` (entries 50 to 57):** these are the Abandoned carts page's own features. I placed them as ZD-1 placed that page: the records and their value on CM-CHK-007, and the reminders, the converted carts and the payback on CM-MKT-022. I read the page at `20261028T160128Z-dashboard-routes-rest-en/steps/183.text.txt`, lines 30 to 48 ('Total value of all abandoned carts', 'Total value of carts that have been converted into orders', 'Payback % from carts converted into orders', 'Send reminder').
- **`checkout_page_options.*` (entries 115 to 122):** I read them with the Checkout page options page (`20261028T150740Z-settings-gaps-en/steps/006.text.txt`), which ZD-1 placed on CM-CHK-001. Each option takes the capability its own words name. The CM-CHK-001 line goes only to the options that name the checkout itself: one-page or single-page checkout, and the checkout's last page.
- **ZD-6's plan lines:**
  - Apple Pay's fast checkout takes CM-CHK-008 and CM-PAY-012;
  - the API's direct integration and `zam_api_access` take CM-APP-009 and CM-API-001, as 'Connect your store with external systems (via API)';
  - `coupons` takes CM-MKT-002. It takes no CM-MKT-001 line: unlike ZD-6's 'coupons discounts', the key names coupons only.
- **ZD-1's and ZD-8's lines:**
  - Mokafaa and Qitaf take CM-LOY-004 and CM-PAY-012;
  - the abandoned carts' automatic messages take CM-MKT-022 and CM-MKT-006;
  - the order status messages take CM-NTF-001.
- **The model's cells:**
  - the plan lines Sender Name (CM-NTF-004), Q&A and Review Messages (CM-SUP-001), Barcode Printing (CM-CAT-015), Add Products (CM-CAT-001), Account Details (CM-ACC-001), Affiliate Links, Commission, Affiliate Information and Export Affiliate Data (CM-MKT-014);
  - the blog only on Growth and Professional (CM-CNT-004);
  - API Access (CM-APP-009);
  - `coupons.analytics` takes CM-ANL-001 beside CM-MKT-002, as the model keeps 'Coupons - Coupon Results' on analytics.

**The disabled groups named for third parties' products.** `accounting.*` (11), `analytics_&_reporting.*` (5) and `campaign_tracking.*` (11) each name a product by key, such as `accounting.qoyod`, `analytics_&_reporting.hotjar` and `campaign_tracking.tiktok_pixel`:
- Their group names match Zid's App Market categories that the cells cite: المحاسبة والفوترة (ZD-I-0440, CM-PAY-028), التحليلات والتقارير (ZD-I-0432, CM-ANL-001) and تتبع الحملات والإسناد (ZD-I-0457, CM-MKT-008). That they are apps of those categories, gated by plan, is a reading. Nothing held says what these policies gate.
- No maker is stated, and a key is a flag's name, so none has a `filler`. Each is `shows`, on the capability its key names:
  - the accounting ones on CM-PAY-028;
  - crazyegg, hotjar and qumra on CM-ANL-001, since only the group says what they are;
  - `lableb_search` on CM-SFR-013, by "search";
  - `tajer_report` on CM-ANL-002, by "report";
  - the pixels, conversion APIs and tags on CM-MKT-009, customer events and tracking pixels.

## Entries I couldn't tell, and what would settle each

- **`campaign_tracking.*` on CM-MKT-009, which held nothing (checker: CHANGES, 11 lines).** Each key names a pixel, a conversion API or a tag (`facebook_pixel`, `snapchat_conversion_api`, `google_tag_manager`), which is CM-MKT-009's thing, but each is disabled and in no plan, so all are `shows`. The cell becomes held with `shows` only, not placed.
  - Two keys could also be other capabilities': `google_ads` on CM-MKT-010 (advertising), and `google_analytics` on CM-ANL-007 (data sent to outside analytics platforms, which holds nothing). I didn't place them there on the key alone.
  - The group's name could also put them on CM-MKT-008, sales attribution, whose cell cites the App Market category تتبع الحملات والإسناد.
  - What would settle it: the dashboard's page or the App Market apps these policies gate.
- **`automatic_messages.abandoned_carts_messages` on CM-MKT-006 (checker: CHANGES: gains `core`).** This follows ZD-8's lines for the abandoned carts' automatic messages and ZD-1's Automated Messages, which aren't amended into the model yet. On its own, it is the only `core` line on a cell that holds `extension-point`.
- **`zam.app.subscriptions`, Subscribe to Apps (entry 1).** It is placed on CM-APP-003 (app charges) and CM-APP-001. Whether subscribing pays for an app's plan or only installs the app isn't stated. If it only installs, the CM-APP-003 line goes.
- **`automatic_messages.manage_reviews` (entry 97), on CM-SUP-001 only.** It sits among the automatic messages. It could be the message asking the buyer to rate, ZD-1's Product review notifications, which ZD-1 placed on CM-SUP-002, which holds nothing. I didn't place it there on the key alone. What would settle it: the page this policy gates.
- **`checkout_page_options.add_custom_terms_and_declaration_on_the_last_page` (entry 116), on CM-CHK-001 and CM-CNT-008.** The Checkout page options page held doesn't show the option. The CM-CNT-008 line reads "custom terms" as the store's terms shown to the buyer; it could instead be a declaration of checkout only.
- **`checkout_page_options.one-page_checkout` (disabled) and `.single_page_checkout` (enabled, Growth), on CM-CHK-001.** The page shows one setting, 'Activate one-page checkout'. Why two keys name it, one disabled, isn't stated.
- **`checkout_page_options.geolocation_service` (Elite), on CM-CUS-009.** Read beside the page's 'Customer address determination'. It could also be visitor geolocation (CM-MKS-004).
- **`checkout_page_options.fast_checkout_with_apple_pay` and `.apple_pay_alert_in_all_browsers`.** Both policies are disabled, so both are `shows`, though the store's Checkout page options page shows both settings (unchecked, `steps/006.text.txt` lines 45 to 48 and 66 to 69). What a disabled policy hides isn't stated.
- **`auto_discounts.discount_on_online_payment` (entry 94), on CM-MKT-003 only.** "Online payment" is the condition of the discount, not its thing. It isn't CM-MKT-018 (a given bank's card).
- **`affiliate_marketing.discount` (entry 78), on CM-MKT-014 and CM-MKT-001.** Whether it is an affiliate's coupon (CM-MKT-002) isn't stated.
- **`affiliate_marketing.refer_order` (entry 82), on CM-MKT-014 only.** Crediting an order to an affiliate could also be sales attribution (CM-MKT-008). I didn't place it there.
- **`account_settings.log_out_all_employees_from_the_control_panel` (entry 60), on CM-TRU-001 and CM-STF-001.** I read it as signing out the team's sessions, a sign-in security control.
- **The plan Elite (`elite`, برنامج النخبة).** `automatic_messages.sms_campaigns` and `checkout_page_options.geolocation_service` are available in Elite. ZD-6's offered plans don't hold it. Zid's statements name النخبة among its plans (CM-ANL-002's ZD-S-1048). Whether Elite is a plan above Professional or a programme isn't stated: 'برنامج' reads as programme.
- **`available_in` names one plan.** I read it as the lowest plan the policy is available in, as the coordinator read the abandoned carts' analytics in ZD-7's check. That it means "and the plans above it" isn't stated.

## A structure whose items and sources disagree

None found. The 28 permissions are the items as ZD-7 checked them against the answer's `user.permissions`. The role is `meta.json`'s `roles`. I read the policies' items directly, and each entry's `key` matches its item, in order.

## What a source states that no entry holds (leads for the second stage)

- **`20261028T150740Z-settings-gaps-en/steps/006.text.txt`, Checkout page options.** It shows settings that no policy of this batch names. ZD-10 to ZD-13 may hold some of them as policies:
  - 'Shipping and payment options display' (line 33);
  - 'Sign in with SMS messages' (52), 'Make it mandatory' (61) and 'Sign in with WhatsApp' (62), for CM-CUS-010;
  - 'Login as a pop-up' (70) and 'Buy now as a pop-up' (73), for CM-CHK-008;
  - 'Show coupon code field' (79), for CM-MKT-002;
  - 'Buy as a guest' (82) and 'Direct guest checkout' (92), for CM-CHK-001;
  - 'Customer notes' (94), for CM-CHK-009;
  - pickup items at checkout (104), for CM-SHP-007;
  - 'Allow customers to change their customer type to a company' (107), for CM-B2B-001 or CM-CUS-001.
- **`20261028T160128Z-dashboard-routes-rest-en/steps/183.text.txt`,** lines 34 to 48: the Abandoned carts page's Analytics tab and 'Presets'. These are the analytics that `abandoned_carts_analytics.*` names, for CM-ANL-001.

## The checker's other lines

- **`NOTE` on line 16** (`zid.financing.manage`, a product named with Zid's brand). The staff permission is Zid's own, so it is `core`, as ZD-8's `zid.financing.view`.
- **`NOTE`s on CM-PTN-006 as a first lead "by name: growth, نمو".** These come from the plan's name, Growth / النمو, in `available_in`. They are not leads (brief, rule 1), so I gave them no lines.

## Problems with the brief or the script

- **The leads for `store-plan-policies` are almost all by the plan's name.** Nearly every policy available in Growth has CM-PTN-006 as its only lead. That is a word that every Growth policy holds, so it is not a lead (brief, rule 1). For ZD-10 to ZD-13, the leads' matcher could leave out `available_in`'s names.
- **A policy key's group** (`accounting`, `campaign_tracking`, `analytics_&_reporting`, `checkout_page_options`) is not an entry of its own. So the group-as-container rule (rule 3) has nothing to place: each group is named only in its parts' keys. I gave a part its group's capability only where the key's part names nothing else, as for crazyegg, hotjar and qumra.

## The coordinator's check (30 October 2026, after the batch)

- **The leads for plan policies are fixed for ZD-10 to ZD-13.** They read the plan's name in `available_in` as the entry's words, so nearly every policy led to CM-PTN-006 by "Growth". A policy's plans are its scope, so the leads now leave out `available_in` and `package_restrictions`. A policy's `key` is the platform's own words for its thing, so the leads read its segments, as they read a route's path. With both changes, 95 of ZD-10's 130 entries have leads, each from the key's words (`coupons.search_bar` to coupons and search; `digital_products.file_count` to digital products).
- **CM-MKT-009's disabled `campaign_tracking.*` lines stand as `shows`.** ZD-6's 'Marketing Pixels integration' plan line already makes the cell held with `core`.
- **The Elite plan** (`elite`, برنامج النخبة), where two policies are available, isn't among the offered plans ZD-6 placed. Noted for the plans' cells: a plan the policies name that the store's offer doesn't list.
- **The batch changes no cell beyond Zid's earlier batches.** The permissions confirm their pages' cells, and the first policies confirm plan lines ZD-6 placed.
