# SH-55: Winter '24, from Conversion's payments updates to Operations' lending and Balance (high)

**What the batch is.** 81 entries of `editions-page-data` (observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`, line 6, `routes/($lang).editions.winter2024`), in the page's order:
- Conversion, its last two `sectionGroups`: 'Conversion - S - Payments updates' (6 cards, entries 1 to 6) and 'Conversion - L - Storefront Performance' (1, entry 7). SH-54 held the first ten groups.
- Channels, all thirteen groups: POS Terminal, POS Hardware, POS Extensibility, POS fulfillment and POS Software updates (entries 8 to 23); B2B Sales Reps and B2B (24 to 30); Collective/Faire (31 to 33); Marketplace Connect (34 to 36); Markets Pro, International and Markets (37 to 43).
- Marketing, all nine groups: Audiences (44 to 46), Collabs (47 to 53, with 'Tik Tok for all US businesses'), Shop Campaigns (54 to 57), Shop (58 to 60), Marketing Tools (61 to 63), Reviews Platform (64 to 67), Reporting (68 to 70) and Other (71, 72).
- Operations, its first five groups: AI Image Gen and Magic (73 to 76), Privacy Settings (77), Financial Services Lending and Lending/Balance (78 to 81). SH-56 begins with 'Operations - S - Financial Services'.

I read each entry against the page data's own product (line 6, by its pointer), with its `authenticatedCta*`, `signupCta` and `signupModalTitle`; the media fields are no statement (E1). Every group's `description` is empty, so each card is read with its section, its `productType` and its `headlineTitle` (SH-54's E30).

**Count.** 152 lines: 147 on a capability, 5 `new`.
- Every entry is placed; none is `out`.
- 76 entries are only on capabilities, none only `new`, 5 on both (SH-E-31dd37c9 Planet, SH-E-1f3526dd, SH-E-126592cc, SH-E-6eb269c7, SH-E-a5bde01e).
- Supports over the lines (a line with two counts in each): `core` 67, `shows` 38, `own-service` 34, `extension-point` 20.

**E1 to E33 are kept,** with the rulings in `review-H-rulings.md`'s last section. Two rulings were added while I worked (after SH-38):
- **` and ` in a scope joins two lists, and a source's words holding 'and' are quoted.** None of my scopes holds 'and'. 'Retailers in the UK and Ireland' is written `UK;Ireland`, two alternatives.
- **A post is about the app whose page its own link opens.** No card of mine changes by it: each card that links an app's page names that app in its words too.

`held_entries.py earlier` printed an earlier line for 1 of the 81 entries: the label 'Shopify Audiences' (SH-38, SH-50, SH-54). No batch had placed Winter '24 past Conversion's tenth group.

## Rules I followed where E1 to E33 don't reach

### E34. A maker named in a held changelog post counts for an Editions app

The ruling after SH-37 gives every line about an app `own-service` where 'the platform's own words name, in any held post' its maker. The rulings after SH-35 and SH-53 make 'we' upgrading an app such a statement, in the changelog and the Editions alike. I searched the held entries (`entries.tsv`) for Marketplace Connect, Translate & Adapt, Stocky, Shopify Inbox, Shopify Forms and Shopify Flow, each with 'we', 'our', 'first-party', 'from Shopify' or 'by Shopify' near its name. Two apps of my batch have such a post:
- **Stocky** (entry 19): 'We’ve introduced the option to 'Edit' purchase orders in Stocky' (SH-E-5b89aa16, `structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl`, line 705).
- **Shopify Inbox** (entry 61): 'We’ve rolled out a powerful spam detection system that prevents unwanted messages from arriving in your Inbox' (SH-E-4f0c8272, line 899) and 'We've enhanced conversation metrics for Shopify Inbox' (SH-E-ad0c07b1, line 1166).

Neither post has been placed yet, by `grep` of the placements. The coordinator's check after SH-54 kept Inbox `core` because 'A Google Play listing's publisher isn't the platform's own words in a post'. These are the platform's own words in posts, so I made Inbox's line `own-service` (case 1).

I found no such post for Marketplace Connect, Translate & Adapt or Shopify Forms. Their lines follow the ruling after SH-36: an app's page with no maker is `shows`, with a CM-APP-007 line; a card that names the app with no admin address is `core`, the maker a gap.

### E35. The ruling after SH-37, read for devices and services

The ruling names an app. I applied it in the same way to a separate device or service whose maker a held card of the Editions names:
- **POS Go:** SH-53's 'Canadian businesses can now purchase POS Go, our all-in-one POS device' (SH-E-fc9fba8c). So POS Go is `own-service` on CM-POS-002 in entries 12 and 13. Entry 14's POS Go is in early access, so it is `shows` (SH-54's E29).
- **Markets Pro:** SH-53's 'Our Merchant of Record capability' (SH-E-9e3f5c76). So CM-MKS-003 is `core;own-service` in entries 37 and 38. The `core` rests on the admin link `settings/markets/pro/apply`.
- **Shopify Collective:** Summer '23's B2B selling, where its Collective card stands, says 'our new curated network for sourcing and selling products' (`items.jsonl` line 5, `collections.displayCollections[6].description`; SH-54 named it as a maker lead in E29). Winter '24's two Collective cards are released, so they are `own-service` on CM-CHN-005. The supplier-sourcing side is `shows` on CM-CAT-010, as its note keeps Collective's statements (case 2).
- **Shopify Lending:** entry 78 says 'Our new lending portfolio features three products'. Its Line of Credit and Term Loans cards (79, 80) take `own-service` from it, with `core` for their admin links (`capital/offers`, `capital/offers/line`, 'right in your admin').

A device with no maker statement stays `shows`, as E3's 'Shopify POS hardware' was. That covers POS Terminal (entries 8 to 11), whose 'Shop now' links open shopify.com's hardware store, a channel and not a maker statement. CM-POS-002's own-service rests on its terms (SH-S-7269, SH-S-7251), which a later reading might extend to POS Terminal. Neither choice changes the cell.

### E36. A group's lead card with no description

Four groups open with a card that has only a title, a `productType` and a `headlineTitle`. They are POS Terminal (entry 8), Shopify Audiences (44), Shop Campaigns (54) and Integrated reviews (64). Each is placed by those words, on the capability of the product they name, as SH-54's E31 places a lead card:
- 'Stronger retargeting and benchmarks for your ads' gives Audiences two lines, one for the retargeting and one for the benchmarks.
- The maker is the product's, by E34 and E35, where the product is the same. Integrated reviews is Shop's product reviews: its cards say 'Shop-generated' reviews and 'Replies to reviews in Shop', and each links the Shop channel's reviews onboarding (`settings/channels/install_shop_channel?onboardingRedirect=reviews`). So it is `own-service`, by the ruling after SH-34.

### E37. A non-Shopify-branded app at the admin's `apps/` address

TikTok (entry 53, `apps/tiktok-ads-2`) and Faire: Sell Wholesale (entry 33, `apps/faire-sell-wholesale`) are named for a third party's platform, with no maker stated. I followed SH-54's E33 for the Google & YouTube app:
- `extension-point` on what the app does, with the venue as its filler (M-3);
- CM-APP-007 `core` for the app's page (M-10).

'We've partnered with Faire, the leading online wholesale marketplace' names Faire as the partner and the venue, not the app's maker.

### E38. Payment providers and stored cards

'Payment providers now have access to securely stored credit card information, so subscription and pre-order apps work with more payment options' (entry 3) takes these lines:
- CM-PAY-022 `extension-point`: third parties charging the cards the store keeps, through the access the platform gives them;
- CM-PAY-011 `extension-point`: the providers themselves;
- CM-SEL-001 and CM-SEL-005 `extension-point`: their headline names the subscriptions and pre-orders.

The card 'Vaulted credit cards for stores' (entry 1) is CM-PAY-014's, as SH-54's E33 placed saved cards for a faster checkout. Card Account Updater (entry 2) keeps the vaulted cards current, CM-PAY-022 `core`, 'included with Shopify Payments' (CM-PAY-002 `core`).

### E39. Eligibility and kinds of business as scope

- 'Exclusive to eligible Shopify merchants' (entry 78) is a listing condition, its scope: eligibility, not E5's limited release to 'select businesses'.
- 'Retailers with multiple locations and hardware devices can more easily install and activate' (entry 15) says who gains most, not a condition, so it takes no scope.
- A paid offer's own words for the offer are its lines' scope where its `productType` names it: 'Shopify Markets Pro' for the DHL eCommerce card (entry 38), by the ruling after SH-70 and SH-53's SH-E-9e3f5c76.

### E40. Qualities of this batch (E9)

- 'Shopify's 99.9% platform uptime', on CM-OPS-001, the platform's own availability (entry 9);
- the PIN lengths '4, 5, or 6 digit PINs' (entry 23);
- the window 'within 15 minutes of completing a transaction' and 'without incurring transaction fees' (entry 22);
- 'cost-free' (Card Account Updater);
- 'no order minimums' (DHL eCommerce);
- 'a fixed cost per acquisition' (Shop Campaigns);
- 'only pay interest on what you use' (Line of Credit);
- 'No credit checks and no surprise fees' (Term Loans);
- the Balance account's 'free', 'No minimum balance' and no limit to what it earns.

These are claims, not qualities: '35% faster', 'at least double', '258% growth', '$40K in fraud', 'over 1M new customers', 'up to 24%', '100M+ customers'.

### E41. A thing a capability's note sends elsewhere

DHL eCommerce's 'delivered duty paid (DDP) shipping labels' (entry 38) are duties paid before delivery. CM-TAX-008's note leaves 'A merchant of record that handles duties for the store' to CM-MKS-003, so the DDP line is on CM-MKS-003 with Markets Pro's support, not on CM-TAX-008.

## New things

Shopify's Editions are in English only: no Arabic name is held.

| New thing | Entries | Place of its own | Proposed domain, area, parent | Terms searched (`caps --terms`) | Leads read |
| --- | --- | --- | --- | --- | --- |
| Planet (SH-50's) | SH-E-31dd37c9: 'Use Planet to surface a carbon-neutral shipping option', the Planet 'app from Shopify' (its CM-APP-011 `own-service` line beside it) | As SH-50: none held | As SH-50: C, SHP, under CM-SHP-001 | As SH-50 | The checker's CM-DVT-004 and CM-APP-012 (by name: app, build, install): neither |
| Web performance dashboard | SH-E-1f3526dd: 'Track and optimize your storefront performance with trusted insights across three Core Web Vitals, with our new web performance dashboard.' `core`: the platform's own report, in the present tense | None in this entry, and the held admin router holds no route for it (`grep -i 'web.performance'` of `structures/shopify/admin-router/items.jsonl` finds none). `grep` finds the words in the Help Center's held section lists (`help-section-children`), which are no place by B-extent's list | E, SFR, beside CM-OPS-003 (the platform's hosting, which the same card names), or D, ANL, under CM-ANL-001 | web performance; Core Web Vitals; storefront performance; online store speed; page speed; speed; performance dashboard; lighthouse; vitals; site speed; load time | CM-ANL-003 (overview dashboards of the store's sales: 'store performance' is a homonym); CM-B2B-007, CM-PLN-001, CM-DVT-006, CM-MKT-017 (by name): none. SH-34's 'payments and web performance data in Sidekick' (SH-E-3eca5e44) names the same data |
| Staff sales attribution (SH-50's) | SH-E-126592cc: Send Cart's sale 'will be attributed to the retail location and staff member' | As SH-50: none held | As SH-50: A, STF, under CM-STF-001 | As SH-50 and SH-53 | CM-INV-005, CM-CHK-002, CM-CHN-001, CM-POS-001 (by name); CM-PAY-032 takes Send Cart's own link (case 4). My line is `core`; SH-50's and SH-53's are `shows`. The coordinator's check after SH-54 says a new thing's support is what the platform does with it, so the three should be aligned |
| Quick order lists (SH-53's) | SH-E-6eb269c7: the Trade theme's 'all-new quick order features' for bulk orders, coming (`shows`) | As SH-53: none held | As SH-53: D, B2B, under CM-B2B-001 | As SH-53 | CM-ACC-009, CM-EVO-001, CM-B2B-005 (by name): none |
| Shoppable videos | SH-E-a5bde01e: 'shoppable videos on the home feed from' Tolstoy and 'shoppable videos in your store from' Videowise and Showday, apps with no maker named. `extension-point`, their fillers | None in this entry: App Store listings, no category | B, CAT, beside CM-CAT-007 (product media), or E, CHN, under CM-CHN-002 where it is Shop Minis' | shoppable; video; quiz | CM-CAT-007 (product media, not videos to buy from), CM-MKT-010 (by 'video'), CM-CHN-004 (by 'shoppable'), CM-PAY-015 (by name): none. SH-53 left Tolstoy's shoppable videos as a lead with no line (SH-E-ee1a4e53); the coordinator may align the two |

## The CHANGES lines, and what I decided on each

Each was read again against its entry and the page data. Line numbers are the placements file's.

**Repeats of earlier batches' changes, which the coordinator kept and which aren't merged yet:**
- CM-AIA-005 `own-service` (line 123, Shop's AI shopping assistant);
- CM-B2B-001 `extension-point` (lines 57, 62, 67: discounts by apps for B2B customers, Acumatica's ERP integration, Faire's wholesale marketplace);
- CM-CHN-002 `extension-point` (line 118, Shop Minis from Tolstoy, Videowise and Showday);
- CM-CUS-007 `own-service` and CM-CUS-010 `own-service` (lines 121, 122, Shop's lead capture and sign-in);
- CM-MKS-003 `own-service` (lines 75, 79, Markets Pro);
- CM-MKT-007 `own-service` (line 125, Shopify Email);
- CM-MKT-011 `own-service` (lines 90, 92, 94, Shopify Audiences);
- CM-MKT-023 becoming held (line 120; SH-50's `core`);
- CM-ORD-008 `core` (line 35, POS's printed receipts' Liquid editor, as SH-53's custom QR code);
- CM-SUP-001 `own-service` (lines 130, 132, 134, Shop's reviews).

All are kept.

**New changes:**
- **CM-PAY-022 gains `extension-point`** (line 5, SH-E-4b3f7d64). 'Payment providers now have access to securely stored credit card information'. The providers are third parties (CM-PAY-011's apps), charging the vault the platform keeps (E38). Kept.
- **CM-PAY-032 becomes held and gains `core`** (line 41, SH-E-126592cc). Send Cart: 'Retail staff can send customers a link to complete an order', in the platform's POS. CM-PAY-032 is 'a link to pay for an order that the merchant sends the buyer'. Kept, open (case 4).
- **CM-LOY-006 gains `core`** (line 11, SH-E-3f1591a4). 'a more personal gifting experience with the option to add a recipient and greeting to their gift card, and schedule when their gift card is sent'. Kept, open (case 3).
- **CM-SEL-002 gains `core`** (line 60, SH-E-1f9ea46e). 'Digital products now supported in B2B checkout', 'non-physical products, like digital downloads, warranties, and services', Shopify Plus. Kept, open (case 5).
- **CM-INV-006 gains `own-service`** (line 38, SH-E-eddcf8ad). The Stocky app's transfers in POS, its maker named in a held post (E34). Kept, open (case 1).
- **CM-CHN-005 gains `own-service`** (lines 63, 65). Collective's filters and supplier details, and its order timeline, by Summer '23's 'our new curated network for sourcing and selling products' (E35). Kept, open (case 2).
- **CM-ANL-001 gains `own-service`** (lines 91, 95). The benchmarks in Shopify Audiences, 'Compare your ad performance to similar stores or industry groupings', the kind of benchmark the changelog places in analytics (SH-E-dd79056c), in an app whose maker a held card names. Kept, open (case 6).
- **CM-CUS-007 gains `extension-point`** (line 121, SH-E-ef0a68f5). Its link 'Try now' opens the App Store collection `apps.shopify.com/collections/shop-sign-in-apps`, apps that put Sign in with Shop on their lead capture forms (E3: a collection the card links). Kept.
- **CM-MKT-023 gains `extension-point`** (line 120, SH-E-a5bde01e). 'product recommendation quizzes from' Shop Quiz, a Shop Mini, an app with no maker named. Kept, open (case 7).

## Entries I couldn't tell, placed where they most plainly belong

1. **Shopify Inbox and Stocky, `own-service`** (SH-E-2bb78e72, SH-E-eddcf8ad; E34). The coordinator kept Inbox `core` on its Google Play publisher alone. The held changelog posts with 'we' are the other basis. If they don't count for an Editions card, Inbox's line is `core` and Stocky's is `extension-point` (an app's extension with no maker named, E3). CM-SUP-004 holds `own-service` already. CM-INV-006 changes either way.
2. **Shopify Collective, `own-service`** (SH-E-e07d939b, SH-E-b3565001; E35). It rests on reading Summer '23's 'our new curated network for sourcing and selling products' as Collective, the Collective card of that collection. If the network names no separate service, the lines are `core`, as CM-CHN-005's plan row is, and nothing changes.
3. **Gift card recipients on CM-LOY-006** (SH-E-3f1591a4). CM-LOY-002's note says 'gift cards (stored value) aren't gifting (CM-LOY-006)'. I read the note as keeping the stored value apart, not a gift card sent to someone with a greeting, which is CM-LOY-006's 'buying a product for someone else, with its message and card'. If the note keeps every gift card out, the line goes and CM-LOY-002's `core` carries the card.
4. **Send Cart on CM-PAY-032** (SH-E-126592cc). Send Cart sends the cart for the buyer to complete online. CM-PAY-032 is Salla's payment link sent from an order. If a cart link isn't a payment link, the line goes, and CM-PAY-032 holds nothing again.
5. **Digital products in B2B checkout on CM-SEL-002, `core`** (SH-E-1f9ea46e). The cell's reading says 'No statement shows Shopify itself delivering digital goods'. This card shows the checkout selling them, not who delivers a download. If `core` needs the delivery, the line is `shows`.
6. **Audiences' benchmarks on CM-ANL-001** (SH-E-e3dff2fc, SH-E-2df027fe). The benchmarks compare ad performance inside the app. If an app's ad metrics aren't the store's analytics, the lines go and CM-MKT-011 carries the cards.
7. **Shop Quiz on CM-MKT-023** (SH-E-a5bde01e). CM-MKT-023 is 'products the platform recommends to buyers on the storefront'. A third party's quiz in a Shop Mini recommends products in Shop. If the capability keeps to the platform's own recommendations on the store's storefront, the line goes. Shop Quiz's name carries Shop's brand and the card names no maker, so it isn't a filler. The App Store handle `product-recommendation-quiz-revenuehunt` is an address, not a statement.
8. **Shopify Lending's Term Loans and Line of Credit on CM-PAY-026** (SH-E-797024ee, SH-E-30f0185f, SH-E-14476db0). CM-PAY-026 is financing 'repaid from a share of the store's sales'. These two are repaid on a schedule or as used. I placed them there because the card calls the portfolio 'The next evolution of Shopify Capital', with all three products at the admin's `capital/offers`. If the coordinator keeps CM-PAY-026 to sales-share repayment, they are a new thing, 'Business loans and lines of credit' (C, PAY, beside CM-PAY-025), with no place of its own held but the route `capital/offers/line`, which the router may hold.
9. **POS Terminal, `shows`** (entries 8 to 11; E35). If CM-POS-002's terms (SH-S-7269, 'may elect to purchase POS Equipment from Shopify') are read as the maker of every device the hardware store sells, these are `own-service`. Neither changes the cell.
10. **POS Go's remote logout** (SH-E-0eb521ee). The admin's control over the devices the POS runs on is `core` on CM-POS-001, which holds PointOfSaleDevice, and POS Go itself is `own-service` on CM-POS-002. CM-TRU-001 is the admin's sign-in, so the logout's 'account security' takes no line.
11. **The Inbox store selector** (SH-E-2bb78e72). The switching between the owner's stores is the app's own, so it takes no CM-ACC-003 line. If it is CM-ACC-003's 'move between them', it takes one, `own-service`, which changes CM-ACC-003.
12. **'Sync 3P customer events'** (SH-E-e7acaf7e). I placed the events pulled from Klaviyo, Mailchimp, Seguno and Pinterest on CM-MKT-009, the capability that holds customer events, as `extension-point`. The coming ad cost and impression data went on CM-MKT-008, for the 'marketing ROI', as `shows`. Both are for the store's marketing insights, its help link `analyze-marketing/app-data-sharing`. The two lines could sit on one capability.
13. **The international expansion guide** (SH-E-93fc6c2a). It is `core` on CM-ONB-003, a guide of the platform's own reached in the admin, and `shows` on CM-MKS-001 for its topic. Rule 4 makes a guide `shows` on its topic's capability, and I read it as the platform's own learning for CM-ONB-003.
14. **Shop Campaigns' coming placements on Meta and Google** (SH-E-e3ca2188). They take a second CM-MKT-012 line, `shows`, with their own fillers, by the ruling after SH-34: a thing under its own condition.

## Structures whose items and sources disagree, or leave things out

- **No disagreement found.** Each entry matches its product in the page data at its pointer (line 6).
- **Characters a quote must keep.** The descriptions hold non-breaking spaces (entries 1, 6, 24, 32, 37, 45, 46, 67, 68, 69) and straight apostrophes ('Shopify's', 'you'll', 'We've'). I quoted around the first, and with “ ” around the second.
- **Entry 76's description ends with a straight double quote** after a curly opening one: '“It usually takes us 25-30 minutes … within a minute."'. It is held as the page states it. A placements row can't hold `"`, so I didn't quote it.
- **Spellings and productTypes as the page has them:** 'Tik Tok' in the title against 'TikTok' in the text (entry 53); `productType: Shopify Form` (entry 63); a lowercase 'try now' on four Markets cards, linking `http://www.shopify.com/admin/...` rather than admin.shopify.com.

## What the sources state that no entry holds (for the second stage)

- **Three of my cards carry YouTube videos** (`productsWithYoutube`): fulfillment-from-retail-locations (`rjMGQlvTLGI`), centralized-privacy-settings (`ucIXAw0YWpQ`) and shopify-lending (`-jhwMVQdxBU`). Two also carry a `speakerBubbleVideo` (gid://shopify/Video/36221445734690, 36221455991074). Their subtitles are `shopify/editions-videos` (selection: not read in this pass). They are leads for these features' cells.
- **Winter '24's page data has more keys than `pageSections`:** `heroContent`, `globalContent`, `chillHillContent`, `navigationContent`, `predictiveSearchContent`, `globalStrings`, `allEditionsDropdownItems`, `searchResultEditionKeys` and `footerContent`. I read only their names. SH-54 read the hero.
- **Leads no line takes,** each named in passing, in a list, or a homonym:
  - CM-APP-010 (app settings, holds nothing): the checker's first lead for Acumatica, by 'integration';
  - CM-CHN-001: Faire's 'a new sales channel for Shopify merchants', placed on CM-CHN-003 as a marketplace;
  - CM-ORD-001: the 'index menu in Orders' from which Ship from Store is reached;
  - CM-SHP-009: the fulfilment that triggers a capture (entry 4);
  - CM-PAY-030 (bank transfer, not-stated): 'checks and bank transfers', examples of off-platform partial payments;
  - CM-B2B-003: the catalog prices B2B discounts stack on;
  - CM-CUS-002: the segments Collabs' commissions follow;
  - CM-MKT-006: the automations Shopify Email's templates are used in;
  - CM-PAY-014: 'Shop Pay’s extensive buyer network' behind the terminal's digital receipts;
  - CM-SFR-012 and CM-CUS-010: the Storefront API and Customer Accounts API that headless B2B uses, a list;
  - CM-MKT-002: the discount the lead capture form applies;
  - CM-SUP-001: Collective's 'verified product ratings', part of its search;
  - CM-RET-002: commissions removed for refunded orders;
  - CM-MKT-010: the ad platforms whose costs and impressions are coming;
  - CM-CUS-010: the saved payment methods' help link in customer accounts (entry 1);
  - CM-TRU-008: its setting lives on the privacy page entry 77 links;
  - the Cohort Analysis report's 'predictive spend metrics', which no capability holds (searched: lifetime value, predict, cohort).

## Problems with the brief or the script

- **The rulings changed while I worked** (two rulings after SH-38). I re-read them, and neither changed a line (above).
- **The checker's quote parser still reads a plural possessive** ('catalogs’ prices') as a closing quote, as SH-51 found. I rewrote thirteen possessives.
- **`held_entries.py earlier` printed one earlier line** in 81 entries. The maker statements of E34 and E35 were found only by searching `entries.tsv` and the earlier placements for each app's name with 'we' or 'our'. A key from an app or product name to the held posts that name its maker would find them for SH-56 to SH-67.
- **`show`'s leads were mostly names' words,** as SH-50 to SH-54 found. The useful ones were by identifier: shopify audiences, shopify collabs, shop campaigns, shopify collective, marketplace connect, shopify capital, shopify balance, inventory transfers, return reasons. The CM-PAY-032 change came from reading a lead whose cell holds nothing (by name: link, order, send) against the card's words.

## Where B-extent and the brief differ

None I relied on.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 81 of 81 entries, no problem.
- **The cell changes stand, each read again:**
  - CM-PAY-032 is held, `core`: Send Cart's 'link to complete an order', sent by the store's staff, is a link to pay, the cell's thing (a marked reading).
  - CM-LOY-006 gains `core`: a gift card bought for a recipient, with a greeting and a date, is buying for someone else with a message. CM-LOY-002's note keeps the stored value apart, not this.
  - CM-SEL-002 gains `core`: digital products sold through the platform's own B2B checkout, a marked reading; who delivers a download isn't stated.
  - CM-PAY-022 and CM-CUS-007 gain `extension-point`: payment providers' access to stored cards, and the App Store's collection of sign-in apps.
  - CM-INV-006 (Stocky: 'We’ve introduced … in Stocky') and CM-ANL-001 (Audiences' benchmarks) gain `own-service`. CM-MKT-023 gains `extension-point` (Shop Quiz).
- **A ruling after SH-55** (`review-H-rulings.md`): a first-party app's own features are `own-service`, and its plan lines `core`, wherever held words name the platform as its maker.
  - Shopify Collective is aligned by it, on 'the Collective app' and 'Let our AI-powered search … in Shopify Collective Discovery' (SH-E-850b28ae). Summer '23's 'our new curated network for sourcing and selling products', this batch's basis, names no product.
  - Shopify Flow, Shopify Email's Editions lines and Translate & Adapt (this batch's line 82) are aligned too: 61 lines of SH-34 to SH-38 and SH-50 to SH-55.
  - E34 and E35 stand under it.
- **E34 to E41 stand for SH-56 to SH-67.**
- **The open cases, decided:**
  - **Term Loans and Line of Credit stay on CM-PAY-026,** as the platform's merchant financing, with their repayment (a schedule, or interest on what is used) as a quality. The cell's definition, 'repaid from a share of the store's sales', is read again at Shopify's amendment, to widen it to merchant financing.
  - 'Sync 3P customer events' keeps its two lines.
- **New things:**
  - Planet, Web performance dashboard, Quick order lists and Shoppable videos;
  - Staff sales attribution, whose support differs: SH-50 and SH-53 write `shows`, this batch `core`. It is decided with the new thing.

  SH-53's Tolstoy line now takes Shoppable videos too.
- **The tools:** `held_entries.py makers --platform P NAME …` prints the held entries that name an app with a maker's cue, with their lines, as this batch asked. The brief names it.
- **Cost:** 30.0 million tokens over 109 requests, about 370,000 an entry. The context reached about 488,000 tokens, largely from searching other structures for makers, which `makers` now does in one call.
