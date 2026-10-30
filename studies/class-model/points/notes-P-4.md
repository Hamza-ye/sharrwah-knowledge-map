# Notes on batch P-4 (S-02: S02-VP-13 to S02-VP-19, S02-VP-26 to S02-VP-29)

For the coordinator. The model read is the merge at a11d4727. Every landing, conflict and lead below is a reading, the drafter's, except where a key is quoted as a fact.

**What happened on the way.** The first drafting pass stopped when `show` warned that C-anchor's and C-bigcommerce's files had changed after the last merge, which was the coordinator's C amendment from S-01's points. After the merge at a11d4727 I read CM-PAY-011's BigCommerce cell again. It is unchanged (`core;extension-point;outside`, with Stripe among its fillers through BC-I-0452), so VP-13's draft stands. None of the other cells this batch rests on (CM-PAY-005, CM-PAY-007, CM-PLN-004, CM-PLN-007, the TAX cells) was in the amendment. `show` printed no warning on the second pass.

**Count:** 7 landed, 4 with conflicts (5 conflicts in all).

## Points that were hard to land

- **S02-VP-13, payouts.** Lands on CM-PAY-005. Zid's variant S02-V-180 opens with its merchant wallet's withdrawal rule (S02-ZD-114, محفظة زد). CM-PAY-005's note keeps that wallet apart as CM-PLN-006, so CM-PLN-006 is added. BigCommerce's one answer, S02-BC-223, is Stripe scheduling the first payout of a store connected through Stripe OCS. That is a third-party provider's flow alone, so under the brief's rule for flows it lands on CM-PAY-011, whose BigCommerce cell already places `outside`. I found it with `caps` (Stripe). The other reading would be a `placement` conflict on CM-PAY-005's BigCommerce cell, which is `core` (BC-C-025/where/BC-S-0141), with no `outside`. I set that aside because CM-PAY-005 is the platform's own payment service's payouts, and BigCommerce Payments isn't Stripe OCS.
- **S02-VP-14, subscription fees and billing currency.** The platforms answer in three capabilities:
  - CM-PLN-004: the platform's own bills;
  - CM-PAY-007: the payment service's fees; WooCommerce answers only here;
  - CM-MKS-007: Shopify's currency conversion fee by store location or entity. The model holds that fee there (SH-C-109/decides/SH-S-0555), not in CM-PAY-007.

  Plan prices per country (S02-SA-256, AED 990; S02-ZD-389, EGP) are CM-PLN-001's thing ("with its tiers and prices"). Paying invoices manually in India (S02-BC-281) is CM-PLN-005's. Neither is any platform's only answer, so I didn't add them. The coordinator may prefer CM-PLN-001 beside CM-PLN-004.
- **S02-VP-16, tax and duty obligations.** The main capability is CM-TAX-001. Four tax capabilities are added, because Salla and BigCommerce answer only there and register answers rest on them:
  - CM-TAX-003, VAT registration number and certificate: S02-SA-350, S02-ZD-098;
  - CM-TAX-007, ZATCA integration: S02-SA-358, which the answer 'the store's country' cites. Found with `caps`;
  - CM-TAX-004, BigCommerce's Settings › Tax › Add tax service: S02-BC-369. Found with `caps`;
  - CM-TAX-009, Form 1099-K: S02-WC-070, which the answer 'the merchant's country' rests on.

  Set aside: Shopify's Managed Markets in Canada, where Global-e sells to the customer as merchant of record (S02-SH-515, S02-V-137), is CM-MKS-003's thing. Shopify also answers in CM-TAX-001 (S02-SH-248, S02-SH-318), so I raised no `placement` conflict on CM-TAX-001's Shopify cell. "Duty" might point to CM-TAX-008, but no variant answers there.
- **S02-VP-17, Shopify products and services.** I landed it as `none`, reach `cross-cutting: markets and the seller's country`, with a `structure` conflict. Each platform answers with a different service, and the leads (CM-POS-001, CM-PAY-026, CM-MKS-003, CM-SHP-002) are each one service's. CM-ACC-008, the closest by name, holds only the countries the platform as a whole serves: sanctions lists, Salla's and Zid's markets. Naming every service's capability would land the point on half the model.
- **S02-VP-18, local language and currency.** The main capability is CM-MKS-005. Added:
  - CM-MKS-008, language: BigCommerce's content in the country's language, S02-BC-288;
  - CM-ACC-006: BigCommerce's Localization Settings by default country, S02-BC-253 and S02-BC-285;
  - CM-MKS-009: WooCommerce's tax label and address locale by base country, S02-WC-137 and S02-WC-154, the page lead on class-wc-countries.php;
  - CM-POS-001: the POS currency by the location's entity, S02-SH-921; cash rounding, S02-SH-935; the native currency for POS, S02-WC-102. The answer 'a business entity' rests on S02-SH-921.

  I found CM-MKS-008 and CM-ACC-006 with `caps`.
- **S02-VP-26 to S02-VP-29, market.** These land on CM-MKS-001. CM-MKS-001's BigCommerce cell is `none-held`, and BigCommerce answers with its storefronts (CM-CHN-007, in VP-26 and VP-27) and its channels (CM-CHN-001, in all four). Zid's marketplaces named as markets (S02-ZD-145, S02-ZD-146, the answer 'a channel') are CM-CHN-003's. Zid also answers in CM-MKS-001, so I didn't add it. Shopify's B2B catalog limits (S02-SH-703) are CM-B2B-003's. Shopify also answers in CM-MKS-001, so I didn't add that either.

## Each conflict, with both sides

1. **S02-VP-14, `count` (rows: S02-M8, model). BigCommerce on CM-PLN-004.**
   - The subject: S02-BC-280 (About Your BigCommerce Invoice: Invoice Line Items; a store in India pays manually) and S02-BC-281 (an email reminder with a payment link on the billing date). These show BigCommerce's own invoicing, built-in behaviour, so `core`.
   - The model: the cell is `not-stated`, on the agreement's terms only (BC-I-0462, BC-C-030/where/BC-S-0184, BC-C-030/decides/BC-S-0188, BC-C-030/decides/BC-S-0189). Its reading says no billing page or invoice list is held.
   - My reading: the statements bear out `core`. What settles it: the help article at S02-BC-C356 and S02-BC-C357.
2. **S02-VP-15, `count` (rows: S02-M3, model). Zid on CM-PLN-007.**
   - The subject: S02-ZD-476 to S02-ZD-483 are Zid's own plan checkout (POST /v1/managers/purchases/v2/checkout/noon/credit-card). Its invoice lines carry "VAT %15" on the Rise plan's price as the Business address country changes. That is Zid's own tax on its charges, so `core`.
   - The model: `not-stated`, on the Terms' duty clause alone (ZD-C-020/responsible/ZD-S-0675).
   - My reading: the observations bear out `core`. What settles it: the run's captured response.
3. **S02-VP-15, `count` (rows: S02-M3, model). BigCommerce on CM-PLN-007.**
   - The subject: S02-BC-359 to S02-BC-365 are BigCommerce's own plan-upgrade checkout. Its Taxes line changes with the billing contact's country: $0.00 in Muscat, $34.80 in Sydney, $69.60 in London.
   - The model: `not-stated`, on the merchant's duty clause alone (BC-C-030/responsible/BC-S-0190).
   - My reading: the observations bear out `core`.
4. **S02-VP-17, `structure` (rows: S02-D3, model).** No capability holds which of the platform's services a store may use by its country.
   - The subject: S02-SH-248, S02-SH-026, S02-SH-217, S02-SH-933, S02-SH-870, S02-SA-169, S02-SA-276, S02-SA-144, S02-ZD-059, S02-ZD-125, S02-WC-095, S02-WC-191, S02-WC-419 (extensions shown by `base_location_country`) and S02-BC-089. They show such availability in every area.
   - The model: it holds each service's eligibility, where it holds it at all, inside that service's cells (SH-C-110/decides/SH-S-0562, WC-C-060/decides/WC-S-0905, WC-C-089/decides/WC-S-0893).
   - S02-D3 reads "the services a store may use" as one rule keyed on the seller's country. Whether the model names it is the coordinator's call. The options are a capability of its own, or the cross-cutting decision on markets and the seller's country with each service's cell citing its eligibility.
5. **S02-VP-26, `count` (rows: S02-D4, model). BigCommerce on CM-MKS-001.**
   - The subject: S02-BC-113 ("separate storefronts per region … our international enhancements for MSF"), S02-BC-164 (selling to several countries, each with its own language, currency and payment methods, "requires a Multi-Storefront (MSF) setup"), S02-BC-172 and S02-BC-177 (one storefront channel for the US and another for Switzerland). BigCommerce's own feature gives per-region versions of the store's selling, so `core`.
   - The model: CM-MKS-001's BigCommerce cell is `none-held`. CM-CHN-007's note keeps MSF out of Markets because "no statement of BC-C-039 ties a storefront to a place". These statements do tie one, but they aren't in the concern map.
   - My reading: the statements bear out `core` on CM-MKS-001, beside CM-CHN-007's `core`. The subject's absence S02-BC-N01 (no country among a channel's properties) bears on how BigCommerce ties a storefront to a place, not whether. If the coordinator reads MSF as CHN-007's thing alone, the conflict becomes `structure`: on BigCommerce one feature is both capabilities.

Not raised:
- **S02-VP-19.** The answer 'every store' says four platforms bind every store's data to one policy and controller. The subject's own statements qualify that: Shopify's controller entity by location (S02-SH-617) and Zid Egypt's policy for zid.eg (S02-ZD-383). But no cell of CM-TRU-013 contradicts the answer, so it isn't a `premise` conflict by the brief's definition. S-08 (S02-M5) may want it.
- **S02-VP-27.** WooCommerce's confirmed absence of a market limit (S02-WC-N01) is the absence of a limit, not of the capability. It makes no `placement` conflict against CM-MKS-001's `core` WooCommerce cell.

## The checker's leads

`check --batch P-4` printed no `lead:` lines. Every landed point has, for each platform whose statements the subject holds, a landing cell with statements on that platform.

## Slot fillers the subject names that `cell` doesn't list

On capabilities with `outside` cells or of the kind `slot`. Each is a lead, not a conflict:
- CM-PAY-005 on Salla: the Saudi Central Bank (البنك المركزي بالمملكة العربية السعودية), whose authority governs Salla's transfer of the stores' funds (S02-SA-211).
- CM-TAX-004 on BigCommerce: Avalara (recommended), CereTax, TaxCloud Simple Sales Tax, TaxJar, Vertex and CCH SureTax, in Settings › Tax › Add tax service (S02-BC-369). The capability lists no fillers on BigCommerce.
- CM-TRU-013 on Shopify: the GDPR (S02-SH-717), the ePrivacy Directive (S02-SH-953) and the European requirements of the DPA (S02-SH-623). The capability lists the GDPR only on WooCommerce.
- CM-TAX-003 on Shopify: Global-e, already listed. CM-PAY-011 on BigCommerce: Stripe, already listed (BC-I-0452). Neither is new.

## Problems with the brief or the script

- A key cited only as a slot filler's source (BC-I-0452 on CM-PAY-011) isn't accepted as a basis key: "not a key a cell … holds". I replaced it with BC-C-026/where/BC-S-0151, which the cell cites.
- `show` once printed the merge warning partway through the batch, when the coordinator's amendment was in the working tree. Stopping there, as the brief says, worked.
- No other problems.
