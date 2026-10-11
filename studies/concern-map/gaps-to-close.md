# Gaps to close (Q1)

Each platform's re-pass records a gap wherever the platform's own sources, as held, state nothing for a concern and placement. This page lists the gaps someone can close and how. It is generated from each platform's `gaps.tsv` by `method/q1_gaps_report.py`.

Gap kinds:

- **observation needed**: a journey, a store on a plan, a page saved from a browser, or a question to the platform would show it.
- **page not read**: a named page would likely state it, and an agent can read it.
- **stated only in general terms**: the platform's terms speak only of its services in general. The clause is cited in the gap. Applying it to one concern would be inference, so it is not a statement.
- **searched, not found**: the likely pages and structures were read, and none states it. Stated reasons are the most common case, because platforms rarely say why.

## Shopify

249 gaps: 15 observation needed, 52 stated only in general terms, 182 searched, not found. Who can close them: 234 an agent, 8 either, 7 the founder.

### Ask the platform (founder, 5)

| Concern | Placement | What would show it | Route |
| --- | --- | --- | --- |
| SH-C-089 Shopify Balance cards | how it meets the rest | The card program terms and the interface between Shopify, Stripe and the issuing bank for Balance cards | admin Banking > Shopify Balance terms (route shopify-balance:terms:detail, path terms/:kind) on a US store that has onboarded to Balance |
| SH-C-093 Shopify Capital in Canada | who is legally responsible | The lender or provider and the agreement for Shopify Capital in Canada | Shopify Capital terms shown in the admin (route capital:account:terms, 'Capital Application') on an eligible store registered in Canada, or Shopify Support |
| SH-C-094 Shopify Capital in Australia | who is legally responsible | The lender or provider and the agreement for Shopify Capital in Australia | Shopify Capital terms shown in the admin (route capital:account:terms) on an eligible store registered in Australia, or Shopify Support |
| SH-C-174 Sanctions and unsupported countries and regions | how it meets the rest | The screening interface or contract term through which sanctions checks meet the rest of the platform | Shopify Support, or the Shopify Payments onboarding flow on a store in a supported country |
| SH-C-201 Shopify Plus contract terms and renewals | stated reason | A Shopify statement of why Plus is sold under its own contract and term (for example the 3-year term) | Shopify Plus sales, or the Plus terms page in a paid Plus store's admin |

### Open a store on a plan (founder, 2)

| Concern | Placement | What would show it | Route |
| --- | --- | --- | --- |
| SH-C-201 Shopify Plus contract terms and renewals | who is legally responsible | The Shopify Plus agreement: the parties and the clauses on renewal and term | a paid Shopify Plus store: admin Settings > Plan, the 'Shopify Plus Terms' route (settings:plan:plus:terms, path plus/terms) |
| SH-C-201 Shopify Plus contract terms and renewals | how it meets the rest | The contract or setting through which a Plus store's term and renewals are agreed (the Plus terms, the 3-year renewal flow) | a paid Shopify Plus store: admin routes settings:plan:shop_plus_self_renewals (Switch to 3-year term) and settings:plan:shop_plus_self_renewals:review |

### Record a journey (either, 8)

| Concern | Placement | What would show it | Route |
| --- | --- | --- | --- |
| SH-C-035 Storefront search and filtering | who decides | The settings or plan lines that turn storefront search and filters on or limit them (the Search & Discovery app's settings) | the Search & Discovery app by Shopify (apps.shopify.com/search-and-discovery) installed on a held store, its settings pages (store owner role) |
| SH-C-036 Hosting and SSL | where it lives | Where the platform shows hosting and the SSL certificate of the store's domains | admin Settings > Domains on a held store with a connected domain (store owner role) |
| SH-C-038 Combined listings | where it lives | Where Shopify places combined listings (the Shopify Combined Listings app and the admin pages it adds) | store capture-plus (Shopify Plus App Development, development store), or a paid Shopify Plus store: install the Shopify Combined Listings app and record its pages (store owner role) |
| SH-C-087 Cash management at POS | where it lives | Where cash tracking lives: the POS app screens and the admin pages for cash drawer sessions | the Shopify POS app on a held store with a POS location (staff role with POS access), and the admin's POS pages |
| SH-C-087 Cash management at POS | who decides | The POS setting or staff permission that turns cash tracking on (cash drawer counts and adjustments) | Shopify POS app > Settings on a held store with a POS location (staff role with POS access) |
| SH-C-170 Partner and expert services hired by merchants | who decides | What the plan subscription pages state about booking a Shopify expert or bringing your own partner (who offers it, on which plans) | admin routes subscribe:book-shopify-expert-intro-call and subscribe:bring-your-own-partner (plan subscription pages) on a trial store, store owner role |
| SH-C-174 Sanctions and unsupported countries and regions | where it lives | Where the platform applies the restriction: sign-up, storefront access, Shopify Payments onboarding, checkout | sign-up at accounts.shopify.com/signup (the 'I'm located in:' list) and storefront and admin access from an unsupported region |
| SH-C-202 Shopify Magic for product descriptions and blog posts | how it meets the rest | The API, intent or extension through which Shopify Magic generates text in the product and blog editors | admin products/new and articles/new on any held store (store owner role), recording the operations the editor calls when 'Generate' is used |

## WooCommerce

182 gaps: 4 observation needed, 9 page not read, 63 stated only in general terms, 106 searched, not found. Who can close them: 0 an agent, 103 either, 79 the founder.

### Read a page (founder, 9)

| Concern | Placement | What would show it | Route |
| --- | --- | --- | --- |
| WC-C-008 WooPayments reserves (funds withheld for risk) | who is legally responsible | A source that states who is legally responsible for WooPayments reserves (funds withheld for risk). | Stripe's Connected Account Agreement (stripe.com/connect-account/legal), which the merchant accepts at WooPayments signup (WC-S-0507) |
| WC-C-009 WooPayments know-your-customer verification | who is legally responsible | A source that states who is legally responsible for WooPayments know-your-customer verification. | Stripe's Connected Account Agreement (stripe.com/connect-account/legal), which the merchant accepts at WooPayments signup (WC-S-0507) |
| WC-C-010 WooPayments availability by country | who is legally responsible | A source that states who is legally responsible for WooPayments availability by country. | Stripe's Connected Account Agreement (stripe.com/connect-account/legal), which the merchant accepts at WooPayments signup (WC-S-0507) |
| WC-C-020 Licence under which WooPayments funds are held and moved | where it lives | A source that states where Licence under which WooPayments funds are held and moved sits (product, host, page or code path). | Stripe's Connected Account Agreement (stripe.com/connect-account/legal), which the merchant accepts at WooPayments signup (WC-S-0507) |
| WC-C-020 Licence under which WooPayments funds are held and moved | who decides | A source that states what turns Licence under which WooPayments funds are held and moved on or off, limits it, or sets its value. | Stripe's Connected Account Agreement (stripe.com/connect-account/legal), which the merchant accepts at WooPayments signup (WC-S-0507) |
| WC-C-020 Licence under which WooPayments funds are held and moved | how it meets the rest | A source that names the API, event, setting or contract at the boundary of Licence under which WooPayments funds are held and moved. | Stripe's Connected Account Agreement (stripe.com/connect-account/legal), which the merchant accepts at WooPayments signup (WC-S-0507) |
| WC-C-020 Licence under which WooPayments funds are held and moved | stated reason | A source that states why Licence under which WooPayments funds are held and moved is placed as it is. | Stripe's Connected Account Agreement (stripe.com/connect-account/legal), which the merchant accepts at WooPayments signup (WC-S-0507) |
| WC-C-051 WooPayments payout currency and currency conversion | who is legally responsible | A source that states who is legally responsible for WooPayments payout currency and currency conversion. | Stripe's Connected Account Agreement (stripe.com/connect-account/legal), which the merchant accepts at WooPayments signup (WC-S-0507) |
| WC-C-115 Stripe Radar screening on WooPayments accounts | who is legally responsible | A source that states who is legally responsible for Stripe Radar screening on WooPayments accounts. | Stripe's Connected Account Agreement (stripe.com/connect-account/legal), which the merchant accepts at WooPayments signup (WC-S-0507); Stripe's Radar terms |

### Record a journey (founder, 4)

| Concern | Placement | What would show it | Route |
| --- | --- | --- | --- |
| WC-C-010 WooPayments availability by country | where it lives | A source that states where WooPayments availability by country sits (product, host, page or code path). | WooPayments onboarding on a test store: WP Admin > Payments > set up WooPayments (country and account type steps) |
| WC-C-010 WooPayments availability by country | how it meets the rest | A source that names the API, event, setting or contract at the boundary of WooPayments availability by country. | WooPayments onboarding on a test store: WP Admin > Payments > set up WooPayments; the release's WooPayments onboarding REST routes (src/Internal/Admin/Settings/PaymentsProviders/WooPayments/WooPaymentsRestController.php) are the store side |
| WC-C-051 WooPayments payout currency and currency conversion | where it lives | A source that states where WooPayments payout currency and currency conversion sits (product, host, page or code path). | A store with WooPayments: Payments > Settings (payout and currency sections) and the Stripe Express dashboard |
| WC-C-115 Stripe Radar screening on WooPayments accounts | how it meets the rest | A source that names the API, event, setting or contract at the boundary of Stripe Radar screening on WooPayments accounts. | A store with WooPayments: Payments > Settings > Fraud protection, and a test transaction blocked by Radar |

