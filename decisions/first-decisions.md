# Sharrwah's first decisions

Reviewed on 1 November 2026 by three reviewers, who wrote none of it.
Their findings are applied here.

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

**The sixteen, in the order they can be settled**
1. The unit of tenancy
2. Areas and their borders
3. Where a shop lives, and consistency within it
4. Who may act, and what they may do
5. Markets
6. Card data
7. APIs and IDs
8. Money
9. Language
10. Events and history
11. Custom data
12. Plans and the shop's state
13. Charges to the merchant
14. Fair use
15. Extensions
16. Personal data and retention

---

## 1. The unit of tenancy

**Question:** What is the unit of tenancy, and what data sits above it or outside it?

**Why every area depends on it**
- The shop is the root of the admin API: "The central configuration and settings hub for a Shopify store." ([admin schema 2026-10, L3149](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3149)).
- Shopify's engineers: "we split everything by shop", including "Asynchronous events", and "the link helps us avoid having data leaks between shops" ([Shopify-Made Patterns in Our Rails Apps, 2021, L222](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L222)). A shop "is the identifying entity for most data models" ([Shard Balancing, 2021, L210](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L210)).
- People sit above the shop: "A Shopify ID belongs to an individual user, and not to a store." ([Help Center: Shopify ID, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/logging-in/sso-migration-guide.md?plain=1#L3))
- One identifier follows each request: "it's useful to pass along some sort of correlation identifier" ([Resilient Payment Systems, 2022, L132](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L132)).

**Reading:** most of every area's data, requests, jobs and events key on the shop, and each request carries one identifier through every area. People and organizations (decision 4) sit above the shop.

**Practice:** Kabbedijk et al. 2015: tenants share one system's resources, each configuring it for itself. AWS 2022 carries the tenant's context through every layer.

**Depends on:** nothing. **Needed first:** all but the logging tools; Shopify later rebuilt keys around the shop: "we create a composite primary key [shop_id, order_id]" ([Composite Primary Keys, 2020, L270](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L270)).

## 2. Areas and their borders

**Question:** How is the platform divided into areas, and how may one area use another area's data and functions?

**Why every area depends on it**
- Shopify chose "a modular monolith", to "ensure that boundaries were defined and respected between different components", organized "by real-world concepts (like orders, shipping, inventory, and billing)" ([Deconstructing the Monolith, 2019, L338](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L338)).
- Its tool for them, Packwerk, is "used to enforce boundaries" ([packwerk README, L8](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/packwerk/main@31e534283f93/files/packwerk-31e534283f93a225b520cddab3c2d735557c76de/README.md?plain=1#L8)). By 2024 Shopify credits it only with "holding the line against new dependencies at the base layer" ([A Packwerk Retrospective, 2024, L55](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L55)), and "our database is still common for all domains" ([Shopify-Made Patterns, L222](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L222)).

**Reading:** each later decision is a rule every area follows; this one says what an area is and how one area may use another's data. In Shopify the borders were an aim; the database stayed shared.

**Practice:** Cervantes & Kazman 2016: a new system's first iteration sets its overall structure. Parnas 1972: modules that each hide a decision likely to change. Evans 2003: bounded contexts, each with its own model and explicit relations to others.

**Depends on:** nothing. **Needed first:** the rule for using another area's data, which cost Shopify "many months of hard work" for one package ([L55](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L55)); the list of areas can wait, "as late as possible" ([L338](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L338)).

## 3. Where a shop lives, and consistency within it

**Question:** How are tenants' data and work placed, how far must one tenant's load or failure be kept from others, and how are a tenant's records kept consistent?

**Why every area depends on it**
- "A pod consists of a set of shops that live on a fully isolated set of datastores." ([A Pods Architecture To Allow Shopify To Scale, 2018, L369](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L369)). Shops move whole, "selecting all records from all tables that have the desired" shop id ([Shard Balancing, L210](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L210)).
- Related records share one database, to "wrap everything in ACID transactions" ([Redis to MySQL for inventory reservations, 2026, L20](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L20)). Writes are safe to repeat, by "API level idempotency" ([Idempotency, 2019, L325](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L325)), and replica reads keep "a form of monotonic read consistency" ([Read Consistency, 2021, L249](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L249)).
- Each team writes "a user-centric resiliency matrix" for failures ([Resiliency Planning, 2020, L259](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L259)).

**Reading:** the shop (decision 1) is the unit of placement. So every area's data moves with its shop, no area joins data across pods, no transaction spans shops, and each area states how it behaves when a dependency fails.

**Practice:** Chong, Carraro & Wolter 2006: tenancy options, from a database per tenant to a shared schema whose rows carry the tenant's ID. AWS 2023: cells chosen by a partition key, behind a thin router. AWS 2020: silo, pool and bridge models. Helland 2007: movable entities with unique keys, and no transactions across them. Homer et al. 2014: the Sharding pattern.

**Depends on:** 1, 2. **Needed first:** these rules; the placement mechanism can wait, as Shopify sharded only when "it was no longer possible to continue buying a larger database server" ([L369](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L369)).

## 4. Who may act, and what they may do

**Question:** Who can act on a tenant's data, and how is each actor's access stated and checked?

**Why every area depends on it**
- An organization is "a grouping of multiple stores with shared settings", with "centralized users and billing" ([Help Center: Managing stores in your organization, L6](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-orgs-and-stores/manage-orgs.md?plain=1#L6)).
- A role "contains all the granular permissions that a user requires to do that job" ([Help Center: Roles, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/users/roles.md?plain=1#L3)). Permissions "grant or restrict access to specific areas of your business" ([Help Center: Permissions, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/users/roles/permissions.md?plain=1#L3)).
- The "admin staff permission selector" holds 21 categories and "142 permissions with their StaffMemberPermission ids and titles" (*the capture's* register, [REGISTER, L132](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/REGISTER.tsv?plain=1#L132)). Beside it sit "Organization-level permissions" and "Shopify POS app-level permissions" ([Help Center: Permissions, L6-L7](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/users/roles/permissions.md?plain=1#L6-L7)).
- Apps get scopes, not roles: what data an app "can read or write, following the format" of an action and a resource ([admin schema, L21](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L21)).

**Reading:** every area names its actions as permissions (for staff) and scopes (for apps) as it is designed: one role mechanism, several permission sets. The organization sits above the shop and holds people and billing.

**Practice:** Sandhu et al. 1996 and ANSI INCITS 359-2012: role-based access control. RFC 6749 (2012): access delegated to a client and limited by scopes. AWS 2022: identity binds each user to a tenant, whose context reaches every authorization check.

**Depends on:** 1, 2. **Needed first:** each area's permissions and scopes; roles and one login across shops can wait, at a migration's cost: roles came "instead of assigning permissions directly" ([Help Center: Migrating to roles, L6](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/users/roles/migrate-to-roles.md?plain=1#L6)), and it isn't easy to "go back to separate logins" ([Help Center: Shopify ID, L37](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/logging-in/sso-migration-guide.md?plain=1#L37)).

## 5. Markets

**Question:** Where do values that differ by market live, and is a market a place Sharrwah is set up in, with its own providers, law and limits, a group of buyers a shop sells to, or both?

**Why every area depends on it**
- In Shopify a market is "A merchant-defined group of buyers identified by conditions" ([admin schema, L1951](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1951)); its kinds are region, location, company location and channel ([admin schema, L2004](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2004)).
- Its values "inherit your store's default settings" ([Help Center: Markets overview, L84](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/overview.md?plain=1#L84)) unless overridden, for currency, catalogs, theme, domain and language, duties and tax, and business entities (L88 to L93). "Resolved values include the resolved catalogs, web presences, currency, and price inclusivity." ([admin schema, L2058](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2058))
- Other values follow the store's own country: "which payment gateways are available in your store's location" ([Help Center: gateway availability, L7](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/payment-gateway-availability.md?plain=1#L7)), and "Changing your store's country might affect the following details:", including "Your tax and duty obligations." and "Your access to Shopify products and services." ([Help Center: store details, L56-L62](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-orgs-and-stores/manage-store-details.md?plain=1#L56-L62)). A market reaches payment processing only when "assigned to a business entity to determine payment processing" ([admin schema, L217](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L217)).

**Reading:** in Shopify a market is a group of buyers whose values inherit from the shop, while providers, tax and duty obligations and access follow the store's country. Each area says which of its values differ by market and reads them from one resolved place. No market's own values are decided here.

**Practice:** Esselink 2000: internationalize first (build places for local values), then localize for each market. Country codes follow ISO 3166-1:2020, as Shopify's do: "which generally follows ISO 3166-1 alpha-2 guidelines" ([admin schema, L978](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L978)).

**Depends on:** 1. **Needed first:** a place for each market's providers, law and limits, before any area holds them; buyers' markets can wait: Shopify's monolith dates from "at least 2006" ([L277](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L277)), its Markets from "February 11, 2022" ([merchant changelog, L1229](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl?plain=1#L1229)).

## 6. Card data

**Question:** Which areas may hold card data, and how is it kept apart from the rest?

**Why every area depends on it**
- The buyer types the card number into a frame on a separate host: "checkout.pci.shopifyinc.com/build/09497de/number-ltr.html" ([buyer checkout journey, L6](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/raw/runs/20260930T025107Z-journey-buyer-checkout/actions.jsonl?plain=1#L6)). One service holds the data: "the payment service that handles sensitive credit card data" ([Resilient Payment Systems, L132](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L132)).
- "Shopify's Services comply with PCI DSS." ([Terms of Service, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/legal-documents/20260930T081039Z-shopify-legal-documents/items.jsonl?plain=1#L1)) Shopify attests to the results of "its annual PCI DSS compliance assessment" ([Help Center: compliance reports, L20](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/privacy-and-security/account-security/compliance-reports.md?plain=1#L20)).

**Reading:** which areas may ever hold card data shapes checkout, payments, orders, events and extensions.

**Practice:** PCI DSS, the standard Shopify names.

**Depends on:** 2. **Needed first:** all of it, before checkout, payments, orders, events or extensions are designed.

## 7. APIs and IDs

**Question:** Through which contract or contracts do areas expose their reads and writes, how do those contracts change over time, and how is an object identified across areas?

**Why every area depends on it**
- Shopify has several APIs, "admin, customer, storefront, partner, payments-apps, 13 Functions APIs", on the same versions (*the capture's* register, [REGISTER, L23](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/REGISTER.tsv?plain=1#L23)). The storefront has its own root: "The entry point for all Storefront API queries." ([storefront schema, L310](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/storefront-graphql-schema/2026-10/items.jsonl?plain=1#L310)) One calendar: "Shopify releases a new API version every three months at the beginning of the quarter" ([How Shopify Manages API Versioning and Breaking Changes, 2019, L315](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L315)).
- One way to name things: "An object with an ID field to support global identification" ([admin schema, L2272](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2272)). 221 types carry it. An ID reads like "gid://shopify/Article/569451675704" ([engineering blog data, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L1)).
- One search syntax, "in GraphQL query arguments, REST query parameters, webhook filters, and the admin." ([shopify.dev front matter, L6756](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl?plain=1#L6756)); 79 of the 298 admin root queries take a query argument ([admin schema, L2804](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2804)).

**Reading:** every area must publish its reads and writes in the platform's contracts, on one release calendar, naming its objects by global ID and filtering with one search syntax.

**Practice:** Medjaoui et al. 2018: versioning and change management across a platform's APIs. RFC 3986 (2005): names as URIs, the form Shopify's IDs take; Shopify itself follows "the Relay specification" ([storefront schema, L259](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/storefront-graphql-schema/2026-10/items.jsonl?plain=1#L259)).

**Depends on:** 1, 2, 4. **Needed first:** the ID scheme, since Shopify still carries a second ID on types that "directly correspond to a REST Admin API resource" ([admin schema, L1886](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1886)); the calendar can wait for outside apps: Shopify "released the first official version" in 2019 ([L315](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L315)).

## 8. Money

**Question:** How is every amount held: as what kind of number, with which currency, and in whose currency (the shop's, the buyer's, or both)?

**Why every area depends on it**
- "A precise monetary value and its associated currency." ([admin schema, L2266](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2266)). 119 types have a field of this type, and plan prices use it: "MoneyV2" ([billing plans, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/billing-plans/2jiwxs-gr/items.jsonl?plain=1#L1)).
- "Used throughout the API for multi-currency pricing and transactions". The shop's half of the pair "contains the equivalent in the shop's base currency" ([admin schema, L2263](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2263)). 66 types hold this pair.
- "The currency codes that represent the world currencies throughout the Admin API." ([admin schema, L985](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L985)) Each market has "A market's currency settings." ([admin schema, L1968](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1968)), with a base currency, local currencies and rounding (same line).

**Reading:** every area that prices, charges, pays or reports must hold amounts the same way, or orders, payments, discounts and payouts would disagree. A market's currencies are its own value (decision 5).

**Practice:** Fowler 2002: the Money pattern, an amount with its currency, split without losing pennies. ISO 4217:2015: currency codes; Shopify's list is wider, with "legacy codes, and non- standard codes" ([web pixels reference, L21](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/web-pixel-events/shopify.dev@2026-09-30/items.jsonl?plain=1#L21)).

**Depends on:** 1, 5. **Needed first:** all of it, before the first area holding an amount, nearly every commerce area (119 types, above); a market's currencies and rounding can wait.

## 9. Language

**Question:** Which text can be translated, how is text kept in more than one language, and how is the language chosen for a staff member or a buyer?

**Why every area depends on it**
- "A locale that's been enabled on a shop." ([admin schema, L3157](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3157)) "A localized version of a field on a resource." ([admin schema, L3616](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3616)), held with a locale and an optional market (same line).
- What can be translated reaches far beyond the catalog: 30 kinds of resource, including "EMAIL_TEMPLATE", "PAYMENT_GATEWAY" and "METAFIELD" ([admin schema, L3615](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3615)).
- Buyers and staff both choose a language. Storefronts ask for "Supported languages for retrieving translated storefront content.", a closed list of 144 codes such as "PT_BR" ([storefront schema, L212](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/storefront-graphql-schema/2026-10/items.jsonl?plain=1#L212)). Each staff member has a locale ([admin schema, L3253](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3253)).

**Reading:** every area that holds text a buyer or staff member reads stores it so a translation can sit beside it, per locale and, where needed, per market. A market's languages are its own value.

**Practice:** BCP 47 (RFC 5646, 2009): language tags, which Shopify's storefront codes are not. Esselink 2000: text kept apart from code so that it can be translated.

**Depends on:** 1, 5. **Needed first:** the rule that no text a buyer or staff member reads is fixed in code: Shopify "hardcoded thousands and thousands of English strings" for twelve years, then extracted them ([Lost in Translations, 2018, L355](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L355)); a market's languages can wait.

## 10. Events and history

**Question:** What record is kept of each change and of who made it, and how do other areas and apps learn of it?

**Why every area depends on it**
- History: "Events chronicle resource activities such as the creation of an article, the fulfillment of an order" ([admin schema, L1494](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1494)), with fields for whether an app or a user acted (same line). There is an audit topic: "audit_events/admin_api_activity" ([CLI webhook topics, L6](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/cli-webhook-topics/app-webhook-trigger@2026-10/items.jsonl?plain=1#L6)).
- Apps learn through webhooks: "The supported topics for webhook subscriptions." ([admin schema, L3704](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3704)), 236 in 2026-10, each subscription tied to an "apiVersion" ([L3694](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3694)). Inside, Shopify reads changes with "a log-based change-data capture (CDC) system" ([Capturing Every Change, 2021, L245](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L245)).
- An order keeps the sale as made: a line item "represents a single product or service that a customer purchased" and holds its own name, title and original unit price, while its links to the variant and product may be empty ([admin schema, L1889](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1889)). An order keeps both "originalTotalPriceSet" and "currentTotalPriceSet" ([L2306](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2306)).

**Reading:** each area records each change, per shop, with the person or app that made it, and keeps each sale as made; Shopify uses separate mechanisms for history, apps and its own systems.

**Practice:** Hohpe & Woolf 2003: event messages on publish-subscribe channels, with guaranteed delivery. CloudEvents 1.0 (2019): one envelope for events from any source. NIST SP 800-92 (2006): computer security logs, which fit the audit topic.

**Depends on:** 1, 4, 6, 7, 8. **Needed first:** recording each change, who made it, and each sale as made, since what is not recorded is lost ("any intermediate state is permanently lost"); delivery to apps can wait for extensions, and internal streams too: Shopify's change capture began "In mid-2019" ([L245](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L245)).

## 11. Custom data

**Question:** May merchants and apps add their own data to the platform's records, or their own kinds of record; if so, on which records, typed how, and who may read and change it?

**Why every area depends on it**
- "Represents information about the metafields associated to the specified resource." ([admin schema, L1722](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1722)) 31 of the "2123" object types carry it ([schema meta, L25](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/meta.json?plain=1#L25)), with owners of 26 kinds ([admin schema, L2163](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2163)).
- A definition "Defines the structure, validation rules, and permissions for" metafields ([admin schema, L2120](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2120)), but is optional: "These are metafields without definitions." ([Help Center: custom data, L12](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/custom-data/overview.md?plain=1#L12)) Custom data has its own permission category, "Metaobjects" ([permission categories, L10](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-permission-tree/use-store-options-f948ecd551d0/categories.jsonl?plain=1#L10)), and "METAFIELD" is a translatable kind ([admin schema, L3615](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3615)).

**Reading:** resources that take custom fields take them the same way, though in Shopify only 31 types do; the API, translations, permissions and privacy then treat them like built-in fields.

**Practice:** Chong, Carraro & Wolter 2006: extensibility patterns for tenant-specific fields (pre-allocated fields, name-value pairs, custom columns). Aulbach et al. 2008: mapping each tenant's extensions onto shared tables. Weissman & Bobrowski 2009: custom objects and fields kept as metadata over shared tables.

**Depends on:** 1, 4, 7, 9. **Needed first:** only the shared place on resources, and who may read and write it; Shopify added the rest later, "App-Owned Metafields" in 2022 ([Editions Summer '22, L157](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/editions/www.shopify.com_editions_summer2022_dev/items.jsonl?plain=1#L157)) and "custom data models with metaobjects" in 2023 ([Editions Winter '23, L619](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/editions/www.shopify.com_editions_winter2023/items.jsonl?plain=1#L619)).

## 12. Plans and the shop's state

**Question:** What decides what a shop may use, and how much, in each of its states, and where is that checked?

**Why every area depends on it**
- "The shop's billing plan and subscription details." ([admin schema, L3178](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3178)) "Represents the feature set available to the shop." ([L3156](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3156)) "Resource limits of a shop." ([L3188](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3188)) "The shop's entitlements." ([L1489](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1489)), which "every admin page loads" (*the capture's* register, [REGISTER, L131](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/REGISTER.tsv?plain=1#L131)).
- States: on the "Pause and Build plan, your checkout is deactivated across all sales channels" ([Help Center: Pausing your store, L5](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-orgs-and-stores/manage-pricing-plan/pause-store.md?plain=1#L5)); after a missed bill a store "is frozen until you settle your bill with Shopify" ([Help Center: Frozen stores, L5](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/billing-charges/frozen-store.md?plain=1#L5)); a deactivated store's "information is guaranteed for 2 years" ([Help Center: Deactivating your store, L66](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-orgs-and-stores/manage-pricing-plan/deactivate-store.md?plain=1#L66)).
- Betas sit in the same check: the admin router's route eligibility, which lists permissions and entitlements, lists betas on 41 of its 1,364 routes ([admin router, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-router/items.jsonl?plain=1#L1)), set per shop: "For Shopify, this is typically our concept of a shop." ([Using Betas, 2021, L251](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L251))

**Reading:** each area asks one place whether a shop may use a feature, and how much, in its current state; that check also reads betas, kept apart from plans.

**Practice:** Hodgson 2017: permissioning toggles that turn features on for some customers, such as paying ones. Golding 2024: tiers and tenant management.

**Depends on:** 1, 4, 8. **Needed first:** the check, since each route states entitlements beside permissions, such as "MANAGE_ABANDONED_CHECKOUTS" and "abandonedCartRecovery" ([admin router, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-router/items.jsonl?plain=1#L1)); plans' contents can wait, and change: "Shopify increased Admin API rate limits for the Advanced plan" ([merchant changelog, 2023, L971](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl?plain=1#L971)).

## 13. Charges to the merchant

**Question:** What is a merchant charged for, by whom, in what currency and under which tax, and how is chargeable usage recorded?

**Why every area depends on it**
- Shopify's fees "appear on an invoice, which will be sent to the Store Owner", from a party chosen "based on the billing address of your Store." ([Terms of Service, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/legal-documents/20260930T081039Z-shopify-legal-documents/items.jsonl?plain=1#L1)) The bill's 37 charge categories come from many areas, such as "ORDER_COMMISSION" ([charge categories, L5](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/billing-charge-categories/fake-demo-sharrwah@expense-report/items.jsonl?plain=1#L5)).
- The bill's currency and payment methods vary by region: some merchants "can be charged in their local currency" ([Help Center: local currency, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/paying-your-bills/managing-payments/local-currency.md?plain=1#L3)), and methods "depend on your store's region and billing currency" ([Help Center: payment methods, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/paying-your-bills/making-payments/payment-methods-for-bills.md?plain=1#L3)).
- Apps can bill merchants through the platform: "The pricing structure can include recurring charges, usage-based pricing, or both." ([admin schema, L101](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L101)) The bill can sit with the organization: "organizationBilling" decides which settings permissions a store shows ([permission categories, L19](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-permission-tree/use-store-options-f948ecd551d0/categories.jsonl?plain=1#L19)).

**Reading:** each area that charges reports its usage the same way, into one ledger, in decision 8's money form, or each area invents its own billing.

**Practice:** AWS 2022: billing and metering as control-plane services fed by each tenant's usage. Golding 2024: billing and metrics.

**Depends on:** 1, 4, 8, 10, 12. **Needed first:** only before the first area that charges, such as orders, whose fees follow "the value of sales made through your Store" ([Terms of Service, L1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/legal-documents/20260930T081039Z-shopify-legal-documents/items.jsonl?plain=1#L1)); other areas do not depend on it.

## 14. Fair use

**Question:** How is one shop's or one app's load kept from hurting the others: which limits apply, how are they counted, and what happens at the limit?

**Why every area depends on it**
- Shopify counts each query's cost, since request counts charge clients alike "even if they don't need all the data in an API response"; "clients receive 50 points per second up to a limit of 1,000 points" ([Rate Limiting GraphQL APIs by Calculating Query Complexity, 2021, L228](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L228)).
- "The limits that apply across Shopify's APIs" ([shopify.dev front matter, L6753](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl?plain=1#L6753)) include "the resource-based throttles that apply to large stores" ([L6780](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl?plain=1#L6780)). Shops have limits of their own, such as "maxProductVariants" ([shop request details, L9](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/shop-request-details/capture-grow/items.jsonl?plain=1#L9)).

**Reading:** every area's operations are counted under one model; Shopify counts each one's cost. Pods (decision 3) keep failures apart; these limits keep load apart inside a pod, per client and store.

**Practice:** Homer et al. 2014: the Throttling pattern. Krebs, Momm & Kounev 2012: performance isolation between tenants. Weissman & Bobrowski 2009: governor limits on customer code running on the shared platform.

**Depends on:** 1, 4, 7, 12. **Needed first:** the cost model, set as each operation is designed: "A higher cost is necessary to account for this increased server load" ([L228](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L228)); the numbers can wait and change by plan: "Advanced plan stores will now get 100 points/second" ([merchant changelog, 2023, L971](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl?plain=1#L971)).

## 15. Extensions

**Question:** May outside developers extend Sharrwah, and if so where, through what, and under which limits and terms?

**Why every area depends on it**
- "A Shopify application that extends store functionality." ([admin schema, L62](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L62)) "Each installation tracks the permissions granted to the app through" its scopes, along with its billing subscriptions and metafields ([admin schema, L74](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L74)).
- Screens in every surface: 82 admin, 64 checkout, 24 customer account and 33 POS targets ([admin](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/ui-extension-targets/admin@2026.10.2/items.jsonl), [checkout](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/ui-extension-targets/checkout@2026.10.2/items.jsonl), [customer account](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/ui-extension-targets/customer-account@2026.10.2/items.jsonl), [POS](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/ui-extension-targets/point-of-sale@2026.10.2/items.jsonl)).
- Logic in many areas: "13 Functions APIs" (*the capture's* register, [REGISTER, L23](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/REGISTER.tsv?plain=1#L23)), from cart validation to order routing. Sales channels are apps too, with products "published to an app" ([admin schema, L2762](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2762)).

**Reading:** each area decides where apps can add a screen, change a calculation, or attach data. Opening an area afterwards means rebuilding its logic.

**Practice:** Bosch 2009: a platform opened to outside developers becomes an ecosystem. Baldwin & Woodard 2009: a stable core with interfaces through which outside parts vary. Weissman & Bobrowski 2009: customer and partner code run inside the shared platform under limits.

**Depends on:** 4, 5, 6, 7, 10, 11, 13. **Needed first:** not shown; an area can open later at the cost of rebuilding its logic: Shopify "launched Shopify Functions" in 2022 ([2023, L74](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L74)), then began "rebuilding our order routing algorithm" ([2023, L63](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L63)).

## 16. Personal data and retention

**Question:** How is a person's request to see, export or erase their data met across every area, apps included, and how long is each kind of data kept?

**Why every area depends on it**
- Public apps must answer data requests and redactions through "mandatory compliance webhooks" ([shopify.dev front matter, L7057](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl?plain=1#L7057)). Erasure and data requests are permissions: "ERASE_CUSTOMER_DATA" and "REQUEST_CUSTOMER_DATA" ([admin schema, L3257](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3257)).
- An erasure reaches the store and "any apps and channels that you've installed", no further: the merchant must "contact any other companies", and "what was sold and the date and time of the sale, is still visible in your admin." ([Help Center: Customer data requests, L25](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/privacy-and-security/privacy/processing-customer-data-requests.md?plain=1#L25))
- Shopify marks personal data in events "stored in our data warehouse": "The privacy context specifically includes marking sensitive data, identifying data subjects, and handling PII" ([Schematizing Deletion at Scale, 2021, L231](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L231)).
- Retention: "we retain store information for two years before we begin the deletion process", and "the merchant, not Shopify, decides how long your information is retained" ([Privacy Policy, L13](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/legal-documents/20260930T081039Z-shopify-legal-documents/items.jsonl?plain=1#L13)). After termination Shopify will "delete or return Your Customer Personal Data", or keep it "as required by law" ([Data Processing Addendum, L4](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/legal-documents/20260930T081039Z-shopify-legal-documents/items.jsonl?plain=1#L4)). The law is the merchant's: "the privacy and data protection laws and regulations that apply to your business" ([Help Center: Customer data requests, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/privacy-and-security/privacy/processing-customer-data-requests.md?plain=1#L3)).

**Reading:** each area lets one person's data be found, exported and erased, and says how long it keeps it; the sale itself stays (decision 10). Which law applies in a market is that market's value, not decided here.

**Practice:** Cavoukian 2009: privacy built into the design, as the default. ISO/IEC 27701:2025: managing personal data across a system. NIST Privacy Framework 1.0 (2020): identifying the data a system processes and governing it.

**Depends on:** 1, 4, 10, 11, 12, 15. **Needed first:** before any area holds data about people, since what it holds is cheapest to record at design: "Lack of guaranteed schemas for events was the root cause of a lot of our challenges." ([L231](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl?plain=1#L231))

---

## Their order

Decisions on the same step depend only on earlier steps, so they can be settled side by side.

| Step | Decisions | Why here |
| --- | --- | --- |
| 1 | 1 The unit of tenancy; 2 Areas and their borders | They depend on nothing. |
| 2 | 3 Where a shop lives; 4 Who may act; 5 Markets; 6 Card data | Each needs only the tenant, the areas, or both. |
| 3 | 7 APIs and IDs; 8 Money; 9 Language | The API is scoped by shop and scope; money's second currency and a translation's market come from markets. |
| 4 | 10 Events and history; 11 Custom data; 12 Plans and state | Events and custom data take the API's shape and names; events carry money and keep to the card boundary. Plans need prices (money) and the organization (access). |
| 5 | 13 Charges; 14 Fair use | Charges count usage from events against plans. Limits are set per plan, client and store, and counted per API call. |
| 6 | 15 Extensions | Apps act through access, the API, events, custom data, market context, the card boundary and charges. |
| 7 | 16 Personal data and retention | It reaches everywhere personal data goes, apps and custom fields included, in every state of the shop. |

**Reading:** two decisions are roots: what a tenant is (1) and what an area is (2). Every other decision is a rule that every area follows.

## Concerns that look cross-cutting but aren't first decisions

Each line is a reading. Where it rests on Shopify's shape, the fact is cited.

- **Sales channels.** In Shopify an app with a publication (decision 15) and a kind of market ("CHANNEL", [admin schema, L2004](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2004)), so decisions 15 and 5 cover them.
- **B2B buyers.** A market condition with its own catalog and prices ("B2B-specific pricing", [storefront schema, L25](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/storefront-graphql-schema/2026-10/items.jsonl?plain=1#L25)): decision 5, then the customer and catalog areas' design.
- **Locations.** "A physical location where merchants store and fulfill inventory." ([admin schema, L1914](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L1914)): a resource of inventory and fulfilment that markets can use as a condition.
- **Taxes and duties.** In Shopify the obligations follow the store's country and a market holds price inclusions (decision 5); calculation is an area's job.
- **Payment providers.** Available by the store's country (decision 5) and connected through an API of their own, "payments-apps" (*the capture's* register, [REGISTER, L23](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/REGISTER.tsv?plain=1#L23)): decisions 5 and 15.
- **Domains and URLs.** Part of a market's web presence, "which defines its SEO strategy" ([admin schema, L2009](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2009)), so decision 5 covers them.
- **Notifications (email, SMS).** An area built on events (10) and translations (9); email templates are translatable.
- **Search, analytics and reports.** Areas that read every area through the API and events (7, 10); the search syntax is part of 7.
- **Bulk import and export, background jobs, files and media.** Features of the API (7) under fair use (14): "An asynchronous operation that exports large datasets or imports data in bulk." ([admin schema, L198](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L198)); files are referred to by ID.
- **Time zone and units.** Values on the shop (its time zone, unit system and weight unit, [admin schema, L3149](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3149)): a place under decision 1, displayed as decision 9 says.
- **One buyer account across shops.** Shopify keeps it outside the shop's data, as a "relationship with Shopify through services like Shop and Shop Pay" ([Help Center: Customer data requests, L30](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/privacy-and-security/privacy/processing-customer-data-requests.md?plain=1#L30)): a product beside the shops, while each shop's customers stay its own (1).
- **Automation and the AI assistant.** Areas that act through the API, permissions and events (7, 4, 10), like any app.
- **The admin's look, programming language and frameworks.** They shape how areas look and are built, not what they hold; they can come with the first screen and build.
- **Monitoring, logging, deploys and recovery.** Operating practice per pod (3), except the request identifier (1) and each area's resiliency matrix (3); a merchant's history is decision 10.

---

## Practice cited

- AWS, *SaaS Tenant Isolation Strategies: Isolating Resources in a Multi-Tenant Environment*, whitepaper, 2020 (now marked by AWS as historical).
- AWS, *SaaS Architecture Fundamentals*, whitepaper, 2022.
- AWS, *Reducing the Scope of Impact with Cell-Based Architecture*, Well-Architected guidance, 2023.
- ANSI INCITS 359-2012, *Information Technology: Role Based Access Control*, 2012, reaffirmed 2022.
- Aulbach, S., et al., *Multi-Tenant Databases for Software as a Service: Schema-Mapping Techniques*, ACM SIGMOD, 2008.
- Baldwin, C. Y., Woodard, C. J., *The Architecture of Platforms: A Unified View*, in A. Gawer (ed.), *Platforms, Markets and Innovation*, Edward Elgar, 2009 (its content *cited from memory*).
- Berners-Lee, T., Fielding, R., Masinter, L., *Uniform Resource Identifier (URI): Generic Syntax*, RFC 3986, IETF, 2005.
- Bosch, J., *From Software Product Lines to Software Ecosystems*, SPLC, 2009 (its content *cited from memory*).
- Cavoukian, A., *Privacy by Design: The 7 Foundational Principles*, Information and Privacy Commissioner of Ontario, 2009.
- Cervantes, H., Kazman, R., *Designing Software Architectures: A Practical Approach*, Addison-Wesley, 2016 (*seen at second hand*).
- Chong, F., Carraro, G., Wolter, R., *Multi-Tenant Data Architecture*, Microsoft, 2006.
- CNCF, *CloudEvents* specification v1.0, 2019 (its date *seen at second hand*).
- Esselink, B., *A Practical Guide to Localization*, John Benjamins, 2000 (only its contents seen; the rest *cited from memory*).
- Evans, E., *Domain-Driven Design: Tackling Complexity in the Heart of Software*, Addison-Wesley, 2003 (*seen at second hand*).
- Fowler, M., *Patterns of Enterprise Application Architecture*, Addison-Wesley, 2002 (splitting without losing pennies *cited from memory*).
- Golding, T., *Building Multi-Tenant SaaS Architectures*, O'Reilly, 2024.
- Hardt, D. (ed.), *The OAuth 2.0 Authorization Framework*, RFC 6749, IETF, 2012.
- Helland, P., *Life beyond Distributed Transactions: an Apostate's Opinion*, CIDR, 2007 (*seen at second hand*).
- Hodgson, P., *Feature Toggles (aka Feature Flags)*, martinfowler.com, 2017.
- Hohpe, G., Woolf, B., *Enterprise Integration Patterns*, Addison-Wesley, 2003 (publish-subscribe channels *cited from memory*).
- Homer, A., et al., *Cloud Design Patterns: Prescriptive Architecture Guidance for Cloud Applications*, Microsoft patterns & practices, 2014.
- ISO 3166-1:2020, *Codes for the representation of names of countries and their subdivisions, Part 1: Country code*.
- ISO 4217:2015, *Codes for the representation of currencies* (the edition *cited from memory*).
- ISO/IEC 27701:2025, the standard for privacy information management systems, 2025 (*seen at second hand*).
- Kabbedijk, J., et al., *Defining multi-tenancy: A systematic mapping study on the academic and the industrial perspective*, Journal of Systems and Software, 2015 (*seen at second hand*).
- Kent, K., Souppaya, M., *Guide to Computer Security Log Management*, NIST SP 800-92, 2006.
- Krebs, R., Momm, C., Kounev, S., *Architectural Concerns in Multi-Tenant SaaS Applications*, CLOSER, 2012.
- Medjaoui, M., et al., *Continuous API Management*, O'Reilly, 2018 (*seen at second hand*).
- NIST, *Privacy Framework: A Tool for Improving Privacy through Enterprise Risk Management*, Version 1.0, 2020.
- Parnas, D. L., *On the Criteria To Be Used in Decomposing Systems into Modules*, Communications of the ACM, 1972 (*seen at second hand*).
- PCI Security Standards Council, *Payment Card Industry Data Security Standard* (*cited from memory*).
- Phillips, A., Davis, M. (eds.), *Tags for Identifying Languages*, BCP 47 (RFC 5646), IETF, 2009.
- Relay, *GraphQL Global Object Identification Specification*, relay.dev, undated.
- Sandhu, R., et al., *Role-Based Access Control Models*, IEEE Computer, 1996.
- Weissman, C. D., Bobrowski, S., *The Design of the Force.com Multitenant Internet Application Development Platform*, ACM SIGMOD, 2009 (*seen at second hand*).
