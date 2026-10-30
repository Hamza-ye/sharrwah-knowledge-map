# C-woocommerce: notes

## Batch 1: CHK and ORD (WC-C-047, WC-C-072, WC-C-087, WC-C-033, WC-C-070)

Read: the brief; `seed --domain C`; `model --domain C --areas CHK,ORD` (23 capabilities, all the anchor's); WooCommerce's domain C concerns and those naming C under `also`; the five concerns' statements, gaps and matches; `candidates --domain C --platform woocommerce --areas CHK,ORD`; searches named in each cell's `searched` and reading.

### How it was cut

- **No new capability.** Every WooCommerce statement of the batch found a capability of the model, or another domain's.
- **WC-C-072** (Cart and checkout) lands in the parent CM-CHK-001 by Q1's M-021: WooCommerce keeps cart and checkout together, as Salla does; Shopify splits them. Its cart endpoints are cited in the child CM-CHK-002.
- **WC-C-087** (Block extensibility and Store API extensions) lands in CM-CHK-004 by M-022, strained: it is coarser than one capability. Its statements go to CM-CHK-004 (slots, filters, events), CM-CHK-006 (Store API extensions changing the cart: a reading on role against Shopify's Cart Transform), CM-CHK-009 (additional checkout fields) and CM-PAY-019 (filtering payment methods).
- **WC-C-070** (Orders and order statuses) lands in the parent CM-ORD-001 by M-023. Its statuses, actions, notes and its deletion and restore topics go to the children CM-ORD-002, -003, -004, -012 and -013.
- **WC-C-033** (HPOS) lands in CM-ORD-001, strained, joined by the term orders. It is order storage, not order management, and it has no place of its own in the statements held: only a released feature and an option. So by the dry run's test it is not a capability. Domain A's CM-TRU-014 cites its reason statement (WC-S-0629) under WC-C-032's key, as where the store's data lives, and scope.tsv names G under `also`. The reviewer may want to move it to A or G, or split it.
- **WC-C-047** (Address autocomplete) is `moved:D`. Domain D's CM-CUS-009 (Map and location services for addresses) already cites all of its statements in WooCommerce's cell. `caps` found address autocomplete nowhere in C.

### Joins on role (readings)

- CM-CHK-006: the guides Marking a cart item as a child of another cart item and Updating the cart on-demand, and /cart/extensions, against Shopify's Cart Transform.
- CM-CHK-008: express checkout methods (the Wallets & express checkouts category; WooPay's Express checkouts section) against Salla's quick checkout and Shopify's accelerated checkout buttons.
- CM-CHK-009: additional checkout fields, added by code, against Salla's custom order fields.
- CM-PAY-019: Filtering payment methods in the Checkout block against Shopify's Payment Customization and Salla's payment restrictions. U-022 is ruled joined on this.
- CM-ORD-006: WooPayments' fraud protection rules and Stripe Radar against the platforms' fraud analysis.

### WordPress and Automattic (readings)

- **WordPress.** The order is a WordPress post type (shop_order), with permissions mapped by WordPress's capabilities (WC-S-5406, WC-S-0039). Orders were traditionally stored as WordPress posts (WC-S-0629). network-orders is WordPress multisite's (WC-S-0089, read as domain A read it). Users' roles are assigned in WordPress's Users screen (WC-S-0884, found under CM-ORD-007, not cited).
- **Automattic's services.** WooPayments is the provider in CM-ORD-006 (fraud protection, Radar rules managed by "our team") and CM-CHK-008 (Express checkouts section). The maker statements are WC-S-0557 ("designed by Woo for Woo") and WC-S-0459 (WooCommerce, Inc. for Woo Services, in WooPayments' terms; it is WC-S-0458, under domain A's WC-C-023, that names WooPayments among Woo services). Stripe Radar is a third party's (outside, and a slot filler). Checkout Field Editor's and Xero's makers are only in their statements' notes, which never count: a gap.

### Homonyms

None new. The word "Draft" in WooCommerce's status Draft (checkout-draft) (WC-I-0324) is not Shopify's Draft orders (CM-ORD-005). The status is cited in CM-ORD-003 only, and its meaning isn't stated.

### Concerns read under `also`

- WC-C-107 (E): the category Cart and checkout features (CM-CHK-004), and Checkout Field Editor (CM-CHK-009).
- WC-C-109 (G): the category Order management (CM-ORD-001).
- WC-C-031 (A, rate limiting): read, not cited.

### Cited from a domain that doesn't name C (the checker's flag)

- WC-C-068/decides/WC-S-5401 (B, Hold stock), in CM-ORD-004 as `shows` only. It is the one statement held that says WooCommerce cancels an order.

### The checker's flags, answered

- **own-service on WC-S-5337, WC-S-0621, WC-S-0862, WC-S-0865.** These statements name WooPayments, not the company. Each cell also cites the maker statements WC-S-0557 and WC-S-0459, as A-woocommerce and D-woocommerce did with WC-S-0458.
- **WC-S-0557 (and WC-S-0459) in two trees, CM-CHK-008 and CM-ORD-006.** They are maker evidence for WooPayments, cited in each cell that WooPayments provides. They are not a sign of one capability.
- **core on boundary statements only (CM-CHK-002, CM-ORD-002, CM-ORD-005, CM-ORD-012, CM-ORD-013).** The Store API, the orders API and the webhook topics are WooCommerce's own APIs for its own features: core, by the dry run's ruling. CM-ORD-002's statement also names the admin's Edit Order screen.
- **none-held with matching statements:**
  - CM-CHK-003: WooPay on the checkout page; PCI and the checkout page; the classic product editor; the Block Email Editor and Unified block editor assets. None is an editor of the checkout.
  - CM-CHK-005: PCI-validated payment fields; WooCommerce Shipping validating data; EU VAT Number. None is a rule that stops a cart or checkout.
  - CM-CHK-007: listed in the cell's reading.
  - CM-ORD-007: the capabilities assigned to roles (WC-S-5415).
  - CM-ORD-008: listed in the reading. Also the merchant's responsibility for giving receipts for each charge (WC-S-0468, WC-C-027, domain A), which is not the store's order invoice.
  - CM-ORD-009: Settings tab labels and shipping labels match "label" and "print". None is a printed order document.
  - CM-ORD-010: Coming soon mode and Blueprint import, which concern the site, not orders.
  - CM-ORD-011: product tags and payment-suggestion tags.

### Uncited statements of the batch's concerns

These are left for other cells:
- WC-S-0452 (AbstractPaymentMethodType) and WC-S-0785 (Payment method integration): for the PAY batches. WC-C-001 holds WC-S-0785 too.
- WC-S-0792 (filters on Coupons): discounts, domain D.
- WC-S-0797 to WC-S-0800 (the product collection and On-Sale Badge blocks): the storefront and catalogue.
- WC-S-0453 (ExtendSchema) and WC-S-0773 to WC-S-0777 (Extending the Store API): domain E's Store API. CM-SFR-012 cites WC-S-0773 under WC-C-079.
- WC-S-0795 (How the checkout block processes an order): CM-CHK-001 or -004 could cite it as `shows`.
- WC-S-5367 and WC-S-5366 (HPOS backfill and CRUD).
- WC-S-0212 (wc-analytics Orders): domain D.
- WC-S-0089 (network-orders): domain A.
- WC-I-0322 (Refunded): left for RET.
- WC-I-0347 (Clear Customer Sessions When Empty): its meaning isn't stated.

### Gaps

- Where WooCommerce's checkout is styled or configured: no statement held, beyond Page setup, whose effect isn't stated (CM-CHK-003, CM-CHK-001).
- No statement held lists WooCommerce's order statuses. CM-ORD-003 and CM-ORD-004 cite Q1's placed inventory entries WC-I-0317 to WC-I-0324.
- There is no maker statement for Checkout Field Editor or Xero.
- Q1's gaps: WC-C-033, WC-C-047, WC-C-070, WC-C-072 and WC-C-087 have responsible stated only in general terms, and reason not found for all but WC-C-033.

### For the later batches

- **CM-PAY-019's WooCommerce cell is written here**, citing WC-S-0784 only, so that U-022 could be ruled. Batches 2 and 3 add evidence rows to it, such as WooCommerce's or an extension's settings for payment-method conditions, and don't write the cell again. They rule U-022's pairs for WC-C-001 when they land it. WC-C-001 holds WC-S-0784 and WC-S-0785.
- **U-021** (SH-C-059, SA-C-122, WC-C-013, WC-C-115): CM-ORD-006's WooCommerce cell already cites WC-C-013's WC-S-0862 and WC-S-0863 and WC-C-115's WC-S-0864 and WC-S-0865. The batch that lands WC-C-013 and WC-C-115 rules their pairs against SH-C-059 and SA-C-122, both in CM-ORD-006: joined:CM-ORD-006 by these cells. If those concerns land in PAY, their fit is strained, since these statements are in the ORD tree.
- **U-026** (SH-C-074, SA-C-079, WC-C-015): CM-CHK-008's WooCommerce cell cites WC-C-015's WC-S-5337 and WC-S-5339. SA-C-079 is landed in CM-CHK-008, so WC-C-015 against SA-C-079 follows CM-CHK-008's cells. WC-S-0654 (WooPay saves the buyer's details) is uncited, for CM-PAY-014.
- **CM-CHK-008 also cites** WC-C-005's WC-S-0707 (Wallets & express checkouts) and WC-C-006's WC-S-0621, WC-S-0557 and WC-S-0459. The PAY batches may cite WC-S-0707 in CM-PAY-012 too.
- **Batch 4:**
  - RET: Refunded (WC-I-0322) is uncited. WC-C-091's WC-S-5443 is cited in CM-ORD-013 as `shows`.
  - TAX: EU VAT Number's validation at checkout (WC-S-5464), and WooPayments' fee invoices (WC-S-5309, WC-S-5310, WC-S-0549), were found under CM-ORD-008 and not cited.
  - SHP: the Marketplace category Inventory and order management (WC-S-0714, WC-C-061's) is cited in CM-ORD-001.
- **U-079:** WC-C-047 against SH-C-111 is ruled apart here. WC-C-047 against SA-C-065 isn't ruled: both are cited in domain D's CM-CUS-009, where WC-C-047 moves. The coordinator, or D's amendment, rules it joined:CM-CUS-009.
- **Rename:** none proposed. CM-CHK-008's name could add WooCommerce's term express checkouts.

## Batch 2: PAY, first batch (WC-C-001 to WC-C-011)

Read: the brief; `model --domain C --areas PAY` (32 capabilities, all the anchor's, CM-PAY-019 with batch 1's WooCommerce cell); the eleven concerns' statements, gaps and matches; the batch-3 concerns' statements (WC-C-012, -014, -015, -016, -020, -042, -048, -098, -116), read to write the cells they bear on; `candidates --domain C --platform woocommerce --areas PAY`; the searches named in each cell's `searched` and reading; the anchor's PAY evidence and slot fillers, to rule; E-woocommerce's notes on the coordinator's corrections.

### How it was cut

- **No new capability.** All eleven concerns joined capabilities of the model, ten by their Q1 match, one (WC-C-004) on role. `caps --terms "suggestion; suggest; recommend; onboarding task; setup task; ..."` found nothing in C for payment suggestions; domain A's CM-ONB-004 holds WooCommerce's setup tasks and extension suggestions in general.
- **WooCommerce cells:** written for all 31 PAY capabilities that had none. 23 cite statements, 8 are `none-held` (CM-PAY-008, -010, -023, -024, -025, -027, -031, -032). CM-PAY-019 has one evidence row added (below).
- **WC-C-001** (gateway payments) lands in the parent CM-PAY-001 by M-025, clean: its settings and API are cited there, its gateway framework (WC_Payment_Gateway, woocommerce_payment_gateways, AbstractPaymentMethodType, Payment method integration) in the child CM-PAY-011 as extension-point, the role of Shopify's Payments Apps API.
- **WC-C-002** (offline methods) lands in the parent CM-PAY-016 by M-033, strained: check payments stay in CM-PAY-016, cash on delivery goes to CM-PAY-029, direct bank transfer to CM-PAY-030; WC-S-0604 (process_payment, 'Awaiting BACS payment') is cited in CM-PAY-020 and WC-S-5004 by batch 1 in CM-ORD-003, both under CM-ORD-001.
- **WC-C-003** (PayPal Standard) lands in CM-PAY-013 by M-032, clean.
- **WC-C-004** (payment provider suggestions per store country) lands in CM-PAY-001 on role, strained: the per-country list of payment extensions offered at Set up payments, against Shopify's providers 'compatible and available in your region' (SH-S-0584). It is a recommendation of extensions, finer than the settings; the reviewer may split it into a capability of its own (it has its own resource, wc-admin payment-gateway-suggestions, and a remote source on WooCommerce.com). Its onboarding tasks would also suit domain A's CM-ONB-004.
- **WC-C-005** (Marketplace Official payments) lands in CM-PAY-011 by M-025, strained: its subcategories are cited in the siblings CM-PAY-012, -015, -018 and -021, and Wallets & express checkouts also in CM-CHK-008 (batch 1). The reviewer may prefer the parent CM-PAY-001, the grain of all its subcategories. B2B payments (WC-S-0710) and Payment management (WC-S-0745) are left uncited: their content isn't stated.
- **WC-C-006** (WooPayments), **WC-C-010** (its countries) and **WC-C-011** (its restricted businesses) land in CM-PAY-002, by M-026 and M-085. WC-C-006 is strained (its statements are cited in CM-CHK-008 and CM-ORD-006 by batch 1, and in E's CM-POS-002, CM-MKS-006 and -007), WC-C-011 strained (WC-S-5296 in CM-PAY-020), WC-C-010 clean.
- **WC-C-007** lands in CM-PAY-005 (M-027), **WC-C-008** in CM-PAY-006 (M-028), both clean; **WC-C-009** in CM-PAY-003 (M-003), strained, since domain A's CM-TRU-002 and CM-TRU-016 cite WC-S-0504, WC-S-0522 and WC-S-0558 as shows (the checker reads only domain C's trees; the mark follows the dry run's S1 across domains).

### Joins on role (readings)

- CM-PAY-001: WooCommerce's payment extension list for each country (WC-S-0618), against Shopify's gateways available in your region (SH-S-0584). U-075 is ruled joined on this.
- CM-PAY-011: WooCommerce's gateway API for plugins, against Shopify's Payments Apps API.
- CM-PAY-019: U-022's pairs for WC-C-001, as batch 1 ruled them for WC-C-087.

### WordPress and Automattic (readings)

- **WooPayments is Automattic's, not WooCommerce core.** Its cells (CM-PAY-002, -003, -005, -007, -009, -014, -021) cite its feature statements as `own-service`, and in each the maker statements WC-S-0557 ('designed by Woo for Woo') and WC-S-0459 (WooCommerce, Inc. for Woo Services), as batch 1 did; CM-PAY-002 also cites WC-S-0460 (WooCommerce Ireland Ltd.), WC-I-0626 (the terms list WooPayments among Woo Services) and WC-S-0476, which E counts as WooPayments' maker statement. By the coordinator's correction in E's notes, each counts for a different feature, each shown by its cell's own statements.
- **Stripe, not WooPayments, does several of these things,** and those cells say so: reserves (CM-PAY-006, outside only: 'Stripe, not WooPayments, applies and manages reserves'), the processing behind the service (CM-PAY-004, outside only), the verification at sign-up (CM-PAY-003, outside beside own-service), payouts refused to debit cards outside the U.S. (CM-PAY-005), and account types by country (CM-PAY-002). Stripe is a slot filler in each.
- **WooCommerce core** does the payment settings, the gateway API, PayPal Standard and the offline gateways (CM-PAY-001, -011, -013, -016, -029, -030): `core`.
- **WooCommerce.com:** the payment suggestions are fetched from WooCommerce.com (WC-S-5011, shows); PayPal Standard has a WordPress.com proxy route (WC-S-5007, shows); WooPayments needs a WordPress.com account (WC-S-0517, shows).
- **Square by Woo** (WC-S-0912) is read as Woo naming itself the extension's maker, so `own-service` in CM-PAY-011, with Square as the provider and a slot filler. 'Stripe by Stripe' and 'PayPal Payments by PayPal' are third parties' extensions: extension-point.
- **WooPay** (CM-PAY-014): no statement held names its maker. The cell rests on 'When you use WooPayments, WooPay may be available as a checkout option' (WC-S-0849), so WooPayments' maker statements are cited: a reading, and a gap.
- **Stripe Capital** (CM-PAY-026): 'WooCommerce has partnered with Stripe to offer ... the Stripe Capital program' (WC-S-0559) is read as Stripe's program: outside.

### Homonyms

None new. 'Payments' is both WooCommerce's settings tab (WC-S-0005) and the admin menu that WooPayments owns once onboarded (WC-S-0621); the cells keep them apart (CM-PAY-001 and CM-PAY-002). 'account balance' in WooPayments (WC-S-0529) is the payout balance (CM-PAY-005), not Shopify Balance's business account (CM-PAY-023). 'reserve' is Stripe's (CM-PAY-006), not CM-PAY-031's amounts withheld for app partners.

### Concerns read under `also`

- WC-C-109 (G): the category Accounting and the Xero extension (CM-PAY-028).
- WC-C-040 (A): its WC-S-0564 is cited under WC-C-005's key (CM-PAY-011).
- WC-C-051 (E): payout currencies, read, not cited (CM-PAY-005's reading names it).
- WC-C-018, WC-C-019, WC-C-027, WC-C-057: read in the candidates, not cited.
- WC-C-103 (D, B2B, doesn't name C): its Purchase Order Gateway is named in CM-PAY-008's `none-held` reading, not cited.

### The checker's flags, answered

- **own-service on statements that don't name the company** (WC-S-0909, WC-S-0621, WC-S-0524, WC-S-0478, WC-S-0516, WC-S-0522, WC-S-0529, WC-S-0531, WC-S-5289, WC-S-0537, WC-S-0538, WC-S-5317, WC-S-0654, WC-S-0849, WC-S-0868): each is a feature of WooPayments (or WooPay with it), and each cell also cites the maker statements WC-S-0557 and WC-S-0459. The 'we' in WC-S-0524, WC-S-0478, WC-S-0516 and WC-S-0537 is the company in Automattic's terms or WooPayments' docs, a reading. WC-S-0459, WC-S-0460, WC-I-0626 and WC-S-0476 are the maker statements themselves. WC-S-0912 is read as above.
- **Maker statements in many trees** (WC-S-0557, WC-S-0459): maker evidence for WooPayments in each cell it provides, not a sign of one capability.
- **WC-S-0621 in CM-CHK-008 and CM-PAY-002:** WooPayments owning the Payments menu; batch 1 cites it for the express checkouts section, here for the service itself.
- **WC-S-0707 in CM-CHK-008 and CM-PAY-012:** the subcategory's name, Wallets & express checkouts, names both.
- **WC-S-5004 in CM-ORD-003 and CM-PAY-030:** the filter sets a bank transfer order On hold: an order status for batch 1, the bank transfer gateway's own behaviour here.
- **WC-S-5296 in CM-PAY-009 and CM-PAY-020:** it names the Transactions and Disputes menus together.
- **core rests only on boundary statements (CM-PAY-020):** WC_Gateway_BACS::process_payment is WooCommerce's own gateway acting on the order's payment, a reading; no admin place for an order's transactions is held.
- **none-held with matching statements:** CM-PAY-008 (Buy now pay later and B2B payments, PO gateway: the cell's reading); CM-PAY-010 (WooPayments' fraud protection and Radar, CM-ORD-006; responsibility statements; warranty disclaimers); CM-PAY-023 (WooPayments' balance and payouts, CM-PAY-005); CM-PAY-024 (the payment suggestions match 'visa' and 'Cards'; buyers' cards); CM-PAY-025 (WooPayments accepts credit cards, WC-S-0871; order attribution 'credit'); CM-PAY-027 (vendor agreements, PCI); CM-PAY-031 (Stripe, partners, deductions, reserves, repayment withholding); CM-PAY-032 (Xero's Send Invoices). None is the capability.

### Rulings

U-022 (WC-C-001's two pairs, joined:CM-PAY-019), U-023 (WC-C-005 against SH-C-078, SA-C-110 and SA-C-119, joined:CM-PAY-012), U-024 (WC-C-006 against SH-C-080 and SA-C-110, joined:CM-PAY-017), U-025 (joined:CM-PAY-018), U-034 (both apart), U-038 (WC-C-011 against SH-C-173 and SA-C-172, joined:CM-PAY-002) and U-075 (joined:CM-PAY-001). The joins for U-023, U-024 and U-025 rest on a category's or a doc's name only; U-024's WooCommerce side is `shows` only ('By default, WooPayments accepts payments via credit and debit cards', under the title Local payment methods). U-038 against SA-C-172 joins two sets of terms accepted to use the payment service; Salla's policy text isn't held. WC-C-011 against WC-C-022 is a pair of one platform, not ruled.

### Batch 1's rows

- No problem found. CM-PAY-019's reading says the PAY batches would search for a setting of payment-method conditions: searched (enable_for_methods; enable for shipping; enable_for_virtual; virtual orders; available_payment_gateways; is_available; hide payment; restrict), nothing found. Its new row cites WC-S-0784 under WC-C-001's key too, so U-022 could be ruled for WC-C-001.
- Batch 1 left WC-S-0452 and WC-S-0785 to the PAY batches: they are cited in CM-PAY-011 under WC-C-001's keys; WC-C-087's keys for them stay uncited.

### For batch 3 (WC-C-012 to -016, -020, -042, -048, -098, -115, -116)

The cells are written; batch 3 lands its concerns and adds evidence rows, without rewriting the cells:
- **WC-C-012** → CM-PAY-007 (M-029). The cell cites WC-S-0537 and WC-S-0538. Left: WC-S-5298, WC-S-5299, WC-S-0649, WC-S-0650, WC-S-0534, and the Amazon Pay statements WC-S-5297 and WC-S-5300, which may also go to CM-PAY-012 (WooPayments offering Amazon Pay isn't stated in those words).
- **WC-C-013, WC-C-115** → U-021, as batch 1's notes say (CM-ORD-006). WC-C-013 is in M-088 with SA-C-122 (CM-ORD-006).
- **WC-C-014** → CM-PAY-021 (M-036 with SH-C-086). The cell cites WC-S-0868 (own-service) and WC-S-0711 (WC-C-005). Left: WC-S-0869 (countries), WC-S-0870 (a quality: card readers collect only the country's default currency), WC-S-0850 (Stripe Terminal terms: a slot filler), WC-S-0481. U-074: WC-C-014 against SA-C-095 (E, naming C) follows CM-PAY-021, whose Salla cell cites SA-C-095; against SH-C-143 (E, not naming C): apart, unless a C cell cites it. E ruled joined:CM-POS-002 from E's cells.
- **WC-C-015** → CM-PAY-014 (no Q1 match; U-026). The cell cites WC-S-0654 and WC-S-0849. U-026: against SH-C-074 (landed in CM-PAY-014) and SA-C-079 (CM-CHK-008, whose WooCommerce cell cites WC-S-5337 and WC-S-5339): both pairs follow those cells. CM-PAY-014 is under CM-CHK-008, one tree.
- **WC-C-016** → CM-PAY-026 (M-038). The cell cites WC-S-0748 and WC-S-0559 (Stripe a slot filler). Left: WC-S-0560 (Celtic Bank, outside, a slot filler), WC-S-0561, WC-S-0861, WC-S-5302.
- **WC-C-020** → CM-PAY-004 (U-027 against SH-C-065, SH-C-066, SH-C-067, SA-C-114 and SA-C-177, all in CM-PAY-004). Its WC-S-0507 (Stripe's Connected Account Agreement) is uncited.
- **WC-C-042, WC-C-098** → CM-PAY-022 (M-035 with SH-C-085). The cell cites WC-S-0943 and WC-S-0438. Left: WC-S-0360, WC-S-0364 (privacy exporter and eraser), WC-S-0554, WC-S-0552, WC-S-0480, WC-S-0501, and WC-S-5468 (Enable payments via saved cards, 'check out much faster'), which may suit CM-PAY-014 better.
- **WC-C-048** → CM-PAY-004 (M-037 with SH-C-064). U-071: against SH-C-064 follows CM-PAY-004; against SA-C-235 (G, naming C) follows whichever C cell cites it.
- **WC-C-116** → CM-PAY-009 (M-030 with SH-C-072). The cell cites WC-S-5317, WC-S-0866 and WC-S-5321. Left: WC-S-5318 (an alert under WooCommerce > Orders), WC-S-5319, WC-S-5320, WC-S-5322, WC-S-0867, WC-S-5323, WC-S-0469, WC-S-0649.
- The pairs whose WooCommerce side batch 3 lands: U-021, U-026, U-027, U-071, U-074.

### Gaps

- Which local payment methods WooPayments offers, and where: only the doc's title is held (CM-PAY-017).
- Who acquires WooPayments' transactions and holds the funds, under which licence (CM-PAY-004; Q1's gap on WC-C-020).
- No maker statement for WooPay itself, nor for the Xero extension (CM-PAY-014, CM-PAY-028).
- What the Marketplace subcategories B2B payments, Payment management, Buy now pay later and Crypto payments hold: only their names (CM-PAY-008, -011, -015, -018).
- Where the store's bank details for direct bank transfer are shown, and who collects cash on delivery (CM-PAY-029, -030).
- Q1's gaps: WC-C-001 to WC-C-005 reason searched, not found; WC-C-002 and WC-C-004 responsible stated only in general terms; WC-C-008, WC-C-009 and WC-C-010 responsible page not read; WC-C-010 where and boundary need observation.

### Renames proposed

None. CM-PAY-016's name could add WooCommerce's term offline, and CM-PAY-002's WooPayments.

## Batch 3: PAY, second batch (WC-C-012 to -016, -020, -042, -048, -098, -115, -116)

Read: the brief; `model --domain C --areas PAY` (32 capabilities, batch 2's WooCommerce cells), CM-ORD-006 and CM-CHK-007 in `model`; the eleven concerns' statements, gaps and matches; the anchor's rulings and evidence on the pairs' other sides (SH-C-059, SA-C-122, SH-C-064 to -067, SH-C-074, SA-C-079, SA-C-114, SA-C-177, SA-C-095); E-woocommerce's U-074 rulings and its CM-POS-002 rows; where else the concerns' statements are cited (A's CM-PLN-005, CM-TRU-007, CM-TRU-010, CM-TRU-018; E's CM-POS-002); `caps --terms "privacy; personal data; share data; processor"`.

### How it was cut

- **No new capability.** All eleven concerns joined capabilities of the model: eight by their Q1 match, one by definition (WC-C-015), two on role (WC-C-020, WC-C-115). No cell was written; 41 evidence rows were added to batch 1's and 2's cells, with four qualities and six slot fillers.
- **WC-C-012** → CM-PAY-007 (M-029), strained by the dry run's S1 across domains, as batch 2 marked WC-C-009: A's CM-PLN-005 cites WC-S-0538 under its key. Its negative balance recovered by debiting the bank account (WC-S-0534) goes to CM-PAY-005, and Amazon Pay as a wallet (WC-S-5300) to CM-PAY-012, both in the same tree.
- **WC-C-013** → CM-ORD-006 (M-088, SA-C-122 landed there), clean; **WC-C-115** → CM-ORD-006 on role, clean. Both stay in ORD with batch 1's cell, not PAY, so batch 1's warning that they'd be strained in PAY doesn't arise.
- **WC-C-014** → CM-PAY-021 (M-036), strained: E's CM-POS-002 cites five of its statements under its keys. WC-S-0481 (third-party POS terminals, as-is) is left to E's device capability.
- **WC-C-015** → CM-PAY-014 by definition against Shop Pay (WC-S-0654, SH-S-0406), clean: its other statements are in the parent CM-CHK-008.
- **WC-C-016** → CM-PAY-026 (M-038), clean.
- **WC-C-020** → CM-PAY-004 on role, clean: its one statement is Stripe's Connected Account Agreement (WC-S-0507), `shows`, with Stripe a slot filler.
- **WC-C-042** → CM-PAY-022 (M-035), strained: its setting Enable payments via saved cards (WC-S-5468) is cited in CM-PAY-014, under CM-CHK-008. Saving a card 'to check out much faster' is CM-PAY-014's definition (and Salla's checkout-save-cards there), not a store charging a saved method without checkout. The reviewer may prefer CM-PAY-022 for it; then the fit is clean.
- **WC-C-048** → CM-PAY-004 (M-037), clean; the terms' power to terminate access or force refunds (WC-S-0472) goes to the parent CM-PAY-002 as `shows`.
- **WC-C-098** → CM-PAY-022 (M-035), clean. Its privacy exporter and eraser (WC-S-0360, WC-S-0364) are cited `shows`: A's CM-TRU-007 cites them as core under WC-C-045's keys, for data requests, so `core` here would put one statement's core in two domains.
- **WC-C-116** → CM-PAY-009 (M-030), clean.

### Joins on role and by definition (readings)

- CM-PAY-004 (WC-C-020): Stripe's Connected Account Agreement, accepted at WooPayments' signup, against Shopify's Payment Processor Terms (SH-S-0144) and Salla's payment services contract (SA-S-0081): the agreement under which the processing behind the service is done. Neither WooCommerce's nor Salla's text is held.
- CM-ORD-006 (WC-C-115): Stripe Radar's screening of WooPayments' transactions against Shopify's fraud analysis (SH-S-0747, SH-S-0750) and Salla's fraud protection system (SA-S-1971).
- CM-PAY-014 (WC-C-015), by definition: WooPay and Shop Pay both save the buyer's shipping and payment details for a faster checkout.

### WordPress and Automattic (readings)

- **WooPayments, Automattic's service:** the fees (CM-PAY-007), the negative balance's recovery (CM-PAY-005), the fraud rules' generic error (CM-ORD-006), the saved-cards setting (CM-PAY-014) and the dispute alert and email (CM-PAY-009) are `own-service`, each cell already citing the maker statements WC-S-0557 and WC-S-0459, as batch 2 did. The dispute alert sits on WooCommerce's own order page under WooCommerce > Orders (WC-S-5318), but it is WooPayments' notice: own-service, not core.
- **Stripe, not WooPayments:** the processing account (a Stripe Express account, WC-S-0504), the Express dashboard where some account details are changed (WC-S-5311), the Connected Account Agreement (WC-S-0507) and Stripe Terminal's terms for in-person payments (WC-S-0850): `outside` or `shows`, Stripe a slot filler.
- **Others named:** Celtic Bank issues the Stripe Capital loans (WC-S-0560, outside, slot filler); the cardholder's bank decides a dispute (WC-S-5322) and card networks impose the dispute fees (WC-S-5323): outside, slot fillers.
- **WooCommerce core:** only the Payment Token API and its privacy exporter and eraser (CM-PAY-022).

### Homonyms

None new. 'account' is WooPayments' account, whose balance is CM-PAY-005's (WC-S-0534), and the Stripe Express account behind it (CM-PAY-004); neither is CM-PAY-023's business account. 'saved cards' in WooPayments (WC-S-5468, CM-PAY-014) and WooCommerce's payment tokens (WC-S-0943, CM-PAY-022) are both read with M-035; the cut between them follows each capability's definition, above.

### Concerns read under `also`

None beyond batch 2's. A's WC-C-018 cites WC-S-0552 and WC-S-0554 (CM-TRU-018), and WC-C-027 cites WC-S-0469 (CM-TRU-010); here WC-S-0554 and WC-S-0469 are cited under WC-C-042's and WC-C-116's own keys, as outside and shows.

### Rulings

- **U-021:** WC-C-013 and WC-C-115, each against SH-C-059 and SA-C-122: joined:CM-ORD-006 (four rows).
- **U-026:** WC-C-015 against SH-C-074, joined:CM-PAY-014; against SA-C-079, joined:CM-CHK-008. nested:CM-PAY-014 would hold too, since WooPay lands in the child. The anchor ruled SH-C-074 against SA-C-079 nested:CM-PAY-014.
- **U-027:** WC-C-020 against SH-C-065, SH-C-066, SH-C-067, SA-C-114 and SA-C-177: joined:CM-PAY-004 (five rows). The joins rest on agreements' names; the licensed entity isn't held on WooCommerce's side or Salla's.
- **U-071:** WC-C-048 against SH-C-064, joined:CM-PAY-004 (M-037); against SA-C-235, apart (domain G's CM-OPS-001; no C cell cites it).
- **U-074:** WC-C-014 against SA-C-095, joined:CM-PAY-021 (C's cells cite WC-S-0868 and SA-S-5040); against SH-C-143, apart (scope.tsv gives it E, not naming C). **For the coordinator:** E-woocommerce ruled both pairs joined:CM-POS-002 from E's cells. For SA-C-095 both domains join it. For SH-C-143 the domains differ, C apart and E joined: the merge's difference, by the coordinator's note after batch 2.

### Earlier batches' cells whose readings are now out of date

The coordinator updates them. Each still says batch 3 will add the rest:
- **CM-ORD-006:** 'U-021 waits on them': U-021 is now ruled. Add: WooPayments shows a generic error so as not to reveal the rules (WC-S-5301, own-service).
- **CM-PAY-002:** add shows: the terms' power to terminate access or force refunds (WC-S-0472, WC-C-048).
- **CM-PAY-004:** 'batch 3 lands WC-C-020 and WC-C-048': add outside: the Stripe Express account (WC-S-0504, under WC-C-048), powered by Stripe (WC-S-0651, under WC-C-048), and account details changed only in the Stripe Express dashboard (WC-S-5311). Add shows: the Connected Account Agreement (WC-S-0507, under WC-C-020 and WC-C-048), an alternative processor that may be integrated (WC-S-0477), no existing Stripe account (WC-S-0873, WC-S-5312), opting out of Stripe's agreement (WC-S-0508, WC-S-0509) and no Stripe Dashboard (WC-S-0506, under WC-C-048). Who holds the funds, and under which licence, is still not held.
- **CM-PAY-005:** add own-service: WooPayments may debit the bank account to recover a negative balance (WC-S-0534, WC-C-012).
- **CM-PAY-007:** 'batch 3 lands WC-C-012 and adds the rest': add own-service: the fee factors (WC-S-5298) and Amazon Pay's fee and refund in the order timeline (WC-S-5297, scope Amazon Pay non-card payments). Add shows: transaction fees not refunded on refunds (WC-S-5299), transaction and dispute fees in the terms (WC-S-0649) and the merchant responsible for fees (WC-S-0650).
- **CM-PAY-009:** add own-service: the alert on the order page (WC-S-5318) and the email (WC-S-5319). Add outside: the outcome decided solely by the cardholder's bank (WC-S-5322) and dispute fees imposed by card networks (WC-S-5323). Add shows: WC-S-5320, WC-S-0469, WC-S-0649 and WC-S-0867.
- **CM-PAY-012:** 'Amazon Pay fees ... are for batch 3': WC-S-5300 is cited here as shows (Amazon Pay a wallet), and WC-S-5297 in CM-PAY-007.
- **CM-PAY-014:** 'batch 3 lands WC-C-015 and rules U-026' and 'WC-S-5468 is left to batch 3': both are done. Add own-service: Enable payments via saved cards (WC-S-5468, WC-C-042). Add shows: U.S. merchants only (WC-S-5338) and Automattic not a party to the transaction (WC-S-0482).
- **CM-PAY-021:** add shows: the countries (WC-S-0869) and the default currency only (WC-S-0870). Add outside: Stripe Terminal's terms (WC-S-0850).
- **CM-PAY-022:** add outside: WooPayments' tokens stored by its payment partner (WC-S-0554, WC-C-042). Add shows: the privacy exporter and eraser (WC-S-0360, WC-S-0364).
- **CM-PAY-026:** add outside: Celtic Bank (WC-S-0560). Add shows: the daily eligibility review (WC-S-0561), repayment by a percentage of transactions (WC-S-0861) and withholding after seven days (WC-S-5302). The reviewer may also read 'WooCommerce has partnered with Stripe to offer ... access' (WC-S-0559) as own-service, the company arranging the financing, beside batch 2's outside.

### The checker's flags, answered

- **own-service on statements that don't name the company** (WC-S-5298, WC-S-5297, WC-S-0534, WC-S-5301, WC-S-5468, WC-S-5318, WC-S-5319): each is a feature of WooPayments, from its docs or its settings guide (WC-S-5468's note: 'The WooPayments settings are under Payments > Settings'). Each cell already cites the maker statements WC-S-0557 and WC-S-0459.
- **none-held cells matching this batch's statements:**
  - CM-PAY-010: WC-C-013's fraud rules (CM-ORD-006) and WC-S-0650's negative balance (CM-PAY-005, -007). None is cover against chargebacks.
  - CM-PAY-023 and CM-PAY-031: WooPayments' balance, payouts and Stripe account (CM-PAY-004, -005). None is a business account or a withholding for app partners.
  - CM-CHK-007: WC-S-0534, 'Paused to recover a negative balance', is payouts, not an abandoned checkout.
  - CM-CHK-005: WC-S-0552 is the PCI-validated payment fields, as batch 1 answered.
  - CM-CHK-003: WC-S-0849, WooPay on the checkout page, as batch 1 answered.
- The other flags are batch 1's and 2's, answered in their sections.

### Uncited statements of the batch's concerns

- Duplicates of a cited statement under another placement of the same concern: WC-C-013/decides/WC-S-0862, WC-C-014/boundary/WC-S-0868, WC-C-015/boundary/WC-S-0849, WC-C-042/boundary/WC-S-0554, WC-C-048/boundary/WC-S-0504, WC-C-098/decides and /boundary/WC-S-0943, WC-C-115/reason/WC-S-0864.
- Left to domain A, which scope.tsv names under WC-C-042's also: WC-S-0552 (the payment fields in the partner's PCI DSS-validated environment, A's CM-TRU-018 under WC-C-018), WC-S-0480 (data shared with the payment processing third party) and WC-S-0501 (the Stripe account information Automattic receives), for A's data protection capabilities, such as CM-TRU-013 or CM-TRU-015.
- Left to domain E: WC-C-014/responsible/WC-S-0481 (CM-POS-002).
- Inventory entries, covered by statements: WC-I-0600, WC-I-0601, WC-I-0602, WC-I-0608, WC-I-0543, WC-I-0596, WC-I-0630, WC-I-0631, WC-I-0642, WC-I-0360, WC-I-0364, WC-I-0438.

### Gaps

- Who holds WooPayments' funds and under which licence: the Connected Account Agreement's text isn't held, and Q1's gaps on WC-C-020 (where, decides, boundary, reason: page not read) stand. CM-PAY-004 names Stripe as the processor only.
- Who withdraws the disputed amount and the dispute fee (WC-S-5320 doesn't say), and who reviews eligibility for Stripe Capital (WC-S-0561): not stated.
- WooPay's own maker, as batch 2 noted.
- Q1's gaps: WC-C-013 responsible stated only in general terms; WC-C-115 responsible page not read and boundary observation needed; WC-C-014, -015, -042, -048 and -098 reason searched, not found; WC-C-098 responsible stated only in general terms.

### Batch 1's and 2's rows

The checker prints no problem on them. Their out-of-date readings are listed above.

### Renames proposed

None. CM-PAY-021's name could add WooCommerce's term In-Person Payments, and CM-PAY-022's payment tokens.

### The coordinator, after batch 3

- **The eleven readings above are updated** as the list asks, each addition marked "(the coordinator, after batch 3)". Every statement it names is cited in its cell with the support the reading gives it.
- **Batch 4 is split in two.** Batch 4 maps TAX now, onto C's anchor, which is complete for TAX. Batch 5 maps SHP and RET once the anchor's last two batches have cut them, rules U-032 (WC-C-058 against SA-C-146, which the anchor's batch 11 lands) and checks the whole part.
- **WC-S-0559** ("WooCommerce has partnered with Stripe to offer ... access"): it names WooCommerce as the partner, not Automattic as the maker or provider, so batch 2's `outside` stands (C5).

## Batch 4: TAX (WC-C-021, WC-C-054, WC-C-055, WC-C-056, WC-C-058, WC-C-118)

Mapped onto C's anchor, complete for TAX (CM-TAX-001 to CM-TAX-009). No capability added: every concern is a thing the anchor already holds. Before landing, `class_slice.py caps --terms` on the batch's terms (VAT invoice; tax invoice; tax document; 1099) found only C's TAX capabilities and A's CM-PLN-007, taxes on the platform's own charges.

### How it was cut

| Concern | Capability | Join | Fit |
|---|---|---|---|
| WC-C-021 Tax reporting tied to payments | CM-TAX-009 | match:M-039 | strained |
| WC-C-054 Core tax calculation with merchant-entered rates | CM-TAX-001 | match:M-040 | strained |
| WC-C-055 WooCommerce Tax | CM-TAX-002 | match:M-040 | strained |
| WC-C-056 Third-party tax extensions (Sales tax and duties) | CM-TAX-004 | role | strained |
| WC-C-058 Customs duties and import taxes | CM-TAX-008 | match:M-042 | strained |
| WC-C-118 EU VAT Number | CM-TAX-005 | match:M-041 | clean |

- **M-040's split is the anchor's cut.** WooCommerce's merchant-entered rates (WC-C-054) land in the parent CM-TAX-001, and WooCommerce Tax (WC-C-055) in its child CM-TAX-002, as CM-TAX-002's note says.
- **WC-C-021 is cut in two by subject, one thing one domain.** The Form 1099-K WooPayments issues (WC-S-0547, WC-S-0860) is CM-TAX-009. The VAT and JCT invoices for WooPayments' fees (WC-S-5309, WC-S-5310, WC-S-0549) are taxes on the platform company's own charges, domain A's CM-PLN-007, which cites WC-S-5309 and WC-S-0549 under WC-C-057's key. They are not cited here.
- **WC-C-058's product customs data is left to SHP.** The three optional customs fields on products and variations (WC-S-5383, WC-S-5384), the REST fields customs_commodity_code, customs_country_of_origin and customs_description (WC-S-5385), and their reason (WC-S-5386, "They do not calculate duties or produce shipping labels") are product customs data for shipping. CM-TAX-008's note gives that to the SHP batch (Salla's SA-C-146). They are uncited, for batch 5.

### Joins on role (readings)

- **WC-C-056 into CM-TAX-004.** WooCommerce's Marketplace category Extensions > Store management > Sales tax and duties (WC-S-0751) and Shopify's App Store category Tax apps (SH-S-2708) play the same role: each is the platform's category for third parties' tax extensions, under different names. The fit is strained, for three reasons:
  - no WooCommerce statement held says the extensions calculate tax in place of WooCommerce's own rates, which CM-TAX-004's definition requires (Q1's gaps: WC-C-056's boundary and reason were searched, not found);
  - the category also names duties, so WC-S-0751 is cited again in CM-TAX-008, under WC-C-058's key;
  - its Terms of Service statements (WC-S-0852, WC-S-0487, WC-S-0656) are cited under WC-C-059 in F's CM-APP-001. Here they are only `shows`.

### WordPress and Automattic (readings)

- **WooCommerce Tax is Automattic's service, not WooCommerce core** (CM-TAX-002, `own-service`). The maker statements:
  - "WooCommerce Tax uses Automattic's servers and a connection to our partners" (WC-S-0956);
  - the Terms of Service list WooCommerce Tax among Woo Services (WC-I-0628);
  - the provider of Woo Services outside the Designated Countries is WooCommerce, Inc. (WC-S-0459).

  They count for this feature, which the cell's own statements show (WC-S-0633, WC-S-0639, WC-S-0636, WC-S-0635, WC-I-0621). Q1 places WC-I-0621 and WC-I-0628 in WC-C-055; `statements` prints them at the end of a two-concern call.
- **Third parties do WooCommerce Tax's calculations.** "Tax Calculations are provided by TaxJar" (WC-S-0957), and Automattic's terms say "tax calculations may be provided by Taxamo" (WC-S-0473). Both are `outside` and slot fillers.
- **The connection WooCommerce Tax needs** (WC-S-0634) is `own-service` in A's CM-ACC-010, under WC-C-049's key. Here it is `shows`, so that it doesn't support `own-service` in two domains.
- **WooPayments, not WooCommerce, issues the Form 1099-K** (CM-TAX-009, `own-service`). The cell cites WooPayments' maker statements WC-S-0557 and WC-S-0459, as batches 1 to 3 did.
- **EU VAT Number is a Woo-made extension** (CM-TAX-005, `own-service`). Its maker:
  - the product card's "EU VAT Number by Woo" (WC-S-0963), read as Woo naming itself the maker, as batch 2 read "Square by Woo";
  - Automattic's terms naming "Woo themes or extensions" among its Paid Services (WC-S-0644).

  Its settings sit in WooCommerce > Settings > Tax (WC-S-0964), but the statement names them as the extension's settings: own-service, not core. The reviewer may read "by Woo" as a brand in the product's name instead. CM-TAX-005 would then rest on WC-S-0644 alone for its maker.
- **WooPayments has no functionality related to charging tax** (WC-S-0546). It is `shows` in CM-TAX-001: the tax settings are WooCommerce's, not the payment service's.

### Homonyms

None new. "Tax" on WooPayments' fees (VAT/GST/CT on the fees, WC-S-0549) is not tax on the store's sales. It goes with A's CM-PLN-007, the anchor's homonym note on CM-TAX-001.

### Concerns read under `also`

None of the 17 `also` concerns bears on TAX. The searches found statements of other concerns, each left in its own cell:
- WC-C-057 (A, naming C): WC-S-5309, WC-S-0549, WC-S-5316;
- WC-C-049 (A, naming F): WC-S-0634;
- WC-C-038 (D): Analytics > Taxes, WC-S-0072, and wc-analytics Taxes, WC-S-0222, both in D's CM-ANL-001 and CM-ANL-002;
- WC-C-046 (E, naming D): MaxMind geolocation to display tax rates, WC-S-0641;
- WC-C-029 (A, naming C): WC-S-0470, export and import laws.

### Rulings

U-030, three rows for WC-C-056:
- against SH-C-103: `joined:CM-TAX-004`, on role;
- against SA-C-160: `joined:CM-TAX-004`. The ruling follows the cells: Salla's cell cites its unreleased flag avalara-tax (SA-S-3511);
- against SH-C-101: `apart`, since CM-TAX-003's WooCommerce cell is none-held.

**U-032 (WC-C-058 against SA-C-146) is left to batch 5**, as the coordinator's split says. SA-C-146 lands in the anchor's batch 11. WooCommerce's side is its product customs data (WC-C-058/where/WC-S-5383, WC-C-058/boundary/WC-S-5385), uncited here. The ruling follows the SHP cell that cites it.

### The checker's flags, answered

- **Two problems are printed, neither on this batch's rows.**
  - "No ruling on U-032" is batch 5's, as above.
  - "The model so far lacks 12 cells, such as CM-SHP-015 for salla": these are the anchor's SHP cells, which C-anchor is writing now (its batch 11). None is a TAX cell: every TAX capability has Shopify's and Salla's cells.
- **`own-service` on statements that don't name the company.**
  - WC-S-0633, WC-S-0639, WC-S-0636, WC-S-0635 and WC-I-0621 are features of WooCommerce Tax; their cell cites the maker statements WC-S-0956, WC-I-0628 and WC-S-0459.
  - WC-S-0964, WC-S-5464, WC-S-5462 and WC-S-5463 are EU VAT Number's; their cell cites WC-S-0963 and WC-S-0644.
  - WC-S-0547 is WooPayments'; its cell cites WC-S-0557 and WC-S-0459.
  - The flagged maker statements themselves are WC-S-0956, WC-I-0628, WC-S-0459, WC-S-0557, WC-S-0963 and WC-S-0644.
- **WC-S-0644 is `own-service` in two domains:** here, for EU VAT Number, and in E's CM-SFR-003, for themes. Under the coordinator's rule a maker statement counts for each feature its cells' own statements show. The merge may flag it.
- **WC-S-0459 and WC-S-0557 appear in many trees.** They are maker evidence, as before; CM-TAX-002 and CM-TAX-009 now cite them too.
- **CM-TAX-003 and CM-TAX-006 are none-held although statements match their terms.** The matches are the statements named in their readings: WooCommerce Tax saying it does not determine tax obligations nor file returns (WC-S-0633, WC-S-0636), WooPayments' registered business country (WC-S-0512), the 1099-K filing (WC-S-0860) and export and import laws (WC-S-0470). None shows the capability.
- **CM-CHK-005 and CM-ORD-008 (batch 1's cells) are none-held although TAX statements match.** EU VAT Number's validation at checkout (WC-S-5464) is now cited in CM-TAX-005. WooPayments' fee invoices (WC-S-5309, WC-S-5310, WC-S-0549) are A's CM-PLN-007. Neither cell's reading needs a change.

### Gaps

- No statement says where the merchant receives the Form 1099-K (CM-TAX-009).
- No statement names the hook or interface through which a tax extension replaces WooCommerce's own rates (CM-TAX-004; Q1's gaps on WC-C-056's boundary and reason).
- The EU VAT Number's maker rests on "by Woo" and on Automattic's general terms. No statement names Automattic as that extension's maker.

### For the coordinator

- **WC-S-5310** (JCT invoices for WooPayments' fees, Japan, WC-C-021/where/WC-S-5310) isn't cited anywhere. It belongs with WC-S-5309 in A's CM-PLN-007 (A-woocommerce), under WC-C-021's key, which names no domain A. That is A's to add, or the coordinator's.
- **The anchor lands SH-C-099 and SH-C-102 as `single`,** although Q1's M-039 and M-041 hold them, with WooCommerce's side only. The C-anchor part could record `match:M-039` and `match:M-041`. This batch's landings cite the matches.
- **Earlier batches' rows:** the checker prints no problem on them, and nothing in this batch makes one of their readings out of date.

### For batch 5

- Rule U-032 once SA-C-146 has landed. Cite WC-C-058's product customs data (WC-S-5383, WC-S-5384, WC-S-5385, WC-S-5386) in the SHP capability the anchor cuts for product customs data, and say in its reading that WC-C-058 lands in CM-TAX-008 (strained, for this reason).
- The whole-part check is batch 5's.

### Renames proposed

None. CM-TAX-004's name could add WooCommerce's category Sales tax and duties. CM-TAX-005's could add EU VAT Number.

### The coordinator, after batch 4

- **WC-S-5310,** the JCT invoices for WooPayments' fees, held only under WC-C-021, is now cited in domain A's CM-PLN-007 (A-woocommerce), beside WC-S-5309, and scope.tsv names A under WC-C-021's `also`.
- **The anchor's `single` landings whose Q1 match has another side in this part** (SH-C-099 with M-039, SH-C-102 with M-041) are rewritten as `match:` with the anchor's other such rows, once its last batch has run.
- **The checker's two problems** are batch 5's: U-032, once SA-C-146 has landed, and the anchor's SHP cells, which its batches 11 and 12 write.
