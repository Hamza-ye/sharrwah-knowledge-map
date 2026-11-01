# Read first

**What this repository is:** the work of shaping Sharrwah, a merchant platform built on Shopify's model (the founder's decision of 1 November 2026). `PLAN.md` governs it.

**The working files.** Only these govern:
- `PLAN.md`: the plan.
- `STATE.md`: where the work is, and the next step.
- `founder-decisions.tsv`: the founder's decisions, with `founder-messages/` for the messages some of them cite. Every decision before 1 November is marked for review (its last column). It binds until the review says otherwise.
- `studies/subjects/S-01/decision-1.md` and `register.tsv`, and `studies/subjects/S-02/decisions.md` and `register.tsv`: Decision 1 and the rulings on what a market is. Both are under review.
- `method/`: five tools.
  - `corpus_search.py` searches Shopify's held evidence: `python3 -I method/corpus_search.py shopify TERM ... --brief --max 3`.
  - `check_report.py` checks each quote against its source.
  - `count_tokens.py` counts what a run cost.
  - `quote_check.py` and `runs_corpus.py` serve the first two.
- `HISTORY.md` and `INVENTORY.md`: how the repository got here, and what stays and why.
- **The evidence:** Shopify's evidence repository, observed-sh, cloned read-only at `/home/user/observed-sh`. Read it through its own guides first: `README.md`, `docs/READING.md` and `index/`.

**Nothing else governs.** Everything that left the working files is in the history, at commit `9f3749d0`. Use it only through a link pinned to a commit in a working file, and only for what that link says it is for.

**The coordinating session:**
- Read `PLAN.md`, `STATE.md` and `founder-decisions.tsv` first, then continue from `STATE.md`'s next step.
- At the top of each reply to the founder, state your reading of their message, so they can correct it.
- Only decisions go in `founder-decisions.tsv`, in words the founder has approved. Don't copy the founder's messages into the repository unless they ask.
- Nothing stays because it cost something. Keep only what a decision needs now.

**An agent working from a brief:** read only your brief and what it names.

**Everyone:**
- The evidence repositories on this machine (observed-sh, observed-sa, other-product-class) are read-only. Never commit or push to them, or to this repository's branch `evidence/other-product-class`.
- Run Python that reads evidence with `python3 -I`.
- The founder's words are never evidence of what a platform does, and the founder's choices are decisions, not claims to verify.
- Every claim is one of three:
  - a fact, traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence. They come from synthetic environments the founder rotates.
