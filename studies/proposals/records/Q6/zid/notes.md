# Q6 on Zid: notes

## Selection

- 17 concerns copied, and 2 added: ZD-C-020 and ZD-C-050.
- 41 rows set aside, among them S-01.
- The copy holds 157 statements and 28 gaps.

## What was read

### Held pages (capture run 20261012T045101Z-q1-zid-sources, at sharrwah-knowledge-map 7d4e86c5e535e465d2cbdba210d64c8b55a0d4a1)

- https://help.zid.sa/ (index only, for links)
- https://help.zid.sa/gcc-merchants/
- https://help.zid.sa/saudi-merchants/
- https://help.zid.sa/payment-requirements/
- https://help.zid.sa/store-info-ksa/
- https://help.zid.sa/category/zid-pay/ (FAQ)
- the FAQ زد يخدم التجار في السعودية فقط؟ هل يخدم الخليج؟
- https://help.zid.sa/activate-online-payments/
- https://help.zid.sa/store-language/ (searched lines only)
- https://zid.sa/ar/legal/terms-conditions/
- https://zid.sa/en/egypt/
- https://docs.zid.sa/create-cashback-rule-42661790e0.md
- https://zid.sa/llms.txt (searched lines only)

For https://zid.sa/ar/legal/terms-conditions/ and https://zid.sa/en/egypt/, `text.txt` holds only the error text "Oops! Something went wrong." These pages were read from `raw.html` beside it, with tags stripped, in a working copy in the scratch directory.

### Live pages, all read on 2026-10-19

| Page | Language served | How it was read | Result |
| --- | --- | --- | --- |
| https://zid.sa/en/syria/ | English | raw HTML through curl | Rendered through `method/capture/page_text.mjs`, it returned only the error text. Statements are quoted from the raw page. |
| https://zid.sa/en/uae/ | English | raw HTML through curl | Same as the Syria page. |
| https://zid.sa/en/oman/ | English | rendered only | Error text only. Nothing recorded. |
| https://zid.sa/en/kuwait/ | English | rendered only | Error text only. Nothing recorded. |
| https://web.zid.sa/register | Arabic | rendered | Redirected to https://dashboard.zid.sa/ar-sa/register. Cited by the URL fetched. Only the first step, before an email is entered, was read. |

## What could not be read

- The FAQ answers on https://zid.sa/en/syria/ are in neither the raw HTML nor its embedded page data. The rendered page returned an error text. See Q6-ZD-N02.
- The registration flow beyond the email step, including its country choices, shows only by signing up. See Q6-ZD-N01, routed to the founder.

## Copies

- Q6-ZD-K0221 (English) gives Zid Egypt's tax ID as 711-549-443. Q6-ZD-K0222 (Arabic) gives it as 711-459-443. Both copies are as recorded. This run did not read the source to settle which is right.
- None of the copies read was found out of date.

## Method

- The payment-requirements article's lists are HTML `<ul>`/`<ol>` items with no text markers. Each statement runs from the first item to the last. Each quote starts at the heading that precedes the list.
- No provider's own terms were read.
- The checker reports the live citations as "pending capture".


## Coordinator's note

- After this run, the coordinator captured the live pages it cites. The registration flow's first page (web.zid.sa/register) is now held, so N01's route was reworded to name only the later steps it asks for, without the page's address. Nothing else was changed.
