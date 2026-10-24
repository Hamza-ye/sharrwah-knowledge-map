# What was done about the review of D-002 and D-003

The review is `D-002-D-003-review.md`: 9 must-fix findings and 15 optional ones, made by an independent agent on 24 October 2026.

The coordinator checked the must-fix findings' key citations against their sources before acting on them:
- the seam's rules 6, 8, 11 and 19;
- the seam's placement of ledgers and of the currency edition (`8946887:studies/payment-seam/seam.md`:49, 59, 86, 137, 156–157, 161, 163);
- the crossing notes' lines 141, 160 and 221–228 (Shopify) and 60 and 77 (Salla);
- E034's scope and its 24-hour retention (E034:71, 109, 137), and E031's keys that don't expire (E031:277).

Every one held.

| Finding | Kind | What was done |
| --- | --- | --- |
| 1. E034 and E035 cited for more than they show | must fix | Fixed in D-002's drivers, and in D-003's drivers and evidence. Payments-app ids are idempotency keys that don't expire (E031, E032); the Admin API makes idempotency mandatory for creating refunds (E034, E035). |
| 2. Long pending: wrong precedent cited | must fix | Fixed: seam.md:76, E033:781–794 and E031:296–298 are cited. The record also says that no precedent shows long pending combined with polling (seam.md:86), and that polling stays behind the boundary. |
| 3. Citations of E030 to E033 run ahead of the captures | optional | Fixed: "requests, resolve or reject"; E033's kinds rest on the finding aid. |
| 4. Missing locators | optional | Fixed: paths for F-06, the Knowledge Map ids, and E040 at `ca45b1b`. |
| 5. Notes for the first market partly adopted | optional | Fixed: what is adopted, restated without the market, is listed. |
| 6. "Flagged by the guard" cites the draft line | optional | Fixed: the guard script's command is given. |
| 7. Obligation reference dropped; outcomes have no ids or links | must fix | Fixed. The attempt carries the reference of the amount owed. The outcome record carries its own id, its attempt, and for a capture, refund or void, the outcome it draws on. Reverse-money requests name the outcome they draw on. |
| 8. No capability for an order before payment | must fix | Fixed: a capability, and the seam's rule 11, in element 2. |
| 9. "Status query" broader than either platform needs | must fix | Fixed: the capability is removed, and the two provider evidence levels are merged into "the provider's record". |
| 10. "Payments owns" leaves out parts of the seam's list | optional | Fixed: settlement, payout and custody ledgers; reconciliation; dispute mechanics and identity checks; partner relationships, licences and positions; tax on fees. |
| 11. The seam's rules neither adopted nor set aside | optional | Fixed: rules 6, 8 and 11 adopted. The others are taken up when their subject comes. |
| 12. No flag for test or live | optional | Fixed: in element 3. D-003 posts only live outcomes. |
| 13. The change scenario leaves out the settlement contract | optional | Fixed. |
| 14. Currency edition misdescribed; still needed in a neutral form | must fix | Fixed. Amounts carry their currency as the money and currency foundation defines it (S-04). Where agreed and charged amounts differ in currency, both are kept, with the rate. The removals are listed for the offer, the amounts and the capabilities, and G1's B7 is given its path. |
| 15. The guard's precedents need more care | optional | Fixed: evidence levels "in part", with Salla's precedent; Shopify's cash at the counter and Salla's courier remittances; manual reversal added. |
| 16. The ledger's owner not stated; inputs with no path | must fix | Fixed. Option 4 is chosen: two ledgers, one per owner, with rule 19 quoted in full. The seller ledger is the order side's ledger of what is owed. Payouts, provider fees and custody stay in payments' records, joined by the identifiers that cross. |
| 17. Per-currency "balances" read as money held | must fix | Fixed: sums per seller, counterparty, custodian and currency. Nothing is netted across them, and the ledger converts nothing. |
| 18. Posting rules missing | must fix | Fixed. Entries post only from live outcomes that succeeded. They carry the outcome id, the provider's reference, the evidence level and the custodian. The key never expires, and a mismatched repost is refused and raised. |
| 19. Minor units, and amounts as reported | optional | Fixed: minor units come from the currency foundation. Amounts are recorded as reported, never through floating point. E040 is cited. |
| 20. Store credit a seller owes is not an entry type | optional | Set aside to S-05 (area A-32), under the guard on money. Stated in D-003's consequences. |
| 21. Option 2's leaks don't show what it claims | optional | Fixed: the leaks are cited for element 6, and option 2 is argued on its own terms. |
| 22. A fairer alternative to option 1 is missing | optional | Fixed: option 3, one uniform adapter library (Active Merchant), compared with option 1. |
| 23. A driver has no evidence | optional | Fixed: E032's versioned fields and E035's breaking change. |
| 24. A driver's wording contradicts element 1 | optional | Fixed: "no rule or type on the order side refers to a particular market, currency variant, wallet or bank". |
