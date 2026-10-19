# Notes: Q7, zid

## What was read (2026-10-19)

The held pages are in capture run `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/` unless another run is named.

- **Selection:** `copy_statements.py show` for each candidate concern, and for ZD-C-015, ZD-C-019, ZD-C-077, ZD-C-083 and ZD-C-099. ZD-C-015 was added.
- **Sentences [1] to [3]:** one corpus search, listed in Q7-ZD-N05. It found 43 documents. These ten were opened:
  - help.zid.sa/store-language/ (159);
  - help.zid.sa/zidpay_staff_and_currencies/ (184);
  - docs.zid.sa/localization-33664641e0.md (045);
  - docs.zid.sa/view-order-12479054e0.md (067);
  - docs.zid.sa/get-manager-profile.md (027), searched for its currency and balance fields only, since it is 1.7 MB;
  - zid.sa/ar/legal/zidpay-terms-conditions-sa/ (189) and -kw/ (188);
  - docs.zid.sa/applepay-checkout-1032876m0.md (009);
  - zid.sa/en/solutions/payments/ (198);
  - docs.zid.sa/create-a-new-product.md (013).
- **Further pages for [2] (data model):**
  - help.zid.sa/markets/ (136);
  - zid.sa/en/legal/terms-conditions/ (194), searched for "currency" only. Its fee-currency clause is the English of the copy Q7-ZD-K0156, so it was not recorded again.
- **Sentence [4]:** one corpus search for the balance. Opened:
  - help.zid.sa/deposits_zidpay/ (110);
  - help.zid.sa/zid-wallet/ (182).
- **For the not-found rows:**
  - help.zid.sa/transactions/ (166);
  - help.zid.sa/refund-requests/ (149), its currency line only;
  - help.zid.sa/gcc-merchants/ (128);
  - the text of help.zid.sa/tap-gateway/ (162) and help.zid.sa/payment-gateways/ (145), searched for currency terms;
  - the raw page of zid.sa/ar/paymob/ (run 20261012T104936Z-s01-sources, item 125), searched for currency terms;
  - docs.zid.sa/payment-paid-event-17956148e0.md (s01 run, item 012) and docs.zid.sa/overview-1340608m0.md (053), searched for currency and amount. They hold neither.
- **Raw pages:** for the Zid Pay terms pages (189, 188), zid.sa/en/solutions/payments/ (198), zid.sa/en/legal/terms-conditions/ (194) and zid.sa/ar/paymob/, `text.txt` holds only the error message "عفواً! حدث خطأ." or "Oops! Something went wrong.". The raw page was read instead. Its text was taken out with a tag-stripping script in the scratch directory.

## Live pages read

- https://docs.zid.sa/llms.txt, an index used only to find the next page's address. Served in English, 2026-10-19.
- https://docs.zid.sa/execute-payment-request-17112105e0.md, the `.md` endpoint. It is not held. Served in English (text/markdown), 2026-10-19. Its quotes Q7-ZD-C025 and Q7-ZD-C026 are pending capture.

## Not read

- The other 33 documents from the currency search, among them:
  - the coupon, abandoned cart, bundle and credit note API pages;
  - create-order, list-of-orders and update-order-by-id;
  - create-cashback-rule and credit-customer-wallet, which name the GCC currencies for customer wallets;
  - zid.sa/en/egypt/;
  - zid.sa/en/partners/developers/blog/partner-payouts/;
  - help.zid.sa/zidpay-digitalproducts/.
- No more pages were opened, because the reading limit for the sentence was reached.
- The dashboard screen لوحة التحكم > الاعدادات > اللغات والعملات is behind a login. It is routed to the founder in Q7-ZD-N03 and Q7-ZD-N05.

## Copies

- No copy was found wrong.
- help.zid.sa/store-language/ holds two notes on changing the currency:
  - one on أسعار المنتجات, the copy Q7-ZD-K0302;
  - one on المبيعات, recorded as Q7-ZD-003.
- The checker reported no copy as changed.

## Problems with the method

- The checker reads a `route` that names a held page as a route to the founder, even when `who_can` is `either`. Routes that named held pages were reworded to "Ask Zid".
