# 5. Building block view

**Level 1, so far.** Two blocks and the contract between them, from S-01. Later subjects add blocks: tenancy, identity and permissions, catalogue and orders, apps and events.

| Block | What it owns | Record |
| --- | --- | --- |
| **The order side** | what was agreed and is due, with its terms and schedules; the amount still owed; the order's states; the seller's rules on payment methods, applied by checkout; the seller ledger | D-002, D-003 |
| **Payments** | provider accounts and protocols; fees, and tax on fees; settlement, payout and custody ledgers; reconciliation with providers; risk, disputes and identity checks for providers; partner positions; which providers are available per market; simulated outcomes | D-002 |

**The contract between them** has seven elements: offer, attempt, outcome record, reverse money, verdicts, capabilities and context reads (D-002). The order side never names a provider. Payments never reads live order data while deciding.

**Reserved, not built:**
- stored permissions to charge later;
- the settlement contract (holding, netting, payouts), needed only if Sharrwah or a processor ever holds the money (D-001).

All three records are *proposed*.
