# SH-11: Shopify's admin router, 98 entries of CommerceProtection, Companies, Content, Credit and CustomStorefronts (notes)

**What this batch is.** The fourth held-pass batch on `admin-router`, after SH-8 to SH-10. Its 98 entries are the manifest's items at lines 379 to 498 of `structures/shopify/admin-router/items.jsonl` (observed-sh at `e38dc17e3`), less the routes the concern map already cites (`commerce-protection`, SH-S-5112; `companies:root`; `company:create`; `companyLocation:details`; `companyLocation:create`; `companyLocation:storeCreditTransactionHistory`; `legacy:settings-files`; `content:parent`, SH-S-5120; `metaobject_entry:new`, SH-S-5121; `file:list`, SH-S-5122; `menus:list`, SH-S-5123; `comments`, SH-S-5124; `credit:inactive`, SH-S-5125, with its make-payment and statements routes; `credit:list`, SH-S-5128; `credit:repayment-settings:update`; `credit:account-setup`; `credit:account:index`; `credit:account-settings`; `credit:card-management`; `headless:parent_route`, SH-S-5134; `hydrogen:parent_route`, SH-S-5135). They come from five sections: CommerceProtection (3), Companies (8), Content (41), Credit (18) and CustomStorefronts (28: the headless and Hydrogen storefronts).

- **Entries:** 98, all placed on capabilities. No `new`, no `out`.
- **Lines:** 103, since five entries take two lines: Credit's profile assessment and its interview and remediation (CM-PAY-025 and CM-TRU-002), and the two Hydrogen environment routes (CM-SFR-011 and CM-DVT-006). By support: 87 `core`, 10 `core;extension-point` (six documented intents, four app-controlled metafield lists) and 6 `shows` (the redirects).
- **The checker's last run:** no problem; three cells change (section 3); no `NEW` line.
- **`held_entries.py earlier`** printed no earlier line for any key of the batch but two word matches ('articles', 'blogs': changelog and Editions lines of SH-35, SH-37 and SH-53 on the blog and on automation), which aren't on these routes' things.
- **Ancestors' gates** aren't looked up, as the coordinator asked. A route's own store gates are its `scope`: `storefront.enabled` on the menus, URL redirects, `articles` and `blogs`; `hasInitiatedOnboardingToCredit` on four Credit routes. Gates on the user are named in `reading`. The coordinator's script names the ancestors' (`commerce-protection`'s productProtection, `companies:root`'s b2b gates, `content:parent`'s metaobjects.enabled, `comments`', `articles`' and `blogs`' storefront.enabled).

**What I read:**
- the brief, SH-8's, SH-9's and SH-10's notes with the coordinator's checks, and `review-H-rulings.md`;
- B-extent.md's "Cells and evidence" and "Conventions from the dry run"; the evidence map; `held/selection.tsv`'s router rows;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, `REGISTER.tsv`'s router, betas and titles rows, `index/ledger-summary.tsv`, `index/ledger/admin-route.tsv` and `derived/admin-routes-resolved.tsv`;
- the structure's `meta.json` and `items.jsonl`, lines 377 to 498, with each item's modules and intent (which `show` leaves out);
- `derived/intents.tsv`, and the Intents API page it joins, `raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz@14590255`;
- the run steps the ledger joins to the routes: `raw/runs/20261007T235903Z-journey-bot-protection/steps/002.text.txt`; `derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/` steps 190, 193 and 196; `raw/runs/20261007T043208Z-journey-hydrogen/steps/` 014 to 022 and its `actions.jsonl`;
- the concern map's SH-S-5112, SH-S-5120 to SH-S-5123 and SH-S-1556 (`class_slice.py key`);
- the cells of CM-TRU-004, CM-B2B-002, CM-ACC-004, CM-CNT-001 to CM-CNT-005, CM-CNT-009, CM-INV-005, CM-SUP-001, CM-CAT-006, CM-PAY-024, CM-PAY-025 (every row), CM-PAY-027, CM-TRU-002, CM-SFR-011, CM-SFR-012, CM-SFR-014, CM-CHN-007, CM-CUS-010, CM-B2B-007, CM-DVT-006, CM-APP-010, CM-OPS-003, CM-OPS-004 and CM-OPS-005.

## 1. Lines by capability

| Capability | Lines | Entries |
| --- | --- | --- |
| CM-CNT-002, custom data | 14 `core`, 5 `core;extension-point`, 5 `shows` | the metaobject routes (Metaobjects, Entries, the read-only entries; Edit Metaobject Entry, `core;extension-point` for its documented intent); every metafield list of companies, company locations, blog posts and blogs, the four app-controlled ones `core;extension-point` (SH-10, A8); the Content index's and the four old `entries` addresses' redirects |
| CM-PAY-025, Shopify Credit | 17 `core` | the Credit section: its main page, overview, transaction modal, Link Shopify Credit to vendors, onboarding, terms, the onboarded account's container, statements, Make Credit payment, sales breakdown, rewards, and the profile assessment with its interview and remediation |
| CM-SFR-011, headless storefronts | 18 `core` | the headless storefronts list, create and overview; the Hydrogen storefronts' list, create, setup, deployments, environments, environment variables, settings, Oxygen deployments and source code explorer |
| CM-CNT-004, store blog | 13 `core`, 2 `core;extension-point` | comments, blog posts with their bulk delete and tag modals, a post's page and delete modal, blogs; Add blog post and a post's page with their documented intents |
| CM-OPS-005, store logs | 6 `core` | the Hydrogen storefront's Integrations, its container and its four observability drains, Datadog, New Relic, Splunk (each its filler) and HTTP |
| CM-TRU-002, identity verification | 3 `core` | Credit's profile assessment, interview and remediation, beside CM-PAY-025, as SH-8 placed Balance's and SH-10 Capital's |
| CM-TRU-004, bot protection | 3 `core` | Bot protection and its two schedule routes |
| CM-CNT-009, URL redirects | 3 `core` | URL redirects, a new redirect and a redirect's page |
| CM-CNT-001, files | 2 `core`, 1 `core;extension-point` | a file's modal and its editor; Pick a file, with its documented intent |
| CM-CNT-005, menus | 2 `core;extension-point` | creating a menu and a menu's page, with their documented intents |
| CM-B2B-002, companies | 2 `core` | Companies and Update B2B Company |
| CM-DVT-006, staging environments | 2 `core` | Edit Hydrogen Environment and Environments and variables, beside CM-SFR-011 (a reading, section 3) |
| CM-CUS-010, CM-SFR-012 | 2 `core` each | the headless and Hydrogen storefronts' Customer Account API and Storefront API pages |
| CM-PAY-024, cards | 1 `shows` | Shopify Credit virtual card, a redirect to `/finance/cards` |

## 2. Rules I followed for kinds of route the rules don't cover

These are for the coordinator to align with SH-12 to SH-18. Each is a reading.

- **B1. A redirect whose target no run shows.** `entry:new_redirect`, `entry:update_redirect` and `entry:list_redirect` (`actionType` `*_redirect`, a loader only) sit at `content/entries/…`. Their two siblings that sweeps opened landed on the metaobject pages (`content:index_redirect` on `content/metaobjects`, `entry:list_all_redirect` on `content/metaobjects/entries`, `index/ledger/admin-route.tsv`). I read the other three as going to the same paths under `content/metaobjects/entries/`, a reading of the paths, and placed each `shows` on CM-CNT-002, the target's capability (the ruling after SH-8).
- **B2. Named providers under the platform's own 'Integrations', each with an admin route.** A Hydrogen storefront's Integrations page lists observability drains, and the router gives Datadog, New Relic, Splunk and HTTP a route each (`hydrogen:integrationDatadog`, modules `LogDrain…`). I read them by M-4: a list of providers the platform's own words call its integrations is `core`, each provider its filler. The section's route and its pathless container take the same capability with no filler, since their own words name none. The alternative is M-3 and M-7, a list of third parties' things to connect, `extension-point`: the page says the third-party services 'store, manage, and analyze' the logs (section 3).
- **B3. A route that the ledger's run step shows to be another capability's thing.** The Hydrogen environments routes' own words name an environment; the journey's page says what one is (section 3). I gave each a second line, as SH-10's A3 and A9 read pages the routes opened.
- **B4. A redirect whose title names another capability's thing.** `credit:card-management-virtual`, 'Shopify Credit virtual card', redirects to `/finance/cards`, the section Cards (CM-PAY-024). I placed it `shows` on the target's capability alone, as SH-9's `batches:details` keeps only its target's line. Its title names Shopify Credit's card (CM-PAY-025). If the coordinator reads the Cards section as holding Credit's cards too (its unlock route takes MANAGE_ALL_SHOPIFY_CREDIT_CARDS, SH-S-5099), the line could be CM-PAY-025's, or take both. No cell changes either way.
- **B5. A loader-only route with an optional parameter named for a redirect.** The two Credit statement details (`statements/:statementId/:redirectOverride?`) have a loader only, and no run opened them (needs an instance). I kept them `core` (SH-8, 2.4), their readings saying the parameter may send the request on. A visit would settle whether they show a statement or redirect to a file.
- **B6. Read-only metaobject entries** (`content/metaobjects/read-only/entries`) are `core` alone on CM-CNT-002. Unlike the app-controlled metafields (SH-10, A8), neither their path nor their page names apps: the page reads 'All read only definitions' and 'These entries can’t be deleted' (`derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/190.html.txt`, lines 28 and 36).
- **B7. A metafield list under another section** (companies, company locations, blog posts, blogs) is CM-CNT-002's alone, by SH-10's A7; the app-controlled list is `core;extension-point` by A8.
- **B8. A part of a headless storefront whose words name an API** (Storefront API, Customer Account API) takes that API's capability alone (SH-8, 2.7): CM-SFR-012 and CM-CUS-010, whose Shopify cell holds 'its Customer Account API'.

## 3. The `CHANGES` lines

- **CM-CNT-001@shopify gains `extension-point`** (line 25, SH-E-1dfddead, `content:file:pick`, 'Pick a file'). Its intent `pick shopify/File`, release `public`, modality `MODAL`, is joined by `derived/intents.tsv` to the Intents API's pages (in `app-home` and `app-home-ui-extension`, not `admin-extensions`). The page's Files section reads 'Use the `pick` action to let merchants choose existing files. The workflow resolves with the selected file IDs in `response.data.ids`.' (`raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz@14590255`). Kept, by the ruling after SH-8, as SH-10's catalog and collection intents: an app opens the admin's own file picker and receives the files the merchant chose.
- **CM-DVT-006@shopify becomes held, with `core`** (lines 86 and 96: SH-E-6eebf1f1, 'Edit Hydrogen Environment'; SH-E-040a5a3a, 'Environments and variables'). A reading. The journey's page at `hydrogen/:id/settings/environments` reads 'Create environments to assign dedicated URLs to specific branches.' and lists Production, at the storefront's domain from the branch `main`, and Preview, 'URLs are generated for each deployment', for 'all other branches' (`raw/runs/20261007T043208Z-journey-hydrogen/steps/019.text.txt`, lines 40 to 51). The Deployments page has the tabs Production and Preview (`…/014.text.txt`). CM-DVT-006 is 'environments where a store's updates are tested and previewed, then deployed, without disrupting the live storefront'. I read Preview as such an environment for a Hydrogen storefront's code. Kept, with two cautions for the coordinator:
  - the environments are a custom storefront's, on Oxygen; the store's own data and settings aren't staged. CM-DVT-006's only other evidence is BigCommerce's product line name (BC-I-0540), so the model doesn't state what BigCommerce stages either;
  - the cell's reading had found 'Deploying a Hydrogen app to Oxygen… names no staging' (SH-S-0710). These routes and their page are the first statements that name a preview environment.

  If the coordinator reads them as Hydrogen's hosting alone, the two CM-DVT-006 lines go, and CM-SFR-011's stay.
- **CM-OPS-005@shopify becomes held, with `core`** (lines 88 to 92 and 98: the container `hydrogen:integration:parent`, the drains for Datadog, New Relic, Splunk and HTTP, and the section Integrations). A reading. The section's page reads 'Connect an observability drain to store, manage, and analyze storefront traffic and server-side logs with third-party observability services.' (`…/021.text.txt`, line 41), and the drains' modules are named `LogDrainDatadog`, `LogDrainNewRelic`, `LogDrainSplunk` and `LogDrainHttpIntegration` (the items). A Hydrogen storefront's server-side logs are entries its logger records, and CM-OPS-005's note already takes WooCommerce's Remote Logging, which sends error logs out, as strained. Kept, with two cautions:
  - **the support:** `core` with each provider its filler, by M-4 (B2). `extension-point` would follow B-extent's 'third parties doing it through something the platform provides', since the third-party services store and analyze the logs;
  - **the thing:** the drains also carry 'storefront traffic', which isn't a log the store's logger records. If the coordinator judges the drains a thing of their own, they are `new:Observability drains`, with a place of its own (the route Integrations, `hydrogen/:id/settings/integrations`, and a route per provider), domain G, area OPS, beside CM-OPS-005 or under CM-SFR-011. Terms searched: 'log drain; logs; log; observability; monitoring; Datadog; New Relic; Splunk; drain; traffic; server-side; error; source code'. They found only CM-OPS-005 for the storefront's logs, and other things' logs (audit, inventory, export, SMS, shipment).

## 4. Entries I couldn't tell, and what would settle each

- **SH-E-dccc64ed, `credit:link-merchant-vendors`** ('Link Shopify Credit to vendors'), is on CM-PAY-025 alone: linking the Credit card to the merchant's vendors. CM-PAY-027, Bill Pay ('the merchant schedules and pays its business bills', provided by Melio), is the other candidate if the vendors are bills' payees. Its sweep visit answered 'There's no page at this address' (`…/196.html.txt`, line 23). Settled by the modal's text on a store with Shopify Credit.
- **SH-E-c21ac79e, `credit:card-management-virtual`:** B4.
- **SH-E-f8ff9ff4 and SH-E-e626c526, the Bot protection schedules,** are on CM-TRU-004, a reading of the path and modules (`CommerceProtectionScheduleCreate`, `…Edit`). What a schedule does (bot protection turned on for a sale's hours, perhaps) isn't stated. The capture-plus journey answered 'There's no page at this address' (`raw/runs/20261007T235903Z-journey-bot-protection/steps/002.text.txt`). Settled by a store with the feature productProtection.
- **SH-E-9047369c, `file_editor_id`** (`content/file-editor/:id`), loads FileDetails like the Files modal. Whether it is an image editor isn't stated; no run opened it.
- **SH-E-8b180677, SH-E-9f52e74b and SH-E-da069090,** the old `entries` addresses: B1.
- **SH-E-34d8f591, `headless:list`** ('Storefronts'), is on CM-SFR-011 alone. CM-CHN-007, several storefronts in one store, holds Shopify's plan row Build headless storefronts (1, or 25 on Plus) read as a number of storefronts. This list may be where those storefronts are listed, but its words name no limit.
- **SH-E-44198652, `hydrogen:errorConsole`,** a deployment's source opened at an error, is on CM-SFR-011. If the error console shows the storefront's runtime errors, it would also be CM-OPS-005's (section 3). No run opened it.
- **SH-E-9caf07f1, `credit:benefits`** ('Shopify Credit rewards'), is on CM-PAY-025: the card's cashback, which the cell's plan row holds ('up to 3% cashback', SH-S-7064). It isn't CM-LOY-003's or CM-LOY-004's rewards to buyers.

## 5. The checker's `NOTE` lines, answered

- **Brand (lines 55, 58, 59, 62 and 68):** 'Shopify Credit', 'Link Shopify Credit to vendors', 'Shopify Credit monthly statements' and 'Shopify Credit rewards' are the titles of the admin's own routes. They are `core` because they are routes, not on any maker. CM-PAY-025's `own-service` rests on the Program Terms' Shopify Capital Inc. (SH-S-7276, SH-S-7279), not on these.
- **Containers.** Each is placed on the capability its title or words name, its children named in its reading (SH-8, 2.6). None names only a grouping.
  - Routes with children: lines 19, 33, 34, 39, 44, 46, 56, 61, 69, 88, 93 and 102.
  - Containers by their path alone, whose path begins their siblings' paths: lines 2 (Bot protection), 6 (a company), 7, 10, 41 and 49 (the metafield lists), 22 (Metaobjects), 28 (URL redirects), 77 (a headless storefront), 82 (a Hydrogen storefront), 83 and 84 (a deployment, Deployments). Lines 16 and 17 are redirects at a shared prefix and stay `shows` (SH-8, 2.6).
  - False matches, as SH-9 and SH-10 found: the checker compares relative paths. `:id` (lines 6, 23, 77 and 82) matches 25 paths under other parents, and line 23, `file_id`, is a modal with no child. `:id/metafields` (lines 7, 41, 49) matches the other sections' metafield lists.

## 6. Item text that reads as instructions

The intents of `metaobject_entry:update`, `content:file:pick`, `articles:create` and `articles:update` (`items.jsonl`, lines 403, 411, 426 and 427) carry two tools, `updateForm` ('Update forms on the page with the given data') and `getFormValues` ('Get the values of the forms on the page'). They describe tools for an agent that fills the page's forms. I read them as the routes' data and followed none of them. They are a lead for the admin's own AI assistant on these pages, as SH-10's `checkout-editor:profile` was. `articles:update`'s value also states 'Accepts a bare article ID, gid://shopify/Article/... or gid://shopify/OnlineStoreArticle/...'.

## 7. What sources state that no entry holds, for the second stage

These are run steps the ledger joins to this batch's routes. They are not placed (M-12).
- **Shopify Credit's main page on capture-advanced** (`derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/193.html.txt`):
  - line 24: 'Up to 3% cashback and two convenient ways to pay';
  - line 25: 'Pay your full statement balance in 1 month without fees, or pay over 10 months from sales for a fee. Earn up to 3% cashback on all eligible marketing, fulfillment, and wholesale spend.' Leads for qualities of CM-PAY-025;
  - line 28: 'Shopify Credit is currently unavailable in your region.' A lead for CM-PAY-025's scope: the cell holds 'only businesses in the Territory' (SH-S-7268);
  - line 31: 'Shopify partners with Stripe Payments Company and Celtic Bank for Shopify Credit.' The cell already holds both.
- **Oxygen deployment tokens** (`raw/runs/20261007T043208Z-journey-hydrogen/steps/016.text.txt`, line 46): 'Tokens allow third-party tools to create new Oxygen deployments. You can use tokens as part of a continuous integration or testing workflow.' A lead for an `extension-point` on CM-SFR-011, third-party tools deploying through Shopify's tokens, and for CM-DVT-006's testing.
- **A Hydrogen storefront's read-only variables** (`…/019.text.txt`): 'These variables provided by Shopify are supplied to all your environments.', with PRIVATE_STOREFRONT_API_TOKEN, PUBLIC_CUSTOMER_ACCOUNT_API_CLIENT_ID, PUBLIC_CUSTOMER_ACCOUNT_API_URL and PUBLIC_STORE_DOMAIN. Leads for CM-SFR-012 and CM-CUS-010. The step holds the capture store's token and session secret, which are cited like any other evidence.
- **Deleting a Hydrogen storefront** (`…/015.text.txt`, line 46): 'Deleting this storefront will delete all its deployments, environments, and deploy history. This can't be undone.'
- **Storefront API permissions** (`…/022.text.txt`): 'The Storefront API token is unique per Hydrogen storefront but Storefront API permission scopes are shared by all your Hydrogen storefronts.' A lead for CM-SFR-012.
- **The Bot protection routes on capture-plus** answered 'There's no page at this address' (`raw/runs/20261007T235903Z-journey-bot-protection/steps/002.text.txt`). This agrees with the feature productProtection being false in the captured stores, which CM-TRU-004 holds. A store on Plus with the feature would show the schedules. A gap at the first level, not a request: the cell is `core` already.
- **For the amendment:**
  - CM-CNT-009's note says 'E-anchor found no Shopify statement of their own' for URL redirects. These three routes are such statements: an admin route of their own, gated by storefront.enabled and LINKS.
  - The concern map placed `credit:card-management`, which only redirects to `/finance/cards` (`items.jsonl`, line 462), `core` on CM-PAY-025 (SH-S-5133). It is a case for the reading again, with SH-S-5044, SH-S-7134 and SH-S-5064.

## 8. Homonyms

- **'company'** is a B2B buyer's company (CM-B2B-002), not a business entity's type Company (CM-ACC-004), and **'location'** is a company's location, not an inventory location (CM-INV-005).
- **'comments'** are the blog's (CM-CNT-004), not product reviews (CM-SUP-001).
- **'tags'** on blog posts are the blog's, not product tags (CM-CAT-006).
- **'redirect'** in URL redirects is the storefront's (CM-CNT-009). The router's own redirects are the `shows` lines.
- **'overview'** (`credit:overview`) is the Credit account's page, not a store dashboard (CM-ANL-003).
- **'transaction'** is the Credit account's, not a partner's payout (CM-PTN-003).
- **'payment'** in Make Credit payment is the merchant paying its card balance, not a buyer's payment (CM-PAY-021) or a refund (CM-RET-002).
- **'rewards'** and cashback are the merchant's on its Credit card, not a buyer's (CM-LOY-003, CM-LOY-004).
- **'monthly'** statements aren't the plan's term (CM-PLN-002).
- **'integrations'** under Hydrogen are observability drains, not apps (CM-APP-001) or an app's settings (CM-APP-010).
- **'environment'** in Hydrogen is a deployment environment (CM-DVT-006, section 3), not the store's hosting environment (CM-OPS-003).
- **'account API'** in Customer account API is the buyer's account, not an account-level API (CM-API-013).

## 9. This brief, B-extent.md and the scripts

- **B-extent.md:** no rule of the brief read differently from it on these entries. B2 is where it bore hardest: M-4 makes a list the platform calls its integrations `core`, while B-extent's `extension-point` names third parties doing it through a provider interface. I followed M-4, the coordinator's ruling on that case.
- **`show` leaves out `intent` and the modules' names,** which these readings rest on often (`LogDrainDatadog`, `CreditLinkMerchantVendors`, `CommerceProtectionScheduleCreate`). They are read from `items.jsonl` at each entry's locator.
- **The checker's container test** compares relative paths, as SH-9 and SH-10 found (section 5).
- **No problem with the checker.**

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 98 of 98 entries, no problem.
- **Ancestors' gates:** 49 lines of 49 routes now name them in `reading`, by `method/held_router_gates.py`.
- **The cell changes stand, each read again:**
  - CM-CNT-001 gains `extension-point` from the documented intent `pick shopify/File`, by the ruling after SH-8.
  - CM-DVT-006 is held, `core`, a marked reading. Hydrogen's environments test a custom storefront's updates on preview URLs 'generated for each deployment' before production serves them. That is the cell's thing, stated for Hydrogen storefronts, not for the store's data or settings.
  - CM-OPS-005 is held, `core`, a marked reading. The Hydrogen storefront's server-side logs go to the drains the platform calls its integrations, each provider a filler (M-4). The cell's note already takes WooCommerce's Remote Logging here, strained, and the drains stand beside it. `new:Observability drains` is the other reading, for the final review.
- **B1 to B8 stand for SH-12 to SH-18.**
- **Read again at Shopify's amendment:** the concern map's `core` on `credit:card-management` (SH-S-5133), a route that only redirects, with SH-S-5044, SH-S-7134 and SH-S-5064.
- **Agent instructions inside the evidence:** four intents carry tool descriptions written for Shopify's own admin agent. The agent read them as data and followed none.
- **Cost:** 17.4 million tokens over 83 requests, about 178,000 an entry. The context reached about 328,000 tokens.
