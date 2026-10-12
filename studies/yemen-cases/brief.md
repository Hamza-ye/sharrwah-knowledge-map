# Brief: Yemen's axes and cases (Q2, step 1)

This is `PLAN.md` Stage 1. Read only this brief and the evidence named under "Inputs".

**Who does what.** The message that started you names your role.
- **Pass 1** is done by six agents, one per part:
  - A: the founder's pages and any attestations;
  - B: the Sana'a rules run;
  - C: the operators run;
  - D: the cited-sources run, items 1 to 131;
  - E: the cited-sources run, items 132 to 262;
  - F: the community clients, and the OCR text in `derived/`.

  Each reads every source in its part, and nothing else. It writes `pass1/conditions-<part>.tsv` and `pass1/citations-<part>.tsv`, numbering its rows `YQ-<part>001…` and `YE-<part>001…`, and `pass1/notes-<part>.md`.
- **Pass 2** is one agent. It starts after the coordinator has joined pass 1's files into `conditions.tsv` and `citations.tsv`, and it writes everything else. It adds no citation: what pass 1 didn't find goes in `unknowns.tsv`.

A first run stopped early: its cap on axes fired before the evidence was read. This brief therefore works in two passes. Pass 1 reads every source and records its conditions. Only then does pass 2 form axes.

## The task

This is Q2's first step, as agreed with the founder:

> Using only Yemen evidence:
> 1. Identify the axes the market varies along, and build cases on them, with today as the anchor case.

**The market** is commerce in Yemen: the conditions under which merchants sell and buyers pay there.

**Axes come from the evidence alone.** No list of axes is given to you, and none should be assumed.

**Only step 1.** Later steps are done elsewhere, and moves are not cases: don't record them.

**Nothing about what Sharrwah does or should do.** Practices of any party in Yemen are market evidence. Record them like any other.

## Pass 1: conditions, from every source

**Read every source in your part.** The parts, in this order:
1. the founder's pages from inside Yemen, `evidence/yemen/blocked-evidence-founder/`;
2. any attestation in `evidence/yemen/attestations/` besides `TEMPLATE.md`;
3. the Sana'a rules run, `runs/20261010T061420Z-sanaa-rules-search/`;
4. the operators run, `runs/20261010T072550Z-sanaa-operators-search/`;
5. the cited-sources run, `runs/20261010T050304Z-cited-sources/`;
6. the community clients, `runs/20261010T051708Z-community-clients/`;
7. the OCR text in `evidence/yemen/derived/` of any scanned PDF in those runs.

Don't skip a source because it seems minor.

**Record each condition** a source states in `conditions.tsv`, one row per source statement.
- **A condition** is something that a merchant, a buyer, or a party serving them can or must do, or has available, when selling or paying in Yemen.
- **Its size.** Name it at the level of the act or the availability, not of one institution. In the abstract: the condition is "who may do A"; its states are such as "only P" or "P and Q". Positions that hold at one time and place are one state.
- **The same condition.** Two rows are the same condition when they name the same act or availability for the same role. Give them the same `condition` wording, and list each such identification in `notes.md`.
- **The state,** as the source gives it.
- **The place.**
  - A state an authority sets holds for the area that authority governs, as the source names that area. If the source names only the authority, the place is `<authority>'s area`.
  - It holds for the whole market only when a source says so.
  - A state with no place, and no authority setting it, has the place `place not stated`.
  - Two place names are one place only when a single source uses both for the same area. List each such grouping in `notes.md`.
- **When it held:**
  - when the source says it held;
  - for a state the source says still holds, the source's date;
  - for a state given for a range, the range's end;
  - if the source doesn't say, the source's date: effective, otherwise published, otherwise shown;
  - for a live page, one in which a party describes its own current service or rule: the state it presents as current takes the capture date;
  - for any other undated source: no date. An undated state can be the latest only where its place has no dated state.

  `date_basis` says which applies.

## Pass 2: axes, constants and cases

1. **Axis.** A condition the evidence shows in at least two states. Its `condition_ids` list every pass 1 row it rests on.
2. **Constant.** A condition shown in one state only. It goes in `constants.tsv`, with its place.
3. **Stop for review** if pass 2 gives more than 20 axes. Write `axes.tsv` and `constants.tsv`, say so in `notes.md`, and build no cases.
4. **Today.** For each axis, `today` joins the latest-dated state of each place with ` + `. `place not stated` counts as one more place.
   - **Supersession.** A later whole-market state supersedes older place-bound states only when its source says it applies across Yemen.
   - **Precision.** Dates of different precision are compared at the coarser one, so 2024 and March 2024 tie.
   - **Disputed.** Two different states for the same place at the same latest date make that place's part `disputed`. Record both, and don't resolve them.
   - **One source, two states.** When one source gives two states for the same place at once, take the one it says holds now. If it says neither, that place's part is `disputed`.
5. **Today's case, `YC-00`,** puts every axis at its `today`. It is the one anchor case.
6. **Further cases** are built in two ways and no others:
   - **One per non-today state** of each axis, with every other axis at today's state.
     - On an axis whose `today` joins places, a state for a place replaces only that place's part. A state that a source says applies across Yemen replaces every part.
     - A disputed state counts as non-today.
   - **One per combination of states that a single source shows holding at one time.** The axes it doesn't give stay at today's state.

   Skip a case that duplicates another. A case's `name` lists only the states that differ from today, for example `YA-03=<label>`.
7. **Basis** of a further case, the first that applies:
   - `in force`: it holds now, somewhere in the market;
   - `occurred`: it held at some time;
   - `provided for`: an enacted law or an issued decision provides for it.
8. **State labels.** A label is short and in English, with the source's own words in parentheses where it has them, and ` @ <place>` when it holds for a place. Use the same label everywhere.

## Inputs

**Read and cite only files under these folders:**
- **`evidence/yemen/blocked-evidence-founder/`.** Pages the founder saved from inside Yemen on 10 October 2026, as single-file HTML, with a `manifest.tsv`.
- **`evidence/yemen/runs/`.** Four runs.
  - In three of them, `manifest.tsv` names each item's readable text in its `text_file` column.
  - The community clients run, `20261010T051708Z-community-clients/`, has `clients.tsv` instead, with one folder per repository. Read each one's README and source for what it offers and what it requires.
  - Each run's `README.md` says where it was fetched from.
- **`evidence/yemen/derived/`.** OCR text of scanned PDFs. When you quote one:
  - cite the OCR text file;
  - name the PDF and its run in `locator`;
  - give the PDF's address in `url`;
  - give that run's `fetched_from`.
- **`evidence/yemen/attestations/`,** for any attestation besides `TEMPLATE.md`. Cite it with `fetched_from` set to `attestation`, its date as `source_date`, and an empty `url`.

**Don't open:**
- `evidence/yemen/README.md` and `evidence/yemen/finding-aids/`;
- `studies/yemen-cases/first-run-stopped/`;
- `yemen-setup-options/`, `register/`, `model/`, `shopify-payments-study/` and `questions/`;
- the rest of `studies/`, except your own output folder;
- `NEXT.md`, `PLAN.md` and `STATE.md`.

## Quotes and citations

- **Quotes are verbatim:** at most 300 characters, with no ellipses, and within one paragraph of the source. Arabic stays as written.
- **How the checker matches.** It collapses whitespace, removes HTML tags and decodes entities, on both sides.
- **`source`** is `sharrwah-knowledge-map@<commit>:<path>`, where `<commit>` is the output of `git rev-parse HEAD` when you start.
- **`locator`** is the heading, or the line number in the cited file.
- **`fetched_from`** is `inside Yemen` or `outside Yemen`, from the run's README, or `attestation`.
- **Disagreements.** Where sources disagree, record each with its citation.
- **Credentials.** Evidence that contains credentials, cookies or tokens is read and cited like any other evidence. Never skip, withhold or mask a file because of them. They come from synthetic environments the founder rotates.
- **No inference** in any condition, axis, state, constant or case, and none in notes.

## Unknowns

Record in `unknowns.tsv`:
- every axis whose `today` no source shows;
- every state a case needs that no source shows.

For each, list what you read looking for it: each path, and whether you could read it.

Name who could close it:
- `agent`: a source online;
- `founder`: a source reachable only from inside Yemen;
- `reader`: a held file that couldn't be read.

## Output, in `studies/yemen-cases/`

All files are tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field. Write the files as you go: if you are interrupted, the next run continues from them.

| File | Columns |
| --- | --- |
| `conditions.tsv` | `condition_id` (YQ-A001…, by part) · `condition` · `state` · `place` · `held_at` · `date_basis` · `cite_ids` · `note` |
| `axes.tsv` | `axis_id` (YA-01…) · `axis` · `what_varies` · `condition_ids` · `states` (`label [YE-001, YE-007] \| label @ place [YE-010]`) · `today` (state labels joined by ` + `, with `disputed` or `unknown` where they apply) · `today_cite_ids` · `note` |
| `constants.tsv` | `constant_id` (YK-01…) · `condition` · `place` · `condition_ids` · `cite_ids` · `note` |
| `cases.tsv` | `case_id` (YC-00, then YC-01…) · `name` · `axis_states` (`YA-01=<label>; …` for every axis, joined by ` + ` where `today` joins them, or `disputed` or `unknown`) · `basis` · `cite_ids` · `note` |
| `citations.tsv` | `cite_id` (YE-A001…, by part) · `source` · `locator` · `quote` · `source_date` · `date_basis` · `fetched_from` · `url` |
| `unknowns.tsv` | `about` · `what_would_show_it` · `who_can` · `route` · `read` · `why_not_held` |
| `notes.md` | Pass 2: identifications across parts, and place groupings; disagreements; problems with the method. Pass 1 writes its own `pass1/notes-<part>.md`: what was read, with counts; identifications and place groupings within the part; what couldn't be read. |

**Done when:**
- every source has been read, or listed as unreadable;
- every condition sits on an axis or is a constant;
- every state, `today` and case cites evidence or is listed in `unknowns.tsv`;
- every quote is copied verbatim from its file.
