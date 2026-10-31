# Q3's check, batch Q-04: checkout, orders and tax (17 rows)

Rows: km:CHK-01 to CHK-06, km:ORD-01 to ORD-07, km:TAX-01 to TAX-04. The check is in `check-Q-04.tsv`; `q3.py check` prints "17 of 17 rows placed; 0 problems".

Counts: 14 covered, 3 partly (CHK-02 with a held rest, CHK-06 and TAX-04 with a rest beyond the class), no whole-row miss, none unclear.

## Rows that were hard to place

- **km:CHK-02 (what a merchant configures about checkout).** Required fields, guest or account, order notes and terms each have a capability with cells (CM-CHK-001's terms hold Salla's Guest checkout and WooCommerce's Enable guest checkout; CM-ORD-013; CM-CNT-008, store policies, cites Zid's terms-and-conditions page type ZD-S-0780). Tipping has none. Its one statement, SH-I-2109, lands in CM-CHK-001, which is coarser than tipping, so by the brief's rule it is a held miss. A reading: tipping could also be taken as one of checkout's settings, which would make it detail of CM-CHK-001. I placed it as a held miss because a tip is an amount of its own on the order, not just a display setting. The coordinator decides which it is.
- **km:CHK-06 (consistency and availability under peak load).** The row asks what checkout *must* guarantee and how that is tested. That is Sharrwah's design, so `engineering:build` answers it, and the rest is beyond the class. The class shows mechanisms that partly answer it, each a fact at its key: CM-OPS-001 (availability under load: Shopify, Salla, BigCommerce); CM-INV-008 (stock held for unpaid orders: WooCommerce's `woocommerce_hold_stock_minutes`, WC-S-5401, and Zid); BigCommerce handling concurrent requests in strict order to avoid overselling (BC-S-0036, in CM-INV-001); and Shopify's idempotency keys toward financial partners (SH-S-0452, in CM-PAY-004). I searched for price consistency at checkout and for load testing and found nothing, in English and in Arabic ("peak", "flash sale", "high traffic", "oversell", "حجز المخزون", "الذروة").
- **km:TAX-04 (the target market's VAT and e-invoicing regime, ZATCA).** What a regime requires, and which party is responsible, is a market's law. S-05 answers it (tax and invoicing; it hasn't run, so the basis is `subjects.tsv S-05`), with the tax authority (`outside`). The class's own part has cells: CM-TAX-007, where Salla and Zid link the store's invoices to ZATCA through the platform, plus CM-TAX-003 and CM-ORD-008. "The target market" is already decided: Yemen is the first market, and a market's law is its setup and never defines the platform (founder-decisions 2026-10-29, Intent (standing)). So that part is `founder:decided`, which sets no time. A reading: ZATCA is Saudi Arabia's authority, so the row's example names a market that isn't the first one. I didn't mark this as `wrong party`, because the row doesn't ask for that decision, it only presumes a market. Time bombs: bundles (answerers' times differ), wrong time (`launch` against S-05's before build) and market fact.
- **km:ORD-01 (an order's axes of state).** Archive is held only as BigCommerce's webhook topic `store/order/archived` (BC-I-0166, cited in CM-ORD-001@bigcommerce), plus Shopify's section title "Set up order processing and archiving" (CM-ORD-010, not-stated). That is enough for coverage. The states and their transitions are detail.
- **km:ORD-07 (the two event catalogs).** The row was written for two platforms. The model holds five, and the order events sit in CM-ORD-001's cells (webhook topics among their terms) and in CM-API-008. How the catalogs line up is detail.
- **km:ORD-04.** The money consequences of an edit are covered by CM-RET-002 and CM-PAY-020. S-01's register row S01-E4 (whoever holds the money carries out a refund) bears on this for Sharrwah. I didn't name engineering, because the row asks what the class does.

## Candidate misses, and what was searched

- **Tipping (km:CHK-02's rest), held: SH-I-2109.**
  - Shopify's help-center section "Setting up tipping options for online orders". It is a title only, and no statement says what it sets.
  - Its concern, SH-C-047, lands in CM-CHK-001. No cell cites it.
  - Searched with `search`: "tip; tipping; tips; gratuity; tip amount; tipping options" on Shopify, WooCommerce and BigCommerce. For Salla and Zid, "tip; tipping; إكرامية; الإكرامية; إكراميات; الإكراميات; بقشيش; البقشيش". Only Shopify matched.
  - Searched with `outscope`: the same terms on all five platforms; nothing on tipping.
  - Shopify's tipping page would settle what the capability holds.

Searches that found a capability, so no miss:
- gift order (CM-LOY-006);
- order filters and bulk actions (ZD-I-0265 and SA-S-1996 in CM-ORD-001, SA-S-1776 in CM-ORD-003);
- order export (ZD-I-0263 in CM-MIG-001);
- archive (BC-I-0166);
- stock held at checkout (CM-INV-008);
- marketplace orders (CM-CHN-003);
- draft-order invoices (SH-S-7225 in CM-ORD-005);
- discount rules at checkout (CM-MKT-004);
- HS code and country of origin (CM-SHP-020);
- terms at checkout (CM-CNT-008).

Searches that found no checkout-specific evidence:
- a terms-acceptance checkbox at checkout: "terms and conditions; الشروط والأحكام; شروط وأحكام; الموافقة على الشروط". These found only the platforms' own legal agreements, and Zid's store policy pages, which are in CM-CNT-008. The checkbox itself is left as detail of CM-CHK-001 and CM-CNT-008.

## Problems with the brief or the evidence

- None that stopped the check.
- The coordinator's change of cdc27c97 (`founder:decided`) was applied to km:TAX-04.
- Receipts are held only as Shopify's App Store category "Invoice and receipt apps" (CM-ORD-008@shopify, extension-point). No platform's own receipt document is held. I noted this as detail for km:ORD-06, not as a miss, since order documents have capabilities.
