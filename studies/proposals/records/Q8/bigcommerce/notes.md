# Q8, BigCommerce (check run): notes

## What was read

No map of BigCommerce's help is held, so reading started from the corpus search. Every page read is a capture in this repository's runs (`evidence/product-class/runs/`). They were found with `corpus_search.py` and located with `held_index.py`, and all are in English. No live page was read, and no founder's save was opened.

- Topic search: `python3 -I method/corpus_search.py bigcommerce plan plans add-on add-ons beta betas edition editions feature features release releases --max 10`. Opened:
  - https://docs.bigcommerce.com/developer/docs/beta.md
  - https://support.bigcommerce.com/s/article/Pricing
  - https://www.bigcommerce.com/pricing/
  - https://www.commerce.com/terms/ai-features-addendum/
  - https://www.bigcommerce.com/product/paypal-agentic-commerce-beta/
  - https://www.bigcommerce.com/blog/closed-beta-opportunity-bigcommerce-payments/
- Search for the account points still unmatched in sentences [1] and [2], as listed in the scratch file `unmatched-points.md`. The command is in `not-found.tsv`. Opened:
  - https://docs.bigcommerce.com/developer/docs/beta/checkout-extensions/overview.md
  - https://www.commerce.com/terms/store-terms/
  - https://www.bigcommerce.com/apps/
  - https://www.bigcommerce.com/product/
  - https://docs.bigcommerce.com/developer/api-reference/rest/integrations/tax-provider.md
  - The search also listed https://docs.bigcommerce.com/developer/docs/integrations/apps/guide/approval-requirements.md, which was opened as well.
- Search for the account points still unmatched in sentence [3]. Opened:
  - https://www.commerce.com/terms/jurisdiction-specific-terms/
  - https://www.commerce.com/terms/ (Master Services Agreement)
  - https://support.bigcommerce.com/s/article/Unified-Billing-for-Partners
  - https://docs.bigcommerce.com/developer/api-reference/rest/admin/payments/methods.md
- One more search for the terms the first two searches left out. Opened:
  - https://docs.bigcommerce.com/developer/docs/integrations/apps/guide/types-of-apps.md
  - https://support.bigcommerce.com/s/article/How-do-I-access-and-install-the-new-single-click-apps-within-my-Bigcommerce-store-control-panel
- The `--with` search for row Q8-BC-N11 (plans). Opened: https://support.bigcommerce.com/s/article/Platform-Limits. That page gives one maximum for Store-level API accounts (50) and names no plan for it. This was not recorded as a statement, because the cap had been reached.

The statement cap was reached at 60, counting each table's rows and each list's runs as one. Reading stopped there.

## Account points not checked (past the 20th not-found row)

These WooCommerce [3] points had no statement or copy to sort against. They were not searched for one by one and have no row:
- Q8-WC-014 and Q8-WC-015: the experimental-features warning.
- Q8-WC-K0559: HPOS under the stable flag.
- Q8-WC-045: releases roughly every five weeks.
- Q8-WC-037: admin suggestions by base location.
- Q8-WC-044: the Marketplace "Country" filter.

## Copies and sources that differ

- The Checkout Extensions page (Q8-BC-041) says the feature "is available without restrictions in development and on a live store". The Closed Betas page (Q8-BC-040) lists Checkout Extensions among its closed betas, as does copy Q8-BC-K0088. Both pages were captured on 2026-10-12.
- The Master Services Agreement defines "Store" as "an individual admin panel" (Q8-BC-021). The Store Terms define it as "an individual, online (not physical) storefront or a shopping cart" (copy Q8-BC-K0462 cites that page).
- The BigCommerce Payments closed-beta post names "a Standard, Plus, or Pro plan" (Q8-BC-065). The pricing pages name Core, Growth, Scale and Performance (Q8-BC-003 to Q8-BC-008).

## Problems with the method

- Selection (step 1) came before the accounts. "What it offers" was taken as the platform's offer to sellers: its plans, editions, products, apps, extension mechanisms and staged features. Concerns that are store-data resources, and the legal and data concerns, were set aside. Among the latter was BC-C-079 (Contracting Entity). The accounts then showed a Shopify point on the contracting party, so the Master Services Agreement and the Jurisdiction-Specific Terms were read for it under sentence [3].
- The repository's commit moved during the run, from f37eb8796cd351c46011ba4f9c2f4eb71a2c5fb1 to a2763afb1e5b6b2b07e4567ab282257e2f13b5a8. `read` paths in `not-found.tsv` are given at f37eb879.
- Some docs pages are held as Markdown. Statements from them (Q8-BC-040, Q8-BC-061, Q8-BC-072 to Q8-BC-076) keep the Markdown link and bold markup verbatim.
