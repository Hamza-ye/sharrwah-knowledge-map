# Founder decisions

What the founder has decided, in the frame's terms (`method/frame.md`). Each entry says what kind of answer it is, when it was given, and what it rules in or out.

The entries record decisions, not evidence. An entry that reports something observed belongs in `evidence/yemen/attestations/` instead.

## Decided

| Id | Decision | Kind | Given | Effect |
| --- | --- | --- | --- | --- |
| F-00 | Sharrwah is a Shopify-class commerce platform for many markets. Yemen is its first market, not its design target. | Boundary on the Built range | The founder's brief at the start of this work; restated 2026-10-10 | The Built model serves many markets. Yemen's two authority zones, its two rial editions, its rails and its licences are Context and Configured values for one market, not the shape of the model. |
| F-01 | Sharrwah has no US ties. | Company fact, step 0 | 2026-10-10, in conversation | Bears on PAY-44. It narrows the sanctions exposure the earlier study assumed, but the legal entity and domicile are still open (O-01). |
| F-02 | In Yemen, its first market, Sharrwah goes live in the Sana'a zone first. | Setting: Configured, release | 2026-10-10, in conversation | The Sana'a zone is switched on at launch. Aden is built but off. |
| F-03 | Within Yemen, Sharrwah is built as if both zones exist. | Boundary on the Built range | 2026-10-10, in conversation | Both of Yemen's authority zones are modelled, and neither may be assumed. This is the Yemen case of F-00: a market can contain more than one regulatory zone, and a currency can circulate in more than one edition. |
| F-04 | Sources dated before 2023 are too old to judge 2025–2026 status. | Method rule | 2026-10-10, in conversation | Applied to all evidence through `age_class`. |
| F-05 | The founder's words are attestations, not evidence. Agents must not reason from them as fact. | Method rule | 2026-10-10, in conversation | Observations go in `evidence/yemen/attestations/` with their limits. |
| F-06 | The founder proposed that payments be its own concern, with its own questions, research and pace, while the rest of the platform proceeds. | Founder direction | 2026-10-10, in conversation | The seam study found this workable behind a narrow contract (`studies/payment-seam/seam.md`). |

## Open company question (step 0)

This goes to the founder and should come back as a boundary or a setting (frame, rule 8).

| Id | Question | Rows |
| --- | --- | --- |
| O-01 | Which legal entity and domicile contracts with sellers and partners? | PAY-44, PAY-53 |

## Not founder questions: where they sit in the model

These were wrongly listed as company questions. The model already places them, and none of them needs a founder answer before building.

- **Which money roles Sharrwah takes, including whether it ever holds buyer money or value** (PAY-42, PAY-45, PAY-47, PAY-49). This is Sharrwah's position on each payment setup, which stays inside payments (`studies/payment-seam/seam.md`).
  - The positions form a Built range: record-only, integrator, partner-held, holder and issuer. Holder and issuer are named but reserved, not built.
  - Which positions are on in each zone is a Configured value. The founder has not set it. The Yemen study proposes record-only at launch, then integrator as rail terms arrive (`yemen-setup-options/report.md`, "Four stages"). That is a provisional proposal.
  - Switching on a holder position depends on Context: the licence rules (PAY-52, PAY-56, PAY-57).
- **How Sharrwah earns** (PAY-51). Prices per plan are a Configured value set by Sharrwah as operator. Billing sellers is a core obligation (seam, rule 5). Fees netted by a partner are a payments option that becomes available only with a partner (stage 2).
- **When to seek a licence, and with what capital** (PAY-52). This is an operator decision on the payments track, made when its Context triggers arrive. It switches on reserved positions and blocks nothing before then.

Nothing in this file comes from earlier orientation documents.
