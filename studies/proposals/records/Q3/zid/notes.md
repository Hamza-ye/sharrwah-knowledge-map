# Notes: Q3 on Zid

## Selection

24 recorded concerns copied, 38 set aside (reasons in `selection.tsv`), and 2 added: ZD-C-025 (Zid Agent) and ZD-C-116 (store mobile app). S-01 copied. The `description` cells of the two added rows are empty, since only the id and terms are taken from `concerns.tsv`.

## What was read

All held, in this repository's capture runs at commit e8243566eb1adf9281e7d864619f529f4d13c092. Zid has no help map, so the reading started from the corpus search.

- https://help.zid.sa/payment-requirements/ (`20261012T045101Z-q1-zid-sources/items/147`)
- https://help.zid.sa/activate-online-payments/ (`…/085`)
- https://help.zid.sa/about_zidpay/ (`…/082`)
- https://help.zid.sa/saudi-merchants/ (`…/151`) and https://help.zid.sa/gcc-merchants/ (`…/128`)
- https://help.zid.sa/store-info-ksa/ (`…/158`)
- https://help.zid.sa/bnpl-2/ (`…/090`), https://help.zid.sa/payment-gateways/ (`…/145`) and https://help.zid.sa/tap-gateway/ (`…/162`)
- https://help.zid.sa/activate-mazeed/ (`…/084`)
- https://help.zid.sa/zid-wallet/ (`…/182`), its verification section only
- the help centre FAQ page, https://help.zid.sa/%d8%a7%d9%84%d8%a3%d8%b3%d8%a6%d9%84%d8%a9-%d8%a7%d9%84%d8%b4%d8%a7%d8%a6%d8%b9%d8%a9/ (`…/077`), its Amazon and Trendyol sections
- https://zid.sa/ar/legal/terms-conditions/ (`20261012T104936Z-s01-sources/items/122`): the sections الحسابات through المحتوى
- https://zid.sa/ar/legal/zidpay-terms-conditions-sa/ (`20261012T104936Z-s01-sources/items/124`): from التعريفات to التحويلات والمدفوعات الدولية
- `zid.sa/en/legal/terms-conditions/` (`…/194`), only to find the address of Apple's terms

The `text.txt` of both legal pages is an error page ("عفواً! حدث خطأ."). Their text was read from `raw.html`, through a working copy in the scratch directory. The checker found every quote in the capture.

## Live pages

No live page was read.

## What was not read

- The other business-type field lists in store-info-ksa (مؤسسة، شركة، جمعية خيرية): only the فرد fields, the upload limits, the company documents line and the SPL step were recorded.
- The Kuwait Zid Pay terms and the English terms, which were not read for this question beyond the Apple Pay address.
- The Apple Pay Merchant Terms (Q3-ZD-N05) and the service provider's terms (Q3-ZD-N06).

## Copies

No copy was found wrong or out of date. Q3-ZD-P0081 and Q3-ZD-K0104 cover إمكان only when Zid Pay is active; Q3-ZD-056 records the page's note for other gateways.

## Problems with the method

- The corpus search printed two different repository commits (a5b8818… and e824356…) in one session; the evidence paths were the same in both. `read` cites the current HEAD, e824356….
- The two legal pages are held with an error page as their `text.txt`, so their text had to be taken from the raw HTML.
- The brief allows `###` subheadings within an account section, but `check_proposals.py` reports every `###` line as an error ("a section is headed by one sentence's number"). The subheadings were removed so that the checker passes.
