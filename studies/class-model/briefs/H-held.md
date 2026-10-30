# Brief: the held pass, the platforms' self-descriptions read entry by entry (Stage 4A)

**What this is.** The class's model was built from the concern map, finished on 12 October 2026. The evidence repositories hold much more of what the platforms list about themselves: route manifests, settings, navigation, plans, permissions, catalogs, events and changelogs. Some was captured after that date; some was held and never read. `studies/class-model/held-vs-read.md` measures the gap.

This pass reads every entry of those self-descriptions and places each on the model. What the platforms show of themselves then reaches the model through their own lists, read entry by entry, not by search alone (the founder, 30 October: the repositories' guides and indexes first, then search).

You draft placements. The coordinator checks them and amends the model from them: an entry placed on a capability becomes that platform's cell's evidence, a new capability is made with its cells, and the merge runs again. This pass sends no capture request. A gap goes in your notes, for the coordinator.

**This brief was rewritten after the dry run's review** (`held/review-H.md`; the coordinator's rulings, `held/review-H-rulings.md`). Two batches ran first and were reviewed line by line against their sources. Most of their misses came from rules this brief had left out or stated loosely, which it now states. The rest were care: a filler the entry doesn't name, a quote not copied exactly, a term left out, a second capability an entry names. The checker now catches most of them.

**Your batch.** Your message names a platform and a batch. `python3 -I method/held_entries.py show --platform <p> --batch <b> --from <i> --to <j> --candidates` prints its entries in order. Each one shows:
- its id;
- its structure, and the labels (a store, a language) it was held under;
- its text: the fields the platform states, in the source's order;
- its leads: capabilities whose cited statements share its identifiers, or whose terms it holds, each with what its cell on your platform holds now (`[cell: holds nothing]`, or its placements). A lead is only a lead.

**Read only this brief and:**
- **the evidence map,** `studies/class-model/evidence-map.md`, for where to start and the faults found so far;
- **your platform's repository guides, before the entries:**
  - for Shopify (`/home/user/observed-sh`) and Salla (`/home/user/observed-sa`): `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`;
  - for Zid, BigCommerce and WooCommerce (`/home/user/other-product-class`): `README.md`, and the platform folder's `README.md` and `GAPS.md`;
  - then, by their rows: `structures/REGISTER.tsv` for your structures, and `index/` (for Shopify and Salla, `index/ledger-summary.tsv` and the `index/ledger/` file your structures enumerate);
- **what each structure is:** `held_entries.py show --platform <p> --batch <b> --meta`, and the rest of a structure's `meta.json`;
- `studies/class-model/held/selection.tsv`, your platform's rows: why each structure is read, its `placement` and its `note`;
- **the model:**
  - `method/class_slice.py caps --terms "<term>; <term>"`, `key` and `search`;
  - `method/land_points.py cell <cap_id> <platform>`;
  - `studies/class-model/merged/capabilities.tsv`, read with `cut` or `grep`, never whole;
- **the model's rules:** `studies/class-model/briefs/B-extent.md`, "Cells and evidence", and "Conventions from the dry run", with "What a place of its own is". Where this brief and B-extent.md read differently, B-extent.md governs: say so in your notes.

**Effort:** your message names it, `high` or `xhigh`, never below `high` (the founder, 30 October). The coordinator sets it from the dry run's review (`held/review-H.md`, section 7) and the calibration of this brief.

## For each entry

1. **Read it as the platform states it.**
   - **Its sources:** the item, at the file and locator `entries.tsv` gives; the file its structure's `meta.json` names under `source` (`held_as` or `answer`), with the step's `.text.txt` beside an HTML or ARIA capture; and the `source.*` file beside `items.jsonl`. The bytes are the evidence. Where the rendering, the item and the source differ, the source governs; say so in your notes.
   - **A row of a table, or an item of a list, inside an article** (a help page, a plan page, a guide) is read with the words the article gives it: its table's heading, the paragraph before it, its columns' definitions, and the footnotes its marks point to. A footnote an entry's mark points to (an asterisk) is part of the entry.
   - **A term the source defines** (a terms page's "Extension", a plan's "Performance") is read by its definition before you join it to a capability on the same word.
   - **To clarify an entry only,** you may also read: the source page around a segment the structure was cut from, the run steps and answers the platform's ledger or `index/runs.tsv` joins to it, the platform's locales for a route no run opened, and the model's cells. A reading that rests on one cites it at its file, such as `<run_id>/steps/<NNN>.text.txt`, and quotes it exactly. Its `scope`, `terms`, `filler` and `quality` still come from the entry and its sources.
   - **What a run step or another file states that no entry holds** isn't placed here. List it in your notes, with its file and line, as a lead for the second stage, which reads held pages for the cells that hold nothing.
   - **Known cases:**
     - BigCommerce's `settings-list` pairs each section with the next section's address, so its entries carry none. Its source step `steps/002.frame-0.aria.yaml` holds each section's own (handoff H-009).
     - In BigCommerce's `plan-comparison`, rows 8 to 13 carry another row's name in `feature`. Their entries are rendered from `feature_text` and the cells, which are the row's own (`source.html`).
     - Zid's `dashboard-route-manifest` items carry each route's `module` and `imports`, which the rendering leaves out. Where a route's path leaves its thing unclear, read its item: the module's name (`platform-switch-call-….js`) often names it.
     - Zid's `dashboard-page-index` items leave out each page's permission, sidebar badge and listing condition; its `source.js` holds them.
2. **Place it,** one of three:
   - **`capability`:** the model's capability whose thing the entry is. Name one cap_id.
     - **Search for its place first.** Before you place a section, a route or a setting, search the model for its own place (such as "Settings > API and MCP > MCP") and its address. Where another capability's cell already cites that place, the entry is that capability's.
     - **Read the placed capability's note.** Where it names a homonym, or says where else such an entry belongs (Mokafaa's points are also a payment method), follow it.
     - **Every thing the entry names takes a line,** on its own capability, with its own `supports` and `reading`, even where that cell already holds the same placement. That includes what a description or tooltip names, the parent's thing where the entry's own words name it (its section is the parent's term), and a feature a table marks for the row (a ✔ under Recurring Payments).
   - **`new`:** no capability of the model is the entry's thing. Before you write `new`, search every domain with `class_slice.py caps --terms "<term>; <term>"`, in English and, for Salla and Zid, in Arabic. Where you would name a capability as the new thing's parent, read that capability's cells first: a place whose thing a capability already holds, as its cells' readings show, is that capability's evidence, not new.
     - Name it in `cap_id` as `new:<its name, in the platform's words>`, and give what it supports. Entries of the same new thing name it the same way.
     - Where it has a place of its own (B-extent, "What a place of its own is"), say which, in your notes. Where it has none, such as a thing one flag or one page shows, write `new:<name>` with `supports` `shows`, and say in your notes that it has no place of its own. A second thing an entry states that no capability holds takes its own `new` line. The coordinator decides each new thing with the others.
   - **`out`:** the entry isn't something the platform does for merchants, buyers, partners or developers. Leave every column but `reading` empty, and say why. Out are:
     - a UI string: a button, message or prompt that names no place, setting, plan line, permission, event or feature, such as "Close", "Dismiss", "Learn more" or "Back";
     - one store's or one account's own data: its orders, products, customers, people, ids, timestamps, tokens, and the values typed into it;
     - market data: a list of countries, currencies, languages, units or formats, or one country's own values. These are the subjects'.

     A setting, feature, flag, plan policy, entitlement or limit that the platform lists for a store is the platform's: place it on its capability, with the plan or store it is stated for as its `scope`. A thing the platform offers for a country or location, such as a payment provider, a free extension or a tax service, is placed on its capability, with that country as its `scope`.
3. **Sub-pages and containers:**
   - A sub-page, sub-route or setting is a capability's entry when it is that capability's own thing, or a part of it: its list, detail, edit or settings page, or one of its settings.
   - **A container** (a sidebar group, a section of sections) is never `out`. It goes on the capability its title or its group names, as the cells' readings show; failing that, on the capability whose page its own path opens; failing both, `new:<its title>` with `core`, since it is the platform's own admin place, its children named in your notes. Where the container has a page of its own with another thing, it takes a second line for it.
   - A section or route that only sits under a container (Settings, Apps, a menu, the admin), and whose own thing no capability holds as the cells' readings show, is `new`. Name its parent in your notes.
   - A field, a toggle or a line of text inside a page is never a place of its own.
4. **`supports`** takes `B-extent.md`'s values, as "Cells and evidence" and its conventions define them. This pass's entries are statements in that sense:
   - **`core`:** "the platform itself does it for the merchant": its own admin section, setting, route or built-in behaviour, a plan line that includes it, or its own API for its own feature. A list of third-party providers that the platform's own words call its integrations is `core`, each provider its filler.
   - **`own-service`:** the entry names the platform's company, or a company of its group, as the maker or provider of a separate product, app, extension or service that does it. A company counts as of the group where any held statement says so: the entry, another source of your batch (a terms page's parties or contracting entities), or a cell's own maker evidence. Cite it in `reading`. "Without a statement naming the company, place the cell by what its statements show, and note the missing maker statement as a gap." A brand in a product's name, a field's value such as `type: salla` or `type: platform`, and a capture's label never name a maker: a product named with the platform's brand is placed by what its entry shows, with the missing maker noted as a gap.
   - **`extension-point`:** "the statement shows third parties doing it through something the platform provides": an app store's category, an extension target, a provider interface, or an API whose statements say apps or partners use it. So are:
     - the platform's own list of third parties' things to connect or install (a channel catalog's card for a third party's solution, a list of tax services, a section for accounting software);
     - a route under an app's name, open only to the apps permission (B-extent's convention).

     A page at an app's address with no maker and no gate stated (Zid's Zid Ads) shows no third party: it is `shows` on what the app does, and `core` on CM-APP-007 as the dashboard's page for an app. A catalog card that names no one, or only the venue, is `core` by what it shows, with the missing maker noted as a gap.
   - **`outside`:** a third party named as doing it, with no interface of the platform named. A statement that makes the merchant or the buyer responsible is `shows`, never `outside`: a tooltip's "you can build a loyalty program with it" is `shows`; what a plan line "includes" is `core`.
   - **A partner's or an app's permission or access** is `shows` (the dry run's S7), and only the staff permission is `core`. That covers Shopify's collaborator permissions, its Partner API permission sets, an app's install consent, and Salla's partner access requests. Their selection rows carry this `note`.
   - **Flags and badges:** a released flag supports `core`, with its plans or store as its `scope`. A flag stated as not released (`released: false`, `is_experimental: true`) is `shows`. A page the platform lists with a badge (`new`, `beta`) is offered to the store: `core`, with the badge in `reading`. A flag named for a third party is the capability's evidence, never a slot filler.
   - **An entry that is only a help page's title, a changelog post or a FAQ** supports what its words state: `core` where it names the platform's own admin place, setting, route, plan line or built-in feature; `extension-point` where it names an app, an extension target or a provider interface; `shows` where it names only a topic, a guide or a third party. A release marker in it (beta, deprecated, sunset, now available) goes in `reading`. A row of a table inside a page isn't a title: rule 1 reads it with the page's words.
5. **The other columns:**
   - `scope`: the plan, country, market or store the entry or its source states it for, in their words, or empty. A listing condition the platform sets for a store (a store flag, a kind of store, a plan) is the entry's scope, in the source's identifier. A condition on the store's own data (a blog turned on, an app installed) goes in `reading`.
   - `terms`: the platform's own words for the thing, `;`-separated, each found in the entry's text. A store's state (suspended, trial) is its scope, never a term.
   - `filler`: a third party or a law the entry's own words name as doing it or setting its terms. A party known only from a source (a link, a sibling card) goes in `reading`, never in `filler`. A company of the platform's group is never a filler.
   - `quality`: a limit or value the entry states, as `<what>: <value in its words>`: a maximum, a rate, a fee, a duration, a certification, an uptime, a data location. A mark of inclusion (a check, "Available", "Included", "Yes") is never a quality: a plan's mark is the line's `scope`, and a provider's feature mark is a line on the feature's capability (rule 2).
6. **Group:** one line may name several entries, `;`-separated, where they have consecutive ids in your batch, are of one structure, and have the same placement, cap_id, supports, scope, terms, filler, quality and reading.
7. **`reading`:** a few words, a reading: why it lands there, or why it's out. A quote in single quotes is copied exactly from the entry or the file it cites. `held_amend.py` writes the reading into the model's evidence.

**Where you can't tell,** place it where it most plainly belongs, and list it in your notes with what would settle it. Don't leave an entry unplaced.

## Rules

- Every claim is one of three (`PLAN.md`, section 6):
  - a fact traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Never decide a maker, a third party or a placement from what you know of the platform: only from what the entry and its sources state, and the held statements the rules above name. A provider's role that only another platform's cell states (instalments, cryptocurrency) is a lead for your notes, not evidence.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence.
- observed-sh, observed-sa and other-product-class are read-only: never write, commit or push to them.
- Run Python with `python3 -I`.
- Don't change the model's files, the subjects' or the entries. Write only your batch's files, and make no commits.

## How to work, keeping your context small

Your batch holds about 150 entries. Your context should stay under about 200,000 tokens. The dry run's agents read every cell and step as they went, and passed it.
- **Read once, at the start:** the guides, your structures' `meta.json` and selection rows, and each structure's source, by the lines you need (`grep -n`, `sed -n`).
- **Work in chunks.** Print 60 to 100 entries at a time with `show --from --to --candidates`, decide them, and write the chunk's lines in one write.
- **Look things up where it can change the model.** Search the model, read a cell, or read a run step only where the entry's thing is unclear from its text and sources, or where its placement would change a cell: a cell that holds nothing, a new thing, or a `supports` the cell doesn't hold yet. The leads print each cell's state. Where the entry's words plainly name a lead's thing and that cell already holds the same placement, place it from its text.
- **A run of entries of one kind** (a list of carriers, gateways, permissions or routes under one section) is decided once, from its first entries and its source, then each entry's text is read for a difference.
- **Where you split a structure with the batch before yours,** read that batch's placements for it first (`held/<platform>/placements-<batch>.tsv`), and keep to them where the things are the same.
- **Write placements as you go,** never at the end.

## Output, in `studies/class-model/held/<platform>/`

- **`placements-<batch>.tsv`:** tab-separated, a header row, no quoting, no tab or newline inside a field, with these columns:
  - `entry_id`: one id, or several consecutive ones `;`-separated;
  - `placement`: `capability`, `new` or `out`;
  - `cap_id`: one cap_id, `new:<name>`, or empty;
  - `supports`: one value, or two different ones, `;`-separated; empty for `out`;
  - `scope`, `terms`, `filler`, `quality`, as above;
  - `reading`.
- **`notes-<batch>.md`:**
  - each `new` thing, with its entries, its place of its own (or none), its proposed domain, area and parent, its name in each language the platform uses, and the terms you searched;
  - entries you couldn't tell, and what would settle each;
  - a structure whose items and sources disagree;
  - what a source or run step states that no entry holds, with its file and line, for the second stage;
  - problems with this brief or the script.

Check your batch with `python3 -I method/held_entries.py check --platform <p> --batch <b>` until it prints no problem. Then read again each line it prints:
- `CHANGES`: a cell one line alone would change. These are the lines that matter most: read each against its sources;
- `NOTE`: each `own-service`, each `core` on a partner's or an app's permission, each third-party line that names a company of the platform's group, each `core` on a product named with the platform's brand, each footnote mark, each quote found nowhere held, each new thing whose entry has leads, each first lead whose cell holds nothing and that no line names, each app's embedded page with no CM-APP-007 line, and each container;
- `NEW`: the new names.

## Report

Back to the coordinator:
- your entries' count by placement;
- each `new` thing, with its entries;
- the `CHANGES` lines, with what you decided on each;
- any problem;
- the checker's final line.

## After the batches: the coordinator

The coordinator checks each batch, decides each new thing in `held/new.tsv` (the capability it is, an existing one, or out), and runs `method/held_amend.py`:
- each placement on a capability becomes an evidence row of that platform's cell, in the part that holds the cell, with its scope, terms, slot filler and quality;
- the cell's reading says what the held pass added;
- a cell that held nothing becomes held.

Then the parts are checked and merged again. `held_amend.py plan` prints, before anything is written, the cells whose supports would change.
