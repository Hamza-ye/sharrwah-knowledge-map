# SH-13: Shopify's admin router, 84 entries of Flow, GiftCards, Growth, Intents, Inventory, Listings, Location and Marketing (notes)

**What this batch is.** The router's sixth batch, items 617 to 731 of `structures/shopify/admin-router/items.jsonl` (the routes the concern map doesn't already cite). SH-8 to SH-12 ran before it, and their rules, with the coordinator's checks and the rulings after them (`held/review-H-rulings.md`, its last section), are the ones these lines follow. SH-14 to SH-18 may run beside it.

- **Entries:** 84, from eight sections: Flow (1), GiftCards (2), Growth (27), Intents (1), Inventory (15), Listings (7), Location (8) and Marketing (23).
- **Placements:** 84 `capability`, no `new`, no `out`. 90 lines, since six entries take two lines.
- **By support, counting each entry of a line:** 66 `core`, 21 `shows` (redirects, and two routes behind a beta), 18 `extension-point` (documented intents, apps' extensions, app-controlled metafields, an ad platform's account), 1 `own-service` (Shopify Flow).
- **The checker's last run:** no problem; two `CHANGES` lines (section 4).
- **What I read:** the brief and what it names; observed-sh at `e38dc17e3` (its `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, `REGISTER.tsv`'s router rows, `index/ledger-summary.tsv` and `index/ledger/admin-route.tsv`); the structure's `meta.json`, `items.jsonl` and `source.jsonl`; `derived/intents.tsv`; `structures/shopify/admin-betas/` (both held stores); and the step texts the ledger names, listed in the lines' readings.

## 1. Lines by capability

| Capability | Lines | What they are |
| --- | --- | --- |
| CM-MKT-005 Marketing campaigns and activities | 25 | Growth's overview, its marketing container, Campaigns and a campaign's pages and modals, Marketing app activities and their extension routes, in both Growth and the legacy Marketing addresses; two redirects to Growth's overview |
| CM-MKT-006 Marketing automations | 17 | Campaign Autopilot, its Store configuration, Defaults and Playbook; the automations' create and update routes; the automations containers; eight redirects, four of them seen landing on the Shopify Messaging app's automations or templates |
| CM-MKT-008 Sales attribution | 6 | The Attribution reports (channels, campaigns, Organic Marketing Reports), in both sections |
| CM-MKT-010 Advertising on ad platforms | 2 | Growth's sign-in pages for connecting an ad platform's account (`extension-point`) |
| CM-INV-001, CM-INV-002, CM-INV-003, CM-INV-006, CM-INV-007 | 11 | Inventory, an inventory movement, an item's history, stock counts behind beta 4d3efaac (`shows`), a transfer, its shipments, a purchase order and a supplier |
| CM-INV-005 Inventory locations | 4 | Settings > Locations, Add location, a location and its container |
| CM-CNT-002 Custom data | 8 | Transfer and location metafield lists and their containers |
| CM-CHN-004 Product listings and feeds | 7 | Shopify Catalog Mapping, its two endpoints, and four redirects |
| CM-AIA-005 Agentic commerce | 4 | Shopify Catalog Mapping's Shopify Catalog, and three redirects to it |
| CM-LOY-002 Gift cards | 2 | The list and a gift card's page |
| CM-AUT-001 Workflow automation | 3 | Flow's custom configuration page (`own-service`); two automation-summary redirects whose words name a flow (`shows`) |
| CM-APP-006 App UI in the admin | 1 | The intents host `intents:render` |

## 2. Rules I followed for kinds of route the rules don't cover

These are for the coordinator to align with SH-14 to SH-18. Each is a reading.

- **D1. A legacy address sent on by its parent's redirect loader.** The Marketing section's routes (`marketing:channels`, `marketing:activities`, `marketing:integrated-campaigns` and the rest) are Growth's pages again, at `marketing/…`, each with its own loader and component, the same modules as Growth's. Their parent `marketing` (cited by CM-MKT-005) loads `growth-section-redirect-loader`, and six stores' sweeps of each were sent on to the `growth/…` twin (`index/ledger/admin-route.tsv`). By SH-8's 2.4 they aren't redirect-only (no `redirect` key, and neither their own loader nor their component is named for one), and SH-10's A2 covers loader-only routes. So I kept them `core` on their twins' capabilities, the redirect named in `reading`. The other reading is `shows` on the twin's capability. The capabilities are the same, so no cell changes either way.
- **D2. An `eligibilityMatch` whose alternative is a redirect.** `growth:autopilot` and `growth-configuration` carry `eligibilityMatch: [{eligibility: {excluded: {features: [growthAgentEnabled]}}, redirect: /growth}]`: where the store lacks that feature, the page sends the request to Growth's overview. It acts as a gate. SH-8's 2.5 says an `eligibilityMatch` gates nothing, so I named it in `reading`. The coordinator may prefer `growthAgentEnabled` as the scope.
- **D3. A redirect whose target page takes two lines** takes a `shows` line on each, as SH-10's A2 did for Capital's remediation. That covers the three redirects to Shopify Catalog Mapping (CM-CHN-004 and CM-AIA-005).
- **D4. A redirect whose own words name a thing its held target doesn't.**
  - `marketing:automation-summary:flows` (`automations/flows`) was sent to the Shopify Messaging app's automation templates. I put it on the target's capability alone (SH-11's B4), CM-MKT-006, and named 'flows' in `reading`.
  - Where no run shows the target (`growth:automation-summary:flow` and `marketing:automation-summary:flow`, at `automations/flows/:automationId`), I read the target from the route's words (SH-11's B1). That gives CM-MKT-006 and CM-AUT-001, both `shows`.
- **D5. An id and a loader named for a redirect, beside a component not named for a page.** `growth:automations:redirect` (`automations/:extensionId`, `extension-redirect-loader`, `AutomationExtensionRoute`) is `shows`. SH-12's C3 keeps `core` where the component is a page's, with a form and an action (`DiscountDetails`). Here the id itself says redirect, and the legacy twin at the same path, `marketing:automations:update`, renders the `Activities` page instead. No run opened it.
- **D6. Action-only routes outside `api/`.** Shopify Catalog Mapping's `update-metafield-filter-status/:metafieldDefinitionId` and `update-metaobject-filter-status/…` have an action and no loader or component. I placed them by SH-10's A1, `core` on the page's capability. I used CM-CHN-004 alone, since their words name a setting of the mapping, not the catalog.
- **D7. A `oneOf` whose store gates are a flag and its exclusion.** `purchaseOrder:view` holds with the organization flag a07955ff and VIEW_INVENTORY_PURCHASE_ORDERS, or without the flag and with PRODUCTS. I wrote the scope as the source states it, `a07955ff;not a07955ff` (SH-8's 2.5). Read together, the alternatives hold on every store: the flag decides only which staff permission the route asks. The coordinator may prefer an empty scope, with the flag in `reading`.
- **D8. A sign-in page for connecting an ad platform's account.**
  - `growth:oauth-provider-selection`, 'Choose sign-in method', reads 'Choose how to connect your Microsoft Advertising account.' (capture-advanced step 558).
  - `growth:oauth-return`, 'Connected successfully', is where that sign-in returns. Opened with no answer, it sent six stores' visits on to `growth`.
  - I placed both `extension-point` on CM-MKT-010, as SH-10's A3 places the admin's pages for setting up a third party's thing. That cell holds only `extension-point`.
  - The provider is known only from the run step, so it is in `reading`, not `filler`.
  - The other reading puts them under Campaign Autopilot's channels (CM-MKT-006), since Growth's overview says 'Campaign Autopilot promotes your products across top channels' (section 6).
- **D9. A first-party app's route in the admin's own router.** `flow-custom-configuration-page` (`flow/custom_configuration_page/:workflowId/:stepId`, section Flow) is the configuration page of a workflow's step in Shopify Flow. The cell says Flow 'is installed from the Shopify App Store' (SH-S-0753), and held posts name Shopify as Flow's maker. So I placed it `own-service`, by the ruling after SH-55 (section 4).
- **D10. Two versions of one section.** Growth (`growth/…`) and the legacy Marketing (`marketing/…`) hold the same pages with the same modules. Each pair is placed alike, except where their own modules differ: D5's `automations/:extensionId`.

## 3. The new things

None. Every entry's thing is a capability the model holds. Searched for things the leads didn't settle (`class_slice.py caps --terms`):
- 'custom configuration; configuration page; playbook; autopilot; utm; oauth; sign-in method; organic; tactic; marketing activit; marketing app';
- 'advertis; ad account; ads; Meta Ads; Microsoft; Google Ads; paid ads; ad campaign; Shop Campaigns; retargeting; connect account';
- 'Shopify Catalog; catalog mapping; agentic; AI shopping; intent; intents'.

## 4. The `CHANGES` lines

- **CM-AUT-001 gains `own-service`, by line 2** (`flow-custom-configuration-page`). Kept, by the ruling after SH-55, which aligned Flow's lines to `own-service`.
  - The maker statements: “We’ve added a new trigger to Shopify Flow for when subscription contracts are created.” (SH-E-aca9896c) and 'Today we’re introducing test runs in Shopify Flow' (SH-E-0678ff26, which SH-35 placed so).
  - SH-35's and others' lines already give this cell `own-service`, so after the amendment this line changes nothing that theirs don't.
  - Two other readings stay open (section 5): `core`, the admin's own route; or `extension-point`, where the custom page is an app's.
- **CM-MKT-006 gains `extension-point`, by lines 30, 82 and 83** (`growth:automations:create`, `marketing:automations:create`, `marketing:automations:update`). Kept.
  - Their path's `:extensionId` names an extension. They render the same `Activities` page as the marketing activities' routes, whose list is titled 'Marketing app activities'.
  - The post of March 5, 2026 names 'Automations that have marketing activities from other apps' (SH-E-42ecf1fa). SH-35 already placed that post `core;extension-point` on CM-MKT-006, so this agrees with a held line.

## 5. Entries I couldn't tell, and what would settle each

- **`flow-custom-configuration-page` (SH-E-f9c1276d), its support.**
  - Placed `own-service`.
  - The held post says 'Steps that use a custom configuration page, such as Send Marketing Email, can't be copied.' (SH-E-699b03b8), as the Help Center's workflow editor page does.
  - shopify.dev's navigation lists 'Build a configuration page' under apps' marketing automations (`structures/shopify/dev-docs-nav/shopify.dev@2026-10-07/items.jsonl`). That suggests apps supply such pages, which would make the route the admin's host for an app's page: `extension-point`, or CM-APP-006's `core`, as SH-12's C6 places the hosts.
  - What would settle it: a visit to the route on a workflow with such a step, which no run made (needs an instance).
- **`growth:automations:redirect` (SH-E-7b060fd9):** a redirect or a page (D5). A visit with an extension's automation id would settle it.
- **`growth:automation-summary:flow` and `marketing:automation-summary:flow`:** their targets aren't held (D4). A visit with an automation's id would settle it.
- **`growth:oauth-return` (SH-E-42f4448c):** which account's sign-in returns there. The reading rests on its sibling's page. A visit after a sign-in would settle it.
- **`inventoryMovement:preview` (SH-E-ca1ba8ed):** placed on CM-INV-001, whose cell cites its parent `inventoryMovement`. What an inventory movement is isn't stated, and `inventory_movements` wasn't rendered on six stores. If a movement is a transfer's or a shipment's, it is CM-INV-006's. A visit to an instance would settle it.
- **The two catalog mapping endpoints:** CM-CHN-004 alone, or CM-AIA-005 too (D6). No cell changes either way.

## 6. What sources state that no entry holds, for the second stage

All are in `derived/step-text-from-html/`, quoted as held:
- **Growth's overview** (`20261002T003931Z-sweep-capture-advanced/266.html.txt`, lines 27 and 29): 'Early access' and 'Campaign Autopilot promotes your products across top channels, and keeps refining the strategy while you stay in control.' That would be the platform running campaigns on third parties' channels: a lead for CM-MKT-010's own side, and for CM-MKT-006's note, 'how Autopilot relates to it, is not stated'. 'Early access' is a badge with no limit stated (the join's D1, within B-extent.md), so Autopilot's line stays `core`.
- **Campaign Autopilot** (`…/269.html.txt`, lines 28 to 52 and on), under 'Channels':
  - 'Find new customers through targeted campaigns on Facebook and Instagram Meta Ads';
  - 'Promote your products to millions of ready-to-buy shoppers in the Shop app Shop Campaigns' (CM-MKT-012);
  - 'Add Shopify Messaging to personalize abandonment automations and recover lost sales Messaging' (CM-MKT-007);
  - and the page's 'Guardrails', 'Target region:', 'Target language:', 'Permissions', 'Create campaign:' 'Always ask' and 'Set up with Sidekick'.
- **Choose sign-in method** (`…/558.html.txt`, line 28): Microsoft Advertising, a filler for CM-MKT-010 if the second stage reads the page as a statement.
- **Attribution's tactic report** (`…/272.html.txt`): five attribution models (Last non-direct click, Last click, First click, Any click, Linear) and 'A 30-day attribution window applies.', a quality of CM-MKT-008: its attribution window.
- **A campaign's page** (`20260930T140054Z-sweep-instances/035.html.txt`, lines 115 to 121): 'Shareable links', with '/?utm_campaign=f4e8f1&utm_source=shareable_link', a campaign's tracked link (CM-MKT-005 or CM-MKT-008).
- **Shopify Catalog Mapping** (`…/294.html.txt`): 'Custom combined listings', 'Bulk edit missing fields' and '14 of 15 active products missing field'.
- **Settings > Locations** (`…/295.html.txt`, lines 118 to 166):
  - 'Point of Sale subscriptions', with each location's 'POS Subscription' column and 'POS Pro Active': POS Pro by location, for CM-POS-001;
  - 'App and custom fulfillment locations', with 'Shopify Test Data' '1 location' 'App' 'Snow City Warehouse': an app's fulfillment location, for CM-INV-005.
- **Marketing app activities** (`…/273.html.txt`, line 46): 'Abandoned checkout emails by Shopify Active Sep 30, 2026', a marketing activity of Shopify's own under Online Store, a lead for abandoned-checkout recovery.

## 7. The checker's `NOTE` lines, answered

- **`own-service` on CM-AUT-001:** D9 and section 4.
- **Lines 56 and 57, `core` on a product named with the platform's brand** (Shopify Catalog Mapping, on CM-CHN-004 and CM-AIA-005). The Shopify Catalog is the platform's own catalog, in the admin's own section Listings, and no separate app. Held lines place it `core`: 'Introducing Shopify Catalog, Shopify’s global product catalog' (SH-E-0a7c8504), and the mapping's Compare-at setting (SH-E-92dbfbaf). So it is `core` by what the entry shows.
- **Containers.**
  - **By their children, each with the children named in `reading`:**
    - `growth:integrated-campaigns:campaignId` and `marketing:integrated-campaigns:campaignId`, with their modals (SH-12's C9);
    - `inventoryTransfer:shipment`;
    - `mappings:shopify-catalog-mapping`, with its two endpoints;
    - `location:parent` and `location:metafields:parent`;
    - `growth:marketing`, `growth-configuration`, `marketing:integrated-campaigns`, `marketing:automations:parent` and `marketing:automation-summary:parent`.
  - **By their path alone** (`activities`, `auto-match`, `activities/:extensionId`, `automations`, `automations/:extensionId`, `:id`, `:id/metafields`): the routes whose paths they begin are their siblings, and each keeps its own support (SH-8's 2.6).

## 8. Item text that reads as instructions

Several intents carry tool descriptions written for Shopify's own admin agent, as SH-10 to SH-12 found. I read them as the routes' data and followed none.
- `growth:autopilot` (`items.jsonl`, line 632): 'Fetches pending actions for a playbook that require merchant approval.' and 'Approve or dismiss a pending playbook action by its ID.', with `updateForm` and `getFormValues`.
- `purchaseOrder:view` (line 663) tells its reader how to write an identifier: 'A purchase order route identifier. Accepts a bare ID or a Shopify purchase order GID such as gid://shopify/InventoryPurchaseOrder/... or gid://shopify/PurchaseOrder/...'.
- `mappings:shopify-catalog-mapping` (line 695) has `openViewProductsModal`, `getCatalogMappingSuggestionContext` ('… so Sidekick can explain them. Read-only; does not accept or change anything') and `focusCatalogMappingSuggestion`. They name Sidekick, the admin's assistant, as their reader.
- `updateForm` ('Update forms on the page with the given data') and `getFormValues` are also on:
  - `inventorySupplier:create`, `inventoryTransfer:editShipment` and `inventoryTransfer:receiveShipment`;
  - `products:inventory:counts:view` and `:perform`;
  - the anchor Default location of `location:list`;
  - `location:new` and `location:details`.

## 9. Homonyms

- **'shopify catalog':** CM-B2B-003's Catalogs (B2B price lists) were a lead by the word for Shopify Catalog Mapping. The Shopify Catalog is the catalog for agentic storefronts.
- **'growth':** CM-PLN-001, the plan Grow, was a lead by the word only, on every Growth route.
- **'editor':** CM-SFR-002, the theme editor, was a lead for an app's activity editor.
- **'oauth' and 'sign-in':**
  - CM-API-002's leads (app authorization) are by 'oauth' only;
  - CM-CUS-010's and CM-CUS-011's (the buyer's sign-in) are by 'sign-in' only;
  - CM-TRU-001's (the admin's sign-in methods) are by 'sign-in method' only.
  - None of them is connecting an ad account.
- **'Store configuration':** Campaign Autopilot's configuration, not the store's details.
- **'status':** CM-OPS-004 and CM-ORD-015 were leads by the word, for the mapping's filter status.
- **'Automations':** Growth's automations are marketing automations (CM-MKT-006). Flow's workflows (CM-AUT-001) take a line only where a route's own words name a flow.

## 10. This brief, B-extent.md and the scripts

- **The checker's quote lookup** doesn't follow an entry id (`SH-E-…`) to its text. A quote from another held entry, such as a changelog post, passed only once the reading named the structure's file (`structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl`).
- **Cost:** this batch read its chunks once each, with the lookups batched. Its context stayed under the brief's limit.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 84 of 84 entries, no problem.
- **Ancestors' gates:** 21 lines of 20 routes now name them in `reading`, by `method/held_router_gates.py`.
- **Two changes:**
  - **`flow-custom-configuration-page` is `extension-point` on CM-AUT-001, with a CM-APP-006 `core` line,** not `own-service`. The page is one an app supplies for its own Flow step: shopify.dev's 'Build a configuration page' stands under apps' marketing automations, and a held post names steps that use one, such as Send Marketing Email (SH-E-699b03b8). The route is the admin's host for that page, as SH-12's C6 places the hosts. Flow's own features stay `own-service` elsewhere.
  - **D7's scope is cleared.** `a07955ff;not a07955ff` holds on every store, its two alternatives each other's negation, so `purchaseOrder:view` takes no scope (SH-4's S1).
- **The other cell change stands:** CM-MKT-006 gains `extension-point` from the automations' routes over apps' marketing activities, as SH-35 placed them.
- **D1 to D10 stand for SH-14 to SH-18,** with D7 as above. D2's redirecting `eligibilityMatch` stays in `reading`, as SH-8's 2.5 has it.
- **Agent instructions inside the evidence:** Autopilot's playbook tools, the purchase order's GID guide, Catalog Mapping's tools written 'so Sidekick can explain them', and `updateForm` and `getFormValues`. The agent read them as data and followed none.
- **Cost:** 14.7 million tokens over 75 requests, about 175,000 an entry. The context reached about 345,000 tokens.
