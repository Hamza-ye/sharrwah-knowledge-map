# What stays in the working files, and why (1 November 2026)

**The rule** (the founder, 1 November): nothing stays because it cost something. An item stays only if a decision on Shopify's model needs it now, and only its smallest useful part. Everything else has left the working files. It stays in the git history: commit `9f3749d0` is the last that holds all of it (`HISTORY.md`).

| Item | What it is | Why it stays |
|---|---|---|
| `founder-decisions.tsv` | The founder's decisions, every one marked for review except the decision of 1 November, which is the frame the review uses | Every decision is bound by them until the review says otherwise |
| `founder-messages/` | The founder's original messages that decisions cite | The bases of those decisions |
| `studies/subjects/S-01/decision-1.md`, `register.tsv` | Decision 1, who holds sellers' money, with its follow-ons | Money records are bound by it. Marked for review |
| `studies/subjects/S-02/decisions.md`, `register.tsv` | The rulings on what a market is | Markets, and the currency entry. Marked for review |
| `method/corpus_search.py`, `runs_corpus.py`, `quote_check.py`, `check_report.py`, `count_tokens.py` | Search of Shopify's held evidence, the quote checker, the token count | Finding Shopify's evidence, and checking every quote against its source |
| `HISTORY.md` | Each baseline, by commit | How anything that left is reached |
| `CLAUDE.md`, `README.md`, `PLAN.md`, `STATE.md` | What a session reads first, the plan and the state | Rewritten for this frame |
| `observed-sh` | Shopify's evidence repository, outside this one | Shopify's shapes are read there, its engineering writing included |

**Left the working files:** the other platforms' evidence and repositories as working evidence; this repository's `evidence/`, including the Shopify engineering writing that `observed-sh` already holds; the concern map; the class model with all its passes and the accuracy probe; Stage 1's Yemen study; the subjects' other files; Q1 to Q3; the architecture plan, its review and the fitness test; the reports; the handoffs; and 83 of the 88 tools.
