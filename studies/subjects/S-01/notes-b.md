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
  - S01-SA-136 is under the payout end only.
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

  S01-BC-056, which A2 gave for this variation point, carries only the payout end.
- **Rechecked against another platform:**
  - S01-V-512 (X is quoted from it), S01-V-513 and S01-V-515.
  - S01-V-522 (X is quoted from it), S01-V-523 and S01-V-524. S01-V-523 and S01-V-524 lost the `identifiers` they shared only with S01-WC-048. S01-V-524 now shares `identifiers` with S01-SH-067: currencies by country.
- **Translations:** the Arabic rows S01-V-516 to S01-V-519 and S01-V-526 to S01-V-528 now mark the translations that `answers` rests on as mine.

