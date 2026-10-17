# S-01 phase B notes

First pass. Phase A2 has not run, so no `a2.tsv` was read and no row was revisited.

Read: this brief; the five platforms' `statements.tsv`, `terms.tsv`, `absences.tsv` and `gaps.tsv`; `kinds.tsv`. No `notes.md` file and no `note` column was read. `citations.tsv` was not needed.

Result: 23 variation points, 10 under (a), 3 under (b) and 10 under (c), within rule 7's limit of 25. There are 531 variant rows: 491 answers, 2 `absent`, 28 `gap` and 10 `not covered`. `method/check_subject.py` reports no issue.

## Merges

None. No two variation points under the same bullet are answered by exactly the same statements.

## Partial overlaps that were split

- **S01-VP-01 "holds the funds" and S01-VP-08 "withhold".** "Hold" is used both for having the funds (S01-SH-099, "Global-e holds the funds"; S01-WC-116, "funds Stripe holds for User") and for holding them back (S01-SH-126, "withhold Settlement"; S01-SH-086, "place a hold on your payout account"). S01-SH-022, S01-SH-033 and S01-SH-034 use "hold funds" while awaiting information, pending resolution or under Legal Process; they are under both.
- **S01-VP-01 "holds the funds" and S01-VP-07 "Reserve".** A Reserve is funds held (S01-SH-133, "collateral funds which Stripe holds and controls"). Statements about reserves name who sets, applies or controls them, which S01-VP-01 does not ask, so they are under S01-VP-07 only.
- **S01-VP-02 "settlement of funds" and S01-VP-03 "payouts".** Both are about funds moving to the merchant. Shopify names a different party for each: S01-SH-019 ("The Payment Processor retains sole and exclusive responsibility for Payment Processing, including the settlement of funds") and S01-SH-075 ("your payouts are sent from Shopify, they're processed by these partners"). Statements whose words are "settle", "settlement" or "تسوية" went under S01-VP-02. Statements whose words are "payout", "deposit", "pay you", or "تحويل" to the merchant went under S01-VP-03. S01-BC-021 ("settles directly to your bank account") is under both.
- **S01-VP-04 "collect payment" and S01-VP-05 "pay you directly".** Both name who first receives the buyer's payment. Statements saying the payment goes "directly" ("مباشرة") from the buyer to the merchant's own account went under S01-VP-05 (S01-WC-093, "lets your customers pay you directly via their bank account"). Statements naming a party that collects or processes the payment went under S01-VP-04.
- **S01-VP-11 "account", S01-VP-12 "licensed" and S01-VP-13 "terms of service".** These follow the three nouns of bullet (b). S01-SH-003, S01-SH-004, S01-SH-108 and S01-SH-109 name both a Payment Facilitator or Acquirer and the terms that apply; they are under S01-VP-12 and S01-VP-13.
- **S01-VP-14 "payout schedule", S01-VP-15 "payout timing" and S01-VP-16 "Minimum payout amount".** All three are about when funds are released. Shopify's `terms.tsv` defines "payout schedule" ("Your payout schedule determines when funds from sales are transferred to your bank account") and "payout timing" ("Shopify Payments payout timing determines when funds from your sales are available in your bank account") separately. S01-SH-067 gives the minimum payout amount in its own column. The statements were split as follows:
  - how often, or on which days, funds are sent: S01-VP-14;
  - how long until funds are available (settlement time, pending period, waiting period, bank processing time): S01-VP-15;
  - an amount threshold: S01-VP-16.

  S01-SH-067, S01-WC-044, S01-SA-051, S01-SA-061, S01-ZD-040 and S01-ZD-085 are under more than one.
- **S01-VP-18 "held", S01-VP-20 "Termination" and S01-VP-21 "refunded to your customers".** Conditions for holding funds went under S01-VP-18, the closing or termination of an account under S01-VP-20, and the return of funds to buyers under S01-VP-21. These statements are under more than one:
  - S01-WC-010, S01-SA-082, S01-ZD-021, S01-ZD-022 and S01-ZD-024: S01-VP-20 and S01-VP-21;
  - S01-ZD-014 and S01-ZD-015: S01-VP-18 and S01-VP-21.
- **S01-VP-18 "held" and S01-VP-23 "currency".** S01-SA-060 and S01-SA-065 (a payout account at an Emirati or Kuwaiti bank, in the local currency) are under both. S01-VP-23 was raised by S01-WC-048, S01-WC-049 and S01-WC-050, which share the identifier "Payout currencies" and match no other (c) variation point.

## `not covered` rows

These go back to the platform for phase A2: bigcommerce 6, salla 3, zid 1, shopify 0, woocommerce 0.

| Variant | Variation point | Platform |
| --- | --- | --- |
| S01-V-101 | S01-VP-04 "collect payment" | bigcommerce |
| S01-V-111 | S01-VP-05 "pay you directly" | bigcommerce |
| S01-V-124 | S01-VP-06 "agent" | bigcommerce |
| S01-V-134 | S01-VP-07 "Reserve" | salla |
| S01-V-151 | S01-VP-08 "withhold" | bigcommerce |
| S01-V-166 | S01-VP-09 "deduct" | bigcommerce |
| S01-V-170 | S01-VP-10 "security interest" | salla |
| S01-V-171 | S01-VP-10 "security interest" | zid |
| S01-V-172 | S01-VP-10 "security interest" | bigcommerce |
| S01-V-394 | S01-VP-17 "reserve" | salla |

## Problems with the method

1. **Sameness across languages.** Rule 0 calls two things the same when they share words, a platform's own translation in `terms.tsv`, or a party or identifier. Many Salla and Zid statements name X in Arabic words that no `terms.tsv` translation links to the English X: "يحتفظ" in S01-SA-056, "احتجاز" in S01-ZD-016, "خصم" in S01-ZD-010. These are under their variation point on `answers` alone, with the Arabic words quoted in `basis_evidence`. The brief does not say whether `answers` may rest on words that rule 0 would not call the same.
2. **The `term` basis.** `term` is recorded when the words are the same, or linked by a platform's own translation, and no two `terms.tsv` definitions of that term differ. Shopify and WooCommerce define "payout(s)", "reserve" and "payout schedule" differently, so `term` is not recorded between them. Those WooCommerce rows were instead compared with a WooCommerce statement in `raised_by` that uses the same term. The brief does not say whether comparing with a `raised_by` statement of the same platform is intended. Two defined Shopify terms with different definitions, such as "Reserve Account" and the Help Center's "reserve", were not treated as the same term either.
3. **`not covered` and partial answers.** A platform gets a `not covered` row only when it has no row of any form. When a platform answers for one arrangement but not another, nothing records the arrangement left without an answer. In S01-VP-02, Salla's rows come from S01-SA-104 (تمارا) and S01-SA-091 (cash on delivery outside بوليصات سلة), and no Salla statement under (a) names who settles مدفوعات سلة funds. In S01-VP-03, BigCommerce's only row is BitPay (S01-BC-021).
4. **Whether a gap covers a variation point** is a judgement:
   - S01-BC-G01 asks who holds the funds. It was taken to cover S01-VP-01 and S01-VP-07 only, not who collects, acts as agent, withholds, deducts or holds a security interest. Those BigCommerce rows are `not covered`.
   - S01-BC-G02 was taken to cover the three (b) variation points.
   - S01-BC-G03 was taken to cover every (c) variation point, because it asks bullet (c) as a whole for BigCommerce Payments and providers other than PayPal.
   - Zid's (a) gaps S01-ZD-G05, S01-ZD-G06 and S01-ZD-G09 name SurePay, other gateways and Amazon. They were placed in S01-VP-01 to S01-VP-04 next to Zid's answers for other arrangements.
5. **Candidates that fit no variation point of their bullet.** Rule 1 gives a statement one candidate for each bullet it carries. Rule 2 does not say whether a candidate that matches no other forms a variation point alone. These statements carry a second bullet whose candidate matches no variation point of that bullet without forcing; each is under a variation point of its other bullet:
   - (a): S01-SH-009, S01-WC-010, S01-WC-051, S01-WC-054, S01-WC-126, S01-ZD-030, S01-ZD-070, S01-BC-017. Of these, S01-WC-126, S01-ZD-030 and S01-ZD-070 name no who.
   - (b): S01-SH-005, S01-SH-019, S01-SA-078, S01-WC-127, S01-WC-129.
6. **One statement under several variation points of a bullet.** Rule 1 speaks of one candidate per bullet, while rule 4 places a statement under every variation point where a basis holds. I followed rule 4. For example, S01-SH-022, S01-SH-033 and S01-SH-034 are under S01-VP-01 and S01-VP-08; S01-WC-115 is under S01-VP-01, S01-VP-02 and S01-VP-06.
7. **One statement giving several answers.** S01-SH-051 (a table), S01-SH-052, S01-SH-125, S01-WC-002 and S01-ZD-040 give more than one distinct answer to a variation point. Each answer has its own row with the same `stmt_ids`.
8. **Tables as excerpts.** For S01-SH-067, S01-SH-113, S01-SH-114, S01-WC-033, S01-WC-038, S01-WC-050 and S01-WC-107, the answers are spread across a table or list. The excerpt is the whole statement, or its opening clause for S01-WC-107, and `basis_evidence` quotes the cells.
9. **Fields with several statements.** The brief fixes no format for these:
   - When the statements of one row give different scopes, `scope` lists each scope followed by its `stmt_ids`; a statement with no scope adds nothing.
   - When their kinds differ, `kind` lists each kind once, in the order of `stmt_ids`.
   - `raised_by` lists every statement that carries the variation point's bullet and is placed in it as an answer. It leaves out statements under bullet (d) only, which are placed by the (d) rule.
   - `x_words` separates platforms with " | ".
10. **Bullet (d) statements that name no X.** These were placed under the variation point that asks about the arrangement they disclaim:
    - S01-SA-088, S01-WC-005, S01-WC-006, S01-WC-008 and S01-WC-009 (no part in the transaction between merchant and buyer): S01-VP-13;
    - S01-SA-083 (no responsibility for late performance by payment gateways or banks): S01-VP-18;
    - S01-BC-014 and S01-BC-017 (conversion fee and rate outside BigCommerce's scope): S01-VP-19 and S01-VP-23.
11. **Statements placed as "reason".** S01-SH-071, S01-SH-079, S01-WC-062, S01-WC-076 and S01-ZD-067 give no time or condition of their own. Each is in the row of the statement it accompanies, except S01-WC-062, which has its own row.

# Second pass, after phases A2 and A3

Read, in addition to the first pass: each platform's `a2.tsv` and `absence-audit.tsv` (without its `note` column), the statements, terms and gaps that phases A2 and A3 added, and the brief as it now reads. No variation point was added, split or merged.

Before this pass there were 531 rows: 491 answers, 2 `absent`, 28 `gap` and 10 `not covered`.

As the coordinator asked, BigCommerce statements were placed only up to S01-BC-065. A re-run of BigCommerce's phase A2 was rewriting its files during this pass. Its statements from S01-BC-066 onward, and any change to its `a2.tsv`, are left for a follow-up; the BigCommerce `a2.tsv` read here is the one dated 13 October. The follow-up is the last section of these notes.

Format changes applied to every row:
- `scope`: when the statements of a row give different scopes, each scope is now followed by its `stmt_ids`, and the scopes are `;`-separated (rule 5). A statement with no scope still adds nothing.

## What changed, by variation point

### S01-VP-01 "holds the funds"

- **Changed form:** S01-V-027 (bigcommerce) changed from `gap` (S01-BC-G01) to an answer from S01-BC-051 and S01-BC-055: "all transactions made through BigCommerce Payments flow through your new BigCommerce Payments account". The new row S01-V-532 is a `gap` row with A2's S01-BC-G04, which asks who holds the funds.
- **Gap and absent rows kept:**
  - S01-V-025 (zid) stays `gap`, now with A2's S01-ZD-G10, S01-ZD-G11 and S01-ZD-G12.
  - S01-V-022 (salla) stays `absent`; the audit confirms S01-SA-N01.
- **New statements placed:**
  - S01-SA-144 joins S01-V-016.
  - S01-WC-132 and S01-WC-148 join S01-V-009 (Stripe).
  - S01-WC-143 is S01-V-013 ("pooled merchant funds accounts").
- **S01-WC-129 left this variation point.** Its only basis was a reference to the section of S01-WC-120, on its own platform. Compared with another platform's statement, no basis holds. Its row, S01-V-013, now holds S01-WC-143.
- **Rechecked against another platform** (first compared within their own platform, or with no statement named): S01-V-001 to S01-V-007, S01-V-010, S01-V-011, S01-V-015, S01-V-016, S01-V-017, S01-V-020 and S01-V-026.
  - S01-V-011 lost `identifiers`, which it shared only with S01-WC-122.
  - S01-V-016 and S01-V-017 lost `term`, which they shared only with Salla statements.
- **Translations:** the Arabic rows S01-V-016 to S01-V-019, S01-V-021, S01-V-023 and S01-V-024 now mark the translations that `answers` rests on as mine.
- **Not placed:** these A2 statements do not say who or what holds the funds:
  - S01-SA-148 and S01-SA-157: tracking of electronic payments in the wallet is "قادم قريبًا";
  - S01-SA-149: tracking of cash on delivery amounts is through the shipping company;
  - S01-BC-058: funds are "managed within a dedicated balance dashboard".

### S01-VP-02 "settlement of funds"

- **Gap rows:**
  - S01-V-040 (zid) stays `gap`, now with A2's S01-ZD-G10, S01-ZD-G11 and S01-ZD-G12.
  - S01-V-534 (salla) is a new `gap` row with S01-SA-G03, which A2 gave this variation point. The audit finds S01-SA-G03 partly contradicted by S01-SA-139.
- **New statements placed:**
  - S01-SA-139 is the new row S01-V-533 ("settling transactions").
  - S01-WC-142 and S01-WC-145 (Network International, "responsible for disbursement of User’s Settlement Funds") replace S01-WC-129 in S01-V-036, for the reason given under S01-VP-01.
- **Not placed:** A2 also listed S01-SA-134 to S01-SA-138 for this variation point. None of them carries bullet (a) with a "تسوية" or "settle" answer:
  - S01-SA-134 is under S01-VP-03 and S01-VP-14;
  - S01-SA-135 is under S01-VP-18;
  - S01-SA-137 is under S01-VP-13 and S01-VP-14;
  - S01-SA-138 is under S01-VP-15;
  - S01-SA-136 carries only the payout end.
- **Gap not used:** A2 also gave S01-SA-G01 for this variation point. It is a bullet (b) gap, so it cannot cover this (a) variation point. It is used under S01-VP-11 to S01-VP-13.
- **Rechecked against another platform:** S01-V-028 to S01-V-032, S01-V-035 and S01-V-043. S01-V-043 lost `term`: BigCommerce's "Settlement Currency" and Shopify's "Settlement" have different definitions in `terms.tsv`.
- **Translations:** S01-V-039 now marks its translation as mine.

### S01-VP-03 "payouts"

- **Gap rows:**
  - S01-V-066 (zid) stays `gap`, now with A2's S01-ZD-G10, S01-ZD-G11 and S01-ZD-G12.
  - S01-V-537 (bigcommerce) is a new `gap` row with A2's S01-BC-G05, which asks who sends payouts for arrangements other than BitPay. The statements A2 gave with it (S01-BC-040, S01-BC-042, S01-BC-045, S01-BC-052, S01-BC-053 and S01-BC-056) carry only the payout end, not bullets (a) to (d), so they cannot be variants.
- **New statements placed:**
  - S01-SA-134 joins S01-V-055 (سلة).
  - S01-WC-150 is S01-V-535 (JCB transactions in Japan).
  - S01-WC-158, a bullet (d) statement, is S01-V-536: WooCommerce is "unable to assist with Stripe account issues (including ... payouts".
- **Not placed:** A2 gave S01-SA-150, S01-SA-158 and S01-SA-168 for Salla. They carry only the payout end, so they cannot be variants.
- **Rechecked against another platform:** S01-V-044 to S01-V-054, S01-V-060 and S01-V-067.
  - Shopify, WooCommerce and Salla define "payout(s)" differently in `terms.tsv`. Rows that had `term` on "payout" between them, or within one platform, now have `answers` only.
  - S01-V-060 lost `identifiers`, which it shared only between two Zid statements.
- **Translations:** the Arabic rows S01-V-055 to S01-V-065 now mark the translations that `answers` rests on as mine.

### S01-VP-04 "collect payment"

- **Changed form:** S01-V-101 (bigcommerce) changed from `not covered` to an answer from S01-BC-051 and S01-BC-055: "PayPal powers the payment processing behind the scenes through your linked PayPal account". The new row S01-V-542 is a `gap` row with A2's S01-BC-G06, for arrangements other than BigCommerce Payments.
- **Gap rows:** S01-V-100 (zid) stays `gap`, now with A2's S01-ZD-G10, S01-ZD-G11 and S01-ZD-G12.
- **New statements placed:**
  - S01-ZD-146 and S01-ZD-147, which A2 gave this variation point, are S01-V-540 and S01-V-541.
  - S01-SH-151 (PayPal) and S01-SH-152 (Adyen) are S01-V-538 and S01-V-539.
  - S01-SA-139 joins S01-V-085 (سلة).
- **Not placed:** S01-BC-044, which A2 also gave this variation point, carries bullet (b) only. It is under the (b) variation points.
- **S01-SA-057 left S01-V-091, and S01-SA-149 was not placed.**
  - Their words, "تابع المبالغ من خلال شركة الشحن" (my translation: "follow the amounts through the shipping company"), say where to track the amounts. They do not say who collects them.
  - The first pass had placed S01-SA-057 beside S01-SA-097, on its own platform. Compared with "to collect payment" (S01-WC-002), no basis holds.
  - S01-SA-149 is the same text for Kuwait.
- **Rechecked against another platform:** S01-V-069 to S01-V-084.
  - The Payment Processor List rows (S01-V-073 to S01-V-080) lost `identifiers`, which they shared only with S01-SH-005.
  - S01-V-081 and S01-V-082 had been compared only with the statement X is quoted from.
- **Translations:** the Arabic rows S01-V-085 to S01-V-099 now mark the translations that `answers` rests on as mine.

### S01-VP-05 "pay you directly"

- **Changed form:** S01-V-111 (bigcommerce) changed from `not covered` to `gap`, with A2's S01-BC-G07 (offline payment methods).
- **New statements:** none placed.
- **Rechecked against another platform:** S01-V-102 (X is quoted from it), S01-V-103, S01-V-104, S01-V-105 and S01-V-107.
- **Translations:** S01-V-108 to S01-V-110 now mark the translations that `answers` rests on as mine.

### S01-VP-06 "agent"

- **Changed form:** S01-V-124 (bigcommerce) changed from `not covered` to `gap`, with A2's S01-BC-G08.
- **New statements placed:**
  - S01-WC-132, S01-WC-142 and S01-WC-148 join S01-V-117 (Stripe).
  - S01-WC-150 is S01-V-543 ("当社", for JCB transactions in Japan).
- **Rechecked against another platform:** S01-V-112 to S01-V-115, which had been compared with Shopify statements only.
- **Translations:** S01-V-122 and S01-V-123 now mark the translations that `answers` rests on as mine.

### S01-VP-07 "Reserve"

- **Changed form:** S01-V-134 (salla) changed from `not covered` to `gap`, with A2's S01-SA-G04. Salla's pages were searched for a reserve and none was found; the audit confirms the gap.
- **Gap rows:** S01-V-135 (bigcommerce) stays `gap`, now with A2's S01-BC-G09 in place of S01-BC-G01.
- **New statements placed:**
  - S01-WC-145 is S01-V-544 (Network International).
  - S01-SH-149 is S01-V-545 ("Shopify and/or the Acquirer may debit your Payout Account or Reserve").
- **Rechecked against another platform:** S01-V-125 (X is quoted from it), S01-V-126 to S01-V-129 and S01-V-133.
  - S01-V-126 and S01-V-129 lost `term`. They had compared "Reserve Account" with another Shopify statement, and WooCommerce defines "Reserve Account" differently.
  - S01-V-127 lost `term`, for the same reason.
- **Translations:** S01-V-133 now marks its translation as mine.

### S01-VP-08 "withhold"

- **Changed form:** S01-V-151 (bigcommerce) changed from `not covered` to `gap`, with A2's S01-BC-G10.
- **New statements placed:** S01-SA-181 and S01-SA-180 are S01-V-546 ("held by the issuing bank due to disputes"). The audit lists them against S01-SA-G01; they carry bullets (a) and (c).
- **Rechecked against another platform:** S01-V-136 to S01-V-140, S01-V-142 and S01-V-149.
  - S01-V-137 to S01-V-140 name "hold", not "withhold". They stay on `answers`, and the difference in words is recorded.
- **Translations:** the Arabic rows S01-V-144 to S01-V-148 and S01-V-150 now mark the translations that `answers` rests on as mine.

### S01-VP-09 "deduct"

- **Changed form:** S01-V-166 (bigcommerce) changed from `not covered` to `gap`, with A2's S01-BC-G11.
- **New statements placed:**
  - S01-SH-149 is S01-V-547 ("Shopify and/or the Acquirer may debit").
  - S01-WC-150 is S01-V-548 ("当社", JCB).
  - S01-ZD-152 joins S01-V-158 (زد باي and the service providers).
- **Rechecked against another platform:** S01-V-152 (X is quoted from it), S01-V-153, S01-V-154 and S01-V-156.
- **Translations:** the Arabic rows S01-V-157 to S01-V-165 now mark the translations that `answers` rests on as mine.

### S01-VP-10 "security interest"

- **Changed form:**
  - S01-V-170 (salla): `not covered` to `gap`, with A2's S01-SA-G05. The audit finds S01-SA-G05 partly contradicted by S01-SA-187 and S01-SA-188, which concern صندوق سلة.
  - S01-V-171 (zid): `not covered` to `gap`, with A2's S01-ZD-G19.
  - S01-V-172 (bigcommerce): `not covered` to `gap`, with A2's S01-BC-G12.
- **New statements placed:**
  - S01-WC-132 is S01-V-549 (Stripe's lien, Singapore).
  - S01-SA-187 is S01-V-550: صندوق سلة is "بلا أوراق ولا ضمانات" (my translation: "without paperwork or collateral"). It names no holder.
- **Not placed:** S01-SA-188 carries bullet (c) only; see S01-VP-19.
- **Rechecked against another platform:** S01-V-167 (X is quoted from it) and S01-V-168.

### S01-VP-11 "account"

- **Changed form:** S01-V-205 (bigcommerce) changed from `gap` (S01-BC-G02) to an answer from S01-BC-051 and S01-BC-055: "you create a new BigCommerce Payments account". The audit finds S01-BC-G02 contradicted.
- **New rows for BigCommerce:**
  - S01-V-551: "your linked PayPal account";
  - S01-V-552: "your Stripe account", from S01-BC-061;
  - S01-V-553: "a PayPal Braintree account", from S01-BC-062;
  - S01-V-554: a `gap` row with A2's S01-BC-G13, for other providers.
- **Gap rows kept:**
  - S01-V-189 (salla) stays `gap` with S01-SA-G01, which the audit finds only partly contradicted. S01-SA-178 and S01-SA-179 are the new answer row S01-V-557 ("لحساب المتجر", Salla's translation "for the store's account").
  - S01-V-202 (zid) stays `gap`, now with A2's S01-ZD-G13 to S01-ZD-G16.
- **New statements placed:**
  - S01-WC-165 joins S01-V-180 ("a single Stripe Express account").
  - S01-WC-141 is S01-V-555: no account with Network International.
  - S01-WC-147 is S01-V-556: no account with SMCC.
- **Not placed here:** A2 gave these BigCommerce statements to this variation point, but none uses "account" words:
  - S01-BC-039, S01-BC-043 and S01-BC-044 ("payment relationship", "direct relationship with PayPal") are under S01-VP-13;
  - S01-BC-041 ("the merchant’s PayPal dashboard") and S01-BC-047 ("Each provider has its own application process") fit no variation point;
  - S01-BC-046, S01-BC-054 and S01-BC-057 carry bullet (e) only.
- **Rechecked against another platform:** S01-V-174, S01-V-178, S01-V-180 (X is quoted from it) and S01-V-181 to S01-V-184.
- **Translations:** the Arabic rows S01-V-185 to S01-V-188, S01-V-190 and S01-V-192 to S01-V-201 now mark the translations that `answers` rests on as mine.

### S01-VP-12 "licensed"

- **Gap rows** (none changed form):
  - S01-V-219 (woocommerce) stays `gap`, now with A2's S01-WC-G03, which the audit confirms: no licence by a regulator was found for Australia, Japan, New Zealand, Singapore or the United Arab Emirates.
  - S01-V-221 (salla) stays `gap` with S01-SA-G01.
  - S01-V-223 (zid) stays `gap`, now with S01-ZD-G13.
  - S01-V-224 (bigcommerce) stays `gap`, now with S01-BC-G14.
  - S01-V-211 (shopify) stays `absent`; the audit confirms S01-SH-N02.
- **New statements placed:** A2's statements name the acquirer, Payment Facilitator or Independent Sales Organization for each of those countries. They are new rows:
  - S01-V-558 to S01-V-560: S01-WC-134 to S01-WC-136;
  - S01-V-561 and S01-V-562: S01-WC-137 and S01-WC-138;
  - S01-V-563: S01-WC-133 and S01-WC-141;
  - S01-V-564: S01-WC-139;
  - S01-V-565: S01-WC-144.

  Their basis is `identifiers`, the same topic as S01-SH-108's "the Acquirer listed in the respective jurisdiction", and, for "Payment Facilitator" and "registered as", `term`. S01-SH-148 is S01-V-566.
- **Elsewhere:** A2's other statements for this variation point (S01-WC-130 to S01-WC-153) are under S01-VP-01, S01-VP-02, S01-VP-03, S01-VP-06, S01-VP-07, S01-VP-09, S01-VP-10, S01-VP-11, S01-VP-13 or S01-VP-17. S01-WC-146 carries bullet (e) only.
- **Rechecked against another platform:**
  - S01-V-206 (X is quoted from it);
  - S01-V-207 to S01-V-210, which had been compared with Shopify statements only. S01-V-209 lost `identifiers`, which it shared only with S01-SH-108.
  - S01-V-213, S01-V-214 and S01-V-216 to S01-V-218. These keep `answers`, and the difference in words is recorded.
- **Translations:** S01-V-220 and S01-V-222 now mark the translations that `answers` rests on as mine.

### S01-VP-13 "terms of service"

- **Changed form:** S01-V-272 (bigcommerce) changed from `gap` (S01-BC-G02) to an answer from S01-BC-039, S01-BC-043 and S01-BC-044: "the merchant’s payment relationship remains directly with PayPal".
  - A2 gave S01-BC-G15 for this variation point, and the audit finds it contradicted by S01-BC-062 to S01-BC-064, so no `gap` row was kept.
  - New BigCommerce rows: S01-V-567 ("the beta terms", S01-BC-059) and S01-V-568 ("a Pricing Contract", S01-BC-062).
- **Gap rows:**
  - S01-V-254 (salla) stays `gap` with S01-SA-G01, which A2 gave again.
  - S01-V-271 (zid) stays `gap`, now with S01-ZD-G13.
- **New statements placed:**
  - S01-SA-137, S01-SA-147 and S01-SA-156 join S01-V-253 (عقد خدمات الدفع, "payment services agreement").
  - Shopify: S01-SH-159 (S01-V-569), S01-SH-147 (S01-V-570) and S01-SH-158 (S01-V-571; with S01-SH-148, S01-V-572).
  - WooCommerce:
    - S01-WC-130 (S01-V-573);
    - S01-WC-133, S01-WC-140, S01-WC-141, S01-WC-142 and S01-WC-151 (S01-V-574, the Network International Terms);
    - S01-WC-148 (S01-V-575);
    - S01-WC-153 (S01-V-576);
    - S01-WC-149 and S01-WC-150 (S01-V-577).
- **Rechecked against another platform:**
  - S01-V-225 (X is quoted from it), S01-V-227 to S01-V-239, S01-V-244, S01-V-245, S01-V-248 to S01-V-251, S01-V-264, S01-V-266, S01-V-273 and S01-V-274.
  - The Payment Processor List rows (S01-V-234 to S01-V-238) lost `identifiers`, which they shared only with S01-SH-006. S01-V-234 keeps `term`, against S01-WC-102 and S01-WC-103.
  - S01-V-244, S01-V-245, S01-V-248 and S01-V-266 now have `identifiers` against S01-SH-147 or S01-SH-159, two statements A3 added.
- **Translations:** the Arabic rows S01-V-253 to S01-V-270 and S01-V-275 now mark the translations that `answers` rests on as mine.

### S01-VP-14 "payout schedule"

- **Gap rows:** S01-V-326 (bigcommerce) stays `gap`, now with A2's S01-BC-G16 in place of S01-BC-G03.
- **New statements placed:**
  - S01-SA-134 joins S01-V-292.
  - S01-SA-151 and S01-SA-152 join S01-V-301 (الإمارات, "كل يوم خميس").
  - S01-SA-142 and S01-SA-143 join S01-V-302 (الكويت, next business day).
  - S01-SA-137 joins S01-V-303.
  - S01-SA-164 joins S01-V-308 (Tuesday).
  - S01-WC-164 is S01-V-578 (instant payout requirements).
  - S01-ZD-150 is S01-V-579 ("أكثر من عملية سحب في اليوم").
- **Not placed:** S01-SA-162, which A2 gave this variation point. It gives the invoice frequency per plan ("Invoice frequency depends on your plan"), not when funds are paid out, and fits no variation point.
- **Rechecked against another platform:** S01-V-276 (X is quoted from it) to S01-V-291 and S01-V-309.
  - Shopify and WooCommerce define "payout schedule" differently in `terms.tsv`. Rows that had `term` on it now have `answers` only.
  - S01-V-277 lost `identifiers`, which it shared only with S01-WC-041.
- **Translations:** the Arabic rows S01-V-292 to S01-V-325 now mark the translations that `answers` rests on as mine.

### S01-VP-15 "payout timing"

- **Gap rows** (none changed form):
  - S01-V-347 (zid) stays `gap`, now with A2's S01-ZD-G17.
  - S01-V-349 (bigcommerce) stays `gap`, now with A2's S01-BC-G17.
- **New statements placed:**
  - S01-SA-138 joins S01-V-341 (الكويت).
  - S01-ZD-150 joins S01-V-343 (2 to 5 working days).
  - S01-WC-152 is S01-V-580: no access "prior to such funds being credited to User’s Payout Account".
- **Rechecked against another platform:** S01-V-327 (X is quoted from it) to S01-V-340, S01-V-348 and S01-V-521.
  - S01-V-328, S01-V-329, S01-V-335 and S01-V-521 lost `identifiers`, which they shared only with statements of their own platform.
  - S01-V-330 lost `term`, which it shared only with S01-SH-061.
  - S01-V-331 and S01-V-337 now share `identifiers` with each other: the time until funds can be paid out, by country.
- **Translations:** the Arabic rows S01-V-341 and S01-V-343 to S01-V-346 now mark the translations that `answers` rests on as mine.

### S01-VP-16 "Minimum payout amount"

- **Gap rows:** S01-V-365 (bigcommerce) stays `gap`, now with A2's S01-BC-G18.
- **New statements placed:** all six statements A2 gave this variation point join existing Salla rows, together with three that A2 gave other variation points.
  - S01-SA-166 joins S01-V-354 (100 riyals).
  - S01-SA-163 joins S01-V-355 (SAR/AED 100).
  - S01-SA-151, S01-SA-153 and S01-SA-154 join S01-V-357 (AED 250).
  - S01-SA-140 and S01-SA-143 join S01-V-358 (KWD 1).
  - S01-SA-141 joins S01-V-359 (no minimum, الكويت).
  - S01-V-358 and S01-V-359 both cover الكويت, with different answers. Both are kept as variants.
- **Rechecked against another platform:** S01-V-350 (X is quoted from it) and S01-V-351.
- **Translations:** the Arabic rows S01-V-354, S01-V-356 to S01-V-364 now mark the translations that `answers` rests on as mine.

### S01-VP-17 "reserve"

- **Changed form:** S01-V-394 (salla) changed from `not covered` to `gap`, with A2's S01-SA-G06, which the audit confirms.
- **Gap rows:** S01-V-395 (bigcommerce) stays `gap`, now with A2's S01-BC-G19.
- **New statements placed:**
  - S01-WC-131 is S01-V-581 (the Reserve Notice, Australia).
  - S01-SH-161 is S01-V-582 (Reserve provisions "continue after termination").
  - S01-SH-149 is S01-V-583 (the Reserve may be debited for refunds, reversals and chargebacks).
- **Rechecked against another platform:** every Shopify and WooCommerce row except S01-V-379 and S01-V-392. That is S01-V-366 (X is quoted from it) to S01-V-378 and S01-V-380 to S01-V-391; most had been compared within their own platform.
  - Shopify and WooCommerce define "reserve", "Reserve Account" and "rolling reserve" differently in `terms.tsv`, so those rows have `answers` only.
  - The Shopify Help Center rows keep `term` against Zid's "مبلغ احتياطي" (S01-ZD-020). Shopify's own Arabic for "reserve" in `terms.tsv` is "الاحتياطي", and Zid gives no definition. Those rows are S01-V-366, S01-V-367 and S01-V-371 to S01-V-374.
- **Translations:** S01-V-393 now marks its translation as mine.

### S01-VP-18 "held"

- **Gap rows:** S01-V-449 (bigcommerce) stays `gap`, now with A2's S01-BC-G20.
- **New statements placed:** all of A2's Salla statements for this variation point are placed.
  - S01-SA-145 joins S01-V-424.
  - S01-SA-185 joins S01-V-432 (commercial accounts only, قطر).
  - New rows:
    - S01-V-584: S01-SA-146 and S01-SA-155, a change of bank account;
    - S01-V-585: S01-SA-169;
    - S01-V-586: S01-SA-159;
    - S01-V-587: S01-SA-160, S01-SA-161 and S01-SA-135, store verification;
    - S01-V-588: S01-SA-172 to S01-SA-176, an approved IBAN certificate;
    - S01-V-589: S01-SA-177;
    - S01-V-590: S01-SA-184, قطر;
    - S01-V-591: S01-SA-181 and S01-SA-180.
  - Shopify: S01-SH-157 (S01-V-592), S01-SH-153 (S01-V-593) and S01-SH-156 (S01-V-594).
  - S01-WC-154, which the audit gives against S01-WC-G02 (PayPal Standard), is S01-V-595.
  - S01-ZD-157 is S01-V-596.
- **Not placed:** S01-ZD-151 says that Gulf merchants moving their store to another country must first empty the wallet ("تصفير رصيد المحفظة"). It states no time or condition on which funds are released or held, and fits no variation point.
- **Rechecked against another platform:** S01-V-396 (X is quoted from it) to S01-V-421.
  - Shopify rows now compare with WooCommerce's "held", "paused", "suspended", "withhold" and "delay", and WooCommerce rows with Shopify's.
  - Rows whose condition shares no word with the other platform keep `answers` only.
- **Translations:** the Arabic rows S01-V-422 to S01-V-433 and S01-V-435 to S01-V-448 now mark the translations that `answers` rests on as mine.

### S01-VP-19 "deducted"

- **Gap rows:** S01-V-490 (bigcommerce) stays `gap`, now with A2's S01-BC-G21. A2's BigCommerce statements for this variation point are new rows: S01-BC-049 (S01-V-597, cross-border fees) and S01-BC-050 (S01-V-598, "you pay 0% on conversion"). S01-BC-048 says Stripe "absorbs the risk" of a rate shift; it is under S01-VP-23 only.
- **New statements placed:**
  - S01-SA-165 joins S01-V-470.
  - S01-SA-188 joins S01-V-475 (صندوق سلة).
  - S01-ZD-150 joins S01-V-480 (withdrawal fees).
  - New rows:
    - S01-V-599: S01-SH-149;
    - S01-V-600: S01-SH-150;
    - S01-V-601: S01-SA-170;
    - S01-V-602: S01-SA-171;
    - S01-V-603: S01-ZD-156;
    - S01-V-604: S01-ZD-155.
- **Rechecked against another platform:** S01-V-450 (X is quoted from it) to S01-V-469, S01-V-488 and S01-V-489.
  - Shopify rows now compare with WooCommerce's "deducted", "deduct", "net of" and "withheld", and WooCommerce rows with Shopify's.
- **Translations:** the Arabic rows S01-V-470 to S01-V-487 now mark the translations that `answers` rests on as mine.

### S01-VP-20 "Termination" and S01-VP-21 "refunded to your customers"

- **Gap rows:**
  - S01-V-501 (bigcommerce, S01-VP-20) stays `gap`, now with A2's S01-BC-G22.
  - S01-V-511 (bigcommerce, S01-VP-21) stays `gap`, now with A2's S01-BC-G23.
  - S01-V-509 (zid, S01-VP-21) stays `gap`, now with A2's S01-ZD-G18.
- **New statements placed:** S01-SH-161 is S01-V-605 (S01-VP-20).
- **Rechecked against another platform:**
  - S01-V-491 to S01-V-493 now compare with S01-WC-010's "terminate". S01-V-492 keeps `identifiers` through its identifier "Effects of Termination".
  - S01-V-502 (X is quoted from it) now compares with S01-WC-010's "refunds ... to your subscribers and customers".
- **Translations:** the Arabic rows S01-V-495 to S01-V-500, S01-V-504 to S01-V-508 and S01-V-510 now mark the translations that `answers` rests on as mine.

### S01-VP-22 "pay in installments" and S01-VP-23 "currency"

- **Changed form:** S01-V-531 (bigcommerce, S01-VP-23) changed from `gap` (S01-BC-G03) to an answer from S01-BC-050: "you continue to settle in your store's default currency". A2 gave no gap for this variation point.
- **Gap rows:** S01-V-520 (zid, S01-VP-22) stays `gap`, now with A2's S01-ZD-G17.
- **New statements placed** (S01-VP-23):
  - S01-V-606: S01-BC-048;
  - S01-V-607: S01-SH-153;
  - S01-V-608: S01-SH-156;
  - S01-V-609: S01-SA-167;
  - S01-V-610: S01-SA-184.

  A2 also gave two other statements for this variation point:
  - S01-BC-056 carries only the payout end;
  - S01-BC-049 names a country, not a currency ("If the shopper’s card-issuing bank differs from the merchant's bank account country"), and is under S01-VP-19 only.
- **Rechecked against another platform:**
  - S01-V-512 (X is quoted from it), S01-V-513 and S01-V-515.
  - S01-V-522 (X is quoted from it), S01-V-523 and S01-V-524. S01-V-523 and S01-V-524 lost the `identifiers` they shared only with S01-WC-048. S01-V-524 now shares `identifiers` with S01-SH-067: currencies by country.
- **Translations:** the Arabic rows S01-V-516 to S01-V-519 and S01-V-526 to S01-V-528 now mark the translations that `answers` rests on as mine.

## Statements that fit no variation point

**Under no variation point.** None of these says who or what fills the X of a variation point of its bullet, and no basis holds.
- S01-SA-057 and S01-SA-149, UAE and Kuwait: "تابع المبالغ من خلال شركة الشحن التي فعّلتها بعقد خارجي أو من خلال مندوب متجرك الخاص" (my translation: "follow the amounts through the shipping company you activated under an external contract or through your store's own courier"). They say where to track cash on delivery amounts, not who collects or holds them.
- S01-SA-148 and S01-SA-157: tracking of electronic payments in the wallet is "قادم قريبًا" (my translation: "coming soon").
- S01-SA-162: "Invoice frequency depends on your plan".
- S01-WC-161: "the payments that we manage for you".
- S01-ZD-151: a Gulf merchant moving the store to another country must first empty the wallet.
- S01-BC-041: "the merchant’s PayPal dashboard".
- S01-BC-047: "Each provider has its own application process".
- S01-BC-058: "funds are conveniently managed within a dedicated balance dashboard".

**A second bullet that fits no variation point of that bullet.** These add to the first pass's list under problem 5. Each is under a variation point of its other bullet.
- (a) S01-SA-163: "They remain pending" names no holder. It is under S01-VP-16.
- (a) S01-WC-152: names no holder. It is under S01-VP-15.
- (a) S01-BC-050: "Stripe ... handles the FX conversion". It is under S01-VP-19 and S01-VP-23.

**BigCommerce from S01-BC-066 onward** was left for the follow-up and is placed there; see "BigCommerce follow-up" below. From that follow-up: S01-BC-071 is under no variation point; S01-BC-068 and S01-BC-078 under bullet (a), and S01-BC-096 under bullet (c), fit no variation point of that bullet.

## `not covered` rows after the second pass

None remain. Of the ten first-pass `not covered` rows:
- S01-V-101 became an answer;
- the other nine became `gap`: S01-V-111, S01-V-124, S01-V-134, S01-V-151, S01-V-166, S01-V-170, S01-V-171, S01-V-172 and S01-V-394.

## Result of the second pass

There are 611 rows: 571 answers, 2 `absent`, 38 `gap` and 0 `not covered`. 80 rows are new: 75 answers and 5 `gap`.

**14 rows changed form:**
- S01-V-101: `not covered` to answer.
- S01-V-111, S01-V-124, S01-V-134, S01-V-151, S01-V-166, S01-V-170, S01-V-171, S01-V-172 and S01-V-394: `not covered` to `gap`.
- S01-V-027, S01-V-205, S01-V-272 and S01-V-531: `gap` to answer.

The other 26 first-pass `gap` and `absent` rows keep their form, with A2's `gap_ids` where A2 gave new ones.

**Rechecks.** Of the 491 first-pass answer rows:
- 434 have new `basis_evidence`, compared with a `raised_by` statement of another platform where there is one;
- 106 changed `basis`;
- 204 now mark the translations that `answers` rests on as mine.

The 57 unchanged rows were already compared with another platform, or are bullet (d) rows.

## Problems with the method, second pass

1. **Different words in one language.** Rule 0 now lets `answers` rest on my translation of a platform's words. It says nothing about English words that differ from X but name the same thing: "custody" or "remain in" for "holds", "hold" for "withhold", "flow through". These rows keep `answers`, and `basis_evidence` records that the words differ.
2. **A term defined by one platform only.** For `term`, I took a term that one platform's `terms.tsv` lists without a definition as not having a different definition, for example WooCommerce's "Payment Facilitator". The brief does not say how to treat an empty definition.
3. **`raised_by` grows during the pass.** Statements A2 added become comparison partners once placed, for example S01-WC-137 ("Payment Facilitator") and S01-BC-051 ("flow through"). Which comparisons are possible depends on what has been placed. The brief does not fix an order.
4. **Partly contradicted gaps.** The audit finds S01-SA-G01, S01-SA-G03 and S01-SA-G05 partly contradicted. They were kept as `gap` next to the new answers, because A2 gave them to the variation point. Gaps the audit finds contradicted (S01-BC-G02, S01-BC-G15, S01-WC-G02) were not kept. The brief does not say what to do with a partly contradicted gap.
5. **What A2 gave that cannot be a variant.** `a2.tsv` lists some statements under variation points whose bullet they do not carry: payout-end statements, bullet (e) statements, and statements of another bullet. These were not placed under those variation points, as the rules allow only statements of the variation point's bullet, or bullet (d).
6. **Scope separator.** Rule 5 separates scopes with `;`, but some scopes contain `;` themselves, for example "السعودية; الكويت". Each scope is followed by its `stmt_ids` in parentheses, which keeps them apart.
7. **Files changing during the pass.** BigCommerce's `statements.tsv`, `gaps.tsv` and `a2.tsv` were rewritten while this pass ran, and one read failed in the middle of a write. Gaps S01-BC-G01 to S01-BC-G23, which the rows cite, are unchanged.
8. **Reading list.** The brief's reading list names `a2.tsv`, while its "Second pass" section also names `absence-audit.tsv`. Both were read, without the `note` column.

# BigCommerce follow-up, after BigCommerce's A2 re-run and second A3 audit

The coordinator asked for this after BigCommerce's A2 re-run (S01-BC-066 to S01-BC-124) and its second A3 audit (S01-BC-125 to S01-BC-128).

Read: BigCommerce's new statements and terms; its `a2.tsv` as it now reads; its new gaps S01-BC-G24 to S01-BC-G40; and its `absence-audit.tsv`, without the `note` column. The coordinator later corrected S01-BC-G08 to `partly contradicted`, citing S01-BC-128, and that row was re-read. Statements S01-BC-001 to S01-BC-038 are unchanged since the first pass, and the excerpts of every row still match their statements. No variation point was added, split or merged.

**Counts.**
- BigCommerce before: 46 rows — 27 answers and 19 `gap`.
- BigCommerce after: 88 rows — 72 answers and 16 `gap`.
- All platforms after: 653 rows — 616 answers, 2 `absent`, 35 `gap`, 0 `not covered`.

**Changed form** (`gap` to answer), where A2 now gives no gap and new statements answer:
- S01-V-532, S01-VP-01: "your merchant account with your merchant service provider" (S01-BC-088);
- S01-V-542, S01-VP-04: hosted payment gateways, S01-BC-089;
- S01-V-111, S01-VP-05: Bank Deposit "directly into your bank account", S01-BC-115;
- S01-V-554, S01-VP-11: S01-BC-088.

**Gap rows kept, with A2's new gap ids:**
- S01-V-537, S01-VP-03: G24, G32;
- S01-V-124, S01-VP-06: G25, G32. The audit finds G25 and G08 partly contradicted by S01-BC-128, which is the new answer row S01-V-623.
- S01-V-135, S01-VP-07: G26, G32;
- S01-V-151, S01-VP-08: G27, G32;
- S01-V-166, S01-VP-09: G28, G32. The audit finds G28 partly contradicted by S01-BC-125 to S01-BC-127, which carry bullet (c) only and are under S01-VP-19.
- S01-V-172, S01-VP-10: G29, G32;
- S01-V-224, S01-VP-12: G30, G33;
- S01-V-326, S01-VP-14: G35, G34;
- S01-V-349, S01-VP-15: G34;
- S01-V-365, S01-VP-16: G36, G34;
- S01-V-395, S01-VP-17: G37, G34;
- S01-V-449, S01-VP-18: G34;
- S01-V-490, S01-VP-19: G38, G34;
- S01-V-501, S01-VP-20: G39, G34;
- S01-V-511, S01-VP-21: G40, G34.
- S01-V-627 is a new `gap` row for S01-VP-13, with G31 and G33.

**Rows added (42, S01-V-612 to S01-V-653):**
- S01-VP-02: S01-BC-069, S01-BC-070, S01-BC-121.
- S01-VP-03: S01-BC-098, S01-BC-090.
- S01-VP-04: S01-BC-066 with S01-BC-077; S01-BC-070 with S01-BC-079; S01-BC-097; S01-BC-104.
- S01-VP-05: S01-BC-116 to S01-BC-118 ("pay you"); S01-BC-119.
- S01-VP-06: S01-BC-128.
- S01-VP-11: S01-BC-068 to S01-BC-070 ("a brand new PayPal platform account"); S01-BC-105 and S01-BC-106 ("a Braintree account").
- S01-VP-13: S01-BC-096 ("the PayPal User Agreement"), and the `gap` row S01-V-627.
- S01-VP-14: S01-BC-073; S01-BC-098 with S01-BC-099; S01-BC-090.
- S01-VP-15:
  - S01-BC-074, two rows (Fast, Standard);
  - S01-BC-090;
  - S01-BC-081;
  - S01-BC-082 with S01-BC-083;
  - S01-BC-098;
  - S01-BC-107;
  - S01-BC-108;
  - S01-BC-099;
  - S01-BC-121.
- S01-VP-17: S01-BC-092 with S01-BC-109.
- S01-VP-18:
  - S01-BC-082 with S01-BC-083;
  - S01-BC-083;
  - S01-BC-092 with S01-BC-109;
  - S01-BC-122.
- S01-VP-19:
  - S01-BC-075 with S01-BC-087;
  - S01-BC-076;
  - S01-BC-100;
  - S01-BC-123 with S01-BC-124;
  - S01-BC-125;
  - S01-BC-126;
  - S01-BC-127.
- S01-VP-22: S01-BC-094.

**Answer rows rechecked, because new statements bear on them:**
- S01-V-026 (S01-VP-01) and S01-V-348 (S01-VP-15), from S01-BC-023, now also hold S01-BC-090. S01-BC-090 gives the same answer for "the standalone PayPal payment gateway", so the rows' `scope` now shows that arrangement.
  - S01-V-026 also holds S01-BC-077 ("PayPal Checkout on BigCommerce is a standalone PayPal integration").
  - S01-V-203 (S01-VP-11) has the same statement, but no new bullet (b) statement gives its answer, so it is unchanged.
- S01-V-027 (S01-VP-01) adds S01-BC-072 and S01-BC-084, and S01-V-205 (S01-VP-11) adds S01-BC-070, S01-BC-078 and S01-BC-084. All of them name the BigCommerce Payments account.
- S01-V-041 (S01-VP-02) and S01-V-531 (S01-VP-23) add S01-BC-100: "payouts to your account are settled in your default currency".
- S01-V-552 (S01-VP-11) adds S01-BC-103 ("Stripe merchant account").
- S01-V-101 and S01-V-551 are unchanged. They name "your linked PayPal account" through which PayPal processes payments (S01-BC-051, S01-BC-055). S01-BC-070 says the BigCommerce Payments account and the PayPal Business account "are two distinct accounts", and that the BigCommerce Payments account "processes and settles all transactions"; that answer is in rows of its own.

**Not placed:**
- A2 gave statements that carry the payout end only, or bullet (e) only, and these cannot be variants: S01-BC-067, S01-BC-080, S01-BC-085, S01-BC-086, S01-BC-091, S01-BC-093, S01-BC-095, S01-BC-101, S01-BC-102, S01-BC-110, S01-BC-111, S01-BC-112, S01-BC-113, S01-BC-114 and S01-BC-120.
- A2 also gave statements to variation points whose bullet they do not carry. These were placed only under variation points of their own bullets:
  - S01-BC-122 (bullet (c)), given to S01-VP-01 and S01-VP-04, is under S01-VP-18.
  - S01-BC-090 is under S01-VP-01, S01-VP-03, S01-VP-14 and S01-VP-15.
- S01-BC-071 is under no variation point. It says "fund holds" are shown in the Actions section, but gives no time or condition on which funds are held.
- Second bullets that fit no variation point of that bullet:
  - (a) of S01-BC-068 and S01-BC-078: an account is created, or "only handles the transactions", but nothing is said to hold, settle or collect;
  - (c) of S01-BC-096: it points to PayPal's policies and states no condition.
- S01-BC-058, S01-BC-041 and S01-BC-047 remain under no variation point. S01-BC-066 has S01-BC-058's words about the Balance dashboard; it is placed only for "powered by PayPal ... accept various payment methods".

**Checker:** `s01-check-b3` reports no error. Its review line lists 11 statements under no variation point, all named in these notes: S01-SA-057, -148, -149, -157, -162, S01-WC-161, S01-ZD-151, S01-BC-041, -047, -058, -071.

**Problems with the brief, follow-up:**
- A2's `a2.tsv` lists statements under variation points of a bullet they do not carry, and statements of bullet (e) or the payout end only. The brief does not say whether those entries should be read as placements.
- A gap that A2 no longer gives may still describe a part of the arrangement that has no answer, as S01-BC-G04, G06, G07 and G13 did. I followed `a2.tsv` and changed those rows to the answers.

# After the independent review

This pass applies the coordinator's ruling on `answers` (17 October 2026, now in the brief's rule 4) to every row of `variants.tsv`, with the review's findings 25, 26, 27, 8 and 16 (`review.md`). It also copies the new kinds from finding 28. No variation point was added, split or merged.

## How the ruling was applied

`answers` now holds only when the statement's own words name the party or thing in X's role, between the buyer's payment and the payout. Shared words no longer decide it; rule 0 still governs the comparison with another platform's statement.

Every `answers` part of `basis_evidence` (574 rows) now begins "answers (role: …):", naming the role, and quotes the words that name it. The clause "the words differ (…)" is gone. For bullet (c), the role is the time, condition, amount or currency the statement gives (rule 1).

| Variation point | Role named in `basis_evidence` |
| --- | --- |
| S01-VP-01 "holds the funds" | the holder of the merchant's funds between the buyer's payment and the payout |
| S01-VP-02 "settlement of funds" | the party that settles the funds to the merchant |
| S01-VP-03 "payouts" | the party that sends the payout to the merchant |
| S01-VP-04 "collect payment" | the party that collects or processes the buyer's payment |
| S01-VP-05 "pay you directly" | the merchant, or the merchant's own account, receiving the buyer's payment directly |
| S01-VP-06 "agent" | the party acting for the merchant in collecting or holding the payment |
| S01-VP-07 "Reserve" | the party that sets or holds a reserve on the merchant's funds |
| S01-VP-08 "withhold" | the party that holds back the merchant's funds |
| S01-VP-09 "deduct" | the party that takes amounts from the merchant's funds |
| S01-VP-10 "security interest" | the holder of a security interest in the merchant's funds |
| S01-VP-11 "account" | the account under which the funds are held |
| S01-VP-12 "licensed" | the licence or legal status under which the funds are held |
| S01-VP-13 "terms of service" | the terms under which the funds are held |
| S01-VP-14 "payout schedule" | the schedule on which payouts are made |
| S01-VP-15 "payout timing" | the time until the funds reach or are available to the merchant |
| S01-VP-16 "Minimum payout amount" | the minimum amount for a payout |
| S01-VP-17 "reserve" | the condition on which a reserve is kept or released |
| S01-VP-18 "held" | the condition on which the funds are held back |
| S01-VP-19 "deducted" | what is taken from the funds before payout |
| S01-VP-20 "Termination" | what happens to the funds when the account or service ends |
| S01-VP-21 "refunded to your customers" | the condition on which the funds go back to the buyers |
| S01-VP-22 "pay in installments" | when the merchant is paid under an instalment or pay-later arrangement |
| S01-VP-23 "currency" | the currency in which the funds are paid out or settled |

## Rows rewritten

- **The review's rows that stay (118).** Findings 26 and 27 point to 146 rows: the `answers`-only rows whose `basis_evidence` said the words differ or showed no shared word, and the rows finding 27 names. 118 of them keep their place, with the role named:
  - by variation point: S01-VP-01 8, S01-VP-02 1, S01-VP-03 13, S01-VP-04 6, S01-VP-05 3, S01-VP-08 3, S01-VP-09 2, S01-VP-11 1, S01-VP-12 2, S01-VP-13 3, S01-VP-14 22, S01-VP-15 10, S01-VP-16 1, S01-VP-18 10, S01-VP-19 14, S01-VP-20 6, S01-VP-21 3, S01-VP-22 7, S01-VP-23 3.
  - S01-V-331 (S01-VP-15), S01-V-350 (S01-VP-16) and S01-V-525 (S01-VP-23) took the table's header as excerpt (finding 27). Each now takes the table's rows, from "Australia AUD" on, which give the times, minimum amounts and currencies; `basis_evidence` quotes the cells.
  - S01-V-536 (S01-VP-03) stays: S01-WC-158 carries bullet (d) and is WooCommerce's own statement, so rule 3 makes it WooCommerce's variant.
- **The other `answers` rows (452)** now name the role too. Their placement, excerpt and comparison are unchanged.
- **New comparison.** S01-V-046 to S01-V-049 (S01-VP-03) were compared with S01-WC-078, which is no longer placed. They are now compared with "WooPayments can send payouts" (S01-WC-026).
- **On `term` only.** These name something outside the flow, so `answers` no longer holds; `term` still holds, so they stay:
  - S01-V-143 (S01-VP-08) and S01-V-421 (S01-VP-18): S01-WC-080, WooCommerce withholding "revenue from all Partner Products", the vendors of Woo Marketplace products;
  - S01-V-149 (S01-VP-08) and S01-V-434 (S01-VP-18): S01-SA-120, S01-SA-121 and S01-SA-123, money an app partner withholds "from the Merchant's wallet" until it is "transfered to the Partner".
- **Statements dropped from a row.** S01-V-435 (S01-VP-18) drops S01-SA-125, label amounts held "من رصيدك في المحفظة" (my translation: "from your wallet balance"). It keeps S01-SA-126, label values held "من رصيد المدفوعات الإلكترونية" (my translation: "from the Electronic Payments Balance").
- **Longer excerpt.** S01-V-601 (S01-VP-19) now takes the whole of S01-SA-170, including "فسيتم الخصم من المدفوعات الإلكترونية" (my translation: "the deduction will be made from the electronic payments").
- S01-V-106 and S01-V-309 take the statements moved in (below).

## Rows moved (3)

- **S01-V-007 (S01-VP-01) into S01-V-106 (S01-VP-05).** S01-SH-017 says the customers' crypto payments are "sent to you", and that Coinbase does not hold them. S01-V-106 is "receive cryptocurrency payments directly from your customers" (S01-SH-015). S01-SH-016 stays in S01-V-174.
- **S01-V-360 (S01-VP-16) into S01-V-309 (S01-VP-14).** S01-SA-013 gives no minimum. It says small amounts can be moved to the wallet and withdrawn "متى شاء" (my translation: "whenever he wishes"), next to S01-SA-014's "at any time".
- **S01-V-606 (S01-VP-23) to the new S01-V-654 (S01-VP-19).** S01-BC-048 names no currency. It says Stripe absorbs the rate risk "so the seller doesn’t have to manage the difference".

## Rows removed (39)

In each, the statement's words name no party or thing in X's role, or name something outside the flow.

- **S01-VP-01:**
  - S01-V-017: Salla's store wallet (finding 27). Salla says it is for "اشتراكات سلة وخدماتها ومشترياتها" (S01-SA-056; my translation: "Salla's subscriptions, services and purchases"), and S01-SA-015 says the same.
  - S01-V-019: S01-SA-034 says where the dues go "وفق دورة التحويل المعتمدة" (my translation: "according to the approved transfer cycle"), not who holds them.
  - S01-V-024: Zid's wallet (findings 8, 16 and 26). S01-ZD-057 describes a wallet the merchant adds balance to, for buying "المنتجات، أو الخدمات المعروضة في منصة زد" (my translation: "the products or services offered on the Zid platform") or transferring out.
  - S01-V-007: moved.
- **S01-VP-02:** S01-V-043. S01-BC-015 says where the merchant sets the settlement currency, not who settles.
- **S01-VP-03:**
  - S01-V-051: S01-WC-027 names who will not send payouts to some debit cards (finding 27).
  - S01-V-054: WooCommerce paying the vendors of Woo Marketplace products (S01-WC-078, finding 27).
- **S01-VP-06:** S01-V-123. S01-SA-124 and S01-SA-125 authorise Salla to pay app partners and carriers from the store wallet.
- **S01-VP-08:**
  - S01-V-140: S01-SH-088 names who asks for more information, not who holds.
  - S01-V-150: S01-SA-125, label amounts held from the store wallet to pay the carrier.
- **S01-VP-09:**
  - S01-V-154: S01-SH-143, a debit of the merchant's bank account.
  - S01-V-164: S01-SA-127, Salla's commission on what it settles with the carrier.
- **S01-VP-10:** S01-V-550 (finding 25). S01-SA-187 is about collateral for صندوق سلة's financing.
- **S01-VP-11:** S01-V-192. S01-ZD-046 names the party in whose name a verification request is made.
- **S01-VP-13:**
  - S01-V-251: the Marketplace Vendor Agreement (S01-WC-079), between WooCommerce and Woo Marketplace vendors;
  - S01-V-273: Shopify's own agreement with its processors (S01-SH-011).
- **S01-VP-14:**
  - S01-V-284: Woo Marketplace vendors (S01-WC-078);
  - S01-V-305: S01-SA-093, which orders an invoice covers;
  - S01-V-310: S01-SA-030, "بعد ذلك" (my translation: "after that"), which names no time.
- **S01-VP-15:** S01-V-521. S01-WC-024 gives no time.
- **S01-VP-16:** S01-V-360, moved.
- **S01-VP-18:**
  - S01-V-429: S01-SA-049 says the order, not the funds, stays pending;
  - S01-V-430 to S01-V-432 and S01-V-590: the payout bank account's country, currency and type (finding 27);
  - S01-V-433: S01-SA-026, no transfer between the two Salla balances;
  - S01-V-584 to S01-V-586, S01-V-589, S01-V-593 and S01-V-594: other requirements on the payout bank account. None says funds are held;
  - S01-V-645: an authorisation hold on the shopper's card until capture (S01-BC-122, finding 27).
- **S01-VP-19:**
  - S01-V-469: Woo Marketplace vendors (S01-WC-078);
  - S01-V-602: S01-SA-171, international label fees settled from the store wallet;
  - S01-V-648: S01-BC-100, a fee applied to the order's purchase price;
  - S01-V-649: S01-BC-123 and S01-BC-124, a fee BigCommerce bills on its invoice.
- **S01-VP-23:** S01-V-606, moved.

## Row added

S01-V-655 is a `not covered` row for Salla under S01-VP-06. Without S01-V-123, Salla has no answer to "agent", and no Salla gap or absence covers it. It goes back to Salla for phase A2.

## `raised_by` and `x_words`

`raised_by` was recomputed from the placed rows.
- **Dropped:**
  - S01-VP-01: S01-SH-016, S01-SH-017, S01-SA-027, S01-SA-029, S01-SA-033, S01-SA-034, S01-ZD-057, S01-ZD-059, S01-ZD-065;
  - S01-VP-02: S01-BC-015;
  - S01-VP-03: S01-WC-027, S01-WC-078;
  - S01-VP-06: S01-SA-124, S01-SA-125;
  - S01-VP-08: S01-SH-088, S01-SA-125;
  - S01-VP-09: S01-SH-143, S01-SA-127;
  - S01-VP-10: S01-SA-187;
  - S01-VP-11: S01-ZD-046;
  - S01-VP-13: S01-WC-079, S01-SH-011;
  - S01-VP-14: S01-WC-078, S01-SA-093, S01-SA-030;
  - S01-VP-15: S01-WC-024;
  - S01-VP-16: S01-SA-013;
  - S01-VP-18: S01-SA-049, S01-SA-060, S01-SA-065, S01-SA-066, S01-SA-026, S01-SA-185, S01-SA-146, S01-SA-155, S01-SA-169, S01-SA-159, S01-SA-177, S01-SA-184, S01-SH-153, S01-SH-156, S01-BC-122, S01-SA-125;
  - S01-VP-19: S01-WC-078, S01-BC-100, S01-BC-123, S01-BC-124, S01-SA-171;
  - S01-VP-23: S01-BC-048.
- **Added:** S01-SH-017 to S01-VP-05; S01-SA-013 to S01-VP-14; S01-BC-048 to S01-VP-19.

Each question's X is still quoted from a statement in its `raised_by`.

`x_words` lost the words of statements no longer placed there:
- S01-VP-01, zid: "حفظ وإدارة المبالغ";
- S01-VP-02, bigcommerce: "settlement currency";
- S01-VP-03, woocommerce: "will pay Partner";
- S01-VP-06: Salla's part;
- S01-VP-08: shopify "put on hold", salla "بحجز مبالغ";
- S01-VP-09, shopify: "debit your account";
- S01-VP-10: Salla's part;
- S01-VP-13, woocommerce: "Marketplace Vendor Agreement";
- S01-VP-18, bigcommerce: "holds the funds until they are captured";
- S01-VP-23, bigcommerce: "that rate is guaranteed".

## Statements now under no variation point

25 more statements are under no variation point, 36 in all. None names a party or thing in a variation point's role, between the buyer's payment and the payout:
- S01-SA-027, S01-SA-029 and S01-SA-033: Salla's store wallet, "يُستخدم لإدارة الأموال ... مثل تجديد باقة المتجر، إصدار البوليصات" (S01-SA-027; my translation: "used to manage funds ... such as renewing the store plan, issuing shipping labels").
- S01-SA-030: amounts can then be moved to رصيد المتجر; "بعد ذلك" names no time.
- S01-SA-066, S01-SA-146, S01-SA-155, S01-SA-159, S01-SA-169, S01-SA-177 and S01-SA-185: requirements on the payout bank account (its type, its name, how to change it). None says funds are held.
- S01-SA-093: which orders a cash on delivery invoice covers.
- S01-SA-124, S01-SA-125, S01-SA-127 and S01-SA-171: payments to app partners and carriers from the store wallet, and Salla's commission on them. S01-SA-124's bullet (d) part disclaims dealings between the merchant and the partner, which no variation point asks about.
- S01-SA-187: collateral for صندوق سلة's financing (finding 25).
- S01-WC-078 and S01-WC-079: WooCommerce and the vendors of Woo Marketplace products.
- S01-ZD-046: the name on a verification request.
- S01-ZD-057: Zid's wallet, for buying Zid's products and services or transferring out.
- S01-BC-015: where the settlement currency is set.
- S01-BC-122: an authorisation hold on the shopper's card before capture.
- S01-BC-123 and S01-BC-124: a fee BigCommerce charges and bills on its invoice.

The 11 named in the earlier sections stay as they were. Finding 24 noted that S01-V-017 was placed on "إدارة" while S01-BC-058 and S01-WC-161 were not. Now none of the three is placed.

## Kinds (finding 28)

The checker rewrote `kinds.tsv`. 32 rows had `stated` (S01-V-158 had `official page;stated`) and now copy `official page`:
- S01-V-087, S01-V-109, S01-V-147, S01-V-148, S01-V-158, S01-V-220;
- S01-V-255, S01-V-257, S01-V-258, S01-V-275, S01-V-307;
- S01-V-422, S01-V-423, S01-V-436, S01-V-472, S01-V-495, S01-V-504;
- S01-V-545, S01-V-547, S01-V-553, S01-V-566;
- S01-V-568 to S01-V-572, S01-V-582, S01-V-583;
- S01-V-599, S01-V-600, S01-V-605, S01-V-623.

## Variation points whose set of answers changed

Phases C and D should revisit these 15: S01-VP-01, -02, -03, -06, -08, -09, -10, -11, -13, -14, -15, -16, -18, -19 and -23. Among them:
- **S01-VP-01:** Zid's rows are now S01-V-023 (the Zid Pay balance) and the gap S01-V-025. Salla's wallet rows are gone.
- **S01-VP-06:** Salla is `not covered`.
- **S01-VP-10:** Salla has only the gap S01-V-170.

S01-VP-05 has one more statement for an answer it already had (S01-V-106). S01-VP-04, -05, -07, -12, -17, -20, -21 and -22 have the same answers as before.

## Result and checker

There are 616 rows: 578 answers, 35 `gap`, 2 `absent` and 1 `not covered`.

`s01-check-b4` reports no error in `variants.tsv` or `variation-points.tsv`. Its review line lists the 36 statements under no variation point, all named in these notes.

Its errors are all in `yemen-marks.tsv`, phase D's file, which this pass does not change:
- Six marks for S01-VP-01 (YC-00, YC-120 to YC-123 and YC-155) name the removed S01-V-024.
- The other 51 errors say a variation point has no mark for a case in `studies/yemen-cases/cases.tsv`, which another session rebuilt during this pass.

## Problems with the ruling

1. **`term` still places statements outside the flow.** The ruling covers `answers` only, and rule 4 places a statement when any basis holds. So S01-V-143, S01-V-421, S01-V-149 and S01-V-434 stay under S01-VP-08 and S01-VP-18 on `term` alone. Their statements are about Woo Marketplace vendors' revenue and money withheld from Salla's store wallet for app partners.
2. **Wallets that hold both top-ups and sales amounts.**
   - **Salla.** The ruling's example fits Salla's store wallet, which is for Salla's "اشتراكات ... وخدماتها ومشترياتها" (S01-SA-056). But sales amounts can be moved into it and withdrawn (S01-SA-030, S01-SA-013, S01-SA-014).
   - **Zid.** The example fits Zid's wallet, which the merchant tops up (S01-ZD-057). But it also receives Zid Ship's cash on delivery dues (S01-ZD-069) and a share of order payments (S01-ZD-066).
   - **Where I drew the line.** I removed rows that rest on the wallet as a services wallet, or on paying for a service from it. I kept rows on holds, deductions and withdrawals of the wallet's funds, for example S01-V-160, S01-V-194, S01-V-307, S01-V-309, S01-V-318, S01-V-343, S01-V-445, S01-V-446, S01-V-448, S01-V-472 to S01-V-474, S01-V-480 to S01-V-485, S01-V-528, S01-V-579 and S01-V-601.
   - **What the ruling leaves open.** It does not say where the flow ends in such a wallet. S01-ZD-069 calls Zid's transfer into the wallet a transfer "إلى التاجر" (my translation: "to the merchant"), and S01-V-061 and S01-V-318 place it as the payout. The rows on wallet withdrawals place the withdrawal to the bank as a payout too.
3. **Bullet (c).** For a (c) variation point, the role is a time, condition, amount or currency, not a party. I read "names the party or thing" as naming that time or condition, as rule 1 does.
4. **Statements that name who does not take the role.** The ruling does not say whether these answer.
   - Following finding 27, I removed S01-V-051 and moved S01-SH-017 out of S01-V-007, because neither is the platform's own (d) statement.
   - I kept S01-V-536, which is.
   - Rows that name the role and say no one, or no account, fills it remain: S01-V-168, S01-V-174, S01-V-183, S01-V-188 and S01-V-256.
5. **Bank-account requirements and holds.** I removed the payout bank account's requirements from S01-VP-18. Rows whose own words tie a requirement to a delay, pause or hold of transfers stay: S01-V-424, S01-V-587, S01-V-588 and S01-V-592. The line is mine; the ruling does not draw it.
