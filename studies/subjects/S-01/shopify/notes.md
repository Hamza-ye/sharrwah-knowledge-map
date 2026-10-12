# S-01 phase A, shopify (SH): notes

Run of 2026-10-12. Brief: studies/subjects/S-01/briefs/A-one-platform.md. Result: 143 statements, 345 citations, 35 terms, 2 absences, no gaps. Bullets a, b, c, d and e and both ends (end-payment, end-payout) are stated.

## What I read

Inputs and tools
- The brief; the Q1 index files concerns.tsv, statements.tsv, gaps.tsv and citations.tsv in studies/concern-map/platforms/shopify/ (searched by concern and by wording; the concerns used are SH-C-062 to SH-C-081, SH-C-088, SH-C-110, SH-C-173 and SH-C-174).
- The tools the brief names (method/held_index.py, method/warc_text.py, method/capture/page_text.mjs) and the checker the coordinator named (method/check_subject.py, with method/quote_check.py and method/source_kinds.py, which it imports), for their usage and the file format.

Shopify's terms and lists (live, 2026-10-12, rendered through method/capture/page_text.mjs)
- https://www.shopify.com/legal/terms-shopify-payments, the whole page (undated). The country addresses such as https://www.shopify.com/legal/terms-payments/us, /de, /ae and /legal/terms-payments-at redirect to it (301).
- https://www.shopify.com/legal/processor-list, the whole page (undated); its raw HTML only to list the agreements each row links.
- https://www.shopify.com/legal/terms-payfac, the whole page (Last modified: September 22, 2026); its raw HTML only for the link behind Pass-Through Terms (https://www.adyen.com/legal/adyen-for-platforms-terms-and-conditions).
- https://www.shopify.com/legal/terms (Last updated on: August 1, 2026): sections 2, 2.3 and 9.9 read for this subject.

Help Center (live, 2026-10-12, .md endpoints of help.shopify.com/en/manual/)
- Read whole: payments/getting-paid; payments/third-party-providers/payment-gateway-availability (for the index excerpt on the banking partner); payments/shopify-payments; payments/shopify-payments/payouts; payouts/payout-timing; payouts/reserves; payouts/account-holds; payouts/schedule-payouts; payouts/view-details; payouts/pay-periods-and-fees; payouts/refunds; payouts/lower-or-missing-payouts; shopify-payments/supported-countries; onboarding/eligibility; onboarding/acceptable-business-practices; payments/chargebacks; payments/third-party-providers; international/managed-markets/overview; finance/shopify-balance/eligibility; finance/shopify-balance/payouts/payout-accounts.
- Searched for wording on holding, holds, reserves, balances, settlement and payouts, without taking statements unless named in statements.tsv: payouts/failed-payouts; store-currency/payouts-in-multiple-currencies; payments/payment-authorization; payments/shop-pay-installments; finance/shopify-balance; payments/paypal; payments/manual-payments; shopify-payments/using-shopify-payments-with-a-third-party-provider; shopify-payments/transactions; international/managed-markets/shopify-payments; onboarding/bank-account-requirements (one statement taken).
- The .md endpoints payouts/payout-statuses and payouts/viewing-payouts answered 404.

Held in observed-sh
- structures/shopify/admin-graphql-schema/2026-10/items.jsonl (the ShopifyPayments types and enums) and structures/shopify/admin-router/items.jsonl (the payouts route), cited at e4984072995bf730a98292a1903de1a49390229a; git shows no change to either file between that commit and 36a6319e2670276d839f353551a140109a3564b1. structures/shopify/admin-webhook-topics names no topic containing 'payout'.
- Archive raw/runs/20260930T020155Z-help-ar-html/fetch.warc.gz at 36a6319e2670276d839f353551a140109a3564b1, read with method/warc_text.py, for Shopify's own Arabic wording of the terms: help.shopify.com/ar/manual/payments/shopify-payments/payouts (offset 22155021), payouts/payout-timing (22248554), payouts/reserves (22323323), payments/getting-paid (20822537) and payments/shopify-payments (21562192, no term taken). The Arabic pages render "payouts" as عمليات الدفع (payouts page, reserves page), عوائد (payout timing page) and دفعات (payout schedule sentence); terms.tsv quotes each with its page.

Agreements the Shopify Payments Terms of Service incorporate (live, 2026-10-12)
- Payment Processor Terms linked from the United States row for Stripe, Inc.: https://stripe.com/legal/connect-account (whole page, Last modified: November 18, 2025); https://stripe.com/legal/ssa (General Terms, Last modified: September 28, 2026: sections 7 and 10 read, the definitions searched); https://stripe.com/legal/payment-terms (a list of per-method terms; nothing taken).
- https://www.adyen.com/legal/adyen-for-platforms-terms-and-conditions (Effective from: October 2025): definitions and sections 2.6 to 2.10 read. The Payment Processor List names it for Adyen N.V., and the Payment Facilitator Terms link it as the Acquirer's Pass-Through Terms.
- Service Terms - Shopify Managed Markets for the United States, linked from Part II, D of the Shopify Payments Terms: https://s3.global-e.com/policies/shopify/ww-merchant-terms-v3.html (raw HTML, Effective as of: January 26, 2026): sections 1 and 4 read.

How statements were made
- Statements copied from the Q1 index keep the index citation (source, locator, quote and dates) unchanged. Where the index excerpt stopped before the part that bears on the subject, I read the source again on 2026-10-12, kept the copied citation first, extended the statement to the rest of its sentence or paragraph and cited the rest separately; the statement's note says so. Every copied quote was also found in my 2026-10-12 working copy of its page.
- During the run the coordinator announced that observed-sh's 70 fetch archives are in git at 36a6319e2670276d839f353551a140109a3564b1. Citations written before that stay as written (live addresses, or observed-sh at e4984072995bf730a98292a1903de1a49390229a); the Arabic quotes taken after it cite the archive at 36a6319e2670276d839f353551a140109a3564b1 with the record's offset as the locator.

## What I could not read

Not read, for time and the 150-statement limit (the Shopify Payments Terms, the Payment Processor List, the Payment Facilitator Terms and the Help Center payout pages came first, then one set of Payment Processor Terms each for Stripe and Adyen):
- The Stripe Connected Account Agreement and Stripe Services Agreement versions linked from the rows of Designated Countries other than the United States.
- PayPal's Account Terms linked from the processor rows: PayPal User Agreement (United States, EMEA rows), PayPal Platform Seller Agreement (France row); the PayPal and Stripe debit authorizations.
- Bridge Terms (row A. Global) and the Antom Merchant Services Agreement (row China (Mainland)).
- Coinbase Payments Protocol Terms of Service; Shop Pay Installments Terms and the Merchant Agreement (Shop Pay Installments) with Affirm; Service Terms - Shopify Managed Markets for Canada and the United Kingdom (content.global-e.com/merchant-terms-ca and merchant-terms-uk).
- The 40 Help Center pages "Shopify Payments for <country>" (bank account and payout details per country).
- Help pages answering 404 as .md endpoints: payouts/payout-statuses, payouts/viewing-payouts.

## Problems with the method

- The checker looks for a statement verbatim in its first citation's source, so a list under (e) can be one statement only where the list runs unbroken in the source. The supported countries list does (S01-SH-096). The Payment Processor List does not: one table interleaves countries, processors and agreement names. I recorded it as one statement per table for A. Global, B. North America and D. Asia-Pacific, and one statement per Payment Processor for C. EMEA, whose scope names every row that names it, each row cited.
- Quotes from .md endpoints are written with link markup removed and list markers ("* ", "- ") kept, as the checker's "markup removed" form keeps them. Where an inline HTML tag ends just before punctuation, that form leaves a space before it (for example "process the payout , and" in S01-SH-077), and the quote carries the space.
- Absence S01-SH-N02 takes its list from the Payment Facilitator Terms and its words of completeness from another document, the Shopify Payments Terms of Service (Part I, A: "The Designated Countries where a Shopify affiliate acts as a Payment Facilitator are listed in the Payment Facilitator Terms.").
- Index citations for live pages keep their index dates (2026-10-10 or 2026-10-11) although I read the pages again on 2026-10-12.
- Housekeeping: before seeing that other agents use it, I wrote four helper scripts (add.py, idx.py, grep_idx.py, show_concern.py) into the shared scratchpad folder tools/ and then moved them to sh-s01/tools/. A file of the same name already there would have been overwritten.
