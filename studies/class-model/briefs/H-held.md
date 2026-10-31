# Brief: the held pass, the platforms' self-descriptions read entry by entry (Stage 4A)

**What this is.** The class's model was built from the concern map, finished on 12 October 2026. The evidence repositories hold much more of what the platforms list about themselves: route manifests, settings, navigation, plans, permissions, catalogs, events and changelogs. Some was captured after that date; some was held and never read. `studies/class-model/held-vs-read.md` measures the gap.

This pass reads every entry of those self-descriptions and places each on the model. What the platforms show of themselves then reaches the model through their own lists, read entry by entry, not by search alone (the founder, 30 October: the repositories' guides and indexes first, then search).

You draft placements. The coordinator checks them and amends the model from them: an entry placed on a capability becomes that platform's cell's evidence, a new capability is made with its cells, and the merge runs again. This pass sends no capture request. A gap goes in your notes, for the coordinator.

**This brief was rewritten after the dry run's review and inspected again** (`held/review-H.md`; the coordinator's rulings, `held/review-H-rulings.md`; `inspection-H2.md`). Most of the dry run's misses came from rules the brief had left out or stated loosely. The rest were care: a capability whose cell held nothing that the agent never looked for, a second thing an entry names left without its line, a quote not copied exactly. The checker now catches part of them; the lookups below catch the rest.

**Your batch.** Your message names a platform and a batch. `python3 -I method/held_entries.py show --platform <p> --batch <b> --from <i> --to <j> --candidates` prints its entries in order. Each one shows:
- its id;
- its structure, and the labels (a store, a language) it was held under;
- its text: the fields the platform states, in the source's order;
- its leads: capabilities whose cited statements share its identifiers, whose terms its values or its route's path hold, or whose own name shares its words (`by name`), each with what its cell on your platform holds now (`[cell: holds nothing]`, or its placements). A lead is only a lead. A lead whose `by` is only a field's name, or a word every entry of your structure holds, is no lead. About a quarter of the entries have none.

**Read only this brief and:**
- **the evidence map,** `studies/class-model/evidence-map.md`, for where to start and the faults found so far;
- **your platform's repository guides, before the entries:**
  - for Shopify (`/home/user/observed-sh`) and Salla (`/home/user/observed-sa`): `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`;
  - for Zid, BigCommerce and WooCommerce (`/home/user/other-product-class`): `README.md`, and the platform folder's `README.md` and `GAPS.md`;
  - then, by their rows: `structures/REGISTER.tsv` for your structures, and `index/` (for Shopify and Salla, `index/ledger-summary.tsv` and the `index/ledger/` file your structures enumerate);
- **what each structure is:** `held_entries.py show --platform <p> --batch <b> --meta` prints each structure's descriptive keys. Read any other key of a `meta.json` only where an entry needs it, by that key;
- `studies/class-model/held/selection.tsv`, your platform's rows: why each structure is read, its `placement` (the concern map's kind of statement: `where`, `decides`, `boundary`, `responsible`, not your output's column of that name) and its `note`;
- **the model:**
  - `method/class_slice.py caps --terms "<term>; <term>"`, `key` and `search`;
  - `method/held_entries.py cells --platform <p> <cap_id> <cap_id> ...`: each capability's cell on your platform, compactly (name, parent and note, what the cell holds and places, its terms, reading and evidence reasons). Read a chunk's leads with one call of it;
  - `method/land_points.py cell <cap_id> <platform>`, where you need a cell's every row;
  - `studies/class-model/merged/capabilities.tsv`, read with `cut` or `grep`, never whole;
- **the model's rules:** `studies/class-model/briefs/B-extent.md`, "Cells and evidence", and "Conventions from the dry run", with "What a place of its own is";
- **the coordinator's rulings,** `studies/class-model/held/review-H-rulings.md`.

The rules marked (M-n) or (ruling) are the coordinator's, on cases B-extent.md leaves open, each listed for the founder's veto: follow them. Where any other rule of this brief reads differently from B-extent.md, B-extent.md governs: say so in your notes.

**Effort:** your message names it: `high`, never below (the founder, 30 October). The dry run's review proposed `xhigh` for entries whose own words name what they are. A calibration placed 82 such entries again at `high` and at `xhigh` under this brief: `xhigh` cost 1.6 and 2.4 times as much, and missed the same important details, or others like them (`held/calibration.md`). Those misses are of a capability whose cell holds nothing and that no lead showed, which the lookups below are for.

## For each entry

1. **Read it as the platform states it.**
   - **Its sources:** the item, at the file and locator `entries.tsv` gives; and whatever its structure's `meta.json` names under `source`:
     - a held file (`held_as`, `file`, `html_file`, `held_in`);
     - an answer (`answer`);
     - a run's step (`run_id` with `step` or `steps`: `raw/runs/<run_id>/steps/<NNN>.*`, with its `.text.txt`);
     - an archive record (`warc`, `record_id`, `uri`): `python3 -I method/held_index.py <uri>` gives its offset, and `python3 -I method/warc_text.py <repository> <warc>@<offset>` prints it.

     Also the `source.*` file beside `items.jsonl`, and, for a structure built by a rule (`json:`, `rows:`, `release:`, `changes:`), the files its rule names in `selection.tsv`. The bytes are the evidence. Where the rendering, the item and the source differ, the source governs; say so in your notes.
   - **A row of a table, or an item of a list, inside an article** (a help page, a plan page, a guide) is read with the words the article gives it: its table's heading, the paragraph before it, its columns' definitions, and the footnotes its marks point to. A footnote an entry's mark points to (an asterisk) is part of the entry.
   - **A term the source defines** (a terms page's "Extension", a plan's "Performance") is read by its definition before you join it to a capability on the same word.
   - **To clarify an entry only,** you may also read: the source page around a segment the structure was cut from, the run steps and answers the platform's ledger or `index/runs.tsv` joins to it, the platform's locales for a route no run opened, the platform's features list (Salla's `dashboard-features`) for whether a feature an entry names is released and on which plans, and the model's cells. A reading that rests on one cites it at its file, such as `<run_id>/steps/<NNN>.text.txt`, and quotes it exactly. What such a file states clarifies the entry: the entry's `terms` and `filler` still come from its own text (rule 5, which the checker tests), and its `scope` and `quality` from its text and its structure's sources.
   - **What a run step or another file states that no entry holds** isn't placed here (M-12). List it in your notes, with its file and line, as a lead for the second stage, which reads held pages for the cells that hold nothing.
   - **Known cases:**
     - BigCommerce's `settings-list` pairs each section with the next section's address, so its entries carry none. Its source step `steps/002.frame-0.aria.yaml` holds each section's own (handoff H-009).
       An entry's `section` is its own title; its `group` (Setup, General, Orders, Products, Marketing, Domain, Advanced, API and MCP) is the group it sits under, with no entry of its own. A section takes its group's line only where it is a kind of the group's thing, or its description names that thing (rule 2). Name each group in your notes, with the capability its title names, as a lead.
     - In BigCommerce's `plan-comparison`, rows 8 to 13 carry another row's name in `feature`. Their entries are rendered from `feature_text` and the cells, which are the row's own (`source.html`).
     - Zid's `dashboard-route-manifest` items carry each route's `module` and `imports`, which the rendering leaves out. Where a route's path leaves its thing unclear, read its item: the module's name often names it.
     - An entry of Salla's `dashboard-app-routes` or `portal-app-routes` stands for every item with its app and path. A bundle may hold the same path as a route and as another object, such as a cookie library's `{path:'/'}`, and the entry's locator names only the first. Each item's `keys` lists the object's other keys: a route's include `element`, `children`, `redirect` or `index`. `show` prints each entry's items under it, with their keys and the bundle record each is in, and `show --code 300` also prints the bundle's code at each item's path: read a route's element, guard and redirect there, and open the bundle only where that code isn't enough. Place the entry for each item that is a route. It is `out` only where none of them is (SA-9's check).
     - Salla's `com-plans` holds the plans page's text nodes only. Its "Key features" rows mark each plan in the page's HTML, not in `text.txt`: `data-framer-name="Included (Check)"` or `"Not Included (Cross)"`, one per plan, in the cards' order. The page is the archive record its `meta.json` names: print it as above. Write the plans each row is included in as its `scope`. A line the page repeats is one entry: grep `text.txt` for each place it stands.
     - A row of a repository's derived table (Salla's `plan-gates` and `permission-gates`, Shopify's `admin-router-changes`) joins bytes the repository holds (`capture/gates.py` says what each column holds). The columns that quote the platform are the entry's text:
       - in `plan-gates`: the features (`nav_features`, `features_list_plans`, `enabled_merchant`, `enabled_demo`, `enabled_public_demo`), `edu_allowedPlans`, and each store's plan lines, quoted whole from its page: `merchant` (store-1-da, on Basic), `demo` (store-sherawya, on Pro) and `public_demo` (giftshop2024, on Basic);
       - in `permission-gates`: `permissions`, and each store's 'Access restricted' lines (`merchant_or_feature`, `demo_or_admin`, `public_demo_or_shown` on a dashboard row);
       - in `admin-router-changes`: `eligibility before` and `after`.

       A row's address is the step's requested path. A settings address (`/?settings=/orders`) opens a drawer over the home page, so a store's lines at that address can be the home page's, such as its Abandoned carts widget's 'Not included in your plan'. Read the step to see which element each line belongs to, and place the row by its own address's gate. A row whose only lines are another page's states nothing of its own: it is `out`, its reading naming the entry that holds the statement (SA-33's check).

       The repository's own columns, such as `held` (whether the staff permission groups hold each permission) and `steps`, are its observations: never the platform's terms, a scope or a quote. Where a placement rests on a row, cite the step or file it was built from. (Corrected after SA-32: `demo` was listed as the repository's own.)
     - A `parent` or `within` that is still a number is the `position` of an item with no name of its own: an Android layout node, whose screen is its label, or a route whose path is a constant (Salla's `parent: 2388`, a route at `T.inventoryTransfer`). Find the item by that `position` in the same `items.jsonl`.
2. **Place it**, one of three:
   - **`capability`:** the model's capability whose thing the entry is. Name one cap_id.
     - **Search for its place first.** Before you place a section, a route or a setting, search the model for its own place (such as "Settings > API and MCP > MCP") and its address, where its own identifier (a route id, a path, a key) gave no lead. Where another capability's cell already cites that place, the entry is that capability's.
     - **Read the placed capability's note.** Where it names a homonym, or says where else such an entry belongs (Mokafaa's points are also a payment method), follow it.
     - **Every thing the entry names as its own takes a line,** on its own capability, with its own `supports` and `reading`, even where that cell already holds the same placement. That includes what a description or tooltip names, the parent's thing where the entry's own words name the entry as one of it (its section or title is the parent's term, and the entry is a kind of what that term names, as Bank deposit under OFFLINE PAYMENT METHODS is an offline payment method; a pageKey's or path's prefix isn't the entry's words) (M-6, refined after the calibration), and a feature a table marks for the row (a ✔ under Recurring Payments). The marked feature's line is `shows` unless the row says who does it, with the provider as its `filler` (D4). A third party's own feature that the platform's listing names is `extension-point` on that feature's capability, beside the provider's line (M-8). A route's `nextRoutes` or `redirect` names another place, not its own thing. A group the entry only sits under (BigCommerce's `group: General`, a sidebar's group, Settings), whose title says where the entry is, not what it is, gives the entry no line: the group is placed once, as a container (rule 3).
     - **Before you write an entry's lines, find the capability of each thing its words name:** from its leads, or with `class_slice.py caps --terms` for a thing no lead names. Read each one's cell where the leads don't print it. Where a cell's reading cites the same page, place or term, the entry is that capability's too.
     - **A lead to a broad capability doesn't end the search** where the entry names a narrower thing: a lead to reviews (CM-SUP-001) for "Product review notifications" doesn't settle whether it is review requests (CM-SUP-002). Search for the narrower thing too. `caps --terms` finds a term inside a capability's name, note or cells' terms, so search the phrase, then its words' roots, in each language the entry gives (`review request`; `تقييم`, not `التقييمات`).
   - **`new`:** no capability of the model is the entry's thing. Before you write `new`, search every domain with `class_slice.py caps --terms "<term>; <term>"`, in English and, for Salla and Zid, in Arabic. Where you would name a capability as the new thing's parent, read that capability's cells first: a place whose thing a capability already holds, as its cells' readings show, is that capability's evidence, not new.
     - Name it in `cap_id` as `new:<its name, in the platform's words>`, and give what it supports. Entries of the same new thing name it the same way.
     - Where it has a place of its own (B-extent, "What a place of its own is"), say which, in your notes. Where it has none, such as a thing one flag or one page shows, write `new:<name>` with `supports` `shows`, and say in your notes that it has no place of its own. A second thing an entry states that no capability holds takes its own `new` line. The coordinator decides each new thing with the others.
   - **`out`:** the entry isn't something the platform does for merchants, buyers, partners or developers. Leave every column but `reading` empty, and say why. Out are:
     - a UI string: a button, message or prompt that names no place, setting, plan line, permission, event or feature, such as "Close", "Dismiss", "Learn more" or "Back";
     - one store's or one account's own data: its orders, products, customers, people, ids, timestamps, tokens, its subscription records, and the values typed into it;
     - market data: a list of countries, currencies, languages, units or formats, or one country's own values. These are the subjects';
     - the software's own bookkeeping: a schema or database version, a migration's done-marker, a cache, a stored state, an install or activation time;
     - a template or scaffold the code holds for no place (a `{app-name}` placeholder), and a layout node that names nothing.

     A setting, feature, flag, plan policy, entitlement or limit that the platform lists for a store or an account is the platform's: place it on its capability, with the plan, store or account it is stated for as its `scope`. Its value for that store goes in `reading`. The add-on a store's subscription names (`type: addon`) is the platform's offer: place it on its capability, the store as its `scope`. A thing the platform offers for a country or location, such as a payment provider, a free extension or a tax service, is placed on its capability, with that country as its `scope`.
3. **Sub-pages and containers:**
   - A sub-page, sub-route or setting is a capability's entry when it is that capability's own thing, or a part of it: its list, detail, edit or settings page, or one of its settings.
   - **A container** (a sidebar group, a section of sections, a menu's parent) is never `out`. It goes on the capability its title or its group names, as the cells' readings show; failing that, on the capability whose page its own path opens; failing both, `new:<its title>` with `core`, since it is the platform's own admin place, its children named in your notes (M-13). Where the container has a page of its own with another thing, it takes a second line for it. A section whose title names only a grouping is placed the same way. A title the source gives under a condition is a statement of its own, with that condition as its `scope` (M-14).
   - A section or route that only sits under a container (Settings, Apps, a menu, the admin), and whose own thing no capability holds as the cells' readings show, is `new`. Name its parent in your notes.
   - A field, a toggle or a line of text inside a page is never a place of its own.
4. **`supports`** takes `B-extent.md`'s values, as "Cells and evidence" and its conventions define them. This pass's entries are statements in that sense:
   - **`core`:** "the platform itself does it for the merchant": its own admin section, setting, route or built-in behaviour, a plan line that includes it, or its own API for its own feature. A list of third-party providers that the platform's own words call its integrations is `core`, each provider its filler (M-4).
   - **The platform's own API** (its folder, object, access scope, webhook topic, REST controller, or a mutation's requirement) for its own feature is `core`, on that feature's capability, a guide addressed to app developers included. It is `extension-point` only where the API's statements say apps or partners use it to do the work (B-extent, "Conventions from the dry run"). A scope or scope group of the API's own list (Shopify's `dev-dashboard-scopes`) is `core`, as the model places the same scopes (CM-POS-003: "own access scope read_cash_tracking").
   - **`own-service`:** the entry names the platform's company, or a company of its group, as the maker or provider of a separate product, app, extension or service that does it. A company counts as of the group where any held statement says so: the entry, another source of your batch (a terms page's parties or contracting entities), or a cell's own maker evidence. Cite it in `reading` (M-1). The companies the model holds as the platform's group are in its CM-ACC-002 cell (`land_points.py cell CM-ACC-002 <platform>`), and the checker's `GROUP` list holds them; a company a held statement places in the group, which that cell lacks, goes in your notes. A named company that no held statement places in or out of the group is not a third party for that reason: place the line by what the entry shows, and note the missing maker statement as a gap. A brand in a product's name, a field's value whose meaning the source doesn't state (Salla's `type: salla`, `type: platform`), and a capture's label never name a maker. A field that the platform's own code shows to merchants as a maker statement does (ruling): WooCommerce's `is_built_by_wc: true`, which its admin shows as "Built by WooCommerce" (`woocommerce-11.2.1:assets/client/admin/chunks/3799.js`; `src/Internal/Admin/RemoteFreeExtensions/DefaultFreeExtensions.php`, line 123), names WooCommerce as the maker: `own-service`, citing both in `reading`. The release is unpacked at `/home/user/woocommerce-release/11.2.1/woocommerce/`, the root of those paths. `is_built_by_wc: false` names no maker. A tag or field that no admin asset shows to merchants names no maker either, the more so where a statement merchants are shown names another: WooCommerce's payments suggestions' tag `made_in_woo`, which the release defines only in a constant's comment, 'For extensions developed by Woo.' (`src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php`, line 105), against 'PayPal Payments by PayPal' (WC-S-0911) (ruling, after WC-4). A held line places one entry: place it by what the entry shows.
   - **`extension-point`:** "the statement shows third parties doing it through something the platform provides": an app store's category, an extension target, a provider interface, or an API whose statements say apps or partners use it to do the work. So are (M-3, M-7):
     - the platform's own list of third parties' things to connect or install (a channel catalog's card for a third party's solution, a list of tax services, a section for accounting software);
     - a route under an app's name, open only to the apps permission (B-extent's convention).

     A page at an app's address with no maker and no gate stated (Zid's Zid Ads) shows no third party: it is `shows` on what the app does, and `core` on CM-APP-007 as the dashboard's page for an app (M-10). A catalog card that names no one, or only the venue, is `core` by what it shows, with the missing maker noted as a gap. The venue it names is its `filler` (M-3): a marketplace or an ad platform, such as Google in "Google for WooCommerce".
   - **`outside`:** a third party named as doing it, with no interface of the platform named. A statement that makes the merchant or the buyer responsible is `shows`, never `outside`: a tooltip's "you can build a loyalty program with it" is `shows`; what a plan line "includes" is `core` (M-9).
   - **What a partner or an app asks of a merchant or of the platform** (a collaborator request, a Partner API permission set, an app's install consent) is `shows` (ruling: the dry run's S7, as `inspection-H.md`'s B-1 widened it), and only the staff permission is `core`. That covers Shopify's collaborator permissions, its Partner API permission sets, an app's install consent, and Salla's partner access requests. Their selection rows carry this `note`. The permissions of a platform's own Partners portal, which gate what a partner's own team does there (Salla's `permission-gates` rows of `surface: portal`), are the platform's own feature: `core` on the capability of what they gate, as a staff permission is in a merchant's admin (ruling).
   - **Flags, badges and release states (ruling):**
     - a flag the source states isn't released (`released: false`, `is_experimental: true`) is `shows`, whatever its value for the store;
     - a released flag (`released: true`, `is_experimental: false`) supports `core`, with its plans as its `scope`, or the store's label where it names no plan. Its value for that store (`enabled`, `enabled_by_default`) goes in `reading`;
     - a released flag the platform leaves off by default and hides from the admin (WooCommerce's `disable_ui` true, with `enabled_by_default` false or left at its default, false) isn't offered to merchants to turn on: `shows` (ruling, after WC-6);
     - a store's flag stated only by its value (Zid's `feature_flags`, `key: …; value: true|false`): `true` supports `core`, the store as its `scope`; `false` supports `shows`, the value in `reading`. A name that says pilot, preview or test (`is_mazeed_pilot`) supports `shows` while its value is `false`;
     - what the platform states is in early access, a preview or a beta available only to some merchants or stores supports `shows`, its words in `reading`: Shopify's help notes ("is in early access, and is available only to certain merchants"); a dev store's feature previews ("before they're generally available");
     - a route gated only by Shopify's hashed `betas`: read `structures/shopify/admin-betas/<store>/items.jsonl`. A beta `enabled: true` in a held store makes the route `core`, that store its `scope`; `false` in every held store makes it `shows`;
     - a page or route the platform lists with a badge (`new`, `beta`), with no such limit stated, is offered to the store: `core`, the badge in `reading` (D1);
     - a flag named for a third party is the capability's evidence, never a slot filler.
   - **An entry that is only a help page's title, a changelog post or a FAQ** supports what its words state: `core` where it names the platform's own admin place, setting, route, plan line or built-in feature; `extension-point` where it names an app, an extension target or a provider interface; `outside` where it names a third party as doing it with no interface of the platform; `shows` where it names only a topic or a guide. A release marker in it (beta, deprecated, sunset, now available) goes in `reading`. A row of a table inside a page isn't a title: rule 1 reads it with the page's words.
5. **The other columns:**
   - `scope`: the plan, country, market, store or account the entry or its sources state it for, in their words, or empty. Where your reading rests on the source's words for a plan, a country or a store (a region's "with paid plan"), put them in `scope`. Several go `;`-separated. An entry's lines share one scope: give each of them the same, except where the entry stands for several items whose conditions differ (a route structure's repeated path), where each line takes its own item's scope. A listing condition the platform sets for a store (a store flag, a kind of store, a store's state such as trial or suspended, a plan) is the entry's scope, in the source's identifiers. A route's gate on the store (`features`, `entitlements`, `betas`, `organizationFeatures`, `organizationFlags`, `regions`, a plan) is its scope too. A condition with no name of its own is named by the module it comes from, or by what it is computed from, as a reading (M-11). A module an item imports isn't a condition by being imported (nearly every Zid route imports `use-is-ngo-store`); a guard the route is wrapped in is (`new-zones-feature-guard`). A gate on the user (a staff permission: Shopify's `permissions` and `organizationPermissions`, Zid's page permission) is named in `reading`, and takes a line on CM-STF-002 only where the entry names the permission as its own thing. In a list of permissions (Zid's `store-permissions`, Shopify's role permissions), each permission is `core` on the capability it gates, as CM-STF-002's note keeps them, and only a permission over the staff's permissions themselves goes on CM-STF-002 (ruling, after ZD-7). A condition on the store's own data (a blog turned on, an app installed) goes in `reading`.
   - `terms`: the platform's own words for the thing, `;`-separated, each found in the entry's text. A store's state (suspended, trial) is its scope, never a term.
   - `filler`: a third party or a law the entry's own words name as doing it or setting its terms. A catalog card's venue is its filler (M-3). A party known only from a source (a link, a sibling card) goes in `reading`, never in `filler`. A company of the platform's group is never a filler.
   - `quality`: a limit, a certification, an uptime or a data location the entry states, or a value of the kind the model's `qualities.tsv` records (a maximum, a rate, a fee, a price, a duration), as `<what>: <value in its words>`, by plan where the entry gives one. This follows the model's practice, wider than B-extent.md's list. A mark of inclusion (a check, "Available", "Included", "Yes") is never a quality: a plan's mark is the line's `scope`, and a provider's feature mark is a line on the feature's capability (rule 2). A store's own value of a setting or a flag (an option's value, `enabled: true`, `value: false`) is never a quality: it goes in `reading`.
6. **Group:** one line may name several entries, `;`-separated, where they have consecutive ids in your batch, are of one structure, and have the same placement, cap_id, supports, scope, terms, filler, quality and reading.
7. **`reading`:** a few words, a reading: why it lands there, or why it's out. A quote in single quotes is copied exactly from the entry or the file it cites. `held_amend.py` writes the reading into the model's evidence.

**Where you can't tell,** place it where it most plainly belongs, and list it in your notes with what would settle it. Don't leave an entry unplaced.

## Rules

- Every claim is one of three (`PLAN.md`, section 6):
  - a fact traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Never decide a maker, a third party or a placement from what you know of the platform: only from what the entry and its sources state, and the held statements the rules above name. A provider's role that only another platform's cell states (instalments, cryptocurrency) is a lead for your notes, not evidence (M-5).
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence.
- observed-sh, observed-sa and other-product-class are read-only: never write, commit or push to them.
- Run Python with `python3 -I`.
- Don't change the model's files, the subjects' or the entries. Write only your batch's files, and make no commits.

## How to work, keeping your context small

Your batch holds 50 to 200 entries. Your context should stay under about 200,000 tokens.
- **Read once, at the start:** the guides, your structures' descriptive keys (`show --meta`) and selection rows, and each structure's source, by the lines you need (`grep -n`, `sed -n`). Don't read the scripts' code: this brief and each script's `--help` say what it prints and what the checker tests.
- **Work in chunks.** Print 30 to 60 entries at a time with `show --from --to --candidates`, decide them, and write the chunk's lines in one write. An entry longer than the print's width ends in `…`: print it whole with `--width 4000`.
- **Make your lookups together.** Each turn re-reads your whole context, so one turn that asks for five things costs a fifth of five turns. Put several commands in one call, or make several calls in one turn: the cells of a chunk's leads, one `caps --terms` search with the words of every entry no lead names, the run steps of several entries.
- **Rule 2's lookups always run:** the search for a section's, a route's or a setting's own place where its own identifier gave no lead; the capability's note, before you place on it; and the capability and cell of every thing the entry's words name. Rule 1's reading always runs where the entry's text leaves a column open: the heading, plan card, country line or listing condition that gives its `scope`, `filler` or `quality`. Skip a lookup only where all of these hold: a lead names the entry's thing by the entry's own identifier; its cell already holds the same placement; its note names no homonym; and the entry's text states its scope, filler and quality.
- **Read as far as the entry's sources go, not further.** Its item, its structure's source and `meta.json`, and the run steps, answers, locales and cells rule 1 names. Don't trace a condition, a key or a module through other code or archives: write what those sources state, and put what a deeper read would settle in your notes.
- **A run of entries of one kind** (a list of carriers, gateways or permissions) is decided once, from its first entries and its source, then each entry's text is read for a difference. Routes and settings are placed one by one, since a section's routes are many capabilities' (rule 3).
- **Where you split a structure with the batch before yours,** read that batch's placements for it first (`held/<platform>/placements-<batch>.tsv`), and keep to them where the things are the same. If it hasn't run yet, say so in your notes; the coordinator aligns the two.
- **Write placements as you go,** never at the end.
- **Keep your working files in a folder of your own,** named for your batch, inside the scratchpad directory your system prompt names (such as `<scratchpad>/ZD-6/`), never in its root: other agents share it, and a batch overwrote another's file there.

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
