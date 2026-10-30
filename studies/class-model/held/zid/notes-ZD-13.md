# Notes on ZD-13 (Zid: `store-plan-policies`, items 492 to 633)

**What the batch holds:** 142 entries, at `high` effort, all of `store-plan-policies` (`zid/structures/store-plan-policies/items.jsonl`, lines 492 to 633, `terms_&_conditions.license` to `zidship.zidship_shipments_details`). All evidence is at other-product-class@0d79b794f. The policies are the Demo Store's (store 127604), on `new_professional.yearly` (`meta.json` `of`), from the answer `meta.json` names under `source`: `GET /v1/managers/account/profile`, run 20261028T144855Z-dashboard-routes-en.

**Where the rest is.** ZD-9 placed items 1 to 101, ZD-10 items 102 to 231, ZD-11 items 232 to 361 and ZD-12 items 362 to 491. I read their lines and notes, with the coordinator's checks, first, and kept to them. This is the structure's last batch. `terms_&_conditions.*` is split between ZD-12 and this batch.

**Count:** 142 entries: 140 on a capability alone, 2 with a `new` line beside their capability line (`zidpos.employee_attendeance`, `zidpos.employee_commision`), 0 `out`. That makes 217 lines: 215 `capability` and 2 `new`, with 195 `core`, 20 `shows` and 2 `extension-point`. There are no `own-service` or `outside` lines and no filler. Three lines carry a quality from `config`.

## How the entries were read

I kept the earlier batches' rules, with the coordinator's checks:
- **Enabled policies** (`enabled: true`, a plan in `available_in`, `policies: true`; 129 here): `core`. The `scope` is the plan key the source states the policy is available in. The reading says 'available in <plan> (<Arabic>)', with no claim that this is the lowest plan including it.
- **Disabled policies** (`enabled: false`, `config: null`, `available_in: []`, `policies: null`; 13 here): `shows`, with the scope `Demo Store (store_id 127604)`. They are `transferring_stock`, `zidpay.apple_pay_fast_checkout`, `zidpay.apple_pay_full_form` and ten `zidship.*` (the Aramex, Saudi Post and SMSA drop-offs, `aramex_customized`, and the service levels `cold`, `fast`, `heavy`, `no_rush`, `now`). No disabled item here states a plan.
- **Terms.** The only term is the key. No item has a label.
- **A key's own words decide its capability** (the coordinator's check of ZD-12). A product named only by its brand is placed by its group. Here the groups are Zid's own products, `zidpay` (Zid Pay), `zidpos` (Zid POS, زد كاشير), `zidship` (ZidShip, زد شب) and `zam` (the App Market), each a capability the model holds.
- **A group's line.** As ZD-11 gave each `order_management_new_order.*` part CM-ORD-005, and ZD-12 each `subscription_management.*` part CM-PLN-001, each part of a group that is a feature of the group's product takes the group's line beside its own:
  - `users_management.*`: CM-STF-001;
  - `zidpay.*`: CM-PAY-002;
  - `zidpos.*`: CM-POS-001;
  - `zidship.*`: CM-SHP-002.

  Three kinds of part take no group line:
  - the analytics' and reports' measures (`zidpay_analytics.*`, `zidship.cod_analytics`, `.online_payments_analytics`, `.total_cod_collections`, `.total_orders_analytics`, `.zidship_reports*`), on CM-ANL-001 alone, as ZD-9 to ZD-12 placed the measures and ZD-8 placed `zidship.view.reports`;
  - `zidship.custom_shipping`, `.smsa_customized` and `.aramex_customized`, on CM-SHP-015 alone: the merchant's own carrier contract, not ZidShip's labels at Zid's rates, as ZD-8 placed `zidship.custom.shipping.management` and ZD-12 `shipping.custom_shipping`;
  - `vat_tax_settings.*` parts, whose group is CM-TAX-001's own thing: they take CM-TAX-001 as their own line.
- **A part that names another thing takes that thing's line too** (rule 2), such as `zidpos.coupons_management` on CM-MKT-002, `zidpos.e-invoicing` on CM-TAX-007, `zidpay.card_discount` on CM-MKT-018. A part that names only the POS's own working (`cashier_access`, `create_transaction`, `hold_carts`, `order_history`, `session_history`, `split_payment`, `organizing_products`, `product_description`, `multi-language_cashier_app`, `barcode_scanning`, `bluetooth_prinitng`, `custom_products_screen`, `customer_display_screen`, `geobased`, `inapp_reports`, `cash_payment`) takes CM-POS-001 alone.
- **Exports** take a CM-MIG-001 line beside their thing's line (5 lines: `zidpay_analytics.export`, `zidpay.bulk_deposit_export`, `.deposit_details_invoice_export`, `.transaction_list_details_invoice_and_export`, `zidship.export`).
- **Zid's brand names no maker.** Every line on a Zid-branded product is `core`, as a plan policy that includes it, as ZD-6 and ZD-12 placed `shipping.zidship` and Zid Financing. The cells' own maker statements (CM-PAY-002's, CM-PAY-026's, CM-POS-001's) aren't cited by these lines.

### Pages and locales that clarify the keys

As in ZD-11 and ZD-12, I read the dashboard's strings to clarify the keys only (brief, rule 1), and quoted them at their files (`dashboard-locales/items.jsonl`):
- **The tax settings:** 'Activate VAT in store' (line 3139), 'Do you want to apply VAT on shipping fees?' (3141), 'Tax-taxed countries' (3162), the VAT number and certificate (3146, 3164), and the switches on showing prices with VAT and the VAT number (3149, 3160).
- **The plans table** `subscription:featuresTable.*`: 'Team management' (2326, 2327), 'Zid communities' (2307, 2308), 'Instant payment activation' (2318, 2319), 'Tax by country' (2341), 'Shipping by speed' (2375, 2376) and 'Shipping by weight' (2377, 2378).
- **The team's 'Audit Log'** (`pages:settingsTeamLogs.title`, line 5993), with its page, 'Only actions from the last 30 days are shown below.' (`20261028T150740Z-settings-gaps-en/steps/032.text.txt`).
- **'Close store completely'** (`settings:workTime.storeClosed`, line 3259).
- **Wallet Splitting** (`wallet:wallet-splitting.*`, lines 1891 to 1907).
- **The transactions' 'Bank name'** (`payments:transactions.cardBankName`, line 5406).
- **The POS settings:** 'Enable location-based POS access' (75), 'Default status for POS pickup orders' (72), the cashier as a team member (73), and 'Invoice templates' (249, 250).
- **Zid Logistics' help centre:** its service levels (9388 to 9392), its prepaid balance and 'service collection window' (9381, 9382), its cash-on-delivery transfers (9383), and 'Self drop-off' (9704, 9716).
- **The logistics analytics' 'Total COD payments collected'** (16089).

### Limits and values in `config`

Three policies state a limit, each placed in `quality`:
- **`users_management.order_statuses_notification`** (Enterprise): `notified_staff_limit: 0`, on CM-NTF-002. Whether 0 means none or no limit isn't stated, as ZD-10's `group_limit: 0` and ZD-12's `language_limit: 0`.
- **`users_management.team_members`** (Elite): `team_members limit: 20`, on CM-STF-001. The cell's plan line Add Team Members gives 1 on Starter to 20 on Pro (ZD-S-0939). Here it is stated for Elite.
- **`vat_tax_settings.tax-taxed_countries`** (Elite): `tax-taxed_countries limit: 0`, the same open question.

Two configs give values, which go in `reading`:
- `zid_academy.zid_academy`: `model: FullAccessForThreeUsers`;
- `zidpay`: `package_id: 4`, whose meaning isn't stated.

**The plans available in.** Enterprise (`enterprise`) and Elite (`elite`) appear again, on policies enabled for this Professional store:
- Enterprise: `users_management.order_statuses_notification`;
- Elite: `users_management.team_members`, `vat_tax_settings.tax-taxed_countries`, `zid_academy.zid_academy`, `zidpay`.

`zidpay` itself is available in Elite, while most of its parts are available in Rise, Starter or Growth. What `available_in` means for a product's own key beside its parts isn't stated: for the plans' cells at Zid's amendment.

### Where I kept to the model and earlier batches

- `terms_&_conditions.*`: CM-CNT-008, as ZD-12, the kinds of legal page the cell names (ZD-S-0780). `privacy_policy` takes no CM-TRU-006 line: CM-TRU-005's note keeps the policy page on CM-CNT-008.
- `transferring_stock` (disabled): CM-INV-006, `shows`, as ZD-7's flag `can_use_transferring_stocks` (ZD-E-17aee82f). ZD-10's `inventory_locations.transferring_stock` is enabled on Professional. Why two keys name it, one disabled, isn't stated.
- `url_redirects`: CM-CNT-009.
- `users_management.action_audits`: CM-TRU-003, ZD-5's team/logs, 'Audit Log' (ZD-E-ad139347).
- `zid_academy`: CM-ONB-003, as ZD-6's Zid Academy (ZD-E-a2383ad9).
- `zid_growth`: CM-PTN-005, ZD-1's Growth (ZD-E-48fb2e7a).
- `zid_finance.zid_finance` and `zidpay.zidfinance`: CM-PAY-026, as ZD-6's Zid Financing (ZD-E-d260e0ae).
- `zidpay`: CM-PAY-002, as ZD-11's `payment_options.zidpay`.
- `zidpay_analytics.*`: CM-ANL-001, ZD-1's Payments analytics (ZD-E-e063723f).
- `zidpay.anti_fraud`: CM-ORD-006, as ZD-6's Fraud protection (ZD-E-afce48ed).
- `zidpay.apple_pay_*`: CM-PAY-012, and the quick and fast checkouts CM-CHK-008, as ZD-6's Rise card (ZD-E-0bfc6b1f).
- `zidpay.payment_link`: CM-PAY-032, ZD-1's Payment links.
- `zidpos.inapp_reports`: CM-POS-001 alone, as ZD-8's `pos.reports.view`. `zidpos.session_history` and `.order_history` as ZD-5's POS routes.
- `zidship.waybills_packages`: ZD-1's Label packages (ZD-E-9c07312d). `zidship.zidship_reports*`: as ZD-8's `zidship.view.reports`. `zidship.banking_information`: CM-PAY-029, as ZD-5's logistics/bank-account (ZD-E-ea734a3c).

## New things

- **Employee attendance** (`new:employee attendance`; `zidpos.employee_attendeance`, ZD-E-83a3ed83, available in Professional).
  - **Place of its own:** a plan line, a policy in the plan's own list (B-extent, "What a place of its own is"). The line is `core`.
  - **Proposed:** domain A, area STF, parent CM-STF-001 (staff), or CM-POS-001, whose policy it is.
  - **Names:** English from the key, 'employee attendance' (the key's spelling is `attendeance`). No string names it, in English or Arabic.
  - **Terms searched:** attendance; حضور; الحضور; time clock; staff. No capability holds staff attendance, and no POS cell names it.
- **Employee commission** (`new:employee commission`; `zidpos.employee_commision`, ZD-E-b73bf8bc, available in Professional).
  - **Place of its own:** a plan line, as above. The line is `core`.
  - **Proposed:** domain A, area STF, parent CM-STF-001, or CM-POS-001.
  - **Names:** English from the key, 'employee commission' (the key's spelling is `commision`). No string names it.
  - **Terms searched:** commission; عمولة; عمولة الموظف; sales rep. The capabilities with "commission" are other parties': affiliates (CM-MKT-013, CM-MKT-014), the platform's fee (CM-PLN-003), partners' (CM-PTN-003, CM-PTN-008, CM-PTN-009) and payment fees (CM-PAY-007). The nearest is CM-B2B-006, sales reps for business buyers, which holds nothing on Zid and names no commission.

Each entry also takes CM-POS-001, as a feature of Zid POS. Both have leads only to POS-001 by its words. The coordinator may decide the two together, as a POS staff feature.

## The checker's CHANGES, and what I decided

- **CM-SHP-007 becomes held, with `core` (line 144, `zidpos.order_online_pickup_from_branch`).** I kept it. The key's words are an online order picked up from a branch: the buyer's pickup at the store's location, the cell's thing. The POS's 'Default status for POS pickup orders' (line 72) names pickup orders at the POS. The coordinator's check of ZD-12 places Zid's buyer's pickup in store here by ZD-4's `store-pickup` route, which isn't amended yet, which is why the checker flags this.
- **CM-TRU-003 becomes held, with `core` (line 7, `users_management.action_audits`).** I kept it. ZD-5 placed the team's Audit Log here (ZD-E-ad139347: 'Only actions from the last 30 days are shown below.', `20261028T150740Z-settings-gaps-en/steps/032.text.txt`), and the staff permission `users.logs.view` (View Logs) relies on `users.um.view` (`store-permissions`). ZD-5's line isn't amended yet. That "action audits" names this Audit Log is a reading.

## Entries I couldn't tell, and what would settle each

- **`zam.fulfillment_apps` and `zam.shipping_apps`: `extension-point`, not `core`.** ZD-12 placed `shipping.fulfillment_service` as `core` on CM-SHP-011 (M-9: what a plan line includes). These two keys name the App Market's apps: what the plan includes is access to third parties' apps that do the work, through Zid's App Market, the cell's App Market category الشحن والتخزين. So I placed them `extension-point` on CM-SHP-011 and CM-SHP-015, with `core` on CM-APP-001 (the App Market, Zid's own place). The coordinator may read M-9 as making them `core`.
- **`users_management.control_closing_store`, on CM-ACC-007 and CM-STF-001.** It could be the closing itself ('Close store completely') or the control of which staff may close the store. Its group suggests the second, but no permission or string names it. What would settle it: the page or permission this policy gates.
- **The `users_management.*` CM-STF-001 lines.** I gave each part the group's line, as ZD-12 gave `subscription_management.*` CM-PLN-001. The audit log and the store's closing aren't kinds of staff account, so these two group lines rest only on the group's words. The coordinator may drop them.
- **`vat_tax_settings.merchant_vat`, on CM-TAX-001 and CM-TAX-003.** I read "the merchant's VAT" as its VAT number and certificate. It could instead be the VAT the merchant includes in its prices ('By opting into this choice, you will be responsible for including the VAT in the product prices.', line 3143), which is CM-TAX-001 alone.
- **`vat_tax_settings.vat_appears`, on CM-TAX-001.** It could be showing prices with VAT (line 3149) or showing the VAT number and certificate on the storefront (lines 3159, 3160, CM-TAX-003).
- **`zidpay.apple_pay_full_form` (disabled), on CM-PAY-012 alone.** What "full form" is isn't stated.
- **`zidpay.card_in_use`, on CM-PAY-020.** No string names it. I read it as the card a transaction was paid with.
- **`zidpay.instant_transaction_acceptance`, on CM-PAY-002 alone, and `.instant_account_creation`, on CM-PAY-003.** Both read with the plans table's 'Instant payment activation'. What is instant isn't stated.
- **`zidpay.open_apis_and_ksa`, on CM-PAY-002 alone.** I read "open APIs" as Zid Pay's API. What "ksa" names, a market, a network or a scheme, isn't stated, so I didn't make it a scope. If it names Saudi Arabia as the market, `ksa` belongs in its scope. The lead CM-API-001 (the developer API) is the platform's API for apps. I didn't place it there on "apis" alone.
- **`zidpay.zidpay_insights`, on CM-ANL-001.** It could be ZD-1's Zid Insights (ZD-E-806545f3) or Zid Pay's Payments analytics. Both are CM-ANL-001's.
- **`zidpay.zidsplitting`, on CM-PLN-006 and CM-PAY-002.** I read it as Wallet Splitting: a share of each Zid Payments transaction into the Zid wallet, for 'wallet expenses, such as shipping, add-ons, or internal costs' (line 1891), with the split amount able to be the 'Waybill Amount' (line 1904). The CM-PLN-006 cell holds the wallet deduction from Zid Pay (the coordinator, after batch 3), which may be the same thing.
- **`zidpay.deposit_details_invoice_export`.** Whose invoice it is, the deposit fee's or another, isn't stated.
- **`zidpos.cash_payment`, on CM-POS-001 alone.** It is a POS payment method (ZD-5's 'Cash', ZD-E-f3fa4a49). It isn't CM-POS-003's cash management (cash tracking, drawers). The POS subscription's hardware lists 'Cash drawer' (below, for the second stage).
- **`zidpos.geobased`, on CM-POS-001 alone.** I read it as 'Enable location-based POS access', 'Restrict staff access to POS data and registers based on their assigned locations.' (lines 75, 74). It could take CM-STF-002 (staff access) or CM-INV-005 (locations). The key's word alone doesn't name either.
- **`zidpos.barcode_scanning` and `.bluetooth_prinitng`, on CM-POS-001 alone.** They could take CM-POS-002, whose name is POS hardware, but its note limits it to 'The device that takes the buyer's card at the point of sale'. The POS subscription lists a 'Barcode Scanner' and a 'Receipt Printer' (lines 319, 320).
- **`zidpos.pay_in_card`, on CM-POS-002.** This is the card-present payment the cell holds (ZD-S-0978).
- **`zidpos.request_stock_through_cashier`, on CM-INV-006.** CM-INV-006's own reading says the plan line Request Inventory via POS (ZD-I-0256) 'may be a transfer request, but nothing says so'. I placed it there on that reading. What would settle it: the POS app's request screen.
- **`zidpos.channels_allocation` and `.product_channels`, on CM-CHN-001.** What is allocated, products or stock, and to which channels isn't stated. The leads CM-CHN-004 (feeds) and CM-AIA-005 (agentic commerce) aren't the thing.
- **`zidpos.delivery_through_zidpos`, on CM-SHP-001.** Who delivers isn't stated. If it is the store's own delivery, it is CM-SHP-008 (local delivery), which holds nothing on Zid.
- **`zidpos.customize_bill`, `.send_invoice_through_email` and `.send_sms_invoice`, on CM-ORD-008.** I read the POS bill as the invoice issued for a sale, with the POS's 'Invoice templates'. They take no CM-NTF-004 line: email and SMS are how the invoice is sent, not the thing.
- **`zidpos.traffic_analysis`, on CM-ANL-001.** At a point of sale, traffic may be footfall rather than the store's visits.
- **`zidpos.quantity_clarification_through_cashier`, on CM-INV-001.** What is clarified isn't stated.
- **`zidpos.cashier_support`, on CM-ONB-003.** I read it as Zid's support for the cashier.
- **`zidship.balance_under_processing`, `.current_balance` and `.service_collections_*`, on CM-SHP-002.** I read them with Zid Logistics' prepaid balance and 'service collection window' (lines 9381, 9382). `balance_under_processing` could be the cash collected on delivery awaiting transfer (CM-PAY-029). What a 'prohibited recharge' is isn't stated. The leads CM-PAY-023 (the merchant's money account, Shopify Balance) are another thing, which the cell's own reading says Zid doesn't show.
- **`zidship.commercial_registry_information`, on CM-ACC-004 too,** read as the store's commercial registration given to ZidShip. `contact_information` takes CM-SHP-002 alone.
- **`zidship.smsa_customized` (enabled) and `.aramex_customized` (disabled), on CM-SHP-015 alone.** I read "customized" as the custom connection with a carrier under the merchant's own contract (الربط المخصص مع شركة الشحن, ZD-S-0849). It could instead be a ZidShip service customized for that carrier, which would take CM-SHP-002.
- **The drop-offs (disabled), on CM-SHP-002 and CM-SHP-015.** I read them as ZidShip's self drop-off service levels for each carrier ('Self drop-off', lines 9716, 9704). The carrier named is the capability's evidence, not a filler. The service levels `cold`, `fast`, `heavy`, `no_rush` and `now` (disabled) are on CM-SHP-002 alone. "Now" and "no rush" are read with 'Shipping by speed' and the help centre's delivery speed.
- **`zidship.total_cod_collections`, on CM-ANL-001 alone,** as a measure, read with 'Total COD payments collected' (line 16089). It could instead be a figure of the ZidShip page, with a CM-PAY-029 line.

## A structure whose items and sources disagree

None found. I compared each of the 142 items with the answer's `user.store.subscription.policies_v2` and `policies`: every `enabled`, `config` and `available_in` matches, and each `policies` value matches the older map. Each entry's text matches its item, in order.

## What a source states that no entry holds (leads for the second stage)

- **The POS subscription's hardware** (`zidpos:subscription.features.*`, `dashboard-locales/items.jsonl`, lines 316 to 322): 'Cash drawer', 'Receipt Printer', 'Barcode Scanner', 'Tablet', 'Tablet stand'. For CM-POS-002, and 'Cash drawer' for CM-POS-003, which holds nothing on Zid.
- **'POS order push notifications'**, 'Get notified in the Zid App when POS orders are created' (lines 80, 79), for CM-NTF-002.
- **Zid Logistics' prepaid payment options** (lines 9378, 9379): online top-ups in multiples of 50, up to 1,000,000; bank transfers of at least SAR 50,000. These are qualities for CM-SHP-002.
- **Zid Logistics' weekly invoice** of the amounts deducted from the prepaid balance (line 9382), for CM-SHP-002.
- **The tax settings' 'Show the VAT certificate at the bottom of the website page'** (line 3159) and 'For Saudi stores, tax regulations for e-commerce stores stipulate that the certificate must be shown in the store.' (line 3165), for CM-TAX-003, which holds ZD-S-0820 on the same rule.
- **Wallet Splitting's 'Waybill Amount'** (line 1904), 'Auto calculated based on the base waybill price only.' (line 1903), for CM-SHP-002 and CM-PLN-006.

## The checker's other lines

- **NOTEs on first leads that hold nothing:**
  - CM-PAY-031 (by "settlements", line 46, `zidpay_analytics.total_settlements`): app partners' withholdings, a different thing; the entry is a measure;
  - CM-MKT-004 (by "discount", line 61, `zidpay.card_discount`): apps' discount functions; the entry is the card discount, CM-MKT-018;
  - CM-SFR-015 (by "display", line 111, `zidpos.customer_display_screen`): the storefront's display settings; the entry is the POS's customer-facing screen;
  - CM-AIA-005 (line 148, `zidpos.product_channels`) and CM-AIA-003 (line 150, `zidpos.product_description`): no key names AI;
  - CM-B2B-002 (by "users", line 171, `zidpos.users`): business buyers; the entry is the cashier's users, the store's team;
  - CM-PAY-023 (by "banking" and "balance", lines 181 and 190): Shopify Balance's money account; the cell's reading says Zid's wallet is CM-PLN-006, and these are ZidShip's.

## Problems with the brief or the script

- None with the script.
- One rule the brief leaves loose, as in ZD-11 and ZD-12: when a policy group's part takes the group's line. I followed ZD-11 and ZD-12 (every part that is a feature of the group's product), but kept the measures off it, as the earlier batches kept measures on CM-ANL-001 alone. In this batch, 98 of the 217 lines are on a group's capability (CM-STF-001, CM-PAY-002, CM-POS-001, CM-SHP-002). For 33 entries that is the only line. The other 65 sit beside the part's own line, and only those 65 rest on the group rule.
