# Notes: batch P-6 (S-02, points 55 to 68)

The drafter's notes for the coordinator (`briefs/P-points.md`, "Notes"). The model is the merge at a11d4727. Every placement and slot filler below is the model's cell as `land_points.py cell` printed it. Every "reading" is marked as one.

**Count:** 14 points: 10 `landed`, 4 `conflict` (S02-VP-58, S02-VP-61, S02-VP-62, S02-VP-65), with 6 conflicts: 1 `placement`, 5 `count`. None is under a founder's decision: they rest on S02-F7, S02-F8 and S02-F9, rows that follow by rule (RD3). The checker's final line: `# 14 points in P-6, 0 problems`, with one `lead:` line, answered in "The checker's lead" below.

## Points that were hard to land

- **Several capabilities on one point.** Most of the batch's points are one setting that each platform holds in a different capability. Following the brief's step 1, I named the capability of each platform's answer where it differs, main one first. Where a platform's answer belongs to one flow only, I named that flow's capability: Global-e's to CM-MKS-003, WooCommerce Tax's to CM-TAX-002, WooPayments' buy now, pay later and Affirm's to CM-PAY-015, Zid's carriers' cash on delivery to CM-PAY-029. This gives:
  - S02-VP-58: five capabilities;
  - S02-VP-61: five;
  - S02-VP-62: six;
  - S02-VP-67: five.

  A reading: fewer would leave a platform's answer on a cell that doesn't hold it. If the coordinator prefers one capability per point, the main one is first in each row.
- **S02-VP-55 and S02-VP-56: no lead offered CM-CHK-003.** The point's own words, "Checkout profile and customer account configuration", are Shopify's. Its capability is Shopify's checkout and accounts editor and Checkout and accounts configurations (CM-CHK-003, SH-C-048/where/SH-S-0772). `caps --terms checkout` found it; no lead did. Its reading already says that overrides by market need the markets permissions.
- **S02-VP-59: no lead offered CM-SHP-016.** Salla's answer is a shipping route set for a market (S02-SA-175, "حدد السوق الذي تريد تطبيق المسار فيه"). That is Salla's Shipping Routes, CM-SHP-016, found with `caps`. The cell's note says no statement held says what a route is. S02-SA-175 shows that a route is applied in a market: a lead for that cell's definition, not a conflict.
- **S02-VP-63 and S02-VP-64: reach.** I read the reach as `cross-cutting: markets and the seller's country`. The business entity is the business record (S02-D1) that the architecture plan's section 3 names under that decision. S02-D3 has every rule keyed on the seller's country read it, and Shopify's entity is "used for financial products, markets, apps, and taxes" (S02-V-650). This is a reading.
- **S02-VP-65: where Shopify's "Returns and cancellations" lands.** Shopify's market customization links to `settings/legal/cancel-return-rules` (S02-SH-310). The model reads that route as the cancellation and return policy, under store policies (CM-CNT-008, SH-C-034/decides/SH-S-7089). I followed the model. A reading: the rules a market takes (its default rules, "Add rule") could also be read as a returns setting. If so, CM-RET-001 or CM-RET-003 would take it; Shopify's cells there are core either way.
- **S02-VP-67: Shopify's priorities are its order routing.** I landed Shopify's "inventory and fulfillment priorities" on CM-SHP-005, not CM-INV-009, where Shopify has no cell. The statements are marketCreate (S02-SH-284) and the routing rule "Stay within the destination market" (S02-SH-852).

## Each conflict, with both sides

1. **S02-VP-58, `placement` (rows: S02-F8, model). Avalara and Shopify's duties.**
   - The model: CM-TAX-008 on Shopify is `core` (SH-C-105/where/SH-S-7129, SH-C-105/decides/SH-S-7079, SH-C-105/where/SH-S-0538). Its only slot filler is the customs authorities (SH-C-105/decides/SH-S-0537).
   - The subject: S02-SH-295 (the Duties and taxes dialog in a market) and S02-SH-986 (the duties journey's terms, market Canada) both state "Shopify partners with Avalara to provide duty calculation for a 0.5% transaction fee".
   - A reading: both sides hold. The fix would be `core;outside` with Avalara as a slot filler, through an amendment citing the two subject statements.
   - S02-F8 rests on Avalara as a tax partner bound per market.
2. **S02-VP-61, `count` (rows: S02-F7, model). WooPayments' local payment methods.**
   - The model: CM-PAY-017 on WooCommerce is `not-stated`. It holds only the doc's first line, cards by default (WC-C-006/decides/WC-S-0871).
   - The subject: S02-WC-320 and S02-WC-321 list WooPayments' local methods and the buyer's billing country and currency each needs.
   - Why it counts: the model's maker statement for WooPayments, "designed by Woo for Woo" (WC-S-0557, `own-service` in CM-PAY-002), counts for each feature of the service. So this is `own-service` by the model's rule.
   - A reading: the statements bear it out.
3. **S02-VP-61, `count` (rows: S02-F8, model). WooPayments' buy now, pay later.**
   - The model: CM-PAY-015 on WooCommerce is `extension-point` only (WC-C-005/where/WC-S-0708), with Affirm, Afterpay and Klarna as suggestions and slot fillers.
   - The subject: S02-WC-318 (scope "Affirm, Afterpay and Klarna with WooPayments") shows these methods offered with WooPayments, keyed on the WooPayments account's country.
   - With WC-S-0557, this is `own-service` beside `extension-point`.
   - What would settle it: whether WooPayments' buy now, pay later is WooPayments' own feature or the providers' extensions.
4. **S02-VP-62, `count` (rows: S02-F9, model).** The same cell as conflict 3, here on S02-WC-319 (Affirm with WooPayments, "Affirm may disable your access"). S02-F9 keeps "Affirm's part" open. One amendment would settle both. Affirm withdrawing the method raises no `placement` conflict, since the cell isn't `core`.
5. **S02-VP-65, `count` (rows: S02-F9, model). BigCommerce's return settings.**
   - The model: CM-RET-003 on BigCommerce is `not-stated`. Its reading says no return reason is held, and that Q1's gap BC-C-021/decides (page not read) may hold the workflow.
   - The subject: S02-BC-335, S02-BC-339, S02-BC-340 and S02-BC-341 are its own settings: enable returns, reset Return Reasons and Return Actions, and their translation per storefront. S02-BC-330 and S02-BC-336 give the section Settings > Returns and the permission Manage Returns.
   - A reading: they bear out `core`. The amendment would cite them. CM-RET-001's parent cell is already `core`, by a product line.
6. **S02-VP-65, `count` (rows: S02-F8, model). Shopify's EU right of withdrawal.**
   - The model: CM-RET-004 on Shopify is `not-stated`. It holds only the help-centre section SH-I-2129, and its reading says no Shopify setting is held.
   - The subject: S02-SH-492 names one, the Managed Markets right of withdrawal feature, deactivated at Settings > Customer accounts. S02-SH-491 says Managed Markets applies compliant cancellation and return policies to EU orders.
   - What would settle it: whether the feature is Shopify's (CM-RET-004, `core`) or Managed Markets' with Global-e as merchant of record (CM-MKS-003, `core;outside`). Neither statement names a maker.
   - Consequence: if the coordinator lands it on CM-RET-004 as `core`, S02-VP-66's third party then differs as `placement`. That third party is the "compliant third-party solution" that replaces the feature (S02-SH-492).

## The checker's lead

**S02-VP-64, WooCommerce: no cell of CM-ACC-004, CM-ACC-005 or CM-MKS-003 holds WooCommerce statements.**
- The subject holds S02-WC-517, the business step of WooPayments' onboarding ("What type of legal entity is your business?").
- It also holds the confirmed absence S02-WC-N02: no WooCommerce settings page names a business entity.
- A reading: the WooPayments step could count `own-service` on CM-ACC-004 for WooCommerce, through WC-S-0557. I didn't record it as a conflict. S02-VP-64 is a "who sets" point, and the brief limits that comparison to third parties, through `placement`.
- If the coordinator reads the brief otherwise, it is a `count` on CM-ACC-004, WooCommerce (rows: S02-F9, model). The question is whether the business step is the store's business entity or only the payment account's.

## Leads for slot fillers, and others

Third parties and laws the subject names that the cells don't list. Each is a lead, not a conflict.
- **CM-TAX-008, Shopify:** Avalara (S02-SH-295, S02-SH-986), conflict 1.
- **CM-PAY-017, WooCommerce:** WooPayments' local methods Alipay, Bancontact, EPS, GrabPay, iDEAL | Wero, Multibanco, Przelewy24, SEPA Direct Debit and WeChat Pay (S02-WC-321). The cell's slot fillers are only MB WAY and Bizum (Shopify) and KNET (Salla).
- **CM-PAY-029, Zid:** "بعض شركات الشحن" (some shipping companies), which support cash on delivery for a 10-riyal fee (S02-ZD-127). The cell is already `outside` (ZD-C-014/reason/ZD-S-0635). The statement names no company.
- **CM-RET-004, Shopify:** the EU right of withdrawal, a law the statements name (S02-SH-491). CM-RET-004 is class 1, not a slot.
- **CM-CNT-008, Zid:** the Ministry's e-commerce exchange and return laws (S02-ZD-466).
- **Fastlane by PayPal (S02-BC-124, S02-BC-128) and PayPal translating its methods by the shopper's location (S02-BC-287).** These are PayPal's own product and behaviour on BigCommerce, so I landed neither. CM-PAY-013 on BigCommerce is `not-stated`, so neither makes a `placement` conflict.
- **CM-TAX-002, WooCommerce:** WooCommerce Tax's filter, which developers change (S02-WC-122). A reading: this is WooCommerce Tax's own interface for one of its settings, so the developers set a value; they don't provide the calculation. No third party, no conflict.
- **CM-CNT-008, WooCommerce (S02-VP-66):** WooCommerce's sample draft Refund and Returns Policy page (S02-V-1077) is the platform's own. A reading: it could support `core` where WooCommerce's cell is `not-stated`. I didn't raise it, for the same reason as the checker's lead.

## A difference inside the subject

S02-F8's answer says the tax partner "such as Avalara" is named by "Shopify and BigCommerce". S02-VP-58's own analysis, as `show` prints it, says BigCommerce's automatic tax provider (S02-BC-246) "is unnamed, so it isn't the same party". The model's cells don't contradict either reading: CM-TAX-004 on BigCommerce is `extension-point` for third-party tax providers, none named Avalara. So I raised no `premise` conflict. The coordinator may want to reword the row.

## Problems with the brief or the script

- **"Who sets" points.** The brief limits a "who sets" point's comparison to third parties, through `placement`. Read that way, a `count` the subject's statements show on such a point is never raised, as with S02-WC-517 and S02-V-1077 above. I followed it as written and listed those cases here.
- **The checker.** It checks that a `terms` item is among the point's terms, not that the capability holds the term. I used only terms that a lead printed, or terms that the capability's name or cells hold.
