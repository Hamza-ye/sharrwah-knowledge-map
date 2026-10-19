# Q2 on Zid (check run): notes

## Selection

39 rows copied (38 concerns and S-01), 27 set aside, with reasons in `selection.tsv`. Copying gave 293 statements, 55 gaps, 158 pilot statements, 19 pilot gaps and 4 pilot absences.

## What was read

All held, from capture run `20261012T045101Z-q1-zid-sources` unless noted; read 2026-10-19.
- https://zid.sa/ar/legal/zidpay-terms-conditions-sa/: text file holds only "عفواً! حدث خطأ."; read through `raw.html` with bounded grep.
- https://zid.sa/ar/legal/zidpay-terms-conditions-kw/: same; read through `raw.html` with bounded grep.
- https://zid.sa/ar/legal/terms-conditions/: same; `raw.html` converted to plain text in the scratch directory and searched by heading.
- https://zid.sa/en/legal/privacy-policy/: same; `raw.html` converted to plain text in the scratch directory and searched.
- https://help.zid.sa/payment-requirements/ (text file, read in full).
- https://help.zid.sa/saudi-merchants/ and https://help.zid.sa/gcc-merchants/ (text files, compared).
- https://help.zid.sa/checkout-page-options/ (text file, address section).
- https://help.zid.sa/payment-gateways/ (text file, availability lines).
- https://help.zid.sa/order-status-messages/ and https://help.zid.sa/abandonment-cart/ (the CITC line only; already copied as Q2-ZD-K0614).
- https://docs.zid.sa/upload-file-to-s3-11396102e0.md and https://docs.zid.sa/onesignal-store-settings-39420053e0.md (grep only).

## Live pages

None read.

## Not read

- The other documents listed by the corpus searches named in `not-found.tsv`.
- https://zid.sa/en/legal/zidpay-terms-conditions-sa/ and https://zid.sa/en/legal/terms-conditions/ (the Arabic versions were read).

## Account points not checked

None beyond the six not-found rows and the copied gaps cited in `account.md`. Account points resting only on N, G or H ids were not sorted against, as the brief says. These account points were not sorted, and no row was recorded for them: Shopify's points on Point of Sale fiscal rules in named European countries, domains, Shopify Balance, Bill Pay, Audiences, BACS, 1099-K, crypto, Shop Cash, Managed Markets details, EU consent and compare-at prices; Salla's points on the UAE pages of its agreement, Paylink, the blacklist check; WooCommerce's points on WooPay, Przelewy24, iDEAL, Alipay and WeChat Pay, EU VAT extension, withdrawal note, geolocation, Store Guidelines, Stripe regional law and data parties.

## Copies

No copy was found wrong or out of date. The general terms page (`terms-conditions`) embeds the Zid Pay Saudi and Kuwaiti terms in its own text, so the sanctions wording shows on that page only inside its زد باي section.

## Problems with the method

- To learn the citation format I opened the first three lines of Salla's `citations.tsv`, which the checking brief does not list among what may be opened from another run's folder. Nothing from it was used.
- Dates: for the Zid Pay terms and the privacy policy no date was found in the text read; `source_date` is the capture date, and `date_basis` says so. The copies date these pages from the sitemap.
- The corpus search term "نظام" matched too widely; "موثوق" matched the word موثوقية.


## The coordinator's correction, 19 October 2026

Q2 on Shopify's account cited some of Q2-SH-027 to Q2-SH-035 one number off, in six points: a statement was inserted after those points were written (the Q2 draft's notes found it). The ids are corrected by what each statement says, in Shopify's account and in the points and notes here that name them.
