# The held pass's second stage: its design, for the coordinator (31 October 2026)

**What this is.** The design behind `briefs/S2-held.md`, drafted by an agent from the coordinator's design in `STATE.md` ("The second stage, from about 18:50"). It covers:
- how each finding of `inspection-Q3M.md` is taken (`briefs/Q3-misses.md`, superseded: "That stage's brief takes every finding of the inspection");
- the tools the brief names: the landing script, the checker that must accept a landed quote, and `held_amend.py`'s change;
- the split into agents, and an estimate of the cost, an assumption to be measured on the first agent;
- the open questions.

Nothing here is built yet. `method/s2_held.py` and the changes in section 3 come before the brief's inspection, so the inspector can test them on fixtures, as `inspection-Q3M.md` tested `q3_misses.py`.

**What was read, at which commits:** this repository at `ae0e8343` (`PLAN.md`, `STATE.md`, `founder-decisions.tsv`, the briefs, the tools, `merged/`, `held/`); observed-sh at `04de369da`, observed-sa at `b0bd0b163` and other-product-class at `0d79b794f`, their guides only. The counts below come from `merged/cells.tsv` and `merged/kinds.tsv` at `ae0e8343`, and from a scratch parse of the held pass's notes (section 4).

## 1. The design in one view

1. **The part list.** `s2_held.py parts --write` writes `held/s2-parts.tsv`. Each row holds a part, its platform, its domains, its cells holding nothing, its misses, and the commits fixed for the run:
   - observed-sh, observed-sa and other-product-class at their HEADs;
   - `sharrwah-knowledge-map` at the commit of the model it reads;
   - `woocommerce-11.2.1`.
2. **The agents** (`S2-held.md`), one per part, up to four at once. Each writes `held/<platform>/s2/<part>.tsv` and `.md`. A row is one of:
   - `found`: the passage, at its source and commit, with its locator, quote, supports, scope, terms, filler, quality and reading;
   - `not-found`: what it read and searched;
   - `not-held`: the same, and where the page that would show it isn't held, with a capture lead and `could_change`;
   - `absent`, `unreadable` or `unclear` (Q3M-4);
   - a `new` thing.
3. **The check.** `s2_held.py check --part <part>`, until no problem. Then the coordinator's own check (section 4).
4. **The misses decided across platforms.** `s2_held.py misses-join` prints each miss's rows on the five platforms side by side, with `held` (`yes`, `part` or `no`) computed from its parts. The coordinator writes `held/s2-misses.tsv`, and `s2_held.py check-misses` tests it (Q3M-5).
5. **The landing.** `s2_held.py land --platform <p>` turns each `found` row into a held entry (`held/<platform>/entries-s2.tsv`) and a placement in the batch `S2-<XX>` (`held/batches/S2-<XX>.txt`, `held/<platform>/placements-S2-<XX>.tsv`, `notes-S2-<XX>.md`, a row in `held/batches.tsv`). A row that names a concern-map key goes to `held/<platform>/s2-keys.tsv`. The other outcomes go to `held/<platform>/s2-outcomes.tsv`, and the capture leads to `held/s2-captures.tsv`.
6. **`held_entries.py check --platform <p> --batch S2-<XX>`,** with its new test: an S2 entry's text is found in its source at its locator.
7. **New things.** The rows' `new:` names, and the misses decided `new`, are proposed across the platforms as `briefs/N-new.md` did. The coordinator decides them in `held/new.tsv`, and the `<domain>-amend` parts make the capabilities (`briefs/M-amend.md`).
8. **The amendment.** `held_amend.py plan` and then `apply`, each with `--platform <p> --batch S2-<XX>`. Then `check_class_part.py` on each part it names, and `class_merge.py --complete`.
9. **Then:**
   - Q3's rows that the amendments touch are placed again (`STATE.md`, "Then");
   - the capture leads the coordinator takes go to `handoffs/`;
   - the omission review reads from the evidence's side, with S2's `not-found` rows among what it samples (section 7, question 9).

## 2. Each finding of `inspection-Q3M.md`, and how it is taken

The coordinator's response of 30 October (the inspection's last section) already did four of them, and put the rest into this stage. Each is taken, as below.

| Finding | How it is taken | Where |
| --- | --- | --- |
| **Q3M-1.** This repository's captures can't be cited, so an agent drops them. | A page this repository captured, or a founder's save, is cited as `sharrwah-knowledge-map@<commit>:<path>`, the path as `corpus_search.py` prints it. The S2 checker, and `held_entries.py check` for a landed entry, load `evidence/product-class/runs/*` as capture runs in `quote_check.Sources`, with `q3_misses.py`'s `ROOTS`. No address form is accepted as a source: every held page has a path. | Brief, "Sources and locators"; section 3 |
| **Q3M-2.** `held_index.py` missed other-product-class and archives held in parts. | Done on 30 October: `held_index.py` reads them, and its header says so. The brief keeps the evidence map's caution: "An address it doesn't know isn't proof of absence: grep the platform's `fetch.cdx` and `answers.jsonl` too". | Brief, "Where the held pages are" |
| **Q3M-3.** A thing of several parts gets one `held`. | A miss is read part by part: one subject `M-nn: <part>` for each part, each with its own outcome and its own capture lead. `misses-join` computes `held` per platform from them: `yes` where every part is found, `part` where some are, `no` where none is, with the parts that are absent, unreadable or unclear named. The parts are set in `q3_misses.py`'s `MISSES` (section 3.6). A cell has no parts: a passage that shows the capability makes it held, and what it leaves out goes in its `scope` or `reading`. | Brief, "Q3's misses"; section 3.6 |
| **Q3M-4.** No value for absent, unreadable or can't tell. | The outcomes `absent`, `unreadable` and `unclear`, for cells and misses alike. Each is defined from `PLAN.md`, section 6, and tested in the checker: `absent` and `unclear` cite a passage, `unreadable` names the file, and `unclear` says what would settle it. | Brief, "The outcomes" |
| **Q3M-5.** The capability is written per line but decided across the miss. | Each platform's rows carry its proposal (`cap_id`, and `as`: its thing, feature, new or not a capability). The coordinator decides once per miss, across the five platforms, in `held/s2-misses.tsv`. `check-misses` tests one decision per miss, and that `new` is allowed only where some platform's row names a place other than `none`. The landing uses the decision, never a row's proposal. | Brief, "Q3's misses"; section 3.1 |
| **Q3M-6.** The place-of-its-own test added a clause. | Done on 30 October: B-extent's convention "What a place of its own is". The brief quotes it and adds no clause. | Brief, "What takes a row" |
| **Q3M-7.** `none: <why>` contradicted the plan for paid plans and countries. | `capture` names the run with `needs:` where only the founder can give something, quoting `handoffs/README.md` and H-006. `none: <why>` is only for what no run can capture at all. | Brief, "The outcomes" |
| **Q3M-8.** The brief's example pre-answered M-07. | The brief draws no example from the 13 misses, and names no miss's thing anywhere. | Brief |
| **Q3M-9.** The rests read as facts about the repositories. | `s2_held.py misses` prints each rest under the label "Q3's batch, from the concern map only: its 'none held' and 'not held' are what this check tests". The brief says so too. | Brief, "Q3's misses"; section 3.1 |
| **Q3M-10.** Four misses were worded narrower or wider than their rows. | Done on 30 October in `MISSES`, which `s2_held.py misses` reads. | Section 3.6 |
| **Q3M-11.** No value for a held thing that isn't a capability. | `as` takes `not a capability`, with an empty `cap_id` and the reason in `reading`. Its rows aren't landed in the model; they stay in Q3's record. | Brief, "Q3's misses"; section 3.2 |
| **Q3M-12.** The guides were narrowed, and nothing said what to read whole. | Each platform's guides are read whole once, with their sizes: Shopify about 53,000 characters, Salla 50,000, each of the others 18,000 to 21,000. The rest is grepped: the register, `index/` whole (runs, run notes, the ledger summary and the ledgers), `instruments.json` where it exists, and observed-sh's journey catalog. `read` records the rows that bear on each cell. | Brief, "Read only this brief", item 3 |
| **Q3M-13.** A "searched, not found" isn't at a commit. | The commits are fixed for the run in `s2-parts.tsv` and named in each agent's message. The notes' first line names them, and the checker tests that it matches. A `found` row's source carries its commit, which the checker tests too. The landed cell reading names them as well (section 3.5, proposed). | Brief, "Output"; section 3.1 |
| **Q3M-14.** A search costs more than the brief said. | Done on 30 October: `corpus_search.py --brief`. The brief: one search per chunk and language, with all the chunk's terms, written to a file, of which the first 80 lines and the last are read and the rest grepped. For Shopify and Salla, `--runs-only` first. | Brief, "How to work" |
| **Q3M-15.** `capture` didn't carry what a handoff needs. | `capture`: `<repository>; <instrument>; <the run>; stop at <...>; needs: <...>`, in the parts `handoffs/README.md` lists. The row's `read` and `searched` give what is already held, and its subject and `could_change` give why. | Brief, "The outcomes" |
| **Q3M-16.** What the checker let through. | Each of its thirteen faults, and its two messages, has a test in `s2_held.py check` (section 3.1), or can't arise by design. Three can't: a place naming a statement (a place is now the platform's own words, with its kind), a citation that no statement names, and a statement citing another platform's citation. Each row carries its own source. | Section 3.1 |
| **Q3M-17.** The archive's form didn't fit an archive held in parts, and the release's path wasn't anchored. | An archive's file is named as `fetch.cdx` or `corpus_search.py` names it (`fetch.warc.gz`, or its part `fetch-NNNNN.warc.gz`), with the offset in `locator`, and a pasted `<path>@<offset>` gets the message "the offset goes in `locator`". The release's path is inside `/home/user/woocommerce-release/11.2.1/woocommerce/`. | Brief, "Sources and locators" |
| **Q3M-18.** The model can't cite what this check writes. | This design's reason for being. A `found` row becomes a held entry, `<PREFIX>-E-<hex>`, which `check_class_part.plat()` already resolves. With `class_slice.held_items()` and `subject_citations()` reading `entries-s2.tsv`, `citable()` gives it, with its own source, locator and quote. No new id scheme is needed, and nothing is quoted twice under two ids. | Section 3.2 to 3.4 |
| **Q3M-19.** The held pass reads the same evidence. | The held pass ran first, as the coordinator ruled. A row names an id already held instead of quoting again: a held entry (`XX-E-...`), a concern-map key, or a placed inventory id. An entry the held pass placed elsewhere takes a second line in the S2 batch, where its words also state the cell's thing (H-held.md, rule 2). A concern-map key goes to `s2-keys.tsv`, which `held_amend.py` applies as an evidence row. | Brief, "For each cell", step 4; sections 3.2 and 3.5 |
| **Q3M-20.** A `new` capability needs more than a line gives. | `supports` is on every `found` row. For a `new` thing, the notes give its place of its own (or none), its domain, area and parent, its name in each language the platform uses, and the terms searched. The cross-platform proposal names it in every platform's terms (`N-new.md`), and an amendment part makes it with every platform's cells. | Brief, "Output"; section 1, step 7 |

**The inspection's notes:**
- **Q3M-21:** taken in the wording: "search the concern map ... with the title of a page you read: `q3.py where` on what it finds says which cells cite it".
- **Q3M-22:** taken. The tools' list says that `quote_check.py --text` needs an archive's offset, and a captured page's run folder when it is given by address. `searched` records a search that printed nothing as `nothing`, since `outscope` prints no line then.
- **Q3M-23:** taken: `identifier` includes the item's own id (a route's id, a locale key, a plan's key).
- **Q3M-24:** no longer arises: rows are known by their part and line, and entries by a hash. The coordinator's "ids get four digits" is superseded by this.
- **Q3M-25:** for the record. `MISSES` holds all 15 of Q3's candidate-miss rows; `misses-join` and Q3's re-placement read them.
- **Q3M-26:** taken: the commits are fixed for the run. If an evidence repository advances during the run, its clone stays at the fixed commit until every part is checked. Coverage is then measured again (`PLAN.md`, section 6: "whenever a repository the model reads advances its commit").
- **Q3M-27:** taken from the evidence map into the brief: "WooCommerce's structures come through their saved answers". Cite such a line at its answer file.
- **Q3M-28:** for the record: the brief keeps the plan's rules.

**The inspection's "What I didn't check":**
- Whether Zid's and BigCommerce's lists are complete lists in the plan's sense isn't settled here either. An `absent` row must say what makes its list complete, in the platform's own words, as a reading, and the coordinator reads every `absent` row.
- The fixtures for batch B are covered: the S2 checker is one code for every part, and its fixtures (section 3.7) hold rows of a miss and of a cell.

## 3. The tools

### 3.1 `method/s2_held.py`, the agents' side

- **`parts [--write]`:** for each platform, the cells holding nothing, from `merged/cells.tsv` at the model's commit. Each is placed in a part by its capability's domain (`merged/capabilities.tsv`), as section 4 gives, with the misses each part takes and the commits. `--write` writes `held/s2-parts.tsv`: `part`, `platform`, `domains`, `cells`, `misses`, `commits`, `model`, `state` (`open`, `checked` or `landed`).
- **`leads --part P`:** what the held pass's batches sent to the second stage. It reads `held/<platform>/notes-*.md`, calibration batches included, since their leads point to held files too. A lead is either:
  - a section whose heading names the second stage, up to the next heading of its level, each top-level bullet with its nested lines;
  - or, outside such a section, a bullet or paragraph that names it.

  Each lead prints with its batch, file and line. The three groups:
  - those naming a cell of the part that holds nothing;
  - those naming no capability;
  - those naming only held cells, or another part's: counted, and printed with `--held`, one line each (`batch:line`, the cap_ids and the first 100 characters), for the agent to grep with a chunk's terms.
- **`cells --part P [--from I --to J] [--left]`:** for each cell:
  - the cap_id, domain and area, the definition, the parent and the note;
  - the kind and count (`merged/kinds.tsv`);
  - the cell's `searched` and `reading`;
  - the other four platforms' `terms`, and Shopify's Arabic names (`names-ar.tsv`);
  - the held pass's evidence rows on the other platforms (the `why` of evidence keys `XX-E-...`), clipped;
  - the Q3 rows whose basis names the cell or the capability (`q3/check-*.tsv`), and the subjects' points landed on it (`points/`);
  - the group-1 leads that name it.

  `--left` lists the cells the part's file has no row for, so a fresh agent can continue.
- **`misses --part P`:** the part's misses, each with its thing and parts (`q3_misses.MISSES`) and its Q3 rows and questions. Each rest prints under the label of Q3M-9. Then the capabilities whose names or terms share the thing's words, as leads, the way `held_entries.py show` prints `by name` leads: leads, not answers.
- **`check --part P`:** it tests:
  - **form:** the header; the field count; no `"`; no empty `;` piece;
  - **coverage:**
    - every cell of the part has a row, and so does every part of its misses;
    - no row's subject is outside the part, but `new`;
    - a cell's rows are one or more `found`, or exactly one other;
  - **values:** the outcomes; `supports` (B-extent's values, one or two different ones); `as` on a miss's rows only; `could_change`;
  - **cap_id:**
    - a cell's `found` row names its own cap_id;
    - a miss's row names a cap_id of the merged model, or `new:<name>`, or is empty only with `not a capability`;
    - a `new` name isn't an existing capability's name or id, as `held_entries.py check` tests;
    - one new thing isn't named two ways;
  - **sources (Q3M-1, Q3M-16, Q3M-17):**
    - one of the four forms, or an id that `class_slice.citable()` or the platform's held entries resolve;
    - the platform's repository;
    - the part's commit for that repository;
    - `line N` for a file, with the quote's first words within three lines of N;
    - an offset for an archive, whose file exists at the commit;
    - a source ending in `@<digits>` gets "the offset goes in `locator`";
    - the quote found by `quote_check.Sources(ROOTS, capture runs)`, or a problem;
  - **columns:**
    - `found`, `absent` and `unclear` have a source, a locator and a quote (or an id) and an identifier;
    - each term is in the quote or the id's text, and each filler is named there;
    - a quality isn't a mark of inclusion (`held_entries.MARKS`);
    - `place` is `none` or `<kind>: <words>`, the kind one of the five;
  - **the other outcomes:**
    - `read` and `searched` aren't empty or `-`;
    - `not-held` has a `capture` in its form, or `none: <why>`, and never `none` alone;
    - `unreadable` and `unclear` have a `capture`;
  - **reading:** it isn't empty, and each quote in single quotes is found in the row's quote, its source, or a file the reading names (`held_entries.py`'s `QUOTE` test);
  - **notes:** the notes exist; their first line names the part's commits; they name each new thing and each miss.

  It prints a `NOTE` for:
  - a `found` row whose only support is `shows`;
  - a quote under 30 characters, or one equal to its identifier (a title only);
  - a Salla or Zid `not-found` row with no Arabic search;
  - each `absent` row;
  - each `could_change` of `kind` or `decision`.
- **`misses-join [--miss M-nn]`:** each miss's rows on the five platforms side by side: per part, its outcome on each platform, the proposals and the places, with `held` computed per platform (Q3M-3). It writes nothing.
- **`check-misses`:** tests `held/s2-misses.tsv` (`miss`, `capability`, `as`, `reading`):
  - one row per miss;
  - `as` one of the four;
  - `capability` a cap_id of the merged model, or `new:<name>`, or empty only with `not a capability`;
  - `new` only where a platform's row names a place.
- **`land --platform p`:** section 3.2.

### 3.2 The landing: `s2_held.py land --platform p`

**Inputs:**
- the platform's rows in `s2-parts.tsv`, every one at `checked`;
- each part's `held/<platform>/s2/<part>.tsv` and `.md`;
- `held/s2-misses.tsv`, for every miss with a `found` row on the platform;
- `merged/capabilities.tsv`, for the cap_ids.

It refuses a part not `checked`, and a miss row with no decision.

**Each `found` row:**
- its capability:
  - on a cell's row, the cell's cap_id;
  - on a miss's row, the coordinator's decision, never the row's proposal: `its thing` or `feature` lands on the decided cap_id; `new` lands as `new:<name>`; `not a capability` doesn't land;
  - on a `new` row, `new:<name>`;
- its entry:
  - where `source` is a held entry's id, that entry;
  - where it is a concern-map key or a placed inventory id, a row of `s2-keys.tsv` instead;
  - otherwise, an entry of `entries-s2.tsv`.

`absent`, `unclear` and the rest show no capability, or don't settle one. They become entries of no batch, and go to `s2-outcomes.tsv`.

**The entries' form,** `held/<platform>/entries-s2.tsv`, with the header of `entries.tsv` (`entry_id`, `structure`, `labels`, `source`, `locator`, `section`, `text`):
- `entry_id`: `<PREFIX>-E-` followed by the first 8 hex digits of `sha1("second-stage\x00" + <repository>:<path> + "\x00" + <locator> + "\x00" + fold(<quote>))`. The repository and path are taken without the commit, so the same words cited again at a later commit keep their id. On a collision with an id of `entries.tsv` or `entries-s2.tsv` that names another passage, it is lengthened to 10, 12 or 40 digits, as `held_entries.stable_id` does. Its form is the held pass's, so `plat()`, `cited_text()` (which matches `[A-Z]{2}-E-[0-9a-f]{8}`) and `class_slice` take it as they are;
- `structure`: `second-stage`;
- `labels`: the part or parts whose rows found it, `,`-separated;
- `source`, `locator`: as the row gives them, the commit included;
- `section`: the row's `identifier`;
- `text`: the quote exactly as the row gives it.

The same passage found by two rows is one entry.

**The batch's form:**
- `held/batches/S2-<XX>.txt` (`S2-SH`, `S2-SA`, `S2-ZD`, `S2-WC`, `S2-BC`): the batch's entry ids, in the parts' order and their rows' order. An existing held entry is included where a row names it.
- A row of `held/batches.tsv`: `S2-<XX>`, the platform, the count of entries, `second-stage`. Listing it there is what makes `class_slice.held_items()` read its scopes, and `held_amend.py` take it: a batch not listed is a calibration's, which never reaches the model.
- One batch per platform, landed once all its parts are checked. A correction after the batch is applied lands as `S2-<XX>-R<n>`, with only the changed lines, since `apply` refuses a line applied before.

**The placements,** `held/<platform>/placements-S2-<XX>.tsv`, with H-held's columns (`entry_id`, `placement`, `cap_id`, `supports`, `scope`, `terms`, `filler`, `quality`, `reading`):
- `placement` is `capability` with its cap_id, or `new` with `new:<name>`;
- `supports`, `scope`, `terms`, `filler` and `quality` are the row's;
- `reading` is the row's, followed by `(the second stage: s2/<part>.tsv line <n>)`.

Two rows that put one entry on one capability make one line: the first row's columns, with both rows' references. `held_entries.py check` refuses a second line with the same scope and filler.

**The other files:**
- `held/<platform>/notes-S2-<XX>.md`, written by the script:
  - its first line, the parts' commits;
  - the counts by outcome;
  - each new thing by name, which `held_entries.py check` requires;
  - the rows not landed, and why;
  - the rows sent to `s2-keys.tsv`.
- `held/<platform>/s2-keys.tsv`: `batch`, `cap_id`, `platform`, `supports`, `key`, `why`.
- `held/<platform>/s2-outcomes.tsv`: `batch`, `subject`, `outcome`, `part`, `line`, `commits`, `read` and `searched` (clipped), `capture`, `could_change`.
- `held/s2-captures.tsv`: every capture lead across the platforms, with its row, for the coordinator's handoffs.

**Its rules:**
- **It is idempotent:** a second run writes the same files.
- **It refuses to drop an entry of `entries-s2.tsv` that a placements file names,** as `build` refuses for `entries.tsv`.
- **It prints:** the counts, the cells that would become held, each collision lengthened, and each miss landed.

### 3.3 What `held_entries.py check` must accept, and its other changes

- **`entries(p)`** reads `entries.tsv` and then `entries-s2.tsv`, so an S2 batch's ids resolve in `check`, `show` and `earlier`.
- **The quote test, for an entry of structure `second-stage`.** Its text was written by an agent, so it is tested, unlike a built entry's:
  - the text is found in its source by `quote_check.Sources(ROOTS, captures)`, with the `ROOTS` of `q3_misses.py` and the capture runs `evidence/product-class/runs/*`;
  - at `line N`, its first words fall within three lines of N, and an archive's record is read at its offset;
  - a source that doesn't resolve, or a text not found, is a `PROBLEM`, not a `NOTE`;
  - the source's repository is the platform's;
  - its commit is one that the batch's notes name on their first line, or the repository's HEAD.
- **`whole_text()`** returns the text alone for a `second-stage` entry, since its source can be outside the platform's repository root.
- **`build`** leaves the ids of `entries-s2.tsv` out of its refusal (`lost`), and never writes that file. **`batches`** reads `entries.tsv` alone, so an S2 entry is never cut into a held-pass batch.
- **Everything else stands:**
  - the terms and fillers are tested in the text;
  - a mark of inclusion is refused as a quality;
  - the reading's quotes are tested;
  - the notes must name the new things;
  - the `CHANGES` lines print: every line on a cell holding nothing prints one, as expected.

### 3.4 `class_slice.py`

`held_items()` and `subject_citations()` read `entries-s2.tsv` as they read `entries.tsv`. Then:
- `citable()` gives the S2 entries;
- `check_class_part.py` resolves their keys, since `plat()` already takes `XX-E-`;
- an S2 entry's citation carries its own source, locator and quote.

Q3M-18 is closed without a new id scheme.

### 3.5 `held_amend.py`'s change

Today it plans every listed batch of the platform. `apply` refuses a part whose evidence already cites any planned key ("applied before"), so once a platform is amended, no later batch of it can be applied. The change:
- **`--batch B`, repeatable** (`--batch S2-ZD`): `plan()` reads only those batches' placements and their rows of `s2-keys.tsv`. Without it, it works as today.
- **The refusal, with `--batch`:** a part is refused where a planned row's (`cap_id`, `platform`, `key`) is already in its evidence: that batch, or that line, was applied before. A key alone is not enough to refuse: an entry the held pass placed on another capability may take a second line (Q3M-19). Without `--batch`, it refuses as today.
- **Pending new things:** only the named batches'.
- **The cell's reading names the batch:** "The held pass's second stage (S2-ZD) adds ...". A cell that held nothing reads: "Nothing in the concern map; the held pass's second stage adds ...".
- **`s2-keys.tsv` rows** become evidence rows: `key` is the statement's key, and `why` is `(the held pass's second stage, <part> line <n>) <reading>`.
- **Proposed** (question 3): for each cell of the platform still `none-held` after the batch, `apply` adds a sentence from `s2-outcomes.tsv` to its `reading`: "The held pass's second stage read the held pages at <commits> (held/<platform>/s2/<part>.tsv, line <n>): <outcome>." Its terms are added to `searched`. The model itself then holds what `PLAN.md`, section 6 asks of a "searched, not found": what it read, at a commit.

Then `check_class_part.py` on each part it names, and `class_merge.py --complete`, as today.

### 3.6 `q3_misses.py`

**`MISSES` gains each miss's parts** (Q3M-3). The parts proposed below are cut from each thing's own words, as reworded on 30 October; alternatives stay one part. The coordinator sets them: a tool ruling, listed in section 6.

| Miss | Parts |
| --- | --- |
| M-01 | a tip the buyer adds, online or in person; the tip options the merchant sets |
| M-02 | test orders and simulated payment outcomes; how they stay apart from live orders, balances and reports |
| M-03 | an AI agent linking to, or acting as, a buyer's account |
| M-04 | the admin's own language; right-to-left layout; numerals; date formats; mixed-direction text |
| M-05 | a delivery date or time slot the buyer chooses |
| M-06 | the package dimensions a merchant saves for labels and rates |
| M-07 | the return window; return fees; restocking fees; final sale |
| M-08 | handing the store's ownership to the client; its billing |
| M-09 | the dated record for merchants; the dated record for developers |
| M-10 | goods received before the buyer is charged, charged later on a trigger |
| M-11 | the shipment's return when the buyer refuses it at the door; what is charged |
| M-12 | strong buyer authentication (3D Secure); the shift of a fraud loss or chargeback liability away from the seller |
| M-13 | a transfer receipt or proof of payment the buyer submits for an order |

That makes 26 parts on each platform.

**`misses` labels each rest,** as Q3M-9 asks.

### 3.7 Before the inspection

The coordinator builds `s2_held.py` and the changes in 3.3 to 3.6. They are tested on fixtures that cite real held files, in a scratch copy of `studies/class-model` (`CLASS_MODEL_DIR`), as `inspection-Q3M.md` did:
- a baseline part that passes, with a cell's row of each outcome, a miss's rows and a `new` row;
- one-fault variants, among them every fault of Q3M-16's table;
- a landing from the baseline, checked by `held_entries.py check` and planned by `held_amend.py plan --batch`.

Then the brief goes to an inspector who made none of it (`PLAN.md`, section 3). The inspection compares each rule of the brief with its source.

## 4. The split, and the estimate

**Up to four agents at once** (the founder, 30 October), fewer if agents are stopped mid-run. A platform is cut in two by domain where it has more than about 60 cells: A to C, and D to G. That way a help centre's section, or an admin area, is read by one agent. The cells holding nothing, by part, from `merged/cells.tsv` at `ae0e8343`:

| Part | Platform | Domains | Cells | Misses |
| --- | --- | --- | --- | --- |
| `S2-SH` | Shopify | A to G | 56 (A 8, B 8, C 6, D 14, E 4, F 11, G 5) | all 13 |
| `S2-SA-1` | Salla | A to C | 51 (17, 8, 26) | M-01, M-02, M-05 to M-07, M-10 to M-13 |
| `S2-SA-2` | Salla | D to G | 35 (11, 9, 10, 5) | M-03, M-04, M-08, M-09 |
| `S2-ZD-1` | Zid | A to C | 62 (16, 10, 36) | as SA-1 |
| `S2-ZD-2` | Zid | D to G | 76 (23, 14, 29, 10) | as SA-2 |
| `S2-WC-1` | WooCommerce | A to C | 75 (22, 17, 36) | as SA-1 |
| `S2-WC-2` | WooCommerce | D to G | 86 (35, 20, 25, 6) | as SA-2 |
| `S2-BC-1` | BigCommerce | A to C | 97 (25, 24, 48) | as SA-1 |
| `S2-BC-2` | BigCommerce | D to G | 82 (37, 10, 26, 9) | as SA-2 |

Shopify is one part. Its 56 cells, its 13 misses, its leads and its guides fit one context, and its searches are its cost. A miss goes to the half of the domain where a capability that may hold it sits. That is a routing only: the agent may name any capability.

**The order:**
1. `S2-ZD-1` alone first. It is checked and landed end to end (`land`, `held_entries.py check`, `held_amend.py plan --batch`) before the others run, as the held pass's dry run went first. It exercises the most source forms in one part:
   - other-product-class's structures, run steps and saved answers;
   - this repository's captured help.zid.sa, docs.zid.sa and zid.sa pages (Q3M-1);
   - the dashboard's locales in English and Arabic;
   - nine misses.
2. Then four at once: `S2-SH` (its searches take longest, about two minutes each), `S2-BC-1`, `S2-WC-2` and `S2-ZD-2`.
3. Then `S2-BC-2`, `S2-WC-1`, `S2-SA-1` and `S2-SA-2`.

**What the leads add, measured** (a scratch parse of `held/<platform>/notes-*.md` at `ae0e8343`). It counts a nested bullet on its own, so `leads` will print fewer items:

| Platform | Pieces naming the second stage | Characters | Items naming a cell holding nothing | Naming no capability | Naming only held cells |
| --- | --- | --- | --- | --- | --- |
| Shopify | 119 | 172,530 | 22 (3,666 characters) | 567 (79,420) | 348 (70,261) |
| Salla | 82 | 125,651 | 9 (2,109) | 256 (39,108) | 351 (78,607) |
| Zid | 20 | 29,959 | 10 (1,655) | 64 (7,038) | 122 (19,950) |
| WooCommerce | 14 | 13,760 | 4 (1,134) | 39 (5,301) | 27 (6,589) |
| BigCommerce | 2 | 4,117 | 6 (1,465) | 18 (1,401) | 7 (938) |

The first two groups are printed whole. The third is counted, and printed only with `--held`: at one line each, it would add about 35,000 to 50,000 characters on Shopify and on Salla, for leads that take no row here (`S2-R2`). So a Shopify agent starts with about 85,000 characters of leads and 53,000 of guides, about 40,000 tokens. That is a reading of the counts. It is the one place this design departs from making every lead a first read: the third group is grepped, not read whole.

**The estimate, an assumption to be measured on `S2-ZD-1`:**
- **The rate an entry in the held pass:** its batches cost 105,000 to 372,000 tokens an entry, most between 120,000 and 225,000 (`method-report.md`, section 18), with each entry's source given.
- **The rate a row assumed here:** a row here starts from a search. Assumed: 150,000 to 350,000 tokens a row on Shopify and Salla, whose corpora are deepest (31,269 and 8,641 readable addresses, `held-vs-read.md`). On Zid, WooCommerce and BigCommerce, 100,000 to 250,000 (1,039, 175 and 381 addresses), where many rows end at one search per language. A miss is counted as one row per platform, since its parts share their searches.

| Item | Rows | Million tokens |
| --- | --- | --- |
| Shopify | 56 + 13 | 10 to 24 |
| Salla | 86 + 13 | 15 to 35 |
| Zid | 138 + 13 | 15 to 38 |
| WooCommerce | 161 + 13 | 17 to 44 |
| BigCommerce | 179 + 13 | 19 to 48 |
| The coordinator's checks, at 15 to 19 percent of the agents' (`method-report.md`, section 18) | | 12 to 36 |
| The landing, the new things' proposals and amendment parts, the amendments and the merge | | 10 to 25 |
| **The second stage, in all** | **685** | **about 100 to 250** |

- **Against the projection:** at 18:40 the coordinator projected 270 to 370 million for the second stage, the omission review, the final review and its corrections, and the architecture plan's review. At its top, the second stage alone takes most of that. A reading: the extent's projection, about 5.4 to 5.6 billion, would rise.
- **The measure:** `S2-ZD-1`'s tokens a row, by outcome, `found` against the others (`method/count_tokens.py` and its transcript). They re-project the rest. Shopify's and Salla's rates are measured again on their first parts.
- **What keeps it down:**
  - a chunk's terms searched in one call per language, `--runs-only` first on Shopify and Salla;
  - the strongest passage first, then stop (`S2-R1`);
  - the leads read first;
  - a fresh agent past about 200,000 tokens of context, continuing from the file.

**Effort:** `high`, the founder's floor. The held pass's calibration found that effort wasn't the lever: "`xhigh` cost 1.6 times as much ... and missed the same details, or others like them ... effort isn't the lever, search is" (`STATE.md`, "The calibration"). But this stage's errors are of another type, a passage missed in a search. So `S2-ZD-1`'s check searches a sample of its `not-found` rows again with other words. If care missed passages, a "searched, not found" runs at `xhigh` from then on. The founder, 30 October: "Where `high` or `xhigh` consistently misses important details for a type of task, evidence review above all, that type runs at `xhigh` or `max`."

**The coordinator's check of each part (proposed):**
- the checker's lines;
- every `found` row that gives a cell `core` or `own-service`, read against its source, since each one changes a count;
- every `absent`, `unreadable` and `unclear` row, every `new` thing, and every `could_change` of `kind` or `decision`;
- a seeded sample of the `not-found` rows searched again: one in five on `S2-ZD-1`, one in ten after it.

## 5. The misses: with the platforms' cells, or their own agent

**Proposed: with the platforms' cells,** each miss read by its platform's agent, in the half section 4 gives it. The reasons:
- **The model has moved since Q3's check.** Three misses' things now have capabilities made in the held pass, whose cells holding nothing are in the parts already:
  - M-01's tipping: CM-CHK-012, holding nothing on Salla, Zid, WooCommerce and BigCommerce;
  - M-04's language part: CM-SRF-003, the admin's interface language, holding nothing on Zid, WooCommerce and BigCommerce;
  - M-12's authentication part: CM-PAY-033, 3D Secure, holding nothing on Salla, Zid and WooCommerce.

  A misses agent would read those ten cells a second time, and could answer them differently (a reading of `merged/capabilities.tsv` and `cells.tsv`).
- **The guides.** Every platform's agent reads its guides and leads anyway. A misses agent would read all five: about 132,000 characters of guides (Q3M-12) before its first search.
- **The decision across platforms** that Q3M-5 asks for is made once, by the coordinator, from the five platforms' rows side by side (`misses-join`). That is how the held pass's new things were decided across platforms (`N-new.md`).

**The alternative, one agent for the 13 misses,** keeps one reader for each miss's five platforms, so its proposal is made with every line in view. It costs the guides of every repository, and the second reading of those ten cells. Choose it if `S2-ZD-1`'s nine miss rows show that a platform's agent can't judge a miss's capability from one platform: say, `as` read differently from the cells' own placements.

## 6. The rulings this brief adds, for the founder's veto

Each is the coordinator's to confirm. Each is listed in one plain line at the next report (`PLAN.md`, section 3).
- **`S2-R1`:** a cell's `found` rows begin with the passage that shows the strongest placement, and add one only for a support value or a scope not shown yet. Why: the count reads `core` and `own-service`, and every further passage costs a read.
- **`S2-R2`:** a cell already held takes no row in this stage, even where a passage read here also states its thing. Where the passage would change what the cell is placed as, it is named in the notes. Why: the stage is "each cell still holding nothing" (`PLAN.md`, Stage 4A).
- **The misses' parts,** section 3.6: a tool ruling, cut from each thing's own words.
- **`could_change`'s use,** proposed:
  - `kind` and `decision` go to a handoff;
  - `count` is listed among the extent report's gaps, with no handoff;
  - `no` gets neither.

  It carries out `PLAN.md`, section 6 ("a capture request, where the thing could change the model or a decision") and `STATE.md`'s "Capture stays the exception". A count changes the model only by one platform, and never its kind.

## 7. Open questions

1. **The leads that name only held cells,** about 350 items each on Shopify and Salla, 122 on Zid, 27 on WooCommerce and 7 on BigCommerce by the scratch parse. They take no row here (`S2-R2`): `leads` counts them, and prints them with `--held` for a grep. Proposed: the final review's selection takes them, as it takes "the parts' leads" (`method/review_select.py`), by risk. Risk here means a lead whose words name a maker, a support value the cell lacks, or a quality. The alternative is a short pass per platform after this stage.
2. **`absent`:** proposed, in the cell's reading and `s2-outcomes.tsv`, the cell staying `none-held`. The alternative is a state of its own (`held` `absent`), which `class_merge.py`, `check_class_part.py` and `km_page.py` would need. The Knowledge Map's page would then show it: "A cell with nothing held reads as nothing held, never as absent" (`PLAN.md`, Stage 4A) holds for a cell with nothing held, and an absent cell is another case.
3. **The other outcomes in the model's readings:** `held_amend.py`'s proposed sentence (section 3.5), or kept in this stage's files only.
4. **Effort:** `high` with a re-search sample, or `xhigh` from the start for the `not-found` rows (section 4).
5. **The misses:** with the platforms' cells, as proposed, or their own agent (section 5).
6. **`could_change`'s triage,** as section 6 proposes.
7. **A held cell whose placement a passage would change** (`S2-R2`'s notes): read at the final review, or in a later round of this stage.
8. **The cells of new capabilities made from this stage.** An amendment part searches each platform's cell in the concern map only (`M-amend.md`, step 2). So a capability made from this stage's new things would get cells holding nothing that no one has read against the held pages. Proposed: those cells are read by this brief, in one more part, `S2-NEW`, before the omission review. The held pass's 16 new capabilities aren't affected: their cells are among the 620 already.
9. **The omission review's frame.** It reads "a cell holding nothing where something is held" and "samples what stays unread, by group, so the rate of what is missed is measured" (`PLAN.md`, Stage 4A). Proposed: its brief samples this stage's `not-found` rows by platform, so it measures this stage's miss rate.
10. **The cost.** If `S2-ZD-1`'s rate puts the second stage near the estimate's top, the extent's projection rises above the 5.4 to 5.6 billion of 18:40. The work goes on, by the founder's standing decision of 27 October: "The budget must never cost evidence about the references". The coordinator says when a higher plan is needed.
11. **A batch per platform or per part.** Proposed: one per platform, landed once its parts are checked. Landing `S2-ZD-1` early, for the end-to-end test, makes `S2-ZD` from it alone, and `S2-ZD-2`'s rows land as `S2-ZD-R1` under section 3.2's rule for a later batch.

## The coordinator's decisions (31 October, about 19:10 UTC)

On the draft's open questions:
1. **Leads that name only cells already held** go to the final review's selection, by risk; this stage counts and greps them, as the draft has it.
2. **`absent` is not a cell state of its own.** PLAN's Stage 4A has the Knowledge Map's page read a cell with nothing held 'as nothing held, never as absent'; an `absent` outcome (a complete list that lacks the thing) stays in `s2-outcomes.tsv` and is written into the cell's reading and `searched`, with its source at its commit.
3. **Not-found outcomes are written into the model's cells:** the cell's `searched` and reading take what was read and searched, at its commits, as PLAN's section 6 asks of a 'searched, not found'.
4. **Effort `high`,** and the first part's check searches again a sample of its `not-found` rows; if a missed passage turns up, the later parts' `not-found` rows run at `xhigh`.
5. **Q3's misses are read with the platforms' cells,** as the draft proposes, and the coordinator decides each miss once, from the five platforms' rows side by side.
6. **The capture triage by `could_change`** as the draft has it: `kind` and `decision` go to a handoff in `handoffs/`, `count` into the extent report's list of gaps, `no` to neither.
7. **A held cell whose placement a passage would change** is read at the final review, from this stage's notes.
8. **`S2-NEW`** runs, as one more part, if this stage makes new capabilities: their cells, searched so far only in the concern map, are read against the held pages before the omission review.
9. **The omission review samples this stage's `not-found` rows,** so this stage's rate of misses is measured.
10. **The cost** goes to the founder only if its projection's top moves past 6.04 billion (the founder's standing rule since 27 October).
11. **One batch per platform** (`S2-SH`, `S2-SA`, `S2-ZD`, `S2-WC`, `S2-BC`), the parts' rows landed into it in turn.

**S2-R1 and S2-R2** are kept as engineering rulings, listed for the founder's veto with the extent's report.

**Order:** the tools are built and tested on fixtures first; then the brief and the tools are inspected by an agent that made none of them; then Zid A–C runs alone and is landed end to end; then the other parts, four at a time.
