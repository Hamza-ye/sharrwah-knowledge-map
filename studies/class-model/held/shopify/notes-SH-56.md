# SH-56: Winter '24, from Operations' Financial Services to Developer's App Development (high)

**What the batch is.** 83 entries of `editions-page-data` (observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`, line 6, `routes/($lang).editions.winter2024`), in the page's order:
- Operations (`pageSections/3`), its last twelve `sectionGroups`, 5 to 16: Financial Services (entries 1, 2), Tax and Tax updates (3 to 6), Admin/Mobile App (7 to 9), Admin (10 to 14), Flow (15 to 18), Ship like a pro and the two Shipping/Fulfillment groups (19 to 27), Exchanges (28), App Store and Apps (29 to 32). SH-55 held groups 0 to 4.
- Developer (`pageSections/4`), its groups 1 to 16 (5 and 15 hold no product): OS 3.0 and Liquid Dev (33 to 40), Hydrogen and Hydrogen/CA API (41 to 51), Customer Accounts (52), the two Checkout Extensions groups (53 to 62), Variants (63), Shipping Functions/Discounts/Reducer (64 to 66), Discount/Fulfillment/Marketing APIs (67 to 72), Store Credit (73), Shopify Flow (74 to 76), UI extensions (77 to 79) and App Development (80 to 83). SH-57 begins with group 17, 'Developer - DevX - M - Webhooks and Functions'.

I read each entry against its product in the page data (line 6, by its pointer). `show` leaves out a field whose value is empty: 81 of the edition's products have an empty `productType` and 10 an empty `description` (among mine, the five lead cards 15, 33, 41, 74 and 80). I checked this in the item, so nothing is missing. Every group's `description` is empty, and each card is read with its section, its `productType` and its `headlineTitle` (SH-54's E30).

**Count.** 137 lines: 134 on a capability, 3 `new`.
- Every entry is placed, and none is `out`.
- 80 entries are only on capabilities. None is only `new`. 3 are on both: SH-E-1d061b2f (Saved views), SH-E-4dcb5dea (Admin search) and SH-E-b8c4bf95 (Web performance dashboard).
- Supports over the lines, a line with two supports counting in each: `core` 81, `extension-point` 27, `shows` 25, `own-service` 8.

**E1 to E41 are kept,** with the rulings in `review-H-rulings.md`'s last section. The ruling after SH-55 makes Shopify Flow's own features `own-service`. Its maker statement is 'Today we’re introducing test runs in Shopify Flow' (SH-E-0678ff26, printed by `held_entries.py makers`). `makers` found none for Bill Pay. Shopify Balance and Shopify Tax have 'we’ve added' posts, but earlier batches placed them as the platform's own admin services, `core`, and I kept to that.

`held_entries.py earlier` printed no earlier line for any of the 83 entries. No batch had placed these groups. I read SH-55's last lines (Lending and Balance) and kept to them on Balance (SH-E-22226326).

## Rules I followed where E1 to E41 don't reach

### E42. A notice a feature sends the store's staff

Two cards name a notice to the merchant as one of the feature's own things:
- Bill Pay: “You'll be notified whenever a bill is paid.” (entry 1);
- Flow's failed workflows: 'Automatic notifications for failed workflows', with the lead card's 'notifications for Flow' (entries 18 and 15).

I gave each a CM-NTF-002 line (staff notifications) with the feature's own support. Bill Pay's is `core`, since it is at the admin's finances/billpay. Flow's is `own-service`, by the ruling after SH-55. Earlier batches put an app's notices to the store there too, such as Forms' 'email notifications on form submission' (SH-E-ea456de2, `core`). If the coordinator reads such a notice as part of the feature, the three lines fold into CM-PAY-027 and CM-AUT-001, and CM-NTF-002's `own-service` goes (case 1).

### E43. A group whose lead card states a developer preview

OS 3.0's lead card says 'New theme blocks in developer preview', with 'Sign up for developer preview' (entry 33). Its three cards, Theme blocks, Nested theme blocks and Blocks presets (34 to 36), state no release of their own. I read them with the lead card's limit, as E5 reads a collection's cards, so all four are `shows` on CM-SFR-002. That capability's cell holds 'generating theme blocks' (SH-I-0990).

A card that states its own preview is `shows` by its own words: Customer Accounts Extensibility, the variants API, the Discount Allocator and Store Credit (52, 63, 66, 73). 'Now in full release' and 'stable release' (64, 78, 49) are release markers. Their support is the one the card's words give.

### E44. The CLI is CM-DVT-002

Four cards name a CLI command: the Liquid console (37), `h2 deploy` (44), ‘h2 upgrade’ (46) and Flow's `dev` command (76). Each takes CM-DVT-002, the command-line tool, which is narrower than CM-DVT-001 (rule 2). The earlier Editions batches placed the CLI there (SH-E-f8406c78, SH-E-0f55ae79 and others). Theme Check and its LSP features (39) and the app libraries and template (83) stay on CM-DVT-001.

### E45. Webhooks the platform sends apps

'Third party apps can now use webhooks to get notified when metaobjects … are created' (38) and 'Dedicated webhook topics … helping keep your discount apps in sync' (67) are `core`:
- on CM-API-008, whose cell reads webhooks as 'Shopify's own delivery to an app, not work done by the app';
- on the capability whose events they carry (CM-CNT-002, CM-MKT-001).

E3 made 'Apps can now use metafields' `extension-point`. There, apps store their data in metafields. Here, apps only receive the platform's events. If the coordinator reads 'apps can now use' as E3 does, the four lines become `extension-point`. No cell changes either way.

### E46. A new thing's support is what the platform does with it

The coordinator's check after SH-54 reads a new thing's support as what the platform does with it, and keeps `shows` for a thing that is only named. My three new lines are the platform's own released features, so they are `core`:
- the inventory page's saved views (25);
- the admin's search for apps (32);
- the RUM API's Core Web Vitals (40).

SH-35, SH-36, SH-37 and SH-54 wrote `shows` for Saved views and Admin search. The coordinator aligns them.

### E47. A store's setting shown in the admin

'Add a personal touch to your Shopify admin with a custom logo or store icon' (11) links the admin's settings. The ruling after SH-37 makes the admin's own look no capability's thing. The logo or icon, though, is a setting of the store, so I placed it on CM-ACC-006, store details and general settings, `core`. If the coordinator reads it as the admin's look, the entry is `out` (case 5).

### E48. Address validation at checkout is CM-CUS-009

'Now addresses in checkout are automatically validated and corrected for free' (20), and the lead card's 'automatic address validation' (19), are `core` on CM-CUS-009, the map and location services for addresses. That cell's own reading holds Shopify's address autocompletion at checkout, and SH-54 put apps' address correction at checkout there (SH-E-6242fae0).

The changelog batches put the admin's validation of order addresses on CM-CUS-008 (SH-E-8de93795, SH-E-1a244cc9). CM-CUS-008's note leaves out 'the order's shipping address'. The coordinator may join the two.

### E49. What an order edit changes stays with the edit

'Edit shipping costs and discounts on orders' (23) is one line, on CM-ORD-002. Its cell already holds the discounts applied in an edit: 'an order-edit mutation needs the user's apply_discounts_to_orders permission'. So the shipping line and the discounts are what the edit changes, as CM-MIG-001's note keeps the objects of an import in its reading. Entry 7's smart collections and metafields are kept the same way.

### E50. Other readings of this batch

- **Carriers of Shopify Shipping.** USPS Ground Advantage (26) and UPS Ground Saver (27) follow E15: `core` on CM-SHP-002 with the carrier as filler, and CM-SHP-015 `shows`. UPS Ground Saver's card doesn't name Shopify Shipping. It links the admin's orders ('Try UPS Ground Saver in Orders'), and I read it with USPS's card.
- **The Shopify Fulfillment Network** (22):
  - 'Connect your store with our official fulfillment partner Flexport' is `extension-point`, Flexport its filler. 'Our' names Flexport as the partner, and no held statement places Flexport in the group.
  - 'track fulfillments without leaving Shopify' is `core`, by the ruling after SH-2 (case 3).
  - The CTA's address, admin.shopify.com/shopify-fulfillment-network, isn't an `apps/<handle>` route, so it takes no CM-APP-007 line. CM-SHP-012's cell reads that route as the app's page.
  - The ruling after SH-55 names the Fulfillment Network among the apps with no maker statement held.
- **Tax** (3 to 6):
  - The US sales tax report is CM-TAX-002 and CM-ANL-002, scope US, as SH-54 placed the same report (SH-E-a77b9c6a).
  - The Tax Platform with Vertex is CM-TAX-004 `extension-point`, Vertex its filler.
  - 'Shopify Tax supports international businesses selling in the US' takes the kind of business as its scope (E27), on CM-TAX-002, CM-TAX-003 ('determine where you may be liable') and CM-ANL-002.
  - The VAT guidance for France, Germany and the UK is a help doc: CM-TAX-003 `shows`, a guide, and CM-ONB-003 `core`, the platform's learning (case 9).
- **The App Store** (29 to 32): its guided search, its comparison of up to four apps and its up-front permissions are the platform's own App Store, CM-APP-002 `core`.
  - The permissions an app needs are its install consent: CM-API-003 `shows` (the ruling on S7).
  - 'our install flow' is CM-APP-001 `core`.
  - The guided search's 'AI-powered guidance' takes CM-AIA-001 `core` (case 6).
- **Shopify Flow for developers** (74 to 76):
  - The lead card is `own-service;extension-point`: Flow's own features, and the triggers apps add to it, which the next cards describe.
  - The `Run code` action is `own-service`, with CM-APP-007 for its apps/flow address.
  - Triggers built with the `dev` command are `extension-point`: third parties' extensions of Flow (the ruling after SH-55).
- **The Selling Plan API's automatic discounts** (62) are `core` on CM-MKT-003, discounts applied without a code, as SH-54 placed draft orders' automatic discounts. The Selling Plan API is `extension-point` on CM-SEL-001, as SH-51's E13 placed the subscription APIs.
- **Function APIs** (55, 61, 64 to 66) are `extension-point`, by their capabilities' own definitions (E24). A card whose title or `productType` names Shopify Functions takes CM-APP-005 too (M-6 refined). Cart Transform's add-ons and bundle components are what it may change, named in a list, so they take no CM-SEL-006 line.
- **Case studies** (50, 51, 59) are `shows` on each feature they name (E19). The merchants and the agency Form Factory aren't fillers. Checkout Blocks (59) is Shopify's own app ('we’re upgrading the Checkout Blocks app', SH-E-a2643162), but the story states none of its features, so it takes no `own-service` line.
- **The RUM API** (40) is the platform's own API for the store's own data, a guide to developers naming no app: CM-ANL-006 `core`. It takes `new:Web performance dashboard` too, so it is decided with SH-55's dashboard for the same Core Web Vitals.
- **Qualities (E9):**
  - 'No additional software, technology, or costs' (the 3D scanner);
  - '60+' reports;
  - 'for free where possible' (address validation);
  - 'Eligible merchants can save up to 10% on their first inventory batch';
  - USPS's '2–5 business days' and 'Save up to 86% compared to standard retail rates', a discount on rates as SH-54 took DHL's 'reduced by 13.25%';
  - UPS's 'Monday to Sunday deliveries' and 'no volume commitments';
  - 'up to four' apps compared;
  - 'up to eight layers of blocks';
  - '50+ new color properties';
  - 'up to 2,000 variants per product'.

  Nour Hammour's '63% year-over-year increase in conversion rates' is a claim.

## New things

Shopify's Editions are in English only, so no Arabic name is held.

| New thing | Entries | Place of its own | Proposed domain, area, parent | Terms searched (`caps --terms`) | Leads read |
| --- | --- | --- | --- | --- | --- |
| Saved views (SH-35's) | SH-E-1d061b2f: 'saving filters', 'Access these views conveniently at the top of the inventory page', `core` | None in this entry: a feature of the inventory page, whose own place is CM-INV-001's (`products/inventory`) | As SH-35: F, near the admin's tools, no parent; or no capability, if read as the admin itself | saved view; saved filter; custom view (none) | CM-SFR-013 (the storefront's search and filters, not the admin's) and CM-ORD-003 (by name): neither |
| Admin search (SH-36's) | SH-E-4dcb5dea: 'The global search in the Shopify admin now supports searching for popular apps by name', `core` | None in this entry | As SH-36: decided with Zid's and Salla's admin search (the ruling after SH-37) | admin search; global search; search for apps (none) | CM-APP-002 (placed: the App Store's apps found from the admin), CM-SHP-017 (by name), CM-SFR-013 (the storefront's search): none is the admin's search |
| Web performance dashboard (SH-55's) | SH-E-b8c4bf95: 'your store’s Core Web Vitals', 'monitor web performance', through the 'public RUM API', `core`, beside CM-ANL-006 | None in this entry: an API query (`performanceMetrics`, its address under `unstable`), not an API group | As SH-55: E, SFR, beside CM-OPS-003, or D, ANL, under CM-ANL-001. If the coordinator names it for the storefront's performance data rather than the dashboard, this line keeps it | Core Web Vitals; RUM; performance metrics; web performance; site speed (none) | CM-ANL-003 ('dashboard': overview dashboards of sales, a homonym, as SH-55 found), CM-B2B-007, CM-CHN-007, CM-SFR-011 (by 'storefront' or name), CM-DVT-001: none |

## The CHANGES lines, and what I decided on each

Each line was read again against its source.
- **CM-AUT-001 gains `own-service`** (lines 25, 27, 29, 31, 126, 127): Shopify Flow's own features, by the ruling after SH-55, whose maker statement is 'Today we’re introducing test runs in Shopify Flow' (SH-E-0678ff26). The ruling has aligned 38 earlier lines. Kept.
- **CM-NTF-002 gains `own-service`** (lines 26, 32): Flow's notices of failed workflows, a feature of the first-party app (E42). Kept, case 1.
- **CM-PAY-028 gains `core`** (line 3): Bill Pay's 'automatically syncing invoices from Gmail, QuickBooks Online, or Stocky'. The store's bills are brought in from an accounting system by the platform's own Bill Pay, at the admin's finances/billpay. QuickBooks Online is the filler. The cell had held only the App Store's accounting categories. Kept, case 2.
- **CM-SHP-012 gains `core`** (line 40): 'track fulfillments without leaving Shopify', the platform's own words for its admin (the ruling after SH-2), beside Flexport's `extension-point`. Kept, case 3.
- **CM-DVT-006 becomes held, `core`** (line 77): 'Let anyone preview your Hydrogen storefront deployment, even those without access to admin, using tokenized links'. A deployment is previewed apart from the live storefront, which is CM-DVT-006's thing (a reading). SH-11 put Hydrogen's Production and Preview environments there, `core` (SH-E-6eebf1f1, SH-E-040a5a3a), so the change isn't this line's alone once SH-11 is amended. Kept, case 4.
- **CM-MKT-003 becomes held, `core`** (line 105): 'The Selling Plan API now supports automatic discounts on subscription products', 'Automatic discounts now work with subscriptions'. This repeats SH-54's change (draft orders' automatic discounts), which the coordinator let stand. Kept.
- **CM-CHN-006 gains `core`** (line 99): Checkout Sheet Kit, the platform's own kit for the store's own mobile app. This repeats SH-54's change (SH-E-b3ea5e29), which the coordinator let stand. Kept.

## Entries I couldn't tell, placed where they most plainly belong

1. **Notices on CM-NTF-002** (SH-E-f2b55645, SH-E-2db06db9, SH-E-27194e31). To settle: whether a feature's notice to the staff about its own events, such as a bill paid or a workflow failed, is the staff notifications capability's thing, or the feature's own.
2. **Bill Pay's invoice sync on CM-PAY-028** (SH-E-f2b55645). CM-PAY-027's cell holds 'Shopify Bill Pay is provided by Melio' (`outside`), which the card doesn't say. To settle: whether an accounting system that a payment feature reads bills from is CM-PAY-028's 'connecting the store's sales and finances to an accounting system'. Gmail and QuickBooks Online are fillers on CM-PAY-027's line too, as the parties of the sync (E15). Stocky is Shopify's own app, so it is no filler.
3. **The Shopify Fulfillment Network's `core`** (SH-E-951ac77a). To settle: whether 'without leaving Shopify' is a held statement that outranks the route's apps permission, as 'its own page in your Shopify admin' did for Agentic (the ruling after SH-2).
4. **CM-DVT-006** (SH-E-b3ce6420). To settle: whether a preview deployment of a custom storefront is a staging environment as BigCommerce's StagingPro is. 'Catch bugs before they ship, with improved support for automated end-to-end testing' (SH-E-ed8a62d6) and the runtime mirroring (SH-E-914295c9) are further leads. I placed them on CM-SFR-011 and CM-OPS-003 only.
5. **The admin's logo or store icon** (SH-E-a37cae23), `core` on CM-ACC-006 (E47). To settle: whether a store's icon shown in its admin is the store's detail or the admin's look.
6. **The App Store's AI search on CM-AIA-001** (SH-E-ea2e312c). CM-AIA-001 is 'the platform's AI features in the merchant's admin', and the guided search is on apps.shopify.com. To settle: whether the platform's AI for merchants outside the admin is CM-AIA-001's.
7. **Fulfillable inventory** (SH-E-e42d2b53), `shows` on CM-INV-001 and CM-SHP-001: 'limiting products available on the storefront and checkout to inventory that's physically fulfillable based on your shipping configurations. Available to select businesses.' CM-INV-010, products shown by the customer's city, which holds nothing on Shopify, may be the same thing: products a buyer sees by where they can be delivered. Its note says that following the stock at locations is a reading. To settle: CM-INV-010's definition.
8. **Webhooks `core`** (SH-E-bd999336, SH-E-65b5cf56), against E3's 'Apps can now use metafields' (E45).
9. **VAT guidance** (SH-E-f826f940): 'Shopify now provides merchants … with comprehensive guidance on VAT registration', a help doc. I placed it `shows` on CM-TAX-003 and `core` on CM-ONB-003. The title 'VAT recommendations' may name recommendations in the admin's tax settings, which the card doesn't state. If it does, the line is CM-TAX-003 `core`.

## Structures whose items and sources disagree, or leave things out

- **None disagree.** `show` omits fields whose value is empty (`productType: ''`, `description: ''`), which is right. I checked it in the item.
- **The Developer section's four groups with no products** (`pageSections/4/sectionGroups/0`, `5`, `15`, `20`), titled 'Storefronts', 'Extensibility', 'Developer experience' and 'App Growth', head the cards after them. No entry holds them, since the structure's entries are products. Each names a grouping over several capabilities' cards. By the ruling after SA-28 such a title would be `out`, and none is placed.

## What the sources state that no entry holds (for the second stage)

- **The four Developer headings above.** They are layout titles, a lead for no cell.
- **Release states in the cards' link addresses.** The links point under `unstable` (`admin-graphql/unstable/queries/performanceMetrics`, `checkout-ui-extensions/unstable/apis/customer-privacy`, `checkout-ui-extensions/unstable/components`) or to `release-notes/developer-previews#…` (the variants, the discounts allocator, store credit). Each line names the state in `reading`, and the support stays the card's (SH-51's E13).
- **The Discounts allocator.** observed-sh's `docs/GAPS.md` ('Shopify Functions the platform does not offer or accept from the capture app') holds its release refused to the capture app: 'API not found for target: `purchase.discounts-allocator.run`'. This agrees with entry 66's developer preview, `shows`.
- **Held changelog posts on this batch's features,** from `makers`. Their own batches place them, and the coordinator may align them:
  - 'New release: On September 14, 2023, we released the ability to set aside sales tax on Shopify Balance.' (SH-E-d7795c30), entry 2's feature;
  - 'We're thrilled to announce the launch of the Shopify Tax Platform, a robust infrastructure that can integrate your preferred tax service with Shopify.' (SH-E-2308aaa9), entry 4's;
  - 'That’s why we’ve upgraded Shopify Tax’s enhanced sales tax report so you can select the exact timeframe you need to file.' (SH-E-9ec6f277, SH-E-8e417824), entry 3's.

  `makers` printed no line for any of them.
- **The changelog posts the Flow cards link** (`shopify-flow-improved-ux-for-browsing-and-searching-tasks`, `shopify-flow-get-notified-when-errors-happen`), and shopify.dev's post on syncing external marketing activities (entry 71). They are leads for the coordinator to join with their own batches' lines.

## Problems with the brief or the script

- **The checker's brand NOTE** fires on the platform's own services named with its brand: Shopify Tax, Shopify Shipping, the Shopify App Store, the Shopify admin and the Shopify app, and the CM-APP-007 lines for Flow's address. I read each again. Each is `core` by E3 or E7 (an admin address, a plan statement, or the platform itself), and each reading names the words that place it.
- **The NOTE on a new thing whose entry has leads** points at the entry's first line: lines 43 and 68, whose `new` lines are 44 and 69, and line 56, the `new` line itself. I read the leads it names (the table above).
- No other problem. `makers` answered the maker question for Flow, Bill Pay, Balance, Tax and Checkout Blocks in one call each, with no search of other structures.

## Where B-extent and the brief differ

None I relied on.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 83 of 83 entries, no problem.
- **The cell changes stand, each read again:**
  - CM-AUT-001 and CM-NTF-002 gain `own-service` from Shopify Flow's own features and its notices of failed workflows (the ruling after SH-55; E42).
  - CM-PAY-028 gains `core`, a marked reading: Bill Pay's 'automatically syncing invoices from Gmail, QuickBooks Online, or Stocky', at the admin's own page, QuickBooks Online its filler. Bill Pay's provider, Melio, stands on CM-PAY-027's cell.
  - CM-SHP-012 gains `core` beside Flexport's `extension-point`, a marked reading: 'track fulfillments without leaving Shopify'.
  - CM-DVT-006's shareable Hydrogen preview stands beside SH-11's environments.
  - CM-MKT-003 and CM-CHN-006 repeat SH-54's changes.
- **E42 to E50 stand for SH-57 to SH-67, with one alignment.** Address validation is CM-CUS-009's (E48), an address service beside autocompletion, as SH-35's line 91 places 'our address autocomplete and validation systems'. SH-38's lines 135 and 144 and SH-39's line 68, which wrote CM-CUS-008, are aligned. E45's webhooks for apps change no earlier line, since none wrote `extension-point` on CM-API-008.
- **New things:** Saved views, Admin search and Web performance dashboard. This batch writes them `core` and SH-35 and SH-36 `shows`, so their support is decided with them.
- **For the second stage:** the four Developer headings with no products: Storefronts, Extensibility, Developer experience and App Growth.
- **Cost:** 20.4 million tokens over 83 requests, about 246,000 an entry, against SH-55's 370,000: `makers` answered every maker question in one call. The context reached about 411,000 tokens.
