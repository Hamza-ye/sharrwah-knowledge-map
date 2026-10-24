# History

How this repository reached its current state. Each **baseline** below is the commit at one of the founder's decision points or at a planned pause. Open a baseline to see the repository as it stood, and compare two to see what changed between them. `STATE.md` says what is settled, open or superseded now. This file says where each part came from.

On GitHub, commit `abc1234` opens at `https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/abc1234`, and the changes between two commits at `…/compare/abc1234...def5678`.

## Before PR #4

| Date | What | Where | On `main` |
| --- | --- | --- | --- |
| 10 Oct | The founder's earlier work, brought in: the payments studies, the Yemen setup options and the payment rows | `caad5aa` | Yes |
| 10 Oct | Yemen's cited sources and the pinned wallet clients | PR #1 | Yes, merged |
| 10 Oct | The payment seam in `NEXT.md`, Sana'a sources, and the fetch list for inside Yemen | PR #2 | Yes, merged |
| 10 Oct | The payment seam study, the frame (`method/frame.md`) and the founder's first decisions (`decisions/founder.md`) | PR #3, ending at `8946887` | Its commits, through `968cc8a`; its files, no |

**PR #3** was closed without merging on the evening of 10 October, when the work restarted from `main` as PR #4. Commit `968cc8a` records PR #3's commits in this history, using git's "ours" merge, so they stay reachable without their files being taken in.

Its `decisions/founder.md` holds the founder's decisions F-00 to F-06 and one open question, O-01: which legal entity and domicile contracts with sellers and partners. Some of these reached the later record in other words. For example, `PLAN.md` section 1 says "Yemen is the first market, not the design target". The others are not in `founder-decisions.tsv`. To read them: `git show 8946887:decisions/founder.md`.

## PR #4: 10 to 24 October

| Baseline | Commit | Date | What it holds | The founder's decision on record | Changes since the previous baseline |
| --- | --- | --- | --- | --- | --- |
| G0 | `5468e7b` | 12 Oct | Q1's five-platform concern map, and `PLAN.md` | `founder-decisions.tsv`, G0 | [`c12d171...5468e7b`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/c12d171...5468e7b) |
| Map frozen | `3e5b37b` | 12 Oct | Stage 0: the concern map checked against what is held, and frozen | | [`5468e7b...3e5b37b`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/5468e7b...3e5b37b) |
| G1 entry | `e4d5cee` | 17 Oct | The pilot, S-01: `studies/subjects/S-01/entry.md` (14 decisions, with the coordinator's recommendations), `review.md` and `method-report.md`. Stage 1's Yemen axes and cases. | Waiting for the founder | [`3e5b37b...e4d5cee`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/3e5b37b...e4d5cee) |
| G1 answer | `cc96b2b` | 18 Oct | The founder's answer to G1 | `founder-messages/2026-10-18-g1-answer.md`; `founder-decisions.tsv`, G1 | [`e4d5cee...cc96b2b`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/e4d5cee...cc96b2b) |
| Re-frame go | `7fec7f0` | 18 Oct | The plan change, with the founder's five changes; `PLAN.md` re-framed | `founder-decisions.tsv`, 18 Oct | [`cc96b2b...7fec7f0`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/cc96b2b...7fec7f0) |
| 19 October decisions | `35b50a8` | 19 Oct | The areas list with the founder's marks (G2), and the drafting decisions | `founder-decisions.tsv`, 19 Oct | [`7fec7f0...35b50a8`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/7fec7f0...35b50a8) |
| Drafts revised | `77c4849` | 24 Oct | All eight drafts, written and revised | | [`35b50a8...77c4849`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/35b50a8...77c4849) |
| Paused | `32653ac` | 24 Oct | R5's checks stopped at the founder's question. The files of the 16 stopped runs are kept as they stood, unchecked. | `STATE.md` | [`77c4849...32653ac`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/77c4849...32653ac) |
| Method proposed | `b78686e` | 24 Oct | `METHOD.md`, proposed | Accepted by the founder on 24 October, recorded in the next pull request | [`32653ac...b78686e`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/32653ac...b78686e) |

**PR #5,** the founder's BigCommerce Help Center capture, was merged into this branch by `4723d64`, then closed.

## How history is kept from here

- **Nothing is rewritten:** no squash, rebase or force-push on a shared branch. Documents cite commits by hash, and rewriting would break those citations.
- **One pull request per milestone.** Each one closes with its milestone report, is merged into `main` with a merge commit, and gets a row here.
- **Superseded work stays in history.** `STATE.md` marks what is settled, open or superseded. Nothing is deleted to mark it.
- **Named by commit, not by tag.** This session's git access can push its working branch but not tags, so the baselines are named here by commit. A session or person allowed to push tags can turn each row into one.
