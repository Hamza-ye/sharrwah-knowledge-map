# Q2 · BigCommerce (checking run): notes

## Selection

20 concerns copied (with S-01), 2 added (BC-C-084 Third-Party Products, BC-C-030 Fees and billing), 22 set aside. The copy script reported 144 statements, 27 gaps, 128 pilot statements, 40 pilot gaps and 0 pilot absences.

## What was read (all held; accessed 2026-10-19)

Topic search (`python3 -I method/corpus_search.py bigcommerce sanctions "restricted countries" "not available in" "only available" regulated regulation regulations licence license "local requirements" --max 10`), 9 documents read:
- https://www.commerce.com/terms/ (Master Services Agreement), https://www.commerce.com/terms/acceptable-use-policy/, https://www.commerce.com/terms/jurisdiction-specific-terms/, https://www.commerce.com/terms/store-terms/
- https://support.bigcommerce.com/s/article/Tax-Overview, https://support.bigcommerce.com/s/article/Available-Payment-Gateways?language=en_US, https://support.bigcommerce.com/s/article/Collecting-Newsletter-Subscriptions
- https://docs.bigcommerce.com/developer/docs/admin/multi-storefront/msf-international-enhancements/overview.md
- founder's save: Commerce & International Data Transfers Whitepaper (9.16.2025).pdf

Sentence searches, with the documents opened, are given in `not-found.tsv` (`searched`): for [1] five documents (Connecting with BigCommerce Payments, Connecting with Braintree, bigcommerce.com/payments/paypal/, bigcommerce.com/product/, bigcommerce.com/product/consumer-financing/); for [2] three founder-saved PDFs; for [3] three documents (bigcommerce.com/payments/embedded-payment-providers/, Using Script Manager, Implementing CCPA with BigCommerce).

## Live pages

None read.

## Copies and gaps

- Q2-BC-G0154 (which region a store's data is stored in, and whether a merchant can choose it): Q2-BC-031 and Q2-BC-032 close it, from the founder-saved whitepaper.
- Q2-BC-K0132 and Q2-BC-P0029 say BigCommerce Payments is "initially" for US-based merchants; Q2-BC-P0030, Q2-BC-P0068 and Q2-BC-P0087 name UK and US stores. Both are copies of different pages; neither copy was changed.
- Q2-BC-012 and Q2-BC-014 record clauses (b) to (d) of items that Q2-BC-K0430 and Q2-BC-K0432 copy only to clause (a).

## Account points not checked (past the cap, or set aside by order)

Not recorded as rows and left out of `account.md`:
- Shopify [1]: Shop Cash exceptions (Q2-SH-K1759); Bill Pay, BACS notifications and Audiences (Q2-SH-K1852; Q2-SH-K1827; Q2-SH-K2053); Managed Markets' DDU/DDP, Shopify Protect and order caps (Q2-SH-010; Q2-SH-021); EEA consent mode, address and tax fields, compare-at prices, `.at`/`.fr` domains (Q2-SH-030; Q2-SH-032; Q2-SH-024; Q2-SH-035); France's Shopify Payments requirements (Q2-SH-038); Singapore GTO (Q2-SH-048).
- Salla [1]: Paylink acquisition (Q2-SA-046); CheckSallaBlacklisted (Q2-SA-059); pharmacies (Q2-SA-057); Business Platform certificate (Q2-SA-K0093); external gateway replacing Salla Payments (Q2-SA-K1639).
- WooCommerce [1]: WooPay (Q2-WC-K0447); iDEAL KVK (Q2-WC-018); Przelewy24 changes and MCCs (Q2-WC-020; Q2-WC-023); Alipay and WeChat Pay prohibited types (Q2-WC-014); In-Person Payments country lists (Q2-WC-K0439, apart from the fees sorted in the account); Store Guidelines (Q2-WC-K0493).
- WooCommerce [2]: Stripe as additional data party (Q2-WC-068); Canada and UAE data notices (Q2-WC-066).
- [3] reasons on domains, Brexit card rates, BACS, WooPay, UAE trade licence and WooPayments country priority (Q2-SH-035; Q2-SH-037; Q2-SH-K1827; Q2-WC-041; Q2-WC-K0411; Q2-WC-K0403).

## Problems with the method

- `R3-checking.md` changed on disk during the run: its account limit went from about 800 to about 1,200 words. The account was written to the shorter limit.
- The Help Center pages read are undated; their `source_date` is the capture date, with `date_basis` "undated; date captured".
- The corpus search's `--max 10` lists up to 10 documents per corpus (capture runs and founder's saves separately), so a search listed more than 10.


## The coordinator's correction, 19 October 2026

Q2 on Shopify's account cited some of Q2-SH-027 to Q2-SH-035 one number off, in six points: a statement was inserted after those points were written (the Q2 draft's notes found it). The ids are corrected by what each statement says, in Shopify's account and in the points and notes here that name them.
