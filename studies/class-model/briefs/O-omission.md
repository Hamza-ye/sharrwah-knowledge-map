# Brief: the omission review, from the evidence's side (Stage 4A)

**What this is.** `PLAN.md`, Stage 4A: "An omission review (the founder's suggestion, 30 October), after the held pass and before the final review, by an agent that made none of the model. It reads from the evidence's side, not the model's: through each repository's guides, registers and run indexes, for what the model still lacks. That means a capability some platform gives a place of its own, or a cell holding nothing where something is held. It samples what stays unread, by group, so the rate of what is missed is measured, not assumed. What isn't held at all, it names as capture requests. Its findings are corrected with the final review's."

The held pass placed the platforms' self-descriptions entry by entry, and its second stage read each cell still holding nothing against the held pages (`briefs/S2-held.md`). Both read from the model's side: an entry was given a capability, a cell was searched for. You read from the other side. You take what the platforms hold, as their own guides list it, and ask of each piece: does the model hold its thing, and where?

**You made none of the model.** You are a fresh agent, given this brief alone. You never wrote a part, a batch, a second-stage row, an amendment or a ruling, and nothing you read of the model is a reason to agree with it. `PLAN.md`, section 3: "A review tries to refute what it reviews, claim by claim, and reports counter-evidence and missing evidence, not agreement."

You write one row per item you read, and a finding row for each miss that can land. The coordinator checks every row and decides. A finding row is a row of the second stage's form, and lands through the same script, so the model cites it as it cites the held pass's entries. The coordinator's design is in `briefs/O-omission-design.md`, which you don't need to read.

**Your part.** Your message names it (such as `OM-ZD`), with its platform, its groups, the commits fixed for the review, and your effort. The parts are listed in `studies/class-model/omission/parts.tsv`.
- `python3 -I method/om_sample.py show --part <part>` prints your items, one by one, with what each needs;
- `python3 -I method/om_sample.py walk --part <part>` prints your platform's top-level places (below, "The walk"), if your part takes the walk.

**Effort:** your message names it. The founder, 30 October: "No agent runs at `medium` or `low` for reading evidence, reviewing, or making an engineering judgement: `high`, `xhigh` or `max`."

## Read only this brief and, in this order

1. **The evidence map,** `studies/class-model/evidence-map.md`: where to start, the coverage levels, and the faults the tools have shown. Its "Found in the held pass" names faults on each platform: read your platform's.
2. **Your platform's guides, read whole once, at the start:**
   - Shopify (`/home/user/observed-sh`) and Salla (`/home/user/observed-sa`): `README.md`, `docs/READING.md`, `docs/GAPS.md`, `docs/OPERATING.md` and `structures/README.md`;
   - Zid, BigCommerce and WooCommerce (`/home/user/other-product-class`): `README.md`, `docs/OPERATING.md`, and your platform folder's `README.md` and `GAPS.md`.

   Then grep, never read whole: `structures/REGISTER.tsv`, `index/runs.tsv`, `index/run-notes.tsv`, `index/ledger-summary.tsv` and `index/ledger/*.tsv` where your repository has them, `index/instruments.json` where it exists, and observed-sh's `derived/journey-catalog.jsonl`. The founder's rule of 30 October: "what the evidence repositories hold is read through their own reading guides and indexes, not by search alone ... Search (method/held_index.py, method/corpus_search.py) follows the guides" (`founder-decisions.tsv`, 30 October, "Method (standing)").
3. **The model's rules:**
   - `studies/class-model/briefs/B-extent.md`: "Build capabilities", "Cells and evidence" and "Conventions from the dry run", with "What a place of its own is";
   - `briefs/S2-held.md`, its sections "The outcomes", "The row" and "Sources and locators". They govern your finding rows, as they govern the second stage's;
   - `briefs/H-held.md`, "For each entry", rules 2, 4 and 5: a new thing's line, `supports`, and the columns `scope`, `terms`, `filler` and `quality`. The rulings they name (M-1 to M-14, and those in `held/review-H-rulings.md`) apply to a finding row.

   The rules marked (ruling, proposed) below are the coordinator's, each listed for the founder's veto. Where any other rule of this brief reads differently from B-extent.md, S2-held.md or H-held.md, those govern: say so in your notes.
4. **The tools,** by their `--help` and headers, not their code:
   - `method/om_sample.py`: `show`, `walk`, `reveal`, `check` and `rates` (below);
   - `method/corpus_search.py`, `method/held_index.py`, `method/warc_text.py`, `method/quote_check.py` and `method/schema_type.py`, as `S2-held.md` lists them, with the evidence map's table of what each misses;
   - the model's: `method/class_slice.py` (`caps --terms`, `search`, `key`, `outscope`), `method/q3.py where`, `method/held_entries.py cells --platform <p> <cap_id> ...` and `earlier`, and `method/land_points.py cell <cap_id> <platform>`.

## The evidence first, then the model (ruling, proposed: `O-R1`)

For every item, read the evidence first. Say in the platform's own words what the item states, and whether it is a thing at all, before you look at the model. Only then look the thing up in the model. This keeps the model's words from deciding what the evidence says.

On an item of group 5, a cell the second stage wrote `not-found` or `not-held`, `show` prints the cell, never the second stage's row. Search and read as if no one had. Write your row. Then `om_sample.py reveal --part <part> --item <id>` prints the second stage's row, which it refuses to do while your row has no verdict. Then fill `cause` (below).

## What you read

Your items were drawn by `om_sample.py` with a fixed seed, at the commits your message names, from what stays unread on your platform. Each item carries its group:

1. **A structure the held pass didn't select,** or that it left as read by the concern map: one item of it (a line of its items, or a file where it has none). `held/selection.tsv` gives the structure's `reason`, the held pass's claim that it needn't be read. Your item tests that claim too.
2. **An item a selected structure's rule cut:** an item the selection's rule leaves out (`where:`, `labels:`, `latest:`, `drop-match:`, `new-vs:`, `read-as:`), the words a `drop:` rule leaves out of an item, or a part of a source that the structure's extractor dropped, as the evidence map and `held/<platform>/amendment-notes.md` name them.
3. **A help centre's, docs' or site's page no cell cites:** a page of a fetch archive or of this repository's capture runs.
4. **A run's page no cell cites:** a browser step's page text, or a saved answer.
5. **A cell the second stage wrote `not-found` or `not-held`,** that still holds nothing.
6. **A line the held pass placed `out`,** or a new thing the coordinator decided `out` in `held/new.tsv`.
7. **A place the platform lists that isn't held:** a ledger's entry `not attempted`, `not opened` or `not reached`, a sitemap entry not captured, or a `GAPS.md` row.

And, where your part takes it, **the walk** (below).

`show` prints, for each item: its group and stratum; where it is held (its file and line, its address and readable form, or the second stage's cell); its text, clipped, and how to read it whole; and its leads, which you read only after the evidence (`O-R1`):
- the model's lines that cite the same address, file and line, route, key or label (as `held_entries.py earlier` finds them);
- the capabilities whose cited statements share its identifiers, or whose terms it holds (as `held_entries.py show --candidates` finds them).

A lead is only a lead.

## For each item

1. **Read the item whole,** at its source. A page or a step in parts, with `quote_check.py --text`, `sed -n` or `grep -n`. A saved answer by its record. For group 5, read the cell as `show` prints it, and search and read what your platform holds for it, as `S2-held.md`, "For each cell", steps 2 and 3 say: the admin as captured first, then help, then docs, in every language your platform holds.
2. **Say what it states,** in the platform's own words: the thing it names, and what it shows of it (the platform's own section, setting, route, API or plan line; a third party's service; a market's value; nothing a store has).
3. **Is it a thing?** B-extent, "Build capabilities": "A capability is something a store or the platform can have or not have." A screen's frame, a filter's options, one account's records, a code module or a market's list of countries isn't. A market's values are the subjects' evidence, not the model's (`held/selection.tsv`, "market data, the subjects'"), unless they name a thing the model lacks.
4. **Look it up in the model:** `class_slice.py caps --terms "<term>; <term>"`, in English and, for Salla and Zid, in Arabic (singular and plural, with and without ال); then `held_entries.py cells --platform <p> <cap_id>` for the platform's cell; then the leads `show` printed. Read the capability's definition and note: where it names a homonym, or says where else such a thing belongs, follow it.
5. **Write the verdict** (below), and a finding row where the miss can land.

## The verdicts

- **`held`:** the model holds the thing on your platform's cell, with evidence that shows at least what the item shows. `basis` names that evidence: a statement's key, a held entry's id with its batch, or a subject's statement.
- **`not a thing`:** the item states nothing a store or the platform can have (step 3). `reading` says what it is.
- **`miss`:** the item states a thing the model doesn't hold as it should. `miss` says which:
  - `cell`: a capability holds the thing, and your platform's cell of it holds nothing. Write a `found` finding row on that cell (below).
  - `support`: your platform's cell of the capability is held, but the item shows a support value it lacks among `core`, `own-service`, `extension-point` and `outside`. Cite the passage in the item's own `source`, `locator` and `quote`. It takes no finding row: the coordinator's decision of 31 October on the second stage, decision 7: "A held cell whose placement a passage would change is read at the final review, from this stage's notes" (`briefs/S2-held-design.md`; ruling, proposed: `O-R2`, that this review follows it).
  - `new`: no capability holds the thing, and your platform gives it a place of its own. Write a `new` finding row.
  - `no place`: no capability holds the thing, and it has no place of its own. Write a `new` finding row with `supports` `shows` and `place` `none` (H-held.md, rule 2).
  - `out`: a line of group 6 whose thing is a thing of the class, by the rules above. Cite the line's entry, and name the capability, or `new:<name>`, in `cap_id`. A `cell` or `new` miss of an `out` line also takes its finding row.
  - `capture`: the thing is one the model lacks, and only a place that isn't held would show it (group 7, or a held page's link to a page not held). Write a `not-held` finding row on the cell, where a capability holds the thing; otherwise name the capture in your notes (below).
- **`unclear`:** a held passage may show a miss, but its words don't settle it. Cite it, and say in `reading` what would settle it.

"Absence counts only from a complete list the platform publishes, such as an enumerated schema or a full plan table. Otherwise it is a gap" (`PLAN.md`, section 6, the test form, step 2). Nothing you read makes a cell `absent` unless it is such a list: then write an `absent` finding row, as `S2-held.md` defines it.

## The walk, for a place of its own the model lacks

The held pass read each list's entries in batches, and gave each entry a capability. B-extent's convention, "A place whose thing a capability already holds, as its cells' readings show, is that capability's evidence, not a new one", let a wide capability take a place that has a thing of its own. The walk reads the other way: the platform's own top-level lists, as its guides name them, each place against the model's capabilities.

`walk --part <part>` prints each list of your platform (its admin's navigation and settings, its route manifest's sections, its API reference's groups, its plan table, its app store's categories), and for each top-level place:
- its words, in each language held, and its kind (`admin route`, `admin section`, `API group`, `plan line` or `app category`, B-extent's five);
- its held entries, and each line the held pass gave them: the capability, its definition, the support and the batch, or `out` or `new` with its reason;
- the platform's cell of each such capability: held or not, and its supports;
- its flags (ruling, proposed: `O-R3`):
  - `unread`: no entry, or no line;
  - `out`: its only lines are `out`, or a new thing decided `out`;
  - `shows`: its only lines are `shows`;
  - `no shared word`: its words share no word with the capability's name, definition and the platform's cell terms, folded, in English and Arabic;
  - `absorbed`: its capability takes three or more places of the same list and level.

Read every flagged place whole, and the places `walk` marks `sampled` among the unflagged. For each, answer: is the place's thing the thing of the capability its lines name, in that capability's definition? Write a row for it as for an item (group `walk`). Where it isn't, and no capability holds it, it is a `new` miss with its place. Where the walk shows a capability that takes several places, each a thing of its own, write each as a `new` miss, and say so in your notes for the coordinator.

A list your guides show and `walk` doesn't print goes in your notes, with its file. Read its top level as `walk` would.

## The rows

### `studies/class-model/omission/<part>-items.tsv`: one row per item and per walked place

Tab-separated, with a header row, no quoting, no double quote (`"`), and no tab or newline inside a field. Its columns:
- `item`: the id `show` or `walk` prints.
- `verdict`: `held`, `not a thing`, `miss` or `unclear`.
- `miss`: on `miss`: `cell`, `support`, `new`, `no place`, `out` or `capture`; else empty.
- `cap_id`: on `held`, the capability that holds the thing; on a miss, the capability it should be on, or `new:<name>`; else empty.
- `basis`: on `held`, the model's evidence (a key, `<entry id>@<batch>`, or a subject's statement id), `;`-separated; else empty.
- `source`, `locator`, `quote`: on `miss` and `unclear`, the passage that shows it, by `S2-held.md`'s "Sources and locators". For an id already held, `source` is the id, and `locator` and `quote` are empty. Where a finding row carries the passage, these repeat it.
- `finding`: on a miss of kind `cell`, `new`, `no place` or `capture`, and on `absent`, the finding row that carries it, as `<part>.tsv line <n>`; else empty.
- `cause`: on group 5 only, after `reveal`: on `miss` or `unclear`, why the second stage didn't find it: `term not searched`, `searched, not read`, `read, not taken`, `place not in the guides read`, `tool missed` (a fault of a tool, named in `reading`) or `other`; on `held` or `not a thing`, `agrees`.
- `read`: what you read and searched, `;`-separated, in the second stage's form (`<tool> <language>: <terms>`, a file and its lines, a guide's row), each search's own terms, a search that found nothing ending in ` (nothing)`. `PLAN.md`, section 6: "A 'searched, not found' lists what it read, at a commit."
- `reading`: a reading, marked as one: what the item states, and why your verdict follows. A quote in single quotes is copied exactly from the item, its source or a file the reading names.

### `studies/class-model/held/<platform>/s2/<part>.tsv`: the finding rows

A row of `S2-held.md`'s form, its columns and outcomes as "The outcomes", "The row" and "Sources and locators" define them, with these differences only:
- **`subject`** is the cap_id of a cell of your platform that holds nothing in the merged model, or `new`. There are no miss subjects (`M-nn: <part>`) here, and `as` stays empty.
- **The outcomes** are `found`, `not-held`, `absent` and `unclear`. A `not-found` takes no finding row: your item's row records what you read.
- **A cell takes no row** for an item that showed nothing on it. Rows are findings only.
- **`read`,** on a `found` row, names your item's id first: `item <id>`.
- **`could_change`,** on `not-held` and `unclear`, by `S2-held.md`'s definitions, and `capture` in its form: `<repository>; <instrument, from index/instruments.json>; <the run>; stop at <...>; needs: <...>`. `handoffs/README.md`: "**A request may need the founder,** for something only the founder can give: a payment, a phone, a store on a paid plan. It says so under **Needs**".

`PLAN.md`, section 6, Evidence: "exists but isn't captured: a capture request, where the thing could change the model or a decision". A capture for a thing no capability holds has no cell to sit on: write it in your notes in the parts `handoffs/README.md` lists (repository and instrument; what to capture, step by step, and where to stop; already held; why; needs; done when), with its `could_change`.

## Rules

- Every claim is one of three (`PLAN.md`, section 6):
  - a fact traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence.
- observed-sh, observed-sa and other-product-class are read-only: never write, commit or push to them.
- Run Python with `python3 -I`.
- Never decide a maker, a third party or a placement from what you know of the platform (H-held.md, "Rules"). B-extent, `own-service`: "A product's name that carries the platform's brand doesn't name its maker."
- Don't change the model's files, the held pass's files, the second stage's, Q3's or the subjects'. Write only your part's three files, and make no commits.
- Nothing gets settled that the evidence didn't settle. Where you can't tell, write `unclear`, with what would settle it.

## How to work, keeping your context small

Your context should stay under about 200,000 tokens.
- **Read once, at the start:** the evidence map and the guides. Don't read the scripts' code.
- **Work in chunks** of 10 to 20 items of one group and stratum: `show --part <part> --from <i> --to <j>`. Decide them, and write the chunk's rows in one write, before the next chunk.
- **Make your lookups together:** one `caps --terms` call with every term of a chunk, one `corpus_search.py --brief` per language for a chunk of group 5, its output written to a file in your folder, then grepped. For Shopify and Salla, `--runs-only` first.
- **Read a long document in parts,** never whole.
- **Keep your working files in a folder of your own,** named for your part, inside the scratchpad directory your system prompt names (such as `<scratchpad>/OM-ZD/`), never in its root: other agents share it.
- **When your context passes about 200,000 tokens,** finish the chunk, write it, and stop. Report the items left: a fresh agent continues from your files (`show --part <part> --left`).

## Output

- **`studies/class-model/omission/<part>-items.tsv`,** as above.
- **`studies/class-model/held/<platform>/s2/<part>.tsv`,** the finding rows, as above. Write the file with its header even where you found nothing to land.
- **`studies/class-model/held/<platform>/s2/<part>.md`,** your notes, beside the finding rows, where `s2_held.py check` reads them:
  - its first line, the commits you read: `observed-sh@<c>`, `observed-sa@<c>`, `other-product-class@<c>`, `sharrwah-knowledge-map@<c>` and `woocommerce-11.2.1`, as your message names them;
  - its second line: `made none of the model: a fresh agent, given only briefs/O-omission.md`;
  - the guides you read whole, and what you grepped;
  - each `new` thing, as `S2-held.md`, "Output", asks: its rows, its place of its own (or none), its proposed domain, area and parent, its name in each language your platform uses, and the terms you searched;
  - each capture with a `could_change` of `kind` or `decision`, and each capture for a thing no capability holds, in `handoffs/README.md`'s parts;
  - each `support` and `out` miss, one line each, for the final review;
  - each place the walk shows a capability taking with others, each a thing of its own;
  - for group 5: the causes, counted, and any pattern among them;
  - each list your guides show that `walk` doesn't print;
  - problems with this brief or the scripts.

Check your part with `python3 -I method/om_sample.py check --part <part>` until it prints no problem. It tests the items file (every item and sampled place has one row; the values; each `finding` names a row; each quote against its source) and runs `s2_held.py check --part <part>` on the finding rows. Then read again each line it prints as `NOTE`.

## Report

Back to the coordinator:
- your items' count by group and verdict, and the misses by kind;
- `om_sample.py rates --part <part>`'s table: each group's and stratum's misses against items read, with the bound;
- each `new` thing, with its rows;
- for group 5, the causes;
- the captures whose `could_change` is `kind` or `decision`;
- any problem;
- the checker's final line.

## After the parts: the coordinator

The coordinator checks each part:
- the checker's lines;
- every finding row against its source, and every `support`, `out` and `unclear` row;
- a seeded tenth of the `held` and `not a thing` rows read again, since a wrong `held` is a miss of this review.

Then, for each platform, `s2_held.py land --platform <p> --batch S2-<XX>-R<n>` lands the finding rows, as the second stage's later rows land: each `found` row becomes a held entry and a placement, which `held_entries.py check` checks and `held_amend.py apply` puts in the model. The new things are decided in `held/new.tsv`, and the captures it takes go to `handoffs/`. `om_sample.py rates --write` measures the rates over every part, and draws the second phase where a stratum showed a miss (ruling, proposed: `O-R4`). The rest (`support`, `out`, `unclear`, the places a capability takes with others) goes to the final review, whose selection reads it, and is corrected with the final review's findings.
