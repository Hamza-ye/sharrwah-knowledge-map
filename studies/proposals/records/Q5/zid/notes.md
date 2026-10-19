# Q5 on zid: notes

## Selection
25 concerns copied, 40 set aside (reasons in `selection.tsv`), S-01 copied as preset. ZD-C-022 (App Market subscriptions and partner payouts) was set aside; it may show how app charges are paid through Zid, which row Q5-ZD-N18 records as not in what was read.

## What was read (all held captures; no live page was read)
- First reading search: `corpus_search.py zid "طرق الدفع" "بوابة الدفع" "بوابات الدفع" "payment method" "payment methods" "payment gateway" "payment gateways" --max 10`. Read: help.zid.sa/zidpay_staff_and_currencies/, help.zid.sa/payment-gateways/, help.zid.sa/tap-gateway/, the FAQ ماهي طرق الدفع التي استطيع توفيرها في متجري؟, docs.zid.sa/list-of-payment-method.md (schema only, no list of codes). Not read (copied already): help.zid.sa/payment-requirements/, help.zid.sa/gcc-merchants/, the commercial-registration FAQ, the Mazeed gateway FAQ.
- Unmatched account points, with terms, listed in the scratch file `unmatched-points.md`. Searches S1 (sentence 1), S2 (sentence 2, also carrying sentence 1 terms), S3 ([3]), S4 ([4]), S5 ([5]), and S6, one second search shared by sentences 1 to 5 for the points left out of S1 to S5. The commands and the documents opened are in `not-found.tsv`.
- zid.sa pages whose text file holds only the error page were read from `raw.html` (zid.sa/ar/legal/zidpay-terms-conditions-sa/, zid.sa/ar/legal/terms-conditions/, zid.sa/en/legal/terms-conditions/, zid.sa/ar/solutions/payments/, zid.sa/en/pricing/, zid.sa/ar/paymob/), with a tag-stripping working copy in the scratch directory.
- Paths in `not-found.tsv` cite the repository at 309e428ae340c40084d9bbfd2641bc654460ce5b, the HEAD when the rows were written; the corpus search printed 3e1d174b368f5e02692393624d97b26968c1cf54 earlier in the run. The evidence files read are the same captures.

## Not checked
Account points past the 20th row, not recorded as rows and left out of `account.md`:
- BigCommerce [1]: Q5-BC-072 (a notification and a staff log entry when a payment method changes). S6 carried its terms.
- Salla [1]: Q5-SA-003 (the merchant must run payments through the set methods). S6 carried its terms.
- Salla [3]: Q5-SA-012 / BigCommerce [3]: Q5-BC-002 (PayPal as a digital wallet). S3 carried its terms; nothing found.
- Shopify [3]: Q5-SH-K1533 / BigCommerce [3]: Q5-BC-067 (accelerated checkout). S6 carried its terms.
- Shopify [4]: Q5-SH-015 (a previous provider staying available for refunds). S4 carried its terms.
- Salla [4]: Q5-SA-K1654 (methods linked to a gateway cancelled with it). S4 carried its terms.

## Copies
No copy was found wrong or out of date. Copies Q5-ZD-K0097 and Q5-ZD-P0143 (Advanced Payment Methods, starter false, listing COD) and Q5-ZD-K0113 (Cash on Delivery, starter true) are both from the compare-plans data, as copied.

## Problems with the method
- Both briefs changed on disk during the run. The revised checking brief (item 8: list points first, one second search per sentence; item 10: rows up to 20) was applied from then on. S1 and S2 had already been run without a prior list, so the list was written afterwards for them.
- Many help pages match menu words (الجمعيات, كاشير, كاش باك) in every page's navigation, which fills the `--max 10` listing with pages that don't bear on the terms.
