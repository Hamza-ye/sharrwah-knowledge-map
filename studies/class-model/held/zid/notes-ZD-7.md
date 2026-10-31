# Notes on ZD-7 (Zid: `store-feature-flags`, then the first 57 of `store-permissions`)

**What the batch holds:** 130 entries, at `high` effort:
- entries 1 to 73: all 73 of `store-feature-flags`, the store's flags as the answer to `GET hermod.zid.sa/v1/managers/store/feature-flags` states them (`other-product-class@0d79b794f:zid/raw/runs/20261028T144855Z-dashboard-routes-en/answers/hermod.zid.sa/v1/managers/store/feature-flags/e8462761….json`);
- entries 74 to 130: the first 57 of `store-permissions`' 215 items (`items.jsonl` lines 1 to 57).

**Where the rest is.** The other 158 permissions are in `ZD-8` and `ZD-9`, which haven't run. No batch had placed either structure before this one, so there was nothing to align with. The coordinator should align `ZD-8` and `ZD-9` with the rules these lines follow, set out below: each permission `core` on the capability it gates, an `Export` or `Import` permission also on CM-MIG-001, and no CM-STF-002 line except for permissions on the permissions themselves.

**Count:** 123 entries on a capability, 7 `new`, 0 `out`. That is 152 lines: 145 `capability` and 7 `new`; 88 `core` and 64 `shows`.

## How the entries were read

**The feature flags.** I followed the brief's ruling for a store's flag stated only by its value:
- `true` supports `core`;
- `false` supports `shows`;
- the value is in `reading`;
- a `pilot`, `demo` or `dev` name supports `shows`, because its value is `false`.

The scope is the store the answer was received for, `Demo Store (store_id 127604)`. The answer itself names no store. The store comes from `store-permissions`' `meta.json` (`of.store_id`, `of.store_title`), taken in the same run, and from `index/instruments.json`.

None of the 73 flags had a lead. Each was placed from its key's words, so every line is a reading. Where an earlier batch had placed the page listed under the same condition, I kept to that line's capability:
- `must_use_markets_pricing` (mustUseMarketsPricing): CM-MKS-001;
- `has_new_gifting` (hasNewGifting): CM-LOY-006;
- `customer_wallets` (customerWallets): CM-LOY-001;
- `show_new_zones` (showNewZones): CM-SHP-001.

The dashboard's locales (`zid/structures/dashboard-locales/items.jsonl`) clarified some keys. Each reading that rests on them quotes the string and gives its line:
- 2572, 19412: `serviceFee` is "Zid assurance" / "ضمان زد";
- 6299, 6309: `orderDue`;
- 6349: reverse order;
- 6388: waybill and packing list;
- 7548, 7579, 10446: cashback campaigns and milestones;
- 10603, 13424: Noon, the gateway of the store's purchases from Zid;
- 13365: the subscription's auto-renewal.

**The permissions.** Each is the platform's own staff permission. It is `core` on the capability of what it gates, as CM-STF-002's note says: "the permissions each other capability cites are evidence for those capabilities, not here". So only `users.permissions.edit` is on CM-STF-002, and `users.um.view` is on CM-STF-001.

Other things an entry names take their own line:
- every `Export` and `Import` permission also takes a line on CM-MIG-001;
- where an earlier batch placed the same page on two capabilities, I followed it: Automated Messages (CM-MKT-006 and CM-NTF-001), Abandoned carts (CM-CHK-007 and CM-MKT-022), Orders and products properties (CM-ORD-001 and CM-CAT-001), and the store app's push notifications (CM-CHN-006 and CM-MKT-007).

A permission's `relies_on` names another permission, not the entry's own thing, so it takes no line. Its scope is empty, except where `package_restrictions` names plans (next section).

## Entries I couldn't tell, and what would settle each

**`package_restrictions` (entries 76 and 117, `abandoned.carts.export` and `abandoned.carts.manage`).** The source doesn't define the field. `REGISTER.tsv` calls it "the plans that restrict them", which is a finding aid.
- I read the plans it lists as the plans the permission is restricted to, and wrote their `package_key`s as `scope`.
- Two things support that reading: neither list names `rise`, and the demo store's `new_professional` is in both.
- The opposite reading, the plans it is restricted from, would invert the scope.
- What would settle it: a Zid statement of what the field means, or a store on `rise` whose permission list leaves these two out.

**Flags whose subject is ambiguous:**
- **`whatsapp_otp` (CM-CUS-013) and `is_charged_for_otp` (CM-CUS-010).** It isn't stated whether these are the buyers' codes or the merchant's. ZD-1 placed the dashboard's OTP setting (security settings) on CM-TRU-001.
- **`product_listing` (CM-CAT-001).** It could also be a listing on a channel (CM-CHN-004, which holds nothing on Zid). I didn't place it there on the name alone.
- **`ai_product_fields` (CM-AIA-003, `core`).** This makes a cell that held nothing held, on the flag's name alone (checker: CHANGES). The home strings back it as a lead, not as the entry's words: "Enhance your store with Zid AI: better descriptions, sharper visuals, and a persuasive tone." (line 10570), along with the theme editor's AI-generated sections (lines 2033 to 2058). The second stage should read a page where the AI writes product fields, which would settle it.
- **`has_wallet` (CM-PLN-006) and `has_wallet_payments` (CM-PLN-005).** I read the wallet as the merchant's, because `customer_wallets` is a flag of its own. Whether `has_wallet_payments` means paying Zid from the wallet or buyers paying with a wallet isn't stated.
- **`new_purchase_*`, `native_apple_pay_in_subscription_checkout`, `noon_apple_pay_v2`, `noon_egp`, `subscription_auto_purchases*` and `pv2_subscription_cn_jitter` (CM-PLN-001, 002, 004, 005, 006).** These are read as the store's purchases from Zid and its subscription. The reading rests on the dashboard's `checkout` namespace, which holds the subscription's renewal, the wallet balance, Apple Pay and Noon. Noon is also a marketplace in the `marketplace-connect` strings. `pv2`, `cn` and `jitter` aren't defined anywhere held.
- **`is_apple_pay_default_payment_method` (CM-PAY-012).** It isn't stated whether this is the buyer's checkout or the store's purchases from Zid.
- **`checkout_constraints` (CM-PAY-019 and CM-SHP-001, both `core`).** This is read as ZD-1's Shipping and payment constraints. It could also be other rules at checkout.
- **`order_due` (CM-PAY-032 and CM-ORD-002).** This rests on the `orders:details.orderDue.*` strings: an amount added after an order's products are updated, paid by a payment link. It could also be CM-ORD-015, the order's payment status.
- **`service_fee` (CM-TRU-020).** This rests only on the locale key `checkout.form.serviceFee` = "Zid assurance". CM-SUP-008 also cites Zid Assurance.

**Flags that are `false` while the dashboard lists the page.** These are:
- `is_loyalty_enabled`;
- `stocktaking`;
- `can_use_transferring_stocks`;
- `customizable_reports`;
- `use_export_request_system`;
- `einvoicing`;
- `has_product_landing_pages`.

What each flag switches isn't stated, so each is `shows` with its value. None says the feature is missing.

## New things

None of them has a place of its own. Each is one flag, with no route, section, plan line or category held. Each is `shows`. Its name is the flag's key, since no Arabic or English title is held for any of them.

| Name | Entries | Searched (`caps --terms`; dashboard locales; route ledger) | Proposed |
| --- | --- | --- | --- |
| `cashback campaigns` | ZD-E-d823b4c2 (`cashback_campaigns_demo`), ZD-E-549b7c7b (`cashback_enable_order_milestones`) | cashback; كاش باك; milestone; reward; مكافأة; campaign | Domain A, area PLN, near CM-PLN-006 (a reading, below). The alternative is CM-LOY-003, the buyers' cashback offers |
| `hermes` | ZD-E-433a6af7 (`hermes_pilot`) | hermes: no hit in the model, the locales or the route ledger | Undecided; possibly out |
| `es pushdown` | ZD-E-5adf7319 (`has_es_pushdown`) | pushdown, Elasticsearch: no hit | Undecided. If the coordinator reads it as the software's own bookkeeping, it is `out` |
| `vitrin` | ZD-E-5d790d60 (`has_vitrin`, `true`) | vitrin; فاترين: no hit | Undecided |
| `collection moderators presenter` | ZD-E-3e4bd6bd | collection; moderator; presenter: only CM-CAT-003 matches, on "collection" | Undecided; possibly CM-CAT-003 |
| `nd2026` | ZD-E-a25b9497 (`nd2026_unassign`) | nd2026, unassign: no hit | Undecided. A lead: the locales' `national-day-offer` namespace (94 English strings, such as "Celebrate Saudi National Day with Zid", line 7526) may be what "nd" names |

**Why I made `cashback campaigns` new (a reading).** In the dashboard's strings, cashback with "campaign" and with "milestones" appears only in two places:
- the `national-day-offer` namespace: "Complete eligible orders during the campaign period to earn a free year subscription and / or cashback." (line 7548);
- the home page's `cashbackMilestones.*`: "Added to wallet" (line 10446).

Both are Zid's rewards to the merchant for completed orders, not a store's offer to its buyers. No capability holds the platform's incentives to merchants. If the coordinator reads these flags as the buyers' cashback instead, both go to CM-LOY-003 as `shows`.

## A structure whose items and sources disagree

None:
- `store-permissions`' 215 items match the answer's `user.permissions` field by field, in order;
- the flags' answer holds the 73 flags the entries hold, beside `status: object` and a `message`.

## What a source states that no entry holds (leads for the second stage)

**Leads for cells that hold nothing, or hold little:**
- `dashboard-locales`, `orders:details.waybillAndPackingList`, "Shipping label & packing list" / "بوليصة الشحن وقائمة التعبئة" (lines 6388, 23236): a printed packing list, for CM-ORD-009 on Zid. This batch gives that cell a `shows` line from the flag alone (checker: CHANGES).
- `dashboard-locales`, `home:fiveSalesJourney.steps.description_optimizationTrust` (line 10570) and `theme-editor:ai*` (lines 2033 to 2058, "AI generator", "AI Generated", "{{remaining}} of {{limit}} AI sections left today"): for CM-AIA-003. The theme editor's daily limit is a quality.

**Leads for a new thing:**
- the `national-day-offer` namespace (lines 7515 to about 7610) and `home:cashbackMilestones.*` (lines 10442 to 10449): Zid's cashback and free-year rewards to merchants, for the `cashback campaigns` question above.

**Leads for cells already held:**
- `dashboard-locales`, `home:noonSwitchNotification.body` (line 10603): Zid's payment gateway for automatic renewal changes, and saving a card "requires completing a purchase, namely a subscription renewal". For CM-PLN-002 (renewal) and CM-PLN-005.
- `dashboard-locales`, `checkout:*` (239 strings): the checkout of the store's purchases from Zid, with Apple Pay, bank transfer, the wallet balance and "Auto-renews every {{type}} on {{date}}". For CM-PLN-002 and CM-PLN-005.
- `dashboard-locales`, `orders:details.orderDue.*` (lines 6299 to 6311): an additional amount after editing an order, paid by a payment link that expires. For CM-ORD-002 and CM-PAY-032.
- `dashboard-locales`, `products:trashBin` and `pages:productsTrashBin.title` (lines 4507, 5912): ZD-5 already holds the page.
- The profile answer's `user.store.subscription.policies_v2` (`…/v1/managers/account/profile/c9cbd4a4….json`) holds each policy's `available_in.package_key`. `store-plan-policies` (ZD-9 to ZD-13) places these.

## Problems with the brief or the script

**Permission lists.** The brief says a staff permission "takes a line on CM-STF-002 only where the entry names the permission as its own thing". In a permission list, every entry is a permission. I followed CM-STF-002's own note, which keeps the permissions on the capabilities they gate. This is the reading B-extent.md supports ("cite the staff permission for `core`"). The coordinator may want to state it in the brief for ZD-8 and ZD-9, and for Salla's and Shopify's permission lists.

**`faqs.manage` relies on itself** (`relies_on: [faqs.manage]`, `items.jsonl` line 25), as the source states. This is likely meant to be `faqs.view`, but that is not a fact.

**The checker's leads by a field's common word.** These were not leads, as the brief says, and were left without lines:
- CM-API-009 for "notifications" (entry 83);
- CM-OPS-004 for "status" (entry 123);
- CM-API-010 for "conditions" (entry 78);
- CM-ACC-004 for "business", a `package_key` (entries 76 and 117).

## The coordinator's check (30 October 2026, after the batch)

- **CM-AIA-003 rests on more than the flag's name.** The dashboard's home page names it: 'Enhance your store with Zid AI: better descriptions, sharper visuals, and a persuasive tone.', with the action 'Optimize with Zid AI' (`dashboard-locales/source/en/home.json`, `fiveSalesJourney.steps.optimizationTrust`). The line cites it.
- **`package_restrictions` lists the plans a permission is open to,** as the batch read it. The lists hold only higher plans: Manage Abandoned carts holds Growth and up, and its Export starts at Professional, as the plan policies place abandoned carts' analytics in Growth. A list of plans the permission is closed to would hold Starter and Rise.
- **The cashback flags are Zid's cashback to merchants,** as the batch read them. The same page reads 'Reinvest your earned cashback into purchasing shipping labels to keep orders moving smoothly.' (`fiveSalesJourney.steps.description_shippingLabel`). Not CM-LOY-003, buyers' cashback. The new thing is decided with Zid's others.
- **A list of permissions is placed as this batch placed it:** each permission `core` on the capability it gates, and CM-STF-002 only for the permissions that manage staff permissions. That is CM-STF-002's own note, and the brief now says so (3.3), for ZD-8 and ZD-9.
- **The opaque flags** (hermes, es pushdown, vitrin, collection moderators presenter, nd2026) are decided with Zid's other new things. A flag whose name says nothing a held string explains, and that has no place of its own, is likely `out`.
