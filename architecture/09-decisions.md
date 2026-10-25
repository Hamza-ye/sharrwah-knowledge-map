# 9. Architecture decisions

The decision records are in `decisions/`. `python3 -I method/decision_status.py` lists them with their status.

| Record | Decision | Door | Status |
| --- | --- | --- | --- |
| D-001 | Who holds sellers' money at launch: never Sharrwah; A and B reserved, not built; with three choices on the line's extent | one-way | proposed, waiting on the founder's line |
| D-002 | The payment boundary: seven elements between the order side and payments | two-way | proposed, the working basis; not acceptable until S-05, S-07, S-10 and S-11 settle the nine items it doesn't carry (its Scope) |
| D-003 | The seller ledger: what is owed, two ledgers per owner, holds no money | two-way | proposed, the working basis; not acceptable before D-002, nor until S-03, S-05 and S-07 settle the four items it doesn't carry |
| D-004 | The pilot's Decisions 2 to 12 follow column C | one-way | proposed; settled by D-001's line |
| D-005 | When the seller is paid under installments | one-way | deferred until an installment provider is offered in a market Sharrwah serves |
