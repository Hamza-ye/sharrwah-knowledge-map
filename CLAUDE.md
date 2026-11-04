# Read first

**What this repository is:** the work of shaping Sharrwah, a merchant platform built on Shopify's model. `PLAN.md` governs it. It is the plan the founder accepted on 3 November 2026, with its amendments.

**The working files.** Only these govern:
- `PLAN.md`: the plan, with its stages, method and risks, the founder's decisions and when each is needed, and how the work is organised and cited.
- `decisions/founder.tsv`: the founder's decisions (FD-n), each in words the founder approved.
- `STATE.md`: where the work is. `python3 -I method/status.py` generates it from `work.tsv` (the work items, W-n) and `risks.tsv` (the risk register, RISK-n). Never edit it by hand.
- `decisions/first-decisions.md`: the first architecture decisions and the evidence on each, an input to stage 2.
- `method/`: the tools.
  - `corpus_search.py` searches Shopify's held evidence.
  - `check_report.py` checks each quote against its pinned source.
  - `count_tokens.py` counts what a run cost.
  - `status.py` generates `STATE.md`.
  - `quote_check.py` and `runs_corpus.py` serve them.
- **The evidence:** Shopify's evidence repository, observed-sh, cloned read-only at `/home/user/observed-sh`. Read it through its own guides first: `README.md`, `docs/READING.md`, `structures/REGISTER.tsv`, `index/` and `docs/GAPS.md`.

**Nothing else governs.** The work from before 3 November 2026 is in the history, at the commit `README.md` names. It doesn't bind, and it isn't read for the work.

**The coordinating session:**
- Read `PLAN.md`, `STATE.md` and `decisions/founder.tsv` first. Then continue from the current stage's open items in `work.tsv`.
- Regenerate `STATE.md` after every change to `work.tsv` or `risks.tsv`.
- At the top of each reply to the founder, state your reading of their message, so they can correct it.
- Only the founder's decisions go in `decisions/founder.tsv`, in words the founder approved. Don't copy the founder's messages into the repository unless they ask.
- Bring the founder only genuine founder decisions, one at a time, each with a recommendation.
- Nothing stays because it cost something. Keep only what a decision needs now, and create each piece when its stage first needs it.

**Legal matters are the founder's.** Don't raise legal concerns in the work, put them into the evidence capture, or turn them into decisions. The founder consults a lawyer. Where the platform needs legal content, the founder supplies it.

**Evidence capture serves the decisions.** Capture when a gap could change a decision that is coming up, or when an observation would be lost if it isn't taken now. A capture tool found faulty is fixed before the next capture. A capture request is an issue on `Hamza-ye/observed-sh`, for its local agent. It states:
- what to capture;
- why: the decision it could change;
- how;
- what must be visible for the capture to count;
- when it expires.

**An agent working from a brief:** read only your brief and what it names.

**Everyone:**
- The evidence repositories on this machine (observed-sh, observed-sa, other-product-class) are read-only. Never commit or push to them, or to this repository's branch `evidence/other-product-class`. Opening an issue on observed-sh is allowed.
- Run Python that reads evidence with `python3 -I`.
- The founder's words are never evidence of what a platform does. The founder's choices are decisions, not claims to verify.
- Every claim is one of three:
  - a fact, traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- Evidence that contains credentials, cookies or tokens is read, cited and used like any other evidence, including to check how a mechanism works. It comes from environments and accounts made only for capture. Don't redact it or avoid capturing it. Cite it by locator; Sharrwah's own documents don't need the values.
