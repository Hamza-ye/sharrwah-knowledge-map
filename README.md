# Sharrwah knowledge map

Questions agreed with the founder, the evidence captured to answer them, and derived documents written in October 2026 by Claude Code agents.

**Where the work stands.** The three questions in `questions/` drive the work now. `NEXT.md` gives their order.

**What the documents draw on.** The derived documents draw on two kinds of source:

- the evidence captured in [observed-sh](https://github.com/Hamza-ye/observed-sh) (Shopify) and [observed-sa](https://github.com/Hamza-ye/observed-sa) (Salla);
- desk research on Yemen.

**Claims, not evidence.** The derived documents are claims about that evidence, not evidence themselves. Where a claim and its source disagree, the source wins.

**The exception is `evidence/`.** It holds raw copies of sources, and each area's README sets the rules for its folder.

## Contents

| Folder | What it holds |
| --- | --- |
| `questions/` | The three agreed questions: Q1, the concern map; Q2, the Yemen stress test; Q3, placing the rows. Each file holds the question as agreed and what was settled before it runs. |
| `method/capture/` | The capture tools that make the copies in `evidence/`, and how to run them. |
| `shopify-payments-study/` | Eight reading passes over Shopify's Help Center, developer docs and API schemas: arrangements (A1), the processor (A2), order obligations (B), the payment provider slot (C), the money model (D), point of sale, finance and billing (E), country variability (F) and the Universal Commerce Protocol (G). Statements are from the docs unless marked "Inference". |
| `yemen-setup-options/report.md` | "Build Yemen payments around roles, not wallets": seventeen payment setup options across five positions Sharrwah can take, the two authority zones, and the register rows PAY-43 to PAY-81. |
| `yemen-setup-options/notes/` | The six research notes behind the report: regulation and licensing, wallets and e-money, banks, exchange networks and cards, cash and commerce practice, currency and the territorial split, and analogous markets. |
| `register/pay-questions.tsv` | The question register, PAY-01 to PAY-81, with evidence pointers, feeds, lane and status. |
| `register/pay-evidence-additions.tsv` | Evidence entries the register cites that were not yet in the knowledge map's evidence list. |
| `model/obligation-to-payout.html` | The obligation-to-payout model page: what is agreed, attempted, moved and due, the proposed questions, the Yemen setup options and the sources. Open it in a browser. |
| `evidence/yemen/` | Raw copies of the cited Yemen sources and of the community payment-client repositories, with manifests. Also holds the list of sources that can only be fetched from inside Yemen, and the template for founder attestations. |
| `evidence/shopify-engineering/` | Raw copies of Shopify's engineering talks, blog posts and payments developer docs, and three repositories pinned at a commit. |

## Limits

- **Not inputs to Q1.** The payments study, the Yemen setup options, the register and the model page were written before the three questions, and Q1 doesn't use them. The Q2 and Q3 files say which of them those questions may use, and how.
- **Shopify study.** File paths such as `help/manual/...` are Help Center URL paths. The same pages are captured in observed-sh runs `20260930T003703Z-help-en-md` and `20260930T003705Z-shopify-dev-md`.
- **Yemen sources were captured on 10 October 2026, from outside Yemen.** `evidence/yemen/` holds the copies. Some Sana'a-side sites can only be reached from inside Yemen.
- **Sources dated before 2023 are historical.** They can show what a document said, but not 2025–2026 status.
- **Yemen coverage is uneven.**
  - It holds no official source from the Sana'a side; facts about that zone come from secondary sources.
  - Provider facts come from community client code, operator pages and app listings, not from providers' merchant documentation.
  - Commerce practice rests on one Sana'a store's payment page and one survey of Aden users.
- **One redaction.** A provider endpoint's raw IP address is left out of `notes/wallets_emoney.md`.
- **Ids.** PAY-01 to PAY-81 are this register's own ids. Other Sharrwah documents that use PAY- labels number different things.

Values are as of 10 October 2026.
