# SH-54: Summer '23 from Full-stack marketing, and Winter '24's first 22 features (high)

**What the batch is.** 82 entries of `editions-page-data` (observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`):
- entries 1 to 60: the Summer '23 Edition (line 5, `routes/($lang).editions.summer2023._index`), its collections `displayCollections/5` to `/9`:
  - Full-stack marketing (19 cards, entries 1 to 19);
  - B2B selling (11, entries 20 to 30);
  - Manage your money (8 of its 9, entries 31 to 38; its `shopify-credit` is SH-53's entry 4);
  - Orders & fulfillment (12, entries 39 to 50);
  - Everyday operations (10 of its 11, entries 51 to 60; its `admin-quality-improvements` is SH-53's entry 13);
- entries 61 to 82: the Winter '24 Edition (line 6, `routes/($lang).editions.winter2024`), the first ten of its section Conversion's twelve `sectionGroups`, from 'Product merchandising updates' to 'Shop Pay Commerce Component'. SH-55 begins with the next group, `conversion-s-payments-updates`.

**Count.** 156 lines: 151 on a capability, 5 `new`.
- Every entry is placed; none is `out`.
- 77 entries are only on capabilities, 1 only `new` (SH-E-62f84891, Quick order lists), 4 on both (SH-E-ef05c168, SH-E-1a4f382c, SH-E-708cd142, SH-E-2679b6b1).
- Supports over the lines (a line with two counts in each): `core` 99, `shows` 30, `own-service` 16, `extension-point` 12, `outside` 1.

**E1 to E25 are kept,** with the rulings in `review-H-rulings.md`'s last section, the free themes' ruling after SH-53 among them. Two rulings were added while I worked (after SH-37), and I revised my first chunk to them:
- **An app whose maker the platform's own words name, in any held post, takes `own-service` on every line about it.** Shopify Email's two lines (entries 1 and 10) and Collabs' four (entries 15 and 16) moved to `own-service`. I applied it to every app of my batch whose maker a held card names. The list is in E29 below.
- **The admin's own frame is no capability's thing, and the admin's search stays a new thing.** Entry 51's search takes `new:Admin search`, the name earlier batches used. Entry 56's bottom bar and menu take no line.

`held_entries.py earlier` printed an earlier line for 2 of the 82 entries: SH-69's plan row 'Shopify Combined Listings' and SH-50's and SH-51's Winter '23 'One-page checkout'. No batch had placed these collections. Where an entry is of a kind E1 to E25 don't cover, the rule I followed is below, for the coordinator to align with SH-55 to SH-67.

## Rules I followed where E1 to E25 don't reach

### E26. A collection's overview card that names its tools

Full-stack marketing opens with 'Keep customers coming back with email, chat, forms, segmentation, and automation tools' (SH-E-7bb3b9b0). Its description names 'the latest updates to automations, segmentation, Shopify Email, Shopify Forms, and Shopify Inbox'.
- These are the card's own things: the updates it announces, each with a card of its own after it.
- They aren't a list of what may be used (the ruling after SA-41), so each tool takes a line.
- Its words 'Start and scale your marketing on Shopify' place them in the platform (E3). Hence `core` on CM-MKT-005 (marketing tools; Shopify Forms, the lead capture SH-36 placed there), CM-MKT-006, CM-CUS-002 and CM-SUP-004, and `own-service` on CM-MKT-007 (Shopify Email, the ruling after SH-37).

### E27. A kind of business the card's own words name is its scope

E6 makes no scope of the tag 'Enterprise'. Three cards name the business the feature is for in their own text. I took those words as the scope (the brief: a kind of store is a listing condition):
- 'For businesses using a custom checkout' (SH-E-ef05c168, payments apps);
- 'Enterprise businesses can offer customers a secure way to save payment methods.' (SH-E-aed55470);
- 'Shop Pay Commerce Component' (SH-E-2679b6b1), the title naming the offer, as E23 took a `productType`.

A plan named in the text is the scope in its words: 'Basic plan' (SH-E-f8d1f2a1), 'Shopify Advanced plan' (SH-E-19b56fd5). A country is too: 'US' for the 'enhanced US sales tax report' (SH-E-a77b9c6a); 'United States' for 'Currently available to businesses in the United States.', which names a country and not a limited release, unlike E5's 'select businesses'.

### E28. A plan statement for an app at its address

'Shopify Flow available to more plans', 'Now businesses on the Basic plan can easily automate workflows with Shopify Flow.' (SH-E-f8d1f2a1) links the app at admin.shopify.com/apps/flow.
- The ruling after SH-36 makes an app's page with no maker `shows`.
- E3 makes a plan statement `core`.
- I read the card's own words as the plan statement, so CM-AUT-001 is `core`, scope Basic plan, with CM-APP-007 `core` for the app's page.
- Bill Pay (SH-E-625bb5f9) says 'with Bill Pay in the admin' and links admin.shopify.com/apps/bill-pay. That is no plan statement, so it stays `shows` by the ruling. The cell's own routes finance:billpay hold its `core`.

### E29. Apps whose maker a held card names (the ruling after SH-37)

- **The app's lines take `own-service`, though the card itself names no maker:**
  - Shopify Email: the ruling's own case;
  - Shopify Audiences: 'a new app from Shopify' (SH-50's SH-E-234dcbd7); its own card adds 'custom audience lists powered by our unique commerce insights';
  - Shopify Collabs: 'our creator platform' (SH-50's SH-E-709b37e4), with the cell's publisher, Shopify Inc. (SH-S-2760);
  - Planet: 'Planet—An App From Shopify' (SH-50's SH-E-bc581483);
  - Search & Discovery: 'We’ve also made it easier…' (SH-53's SH-E-9b869699);
  - Shopify Bundles: 'our new, free bundles app' (SH-53's SH-E-1d272a37), and its own card's 'We've increased the maximum number of products'.
- **By its own card's words:**
  - Shopify Subscriptions: 'our new, free subscriptions app' (SH-E-4c0f3472), with CM-APP-011 `own-service` as E22 gave Bundles. SH-53 placed Summer '23's Shopify Subscriptions `core`, named with no maker; under the ruling, the coordinator aligns it.
  - The Combined Listings app (SH-E-dc618719): the group's lead card says 'We’ve improved how all products … are listed and discovered on Shopify with the largest update to our product model', 'From a new app for merchandising products that come in multiple colors and styles'. I read the 'we' as shipping the app (the ruling after SH-35). This changes CM-CAT-008 (case 2).
- **No line takes CM-APP-011 for an app named only by its brand in my cards.** SH-50's rule gives it only where the card calls the app Shopify's. The ruling after SH-37 speaks of the app's own lines.
- **Kept without a maker, none being named in a held post I know of:**
  - Shopify Inbox: CM-SUP-004's cell has its Google Play publisher, which is not a post (case 7);
  - Shopify Forms, Shopify Flow, Shopify Fraud Control, Bill Pay, the Privacy & Compliance app, and ShopifyQL Notebooks. SH-51's `core` on Notebooks rested on 'our intelligent query language', which entry 58 doesn't say.
- **A feature that isn't yet offered stays `shows` by E5, whatever its maker.** The Combined Listings card (SH-E-706f11a3, 'Sign up for early access') and Shopify Collective ('Currently available to select businesses in the United States.') are the cases. The maker statement is named in `reading`. B2B selling's collection calls Collective 'our new curated network for sourcing and selling products' (`displayCollections[6].description`).

### E30. Winter '24's section groups

Winter '24's `within` has a second part, the `sectionGroups` title, such as 'Conversion - L - Products 2.0'. That is the page data's layout group: L, M and S match its `productSize`, and every group's `description` is empty.
- The rendered page shows the section 'Conversion' (h2), the card's `productType` as a label ('Product merchandising') and its `headlineTitle` (h3) (`structures/shopify/editions/www.shopify.com_editions_winter2024/items.jsonl`, lines 1 to 5).
- So I read each card with 'Conversion', its `productType` and its `headlineTitle`, and give the group title no line or scope.

### E31. A group's lead card that names the next cards' things

'Product merchandising updates' (SH-E-dc618719) names the product model, 'a new app' and 'a new product taxonomy'. The next cards are 'Shopify Combined Listings' and 'New taxonomy'.
- Each thing the lead card names takes a line by the lead card's own words: `core` on CM-CAT-001 and CM-CAT-004, `own-service` on CM-CAT-008 (E29).
- The next cards' early access ('Sign up for early access') isn't read back into it. E5 reads a collection's cards with their lead card's limit, not a lead card with its followers'.
- Each next card keeps its own `shows`, as E10 keeps each entry to its own words.

### E32. Case studies and carriers

E19 is applied to the four further case studies: Laurie Ellen, Drake Related, Element Brooklyn and Snarky Tea. Monos, a fifth in Winter '24, takes E19 too.
- Each is `shows` on its feature's capability. Its numbers are claims (E9), and the merchant isn't a filler.
- Snarky Tea's 'discounted USPS labels from Shopify Shipping' takes USPS as the label line's filler, and a CM-SHP-015 `shows` line, as E15 does for a card's carriers. So does DHL Express (SH-E-fcf1dfa9).

### E33. Other readings of this batch

- **The Google & YouTube app** isn't Shopify-branded, and no card names its maker. SH-50's YouTube placement holds (E3: an app with no maker named, doing the feature, `extension-point`, the venue its filler): YouTube selling on CM-CHN-001 and CM-CHN-004, filler YouTube. Its Google Analytics 4 card (SH-E-6bff85f5) is CM-ANL-007's thing, commerce data sent to outside analytics platforms, and its first Shopify line (CHANGES). Its AI imagery is in early access: CM-CAT-007 `shows`, filler Google.
- **Admin-wide cards** ('Experience an easier-to-use admin', SH-E-708cd142) take no line of their own (the rulings after SA-21 and SH-37). Each feature they name takes its own:
  - the bulk editor on CM-CAT-001, as SH-50 placed it;
  - the search on `new:Admin search`;
  - the store data, dashboards, insights and alerts feed on CM-ANL-003, its Home > Home.
- **The organization settings card** (SH-E-056126c7, Shopify Plus) takes a line for each highlight's own thing:
  - stores: CM-ACC-003;
  - user roles and access: CM-STF-002;
  - new stores with imported merchandising data: CM-MIG-001;
  - the consolidated bill: CM-PLN-004;
  - its one payment method: CM-PLN-005;
  - performance across the organization: CM-ANL-001;
  - draft order permissions: CM-ORD-005, as the brief places a permission on what it gates.
- **Saved cards for a faster checkout** (SH-E-aed55470) are CM-PAY-014's, by its note and CM-PAY-022's: cards saved 'so that next time, checkout will be faster', not charged later without a checkout. Winter '23's and Summer '23's B2B vaulted cards (SH-E-b0429a57), used to pay draft orders and invoices, stay CM-PAY-022's, as SH-53 placed them.
- **The cards' counts and limits are qualities (E9):**
  - 'up to 100 shipping labels';
  - 'up to 5 additional accounts';
  - 'FDIC insured up to $250,000';
  - DHL Express rates 'reduced by 13.25%';
  - 'up to 2,000 variants per product';
  - bundles 'from 10 to 30';
  - '14 new APIs and UI components';
  - '90+ apps' of '400+';
  - 'a 2X increase in Admin API rate limits';
  - the subscriptions app's 'free';
  - support 'in French, Spanish, and German at any time of day'.

  The speed and saving claims aren't qualities: 'up to 4 days faster', 'by 4 seconds', 'up to 95%', 'up to 50%'.

## New things

Shopify's Editions are in English only: no Arabic name is held.

| New thing | Entries | Place of its own | Proposed domain, area, parent | Terms searched (`caps --terms`) | Leads read |
| --- | --- | --- | --- | --- | --- |
| Quick order lists (SH-53's) | SH-E-62f84891, B2B selling's own card, which SH-53 asked to be named the same: 'Show customers a list of product variants, so they can easily order sizes, colors, and more, all from one section of your product pages. Exclusive to Shopify Plus.' | As SH-53: none held (a theme section on one help page). So `shows` | As SH-53: D, B2B, under CM-B2B-001 | As SH-53 | CM-CAT-002 (variants, what the list shows), CM-B2B-001, CM-API-013 (by name): none |
| 3D Secure | SH-E-ef05c168: 'adding support for Apple Pay, Google Pay, and 3D Secure.' to the platform's processing of card payments for payments apps | None in this entry. So `shows` | C, PAY, under CM-PAY-001, near CM-PAY-011 (the payments apps it serves) or CM-ORD-006 (fraud) | 3D Secure; 3DS; authentication; SCA; card verification; chargeback | CM-CHK-003, CM-CHK-004, CM-ORD-006 (order risk analysis, not card authentication), CM-ONB-003, CM-MKT-018 (by name): none. BigCommerce's providers name 3DS within CM-PAY-011's lines |
| Planet (SH-50's) | SH-E-1a4f382c: 'With the latest enhancements to the Planet app, now you can share a more holistic view of your commitment to carbon-neutral shipping', its badge and impact page | As SH-50: none held but the app's admin page (CM-APP-007's line) | As SH-50: C, SHP, under CM-SHP-001 | As SH-50 | CM-TRU-010, CM-ORD-001, CM-SFR-015, CM-ORD-003, CM-B2B-005 (by name): none |
| Admin search (the ruling after SH-37) | SH-E-708cd142: 'You can now search for orders, apps, products, or settings across your store(s) and get accurate and relevant results.' | None in this entry. So `shows` | As the earlier batches' Admin search, decided with Zid's and Salla's | admin search; search | CM-SFR-013 (the buyer's storefront search: a homonym), CM-ANL-003, CM-CAT-006, CM-PLN-001, CM-ORD-003 (by name): none |
| Commerce Components by Shopify (SH-51's) | SH-E-2679b6b1: 'Shop Pay Commerce Component', one of the components (E23) | As SH-51: none held | As SH-51 | As SH-51 | CM-ACC-002, CM-CAT-005, CM-PAY-014 (its own line), CM-PAY-015, CM-PTN-010 (by name): none |

The Planet line is `own-service`, not the `shows` the brief gives a new thing with no place of its own. The ruling after SH-37 gives every line about an app whose maker a held post names `own-service`. SH-50's own new:Planet line is `shows`, so the coordinator aligns the two (case 1).

## The CHANGES lines, and what I decided on each

Each was read again against its entry. Line numbers are the placements file's.
- **CM-ANL-007 becomes held and gains `extension-point`** (line 26, SH-E-6bff85f5). 'Upgrade to Google Analytics 4 in the Google & YouTube app for enhanced, real-time, multi-channel data measurement', its help link `google-analytics-setup`: the store's data measured in an outside analytics platform, through an app with no maker named. CM-ANL-007's cell had found only exports. Kept.
- **CM-CAT-008 gains `own-service`** (line 119, SH-E-dc618719). 'We’ve improved how all products … are listed and discovered on Shopify with the largest update to our product model in over a decade. From a new app for merchandising products that come in multiple colors and styles…' (E29, E31). The cell's note says no statement had named the Combined Listings app's maker. Kept, open (case 2).
- **CM-CHN-006 gains `core`** (line 153, SH-E-b3ea5e29). 'Bring your customized checkout to your mobile app with Checkout Sheet Kit', 'Available for iOS/Swift, Android, and React Native.', its link shopify.dev's `custom-storefronts/mobile-apps#checkout`. This is the platform's own kit for the store's own mobile app: B-extent's convention makes the platform's own API for its own feature `core` where no statement says apps or partners do the work. The cell holds only the App Store's Mobile app builder apps. Kept, open (case 4).
- **CM-MKT-003 becomes held and gains `core`** (lines 143 and 146). Draft orders' 'support for discount codes, automatic discounts' (SH-E-a890e154, its link `draft_orders/new`), and 'new types of discounts, including free automatic shipping' (SH-E-8c1d6bd3, its link `admin/discounts`). These are discounts applied without a code, and the cell said no Shopify statement held names them. Kept.
- **CM-MKT-006 gains `extension-point`** (line 24, SH-E-b6214d50). 'You can also automate SMS, web push, and email marketing efforts with integrated apps like AfterShip, PushOwl, and Seguno, and new templates highlighting each one': third parties' apps in the platform's automations, the apps their fillers (E15). Kept.
- **CM-MKT-007 gains `own-service`** (lines 5 and 20). Shopify Email, by the ruling after SH-37. Kept.
- **CM-MKT-011 gains `own-service`** (line 10, SH-E-6589fc34). 'custom audience lists powered by our unique commerce insights', and SH-50's 'a new app from Shopify', which the coordinator kept and which isn't merged yet. Kept.
- **CM-SEL-001 gains `own-service`** (line 136, SH-E-4c0f3472). 'our new, free subscriptions app'. Kept.
- **CM-SEL-006 gains `own-service`** (line 138, SH-E-385c34a8). Bundles: 'We've increased the maximum number of products', and SH-53's 'our new, free bundles app', which the coordinator kept. Kept.
- **CM-SFR-013 gains `own-service`** (lines 130, 132 and 134). Search & Discovery's Semantic Search ('one of our new AI-powered storefront search features'), swatch filters and filter logic, by SH-53's maker statement and the ruling after SH-37. Kept.
- **CM-SFR-015 gains `core`** (line 125, SH-E-b049ecab). 'Make it easier for your buyers to find and buy your products by adding' 'color or pattern swatches' 'directly on your product listing.', its help link `theme-settings#options-with-swatches`. This is how the storefront shows a product's options, in the platform's own themes (the ruling after SH-53). Kept, open (case 3).

## Entries I couldn't tell, placed where they most plainly belong

1. **Planet (SH-E-1a4f382c), `new:Planet` `own-service`.** The brief's rule for a new thing with no place of its own gives `shows`. The ruling after SH-37 gives every line about the app `own-service`. What would settle it: the coordinator's choice between the two for a new thing, aligned with SH-50's line.
2. **The Combined Listings app's maker (SH-E-dc618719), CM-CAT-008 `own-service`.** It rests on reading 'From a new app…' as part of what 'We’ve' made. If the fragment only lists the update's contents without naming their maker, the line is `core` by what it shows, as the cell's plan row is.
3. **Color swatches (SH-E-b049ecab), CM-SFR-015 `core`.** No capability holds swatches. The help link is the theme's settings, which is how the storefront shows options (CM-SFR-015). If the coordinator reads swatches as the options' own values, the line is CM-CAT-002's, which changes nothing.
4. **Checkout Sheet Kit (SH-E-b3ea5e29), CM-CHN-006 `core`, with CM-CHK-001 `core`.** If a kit for developers' mobile apps reads as an interface third parties build on, the line is `extension-point`, which changes nothing.
5. **Bill Pay (SH-E-625bb5f9), `shows`.** The card says 'in the admin' but links an app's address. The router holds finance:billpay as the admin's own route, which suggests the app's address opens the platform's own page. If so, the line is `core`, with no CM-APP-007 line.
6. **Flow on the Basic plan (SH-E-f8d1f2a1), `core`** (E28).
7. **Shopify Inbox (SH-E-7bb3b9b0, SH-E-890aeb6f), `core`,** as SH-50's E12.3 and SH-53 placed it. The cell holds the Inbox app's Google Play publisher, Shopify Inc. (SH-S-2758). If the coordinator reads a store listing's publisher as a held maker statement under the ruling after SH-37, these lines become `own-service`, which changes nothing. That is SH-53's case 13 again.
8. **'For businesses using a custom checkout' (SH-E-ef05c168).** The card doesn't say whether this is a checkout built apart from Shopify's or the merchant's customized checkout. The scope keeps the card's words. If it means every customized checkout, the scope goes.
9. **'Enterprise businesses' (SH-E-aed55470).** I read the card's sentence as a condition (E27). If it is the tag's topic again, the scope goes.
10. **3D Secure (SH-E-ef05c168), `new`.** It is a card's list of what the payments apps' processing supports. If the coordinator reads that list as named in passing, the line goes. The wallets in the same list take CM-PAY-012 `core`, which changes nothing.
11. **The support languages (SH-E-5e5b7954) as a quality** of CM-ONB-003. The brief makes a list of languages market data, but these are the platform's support's own. If the coordinator disagrees, the quality goes, and the line stays.
12. **Shopify Balance's bank (SH-E-1079788e).** 'Funds are held at Evolve Bank and FDIC insured up to $250,000.' takes a second CM-PAY-023 line, `outside`, fillers Evolve Bank and FDIC. The cell already holds `outside`.

## Structures whose items and sources disagree, or leave things out

- **Winter '24's `within` carries the page data's layout groups** (E30), such as 'Conversion - M - Bundles/Draft Orders/Discounts'. The rendered page doesn't show them (`www.shopify.com_editions_winter2024/items.jsonl`, lines 2 to 4).
- **Summer '23's cards are the page data's only text,** as SH-53 found (the register: 2 of 143 descriptions in the rendered page). Quotes are taken within one text node of `descriptionHtml` (E25).
- **No other disagreement found.** The items match the page data at each locator.

## What the sources state that no entry holds (for the second stage)

- **The Summer '23 collections' descriptions** (`items.jsonl` line 5, `collections.displayCollections[5]` to `[9]`). I read them with their cards (rule 1). Their British, French and German variants (`descriptionGb`, `descriptionFr`, `descriptionDe`) say more:
  - B2B selling: 'With the latest updates to our built-in B2B features and our new curated network for sourcing and selling products' (the maker lead for Collective, E29). Its other variants say 'Our B2B selling solution now includes automations to streamline routine tasks … while new APIs help you and your customers manage orders, inventory and pricing'.
  - Orders & fulfillment: 'Built-in order management and delivery tools help you fulfill orders faster and for less'. Its German variant says 'delivery and carbon emission tracking'.
  - Full-stack marketing: 'We're connecting our marketing tools to help you scale your audience'. Its other variants add 'stay compliant across every region you work'.
  - Manage your money: 'everything from payment support to spending, borrowing, and banking tools'.
  - Everyday operations: 'We've reimagined the admin and enhanced performance across the platform'.
- **Summer '23's `bundleCollections`:** 'Modal bundle - Marketing Tools' (gid://shopify/Collection/430158053398), the `modalBundleCollection` of entry 1. Its handle names the bundles and subscriptions apps, and it has no products.
- **Winter '24's hero:** 'FOUNDATIONS', 'Elevate your commerce business with 100+ foundational product updates from Shopify' (the rendered page, lines 0 and 1). Its `heroContent` names the Combined Listings feature, 'IMPROVED MERCHANDISING FOR PRODUCTS', with its media.
- **Leads no line takes,** each a homonym, named in passing, or in a list:
  - CM-PTN-009, the checker's lead for the Collabs cards: a partner's affiliates in the partner dashboard, ruled apart from Collabs (its note, U-056);
  - CM-CAT-005 (brands, holds nothing): Collective's 'Shopify brands' are merchants (SH-53);
  - CM-SFR-016 (share buttons, holds nothing): YouTube's 'share promos';
  - CM-CHK-009 (custom fields at checkout, holds nothing): Shopify Forms' 'custom fields' are a form's; the PO number captured 'at checkout' is B2B's own field (CM-B2B-001's WooCommerce cell holds the purchase order number), not one the merchant adds;
  - CM-SFR-011: Collabs' tracking 'for stores using Hydrogen', where it works;
  - CM-CUS-001: the pixel events' 'richer customer profiles', a purpose;
  - CM-MKT-021 (upsell): Monos' 'better upsell capability' and the checkout apps' 'upsells', in a list;
  - CM-LOY-004 (loyalty): 'loyalty programs' among the checkout apps' features;
  - CM-LOY-002 (gift cards): the payments apps' 'built-in experiences to your custom checkout like gift cards', an example;
  - CM-AIA-001 and CM-AIA-003: Google's AI imagery and Semantic Search's AI, neither the platform's AI in the admin nor text it writes;
  - CM-CAT-006 (tags): the bulk editor's 'manage tags';
  - CM-INV-001 and CM-INV-005: the variants card's 'availability information for both single and multiple inventory locations', fields it edits;
  - CM-PAY-008 (payment terms): the draft order permissions' 'set payment terms' and Flow's 'assign terms', in lists;
  - CM-CUS-010: subscription orders modified 'directly from their account', PO numbers 'within customer accounts', payment details edited 'within their account', each named as where;
  - CM-CHN-001: 'the Shopify Plus Wholesale Channel', the migration's condition;
  - CM-STF-001: the organization's 'Add, suspend, remove' users, read with 'manage user roles and access' on CM-STF-002.
  - CM-LOY-007 (reorder reminders, holds nothing), the checker's first lead for the swatches card (SH-E-b049ecab): a lead by name words ('buy', 'buyer', 'product'); the card names no reminder.

## Problems with the brief or the script

- **The rulings file changed while I worked** (after SH-37). I re-read its new rulings and revised the eight lines of my first chunk they touch.
- **The brief's rule for a new thing and the ruling after SH-37 differ** for an app with no place of its own whose maker a held post names (Planet, case 1).
- **`held_entries.py earlier` matched 2 of 82 entries.** No batch had placed these collections.
- **`show`'s leads were mostly names' words,** as SH-50 and SH-53 found. The useful ones were by identifier: shopify audiences, shopify collabs, shopify inbox, bill pay, shopify combined listings, fulfillment constraints. The two empty cells this batch fills (CM-ANL-007, CM-MKT-003) came from reading each lead whose cell holds nothing, against the entry's own words.
- **The checker's brand note fired on 11 `core` lines:** Shopify Marketing Tools and Forms, Inbox, Flow, Balance, Tax, Shipping and the App Store. Each line's reading names the words that place it:
  - an admin address or admin words (E3, E7);
  - a plan statement (E28);
  - the platform's own service (Shopify Shipping, Shopify Tax, the App Store);
  - or the ruling after SH-36 for a branded app named with no address.

## Where B-extent and the brief differ

None I relied on.

## The coordinator's check (31 October 2026, after the batch)

- **The cell changes stand, each read again:**
  - CM-ANL-007 is held, `extension-point`, from Google Analytics 4 through the Google & YouTube app;
  - CM-MKT-003 is `core`, from draft orders' automatic discounts and free automatic shipping;
  - CM-CAT-008 is `own-service`, from Combined Listings: 'We’ve improved… a new app for merchandising products';
  - CM-CHN-006 is `core`, from Checkout Sheet Kit, the platform's own kit for the store's own app;
  - CM-MKT-006 gains `extension-point`, with its apps as fillers;
  - CM-MKT-007, CM-MKT-011, CM-SEL-001, CM-SEL-006 and CM-SFR-013 gain `own-service` from their makers' statements;
  - CM-SFR-015 is `core`, from colour swatches.
- **Aligned by the ruling after SH-37:**
  - SH-36's and SH-53's lines on the Shopify Subscriptions app are `own-service;extension-point`. 'Our new, free subscriptions app' names its maker.
  - SH-50's Planet line is `own-service`, as this batch's is. A new thing's support is what the platform does with it, and the brief's `shows` is for one named only. Planet still has no place of its own.
- **Shopify Inbox stays `core`.** A Google Play listing's publisher isn't the platform's own words in a post.
- **E26 to E33 stand for SH-55 to SH-67.**
- **New things:** Quick order lists, 3D Secure, Planet, Admin search, Commerce Components by Shopify.
- **Cost:** 24.5 million tokens over 96 requests, about 299,000 an entry. The context reached about 460,000 tokens.
