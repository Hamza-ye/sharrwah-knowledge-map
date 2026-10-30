# Brief: the held pass, the platforms' self-descriptions read entry by entry (Stage 4A)

**What this is.** The class's model was built from the concern map, finished on 12 October 2026. The evidence repositories hold much more of what the platforms list about themselves: route manifests, settings, navigation, plans, permissions, catalogs, events and changelogs. Some was captured after that date; some was held and never read. `studies/class-model/held-vs-read.md` measures the gap.

This pass reads every entry of those self-descriptions and places each on the model. What the platforms show of themselves then reaches the model through their own lists, read entry by entry, not by search alone (the founder, 30 October: the repositories' guides and indexes first, then search).

You draft placements. The coordinator checks them and amends the model from them: an entry placed on a capability becomes that platform's cell's evidence, a new capability is made with its cells, and the merge runs again. This pass sends no capture request. A gap goes in your notes, for the coordinator.

**Your batch.** Your message names a platform and a batch. `python3 -I method/held_entries.py show --platform <p> --batch <b> --from <i> --to <j> --candidates` prints its entries in order. Each one shows:
- its id;
- its structure, and the labels (a store, a language) it was held under;
- its text: the fields the platform states, in the source's order;
- its leads: capabilities whose cited statements share its identifiers, or whose terms it holds. A lead is only a lead.

**Read only this brief and:**
- **the evidence map,** `studies/class-model/evidence-map.md`, for where to start;
- **your platform's repository guides, before the entries:**
  - for Shopify (`/home/user/observed-sh`) and Salla (`/home/user/observed-sa`): `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`;
  - for Zid, BigCommerce and WooCommerce (`/home/user/other-product-class`): `README.md`, and the platform folder's `README.md` and `GAPS.md`;
  - then, by their rows: `structures/REGISTER.tsv` for your structures, and `index/` (for Shopify and Salla, `index/ledger-summary.tsv` and the `index/ledger/` file your structures enumerate);
- **what each structure is:** `held_entries.py show --platform <p> --batch <b> --meta` prints the descriptive keys of each structure's `meta.json`. Read the rest of a `meta.json` only where an entry needs it;
- `studies/class-model/held/selection.tsv`, your platform's rows: why each structure is read, its `placement` and its `note`;
- **the model:**
  - `method/class_slice.py caps --terms "<term>; <term>"`, `key` and `search`;
  - `method/land_points.py cell <cap_id> <platform>`;
  - `studies/class-model/merged/capabilities.tsv`, read with `cut` or `grep`, never whole;
- **the model's rules:** `studies/class-model/briefs/B-extent.md`, "Cells and evidence", and "Conventions from the dry run", with "What a place of its own is".

**Effort:** `high` at least (the founder, 30 October).

## For each entry

1. **Read it as the platform states it.** Where its text leaves it unclear, read its item at the source and locator `entries.tsv` gives: a file and line, or a JSON pointer. The bytes are the evidence. Where a structure's items and its source disagree, the source governs; say so in your notes. Known cases:
   - BigCommerce's `settings-list` pairs each section with the next section's address, so its entries carry none. Its source step `steps/002.frame-0.aria.yaml` holds each section's own (handoff H-009).
   - In BigCommerce's `plan-comparison`, rows 8 to 13 carry another row's name in `feature`. Their entries are rendered from `feature_text` and the cells, which are the row's own (`source.html`).
2. **Place it**, one of three:
   - **`capability`:** the model's capability whose thing the entry is. Name one cap_id. Where the entry is two capabilities' at once, write two lines with the same `entry_id`, each with its own `supports` and `reading`.
   - **`new`:** no capability of the model is the entry's thing. Before you write `new`, search every domain with `class_slice.py caps --terms "<term>; <term>"`, in English and, for Salla and Zid, in Arabic.
     - Name it in `cap_id` as `new:<its name, in the platform's words>`, and give what it supports. Entries of the same new thing name it the same way.
     - Where it has a place of its own (B-extent, "What a place of its own is"), say which, in your notes. Where it has none, such as a thing one flag or one page shows, write `new:<name>` with `supports` `shows`, and say in your notes that it has no place of its own. The coordinator decides each new thing with the others.
   - **`out`:** the entry isn't something the platform does for merchants, buyers, partners or developers. Leave every column but `reading` empty, and say why. Out are:
     - a UI string: a button, message or prompt that names no place, setting, plan line, permission, event or feature, such as "Close", "Dismiss", "Learn more" or "Back";
     - one store's or one account's own data: its orders, products, customers, people, ids, timestamps, tokens, and the values typed into it;
     - market data: a list of countries, currencies, languages, units or formats, or one country's own values. These are the subjects'.

     A setting, feature, flag, plan policy, entitlement or limit that the platform lists for a store is the platform's: place it on its capability, with the plan or store it is stated for as its `scope`. A thing the platform offers for a country or location, such as a payment provider, a free extension or a tax service, is placed on its capability, with that country as its `scope`.
3. **Sub-pages and containers:**
   - A sub-page, sub-route or setting is a capability's entry when it is that capability's own thing, or a part of it: its list, detail, edit or settings page, or one of its settings.
   - A section or route that only sits under a container (Settings, Apps, a menu, the admin), and whose own thing no capability holds as the cells' readings show, is `new`. Name its parent in your notes.
   - A field, a toggle or a line of text inside a page is never a place of its own.
4. **`supports`** takes `B-extent.md`'s values exactly as "Cells and evidence" and its conventions define them. This pass's entries are statements in that sense. In particular:
   - **`core`:** the platform's own admin place, setting, route, plan line or staff permission, its own API for its own feature, or a built-in feature it states;
   - **a partner's or an app's permission or access** is `shows` (the dry run's S7), and only the staff permission is `core`. That covers Shopify's collaborator permissions, its Partner API permission sets, an app's install consent, and Salla's partner access requests. Their selection rows carry this `note`;
   - **`own-service`:** only where the entry names the platform's company, or a company of its group, as the maker or provider of a separate product, app, extension or service. A brand in a product's name, a field's value such as `type: salla`, and a capture's label never name a maker;
   - **`extension-point`:** an app's page, an app store's category, an extension target or a provider interface. A route under an app's name, open only to the apps permission, is the app's page (B-extent's convention);
   - **`outside`:** a third party named as doing it, with no interface of the platform named. A statement that makes the merchant or the buyer responsible is `shows`, never `outside`;
   - **flags:** a released flag supports `core`, with its plans or store as its `scope`. A flag that isn't released (`released: false`, `is_experimental: true`, a beta) is `shows`. A flag named for a third party is the capability's evidence, never a slot filler;
   - **a help page's title, a changelog post, or a FAQ** supports what its words state: `core` where it names the platform's own admin place, setting, route, plan line or built-in feature; `extension-point` where it names an app, an extension target or a provider interface; `shows` where it names only a topic, a guide or a third party. A release marker in it (beta, deprecated, sunset, now available) goes in `reading`.
5. **The other columns:**
   - `scope`: the plan, country, market or store the entry states it for, in its words, or empty;
   - `terms`: the platform's own words for the thing, `;`-separated, each found in the entry's text;
   - `filler`: a third party or a law the entry names as doing it or setting its terms, or empty;
   - `quality`: a limit or value the entry states, as `<what>: <value in its words>`, or empty.
6. **Group:** one line may name several entries, `;`-separated, where they have consecutive ids in your batch, are of one structure, and have the same placement, cap_id, supports, scope, terms, filler, quality and reading.
7. **`reading`:** a few words, a reading: why it lands there, or why it's out.

**Where you can't tell,** place it where it most plainly belongs, and list it in your notes with what would settle it. Don't leave an entry unplaced.

## Rules

- Every claim is one of three (`PLAN.md`, section 6):
  - a fact traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Never decide a maker, a third party or a placement from what you know of the platform: only from what the entry and its source state.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence.
- observed-sh, observed-sa and other-product-class are read-only: never write, commit or push to them.
- Run Python with `python3 -I`.
- Don't change the model's files, the subjects' or the entries. Write only your batch's files, and make no commits.

## How to work, keeping your context small

- Print your entries 60 to 100 at a time with `show --batch <b> --from --to --candidates`. Your batch holds about 300.
- Where you split a structure with the batch before yours, read that batch's placements for it first (`held/<platform>/placements-<batch>.tsv`), and keep to them where the things are the same.
- Write placements as you go, never at the end.

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
  - a structure whose items and source disagree;
  - problems with this brief or the script.

Check your batch with `python3 -I method/held_entries.py check --platform <p> --batch <b>`, until it prints no problem. It prints each `own-service`, each `core` on a partner's or an app's permission, and the new names: read them again.

## Report

Back to the coordinator:
- your entries' count by placement;
- each `new` thing, with its entries;
- any problem;
- the checker's final line.

## After the batches: the coordinator

The coordinator checks each batch, decides each new thing in `held/new.tsv` (the capability it is, an existing one, or out), and runs `method/held_amend.py`:
- each placement on a capability becomes an evidence row of that platform's cell, in the part that holds the cell, with its scope, terms, slot filler and quality;
- the cell's reading says what the held pass added;
- a cell that held nothing becomes held.

Then the parts are checked and merged again. `held_amend.py plan` prints, before anything is written, the cells whose supports would change.
