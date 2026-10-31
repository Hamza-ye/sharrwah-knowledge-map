# SH-15: notes

Shopify's `admin-router`, 130 entries: items 832 to 995 of `structures/shopify/admin-router/items.jsonl` (observed-sh at `e38dc17e3`), the sections Orders (entries 1 to 50, from the draft orders) and OrganizationSettings (entries 51 to 130, up to the partner payouts of its second tree). Effort `high`.

## What I read

- The brief, the router digest (`held/rules/admin-router.md`, whole, its section 6 included), and the last section of `held/review-H-rulings.md`, with the ruling after SH-43 that the coordinator sent while the batch ran.
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the router's `REGISTER.tsv` rows, `index/ledger-summary.tsv`'s admin-route rows and, by route, `index/ledger/admin-route.tsv`; the evidence map; B-extent's "Cells and evidence" and "Conventions from the dry run".
- Batch notes: only `notes-SH-12.md`'s lines on `new:Email customer` (by grep), to align entry 46 with the thing SH-12 named. Earlier placements read by line, for twins: SH-9 (the store's Billing modals and pages), SH-10 (settings/checkout's catch-all), SH-14 (its last lines, the batch before mine), SH-31 (Feature test drives), SH-35 (Shopify Product Network), SH-42 (the email invoice modal), SH-50 (Payment reminders).
- Each route's item in `items.jsonl` (modules, intents, eligibility, eligibilityMatch, redirect), `derived/intents.tsv` for every intent (none of the batch's 17 intents has an Intents API page), `structures/shopify/admin-betas/` for beta bfbcab91, and a visit's text only where a route's own fields left its capability or support open (Product Network orders, Scan to verify and Scan to pick, the bulk action, the organization's Billing and a store's billing in it, the partner routes, Users and Groups, and the journey steps of the organization's billing).

## The split with SH-14 and SH-16

- SH-14 ended in the OnlineStore section. Orders begins at item 831 (`draftOrders`, which the concern map cites), so no section is split with SH-14.
- SH-16 begins at item 996, `organization-settings:organizations:partner-billing`, the second tree's container of partner billing. Its children twin my entries 95 to 97 (`settings:organizations:partner-billing:*`, CM-PTN-004 `core`), and its other routes may twin the first tree's. The coordinator may align them.

## What each section's routes are

- **Orders:** draft orders (CM-ORD-005: the calculate endpoint, Drafts, a draft's page, and the splat redirect as `shows`); metafield lists (CM-CNT-002, the app-controlled ones `core;extension-point`); Product Network orders (CM-ORD-001 and CM-CHN-005, both `core`); Payment reminders and an order's Payment terms (CM-PAY-008); the order list and page (CM-ORD-001); write-off reversal (CM-ORD-001 `shows`, its beta bfbcab91 false in both held stores); fulfilment holds, packing, scanning, fulfilment requests and the next shipment (CM-SHP-009, the requests with CM-SHP-011); payout breakdowns (CM-PAY-005); returns, return labels and the return request redirects (CM-RET-003, the redirects `shows`); batches (CM-SHP-010); the insurance claim (CM-SHP-003); recording and capturing payments (CM-PAY-016, CM-PAY-020); cancelling orders (CM-ORD-004); voiding a shipping label (CM-SHP-002); the native routes named for mobile (CM-SRF-001 beside their own capability); Send invoice (CM-ORD-005, below); Contact customer (`new:Email customer`). The fallback at `orders/*` is `out`.
- **OrganizationSettings:** the organization's Billing and each of its stores' billing (CM-PLN-004; payment methods and authentications CM-PLN-005; tax info CM-PLN-007), as SH-9 placed their twins in the store's Billing; the Organization page (CM-ACC-003, its anchor Business Entities CM-ACC-004), creating a store (CM-ACC-003) and business details (CM-ACC-004); Feature test drives (CM-EVO-001); Users (CM-STF-001), Roles (CM-STF-002), Groups (CM-STF-003), the collaborator route (CM-STF-005) and the user activity log (CM-TRU-003); partner billing (CM-PTN-004) and partner payouts (CM-PTN-003). The billing catch-all is `out`.
- The section OrganizationSettings is CM-ACC-003's in the concern map (SH-S-1589), but the section gives no line (the digest's rule 3), so each route takes the capability its own words name. CM-PLN-004's cell already reads the organization's Billing as its own ('Billing pages in the store's and the organization's settings'), and CM-ACC-003's note names the organization's Users and Billing as its settings.

## The new thing

- **`new:Email customer`:** SH-E-d00ddc9a, `order:mobile:email-customer`, titled 'Contact customer', with a CM-SRF-001 line.
  - **What it is:** staff emailing the order's customer, a modal over the order's page at `orders/:orderId/mobile_email_customer`, for the native client only. It loads the order page's loader (`OrdersOrderDetails-loader`) and has its own component, `MobileOrderEmailCustomer`.
  - **The same thing as SH-12's** `mobile-email-customer:show` (SH-E-b3247925), as the digest's section 4 says, so it keeps that name for the coordinator to align. Its title here is 'Contact customer'.
  - **Its place of its own:** this admin route, a modal with its own path and title.
  - **Proposed, as SH-12:** domain D, area CUS, parent CM-CUS-001; another reading puts it under CM-NTF-001, beside CM-NTF-004.
  - **Its name:** English only, since the admin isn't held in Arabic (`docs/GAPS.md`).
  - **Terms searched:** 'contact customer; email customer; customer email; send email; staff email' (`caps --terms`). They found only CM-RET-004, by 'staff email', which isn't this. I read the cells of the entry's leads: CM-MKT-007 (campaigns), CM-NTF-004 (its Shopify side is the SMS sender ID), CM-API-004 (an app's access to buyers' data) and CM-CUS-007 (consent). None is a staff member writing to one customer, as SH-12 found.

## The rules I followed that the digest doesn't state, for the coordinator

- **R15.1:** a loader-only callback whose visit landed on another page is a redirect (the digest's rule 11). It is `shows` on the landing's capability, even where its twin with no visit stayed `core`.
  - The cases: `organization-billing-shop:invoice-complete-authentication` (SH-E-55db6aea). Its journey step 62 requested `…/complete_payment_authentication` and landed on the bill (`raw/runs/20261005T102756Z-journey-organization-billing/actions.jsonl`). And `billing:next:profile:complete-authentication` (SH-E-24b8ee07): six of seven sweeps landed on `settings/organization-billing`.
  - SH-9's twins with no visit, SH-E-3dfc6e4e and SH-E-29bae7c9, are `core` on CM-PLN-005. If the coordinator reads the callback's own work as the thing (completing a payment authentication), as R14.2 does for a callback with a page, both lines become `core` on CM-PLN-005.
- **R15.2:** a route tree that repeats another under a second parent takes its twin's line, the concern map's included, with its own gates as its scope. The case is OrganizationSettings' `organization-settings:organizations:*` beside `settings:organizations:*`: the same paths, loaders and components, the same ledger addresses and visits. My entries 102 to 130 follow the first tree's lines and the concern map's (SH-S-5228 to SH-S-5240, SH-S-7151).
- **R15.3:** a route whose id names mobile but whose eligibility admits every client (no `clients` gate) takes no CM-SRF-001 line, and its reading says so. The cases: `order:mobile:payment-terms`, `:send-invoice`, `:hold-fulfillment`, `:fulfillment-request-cancellation`, `:cancel-return`, `:upload-return-label` and `:cancel-orders`. A native-only route whose id and path name no mobile names its client in `reading` (`order:bulk-action`). This reads the digest's rule 35 strictly.
- **R15.4:** a redirect whose target page takes a second line for an anchor takes both lines where its own words name the anchor's thing. The cases are the business-details index routes (SH-E-80042c6a, SH-E-5224728f), sent to the Organization page: CM-ACC-003 for the page, and CM-ACC-004 for its anchor Business Entities, the business details the route's words name.
- **R15.5:** a visit that the ledger joins to a route only because the route's pattern matches another route's address is that other route's visit, and states nothing of the route (the digest's rule 7). The cases:
  - `…:accounts:collaborator` at `:accountId/:shopId`, joined to the visits of `roles/:roleId`;
  - `organization-billing:catch-all` at `:catchAll/*`, joined to `store/…` visits;
  - `draftOrders:redirect` and `orders:fallback` at `*`, joined to their prefix's own visit.
- **R15.6:** a fulfillment order's request routes ('Request fulfillment', SH-E-506b2350; 'Request cancellation?', SH-E-61545990) take CM-SHP-011 beside CM-SHP-009. This is a reading of CM-SHP-011's cell: fulfillment services accept or reject requests to fulfill orders (SH-S-0704). The route's own words name no fulfillment service.

## Entries I couldn't tell, and what would settle each

- **SH-E-6e828d67, Send invoice (an order's, the mobile route):** CM-ORD-005, keeping to SH-42's line on the changelog's 'email invoice modal on Orders and Draft orders' (SH-E-f543d41f). The other readings are CM-PAY-032 (payment links, which holds nothing for Shopify) and CM-ORD-015. A visit to an unpaid order's Send invoice page would settle it, or help's page on sending an order's invoice.
- **SH-E-ae8f3d2c and SH-E-a4591f73, the payout breakdowns:** CM-PAY-005. They could instead be a network sale's commission split (Product Network or Collective). An order with a payout, opened at the modal, would settle it; they need an instance.
- **SH-E-88713235, `order:fulfillment:prepare-package`:** CM-SHP-009 by its own path. Its component `PreparePickup` points to local pickup (CM-SHP-007); a visit to a pickup order would settle it.
- **SH-E-584378b9 and SH-E-917fb8db, `review/:accountId`:** CM-STF-001, by the user page's loader and component. 'Review' could be a collaborator request's review (CM-STF-005) or an account review. A visit with an account under review would settle it.
- **SH-E-61545990, the CM-SHP-011 line:** a reading (R15.6).
- **SH-E-a5d17065, SH-E-2c02f51b and SH-E-64241c46, the test drive:** CM-EVO-001, as SH-31 placed Feature test drives. The concern map places the test drive's eligibility, the organization feature TEST_DRIVE, on CM-ACC-003 (SH-S-5232). I gave CM-ACC-003 no line, since a gate's feature gives none (the digest's rule 6). If the coordinator reads the organization's test drive as an organization setting, each takes a CM-ACC-003 line.
- **SH-E-39ac0126 and SH-E-c5c92a40, the return labels:** CM-RET-003. Whether the label is bought through the platform (CM-SHP-002) isn't stated, and no run opened either.
- **SH-E-50fd1d85 and SH-E-e62285fa, Scan to verify and Scan to pick:** CM-SHP-009, read from their titles and modules. capture-grow's sweep answered “There's no page at this address” at both. A store eligible for fulfillment batching, or the native client, would show what they are.

## The ruling after SH-43, as it bears on this batch

- Shopify Product Network (SH-E-a40368bd, SH-E-80dda083): help calls it 'the Shopify Product Network app' (`structures/shopify/help-center/help.shopify.com@en-ar/outline.md`, line 11599), and `held_entries.py makers` finds no maker statement. My lines are on the admin's own route for it, in the section Orders, so they stay `core` (the ruling after SH-43, with the ruling after SH-41), with the maker a gap. The ruling names Product Network's changelog line (SH-35) among those aligned at Shopify's amendment.
- No other line of mine rests on an app's own feature with no maker held.

## What a run step or source states that no entry holds (M-12), for the second stage

- `derived/step-text-from-html/20261004T092557Z-sweep-instances/044.html.txt`, line 126: 'Next bill in 27 days or when your $1,280 USD threshold is reached. You have $1,280 remaining.' This is a store's billing threshold, a quality for CM-PLN-004.
- `derived/step-text-from-html/20261002T004032Z-sweep-capture-grow/363.html.txt`, lines 89 and 92: 'User account limit reached. Remove users from your stores or view pricing for plans with higher limits.' This is the staff account limit by plan, for CM-STF-001 (its plan line Additional staff accounts).
- `raw/runs/20261005T115840Z-journey-organization/steps/039.text.txt`, lines 56 to 82: the organization's Billing with 'Store billing', each store's plan (Unlimited, Shopify plus, Professional, Basic) and amount. This is for CM-PLN-004, and for CM-ACC-003 as the organization's stores.
- `structures/shopify/help-center/help.shopify.com@en-ar/outline.md`, lines 11597 to 11602: help's Shopify Product Network pages, among them 'Eligibility requirements for using the Shopify Product Network app'. They bear on CM-CHN-005's maker gap and its eligibility. The app's listing (`apps.shopify.com/product-network`) isn't held (`held_index.py`).
- `structures/shopify/admin-router/items.jsonl`, line 835: `draftOrders:show`'s intent carries tool descriptions written for Shopify's admin agent (`getDraftOrderSummary`). I read them as data and followed none (the digest's rule 41). They are a lead for the admin's AI assistant.

## Structures whose items and sources disagree

- None found. `order:ship-next`'s path `:orderId/ship_next`` holds a backtick, and the source holds it too (`structures/shopify/admin-router/source.jsonl`), so the item copies the source.
- `index/ledger/admin-route.tsv` joins a route whose path is a pattern to visits of other routes' addresses (R15.5). Its owner could mark such joins.

## Problems with the brief or the scripts

- **`method/held_router_gates.py` skips an ancestor whose id is a substring of a line's reading.** So a reading that names a child or a resource beginning with the ancestor's id loses that ancestor's gate. Examples are `organization-settings:organizations:details:list` holding `organization-settings:organizations` (DIRECT_ACCESS), and the resource `draftOrders` (storefront.enabled).
  - Its dry run first reported 44 of 55 lines; I rephrased four kinds of reading, and it now reports 55 lines of 53 routes.
  - The script could match a whole id, or only its own phrase 'reached under <id>'.
  - Earlier batches' lines that name a child's or a twin's id may have lost an ancestor's gate the same way.
- **`held_router_gates.py --help` is read as a batch name** and fails. Its docstring gives the usage, and a run without `--apply` only prints.
- **`held_entries.py earlier` matches route ids whole,** so it printed no twin across the two OrganizationSettings trees, nor between the Billing section's modals (`billing:profile:*`) and the organization's (`organization-billing-next:billing:profile:*`, `organization-billing-shop:billing:profile:*`). I found them by path and by the id's last part. A match on the id after its namespace, or on the resolved address, would print them.

## The check

`python3 -I method/held_entries.py check --platform shopify --batch SH-15`: no `CHANGES` line. The `NOTE` lines are the containers, each named in its reading with its children, and the new thing's leads, whose cells I read (above). `NEW`: Email customer.
