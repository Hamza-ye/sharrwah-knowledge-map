# S-01 phase D: notes

Status: checkpoint. `bears-on.tsv` has all 23 variation points; `yemen-marks.tsv` has `YC-00` for each. The other cases are not marked yet.

## How the conditions were read

- **Three sources, per statement.** For each answer variant, each of its statements was taken with the (e) statements whose `conditions` name it and with its own `scope`. A statement with neither has no condition. A variant counts as working when one of its statements' conditions is shown met, and as failing only when every statement's conditions are shown failed. So a variant whose statements carry only places in different countries (one in the UAE, one in Kuwait) holds where any of them holds.
- **Alternatives within one statement.** S01-ZD-141 (Zid's plan table: bank transfer on every plan) and S01-ZD-149 (Zid Egypt's Starter plan) both name S01-ZD-075. They say where the variant holds in two markets, so they were taken as alternatives, not as two conditions that must both hold.
- **The nine (e) statements marked `none stated`.** None has an identifier that appears in a variant's statements, either as a statement's identifier or in its text. So none conditions a variant. This drops S01-SA-189 ("منصة سلة متاحة حاليًا في السعودية والإمارات فقط"), S01-SH-154 and S01-SH-155 (Multi-Currency Payouts), S01-SA-186, S01-ZD-134, S01-ZD-135, S01-BC-031, S01-BC-037 and S01-BC-038.

## What Stage 1 can check

- **YA-62 is the only axis that names a reference's provider.** Its parts at PayPal ("Available", or "Send only" in YC-156), Stripe ("Unavailable"), WooPayments ("Not available, a request to add it open") and Zid Pay ("Unavailable") decide every mark that depends on a provider. It is in every variation point's `bears-on.tsv` row except S01-VP-05.
- **Payment into the merchant's own account, cash on delivery, cheques, payment at the shop:** YA-131, YA-126, YA-128, YA-130 and the constants YK-167, YK-184 and YK-203.
- **A carrier's app linked to the store:** YK-206 gives Torod's link as "not available, being developed". It shows no party that can take the role, and it doesn't show that none can, so these variants (S01-V-123, S01-V-150, S01-V-164, S01-V-435) stay undetermined.
- **SoftPOS card payments through a provider such as Geidea (S01-V-059):** YK-161 gives SabaCard acquiring local and international Visa and Mastercard cards. I took this as a party that can take the provider's role. Stage 1 says nothing about SoftPOS itself.
- **Sanctions (S01-SH-047):** checked against YA-27, YK-22, YK-23 and YK-24. YK-23 ("allowed if the recipient is not on a sanctions list") and YK-24 ("named as a limit on e-commerce") don't settle whether Yemen is "a sanctioned country or region embargoed". S01-SH-047 decides no mark, because every variant it conditions also needs a Shopify Designated Country.

## Unchanged or with a partner

`carried unchanged` and `carried only with a partner` can both hold for one variant, and the first in the list wins. I gave `carried unchanged` when the variant works with the parties it names and the evidence shows them serving the case (PayPal, per YA-62), or when its role is held by the merchant's own account (direct bank transfer, cheques, Zid's bank transfer). I gave `carried only with a partner` when the variant puts a role with a party it doesn't name, such as "شركة الشحن" in S01-SA-091, "مزود الخدمة مثل جيديا" in S01-SA-113, or "البنك" whose terms apply in S01-ZD-075 (S01-V-269), and Stage 1 names a party that can take it (Torod, SabaCard, Kuraimi). A reviewer could read the carrier variants as unchanged instead. In S01-VP-02 that would change YC-00's mark from partner to unchanged, with the same variant.

## Marks that were hard to give

- **S01-VP-14, YC-00 (S01-V-630).** The variant is a withdrawal from PayPal to the merchant's bank at any time. YA-62 gives PayPal as available for payments from or to Yemen. It doesn't say whether a PayPal account in Yemen can withdraw to a bank in Yemen. The mark rests on S01-BC-091's condition, which is all the brief asks to check. S01-V-616 and S01-V-633 have the same gap.
- **S01-VP-05, YC-00 (S01-V-102).** YA-131 gives buyers paying online sellers by transfer into the sellers' accounts. YA-126 gives payments between banks as "none, only cash, cheques or within one institution" in government-controlled areas. The parts of YA-131 that name an account are the Dakhm store's Kuraimi accounts and "the seller's account". Both are consistent with transfers within one institution.
- **WooCommerce's Ecommerce Services (S01-V-494, S01-V-503).** The scope covers WooPayments, WooPay and the Payments feature. YA-62 gives a state only for WooPayments, so these variants stay undetermined rather than failing.

## Problems with the method

- **No constant for the merchant's country.** Stage 1 has no constant saying that the merchant is in Yemen. So a condition that names only other countries ("Users in the United States", Shopify's Designated Countries, "السعودية; الكويت") can't be shown failed with Stage 1 ids. A condition that every merchant outside a country meets (S01-ZD-121 "استخدام المحفظة متاح لجميع التجار خارج المملكة", S01-ZD-122 "التجار خارج المملكة", S01-WC-012 "If you reside outside of the Designated Countries") can't be shown met either. The only exception is where YA-62 names the provider.
- **No placement is out of reach.** 22 of the 23 variation points have at least one answer variant with no condition at all, so no failure can be shown for them. In S01-VP-10, S01-V-167 (Shopify) and S01-V-550 (صندوق سلة) block it. So no `no placement` mark is possible in any case, and every variation point without a carried variant is `unknown`.
- **Moves.** YA-62's WooPayments part is "Not available, a request to add it open" (YE-E641, YE-E642, YE-E645), from a feature request on WooCommerce's site. That is not a consultation, partnership, licence or regulator's action, so `moves` is empty. No other cited evidence names one that would change a mark.
