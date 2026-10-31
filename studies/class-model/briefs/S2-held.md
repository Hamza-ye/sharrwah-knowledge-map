# Brief: the held pass's second stage, the cells holding nothing read against the held pages (Stage 4A)

**What this is.** `PLAN.md`, Stage 4A, the held pass: "Then each cell still holding nothing is read against the held pages: the admin as captured, then help and docs, through each repository's guides first." The held pass's first stage placed the platforms' self-descriptions entry by entry, and the coordinator amended the model from them (`STATE.md`). The cells still holding nothing are those of `studies/class-model/merged/cells.tsv` with `held` `none-held`: Shopify 56, Salla 86, Zid 138, WooCommerce 161 and BigCommerce 179, at the commit the part list names. Each was searched in the concern map only. `B-extent.md`, "Cells and evidence": "`none-held` means only that the concern map holds nothing found by the terms searched. It never means the platform lacks the capability." This stage reads what the evidence repositories hold for each of them.

It also reads Q3's 13 candidate misses, part by part, on your platform. `briefs/Q3-misses.md`, superseded before it ran: "Q3's 13 candidate misses are checked in its second stage, which reads the held pages for the cells that still hold nothing."

You draft one row per finding. The coordinator checks every row and decides. A `found` row becomes a held entry and a placement through the coordinator's script, so the model cites it as it cites the held pass's entries. The coordinator's design is in `briefs/S2-held-design.md`, which you don't need to read.

**Your part.** Your message names it (such as `S2-ZD-1`), with its platform, its domains, the commits fixed for the run, and your effort. The parts are listed in `studies/class-model/held/s2-parts.tsv`.
- `python3 -I method/s2_held.py cells --part <part>` prints its cells;
- `python3 -I method/s2_held.py misses --part <part>` prints the parts of Q3's misses that are yours.

**Effort:** your message names it. The founder, 30 October: "No agent runs at `medium` or `low` for reading evidence, reviewing, or making an engineering judgement: `high`, `xhigh` or `max`."

## Read only this brief and, in this order

1. **Your platform's leads for the second stage,** your first reads: `python3 -I method/s2_held.py leads --part <part>`. The held pass's brief sent them here: "**What a run step or another file states that no entry holds** isn't placed here (M-12). List it in your notes, with its file and line, as a lead for the second stage, which reads held pages for the cells that hold nothing" (`briefs/H-held.md`, rule 1). They come from `held/<platform>/notes-*.md`, each with its batch, file and line, in three groups:
   - those that name one of your cells;
   - those that name no capability: a thing your cells may hold, or a new thing;
   - those that name only cells already held: `leads` counts them, and `leads --part <part> --held` prints them one line each. They take no row here (see "What takes a row"): grep them with a chunk's terms, for a lead that bears on one of your cells by its words.

   A lead is only a lead: what it says a file states, you read in the file.
2. **The evidence map,** `studies/class-model/evidence-map.md`: where to start, and the faults the tools have shown. Its "Found in the held pass" names faults on each platform: read your platform's.
3. **Your platform's guides, read whole once, at the start:**
   - Shopify (`/home/user/observed-sh`) and Salla (`/home/user/observed-sa`): `README.md`, `docs/READING.md`, `docs/GAPS.md`, `docs/OPERATING.md` and `structures/README.md`. That is about 53,000 characters for Shopify and 50,000 for Salla.
   - Zid, BigCommerce and WooCommerce (`/home/user/other-product-class`): `README.md`, `docs/OPERATING.md`, and your platform folder's `README.md` and `GAPS.md`. That is about 18,000 to 21,000 characters.

   Then grep, never read whole, with each cell's terms in each language: `structures/REGISTER.tsv`, `index/runs.tsv`, `index/run-notes.tsv`, `index/ledger-summary.tsv` and `index/ledger/*.tsv` where your repository has them, `index/instruments.json` where it exists, and observed-sh's `derived/journey-catalog.jsonl`. The founder's rule of 30 October names these: "what the evidence repositories hold is read through their own reading guides and indexes, not by search alone ... Search (method/held_index.py, method/corpus_search.py) follows the guides."
4. **The model's rules:**
   - `studies/class-model/briefs/B-extent.md`: "Build capabilities", "Cells and evidence" and "Conventions from the dry run", with "What a place of its own is";
   - `briefs/H-held.md`, "For each entry", rules 4 and 5: `supports`, and the columns `scope`, `terms`, `filler` and `quality`. A `found` row follows them as an entry's line does, and the rulings they name (M-1 to M-14, and the rulings in `held/review-H-rulings.md`) apply to it.

   The rules marked (ruling, proposed) below are the coordinator's, each listed for the founder's veto. Where any other rule of this brief reads differently from B-extent.md or H-held.md, those govern: say so in your notes.
5. **The tools,** by their `--help` and headers, not their code:
   - `method/corpus_search.py`: a platform's held text in every language it holds, with case, diacritics and Arabic letter forms folded. `--brief` prints a count per corpus past the cap, not every address. For Shopify and Salla, `--runs-only` searches only the observed repositories' runs, in seconds;
   - `method/held_index.py <address>`: what is held at an address, and in what readable form;
   - `method/warc_text.py <repository root> <archive>@<offset> [--text]`: one record of a fetch archive;
   - `method/quote_check.py`, to test each quote before you write it. `--text SOURCE [LOCATOR] [CAPTURE_RUN]` prints a source's text as the checker reads it: an archive needs its record's offset, and a captured page given by its address needs its run's folder;
   - `method/schema_type.py`, for a GraphQL type in full;
   - the model's: `method/class_slice.py` (`caps --terms`, `search`, `key`, `outscope`), `method/q3.py where`, `method/held_entries.py cells --platform <p> <cap_id> ...` and `method/land_points.py cell <cap_id> <platform>`.

## Where the held pages are

Each repository's own guide says where its platform's pages are. The admin as captured is read first, then help, then docs (`PLAN.md`, Stage 4A):
- **Shopify:** observed-sh's `README.md`, "Starting points", for the admin (its router, operations, runs' answers and steps), and `docs/READING.md` for the runs and structures; the Help Center is `structures/shopify/help-center/` (`docs/READING.md`, "Structures"); shopify.dev's pages are in its fetch runs, with their navigation in the structures `structures/REGISTER.tsv` lists for `shopify.dev`.
- **Salla:** observed-sa's `docs/READING.md`, "Surfaces and Salla's maps of them": the dashboard's maps, then help.salla.sa's and docs.salla.dev's. Help articles are in `structures/salla/help-articles/{ar,en}/texts.jsonl`.
- **Zid:** `zid/README.md`, "Where to start", for the dashboard: its route manifest, page index, locales, plan policies, permissions, the ledger of its routes, and its runs' steps and answers. Help and docs are not in other-product-class: "Zid's other surfaces: help.zid.sa, docs.zid.sa, zid.sa, the app and theme markets, the mobile apps | not captured here; sharrwah-knowledge-map holds some of their pages (`evidence/product-class/`)" (`zid/GAPS.md`).
- **BigCommerce:** `bigcommerce/README.md`, "Where to start": the store's settings, plans and channels runs, the Help Center runs, and the fetch runs of its terms, fees and API reference. This repository holds more of its docs and help pages (`evidence/product-class/runs/`), and the founder's saves (`evidence/product-class/blocked-evidence-founder/bigcommerce/`).
- **WooCommerce:** `woocommerce/README.md`, "Where to start": the store's runs, its database runs' `options.tsv`, and the plugins' code. Its release is unpacked at `/home/user/woocommerce-release/11.2.1/woocommerce/`. This repository holds its docs pages (`evidence/product-class/runs/`).

`corpus_search.py` reads all of these for your platform, this repository's captures and the founder's saves among them (its header). The evidence map's table of the tools says what each misses:
- `held_index.py`: "An address it doesn't know isn't proof of absence: grep the platform's `fetch.cdx` and `answers.jsonl` too";
- `corpus_search.py`: "It finds words, not things, so a title that doesn't hold the term is missed: read the denominators first. WooCommerce's structures come through their saved answers". Cite such a line at its answer file.

## For each cell

1. **Read the cell.** `cells` prints, for each:
   - the capability: its definition, parent and note, and its kind and count (`merged/kinds.tsv`);
   - your platform's cell: the terms it searched and its reading;
   - the other platforms' terms for it, and Shopify's names in Arabic (`names-ar.tsv`);
   - the held pass's lines on the other platforms;
   - the Q3 rows and the subjects' points that name the cell or the capability;
   - the leads that name it.

   Read the capability's note before you place on it: where it names a homonym, or says where else such a thing belongs, follow it.
2. **Find where your platform would hold it,** from the guides: the structures `REGISTER.tsv` names for its surface, the admin routes or pages the ledger and the route manifests name, the runs `runs.tsv` and `run-notes.tsv` name, the help and docs sections, and what `GAPS.md` says isn't held. Record in `read` the rows that bear on it: structure ids, run ids, ledger rows, and the `GAPS.md` row.
3. **Read the admin as captured first, then help, then docs.**
   - The admin: its own places (route manifests, navigation, settings, page indexes, plan tables, permission lists), the run steps that opened them, the answers its pages received, and its locale strings for a page no run opened.
   - Then the platform's help pages, then its docs and API reference.
   - Search with `corpus_search.py --brief`, in every language your platform holds: English, and Arabic too for Salla and Zid, and Shopify's Arabic help pages where they help. Use the capability's own words, the other platforms' terms, and your platform's words for the thing where a guide or a lead gives them. Search each Arabic term in its singular and its plural, with and without ال (B-extent, "The anchor part").
   - Use `held_index.py` for an address you expect.
   - Search the concern map too with `class_slice.py search`, with terms the cell's own search didn't use, and with the title of a page you read: `q3.py where` on what it finds says which cells cite it.
4. **Name what is already held.** Where the passage is already a held entry or a concern-map statement, name its id rather than quoting it again:
   - grep `studies/class-model/held/<platform>/entries.tsv` for its words, or for its file and line;
   - use `class_slice.py search` for a statement.

   A held entry the held pass placed elsewhere takes a second line here where its words also state this cell's thing (H-held.md, rule 2: "Every thing the entry names as its own takes a line"). Write a quote only for what neither holds.
5. **Write the row,** by its outcome (below).

## The outcomes

- **`found`:** a held passage states that your platform has the thing. Quote the passage that states it most plainly, in the platform's own words: a help page or an API reference over a title or a list entry.
  - Write first the passage that shows the strongest placement (`core` or `own-service`, then `extension-point` or `outside`, then `shows`). Add a passage only for a support value or a scope your rows don't show yet, and stop there (ruling, proposed: `S2-R1`).
  - `supports` takes B-extent's values. "`core`: the platform itself does it for the merchant. The statement names its own admin section, setting, route or built-in behaviour, a plan line that includes it, or its own API for its own feature". `own-service`, `extension-point`, `outside` and `shows` are defined in the same section, and H-held.md's rule 4 says how each reads a held source. Never decide a maker, a third party or a placement from what you know of the platform (H-held.md, "Rules").
- **`not-found`:** what is held was read and searched, and no passage states the thing. `read` and `searched` list what you read and searched. `PLAN.md`, section 6: "A 'searched, not found' lists what it read, at a commit." Your part's commits are fixed, and your notes name them.
- **`not-held`:** as `not-found`, and the place where your platform would state the thing isn't held. That means one of these:
  - a row of the platform's own list that the repository marks as not captured: a ledger's `not attempted` or `not opened`, or a sitemap entry not captured;
  - a `GAPS.md` row;
  - a held page's link to a page not held.

  That such a page would state the thing is an assumption: say so. `capture` and `could_change` follow (below).
- **`absent`:** "Absence counts only from a complete list the platform publishes, such as an enumerated schema or a full plan table. Otherwise it is a gap" (`PLAN.md`, section 6, the test form, step 2). A complete list the platform publishes leaves the thing out, or the platform states it doesn't do it. Cite the list's passage or the statement as for `found`, and say in `reading` what makes the list complete in the platform's own words, as a reading. `capture` stays empty.
- **`unreadable`:** the place is held, but only in a form the tools can't read: an index line whose archive isn't in git (`held_index.py`'s `cdx-only`), or a trace or screenshot not committed. `PLAN.md`, section 6: "if it is held but not readable, the reader is extended". `capture` names the file and where it is held, so the reader is extended rather than a new run made.
- **`unclear`:** a held passage may be the thing, but its words don't settle it. Cite it as for `found`, and say in `capture` what would settle it.

**A cell's rows** are one or more `found` rows, or exactly one row of another outcome.

**`could_change`,** on `not-held`, `unreadable` and `unclear`. `PLAN.md`, section 6, Evidence: "exists but isn't captured: a capture request, where the thing could change the model or a decision". Write which:
- `kind`: the capability is `slot` or `open` (`cells` prints it), and a held `core` or `own-service` would make it `class`;
- `count`: only its count would change;
- `decision`: a Q3 row or a subject's point names the cell or its capability (`cells` prints them);
- `no`.

Say why in `reading`. The coordinator decides which go to `handoffs/`.

**`capture`,** for `not-held`: `<repository>; <instrument, from index/instruments.json>; <the run: a journey unit by its ledger id, a fetch of the named addresses, or the GAPS.md row, quoted>; stop at <...>; needs: <what only the founder can give, or nothing>`.
- `handoffs/README.md`: "**A request may need the founder,** for something only the founder can give: a payment, a phone, a store on a paid plan. It says so under **Needs**". A store in another country can be such a run too: H-006 ran "with a new Shopify account located in the United States".
- Write `none: <why>` only where no run can capture it at all, such as a document only the platform holds, or what only a real verification would show.

## Q3's misses

`misses --part <part>` prints each miss that is yours with its parts, its Q3 rows, and what each row's rest says. A rest's 'held', 'not held' and 'none held' are about the concern map, not the repositories: Q3's batches searched the concern map only, and that is what this stage tests.

- **Each part of a miss** is read as a cell is: the same steps, the same outcomes and the same row, with `M-nn: <part>`, as `misses` prints it, for its subject.
- **Every row of a miss also carries `cap_id` and `as`:** the capability you propose for the miss from what your platform holds.
  - `its thing`: the cap_id whose thing it is;
  - `feature`: the cap_id of the capability whose thing contains it;
  - `new`: no capability holds it, and your platform gives it a place of its own; `cap_id` is `new:<name>`, and `place` says which place;
  - `not a capability`: it is held, but it isn't "something a store or the platform can have or not have" (B-extent, "Build capabilities"); `cap_id` is empty, and `reading` says why.
- **The coordinator decides each miss's capability once,** across the five platforms' rows. Your notes say, for each miss, what your platform holds of each part, and why you propose what you do.

## What takes a row

- Your part's cells, and your misses' parts.
- **A thing no capability holds** that you find while reading them: subject `new`, outcome `found`, `cap_id` `new:<its name, in the platform's words>`. Before you write it, search every domain with `class_slice.py caps --terms "<term>; <term>"`, in English and, for Salla and Zid, in Arabic (H-held.md, rule 2). B-extent's convention: "**When something becomes a capability:** where at least one platform gives it a place of its own: an admin section or route, an API group, a plan line, or an app category. A single feature flag isn't enough." Its "What a place of its own is" defines each kind, and adds: "A field, a toggle or a line of text inside a page isn't one, and neither is a feature flag. A place whose thing a capability already holds, as its cells' readings show, is that capability's evidence, not a new one." A thing with no place of its own is still written as `new:<name>`, with `supports` `shows` and `place` `none`, and your notes say it has no place of its own (H-held.md, rule 2).
- **Not a cell already held,** in your part or out of it: this stage reads the cells still holding nothing (`PLAN.md`, Stage 4A). Where a passage you read would change what a held cell is placed as (a support value it lacks), name it in your notes with its file and line, for the coordinator (ruling, proposed: `S2-R2`).

## The row

`studies/class-model/held/<platform>/s2/<part>.tsv`: tab-separated, with a header row, no quoting, no double quote (`"`), and no tab or newline inside a field. Its columns:
- `subject`: a cap_id of your part's cells, `M-nn: <part>`, or `new`.
- `outcome`: `found`, `not-found`, `not-held`, `absent`, `unreadable` or `unclear`.
- `cap_id`:
  - a cell's own cap_id on its `found` rows;
  - on a miss's rows, the capability you propose (above);
  - `new:<name>` on a `new` row;
  - otherwise empty.
- `as`: on a miss's rows only, `its thing`, `feature`, `new` or `not a capability`.
- `source`, `locator`, `quote`: on `found`, `absent` and `unclear` (below). For an id already held, `source` is the id, and `locator` and `quote` are empty.
- `identifier`: the page's title, the API's name, or the item's own id (a route's id, a locale key, a plan's key).
- `place`: on `new` rows and on a miss's `found` rows: `<kind>: <the words or identifier the platform's own list names it by>`, the kind one of `admin route`, `admin section`, `API group`, `plan line` or `app category`; or `none`.
- `supports`: on `found` rows, one value, or two different ones, `;`-separated.
- `scope`, `terms`, `filler`, `quality`: on `found` rows, by H-held.md's rule 5. Each term is the platform's own word, found in the quote. A filler is named in the quote. A mark of inclusion is never a quality.
- `read`: on every row but `found`: the guides' rows and the documents you read, `;`-separated. On a `found` row, what led you to it.
- `searched`: on every row but `found`: each search as `<tool> <language>: <terms>`, `;`-separated, such as `corpus_search ar: <term>, <term>`, `class_slice search en: <term>`, `held_index: <address>`. A search that printed nothing is recorded as `nothing`: `outscope` prints no line when nothing matches.
- `capture`: on `not-held`, as above; on `unreadable`, the file and where it is held; on `unclear`, what would settle it.
- `could_change`: on `not-held`, `unreadable` and `unclear`.
- `reading`: a reading, marked as one: why the passage states the thing and supports what it does, or what you read and why it doesn't state it. A quote in single quotes is copied exactly from the passage or from a file the reading names.

## Sources and locators

- **A held file:** `<repository>@<commit>:<path>`, at the commit your message names, with `line N` as `locator`: the line where the quote begins. The checker looks for the quote's first words within three lines of N.
- **A record of a fetch archive:** `<repository>@<commit>:<the archive's file, as fetch.cdx or corpus_search.py names it: fetch.warc.gz, or its part fetch-NNNNN.warc.gz>`, with the record's offset as `locator`. `corpus_search.py` prints `<path>@<offset>`: split it.
- **A page this repository captured, or a founder's save:** `sharrwah-knowledge-map@<commit>:<path>`, the path as `corpus_search.py` prints it (`evidence/product-class/runs/<run>/items/<n>-<host>/text.txt`, or a file under `evidence/product-class/blocked-evidence-founder/<platform>/`), with `line N`.
- **WooCommerce's release:** `woocommerce-11.2.1:<path>`, the path inside `/home/user/woocommerce-release/11.2.1/woocommerce/`, as `corpus_search.py` prints it, with `line N`.
- **The repository is your platform's:**
  - observed-sh for Shopify, observed-sa for Salla;
  - `other-product-class@<commit>:<platform>/...` for Zid, BigCommerce and WooCommerce, and the release for WooCommerce;
  - and this repository's captures of your platform's hosts, or its saves.
- **The quote** is verbatim, as held: the shortest whole part that states the thing. That is a sentence, a table row with its heading, a list item with the heading it sits under, or a locale string with its key. `corpus_search.py`, its header: "Snippets are folded for matching (case, diacritics, letter forms): never quote one; quote the document." Test each quote with `quote_check.py SOURCE LOCATOR TEXT` before you write it.

## Rules

- Every claim is one of three (`PLAN.md`, section 6):
  - a fact traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence.
- observed-sh, observed-sa and other-product-class are read-only: never write, commit or push to them.
- Run Python with `python3 -I`.
- Don't change the model's files, the held pass's files, Q3's or the subjects'. Write only your part's two files, and make no commits.
- Nothing gets settled that the evidence didn't settle. Where you can't tell, write `unclear`, with what would settle it.

## How to work, keeping your context small

Your context should stay under about 200,000 tokens.
- **Read once, at the start:** the leads, the evidence map and the guides. Don't read the scripts' code: this brief and each script's `--help` say what it prints and what the checker tests.
- **Work in chunks** of 10 to 20 cells of one area, from `cells --part <part> --from <i> --to <j>`. Decide them, and write the chunk's rows in one write, before the next chunk.
- **Search a chunk at once:**
  - one `corpus_search.py --brief` per language, with all the chunk's terms in one call (any term matches), its output written to a file in your folder;
  - read the file's first 80 lines and its last line, and grep the rest for each cell's terms;
  - for Shopify and Salla, run `--runs-only` first for the admin's runs, which takes seconds. A Shopify search over every corpus takes about two minutes;
  - grep the leads that name only held cells (`leads --part <part> --held`) with the same terms.
- **Read a long document in parts,** with `quote_check.py --text`, `sed -n` or `grep -n`, never whole.
- **Make your lookups together.** Each turn re-reads your whole context, so one turn that asks for five things costs a fifth of five turns.
- **Keep your working files in a folder of your own,** named for your part, inside the scratchpad directory your system prompt names (such as `<scratchpad>/S2-ZD-1/`), never in its root: other agents share it.
- **When your context passes about 200,000 tokens,** finish the chunk, write it, and stop. Report the cells left: a fresh agent continues from your file (`cells --part <part> --left`).

## Output, in `studies/class-model/held/<platform>/s2/`

- **`<part>.tsv`:** the rows, as above.
- **`<part>.md`,** your notes:
  - its first line, the commits you read: `observed-sh@<c>`, `observed-sa@<c>`, `other-product-class@<c>`, `sharrwah-knowledge-map@<c>` and `woocommerce-11.2.1`, as your message names them;
  - the guides you read whole, and what you grepped;
  - each `new` thing: its rows, its place of its own (or none), its proposed domain, area and parent, its name in each language your platform uses, and the terms you searched;
  - for each miss: what your platform holds of each part, and the capability you propose, with why;
  - each capture lead whose `could_change` is `kind` or `decision`;
  - what a passage states that would change a held cell's placement (`S2-R2`);
  - problems with this brief or the scripts.

Check your part with `python3 -I method/s2_held.py check --part <part>` until it prints no problem. It tests every quote against its source. Then read again each line it prints as `NOTE`.

## Report

Back to the coordinator:
- your rows' count by outcome, and the `found` rows by support;
- each `new` thing, with its rows;
- each miss's proposal;
- the capture leads whose `could_change` is `kind` or `decision`;
- any problem;
- the checker's final line.

## After the parts: the coordinator

The coordinator checks each part, decides each miss's capability across the platforms (`held/s2-misses.tsv`) and each new thing (`held/new.tsv`), and runs `method/s2_held.py land --platform <p>`:
- each `found` row becomes a held entry: a stable id, the quote its text, and its source and locator its own (`held/<platform>/entries-s2.tsv`);
- each entry takes a placement in a new batch of its platform (`S2-<XX>`), which `held_entries.py check` checks, its quote against its source;
- `held_amend.py apply --platform <p> --batch S2-<XX>` puts it in the model.

Then the parts are checked and merged again, and Q3's rows that the amendments touch are placed again. The capture leads the coordinator takes go to `handoffs/`.
