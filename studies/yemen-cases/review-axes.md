# Review of the axes

Past 20 axes, the build writes no cases until the coordinator has reviewed the axes (`brief.md`, "The build", rule 5). The review changes nothing itself: it may only return groups to step 2a, naming the rule each one breaks.

This file names an `axes.tsv` in full by its sha256 only when the review lets it through. That full name is what lets the build write cases. A review that returns groups names the file by a shortened sha256.

## First review, 17 October 2026: 128 groups returned

- **Reviewed:** `axes.tsv` at commit `40a11e7`, sha256 `cad03aa3…ca79`. It has 253 axes; `constants.tsv` has 308 constants.
- **Drafted by** two agents at `max`, one for YA-01 to YA-126 and one for YA-127 to YA-253. Their drafts are in `review/`: `returns-1.tsv`, `returns-2.tsv`, `review-notes-1.md` and `review-notes-2.md`.
- **The coordinator's decision:** every drafted return goes back to step 2a, 142 rows on 128 groups. A sample was checked against the rows' own words, and each names a rule its group breaks.

  | Rule | Rows |
  | --- | --- |
  | 2, states are alternatives | 96 |
  | 1, one condition | 19 |
  | 4, places | 14 |
  | step 2b's label rule | 11 |
  | 5, grouping | 2 |

- **What most returns share.** The states add up rather than replace each other, so the build's latest state drops facts that still hold. Examples:
  - bans and designations that each name only the parties they add;
  - requirements a circular adds;
  - a law and its regulation;
  - a party's pages on one date.

  The same states also give disputes that no source makes: 20 of the 34 `disputed` parts in today.
- **Rulings from rule 2, added to the brief:**
  - lists that grow, instruments in force together, and parts of one source: each addition, instrument or fact is its own condition;
  - rows that state one thing at different detail share the label of what both state. The rest goes in `note`.
- **Disputes the sources make stay.** `review/review-notes-1.md` lists them, such as fixed against floating in the government's area in February 2026.
- **Noted, not returned:**
  - The seatless `Central Bank of Yemen's area` leaves stale or doubled parts in today. The seat rule allows it, unless a cited source gives the side.
  - A year-only date ties with every date in its year, under the brief's precision rule. Where such states can't hold together, the dispute stands.

## Second review, 17 October 2026: 38 returns on 37 axes

- **Reviewed:** `axes.tsv` at commit `71ab056`, sha256 `0b7ef7ad…03aa`, after step 2a's fix round: 728 groups, 241 axes and 487 constants.
- **The review covered** the 116 axes that rest on rows of the first review's returned groups. The same two agents reviewed them: 71 axes from YG-001 to 223, and 45 from YG-224 to 561.
- **What it found:**
  - every first-round return was followed, or step 2a's reason for not following it holds under the brief;
  - every split kept each condition whole;
  - 38 returns remain, on 37 axes. Their drafts are `review/returns-1b.tsv` and `returns-2b.tsv`, and each reviewer's notes have a "Second review" section.

  | Rule | Rows |
  | --- | --- |
  | step 2b's label rule | 21 |
  | 2, states are alternatives | 11 |
  | 1, one condition | 3 |
  | 4, places | 2 |
  | 5, grouping | 1 |

- **Most of the label returns** are a figure or a list given with and without its detail, under the brief's new label line.
- **Disputed parts left in today:**
  - three are made by their sources, and stay;
  - one is a tie under the precision rule, YA-01's, and stays;
  - two are made by no source: Cash's hours (YA-225) and the wallet counts of 11 July 2026 (YA-226). They are returned.
- **The coordinator's decision:** all 38 go back to step 2a. A third review checks only the axes they change.

Cases stay unbuilt until a review lets an `axes.tsv` through.
