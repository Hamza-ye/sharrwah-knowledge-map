# SH-65: notes

**What this batch is.** 81 entries of Shopify's `editions-page-data` (observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`):
- the Winter 2026 Edition's Developer collection, 'A completely new way to build for commerce with the power of AI.', its sections Platform + Tools (entries 1 to 16, its list `text-list-5`) and Storefronts + Extensions (17 to 44, its list `text-list-2`); neither section has a description of its own;
- the Spring 2026 Edition's Agentic collection, 'The only platform you need to be in every AI channel', its sections Discovery (45 to 48) and Development (49 to 55);
- its Sidekick collection, with no description (56 to 64);
- its Online collection's section Online store (65 to 81).

**What I read.** The brief, the digest `held/rules/editions-page-data.md` whole (its section 6 included), the last section of `held/review-H-rulings.md`, observed-sh's guides and its register and selection rows for the structure. Of the batches' notes, only `notes-SH-61.md` for E90 (a separate tool at its own site) and E95 (each place the card names), and a grep of `notes-SH-53.md` for E23. For the earlier lines I used `earlier`, `makers` and greps of the placements files; each line I kept to is named in its reading.

**Pages read beyond the cards' own text,** each only where the card left its capability or support open (all cited in the readings):
- `derived/intents.meta.json` (observed-sh): the Intents API's held pages are under `app-home`, `admin-extensions`, `app-home-ui-extension` and `customer-account-ui-extensions` (SH-E-376afaab);
- `raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz@26254944`: the page the new code editor card links, titled 'Shopify Liquid VS Code extension' (SH-E-43f98b7e);
- `raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz@23889545`: Nested cart lines, 'Your app can create nested relationships using Shopify's Cart APIs and Checkout UI extension API. Shopify renders these relationships throughout the buyer and merchant journey' (SH-E-8953e070);
- `raw/runs/20261004T193247Z-shopify-dev-agents-md/fetch.warc.gz@24908`: agents/catalog, its section Promoted placements (SH-E-e1827630);
- the merchant changelog's post 'Customer accounts get a design uplift' (`merchant-changelog/changelog.shopify.com@posts/items.jsonl`, position 87, the entry SH-E-ba79302c), which the Refreshed customer accounts card links (SH-E-7c6690f2).

## Count

- 81 entries in 141 lines: 139 on capabilities, 2 `new`, none `out`.
- By entry: 79 on capabilities only; SH-E-0c55a64f `new` only; SH-E-e1827630 `new` plus a CM-AIA-005 line.
- Supports: `core` 87, `extension-point` 32, `core;extension-point` 8, `shows` 6, `own-service` 6, `extension-point;shows` 1, `own-service;extension-point` 1.

## New things

**`new:Tangle`** (SH-E-0c55a64f, Winter 2026, Developer, Platform + Tools, 'Introducing Tangle').
- What it states: 'Build ML and data pipelines collaboratively with an open-source experimentation platform that comes with a powerful visual editor.', its CTA to tangleml.com.
- `shows`: a separate tool at its own site with no maker held (`makers`: none; E90).
- No place of its own: the card and an outside site, no route, section, API group, plan line or category.
- No capability holds it. Searched: pipeline, experimentation, data science, machine learning, visual editor, testing. It isn't a tool for building apps and themes, CM-DVT-001's thing.
- Proposed: domain F, under CM-DVT-001 if kept. The coordinator may rather find it `out`: like the Shopify Keyboard (the digest's rule 57), it is something Shopify offers that the store doesn't use. Rule 57 lists only things that state no feature, so I didn't write `out`.
- English only, as all the Editions are.

**`new:Sponsored products`** (SH-E-e1827630, Spring 2026, Agentic, Development, 'Sponsored products with Catalog API').
- What it states: 'Earn revenue on sales made in your agentic experiences with Catalog API. Developer preview coming soon.'
- Its link opens agents/catalog#earn-with-paid-placements. That page's section Promoted placements says they 'let approved developers request paid placements in Global Catalog responses and earn commission on eligible attributed purchases'.
- `shows`: coming soon (the digest's rule 32).
- No place of its own: an anchor of a docs page. Its own page, shopify.dev/docs/agents/catalog/promoted-placement, which the section links, may be held (not read).
- Searched: sponsored, paid placement, affiliate, advertising, ads.
- The candidates:
  - CM-MKT-012, Shop Campaigns, 'an ads program' charged per conversion that runs on 'optional third-party placements' (its cell). It would be that capability's thing only if a held statement ties promoted placements to Shop Campaigns, and none I read does.
  - CM-AIA-005, where the entry's second line stands.
- Proposed: domain D or F, under CM-MKT-012 or CM-AIA-005. English only.

## Rules followed where the digest doesn't cover the kind (for the coordinator, from E125)

- **E125. A Dev MCP card is CM-DVT-001 `core`, and each thing of the platform the MCP now covers takes its own line, by its own support.** Shopify Dev MCP is the platform's own developer tool (the digest's rule 17), as SH-E-0d7af8a7 placed the Shopify.dev MCP Server; CM-AIA-004, a lead by 'MCP', is a homonym. What the MCP covers follows E74: Hydrogen (CM-SFR-011), the Storefront API (CM-SFR-012) and Liquid (CM-SFR-002) are `core`, and POS UI extensions (CM-POS-004) `extension-point`. The AI coding tools a card names after 'such as' (Cursor, Claude Code) are tools the developer may use, not fillers (SH-E-e66eb919).
- **E126. The Admin Intents API is CM-APP-006 `extension-point`.** The ruling after SH-8 makes the intents `extension-point` ('an app opens the admin there'). The held Intents API pages sit under App Home and admin extensions, so the line goes on their parent (SH-E-376afaab).
- **E127. A developer card's Polaris for another surface goes on that surface's extension capability, `extension-point`.** Polaris web components for POS are CM-POS-004's (SH-E-fc70c128). CM-APP-006's note sends the POS surface there, and Polaris's own `core` stands in CM-APP-006 for the admin (SH-E-51d1de4f). `core` on CM-POS-004 would say the platform makes the POS extensions itself.
- **E128. A developer card that names the Function or API a merchant card's feature is built on keeps its twin's capabilities, and the API it is built with takes no line of its own (rule 51).**
  - The Payment Customization Function cards keep SH-E-e22be35a's and SH-E-d8190ffb's CM-PAY-008, CM-ORD-005 and CM-APP-005 lines (`extension-point`, Plus), with no CM-PAY-019 line (SH-E-10e2b8bc, SH-E-bb2ddc24).
  - 'B2B orders' adds CM-B2B-001 (the digest's rule 46, E78).
- **E129. Where a linked page settles a card's support, the line rests on it, cited by its record.** The case is nested cart lines: apps create them through the platform's Cart APIs, and the platform renders them, so the line is `core;extension-point` (SH-E-8953e070).
- **E130. The Agentic plan is CM-PLN-001 `core`, scoped by the businesses its card names ('Businesses not on Shopify', rule 27).** What comes with it takes 'Agentic plan' as its scope (rule 28): selling in AI channels through Shopify Catalog (CM-AIA-005 `core`) and in the Shop app (CM-CHN-002 `own-service`), as the pricing pages' Agentic rows (SH-E-2465bc51, SH-E-d38d1f84) placed them (SH-E-00aefd26).
- **E131. A card's place that names where a feature is now run or shown takes its line, `core` where the platform runs it (E68, E95):**
  - the POS for the Cart Transform Function API (CM-POS-001), as SH-E-ad3dbd9b took draft orders' line;
  - the return and order cancellation APIs for store credit refunds (CM-RET-003, CM-ORD-004);
  - the store, the AI channels and the Shop app for product warnings (CM-SFR-001, CM-AIA-005, CM-CHN-002 `own-service`);
  - the checkout for nested cart lines (CM-CHK-001).
- **E132. A release marker inside a card that keeps its other line on the same capability makes one line of two supports, not two lines.** The checker refuses a second line with the same scope and filler. SH-E-5a3303bc's personalized search 'coming soon' is CM-AIA-005 `extension-point;shows`, as SH-E-2f39c99b. A thing with its own filler keeps its own line: SH-E-cf087d24's 'soon Meta ads' is `shows`, filler Meta, beside Copilot's `core;extension-point`.

## Cases I couldn't tell, and what would settle each

1. **Tangle:** `new` or `out` (above). The coordinator's reading of rule 57 settles it.
2. **Sponsored products:** `new`, or CM-MKT-012's thing (above). The held page agents/catalog/promoted-placement, if it names who pays for the placements, would settle it.
3. **Rollouts (SH-E-27149592, SH-E-274cd571).**
   - What I did: CM-MKS-002 alone. The themes, checkout configurations and customer accounts setups it publishes take no line, as SH-E-2908de12's theme changes took none.
   - The other reading: E68 would give the title's online store and checkout (CM-SFR-001, CM-CHK-003) and the customer accounts (CM-CUS-010) lines.
   - The translation of localized themes did take CM-MKS-008, since the card's news names it.
4. **'different retail locations' (SH-E-9fef47cd).** I placed it on CM-POS-001, the stores' in-person selling, a marked reading. It may rather be CM-INV-005, the locations themselves.
5. **'pricing' per sales channel's market (SH-E-0d54922a).** I placed it on CM-B2B-003, whose name holds price lists 'assigned to B2B buyers or markets', a marked reading. CM-MKS-001 alone would also hold it.
6. **Nested cart lines' 'post-purchase views' (SH-E-8953e070).** No line. The page names them 'post-purchase surfaces such as order confirmation emails and order status pages', and the card names no capability's own place.
7. **Subscription contracts without a payment method (SH-E-67593db8).** I dropped a CM-PAY-022 line, since the requirement is the contract's. A CM-PAY-022 `extension-point` line would rest on 'collect or update the details later', the card kept for later charges (rule 43).
8. **Agentic Storefronts insights (SH-E-24e377b8).** CM-ANL-001 `core` for the insights the title names ('See how you’re performing, track sales'). No earlier line places the agentic section's analytics, and CM-ANL-003 (overviews) is the alternative.
9. **The Inbox AI sales associate (SH-E-716f5cb1).**
   - Its lines: CM-SUP-004 `own-service` ('our messaging tool'); CM-AIA-005 `own-service;extension-point`, the extension-point resting on its App Store collection ai-shopping-assistants; CM-MKT-023 `own-service`.
   - CM-MKT-023 stands for its recommendations 'For customers signed in with Shop'. I put that buyer condition in `reading`, not `scope`: the brief's scopes are a plan, country, market, store or account.
10. **Refreshed customer accounts (SH-E-7c6690f2).** CM-CUS-010 alone, keeping to the post's own line, SH-E-ba79302c. Its 'recommendations for first-time shoppers' are 'product recommendations you curate' (the post), not the platform's recommendations, CM-MKT-023's thing. I dropped a CM-MKT-023 line I had written.

## The CHANGES lines, as decided

All of them stand, each resting on its own words and, where named, an earlier line or a digest rule:
- CM-AIA-005 gains `own-service`: Inbox's assistant, as SH-E-28190bfc and SH-E-0603b0e7 placed Shop's.
- CM-ANL-006 gains `extension-point`: the ShopifyQL API, as SH-E-6aa48f41 and SH-E-cd6a5f8e.
- CM-APP-006 gains `extension-point`: the Admin Intents API (E126).
- CM-AUT-001 gains `own-service`: Flow's test events (the digest's table).
- CM-B2B-001 gains `extension-point`: B2B order review by apps' functions (E78, E128).
- CM-CHK-002 gains `extension-point`: nested cart lines (E129).
- CM-CHN-002 gains `extension-point`: Shop Minis built with the SDK (rule 11; SH-58's SH-E-f1bd4c0f).
- CM-CUS-010 gains `own-service`: Shop sign-in (rule 11; SH-E-46f1bc0c).
- CM-INV-002 gains `extension-point`: apps' adjustments shown in the admin history through referenceDocumentUri, beside the history's own `core`.
- CM-MKT-003 gains `core` and becomes held: targeted automatic discounts (rule 47).
- CM-MKT-023 gains `own-service` and becomes held: Inbox's recommendations (E75, E120).
- CM-ORD-005 and CM-PAY-008 gain `extension-point`: the developer twins of SH-E-d8190ffb and SH-E-e22be35a, and the pre-order apps' due-on-fulfillment terms (SH-E-21aeb99a).

The checker's notes on leads, read again:
- Tangle's leads (line 6) are by the words 'tools', 'build' and 'developer' only.
- The order review's first lead (line 71) is CM-API-010, by 'conditions' only.
- Sponsored products' leads (line 86) are CM-ACC-009, by 'coming soon', a homonym (a store's visibility before launch); CM-ANL-002, by 'revenue'; CM-API-001 and CM-APP-010, by name. CM-AIA-005 takes its second line.
- None of them is the entry's thing.

Each `own-service` note rests on a maker statement named in its line's reading: Shop's (rule 11), Flow's (the digest's table) and Inbox's ('our messaging tool').

Two lines I first wrote changed a cell, and I took them back:
- CM-POS-004 `core`, for Polaris for POS (E127);
- CM-PAY-022 `extension-point` (case 7).

## Leads for the second stage

- The Promoted placements section of agents/catalog (`raw/runs/20261004T193247Z-shopify-dev-agents-md/fetch.warc.gz@24908`) and its own page, agents/catalog/promoted-placement: the place of Sponsored products.
- The nested cart lines page (`fetch.warc.gz@23889545`) lists where Shopify honours nested lines, buyer-facing and merchant-facing. Under Buyer Facing it names the cart in Horizon and Dawn themes, the checkout and thank-you page, the order status page, and order and abandoned checkout emails. No entry holds the list.
- The Liquid VS Code extension's page (`fetch.warc.gz@26254944`) names its features (syntax highlighting, documentation on hover and others) and the Liquid Language Server it is built on. No entry holds them.

## Problems with the brief or the script

- **`show` prints a non-breaking space as a space.** Every description of this batch ends with a non-breaking space before its last word (as do 'Shopify Markets' inside SH-E-0d54922a's link and 'Azure ID' in SH-E-3bd4da2b). I copied each quote, term and filler with the character itself; a scratch script (`marks.py`) found where they are.
- SH-E-395a3886's 'audit‑ready' holds a non-breaking hyphen. I didn't quote it.
- The checker refuses a second line on one capability under a release marker of its own, since a marker is not a scope (E132). That is consistent with rule 52's 'two supports on it where stated', so I merged the line.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 81 of 81 entries, no problem.
- **One line changed:** Tangle (SH-E-0c55a64f) is `out`, not a new thing. It is an open-source tool for machine-learning and data pipelines, at its own site, which no merchant or app uses on a store. So it is no capability of the class, as SH-57 placed the Shopify Keyboard `out`.
- **The 15 `CHANGES` stand,** each on the digest's table, its rules or a twin's line. The three lines the batch took back stay taken back.
- **The new thing** Sponsored products is `shows`, in developer preview, with no place of its own. CM-MKT-012 is a candidate parent, which no held statement ties to it.
- **The rules E125 to E132 stand** and join the digest's section 6.
- **The open cases stay as placed:** Rollouts on CM-MKS-002 alone, retail locations on CM-POS-001, per-channel pricing on CM-B2B-003, and the Agentic Storefronts insights on CM-ANL-001.
- **Cost:** 23.8 million tokens over 104 requests, about 294,000 an entry. The context reached about 387,000 tokens.
