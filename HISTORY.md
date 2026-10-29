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

Its `decisions/founder.md` holds the founder's decisions F-00 to F-06 and one open question, O-01: which legal entity and domicile contracts with sellers and partners. Some of these reached the later record in other words. For example, `PLAN.md` section 1 says "Yemen is the first market, not the design target". The others are not in `founder-decisions.tsv`. They were restored on 24 October and lapsed at the reset of 25 October (`founder-decisions.tsv`, the reset). To read them: [`decisions/founder.md` at `8946887`](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/894688732f17282d8a268f657aba17b430020fed/decisions/founder.md).

## PR #4: 10 to 24 October

| Baseline | Commit | Date | What it holds | The founder's decision on record | Changes since the previous baseline |
| --- | --- | --- | --- | --- | --- |
| G0 | `5468e7b` | 12 Oct | Q1's five-platform concern map, and `PLAN.md` | `founder-decisions.tsv`, G0 | [`c12d171...5468e7b`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/c12d171...5468e7b) |
| Map frozen | `3e5b37b` | 12 Oct | Stage 0: the concern map checked against what is held, and frozen | | [`5468e7b...3e5b37b`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/5468e7b...3e5b37b) |
| G1 entry | `e4d5cee` | 17 Oct | The pilot, S-01: `studies/subjects/S-01/entry.md` (14 decisions, with the coordinator's recommendations), `review.md` and `method-report.md`. Stage 1's Yemen axes and cases. | Waiting for the founder | [`3e5b37b...e4d5cee`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/3e5b37b...e4d5cee) |
| G1 answer | `cc96b2b` | 18 Oct | The founder's answer to G1 | `founder-messages/2026-10-18-g1-answer.md`; `founder-decisions.tsv`, G1 | [`e4d5cee...cc96b2b`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/e4d5cee...cc96b2b) |
| Re-frame go | `7fec7f0` | 18 Oct | The plan change, with the founder's five changes; `PLAN.md` re-framed | `founder-decisions.tsv`, 18 Oct | [`cc96b2b...7fec7f0`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/cc96b2b...7fec7f0) |
| 19 October decisions | `35b50a8` | 19 Oct | The re-frame's areas list with the founder's marks (that work's G2, not the plan's), and the drafting decisions | `founder-decisions.tsv`, 19 Oct | [`7fec7f0...35b50a8`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/7fec7f0...35b50a8) |
| Drafts revised | `77c4849` | 24 Oct | All eight drafts, written and revised | | [`35b50a8...77c4849`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/35b50a8...77c4849) |
| Paused | `32653ac` | 24 Oct | R5's checks stopped at the founder's question. The files of the 16 stopped runs are kept as they stood, unchecked. | `STATE.md` | [`77c4849...32653ac`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/77c4849...32653ac) |
| Method proposed | `b78686e` | 24 Oct | `METHOD.md`, proposed | Accepted by the founder on 24 October, recorded in PR #6 | [`32653ac...b78686e`](https://github.com/Hamza-ye/sharrwah-knowledge-map/compare/32653ac...b78686e) |

**PR #5,** the founder's BigCommerce Help Center capture, was merged into this branch by `4723d64`, then closed.

**PR #4 was merged into `main`** by `a05974a` on 24 October 2026.

## Milestones from 24 October

Each milestone is one pull request, merged into `main` with a merge commit. Its description is the milestone report. The reports of M0 and M1 are in `reports/` at [commit `4923e1c`](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/4923e1c96a0296abdaf3f5bdbd8c155e09acfebf/reports).

| Milestone | Pull request | Date | What it holds | The founder's decision on record |
| --- | --- | --- | --- | --- |
| M0, the re-baseline | PR #6 | 24 Oct | `METHOD.md` adopted with amendment 1; the founder's decisions of 24 October; F-00 to F-06 and O-01 restored; the backlog, the risk register and the scripts; `STATE.md` on one page; `reports/M0.md` | `founder-decisions.tsv`, 24 October; `founder-messages/2026-10-24-method-accepted.md` and `founder-messages/2026-10-24-approved-plan.md` |
| M1, the money boundary, ended by the reset | PR #7, merged by [`898f882`](https://github.com/Hamza-ye/sharrwah-knowledge-map/commit/898f8823ada9bc67d0e977307aa203096dc54b54) on 26 Oct | 25 to 26 Oct | The work under the method of 24 October, then the reset to the plan as it stood at G1, and what followed it (below) | `founder-decisions.tsv`, 25 and 26 October |

## The reset of 25 October, and what followed

On 25 October 2026 the founder reset the work to the plan as it stood at G1, with the pilot's own changes (`PLAN.md`, section 11).

| Baseline | Commit | What it holds |
| --- | --- | --- |
| Before the reset | [`4923e1c`](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/4923e1c96a0296abdaf3f5bdbd8c155e09acfebf) | Everything done between G1 and the reset: the re-frame's work, the method of 24 October and its amendments, the decision records and their checks, the M0 and M1 reports, and the decisions made on them |
| The reset | [`005bdf1`](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/005bdf1f59d72af53c66aa3d66e6e17aa6306f8d) | The plan as it stood at G1, with the pilot's own changes; the working files only (`CLAUDE.md` lists them). The fixes from its two cold-start tests follow in the commits after it, on the same branch. |
| G1 closed, and S-01 reviewed | [`40a06e7`](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/40a06e7db0da6b14cec31ae09ac039fc818f4fb2) | The founder's answer to Decision 1 (C, with the three defaults) and the pilot's open items ruled; S-01's decision register and its review pack, after an independent review and a check of every quote; Stage 3's draft subject list, at G2. The founder's review of this result follows. |
| G2 answered | [`4787069`](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/4787069026eac0f182598a8478316a82b9334ad1) | The founder's answers after the orientation page: G2, evidence for all ten subjects; E1 and E2 kept; default 2's "never" at launch. The scenario walk added to each subject (`PLAN.md`, section 6, step 7). Merged into `main` with PR #7 |
| S-02 goes on | [`3a013c4`](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/3a013c409d724f0beac4fc66f8c4085e41839a93) | The founder's answers of 27 October: S-02 continues at 700 million, and the budget never costs evidence; evidence a run could capture goes to the local agent as a request (`handoffs/`) |
| The scope of 28 October | [`537ddb7`](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/537ddb771587ce173e930508e3683eaaddc4c995) | The founder's standing decision on markets: MENA, with Yemen one market among them; neither Yemen's present circumstances nor today's capacity becomes a permanent constraint without a justified reason |
| The intent of 29 October | [`9cba321`](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/9cba3217668018f9ba219cf6eb9e291bf4d22ef2) | The founder's intent recorded and folded into the plan: the class's model is the work's base, and its extent comes before architecture (Stage 4A, gate GM). S-02's register re-statused as engineering's rulings, for the founder's veto, follows at [`7920f91`](https://github.com/Hamza-ye/sharrwah-knowledge-map/commit/7920f9123153f613c900d3152726d89120010de4); the fixes from an independent reading of the plan change (`reports/plan-change-check.md`) follow in the commit after it, on the same branch. S-02's end, the night before, is in `reports/S-02.md` and the subject's own files |

## How history is kept from here

- **Nothing is rewritten:** no squash, rebase or force-push on a shared branch. Documents cite commits by hash, and rewriting would break those citations.
- **One pull request per milestone.** Each one closes with its milestone report, is merged into `main` with a merge commit, and gets a row here.
- **Superseded work stays in history.** At the reset of 25 October, the work done between G1 and the reset left the working files, so that no search of them finds it. It is read at its commit. Nothing was rewritten.
- **Named by commit, not by tag.** This session's git access can push its working branch but not tags, so the baselines are named here by commit. A session or person allowed to push tags can turn each row into one.
