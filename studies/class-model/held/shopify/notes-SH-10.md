# SH-10: Shopify's admin router, 84 entries of Capital, Cards, Catalogs, Checkout and Collections (notes)

**What this batch is.** The third held-pass batch on `admin-router`, after SH-8 and SH-9. Its 84 entries are the manifest's items at lines 284 to 377 of `structures/shopify/admin-router/items.jsonl` (observed-sh at `e38dc17e3`), less the routes the concern map already cites (`capital:access-account`, SH-S-5096; `capital:root`, SH-S-5097; `cards:section`, SH-S-5098; `cards:unlock:update`, SH-S-5099; `catalog:parent`, SH-S-5101; `checkout-accounts-editor`, SH-S-5103; `checkout-settings:customizations-report:list`, SH-S-5105; `checkout-settings`, SH-S-5106; `collections:root`). They come from five sections: Capital (46), Cards (13), Catalogs (4), Checkout (12) and Collections (9).

- **Entries:** 84. 82 are placed on capabilities alone, 1 also takes a `new` line (SH-E-330a0296, Settings > Checkout, for its anchor Tipping), and 1 is `out` (SH-E-e26fc9c2, a catch-all).
- **Lines:** 94, since five entries take two lines and one takes seven (Settings > Checkout's title and anchors). By support: 79 `core` (one of them the `new` line), 4 `core;extension-point`, 4 `extension-point`, 6 `shows` and the `out` line.
- **The checker's last run:** no problem; two `CHANGES` lines, both from documented intents (section 4); one `NEW` line (Tipping).
- **`held_entries.py earlier`** printed no earlier line for any key of the batch.
- **Ancestors' gates** aren't looked up, as the coordinator asked: no route of the batch has a store gate of its own, so every `scope` is empty. The coordinator's script names `capital:root`'s, `cards:section`'s, `catalog:parent`'s and `checkout-settings`' gates in the readings.

**What I read:**
- the brief, SH-8's and SH-9's notes with the coordinator's checks, and `review-H-rulings.md`;
- B-extent.md's "Cells and evidence" and "Conventions from the dry run"; the evidence map; `held/selection.tsv`'s three router rows;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, `REGISTER.tsv`'s router, betas and titles rows, `index/ledger-summary.tsv`, `index/ledger/admin-route.tsv` and `derived/admin-routes-resolved.tsv` (each route's joined path and visits);
- the structure's `meta.json` and `items.jsonl`, lines 281 to 377;
- `structures/shopify/admin-betas/` (both held stores), for betas a4989aa0 and e0d8659f, both `enabled: false` in `2jiwxs-gr` and `fake-demo-sharrwah`;
- `derived/intents.tsv`, and the Intents API page it joins, `raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz@14590255`;
- the run steps and actions the ledger joins to the routes, cited in the lines and in section 7;
- the cells of CM-PAY-026, CM-TRU-001, CM-TRU-002, CM-PAY-003, CM-PAY-005, CM-PAY-024, CM-B2B-003, CM-CAT-003, CM-CNT-002, CM-CHK-001, CM-CHK-003, CM-CHK-004, CM-CHK-005, CM-CHK-009, CM-CUS-007, CM-CUS-008, CM-CUS-010, CM-MKS-008 and CM-SFR-002.

## 1. Lines by capability

| Capability | Lines | Entries |
| --- | --- | --- |
| CM-PAY-026, merchant financing (Shopify Capital) | 44 `core`, 1 `shows` | the Capital section, apart from those below; the `shows` line is the information request's redirect |
| CM-PAY-024, business cards | 13 `core` | the Cards section: the card list, a card's page and its modals, Create card, Activate card |
| CM-TRU-002, identity verification | 3 `core`, 1 `shows` | Capital's profile assessment, its interview and remediation, beside CM-PAY-026, as SH-8 placed Balance's; the information request's redirect |
| CM-TRU-001, sign-in security | 1 `core` | `capital:mfaLandingPage`, two-step authentication asked before Capital's bank account page |
| CM-B2B-003, catalogs | 3 `core`, 1 `core;extension-point` | the Catalogs section; `catalog:update` with its documented intent |
| CM-CAT-003, collections | 2 `core`, 2 `core;extension-point` | the collections list and the delete modal; Add collection and Collection Details, with their documented intents |
| CM-CNT-002, custom data | 4 `core`, 1 `core;extension-point` | a collection's metafield routes; the app-controlled metafields |
| CM-CHK-003, checkout customization | 5 `core`, 2 `shows` | the checkout and accounts editor, the two Rename configuration modals, the Customizations report, the anchors Customize checkout and Order status page additional scripts; the editor's index and the customizations_report redirect |
| CM-CHK-005, cart and checkout validation | 3 `extension-point`, 1 `shows` | the anchor Checkout rules, the add and edit rule routes; the legacy rule address |
| CM-CHK-001, checkout | 1 `core` | Settings > Checkout, with its anchors Customer contact method, Customer information and Address collection preferences |
| CM-CHK-004, CM-CUS-007, CM-MKS-008 | 1 each | the anchors Post-purchase page (`extension-point`), Marketing options and Checkout language (`core`) |
| CM-SFR-002, theme editor | 1 `shows` | `checkout-settings:theme-content`, a redirect to a theme's content |
| new:Tipping | 1 `core` | SH-E-330a0296's anchor Tipping |
| out | 1 | SH-E-e26fc9c2, `checkout-settings:catch-all` |

## 2. Rules I followed for kinds of route the rules don't cover

These are for the coordinator to align with SH-11 to SH-18. Each is a reading.

- **A1. An action-only route** (its path under `api/`, an `action` and no loader or component), such as `capital:account:withdraw:api:scenario` at `capital/account/withdraw/api/withdrawal-scenario`. It is the page's endpoint: the page posts to it and it opens no page. Its path is its own and its id names a thing of the page (a withdrawal scenario, a custom offer's preview), so it isn't `out` under SH-8's 2.9. I placed it `core` on the page's capability, its reading saying it opens no page. Nine entries: SH-E-88a52912, SH-E-b0b2a2a5, SH-E-fc4abe66, SH-E-fabe6c42, SH-E-fbb318de, SH-E-87177ad2, SH-E-596f21fa, SH-E-0075523d, and the loader-only lookup SH-E-1219cd6d, which follows SH-8's 2.4. If the coordinator reads an endpoint as a field of its page (rule 3, "a field ... inside a page is never a place of its own"), these could be `shows`; no cell changes either way.
- **A2. A loader-only route that a visit shows redirecting.** SH-8's 2.4 keeps a loader-only route `core` where its names don't say redirect. Two of this batch's were seen sent elsewhere, at their own requested address (`actions.jsonl`, `target` against `url`):
  - `capital:informationRequest` (`capital/information_request`) landed on `capital/profile-assessment/remediation/capital` (`raw/runs/20261002T003931Z-sweep-capture-advanced/actions.jsonl`, step 149);
  - `checkout-editor:index` (`settings/checkout/editor`) landed on the active configuration's editor, `profiles/6459654249?page=checkout` (the same run, step 162; `raw/runs/20261005T015805Z-sweep-observe-redrive/actions.jsonl`, step 1).

  With no component, neither can show a page of its own, so I read both as redirects: `shows` on the target's capability (the ruling after SH-8). The information request's target, Capital's remediation, takes two capabilities (CM-PAY-026 and CM-TRU-002), so the redirect takes a `shows` line on each.
- **A3. An admin route where the merchant sets up a third party's extension.** `checkout-rule:create` and `checkout-rule:update` (`rules/:apiType/add/:id`, `rules/:apiType/edit/:id`) and the anchor Checkout rules. The edit page of a validation rule reads 'Block checkout if app experiences a problem' (`raw/runs/20261008T012654Z-journey-checkout-rules/steps/050.text.txt`), and the Checkout rules section reads 'There are no apps installed with rules for checkout or cart. Visit the Shopify App Store to install one.' (`derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/164.html.txt`, line 206).
  - I placed them `extension-point` on CM-CHK-005, whose cell holds `extension-point` only: apps write the rules, and the admin's pages are the platform's place for them.
  - SH-8's 2.4 makes every admin route `core`. A `core` line here would add `core` to CM-CHK-005 and claim the platform validates checkouts itself, which no held statement shows.
  - The anchor Post-purchase page (CM-CHK-004) follows the same reading, from that cell's Post-purchase UI alone, since the swept store's page shows no such section (section 5).
- **A4. A documented intent on the route's own capability.** The ruling after SH-8 gives a documented intent an `extension-point` line on the route's capability. The checker refuses a second line on one capability with the same scope and filler, so I wrote one line with `core;extension-point`, its reading giving both: `catalog:update`, `collection:create` and `collection:update`.
- **A5. A catch-all with a loader only** (`checkout-settings:catch-all`, `:catchAll/*`, `loader-catch-all`) is `out`, as SH-9's rule 3 has a not-found catch-all. It has no title, gate or resource; its id names only its role, and a splat isn't a place's own path. Unlike SH-9's, it renders no `NotFound`: its loader's work isn't stated (section 5).
- **A6. A sweep's visit matched to a route by its pattern can be another route's address.** The `20261004T092454Z-sweep-instances` run visited `checkout-settings:catch-all` and `checkout-rule:legacy` at the editor's address, `settings/checkout/editor/profiles/6459654249` (its `actions.jsonl`, steps 12 and 13), the `checkout-editor:profile` route's own address. Those visits state nothing of the two routes, and their readings say so.
- **A7. A page of one section whose words name another capability's thing** takes that capability alone (SH-8, 2.7): `capital:mfaLandingPage` on CM-TRU-001 (its 'mfa', and its page's 'Why is two-step authentication important?'), and the collection metafield routes on CM-CNT-002, not also on CM-CAT-003. The Collections section's resource `collection`, and the word Collection in their titles, say whose metafields they are; a collection's metafield isn't a kind of collection (M-6 refined).
- **A8. Metafields that apps control** (`collections:metafield:appControlled`, 'Read only collection metafields', path `app-controlled`) are `core;extension-point` on CM-CNT-002: the admin's own page, and apps keeping their data on the store's records through the platform's metafields, a reading of the path. No cell changes.
- **A9. Anchors read with the page the route opened.** Settings > Checkout's ten anchors are each placed on their own capability, and the page's text at `settings/checkout` clarifies them (`…/164.html.txt`). The three on the route's own capability, CM-CHK-001 (Customer contact method, Customer information, Address collection preferences), go in the route's line (SH-9, rule 10). Customize checkout and Order status page additional scripts share one line on CM-CHK-003, since neither has a condition of its own (the ruling after SH-34).

## 3. The new thing

**new:Tipping** (SH-E-330a0296, the anchor `tipping` of `checkout-settings:index`, at `settings/checkout/*`).
- **What it is:** the buyer's tip at checkout. The anchor's section reads 'Show tipping options at checkout' (`derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/164.html.txt`, line 186).
- **Its place of its own:** the anchor Tipping, with its own title and path, within Settings > Checkout (B-extent, "What a place of its own is": "An anchor the manifest names within a route, with its own title and path, is one"). So it is `core`.
- **Proposed domain, area and parent:** C, CHK, under CM-CHK-001, the checkout, whose settings page holds it. Its cell there holds no tip.
- **Its name:** 'Tipping', the anchor's title. Shopify's admin is held in English only (`docs/GAPS.md`: the admin in Arabic isn't held).
- **Terms searched** (`class_slice.py caps --terms`): 'tip; tipping; tips; gratuity'. They found nothing. CM-CHK-001, CM-CHK-004, CM-CUS-010, CM-PAY-014 and CM-PAY-022, the leads of the entry, hold no tip: the last four are leads of other anchors, or word leads ('address', 'checkout', 'method').
- **A lead for the coordinator:** a POS tip, if another batch holds one, may be the same thing at the counter.

## 4. The `CHANGES` lines

- **CM-B2B-003@shopify gains `extension-point`** (SH-E-15f4ca1c, `catalog:update`). Its intent, `edit shopify/Catalog`, release `public`, is joined by `derived/intents.tsv` to shopify.dev's Intents API pages. Their table has the row `edit` `shopify/Catalog`, and the page states 'When your extension calls an intent, merchants complete their changes using the standard Shopify admin UI, and your app receives the result.' (`raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz@14590255`). Kept: an app opens the catalog's page through the platform's interface, by the ruling after SH-8.
- **CM-CAT-003@shopify gains `extension-point`** (SH-E-fac9f8eb, `collection:create`; SH-E-35bb1f42, `collection:update`). The same page's table holds `create` and `edit` for `shopify/Collection`, and its use cases begin 'Invoke admin workflows to create products, collections, discounts, or other Shopify resources.' Kept, for the same reason.
- **What the coordinator may weigh:** the intent lets an app open the admin's own form, where the merchant does the work. So the `extension-point` shows an interface apps use to open the page, not third parties keeping catalogs or collections. That is how the ruling reads it, and the readings say so.

## 5. Entries I couldn't tell, and what would settle each

- **SH-E-0f063d2f, `capital:informationRequest`.** Placed `shows` on CM-TRU-002 and CM-PAY-026, as a redirect to Capital's remediation (A2). Only one store's visit was read, and its remediation answered 'There's no page at this address' (`…/149.html.txt`). Settled by a store with an open Capital information request.
- **SH-E-330a0296's anchor Post-purchase page** is `extension-point` on CM-CHK-004, a reading of that cell's Post-purchase UI. The swept store's checkout page shows no Post-purchase section (`…/164.html.txt`). If the section offers a page of Shopify's own, its line is `core`. Settled by the section's text on a store with a post-purchase app, or the admin's UI strings (REGISTER: `shopify/admin-ui-copy`, backlogged).
- **SH-E-330a0296's anchor Order status page additional scripts** is on CM-CHK-003, as a customization of a checkout page. CM-MKT-009 (customer events and tracking pixels) is the other candidate, if the scripts are for tracking; the page doesn't say. Settled by the section's text, which the swept store's page doesn't show.
- **SH-E-330a0296's anchor Address collection preferences** is in CM-CHK-001's line. CM-CUS-008 (customer addresses) is the other candidate: its name holds Salla's Shipping addresses settings, a setting of how addresses are collected. Its note puts the order's shipping address elsewhere, and the anchor reads 'Manage how you collect shipping and billing addresses' at checkout, so I kept it with the checkout.
- **SH-E-330a0296's anchor Customer information** is in CM-CHK-001's line. The page lists Full name, Company name, Address line 2 and Shipping address phone number, each required, optional or left out (`…/164.html.txt`, lines 157 to 165). CM-CHK-009 (order options and custom fields) holds nothing on Shopify, and its reading leaves 'Editing the checkout form options' (SH-I-2107) uncited for want of a statement saying what they are. The anchor and its page are such a statement, but they configure the checkout's own fields; they add none. If the coordinator reads CM-CHK-009 as covering the checkout form's options, this anchor is its first Shopify evidence.
- **SH-E-c0814ef2, `checkout-settings:theme-content`,** is `shows` on CM-SFR-002, as a redirect to a theme's content (its names). CM-MKS-008 is the other candidate, if the content is the theme's translations: the Checkout language section offers 'Edit checkout content'. No run opened the route.
- **SH-E-0eb489f6, `checkout-settings:scripts-report:list`** ('Customizations report'), is `core` on CM-CHK-003. Its visit answered 'There's no page at this address' (`…/165.html.txt`). The concern map places another route, `customizations-report`, which the `customizations_report` redirect reached ('Upgrade guide'), `extension-point` on CM-CHK-003, as apps' customizations (SH-S-5105). What this one reports isn't stated.
- **SH-E-e26fc9c2, `checkout-settings:catch-all`,** is `out` (A5). If its loader redirects sub-addresses of Settings > Checkout, it would be `shows` on CM-CHK-001. Settled by a visit at its own address.
- **SH-E-057f8818, `capital:bankAccountDetails`** ('Bank account'), is on CM-PAY-026, as the Capital section's bank account (a reading of its place). Whether Capital pays into it or debits it isn't stated. It isn't CM-PAY-005's payout bank account, nor CM-PAY-030's bank transfer.
- **SH-E-1cdf4309 and SH-E-03cc6717, the PAD routes,** read 'pad' as a pre-authorized debit, as CM-PAY-026's Canada's pre-authorized debit agreement. That is a reading of the abbreviation: the routes state no country, so no scope.
- **SH-E-ed97aa15, `capital:flex-sales-breakdown`:** what 'flex' names isn't stated. The Capital account's routes (request funds, change the repayment rate) read as a financing drawn and repaid from sales, which is CM-PAY-026's thing. A Capital product of its own, if 'flex' names one, would be a lead for a child capability.

## 6. The checker's `NOTE` lines, answered

- **Containers.** Lines 4, 5, 6, 13, 17, 22, 33, 41, 52, 53, 70, 72 and 90 are routes with children. Each is placed on the capability its title or words name, `core`, its children named in its reading (SH-8, 2.6). None names only a grouping.
- **Line 66: 'path :id begins 6 other entries' paths'.** A false match, as SH-9's section 5 found: the checker compares relative paths. `catalog:update`'s `:id` is `catalogs/:id`; the matches are `catalogs/:id/editor` and `catalogs/:id/changesets/…` (its siblings, so it is a container by its path alone) and the collections' `:id/metafields/…`, under another parent.
- **Line 93: 'path :id/metafields begins 3 other entries' paths'.** `collections:metafield:create` (`collections/:id/metafields`) begins its siblings' paths (`…/app-controlled`, `…/unstructured`, `…/:namespace/:key`). It is a container by its path alone, and keeps its line.
- **Lines 29 and 31: 'core on a product named with the platform's brand'.** 'Shopify Capital' and 'Shopify Capital Amendment' are the titles of the admin's own routes. They are `core` because they are routes, not on any maker; no `own-service` is claimed. CM-PAY-026's `own-service` rests on its help pages' maker statements (SH-S-0484, SH-S-0491, SH-S-0493), not on these.
- **Line 72: 'a new thing whose entry has leads'.** Answered in section 3.

## 7. What sources state that no entry holds, for the second stage

These are run steps the ledger joins to this batch's routes, and one key of an item that the selection drops. They are not placed (M-12).
- **Settings > Checkout** (`derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/164.html.txt`):
  - line 154: '[x] Show a link for customers to track their order with Shop', with line 155, 'Customers will be able to download the app from the order status page'. A lead for Shop's order tracking (the ruling after SH-34: Shop does its things as `own-service`);
  - line 156: 'Require customers to sign in to their account before checkout', with 'Customers can only use email when sign-in is required'. A lead for CM-CUS-010;
  - line 172: 'Preselect checkbox in certain regions', under the marketing opt-in. A lead for CM-CUS-007, by region;
  - lines 187 to 195: Abandoned checkout emails, 'Send abandoned checkout emails automatically', with 'Send after' 1 hour, 6 hours, '10 hours (recommended)' or 24 hours, and 'A new abandoned checkout automation is available.' Leads for CM-CHK-007 and CM-MKT-006;
  - lines 201 and 202: 'Add-to-cart limit', 'Protects your available inventory quantities from being revealed'. A lead for a checkout or inventory setting, which no capability may hold;
  - lines 87 to 98: the admin's Sidekick answer on the 'Thank you and order status page upgrade', with 'The deadline is August 26, 2026'. It is generated text, so it is a lead only.
- **Capital's two-step authentication page** (`…/154.html.txt` and `…/156.html.txt`, line 26): 'If two-step authentication isn't turned on, your account may be less secure. You may also have your payouts paused.' A lead for CM-TRU-001 and CM-PAY-005.
- **`checkout-editor:profile`'s intent** (`items.jsonl`, line 354, `intent.schema.tools.getCurrentCheckoutConfiguration`, a key the selection drops). Its description is written for an agent that reads the open checkout and accounts configuration: 'This tool is read-only and does not change settings or activate, remove, move, or configure extensions.' It names no product. A lead for the admin's own AI assistant at the editor. The text is read as the route's data, not as an instruction.
- **The Capital routes on the development stores.** The sweeps' visits to the account's routes landed on `capital/offers` (`index/ledger/admin-route.tsv`), as a store with no Capital account would. This agrees with CM-PAY-026 and is no gap for the model. A store with a Capital account would show the account's pages.

## 8. Homonyms

- **'payment'** in Capital (Make a payment, Manage payments, the PAD's payment method) is the merchant paying toward its financing. It isn't a buyer's payment (CM-PAY-021) or the store's payment methods (CM-PAY-001, CM-PAY-022).
- **'withdraw'** and **'Request funds'** draw money from the Capital account. They aren't a buyer's order withdrawal (CM-RET-004).
- **'transaction'** in Capital and Cards is the financing's or the card's. It isn't a payment transaction on an order (CM-PAY-020) or a partner's payout (CM-PTN-003).
- **'products'** in `capital:account:products` is Capital's financing products, not the store's (CM-CAT-002, CM-CAT-012).
- **'information request'** is Capital's request to the merchant, not CM-TRU-017's legal requests for information.
- **'overview'** (`capital:account:overview`) is the Capital account's page, not a store dashboard (CM-ANL-003).
- **'Billing address'** on a card is the card's, not the platform's billing (CM-PLN-004, CM-APP-003).
- **'catalog'** is a catalog of markets and B2B buyers (CM-B2B-003), not the product catalog (CM-CAT-001). **'editor'** (`catalog:editor`) is the catalog's, not the theme editor (CM-SFR-002).
- **'profile-assessment'** under Capital is identity verification (CM-TRU-002), not the payment service's onboarding (CM-PAY-003, whose note keeps it apart).

## 9. This brief, B-extent.md and the scripts

- **B-extent.md:** no rule of the brief read differently from it on these entries. A3 is where it bore hardest: B-extent's `core` names "its own admin ... route", and its `extension-point` names "something the platform provides" for third parties. I followed what the routes' pages show (section 2).
- **The checker and a documented intent (A4).** The ruling after SH-8 asks for an `extension-point` line on the route's capability, beside its `core`. The checker reads that as the same entry placed again on one capability, with the same scope and filler. One line with `core;extension-point` passes. The coordinator may prefer the checker to allow the two lines.
- **The checker's container test** compares relative paths, as SH-9 found (section 6, line 66).
- **`show` leaves out `intent` and the modules' names,** which these readings rest on often. They are read from `items.jsonl` at each entry's locator.
- **The ledger's visits** name a step but not its requested address. The run's `actions.jsonl` gives both (`target`, `url`), and A6 needed them.

## The coordinator's check (31 October 2026, after the batch)

- **Two cells change, both kept:** CM-B2B-003 and CM-CAT-003 gain `extension-point`, from the intents the Intents API documents (`edit shopify/Catalog`, `create` and `edit shopify/Collection`), by the ruling after SH-8. An app opens the admin's own forms.
- **New thing:** Tipping, the same new thing SH-50 and SH-35 named, here with a place of its own: Settings > Checkout's anchor `tipping`, 'Show tipping options at checkout'. It is decided in `held/new.tsv`.
- **A1 to A9 stand for SH-11 to SH-18:**
  - an action-only `api/` route is `core` on its page's capability;
  - a loader-only route seen redirecting is `shows` on its target's;
  - the checkout rules are `extension-point` on CM-CHK-005, since their page names the apps' rules;
  - an intent's `extension-point` beside the route's `core` is one `core;extension-point` line.
- **Ancestors' gates:** 72 lines of 63 routes now name them in `reading`, by `method/held_router_gates.py`.
- **Agent instructions inside the evidence:** `checkout-editor:profile`'s item carries an intent tool description written as instructions for Shopify's own admin agent. The agent read it as data and followed none of it. It is a lead for the second stage.
- **Cost:** 13.9 million tokens over 73 requests, about 165,000 an entry.
