# Notes: Q6, shopify

## Selection

- Copied 22 rows: SH-C-001, 002, 004, 005, 006, 008, 062, 063, 064, 068, 075, 081, 086, 088, 091, 098, 100, 104, 110, 173, 174, and S-01.
- Set aside the other 86. Their reasons are in `selection.tsv`.
- Added no concern.

## What was read

Held, observed-sh at c8b5fbee25966372a0475e6ed81f0b7760ac2921:

- Help Center pages, through `method/help_map.py shopify page`, all in English (md/en):
  - intro-to-shopify/initial-setup/setup-getting-started (nothing new);
  - intro-to-shopify/pricing-plans/free-trial;
  - intro-to-shopify/initial-setup/setup-business-settings;
  - intro-to-shopify/initial-setup/new-to-shopify-checklists/general-checklist;
  - payments/shopify-payments/supported-countries;
  - payments/shopify-payments/onboarding/eligibility;
  - payments/third-party-providers/payment-gateway-availability;
  - intro-to-shopify/pricing-plans/pricing-overview;
  - payments/third-party-providers/configuring-providers;
  - checkout-settings/test-orders/payments-test-mode (it repeats what configuring-providers says);
  - your-account/manage-billing/paying-your-bills/making-payments/payment-methods-for-bills;
  - your-account/manage-billing/paying-your-bills/managing-payments/billing-address.
- `raw/runs/20261006T232216Z-journey-signup-new-account`: `actions.jsonl`, `run.json`, the text of steps 001 to 003, 012, 013 and 019, the aria of steps 004 and 010, and these answers:
  - ShopifyPaymentsData, ShopifyPaymentsActive, SignupMutation, BusinessDetailsData;
  - EligibilityQuery, FinanceApp, CoreCapital;
  - the first part of atlas.shopifysvc.com/countries.
- `structures/shopify/sign-in-methods/accounts.shopify.com@signup` (items.jsonl, meta.json).
- `structures/shopify/com-llms/llms-txt` (source.txt line 43, items.jsonl line 28, meta.json).
- `structures/shopify/help-center/help.shopify.com@en-ar/meta.json`.
- `raw/runs/20260930T050139Z-shopify-com-pages/fetch.warc.gz@41642451` (https://www.shopify.com/payment-gateways), through `warc_text.py`.

Held in this repository's capture runs:

- https://www.shopify.com/legal/terms, from `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/143-shopify.com/text.txt`: sections 1 and 2.
- https://help.shopify.com/en/manual/your-account/legal/unsupported-countries-and-regions.md, from items/101-help.shopify.com/text.txt.

Corpus searches (commands are in `not-found.tsv` where a row rests on them):

- "age of majority", "business purposes", "سن الرشد", "18 عامًا";
- "isn't available in your country", "not available in your region", "unsupported country", "غير متاح في بلدك", "غير مدعوم".

## Live pages read

- https://www.shopify.com/payment-gateways, read 2026-10-19 through `method/capture/page_text.mjs`, served in English.
  - It showed the "Type in your country" filter and the unfiltered list of providers. Nothing from it is cited.
  - Working copy: `/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/records/Q6-shopify/pg-live.txt`.

## What could not be read

- The per-country results of the payment gateways filter. They show only after typing a country (Q6-SH-N01).
- The Settings > Payments page of store 2jiwxs-gr. It is not held (Q6-SH-N02).
- Steps 002 and 003 of the sign-up journey. Their visible-text files hold only an extraction error ("visible text failed"). Their aria files were not needed: the aria of step 004 holds the "I'm located in:" combobox.

## Copies out of date or wrong

- Q6-SH-P0097, the pilot's list of "Shopify Payments for <country>" pages, has 40 items and no China item.
  - The held Help Center page (observed-sh c8b5fbee, run 20261016T213535Z-help-en-ar-html-md) lists 41 items, including "Shopify Payments for China".
  - Recorded as Q6-SH-023. The pilot's absence Q6-SH-A0002 counts 40 items.

## Problems with the method

- `check_proposals.py` rejects a not-found row whose `route` names an address that is held, even when `who_can` is `either`.
  - For Q6-SH-N01 and Q6-SH-N03, the held copies (the shopify.com/payment-gateways archive record and the accounts.shopify.com@signup structure) were read. They don't show what the rows ask for: filtered results, and what happens after choosing a place.
  - The routes now name the pages in words instead of by address.
- `help_map.py shopify page` reports "not held" for `md/en/manual/your-account/legal/unsupported-countries-and-regions.md`. That page was read from this repository's capture run instead.
- The `I'm located in:` list has 233 options. It is recorded whole as one statement (Q6-SH-010) with 19 citations. Nothing presents it as complete, so no absence rests on it.
