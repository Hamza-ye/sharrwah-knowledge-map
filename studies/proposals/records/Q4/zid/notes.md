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

## Searches added after the brief was fixed

The first per-sentence searches left out the terms of 33 account points. Following the fixed item 8, the points and their terms were listed in the scratch directory (`left-out-points.md`), and one more search was run for each sentence group whose search had left them out. All read 2026-10-19, held only; the commit printed was `dcabee220a75fb21b48e889f271b9dcf71287532`.

- [1] and [5]: `"PayPal" "باي بال" "stc pay" "اس تي سي" "كاشير" "مرسول" "هنقرستيشن" "وسيط" "الإمارات" "الكويت" "app" "apps" --with "الدفع عند الاستلام" "نقد" "cash on delivery" "COD" "طرق الدفع" --max 10`: read help.zid.sa/zid-pos-app/ (held in run 20261013T003518Z-s01-a2-sources), docs.zid.sa/-user-roles-and-permissions-604944m0.md, help.zid.sa/category/zid-pay/, help.zid.sa/gcc-merchants/.
- [3]: `"تعليمات" "instruction" "instructions" "إثبات الدفع" "دفع جزئي" "partial payment" "partial payments" "مسودة" "draft order" "draft orders" "محفظة العميل" "cashback" "الدرج" "cash drawer" "cash drawers" "تقارير الشحن" "رسالة تأكيد" "إلغاء الطلب" --max 10`: read help.zid.sa/customer-wallet/; credit-debit-notifications and change-order-status again.
- [4]: `"إلغاء البوليصة" "إلغاء بوليصة" "B2B" "error code" "error codes" "انتهاء الاشتراك" "Interac" "email transfer" "email transfers" --max 10`: read docs.zid.sa/get-payment-options-43307434e0.md.

They added statements Q4-ZD-033 to Q4-ZD-040 and rows Q4-ZD-N14 to Q4-ZD-N20. The wallet-tab point (Salla Q4-SA-A0002) had no term of its own in these searches; its row Q4-ZD-N16 gives the [5] search, which carried "محفظة".

Citations' `access_path` is now `rendered` for capture text files and `raw` for the Terms page's `raw.html`.

## Account points not checked

20 rows are recorded. These points come past the 20th row in item 10's order and were not checked:

- Salla [5]: Q4-SA-K1602, Q4-SA-P0150 (COD tracking in the UAE and Kuwait).
- Shopify [3]: Q4-SH-011 (mark as paid not captured again; confirmation email); Q4-SH-032 (cancelling a fulfilled unpaid order).
- Salla [3]: Q4-SA-063 (COD confirmation message).
- Shopify [4]: Q4-SH-027 (email money transfers), Q4-SH-029 (B2B drafts).
- Salla [4]: Q4-SA-012 (label cancellation), Q4-SA-040 (Salla Point after the card subscription lapses).

## Problems with the method

- Zid has no help map, so the per-sentence searches were combined for [1] and [2].
- Several pages read for a sentence were in a search's list past its first 10, not in the first 10.
- The Terms page (zid.sa/ar/legal/terms-conditions/) is dated "اغسطس 2026", a month only; its `source_date` is given as 2026-08.
