# Notes: Q6 on BigCommerce (checking run)

## What was read

- Topic search (no help map is held for BigCommerce): `python3 -I method/corpus_search.py bigcommerce "sign up" "signup" "free trial" "free trials" "create a store" "create an account" "eligibility" "18 years" "age of majority" "countries" "country" --max 10`. Read: https://www.commerce.com/terms/ (capture 20261012T0419Z-q1-bigcommerce-sources, item 108), https://www.bigcommerce.com/pricing/ (item 102, its raw.html for the FAQ answers), https://support.bigcommerce.com/s/article/Available-Payment-Gateways?language=en_US and https://support.bigcommerce.com/s/article/Getting-Started-Payments (capture 20261013T053949Z-s01-bigcommerce-help-founder-machine, items 002 and 028).
- Searches for the account points not yet matched, with their terms, are in `not-found.tsv` (`searched`), and the points with their terms are listed in the scratch file unmatched-points.md. Documents opened from them: acceptable-use-policy, store-configuration.md, Store-API-Accounts, store-information/v2.md; jurisdiction-specific-terms; Automatic-Tax-Setup, Tax-Overview, product/consumer-financing, payments/paypal, Intro-to-APMs; Connecting-with-BigCommerce-Payments, blog/bigcommerce-payments-uk-expansion.

## Live pages read

- https://www.bigcommerce.com/start-your-trial/, read 2026-10-19 through method/capture/page_text.mjs, served in English. Not held before this run: it is cited live and is "pending capture".

## Couldn't read

- What the sign-up flow asks after "Create your store" was not read: it needs an account to be created.

## Copies

- The pricing page captured 2026-10-12 says a trial store can take payments (Q6-BC-014). The live sign-up page read 2026-10-19 says trial stores can no longer process live payments from 14 October (Q6-BC-019). No copy holds either.

## Account points past the 20th not-found row (not checked)

- Zid [1]: plan choice inside the sign-up flow (Q6-ZD-007); store must display its name, address and registration (Q6-ZD-K0245, Q6-ZD-K0247); one published product before Zid Pay activation (Q6-ZD-K0007).
- Shopify [2]: tax services by business location (Q6-SH-K1865, Q6-SH-K1909); POS card payments and hardware by country (Q6-SH-K1783, Q6-SH-031); sales channel eligibility by region (Q6-SH-030, Q6-SH-032); standalone Stripe in Shopify Payments countries (Q6-SH-K1527); the store created with country=YE (Q6-SH-033, Q6-SH-034).
- Salla [2]: the Kuwait store-creation article and gcc-ecommerce page (Q6-SA-004, Q6-SA-053, Q6-SA-054); primary markets (Q6-SA-K1987, Q6-SA-K1990).
- Zid [2]: shipping companies for Gulf stores (Q6-ZD-008, Q6-ZD-K0345); Mazeed (Q6-ZD-K0547, Q6-ZD-K0546); Amazon and Jahez by place (Q6-ZD-K0631, Q6-ZD-K0632); ROVO in Syria (Q6-ZD-027).

## Problems with the method

- The sign-up page's hosting-region question has no counterpart in the accounts, so it is sorted as "goes beyond".
- Several not-found rows each cover account points from more than one in-depth platform where they describe the same matter, to keep within 20 rows.
