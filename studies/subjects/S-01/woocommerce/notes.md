# S-01, phase A: WooCommerce (WC), notes

Run of 12 October 2026. The run was interrupted after the five TSV files were written. It resumed to write these notes and run the checker. The lists below come from three records: the citations, the `read` column of `gaps.tsv`, and the copies of pages saved when they were read.

## What was read

### Q1 index

`studies/concern-map/platforms/woocommerce/`: `concerns.tsv`, `statements.tsv`, `gaps.tsv` and `citations.tsv`. No other file in that folder was opened.

### WooCommerce 11.2.1 release files

Read locally in `/home/user/woocommerce-release/11.2.1/woocommerce`:

- `readme.txt`
- `includes/gateways/bacs/class-wc-gateway-bacs.php`
- `includes/gateways/paypal/class-wc-gateway-paypal.php`
- `includes/gateways/paypal/includes/settings-paypal.php`
- `src/Gateways/PayPal/Request.php`
- `src/Gateways/PayPal/TransactAccountManager.php`

### Live pages

All were read on 2026-10-12. Citations copied from the Q1 index keep the index's source, locator, quote and dates, so some show `accessed` 2026-10-10 or 2026-10-11. Their pages were read again on 2026-10-12.

Terms, raw HTML:

- https://wordpress.com/tos/ ("Last Updated: October 6, 2026"). The WooPayments "Our Policies" page links its words "Terms of Service" to this URL.

WooPayments documentation, rendered through `method/capture/page_text.mjs`:

- https://woocommerce.com/document/woopayments/ (the documentation index; nothing cited)
- https://woocommerce.com/document/woopayments/account-management/
- https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/
- https://woocommerce.com/document/woopayments/account-management/access-stripe-account/ (nothing cited)
- https://woocommerce.com/document/woopayments/account-management/delete-account/ (nothing cited)
- https://woocommerce.com/document/woopayments/account-management/transfer-site-to-new-owner/ (nothing cited)
- https://woocommerce.com/document/woopayments/startup-guide/
- https://woocommerce.com/document/woopayments/managing-money/
- https://woocommerce.com/document/woopayments/payouts/
- https://woocommerce.com/document/woopayments/payouts/payout-schedule/
- https://woocommerce.com/document/woopayments/payouts/change-payout-schedule/
- https://woocommerce.com/document/woopayments/payouts/change-payout-account-info/ (nothing cited)
- https://woocommerce.com/document/woopayments/payouts/deposits-and-payouts/
- https://woocommerce.com/document/woopayments/payouts/instant-payouts/
- https://woocommerce.com/document/woopayments/payouts/scheduled-payout-vs-instant-payout/ (nothing cited)
- https://woocommerce.com/document/woopayments/payouts/payout-currencies/
- https://woocommerce.com/document/woopayments/payouts/why-payouts-suspended/
- https://woocommerce.com/document/woopayments/fees/ (nothing cited)
- https://woocommerce.com/document/woopayments/fees/why-was-i-debited/ (nothing cited)
- https://woocommerce.com/document/woopayments/fees/account-showing-negative-balance/
- https://woocommerce.com/document/woopayments/our-policies/
- https://woocommerce.com/document/woopayments/our-policies/reserves/
- https://woocommerce.com/document/woopayments/our-policies/know-your-customer/ (nothing cited)
- https://woocommerce.com/document/woopayments/fraud-and-disputes/managing-disputes/
- https://woocommerce.com/document/woopayments/payment-methods/buy-now-pay-later/
- https://woocommerce.com/document/woopayments/payment-methods/local-payment-methods/ (nothing cited)
- https://woocommerce.com/document/woopayments/compatibility/countries/
- https://woocommerce.com/document/woopayments/compatibility/woopayments-vs-stripe-plugin-comparison/ (nothing cited)
- https://woocommerce.com/document/woopayments/stripe-capital/overview/
- https://woocommerce.com/document/woopayments/in-person-payments/

Other WooCommerce documentation, rendered:

- https://woocommerce.com/document/bacs/
- https://woocommerce.com/document/cheque/
- https://woocommerce.com/document/cash-on-delivery/
- https://woocommerce.com/document/paypal-standard/
- https://woocommerce.com/document/woocommerce-paypal-payments/ (nothing cited)
- https://woocommerce.com/document/stripe/
- https://woocommerce.com/document/woocommerce-square/ (nothing cited)

Other woocommerce.com pages, rendered:

- https://woocommerce.com/payments/ (nothing cited)
- https://woocommerce.com/woo-vendor-agreement/ (Marketplace Vendor Agreement)

WooCommerce repository, raw Markdown:

- https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/features/payments/payment-gateway-api.md

Stripe agreements, rendered (see problem 2):

- https://stripe.com/legal/connect-account (Stripe Connected Account Agreement, "Last modified: November 18, 2025")
- https://stripe.com/legal/ssa (Stripe Services Agreement, General Terms, "Last modified: September 28, 2026")
- https://stripe.com/legal/ssa-service-terms (Service Terms: the Stripe Financial Services Terms and the Stripe Payments Terms, General and Regional Terms)

## What wasn't read, or couldn't be

- No read is recorded as failed. Every rendered page was saved with HTTP status 200. The raw Terms and the Markdown document were saved with their text. No login, paywall or bot challenge is recorded.
- These pages are named in a gap's route and were not read:
  - G01: https://stripe.com/au/legal/ssa, https://stripe.com/jp/legal/ssa, https://stripe.com/nz/legal/ssa, https://stripe.com/en-sg/legal/ssa, https://stripe.com/ae/legal/ssa and https://stripe.com/au/fsg-pds.
  - G02: PayPal's user agreement and Square's terms.

## Problems with the method

1. **The interruption.** These notes were written after the run resumed. The lists above are rebuilt from the output files and the page copies saved during the run. A page opened before the interruption that was neither cited nor saved is missing from them. Only the release files that are cited are listed.

2. **Which agreements count as incorporated.** The brief admits an agreement that the platform's terms "name as binding on the merchant".
   - The Terms (8.j) say that using WooPayments means agreeing to comply with the terms and conditions of the third parties it uses, including payment processing third parties (S01-WC-016, S01-WC-017). They also say "WooPayments is powered by Stripe" (S01-WC-002). They name no agreement by title.
   - The WooPayments documentation names the Stripe Connected Account Agreement as containing "the terms you agreed to during the WooPayments signup process" (S01-WC-020).
   - That agreement incorporates the Stripe Services Agreement "by this reference" (S01-WC-103). The Services Agreement's Service Terms page holds the Stripe Financial Services Terms and the Stripe Payments Terms, which "supplement the General Terms" (S01-WC-108, S01-WC-119).
   - S01-WC-102 to S01-WC-129 were recorded on that chain.
   - For PayPal and Square, the Terms say only that a third party's terms "may apply" (S01-WC-003). Their agreements were not read, and G02 records bullet (c) for those methods as stated only in general terms.

3. **A bullet stated for one arrangement but not another.** Rule 9 asks for a gap for each bullet the platform doesn't state. Bullets (b) and (c) are stated for WooPayments, but not for every arrangement:
   - (b): the licence or regulatory status under which Stripe holds WooPayments funds is not stated for accounts in Australia, Japan, New Zealand, Singapore and the United Arab Emirates (G01).
   - (c): it is not stated for PayPal Standard or for third-party payment extensions (G02).

   Each of these is recorded as a gap. The brief has no rule for this case.

4. **Two lists of WooPayments countries.** `readme.txt` in the 11.2.1 release names 10 countries (S01-WC-088). The Supported countries list in the documentation names 38 (S01-WC-082). Both are recorded, and the absence N01 is drawn from the documentation's list. The words cited as making that list complete (S01-WC-C088) come from its Other countries section, which says the WooCommerce team "is actively working to make WooPayments available to other countries". No sentence on the page says in so many words that the list is the full set.

5. **Apostrophes in a copied quote.** S01-WC-C055 was copied unchanged from index citation WC-S-5289, as rule 5 requires. Its quote has a straight apostrophe ("there's") where the page read on 2026-10-12 has a curly one ("there’s"). The brief says only that the checker collapses whitespace, removes tags and decodes entities. A test on a scratch copy of this folder showed that the checker also treats the two apostrophes as the same, so the quote was left as copied. Every other live quote was found in the page copies saved when they were read. So was every statement whose first citation is live.

6. **Which merchant.** The brief doesn't say which merchant it means. In the Marketplace Vendor Agreement (S01-WC-078 to S01-WC-080), the merchant is the Partner, "the third party offering Products on the Marketplaces" (S01-WC-079). It is recorded because its section 2.2 names both ends for that Partner (S01-WC-078). Its statements carry the scope "Products listed on the Woo Marketplace" or "Partner Products on the Marketplaces".

7. **The live host for the terms.** The brief's table gives woocommerce.com for WooCommerce's live legal pages. The Terms of Service are at https://wordpress.com/tos/. The WooPayments "Our Policies" page, the source of S01-WC-015, links its words "Terms of Service" to that URL, and the Q1 index cites the same URL.
