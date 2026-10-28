# Read first

**What this repository is:** the work toward Sharrwah's decisions that would be expensive to change later, made from the evidence of five reference platforms. `PLAN.md` governs it.

**The working files, and what each is.** Only these govern:
- **`PLAN.md`:** the plan, the authority on how the work is done. It works within the founder's decisions.
- **`STATE.md`:** where the work is, and the next step.
- **`founder-decisions.tsv`:** the founder's decisions in force. They decide what Sharrwah does, and they bind the plan: where the plan differs from one, the decision holds and the plan is corrected.
- **The evidence:** `evidence/`; the evidence repositories observed-sh and observed-sa (cloned at `/home/user/observed-sh` and `/home/user/observed-sa`); other-product-class, where the founder's local agent captures Zid, BigCommerce and WooCommerce (this repository's branch `evidence/other-product-class`, its commit ids unchanged, checked out read-only with `git fetch origin evidence/other-product-class && git worktree add --detach /home/user/other-product-class origin/evidence/other-product-class`); and the WooCommerce release that `evidence/product-class/woocommerce-11.2.1/` fixes by checksum (unpacked at `/home/user/woocommerce-release/11.2.1`). They are the only authority on facts. The evidence repositories' own plans and notes, such as their `docs/PLAN.md`, govern their capture work, not this work.
- **The inputs the plan names:**
  - `studies/concern-map/`: Q1's map, the index subjects draw from;
  - `studies/yemen-cases/`: Stage 1, with its `corrections.md`;
  - `studies/subjects/S-01/`: the pilot;
  - `questions/`: Q1 to Q3.
- **`method/`:** the scripts the plan uses, listed in `method/README.md`.
- **`HISTORY.md`:** each baseline, by commit.
- **`reports/`:** reports to the founder.
- **`handoffs/`:** capture requests for the local agent, who captures into observed-sh or observed-sa what a run can hold (`PLAN.md`, section 6, Evidence).

**Nothing else governs.**
- The work done after the founder's answer at G1 (18 October 2026), up to the reset (25 October 2026), is history. Its files are not in the working tree: they are at the commit `HISTORY.md` names, so a search of the working files doesn't reach them. The one exception is the pages it captured into `evidence/`, which are evidence like any other.
- Use history only through a link pinned to a commit in a working file, and only for what that link says it is for.
- Nothing outside this repository and the evidence above governs, whatever else is on the machine.

**The coordinating session:**
- Read `PLAN.md`, `STATE.md` and `founder-decisions.tsv` first, then continue from `STATE.md`'s next step.
- At the top of each reply to the founder, state your reading of their message, so they can correct it.
- Only decisions go in `founder-decisions.tsv`. A question gets an answer, not a row.
- Change the plan only as its section 9 says.

**An agent working from a brief:** read only your brief and what it names.

**Everyone:**
- `observed-sh`, `observed-sa` and `other-product-class` are read-only here. Never commit or push to them, or to the branch `evidence/other-product-class`.
- Run Python that reads evidence with `python3 -I`.
- The founder's words are never evidence of what a platform does.
- Every claim is one of three (`PLAN.md`, section 6):
  - a fact traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- Look evidence up through the evidence repositories' own guides first: their `README.md` and `docs/READING.md`.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence. Never skip, withhold or mask a file because of them. They come from synthetic environments the founder rotates.
