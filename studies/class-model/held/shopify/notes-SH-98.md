# SH-98: Shopify's `shop-request-details` (last 8) and `shopify-cli-commands` (first 122) (notes)

**The batch:** platform `shopify`, batch `SH-98`, effort `high`, 130 entries in 220 lines, at observed-sh `e38dc17e3`.
- `shop-request-details` (entries 1 to 8): the last fields of the admin's `RequestDetails` answer about the shop, each standing for every store whose answers state the same value. SH-97 placed the first 41.
- `shopify-cli-commands` (entries 9 to 130): the oclif manifests of Shopify CLI 4.8.3 (run `20260930T093750Z-npm-shopify-cli-tarball`) and 5.0.0 (run `20261031T003934Z-npm-dev-mcp-1.18.0-cli-5.0.0`), each command and topic once, in its latest version's words (`selection.tsv`, row 54). My 122 are:
  - 3 commands that only 4.8.3 holds (entries 9 to 11);
  - 8 commands both versions hold in the same words: `plugins`, its six subcommands and `commands` (12 to 19);
  - the 16 topics of 4.8.3, which 5.0.0 keeps in the same words (20 to 35);
  - 95 commands in 5.0.0's words (36 to 130).

  SH-99 holds the other 38, among them the three topics only 5.0.0 has (`app:import`, `app:subscription-migrations`, `app:security`) and the `store:` commands after `store:auth`.

**Count by placement:** 126 entries on capabilities alone, 4 with a `new` line too (App versions), none `out`. By line: 190 `core`, 18 `shows` and 8 `extension-point` on capabilities, and 4 `new` lines, all `core`. Every CLI entry has its CM-DVT-002 line (122).

**What I read:**
- the brief, the evidence map, B-extent's "Cells and evidence" and "Conventions from the dry run", and the rulings;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, `REGISTER.tsv` rows 58 and 131, and `index/ledger-summary.tsv` (no `index/ledger/` file enumerates these two structures);
- `selection.tsv` rows 53 and 54, `show --meta`, both CLI `meta.json` files, SH-97's notes and placements, and `index/instruments.json` lines 81 to 86;
- the Editions digest: its rules 17, 41, 51 and 53, and E71, E85, E151 to E153 and R49.3 to R49.5;
- the CLI's source: `package/oclif.manifest.json` and `package/package.json` of each version, which I took out of the npm tarballs in the WARC records `meta.json` names into my scratch folder. Their sha256 match `meta.json`'s `member_sha256` and `package_json_sha256`;
- the earlier lines that cite the CLI or its things: SH-11, SH-23, SH-41, SH-49, SH-51, SH-53, SH-56, SH-57, SH-59, SH-61, SH-65 and SH-67.

## `shop-request-details`: SH-97's rules, kept

I took S97.6 to S97.16 and SH-97's coordinator's check: a true flag or entitlement, or a value that grants it, is `core`; false or null is `shows`; the stores are the scope and the key is the term (for a plan's name or displayName, the value, as SH-97's lines have it).
- **The four `trialPeriod` entries** (SH-E-fd725044, SH-E-44c6ce1e, SH-E-c2fa155d, SH-E-0c588538) take CM-PLN-001 `core`, each store its scope and the dates in `reading`, as SH-97 placed 2jiwxs-gr's (SH-E-e0033d91). Their scopes differ, so they aren't grouped. Each period is three days long, as SH-97 found for every held trial store.
- **ctcbwa-r1 and fake-demo-sharrwah are one store.** `index/instruments.json` (lines 81 to 86) gives ctcbwa-r1 as the myshopify handle of the admin handle fake-demo-sharrwah. Their shared trial period is that store's. I kept both labels in the scope, as SH-97 did.
- **Advanced, basic and Basic App Development** take CM-PLN-001 `core`. Basic App Development also takes CM-DVT-004 `core`, a reading (S97.11), as SH-97's lines 47, 68 and 77 do.
- **`catalogStatusOverrideChangesetsEnabled` false** (SH-E-f48a815d) takes CM-B2B-003 `shows`, a reading of the key: a catalog's status overrides, in changesets. It is false on ibx5bt-xy, zyd38b-ze, demo-fake-dev-store and fake-demo-sharrwah's first answers, and true on every other store. The concern map left its true value unplaced (SH-I-2588: 'no route's eligibility in the admin router names it').

## `shopify-cli-commands`: the rules I set (R98.1 to R98.11), for the coordinator to check and SH-99 to keep

- **R98.1: each command** is CM-DVT-002 `core`, the platform's own command-line tool (the Editions digest's rules 17 and 41).
  - Its id is the term, with its aliases (`plugins:add`; `plugins:unlink`, `plugins:remove`) and a name its summary gives (App Doctor).
  - It takes no scope, unless R98.11 gives one. Its version or versions go in `reading`.
  - Every command's `pluginName` is `@shopify/cli` in both manifests, the oclif `plugins:` and `commands` commands included. So no other maker is in question.
- **R98.2: a topic** (package.json's `oclif.topics`, in `topics.jsonl`) is a container of the CLI's commands (M-13): CM-DVT-002 `core`, its id the term.
  - Where its description names a platform's thing that one capability holds, the topic takes that capability too, with that thing's support:
    - `doc`: shopify.dev's documentation, CM-DVT-001;
    - `hydrogen`: Hydrogen storefronts, CM-SFR-011;
    - `theme`: Liquid themes, CM-SFR-002;
    - `store:bulk` and `app:bulk`: bulk Admin API operations, CM-API-007;
    - `app:function`: Shopify Functions, CM-APP-005 `extension-point`.
  - Descriptions that name stores, apps, configuration, environment variables, auth or the CLI's own options name no other capability's thing. These topics take CM-DVT-002 alone: `app` (building apps is CM-DVT-002's own thing by its name), `store`, `store:create`, `app:config`, `app:env`, `auth`, `config`, `config:autocorrect` and `plugins`.
  - `store:create`'s two commands create two kinds of store: `store:create:dev`, 'Create a new dev store.', and `store:create:preview`, 'Create a preview Shopify store.'. SH-99 places them.
- **R98.3: the thing a command works on.** A thing the platform keeps or runs for a store or an app, which the command creates, lists, changes, runs or deletes, takes that thing's capability too, `core`. The CLI is the platform's own tool for the platform's own feature, as the Editions' CLI cards were placed: dev stores (SH-49:81), `h2 deploy` and `h2 upgrade` (SH-56:72 and 77), bulk operations and GraphQL queries (SH-67:83 and 84), and a webhook's sample delivery (SH-51:91). The cases in this batch:
  - **themes:**
    - the store's themes and theme library take CM-SFR-001: `list`, `info`, `open`, `preview`, `publish`, `rename`, `duplicate`, `delete`, `share`, `dev`, `push`, `pull`, and `package`, which prepares a theme for upload to the Online Store;
    - a theme's code and Liquid take CM-SFR-002: the topic, `init`, `check`, `console` and `profile`;
    - other tools of the platform's that a command runs or copies take CM-DVT-001, by rule 41's 'other tools': Theme Check, the Language Server, and Shopify's Skeleton theme;
  - **Hydrogen:** CM-SFR-011 for every `hydrogen:` command that works on a storefront. On 23 of them, the flag `path` is 'The path to the directory of the Hydrogen storefront.' (the manifest). `hydrogen:shortcut`, the CLI's `h2` alias, takes CM-DVT-002 alone. What Hydrogen supports takes its own line (E85):
    - markets take CM-MKS-001;
    - the Storefront API's queries take CM-SFR-012;
    - the Customer Account API's OAuth for the storefront takes CM-CUS-010;
    - the storefront's environments on Oxygen take CM-DVT-006, as SH-11 and SH-56 read them;
  - **dev stores:** CM-DVT-004;
  - **metafield and metaobject definitions:** CM-CNT-002;
  - **an app's versions:** `new:App versions`;
  - **the Developer Dashboard,** where `app config link` fetches the app's configuration: CM-PTN-001 (E151). The developer's organizations take CM-PTN-002;
  - **the platform's API:**
    - bulk operations take CM-API-007;
    - Admin API queries and GraphiQL take CM-API-001;
    - a webhook topic's sample delivery takes CM-API-008;
    - an app's authorization on a store takes CM-API-002;
  - **app subscriptions** migrated to Shopify-managed app pricing: CM-APP-003.

  A thing that only the developer's machine or the CLI holds takes CM-DVT-002 alone: a build, environment and configuration files, the CLI's own settings, plugins and aliases, security check results, and a local list of the stores authenticated. So do the things a description lists as what a command prints or returns, a link or an example (the ruling after SA-41; the digest's rules 51 and 53).
- **R98.4: a hidden command** (`hidden: true`) is `shows` on every line, with the reason in `reading`.
  - The CLI leaves such a command out of its help and its list of commands. Its `commands` command lists them only with its flag `hidden` (the manifest).
  - The cases bear this out:
    - 4.8.3's hidden commands were later released (`app:subscription-migrations:*`, not hidden in 5.0.0);
    - or replaced (`app:doctor` by `app:security:*`);
    - or are aliases and earlier names (`hydrogen:g`, `app:import-custom-data-definitions`, `app:import-extensions`);
    - or a stub (`app:logs`), or the CLI's own tools (`kitchen-sink`, `demo:watcher`).
  - The ruling after WC-6 reads a thing that is shipped but hidden from its users as `shows`. This is a reading. The alternative is `core`, with hidden in `reading`. No cell changes either way here, since CM-DVT-002 is `core`.
  - A topic all of whose commands are hidden (`kitchen-sink`) is `shows` too.
- **R98.5: a command that only 4.8.3 holds** is `shows`, retired by 31 October 2026.
  - 5.0.0's manifest is the CLI's complete list of its commands, and leaves these out: `app:doctor`, `app:doctor:instructions` and `app:logs:sources`.
  - The replacement goes in `reading` where 5.0.0 holds the same words under another id (`app:security:check`, `app:security:instructions`), or where it says so ('App logs were removed in Shopify CLI 5.0.'). The replacement's lines are on its own entry (R49.5).
- **R98.6: the `plugins:` commands** take CM-DVT-002 `core` alone. The plugins they install are named with no maker ('user-installed or core plugin'), so no `extension-point` line.
- **R98.7: an app's code that the platform runs.**
  - Shopify Functions take CM-APP-005 `extension-point`: the function commands, the topic `app:function`, and app logs' sources. Developers write them through the platform's tool, and a Function API is `extension-point` by definition (rule 17; E71).
  - SH-61's line on Functions' CLI logs was `core;extension-point`. These commands' words name no run by the platform: `run` and `replay` run locally. So `extension-point` alone.
  - An app extension of a named kind takes its target's capability, `extension-point`: a theme app extension, CM-SFR-004 (`app build`), and a `channel_config` extension, CM-CHN-001 (`app import channel-config`, hidden, so `shows`).
  - 'Extensions' with no kind named take no line: `app build`, `deploy`, `info`, `generate extension` and `import dashboard-extensions`.
- **R98.8: a flag** is a field of its command, with no line of its own.
  - Its words are read with the command's, for a scope (R98.11), a limit (R98.9) or the command's own thing.
  - What flags name in passing takes no line: extension kinds, templates, webhook delivery methods, the Theme Access password, and the customer account push of `hydrogen dev`.
  - Flags that every command of a topic holds state nothing on their own: `no-color`, `verbose`, `path`, `json-schema`, `auth-alias`, `config`, `client-id`, `reset`, `no-input`, `password`, `environment`, and `store` except as R98.11 reads it. Nor do their `SHOPIFY_FLAG_*` environment names.
- **R98.9: a limit a command's words state** is a quality, on the line of the capability it bears on:
  - mutations only on dev stores (`app execute`, `app bulk execute`), on CM-DVT-002;
  - bulk operations listed for the last 7 days (`app bulk status`), on CM-API-007;
  - 'an unlimited number of development environments' linked to one Hydrogen storefront (`hydrogen link`), on CM-SFR-011.
- **R98.10: a command its words state experimental** ('EXPERIMENTAL:', `hydrogen setup vite`) is `shows` on every line, by the brief's flags rule.
- **R98.11: a kind of store a command requires** is the entry's scope, on every line of the entry. It is a listing condition the platform sets for a store (the brief's rule 5). The manifest's flag `store` states it:
  - 'The store domain. Must be an existing dev store.' for `app:bulk:*`;
  - 'Store URL. Must be an existing development or Shopify Plus sandbox store.' for `app dev`, `app import custom-data-definitions` and its hidden earlier name;
  - 'Store URL. Must be an existing development store.' for `app dev clean`.

  'The app must be installed on the store.' (`app execute`, `app graphiql`) is a condition on the store's own data, so it goes in `reading`.

## The new thing

**`new:App versions`**, SH-53's new thing, which SH-23 and SH-57 placed `core`.
- **Entries:** SH-E-76380e0d (`app deploy`: 'This command creates an app version…', the manifest's second paragraph), SH-E-e6c93b43 (`app dev clean`: the app's active version restored), SH-E-c0fccba3 (`app release`) and SH-E-0ef3926d (`app versions list`). Each is `core`, the platform keeping and releasing an app's versions (R98.3).
- **A place of its own:** the Dev Dashboard's item Versions (SH-23's SH-E-c14d6233), a navigation item with its own title. The CLI's commands are the CLI's, not a place.
- **Proposed:** domain F, area APP, under CM-APP-001 or beside CM-DVT-002, as SH-53's notes proposed. This is a reading.
- **Names:** English only, the CLI's: app version, app versions, active version.
- **Searched:** `caps --terms` for app version, app versions, versioning, snapshot and release. CM-API-006 is the platform's API versions, a homonym; CM-APP-010 is settings the platform holds per store. The 'release' hits are other things.
- **The leads the checker names** (CM-APP-001, CM-APP-011, CM-NTF-004, CM-SHP-017, CM-DVT-001, CM-DVT-002) matched only words, such as app, name and dev.

## The checker's lines

- **CHANGES: CM-DVT-004@shopify gains `core`, by lines 7, 54, 56 and 68.** I read each again.
  - Line 7 is a reading (S97.11), as SH-97's lines 47, 68 and 77 are.
  - Lines 54, 56 and 68 rest on the commands' own words:
    - 'Builds and previews your app on a dev store' (`app dev`);
    - the active version restored 'to the selected development store' (`app dev clean`, its second paragraph in the manifest);
    - 'Import metafield and metaobject definitions from your development store.'.
  - SH-97's line 50 (`partnerDevelopment: true`) already gives the cell `core`, and its coordinator kept it. Any of these lines supports it with that one.
- **CHANGES: CM-DVT-006@shopify gains `core` and becomes held, by lines 175 and 203.** Both are readings, aligned with SH-11's two route lines and SH-56's card line (SH-E-6eebf1f1, SH-E-040a5a3a, SH-E-b3ce6420), which the model doesn't hold yet.
  - Line 203 is `hydrogen env list`'s own words: 'Lists all environments available on the linked Hydrogen storefront.'.
  - Line 175 is `hydrogen deploy`'s flags in the 5.0.0 manifest:
    - `preview`, 'Deploys to the Preview environment.' (line 9462);
    - `env`, which picks an environment by its handle;
    - `auth-bypass-token`, a token 'which can be used to perform end-to-end tests against the deployment' (line 9485).

    The item holds only the flags' names, so the line has no term.
  - **What would settle it:** a held statement that a storefront's Preview or other environment stages changes before they reach the live storefront. SH-11's run page names Production and Preview, with 'URLs are generated for each deployment'.
- **NOTE, quotes found nowhere held** (lines 52, 174 and 198). Each is copied exactly from the 5.0.0 manifest, which the checker doesn't search (see below):
  - line 52: `app deploy`'s second paragraph (manifest line 367);
  - line 174: `hydrogen deploy`'s flag `metadata-user`, 'Will be saved and displayed in the Shopify admin' (line 9590);
  - line 198: `hydrogen customer-account-push`'s flags (lines 10660 and 10667).
- **NOTE, first leads whose cell holds nothing.** Each reading names the lead and why it isn't the entry's thing:
  - CM-OPS-005 (lines 63 and 183): app logs are an app's, not the store's logger's, as SH-49 read it; 'Logs in' is a verb;
  - CM-OPS-004 (line 85): the store's system status;
  - CM-DVT-006 (lines 92, 149 and 157): the words update, without, environment and live; the CLI's environments are its configuration's named stores;
  - CM-CNT-010 (line 214): the format of product, category and page addresses. The markets' URL structure (subfolders, domains, subdomains) is CM-MKS-001's.
- **NOTE, the brand rule:** cleared by the terms Liquid REPL and Liquid, the platform's own template language, `core`.
- **NOTE, new things with leads:** read, above.
- **NEW:** App versions, 4 lines.

## Entries I couldn't tell, and what would settle each

1. **Hidden commands** (R98.4): `shows`, or `core` with hidden in `reading`. A held statement of what `hidden` means to the CLI's users would settle it, such as shopify.dev's CLI reference listing or leaving out a hidden command. No cell changes either way.
2. **`catalogStatusOverrideChangesetsEnabled`:** CM-B2B-003, CM-MKS-002 (Rollouts, a scheduled set of changes to product catalogs among others), or a new flag thing (S97.15). A held statement of what catalog status override changesets are would settle it. `shows` either way.
3. **`organization:list`:** CM-PTN-002, the developer's organization, as `app init`'s flag `organization-id` finds the ID in 'your Dev Dashboard URL' (the manifest). The alternative is CM-ACC-003's organization, the merchant's. A held statement that the CLI's organizations are the Dev Dashboard's or the admin's would settle it. Both cells are `core`.
4. **CM-APP-005's support** for the function commands: `extension-point` (R98.7), against SH-61's `core;extension-point`. Settled with the cell; it holds both already.
5. **Theme files** (`push`, `pull`): CM-SFR-001, a theme of the store, or CM-SFR-002, theme code, whose reading names writing theme files. Both cells are `core`.
6. **`hydrogen codegen`'s CM-SFR-012:** the Storefront API's queries are its object, as `app execute`'s Admin API queries are. The digest's rule 51 gives no line to 'the APIs a thing is built with', the other reading. No cell changes.
7. **`app config link`'s CM-PTN-001:** the Developer Dashboard is named as where the app's configuration lives. If that is named in passing, the line drops, and no cell changes.
8. **The topic `store:create`:** CM-DVT-002 alone, against CM-DVT-004 (its first command creates dev stores) or CM-ACC-001 (its second creates a store 'with no need for an existing account', in the manifest). SH-99's two commands settle what each is.
9. **The 4.8.3-only commands** (R98.5): `shows` as retired, against `core` as stated on 30 September. Settled by the coordinator's rule on a version that a later complete list replaces.
10. **The autocorrect default:** the topic and the `on` and `off` commands say 'Off by default.', while `status` says 'On by default.'. The platform's two statements differ. No cell depends on it.

## Structures whose items and sources disagree

- **`shopify-cli-commands`: the items keep only each description's first paragraph, and none of the flags' descriptions.**
  - The source is `package/oclif.manifest.json`, verbatim inside the npm tarball of the WARC record `meta.json` names. 51 of 4.8.3's 133 commands and 110 of 5.0.0's 138 have a longer description in the manifest than in their item; the items of 3 and 2 others only trim the description's leading space.
  - A flag's item keeps its name, type, char, env, default, options and, for some, a summary.
  - The manifest also holds, for 5.0.0, the JSON schemas of each command's `--json` output, which state nothing of a capability.
  - The source governs. A line that rests on a later paragraph or on a flag cites the manifest, by its line where it matters, and quotes it exactly. Its term is empty, or one of the item's own words, since the checker tests terms against the item. These are lines 46, 52, 56, 57, 123 and 175, which have no term, and the scopes of R98.11.
  - The extractor (`capture/structure_cli.py`, by `meta.json`) could keep the whole description and the flags' descriptions. That is for its owner.
- **`shop-request-details`:** nothing beyond SH-97's.

## What the sources state that no entry holds (for the second stage)

From 5.0.0's manifest (`raw/runs/20261031T003934Z-npm-dev-mcp-1.18.0-cli-5.0.0/fetch.warc.gz@16067323`, member `package/oclif.manifest.json`):
- **`hydrogen deploy`:**
  - `auth-bypass-token-duration`: 'Specify the duration (in hours) up to 12 hours for the authentication bypass token. Defaults to `2`' (line 9496), a quality for CM-DVT-006 or CM-SFR-011;
  - `json-output` writes the deployment's details 'in CI environments' (line 9555);
  - `metadata-user`: the deployment's user is shown in the Shopify admin (line 9590), the admin's page of the storefront's deployments.
- **`app deploy`:**
  - `no-release`: a version 'not made available to merchants' (line 472);
  - `allow-updates`: 'Recommended option for CI/CD environments.' (lines 456 and 2719, the second `app release`'s), for E152.
- **`store create dev`** (SH-99's entry), its flags (line 12082 and around): a plan of basic, grow, advanced or plus, a feature preview 'to enable on the new dev store', and demo data. These are leads for CM-DVT-004 and the Feature test drives (the ruling after SH-34).
- **`app webhook trigger`:** the delivery methods http, google-pub-sub and event-bridge (lines 5415 and 5545), a lead for CM-API-008's deliveries to Google Pub/Sub and Amazon EventBridge.
- **The theme commands' flag `password`:** 'Password generated from the Theme Access app or an Admin API token.', for CM-SFR-002's Theme Access.
- **`theme init`'s second paragraph** (line 5752): Shopify's Skeleton theme, placed on CM-DVT-001, and a caution for themes built for the Shopify Theme Store, a lead for CM-SFR-003.
- **`app security check`, `record` and `review`:** they report the number of findings to Shopify as usage telemetry (lines 975, 1408 and 1509).
- **The flag `store`:** 'Shopify Plus sandbox store' (`app dev`, `app import custom-data-definitions`) is a kind of store no capability holds (5.0.0; and 4.8.3’s manifest, lines 512, 987 and 1182, of `app dev`, `app logs` and `app import-custom-data-definitions`). Searched sandbox, sandbox store and Plus sandbox. It is a lead for CM-DVT-004, or for CM-ACC-003's expansion stores on Plus. Here it is placed only as a scope.

From 4.8.3's manifest (`raw/runs/20260930T093750Z-npm-shopify-cli-tarball/fetch.warc.gz@1156`):
- **`app doctor`'s CVE detection** sends package names and versions to the public npm registry (line 812).
- **`app logs`** streamed an app's logs from 'an existing development or Shopify Plus sandbox store' (line 987). 5.0.0 removed it.

## Problems with this brief or the script

- **The checker can't read the CLI's source,** which is inside a tarball in a WARC record. So a quote from the manifest is a `NOTE`, and the manifest's words can't be terms. A `meta.json` key naming the member (`member`) could let the checker open it.
- **No rule covered a command's `hidden` key** or a version a later complete list replaces. R98.4 and R98.5 are mine, for the coordinator.
- **The checker's `NOTE` on a new thing whose entry has leads** names the line before the `new` line (line 51 for line 52, and the like).
- **No rule of the brief read differently from B-extent.md here.**
