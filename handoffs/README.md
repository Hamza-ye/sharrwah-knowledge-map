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

## What can be captured from Yemen (the founder, 27 October 2026)

The founder reports, from Yemen: Zid's sign-up code, sent by SMS, never arrives, so no Zid account can be made; and on Zid and Salla, a purchase, and the store's or the owner's verification, can't be completed. Salla's sign-up works. This is what the founder can do from Yemen, not evidence of what either platform does. What it means for these requests:
- **Can run now, at no cost:** H-001 (read-only, on the held merchant store), H-003 (public pages, in a browser), H-002 up to the verification step, and H-007 (a new Shopify account by email; stop before any document).
- **H-004** is shown at verification, so it may stop before the contract; its first step can ride on H-002's run, with a store whose country is the UAE or Kuwait.
- **H-005** needs a store on Salla's Special plan, which can't be bought from Yemen. Only its step 1 runs: whether a held store's plan opens markets.
- **H-006** needs a business entity outside Yemen, and **H-008** answers questions that phase C is not expected to turn on. Both wait until phase C shows a need.
- *Since then (27 October 2026):* H-006, H-007 and H-008 all ran, at the founder's word, with a new Shopify account located in the United States in place of a business entity outside Yemen. The table below says what each settled.

## Requests

| Id | Repository | Asks for | For | Raised | Status |
| --- | --- | --- | --- | --- | --- |
| [H-001](H-001-observed-sa-store-country-settings.md) | observed-sa | Where the merchant store shows its country, and whether it can be changed | S-02, RD1: S02-SA-G01 | 27 October 2026 | open; ran at observed-sa `b0bd0b16` (28 October 2026), read by A2-SA-R |
| [H-002](H-002-observed-sa-onboarding-countries.md) | observed-sa | What the onboarding shows after a store country other than Saudi Arabia (its list of countries is held), and the new store's currency, language and apps | S-02, RD1: S02-SA-G03, S02-SA-G07; RD3: S02-SA-G09 | 27 October 2026 | open; narrowed on 27 October 2026 by the absence audit, and extended the same day by gap-closing; ran at observed-sa `b0bd0b16` (28 October 2026), read by A2-SA-R |
| [H-003](H-003-observed-sa-plans-faq.md) | observed-sa | The plans pages' answers on using Salla outside Saudi Arabia | S-02, RD1: S02-SA-G04 | 27 October 2026 | open; ran at observed-sa `b0bd0b16` (28 October 2026), read by A2-SA-R |
| [H-004](H-004-observed-sa-verification-contract.md) | observed-sa | The payment services contract a store in the UAE or Kuwait signs at verification | S-02, RD1: S02-SA-G02 | 27 October 2026 | open; ran at observed-sa `b0bd0b16` (28 October 2026), read by A2-SA-R |
| [H-005](H-005-observed-sa-multi-market.md) | observed-sa | Multiple markets, switched on and set up, and which settings take a value per market | S-02, RD2 and RD3: S02-SA-G06, S02-SA-G08 to S02-SA-G11 | 27 October 2026 | open; may need a store on Salla's Special plan; extended on 27 October 2026 by gap-closing; ran at observed-sa `b0bd0b16` (28 October 2026), read by A2-SA-R |
| [H-006](H-006-observed-sh-store-outside-yemen.md) | observed-sh | The admin as a store based outside Yemen sees its markets, business entities, Managed Markets and payments | S-02, RD1 and RD3 | 27 October 2026 | done at observed-sh `19a5f6435` (27 October 2026; read by A2-SH-R1 and A2-SH-R2), up to Shopify Payments' set-up, which stops at its step 2 without a valid SSN or ITIN. Held: a US store's Settings > General, its markets and a new market's parts, Managed Markets' eligibility (missing Shopify Payments only), and Payments. The new market's page showed no business entity part (S02-SH-1095, S02-SH-1100). What lies past Shopify Payments is S02-SH-G15, which no capture can reach |
| [H-007](H-007-observed-sh-store-country-sign-up.md) | observed-sh | What sets a store's country at sign-up, and whether a change of its business entity's country is checked | S-02, RD1: S02-SH-G01, S02-SH-G02 | 27 October 2026 | done at observed-sh `19a5f6435` (27 October 2026; read by A2-SH-R1). Step 1 answered S02-SH-G10: a sign-up that chose the United States, from a network traced to Yemen, made a store that is American in its country, address, business entity and currency (S02-SH-1035 to S02-SH-1047). Step 2 narrowed S02-SH-G09 into S02-SH-G14: the switch saved with no step asking for verification, and whether a check follows later can't be seen in a run, so G14 is a question to the platform |
| [H-008](H-008-observed-sh-markets-per-plan-checkout-address.md) | observed-sh | How many markets of each kind each plan allows, which business types Markets is offered to, and the checkout's address form per buyer country, on its dev stores | S-02, RD2 and RD3: S02-SH-G06, S02-SH-G07, S02-SH-G08 | 27 October 2026 | done at observed-sh `19a5f6435` (27 October 2026; read by A2-SH-R1 and A2-SH-R2) for the Basic and the paid Advanced store. Item 3 answered S02-SH-G11 (the checkout's form for the five countries). Item 1 narrowed S02-SH-G12 into S02-SH-G16: no step on Basic showed a limit, and the Grow, Advanced and Plus dev stores, channel markets and a number per plan aren't held. Item 2 narrowed S02-SH-G13 into S02-SH-G15 |
