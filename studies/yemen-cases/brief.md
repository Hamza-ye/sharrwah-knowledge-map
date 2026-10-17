# Brief: Yemen's axes and cases (Q2, step 1)

This is `PLAN.md` Stage 1. Read only this brief and the evidence named under "Inputs".

**Who does what.** The message that started you names your role.
- **Pass 1** is done by six agents, one per part:
  - A: the founder's pages and any attestations;
  - B: the Sana'a rules run;
  - C: the operators run;
  - D: the cited-sources run, items 1 to 131;
  - E: the cited-sources run, items 132 to 280 (the run's last);
  - F: the community clients, and the OCR text in `derived/`.

  Each reads every source in its part, and nothing else. It writes `pass1/conditions-<part>.tsv` and `pass1/citations-<part>.tsv`, numbering its rows `YQ-<part>001…` and `YE-<part>001…`, and `pass1/notes-<part>.md`.
- **Pass 2** starts after the coordinator has joined pass 1's files into `conditions.tsv` and `citations.tsv`. It adds no citation: what pass 1 didn't find goes in `unknowns.tsv`.
  - Step 2a, one agent: `groups.tsv` and `places.tsv`.
  - Step 2b, several agents, each given a range of groups: `pass2/states-<k>.tsv` and `pass2/notes-<k>.md`, and `pass2/places-<k>.tsv` for any place it adds. The coordinator joins them with `method/join_pass2.py`.
  - The build, run by the coordinator, writes `axes.tsv`, `constants.tsv` and `cases.tsv`.
  - Step 2c, the step 2a agent: `unknowns.tsv` and `notes.md`.

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

## Pass 2: from conditions to axes and cases

Pass 2's agents make three judgments: which rows are one condition, which place names are one place, and each row's state. The build then applies the rules below to them, the same way for every axis.

### Step 2a: conditions and places (one agent)

Read `conditions.tsv`, `pass2/wordings.tsv` and the six `pass1/notes-<part>.md`. Open a source only to settle what its rows and quotes leave open, and list in `notes.md` each source you open, and why.

1. **One condition.** Rows whose states answer the same question are one condition, whatever their part. The question is about an act or an availability, for example who may do A, or whether B is available. Name it at that level, not per institution: an institution's own service is a place (rule 4).
2. **States are alternatives.** At one place and time, only one state of a condition holds. If two rows' states can hold together at one place and time, either they state the same thing, or they belong to different conditions. Size each condition so that this holds.
3. **`groups.tsv`.** Write each condition there:
   - its rows in `condition_ids`;
   - what differs between their states in `what_varies`.

   Every pass 1 row is in exactly one group. List each identification across parts in `notes.md`.
4. **Places.** A state's place is the scope its source gives it. List each place in `places.tsv`, with its `kind`:
   - **`authority`:** `<authority>'s area`, where a rule an authority sets holds. An authority is a body that sets rules: a government and its organs, such as its central bank, ministries and tax authority; or a foreign or international body, for the rules it sets. One governing body has one area, taking in each organ a cited source says belongs to it.
   - **`service`:** `<party>'s service`, where what a source says of a named party's own service holds. List one for each party whose service a row describes.
   - **`area`:** an area a source names, such as a city, a governorate, or the areas a side controls.
5. **Grouping.** Every place pass 1 gives goes in `places.tsv`. Its `grouped` names the place it is one with, or itself. A grouping joins places of one kind. `why` says why:
   - **`variant`:** the same words respelled, reordered, abbreviated or translated. Any other name needs `source`.
   - **`source`:** a single source uses both names for the same area. Cite those citations in `basis`.
   - **`rule`:** "Yemen", "the Republic" and their variants, and pass 1's `across Yemen`, are `place not stated`. A rule an authority sets takes that authority's area instead (step 2b).

   Groupings chain: `grouped` may name a place that is itself grouped with another, and each link needs its own `why` and `basis`. The rows take the place the chain ends at. Chaining has two limits:
   - **Seat or side.** A body or area named without its seat or side, such as a central bank or a tax authority, groups only on a source that gives its seat or side. Spellings of one seatless name group as `variant`, and stay seatless.
   - **One area.** A name that sources use for different areas never groups or chains, and stays its own place.

   A rule set by a body whose seat or side no source gives, such as a law of the unified Republic, takes `<body>'s area` and joins neither side.

### Step 2b: states (several agents, each given a range of groups)

For every row of its groups, an agent writes one line of `pass2/states-<k>.tsv`, with these columns.

**`label`:** the state, short and in English.
- Rows that state the same thing share one label, word for word. Rows that state different things get different labels. When the parties named are what differs, such as which banks may do something, the label names them, or the list that names them.
- The source's own words go in `note`.
- Leave the place out: the build adds it.
- A label never contains `;`, `|`, `[`, `]`, ` + ` or ` @ `.

**`place`:** the first that applies:
- a rule an authority sets: that authority's area, whatever area its text names;
- what a source says of one named party's own service: that party's service. Where the party offers several products and the row names one, the place is that product's, `<product> (<party>)'s service`. A row about several parties' services keeps its grouped place, and its label names the parties;
- `across Yemen`: a state that no authority sets and no party says of its own service, whose source says it holds in all of Yemen. Quote those words in `note`;
- otherwise, the row's place as `places.tsv` groups it.

If an authority's area or a party's service you need isn't in `places.tsv`, add it to `pass2/places-<k>.tsv`, with the same columns, grouped with itself. Step 2c groups variants among the added places.

**`holds`:**
- **`held`:** a source says or shows that the state held or holds. A rule holds once its effective date is on or before its source's date, or a source shows it in effect.
- **`provided for`:** an enacted law or issued decision provides for the state, its effective date is after its source's date, and no source shows it in effect.
- **`ended`:** a source says the state held and then ended, such as a suspension lifted or a rule repealed.
- **`proposed`:** a draft, plan or announcement, not enacted or issued. It is listed on its axis, but is never today and builds no case.
- A forecast or projection of a future value is `proposed` too: no source shows it held. A source's estimate of a present value says the state holds.

**`now`:** `yes` on the state a source presents as current, when the same source gives an earlier state for the same place dated the same at the coarser precision. Otherwise it is empty.

Each agent also writes `pass2/notes-<k>.md`, recording:
- rows that were hard to label, and why;
- disagreements between sources;
- problems with the method.

### The build

The coordinator runs `python3 -I method/join_pass2.py studies/yemen-cases` after step 2b, and again after step 2c has grouped the added places. It adds step 2b's places to `places.tsv`, and joins the states into `states.tsv`, taking each row to the place it is grouped with. Then it runs `python3 -I method/build_yemen_cases.py studies/yemen-cases`. The build writes `axes.tsv`, `constants.tsv` and `cases.tsv`, and nobody edits them by hand. `method/test_build_yemen_cases.py` tests its rules. They are:

1. **Axis or constant.**
   - An axis is a condition whose `held`, `ended` or `provided for` rows carry at least two labels. Its `condition_ids` list every row it rests on.
   - Any other condition is a constant. It takes its one label, with each place where it is `held`. Its `note` lists its other rows.
2. **State labels** carry ` @ <place>` when they hold for a place.
3. **Dates.**
   - A `held_at` that isn't a date counts as undated. A time of day is ignored, so states on one day tie. `after <date>` counts as that date. A state dated only `before <date>` is never today.
   - No source attests a state after 10 October 2026, when the evidence was captured, so a later date counts as that day.
4. **Today.** For each axis, `today` joins the latest-dated `held` state of each place with ` + `. `place not stated` counts as one more place.
   - **Overlap.** Parts may overlap: an authority's area, a party's service and a named area can cover the same ground. A part for one place says nothing about another.
   - **Supersession.** An `across Yemen` state supersedes a place's state only when it is strictly later. At a tie, the place's own state stands. No other state supersedes a state at another place.
   - **The `across Yemen` part** stands for the places the axis doesn't name. It is there only when an `across Yemen` state is held.
   - **Precision.** Dates of different precision are compared at the coarser one, so 2024 and March 2024 tie.
   - **Undated.** An undated state can be the latest only where its place has no dated state.
   - **One source, two states.** A source's `now` state replaces that source's other states.
   - **Disputed.** Two different states for the same place at the same latest date make that place's part `disputed @ <place>`. The axis's `note` records both, unresolved.
   - **Unknown.** A place with no `held` state, or whose latest state `ended`, takes `unknown @ <place>`.
   - The axis's `note` gives each part's date.
5. **Stop for review** past 20 axes. The build writes `axes.tsv` and `constants.tsv` and builds no cases until the coordinator has reviewed the axes. The review is recorded in `review-axes.md`, which names the sha256 of the `axes.tsv` it reviewed. The review changes nothing itself: it may only return groups to step 2a, naming the rule each one breaks.
6. **Today's case, `YC-00`,** puts every axis at its `today`. It is the one anchor case.
7. **Further cases** are built in two ways and no others:
   - **One per non-today state** of each axis, with every other axis at today's state.
     - On an axis whose `today` joins places, a state for a place replaces only that place's part. An `across Yemen` state replaces every part.
     - A disputed state counts as non-today.
   - **One per combination of `held` states that a single source shows at one dated time.** The axes it doesn't give stay at today's state.

   A `proposed` state builds no case. A case that duplicates another or today's is skipped. A case's `name` lists only the axes that differ from today, each with its value, for example `YA-03=<label>`.
8. **Basis** of a further case comes from the states that differ from today. Take the first that applies:
   - `in force`: they all hold now at their place (a disputed state counts);
   - `occurred`: they all held at some time, including states that ended;
   - `provided for`: otherwise.

### Step 2c: unknowns and notes (the step 2a agent)

Before the build, group the places step 2b added (`pass2/places-<k>.tsv`) as variants among themselves or of any listed place. After it, write `unknowns.tsv`, as below, and complete `notes.md`.

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
| `groups.tsv` | `group_id` (YG-001…) · `condition` · `what_varies` · `condition_ids` · `note` |
| `places.tsv` | `place` (as pass 1 gives it, an authority's area, or a party's service) · `grouped` · `kind` (`authority`, `service` or `area`) · `why` (`variant`, `source` or `rule`; empty when grouped with itself) · `basis` (for `source`: cite_ids from one source using both names) · `note` |
| `states.tsv` | `condition_id` · `group_id` · `label` · `place` · `holds` · `now` · `note` (step 2b writes `pass2/states-<k>.tsv`) |
| `axes.tsv` | Written by the build: `axis_id` (YA-01…) · `axis` · `what_varies` · `condition_ids` · `states` (`label [YE-001, YE-007] \| label @ place [YE-010]`) · `today` (state labels joined by ` + `, with `disputed @ <place>` or `unknown @ <place>` where they apply) · `today_cite_ids` · `note` |
| `constants.tsv` | Written by the build: `constant_id` (YK-01…) · `condition` · `state` · `place` · `condition_ids` · `cite_ids` · `note` |
| `cases.tsv` | Written by the build: `case_id` (YC-00, then YC-01…) · `name` · `axis_states` (`YA-01=<label>; …` for every axis, joined by ` + ` where `today` joins them, or `disputed` or `unknown`) · `basis` · `cite_ids` · `note` |
| `citations.tsv` | `cite_id` (YE-A001…, by part) · `source` · `locator` · `quote` · `source_date` · `date_basis` · `fetched_from` · `url` |
| `unknowns.tsv` | `about` · `what_would_show_it` · `who_can` · `route` · `read` · `why_not_held` |
| `notes.md` | Pass 2: identifications across parts, and place groupings; disagreements; problems with the method. Step 2b writes `pass2/notes-<k>.md`. Pass 1 writes its own `pass1/notes-<part>.md`: what was read, with counts; identifications and place groupings within the part; what couldn't be read. |

**Done when:**
- every source has been read, or listed as unreadable;
- every condition sits on an axis or is a constant;
- every state, `today` and case cites evidence or is listed in `unknowns.tsv`;
- every quote is copied verbatim from its file.
