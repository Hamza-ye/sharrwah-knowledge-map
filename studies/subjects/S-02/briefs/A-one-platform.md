# Brief: S-02, what one platform states (step 1, phase A)

This is `PLAN.md` Stage 4, subject S-02. You are one agent with one task, for one platform. The message that started you names the platform; this brief calls it "your platform". Read only this brief and the inputs it names. You don't see the other platforms' work.

## The subject

> What fills "a market": which settings bind per market, and who sets each?

A platform may use "market", "country", "region", "channel" or "storefront" for different things. Place each statement by what it says, never by the word it uses.

**What bears on the subject:** any statement by your platform, or by an agreement its terms incorporate (one its terms name as binding on the merchant), that says one of these. The bullets are in `studies/subjects/S-02/bullets.tsv`:
- **(a)** what fills the store's own country: the country, location, address or jurisdiction the platform holds for a store or its merchant, and where it holds it;
- **(b)** who sets, checks or changes the store's country, and on what conditions;
- **(c)** what the platform binds to the store's country: documents, terms, the contracting party, payments, fees, taxes, or anything else it names;
- **(d)** the countries the platform serves merchants in, or says it doesn't, and how it holds them;
- **(e)** what defines a market a store sells into (a country, region, city, group of customers, location, channel or storefront), how many a store can hold, and who creates, changes or removes one;
- **(f)** a setting that takes its value per market, of either kind, or per buyer's country, such as an address format; and who sets that value, the platform or the seller;
- **(g)** that a setting holds for the whole store whatever the market, or that the platform has no market of the kind in (e);
- **(h)** where, or for whom, what a statement under (a) to (f) describes is offered: the plans, features, countries or business types the platform states.

**Your task:** collect everything your platform states that bears on the subject, in its own words, and record what it doesn't state. Don't compare it with any other platform, and don't judge it.

## Inputs

**1. What is already recorded, in your output folder** `studies/subjects/S-02/<platform>/`:
- `recorded.tsv`: statements the concern map holds for this subject's concerns, and statements from an earlier subject (S-01) on where, or for whom, each way of holding sellers' money is offered. `held_in` says where each is held. `from` is the value a statement you copy from it takes.
- `recorded-citations.tsv`: the citations they cite.

Both were checked word for word against their sources. **Start here:** read both files in full, and copy each statement that bears on a bullet (rule 5).

**2. Your platform's Q1 index,** in `studies/concern-map/platforms/<platform>/`. Open only these four files there: `concerns.tsv`, `statements.tsv`, `gaps.tsv` and `citations.tsv`. Use them to find statements of other concerns that bear on a bullet, and the pages a gap names.

**3. Your platform's own material, as held or live.** For every platform this includes any agreement its terms incorporate (`PLAN.md`, section 6, allows them).

| Platform | How you read it | Held | Live (declarations only) |
| --- | --- | --- | --- |
| shopify | **In full** (below) | observed-sh at `febbf6c98a1f2a464bb92bd97856b8ba070f3185`: `structures/shopify/` and committed text under `raw/runs/` | help.shopify.com, shopify.dev, shopify.com/legal |
| salla | **In full** (below) | observed-sa at `4ca2e896a729215f422a137a364e7e9488610ba3`: `structures/salla/`, including `help-articles/{ar,en}/texts.jsonl`, `com-policies/` and `partners-legal/` | docs.salla.dev |
| zid | **From what is recorded** (below) | none | docs.zid.sa, zid.sa and Zid's help pages |
| woocommerce | **From what is recorded** (below), and the release's address formats | WooCommerce 11.2.1 release files in `/home/user/woocommerce-release/11.2.1/woocommerce`, cited as `woocommerce-11.2.1:<path>` relative to that folder | woocommerce.com docs and legal pages |
| bigcommerce | **From what is recorded** (below) | none | docs.bigcommerce.com, bigcommerce.com and its legal pages, support.bigcommerce.com where it can be read |

For observed-sh and observed-sa, their own guides say what each folder and run holds: their `README.md` and `docs/READING.md`. Read them first.

**In full** means: read each starting point below in full, then whatever it leads to that bears on a bullet. Before you record a gap, search the held material for it (rule 9). The starting points are where the coordinator found the subject. They are not the limit of your reading.
- **shopify:**
  - the held Help Center, in `structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/`: every page under `markets/`; under `international/`, `managed-markets.md` and `managed-markets/overview.md`, `payments.md`, `managing-international-domains.md`, `geolocation.md`, `languages.md`, `pricing.md` and `shipping.md`; and `checkout-settings/address-collection-preferences.md` and `checkout-settings/checkout-blocks/customizations/address-format-validation.md`;
  - the store's own address and country settings: find their pages with `corpus_search.py` ("store details", "store address", "billing address", "home country");
  - the Admin API schema, `structures/shopify/admin-graphql-schema/2026-10/`: the types `Market` and every type named `Market…` or `Markets…`, `BusinessEntity`, `BusinessEntityAddress`, `Shop` and `ShopAddress`. Read each type in full with `method/schema_type.py` (below); `items.jsonl` cuts each description at its first line break;
  - the page that lists unsupported countries (the source of `recorded.tsv`'s SH-C-006 statements).
- **salla:**
  - in `structures/salla/help-articles/ar/texts.jsonl` and its English twin `en/texts.jsonl`, the articles on الأسواق المتعددة (multiple markets), and on creating or verifying a store in each country (إنشاء متجر جديد خارج السعودية, توثيق متجرك). Find them, and every article that mentions a market, with `corpus_search.py salla "الأسواق المتعددة" "دولة المتجر"`;
  - `structures/salla/dashboard-features/`: the features named `multi-countries…`, `multi-market…` and `…market…`, with their plans and countries;
  - `structures/salla/dashboard-countries/`, `storefront-shipping-countries/`, `kyc-schema/` and `settings-center/`, for the store's country and the countries Salla holds;
  - `structures/salla/docs-operations/`: the store scopes (`GET /scopes`), countries, cities and addresses;
  - `structures/salla/dashboard-translations/`, for the dashboard's own words on markets and countries.

**From what is recorded** means: your statements come from `recorded.tsv` and your Q1 index. Read further only:
- to read a page instead of routing a gap to the founder, when `held_index.py` finds it held and readable (rule 9);
- **woocommerce only:** read the address formats and country locales in `includes/class-wc-countries.php` of the release (`get_address_formats()` and `get_country_locale()`), since the subject's question names address formats.

Record every other bullet your platform doesn't state as a gap, with the pages that would likely state it in `route`. Gaps a root decision needs are closed in a later step.

**Tools:**
- To find whether a page is held: `python3 -I method/held_index.py <url>`.
- To read a record held in a fetch archive: `python3 -I method/warc_text.py <repository root> <location> --text`.
- To search a platform's held text: `python3 -I method/corpus_search.py <platform> <terms>`. Snippets are folded for matching: never quote one; quote the document.
- To read a GraphQL type in full (shopify): `python3 -I method/schema_type.py /home/user/observed-sh/structures/shopify/admin-graphql-schema/2026-10 <Type> [<Type> ...]`, or `--search <words>` to find types. It prints the `source` and the `locator` (the record's offset) that a quote from it takes. Put the type's name in the locator after the offset, such as `1029798 (type Market)`.

**Reading a live page.** Read it as the Q1 runs did: a `.md` endpoint, the raw file, or the rendered page through `method/capture/page_text.mjs`. A summary returned by a fetching tool is not the page. Don't get around logins, paywalls or bot challenges.

**Don't open:**
- anything else under `studies/`, except your own output folder and the four index files above;
- `PLAN.md`, `STATE.md`, `HISTORY.md`, `founder-decisions.tsv`, `questions/` and `reports/`;
- `evidence/yemen/`.

## Rules

1. **A statement** is your platform's own words or data, or those of an agreement its terms incorporate, copied verbatim. It carries the platform's identifiers where it has them, such as a key, scope, route, field, plan name or section heading. Never use a category name of ours.
2. **Placement.** Give each statement the one question it answers:
   - `where`: where the platform puts it in its own organization;
   - `decides`: what turns it on or off, limits it, or sets its value;
   - `responsible`: who answers for it, as terms, policies or legal-entity records state;
   - `boundary`: the API resource, webhook topic, access scope, extension target or event where it meets the rest;
   - `reason`: a reason the platform states.

   Typical sources for each:
   - `where`: admin sections and routes, API groups, app or extension targets, separate hosts or products, code paths;
   - `decides`: eligibility conditions, entitlements and features, plan lines, settings, staff permissions;
   - `responsible`: terms, policies, legal-entity records;
   - `boundary`: APIs, webhooks, scopes, extension targets, events.

   For a help page, the question the statement answers decides its placement.
3. **Scope.** A statement holds where the platform says it holds: a store, plan, country, market or role. Record that scope as stated, and leave it empty when the statement is general.
4. **Release marker.** When the source attaches a word that marks a stage of release to what the statement describes, such as beta or sunset, copy that word into `marker`, verbatim.
5. **Copying what is recorded.**
   - Copy a statement from `recorded.tsv`, or from your Q1 index, only if it bears on a bullet. Leave out the rest.
   - Give it a new `cite_id` for each citation it keeps, with the citation's `source`, `locator` and `quote` unchanged.
   - Set `from` to the recorded row's `from`. For a statement of your Q1 index that isn't in `recorded.tsv`, set it to `index:<concern_id>:<index cite_id>`.
   - Read its source again only if the excerpt is too short to show what bears on the subject. Then record what you read as a new statement, with `from` set to `new`.
6. **Terms.** Record each word your platform uses for a store's country, for a market and its kinds, and for the settings it sets per market:
   - quote the platform's own definition where it gives one;
   - where the platform gives its own translation of the term, such as an Arabic and an English page for the same thing, quote that too.
7. **Bullets.** Give each statement every bullet it fits, such as `c;f`.
   - **Conditions.** A statement under (h) names, in `conditions`, the `stmt_id`s of the (a) to (f) statements whose arrangement it conditions. If none exists, write `none stated`, and name the arrangement in `identifier`.
   - **Lists.** Record a list in full, as one statement, such as the countries a platform serves or the settings a market takes. Cite each item, or each run of items. Also cite the words that present the list as complete, if there are any. A statement may run past 300 characters; only quotes are capped.
8. **Absences.** Absence counts only from a complete list your platform publishes, whose own words present it as the full set. Record such an absence in `absences.tsv` under the bullet it bears on, citing:
   - the list;
   - the words that make it complete.

   Anything else your platform doesn't state is a gap.
9. **Gaps.** Make one gap for each of (a) to (f) and (h) that your platform doesn't state. Bullet (g) needs no gap.
   - `read`: list what you read looking for it. Write held paths with their commit, and live URLs with the date you read them.
   - `gap_kind`:
     - `page not read`: a named page or file that would likely state it hasn't been read yet;
     - `observation needed`: a journey, a store on a plan, a page saved from a browser, or a question to the platform would show it;
     - `searched, not found`: the likely pages and structures were read, as `read` lists, and none states it. An index or a sitemap doesn't count as reading the pages it lists. A held collection of the platform's pages that you didn't search rules this kind out. Before recording one, run `python3 -I method/corpus_search.py <platform> <terms>`:
       - with your platform's own words for what is missing, in every language it uses;
       - with each country, plan or arrangement your statements name.

       Read each listed document that could state it, and give the commands and the documents in `read`.
     - `stated only in general terms`: the terms speak only of the platform's services in general.
   - `who_can`: `agent`, `founder` or `either`.
   - Before you give a gap `founder` or `either`, run `method/held_index.py` on each address in its route. If the page is held and readable, read it instead.
10. **Credentials.** Evidence that contains credentials, cookies or tokens is read and cited like any other evidence. Never skip, withhold or mask a file because of them. They come from synthetic environments the founder rotates.
11. **No inference, anywhere.** Notes record what was read, what couldn't be read, and problems. They never record inference.
12. **Write as you go.** Write each statement, citation, term, absence and gap to your files as soon as it is checked, never holding work in memory or in scratch files. If you are stopped, your files must hold everything done so far, and the next run continues from them.
13. **Stop and report** past 250 statements.

## Quotes and citations

- **Quotes are verbatim,** at most 300 characters, with no ellipses, and within one paragraph of the source. Arabic stays as written. The checker collapses whitespace, removes HTML tags and decodes entities, on both sides.
- **A local source** is `<repository>@<commit>:<path>`.
  - Copied citations keep their own commit. New ones use the full commits in the table, or `woocommerce-11.2.1:<path>`.
  - A record in a fetch archive is cited by its archive path, with the offset as the locator.
- **A live source** is the exact URL you fetched: the `.md` endpoint if that is what you read. The coordinator captures every cited URL after your run, and the checker looks for each quote in that capture.
- **`locator`** is the heading, anchor, line or offset.
- **`source_date`** is the date the source shows: published, updated or effective. For an undated live page, it is the date you read it. `date_basis` says which.
- **`accessed`** is the date you read it.

## Output, in `studies/subjects/S-02/<platform>/`

All files are tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field. `XX` is your platform's code: SH, SA, WC, ZD or BC. Leave `recorded.tsv` and `recorded-citations.tsv` as they are.

| File | Columns |
| --- | --- |
| `statements.tsv` | `stmt_id` (S02-XX-001…) · `bullet` (every bullet it fits, `;`-separated, from `a` to `h`) · `placement` · `identifier` · `statement` · `scope` · `marker` · `conditions` (for (h): the stmt_ids it conditions, or `none stated`) · `cite_ids` · `from` (the recorded row's `from`, `index:<concern_id>:<index cite_id>`, or `new`) · `note` |
| `terms.tsv` | `term` · `translation` (verbatim, or empty) · `definition` (verbatim, or empty) · `cite_ids` |
| `absences.tsv` | `absence_id` (S02-XX-N01…) · `bullet` · `what_is_absent` · `list_cite_ids` · `complete_cite_ids` · `note` |
| `gaps.tsv` | `gap_id` (S02-XX-G01…) · `bullet` (one of `a` to `f`, or `h`) · `what_is_missing` · `read` · `gap_kind` · `who_can` · `route` |
| `citations.tsv` | `cite_id` (S02-XX-C001…) · `source` · `locator` · `quote` · `source_date` · `date_basis` · `accessed` · `access_path` (`md`, `raw`, `rendered` or `local`) |
| `notes.md` | What you read; what you couldn't read; problems with the method. |

**Before you finish,** run `python3 -I method/check_subject.py studies/subjects/S-02 <a folder in your scratchpad>`, and fix every line of level `error` whose file starts with your platform's folder. `pending capture` lines are live pages the coordinator captures later: leave them. Ignore other platforms' lines.
