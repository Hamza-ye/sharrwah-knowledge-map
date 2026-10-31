# SH-100: notes (Shopify, 61 entries, effort high)

Five structures, all their entries, read in observed-sh at `e38dc17e3` (the clone at `04de369da`, which changes none of them): `sidekick-quotas` (1), `sign-in-methods` (8), `signup-onboarding-questions` (5), `signup-router` (19) and `theme-editor-templates` (28). No earlier batch placed any of them, and `held_entries.py earlier` found no line on their own keys but the links' addresses and labels named below.

**Count by placement:** 61 entries in 68 lines. 57 entries are placed on a capability (64 lines), 4 are `out`, and none is `new`.

## The rules I set (R100.1 to R100.14), for the coordinator to check

### `sidekick-quotas` (R100.1 to R100.3)

The entry is Sidekick's own API's answer for the store: `GET sidekick.shopify.com/api/store/capture-plus/quota`, 200 (meta.json; the trace of run `20261007T030938Z-journey-sidekick`). It names two quotas, `app_generation` and `storefront_agent`.

- **R100.1, Sidekick's limits are its qualities, on CM-AIA-002 `core`.** This follows the coordinator's message and R99.7, which keeps the composer's counters as qualities. The qualities are all three limits the API states: `app_generation`'s hourly limit 12800 and weekly limit 51200, with no unit stated, and `storefront_agent`'s `limit_cents` 1000. The store's own values go in `reading`, never in `quality`: `enforced`, `temporary_access`, `temporary_boost`, `percent_used`, `used_cents`, `resets_at` and `exceeded_at`. `temporary_boost: true` matches what Generate app showed: 'Enjoy a temporary boost to your app generation limits.' (`steps/052.text.txt`, line 128).
  - **Scope `capture-plus`.** The quota is the API's answer for that store, and rule 2's last paragraph says a limit the platform lists for a store takes that store as its `scope`. R99.9 gave the composer's controls no scope, but they are controls, not limits. If the coordinator reads the structure as one store's observation with no condition, the three scopes drop.
- **R100.2, the quota `app_generation` takes CM-APP-009 `core`.** Its thing is the custom app Sidekick generates for the store, as R99.8 placed Generate app (E105). The steps show it: 'Describe your app' (`steps/052.text.txt`, line 131), then 'App is ready' (`steps/055.text.txt`, line 115). The limits stay on the CM-AIA-002 line, so they aren't counted twice.
- **R100.3, the quota `storefront_agent` takes CM-SUP-004 `shows`.** Its limit stays on the CM-AIA-002 line, as Sidekick's API's (R100.1). That the agent is CM-SUP-004's is a reading:
  - the same run's analytics schemas describe a buyer-facing agent: 'Storefront Agent message activity and buyer feedback, one row per conversation turn' (`answers/admin.shopify.com/AnalyticsSchemas/827dd3e0….json`);
  - SH-47 placed the Fall 2026 Edition's storefront agent card on CM-SUP-004 `own-service`, as Shopify Inbox's (SH-E-1221bb25, its line 55).

  I wrote `shows` because the quota names no maker or provider of the agent. `own-service` would rest only on joining the term to that card. **Other readings:** CM-AIA-005, buyers buying through AI agents, though its cell's channels are AI chats outside the store; or a Sidekick agent for the storefront, which would make this line CM-AIA-002's. If the limit is read as the storefront agent's own quality, it moves to this line.

### `sign-in-methods` (entries 2 to 9)

The structure's sign-in methods themselves are already cited in CM-TRU-001's cell (SH-S-2512, and the inventory entries SH-I-1747 to SH-I-1755). Its remaining 8 entries are these:
- 'Close message', 'Refresh' and '@.' are `out`, as UI strings:
  - 'Refresh' is the button of the banner “Captcha couldn't load. Refresh the page and try again.”;
  - '@.' is the email field's typo suggestion, 'Did you mean' a button the page's script fills (`20261007T044524Z-journey-cli-login/steps/001.html`).
- Get started and Log in are CM-ACC-001 `shows`. A link takes the line of the page it opens, as SH-92's links to the sign-up (line 10) and SH-99's Log in (line 85) were placed.
- Need Help? is CM-ONB-003 `core`. It opens the Help Center's 'Logging in to your Shopify account' (`help-center/help.shopify.com@en-ar/pages.jsonl`, line 225).
- Terms and Privacy Policy are read with their sentence, 'By continuing, you agree to the Terms and Privacy Policy, and to receive marketing emails from Shopify. Unsubscribe anytime.':
  - Terms is CM-ACC-001 `shows`, as the cell reads SH-S-0229: signing up binds the merchant to the Terms;
  - Privacy Policy is CM-TRU-013 `core`, as SH-20 placed a link to the same page (line 66).

### `signup-onboarding-questions` (R100.4, R100.5)

- **R100.4, each choice of 'What can we help you do?' is CM-ONB-004 `core`.** The question is “Select all that apply. We'll tailor your setup.” (`20261005T115840Z-journey-organization/steps/036.text.txt`; `20261006T232216Z-journey-signup-new-account/steps/013.text.txt`). It is the merchant's onboarding profile that tailors the store's setup. CM-ONB-004's note names Shopify's onboarding question as the thing no capability held. The answer's value goes in `terms` as the platform's identifier, and the preselected state (`[x]`) goes in `reading`.
- **R100.5, the way of selling a choice names takes that capability's line, `shows`:**

  | Choice | Capability |
  | --- | --- |
  | Sell online | CM-SFR-001 |
  | Sell in-store | CM-POS-001 |
  | Dropshipping | CM-CAT-010 |
  | Sell digital products | CM-SEL-002 |
  | Move existing store | CM-MIG-005 |

  A choice states what the merchant asks the setup to be tailored to. It is not the platform's place for that thing, and it names no one who does it, so it supports no placement. SH-80 placed the setup guide's section Sell online `core` on CM-SFR-001 (line 42), but that rests on the section's tasks, which is another thing. A `core` here would lift CM-SEL-002, whose cell says no statement shows Shopify itself delivering digital goods, and CM-CAT-010, whose placement rests on the App Store's categories (`extension-point`).

### `signup-router`: where the router digest's rules fit (R100.6 to R100.11)

The sign-up app is the platform's own app at admin.shopify.com/signup (`signup-router-481e50eda217.js`, `raw/runs/20261006T215853Z-signup-bundles/fetch.warc.gz@723109`). The digest's rules fit its reading of a route, as follows:
- **Support:** every route is the platform's own, `core` (rule 9).
- **Redirects:** a route that only redirects is `shows` on its target (rule 10).
- **Containers:** rule 8 and R14.4.
- **A catch-all:** R18.1.

**Where they don't fit:**
- **Gates and scope:** no route has `eligibility` (meta.json: `with_eligibility: 0`), so no line takes a scope. `held_router_gates.py` reads only the admin router, and it has nothing to add here.
- **Full addresses:** the routes aren't in `index/ledger/admin-route.tsv`, and their paths are calls to path builders that resolve in another bundle (the register). So rule 4's full address comes from the code's own map of legacy targets and from the runs' URLs.

The rules:
- **R100.6, the helper `p`'s six routes are legacy redirects.** `signup-questionnaire` and `optional-checkout:*` have, as their only content, a loader that counts `SignupEvent.LegacyRouteHit` and redirects to `/signup/${i.signupUuid}${A[r]}${o}`. Each is `shows` on its target:
  - `signup-questionnaire` goes to the sign-up itself, CM-ACC-001;
  - `optional-checkout:index`, `:checkout` and `:extend-trial` go to the subscribe checkout, CM-PLN-001 (the digest's rule 33);
  - `:select-plan` goes to the plans, CM-PLN-001;
  - `:pos-pro` goes to the POS Pro step, CM-POS-001.

  Their own words ('questionnaire', 'extend-trial') go in `reading`, since each target takes one line.
- **R100.7, the subscribe flow is CM-PLN-001 `core`.** That covers `signup:subscribe:layout`, `signup:subscribe:root`, `plans` and `checkout`. The flow is the new store starting its plan, and Billing's checkout is the merchant paying Shopify (rules 33 and 43). `pos-pro` is CM-POS-001 `core`, by its own words. The subscribe checkout page's prices and trial ('Start for free, stay for $1', `steps/034.text.txt`) are a run's, not the route's (M-12).
- **R100.8, `signup:store-details` is CM-ONB-004 `core`.** Both runs met the onboarding question at its address. The other reading is CM-ACC-006, by the route's words 'store details', but that capability is the admin's Settings > General, and no held page of this step shows a store's details.
- **R100.9, `signup:subscribe:address` is CM-ONB-001 `core`.** This reads its component Address, which imports `updateSignupCountry`: the address sets the sign-up's country. No run opened it. That it is the subscription's billing address (CM-PLN-005) is the other reading.
- **R100.10, the containers:**
  - `signup:root` and `signup` are CM-ACC-001 `core`. `signup:root` is the app's root, over the sign-up alone (one part of the platform: rule 38, M-13), and `signup` is the merchant's sign-up, as the links to admin.shopify.com/signup were placed.
  - `store-select` and `organization-select` are CM-ACC-003 `core`: choosing among the owner's stores ('Choose a store or create a new one', `20261005T115840Z-journey-organization/steps/033.text.txt`, line 2) and the organization the store goes under, as SH-2 placed Create store (line 58).
- **R100.11, `signup:post-store-selection-decision` (the index) and `signup:unexpected-route` (at `*`) are `shows` on CM-ACC-001.** Their components, PostStoreSelectionDecisionRoute and UnexpectedSignupRouteRedirect, both import `useNextRoutedSignupDestination` (the bundle's module map). That reads them as routes that send the merchant on to the sign-up's next step: a redirect to a named page, not the root (rule 10; R18.1). This is a reading of the modules' names. The index's name doesn't say redirect, so by rule 11's letter it could stay `core`, and the catch-all could be `out` if its target is the root. Opening either address would settle it.

### `theme-editor-templates` (R100.12 to R100.14)

The picker is the theme editor's dialog `topbar-picker-templates` on capture-plus, editing the published theme test-data (run `20261004T111454Z-journey-theme-editor`, steps 3 to 19, frame 0). No line takes a scope: the structure is one store's observation, and it states no condition.
- **R100.12, the picker's own controls:**
  - its search field, 'Online store search' (placeholder 'Search online store'), is the theme editor's own, CM-SFR-002 `core`; CM-SFR-013 is the buyer's search, a homonym;
  - the back button is `out`, a UI string.
- **R100.13, a template the picker offers is the theme's own page type, CM-SFR-001 `core` (Themes and templates), as the coordinator's message reads it.** The run is decided at once:
  - it covers the picker's 13 template buttons, the five views' headings (containers of the type's templates, M-13), their default and alternate templates (counted 'Assigned to N', the store's own data, in `reading`), and Create template;
  - the editor is where the entry sits, so it gives no line;
  - the resource a template is for (products CM-CAT-001, collections CM-CAT-003, pages CM-CNT-003, blogs CM-CNT-004, the gift card CM-LOY-002, the cart CM-CHK-002, search CM-SFR-013, metaobjects CM-CNT-002) is named in `reading`, not given a line, as R14.7 keeps a notification template on CM-NTF-001 alone.

  **Other readings:**
  - SH-23's R23.1 placed each page of the checkout editor's picker on the editor itself (CM-CHK-003). Read so, each template button would also take CM-SFR-002 `core`.
  - Rule 2's 'every thing the entry names' would give each template a line on its resource's capability. Every such cell is `core` already, so either way no cell changes.
- **R100.14, 'Checkout and customer accounts' is CM-CHK-003 `core` alone.** It isn't a theme template. It leaves for settings/checkout/editor/profiles/9408086312, 'capture plus · Checkout Editor · Shopify Plus' (actions.jsonl, step 19), the editor whose note says it configures the checkout and the customer accounts pages together. Its way back, Online store theme, is SH-23's R23.3.

## New things

None. These are the terms I searched with `class_slice.py caps --terms` before placing:

| Topic | Terms searched |
| --- | --- |
| The account and onboarding | onboarding; questionnaire; sign in; sign-in; log in; login; sign up; signup; setup guide; passkey; captcha; migration; import store; dropshipping; terms of service |
| Agreements and legal | merchant agreement; terms of service; legal; agreement; marketing emails; unsubscribe |
| Sidekick and agents | storefront agent; shopping assistant; AI agent; agent; generate app; app generation; custom app; quota |
| Chat | chat; shopping; assistant; conversation; buyer message; live chat; chatbot |
| The theme editor | template; theme editor; metaobject; password page; 404; storefront search; search page; gift card; home page; collection list |
| Checkout editor and storefront password | checkout editor; checkout branding; customize checkout; checkout customization; password; coming soon; storefront password |

## Entries I couldn't tell, and what would settle each

- **Entry 1's storefront agent** (R100.3): a held statement of what Sidekick's `storefront_agent` quota limits, such as a help page on the storefront agent's cost or limit, would settle its capability and its support.
- **The scope of entry 1's limits** (R100.1): the quota of a store on another plan would show whether the limits are the store's or every store's.
- **`signup:post-store-selection-decision` and `signup:unexpected-route`** (R100.11): a run that opens /signup/<uuid> with a store already chosen, and an unknown /signup/<uuid>/x, would settle them.
- **`signup:subscribe:address` and `signup:organization-select`** (R100.9, R100.10): no run opened either. Their pages would settle each capability.
- **The templates' second lines** (R100.13): the coordinator's reading of 'on the theme capabilities' decides whether each template also takes CM-SFR-002, or its resource's capability.

## Structures whose items and sources disagree (the source governs)

- **`sidekick-quotas`:** the entry's text drops `storefront_agent`'s `exceeded_at: null`, which `source.json` holds. The register names it too. Its reading carries it.
- **`signup-router`:** `items.jsonl` gives five routes no parent: `signup-questionnaire`, `optional-checkout:index`, `signup:subscribe:layout`, `signup` and `signup:root` (meta.json: `top_level: 5`). The code nests them differently:
  - `signup:root`'s `children` are the routes `O()` returns, the route `signup` alone;
  - `signup`'s children spread in `...L(...)`, the helper's six routes, and `...T(...)`, the subscribe layout. So those routes are `signup`'s children, and `signup:unexpected-route`'s position 5 counts them.

  The helper's two top-level routes have `position: null`. No line rests on the items' nesting.

## Statements no entry holds: leads for the second stage (M-12)

| Lead | Where | What it may change |
| --- | --- | --- |
| A captcha on the Shopify account's log-in: “Captcha couldn't load. Refresh the page and try again.” and `data-captcha-simple` on the form | `20261007T044524Z-journey-cli-login/steps/001.html`, the banner before the button `refresh-page-trigger` | CM-TRU-001, sign-in security; CM-TRU-004 and CM-CUS-012 are bot protection at checkout and for buyers, other things |
| Consent to Shopify's marketing emails at sign-in and sign-up: 'and to receive marketing emails from Shopify. Unsubscribe anytime.' | `20261007T044524Z-journey-cli-login/steps/001.text.txt`, line 17; `20261006T232216Z-journey-signup-new-account/steps/004.text.txt`, line 11 | no capability holds the platform's own emails to its merchants (searched: marketing emails; unsubscribe) |
| The log-in page for the CLI: 'Continue to Shopify CLI', titled 'Log in — Shopify CLI' | `20261007T044524Z-journey-cli-login/steps/001.text.txt`, line 2 | CM-DVT-002, the CLI's sign-in through the Shopify account |
| The sign-up page's trial: 'Start your free trial', '3 days free, then 3 months for $1/month' | `20261006T232216Z-journey-signup-new-account/steps/004.text.txt`, lines 1 and 2 | CM-PLN-001, which SH-1 already gives the quality 'paid trial: 3 months for $1/month' |
| The store selection's trial: '3 days free, then $1/mo for 3 months' | `20261005T115840Z-journey-organization/steps/033.text.txt`, line 4 | CM-PLN-001 |
| The subscribe checkout's domain offer: 'Includes domain offer', 'Earn $20 USD in subscription credits toward future bills when you buy or connect a domain. Terms apply' | `20261005T115840Z-journey-organization/steps/034.text.txt`, lines 10 and 11 | CM-SFR-008 (domains) and CM-PLN-001, a credit toward the plan's bills |
| The subscribe checkout's renewal: 'Renews Jan 6, 2027 on Basic plan, $27/mo + tax. Cancel before 3-day free trial ends to avoid charges.' | `20261005T115840Z-journey-organization/steps/034.text.txt`, line 28 | CM-PLN-002 |
| The setup the answers tailored: after every choice was chosen, the new store's home shows 'Help me get started', 'Import your product catalog' and 'Add your first digital product' | `20261006T232216Z-journey-signup-new-account/steps/018.text.txt`, lines 34, 37 and 40 | CM-ONB-004's setup tasks, with CM-MIG-001 and CM-SEL-002, unless the admin's setup structures already hold them |
| The storefront agent's analytics: the schemas `consumer_agent_messages` and `consumer_agent_sessions` (conversation turns, assisted sessions, 'Number of distinct orders placed in sessions where the Storefront Agent provided assistance') | `raw/runs/20261007T030938Z-journey-sidekick/answers/admin.shopify.com/AnalyticsSchemas/827dd3e0aad122d77c02c472c7b1aff923639ddcc1133381ab01eb89086b7693.json` | the analytics capabilities and CM-SUP-004 (R100.3) |
| A storefront password page: the theme's Password template, with nothing held stating what sets the password | the picker | CM-ACC-007, whose note says no Shopify statement holds a storefront password setting, and CM-ACC-009, private mode |

## The checker's lines, and what I decided

- **CHANGES, CM-ONB-004@shopify becomes held and gains `core`, by lines 13, 15, 17, 19, 21 and 31.** These are the five choices and `signup:store-details`. I read each again against its step. The question 'What can we help you do?' says the platform tailors the setup to the answers, and the new store's home after them shows the setup's tasks (`018.text.txt`). That is CM-ONB-004's onboarding profile, the onboarding question its note names. Kept. Earlier batches already place the setup guide on CM-ONB-004 `core` (SH-80's line 41, among others), so the change isn't these lines' alone.
- **NOTE, containers:**
  - `optional-checkout:index` (line 24) is a container whose own loader redirects: `shows` on its target (R14.4).
  - `signup:subscribe:layout` (line 29) and `signup:subscribe:root` (line 30) are on CM-PLN-001 by their id, with their children named in `reading`.
  - `signup` (line 36) is on CM-ACC-001 by its id, with its children named.

  Kept.
- **NOTE, lines 55 and 69, the first lead CM-SFR-016 (social sharing).** It comes by the words 'button' and 'product', which every button of the structure holds. It is no lead, and the entries aren't its thing.

## Problems with the brief or the scripts

- **The router digest assumes the admin router.** Its rule 4 takes a route's full address from `index/ledger/admin-route.tsv`, and rule 23 takes ancestors' gates from `held_router_gates.py`. Neither reaches the sign-up app, as R100.6 to R100.11 say. The digest's rules on reading, support and containers carry over.
- **`held_entries.py show` drops a JSON `null`.** It dropped `exceeded_at` from the Sidekick entry. A null is a statement too, here that the limit wasn't exceeded.
- **The checker's first-lead note** (CM-SFR-016) comes by words every entry of a structure holds. The brief already says such a lead is none.

## The coordinator's check

Measured: 20.2 million tokens over 101 requests, about 331,000 an entry, five structures' first rules in one batch. The checker prints no problem.
- **Kept:** R100.1 to R100.14 and the `CHANGES` line on CM-ONB-004, which SH-80's setup guide also holds.
- **The storefront agent's quota on CM-SUP-004 `shows`:** it agrees with SH-47's line, which put the storefront agent on CM-SUP-004 with Shopify Inbox (`own-service`); a quota only shows the agent exists for the store, so `shows` stands.
- **The open entries** (the quota's scope, the decision index and the catch-all, the steps no run opened): kept as placed, each a marked reading. `sidekick-quotas`, `sign-in-methods`, `signup-onboarding-questions`, `signup-router` and `theme-editor-templates` are placed whole.
