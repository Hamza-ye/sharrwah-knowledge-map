# SH-99: Shopify's `shopify-cli-commands` (last 38), `shopify-com-header-nav` (29, all) and `sidekick-composer` (20, all) (notes)

**The batch:** platform `shopify`, batch `SH-99`, effort `high`, 87 entries in 105 lines, at observed-sh `e38dc17e3` (the clone is at `04de369da`, which changes no structure read here).
- `shopify-cli-commands` (entries 1 to 38): the rest of the oclif manifests of Shopify CLI 4.8.3 (run `20260930T093750Z-npm-shopify-cli-tarball`) and 5.0.0 (run `20261031T003934Z-npm-dev-mcp-1.18.0-cli-5.0.0`), each command and topic once, in its latest version's words (`selection.tsv`, row 54). SH-98 placed the first 122. Mine are:
  - the `store:` commands after `store:auth:list` and `store:auth` (1 to 12);
  - the top-level and CLI-housekeeping commands (`search`, `upgrade`, `version`, `send-analytics`, `help`, `auth:*`, `debug:command-flags`, `kitchen-sink:*`, `doctor-release:*`, `doc:*`, `docs:generate`, `notifications:*`, `cache:clear`, `config:autoupgrade:*`) (13 to 35);
  - the three topics only 5.0.0's `package.json` has: `app:import`, `app:subscription-migrations`, `app:security` (36 to 38).
- `shopify-com-header-nav` (39 to 67): www.shopify.com's header, run `20260930T050139Z-shopify-com-pages`, the items the concern map didn't cite. Of its 59 items, the concern map's statements quote positions 12 to 16, 18 to 25, 27 to 31, 33 to 36, 38 to 40 and 42 to 44 (`studies/concern-map/checks/shopify-quotes.tsv`, SH-S-2727 to SH-S-2754). Positions 57 and 58 repeat Log in and Start for free (54 and 55) and have no entry of their own: a reading, that the build keeps a repeated line as one entry.
- `sidekick-composer` (68 to 87): run `20261007T030938Z-journey-sidekick` on capture-plus, steps 006 (the popover Add files and more), 031 (the dialog Create new Skill) and 004 (Sidekick's Settings).

**Count by placement:** 70 entries on capabilities alone, 1 with a `new` line too (Store preview), 16 `out`. By line: 64 `core`, 24 `shows` and 1 `own-service` on capabilities, 1 `new` line (`shows`), 15 `out` lines. Every CLI entry has its CM-DVT-002 line (38).

**What I read:**
- the brief, the evidence map, B-extent's "Cells and evidence" and "Conventions from the dry run", the rulings (all of them, the last section governing), SH-98's notes and placements;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, `REGISTER.tsv` rows 56, 58 and 103, `index/ledger-summary.tsv`, and `index/ledger/sitemap--shopify-com-sitemap.tsv` and `journey-unit.tsv` (the rows for my pages and Sidekick's journey);
- `selection.tsv`'s three rows, `show --meta`, and each structure's `meta.json`;
- the CLI's source: `package/oclif.manifest.json` and `package/package.json` of each version, taken out of the npm tarballs in the WARC records `meta.json` names (5.0.0 at `fetch.warc.gz@16067323`, 4.8.3 at `@1156`) into my scratch folder. Their sha256 match `meta.json`'s `sha256`, `member_sha256` and `package_json_sha256`. Every quote my CLI lines take from them was checked against the decoded manifests by script;
- the header's `source.html`, and the three pages its links open that the readings rest on (`/start`, `/sell`, `/enterprise`, by the ledger's records in `20260930T050139Z-shopify-com-pages`): their titles, descriptions and headings only;
- Sidekick's run: `actions.jsonl` (steps 1 to 40), and steps 004, 006, 030 and 031 (`aria.yaml`, `text.txt`, and `006.html` for the popover's structure);
- the cells of every lead and of the capabilities the entries name (AI's CM-AIA-001 to 005 among them), the Editions digest's rules 17, 41, 51, 53, 54 and E105, E106, E112, R47.1, SH-47's notes on Store preview, SH-68's R3 and R4, and the earlier lines `earlier` printed or the readings cite (SH-1, SH-23, SH-34, SH-35, SH-36, SH-47, SH-48, SH-51, SH-63, SH-65, SH-66, SH-67, SH-73, SH-92, SH-93, SH-98).

## `shopify-cli-commands`: R98.1 to R98.11, kept

Each command is CM-DVT-002 `core`, its id the term (R98.1); a topic a container (R98.2); the platform's thing a command works on takes its own capability (R98.3); hidden commands `shows` (R98.4); flags read with their command (R98.8); limits as qualities (R98.9). The cases this batch adds:
- **R99.10, a `store` flag that names no kind of store gives no scope** (R98.11 read the other way). The `store:bulk:*`, `store:execute`, `store:graphiql`, `store:info`, `store:open` and `store:delete` flags read only 'The myshopify.com domain of the store.', so their lines take none, unlike `app:bulk:*`'s 'Must be an existing dev store.'. `store:delete` deletes 'a dev store' by its own words: the dev store is its object, on CM-DVT-004, not a condition.
- **R99.11, a command's own default isn't a quality.** 'Mutations are disabled by default.' (`store:execute`, `store:graphiql`, `store:bulk:execute`), with the flag `allow-mutations` to run them, goes in `reading`: it is the CLI's option, not a limit of the platform such as `app:execute`'s 'only allowed on dev stores' (R98.9).
- **R99.12, two statements of the platform that differ give no quality.** `config:autoupgrade:on` says the CLI 'automatically updates to the latest version once per day' (5.0.0's manifest, line 13670), `config:autoupgrade:status` 'after each command' (line 13726). Both go in `reading`, as SH-98 read autocorrect's two defaults.
- The things the `store:` commands work on, by R98.3:
  - bulk operations CM-API-007, the 7 days of `store:bulk:status` its quality, in SH-98's words (line 6);
  - the Admin API's queries and GraphiQL CM-API-001 (`store:execute`, `store:graphiql`), as SH-98's `app:execute` and `app:graphiql`;
  - an app's online access token CM-API-002 (`store:stripe-auth`, hidden, so `shows`), as SH-98's `store:auth`;
  - dev stores CM-DVT-004 (`store:create:dev`, `store:delete`);
  - the organization's stores CM-DVT-003 (`store:list`), a reading: the organization is the Dev Dashboard's ('Your organization ID can be found in your Dev Dashboard URL', `app init`'s flag, line 2496), as SH-98 read `organization:list` on CM-PTN-002, and SH-23 placed the Dev Dashboard's item Stores on CM-DVT-003 (SH-E-51754798);
  - the storefront CM-SFR-001 (`store:open`), as SH-98's `theme:open`;
  - the preview store, `new:Store preview` (below).
- `store:info` returns a list of what it prints (id, organization, store owner, plan, feature preview, access and save URLs): CM-DVT-002 alone (the ruling after SA-41; R98.3).
- **Documentation:** `search`, `doc:fetch` and `doc:search` take CM-DVT-001 for shopify.dev's documentation, as SH-98's topic `doc`. `docs:generate`, hidden, generates 'CLI commands documentation' with no word on where it goes: CM-DVT-002 alone.
- **The CLI's own housekeeping** (`upgrade`, `version`, `help`, `auth:login`, `auth:logout`, `config:autoupgrade:*`, and the hidden `send-analytics`, `debug:command-flags`, `kitchen-sink:*`, `doctor-release:*`, `notifications:*`, `cache:clear`): CM-DVT-002 alone, the hidden ones `shows`. The CLI's notifications, cache and analytics are its own, not the store's (CM-NTF-001, CM-API-012, the analytics capabilities: homonyms).
- **The 5.0.0-only topics:** `app:import` CM-DVT-002 alone (the app's configuration, R98.2); `app:subscription-migrations` CM-DVT-002 and CM-APP-003, as SH-98's commands under it; `app:security` CM-DVT-002 alone (the security check's results are the CLI's, R98.3).

## `shopify-com-header-nav`: the rules I set (R99.1 to R99.6), for the coordinator to check

- **R99.1, the frame and the small screen's controls are `out`.** The mark 'Shopify' linking to `/` is the frame's logo (SH-23's SH-E-704dbc2d; the ruling after SH-37). 'Back', twice, is the source's `<label for="bk-nav-…">`, the toggle that closes its menu, and 'Menu' the `navigation-toggle` label, hidden on large screens (`lg:hidden`): UI strings.
- **R99.2, a heading is a heading of the public site** (the ruling after SA-2 and SA-5):
  - `out` where its links are several capabilities' pages: the menus Why Shopify and Products, and the groups Built into every store, Build your website, Sell anywhere, Marketing & analytics, Run your business, Get paid and Customize & extend Shopify. Each link is placed on its own.
  - On one capability where all its links are its pages: Non-stop innovation and Latest updates, whose links all open the Editions, take CM-ONB-003 `core`.
  - A heading's words that state something of its links are read with each link: 'Built into every store' makes its two links `core`.
- **R99.3, a link to a product or feature takes its capability, with the support its words, or its heading's, give it.**
  - `core` where they state the platform does it: World's best checkout (CM-CHK-001) and Sidekick (CM-AIA-002) under 'Built into every store', as the concern map placed the links of Shopify's own list of products `core` ('Sidekick in Shopify's own list of products', SH-I-1967, and its SH-I-1969, SH-I-1984, SH-I-1988 and SH-I-1990).
  - `shows` where they name only a topic or whom the platform serves, as SH-68's R3 and R4 placed shopify.com's titles and blocks: Get started fast (CM-ONB-004), Switch to Shopify (CM-MIG-005), Trusted by enterprise brands and Enterprise (CM-PLN-001), Pricing (CM-PLN-001), Log in (CM-ACC-001). The concern map's `shows` on 'product Analytics on shopify.com' (SH-I-1979) is the same kind of reading.
  - A topic's capability is read from the page the link opens, its title and description in the held record the ledger joins to it (rule 1's clarifying reads). Its other statements aren't placed (M-12; below).
- **R99.4, a link to an Edition's feature card takes the card's lines.** Latest updates' three links open the Spring 2026 Edition at a card's anchor, so they take the lines the card's own entry took. A second line follows the page, not the link's words (the ruling after SA-19). The card's fillers go in `reading`, since a party known only from a sibling isn't a filler.
  - Agentic Storefronts, at `#agentic-storefronts-insights` (SH-E-24e377b8, SH-65): CM-AIA-005 `core` (the admin's own section, the ruling after SH-2) and CM-ANL-001 `core`. No `extension-point`, since the link names no AI channel.
  - Campaign Autopilot, at `#introducing-campaign-autopilot` (SH-E-de8f66e5, SH-66): CM-MKT-006 and CM-MKT-005 `core`.
  - Shopify AI Toolkit for devs, at `#shopify-ai-toolkit-for-developers` (SH-E-e63a0cd0, SH-67): CM-DVT-001 `core` (the digest's rule 17) and CM-AIA-004 `core`.
- **R99.5, Shopify Editions is CM-ONB-003 `core`,** where the changelog goes (the rulings after SA-2 and SA-5): the platform's news of '150+ updates to Shopify, twice a year.', as the changelog's posts announcing an Edition were placed (SH-E-79328285, SH-E-b15ef0cf). The count and the cadence are the announcement's, no quality.
- **R99.6, the sign-up and sign-in.** 'Start for free', twice (with and without its aria label), is CM-ACC-001 `shows` and CM-PLN-001 `shows` with the quality 'start: free', as SH-73's lines 3 and 4 and SH-92's line 11. Its address's signup type `paid_trial_experience` goes in `reading`. 'Log in' is CM-ACC-001 `shows`; CM-CUS-010's login (SH-38) is the buyer's.
- **No scope on any line:** the structure holds www.shopify.com alone ('other locales/regions not captured (en decided)', the register), so no comparison of sites can be made. The pricing pages' site scopes compare the sites they hold.

## `sidekick-composer`: the rules I set (R99.7 to R99.9), for the coordinator to check

- **R99.7, each control is CM-AIA-002 `core`,** the admin's AI assistant's own control (the Editions digest's R47.1; E105; SH-1's composer lines, SH-E-67c56c0c):
  - what Sidekick takes in: Files, Upload from device, Target, Mention;
  - its skills: Skills /, the dialog Create new Skill and its heading, Shortcut, Instructions and their counters, as SH-36 and SH-63 placed custom skills (SH-E-0fc36b06, SH-E-cf35b212);
  - its apps: the button Apps;
  - its memory: the Settings dialog's Memory, as SH-35 and SH-63 placed it (SH-E-d5bbca5f, SH-E-4f00e971).

  A field and a counter are no places of their own. A counter's maximum is a quality, a reading of '0/50' (the shortcut) and '0/5500' (the instructions); the register reads them the same ('Shortcut up to 50 characters, Instructions up to 5,500').
- **R99.8, a thing a control names that another capability holds takes that line too:**
  - Generate app: CM-APP-009 `core`, the custom app Sidekick builds (E105), as SH-E-721ad9fb and SH-E-c61042b3;
  - Files: CM-CNT-001 `core`, a reading: 'Files', beside 'Upload from device', names the admin's own Files (see below);
  - the Shop app's icon in the Apps button: CM-CHN-002 `own-service`, Shop being the platform's own app ('Shop is a Shopify application that is available to Eligible Merchants', SH-S-0056), so `own-service` on every line about it (the rulings after SH-34 and SH-37), as SH-35 placed it (SH-E-b7bd0730). What Shop does in Sidekick isn't stated, a gap; `shows` is the alternative, as SH-51 placed a card on building into the Shop app (SH-E-3d312545).
- **R99.9, what isn't placed on a capability:**
  - Close, Cancel and Save are `out`, UI strings;
  - the placeholder 'Summarize yesterday's sales and traffic.' is an example, no line (the ruling after SA-41);
  - the store's own values (Memory on, `[x]`) go in `reading`;
  - no line takes a scope: the structure is one store's observation (capture-plus), as SH-1's composer lines took none.

## The new thing

**`new:Store preview`**, SH-47's new thing.
- **Entries:** SH-E-345783b6 (`store:create:preview`: 'Create a preview Shopify store.', 'Creates a new Shopify store, with no need for an existing account.'), beside its CM-DVT-002 line. SH-47's two are SH-E-de899665 and SH-E-2730895b. `store:info`'s 'access and save URLs for preview stores' (SH-E-13544a26, placed on CM-DVT-002 alone) and the output schema's 'Preapproved Admin API scopes for the preview store.' (5.0.0's manifest, line 12121) say a preview store can be kept and comes with scopes.
- **A place of its own:** none. The CLI's commands are the CLI's (SH-98's notes), and no admin route, plan line or API group for it is held in my sources. So `shows`, as the coordinator's check on SH-47 has it.
- **Proposed:** as SH-47: domain ONB, the merchant's start, under CM-ONB-004 or CM-ACC-001, a reading. Not CM-DVT-004: a dev store is given to developers to test on.
- **Names:** English only, the CLI's: preview Shopify store, preview store.
- **Searched:** `caps --terms` for preview store; signup; sign up; create store; store creation; claim; new store; storefront; online store; store transfer; client transfer; trial; onboarding; registration; register; account creation; open a store; start a store; demo store; sandbox; preview. `class_slice.py search` found no statement for preview store or client transfer. The placements hold it only in SH-47.

## The checker's lines

- **CHANGES: CM-DVT-004@shopify gains `core`, by lines 11 and 15.** I read both again. They rest on the commands' own words: 'Creates a new dev store in your organization.' (`store:create:dev`) and 'Deletes a dev store from your organization.' (`store:delete`). SH-98 gave the cell `core` the same way (its lines 54, 56 and 68) and its coordinator kept it, and SH-97's line 50 (`partnerDevelopment: true`) and SH-49's card (SH-E-c0eaf790) support it too. Kept.
- **CHANGES: CM-AIA-004@shopify gains `core` and becomes held, by line 80** (Shopify AI Toolkit for devs). The line rests on R99.4: the link opens the card SH-E-e63a0cd0, and SH-67 placed that card CM-AIA-004 `core` ('from AI tools like Claude Code, Codex, Cursor, Hermes, and more'), as SH-66 placed its twin (SH-E-80bdfc5c). The change is SH-66's and SH-67's, which the model doesn't hold yet. Mine is a third line on it. If the coordinator reads a header link by its own words only, it drops and nothing changes. CM-AIA-004's note keeps Shopify's buyer-side MCP servers apart, and the toolkit's AI tools are the merchant's and the developer's, so the note doesn't bar it.
- **CHANGES: CM-ONB-004@shopify becomes held, by line 58** (Get started fast). The line is `shows`: the link opens /start, 'Start your online store today. Start selling tomorrow.', 'Choose a design, add products, get paid.'. SH-1 already placed the Home's setup heading CM-ONB-004 `core` (SH-E-db7d0638), so the cell is held by SH-1 once merged. The alternative is CM-ACC-001 (starting is signing up), which no word of the link names.
- **NOTE, quotes found nowhere held** (lines 2, 4, 11, 13, 16, 18, 22, 29, 32, 49 and 50): each is copied from a CLI manifest, inside the held tarball, which the checker can't search (SH-98's coordinator's check). Line 13's are from the output schema of `store:create:preview` (5.0.0, line 12121), line 22's from `app init`'s flag (line 2496), and line 29's from `app security review` (line 1509).
- **NOTE, the brand rule** (lines 73 and 79): Shopify Editions is the platform's announcements, not a product; Shopify AI Toolkit is the platform's own developer tool, `core` by the digest's rule 17 ('The platform's own developer tools are `core`'), as SH-66 and SH-67 placed it.
- **NOTE, `own-service` on CM-CHN-002** (line 98, the Shop app's icon): the maker statement is the cell's own, 'Shop is a Shopify application that is available to Eligible Merchants' (SH-S-0056), and Shop takes `own-service` on every line about it (the rulings after SH-34 and SH-37). See R99.8 for the alternative.
- **NOTE, first leads whose cell holds nothing:**
  - CM-OPS-005 (lines 31 and 32): 'Logs you in', 'Logs you out', a verb, as SH-98 read it;
  - CM-MIG-006 (line 51): a store's configuration, while `app:import` imports an app's;
  - CM-B2B-005 (line 73): the words edition and product only.
- **NOTE, containers:**
  - Why Shopify (line 56) and Products (line 64) are `out` by R99.2: headings of the public site over several capabilities' pages.
  - Back (lines 57 and 65) is no container: the source's label for the menu's toggle. `items.jsonl` nests the next items under it only because one list item holds both (below).
  - Latest updates (line 74) is CM-ONB-003's container, its links one capability's pages.
- **NEW:** Store preview, 1 line.

## Entries I couldn't tell, and what would settle each

1. **Files' CM-CNT-001 line** (line 90). 'Files', apart from 'Upload from device', reads as the admin's own Files library; SH-1 called CM-CNT-001 a homonym for the popover's Add files and more. A step that opens Files would settle it (the run closed the popover at step 007). The cell is `core` either way.
2. **Target and Mention:** what Sidekick is pointed at, and what can be mentioned (resources, apps). Steps that open them would settle it. CM-AIA-002 either way.
3. **Sidekick's Apps:** whether it lists the store's installed apps or apps with Sidekick extensions (the cell's App data and App action templates). A step that opens it, showing a third party's app, would make it `extension-point` beside `core`. Only Shop's icon is held.
4. **`store:list`:** CM-DVT-003 (the Dev Dashboard's stores), or CM-ACC-003 (the merchant's organization and its stores). A held statement that the CLI's organizations are the Dev Dashboard's or the admin's would settle it, as for SH-98's `organization:list`. Both cells are `core`.
5. **The enterprise links** (lines 60 and 82): CM-PLN-001 `shows`, by the page's 'Shopify Plus and Enterprise plans built for unrivaled scale', or `out`, as a link naming whom the platform markets to (the ruling after SA-2 and SA-5). Enterprise is a size of business, not a sector, and its page is held, so I took the page's plans.
6. **Headings whose titles name a capability over several capabilities' links:** Build your website (CM-SFR-001's website), Sell anywhere (CM-CHN-001's channels), Get paid (payments), Marketing & analytics. The public-site ruling decides by the links, so they are `out`. The ruling after SA-28 ('a title that names a capability or one part of the platform') would give them a container line. No cell changes either way: each is `core` already.
7. **R99.4's second lines** (CM-ANL-001, CM-MKT-005, CM-AIA-004): an anchor read as the link's page. If a header link takes only its own words' line, the three drop.
8. **`auth:login` and `auth:logout`:** CM-DVT-002 alone (the CLI's session), against a line on the accounts they name (the Shopify account, CM-PTN-002's Partner account). Both cells are `core`.
9. **`send-analytics`, `cache:clear` and the other hidden housekeeping:** CM-DVT-002 `shows` (R98.4), against `out` as the software's own bookkeeping. No cell changes.
10. **Hidden commands** (R98.4), as SH-98's item 1: `shows`, or `core` with hidden in `reading`.

## Structures whose items and sources disagree

- **`shopify-com-header-nav`, its nesting.** `items.jsonl` gives `parent` by list items. The source's 'Back' labels are the first text of the list item that also holds the menu's first group, so 'Get started fast' and 'Build your website' (and its links) are nested under 'Back' (positions 3 and 11 to 16). 'Customize & extend Shopify' and 'Non-stop innovation' get no children, while the source puts each over its list: the first as that list's first item, the second as a `<p>` before it. The source governs: my readings follow it. The extractor (`capture/structure_nav.py`, by `meta.json`) could read a `<label for="bk-nav-…">` as a control, and a heading before a list as the list's parent. That is for its owner.
- **`sidekick-composer`, the popover.** The items are the ARIA snapshot's siblings, as the register says. The step's HTML (`steps/006.html`) nests them as action groups (`data-sidekick-action-group`) after a file input, and marks Mention, Skills / and Apps with a chevron to a submenu, which the items lose. The text node '0/50 Instructions' joins the shortcut's counter and the next field's label; `031.text.txt` gives them as two lines (123 and 124).
- **`shopify-cli-commands`:** as SH-98 found: the items keep only each description's first paragraph, and no flag's description. My lines cite the manifest by its line where they rest on the rest.

## What the sources state that no entry holds (for the second stage)

- **Sidekick's composer** (`raw/runs/20261007T030938Z-journey-sidekick/steps/006.html`):
  - its prompt's textarea `name="sidekickMessage"`, `maxlength="5000"`: a limit of a prompt, for CM-AIA-002;
  - its file input, `accept="image/jpeg,image/jpg,image/png,image/webp" multiple`: the types Sidekick takes, for CM-AIA-002 (the register names it).
- **Sidekick's skills list** (`steps/030.text.txt`, lines 117 and 118): 'No results found', 'New Skill', the list before any skill is saved. Step 034 saves one: the store's own data.
- **The pages the header opens** (`raw/runs/20260930T050139Z-shopify-com-pages/fetch.warc.gz`):
  - `/sell` (`@61769304`): its description, 'Try free for 3 days, then get 1 month for $1.', a trial for CM-PLN-001; its headings 'Get discovered across AI platforms', 'Lower platform fees', 'Updates shipped 2x per year';
  - `/enterprise` (`@12767941`): its headings 'Sell in AI with the Agentic Plan' (a plan named for AI selling, a lead for CM-PLN-001 and CM-AIA-005), 'Add Shop Pay to your checkout' and 'Replatform to Shopify' (CM-MIG-005);
  - `/start` (`@66429916`): its headings 'Choose your design', 'Make your products shine', 'Get ready to get paid', the setup it promises, for CM-ONB-004.
- **The CLI** (5.0.0's manifest, `raw/runs/20261031T003934Z-npm-dev-mcp-1.18.0-cli-5.0.0/fetch.warc.gz@16067323`, member `package/oclif.manifest.json`):
  - `config:autoupgrade:on`, 'Major version upgrades are skipped and must be done manually.' (line 13670);
  - `store:create:preview`'s output schema: the preview store's type 'preview' and its preapproved Admin API scopes; `store:info`'s schema: the preview store's `accessUrl` and `saveUrl`, and 'The country selected when creating the preview store, if specified.'. Leads for Store preview;
  - `store:create:dev`'s flags (plan, feature preview, demo data, country), as SH-98 listed them;
  - `doc:fetch`'s flag `language`: code examples filtered to ten languages, javascript to html (line 13389);
  - `doc:search`'s flags `api-name` and `api-version` (lines 13485 and 13493).

## Problems with this brief or the script

- **The checker can't read the CLI manifest,** inside a tarball in a WARC record, as SH-98 found: 14 quote NOTEs on 11 lines. A `meta.json` key naming the member (`member`, which 5.0.0's and 4.8.3's `meta.json` already hold) could let it open the member.
- **The checker's container NOTE follows `items.jsonl`'s nesting,** so it names 'Back' twice, a control the extractor made a parent.
- **`earlier` matches a command's id as a label** when it is a common word (`search`, `upgrade`, `version`, `help`), printing lines on unrelated things (Collective, plans, POS, Sidekick). They were no leads.
- **No rule covered a public-site link to an anchor of an Editions page,** or a heading whose words state something of its links ('Built into every store'). R99.2 and R99.4 are mine, for the coordinator.
- **No rule of the brief read differently from B-extent.md here.**

## The coordinator's check

Measured: 27.4 million tokens over 114 requests, about 315,000 an entry. The checker prints no problem.
- **Kept:** R98's rules for the CLI's last 38, and R99.1 to R99.12; the `CHANGES` lines (CM-DVT-004 by the commands' own words; CM-AIA-004 by the card the AI Toolkit link opens, SH-E-e63a0cd0, as SH-66 and SH-67 placed it; CM-ONB-004 `shows` for 'Get started fast'); and `new:Store preview`, SH-47's, with this command's entry.
- **The quotes the checker can't find** are the CLI manifest's, inside the held tarball, checked against it by script, as SH-98's were.
- **The open choices** (Files' CM-CNT-001, `store:list`, the Enterprise links, the headings that name a capability, the three lines taken from Editions cards): kept as placed. `shopify-cli-commands`, `shopify-com-header-nav` and `sidekick-composer` are placed whole.
