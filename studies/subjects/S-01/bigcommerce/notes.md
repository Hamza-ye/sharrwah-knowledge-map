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

# Phase A2: closing gaps on the variation points

Read on 2026-10-13, following `studies/subjects/S-01/briefs/A2-close-gaps.md`. Statements S01-BC-039 to S01-BC-061, citations S01-BC-C047 to S01-BC-C079, gaps S01-BC-G04 to S01-BC-G23 and `a2.tsv` are from this phase. No absence was recorded.

## What I read

- **Commerce press releases** (rendered): "Commerce Introduces BigCommerce Payments Powered by PayPal" (October 20, 2025), "Commerce Delivers BigCommerce Payments by PayPal…" (May 6, 2026) and the Commerce Live 2026 release.
- **bigcommerce.com blog posts** (rendered; dates from each page's datePublished): the BigCommerce Payments announcement, UK expansion, playbook and closed beta posts; the Stripe Adaptive Pricing, Stripe OCS upgrade and Stripe on BigCommerce posts; the PayPal payment gateway and PayPal funding posts.
- **bigcommerce.com pages** (raw HTML): BigCommerce Payments on .com, .co.uk and .com.au, its trial and treatment pages, `/payments/`, `/payments/embedded-payment-providers/`, `/payments/paypal/`, `/partners/stripe/payments/`, `/partners/stripe/`, `/affirm/`, `/square-offer/`, `/product/consumer-financing/`, `/solutions/cryptocurrency-payments/`, `/payments/recurring/`, and the 32 country pages under `/payments/gateways/`.
- **Legal pages** (rendered), searched again for agency, reserves, withholding, set-off, security interests, payouts and funds: the Master Services Agreement, Store Terms, Fees and Billing, Jurisdiction-Specific Terms, Acceptable Use Policy.
- **Developer docs:** the 348 `.md` pages of `docs.bigcommerce.com/developer/llms.txt` whose addresses name payments, orders, refunds, checkout, currencies, PayPal, Stripe, wallets, transactions, captures, voids or B2B invoices, searched for payout, settle, funds, disburse, reserve, withhold and "on hold"; the matching passages were read.
- **Indexes,** used only to find pages: `www.bigcommerce.com/robots.txt` and the blog, press, articles and glossary sitemaps; `www.commerce.com/sitemap.xml`.

## What I couldn't read

- **The Help Center** still renders no text (0 characters) for `Connecting-with-BigCommerce-Payments`, `Available-Payment-Gateways` and `Offline-Payment-Methods`, and `support.bigcommerce.com/llms.txt` still redirects to a login page. The BigCommerce Payments announcement and UK posts link `Connecting-with-BigCommerce-Payments` as the knowledge-base article; it is in the routes of G04 to G23. `method/held_index.py` reports none of the routes' addresses as held.
- **The control panel** (Money Dashboard, BigCommerce Payments activation) needs a store login and was not opened.

## Problems

- **Press releases and blog posts as sources.** The statements about the BigCommerce Payments account, the merchant's relationship with PayPal and the Money dashboard come from Commerce press releases and bigcommerce.com blog posts, not from a product or legal page. S01-BC-039 to S01-BC-041 come from the October 2025 release, written before launch in the future tense.
- **Plan and region differ between sources.** The May 2026 release says "Retail plans in the United States" (S01-BC-046); the March 2026 announcement says "US customers on Core, Growth, and Scale plans" (S01-BC-054); the UK post says "UK and EMEA customers on Core, Growth, and Scale plans" (S01-BC-057); the closed beta post says "Standard, Plus, or Pro plan" (S01-BC-060). All are recorded.
- **Conditions added to phase A rows.** As the A2 brief allows, I added new stmt_ids to the `conditions` of S01-BC-028, S01-BC-029 and S01-BC-030 (replacing `none stated`) and of S01-BC-034.
- **A footnote checked and not used.** On the PayPal page, footnote 11 ("Availability may vary depending on merchant’s integration method and geographic location.") sits on "Local payment methods used around the world", not on "Funds credit immediately…", in the raw HTML, so it is not recorded as conditioning S01-BC-023.
- **Shared scratchpad.** Other agents write to the same scratchpad directory; a helper script of mine was overwritten once by another agent's file of the same name before it ran. Nothing was written to this folder by it; my work then moved to its own subfolder.

# Absence audit

Phase A3, read on 2026-10-13, following `studies/subjects/S-01/briefs/A3-absence-audit.md`. Statements S01-BC-062 to S01-BC-065, citations S01-BC-C080 to S01-BC-C084, two terms and `absence-audit.tsv` are from this phase.

## What I found

- **Claims audited:** eleven gaps, every gap not of kind `page not read`: G02, G08, G09, G10, G12, G14, G15, G19, G20, G22 and G23. `absences.tsv` has no rows.
- **Contradicted: G02 and G15.** They rest on one held page, the pricing page (`https://www.bigcommerce.com/pricing/`, captured 2026-10-12, which is in G02's own `read`). Its footnote "To qualify for the PayPal Braintree rate" names:
  - a "PayPal Braintree account", trial and then full;
  - a "Pricing Contract" the merchant is emailed to sign after approval.

  These are recorded as S01-BC-062 (b). The page's conditions are recorded as S01-BC-063 ("Eligibility requires that you must be a United States-based business.") and S01-BC-064 ("Application for a PayPal Braintree account does not guarantee approval."), both (e) and conditioning S01-BC-062. The page names no licence. It does not say where funds are held.
- **Confirmed:** G08, G09, G10, G12, G14, G19, G20, G22 and G23. No held document speaks of:
  - an agent collecting or holding the shopper's payment;
  - a reserve, withholding, hold or suspension of funds or payouts;
  - a lien, security interest or set-off;
  - a licence to hold or transmit funds;
  - what happens to funds on termination;
  - refunds to shoppers when a store closes.
- **Also recorded, as the brief now asks.** S01-BC-065 (end-payout): the BigCommerce Payments page's step "2 Configure", "Add your bank account and set payment preferences."
- **Read and not recorded.** The UK post's "For full details, see PayPal Merchant Fees." refers BigCommerce Payments' rates to a PayPal fee schedule. It names no terms for holding funds.
- **Sources.** Every new citation is to a held capture in this repository at commit `7611d459e3e09c1503a27d4f02f57850e82e9ffb` (`access_path` `local`). I did not fetch any live page.
- **The routes:**
  - The Help Center articles are held, but `text.txt` is empty and `raw.html` is the application shell ("Loading", "Sorry to interrupt", "CSS Error").
  - `http://login.bigcommerce.com/deep-links/manage/balance` is not held and was not opened.

## Searches too large to read in full

- `corpus_search.py` matches substrings, and its bigcommerce host pattern `commerce\.com$` also takes in woocommerce.com captures. "terms of service" (122 documents), "refund" (144), "lien" (135, from "client"), "Enterprise" (147), the plan names (88) and "hold" (54) were mostly woocommerce.com pages or matches inside other words. I set the woocommerce.com documents aside as not BigCommerce's.
- For the remaining 178 held records of the bigcommerce hosts, I read:
  - each listed snippet;
  - every passage matching the claim words (reserve, withhold, hold, held, suspend, pause, freeze, delay, agent, behalf, lien, security interest, set-off, licence, regulated, money transmitter, terms, agreement, contract, termination, refund, payout, settle, funds, disburse, deduct, chargeback).
- I read the payment, marketing, blog and press pages in full, and the legal pages' payment, agency, suspension and termination passages. I read the developer docs (121 pages) only by these passages.

## Problems with the method

- **The host pattern.** `method/corpus_search.py`'s pattern for bigcommerce (`bigcommerce\.com$|commerce\.com$|bitpay\.com$`) matches woocommerce.com, so bigcommerce searches list WooCommerce documents.
- **Substring matching.** Terms match inside words: "lien" in "client", "reserve" in "preserved", "hold" in "holdings". Short terms list many documents that do not use the word.
- **G02 and G15 overlap with G13,** a `page not read` gap outside this audit, on the account for providers other than BigCommerce Payments, PayPal and Stripe. S01-BC-062 bears on G13 too. G13 is left unchanged.
- **Accounts versus funds.** G02 was written in phase A, before A2 recorded S01-BC-051 and S01-BC-055, which name the BigCommerce Payments account. I count a provider account the merchant holds as (b), as A2 did for S01-BC-061 ("Connect or create your Stripe account"). The pricing page names the account and contract only in the steps to a processing rate.
- **The brief changed while I worked.** It added the instruction to record anything else on the subject in the documents read. I applied it from then on. It produced S01-BC-065.
- **The checker writes outside this folder.** It writes `studies/subjects/S-01/kinds.tsv`, as noted in phase A.

# Phase A2 re-run: the founder's Help Center capture

Read on 2026-10-17, following `studies/subjects/S-01/briefs/A2-close-gaps.md` and the coordinator's message. The new evidence is the run `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/` (commit `7f7fdb3999568148dd5edb59912d3c47b3cd1b69`), captured from the founder's machine on 2026-10-13. Statements S01-BC-066 to S01-BC-124, citations S01-BC-C085 to S01-BC-C215, 18 terms, gaps S01-BC-G24 to S01-BC-G40 and the updated `a2.tsv` are from this re-run. No absence was recorded, and no phase A, A2 or A3 row was changed.

## What I read

- **In full, from each item's `text.txt`** (after the Help Center's menus):
  - item 1, Connecting with BigCommerce Payments;
  - item 2, Available Payment Gateways;
  - item 3, Connecting with PayPal;
  - item 4, Connecting with Stripe OCS;
  - item 5, Connecting with Braintree;
  - item 6, Offline Payment Methods;
  - item 7, Processing Refunds;
  - item 8, Manually Capturing Transactions (Authorize Only);
  - item 9, the Help Center's front page.
- **By the passages the searches matched,** in the same run: items 14, 15, 16, 19, 21, 25, 26, 28, 30, 32, 33, 36, 37, 38, 40 (About BigCommerce Pricing: its Open Payment Provider fee section, recorded as S01-BC-123 and S01-BC-124), 41, 43, 46, 48 and 49.
- **Searches:** `python3 -I method/corpus_search.py bigcommerce <term>` for each gap's words and for each arrangement, country and plan the statements name. Each gap's `read` lists its commands.
- Every citation is to a held capture (`access_path` `local`). The articles show no date, so `source_date` is the capture date, 2026-10-13. I fetched no live page.

## Gaps settled

- **Closed by the articles:** G01, G04, G06, G07, G11 (in part), G13, and the parts of G02, G03, G05, G16, G17, G20 and G21 that the articles state. `a2.tsv` no longer lists any of G01 to G23.
  - **(a) who holds the funds:**
    - For BigCommerce Payments, the article names "a brand new PayPal platform account dedicated to your BigCommerce store", which "will handle all settlement" (S01-BC-068 to S01-BC-070).
    - For the standalone PayPal gateway, "Funds are deposited immediately into your PayPal account" (S01-BC-090).
    - For any gateway: "You will control and direct funds in your merchant account with your merchant service provider" (S01-BC-088).
  - **Offline methods:** the merchant's own bank account, address or store (S01-BC-115 to S01-BC-119).
- **Remaining, `searched, not found`:** G24 to G31 and G35 to G40, one per variation point.
- **Remaining, `page not read`:** G32 (a), G33 (b) and G34 (c), for the Embedded and Open Payment Providers other than BigCommerce Payments, PayPal, Stripe OCS and Braintree. Their Help Center articles are not held.

## What changes an answer already given

- **S01-BC-023,** "Funds credit immediately into your PayPal business account", is from the PayPal product page.
  - The Help Center says the same of the standalone PayPal gateway (S01-BC-090).
  - Under BigCommerce Payments, the funds sit in a separate PayPal platform account, the "BigCommerce Payments balance". Automatic payouts go from there to the PayPal account or a bank (S01-BC-073).
  - "For new BigCommerce Payments accounts, initial payments are held for up to 21 days before being available for payout" (S01-BC-082).
- **Where BigCommerce Payments is offered.**
  - The Help Center says United Kingdom and United States stores, on Core, Growth or Scale plans, with select Performance plan stores (S01-BC-067, S01-BC-086).
  - This agrees with S01-BC-029 (.co.uk), not with S01-BC-028 ("only to US-based merchants").
- **The dashboard's name.** The Help Center calls it the "Balance dashboard" (Finance › BigCommerce Payments). Earlier sources call it the "Money Dashboard" or "Money dashboard" (S01-BC-018, S01-BC-040, S01-BC-052).

## Read and not recorded

- **Transaction rates.** Item 1 gives BigCommerce Payments' US and UK rates. It does not say the rates are deducted from the funds. G28 and G38 note this.
- **Lists.** Not recorded:
  - the gateway tables in item 2;
  - the currency lists in items 1, 4 and 5;
  - the APM tables in item 32.

  They name payment methods and currencies, not who holds funds or on what conditions.
- **Repeats.** "Why did my refund fail?" (item 1) repeats S01-BC-075 and S01-BC-087.
- **Items 25 and 26** (stored payment methods, Fastlane) name gateways and accounts, and nothing about funds.

## Problems

- **Old gaps left in place.** The brief forbids changing existing rows, so G01 to G23 stay in `gaps.tsv` with their founder routes. The checker clears the routes through `a2.tsv`'s `read`.
- **`variants.tsv` points to settled gaps.** It still points to G02, G03 and G04 to G23, which `a2.tsv` now settles. That file is phase B's.
- **`corpus_search.py` matches whole words now.** Phase A3 noted substring matches. Partial words such as "licen" and "terminat" find nothing, so I searched with full word forms.
- **The same words in several articles.** The Pay Later sentence is in three articles, and the 21-day note three times in item 1. Each such statement quotes the first occurrence and cites the others.
- **The checker writes outside this folder.** It writes `studies/subjects/S-01/kinds.tsv` again.
