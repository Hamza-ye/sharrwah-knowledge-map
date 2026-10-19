# Q4 on Zid (checking run): notes

## What was read

All reading was of held captures in `sharrwah-knowledge-map@7d4a58f6c0d717982322f6bc0fe7f0aff7fa1516:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/`, read 2026-10-19. No live page was read.

- Topic search (`"التحويل البنكي" "الدفع عند الاستلام" "bank transfer" "bank transfers" "cash on delivery" "حالة الدفع" "تم الدفع" --max 10`): read help.zid.sa/cod/, help.zid.sa/bank-accounts/, help.zid.sa/checkout-page-options/, help.zid.sa/credit-debit-notifications/; the others listed (webhooks, logistics T&Cs, the payment-methods FAQ, the COD FAQ, pricing, zid.sa/en/uae/) are already among the copies and were not reopened. help.zid.sa/zid-wallet/ (in that search's list past the first 10) was searched for COD terms.
- Sentence [1] and [2] search (one call for both): read zid.sa/ar/legal/terms-conditions/ (its text file holds only "عفواً! حدث خطأ."; searched in `raw.html`) and help.zid.sa/logistics-shipping-methods/.
- Sentence [3], two searches: read help.zid.sa/invoice-settings/, orders-properties/, order-status-messages/, partial-return/, payment-constraints/, change-order-status/, dashboard-analytics/, and docs.zid.sa/list-of-payment-method.md and create-order-20612055e0.md (searched for payment fields; over 100 KB).
- Sentence [4] search: read docs.zid.sa/view-order-12479054e0.md and update-order-by-id.md (both over 100 KB, searched with grep), help.zid.sa/defaulting/.
- Sentence [5] search: the documents it listed are Zid Pay, Mazeed and Jahez pages; none was opened besides the COD FAQ already copied.
- help.zid.sa/return-order/ was searched for payment terms through `held_index.py`; it was not listed by a search.

## Selection

ZD-C-011 (other gateways) was set aside at first and added after reading the Salla account, whose [1] has a point on gateways the merchant connects; the copy was re-run.

## Account points not checked

Rows were recorded for 13 points. These account points were not checked and have no row:

- Shopify [1]/[5]: Q4-SH-045, Q4-SH-046 (COD in Italy as a custom method, and COD apps) beyond what Q4-ZD-N07 covers.
- Shopify [3]: Q4-SH-006, Q4-SH-009 (payment instructions); Q4-SH-011 (mark as paid not captured again); Q4-SH-026 (draft order amount received); Q4-SH-031, Q4-SH-032 (cancelling unpaid fulfilled orders).
- Shopify [4]: Q4-SH-027 (email money transfers), Q4-SH-029 (B2B drafts), Q4-SH-043 (error codes).
- Salla [1]: Q4-SA-034, Q4-SA-035 (Salla Point custom methods); Q4-SA-K1626, Q4-SA-K1627 (PayPal, stc pay); Q4-SA-A0002 (wallet tabs).
- Salla [3]: Q4-SA-016, Q4-SA-K0563 (proof of partial payment); Q4-SA-063 (COD confirmation message); Q4-SA-032 (Salla Point cash orders); Q4-SA-010, Q4-SA-053 (قيد الاسترجاع, cashback); Q4-SA-042 to Q4-SA-044 (drawer); Q4-SA-051, Q4-SA-052, Q4-SA-064, Q4-SA-065 (COD in reports); Q4-SA-036, Q4-SA-037.
- Salla [4]: Q4-SA-012 (label cancellation), Q4-SA-040 (Salla Point lapsed card subscription).
- Salla [5]: Q4-SA-K1602, Q4-SA-P0150 (COD tracking in the UAE and Kuwait).

## Problems with the method

- Zid has no help map, so the per-sentence searches were combined for [1] and [2].
- Several pages read for a sentence were in a search's list past its first 10, not in the first 10.
- The Terms page (zid.sa/ar/legal/terms-conditions/) is dated "اغسطس 2026", a month only; its `source_date` is given as 2026-08.
