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

