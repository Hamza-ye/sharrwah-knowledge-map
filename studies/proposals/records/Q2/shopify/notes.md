# Q2 on Shopify: notes

## What was read

Every page was read through `method/help_map.py shopify page` from observed-sh at `c8b5fbee25966372a0475e6ed81f0b7760ac2921`, in English. The Help Center's REGISTER date seen is 2026-10-16. Pages were read on 2026-10-18.

Read in full or to the relevant section:
- compliance/legal/hemp/payments.md
- compliance/legal/hemp/selling-hemp.md
- compliance/legal/alcohol.md (no statement recorded: it gives the law to the seller as information)
- compliance/legal/eu-right-of-withdrawal.md
- compliance/legal/pricing-indication-directive.md
- international/pricing/checkout-restrictions.md
- international/managed-markets/prohibited-items.md (to the end of the category table)
- international/managed-markets/requirements-and-considerations.md (to the start of its compatible-countries table)
- privacy-and-security/privacy/customer-privacy-settings.md
- privacy-and-security/privacy/customer-privacy-settings/understanding-customer-privacy-settings.md
- sell-in-person/shopify-pos/country-requirements.md
- payments/shopify-payments/supported-countries/france/requirements.md (first section)

Read only for lines found with `grep`:
- international/managed-markets/deactivation.md
- international/managed-markets.md
- international/managed-markets/overview.md
- checkout-settings/checkout-form-options.md
- domains/managing-domain-ownership/edit-domain-contact-information.md
- domains/troubleshoot-issues-with-domains.md
- intro-to-shopify/pricing-plans/pricing-overview.md
- sell-in-person/shopify-pos/customize-pos/printed-receipts/considerations-for-the-visual-editor.md
- compliance/legal.md and payments/shopify-payments/onboarding/eligibility.md (for "hemp")

Corpus searches, each run with `--max 10`:
- `"regulatory requirements" "local regulations" "due to regulations" "legal requirements" "المتطلبات التنظيمية" "اللوائح المحلية"`
- `"to comply with" "in order to comply" "للامتثال" --with "not available" "isn't available" "unavailable" "غير متاح" "غير متوفر"`
- the two searches given in not-found.tsv

No live page was read.

## Not read

- The compatible-countries table of Managed Markets, and the full list of prohibited item categories. Neither is recorded as a list.
- The Managed Markets pages for Canada and the UK.
- The POS retail requirements for Italy (retail-requirements-italy).
- The Comply app's own terms. The Help Center names the app, and no agreement in Shopify's terms incorporates them.
- The Arabic versions of the pages read. The English pages were quoted.

## Problems with the method

- `help_map.py page` prints HTML inside `<aside>` notes. A quote that spans a `<strong>` tag depends on how the checker removes tags. The "Neighborhood" sentence was therefore left out, and only the next sentence was recorded (Q2-SH-032).
- The Managed Markets compatible-countries table runs to more than 50 rows. Under rule 5 each row would be its own statement, so it was left unrecorded.
- The run was stopped once by a usage limit before account.md was written. It continued from the files already in the folder.
