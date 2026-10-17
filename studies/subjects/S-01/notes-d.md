# S-01 phase D: notes

Status: done, on Stage 1 as rebuilt at `b9928d9` (228 axes, 514 constants, 342 cases). `bears-on.tsv` has the 23 variation points. `yemen-marks.tsv` has 122 rows: `YC-00`, and every case whose `name` lists an axis that a variation point bears on (`YC-120`, `YC-121`, `YC-122`, `YC-123`, `YC-155`, `YC-163`, `YC-200`, `YC-201`, `YC-202`, `YC-203`, `YC-309`, `YC-336`, `YC-339`, `YC-340`, `YC-341`). The checker reports no errors. Its one review line is about `variants.tsv`, which is phase C's file.

## The marks

| Mark | `YC-00` | All 122 rows |
| --- | --- | --- |
| carried unchanged | 10 | 62 |
| carried with configuration | 0 | 0 |
| carried only with a partner | 3 | 20 |
| no placement | 0 | 0 |
| unknown | 10 | 40 |

- **Carried unchanged at `YC-00`:**
  - Eight rest on Zid's wallet terms for merchants outside the Kingdom (S01-ZD-121, S01-ZD-122), checked against Q2's frame:
    - S01-VP-01 (S01-V-024);
    - S01-VP-09 (S01-V-160);
    - S01-VP-11 (S01-V-194);
    - S01-VP-14 (S01-V-579);
    - S01-VP-15 (S01-V-343);
    - S01-VP-18 (S01-V-445);
    - S01-VP-19 (S01-V-480);
    - S01-VP-23 (S01-V-528).
  - S01-VP-13 (S01-V-244) rests on WooCommerce, Inc. as the party for residents outside the Designated Countries (S01-WC-012, S01-WC-014), checked against Q2's frame.
  - S01-VP-05 (S01-V-102), direct bank transfer, rests on YA-131.
- **Carried only with a partner:**
  - S01-VP-02 (S01-V-038) and S01-VP-04 (S01-V-093): a carrier outside Salla's shipping labels. The partner is Torod (YK-203, YA-130).
  - S01-VP-03 (S01-V-059): SoftPOS through a card service provider. The partner is SabaCard (YK-161).
- **Unknown:** S01-VP-06, 07, 08, 10, 12, 16, 17, 20, 21 and 22.
- **The other cases carry `YC-00`'s marks.** No variant's status differs from `YC-00`'s in any of them, with one exception: in `YC-155`, the PayPal variants can't be shown either way. No mark names them.
- **No placement:** none. So there are no product gaps and no founder items.
- **Moves:** none (see the last section).

## How the conditions were read

- **Three sources, per statement.** Each statement of an answer variant was taken with two things:
  - the (e) statements whose `conditions` name it;
  - its own `scope`.

  A statement with neither has no condition. A variant counts as working when one of its statements has its conditions shown met. It counts as failing only when every statement has its conditions shown failed.
- **Alternatives within one statement.** S01-ZD-141 (Zid's plan table: bank transfer on every plan) and S01-ZD-149 (Zid Egypt's Starter plan) both name S01-ZD-075. They say where the variant holds in two markets, so I took them as alternatives, not as two conditions that must both hold.
- **The nine (e) statements marked `none stated`.** None has an identifier that appears in a variant's statements, either as a statement's identifier or in its text. So none of them conditions a variant. This drops:
  - S01-SA-189 ("منصة سلة متاحة حاليًا في السعودية والإمارات فقط");
  - S01-SH-154 and S01-SH-155 (Multi-Currency Payouts);
  - S01-SA-186, S01-ZD-134, S01-ZD-135, S01-BC-031, S01-BC-037 and S01-BC-038.
- **Q2's frame: which conditions it checks.** This is the coordinator's line in the brief. These conditions were checked against it and cited as `Q2`:
  - words that name only countries or regions (S01-ZD-112, "متاح لتجار المملكة العربية السعودية و دولة الكويت");
  - words that require the store, the business or its account to be in a named place (S01-BC-067, "Your store must be located in the United Kingdom or the United States"; S01-ZD-133, "مسجلة في المملكة العربية السعودية");
  - scopes that name only a place (S01-SA-052, "الإمارات").

  Some (e) statements have a scope that names only a place: S01-SA-059 (UAE), S01-SA-064 (Kuwait), S01-SA-162 (Saudi Arabia), S01-ZD-107, S01-ZD-108, S01-ZD-110, S01-ZD-117, S01-ZD-118 (Saudi Arabia, Kuwait) and S01-SH-045 ("your Designated Country"). I read each as a condition placed there.
- **What the frame meets.**
  - Met: a place that includes the Yemeni market. These are "خارج المملكة" (S01-ZD-121, S01-ZD-122) and "outside of the Designated Countries" (S01-WC-012, with S01-WC-014's list: Australia, Canada, Japan, Mexico, New Zealand, Russia and the countries of Europe).
  - Also met: three conditions that name only another place and restrict only merchants there. These are S01-WC-042 ("Merchants in Japan cannot receive daily payouts"), S01-SH-144 (merchants in mainland China) and S01-SH-146 (Shopify Payments only in mainland France).
  - Not met: every other place condition.
  - EMEA: "UK and EMEA customers on Core, Growth, and Scale plans" (S01-BC-055, S01-BC-057) meets the region, but it adds plans that Stage 1 has no evidence for, so it stays unsettled. The paths it is on fail on S01-BC-029 anyway.
- **What the frame doesn't settle.** These conditions require something other than a place, so they stay unsettled, and so do their variants:
  - S01-SA-074: an Absher account, a bank account in a Saudi bank and a Saudi mobile number;
  - S01-BC-033: "all merchants", for BitPay;
  - S01-ZD-130: "متاح لجميع متاجر زد", for Mazeed, together with S01-ZD-129's documents;
  - S01-BC-035 and S01-BC-036: "more than 150 countries" and "100+ countries", none of them named.
- **Testing the readings.** I re-evaluated `YC-00` with some readings reversed:
  - the scope-only (e) statements read as unsettled: no variant's status changes;
  - the three other-place restrictions read as unsettled, or as not met: no variant's status changes;
  - S01-BC-033 and S01-ZD-130 read as met: two statuses change, and they would change marks (see "Marks that were hard to give").

## What each variation point bears on

- **YA-62** decides every provider condition: PayPal, Stripe, WooPayments and Zid Pay Kuwait. Its PayPal part today is "Sending from Yemen @ PayPal's service". With YK-514, "cannot receive money" (PayPal's service, YE-D997), every PayPal condition fails at `YC-00`. YA-62 is in every row except S01-VP-05.
- **Payment into the merchant's own account, cash on delivery, cheques and payment at the shop:**
  - axes: YA-131, YA-68, YA-126, YA-128, YA-129, YA-130;
  - constants: YK-203, YK-167, YK-184.
- **A carrier's app on Salla** (S01-SA-125, S01-SA-126, S01-SA-127): YK-206 gives Torod's link to online stores as "not available, being developed". That shows no party that can take the role, and it doesn't show that none can.
- **Sanctions** (S01-SH-047: "a resident of a sanctioned country or region embargoed by the United States, Canada, or the European Union, or ... a person or entity blocked or denied by [them]"):
  - it bears on YA-27, YA-28, YK-22, YK-23, YK-24 and YK-392;
  - none of them settles it in any case;
  - every statement S01-SH-047 conditions also fails on Q2 through Shopify Payments' place conditions (S01-SH-041 and the others), so it decides no mark.

**The items the independent reviewer found related.** Each is in or out as follows.

- **YK-514 (in).** "cannot receive money" (PayPal's service) bears on the PayPal conditions. Among them are S01-BC-091, S01-BC-110, and the PayPal scopes of S01-BC-090, S01-SH-050, S01-SH-051's PayPal row and WooCommerce's PayPal Standard.
- **YK-513 (out).** Wise is "listed among the best payment options for use in Yemen". No variant's condition names Wise, and no phase A statement mentions it.
- **YA-107 (out).** Its states are about online card-payment gateways: MEPS Yemen's e-invoicing and e-payment gateway, "nearly stopped since the war" and "lacking".
  - The conditions on card processing each name a provider: Stripe, Adyen, Network International, SMCC and JCB, Shopify Payments, Zid Pay, Salla Payments, PayPal and Braintree, or Tap. Q2 or YA-62 settles those, and YA-107's states name none of those providers.
  - The one card condition that names no provider is S01-SA-113: card payment at Salla Point's cashier through SoftPOS. That is payment at a point of sale, not an online gateway, and YK-161 bears on it.
- **YK-335 (in).** International payment cards are "no longer used" (buyers, place not stated, YE-E974, dated 2023-02-23). It bears on S01-SA-113's card payment. It doesn't decide S01-VP-03's mark, because YK-161 gives SabaCard acquiring local cards as well as international ones.
- **YA-68 (in).** Its bank-app parts (Bazzarry with Al-Qutaibi Bank, Kuraimi, Hasseb, Etlobni) bear on the conditions of payment into the merchant's own account:
  - S01-WC-092, S01-WC-093 and S01-WC-094 (BACS);
  - S01-SH-103 (manual payment methods);
  - S01-ZD-141;
  - S01-BC-120, for bank deposit.

  It appears in S01-VP-05, 11 and 13. YC-163, YC-340 and YC-341 change only its Procorners part, and the marks there are `YC-00`'s.
- **YK-61 (out).** "Through intermediary banks, not direct" concerns banks receiving wire transfers from abroad. No variant's condition names a transfer from abroad or the receiving bank. The wallet transfers out of Saudi Arabia (S01-ZD-058, S01-ZD-150) are the variants' own words, and their conditions (S01-ZD-121, S01-ZD-122) name only places.
- **YA-129 (in).** "Cash on delivery, preferred by 74 percent @ Aden" and "mostly cash on delivery" bear on the cash-on-delivery conditions, as YA-128 does:
  - the carrier scopes of S01-SA-090 and S01-SA-091;
  - S01-BC-120, for cash on delivery.

  It appears in S01-VP-02, 04, 05 and 13. YC-202 changes it, and the marks there are `YC-00`'s.
- **YA-28 (in) and YK-392 (in).** YK-392 gives "none [no secondary-sanctions risk] for transactions a US person could do without a specific licence". The general licences in YA-28's states say which transactions those are. Both bear on whether the US measures that S01-SH-047 names reach the merchant. They appear in the 11 rows that carry S01-SH-047. YC-122 and YC-123 change YA-28, and the marks there are `YC-00`'s.
- **YK-370 (out).** Yemen Kuwait Bank's designation says neither where the merchant resides nor whether the merchant is blocked, which is what S01-SH-047 asks. No variant's condition names a bank in Yemen.

## Stale and disputed parts

I read each part's date in the axis `note` column for YA-27, YA-62, YA-68, YA-126, YA-128, YA-129, YA-130 and YA-131.

The parts the marks rest on are:

| Axis | Parts | Date |
| --- | --- | --- |
| YA-131 | the Dakhm store's part | 2026-10-10 |
| YA-131 | Sana'a | 2025-05-14 |
| YA-131 | Taiz | 2025-09-12 |
| YA-130 | Torod | 2026-10-10 |
| YA-62 | the PayPal, Stripe, WooPayments and Zid Pay Kuwait parts | 2026-10-10 |

No later part names the same ground as any of them:
- YA-131's other parts are at a store's service or at "place not stated", and they all read "accepted, by money transfer".
- No other part of YA-130 names Torod.

So no mark rests on a stale part. If the Sana'a and Taiz parts were stale, the Dakhm store's part of 2026-10-10 would still carry S01-VP-05's mark. No part these marks rest on is disputed, and none comes from a precision tie.

## Unchanged or with a partner

`carried unchanged` and `carried only with a partner` can both hold for one variant, and the first in the list wins.

- I gave `carried unchanged` in two situations:
  - the variant's condition is shown met and its role is held by the platform or by the merchant's own account (Zid's wallet, direct bank transfer, cheques, Zid's bank transfer);
  - the condition names the party, and Q2 meets it (WooCommerce, Inc.).
- I gave `carried only with a partner` when the variant puts a role with a party outside the platform and Stage 1 names a party that can take it:
  - "شركة الشحن" in S01-SA-090 and S01-SA-091, taken by Torod;
  - "مزود الخدمة مثل جيديا" in S01-SA-113, taken by SabaCard;
  - "البنك" whose terms apply in S01-ZD-075 (S01-V-269), taken by Kuraimi, through YA-131's Dakhm part.

A reviewer could read the carrier variants as unchanged instead. That would change S01-VP-02's and S01-VP-04's marks to `carried unchanged`, with the same variants.

## Marks that were hard to give

- **S01-VP-19 (S01-V-480).** The variant's own words give a 9-riyal fee "في حال كانت الحوالة داخل السعودية". The same statements (S01-ZD-058, S01-ZD-150) give 50 riyals for a transfer outside Saudi Arabia.
  - The brief's three sources of a condition don't include a variant's own words, and its conditions (S01-ZD-121, S01-ZD-122) are met on Q2.
  - S01-V-481 (Zid's automatic deduction from wallet deposits, S01-ZD-060) also qualifies unchanged. So the mark doesn't rest on the 9-riyal words, though the variant named would.
- **S01-VP-23 (S01-V-528), and S01-V-448 in S01-VP-18.**
  - The variant bars withdrawing wallet amounts in Omani, Emirati, Kuwaiti or Bahraini currency. Its condition is its own scope, "التجار خارج المملكة", which Q2 meets.
  - S01-ZD-121 sets the wallet of a merchant outside the Kingdom in Saudi riyals, except for merchants in those four states and Qatar.
- **S01-VP-02 and S01-VP-03: BitPay's "all merchants" (S01-BC-033).** It names no place, and Stage 1 has nothing on BitPay, so S01-V-042 and S01-V-067 stay unsettled. Read as met, S01-V-042 would make S01-VP-02 `carried unchanged`, and S01-V-067 would do the same for S01-VP-03.
- **S01-VP-03 (S01-V-059).** YK-161 names SabaCard as acquiring "local and international" cards, so YK-335 ("no longer used", international cards) doesn't remove the partner. Stage 1 says nothing about SoftPOS itself.
- **S01-VP-05 (S01-V-102) in YC-200, YC-201, YC-309 and YC-339.** YA-126 there gives no payments between banks, or almost none, where it states no place. The mark rests on YA-131, whose parts give payment into the seller's own account: the Dakhm store's Kuraimi accounts, and the seller's account in Sana'a and in Taiz. Those cases leave YA-131 as `YC-00` has it.
- **YC-155.** YA-62's PayPal part is "Available" (YE-E634, wise.com, no date), against YK-514 "cannot receive money" (YE-D997, no date). I read the PayPal conditions as unsettled there: neither met nor failed. No mark depends on them. In the unknown rows of that case, `what_would_show_it` adds evidence that settles PayPal's state.
- **S01-VP-13 (S01-V-244).** The variant names the contracting party, WooCommerce, Inc., which answers "who fills 'terms of service'". The mark says only that its condition, residence outside the Designated Countries, is met on Q2.
- **WooCommerce's Ecommerce Services (S01-V-494, S01-V-503).** The scope covers WooPayments, WooPay and the Payments feature. YA-62 gives a state only for WooPayments, so these variants stay unsettled rather than failing.

## What changed from the checkpoint, and why

The checkpoint marks had 10 `carried unchanged`, 1 `carried only with a partner` and 12 `unknown` at `YC-00`.

- **PayPal.** YA-62's PayPal part was "Available", which the independent review found to be a Stage 1 error. It now reads "Sending from Yemen", and YK-514 is new. So every PayPal variant fails at `YC-00`, and nine checkpoint marks named one. They changed as follows:
  - S01-VP-01: S01-V-026 to S01-V-024;
  - S01-VP-11: S01-V-182 to S01-V-194;
  - S01-VP-13: S01-V-626 to S01-V-244;
  - S01-VP-14: S01-V-630 to S01-V-579;
  - S01-VP-15: S01-V-348 to S01-V-343;
  - S01-VP-18: S01-V-595 to S01-V-445;
  - S01-VP-19: S01-V-650 to S01-V-480;
  - S01-VP-03: from `carried unchanged` (S01-V-048) to `carried only with a partner` (S01-V-059);
  - S01-VP-04: from `carried unchanged` (S01-V-084) to `carried only with a partner` (S01-V-093).
- **Q2's frame.** At the checkpoint, Stage 1 had no constant for the merchant's country, so no condition naming only places could be checked. With Q2:
  - Zid's wallet terms and S01-WC-012 are met. That gives S01-VP-09 (S01-V-160) and S01-VP-23 (S01-V-528) a carried mark where they had `unknown`, and it gives the wallet variants above.
  - Many conditions now fail on Q2 that were unsettled before. That changes no mark: every unknown variation point still has a variant whose failure can't be shown.
- **Unchanged from the checkpoint:**
  - S01-VP-02 (S01-V-038) and S01-VP-05 (S01-V-102);
  - the unknown marks of S01-VP-06, 07, 08, 10, 12, 16, 17, 20, 21 and 22.

## Problems with the method

- **No placement is out of reach.**
  - 22 of the 23 variation points have at least one answer variant with no stated condition, so no failure can be shown for them.
  - In S01-VP-10 every other variant fails, but S01-V-550 (صندوق سلة, S01-SA-187) rests on a programme that Stage 1 doesn't cover.

  So no case can have a `no placement` mark, and every variation point without a carried variant is `unknown`.
- **The frame settles places only.** A condition that mixes a place with other requirements fails on its place (S01-BC-067's plan and location). A condition that requires an account or document tied to a country (S01-SA-074), or names no place at all (S01-BC-033), stays unsettled. Readings of this kind decide two variants (see S01-BC-033 above).
- **A variant's own words can name a place that isn't its condition** (S01-V-480). The brief's three sources leave such words out.
- **Cases that change an axis without touching a mark's evidence.** All 99 rows outside `YC-00` carry `YC-00`'s marks. Every axis that a bears-on row lists bears on some condition, but in these cases the changed parts are not the ones the marks rest on.
- **Moves.** YA-62's WooPayments part, "Not available, a request to add it open" (YE-E641, YE-E642, YE-E645), comes from a feature request on WooCommerce's site. A feature request is not a consultation, partnership, licence or regulator's action, so `moves` is empty. YA-28's general licences are licences, but no mark rests on S01-SH-047, so they change no mark. No other cited evidence names a move that would change a mark.
