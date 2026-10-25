# S02 feasibility: one capability map from Shopify's and Salla's own structures

Date: 2026-10-24. A read-only test of about an hour, working only from the brief and the files it names.

**Path prefixes used below**
- `SH/` = `/home/user/observed-sh/structures/shopify/`
- `SA/` = `/home/user/observed-sa/structures/salla/`
- `AREAS` = `/home/user/sharrwah-knowledge-map/studies/proposals/areas/areas.tsv`
- "SH register" = `/home/user/observed-sh/structures/REGISTER.tsv`; "SA register" = `/home/user/observed-sa/structures/REGISTER.tsv`

Counts are measured with the scripts listed in section 10. Anything marked **(estimate)** is my own judgement.

---

## 1. Answer in brief

**Partly feasible.**

- **Capabilities and permissions can be filled for most operational areas.** Within each platform, the link from a capability to the permission that gates it is stated by the platform itself, not inferred: Shopify's router `eligibility`, and Salla's `dashboard-nav` `permission`.
- **Interactions can be filled only where a resource emits events.** That covers products, orders, customers, shipping and apps. Several areas have no events at all.
- **No key joins the two platforms mechanically.** In five families of names, between 1 and 13 names match exactly after normalization (section 5).
  - A crosswalk of resource nouns has to be built by hand.
  - Once it exists, events and API groups join largely by rule.
  - Permissions and area boundaries stay manual.
- **Assigning entries to areas is manual.** The ids in AREAS' `platform_area_ids` column (for example `SH-A-11;SA-A-06`) appear in none of the named structures. Every group therefore has to be placed in an area by a rule table made by hand, not looked up.
- **A full map would take about 18–26 hours of agent work (estimate).** See section 7.

---

## 2. Survey of the structures

### 2.1 Shopify (`SH/`)

| Structure (folder → file) | What it holds (measured) | Size | Ids, names or paths usable as keys | Seen |
|---|---|---|---|---|
| `admin-router/items.jsonl` | 1,364 routes in 72 `section`s, plus 21 routes with no section. Each route has: `path` (relative, nested through `parent`; 10 paths are code expressions such as `` `${o.settings()}/*` ``); `resource` (245 distinct values); `actionType`; `eligibility` (`permissions`, `oneOf`, `organizationPermissions`, entitlements, features, betas); `metadata.nextRoutes` | 818 KB, plus 2.8 MB `source.jsonl` | route `id` (unique), resolved path, permission handles | 2026-09-29 |
| `admin-route-titles-en/items.jsonl` | 827 pairs of `"<route-id>:title"` → title; 711 of them match a router id | 62 KB | route id | 2026-09-29 |
| `admin-main-nav/<store>@<page>/items.jsonl` | The navigation as rendered: 3 captures of 24–42 items each (text, href, parent) | 2–5 KB each | href | 2026-09-29 |
| `admin-settings-nav/<store>/items.jsonl` | 21–23 items per store, for 3 stores (`id` such as `payments`, title, `scope` ORGANIZATION or SHOP, url) | ~4.5 KB each | id, url | 2026-09-29 |
| `admin-permission-tree/use-store-options-f948ecd551d0/` | `categories.jsonl`: 21 categories, with Settings listed twice. `items.jsonl`: 142 permission rows, 130 distinct ids, each with category, title, dependencies and visibleBy | 39 KB | permission id (e.g. `MANAGE_ORDERS_INFORMATION`) | 2026-09-30 |
| `admin-roles/ctcbwa-r1/`, `org-239421532/` | 15 and 12 roles: name, category (ORGANIZATION, STORE or POINT_OF_SALE), roleType, systemRoleHandle | ~5 KB | role gid, systemRoleHandle | 2026-10-05 / 10-07 |
| `admin-role-permissions/ctcbwa-r1/items.jsonl` | 768 grants (role → handle, accessLevel) across the 15 roles; 313 distinct handles | 175 KB | handle | 2026-10-05 |
| `admin-assignable-permissions/ctcbwa-r1/items.jsonl` | 124 handles, of which 114 are tree ids | 8 KB | handle | 2026-10-05 |
| `admin-webhook-topics/fake-demo-sharrwah/items.jsonl` | The 99 topics the admin offers (label, enum value, formats). All 99 are in the schema's enum | 18 KB | enum value (e.g. `ORDERS_CREATE`) | 2026-10-07 |
| `admin-graphql-schema/<version>/items.jsonl` | 6 versions (2025-10 to unstable). Version 2026-10 has 3,716 types, 298 `QueryRoot` fields, 537 `Mutation` fields and 236 `WebhookSubscriptionTopic` values | 1.4–1.9 MB per version | type and field names | 2026-09-30 |
| `admin-graphql-reference-nav/shopify.dev@latest/items.jsonl` | 28 categories holding 4,637 items. It puts 298 of 298 queries, 532 of 537 mutations and 3,691 of 3,716 types each in exactly one category. Two of the categories are not domains: "Common objects" (40 queries, 36 mutations, 215 objects) and "GraphQL Types" | 820 KB | category label, leaf name | 2026-10-07 |

**Links Shopify itself states (measured)**

- **Route → permission.** 868 of the 1,364 routes are gated: 402 by their own `eligibility`, the rest through a parent route.
  - They use 112 distinct handles: 108 appear in `admin-role-permissions` and 72 in the permission tree.
  - 4 appear in neither: `BALANCE_BANK_ACCOUNTS_MANAGEMENT`, `CAPITAL`, `MANAGE_ALL_SHOPIFY_CREDIT_CARDS`, `SHOPIFY_PAYMENTS`.
  - Handles are nested in `oneOf` on 83 routes (of 98 with a `oneOf`), and given as `organizationPermissions` on 45 routes (7 values: `MANAGE_BILLING`, `INVITE_USERS`, `MANAGE_STORES`, …).
- **Nav entry → route, by resolved path.**
  - In `admin-main-nav/demo-fake-dev-store@settings-organization-account`, all 34 links into the store admin resolve to a route.
  - In `admin-settings-nav/ibx5bt-xy`, 21 of 23 resolve once `${o.settings()}` is read as `/settings`. Plan and Markets do not.
- **Role → permission:** stated in `admin-role-permissions`.
- **API leaf → category:** stated in `admin-graphql-reference-nav`.
- **Topic → resource:** by name only (`ORDERS_CREATE` → orders).

### 2.2 Salla (`SA/`)

| Structure (folder → file) | What it holds (measured) | Size | Ids, names or paths usable as keys | Seen |
|---|---|---|---|---|
| `dashboard-nav/prod/items.jsonl` | 6 top-level items (Home, Orders, Products, Marketing, Store & Channels, Reports) and 64 nodes in all. Each node has url, label {ar, en}, `permission`, feature, tags and actions. 55 nodes name permissions, 93 distinct names | 24 KB | url, permission name | 2026-10-08 |
| `dashboard-main-navigation/merchant@en/` (and `@ar`) | The rendered mega-menu: 133 items (88 links, 7 buttons, 38 texts) | 13–15 KB | href | 2026-10-08 |
| `dashboard-settings-menu/merchant@en/` | 4 group labels and 23 settings pages, written as bare paths (`/profile`, `/payments`) | 2 KB | href | 2026-10-08 |
| `dashboard-menu-{orders,products,marketing,store-channels,reports}/merchant@en/` | 52 links, of which 50 are also in the main navigation | 0.3–2 KB | href | 2026-10-08 |
| `dashboard-staff-roles/demo@en/`, `real-merchant@en/` | 10 and 15 roles: id, slug, name (Arabic), type (default or custom). No grants | 1–2 KB | slug | 2026-10-12 |
| `staff-permission-groups/demo@en/items.jsonl` | 16 groups, named in Arabic only, holding 201 permissions with English snake_case names | 20 KB | permission name (e.g. `order_browse`) | 2026-10-08 |
| `dashboard-webhook-events/demo@en/`, `real-merchant@en/` | 63 events with dotted names (e.g. `shipping.company.deleted`), identical on both stores. None for orders or apps | 7 KB | event name | 2026-10-12 |
| `docs-event-lists/<page>/` | 37 lists, 371 rows, each list kept separate. `webhooks` has 58 rows in 12 tables (the Order table has 17); `partner-apis.app-events` has 13 | 111 files | event name (inside markdown cells) | 2026-10-05 |
| `docs-operations/md-openapi/items.jsonl` | 285 operations, one OpenAPI document each, under 67 tags (e.g. Products 13, Orders 9, Order Status 7). 261 of them name scopes in a description block; parsed, that gives 40 distinct scopes (e.g. `orders.read_write`) | 4.4 MB | path + method, tag, scope | 2026-10-05 / 10-08 |
| `docs-dataschemas/{definitions,placements,schema-pages}/` | 409 definitions. Their x-tags: Store Events Webhook Model 25, Models 18, Responses 5. 72 definitions carry event names. 303 placements, of which 159 are on twilight-sdk pages and 62 on twilight-engine pages | 1.2 MB | definition id, title | 2026-10-05 to 10-09 |

**Links Salla itself states, and the gaps (measured)**

- **Nav node → permission:** stated for 55 of the 64 `dashboard-nav` nodes.
  - 92 of the 93 names are in `staff-permission-groups`; `product_inventory` is not.
  - 109 of the 201 permissions are named by no node.
- **Rendered link → nav node:** 51 of the 88 main-navigation links match a `dashboard-nav` url. The other 37 are:
  - the Customers, Staff, Help Desk, Shipping, Payment, Tools and Logs groups (36 links), which `dashboard-nav` does not hold;
  - Salla Ads, which is `/marketing/ads/dashboard` in the mega-menu but `/marketing/ads/v2/dashboard` in `dashboard-nav` and in `dashboard-menu-marketing`.
- **Settings page → nav node:** the two write addresses differently. The settings menu writes `/orders`; `dashboard-nav` writes `?settings=/orders`. A plain match gives 2 false joins: `/orders` and `/products` hit the order and product *list* pages.
- **Role → permission:** not held. The SA register row `salla/dashboard-staff-roles` says: "each role's permissions and restrictions are its own answer (/admin/v2/users/roles/<id>), not held yet".
- **Operation → tag and scope:** stated. **Event → resource:** by name only.
- **Numeric ids cannot be keys.** `/home/user/observed-sa/docs/READING.md` warns that Salla's numbers recur across unrelated lists. Here, 1473353380 is at once:
  - the role `user` (`SA/dashboard-staff-roles/demo@en/items.jsonl`);
  - the group الرئيسية (`SA/staff-permission-groups/demo@en/items.jsonl`);
  - the permission `dashboard_summery_month` (same file).

---

## 3. Five sample areas

Structure names below are folders under `SH/` or `SA/`. The file read is the `items.jsonl` in the label folder named in section 2. "Gated" counts include permissions a route inherits from its parent.

### A-01 Accounts, stores and staff

**Shopify**

- **Capabilities**
  - `admin-settings-nav/ibx5bt-xy`: Organization (`organization_details`, scope ORGANIZATION), Users (`user_management`), Roles, Security.
  - `admin-router`, section OrganizationSettings: 104 routes, 48 gated. Examples: `settings:organizations:accounts:roles:create` "Add role"; `organization-settings:organizations:details:stores:create` "Create store".
  - `admin-router`, section Account: 5 routes. Example: `settings-account:invite` "Add staff".
  - GraphQL: `StaffMember` and `staffMembers` sit in "Common objects"; `Shop` and `BusinessEntity` in "Store properties".
- **Roles**
  - `admin-permission-tree`, category USER_MANAGEMENT: `MANAGE_STAFF_PERMISSIONS`, `ADD_REMOVE_STAFF`, `AUTHENTICATION_MANAGEMENT`, `STAFF_API_PERMISSION_MANAGEMENT`, `MANAGE_COLLABORATORS`.
  - Router gates: `STAFF_MANAGEMENT_CREATE` on "Add staff"; `organizationPermissions` `INVITE_USERS` and `MANAGE_STORES`.
  - `admin-roles/ctcbwa-r1`: 15 roles (Administrator `organization_administrator`, App developer, Customer support, POS roles). Their 768 grants are in `admin-role-permissions`.
- **Interactions**
  - Topic `SHOP_UPDATE`, in both the admin list and the enum.
  - In the enum only: `FINANCE_APP_STAFF_MEMBER_GRANT/REVOKE/DELETE/UPDATE`.
  - No topic for staff or users.

**Salla**

- **Capabilities**
  - `dashboard-main-navigation/merchant@en`, group Staff: Staff members `/users`, Roles & permissions `/users/roles`, Employees targets `/users/targets`.
  - `dashboard-settings-menu`, group Account: Your profile `/profile`, General `/general`, Store plan `/plan`, Manage stores `/stores`.
  - `docs-operations`: `GET /users` (List Employees), `GET /store/info`, `GET /oauth2/user/info`.
  - Not in `dashboard-nav`.
- **Roles**
  - `staff-permission-groups`, group موظفي المتجر: `users_browse`, `users_management`, `roles_browse`, `roles_management`, `order_auto_assign_browse`, `order_auto_assign_management`.
  - Also `account_setting_management` and `audit_logs_management`, in group إعدادات المتجر.
  - `dashboard-staff-roles/demo@en`: 10 default roles (`general_manager`, `orders_manager`, `products_manager`, …, `user` التاجر). No grants held.
  - The 3 docs operations name no scope.
- **Interactions**
  - `store.owner.changed` (`dashboard-webhook-events`).
  - No staff events.

**Key: manual.**
- No handle or name is shared beyond "roles".
- Shopify separates the organization from the store: settings scope ORGANIZATION or SHOP, and role categories ORGANIZATION, STORE and POINT_OF_SALE. Salla has one store-level staff model, plus "Manage stores".
- The role vocabularies do not overlap: Salla's are job titles; Shopify's are system and custom roles.
- The mapping is small: about 15–20 pairs **(estimate)**.

### A-04 Products & inventory

**Shopify**

- **Capabilities**
  - `admin-main-nav`: Products, Collections, Inventory, Purchase orders, Transfers. All resolve to routes.
  - Router sections: Products 49 routes (46 gated), Inventory 32 (31 gated), Collections 11 (10 gated).
  - GraphQL "Products and collections": 41 queries, 78 mutations, 144 objects. "Inventory": 10 queries, 28 mutations, 19 objects.
  - Settings: Locations.
- **Roles**
  - Category PRODUCTS, 16 ids: `PRODUCTS`, `MANAGE_PRODUCTS`, `EDIT_PRODUCT_PRICE`, `EDIT_PRODUCT_COST`, `MANAGE_INVENTORY`, `VIEW_INVENTORY_TRANSFERS`, `PERFORM_INVENTORY_COUNTS`, …
  - Router example: `transfers` is gated by `PRODUCTS` + `VIEW_INVENTORY_TRANSFERS`.
- **Interactions**
  - The admin list has 32 topics by prefix: `PRODUCTS_*` (3), `COLLECTIONS_*` (3), `INVENTORY_ITEMS_*` (3), `INVENTORY_LEVELS_*` (3), `INVENTORY_TRANSFERS_*` (7), `INVENTORY_SHIPMENTS_*` (8), `LOCATIONS_*` (5).
  - The enum adds `VARIANTS_IN_STOCK`, `VARIANTS_OUT_OF_STOCK`, and product listing and publication topics (which belong to A-21).

**Salla**

- **Capabilities**
  - `dashboard-nav` Products (id 25), 17 children. Examples: Inventory management `/products/quantities/bulk`; Inventory transfer `/products/inventory-transfer`; Warehouses & branches `/products/branches`; Multi Market `/localization` (which belongs to A-15).
  - `dashboard-menu-products`: 14 links. Settings: Products, Inventory.
  - `docs-operations` tags: Products 13, Product Images 6, Product Option Templates 5, Product Options 4, Product Option Values 4, Product Variants 4, Product Quantity 4, Digitals Product 3, Product Tags 2, Categories 7 (plus Category 1), Brands 5, Branches 5, Branch Allocations 6.
- **Roles**
  - Group المنتجات, 14 permissions: `product_browse`, `products_management`, `categories_management`, `products_stock_management`, `brands_management`, …
  - Group نقل المخزون, 6 permissions: `inventory_transfer_*`, `inventory_browse`, `inventory_management`.
  - Per node, for example Warehouses & branches → `branches_management`.
  - Scopes: `products.*`, `categories.*`, `brands.*`, `branches.*`.
- **Interactions**
  - `dashboard-webhook-events`: `product.*` 17 (e.g. `product.price.updated`, `product.quantity.low`), `category.*` 4, `brand.*` 3, `store.branch.*` 5.
  - `docs-event-lists/webhooks`: Product 11 (two struck through), Category 2, Brand 3.

**Key: partly mechanical.**
- "product" matches across nav, API group, type and event stem. Verbs map through a small table (`PRODUCTS_CREATE` ↔ `product.created`).
- The rest needs a crosswalk:
  - category ↔ collection;
  - branch or warehouse ↔ location;
  - quantity ↔ inventory level;
  - option and variant ↔ `ProductOption` and `ProductVariant`. These match once camel case is split.
- Salla's brands have no Shopify resource.
- No permission handles are shared.

### A-09 Orders

**Shopify**

- **Capabilities**
  - `admin-main-nav`: Orders, Drafts.
  - Router section Orders: 66 routes, 64 gated.
  - GraphQL "Orders": 34 queries, 98 mutations, 188 objects. Examples: `orderCancel`, `orderEditBegin`, `refundCreate`, `returnCreate`, `draftOrderCreate`.
  - The same category also holds `giftCardCreate` (which belongs to A-32), subscription contracts and `paymentTermsCreate`.
- **Roles**
  - Category ORDERS, 20 ids (`ORDERS`, `EDIT_ORDERS`, `CANCEL_ORDERS`, `REFUND_ORDERS`, `RETURN_ORDERS`, `MARK_ORDERS_AS_PAID`, …); category DRAFT_ORDERS, 9 ids.
  - Router: `orders` is gated by `ORDERS`, `draftOrders` by `DRAFT_ORDERS`.
- **Interactions**
  - The admin list has 13 topics: `ORDERS_*` (8, including `ORDERS_RISK_ASSESSMENT_CHANGED`), `DRAFT_ORDERS_*` (3), `REFUNDS_CREATE`, `ORDER_TRANSACTIONS_CREATE`.
  - The enum has 27 by prefix. It adds `RETURNS_*` (8), `REQUESTED_ORDER_EDIT_*` (3) and `ORDERS_PARTIALLY_FULFILLED`.

**Salla**

- **Capabilities**
  - `dashboard-nav` Orders (id 24), 11 children: All orders, Order settings, Order statuses, Bulk status update, Auto assignment, Invoice settings, Bookings, Custom fields, Cart options, Export templates, Auto tags.
  - Logs group: Deleted orders `/orders/trash`.
  - `docs-operations` tags: Orders 10, Order Status 7, Order Items 5, Order Invoice 5, Order Options 5, Order Assignment 4, Order Histories 2, Order Reservations 1.
- **Roles**
  - Group الطلبات, 28 permissions: `order_browse`, `order_management`, `order_edit`, `order_refund_payment`, `order_statuses_edit`, 9 `order_browse_status_*`, …
  - The All orders node names 18 of them.
  - Scopes: `orders.read`, `orders.read_write`.
- **Interactions**
  - `docs-event-lists/webhooks`, Order table: 17 (`order.created`, `order.status.updated`, `order.cancelled`, `order.refunded`, `order.payment.updated`, `order.shipment.*`, …).
  - `dashboard-webhook-events` has **no** `order.*` event (0 of 63).

**Key: partly mechanical.**
- "order" matches in every family. Events pair by verb (`ORDERS_CREATE` ↔ `order.created`, `ORDERS_CANCELLED` ↔ `order.cancelled`).
- Manual parts:
  - Salla's custom order statuses have no Shopify resource.
  - Refunds and returns are resources in Shopify but order events in Salla (`order.refunded`, `order.shipment.return.*`).
  - Permissions map many-to-one. Shopify has `CANCEL_ORDERS` and `REFUND_ORDERS`; Salla has `order_management` and `order_refund_payment`.

### A-11 How buyers pay

**Shopify**

- **Capabilities**
  - Settings: Payments `/settings/payments`.
  - Router section Payments: 74 routes, 43 gated. The section mixes A-11 and A-12:
    - A-11, for example: `payments:settings:third-party-providers:list` "Third-party payment providers"; `payments:settings:manual-payment-methods`; `payments:settings:add-payment-methods`; `payments:settings:payment-customizations`; `payments:settings:paypal-express-checkout`.
    - A-12, for example: `payments:settings:shopify-payments`, `payouts`, `dispute-evidences`.
  - The 2026-10 schema has no payment provider or gateway type. A name search finds only:
    - `PaymentSettings`, whose single field is `supportedDigitalWallets`, filed under "Orders";
    - the card-brand enum `PaymentMethods`;
    - `PaypalExpressSubscriptionsGatewayStatus`.
  - `PaymentCustomization` and `PaymentTerms` are in "Common objects"; `OrderTransaction` and `TenderTransaction` are in "Orders".
- **Roles**
  - `MANAGE_PAYMENTS_SETTINGS` (Settings category) gates the provider routes.
  - `PAYMENT_SETTINGS` (Finance category).
  - Order-level: `CAPTURE_PAYMENTS_FOR_ORDERS`, `MARK_ORDERS_AS_PAID`, `PAY_ORDERS_BY_VAULTED_CARD`.
- **Interactions**
  - Admin list: `ORDER_TRANSACTIONS_CREATE`, `TENDER_TRANSACTIONS_CREATE`, `ORDERS_PAID`.
  - The enum adds `CUSTOMER_PAYMENT_METHODS_*`, `PAYMENT_TERMS_*`, `PAYMENT_SCHEDULES_DUE`.

**Salla**

- **Capabilities**
  - Main navigation, group Payment:
    - Payment methods `/payments`;
    - Wallet `/payments/wallet` (A-12);
    - Payment restrictions `/payments/rules`;
    - Tax settings `/payments/taxes` (A-14);
    - Transactions `/payments/transactions`;
    - Store Verification `/payments/kyc` (A-18).
  - Settings menu, group Store: Payments, and Checkout beside it. AREAS' note on A-08 places Salla's checkout here.
  - `docs-operations`: Payments 3 (`GET /payment/methods`, `/payment/banks`), Transactions 4, Settlements 4 (A-12).
  - Not in `dashboard-nav`.
- **Roles**
  - Group المدفوعات, 4 permissions: `payment_method_browse`, `payment_methods_activation`, `bank_accounts_management`, `list_epayments`.
  - In group إعدادات المتجر: `payments_rules_management`, `payments_operations_management`.
  - Scopes: `payments.read`, `transactions.*`.
- **Interactions**
  - `order.payment.updated` (docs webhooks list, Order table).
  - `subscription.charge.succeeded` and `subscription.charge.failed` (`docs-event-lists/recurring-payments.webhook-events`).
  - No payment event in `dashboard-webhook-events`.

**Key: manual.**
- "payment method" and "transaction" occur on both sides, but the units differ. Shopify configures providers and manual methods on admin pages only. Salla lists methods, with activation and restrictions.
- Both platforms' payment groups straddle areas, so every entry needs a judgement:
  - Shopify's Payments section spans A-11 and A-12.
  - Salla's Payment group spans A-11, A-12, A-14 and A-18.

### A-24 Apps

**Shopify**

- **Capabilities**
  - Main nav: Apps, a button with no href. Settings: Apps `/settings/apps`, and Sales channels.
  - Router section Apps: 44 routes, 12 gated (`apps:list`, `apps:extensions`, `apps:functions`, …). Section Extensibility: 11 routes, none gated.
  - GraphQL "Apps": 9 queries, 6 mutations, 9 objects (`appInstallations`, `appUninstall`).
  - GraphQL "Billing": `appSubscriptionCreate`, `appUsageRecordCreate`. "Access": `appRevokeAccessScopes`.
- **Roles**
  - Category "App and sales channel permissions": `APPLICATIONS`, `BILLING_APPLICATION_CHARGES`.
  - Category App development: `VIEW_PRIVATE_APPS`, `EDIT_PRIVATE_APPS`, `ENABLE_PRIVATE_APPS`.
  - Router: `oneOf` `APPLICATIONS` / `LIMITED_APPLICATIONS`.
  - Role "App developer".
- **Interactions**
  - Admin list: none.
  - Enum: `APP_UNINSTALLED`, `APP_SCOPES_UPDATE`, `APP_SUBSCRIPTIONS_UPDATE`, `APP_PURCHASES_ONE_TIME_UPDATE`, `APP_SUBSCRIPTIONS_APPROACHING_CAPPED_AMOUNT`.

**Salla**

- **Capabilities**
  - Main navigation, group Tools: My apps `/apps/installed`; App Store `/apps`; Merchant Services `/manage/experts` (A-26); Developer tools `/manage/webhooks` (A-25).
  - Settings: Installed apps.
  - `docs-operations`, Partner Apps APIs: 5 operations (`/apps/{app_id}/settings`, `/apps/{app_id}/subscriptions`, `/apps/balance`). None names a scope.
- **Roles**
  - `marketplace_apps_management`, in group إعدادات المتجر. Apps have no group of their own.
- **Interactions**
  - `docs-event-lists/partner-apis.app-events`: 13 (`app.installed`, `app.uninstalled`, `app.store.authorize`, `app.trial.*`, `app.subscription.*`, `app.settings.updated`, …).
  - None in `dashboard-webhook-events`.

**Key: partly mechanical, for events and API.**
- "app" matches; `APP_UNINSTALLED` ↔ `app.uninstalled`; app subscriptions exist on both sides.
- The boundary between A-24 and A-25 is manual. Most of what either platform's structures hold here is the developer side (A-25), not the seller's app store.

### What the sample shows

| | Capabilities and gating permissions | Interactions | Join |
|---|---|---|---|
| A-01 | Shopify: stated link. Salla: menus and permission names, no stated link | thin | manual |
| A-04 | both: stated link | rich | partly mechanical |
| A-09 | both: stated link | rich (Salla's only in the docs lists) | partly mechanical |
| A-11 | Shopify: stated link (router pages only). Salla: menus and permission names, no stated link | thin | manual |
| A-24 | Shopify: stated link. Salla: menus and one permission, no stated link | present (Shopify's only in the enum, Salla's only in the docs) | partly mechanical |

---

## 4. How a join could work

- **Within each platform, mostly by rule.**
  - Shopify: route ↔ permission ↔ role, nav ↔ route, leaf ↔ category.
  - Salla: nav node ↔ permission ↔ group, operation ↔ tag ↔ scope.
- **Between platforms, the only workable handle is the resource noun.** It appears in:
  - Shopify: GraphQL category and type, router `resource`, topic stem;
  - Salla: operation tag, url segment, event prefix.
- **What a join needs:** a crosswalk of nouns made by hand, plus a table of verbs (`CREATE` ↔ `created`, `CANCELLED` ↔ `cancelled`, …).
- **Permissions don't fit this pattern.** They are coarse on Salla (`order_management`) and fine on Shopify (`CANCEL_ORDERS`, `REFUND_ORDERS`), so they join many-to-one by hand. Joining at the level of permission categories and groups is feasible: ORDERS ↔ الطلبات, PRODUCTS ↔ المنتجات.

---

## 5. Cross-platform keys (measured)

Normalization: lowercase, singular, separators dropped (camel case split where noted).

| Family of names | Shopify names | Salla names | Exact matches after normalization |
|---|---|---|---|
| Event resource stems: `WebhookSubscriptionTopic` 2026-10 vs Salla's dashboard, docs webhooks and app events | ~106 stems | 18 prefixes | 4: app, customer, order, product |
| API groups: GraphQL reference-nav categories vs Salla operation tags (last segment) | 28 | 62 | 3: Customers, Orders, Webhooks |
| Salla operation tags vs Shopify object type names (camel case split) | 949 types | 64 tags | 7: Customers, Orders, Products, Product Options, Product Option Values, Product Variants, SEO |
| Navigation labels: main and settings menus, English | 57 | 141 | 13 (e.g. Customers, Inventory, Payments, Shipping and delivery) |
| Permission handles: tree ids vs Salla permission names | 130 | 201 | 1: `DOMAINS_MANAGEMENT` = `domain_management` |

**Equivalents that do not match by name.** These are plain to a reader and need the crosswalk:
- category ↔ collection
- branch ↔ location
- shipment ↔ fulfillment
- special offer ↔ automatic discount
- coupon ↔ discount code
- abandoned cart ↔ abandoned checkout
- store ↔ shop
- employees or users ↔ staff member

**Shared words that mean different things:**
- Salla's `subscription.*` events are buyers' recurring payments (`SA/docs-event-lists/recurring-payments.webhook-events/`).
- Shopify's `APP_SUBSCRIPTIONS_UPDATE` is app billing.
- Shopify's `SUBSCRIPTION_CONTRACTS_*` are buyers' contracts.

---

## 6. Judgement: partly feasible

**What works**

1. **Each platform states its own capability → permission link.**
   - Shopify's router `eligibility` gates 868 of 1,364 routes, and 108 of its 112 handles match role grants.
   - Salla's `dashboard-nav` names permissions on 55 of 64 nodes, and 92 of the 93 names are in its permission groups.
2. **Shopify's API arrives grouped.** The GraphQL reference nav puts every query and nearly every mutation and type into one category. 26 of the 28 categories are domains.
3. **Salla's API is small and tagged:** 285 operations, 67 tags, 261 operations with scopes.
4. **Event names are regular on both sides** (`RESOURCE_VERB`, `resource.verb`). Once resources are crosswalked, events join by rule.

**What does not**

1. **The structures hold no cross-platform key.** In any family, only a handful of names match (section 5).
2. **The data does not assign entries to areas.** AREAS gives `platform_area_ids` such as `SH-A-11`, but no named structure carries those ids.
   - Every group (router section, GraphQL category, permission category, Salla nav group, tag, event prefix) must be placed in an area by hand.
   - Several groups straddle areas.
3. **Salla's permission-bearing nav lacks 7 of the main navigation's 13 groups** (Customers, Staff, Help Desk, Shipping, Payment, Tools, Logs; 36 of 88 links). The SA register row `salla/dashboard-main-navigation` describes 13 groups. For the 7 missing ones, a permission can only be matched by name (`/users` ↔ `users_management`).
4. **Some areas have nothing in these structures** (section 6.1).

### 6.1 Coverage of the 34 areas

**From AREAS (measured from `platform_area_ids`):**
- 25 areas draw on both a Shopify and a Salla grouping.
- 5 draw on Shopify only: A-08, A-20, A-23, A-28, A-33.
- 3 draw on Salla only: A-18, A-29, A-34.
- A-17 draws on neither.
- So a two-platform join is possible for at most 25 areas.

**From a keyword probe (estimate; keyword hits are not assignments).** The probe searched Shopify's routes, permissions, topics and GraphQL operations, and Salla's navigation, permissions, operations and events.
- **Well covered on both:** A-04, A-05, A-06, A-07, A-09, A-10, A-14, A-21, A-27. Probably also A-22, A-30, A-31 and A-32, which I did not sample.
- **Covered on Shopify, thin on Salla:**
  - A-03: Shopify has 162 route hits; Salla has 2 nav links (Store plan, Balance & billing).
  - A-13: Shopify has its Capital, Credit and Banking sections; Salla has nothing.
  - A-19: Shopify has legal-entity routes; Salla has nothing.
  - A-20: Shopify has its Privacy section and `ERASE_CUSTOMER_DATA`; Salla has nothing.
- **Nearly empty on both:**
  - A-16: only Salla's `GET /countries` and `/cities`, which are address lists.
  - A-17: no hits at all.
  - A-26: only Salla's Merchant Services link.
  - A-34: only Salla's `quick_donation_management`.

These areas need other evidence, such as help centres and legal pages, or must be recorded as having no structural entry.

---

## 7. Effort to fill all 34 areas (estimate)

| Step | Work | Agent hours (estimate) |
|---|---|---|
| 1. Extract | Build normalized tables per platform (capabilities, permissions, events) carrying the stated links: route → permission (with inheritance and `oneOf`); nav → route; nav node → permission; operation → tag and scope; GraphQL leaf → category; topic or event → resource stem; connection and payload types folded into their base type | 3–4 |
| 2. Assign areas | Write a rule table placing about 380 group keys in areas. Shopify: 72 sections, 26 categories, 21 permission categories, ~100 topic stems, 23 settings items. Salla: 13 nav groups, 16 permission groups, 67 tags, 18 event prefixes, 23 settings pages. Then handle entry-level exceptions in the groups that straddle areas. Shopify: Payments (74 routes), OrganizationSettings (104), Billing (116), "Common objects" (~290 leaves), "Store properties", "Orders". Salla: إعدادات المتجر (41 permissions), the Payment group, Store & Channels | 6–8 |
| 3. Crosswalk | Build 80–120 noun pairs and a verb table of about 20, then join capabilities and events area by area. Map permissions many-to-one where a join is wanted at all | 4–6 |
| 4. Gaps | Record the areas and headings with no structural entry. Check the Salla nav groups that lack stated permissions by name. Re-run against the later Shopify router | 2–3 |
| 5. Review | Spot-check about 10% of rows against the bytes | 3–5 |
| | **Total** | **18–26** |

**Assumptions.**
- One version of each structure is used: the Shopify router of 2026-09-29 or its 2026-10-07 successor, and GraphQL 2026-10.
- English labels are used.
- No new capture is made.

**One more structure may help.** Salla's `dashboard-nav-segments` (157 segments, per the SA register) is answered by the same navigation API as `dashboard-nav`, so it probably has the same item shape, with permissions. It might close the gap for the 7 missing groups. I did not examine it, because it is outside this brief.

**Order of work.** Do the area rules and the crosswalk at group level first, using Shopify's GraphQL categories and Salla's tags as the backbone. Then use the events to check the crosswalk.

---

## 8. Which structures carry the value

**Most value**

- **Shopify**
  - `admin-router`: capabilities, resources and gating permissions in one table.
  - `admin-graphql-reference-nav`: the grouping of resources.
  - `admin-graphql-schema` 2026-10: needed for the 236-value topic enum and field detail.
  - `admin-permission-tree`: permission categories and titles.
  - `admin-role-permissions`: which roles hold which grants.
- **Salla**
  - `dashboard-nav`: capabilities with their permissions.
  - `staff-permission-groups`: the permission vocabulary.
  - `docs-operations`: the API by tag, with scopes.
  - `docs-event-lists`: the fullest event lists, including orders and apps.
  - `dashboard-main-navigation`: the only source for the 7 groups `dashboard-nav` lacks.

**Little added value**

- **Shopify**
  - `admin-main-nav`: every store link is already a router route.
  - `admin-route-titles-en`: labels only; 711 match routes.
  - `admin-assignable-permissions`: 114 of its 124 handles are already in the tree.
  - `admin-webhook-topics`: 99 topics, all in the enum. Useful only to mark which topics the admin offers.
  - The five other schema versions: change history only.
  - `admin-roles`: names only; the grants are in `admin-role-permissions`.
- **Salla**
  - `dashboard-menu-*`: 50 of 52 links are already in the main navigation.
  - `dashboard-settings-menu`: labels; its paths need a prefix rule to join.
  - `dashboard-staff-roles`: names only, no grants.
  - `dashboard-webhook-events`: 63 events, a subset of the docs lists, without orders or apps.
  - `docs-dataschemas`: payload models, mostly placed on storefront SDK pages.

---

## 9. Risks

### Stale

- **The evidence is 2–4 weeks old.** It was captured between 2026-09-29 and 2026-10-12; today is 2026-10-24.
- **Shopify's router changes from day to day.**
  - The SH register row `shopify/admin-router` names two hashes on 2026-09-29.
  - The SH register row `shopify/admin-router-versions` holds a 2026-10-07 router with 1,374 routes: 11 added, 1 removed, 69 changed.
- **Salla's navigation may already differ.** Its dashboard import map moved between 2026-10-08 and 2026-10-11, with 37 of 128 modules at new addresses (SA register row `salla/dashboard-importmap`).

### Partial

- **Results vary by store.**
  - Shopify's main nav differs by store and page, and its settings nav by store (SH register rows). For example, Markets appears only for `ibx5bt-xy`.
  - Salla's roles differ by store (10 vs 15).
  - Salla's permission groups were captured on the demo store only.
- **Salla's structures have gaps.**
  - `dashboard-nav` lacks 7 of 13 groups.
  - Role grants are not held.
  - `dashboard-webhook-events` lacks every order and app event.
- **Shopify's structures have gaps.**
  - The admin offers 99 of 236 topics; app topics are only in the enum.
  - The Admin GraphQL has no payment-provider resource, so A-11's Shopify capabilities come from router pages only.

### Ambiguous

- **Catch-all groups.**
  - GraphQL "Common objects" holds `StaffMember` and payment customizations.
  - "Orders" holds gift-card mutations and subscription contracts.
  - "Store properties" mixes the shop, locations, business entities and policies.
- **Same word, different thing.**
  - Salla's `subscription.*` events (section 5).
  - Shopify's settings "Policies" (`/settings/legal`) are the store's policies for buyers, not the platform's terms (A-19).
  - Salla's settings `/orders` is not the order list `/orders`.
  - Salla Ads has two addresses within one run (the mega-menu and `dashboard-menu-marketing`, both from run `20261008T113513Z-dashboard-menus`).
- **Labels and ids.**
  - Salla's permission groups are named in Arabic only.
  - Salla's numbers recur across unrelated lists.
  - On Shopify, 10 route paths are code expressions, and some permission titles are computed per shop. The SH register row `shopify/admin-permission-tree` notes that "Mark as paid" becomes `RECORD_PAYMENTS` on Plus.
- **Register and folder disagree.**
  - The SH register row `shopify/admin-webhook-topics` says the admin's response was not copied and only its sha256 is kept.
  - But `SH/admin-webhook-topics/fake-demo-sharrwah/source.0.json` (14,451 bytes) is that response, including the store's `webhookSharedSecret`.
  - Under the repository's rules this is evidence like any other. I flag it only because register descriptions may be out of date elsewhere too.

---

## 10. How the counts were made

**Scripts.** They are read-only, run with `python3 -I` from the scratchpad, and read the evidence by absolute path. All are in `/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/`:
- `survey.py`
- `sh_router.py`
- `sh_gql.py`
- `sh_join.py`
- `sa_nav.py`
- `sa_ops.py`
- `events.py`
- `crossjoin.py`
- `probe.py`

**Choices that affect the counts.**
- `sh_join.py` reads the path expression `${o.settings()}/*` as `/settings`, and counts a route as gated if it or a parent names a handle in `permissions`, `oneOf` or `organizationPermissions`.
- `sa_ops.py` reads scopes from each operation's "Scopes" block.
- `crossjoin.py` and `probe.py` use plain name normalization and keywords. Their numbers are indicative, not assignments.
