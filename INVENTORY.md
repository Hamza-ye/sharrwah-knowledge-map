# What stays in the working files, and why (1 November 2026)

**The rule** (the founder, 1 November): nothing stays because it cost something. An item stays only if a decision on Shopify's model needs it now, and only its smallest useful part. Everything else leaves the working files in one commit. It stays in the git history, reachable by a link pinned to that commit (`HISTORY.md`), so nothing is lost and nothing left behind can steer the work.

**The decisions it is measured against:**
- the founder's decisions in force (`founder-decisions.tsv`), the latest being Sharrwah built on Shopify's model;
- architecture's six first decisions:
  1. how stores are kept apart, and where their data lives;
  2. identity and permissions;
  3. money records and currency;
  4. markets and the seller's country;
  5. events, and the places outside services plug in;
  6. settings held per store, varied per market and limited per plan.

**Proposed. Nothing has left yet.**

| Item | What it is | Size | Stays? | The decision that needs it now |
|---|---|---|---|---|
| `founder-decisions.tsv`, `founder-messages/` | Your decisions and their bases | 60 KB | Stays | Every decision is bound by them |
| `observed-sh` (Shopify's evidence repository) | Shopify's admin, its schemas, routes, help and terms, as captured | outside | Stays | All six: Shopify's shapes are read there |
| `evidence/shopify-engineering/` | Shopify's own engineering writing | 16 MB | Stays | 1: how Shopify keeps stores apart, and where it keeps their data |
| `studies/subjects/S-01/decision-1.md`, `register.tsv` | Your Decision 1: who holds sellers' money | small | Stays | 3: money records are bound by it |
| `studies/subjects/S-02/decisions.md`, `register.tsv` | The rulings on what a market is, made from five platforms | small | Stays, to be checked against Shopify's shape | 4: markets, and 3 for the currency entry |
| `method/corpus_search.py`, `runs_corpus.py`, `quote_check.py`, `check_report.py`, `count_tokens.py` | Search of the held evidence, the quote checker, the token count | small | Stays | All six: find Shopify's evidence, and check every quote against its source |
| `HISTORY.md` | Each baseline, by commit | 12 KB | Stays | How anything that leaves is reached |
| `CLAUDE.md`, `README.md` | What a session reads first | small | Rewritten for this frame | Every session |
| `PLAN.md`, `STATE.md` | The plan and state of the old frame | 172 KB | Replaced by a one-page plan and state | — |
| `observed-sa`, `other-product-class` | Salla's, Zid's, BigCommerce's and WooCommerce's evidence | outside | No longer working evidence | None: no other platform's reading shapes the model |
| `evidence/product-class/` | Other platforms' captures | 682 MB | Leaves | None, for the same reason |
| `evidence/yemen/`, `studies/yemen-cases/` | Yemen's evidence and Stage 1's study | 356 MB | Leave | None: Yemen's setup reads Yemen fresh when you decide to set it up |
| `evidence/designs/` | Designs beyond the platforms, read for S-02 (Stripe, TigerBeetle, Unicode) | 15 MB | Leaves | None now. Re-read if money records need a ledger design |
| `studies/concern-map/` | The concern map of five platforms | 33 MB | Leaves | None: Shopify's own guides and index find its evidence at the source |
| `studies/class-model/` | The class model, its passes and briefs, and the accuracy probe | 71 MB | Leaves | None: it names what platforms do, while the decisions need Shopify's shapes, read at the source. The probe's lessons go into the new plan |
| the rest of `studies/subjects/` | The subjects' phases, statements, Yemen rows and walks | 19 MB | Leaves | None |
| `questions/` | Q1 to Q3 | 28 KB | Leaves | None |
| `architecture/` | The architecture plan, its review, the fitness test | 168 KB | Leaves | None: the six decisions above are all it carries forward |
| the other 83 scripts in `method/` | The old passes' tools | 2 MB | Leave | None |
| `reports/`, `handoffs/` | Reports to you; capture requests | 632 KB | Leave | None |

**On what I said before:** last time I said the Shopify readings in the class model would stay, as a way to find where to look. Taken item by item, Shopify's own repository does that job at the source, with its guides and its index, so they leave too.
