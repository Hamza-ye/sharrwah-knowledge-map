# S-01 phase D: notes

Status: redone on two updated inputs:
- Stage 1 as rebuilt at `4e3f3dd` (228 axes, 515 constants, 345 cases);
- `variants.tsv` after phase B's re-check (613 variants).

Then followed up after phase B placed Salla's statements on agent (commit `4fff36c`). S01-VP-03, 04, 06, 11, 13 and 19 were re-marked; see the last section. The other variation points' rows are as they were.

`bears-on.tsv` has the 23 variation points. `yemen-marks.tsv` has 183 rows in 30 cases: `YC-00` and every case whose `name` lists an axis that a variation point bears on. The other 29 cases are `YC-120` to `YC-123`, `YC-156`, `YC-164`, `YC-191` to `YC-194`, `YC-196` to `YC-205`, `YC-294`, `YC-299`, `YC-310`, `YC-311`, `YC-329`, `YC-338`, `YC-341`, `YC-343` and `YC-344`.

The checker reports no errors, both after the redo (`s01-check-d2`) and after the follow-up (`s01-check-d3`). Its one review line is about `variants.tsv`, phase B's file.

## The marks

| Mark | `YC-00` | All 183 rows |
| --- | --- | --- |
| carried unchanged | 9 | 90 |
| carried with configuration | 0 | 0 |
| carried only with a partner | 3 | 35 |
| no placement | 1 | 6 |
| unknown | 10 | 52 |

- **Carried unchanged at `YC-00`:**
  - Six rest on Zid's wallet terms for merchants outside the Kingdom (S01-ZD-121, S01-ZD-122), checked against Q2's frame:
    - S01-VP-09 (S01-V-160);
    - S01-VP-14 (S01-V-579);
    - S01-VP-15 (S01-V-343);
    - S01-VP-18 (S01-V-445);
    - S01-VP-19 (S01-V-480);
    - S01-VP-23 (S01-V-528).

    These marks show only that the wallet's own conditions are met. They don't show that a buyer's payment reaches the wallet for a merchant outside the Kingdom (review finding 8; each row says so).
  - S01-VP-13 (S01-V-244) rests on WooCommerce, Inc. as the party for residents outside the Designated Countries (S01-WC-012, S01-WC-014), checked against Q2's frame.
  - S01-VP-05 (S01-V-102, direct bank transfer) and S01-VP-11 (S01-V-195, Zid's bank transfer, the merchant as account owner) rest on YA-131.
- **Carried only with a partner:**
  - S01-VP-02 (S01-V-038): a carrier outside Salla's shipping labels. S01-VP-04 (S01-V-091): the shipping company, or the store's delegate, collects cash on delivery. In both, the partner is Torod, on YK-203.
  - S01-VP-03 (S01-V-059): SoftPOS through a card service provider. The partner is SabaCard, on YK-161.
- **No placement:** S01-VP-10, in all six of its cases. See the next section.
- **Unknown:** S01-VP-01, 06, 07, 08, 12, 16, 17, 20, 21 and 22.
- **The other cases carry `YC-00`'s marks.** In none of the 160 rows outside `YC-00` does a variant's status differ from `YC-00`'s.
- **Moves:** none (see the last section).

## No placement: S01-VP-10 ("security interest")

Every answer variant fails:

| Variant | What it is | Fails on |
| --- | --- | --- |
| S01-V-167 | Shopify Payments' first-priority lien (S01-SH-023) | Q2: Shopify Payments is for a business located in its Designated Country (S01-SH-041, S01-SH-095, S01-SH-096, S01-SH-147 and others), and none of them takes in the Yemeni market |
| S01-V-168, S01-V-169, S01-V-549 | Stripe's (S01-SH-135, S01-WC-112, S01-WC-132) | Q2, since their regions are the United States and Singapore; and YA-62, "Unavailable @ Stripe's service" |

S01-SH-047 (sanctions) also conditions S01-V-167 and stays unsettled. It decides nothing, because the place conditions on the same statement fail.

- **Product gap:** "Where neither Shopify Payments nor Stripe is offered, no reference places a security interest over the merchant's funds held between the buyer's payment and the payout: every reference's lien or security interest belongs to one of those two services."
- **Founder item:** "Who, if anyone, holds a security interest over the merchant's funds between the buyer's payment and the payout, where Shopify Payments and Stripe, which hold one in the references, are not offered."

The mark is the same in `YC-120` to `YC-123` and `YC-156`. Those cases change only YA-27, YA-28 and YA-62's PayPal part.

## How the conditions were read

- **Three sources, per statement.** Each statement of an answer variant was taken with two things:
  - the (e) statements whose `conditions` name it;
  - its own `scope`.

  A statement with neither has no condition. A variant counts as working when one of its statements has its conditions shown met. It counts as failing only when every statement has its conditions shown failed.
- **Alternatives within one statement.** S01-ZD-149 (Zid Egypt's Starter plan: "Basic payment methods (bank transfer, cash on delivery)") names S01-ZD-069 to S01-ZD-072 and S01-ZD-075. In each, other conditions place the same statement in Zid's own plans: S01-ZD-141 for bank transfer, and S01-ZD-123 to S01-ZD-128 and S01-ZD-142 for Zid Ship's cash on delivery. So S01-ZD-149 is taken as another market's placement, an alternative, not as a further condition.
  - My last marks did this only for S01-ZD-075. Applying it throughout makes nine Zid Ship variants unsettled rather than failing: S01-V-096, S01-V-097, S01-V-122, S01-V-319, S01-V-484, S01-V-485, S01-V-656, S01-V-658 and S01-V-659.
  - It changes no mark.
- **The nine (e) statements marked `none stated`.** None of their identifiers appears in a variant's statements, so none conditions a variant.
  - I read "identifier" as the statement's own key. For S01-SA-189 that is "countryOther.description"; phase A's gloss after it is "(منصة سلة; title: ...)".
  - Review finding 11 reads "منصة سلة" from that gloss as the identifier. I haven't followed it, because the same reading would make "BigCommerce Payments" (from S01-BC-031's identifier) condition 19 variants, and "المدفوعات" (from S01-ZD-134's and S01-ZD-135's breadcrumbs) condition 61.
  - Read the reviewer's way, S01-SA-189 ("منصة سلة متاحة حاليًا في السعودية والإمارات فقط") would fail S01-V-087, S01-V-109, S01-V-258, S01-V-275, S01-V-422, S01-V-495 and S01-V-504 on Q2, and leave S01-V-147 and S01-V-255 unsettled. No mark would change; I re-ran it to check.
  - The three partner marks name Salla variants, so their rows say that S01-SA-189 places Salla's platform in Saudi Arabia and the UAE, and that the mark is about the arrangement the variant names.
- **Q2's frame** (the coordinator's line in the brief). These conditions are checked against it and cited as `Q2`:
  - words that name only countries or regions (S01-ZD-112);
  - words that require the store, the business or its account to be in a named place (S01-BC-067; S01-ZD-133);
  - scopes that name only a place (S01-SA-052).

  An (e) statement whose scope names only a place is a condition placed there. Examples are S01-SA-059, S01-SA-064, S01-SA-162, S01-ZD-107, S01-ZD-108, S01-ZD-110, S01-ZD-117, S01-ZD-118 and S01-SH-045.

  How Q2 decides:
  - Met: a place that includes the Yemeni market. These are "خارج المملكة" (S01-ZD-121, S01-ZD-122) and "outside of the Designated Countries" (S01-WC-012 with S01-WC-014).
  - Also met: S01-WC-042, S01-SH-144 and S01-SH-146, which name only another place and restrict only merchants there.
  - Not met: every other place condition.
  - EMEA (S01-BC-055, S01-BC-057) meets the region but adds plans that Stage 1 has no evidence for. Its paths fail on S01-BC-029 anyway.
- **Not settled by the frame.** These conditions require something other than a place:
  - S01-SA-074: an Absher account, a Saudi bank account, a Saudi mobile number;
  - S01-BC-033: "all merchants", for BitPay;
  - S01-ZD-129 and S01-ZD-130: Mazeed;
  - S01-BC-035 and S01-BC-036: "more than 150 countries", none of them named.
- **PayPal.** YK-514, "cannot receive money" (PayPal's service, YE-D997), is a constant, so it holds in every case. Following review finding 10, every PayPal condition fails on it in `YC-156` too, although YA-62's PayPal part there reads "Available".
  - My last notes treated that case as unsettled, and claimed that `what_would_show_it` added PayPal evidence there. It didn't. Both are now gone.

## What each variation point bears on

Added after the review (findings 30 and 31, which I agree with):
- **S01-VP-03:** YA-122 (the card switch), YA-124 (card terminals) and YA-120 (active debit cards). They bear on SoftPOS card payment at Salla Point's cashier (S01-SA-113), beside YK-161 and YK-335.
- **YA-125** (the instant payment system), beside YA-126. It bears on the conditions of payment into the merchant's own account, in S01-VP-05, 11 and 13.
- **YA-27, YA-28 and the sanctions constants** (YK-22, YK-23, YK-24, YK-392). These now also bear on Zid Pay's prohibited-activity conditions:
  - S01-ZD-110;
  - S01-ZD-111, which lists "اليمن" among "البلدان الخاضعة للعقوبات الدولية".

  So they appear in S01-VP-03, 09, 14, 16, 19, 20 and 21 as well.
- **The crypto constants** YK-127, YK-350, YK-352, YK-353 and YK-354. They bear on BitPay's "all merchants" (S01-BC-033) and Shopify's crypto payments "if eligible" (S01-SH-015), in S01-VP-02, 03 and 05. They don't settle either condition.

Other changes:
- **YA-130** stays, for its sellers' cash-on-delivery parts. Its Torod part, "on pickup, on delivery, or by Jaib, Jawali, Floosak or Kuraimi wallet", is about Torod's own charges, so the carrier marks no longer cite it (review finding 7). They rest on YK-203, whose quote is the courier collecting money from recipients (YE-E613).
- **Quoted labels** are those at `4e3f3dd`, including YA-129's relabelled states.
- **YK-206** (a carrier's app linked to a store):
  - It left S01-VP-06, 08, 09 and 18 with the carrier-app variants that phase B removed.
  - It came into S01-VP-19, where S01-V-601 now cites the carrier app (S01-SA-125, S01-SA-126).
- **New or changed Stage 1 items that bear on no variant's condition:**
  - YK-515 (what a payment service provider licence requires);
  - YA-102, YA-105, YA-106 and YA-44.

  No condition names a licence, an e-money model or a central bank in the merchant's market.

The independent reviewer's earlier items stand as before:

| Item | In or out |
| --- | --- |
| YK-514, YK-335, YA-68, YA-129, YA-28, YK-392 | in |
| YA-107, YK-61, YK-370, YK-513 | out |

The reasons:
- YA-107 is about online gateways, while the one card condition that names no provider is SoftPOS at a point of sale.
- No variant's condition names a transfer from abroad (YK-61) or a bank in Yemen (YK-370).
- No variant's condition names Wise (YK-513).

## Stale and disputed parts

I read each part's date in the axis `note` column for every axis these rows list.

The parts the marks rest on are:

| Axis | Part | Date |
| --- | --- | --- |
| YA-131 | the Dakhm store's part | 2026-10-10 |
| YA-131 | Sana'a | 2025-05-14 |
| YA-131 | Taiz | 2025-09-12 |
| YA-62 | the Stripe part (S01-VP-10's failure) | 2026-10-10 |
| YA-62 | the PayPal, WooPayments and Zid Pay Kuwait parts | 2026-10-10 |

No later part names the same ground as any of them, so no mark rests on a stale part.

YA-122's "not operating @ place not stated" (2026-02) and SabaCard's part (2026-10-10) name different ground, and the partner mark rests on YK-161. No part these marks rest on is disputed or comes from a precision tie.

## Unchanged or with a partner

`carried unchanged` and `carried only with a partner` can both hold for one variant, and the first in the list wins.

- I gave `carried unchanged` in two situations:
  - the variant's condition is shown met and its role is held by the platform or the merchant's own account (Zid's wallet, direct bank transfer, cheques, Zid's bank transfer);
  - the condition names the party and Q2 meets it (WooCommerce, Inc.).
- I gave `carried only with a partner` when the variant puts a role with a party outside the platform and Stage 1 names one that can take it:
  - "شركة الشحن" in S01-SA-090 and S01-SA-091, and the store's delegates in S01-SA-198 ("مندوب محلي أو شركة شحن خارجية غير مرتبطة مباشرة بسلة"), taken by Torod;
  - "مزود الخدمة مثل جيديا" in S01-SA-113, taken by SabaCard;
  - "البنك" in S01-ZD-075 (S01-V-269), taken by Kuraimi.

## Marks that were hard to give

- **S01-VP-05 (S01-V-102), review finding 9.** I kept `carried unchanged`.
  - YA-131 shows sellers taking payment into their own accounts: the Dakhm store's Kuraimi accounts, and in advance to the seller's account in Sana'a and in Taiz. That is the variant as WooCommerce places it, and it is the first mark in the list.
  - YA-126 ("none, only cash, cheques or within one institution" in government-controlled areas) and YA-125 bear on which buyers can pay. The row says the mark doesn't claim every buyer can.
  - The configuration reading, an account at the buyer's institution, would apply only if the unchanged mark didn't hold.
  - The row also says that S01-V-105, listed as qualifying, names WooPayments only to say it has no part.
- **S01-VP-11 (S01-V-195).** S01-V-194, the wallet's IBAN, was removed, so the mark now rests on Zid's bank transfer with YA-131, read as in S01-VP-05.
- **S01-VP-01.** S01-V-024 was removed, and the two wallet holders that phase B added stay unsettled:
  - S01-V-656 (Zid Ship pays into the wallet) rests on Zid Ship's conditions, which Stage 1 doesn't cover. S01-ZD-126 gives cash on delivery as "غير متاح" for international shipping.
  - S01-V-657 (Salla) states no condition.
- **S01-VP-19 (S01-V-480).** The variant's words give a 9-riyal fee "في حال كانت الحوالة داخل السعودية". The same statements give 50 riyals for a transfer outside Saudi Arabia. Its conditions are met on Q2, and S01-V-481 also qualifies.
- **S01-VP-23 (S01-V-528) and S01-V-448.** The variant bars withdrawing Gulf currencies, under its own scope, "التجار خارج المملكة". S01-ZD-121 sets the wallet of a merchant outside the Kingdom in Saudi riyals, except for merchants in the Gulf states.
- **S01-VP-02 and S01-VP-03: BitPay's "all merchants" (S01-BC-033).**
  - It names no place, and the crypto constants don't settle it.
  - Read as met, S01-V-042 would make S01-VP-02 `carried unchanged`, and S01-V-067 would do the same for S01-VP-03.
- **S01-VP-03 (S01-V-059).**
  - YK-161 names SabaCard acquiring "local and international" cards. So YK-335 ("no longer used", international cards) doesn't remove the partner, and neither do the YA-122, YA-124 and YA-120 parts.
  - Stage 1 says nothing about SoftPOS itself.
- **WooCommerce's Ecommerce Services (S01-V-494, S01-V-503).** YA-62 gives a state only for WooPayments, so these variants stay unsettled.

## What changed from the last marks, and why

**The inputs changed.**
- Phase B removed 46 variants, among them S01-V-024, S01-V-194 and S01-V-550, and added six. The answer sets changed in S01-VP-01, 02, 03, 06, 08, 09, 10, 11, 13, 14, 15, 16, 18, 19 and 23.
- Stage 1 renumbered the cases: the PayPal case `YC-155` is now `YC-156`.

**The marks at `YC-00` that changed:**

| VP | Last marks | Now | Why |
| --- | --- | --- | --- |
| S01-VP-01 | `carried unchanged` (S01-V-024) | `unknown` | S01-V-024 was removed, and no remaining variant is shown to work |
| S01-VP-10 | `unknown` | `no placement` | S01-V-550 was removed, and every remaining variant fails |
| S01-VP-11 | S01-V-194 | S01-V-195 | S01-V-194 was removed |

The other 20 marks are unchanged.

**The rows went from 122 to 183**, for two reasons:
- bears-on gained YA-120, YA-122, YA-124 and YA-125, and gained YA-27 and YA-28 in seven more variation points;
- YA-129, relabelled, now has three cases instead of one.

**The review's findings:**
- Applied: 7, 8, 10, 30 and 31.
- Partly applied: 9 and 11. I changed the notes, not the marks, for the reasons above.

## Problems with the method

- **No placement needs every answer variant to carry a condition.** Only S01-VP-10 has no variant with no stated condition. In the other 22 variation points, such variants block `no placement`.
- **The frame settles places only.**
  - A condition that mixes a place with other requirements fails on its place (S01-BC-067).
  - A condition that requires an account or a document tied to a country (S01-SA-074), or names no place (S01-BC-033), stays unsettled.
  - Readings of this kind decide two variants.
- **A variant's own words can name a place that isn't its condition** (S01-V-480). The brief's three sources leave such words out.
- **A rule built on an identifier depends on what counts as the identifier** (S01-SA-189).
- **Cases that change an axis without touching a mark's evidence.** All 160 rows outside `YC-00` carry `YC-00`'s marks.
- **Moves.** None of the cited evidence names a move that would change a mark:
  - YA-62's WooPayments part, "a request to add it open" (YE-E641, YE-E642, YE-E645), is a feature request on WooCommerce's site. That is not a consultation, partnership, licence or regulator's action.
  - YA-28's general licences are licences, but no mark rests on S01-SH-047 or on Zid Pay's prohibited-activity conditions.

## Follow-up: Salla's statements on agent (commit `4fff36c`)

**What changed in the inputs.** Phase B placed Salla's new statements:
- S01-VP-06 gained an answer, S01-V-660: a charity connects its own gateway account and authorises Salla to use it (S01-SA-195). The (e) statement S01-SA-072 conditions S01-SA-195: charities can't use Salla's gateway and must connect an outside one, "pay tabs".
- S01-V-655 became a gap (S01-SA-G07).
- Seven rows gained statements:
  - S01-V-055 (S01-SA-202);
  - S01-V-085 (S01-SA-195, S01-SA-202);
  - S01-V-091 (S01-SA-198);
  - S01-V-187 (S01-SA-195);
  - S01-V-256 (S01-SA-202);
  - S01-V-475 (S01-SA-200);
  - S01-V-601 (S01-SA-190 to S01-SA-192).

**How the new conditions were read.**

| Condition | Read as | Why |
| --- | --- | --- |
| S01-SA-202's scope, "السعودية" (a salla.com guide to starting e-commerce in Saudi Arabia) | not met on Q2 | it names only a place |
| S01-SA-198's scope, "مناديب المتجر: مندوب محلي أو شركة شحن خارجية غير مرتبطة مباشرة بسلة" | the same as the carrier scope of S01-SA-090 and S01-SA-091 | it is the store's delegates, a local one or an outside shipping company. YK-203 shows Torod collecting money from recipients for business accounts, a party that can take that role |
| S01-SA-190's scope, "{{carrier}} app" | a carrier's app, with YK-206 | it is Salla's English for "تطبيق {{carrier}}" |
| S01-SA-195 and S01-SA-072 (charities), S01-SA-200 ("صندوق سلة") | bearing on no Stage 1 axis or constant | Q2's frame does not settle them |

For S01-SA-198: YA-128 gives online sellers in Yemen taking cash on delivery, but not who collects it. So it doesn't show the merchant's own delegate taking the role, and the mark is the partner one.

**`bears-on.tsv`.** The rows of the six variation points now quote the new conditions. No row gained an axis or a constant, so the cases to mark are the same.

**What I revisited.** I re-marked S01-VP-03, 04, 06, 11, 13 and 19 in every case their rows cover: 13, 11, 6, 19, 24 and 6 cases. No other row changed.

**What changed.**

| VP | Rows | Change | Why |
| --- | --- | --- | --- |
| S01-VP-04 | all 11 | the named variant changes from S01-V-093 to S01-V-091; the mark stays `carried only with a partner` | S01-V-091 now holds with a partner through S01-SA-198, with YK-203, and it is the lower id |
| S01-VP-06 | all 6 | mark unchanged (`unknown`); the note and `what_would_show_it` now name S01-V-660 | S01-V-660 rests on the charity conditions, which Stage 1 doesn't settle |
| S01-VP-19 | all 6 | mark unchanged; the note's list of lower variants now gives S01-SA-200 for S01-V-475 | S01-V-475 gained a statement |
| S01-VP-03, 11 and 13 | all | rows unchanged | their marks don't change: S01-V-055 and S01-V-256 gain a statement that fails on Q2 but keep ones with no stated condition, and S01-V-187 stays unsettled |

