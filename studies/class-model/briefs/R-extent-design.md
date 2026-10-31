# The final review of the extent, brought up to the held pass: its design, for the coordinator (31 October 2026)

**What this is.** `briefs/R-extent.md` and `method/review_select.py` were written on 30 October and inspected (`inspection-Q3R.md`, part 2) before the held pass existed. This note says how both now read the model as it is, and what the steps before the final review hand it: the held pass's second stage, the qualities pass and the omission review. It gives the selection's counts per reason, the estimate, the split into agents, the rulings it adds and the open questions. Counts are facts from the files, run on the working tree at `c7224109` (with `reports/GM-rulings.md` as it stood there, being edited); estimates are assumptions, marked.

## 1. What changed, and why

**The selection, `method/review_select.py`:**
- **Kept** every reason of 30 October: `kind`, `count`, `none-held`, `role`, `terms-homonym`, `own-service`, `scope`, `strained`, `flag`, `coordinator`, `lead`, `q3`, `point` and `sample`, with the inspection's fixes (R-1 to R-14). Each still asks where an error would change a kind or a count.
- **Changed, because the held pass grew the merge's questions.** `flags.tsv` went from 175 flags at `9d204b46` to 3,467 (`counted twice` 55 to 2,324, `one capability?` 15 to 1,038). Run as written, the 30 October script selects 2,602 items on today's model, 1,159 of them flags.
  - `one capability?` is read whole where a pair shares five terms or more (`--one-cap-terms`), where one side is a capability made since 30 October, or where the pair was flagged then. A seeded tenth of the other 899 is read. A duplicate made by the held pass's new things is the likeliest kind.
  - `strained?` flags join their capability's `strained` item.
  - The counted-twice flags with no cell resting on them alone stay one item, as the inspection's R-3 asked. Their text now reads "so it counts in each" (M-6).
- **A capability's questions are one item.** A flag, a strained landing, a lead, a Q3 row and a point on one capability are read together, as a cell's reasons already were. A part's notes lines that name the coordinator but no row are one item per part.
- **The parts' evidence rows amended from the held pass** (key `XX-E-…`) aren't taken by the parts' coordinator mark. Their mark comes from the line's own reading, and the held lines' `coordinator` reason reads them by risk.
- **New reasons,** each in section 2: `changed`, `new-cap`, `ruling`, `batch`, `s2-lead`, `s2-note`, `ql-note` and `omission`. The held lines' corrections and alignments join `coordinator`, and the held notes' lines for the final review join `lead`.
- **What the steps before it already read isn't read again:**
  - a none-held cell the second stage read and left holding nothing (`held/<platform>/s2-outcomes.tsv`: `not-found`, `not-held` or `absent`) leaves `none-held`, since the omission review samples those rows (its group 5) and measures the second stage's miss rate (`--none-held-all` keeps them);
  - the cells and entries the omission review's items name leave `sample` and `batch`, as the method report, section 18, says: "the final review's selection doesn't read again what the omission review sampled".
- **The tools:**
  - `--out` writes the selection elsewhere, for a test;
  - `--since` names the merge of 30 October;
  - `--platform-sample P=F` raises a platform's sample, the omission review's decision 13;
  - `--thin R=F` keeps a seeded fraction of the items a reason alone selects, the lean selection of section 3;
  - `check` accepts held entry ids (`ZD-E-…`, `…@<batch>`) in `basis`, and corrections to the held pass's, the second stage's, the omission review's and the qualities pass's files;
  - `rates` counts the verdicts by reason, and the omission review's own miss rate with its Wilson interval;
  - the summary prints each reason's count, the items it alone brings and their cost, the batches per share, and each high-weight ruling's lines and sample.

**The brief, `R-extent.md`:**
- It reads the held pass's lines, their entries, their batches' notes, the rulings in `GM-rulings.md`, `review-H-rulings.md` and the digests, and the second stage's, the qualities pass's and the omission review's files.
- It quotes the rules each reason applies from their sources, as `PLAN.md`, section 3, asks: B-extent's supports (lines 114 to 118), its conventions (lines 131 to 152), "One thing, one domain" (line 67), `H-held.md`'s rule 4, the second stage's S2-R2 and the qualities pass's QL-R8.
- Its eight new reasons each ask one question. A `ruling` item asks two: is the ruling applied as its source words it, and does the line hold by B-extent? A `held` verdict of the omission review is read blind first.
- Its outputs take held lines in `basis` and `correction`. Its findings list each ruling found misapplied, or found to depart from B-extent.
- It adds the 200,000-token stop that the second stage's and the qualities pass's briefs have.

## 2. The reasons and their counts

Run read-only on the working tree at `c7224109`: `python3 -I method/review_select.py --out <scratch>/selection-real.tsv`. **1,599 items, 1,201 of them on one platform, in 55 batches of 30.** "Alone" is the number of items that reason alone selects, which leaving it out would save.

| Reason | What it selects | Items carrying it | Alone |
| --- | --- | --- | --- |
| `coordinator` | the parts' rows, notes and `scope.tsv` rows the coordinator wrote or changed. Also the held lines naming the coordinator's check, correction or alignment: all 39 where an error could move a count (the cell doesn't count, or counts only through such lines), and a seeded third of the other 701 | 433 | 195 |
| `strained` | 132 capabilities with strained landings, with the merge's 87 `strained?` flags | 166 | 60 |
| `count` | held cells of a class placed neither `core` nor `own-service` | 161 | 118 |
| `none-held` | none-held cells with leads in the concern map. Before the second stage lands, all of them; after, only those it didn't read | 155 | 146 |
| `batch` | one seeded line of each of the 181 batches, from the lines no other reason took | 141 | 40 |
| `own-service` | every `own-service` cell | 135 | 35 |
| `changed` | 127 cells whose counting changed since `9d204b46`, and the changed cells of the 10 capabilities whose kind changed (9 slot to class, 1 open to class) | 130 | 58 |
| `kind` | the one counting cell of a class of count 1; every cell of a slot or an open | 123 | 72 |
| `role`, `terms-homonym` | joins on role; joins on a homonym | 117, 3 | 46, 2 |
| `new-cap` | every cell of the 20 capabilities made since `9d204b46` (16 from the held pass's new things, 4 from the points' and Q3's amendments), and the changed cells of the 7 widened | 109 | 68 |
| `flag` | `one capability?` by risk (139 pairs and a tenth of 899), 18 `ruled differently`, 15 counted twice with a sole support, the one loose item | 104 | 28 |
| `ruling` | for each of 25 high-weight rulings from the held pass on that a held line names, one line per platform it reaches, then up to 4, or 2% of its lines: 141 lines | 103 | 24 |
| `s2-lead` | 105 of the 657 leads naming only held cells, which name a maker, a support value a cell lacks, or a quality | 99 | 66 |
| `q3` | Q3's candidate misses, unclear rows, beyond-the-class rows the model doesn't answer, a tenth of its covered rows | 93 | 70 |
| `sample` | a seeded 5% of each part's other cells, at least 2 | 83 | 83 |
| `lead` | parts' and held notes' lines for the final review; inventory-only capabilities | 70 | 27 |
| `point` | conflicted points, and a tenth of the landed | 28 | 4 |
| `scope` | classes under a plan, a beta or one store | 5 | 3 |
| `s2-note`, `ql-note`, `omission` | nothing yet: their inputs don't exist (the summary says so) | 0 | 0 |

**Each high-weight ruling's lines** (the summary prints them). The counts by handle match `GM-rulings.md`'s own:
- 348 lines for the cards left to apps (M-3, M-7);
- 396 for the first-party app (the ruling after SH-55);
- 444 for the staff permission (the ruling after ZD-7);
- 451 for containers (M-13);
- 425 for a thing an entry names (M-6);
- 479 for a route's own gates (an ancestor's gate named by script);
- 287 for the maker field (`is_built_by_wc` or `made_in_woo`);
- 526 for flags, badges and release states.

Five rulings take their lines by a pattern of their own words, not a handle, each a reading (`RULING_PATTERN`): flags, `llms.txt`, a route's own gates, the maker field, and the new things' capabilities. The Editions digest's high rows sample only Editions batches. Two high entries that no held line names, the qualities pass's and the cheapest step's, are listed as such.

**What the steps before it will change** (an assumption, to be counted when the selection runs):
- `none-held` falls by up to 146, as the second stage reads every none-held cell;
- `changed` rises by each cell the second stage, the qualities pass's `shows` rows or the omission review make count;
- `omission` adds about 80 to 120 items. That assumes the omission review's phase 1 of about 550 to 800 items (`O-omission-design.md`, section 3.2), with about 5 to 10% that don't land and a tenth of about 400 to 500 `held` verdicts;
- `s2-note` and `ql-note` add a few tens.

That gives about **1,550 to 1,800 items** when the selection runs.

## 3. The estimate (an assumption)

**The rate.** No review item has been measured. The nearest measured work is a held entry: since 14:00 on 31 October most batches ran at 120,000 to 225,000 tokens an entry, and a structure's first batch up to 303,000 (`method-report.md`, section 18). The 30 October assumption was 0.2 to 0.3 million an item, at the mapping's rate (section 14). An item here reads a cell and its evidence, which now averages about 17 rows a cell (31,927 rows over 1,835 cells), and some cells run to hundreds of held lines. So the assumption is 120,000 to 250,000 tokens an item. The coordinator's checks add 13 to 24% (section 18's measured shares), and its corrections are mostly scripted.

| Selection | Items | Reviewers' agents | With the coordinator's checks and corrections |
| --- | --- | --- | --- |
| Now, in full | 1,599 | 192 to 400 million | about 220 to 500 million |
| When it runs, in full (section 2's assumption) | 1,550 to 1,800 | 185 to 450 million | about 210 to 560 million |
| Lean: `--thin` at a half for `coordinator`, `strained`, `role`, `q3`, `none-held` and `lead` (measured now) | 1,328 | 159 to 332 million | about 180 to 410 million |

**Against the projection:**
- At about 21:00 the final review and its corrections were projected at 180 to 230 million (`method-report.md`, section 18), and the brief's revision and inspection at 30 to 50.
- The full selection's top is about twice that. Even its bottom reaches the projection's top only at the lowest rate.
- The extent's top was 6.9 billion. If the review costs the full selection's top, the extent passes 6.9 billion. Under the founder's rule as the qualities pass's decision 12 restates it, the projection then goes to the founder.

**What keeps it down,** none of it reading less evidence:
- the first batch of each of shares 1 to 4 is measured before the rest run (section 4);
- a reviewer stops at about 200,000 tokens of context and a fresh agent continues, since a batch's cost grows faster than its length (section 18: "an entry's reading stays in the context every later request reads");
- the items group a cell's or a capability's reasons, so each cell's evidence is read once;
- what the second stage and the omission review read isn't read again.

## 4. The split into agents

- **Shares** are the domains' groups, as on 30 October: 1 (A, B), 2 (C), 3 (D), 4 (E, F, G). A fifth holds the items on no capability: held lines placed `out` or on a new thing not yet decided, Q3's rows on none, the loose flag. Now: 343, 386, 276, 479 and 115 items, in 12, 13, 10, 16 and 4 batches.
- **A batch is 30 items, run by one fresh agent** at effort `high`, the founder's floor for reviewing and judging. It writes `review/coverage-<share>-<batch>.tsv` and `findings-<share>-<batch>.md`, and runs `check` until it prints no problem.
- **The order,** up to four agents at once (the founder):
  1. Batch 1 of shares 1 to 4 together, measured per item with `method/count_tokens.py`, and checked by the coordinator, by the checker first. If the measured top puts the review past the projection, the coordinator re-projects before the others run (open question 1).
  2. The other batches, four at a time, share by share, so one share's findings can correct a pattern before its later batches.
  3. Share 5 last. Its `out` lines are the ones the omission review's group 6 also samples.
- **That each made none of the model:**
  - **by construction:** each agent is spawned new with the brief alone. No agent that wrote a part, a batch, a second-stage, qualities or omission row, an amendment, a ruling or the veto list's drafts is resumed or given the task. The coordinator only checks;
  - **by record:** `review/agents.tsv` holds each batch's agent id and the time it was spawned, and `count_tokens.py`'s list of transcripts shows that none is one that wrote under `parts/`, `held/`, `omission/` or `qualities/` (as `O-omission-design.md`, section 6, does).
- **The time:** two agents ran about 70 million tokens an hour (section 18). Four at once, the full selection takes about 3 to 6 hours of running, besides the checks.

## 5. How it was tested

- **On the real repository, read-only.** `review_select.py --out <scratch>` wrote only its output, and `studies/class-model/review/` doesn't exist after the runs. The counts above come from those runs. `--help` was read before the change and after it.
- **On fixtures** (`R-revise/tests/make_fixture.py`, `test_review_select.py` in the coordinator's scratchpad), with `CLASS_MODEL_DIR`, `GM_RULINGS` and `--since-dir`. The fixtures are a model of four capabilities on five platforms with:
  - a capability made since 30 October, one widened and a cell newly counting;
  - two held batches and a calibration batch, with lines naming M-3, the ruling after ZD-7, E80, N12 by its new capability, the coordinator's correction, a coordinator's ruling only, and a script's line;
  - held notes with second-stage leads and a line for the final review;
  - a second stage's notes with an S2-R2 section, and its `OM-ZD.tsv` finding rows;
  - a qualities pass's notes with a QL-R8 section;
  - the omission review's items (a `support` miss, an `out` miss, `unclear`, `absorbed`, `new`, `not a thing` and 20 `held`);
  - a `GM-rulings.md` with high and medium entries before and after the held pass, and a digest table.

  **41 tests, all passed.** Each reason selects what it should and leaves what it shouldn't:
  - **`changed`, `new-cap`:** a cell that now counts, every cell of a capability made since, and a widened capability's changed cell only;
  - **`ruling`:** each high ruling's line; N12 through the new thing decided onto its capability; a digest row within its structure's batches only; never a calibration's line, a medium ruling or one before the held pass; a high ruling no line names, reported;
  - **`coordinator`:** the correction, but neither the ruling-only line nor the script's;
  - **`s2-lead`:** a two-cell lead with a maker as one item, and a quality lead; neither a lead with no risk words nor one on a cell holding nothing;
  - **`s2-note`, `ql-note`:** the bullets of their sections only;
  - **`omission`:** `support`, `out`, `unclear` and `absorbed` (on the capability), the `held` tenth (2 of 20), and an OM- `core` finding; not `new`, `not a thing` or a `shows` finding;
  - **`batch`, `sample`, shares:** a line of each batch; no sampled cell the omission review read; `--platform-sample`; share 5 for no capability;
  - **`check`, `rates`:** `check` passes held ids and a held correction, and refuses a bad severity, an unknown held id, a bad correction and a stray item; `rates` gives the omission review's miss rate.
- **Not tested:** the selection on the second stage's, the qualities pass's and the omission review's real files, which don't exist yet. Their formats are taken from their briefs (`S2-held.md`, "Output"; `QL-qualities.md`, "Output"; `O-omission.md`, "The rows") and from `s2_held.py`'s `HEAD` and `leads_of`. `om_sample.py`, not yet built, may record `absorbed` in a column of its own: the script finds the word in any field of an items row (open question 8).

## 6. The rulings this adds, for the founder's veto

- **`R-R1`, a ruling applied faithfully can still be wrong.**
  - *Decides:* a `ruling` item is `wrong` where the line departs from B-extent's supports, even when it applies its ruling as worded. The finding names the ruling.
  - *Why:* the held pass's dry run found that "55% of its misses came from a brief that restated the model's rules loosely" (`PLAN.md`, section 3).
  - *Risks:* reviewers re-argue settled rulings.
  - *Instead:* test only the ruling's application.
- **`R-R2`, the omission review's `held` verdicts are read blind.**
  - *Decides:* the reviewer decides what the item states before reading the row's basis.
  - *Why:* the omission review's own `reveal` does the same for the second stage's rows (`O-omission-design.md`, section 6). Without it, the measured miss rate is biased low.
  - *Instead:* read the row first.
- **`R-R3`, the second stage's none-held cells are left to the omission review's sample.**
  - *Decides:* a cell the second stage read and left holding nothing isn't selected by `none-held`.
  - *Why:* the second stage reads every such cell, and the omission review measures its misses.
  - *Risks:* a concern-map lead the second stage didn't weigh goes unread, unless the omission review samples it.
  - *Instead:* `--none-held-all`, about 146 items more.
- **`R-R4`, the coordinator's held lines by risk.**
  - *Decides:* all where an error could move a count, and a seeded third of the rest.
  - *Why:* the other 701 sit on cells that count through lines the coordinator didn't touch.
  - *Instead:* all 740, about 70 items more (`--coord-rest 1`).
- **`R-R5`, `one capability?` by shared terms.**
  - *Decides:* five or more shared terms, a capability made since, or flagged on 30 October, read whole; a tenth of the rest.
  - *Instead:* all 1,038, about 900 items more.

## 7. Open questions, each with a proposed answer

1. **The cost.** The full selection's estimate is about twice the 180 to 230 million projected. *Proposed:* run in full; measure the first four batches; re-project; and send the projection to the founder if the extent's top passes 6.9 billion. Thin only on the founder's word. That follows the founder's standing decision of 27 October: "The budget must never cost evidence about the references". *The alternative:* the lean selection now (section 3), 1,328 items.
2. **The rulings before the held pass** aren't sampled by `ruling`. *Proposed:* their applications are tested by the reasons that read their cells: an own interface (C1) and a staff permission (S7) by `count`; the maker rules (C5, the provider statement) by `own-service`; one thing, one domain by `kind` and `one capability?`; a statement counted once or in each by `flag`; the subjects' points by `point`; the unclear pairs by `flag`'s `ruled differently` and `role`; nothing held by `none-held`; inventory ids by `lead`.
3. **The ruling sample's size:** one line per platform, then up to 4 or 2%, 141 lines in all. *Proposed:* as is. A ruling misapplied on one platform shows in its platform's line, and a misapplication found sends that ruling's other lines to the coordinator's script check, not to more review. *The alternative:* 5% (about 330 lines).
4. **The batch sample:** one line per batch. *Proposed:* as is, since the batches were each checked by the coordinator and the checker. *The alternative:* two (about 40 items more).
5. **`s2-lead`'s qualities.** The second stage's decision 1 defines risk as "a maker, a support value the cell lacks, or a quality", but qualities are the qualities pass's. *Proposed:* keep them. The reviewer answers whether `qualities/` holds the quality, and whether a placement moves.
6. **When it runs.** *Proposed:* once, after the omission review's batches and the second stage's `S2-NEW` part are applied, the qualities pass landed and the model merged, with `reports/GM-rulings.md` at the same commit. The selection's commit is named in each reviewer's message.
7. **The inspection.** The brief and the script changed after their inspection, so `PLAN.md`, section 3, asks for another. *Proposed:* an agent that made none of them inspects both, at `high`, on the real files and these fixtures, before the selection runs: about 10 to 20 million of the 30 to 50 the projection holds for this step (an assumption).
8. **The omission review's `absorbed`.** *Proposed:* the build of `om_sample.py` says in which column the walk's flag lands. The inspection confirms the reason reads it.
9. **`review/agents.tsv`,** for the record of independence (section 4). *Proposed:* the coordinator writes it as each batch is spawned, as `omission/parts.tsv` does.
