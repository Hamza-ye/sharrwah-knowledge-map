# Review of the held pass's dry run, part R5b: ZD-1, lines 104 to 144

**What this is.** Part R5b of the review (`studies/class-model/briefs/H-review.md` at `f0dd52bd`). It covers lines 104 to 144 of `held/zid/placements-ZD-1.tsv` at `33946dbc`:
- lines 104 to 123: the last 20 entries of `dashboard-page-index` (batch entries 100 to 119, its items 100 to 119);
- lines 124 to 144: the 34 routes of `dashboard-route-manifest` in ZD-1 (batch entries 120 to 153, its items 2 to 35).

The verdicts are in `review-H-R5b.tsv`: 47 rows, at least one per line.

**What was read, pinned:**
- H-held.md, `held/selection.tsv` and the evidence map at `dc1e6414`;
- B-extent.md, "Cells and evidence" and "Conventions from the dry run" (the same at `dc1e6414` and now);
- ZD-1's placements and notes at `33946dbc` (the working file is the same);
- the model at `13205959`: the merged model and its parts are unchanged since, so the cells read now (`land_points.py cell`) are that commit's;
- other-product-class at `0d79b794f`.

**Abbreviations.** Every file below is at other-product-class@0d79b794f:
- `source.js`: `zid/structures/dashboard-page-index/source.js`;
- `manifest item N`: line N of `zid/structures/dashboard-route-manifest/items.jsonl`;
- `locales`: `zid/structures/dashboard-locales/items.jsonl`, cited by `<namespace>:<key>`;
- `ledger`: `zid/index/ledger/dashboard-routes.tsv`;
- `rest-en#N`: `zid/raw/runs/20261028T160128Z-dashboard-routes-rest-en/steps/NNN.text.txt`;
- `gaps-en#N`: the same in `20261028T150740Z-settings-gaps-en`;
- `en#N`: the same in `20261028T144855Z-dashboard-routes-en`;
- `devstore-billing-en#N`: the same in `20261028T190230Z-devstore-billing-en`;
- `signup-en`: run `20261028T155912Z-signup-en`.

`<cap>@zid` is that capability's Zid cell.

## Counts

| Verdict | Rows | Lines |
| --- | --- | --- |
| stands | 29 | 27 lines stand whole, of 41 |
| missing scope | 7 | 111, 116, 117, 118, 119, 120, 143 |
| can't tell | 4 | 126 (one entry of three), 129 (two entries of six), 135 |
| wrong reading | 3 | 116, 117, 141 |
| missing line | 2 | 104 (CM-SHP-002), 133 (CM-ACC-004) |
| wrong capability | 1 | 130 (CM-ACC-001) |
| wrong terms | 1 | 143 |

**The 18 misses, by cause and effect:**

| Cause | column | count | capability | Rows |
| --- | --- | --- | --- | --- |
| care | 104, 116, 117, 141, 143 | | 130 | 6 |
| brief | 111, 116, 117, 118, 119, 120, 143 | | | 7 |
| evidence | 129 (where-do-you-sell), 133 | 126 (platform-switch-call), 129 (platform-switch) | 135 | 5 |
| tool | | | | 0 |

**By structure:**
- `dashboard-page-index`, lines 104 to 123: 13 of 20 lines stand whole. Its 9 misses are 6 missing scopes (`brief`), 2 wrong readings and 1 missing line (`care`), all `column`.
- `dashboard-route-manifest`, lines 124 to 144: 14 of 21 lines stand whole. Its 9 misses are:
  - 4 can't tell (`evidence`);
  - 1 missing line (`evidence`);
  - 1 wrong capability (`care`);
  - 1 wrong reading and 1 wrong terms (`care`);
  - 1 missing scope (`brief`).

No miss changes `held` or `kind`, and no `supports` was wrong. Two misses would change a count if settled one way: platform-switch and platform-switch-call, if Zid offers there to move the store, would give CM-MIG-005@zid (`not-stated`) `core`.

## The cells these lines change as they stand

The checker's `CHANGES` lines (working tree) name three cells, and each was tested:
- **CM-STF-005@zid** holds nothing; lines 125, 127 and 134 make it held, `core`. The lines stand (below, "The access requests").
- **CM-ONB-004@zid** holds nothing; lines 126, 129, 131, 133, 136 and 140 make it held, `core`. The create-store routes are steps of the store-creation flow by their own ids: the onboarding profile, CM-ONB-004's thing. They stand, but three of the 14 entries can't be told and one also holds CM-ACC-004.
- **CM-ONB-002@zid** is `not-stated`, holding only ZD-S-0719 as `shows`; lines 142 and 144 give it `core`. The routes' own ids name the suspended store (manifest items 30 and 35), and the locales say "Your subscription has ended. select a plan to pick up right where you left off." (`subscription:suspended.dialog.description`). They stand.

Every other cell my lines touch already holds `core`, so the rest add evidence only.

## The cases

### Containers: Payments, Channels, Apps (lines 106, 113, 121)

**Ruling:** B-extent settles it.
- "What a place of its own is" counts "a page its admin's own page index names" as an admin route, and a section the navigation "names with its own title" as an admin section. Each container is one: `source.js` gives it a pageKey, a path and a title. Payments and Channels are sidebar groups, and Apps shows only its children.
- "A place whose thing a capability already holds, as its cells' readings show, is that capability's evidence". So a container goes to the capability whose admin place it is, `core`, and never `out`.

In my lines all three stand:
- **Payments → CM-PAY-002.**
  - The container's own permission is `all[ZIDPAY.view, ZIDPAY.viewPaymentLinks]` (`source.js`).
  - CM-PAY-002@zid reads Zid Pay "activated from the sidebar's المدفوعات" (ZD-S-0527).
  - CM-PAY-001@zid puts payment methods under Settings > Payment methods (ZD-S-0610).
  - The landing page (rest-en#64) also shows BNPL providers and the bank transfer accounts. Those providers have routes of their own (`services/payments/tabby` and others, ledger), which later batches place.
- **Channels → CM-CHN-001.** Its children are Marketplaces, Mobile app and POS (`source.js`, and the sidebar at rest-en#221). CM-CHN-001@zid's section منصات البيع (ZD-S-0985) is the child Marketplaces' own title (`navbar:marketplaces` = منصات البيع, locales).
- **Apps → CM-APP-001**, the parent of CM-APP-002 to CM-APP-009.
  - Its children are App Market, My apps and, when the App Market answers with categories, a Categories group (`source.js`).
  - Its sidebar is `childrenOnly`, and its path `apps` is the App Market's too.

**Fix to H-held.md, rule 3** (within B-extent; add after its second point):
> A container itself (a section with children, such as Payments, Channels or Apps) is a place of its own when the navigation or page index names it with its own title. Place it on the capability whose admin place it is, as the cells' readings show, `core`. Where no capability's cells read it, write `new`. It is never `out`.

**Checker:** no test can judge the capability. The build could mark a page object that has `children` (in `source.js`) as a container in the entry's text, and the checker could print a NOTE for each container line, for a second reading.

### Pages with a release badge

None in my lines.
- No page object from `logistics.shipment-transactions` to `apps.installed` carries `badge` (`source.js`).
- `growth` carries `sidebar.hasPulseDot: true`, a dot that states no release. Line 112 keeps `core`.

### Pages listed only under a store condition (lines 111 and 116 to 120; and 143)

Facts, from `source.js`:
- `financing` is listed under `...s?[]:[{pageKey:'financing',…}]`. `s=N()`, and `N` is imported from `./use-is-ngo-store-SFG8ijPH.js`, so the page is listed only for a store that isn't an NGO store. The same condition hides the dropped `channels.marketplaces`.
- The five POS sub-pages are `children:_?[…]:[]`, where `_=!!(n||r?.is_trial)` and `{hasPos:n, subscription:r}=k()`. They are listed only for a store that has POS or whose subscription is a trial.

Line 116's reading says the POS condition ("listed only with POS or a trial") and line 111's says "hidden for charity stores". Lines 117 to 120 don't say it, and every scope is empty.

**Ruling:** the condition is the `scope`, in the source's identifiers. `supports` stays `core`, since the page is the platform's own admin place.
- B-extent gives the model: "A released flag supports `core`, with its plan or store as its scope."
- H-held.md's rule 2 places a listed feature "with the plan or store it is stated for as its scope".
- Rule 1 makes the source govern where it and the item differ. Here the item leaves the condition out.
- The ambiguity is rule 5's "the entry states it for", which the agent read as the item alone (notes, "Store-flag conditions and scope").

Line 143 is the same case in the manifest. The wallet's four routes are children of `$lang.suspended.$storeId` (manifest items 31 to 34), so they are stated for a suspended store. The batch put `suspended` in `terms` instead (a `care` miss) and left `scope` empty.

**Fix to H-held.md, rule 5** (within B-extent):
> `scope`: the plan, country, market, store or store condition the entry states it for, with its item's source. Where the source lists the entry only under a condition, write that condition in the source's identifiers. A condition can be:
> - a store flag, such as `hasPos`;
> - a store's state, such as `subscription.is_trial` or a parent route `suspended`;
> - a kind of store, such as `use-is-ngo-store`.
>
> A condition the source names only by a minified variable takes the name of the module it is imported from, or of what it is computed from. Mark it as a reading.

**Checker:** the present checker can't catch it, because the items don't carry the condition (the evidence map says so too). The build of `held_entries.py` should render each page's condition into the entry's text, as `listed_if: <condition>`, from `source.js`. A test would then flag a line with an empty `scope` whose entries carry `listed_if`. For the manifest, the parent's id is already in the text: a NOTE could flag a line whose entries' `parentId` names a store state (`suspended`) when its scope is empty.

### The bank accounts page against CM-PAY-030's cell (line 110)

**Facts:**
- The page (rest-en#97, `services/payments/bank-accounts`) says:
  - "Enable bank transfer payment method";
  - "These bank accounts will appear as payment methods for customers on your store.";
  - "Manage your payout bank account separately here.";
  - and it has a column "Visible at checkout".
- It is under `any[PAYMENT_OPTIONS.manage, PAYMENT_OPTIONS.view]` (`source.js`), not a ZIDPAY permission.
- CM-PAY-030@zid holds `core` from ZD-S-0643, ZD-S-0645 and ZD-S-0644. Its reading ends: "The bank accounts page (ZD-C-004) is cited in CM-PAY-005: none of its statements says it holds the accounts shown for transfer."
- CM-PAY-005@zid cites ZD-C-004's statements:
  - bank accounts under إدارة طرق الدفع (ZD-S-0557);
  - choosing the bank account that receives the deposits (ZD-S-0558);
  - the identity must match the account (ZD-S-0559).
- CM-PAY-005@zid carries the term الحسابات البنكية, the page's own Arabic title. That is why CM-PAY-005 leads entry 106.

**Ruling:** line 110 stands on CM-PAY-030, `core`.
- The notes say this "contradicts" CM-PAY-030's cell. That is half right. The cell's reading is true of ZD-C-004: its statements describe the deposit account, not the accounts shown at checkout. But the cell doesn't know that the dashboard's Bank accounts page is the transfer page.
- So ZD-C-004 stays on CM-PAY-005, and the notes' "the coordinator may want to move ZD-C-004's page there" isn't supported.

**What to change.** When `held_amend.py` writes CM-PAY-030@zid's reading, it should say this: the dashboard's Bank accounts page holds the accounts shown at checkout, and by its own words the payout account is managed separately.

**For the coordinator, a reading:** الحسابات البنكية means two things on Zid, the transfer accounts and the deposit account. CM-PAY-005's note could gain Zid's homonym, as CM-PAY-030's note already holds Salla's.

Without the page's text, the entry and the cells' terms would have led to CM-PAY-005. The run step decided it (see "Readings that rest on other files").

### The access requests by Zid's own team (lines 125, 127, 134)

**Facts:**
- The routes are `access-request/:requestId`, `/approve` and `/deny`, outside any store (manifest items 19, 3 and 7). No run opened them (ledger).
- The locales' `access-request` strings say:
  - "Zid technical team would like to access your account to provide support and solve the challenges you are facing in your store setup." (`body.sentiment`);
  - "Access request for your store";
  - details "Role", "Access duration" (`{{count}} hours`), "Employee name" and "User name";
  - "In case you want to grant the employee access, please contact customer support."
- CM-STF-005@zid holds nothing. CM-STF-005@salla places "support's temporary access requests appear on /manage/support-access, granted only on approval" (SA-S-5132) as `core`.
- CM-ONB-003's note says: "Salla's support team's temporary access requests (SA-S-5132) are cited in CM-STF-005."

**Ruling:** `core` on CM-STF-005 stands.
- H-held.md rule 4's S7 makes a partner's or an app's access `shows`. These requests are the platform's own team's, so S7 doesn't apply.
- B-extent's `core` ("the platform itself does it for the merchant", by its own route) applies, as the cell's own reading of SA-S-5132 does.

Two points for the coordinator:
- **Who requests rests on the locales**, which H-held.md doesn't let an agent read and the selection marks `read: no`. The route's own item names no requester. Under H-held.md as written, the line would have been a "can't tell", or `shows` by S7 if read as a partner's. See the fix below.
- **CM-STF-005's name is "Third-party access to the merchant's admin"**, and its note says "a partner outside the store's staff". The model already holds the platform's support team there, by CM-ONB-003's note, and Zid's requester is the platform's own team. B-extent's "Names" rule lets a part propose a rename: "Access to the merchant's admin by people outside its staff (partners, the platform's support), requested and granted per store". This stays within B-extent. The coordinator renames.

### The notes' other "couldn't tell" items in my lines

- **133, reset-password (line 130): wrong capability, CM-ACC-001.**
  - The model keeps the account's password and sign-in pages in CM-ACC-001: Zid's "Settings > Account settings: email and password" (ZD-S-0900) and Salla's "dashboard app for sign-in, on /auth" (SA-S-3534) are its `core`.
  - CM-TRU-001 holds the security added to sign-in: 2FA (ZD-S-0943) and passkeys (SH-S-2512).
  - The locales' `auth:forgotPassword.title` is "Password recovery!".
- **138, login/impersonate/:token (line 135): can't tell.**
  - No Zid run's actions name `impersonate` (searched: partner-signup-en, devstore-markets-en).
  - `index/instruments.json` says the development store is signed in to by "a one-time link to dashboard.zid.sa". Whether that link is this route isn't held.
  - CM-TRU-001 is the weakest of three. The alternatives are CM-ACC-001 (sign-in pages) and CM-STF-005: `core` if Zid's team uses it, `shows` if a partner does.
- **143, 146, 147, register OTP (lines 138, 141): stand on CM-ACC-001.**
  - The notes' "No capability holds merchant sign-up as such" misses two things. CM-ACC-001@shopify holds "what Account registration requires" (SH-S-0017), and its reading defines the Store Owner as the person who signs up. Salla's sign-in app is CM-ACC-001's `core` (SA-S-3534).
  - Line 141's reading cites "steps 20 and 21" for "is sent to your whatsapp number". The text of those steps is "Code was sent to number ending with ********5871". The words are in the answer to `POST /v1/managers/store/link-mobile-otp`, called at step 20 (signup-en `answers/hermod.zid.sa/v1/managers/store/link-mobile-otp/cebd39d4c2674258aae12da7bcf7dc75843972a2d345945740c56fe702d234f0.json`).
- **120, 142, 144, subscription (lines 124, 137, 139): stand on CM-PLN-001.**
  - CM-PLN-001's own note reads Shopify's "subscribe and pick-period routes" as its own, which is the same kind of route.
  - The in-store checkout that the root route sends a store to holds a card payment and "Auto-renews every month" (devstore-billing-en#5). That bears on CM-PLN-005 and CM-PLN-002, but it is `$lang.stores.$storeId.checkout._index`, a later batch's entry.
- **create-store (lines 126, 129, 131, 133, 136, 140): stand on CM-ONB-004, with four exceptions.**
  - business-type also holds CM-ACC-004. A reading: Zid's strings give "Business type" the values Individual, Company, Corporate and Charity (`common:businessType.*`), which CM-ACC-004@zid reads as the activity type (ZD-S-0753).
  - where-do-you-sell can't be told against CM-ONB-001.
  - platform-switch and platform-switch-call can't be told against CM-MIG-005. The notes' "they are questions, not a migration service" isn't settled by the route names. The growth page sells a "Switch store service" (rest-en#182).
- **Badges:** none in my lines.

### Readings that rest on files beyond the entry's item and source

H-held.md's rule 1 names the item and its source. Its read list names `index/` as a guide.

| What the reading rests on | Lines | Does H-held.md allow it? |
| --- | --- | --- |
| `source.js`, the item's source | 105, 106, 107, 109, 110, 111, 113, 114, 116, 121 | yes (rule 1) |
| the item's own fields beyond the rendering (the manifest's imports) | 144 | yes (rule 1: the item) |
| the cells' readings ("the cell's …") | 107, 108, 109, 112, 122, 123 | yes (its model tools) |
| the ledger's status alone (redirected, not opened) | 124, 126, 129 to 133, 135 to 140, 143 | as a guide (`index/`); it decides no placement |
| a run step the ledger names (page text) | 104, 105, 106, 110, 111, 112, 114 to 120, 128 | no: rule 1 doesn't name it |
| a run's answer, cited as its steps | 141 | no |
| the locales (`read: no`) | 125, 127, 134, 142 | no, and the selection excludes them |

The run steps decided the placements at lines 104 and 110, and the locales decided `core` at 125, 127 and 134. Without them those lines would have read differently, so these files bear real weight.

**Fix to H-held.md, rule 1** (within B-extent: the entry stays the statement, and these only clarify it):
> Where the item and its source leave a page or route unclear, you may also read:
> - the run steps the platform's ledger names for its route (`index/ledger/`), and a run's answers received at those steps, cited by run, step and file;
> - for a route no run opened, the locale strings of the route's own namespace, cited by `<namespace>:<key>`. Never place a string as an entry.
>
> Mark each reading that rests on them as a reading, and quote them exactly. An unopened route's placement that rests on nothing but its name is listed in your notes.

**Checker:** the new quote test ("found nowhere held, in the entry, its structure's sources or the platform's run pages") flags lines 125 and 142, whose quotes are true and in the locales, and line 141, whose quote is in an answer. Two changes would make it exact: search the locales and the runs' answers too, and check each quote against the file the reading cites. Then 141 would be caught as citing the wrong file, and 125 and 142 would pass.

## Recurring misses, and whether the checker would catch them

| Miss | Lines | Test |
| --- | --- | --- |
| scope empty where the source lists the page under a condition | 111, 116 to 120, 143 | none now: the build must render `listed_if` from `source.js`, then test for an empty scope |
| a reading that misstates its source | 116, 117, 141 | 141 only: the quote test, as a NOTE, better against the cited file. 116 states a claim about the model ("the ANL cell leaves POS reports to it") that no cell holds, and 117 adds "devices"; no test reads meaning |
| an entry that is two capabilities' at once, with one line | 104, 133 | none. The leads would help. Entry 100's leads (PAY-020, PTN-003, SHP-009) hold neither of its capabilities, while `caps --terms "shipping fees"` finds CM-SHP-002. Entry 136 has no lead, and the English "business type" is in no capability's terms |
| a state of the store written as a term | 143 | a NOTE: one term on lines of different capabilities in one structure (`suspended` is on CM-ONB-002 at 142 and 144, and on CM-PLN-006 at 143) |
| the capability of a sign-in route | 130 | none |

## What the batch never placed

### dashboard-page-index, items 100 to 119 and their source

The items match `source.js` for my 20 pages: pageKey, path and title key, in the source's order. The extractor drops these page objects of the Channels and Apps groups, whose helpers (`mt`, `at`, `st`, `lt`, `ut`) the source defines before the page list:

| Page object | What the source states | Its route in the manifest | Would it change a cell? | Left out by |
| --- | --- | --- | --- | --- |
| `channels.marketplaces` | title `navbar:marketplaces` (Marketplaces / منصات البيع, locales); path computed by `mt()` (`channels/marketplaces/connect/marketplaces`, or `…/connect/get-started` when no marketplace is active), `alternativePaths: ['channels/marketplaces']`; permission `re.useMarketplaceConnect`; listed only when not an NGO store | yes: `connect/marketplaces` (opened, rest-en#36), `connect/get-started` (redirected), `connect` (rest-en#39, #69), later batches | no: CM-CHN-001@zid holds `core` for منصات البيع (ZD-S-0985), the page's own Arabic title. Its title, permission and condition reach no entry | the build (the extractor skips a computed path) |
| `apps.categories` | title `navbar:appsMenu.categories` (Categories / التصنيفات); path `apps/browse` (the variable `K`); listed only when the App Market's answer has categories | yes: `apps/browse` (gaps-en#38, and run 20261028T185150Z-devstore-tracking-apps-en) | no: CM-APP-002@zid holds `core` for browsing by category (ZD-I-0538) and categories as `extension-point` (ZD-S-0422, ZD-I-0442) | the build |
| `apps.categories.${e.id}`, `apps.categories.${e}.${t.id}` | one page per category and subcategory, titled by the answer's names (`apps_by_category`), which `source.js` doesn't hold | `apps/browse` with `?tab=` | not tested. A category the answer lists and the concern map's inventory lacks would be an `extension-point` for its capability. Its names are in a run's answer, not this structure | the build; the names are in no structure |
| `apps.${e.id}` | one page per installed app, from the store's `installed_applications` | `apps/:id/embedded` (not opened) | no: the list is one store's own data (rule 2, `out`), and the route is an app's page | the build |

**What the items also leave out for my 20 pages:**
- each page's permission (ZIDSHIP, ZIDPAY, PAYMENT_OPTIONS, POS's `S.*`, `ne.view`, `ie.mobileApp`);
- the two listing conditions (rows above);
- the sidebar's marks (growth's `hasPulseDot`).

The conditions are the scopes this part finds missing. The permissions name staff permissions, which `store-permissions` holds for its own batches.

**The evidence map's reading,** added after the batch ("each dropped page's route is in `dashboard-route-manifest`… so the model loses nothing"), holds for my stretch as to placements. Every dropped page's route is in the manifest, and no cell's placement would change. It doesn't hold for three things, and nothing else carries them:
- the pages' own titles: Marketplaces / منصات البيع and Categories / التصنيفات;
- the marketplaces page's permission;
- the marketplaces page's NGO condition, which would be a scope.

### dashboard-route-manifest, items 2 to 35

- The items equal the source. All 437 routes of `items.jsonl` equal the `routes` values of `source.js` in the same order (compared as JSON). Item 1 (`root`, no path) is the dashboard's root layout, no place: the ledger marks it redirected, and nothing is lost.
- **The rendering** prints `id`, `parentId`, `path` and `index`, and leaves out each route's `module`, `imports`, `css` and loader flags. The imports name what a page holds:
  - `suspended._index` and `subscription._index` import `packages`, `package-card` and `package-card-pos-subscribe-price`;
  - `suspended.$storeId` imports `use-whatsapp-subscription` and `use-navigate-to-checkout`;
  - `subscription.checkout` imports `use-checkout-noon-session-cleanup` and `check-subscription`.

  None changes a cell. The plans are CM-PLN-001's, which holds `core`. "noon" in a hook's file name doesn't say the checkout's processor is a company of that name: CM-PLN-005@zid's `outside` rests on an unnamed processor (ZD-S-0680), and a file name isn't a statement naming one. **Left out by the tool** (the rendering). Line 144 read the imports from the item. Printing the module and the imports' names, without their hashes, would let every batch read them.
- **Held, but in no entry, found while reading these lines.** Both are left out by the selection (`dashboard-locales`, `read: no`):
  - The suspended store's "Your store information will be stored for 2 years." (`subscription:suspended.dialog.storeInformation`). CM-TRU-016@zid is `not-stated`: "no statement held says what happens to a store's data after the store closes". A reading: a suspended store isn't stated to be closed, so this is a lead for that cell, with the quality "store information stored: 2 years", not a placement.
  - The access request's duration in hours, a quality of CM-STF-005@zid, with the employee's name and role.

## The notes' claims for my structures

| Claim | Verdict | Why |
| --- | --- | --- |
| ZD-1 holds "the first 34 routes of its route manifest (items 2 to 35, the routes outside a store…)" | stands | manifest items 2 to 35: every parentId is `root` or `$lang.suspended.$storeId` |
| "Every placement supports core except entries 12 and 13"; "No own-service" | stands for my lines | `own-service` tested at lines 111 and 115: the pages name a brand, not a maker |
| 106, Bank accounts, contradicts CM-PAY-030's cell; move ZD-C-004 there | half right | above: the page is CM-PAY-030's; ZD-C-004 is the deposit account and stays on CM-PAY-005 |
| 133 and 138: "CM-ACC-001 is the alternative" for 133; for 138, who impersonates isn't stated | 133: wrong capability, CM-ACC-001; 138: stands as a can't tell | above |
| 143, 146, 147: "No capability holds merchant sign-up as such" | partly wrong | SH-S-0017 and SA-S-3534 are in CM-ACC-001, where the lines are |
| 120, 142, 144: "CM-PLN-005 is the alternative" | the lines stand on CM-PLN-001 | CM-PLN-001's note reads subscribe routes as its own |
| 121, 125, 137: core, as Zid's own team requests; "a run that opens an access request would settle it" | stands | the locales already settle the requester; a run would add the values of role and duration |
| create-store on CM-ONB-004; 130 and 131 "are questions, not a migration service" | stands for most | business-type also holds CM-ACC-004; where-do-you-sell, platform-switch and platform-switch-call can't be told |
| the containers placed on their children's capability; "42 is the weakest" | for 102, 109 and 117: stands | B-extent settles containers |
| no rule for a route's release badge | none in my lines | |
| `dashboard-page-index`: its source holds 137 objects, its items 119; the extractor drops 18 | stands for my stretch | `channels.marketplaces` and the four app entries, for the reasons the notes give: a computed path or key |
| "Several readings depend on them (47/48, 51, 72, 81, 88/89, 97, 41)" | partly: it leaves out my lines | entries 107 (line 111) and 112 to 116 (lines 116 to 120) also depend on a condition |
| Route manifest: item 1 isn't an entry, "consistent with the ledger" | stands | above |
| Qualities on the pages: Zid Financing's terms (rest-en#156) | stands | the page says "exceed 40,000 in the past 3 months", "Up to 10m financing", "10-25% annual profit margin", "5-36 months flexible payment plans" |
| the suspended store's "stored for 2 years", "a lead for CM-TRU-016" | stands, as a lead | above |
| Problems: what may be read; container rule; store-flag scope | each stands | the fixes above |
| "The script: the checker printed no problem" | stands | at the working tree: 0 problems, and NOTEs at lines 125, 141 and 142 (the quote test) |

## The leads

The leads as `show --candidates` prints them now.

**`dashboard-page-index`, lines 104 to 123:** the right capability is among the leads for 8 of 20 lines (107 to 112, 114, 123).
- For 8 lines the entry has no lead at all: 105, 106, 113, 115, 117, 118, 120, 121.
- For 4 lines the leads miss: 104, 116 (CM-ANL-002 only), 119, 122 (CM-APP-001 only).

**`dashboard-route-manifest`, lines 124 to 144:** the right capability is among the leads for 2 of 21 lines (128, 132).
- Of the 34 routes, 30 have no lead.
- Line 130's only lead is CM-CUS-010, the buyer's.
