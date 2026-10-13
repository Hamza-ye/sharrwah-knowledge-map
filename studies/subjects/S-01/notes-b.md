# S-01 phase B notes

First pass. Phase A2 has not run, so no `a2.tsv` was read and no row was revisited.

Read: this brief; the five platforms' `statements.tsv`, `terms.tsv`, `absences.tsv`, `gaps.tsv`; `kinds.tsv`. No `notes.md` file and no `note` column was read. `citations.tsv` was not needed.

## Merges

None so far.

## Partial overlaps that were split

- **S01-VP-02 "settlement of funds" and S01-VP-03 "payouts".** Both are about funds moving to the merchant. They partly match: Shopify names a different party for each in S01-SH-019 ("The Payment Processor retains sole and exclusive responsibility for Payment Processing, including the settlement of funds") and S01-SH-075 ("your payouts are sent from Shopify, they're processed by these partners"). Statements whose words are "settle", "settlement" or "تسوية" went under S01-VP-02. Statements whose words are "payout", "deposit", "pay you", or "تحويل" to the merchant's account went under S01-VP-03. S01-BC-021 ("settles directly to your bank account") is under both.
- **S01-VP-04 "collect payment" and S01-VP-05 "pay you directly".** Both name who first receives the buyer's payment. They partly match: in S01-WC-093 ("lets your customers pay you directly via their bank account") the payment reaches the merchant with no party between. Statements saying a payment goes "directly" ("مباشرة") from the buyer to the merchant's own account went under S01-VP-05; statements naming a party that collects or processes the payment went under S01-VP-04.

- **S01-VP-01 "holds the funds" and S01-VP-08 "withhold".** "Hold" is used both for having the funds (S01-SH-099, "Global-e holds the funds"; S01-WC-116, "funds Stripe holds for User") and for holding them back (S01-SH-126, "withhold Settlement"; S01-SH-086, "place a hold on your payout account"). The two only partly match, so the variation point was split. S01-SH-022, S01-SH-033 and S01-SH-034 use "hold funds" while awaiting information, pending resolution or under Legal Process; they are under both.
- **S01-VP-01 "holds the funds" and S01-VP-07 "Reserve".** A Reserve is funds held (S01-SH-133, "collateral funds which Stripe holds and controls"), but statements about reserves name who sets, applies or controls them, which S01-VP-01 does not ask. They went under S01-VP-07 only.

## `not covered` rows

These go back to the platform for phase A2.

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
