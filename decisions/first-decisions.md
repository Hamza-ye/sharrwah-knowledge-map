# Sharrwah's first decisions

These are the decisions every area of Sharrwah depends on: the concerns that cut across all areas, to be settled before any area is designed. For a new system, the first iteration of attribute-driven design does this: it sets the overall structure before any one part is designed (Cervantes & Kazman 2016).

They come from two sources only:
- **Shopify's own shape**, read in its evidence repository observed-sh at commit `04de369da9ac84ae530ae80a55749167ff4139d4`. Every link below is pinned to that commit.
- **Published practice** for platforms where many businesses share one system. Full references are at the end.

**How to read it**
- A sentence with a pinned link is a fact. The words in quotation marks are on the linked line.
- **Reading:** marks a reading. **Assumption:** marks an assumption.
- Each decision's *Depends on* line, and the order, are readings drawn from the facts above them.
- A count without a quote (such as *31 types*) was counted by this review in the linked file.
- Some lines in the evidence are the capture's own descriptions (its register and reading guide), not Shopify's words. They are marked *the capture's*.
- Market specifics (one country's law, its providers, its currency's quirks) are left out. A first decision only makes a place where such values can go.

**The fifteen, in the order they can be settled**
1. The shop is the tenant
2. Areas and their borders
3. Where a shop lives
4. Who may act, and what they may do
5. Markets: the place for each market's values
6. One API for every area
7. Money
8. Language
9. Events and history
10. Custom data
11. Plans and the shop's state
12. Charges to the merchant
13. Fair use
14. Extensions
15. Personal data

---

## 1. The shop is the tenant

**Question:** What is the one unit that every record, request, job and event belongs to, so that no shop ever sees another shop's data?

**Why every area depends on it**
- The shop is the root of the admin API: "The central configuration and settings hub for a Shopify store." ([admin schema 2026-10, L3149](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3149)). Its fields lead to the shop's products, orders, customers, locations, staff members and channels (same line).
- Records belong to a shop, customers included: "Information about a customer of the shop" ([admin schema, L992](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L992)). So are apps: "An app installed on a shop." ([admin schema, L74](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L74)).
- Every call names one shop. Apps call "POST https://{shop}.myshopify.com/admin/api/" ([shopify.dev line, L2618](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/dev-access-lines/shopify.dev_md/items.jsonl?plain=1#L2618)). The admin's own calls carry the store in the path: "/api/operations/{hash}/Experiments/shopify/fake-demo-sharrwah" ([operations index, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/index/operations.jsonl?plain=1#L1)).
- Shopify's engineers: "we look at data in the context of the merchant's store", "we split everything by shop", including "Asynchronous events"; "every table in a podded database is connected to a shop", and "the link helps us avoid having data leaks between shops" ([Shopify-Made Patterns in Our Rails Apps, 2021, L222](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L222)).
- A shop "is the identifying entity for most data models", and its id is attached "to all shop-owned tables and have it serve as a sharding key" ([Shard Balancing, 2021, L210](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L210)).

**Reading:** every area keys its data, requests, jobs and events on the shop. If the tenant were settled after an area, that area would have to be redone.

**Practice:** Chong, Carraro & Wolter 2006 set out the tenancy options, from a database per tenant to one shared schema where each row carries its tenant's ID and every query is filtered by it. Kabbedijk et al. 2015 define multi-tenancy as tenants sharing one system's resources while each can configure it for itself. AWS 2022 carries the tenant's context through every layer.

**Depends on:** nothing.

## 2. Areas and their borders

**Question:** How is the platform divided into areas, and how may one area use another area's data and functions?

**Why every area depends on it**
- "We chose to evolve Shopify into a modular monolith, meaning that we would keep all of the code in one codebase, but ensure that boundaries were defined and respected between different components." ([Deconstructing the Monolith, 2019, L338](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L338))
- The components follow the business: "The goal was to re-organize it by real-world concepts (like orders, shipping, inventory, and billing)" ([same post, L338](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L338)).
- Shopify publishes the tool that holds the borders: "Packwerk is a Ruby gem used to enforce boundaries and modularize Rails applications." ([packwerk README, L8](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/packwerk/main@31e534283f93/files/packwerk-31e534283f93a225b520cddab3c2d735557c76de/README.md?plain=1#L8)).
- The admin's staff permissions are grouped by the same areas: 21 categories, from Home and Orders to "App and sales channel permissions" ([permission categories, L21](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-permission-tree/use-store-options-f948ecd551d0/categories.jsonl?plain=1#L21)).

**Reading:** each later decision is a rule every area follows. This one says what an area is, and that areas meet only through each other's published interfaces, never through each other's tables.

**Practice:** Cervantes & Kazman 2016: the first iteration for a new system chooses its overall structure. Parnas 1972: divide a system by the decisions likely to change, each hidden behind an interface. Evans 2003: bounded contexts, each with its own model and explicit relations to the others.

**Depends on:** nothing.

## 3. Where a shop lives

**Question:** Where do a shop's data and work run, how is each request sent there, and how is a shop moved, so that shops fail apart rather than together?

**Why every area depends on it**
- "A pod consists of a set of shops that live on a fully isolated set of datastores." Beyond that, "all shared resources can only ever communicate to a single pod at a time" ([A Pods Architecture To Allow Shopify To Scale, 2018, L369](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L369)).
- "Sorting Hat matches every request to a pod and adds a header to that request." and "We assigned each pod a pair of data centers" ([same post, L369](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L369)).
- "Each pod runs Shopify independently, with a database containing a portion of our shops." and "If one pod shuts down temporarily, the other pods" carry on ([Shopify-Made Patterns, L222](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L222)).
- Shops are moved whole: "Moving a shop from one shard to another involves selecting all records from all tables that have the desired" shop id ([Shard Balancing, L210](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L210)).

**Reading:** the shop (decision 1) is the unit of placement. So every area's data must move with its shop, and no area may join data across pods. The pod's location is also the place where a market's rule on where data is held can later go.

**Practice:** AWS 2023: cells, each serving a slice of customers chosen by a partition key, behind a thin router. AWS 2020: silo, pool and bridge models for keeping tenants' resources apart. Helland 2007: scale by entities with unique keys, which can be moved, and no transactions across them. Homer et al. 2014: the Sharding pattern.

**Depends on:** 1.

## 4. Who may act, and what they may do

**Question:** Who can act on a shop (people, through an account and an organization; apps, through an installation), and how does one permission model cover every area?

**Why every area depends on it**
- "An organization is a grouping of multiple stores with shared settings." With it "you can manage them more efficiently with centralized users and billing" ([Help Center: Managing stores in your organization, L6](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-orgs-and-stores/manage-orgs.md?plain=1#L6)).
- "A role represents a staff member's job, and contains all the granular permissions that a user requires to do that job." ([Help Center: Roles, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/users/roles.md?plain=1#L3)). Shopify names the model: "Migrating to the role-based access control model" ([same page, L13](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/users/roles.md?plain=1#L13)).
- "Permissions grant or restrict access to specific areas of your business for a specific context." ([Help Center: Permissions, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/users/roles/permissions.md?plain=1#L3))
- One tree covers every area: 21 categories and "142 permissions with their StaffMemberPermission ids and titles" (*the capture's* register, [REGISTER, L132](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/REGISTER.tsv?plain=1#L132)). A role can reach several stores: one "can perform all Point of Sale actions across all stores" ([admin roles, L10](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-roles/ctcbwa-r1/items.jsonl?plain=1#L10)).
- Apps get scopes, not roles. A scope says what data an app "can read or write, following the format" of an action and a resource ([admin schema, L21](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L21)). "Only request as much data access as your app needs to work." ([shopify.dev line, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/dev-access-lines/shopify.dev_md/items.jsonl?plain=1#L1))
- The install screen lists an app's access by area: "Customers, products, orders, discounts, store analytics, staff accounts, Online Store, custom data" ([app install consent, L14](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/app-install-consent/collabs@capture-plus/items.jsonl?plain=1#L14)).

**Reading:** every area must name its actions in this one model (for staff) and in scopes (for apps) as it is designed. The organization sits above the shop and holds people and billing.

**Practice:** Sandhu et al. 1996 and ANSI INCITS 359-2004: role-based access control. RFC 6749 (2012): access delegated to a client and limited by scopes. AWS 2022: identity binds each user to a tenant, so the tenant's context reaches every authorization check.

**Depends on:** 1, 2.

## 5. Markets: the place for each market's values

**Question:** What is a market, how is a buyer matched to one, and which of the shop's settings can a market hold differently?

**Why every area depends on it**
- A market is "A merchant-defined group of buyers identified by conditions" ([admin schema, L1951](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1951)). Its kinds are region, location, company location and channel ([admin schema, L2004](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2004)). Its fields hold catalogs, currency settings, price inclusions, delivery, discounts, a return policy, web presences, and parent and child markets (L1951).
- "Conditions: Conditions define who your market applies to." ([Help Center: Markets overview, L7](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/overview.md?plain=1#L7)) "Customizations: Customizations define your store experience for the customers in that market" ([same page, L8](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/overview.md?plain=1#L8)).
- Markets inherit and override: "their market customizations inherit your store's default settings" ([same page, L84](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/overview.md?plain=1#L84)). "You can override inherited values and customize the following aspects of your store:" ([same page, L86](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/overview.md?plain=1#L86)). The list that follows covers currency, catalogs, theme, domain and language, duties and tax, and business entities (L88 to L93).
- The API resolves a buyer to one set of values: "Resolved values include the resolved catalogs, web presences, currency, and price inclusivity." ([admin schema, L2058](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2058))
- Other areas hold market values the same way. Checkout: "modifies a parent configuration for specific markets" ([admin schema, L525](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L525)). Prices: "Price lists override default product prices with either fixed prices or percentage-based adjustments." ([admin schema, L2551](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2551)) Tax-inclusive prices: "The inclusive pricing strategy for a market." ([admin schema, L1987](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1987)) The seller: "A legal entity through which a merchant operates." ([admin schema, L217](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L217))
- The market reaches extension code and storefronts. Each Function receives "Details about the localized experience for the store in a specific region, including country and language" with its market; the inputs of all 13 Functions APIs hold it ([Functions schema, discount 2026-10, L75](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/functions-graphql-schema/discount/2026-10/items.jsonl?plain=1#L75)). Storefront fields "reflect the active localization context" ([storefront schema 2026-10, L213](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/storefront-graphql-schema/2026-10/items.jsonl?plain=1#L213)).

**Reading:** the market is where every market's values go: currency, languages, domain, tax inclusion, duties, the selling legal entity, catalog and prices, checkout settings. Each value inherits from the shop unless the market sets it. Each area must say which of its settings a market may hold, and read them through the resolved context, never from the shop directly. No market's own values are decided here.

**Practice:** Krebs, Momm & Kounev 2012 name per-tenant customization among the architectural concerns of multi-tenant applications. Mietzner et al. 2009: model the points where customers vary, then bind values to them. Esselink 2000: internationalize first (build places for local values), then localize for each market. Country codes follow ISO 3166-1:2020, as Shopify's do: "which generally follows ISO 3166-1 alpha-2 guidelines" ([admin schema, L978](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L978)).

**Depends on:** 1.

## 6. One API for every area

**Question:** What single, versioned contract does every area expose (to the admin, apps and storefronts alike), and how is every object named across areas?

**Why every area depends on it**
- One graph: "This acts as the public, top-level API from which all queries must start." ([admin schema, L2804](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2804)). The 2026-10 version has "3716" types ([schema meta, L20](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/meta.json?plain=1#L20)).
- The admin uses the same API: "The admin calls its own API as persisted GraphQL operations" (*the capture's* reading guide, [READING, L41](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/docs/READING.md?plain=1#L41)).
- One calendar: "Shopify releases a new API version every three months at the beginning of the quarter" ([How Shopify Manages API Versioning and Breaking Changes, 2019, L315](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L315)). "Shopify APIs are versioned so that developers can better plan their development cycle." ([shopify.dev front matter, L6757](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl?plain=1#L6757)) The storefront schema and the "13 Functions APIs" are held by the same dated versions (*the capture's* register, [REGISTER, L23](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/REGISTER.tsv?plain=1#L23)).
- One way to name things: "An object with an ID field to support global identification" ([admin schema, L2272](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2272)). 221 types carry it. An ID reads like "gid://shopify/Article/569451675704" ([engineering blog data, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L1)). "Learn how global IDs work in Shopify APIs" ([shopify.dev front matter, L6751](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl?plain=1#L6751)).

**Reading:** every area must publish its reads and writes in this one contract, on one release calendar, naming its objects by global ID. Then the admin, apps, extensions and other areas all reach it the same way.

**Practice:** Medjaoui et al. 2018: versioning and change management across a platform's APIs. RFC 3986 (2005): globally unique names as URIs, the form Shopify's IDs take.

**Depends on:** 1, 2, 4.

## 7. Money

**Question:** How is every amount held: as what kind of number, with which currency, and in whose currency (the shop's, the buyer's, or both)?

**Why every area depends on it**
- "A precise monetary value and its associated currency." ([admin schema, L2266](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2266)). 119 types have a field of this type.
- "Used throughout the API for multi-currency pricing and transactions". The shop's half of the pair "contains the equivalent in the shop's base currency" ([admin schema, L2263](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2263)). 66 types hold this pair.
- "The currency codes that represent the world currencies throughout the Admin API." ([admin schema, L985](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L985)) Each market has "A market's currency settings." ([admin schema, L1968](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1968)), with a base currency, local currencies and rounding (same line). Functions receive a "presentmentCurrencyRate" ([Functions schema, discount input, L69](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/functions-graphql-schema/discount/2026-10/items.jsonl?plain=1#L69)).
- Shopify's open-source money library "encapsulates all information about a certain amount of money, such as its value and its currency" ([money README, L10](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/money/main@4d9b0127e5a2/files/money-4d9b0127e5a242a3343d67285a70c328556158eb/README.md?plain=1#L10)). It "Does NOT provide APIs for exchanging money from one currency to another." ([L13](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/money/main@4d9b0127e5a2/files/money-4d9b0127e5a242a3343d67285a70c328556158eb/README.md?plain=1#L13)) It "Will not lose pennies during divisions." ([L14](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/money/main@4d9b0127e5a2/files/money-4d9b0127e5a242a3343d67285a70c328556158eb/README.md?plain=1#L14))
- The platform's own plan prices use the same type: "MoneyV2" ([billing plans, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/billing-plans/2jiwxs-gr/items.jsonl?plain=1#L1)).

**Reading:** every area that prices, charges, pays or reports must hold amounts the same way. If each area chose for itself, orders, payments, discounts and payouts would disagree. Which currencies a market uses is that market's value (decision 5), not decided here.

**Practice:** Fowler 2002: the Money pattern, an amount with its currency, split without losing pennies. ISO 4217:2015: currency codes.

**Depends on:** 1, 5.

## 8. Language

**Question:** Which text can be translated, how is a translation stored, and how is the language chosen for a staff member or a buyer?

**Why every area depends on it**
- "A locale that's been enabled on a shop." ([admin schema, L3157](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3157)) "A localized version of a field on a resource." ([admin schema, L3616](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3616)), held with a locale and an optional market (same line). Wording can also differ per market: "The market localization of a field within a resource, which is determined by the market ID." ([admin schema, L1983](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1983))
- What can be translated reaches far beyond the catalog: 30 kinds of resource, including "EMAIL_TEMPLATE", "PACKING_SLIP_TEMPLATE", "PAYMENT_GATEWAY", "DELIVERY_METHOD_DEFINITION" and "METAFIELD" ([admin schema, L3615](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3615)). "Published translations associated with the resource." is carried by 19 types ([admin schema, L1724](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1724)).
- Buyers and staff both choose a language. Storefronts ask for "Supported languages for retrieving translated storefront content." ([storefront schema, L212](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/storefront-graphql-schema/2026-10/items.jsonl?plain=1#L212)). Each staff member has a locale ([admin schema, L3253](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3253)), and the admin itself is translated: "Lost in Translations: Bringing the World to Shopify" ([engineering blog, 2018, L355](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L355)).

**Reading:** every area that holds text a buyer or a staff member reads must store it so that a translation can sit beside it, per locale and, where needed, per market. Which languages a market uses is that market's value.

**Practice:** BCP 47 (RFC 5646, 2009): language tags. Esselink 2000: text kept apart from code so that it can be translated.

**Depends on:** 1, 5.

## 9. Events and history

**Question:** How does every area record what happened and who did it, and tell the other areas and apps?

**Why every area depends on it**
- "The supported topics for webhook subscriptions." ([admin schema, L3704](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3704)) There are 236 in 2026-10. The CLI's 230 topics span 72 kinds of resource, for example "orders/create" ([CLI webhook topics, L143](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/cli-webhook-topics/app-webhook-trigger@2026-10/items.jsonl?plain=1#L143)) and "markets/create" ([L131](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/cli-webhook-topics/app-webhook-trigger@2026-10/items.jsonl?plain=1#L131)).
- Use webhooks to "execute code after a specific event occurs in a shop" ([shopify.dev front matter, L7435](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl?plain=1#L7435)).
- History: "Events chronicle resource activities such as the creation of an article, the fulfillment of an order" ([admin schema, L1494](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1494)), with fields saying whether the event is attributed to an app or to a user (same line). "Represents an object that has a list of events." is carried by 17 types ([admin schema, L1718](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1718)). "Deletion events chronicle the destruction of resources" ([admin schema, L1144](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1144)). There is an audit topic: "audit_events/admin_api_activity" ([CLI webhook topics, L6](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/cli-webhook-topics/app-webhook-trigger@2026-10/items.jsonl?plain=1#L6)).
- Events are split by shop, like requests and jobs (decision 1, L222).

**Reading:** each area must emit its events in one shared shape, per shop, saying which person or app acted. Otherwise apps, automation, notifications and analytics would need a different feed for each area.

**Practice:** Hohpe & Woolf 2003: event messages on publish-subscribe channels, with guaranteed delivery. CloudEvents 1.0 (2019): one envelope for events from any source. NIST SP 800-92 (2006): records of who did what, kept and reviewed.

**Depends on:** 1, 4, 6.

## 10. Custom data

**Question:** How can merchants and apps add their own fields and types to any area's resources, with definitions that say what each field holds and who may see it?

**Why every area depends on it**
- "Represents information about the metafields associated to the specified resource." ([admin schema, L1722](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1722)) 31 types carry it, from products and orders to markets, locations and the shop itself. There are 26 kinds of owner: "Possible types of a metafield's owner resource." ([admin schema, L2163](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2163))
- A definition "Defines the structure, validation rules, and permissions for" metafields ([admin schema, L2120](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2120)). Whole new types are possible too: they "store reusable data that extends beyond Shopify's standard resources" ([admin schema, L2180](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2180)).
- Custom data is meant to "use it across the platform" ([shopify.dev front matter, L7058](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl?plain=1#L7058)). It has its own permission category, "Metaobjects", titled Content ([permission categories, L10](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-permission-tree/use-store-options-f948ecd551d0/categories.jsonl?plain=1#L10)), and its own entitlement, "metaobjects" ([shop request details, L31](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/shop-request-details/capture-grow/items.jsonl?plain=1#L31)). It is translatable: "METAFIELD" is one of the translatable kinds ([admin schema, L3615](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3615)). It is also one of the access groups an app asks for (decision 4).

**Reading:** every area's resources must accept custom fields the same way. The API, translations, permissions and privacy must then treat them like built-in fields.

**Practice:** Chong, Carraro & Wolter 2006: extensibility patterns for tenant-specific fields (pre-allocated fields, name-value pairs, custom columns). Aulbach et al. 2008: mapping each tenant's extensions onto shared tables. Weissman & Bobrowski 2009: custom objects and fields kept as metadata over shared tables.

**Depends on:** 1, 4, 6, 8.

## 11. Plans and the shop's state

**Question:** How do a shop's plan and state decide what each area lets it do, and how much of it, and where is that checked?

**Why every area depends on it**
- "The shop's billing plan and subscription details." ([admin schema, L3178](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3178)) "Represents the feature set available to the shop." ([L3156](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3156)) "Resource limits of a shop." ([L3188](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3188)) "The shop's entitlements." ([L1489](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1489))
- The admin asks for them on every page: "every admin page loads it" (*the capture's* register, [REGISTER, L131](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/REGISTER.tsv?plain=1#L131)). For one store they hold the plan, "professional" ([shop request details, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/shop-request-details/capture-grow/items.jsonl?plain=1#L1)). They also hold entitlements for most areas: "inventory" ([L20](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/shop-request-details/capture-grow/items.jsonl?plain=1#L20)), "checkoutExtensibility" ([L22](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/shop-request-details/capture-grow/items.jsonl?plain=1#L22)), "markets" ([L29](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/shop-request-details/capture-grow/items.jsonl?plain=1#L29)) and "maximumLocations" ([L30](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/shop-request-details/capture-grow/items.jsonl?plain=1#L30)), and further down shipping, tax, POS, finance and app development.
- Six plans, each with a monthly and an annual price ([billing plans, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/billing-plans/2jiwxs-gr/items.jsonl?plain=1#L1) to L6).
- A shop's state changes every channel at once: "your checkout is deactivated across all sales channels" ([Help Center: Pausing your store, L5](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-orgs-and-stores/manage-pricing-plan/pause-store.md?plain=1#L5)).
- The plan also shapes access and markets: roles "depend on whether your store is part of an organization, on the Shopify Plus plan" ([Help Center: Roles, L9](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/users/roles.md?plain=1#L9)). On the Basic, Grow and Advanced plans "you can assign up to 3 active catalogs across all your B2B markets" ([Help Center: Markets overview, L31](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/overview.md?plain=1#L31)).

**Reading:** each area must ask one place whether a shop may use a feature, and how much of it. If plan checks were scattered through the areas, plans could not be changed.

**Practice:** Hodgson 2017: permissioning toggles that turn features on for some customers, such as paying ones. AWS 2020: tier-based isolation. Golding 2024: tiers and tenant management.

**Depends on:** 1, 4, 7.

## 12. Charges to the merchant

**Question:** How does every area that costs the merchant money put its charges on one bill, and how is usage counted?

**Why every area depends on it**
- The bill's charge categories come from many areas, 37 choices in all, All first: "APPLICATION_FEE" ([charge categories, L2](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/billing-charge-categories/fake-demo-sharrwah@expense-report/items.jsonl?plain=1#L2)), "SUBSCRIPTION_FEE" ([L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/billing-charge-categories/fake-demo-sharrwah@expense-report/items.jsonl?plain=1#L3)), "SHIPPING_FEE" ([L4](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/billing-charge-categories/fake-demo-sharrwah@expense-report/items.jsonl?plain=1#L4)), "ORDER_COMMISSION" ([L5](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/billing-charge-categories/fake-demo-sharrwah@expense-report/items.jsonl?plain=1#L5)), "DOMAIN_FEE" ([L9](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/billing-charge-categories/fake-demo-sharrwah@expense-report/items.jsonl?plain=1#L9)), "SHOPIFY_EMAIL" ([L16](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/billing-charge-categories/fake-demo-sharrwah@expense-report/items.jsonl?plain=1#L16)), "POS_FEE" ([L21](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/billing-charge-categories/fake-demo-sharrwah@expense-report/items.jsonl?plain=1#L21)) and "THEME_FEE" ([L36](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/billing-charge-categories/fake-demo-sharrwah@expense-report/items.jsonl?plain=1#L36)).
- Apps bill merchants through the platform: "The pricing structure can include recurring charges, usage-based pricing, or both." ([admin schema, L101](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L101)) "Store usage for app subscriptions with usage pricing." ([admin schema, L127](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L127))
- The bill can sit with the organization: "organizationBilling" decides which settings permissions a store shows ([permission categories, L19](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-permission-tree/use-store-options-f948ecd551d0/categories.jsonl?plain=1#L19)). Organizations bring "centralized users and billing" ([Help Center: organizations, L6](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-orgs-and-stores/manage-orgs.md?plain=1#L6)).

**Reading:** each area that charges must report its usage the same way, into one ledger, in the money form of decision 7. Otherwise each area invents its own billing.

**Practice:** AWS 2022: billing and metering as control-plane services fed by each tenant's usage. Golding 2024: metering and billing.

**Depends on:** 1, 4, 7, 9, 11.

## 13. Fair use

**Question:** How is one shop's or one app's load kept from hurting the others: which limits apply, how are they counted, and what happens at the limit?

**Why every area depends on it**
- "Rate limiting is a system that protects the stability of APIs." Among the reasons: "Bad actors abusing the API by sending too many requests." ([Rate Limiting GraphQL APIs by Calculating Query Complexity, 2021, L228](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L228))
- "The limits that apply across Shopify's APIs" ([shopify.dev front matter, L6753](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl?plain=1#L6753)), including "the resource-based throttles that apply to large stores" ([L6780](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl?plain=1#L6780)).
- API answers carry a cost field, which the capture calls "the API's cost and rate-limit counter" (*the capture's* reading guide, [READING, L29](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/docs/READING.md?plain=1#L29)). Shops have limits of their own, such as "maxProductVariants" ([shop request details, L9](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/shop-request-details/capture-grow/items.jsonl?plain=1#L9)).

**Reading:** every area's operations must carry a cost under one model. Pods (decision 3) keep failures apart; these limits keep load apart inside a pod.

**Practice:** Homer et al. 2014: the Throttling pattern. Krebs, Momm & Kounev 2012: performance isolation between tenants. Weissman & Bobrowski 2009: governor limits on customer code that runs on the shared platform.

**Depends on:** 1, 3, 6, 11.

## 14. Extensions

**Question:** Where, in every area, can outside developers add screens, logic and data; through what; and under which limits and terms?

**Why every area depends on it**
- "A Shopify application that extends store functionality." ([admin schema, L62](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L62)) "Each installation tracks the permissions granted to the app through" its scopes, along with its billing subscriptions and metafields ([admin schema, L74](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L74)).
- Screens in every surface: 82 admin targets, such as "admin.product-details.block.render" ([admin targets, L2](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/ui-extension-targets/admin@2026.10.2/items.jsonl?plain=1#L2)) and "admin.order-details.block.render" ([L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/ui-extension-targets/admin@2026.10.2/items.jsonl?plain=1#L3)); 64 checkout targets, such as "purchase.checkout.actions.render-before" ([checkout targets, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/ui-extension-targets/checkout@2026.10.2/items.jsonl?plain=1#L1)); 24 customer account targets, such as "customer-account.order-status.block.render" ([customer account targets, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/ui-extension-targets/customer-account@2026.10.2/items.jsonl?plain=1#L1)); and 33 POS targets, such as "pos.home.tile.render" ([POS targets, L2](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/ui-extension-targets/point-of-sale@2026.10.2/items.jsonl?plain=1#L2)).
- Logic in many areas: "13 Functions APIs" (*the capture's* register, [REGISTER, L23](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/REGISTER.tsv?plain=1#L23)), held as cart validation, cart transform, delivery and payment customization, discounts, fulfillment constraints and order routing. Each Function receives the shop and its "localization", in the inputs of all 13 ([Functions schema, discount input, L69](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/functions-graphql-schema/discount/2026-10/items.jsonl?plain=1#L69)).
- Sales channels are apps too. A publication is a set of products and collections "that are published to an app" ([admin schema, L2762](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2762)). The permission tree ends with "App and sales channel permissions" ([permission categories, L21](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-permission-tree/use-store-options-f948ecd551d0/categories.jsonl?plain=1#L21)).

**Reading:** every area must decide, while it is designed, where apps can add a screen, change a calculation, or attach data. Adding extension points afterwards means redesigning the area.

**Practice:** Bosch 2009: a platform opened to outside developers becomes a software ecosystem. Baldwin & Woodard 2009: a platform is a stable core with interfaces through which outside parts vary. Weissman & Bobrowski 2009: customer and partner code running inside the shared platform under limits.

**Depends on:** 4, 5, 6, 9, 10, 12.

## 15. Personal data

**Question:** How does every area mark the personal data it holds, so that one person's data can be found, exported or erased everywhere at once, apps included?

**Why every area depends on it**
- Public apps must handle "customers/data_request" ([CLI webhook topics, L46](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/cli-webhook-topics/app-webhook-trigger@2026-10/items.jsonl?plain=1#L46)), "customers/redact" ([L52](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/cli-webhook-topics/app-webhook-trigger@2026-10/items.jsonl?plain=1#L52)) and "shop/redact" ([L205](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/cli-webhook-topics/app-webhook-trigger@2026-10/items.jsonl?plain=1#L205)): "Set up mandatory compliance webhooks that the Shopify platform requires for public apps." ([shopify.dev front matter, L7057](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl?plain=1#L7057))
- One request reaches every place the data went: a merchant can erase a customer's personal data from the store and "from any apps and channels that you've installed" ([Help Center: Customer data requests, L25](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/privacy-and-security/privacy/processing-customer-data-requests.md?plain=1#L25)).
- Erasure and data requests are permissions of their own: "ERASE_CUSTOMER_DATA" and "REQUEST_CUSTOMER_DATA" ([admin schema, L3257](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3257)). A change of consent is an event: "customers_email_marketing_consent/update" ([CLI webhook topics, L54](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/cli-webhook-topics/app-webhook-trigger@2026-10/items.jsonl?plain=1#L54)).
- Shopify's engineers: "The privacy context specifically includes marking sensitive data, identifying data subjects, and handling PII" ([Schematizing Deletion at Scale, 2021, L231](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L231)).
- The law is the merchant's to meet, wherever they sell: "complying with the privacy and data protection laws and regulations that apply to your business" ([Help Center: Customer data requests, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/privacy-and-security/privacy/processing-customer-data-requests.md?plain=1#L3)).

**Reading:** each area must mark, as it is designed, which of its fields are personal and whose they are. The platform can then serve every market's law from one mechanism. Which law applies in a market is that market's value, not decided here.

**Practice:** Cavoukian 2009: privacy built into the design, as the default. ISO/IEC 27701:2019: managing personal data across a system. NIST Privacy Framework 1.0 (2020): identifying the data a system processes and governing it.

**Depends on:** 1, 4, 9, 10, 14.

---

## Their order

Decisions on the same step depend only on earlier steps, so they can be settled side by side.

| Step | Decisions | Why here |
| --- | --- | --- |
| 1 | 1 The shop is the tenant; 2 Areas and their borders | They depend on nothing. |
| 2 | 3 Where a shop lives; 4 Who may act; 5 Markets | Each needs only the tenant; access also needs the areas, since permissions are named by area. |
| 3 | 6 One API; 7 Money; 8 Language | The API is scoped by shop and scope. Money's second currency and a translation's market come from markets. |
| 4 | 9 Events and history; 10 Custom data; 11 Plans and state | Events and custom data take the API's shape and names. Plans need prices (money) and the organization (access). |
| 5 | 12 Charges; 13 Fair use | Charges count usage from events against plans. Limits are set per plan and per pod and counted per API call. |
| 6 | 14 Extensions | Apps act through access, the API, events, custom data, market context and charges. |
| 7 | 15 Personal data | It must reach every place personal data can go, apps and custom fields included. |

**Reading:** two decisions are roots: what a tenant is (1) and what an area is (2). Every other decision is a rule that every area follows inside one tenant.

## Concerns that look cross-cutting but aren't first decisions

Each line is a reading. Where it rests on Shopify's shape, the fact is cited.

- **Sales channels.** In Shopify a channel is an app with a publication ("that are published to an app", [admin schema, L2762](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2762)) and a kind of market ("CHANNEL", [admin schema, L2004](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2004)). Decisions 5 and 14 cover it.
- **B2B buyers.** A market condition with its own catalog and prices ("contextualize Storefront API queries with data like B2B-specific pricing", [storefront schema, L25](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/storefront-graphql-schema/2026-10/items.jsonl?plain=1#L25)). Decision 5 covers it; the rest is the customer and catalog areas' design.
- **Locations.** "A physical location where merchants store and fulfill inventory." ([admin schema, L1914](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1914)) A resource of the inventory and fulfilment areas that markets can use as a condition, not a rule every area follows.
- **Taxes and duties.** Each market's law. Decision 5 gives them their place (the market's price inclusions and legal entity); calculating them is an area's job.
- **Payment providers.** A market's setup. The place is the market's legal entity, which can carry its own payments account (decision 5).
- **Domains and URLs.** Part of a market's web presence, "which defines its SEO strategy" ([admin schema, L2009](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2009)), so decision 5 covers them.
- **Notifications (email, SMS).** An area built on events (9) and translations (8); email templates are one of the translatable kinds.
- **Search, analytics and reports.** They read every area through the API and events (6, 9). Each is an area.
- **Bulk import and export, background jobs.** "An asynchronous operation that exports large datasets or imports data in bulk." ([admin schema, L198](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L198)) A feature of the API (6), under fair use (13).
- **Files and media.** A shared service that areas refer to by ID (6). No area's model depends on how files are stored.
- **Time zone and units.** Values on the shop (its fields include its time zone, unit system and weight unit, [admin schema, L3149](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3149)), so they have a place under decision 1; how they display follows decision 8.
- **One buyer account across shops.** Shopify keeps that outside the shop's data, as a "relationship with Shopify through services like Shop and Shop Pay" ([Help Center: Customer data requests, L30](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/privacy-and-security/privacy/processing-customer-data-requests.md?plain=1#L30)). It is a product built beside the shops; each shop's customers stay the shop's (1).
- **Automation and the AI assistant.** Areas that act through the API, permissions and events (6, 4, 9), like any app.
- **The admin's look (design system).** It shapes how areas look, not what they hold or who may use them. It can be set with the first screen.
- **Feature previews and betas.** Temporary release switches, unlike plans (11). They shape no area's model.
- **Monitoring, logging and deploys.** Operating practice applied per pod (3). The history a merchant sees is decision 9.
- **Programming language and frameworks.** Shopify's choice does not fix any area's model. They can be chosen with the first area's build.

---

## Practice cited

- AWS (Amazon Web Services), *SaaS Tenant Isolation Strategies: Isolating Resources in a Multi-Tenant Environment*, whitepaper, 2020.
- AWS, *SaaS Architecture Fundamentals*, whitepaper, 2022.
- AWS, *Reducing the Scope of Impact with Cell-Based Architecture*, Well-Architected guidance, 2023.
- ANSI INCITS 359-2004, *Information Technology: Role Based Access Control*, 2004.
- Aulbach, S., Grust, T., Jacobs, D., Kemper, A., Rittinger, J., *Multi-Tenant Databases for Software as a Service: Schema-Mapping Techniques*, ACM SIGMOD, 2008.
- Baldwin, C. Y., Woodard, C. J., *The Architecture of Platforms: A Unified View*, in A. Gawer (ed.), *Platforms, Markets and Innovation*, Edward Elgar, 2009.
- Berners-Lee, T., Fielding, R., Masinter, L., *Uniform Resource Identifier (URI): Generic Syntax*, RFC 3986, IETF, 2005.
- Bosch, J., *From Software Product Lines to Software Ecosystems*, SPLC, 2009.
- Cavoukian, A., *Privacy by Design: The 7 Foundational Principles*, Information and Privacy Commissioner of Ontario, 2009.
- Cervantes, H., Kazman, R., *Designing Software Architectures: A Practical Approach*, Addison-Wesley, 2016.
- Chong, F., Carraro, G., Wolter, R., *Multi-Tenant Data Architecture*, Microsoft, 2006.
- CNCF (Cloud Native Computing Foundation), *CloudEvents* specification v1.0, 2019.
- Esselink, B., *A Practical Guide to Localization*, John Benjamins, 2000.
- Evans, E., *Domain-Driven Design: Tackling Complexity in the Heart of Software*, Addison-Wesley, 2003.
- Fowler, M., *Patterns of Enterprise Application Architecture*, Addison-Wesley, 2002.
- Golding, T., *Building Multi-Tenant SaaS Architectures*, O'Reilly, 2024.
- Hardt, D. (ed.), *The OAuth 2.0 Authorization Framework*, RFC 6749, IETF, 2012.
- Helland, P., *Life beyond Distributed Transactions: an Apostate's Opinion*, CIDR, 2007.
- Hodgson, P., *Feature Toggles (aka Feature Flags)*, martinfowler.com, 2017.
- Hohpe, G., Woolf, B., *Enterprise Integration Patterns*, Addison-Wesley, 2003.
- Homer, A., Sharp, J., Brader, L., Narumoto, M., Swanson, T., *Cloud Design Patterns: Prescriptive Architecture Guidance for Cloud Applications*, Microsoft patterns & practices, 2014.
- ISO 3166-1:2020, *Codes for the representation of names of countries and their subdivisions, Part 1: Country code*.
- ISO 4217:2015, *Codes for the representation of currencies*.
- ISO/IEC 27701:2019, *Extension to ISO/IEC 27001 and ISO/IEC 27002 for privacy information management*.
- Kabbedijk, J., Bezemer, C.-P., Jansen, S., Zaidman, A., *Defining multi-tenancy: A systematic mapping study on the academic and the industrial perspective*, Journal of Systems and Software, 2015.
- Kent, K., Souppaya, M., *Guide to Computer Security Log Management*, NIST SP 800-92, 2006.
- Krebs, R., Momm, C., Kounev, S., *Architectural Concerns in Multi-Tenant SaaS Applications*, CLOSER, 2012.
- Medjaoui, M., Wilde, E., Mitra, R., Amundsen, M., *Continuous API Management*, O'Reilly, 2018.
- Mietzner, R., Metzger, A., Leymann, F., Pohl, K., *Variability Modeling to Support Customization and Deployment of Multi-Tenant-Aware Software as a Service Applications*, PESOS workshop at ICSE, 2009.
- NIST, *Privacy Framework: A Tool for Improving Privacy through Enterprise Risk Management*, Version 1.0, 2020.
- Parnas, D. L., *On the Criteria To Be Used in Decomposing Systems into Modules*, Communications of the ACM, 1972.
- Phillips, A., Davis, M. (eds.), *Tags for Identifying Languages*, BCP 47 (RFC 5646), IETF, 2009.
- Sandhu, R., Coyne, E., Feinstein, H., Youman, C., *Role-Based Access Control Models*, IEEE Computer, 1996.
- Weissman, C. D., Bobrowski, S., *The Design of the Force.com Multitenant Internet Application Development Platform*, ACM SIGMOD, 2009.
