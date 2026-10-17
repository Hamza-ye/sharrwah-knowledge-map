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

## Third review, 17 October 2026: the axes are let through

- **Reviewed:** `axes.tsv` at commit `f3ed2df`, sha256 `02850db5…2375`, after step 2a's second fix round: 739 groups, 227 axes and 512 constants.
- **The review covered** the 24 axes that round changed. The same two agents reviewed them: 15 axes from YG-001 to 223, and 9 from YG-224 to 561. Their drafts are `review/returns-1c.tsv` and `returns-2c.tsv`, with a "Third review" section in each reviewer's notes.
- **What it found:**
  - every second-round return was fixed;
  - the two returns step 2a didn't follow give reasons that hold under the brief. Item 046 doesn't name who banned the notes, and item 155 never uses "the south" and "government-controlled areas" for one area;
  - one label return remained. In YA-200, YQ-E379 kept "outages up to 20 hours a day" where YQ-E366 and YQ-E436, stating the same outages, read "prolonged outages".
- **The last fix.** Step 2a gave YQ-E379 "prolonged outages", with its figure in `note`. The coordinator checked the result:
  - the join, `--groups` and `--states` run clean;
  - against the reviewed file, only YA-200's `states` and `today` change, by that label.
- **Disputed parts left in today: 10.** Each is made by its sources, or is a tie under the precision rule (YA-01, and YA-227's 8.8 against 10 percent of the population in 2022).
- **The coordinator's decision:** the review lets this `axes.tsv` through, at sha256 47b5c642765d2e25db20f0795fceebbce3e175a6ffdfa884271f005dadf8c735.

## The independent review, 17 October 2026

`review-independent.md`, by an agent that produced none of Stage 1, read a sample of 45 axes against their quotes.

- **What it found.** 12 of the 45 have an error that changes `today` or a case, and 6 of the 23 `in force` cases aren't in force. The rule-based reviews above couldn't see these: wrong `holds` values, a cancellation placed where it supersedes neither side, a later statement left on another axis, and evidence held but not recorded.
- **Its fixes 1 to 5 and 7** go back to step 2a. The coordinator checks the axes they change before the build writes cases again.
- **The coordinator's decisions on the rest:**
  - **6, precision ties.** They stay disputes, as the brief says. Phase D marks a disputed part `unknown`, so no false mark follows. The cases that rest on such a tie aren't treated as in force for marking.
  - **8, stale parts.** Parts for overlapping place names can keep old states in `today`. Until the method changes, phase D reads each part's date in the axis's `note`, and treats a part as stale where a later part names the same ground.
  - **The method change, before Stage 4:** a `within` relation between places, each link on a source, so that a strictly later state supersedes the states at places inside its own. It extends the `across Yemen` rule.

## The fixes from the independent review, checked by the coordinator, 17 October 2026

Step 2a made fixes 1 to 5 and 7. The coordinator diffed the result against the `axes.tsv` let through above, and read each changed `today`.
- **What changed:** axes YA-03, 05, 15, 25, 40, 59, 60, 62 and 64; one new axis, YA-228; one new constant, YK-513. No other axis or constant changed or moved. The join, `--groups` and `--states` run clean.
- **YA-25.** Each side's 2024 ban is now ended at its own area by the July 2024 agreement row that ends it.
- **YA-62.** PayPal reads "Sending from Yemen". The source's "only" stays in YQ-D634's `note` and its quote, under the label rule. Wise is `Unavailable`, no longer disputed.
- **YA-05.** The government's area reads "fixed", from the April 2026 statement.
- **YA-15.** The withdrawal of pre-2016 notes is `provided for`, so the government's area keeps "all notes, new and old, legal tender".
- **YA-40.** The founder unknown is closed from held evidence (YQ-D636, YE-D1000), and its `unknowns.tsv` row is gone.

The coordinator lets this `axes.tsv` through, at sha256 ef7e2d6c70aae0e46218cc95c1dd9e14c15a8beec43428f7fe1e69d1f4837f06.

## The fixes from the check of S-01's axes, checked by the coordinator, 17 October 2026

The independent reviewer checked against their quotes the axes and constants in the pilot's `bears-on.tsv` ("Check of S-01's axes" in `review-independent.md`). Step 2a made its six fixes. The coordinator diffed the result against the file let through above:
- **What changed:** axes YA-62, 126, 128 and 130; constant YK-23; one new constant, YK-514. No other axis or constant changed or moved. The checks run clean.
- **PayPal's receiving** is its own condition, constant YK-514: "cannot receive money @ PayPal's service" (YQ-D634, YE-D997). YA-62 keeps "Sending from Yemen" from YQ-E728.
- **YK-23** reads "personal or humanitarian transfers allowed if the recipient is not on a sanctions list", as YE-D420 says.
- **Zid Pay's** "Unavailable" is placed at "Zid Pay Kuwait (Zid)'s service", the scope of the terms it comes from.
- **YA-130:** Wagbat's label names cash on delivery. **YA-126 and YA-128:** labels that state one thing now share one label.

The coordinator lets this `axes.tsv` through, at sha256 5e2efc31910483b7732065d96bf88306d0194cdee34014746185532c346581f4.
