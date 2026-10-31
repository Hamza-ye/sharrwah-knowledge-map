# SH-61: notes

Batch SH-61: 82 entries of Shopify's `editions-page-data`, read in observed-sh at `e38dc17e3`. They come from `structures/shopify/editions-page-data/loaderData/items.jsonl`:
- line 8, Winter 2025's developer collections: Growth <developer> (12 cards, entries 1 to 12) and Tools <developer> (10, entries 13 to 22);
- line 9, Summer 2025's collections: Sidekick (5, entries 23 to 27), Retail (11, 28 to 38), Checkout (11, 39 to 49), Global (19, 50 to 68) and Marketing (14, 69 to 82).

I worked from the brief, the rules digest (`held/rules/editions-page-data.md`, section 6 included) and the last section of `review-H-rulings.md`. I read one batch's notes beyond the digest: `notes-SH-50.md`, its E3 only, to see what rule 19's "one with no maker named" covers (entry 71). Every placement rests on the card's own words, its section's title, its CTAs' addresses (in `reading`) and the cells. I read no shopify.dev, help or blog page.

**The split with SH-60.** SH-60's last lines are Winter 2025's developer Extensions cards; this batch starts at the next collection, Growth. Its lines on the developer cards (API, pixels, GraphQL) were read for their patterns. SH-62 to SH-67, which may run beside this batch, weren't read.

**The collections.** None of the collections has a description of its own (`descriptionHtml`/`description` empty). Winter 2025's developer collections are titled 'Growth <developer>' and 'Tools <developer>' in the source itself. The page's developer summary (`developerCollections/0`, 'Top updates <developer>', `isSummary: true`, no products) links this batch's entries 14 and 16: 'GraphQL replaces REST' and 'new endpoint mappings to find equivalent operations'. Both readings quote it.

## Counts

- 82 entries: 81 `capability`, 1 `new`, 0 `out`.
- 132 lines on 64 capabilities and one new thing, by support:
  - `core` 107;
  - `core;extension-point` 9;
  - `own-service` 6;
  - `extension-point` 5;
  - `shows` 5.

## The new thing

- **`new:Planet`** (SH-E-bf8da5d5, 'Carbon-neutral shipping in checkout'): the name SH-50 keeps (the digest's section 4), `own-service` on its maker statement SH-E-bc581483, scoped Plus ('Exclusive to Plus.').
  - The checkout it acts on takes no line (E81).
  - Its leads CM-LOY-008 (referral) and CM-SHP-019 (delivery option generators) aren't its thing.
  - Nothing new to add to SH-50's description of it: no place of its own in this entry. Its only address is the App Store's `apps.shopify.com/planet`.

## The checker's lines, and what I decided

**CHANGES:**
- **CM-CHN-005 gains `own-service`** (line 15, SH-E-c3e9ffe2, 'Automate Collective returns').
  - The cell holds only `core` now. The digest's section 3 makes Shopify Collective's own features `own-service` (SH-E-850b28ae, SH-40's `own-service` line on CM-CHN-005), and its rule 16 and E82 keep Collective's work with others in its CM-CHN-005 line.
  - The card's 'new Shopify Collective automated returns flow' is Collective's own. Kept.
  - The returns app and the webhook take their own lines: CM-RET-003 `core;extension-point` and CM-API-008 `core` (rule 17, E82).
- **CM-MKT-007 gains `own-service`** (lines 119, 120 and 123). These are Shopify Email's 'Cancel email campaigns mid-send', 'Customize email padding and footer' and 'Store credit in Liquid' (its marketing emails).
  - Each card's link opens Shopify Email's help pages (`shopify-email/create-email/...`), so each is about that app (rule 53, the ruling after SH-38).
  - The digest's section 3 holds its maker statement (SH-E-32e5ccc3) and the rename to Shopify Messaging. Kept.
- **CM-ORD-014 becomes held and gains `core`** (line 132, SH-E-32bece5d, 'Disable “Buy again” button').
  - The cell is Reorder: 'repeating a past order', which on Shopify holds nothing.
  - The card's toggle shows or hides the buyer's Buy again button on the Order Status page. Its help address is `customer-accounts/new-customer-accounts/manage#buy-again`.
  - The button is a buyer's repeat of a past order, and the toggle is the store's own setting: `core`. Kept.
  - CM-LOY-007 (reminders to buy again) and CM-B2B-005 (a business buyer's lists) are the cell note's own homonyms.
- **CM-SHP-020 gains `core`** (line 98, SH-E-6ce26bee, 'Expanded flexibility on Managed Markets').
  - The card lets the merchant 'decide whether to handle duties, taxes, customs, and restrictions yourself or have Shopify do it'.
  - Customs is a list item of the card's news (E80). Managed Markets' customs codes are already placed on CM-SHP-020 `core` by the changelog's SH-E-f595384d, and SH-E-6f1a6cfc places HS codes there. The cell isn't amended with them yet. Kept.
  - Duties and restrictions stay on CM-MKS-003 (rule 45). Taxes go on CM-TAX-001, as SH-60's SH-E-84c5eea1 placed Managed Markets' taxes.
- **CM-SUP-006 would have gained `core`** from my first line on SH-E-3777b8ea ('Knowledge Base app for AI shopping'). I changed it to `extension-point`, and the CHANGES line went away. See case 1 below.

**NOTE, a product named with the platform's brand, on a `core` line:**
- the Shopify App Store's own features (lines 3, 4, 13): rule 7;
- the Shopify CLI and Shopify Functions, the platform's developer tools (27 to 29): rules 17 and 41;
- Shopify POS (38, 44, 52): rule 9.

None of them is a separate product.

**NOTE, a first lead that holds nothing:**
- CM-OPS-004 (store status) for the Tools cards (lines 18 to 21, 26) and the 'Order Status page' (132): the word 'tools' is the collection's title, and 'status' is the page's name;
- CM-APP-010 (app settings) for Roblox's 'integration' (64);
- CM-LOY-008 for Planet (74);
- CM-MKS-009 (countries' reference data) for Klarna's and Apple Pay's lists of countries (91, 93), which are scopes, the subjects' market data.

None is the entry's thing.

**NOTE, `own-service`:**
- Collective, Planet and Shopify Email, above;
- Shopify Collabs' new mobile app for creators (SH-E-b9ec2d82): CM-MKT-015, on 'our creator platform' (SH-E-709b37e4), as SH-50 placed Collabs.

## Rules followed that the digest doesn't state (for the coordinator)

- **E86. The App Store's tools for developers' own listings, ads and installs are CM-APP-002 `core`.**
  - Examples: bid suggestions, ecommerce events on ad campaigns, click dates for attribution, the 'Get support' button. Entries 2, 3, 4 and 7.
  - This follows SH-59's ads metrics dashboard (SH-E-13fed6d0).
  - `core;extension-point` stays for features that match, rank or mark third parties' apps, as E70 has it: brand-term search, feature-based discovery, in-admin discovery points, Built for Shopify. Entries 5, 6 and 8 to 10.
  - CM-MKT-008 (a store's sales attribution) and CM-SFR-013 (the storefront's search) are homonyms.
- **E87. The Partner Dashboard takes CM-PTN-001 `core` where the card's news is in it.** The cases are 'click dates now included in the partners export feature' (entry 3) and 'monitor your mandatory compliance webhook subscriptions in the partner dashboard' (entry 17).
  - This is E68 applied.
  - SH-59 left the dashboard 'named in passing' where it was only where managed pricing is set (SH-E-292688e3). The two readings differ by whether the dashboard's own feature is the news.
- **E88. A forum for developers is CM-DVT-001 `core`** (entry 19, community.shopify.dev): the platform's own resources for building apps. CM-ONB-003 is support and learning for merchants. See case 6 below.
- **E89. An app the card names at an App Store address with no maker held, whose name carries no brand, is `extension-point`** (SH-50's E3, 'Install the Twitter App.'; the digest's rule 19). The case is the Knowledge Base app, entry 71. This holds even where the address's handle carries the brand (`shopify-knowledge-base`), since an App Store address names no maker (rule 53). Rule 13 is for an app whose name is Shopify-branded.
- **E90. A separate tool at its own site is `shows` on what it does** (entry 56, 'Tariffguide.ai to classify products', 'Get app' to tariffguide.ai).
  - It is named by its brand, with no maker held (`makers`: none), and placed in no admin, plan or App Store address. That is rule 21.
  - It isn't `outside`: no held statement names its maker a third party (the brief's 'not a third party for that reason').
  - Its lines are CM-SHP-020 (the HS code) and CM-TAX-008 (the duty rate).
- **E91. 'Rolling out now for those new to Shopify' is `shows`, with the group named as its scope** (entry 27, Sidekick's screen share). This is rule 32 with E69. The group is the card's own words, as rule 27 takes a kind of business.
- **E92. A condition on countries by what they lack ('in select countries without small coins', entry 36, cash rounding) is the scope, not a release marker.** Rule 32's 'select businesses' says who is let in. This says where the feature applies.
- **E93. A feature told by a POS card and a merchant card in other words takes both cards' capabilities (E79), each support by its own words.** The case is one discount across products, orders and shipping.
  - The Marketing card (entry 69) says 'with select discount apps' and links an App Store collection, so it is `extension-point` on CM-MKT-004 and on CM-MKT-001.
  - The POS card (entry 38) names no app. Its help address files it under discounts with apps, so it is `core` on CM-MKT-001 and CM-POS-001, and `shows` on CM-MKT-004, all scoped POS Pro.
- **E94. Managed Markets' list of what the merchant or Shopify handles splits by rule 45** (entry 60).
  - Duties and restrictions stay in the CM-MKS-003 line (scope US, no add-on scope).
  - Taxes (CM-TAX-001) and customs (CM-SHP-020) take their own lines, with the market-level control on CM-MKS-001. Each is scoped `US and Managed Markets`.
- **E95. A store credit balance 'in Liquid' takes CM-LOY-001 `core`, and each place the card names takes its line** (entry 77).
  - The marketing emails are Shopify Email's, whose custom Liquid page its link opens: CM-MKT-007 `own-service`.
  - The online store's Liquid is the theme code: CM-SFR-002 `core`.

## Entries I couldn't tell, and what would settle each

1. **SH-E-3777b8ea, the Knowledge Base app** (CM-AIA-005 and CM-SUP-006, `extension-point`).
   - Its App Store handle is `shopify-knowledge-base`, but no held statement names its maker.
   - A later changelog post puts a Knowledge base 'built into your Shopify admin at Sales channels > Agentic > Knowledge base' (SH-E-a50b68cc, the ruling after SH-2, `core`).
   - What would settle it: a maker statement, such as the app's store listing (its developer), which the second stage reads with single app listings. With one, the lines are `own-service`.
2. **SH-E-0b98d8b4, 'Better in-admin app visibility'** (no link).
   - It is placed on CM-APP-002 (the platform's distribution of apps, E70) rather than CM-APP-001 (the admin's apps place), since the card is about apps being found.
   - What would settle it: a statement of where the discovery points are, such as an admin route.
3. **SH-E-e577db92, 'Offer Apple Pay as a payment method while supporting your custom checkout experience.'**
   - If 'your custom checkout experience' names merchants on a custom (non-Shopify) checkout, as SH-54's 'For businesses using a custom checkout' does (rule 27), it is the line's scope. If it means a customized Shopify checkout, it isn't.
   - I left the scope empty. The help page `payments/accelerated-checkouts/apple-pay` would settle it.
4. **SH-E-b51eb547, Klarna on Shopify Payments in eleven countries.**
   - It keeps SH-60's CM-PAY-015 for the Winter 2025 card (SH-E-89e5e282; rule 4), though this card's words don't say pay later.
   - Its help address is under `shopify-payments/local-payment-methods`, which is CM-PAY-017's definition ('region-specific ways to pay, offered through the platform's payment service').
   - The coordinator may move both cards, or add CM-PAY-017.
5. **SH-E-b36fa4c0, 'Accept Apple Pay for subscriptions'.**
   - Placed on CM-PAY-012 and CM-SEL-001.
   - Whether the wallet is kept for the later charges (CM-PAY-022, rule 43) isn't stated. The help anchor `apple-pay#requirements` would say.
6. **SH-E-8cc0cb8a, the developer community forum.**
   - Placed on CM-DVT-001 (E88). No capability holds a developers' community.
   - The coordinator may prefer CM-PTN-001 (the programme for developers), or extend CM-ONB-003's note to developers.
7. **SH-E-d6369588, 'AI-powered fraud models on Shopify Payments that automatically authenticate risky transactions'.**
   - Placed on CM-PAY-002 and CM-ORD-006, as the changelog's SH-E-1a1ee996.
   - The authentication of risky transactions may be 3D Secure (`new:3D Secure`, SH-54), but the card doesn't name it. The linked blog post (`shopify-payments-pre-authorization`) would say.
8. **SH-E-7a30434a, Campaigns' 'QR codes, shareable links'.**
   - No capability holds them (`caps --terms` QR code, shareable link: no hit). I kept them as terms of the CM-MKT-005 line, tools of the Campaigns page, which is not a place of its own.
   - The UTMs take CM-MKT-008 (the ruling after SA-25 on `utm_source`).
9. **SH-E-8490fddf and SH-E-ad263289, selling from multiple business entities.**
   - Both take CM-POS-001 beside CM-ACC-005. The Retail card's words are 'retail operations' and 'retail entities', under the section Retail, with the help anchor `#retail`. The Global card's word is 'in-person'.
   - Shopify Payments is the condition of both (each entity's own account), not a line of its own.
   - The coordinator may hold the POS line as named in passing.

## What the sources state that no entry holds (for the second stage)

- **Summer 2025's `heroContent`** (items.jsonl line 9): 'Horizons', '150+ updates to Shopify', and a summary whose links name this batch's cards. They are 'Sidekick gets smarter', 'in 20 languages', 'redesigned POS', 'business entities' and 'payout currencies', with the batches' later cards ('theme foundation', 'vibe-ready dev platform', 'AI shopping agents', 'Shopify's Global Catalog'). It is a heading with no products (rule 37).
- **Winter 2025's developer summary** (`developerCollections/0`, line 8), as above. It also names SH-60's cards (Functions, Hydrogen, the Theme CLI).
- **Summer 2025's `globalContent.carouselAriaDescription`**: 'A carousel that displays 10 distinct new themes built off the Horizon theme platform, as jumping off points to start your store.' It is an aria string, so no statement (rule 1). The Horizon themes are presumably the theme cards of a later batch.

## The structure

No disagreement found between the items and the source for these entries. The `title` and `headlineTitle` differ on many cards, such as 'Shopify POS version 10' and 'Redesigned Shopify POS'. I took both as the card's words (rule 1), and both appear in the terms.

## Problems

None with the script. The brief's NOTE on 'a product named with the platform's brand' fires on every line whose terms hold 'Shopify App Store', 'Shopify CLI', 'Shopify Functions' or 'Shopify POS'. The digest's rules 7, 9 and 17 already settle these.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 82 of 82 entries, no problem.
- **The `CHANGES` stand:**
  - Collective's returns are `own-service` on CM-CHN-005 (E82).
  - Shopify Email's three cards are `own-service`.
  - The 'Buy again' toggle makes CM-ORD-014 held, `core`, as SH-42's reorder post does.
  - Managed Markets' customs are CM-SHP-020 `core`, as the changelog places them.
- **The Knowledge Base app (open case 1)** stays `extension-point` (E89). No maker statement is held for it, and `makers` finds none. The changelog's 'Knowledge base is now built into your Shopify admin at Sales channels > Agentic > Knowledge base', which the ruling after SH-2 quotes, is about the later admin section, which is `core`. It doesn't name the earlier app's maker. Both are read again with Agentic's routes (SH-S-5027, SH-S-5028) at Shopify's amendment.
- **The rules E86 to E95 stand** and join the digest's section 6.
- **The open cases stay as placed.** None changes a cell.
- **Cost:** 15.6 million tokens over 81 requests, about 190,000 an entry. The context reached about 357,000 tokens.
