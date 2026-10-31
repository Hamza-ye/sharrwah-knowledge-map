# SH-26: notes

**The batch:** 81 entries of two Shopify structures (observed-sh, cited at `e38dc17e3` as the entries are; read at `04de369da`). Effort `high`.
- **`dev-docs-nav`, entries 1–33, the last 33 of its 119:** `structures/shopify/dev-docs-nav/shopify.dev@2026-10-07/items.jsonl`, lines 28 to 48: the Payments Apps API (1–3), POS UI extensions (4), Shop (5–8), Shop Minis (9), Shop SDK (10), Shopify App React Router (11), Shopify App Remix (12), Shopify CLI (13), ShopifyQL (14), Storefront events and actions (15), Storefront web components (16), the Storefront API (17–22), the Web Pixels API (23), the Apps docs' headings (24–30, line 47) and the Storefronts docs' headings (31–33, line 48).
- **`dev-nav`, entries 34–81, the first 48 of its 102:** `structures/shopify/dev-nav/`: the top bar of `https://shopify.dev/docs/agents` (`shopify.dev_docs_agents.top`, 34–46), the Agents sidebar (`shopify.dev_docs_agents`, 47–71) and the first ten items of the Apps sidebar (`shopify.dev_docs_apps_build`, lines 1–10, entries 72–81).

**Counts:** 81 entries: 65 on a capability, 1 `new`, 15 `out`. They make 95 lines (79 capability, 1 new, 15 out).

**What I read beyond each entry's item, to clarify it** (as SH-25's check accepted: held evidence read where a label leaves its thing open, each reading citing its file):
- the pages of `dev-docs-nav`'s own source run, `raw/runs/20261007T125415Z-published-dev-docs-nav/fetch.warc.gz`, at the offsets each reading cites (their meta description and first paragraph);
- `structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl`, by position;
- the `dev-nav` sources' own pages: `raw/runs/20261004T193106Z-shopify-dev-agents/fetch.warc.gz@84547` (`/docs/agents`) and `raw/runs/20261004T193432Z-shopify-dev-sections/fetch.warc.gz@1137` and `@100964` (`/docs/apps/build`, `/docs/storefronts`);
- the Agents docs' `.md` pages, which `docs-front-matter` doesn't hold (the register: 'the agents section is not in sitemap_standard.xml.gz'), in `raw/runs/20261004T193247Z-shopify-dev-agents-md/fetch.warc.gz` (18 records);
- the Shop Partners and Shop Users API pages, `raw/runs/20260930T012759Z-shopify-dev-md-robots-disallowed/fetch.warc.gz@385798` and `@523835`;
- for a `dev-nav` button with no children of its own, its children in `dev-docs-nav`'s loader data for the same page (lines 2 and 47), which the selection drops (`drop:children`).

## `dev-docs-nav` (entries 1–33): SH-25's rules, kept

- **R25.4, version headings:**
  - POS UI extensions: CM-POS-004 `extension-point`;
  - Shop Minis: CM-CHN-002 `extension-point`, others' Shop Minis (the digest's rule 11), as the Winter 2026 Edition's 'Build Shop Minis' card (SH-E-284a1a18) was placed;
  - Shop SDK (10): CM-CHN-002 `own-service;extension-point` (R49.2), the twin by meaning of the Shop page's heading Shop SDK (7);
  - Shopify App React Router and Shopify App Remix: CM-DVT-001 `core`, the platform's own packages for building apps (the digest's rules 17 and 41), as SH-25:67 read the React Router app package. The Remix page's note on the React Router package ('package is here and is the recommended path forward…') is a release marker, in `reading`;
  - Shopify CLI: CM-DVT-002 `core` (R98.1, R98.2);
  - ShopifyQL: CM-ANL-006 `core`, as SH-67:91;
  - Storefront events and actions: CM-SFR-004 `extension-point`. Its page says apps and AI agents use the standard events and actions on a storefront, and the Apps docs list 'Events and actions' under App surfaces > Online store, beside Theme app extensions (line 47). This is a reading;
  - Storefront web components: CM-SFR-011 `core`. Its cell already holds the API resource Storefront Web Components, and the Storefronts docs list it under Headless > Bring your own stack (line 48);
  - Web Pixels API: CM-MKT-009 `extension-point`: 'For app developers integrating app web pixels, pixels are loaded in a strict sandbox.'
- **R25.5, API groups:**
  - Payments Apps API: Payment Processing and GraphQL Types are CM-PAY-011 `extension-point`. The cell holds that API group as `extension-point`, and the page says 'The Payments Apps API is available only to' 'approved Payments Partners'. Platform holds only `publicApiVersions` and `ApiVersion`, so it is CM-API-006 `core` alone, whose cell holds `publicApiVersions` (E157);
  - Storefront API: Cart is CM-CHK-002, Metaobjects CM-CNT-002, Search CM-SFR-013 and GraphQL Types CM-SFR-012, each `core`, with no extra CM-SFR-012 line on the groups (E157). Common objects is `out`, since it groups 27 queries and 132 objects of several capabilities, and the API's own groups stand beside it;
  - Storefront API's Customers takes two lines, by R25.6: CM-CUS-001 by its title, and CM-CUS-010 for its whole content (customer access tokens, Multipass, activate, create, recover, reset, update, addresses: the buyer's own account). CM-CUS-010 has no parent, so 'narrower' is a reading.
- **R25.1, headings:**
  - Shop's Getting started and Related APIs are CM-CHN-002's containers, since all their items are Shop's (About Shop, Creating an app, Set up the Shop SDK; the Shop Partners API, Shop Minis, the Shop Users API). They take `own-service;extension-point` (rule 11, R49.2). The Shop SDK heading takes the same line. Shop's Use cases is `out`: lead capture, sign-in, third-party identity providers and user data are several capabilities' (rule 11 itself puts Shop's sign-in on CM-CUS-010 and lead capture on CM-CUS-007);
  - the Apps docs' Dev tools is CM-DVT-001 `core`, as SH-25:67. The other six Apps headings are `out`: Building and deploying apps, Building blocks, Design and quality, App surfaces, Use cases, and Selling and growing your app each group several capabilities' pages, named in each reading;
  - the Storefronts docs' Themes is CM-SFR-001 `core`, Headless CM-SFR-011 `core` (E85), and Mobile CM-CHN-006 `extension-point`, as SH-25 placed the REST Admin API's Mobile Support. The page reads 'Build iOS, Android, and React Native apps with the Storefront API and Checkout Kit.'

## `dev-nav`: the rules I set (R26.1 to R26.8), for the coordinator to check and SH-27 to keep

`dev-nav` is shopify.dev's navigation as its pages render it: the top bar (`<nav>` index 0) and the sidebar (`<nav>` index 1) of each section page, from `capture/structure_nav.py` (each `meta.json`). Its items are links, buttons and text. A collapsed group renders as a button without its children, and the register says those children are in the page's embedded router JSON. The same page's `dev-docs-nav` loader data holds them as children.

- **R26.1: a rendered twin takes its loader data item's line.** A sidebar's heading text (`kind: text`) is the rendered form of a `dev-docs-nav` heading of the same page and label. It takes that heading's lines and names the heading in `reading`:
  - the Agents sidebar's Getting started, Negotiate and authenticate and Discover products take CM-AIA-005 `extension-point` (SH-25's SH-E-e745379d, SH-E-10f5abb8, SH-E-db9cba48);
  - Complete checkout adds CM-CHK-001 `core`, and Monitor orders adds CM-ORD-001 `core` (SH-E-0d9b063c, SH-E-80c59d8a; R25.2);
  - the Apps sidebar's Building and deploying apps is `out` and Dev tools is CM-DVT-001 `core` (this batch's SH-E-6f53ec3a, SH-E-0156a09c).
- **R26.2: the site's own chrome is `out`.** This covers the menu button ('Open navigation menu'), Search, Toggle dark mode, the separator '•' and Log in. The link 'Log in' goes to `http://dev.shopify.com/dashboard`, but the coordinator's message names log in as chrome. So does the sidebar's last item Full index: an `<a>` with no `href`, inside `<div class="_HiddenLink_1gye5_123" data-markdown="remove">` on all three sidebars, so it opens no held place. The two empty buttons at positions 7 and 8 of the top bar are scroll hints (`data-testid="scroll-hint-start"`, `"scroll-hint-end"`), and the build gave them no entries.
- **R26.3: the top bar's area links are containers of the docs areas.** Each is placed by its title, as M-13 and the ruling after SA-28 read a title that names a capability or one part of the platform:
  - Apps (`/docs/apps/build`): CM-APP-001 `extension-point`. Its page reads 'Merchants run their whole business on Shopify, and they turn to apps for the features they need next.', and the cell reads apps made by third-party developers as `extension-point`;
  - Storefronts (`/docs/storefronts`): CM-SFR-001 `core`, as SH-25 read the heading Storefronts (SH-E-b93ee327). Its page reads 'A storefront is the part of Shopify buyers see.';
  - Agents (`/docs/agents`): CM-AIA-005 `extension-point` (R25.2; SH-25:2, SH-64:134, SH-65:83).

  A sidebar's Overview link to the same address takes the same line, and its term is left empty, since 'Overview' doesn't name the thing.
- **R26.4: the site's own places.**
  - A label that names the docs as such takes CM-DVT-001 `core` (R25.3): the logo's link to `/docs`, whose images' alt text is 'Docs page', and the References button, which opens the menu of the API references.
  - The 'Ask assistant' button is shopify.dev's assistant, AI outside the admin on the place's capability (the digest's rule 50). So it is CM-DVT-001 `core`.
  - The Changelog link is shopify.dev's developer changelog, “Shopify’s developer changelog documents all changes to Shopify’s platform.” (its page, `fetch.warc.gz@148544` of the `dev-docs-nav` run). That is CM-API-006's 'record of changes', so the link is `core` there. It isn't the merchants' changelog, which the ruling after SA-2 and SA-5 puts on CM-ONB-003.
  - Help (`/support`) is CM-PTN-001 `shows`, as SH-86 read the Partner Dashboard's Support for developers. The page isn't held, so the link names only a topic.
- **R26.5: a sidebar's link or button is placed by its own label, read with its page where the label leaves its thing open.**
  - A link's page is read through its front matter (`docs-front-matter`), or for the Agents docs through its `.md` record in run `20261004T193247Z-shopify-dev-agents-md`.
  - A collapsed button is a container (R25.1), read with its children from `dev-docs-nav`'s loader data for the same page. Its children's own things take no line.
- **R26.6: the Agents docs' links** are CM-AIA-005 `extension-point` (R25.2, E122). A link whose own words name the platform's own thing offered to agents also takes that thing's capability, `core`:
  - carts: CM-CHK-002, for Build a cart, About carts and checkout and Cart MCP, as SH-65 placed the Cart MCP;
  - checkout: CM-CHK-001, for Finish checkout, About carts and checkout and the Checkout button, as SH-64 placed the Checkout MCP;
  - orders: CM-ORD-001, for Monitor orders, About orders, Order MCP and Order webhooks;
  - webhooks: CM-API-008, for Order webhooks (the digest's rule 17).

  Catalog search stays on CM-AIA-005 alone. That cell's thing is buyers 'discovering and buying a store's products through AI chats and agents', and SH-25 and SH-64 placed the Catalog so.
- **R26.7: developer tools.**
  - The CLI is CM-DVT-002 `core`: the Shopify CLI button, and Scaffold an app ('Use Shopify CLI to quickly set up your development environment and generate starting code for your app.').
  - The AI Toolkit is CM-DVT-001 `core`, as SH-66 placed it.
  - The Dev Dashboard is CM-PTN-001 `core` (E151).
- **R26.8: the Apps sidebar's lifecycle items.**
  - Build an app, a tutorial for building an app with the platform's tools, is CM-APP-001 `extension-point`, as the Apps area is (R26.3).
  - Deployment is `new:App versions` `core`. Its children are hosting guides and the app's versions, and the platform keeps a deployment as an app's version: 'Learn how to release your app configuration and extensions to users.' Hosting the app's server is the developer's own work, named in passing.
  - Distribution is CM-APP-002 `core`, whose name and note hold App distribution, 'Shopify's choice between the App Store and custom distribution'.

## The new thing

**`new:App versions`**, `core`, one entry: SH-E-6f6e31d0, the Apps sidebar's button Deployment.
- **What it is:** an app's versions, released and rolled back through the platform. It is the new thing SH-53 named, which SH-23 placed for the Dev Dashboard's Versions (R23.6), SH-86 and SH-87 for the Partner Dashboard's version routes, and SH-98 for the CLI's `app deploy`.
- **Its place of its own:** the Dev Dashboard's Versions item and the partner dashboard's `/:orgId/apps/:appId/versions` routes. This entry is a group of the docs, not a place of its own.
- **Its names:** English only: Deployment, app versions ('About app versions', 'Deploy and release app versions').
- **Where it goes:** as SH-98 proposed, domain F, area APP, under CM-APP-001 or beside CM-DVT-002.
- **The checker's lead:** CM-DVT-001, by the words app and building only. I read its cell, the platform's tools and docs for building apps, and it doesn't hold app versions.
- **What I searched:** nothing beyond what SH-53 and SH-98 searched. The alternative to this line is `out`, a grouping of the developer's hosting and the platform's versions (below).

## The `CHANGES` line

**CM-CHN-002@shopify gains `extension-point`, by lines 6, 8, 9, 10 and 11.** These are Shop's Getting started, Shop SDK and Related APIs headings, the Shop Minis reference and the Shop SDK reference.

I kept them:
- **Shop Minis (line 10)** is others' Minis in Shop's app, the case rule 11 names: 'Shop Minis are immersive, full-screen buyer experiences within the Shop app.' The Editions' developer cards on Shop Minis are already `extension-point` on CM-CHN-002 in the held pass (SH-E-050da4d8, SH-E-f1bd4c0f, SH-E-284a1a18; `own-service;extension-point` for SH-E-6d43442a and SH-E-15aa8b66). The cell doesn't show them yet, since the held pass's lines aren't amended in.
- **The other four** are Shop's APIs and SDKs offered for developers' own storefronts and integrations: “Use the Shop platform's APIs and SDKs to connect with Shop users on your storefront”. That is R49.2's `own-service;extension-point` for Shop's things offered to developers. They sit on CM-CHN-002 because that cell holds the Shop API (`own-service`, SH-23 and SH-24's scope picker lines).
- **The alternative:** place Shop's SDK features on their own capabilities (Login on CM-CUS-010, Lead Capture on CM-CUS-007), as R49.2's sign-in is. A heading's items take no line (R25.1), so I didn't.

## Entries I couldn't tell, and what would settle each

- **Deployment (SH-E-6f6e31d0):** `new:App versions` `core`, or `out` as a grouping of hosting (the developer's own server, 'Learn how to choose a hosting service and deploy your Shopify app.') and the platform's app versions. Deciding `new:App versions` in `held/new.tsv` would settle it: if it becomes a capability, this line follows it.
- **The logo link 'Docs page' (SH-E-9ed7ee34):** CM-DVT-001 `core`, since its label names the docs, or `out` as chrome. What would settle it: a ruling on whether a site logo is chrome.
- **Full index (SH-E-69ebb72b):** `out`, a hidden anchor with no address. The alternative is CM-DVT-001 `core`, as a label naming the docs' index. What would settle it: the page that index stands for, which no held source names.
- **Help (SH-E-1257a4c9):** CM-PTN-001 `shows`. The alternatives are `out` as chrome, or CM-PTN-001 `core` as SH-86:14's Support. What would settle it: shopify.dev's `/support` page, which isn't held.
- **Log in (SH-E-c648eda2):** `out` as chrome, as the coordinator's message says. Its address is the Dev Dashboard, so the alternative is CM-PTN-001 `shows`, the way SH-99:85 read shopify.com's Log in on CM-ACC-001.
- **Storefronts (SH-E-126c336a):** CM-SFR-001 `core`, as SH-25's heading Storefronts. The page names three ways: theme (CM-SFR-001), headless (CM-SFR-011) and a native mobile app (CM-CHN-006). So the alternative is `out`, a grouping over three capabilities. SH-25's same choice was kept as placed but left open.
- **Apps (SH-E-3a9f2659) and its Overview (SH-E-5f176fee):** CM-APP-001 `extension-point` by the title Apps. The alternative is `out`, since the area's pages are many capabilities'.
- **Changelog (SH-E-1ac72031):** CM-API-006 `core`. Its note says 'Shopify's statements hold no change log found', so this line gives Shopify's cell a change log. What would settle it: whether CM-API-006's change log means the developer changelog, which covers more than the API, or only the API's.
- **Ask assistant (SH-E-0f0df524):** CM-DVT-001 `core` by the digest's rule 50. No held page of the assistant states what it does. Its features (`dev_assistant_v2_m2` and the like in the loader data's `features`) are no entry.
- **Storefront API's Customers (SH-E-1e1f87fd):** the CM-CUS-010 line rests on the group's mutations. The coordinator may keep CM-CUS-001 alone, as SH-25 did for the Admin APIs' Customers.
- **Payments Apps API's Platform (SH-E-f707c32e):** CM-API-006 alone, by its content. The alternative is adding CM-PAY-011, as the API the group is in. E157 makes it the holding cell's line alone.
- **Storefront events and actions (SH-E-851dba58):** CM-SFR-004 `extension-point`. The events are the platform's own, so a `core` line on the events' capability, as R49.3 places webhooks, would need a capability for storefront events. I found none: CM-MKT-009 holds the analytics customer events of pixels.
- **The Agents docs' catalogs (SH-E-c0f69cf0, SH-E-b9fb2d2c, SH-E-310b8afc):** CM-AIA-005 alone. Storefront Catalog, one store's products offered to agents, is a lead for CM-CAT-001, as Cart MCP is CM-CHK-002's. SH-25's Discover products took no CM-CAT-001 line, and I kept to it.

## The structures' items against their sources

I found no disagreement that changes a placement. What I noted:
- **`dev-nav`:**
  - The top bar's 'Docs pageDocs page' joins the alt text of the logo's two images, light and dark (`source.html`).
  - 'Full index' is recorded as `kind: text`, but the source holds it as an `<a>` with no `href`.
  - Collapsed groups have no children in the structure, as its register says. The same page's `dev-docs-nav` item holds them.
- **`dev-docs-nav`:**
  - Version headings name other versions than their page's latest: `shopify_app_react_router_v2` (its page 'v3 latest') and `shopify_app_remix_v5` ('v6 latest'). `pos_ui_extensions_2026_07` matches '2026-07 latest'.
  - The Shop page (line 33) is the only page of the batch whose `navData` has no `title`.

## What the sources state that no entry holds, for the second stage

All `dev-docs-nav` lines are in `structures/shopify/dev-docs-nav/shopify.dev@2026-10-07/items.jsonl`.
- **Line 28, the Payments Apps API's mutations:** payment, refund, capture, void and verification sessions, and `paymentsAppConfigure`. They lead to CM-PAY-011's refunds and captures.
- **Line 32, the POS UI extensions' targets:** App background, Cart details, Customer details, Draft order details, Home screen (smart grid), Order details, Post-purchase, Product details and Register details, with the Platform APIs (Camera, Cash Drawer, PinPad, Print, Scanner). They lead to CM-POS-004.
- **Line 33, Shop's use cases:**
  - Lead capture, CM-CUS-007;
  - Store metafields, custom data on a Shop user's profile;
  - Sign in with Shop, CM-CUS-010;
  - Third-party identity provider, CM-CUS-011;
  - Get user information and Recognize returning users.
- **Line 34, Shop Minis:**
  - the Minis Admin API (`miniToggle`, `userTokenVerify`);
  - Publishing and the `submit`, `check-submission` and `cancel-submission` commands, a review of Minis;
  - Analytics, 'Access aggregated data about your Mini.'
- **Lines 36 and 37, the app packages:** Authenticate (Admin, Flow, Fulfillment Service, Webhook, Public), leads for CM-API-002, and APIs (Billing, Scopes), leads for CM-APP-003 and CM-API-003.
- **Line 39, ShopifyQL's Schemas:** Customers, Finance and payments, Inventory, Marketing, Orders, Sales revenue, Sessions and behavior.
- **Line 42, the Storefront API's Common objects:**
  - `shopPayPaymentRequestSessionCreate` and `Submit`, Shop Pay's payment requests, a lead for CM-PAY-014;
  - `localization`, `menu` (CM-CNT-005), `sitemap`, `urlRedirects` and `productRecommendations`.
- **Line 45, the Web Pixels API:** its Pixel Privacy and `customerPrivacy`, a lead for CM-TRU-006.
- **Line 47, the Apps docs' items:**
  - Built for Shopify (requirements, annual reviews, regain lost status) and App Store ads. `caps --terms` finds no capability for either ('Built for Shopify; App Store ads; app listing; app review');
  - Admin intents (the ruling after SH-8);
  - AI and agents: Sidekick, Storefront MCP, Customer Accounts MCP;
  - Flow triggers, actions and templates;
  - Shopify Collective under Products and pricing;
  - Payments: 'Get approved for payments', CM-PAY-011;
  - Sales channels: Channel config extension, Configure order attribution, Contextual product feeds.
- **Line 48, the Storefronts docs' items:**
  - Themes: Sell themes > Theme Store (CM-SFR-003), and Developer Tools: Theme Access app, Collaborator accounts, Dev stores (CM-DVT-004), GitHub integration;
  - Headless: Bring your own stack > Shopify Plugin for WordPress, Headless with B2B;
  - Mobile: Checkout Kit (CM-CHK-001), Accelerated checkouts with Shop Pay and Apple Pay (CM-CHK-008, CM-PAY-012, CM-PAY-014), the iOS and Android Buy SDKs.
- **`dev-nav`, the References menu:** its items aren't in the structure. The register says they are in the page's router JSON, not extracted.
- **The Agents docs' `.md` records** (run `20261004T193247Z-shopify-dev-agents-md`):
  - Checkout MCP, Global Catalog MCP, Storefront Catalog MCP and Auth and rate limiting have no entries;
  - the Agents section's other pages aren't held there: Checkout WebMCP, Checkout errors, Checkout Kit, Embedded Checkout Protocol, Shop Pay payment handler, Promoted placements, the Catalog extensions, Policy and FAQs MCP and Buyer-linked tokens.
- **Not held:** `https://shopify.dev/support` (`held_index.py`: not held), the target of the top bar's Help.

## Problems with the brief or the script

- **`held_entries.py earlier` prints position twins for `dev-docs-nav`:** the items at the same index of other pages' `navItems`, such as Access, Core concepts and Common objects for Payment Processing. Pages laid out differently put other things there, so none was taken (SH-73's note in the brief). It prints no twin for any `dev-nav` entry.
- **Leads by a field's words:** many `dev-nav` leads come from 'link', 'button' or 'order' (CM-PAY-032 for About orders, CM-APP-008 for Apps). The checker's two `NOTE`s on CM-PAY-032 are such leads.
- **Quotes from a folded YAML description:** in the Agents docs' `.md` records, a quote is found only within one line of the description. I quoted single lines.
- **Reading beyond the selection:** as SH-25 did, these readings rest on the clarifying reads listed at the top: the linked pages, `docs-front-matter` and the loader data's children. The coordinator accepted those reads at SH-25's check.

## For SH-27 (`dev-nav`'s last 54 entries)

The entries are the Apps sidebar's items 11 to 45 (`shopify.dev_docs_apps_build`, Building blocks to Full index) and the Storefronts sidebar (`shopify.dev_docs_storefronts`). R26.1 to R26.8 apply as follows:
- **Heading texts take their loader data twins' lines (R26.1):**
  - Building blocks, Design and quality, App surfaces, Use cases and Selling and growing your app are `out` (this batch's SH-E-df971a94, SH-E-0440fb5a, SH-E-676ffe45, SH-E-cf8026fb, SH-E-9d3c974b);
  - Themes is CM-SFR-001 `core`, Headless CM-SFR-011 `core`, Mobile CM-CHN-006 `extension-point`.
- **Each collapsed button is a container (R26.5),** read with its children in `dev-docs-nav` lines 47 and 48:
  - App surfaces' buttons take their extension capabilities, `extension-point`: Admin CM-APP-008, App Home CM-APP-007, Checkout CM-CHK-004, Customer accounts CM-CUS-014, Online store CM-SFR-004, Point of Sale CM-POS-004;
  - Selling and growing your app's buttons: Shopify App Store is CM-APP-002 and Billing CM-APP-003;
  - Built for Shopify has no capability found: `new`, or `out` if the coordinator reads it as a grouping.
- **Overview links take their area's or heading's line (R26.3):** `/docs/storefronts` is SH-E-126c336a's, and `/docs/storefronts/themes`, `/headless` and `/mobile` are the headings'.
- **Full index is `out` (R26.2),** as SH-E-69ebb72b, whose entry already stands for all three sidebars.

## The coordinator's check

Measured: 29.2 million tokens over 122 requests, about 360,000 an entry, much of it in the linked pages read where a label left its thing open. The checker prints no problem.
- **Kept:** SH-25's rules for `dev-docs-nav`'s last 33, so that structure is placed whole; R26.1 to R26.8, which SH-27 keeps; the `CHANGES` line, CM-CHN-002 `extension-point`, by the Editions digest's rule 11 (others' Minis in Shop) and R49.2 (Shop's APIs and SDKs for developers' storefronts); and `new:App versions` with the Deployment button.
- **Changelog on CM-API-006:** kept, as the developer changelog of the API's versions; CM-API-006's note, which says Shopify holds no change log, goes to the amendment with it (`amendment-notes.md`).
- **The reads beyond the selection** are accepted as SH-25's were, each reading citing what it read. The entries left open are kept as placed.
