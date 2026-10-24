# Q3 · BigCommerce (checking run): notes

## Selection

Copied: BC-C-025, BC-C-026, BC-C-028, BC-C-030, BC-C-047, BC-C-080, BC-C-085, BC-C-086 and S-01. The other 34 concerns were set aside (reasons in `selection.tsv`). No concern was added.

## What was read

Held pages (captures in `evidence/product-class/runs/`), read whole or through `grep`:
- 20261013T053949Z-s01-bigcommerce-help-founder-machine: items 001 (Connecting with BigCommerce Payments), 003 (Connecting with PayPal), 004 (Connecting with Stripe OCS), 025 (Enabling Stored Credit Cards), 028 (Getting Started: Payments), 033 (Managing Currencies), 037 (PCI Compliance), 046 (Testing Shipping, Tax and Payment Settings); and `grep` only in 027 (Getting Started: Channels), 032 (Intro to APMs), 040 (Pricing) and 045 (Tax Overview).
- 20261012T0419Z-q1-bigcommerce-sources: items 102 (bigcommerce.com/pricing, including the FAQ answers in `raw.html`), 108 (commerce.com/terms), 109 (Acceptable Use Policy), 112 (Fees and Billing), 119 (Store Terms), 040 (docs settings API).

Live pages, read 2026-10-19, both served in English:
- https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/settings/storefront-status.md (an index of two endpoints only; nothing recorded from it)
- https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/settings/storefront-status/get-settings-storefront-status.md (cited by Q3-BC-C014; "pending capture")

No founder's save was opened: the corpus searches listed only the Trust Center PDFs and SafeBase page, whose snippets were about ISO certificates, policies and PCI guides, not seller requirements.

## Searches

Each sentence's corpus search is given in `searched` of its not-found rows. Sentences [1] and [2] each had a second search, for account points the first one's terms didn't cover (currency, second login step, confirmation codes, payout minimum, financing, digital products, gateway exclusivity). That is one search more per sentence than the checking brief's item 8 allows.

## Not read

- support.bigcommerce.com pages not held, such as the BigCommerce Payments onboarding flow and the Actions section's KYC tasks: not tried live, because the Help Center couldn't be read from outside in earlier runs. Q3-BC-N01 routes the onboarding flow to the founder.
- PayPal's Acceptable Use Policy and Stripe's prohibited and restricted businesses list, which Q3-BC-022 and Q3-BC-021 name: providers' own terms, not read.
- Held pages listed by the searches but not opened are named in each not-found row's `searched`.

## Account points

Every account point on Q3 by Shopify, Salla and Zid was sorted, or left out because it rests only on not-found rows or gaps (Shopify [4] Q3-SH-N03; Salla [4] "Still open"; Zid [2] Q3-ZD-N03; Zid [4] Q3-ZD-G0002/G0058). None was left unchecked for the 20-row cap.

## Problems with the method

- Held help pages carry no date. `source_date` is the capture date, and `date_basis` says so.
- The checking brief allows one not-found row per account point. Several account points on the same matter, such as the verification documents, share one row here (Q3-BC-N01), and one row can be cited by points in more than one section.
- The copied gaps (Q3-BC-G0047 to G0160) cover none of the account points; none was closed.
- Copies were not found wrong or out of date. Q3-BC-006 adds the sentence before Q3-BC-K0459, and Q3-BC-012 adds step (1) of the steps whose (2) to (4) Q3-BC-P0063 copies.
