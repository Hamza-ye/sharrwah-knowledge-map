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
