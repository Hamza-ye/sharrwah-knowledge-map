# Notes: Q5, bigcommerce

## Selection
I copied 12 concerns: BC-C-020, 022, 023, 025, 026, 027, 030, 031, 059, 074, 084 and 085, plus S-01. I set aside 45, each with its reason in `selection.tsv`. I added none.

## What I read (held, at sharrwah-knowledge-map@bb0a660e7405d8873010a4226c14cb3ea757dc73)
- Founder-machine Help Center capture (`evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/`):
  - read in full: Available-Payment-Gateways (002), Getting-Started-Payments (028), Intro-to-APMs (032);
  - read in part: Fastlane-by-PayPal (026, Requirements and Setup), Pricing (040, lines on Open Payment Provider fees), Using-Multiple-Currencies (049, payment lines), Managing-Currencies (033, introduction);
  - searched with grep: Connecting-with-BigCommerce-Payments (001), Checkout-Settings (016), Offline-Payment-Methods (006), PCI-Compliance (037), single-click apps (030), Multi-Storefront (035), Testing-Shipping-Tax-and-Payment-Settings (046).
- Q1 capture run (`evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/`):
  - read: payments/methods.md (051), payments/transactions-api.md (071), b2b/management/payment.md (056, to the start of its code table);
  - searched with grep: commerce.com/terms (108), commerce.com/terms/fees-and-billing (112), bigcommerce.com/apps (097).
- S01 a2 capture run: bigcommerce.com/payments/embedded-payment-providers (`evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/011-bigcommerce.com`).
- The founder's saves folder (`evidence/product-class/blocked-evidence-founder/bigcommerce/`): I listed it. It holds the Trust Center page and its PDFs (certificates, policies, whitepapers), none of them on payment methods. I opened none of them.

## Live pages read (2026-10-19)
- https://www.bigcommerce.com/partners/powered-by/ was served in English. It says nothing on payments (Q5-BC-N02).
- https://www.bigcommerce.com/apps/categories/payments/ returned a 404, served in English (Q5-BC-N03).

Both working copies are in the scratch directory. No statement cites a live page.

## Tables and lists left unrecorded (rule 5)
- Intro-to-APMs, "Available APMs": this table has more than 60 rows, each naming one APM, its supporting gateways and its countries. Only its introduction is recorded (Q5-BC-084). No absence rests on it.
- B2B Payments API (`b2b/management/payment.md`), "Supported payment methods": this table of more than 20 rows gives a code and a provider. Some rows are marked "(legacy)", such as `adyen` and `bluesnap`. Only the support sentence and the Warning above it are recorded (Q5-BC-091, Q5-BC-092).
- I didn't open these Available Payment Gateways links: Multi-Storefront Payment Methods (not held), 3D Secure, Recurring Billing and Optimized One-Page Checkout.

## Capture notes
- Available-Payment-Gateways and Connecting-with-BigCommerce-Payments are also held in `20261013T003518Z-s01-a2-sources`, where `held_index.py` reports them as not readable. The checker found every quote in the readable founder-machine capture.
- Most Help Center pages are undated. I gave their capture date as `source_date`.

## Copies
- None of the copies is wrong. The integration counts differ between pages: Getting-Started-Payments says "over 60 online payment integrations; serving 230 countries", while the copy Q5-BC-K0139 says "more than 65 … 150+ countries". Q5-BC-075 records the first, with a note.
- The checker reports no copy as changed.

## Method problems
- The brief points to the founder's saves, but for BigCommerce they hold only Trust Center documents. All the Help Center text read here comes from the founder-machine capture run that `held_index.py` finds.
