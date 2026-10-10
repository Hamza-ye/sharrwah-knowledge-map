# Open work, in order

Each item says what it decides and what it needs. Items lower down depend on the ones above.

## 1. The payment seam (before the frame sort): done

The answer is in `studies/payment-seam/seam.md`, with the 81 rows tagged in `studies/payment-seam/rows-tagged.tsv`. In short, there is a hard boundary around the rails and a seven-element contract on the order side. The tags are 24 contract rows, 13 foundation rows, 42 payments-internal rows, 1 core row and 1 company row. The original brief follows.


**Question.** Can payments be its own part of Sharrwah, with its own questions, research, regulation, consultations and pace? The rest of the platform would then depend only on a narrow, stable contract and could be built now, while payments evolves alone in parallel.

**Why first.** The answer splits the 81 register rows into three groups:
- rows that belong to the contract, which everything else depends on and which must settle early;
- rows that stay inside payments, which can move at their own pace;
- rows that aren't payments at all.

The frame sort (item 2) then runs separately for each group. Making the split after the sort would mix the concerns again.

**What it needs.** No new research. It can be answered from evidence already held: observed-sh and observed-sa, and the Shopify study in this repository.

**Starting points from the Shopify study.** These suggest a separable concern behind a contract, not a completely separate one:

- **Payment status is a roll-up.** The order's payment status is derived from its transactions. Admin actions such as capture, mark as paid and refund are moves on transactions (A1 §0; D §1.1).
- **Orders work without a processor.** An order placed with a manual method such as cash on delivery is later marked as paid (B §1.1–1.2).
- **Providers sit behind a session contract.** A provider is a remote state machine that Shopify commands, one session per financial operation; checkout and the order never see the rail's internals (C §0, §2).
- **Records live in separate ledgers.** What was agreed, what was attempted, what was booked and what the processor credited are kept apart. Cash is a custody ledger of its own, and merchant billing is a separate invoice ledger (D §0; E §0).
- **Shopify's commerce protocol stops at "order placed".** Authorization, capture, settlement, payouts and fees stay inside Shopify (G §0, §5).
- **Things that cross the seam.** Each would become a contract element:
  - the payment methods offered at checkout;
  - the buyer's step inside a method;
  - capture timing tied to fulfilment;
  - payment terms and deposits, meaning what falls due and when;
  - refunds driven by returns;
  - cash at the counter or on delivery;
  - fraud and risk holds on fulfilment;
  - the currency the buyer pays in;
  - payouts and seller billing.
- **Not payments at all.** Money representation (currency, rial edition) and zone are foundations shared by the whole platform.

**Output.**
- Every crossing between payments and the rest of the platform, on both Shopify and Salla, each with its evidence.
- What stays inside payments.
- The contract's elements.
- The 81 rows tagged as contract, payments-internal or core.

## 2. The frame sort of the 81 rows

Two agents sort the rows without seeing each other's work, then the results are compared.

- **Rules:** the frame's rules (Built, Configured, Chosen, Context; certainty kept separate).
- **References:**
  - platform evidence (observed-sh, observed-sa);
  - Yemen evidence (`evidence/yemen/`);
  - the founder's recorded decisions and attestations;
  - the model.
- **Citations:** every sorted line cites a source that resolves.
- **Disagreements:** a disagreement between the two agents means a rule is missing; a citation that doesn't resolve means the line isn't grounded.
- **Scope:** runs per group from item 1, in this order:
  1. the 24 contract rows and the 13 foundation rows, which settle early;
  2. the 42 payments-internal rows, on their own track, at their own pace.

  PAY-44 (company) goes to the founder as step 0.

## 3. Yemen sources (in progress, payments side only)

- The Arabic-first search for Sana'a rules, operators, couriers and seller payment pages, with the sources reachable from outside Yemen captured.
- `evidence/yemen/to-fetch-from-yemen.md`: what only the founder can fetch from inside Yemen.
- Founder attestations, using `evidence/yemen/attestations/TEMPLATE.md`.

## 4. Before going live in Sana'a (payments side)

- A Sana'a lawyer or accountant on what Sana'a requires of a platform in the launch positions, record-only and integrator (PAY-58).
- Dated screenshots of the payment flows the launch relies on.
