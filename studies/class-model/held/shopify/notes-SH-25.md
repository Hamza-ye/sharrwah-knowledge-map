# SH-25: notes

**The batch:** the first 86 of the 119 entries of Shopify's `dev-docs-nav` (observed-sh, cited at `e38dc17e3` as the entries are; read at `04de369da`): `structures/shopify/dev-docs-nav/shopify.dev@2026-10-07/items.jsonl`, the top-level items of each docs page's sidebar, as its loader data states them (`loaderData.*.navData.navItems`). The selection drops each item's `children` (`selection.tsv`: `nested:navItems;drop:children`), so a heading's children are read from the same item, to see what it groups. Effort `high`.

The entries come from 25 of the structure's 48 pages: the Agents docs (1–5), the Admin Extensions reference (6), the GraphQL Admin API (7–34), the REST Admin API (35–55), the API references' sidebar (56–62), and the references of App Events, App home ui extension, App home, Checkout UI extensions, Shop Pay Wallet, Customer account UI extensions, the Customer Account API, Events, Function APIs, Hydrogen React, Hydrogen, Liquid and the Partner API (63–86).

## The rules I set for `dev-docs-nav` (R25.1 to R25.8), for the coordinator to check and SH-26 to keep

- **R25.1: a heading or group is a container of documentation pages.** It is read with its own children in the item.
  - **Its title names a capability's thing, or one part of the platform:** it takes that capability's line (M-13; the ruling after SA-28).
  - **Its title names only a grouping, but all its items are one capability's thing:** it is that capability's container. Getting started, Core concepts and the Customer Account API's Common objects are the cases.
  - **Its title names only a grouping, over several capabilities' items:** it is `out`, as R47.1 and R49.1 read section headings and the ruling after SA-28 reads 'Others'. Its items are named in `reading`. The cases are App data and logic, Additional APIs, and the GraphQL Admin API's and the Partner API's Common objects.
  - **Its support** is the documented thing's:
    - the platform's own API for its own feature is `core`;
    - an API or target through which apps, agents or partners do the work is `extension-point` (the digest's rule 17).
  - **Its items' own things take no line here.** They are named in passing (the ruling after SA-41), and the selection leaves them out.
- **R25.2: the Agents docs** (`/docs/agents`) are developers' commerce agents on the platform's MCP servers.
  - Each of its five headings is CM-AIA-005's container, `extension-point` (E122), as SH-64 and SH-65 placed the Agents docs' cards.
  - A heading's own words that name the platform's own thing offered to agents take that thing's capability, `core`, as SH-64 and SH-65 placed the Checkout MCP and the Cart MCP:
    - Complete checkout takes CM-CHK-001;
    - Monitor orders takes CM-ORD-001.
- **R25.3: the documentation itself** is CM-DVT-001 `core` only where the label names the docs as such: Guides and Reference (67, 68).
  - A label that names a stage of the work, such as Getting started, isn't the docs as such. Neither is a grouping.
  - The container's own line (R25.1) stands beside the CM-DVT-001 line.
- **R25.4: an API reference's version heading** is the whole reference under one heading. It has no label, and its key is the API's name with a version (`admin_extensions_2026_01`, `app_events_2026_10`, `hydrogen_2026_01`, `shopify_functions_next`).
  - It takes the API's capability, with the API's support. Its term is the page's title, the entry's `within`.
  - The key and the page's `versions` go in `reading`.
  - A release candidate is a release state, in `reading`, the support staying the thing's (the digest's rule 35). The case is `app_home_ui_extension_2026_07_rc`, whose page's only version is '2026-07 release candidate'.
  - The cases:
    - Admin Extensions: CM-APP-008 `extension-point`;
    - App Events: CM-DVT-001 `core`, by the digest's App events rule, and CM-APP-003 `core`, for its page's 'for Shopify App Pricing usage-based pricing';
    - App home ui extension and App home: CM-APP-007 `extension-point`;
    - Checkout UI extensions: CM-CHK-004 `extension-point`;
    - Customer account UI extensions: CM-CUS-014 `extension-point`;
    - Events: CM-API-008 `core`. Its page reads 'Subscribe to resource-level changes (for example, Product) with granular triggers and custom GraphQL payloads.';
    - Function APIs: CM-APP-005 `extension-point`;
    - Hydrogen and Hydrogen React: CM-SFR-011 `core` (E85).
- **R25.5: an API reference's group** is a place of its own, an API group (B-extent).
  - **Its capability:** the one its title names, `core`, as the platform's own API for its own feature (the digest's rule 17).
  - **A group a cell already holds:** where a cell holds the group or its title as a term, the group takes that capability's line alone, with no CM-API-001 line (E157). The cases are Access, Analytics (CM-ANL-006, analytics through the API), Bulk operations, Checkout and accounts configurations, Checkout branding, Localizations, Store properties, Discounts and marketing, Products and collections, and Shipping and fulfillment.
  - **A title that names two things** takes a line for each: Products and collections; Shipping and fulfillment; Discounts and marketing.
  - **A homonym** is named in `reading`:
    - Billing is apps' charges, CM-APP-003, not the store's bill;
    - Liquid's Tags aren't product tags;
    - the Partner API's Transactions are the partner's earnings, CM-PTN-003, not an order's;
    - the Partner API's App events aren't the App Events API.
  - **A GraphQL Admin group's content** comes from the full navigation that the page's loader data names (`fullNavDataPath`, `/docs/api/admin-graphql/2026-10/nav`). That navigation is held as `structures/shopify/admin-graphql-reference-nav/shopify.dev@latest/`, which the selection doesn't read, and it is read only to clarify.
  - **Common objects:**
    - one that groups objects of several capabilities is `out`;
    - the Customer Account API's holds that API's whole content, so it is that API's container, on CM-CUS-010.
  - **GraphQL Types,** the API's own types by kind:
    - the GraphQL Admin API's are on CM-API-001, the conventions common to the API (its cell holds Global IDs and GraphQL pagination);
    - another API's are on that API's capability: the Customer Account API's on CM-CUS-010, and the Partner API's on CM-PTN-001.
- **R25.6: a narrower capability for a group's whole content.** A group can have a title that names one capability's thing, while all its items are another, narrower capability's thing. It then takes both lines:
  - Cart: CM-CHK-002, and CM-CHK-006 for CartTransform, its only object;
  - B2B: CM-B2B-001, and CM-B2B-002 for its companies' records;
  - the REST Admin API's Sales Channels: CM-CHN-001, and CM-CHN-004 for its listings.
- **R25.7: the REST Admin API's groups** are read as the GraphQL Admin API's.
  - The REST page states 'The REST Admin API is a legacy API as of October 1, 2024.' (`raw/runs/20261007T125415Z-published-dev-docs-nav/fetch.warc.gz@699590`).
  - That is a release marker, so it goes in every REST line's `reading`. The support stays the thing's, `core`, since the API is still served.
- **R25.8: a label that leaves its thing open** (Events, Marketing Event, Mobile Support, Plus, Sales Channels, Tender Transaction, Deprecated API Calls, Gift Cards).
  - Its items' pages are read by their own description, quoted:
    - the front matter in `structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl`, by position;
    - or, for a version heading or the Shop Pay Wallet docs, the page's own meta description in the structure's source record.
  - A label that names a plan is its group's scope: Plus, for User, 'Retrieve the permissions on staff.'.
  - A group whose pages say an app does the work as a channel ('your sales channel') is `extension-point`.
  - Mobile Support is `extension-point` on CM-CHN-006, as that cell reads the same objects' scopes (SH-S-6059). I first wrote `core`, which would have changed the cell; I corrected it to follow the cell.

## The new thing

**`new:Timeline events`**, `core`. It has two entries:
- SH-E-693cad6d: the GraphQL Admin API's group Timeline events;
- SH-E-d0f6e2d9: the REST Admin API's group Events.

**What it is:** the events the platform records for a store's resources. The REST Event page describes them: 'Retrieve a list of events, which are important actions in the operation of a shop. Shopify records events for a range of resources, and each resource has its own set of actions that create events.' (`docs-front-matter` position 6623). The group holds:
- BasicEvent;
- CommentEvent, staff comments on a resource's timeline;
- DeletionEvent;
- ResourceAlert and ShopAlert;
- the queries `events`, `comments` and `deletionEvents`.

**Its place of its own:** the GraphQL Admin API reference's group Timeline events, and the REST Admin API's group Events. Each is an API group the reference names.

**Its names:** English only. The GraphQL reference calls it Timeline events, the REST reference Events. shopify.dev's docs hold no Arabic.

**Where it goes:** I propose domain G, area OPS, beside CM-OPS-005, the store's logs, with no parent: records the platform keeps of what happened in the store. Two capabilities come close, and the coordinator may join it to either:
- CM-TRU-003, the audit log of admin activity. That cell holds the merchant audit log's own route and topic, not resources' events.
- CM-ORD-013, notes and comments on an order. That cell holds nothing on Shopify, and CommentEvent is a lead for it.

**What I searched:** `timeline; staff comment; comment; alert; resource event; store events; activity log; audit log; history; notes; activity`.

**The checker's leads:** CM-API-001, CM-API-012, CM-API-013 and CM-APP-004. I read each, and none is the thing:
- CM-APP-004 is an app's lifecycle events;
- CM-API-012 is WooCommerce's response caching;
- CM-API-013 is an account-level API.

## Entries I couldn't tell, and what would settle each

- **App management (SH-E-1c543209):** I placed it on CM-PTN-001 `core`. The App Events API's page names monitoring 'in the Dev Dashboard' (E151's CM-PTN-001), so both items are a developer's management of its own apps.
  - The alternative is `out`: the digest's App events rule puts the App Events API on CM-DVT-001, and the Partner API is CM-PTN-001's, so the heading would group two capabilities.
  - What would settle it: a ruling on whether the Dev Dashboard's monitoring makes the App Events API CM-PTN-001's.
- **Common objects in the GraphQL Admin API and the Partner API (SH-E-d0a8317f, SH-E-a457e7b8):** I placed both `out`. The alternative is CM-API-001 `core`, reading an API's shared objects as conventions common to it. What would settle it: a ruling on API groups that name only a grouping.
- **GraphQL Types (SH-E-47f9b4de):** I placed it on CM-API-001 `core`, as the API's type system. The alternative is `out`, as a grouping by kind over every capability's types. The same ruling would settle it.
- **Cart (SH-E-1e2462d9):**
  - Its CM-CHK-002 line rests on the title alone, since the group holds only CartTransform. The coordinator may drop it.
  - It is also a lead for CM-CHK-006's parent. Its note says 'No parent: Shopify groups it among its Function APIs'. The GraphQL Admin API groups CartTransform under Cart, a second grouping of Shopify's own.
- **Monitor orders (SH-E-80c59d8a), the CM-ORD-001 line:** CM-ORD-001 is the store's orders 'and their management in the admin'. An agent following an order through the Order MCP isn't management. The line follows SH-64's reading of the Checkout MCP, the platform's own thing offered to agents. The coordinator may keep CM-AIA-005 alone.
- **Plus (SH-E-10f74b21):** I chose CM-STF-002 over CM-STF-001 because the User page says 'Retrieve the permissions on staff.'. The scope 'Plus' is the group's title; the page's front matter states no plan.
- **Storefronts (SH-E-b93ee327):** I placed it on CM-SFR-001, reading 'Storefronts' as one part of the platform, the storefront tree CM-SFR-001 roots. The alternative is `out`: its items are several capabilities' APIs (CM-SFR-012, CM-SFR-002, CM-SFR-011, CM-TRU-006, CM-CUS-010, CM-AIA-005).
- **App home ui extension (SH-E-5d0fb077):**
  - I placed it `extension-point`, with the release candidate in `reading`.
  - If a reference held only as a release candidate isn't yet offered to stores, the line is `extension-point;shows`, as E155 has 'before rollout'. The page states no such limit.
- **Getting started (SH-E-e745379d):** I gave it no CM-DVT-001 line (R25.3). The coordinator may read 'Getting started' as naming the docs as such.
- **The one CHANGES line, CM-PAY-014 gaining `extension-point`:** this is Shop Pay Wallet's Guides and Reference (SH-E-ec95f5f4, SH-E-ce830556). Its page says 'Use Shop Pay Wallet to offer Shop Pay in your existing checkout.', which is Shop Pay offered for a developer's own checkout. So `own-service;extension-point`, by R49.2. The cell holds the concern map's API group Shop Pay Wallet API as `core` (SH-S-0852).

## The structure's items against its sources

I found no disagreement between the items and their sources. I noted the following:
- **Version headings name other versions than the page's latest:**
  - `admin_extensions_2026_01`, while its page lists '2026-07 latest';
  - `hydrogen_2026_01` and `hydrogen_react_2026_01`, while their pages list '2026-04 latest'.
- **Pages with no entries of their own:**
  - eleven pages carry the same API references' sidebar as `/docs/api/ajax` (line 8, entries 56–62), so they have no entries of their own: `app-bridge/migration-guide`, `checkout-extensions`, `customer-authentication`, `customer-privacy`, `github-app`, `libraries-and-templates`, `pixels`, `polaris`, `pos-extensions`, `usage/gids` and `web-mcp`;
  - the Webhooks reference's `navItems` is empty (line 46), and so is `/docs`'s (line 1);
  - the changelog's two pages hold no navigation.

## What the sources state that no entry holds, for the second stage

All lines are in `structures/shopify/dev-docs-nav/shopify.dev@2026-10-07/items.jsonl`.

- **Line 2, the Agents docs' items:**
  - Promoted placements (`/docs/agents/catalog/promoted-placement`), which SH-49 and SH-65 hold as `new:Sponsored products`;
  - Shop Pay payment handler, CM-PAY-014 for agents (R47.4);
  - Checkout Kit, the Embedded Checkout Protocol, Checkout WebMCP, Policy and FAQs MCP, the Global and Storefront Catalog extensions, Order webhooks, and Buyer-linked tokens.
- **Line 5, the Admin Extensions' targets, one per admin page:** Abandoned checkouts, App tools, Catalogs, Collections, Companies, Customers, Discounts, Draft orders, Function settings, Gift cards, Orders, Product variants and Products.
- **Line 8, the API references' items:**
  - Feature previews (`/docs/apps/build/stores/feature-previews`), a lead for CM-DVT-004;
  - Shopify GitHub app, CM-DVT-001;
  - Customer Privacy API, CM-TRU-006;
  - WebMCP Tools, CM-AIA-005;
  - Customer authentication, with its Third-party identity providers and Multipass, CM-CUS-011;
  - Web pixel, CM-MKT-009;
  - Shop API;
  - Shop Minis, with its Components and Hooks;
  - Shop Pay Wallet API, CM-PAY-014.
- **Line 21, the Function APIs' items:** Cart and Checkout Validation (CM-CHK-005), Cart Transform (CM-CHK-006), Delivery Customization, Discount (CM-MKT-004), Fulfillment Constraints (CM-SHP-014), Order Routing Location Rule (CM-SHP-005), Payment Customization, and the Deprecated APIs Order Discount, Product Discount and Shipping Discount.
- **Line 20, the Events API's 18 resources:** Article, Blog, Collection, Company, Customer, FulfillmentOrder, InventoryItem, InventoryShipment, InventoryTransfer, Location, MetafieldDefinition, Metaobject, MetaobjectDefinition, Order, Page, Product, Refund and Return.
- **Line 16, the customer account UI extensions' targets:** among them Order status, Payments and returns, and Profile page (B2B).
- **Every page, the site's own data:**
  - `loaderData.routes/global-wrapper.search`: each API reference's name, and whether it is versioned;
  - `loaderData.routes/global-wrapper.features`: the features enabled on shopify.dev.

  Neither is an entry.
- **The GraphQL Admin API's full navigation** (`admin-graphql-reference-nav`, 4,637 items) has no entries. Its 28 categories reach the model here.

## Problems with the brief or the script

- **R25.8 reads beyond the brief's list of clarifying reads.** It reads two things:
  - the `docs-front-matter` structure, which `selection.tsv` doesn't read;
  - the meta descriptions of the structure's own source pages, in their archive records.

  Without them, labels such as Events, Mobile Support, Plus or Tender Transaction would have been placed from what I know of the platform. The coordinator may prefer to leave these to the second stage.
- **The checker finds a quote from the source page only where the reading cites the file.** A quote from the structure's own source record, such as the REST page's legacy sentence, was 'found nowhere held' until the reading cited the record (`raw/runs/<run>/fetch.warc.gz@<offset>`). Quotes from `docs-front-matter` were the same until the reading cited `items.jsonl`.

## For SH-26 (entries 87 to 119)

The entries are:
- the Payments Apps API's groups;
- the POS UI extensions;
- Shop, Shop Minis and Shop SDK;
- Shopify App React Router, Shopify App Remix and Shopify CLI;
- ShopifyQL;
- Storefront events and actions, and Storefront web components;
- the Storefront API's groups;
- the Web Pixels API;
- the Apps and Storefronts docs' headings.

The rules above apply as follows:
- **Version headings:** R25.4.
- **Groups:**
  - each API group goes on the capability its title names, or the one whose cell holds it (R25.5, E157);
  - Common objects is `out` unless it holds the whole API;
  - GraphQL Types goes on the API's own capability, which for the Storefront API is CM-SFR-012.
- **Headings:** a heading that names only a grouping over several capabilities is `out` (R25.1), and Guides and Reference take CM-DVT-001 (R25.3).
- **Shop's references** follow rule 11 and R49.2.
- **The CLI** follows SH-98's R98.1 to R98.3.

## The coordinator's check

Measured: 23.6 million tokens over 106 requests, about 274,000 an entry. The checker prints no problem.
- **Kept:** R25.1 to R25.8, which SH-26 keeps; the `CHANGES` line CM-PAY-014 `extension-point` (Shop Pay Wallet offered for a developer's own checkout, R49.2); the correction of Mobile Support to CM-CHN-006 `extension-point`, as the cell reads the same objects' scopes; and `new:Timeline events` on its places of its own, the two API groups (to `amendment-notes.md`).
- **The reads beyond the selection** (`docs-front-matter`, `admin-graphql-reference-nav`, the source pages' descriptions): accepted, as held evidence read where a label leaves its thing open, the way R47.6 reads a card's linked page; each reading cites what it read. The second stage reads those structures whole.
- **The entries left open** (App management, Common objects, Cart's CM-CHK-002, Monitor orders' CM-ORD-001, Plus, Storefronts, App home): kept as placed.
