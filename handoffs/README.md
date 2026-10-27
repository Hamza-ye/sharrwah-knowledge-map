# Handoffs: capture requests for the local agent

**What this folder is:** requests to capture evidence that a run in observed-sh or observed-sa could hold, but doesn't yet (`PLAN.md`, section 6, Evidence; the founder, 27 October 2026). They aren't decisions for the founder.

**How a request travels:**
1. **The coordinator** checks that the evidence isn't held (`method/held_index.py`, which reads the runs' saved answers too, and `method/corpus_search.py`), records the gap in the subject's files with `who_can` `capture`, and writes one file here, named for the repository and what it asks.
2. **The founder** hands the file to a local agent working in that repository.
3. **The local agent** captures what it can, as that repository records runs: its own `docs/OPERATING.md`, tools and formats, with a note in its `index/run-notes.tsv`. It stops before anything that spends money or can't be undone, and before what the file says to stop at. It pushes, and tells the founder the commit.
4. **The coordinator** reads the new runs at that commit, closes the gaps they answer, and marks the request done below, with the commit.

**A request may need the founder,** for something only the founder can give: a payment, a phone, a store on a paid plan. It says so under **Needs**, with what it buys and what stays open without it (`PLAN.md`, section 5, spending).

**Every file has the same parts:**
- **Repository** and **instrument**: the store or account to use.
- **What to capture**, step by step, and where to stop.
- **Already held**: so the run doesn't repeat it.
- **Why**: the subject, root decision and gap ids it answers.
- **Needs**: anything the founder must give.
- **Done when**: what the run must hold.

**The coordinator's side never writes to observed-sh or observed-sa** (`CLAUDE.md`).

## Requests

| Id | Repository | Asks for | For | Raised | Status |
| --- | --- | --- | --- | --- | --- |
| [H-001](H-001-observed-sa-store-country-settings.md) | observed-sa | Where the merchant store shows its country, and whether it can be changed | S-02, RD1: S02-SA-G01 | 27 October 2026 | open |
| [H-002](H-002-observed-sa-onboarding-countries.md) | observed-sa | What the onboarding shows after a store country other than Saudi Arabia (its list of countries is held) | S-02, RD1: S02-SA-G03 | 27 October 2026 | open; narrowed on 27 October 2026 by the absence audit |
| [H-003](H-003-observed-sa-plans-faq.md) | observed-sa | The plans pages' answers on using Salla outside Saudi Arabia | S-02, RD1: S02-SA-G04 | 27 October 2026 | open |
| [H-004](H-004-observed-sa-verification-contract.md) | observed-sa | The payment services contract a store in the UAE or Kuwait signs at verification | S-02, RD1: S02-SA-G02 | 27 October 2026 | open |
| [H-005](H-005-observed-sa-multi-market.md) | observed-sa | Multiple markets, switched on and set up | S-02, RD2 and RD3 | 27 October 2026 | open; may need a store on Salla's Special plan |
| [H-006](H-006-observed-sh-store-outside-yemen.md) | observed-sh | The admin as a store based outside Yemen sees its markets, business entities, Managed Markets and payments | S-02, RD1 and RD3 | 27 October 2026 | open |
| [H-007](H-007-observed-sh-store-country-sign-up.md) | observed-sh | What sets a store's country at sign-up, and whether a change of its business entity's country is checked | S-02, RD1: S02-SH-G01, S02-SH-G02 | 27 October 2026 | open; step 2 narrowed on 27 October 2026 by the absence audit |
