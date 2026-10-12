# S-01, phase A: bigcommerce (BC)

Read on 2026-10-12, following `studies/subjects/S-01/briefs/A-one-platform.md`.

## What I read

**Q1 index** (`studies/concern-map/platforms/bigcommerce/`): `concerns.tsv`, `statements.tsv`, `gaps.tsv`, `citations.tsv`. Eleven statements are copied from it (`from` = `index:…`): BC-S-0111, 0121, 0123, 0125, 0126, 0141, 0143, 0144, 0160, 0403, 0408.

**Developer docs, as `.md` endpoints:**
- payments: `/developer/docs/admin/checkout-and-cart/payments/overview.md`, `/payments/transactions-api.md`, `/developer/api-reference/rest/admin/payments.md`, `/payments/transactions.md`;
- orders: `/developer/docs/admin/checkout-and-cart/orders/overview.md`, `/orders/refunds.md`, `/developer/api-reference/rest/admin/management/order-operations/get-order-transactions.md`, `/payment-actions/capture-order-payment.md`;
- currencies: `/developer/docs/admin/store-configuration/currencies/overview.md`, `/currencies/how-currencies-work.md`;
- payment providers and checkout: `/payment-providers/stripe/integrating-stripe-adaptive-pricing.md`, `/checkout-and-cart/integrated-fastlane-by-pay-pal.md`, `/checkout-and-cart/overview.md`, `/open-checkout/pciguide.md`, `/payments/stored-instruments.md`, `/storefront/headless/pci-compliance.md`;
- courses: `/learn/courses/checkout-orders-rest-api/management-api/payments.md`, `/transactions-api/transactions-api.md`, `/transactions-api/refunds.md`, `/learn/courses/b2b-graphql/orders-invoices/payments.md`, `/b2b-graphql/company/credit-payment.md`, `/learn/courses/b2b-core/purchasing/rest-orders-payments.md`.

**bigcommerce.com pages,** as raw HTML. Every page cited was also rendered through `method/capture/page_text.mjs`.
- BigCommerce Payments: `/payments/bigcommerce-payments/` (also on bigcommerce.co.uk and bigcommerce.com.au), `/payments/bigcommerce-payments-treatment/` and `/bigcommerce-payments-trial/`;
- payments and providers: `/payments/`, `/payments/embedded-payment-providers/`, `/payments/gateways/` and `/payments/gateways/united-states/`, `/payments/paypal/` (also on bigcommerce.co.uk and bigcommerce.com.au), `/partners/stripe/payments/`;
- products and pricing: `/pricing/`, `/product/`, `/product/checkout/`, `/product/consumer-financing/`, `/product/stored-credit-cards/`, `/product/pos/`, `/product/mobile-wallets/`, `/product/agentic-commerce/`, `/product/paypal-agentic-commerce-beta/`;
- solutions: `/solutions/cryptocurrency-payments/`, `/payments/recurring/`.

**Legal pages,** rendered. The legal pages sit at commerce.com:
- the Master Services Agreement (`https://www.commerce.com/terms/`, Date of Last Revision June 1, 2026);
- every Incorporated Term it links: Store Terms, Fees and Billing, Jurisdiction-Specific Terms, Merchant-Client Terms, Acceptable Use Policy, API Terms, AI Features Addendum, Mobile App Terms, Professional Services Program Document, Infringing Materials Protocol, the Privacy Policy, the Data Processing Addendum and the three Unified Billing terms (`/terms/merchant-unified-billing/`, `/terms/us-uk-ca-merchant-unified-billing/`, `/terms/in-merchant-unified-billing/`);
- the Legal Archives page.

**Indexes,** used only to find pages: `docs.bigcommerce.com/llms.txt`, `docs.bigcommerce.com/developer/llms.txt`, `www.bigcommerce.com/sitemap-main.xml`, and the Help Center's `/s/sitemap.xml` and `/s/sitemap-topicarticle-1.xml`.

## What I couldn't read

- **The Help Center** (support.bigcommerce.com):
  - `page_text.mjs` returned 0 characters for four articles: Available-Payment-Gateways, Connecting-with-PayPal, Connecting-with-Stripe-OCS and Manually-Capturing-Transactions-Authorize-Only.
  - The raw page is the site's application shell, with the text "Loading", "Sorry to interrupt", "CSS Error" and "Refresh".
  - `support.bigcommerce.com/llms.txt` redirects to a login page.
  - Five guessed addresses for a BigCommerce Payments article return HTTP 404: BigCommerce-Payments, BigCommerce-Payments-by-PayPal, Money-Dashboard, BigCommerce-Payments-FAQ and Getting-Started-with-BigCommerce-Payments. The topic-article sitemap lists no BigCommerce Payments article.
  - The BigCommerce Payments page sends readers to "BigCommerce documentation" for details, and that documentation was not reached.
- **The control panel:** the BigCommerce Payments page's Activate link opens `http://login.bigcommerce.com/deep-links/manage/balance`, which needs a store login. I did not open it.
- `method/held_index.py` reports none of the gap routes' addresses as held.

## Problems

- **Partly stated bullets.** The brief asks for one gap for each bullet the platform doesn't state. None of bullets (a), (b) and (c) is stated for BigCommerce Payments, and each is stated for only some providers:
  - (a) for the merchant's payment provider, BitPay, PayPal and Stripe;
  - (b) for PayPal and Stripe;
  - (c) for PayPal, Pay Later and the consumer financing integrations.

  I recorded one gap per bullet, G01 to G03, for what is not stated. The checker would accept no gap at all for these bullets.
- **Two pages differ on where BigCommerce Payments is offered.** The bigcommerce.com and bigcommerce.com.au pages say "available only to US-based merchants" (S01-BC-028). The bigcommerce.co.uk page says "US- and UK-based merchants" (S01-BC-029). Both are recorded.
- **Two pages differ on the number of countries.** The payments page says providers cover "more than 150 countries" (S01-BC-035). The checkout page says "65+ payment providers across 100+ countries" (S01-BC-036). Both are recorded.
- **Text that appears only in the raw HTML:**
  - The BigCommerce Payments page's FAQ answers are in the raw HTML. The rendered page shows the questions collapsed.
  - The payment gateways page shows one region at a time when rendered. Its raw HTML holds every region, so S01-BC-037 cites the raw page.
- **A footnote marker inside a sentence.** The PayPal page puts footnote marker 3, between invisible characters, inside its Pay Later sentence. The statement keeps it as the checker's normalization reads it: "Pay Monthly3" (S01-BC-024).
- **The Incorporated Terms list.** The Master Services Agreement's list names no payments agreement. Its own words don't present it as the full set: the Agreement also incorporates "any additional guidelines or rules applicable to such Services or features that may be posted from time to time". So no absence is recorded, and `absences.tsv` has its header only.
- **The Unified Billing terms** are left out. They speak of Commerce collecting amounts from the merchant, and distributing or remitting them, for the merchant's purchases from Unified Billing Partners. They say nothing of buyers' payments.
- **Translations.** No translation is recorded. The docs and the pages cited are in English, and I did not look at the German, French or other localized sites.
- **Quotes that span paragraphs.** A statement made of a question and its answer cites each paragraph separately. A quote stays within one paragraph, while the statement runs across both, so the checker can find it whole on the page.
- **The checker writes outside this folder.** Running `method/check_subject.py` as instructed writes `studies/subjects/S-01/kinds.tsv`. I left that file in place.
