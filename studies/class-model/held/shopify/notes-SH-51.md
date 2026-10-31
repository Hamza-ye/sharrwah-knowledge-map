# SH-51: Shopify's `editions-page-data`, Winter '23's last solution items and the first of its Product list (high)

**What the batch is.** 92 entries of `editions-page-data` (observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`, line 4, the Winter '23 Edition):
- entries 1 to 69: Winter '23's solution items from SH-50's last, 'Let shoppers manage orders and returns with new customer accounts', to the end:
  - Find & engage customers, from 'Create tokengated experiences' (1 to 4);
  - Fulfill & deliver (5 to 19);
  - Run your business (20 to 34);
  - Build with us (35 to 65), with the item 'API, extensions, and SDK updates' and its ten `apiGroups` (55 to 65);
  - Choose your components (66 to 69);
- entries 70 to 92: the first 23 entries of its Product list, Boost conversion's five collections (`productList/solutions/0/collections/0` to `4`).

**Count.** 157 lines: 153 on a capability, 4 `new`.
- Every entry is placed; none is `out`.
- 88 entries are only on capabilities, 2 only `new` (SH-E-acf42aeb Commerce Components, SH-E-a2c6d918 Sanity integration), 2 on both (SH-E-efe10fd5, SH-E-895783e8).
- Supports over the lines: `core` 99, `extension-point` 34, `shows` 27, `own-service` 8.

**SH-50's rules E1 to E12 are kept.** The coordinator's check after SH-50 keeps them. Where an entry was of a kind they don't cover, the rule I followed is below, for the coordinator to align with SH-52 to SH-67. The rulings file changed once while I worked (the ruling after SA-50 on gated settings sections). It doesn't bear on this structure.

## Rules I followed where SH-50's don't reach

### E13. An API group (`apiGroups`) is read with the edition's card for the same API

- **What the entry is.** The item 'API, extensions, and SDK updates' (SH-E-96fcc48c, Build with us > Get greater access to our platform) holds ten API groups. Each group is one entry: its `heading`, and an `apiList` of API titles, each linked to a shopify.dev changelog post or doc.
- **The container.** The item itself is a container (M-13). Its title names one part of the platform, its API for developers: CM-API-001, `core` (the ruling after SA-28, a title naming one part of the platform). Each group is placed on its own.
- **Each API title takes a line on its capability.** Where a card of the same edition announces the same API, the title takes that card's support: the same feature on two pages (E10), within one edition.
  - Return APIs follow 'Developers can provide businesses better data continuity across systems and returns apps' (SH-E-95676275): `extension-point`.
  - The ShopifyQL API follows the ShopifyQL Stable API's 'Developers can now build apps…' (SH-E-cd6a5f8e): `extension-point`.
  - The Blockchain APIs follow 'Use robust APIs and UI components… Build apps that…' (SH-E-5e333586): `extension-point`.
  - The Shop Minis SDK follows 'Access the early release' (SH-E-3d312545): `shows`.
  - The Inventory states API follows SH-E-7d771ac7: `core`.
  - The function APIs follow 'Extend your checkout' (SH-E-bb2075f4): `extension-point`.
  - The subscription APIs follow SH-50's SH-E-7a77cb5d: `extension-point`.

  A title that no card announces supports what it names (rule 4's titles): `core`, as the platform's own API for its own feature. Examples are the B2B APIs, Checkout Branding API, Product Recommendations API, Bulk Operations API and Predictive Search API.
- **The group's heading takes a line only where its APIs are kinds of its thing** (M-6 refined): B2B on Shopify, Shopify Functions, Custom storefronts, Shopify Blockchain, Custom data and Shop app. 'Fulfillment', 'Merchandising' and 'Analytics and insights' name only a grouping of their APIs and take none (the ruling after SA-28). Each such line's reading says so.
- **A linked post's address is no statement** (E7). Several addresses name a release state:
  - `cart-and-checkout-validations-are-now-available-in-developer-preview`;
  - `cart-transform-api-product-bundles-developer-preview`;
  - `order-routing-location-rule-api-developer-preview`;
  - `checkout-ui-extensions-are-now-available-on-the-order-status-page-in-developer-preview`;
  - `server-pixels-limited-release`.

  Each line names the state in `reading`, and the support stays the title's. If the coordinator reads a post's address as that post's title (rule 4: 'A release marker in it… goes in reading'), the lines on CM-CHK-005, CM-CHK-006, CM-SHP-005, CM-CHK-004 and CM-MKT-009 stay as they are, the state in `reading`. If it reads them under E5 ('a developer preview… shows'), they become `shows`. Neither changes a cell.

### E14. A collection whose first card names the offer the others describe

Choose your components > The composable stack for enterprise retail. Its first card, 'Introducing Commerce Components' (SH-E-acf42aeb), names 'Commerce Components by Shopify'. Its three other cards (SH-E-46e75736, SH-E-efe10fd5, SH-E-3867c827) describe that offer's cart, components, APIs and support without naming it. I gave them `Commerce Components by Shopify` as their `scope`: a reading, as E5 reads a collection's cards with its lead card's limit. Without it, the lines on CM-CHK-002, CM-CHK-001, CM-API-005 and CM-ONB-003 would carry no scope. The dedicated account teams and 24/7/365 support would then read as every merchant's.

### E15. Lines and fillers for named carriers, partners and frameworks

- **The carriers of Shopify Shipping** (USPS, Canada Post, DPD, DHL Express, Poste Italiane, Correos) are the label line's fillers on CM-SHP-002 (`core`). Each also takes a CM-SHP-015 line `shows`, as CM-SHP-015's own cell reads 'labels from Shopify supported carriers' (SH-S-0717, `core` in CM-SHP-002).
- **A carrier under the merchant's own account** ('work directly with UPS Canada', SH-E-50c2a6d9) is CM-SHP-015 `core`, as its cell reads the merchant's own carrier account (SH-S-0616).
- **A post's things in their own countries** take a line each, with their own scope and filler (the brief's exception): Shopify Shipping in Italy with Poste Italiane, and in Spain with Correos (SH-E-3b723f87). So do things under their own plan or offer:
  - SH-E-df2435ce: granular permissions on every plan; duplicating a role on Shopify Plus;
  - SH-E-dc510752: unthrottled API calls for Commerce Components; 10x Admin API limits on Shopify Plus.
- **Parties after 'like'.** E8 makes 'like Google, Facebook, and Instagram' no filler: there the channels are named in passing, as examples of where a discount applies. I made the parties after 'like' fillers where they are the other party of the thing itself:
  - 'customer data shared between Shopify and partners like Pinterest and Meta' (SH-E-12fe7376);
  - 'accounting integrations like Freshbooks, Bench, Sage, and more' (SH-E-b99a8166).

  Where 'like' names examples of where a thing is used, as 'React frameworks like Next.js and Gatsby' (SH-E-d87ac7e2) does, I made no filler.
- **The framework a tool is built on** is its filler, as E8 makes Prettier: 'the open-source Remix framework' (SH-E-f8406c78).

### E16. Shopify's logistics in Winter '23

The cards of Fulfill & deliver > Fully outsource your logistics read differently from Summer '22's 'Shopify Fulfillment Network', which named the network by its brand alone (SH-50, `shows`):
- three of them say 'our network of 20+ distribution hubs and fulfillment centers', 'our network that perfectly positions products closest to buyers' and 'our nationwide freight services';
- 'Advanced returns functionality' says 'our Loop Returns integration'.

'Our' on Shopify's page names Shopify, the company, as the provider of a separate service (E3's reading of 'our'). So those lines are `own-service` on CM-SHP-012, and for the returns on CM-RET-003. The card 'Configurable logistics' (SH-E-0a337a15) names no maker, and its link opens deliverr.com. No held statement places Deliverr in Shopify's group (CM-ACC-002's cell), so it is `shows`, Deliverr in `reading`.

### E17. The admin's mobile client and its list items

'Shopify app improvements' (SH-E-9e07d217) is the admin's own mobile client: CM-SRF-001 `core`, as E3 and SH-50's SH-E-7e985f36 read it. Its three list items name the features of the client, so each takes a line (E4's highlights). Those lines are on:
- CM-SFR-002, the online store editor;
- CM-CAT-007, product images;
- CM-CAT-001 and CM-CAT-002, products and variants;
- CM-MKT-006, marketing automation;
- CM-MKT-007, Shopify Email in the client, `core` as placed in the platform (E3);
- CM-INV-001, inventory;
- CM-ANL-003, the store's performance.

### E18. The Product list: each entry mapped by its collection and order

The Product list's headings differ from the items' headings: 'Checkout editor' against 'Drag-and-drop checkout editor', 'Shop Promise badge' against 'Build trust with Shop Promise'. So `held_entries.py earlier` printed SH-50's line for only 2 of the 23 entries. I mapped each entry to its item by the locators:
- each Product list entry is at `productList/solutions/0/collections/M/products/K`;
- each item is at `solutions/0/collections/M/collectionSections/*/items/*`, in order.

Every collection's counts match: 1, 4, 1, 11 and 6. Each entry takes the line of the item it names. That is the item's capability and support, with its scope where the item states one ('Checkout editor', Shopify Plus; 'Shopify Payments available in France', France). Its terms are the heading's own words. The item's other lines are taken only where the heading names their thing too:
- 'Storefront search and recommendations upgrades' takes CM-SFR-013 and CM-MKT-023;
- 'Deferred purchase options with PayPal' takes CM-PAY-013 (filler PayPal), CM-SEL-005 and Try before you buy;
- no heading names an app's admin address, so none takes CM-APP-007.

## New things

Shopify's Editions are in English only: no Arabic name is held.

| New thing | Entries | Place of its own | Proposed domain, area, parent | Terms searched (`caps --terms`) | Leads read |
| --- | --- | --- | --- | --- | --- |
| Commerce Components by Shopify: the platform's components (checkout, cart, APIs), 'more than 30', offered to enterprises to build into their own commerce stack | SH-E-acf42aeb, SH-E-efe10fd5 (its count, 'components: more than 30 components'); named as a scope in SH-E-dc510752, SH-E-46e75736, SH-E-3867c827 | None held: one section of the Editions page ('Choose your components'), with no admin route, plan line, API group or app category. So `shows` | E, SFR, beside CM-SFR-011 (a stack built apart from the platform's themes, on its commerce data), or A, PLN, as an offer for enterprises with its own API limits and support (SH-E-dc510752, SH-E-3867c827) | Commerce Components; composable; enterprise; modular; commerce stack; components | CM-PTN-010 (partners reselling the platform's stores: not this), CM-API-013 (an account-level API: not this), CM-SFR-011 (headless storefronts: no statement of composable commerce in its reading), CM-ACC-002, CM-DVT-004 (leads by name only) |
| Sanity integration (SH-50's) | SH-E-a2c6d918, the Product list's heading | as SH-50 | as SH-50 | as SH-50 | CM-APP-010, CM-MKS-004, CM-PAY-028, the checker's leads by 'integration': none holds a content system |
| Try before you buy (SH-50's) | SH-E-895783e8, the Product list's 'Deferred purchase options with PayPal' | as SH-50 | as SH-50 | as SH-50 | CM-PAY-011, CM-PAY-013, CM-AIA-005, the checker's leads: none |

## The CHANGES lines, and what I decided on each

Each was read again against its entry.
- **CM-SHP-012 gains `own-service`.** The lines are SH-E-ea1863d0, SH-E-0f3603dd, SH-E-1898004c and SH-E-eaef80dc. They say 'our network of 20+ distribution hubs and fulfillment centers', 'our nationwide freight services', 'our network that perfectly positions products' and 'our Loop Returns integration'. The cell's note and reading say no held statement names Shopify's company as the network's provider, which is a gap. These are that statement (E16). Kept.
- **CM-RET-003 gains `own-service`** (SH-E-eaef80dc): 'Now you can offer instant exchanges and credits through our' Loop Returns 'integration.' This is the integration of Shopify's logistics service, read with its collection, Loop Returns its filler. Kept, but it is open (case 1 below): if the integration is read as the admin's own (M-4), the line is `core`, which changes nothing.
- **CM-SHP-018 gains `own-service`.** The lines are SH-E-ea1863d0 ('pre-approved access to' Shop Promise; delivery dates 'powered by our intelligent software and physical network') and the Product list's 'Shop Promise badge' (SH-E-8af1400e). SH-50 placed the same, and the coordinator kept it; SH-50 isn't merged yet, so the checker shows it again. Kept.
- **CM-CUS-010 gains `own-service`** (SH-E-ce08eead, 'Sign in with Shop'). This is SH-50's item line (SH-E-46f1bc0c), which the coordinator kept. Kept.
- **CM-ANL-006 gains `extension-point`.** The lines are SH-E-cd6a5f8e ('Developers can now build apps or custom solutions for businesses with access to the ShopifyQL Stable API') and the ShopifyQL API of SH-E-2bc8685c (E13). SH-50 placed the same, and the coordinator kept it. Kept.
- **CM-MKT-023 becomes held and gains `core`.** The lines are SH-E-b229dc80 ('Product Recommendations API') and SH-E-8e1c6c36 (the Product list's 'Storefront search and recommendations upgrades'). SH-50 placed the item the same way (SH-E-760fb2b3), and the coordinator kept it. Kept.
- **CM-DVT-004 gains `core`** (SH-E-b69a930f, 'Robust test data for development stores'): 'Now you can populate your store with test data in a single click, so you can start developing your app or theme faster.', with 'Try it in your Partner Dashboard' to partners.shopify.com/current/stores/new?store_type=test_store. The cell is `not-stated`: no place, plan line or definition of a development store is held. This card is the platform's own development stores for building apps and themes, created in its Partner Dashboard (also CM-DVT-003's line). Kept.
- **Withdrawn while working: CM-INV-001's `extension-point`** (SH-E-7d771ac7, the Inventory States API). 'across external platforms' names no app or partner doing the work, and the documentation's address isn't a statement (E7). So it is `core` only (case 9).

## Entries I couldn't tell, placed where they most plainly belong

1. **'Our Loop Returns integration' (SH-E-eaef80dc), CM-RET-003 `own-service`.** I read it as the integration of Shopify's logistics service (its collection 'Fully outsource your logistics'; its link /fulfillment/features). If it is the admin's own integration, M-4 makes it `core`. If it is Loop Returns working through Shopify's interface, it is `extension-point`. Neither of those changes the cell. What would settle it: a held statement of where the integration is set up.
2. **'Consolidated admin domains' (SH-E-b5241eb4), CM-ACC-003 `core`.** The card says 'Access your store(s) through a single point of entry via admin.shopify.com'. I read that as the owner moving between its stores. It could instead be CM-TRU-001 (sign-in to the admin). What would settle it: a held statement on admin.shopify.com's sign-in across stores.
3. **'New index page design' (SH-E-e8868678), CM-ORD-001 `core`, by its link to admin.shopify.com/orders.** The design covers 'all index pages' of the admin, which no one capability holds (the ruling after SA-21: no capability is the admin itself). E11 keeps every feature card placed. If the coordinator reads an admin-wide design as naming no capability, it is `out`.
4. **Shopify Shipping in Italy and Spain (SH-E-3b723f87), CM-SHP-002 `core`.** The card names no admin place. I read Shopify Shipping as the store's own label service, as CM-SHP-002's cell holds it ('directly in your Shopify admin', SH-S-0717), as E12.4 reads Shopify Payments. The checker's brand note asks this of lines 32 and 33.
5. **The Flow OpenAI connector (SH-E-15dc99c5), CM-AUT-001 `shows;extension-point`, filler OpenAI.** I placed it there because the card's own thing is a Flow action for a third party's service. Its other reading is CM-AIA-003, AI content generation: OpenAI's GPT writes the text. But CM-AIA-003's name keeps it to 'text the platform's AI writes', so a third party's AI doesn't fit it. If the coordinator widens CM-AIA-003, the line moves there as `extension-point`, which changes that cell.
6. **'Accounting integrations like Freshbooks, Bench, Sage' (SH-E-b99a8166), CM-PAY-028 `extension-point`.** I read them as the integrations of the Balance account, whose own line is `shows` (named by its brand alone). M-4 would make 'integrations' in the platform's own words `core`, which changes CM-PAY-028 (now `extension-point` only).
7. **The release states in the API groups' addresses** (E13): five lines keep their title's support.
8. **The Shop Minis SDK (SH-E-312c000a), CM-CHN-002 `shows`, read with SH-E-3d312545's early release.** By its title alone (an SDK, a provider interface) it would be `extension-point`, which changes CM-CHN-002 (now `own-service`).
9. **The Inventory States API (SH-E-7d771ac7), CM-INV-001 `core` only.** See the withdrawn change above.
10. **The scope 'Commerce Components by Shopify' on the composable stack's cards** (E14), a reading.
11. **'Configurable logistics' (SH-E-0a337a15), `shows`.** If a held statement places Deliverr in Shopify's group, the card is `own-service` like its siblings.
12. **'Data-sharing with ad platforms' (SH-E-12fe7376).** I put the main line on CM-MKT-009, `core`, the data shared as pixels share customer events (its utm_feature `server-pixels`), with a CM-MKT-010 `extension-point` line for the ad platforms. If the coordinator reads the sharing as advertising itself, the main line is CM-MKT-010's.

## Structures whose items and sources disagree, or leave things out

- **Fulfill & deliver's collections.** The page's nav (`items.jsonl` line 4, `nav.navPillSolutions[5].collectionTitles`) lists four collections: 'Fully outsource your logistics', 'Effectively manage orders and inventory', 'Prep and ship every order with Shopify Shipping' and 'Building for the future of returns'. The content (`solutions[5].collections`) and the Product list hold three.
  - The content's collection 1 holds both the inventory items and the returns items (SH-E-eef98b65, SH-E-95676275).
  - The Product list titles that collection 'Manage orders, inventory, and returns' (`productList.solutions[5].collections[1].heading`).
  - The rendered page shows no heading between those items: it renders collection titles only as the nav's pills (`structures/shopify/editions/www.shopify.com_editions_winter2023/items.jsonl`, lines 60 to 62 and 97 to 99, against lines 457 to 477).

  I gave items 10 to 15 the nav's title for index 1, 'Effectively manage orders and inventory', as E1 reads `collectionTitles[M]`. The pill 'Building for the future of returns' has no collection of its own.
- **The Product list's headings and its collection titles differ from the items' and the nav's.** Examples are 'Checkout editor', and 'The world’s best checkout keeps getting better' against 'gets even better' (SH-50 noted the second). See E18.
- **The rendered page shows the API groups' items only as the page data holds them.** I read them from the page data, which governs.

## What the sources state that no entry holds (for the second stage)

- **The solution headers of my solutions.** These are `solutions[5]`, `[6]`, `[7]` and `[8]`'s `solutionHeader.headingHtml` and `subhead`, in `items.jsonl` line 4. Fulfill & deliver's begins 'No matter what fulfillment looks like for your business'; Choose your components' says the platform 'is built on a collection of underlying components'. They are general statements, which SH-50 listed for the others.
- **The `productNodeMap`, the 'Product map' of Commerce Components** (`items.jsonl` line 4, `content.productNodeMap`). No entry holds it (SH-50's notes). It is the lead for the new thing Commerce Components by Shopify: it names the components and the features they power.
- **Leads no line takes,** each named in passing or in a list of uses:
  - CM-INV-006 (inventory transfers): 'inventory inbounding' into the network's fulfillment centers (SH-E-0f3603dd), which is the network's freight, not the admin's transfers;
  - CM-LOY-004: 'reward your loyal token holders' (SH-E-8916043c), the token-gated perks' purpose;
  - CM-TAX-008: 'to avoid duties and customs fees' (SH-E-ef79b72c);
  - CM-STF-002: 'Only staff with the required permissions… will receive relevant alerts' (SH-E-7184be60), a gate on the user, named in `reading`;
  - CM-MKT-002 and CM-LOY-002: 'applying discount codes and gift cards' with the checkout UI extensions' APIs (SH-E-12f729f6);
  - CM-CHK-009 (custom fields at checkout, which holds nothing on Shopify): 'custom fields' that apps add to the checkout (SH-E-b7ca31af), as SH-50 left it;
  - CM-LOY-008 (referrals, which holds nothing) and CM-SUP-001: 'referral codes, product reviews, and more' on the order status page (SH-E-e873c451);
  - CM-OPS-001: 'the most widely scaled commerce infrastructure' (SH-E-46e75736), a claim;
  - CM-PTN-010, the checker's first lead for SH-E-0f3603dd ('powered by'): 'powered by Flexport' is another sense of the words.

## Problems with the brief or the script

- **`held_entries.py earlier` matched only 2 of the 23 Product list entries.** It matches the heading's text, and the Product list's headings differ from the items'. A key by locator, `productList/solutions/N/collections/M/products/K` against the items of `solutions/N/collections/M` in order, would print each item's line for SH-52 and SH-53 (E18).
- **The checker's quote parser takes a plural possessive (apps', parties') for a closing quote.** It reported a quote found nowhere, made of the words between. I rewrote those possessives ('blocks of apps').
- **A term that crosses a link's markup isn't found,** so 'Loop Returns integration' failed: the text is `Loop Returns</a> integration`. A quote across the markup was found. I kept terms within one text node.
- **The checker's brand note** asks each `core` line whose terms carry the brand. Each such line's reading names the words that place it: the admin's address or words, 'our', or the platform's own developer tools (E3).

## Where B-extent and the brief differ

None I relied on.

## The coordinator's check (31 October 2026, after the batch)

- **The cell changes stand, each read again:**
  - CM-SHP-012 takes `own-service` from 'our network of 20+ distribution hubs', a maker statement;
  - CM-RET-003 takes `own-service`, from the Loop Returns integration read with 'Fully outsource your logistics';
  - CM-SHP-018 and CM-CUS-010 take `own-service`, for Shop's things;
  - CM-ANL-006 gains `extension-point`;
  - CM-MKT-023 is `core`;
  - CM-DVT-004 is `core`, from the platform's own test-data development stores.
  The withdrawn Inventory States line stays withdrawn.
- **E13 to E18 stand** for SH-52 to SH-67.
- **E18 maps the Product list by its collection and order.** SH-52 holds only Product list entries, so the coordinator places them by E18, by script, with each entry taking its item's own line. SH-53's single one is left to its agent.
- **New things:** Commerce Components by Shopify, and two of SH-50's again, Sanity integration and Try before you buy.
- **Cost:** 14.8 million tokens over 65 requests, about 161,000 an entry.
