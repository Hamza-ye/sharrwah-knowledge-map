# 9. Architecture decisions

The decision records are in `decisions/`. `python3 -I method/decision_status.py` lists them with their status.

| Record | Decision | Door | Status |
| --- | --- | --- | --- |
| D-001 | Who holds sellers' money at launch: each provider; A and B reserved, not built | one-way | proposed, waiting on the founder's line |
| D-002 | The payment boundary: seven elements between the order side and payments | two-way | proposed; stays proposed until the first providers are walked through it (S-07), under the acceptance rule |
| D-003 | The seller ledger: what is owed, two ledgers per owner, holds no money | two-way | proposed; accepted no earlier than D-002 |
| D-004 | The pilot's Decisions 2 to 12 follow column C | one-way | proposed; settled by D-001's line |
| D-005 | When the seller is paid under installments | one-way | deferred until an installment provider is offered in a market Sharrwah serves |
