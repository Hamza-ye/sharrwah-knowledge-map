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
