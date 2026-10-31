# SH-53: Winter '23's last Product list heading, and Summer '23's first 81 features (high)

**What the batch is.** 82 entries of `editions-page-data` (observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`):
- entry 1: Winter '23's last Product list heading, 'Commerce Components by Shopify' (line 4, `productList/solutions/8/collections/0/products/0`), left to this batch by SH-51's check;
- entries 2 to 82: the Summer '23 Edition (line 5, `routes/($lang).editions.summer2023._index`; its hero title 'Shopify Editions Summer ’23'):
  - Featured (`featuredCollection`, 14 cards, entries 2 to 15);
  - AI for commerce (9 cards, entries 16 to 24);
  - World's best checkout (products 1 to 11, entries 25 to 35);
  - Sell to every customer (26 of its 29 products, entries 36 to 61);
  - App development (14 cards, entries 62 to 75);
  - The Shop channel (products 1 to 7, entries 76 to 82).

A card listed in Featured and in a collection under the same handle is one entry (`merge:handle`), with both sections in `within`. So the collections' platform-conversion, shopify-bundles-app, flexible-sections, shop-store-updates and shopify-subscriptions-app are entries 3, 7, 11, 12 and 15. Featured's shopify-credit (entry 4) and admin-quality-improvements (entry 13) are also Manage your money's and Everyday operations' cards, which later batches hold. The next batch begins with Full-stack marketing (`displayCollections/5`).

**Count.** 158 lines: 153 on a capability, 5 `new`.
- Every entry is placed; none is `out`.
- 77 entries are only on capabilities, 1 only `new` (SH-E-5105ac99), 4 on both (SH-E-e06df061, SH-E-6970c2c4, SH-E-500cc746, SH-E-9e317cee).
- Supports over the lines (a line with two counts in each): `core` 83, `extension-point` 34, `shows` 33, `own-service` 18.

**E1 to E18 are kept,** with the rulings in `review-H-rulings.md`'s last section. One ruling was added while I worked (after SH-69): a line takes its own scope where its thing is stated under its own condition. I applied it to SH-E-1d272a37 (bundles built with the APIs, Shopify Plus), SH-E-500cc746 (POS access, Shopify Plus), SH-E-f0bed13e (observability, Shopify Plus), SH-E-e18a17fc (organization-level custom apps, Shopify Plus) and SH-E-9e3f5c76 (Markets Pro's shipping). Where an entry was of a kind E1 to E18 don't cover, the rule I followed is below, for the coordinator to align with SH-54 to SH-67.

## Rules I followed where E1 to E18 don't reach

### E19. A case study

Summer '23 puts case studies among its features: 'Stellar Eats increases conversion by 3.5% with Shopify’s one-page checkout' (SH-E-890272d7) and 'KITSCH finds new customers and a low-lift acquisition channel' (SH-E-f76b26ab). Each tells one merchant's story of a feature, linked to a blog post or a customer page.
- I placed each `shows` on the feature's capability: a topic and a claim (rule 4's titles; E3's 'a topic or a claim alone').
- A pricing term the story states is the line's quality: 'Only paying for new customers', as E9 takes 'Only pay for successful sales'.
- The merchant isn't a filler. It uses the feature; it doesn't do it.
- The later batches hold four more (Laurie Ellen, Drake Related, Element Brooklyn, Snarky Tea).

### E20. A stat card that says what its number is about

E11 makes a stat card's bare number `out`. Summer '23's stat cards say what the number is about, so each is placed by its words:
- Shopify Checkout's '15%' (SH-E-79f55e09) has a description of the checkout: CM-CHK-001, CM-PAY-014 and CM-CHK-004;
- 'Over $1.5 billion' 'in earnings by app developers since we launched the Shopify App Store' (SH-E-67b34cd4), a claim alone: CM-APP-002 `shows`;
- 'Shop Pay lifts conversion by up to 50%' (SH-E-3739d728), a claim alone: CM-PAY-014 `shows`.

The number is a claim, not a quality (E9). So are '100M+ buyers' and 'over 100M Shop users'.

### E21. Shopify's free themes, 'Our free themes'

Three cards speak of the free themes:
- 'Our free themes now have built-in support for theme animations' (SH-E-cb98c38c);
- 'Our free themes now come with more styling features' (SH-E-8ca9faf9);
- 'With the latest version of our free themes, you can create and edit color schemes' (SH-E-9ab23837).

E3 reads 'our' as a maker statement where the thing is a separate product, and a free theme is a product Shopify says it makes (the first card links the Theme Store's Dawn). So the themes' own features are `own-service`:
- on CM-SFR-001, the store's theme, for all three;
- on CM-SFR-007 for the announcement bar the free themes carry.

The theme editor, where the colour schemes are edited, stays `core` (CM-SFR-002, E3). The apps a theme shows beside the cart are CM-SFR-004 `extension-point`. CM-SFR-001 and CM-SFR-007 gain `own-service` (CHANGES below). If the coordinator reads a theme as part of the online store rather than a separate product, these lines become `core`, and CM-SFR-007 gains `core` instead.

### E22. 'We' and 'our' on an app, against the platform's own client

The rulings after SH-35 and SH-36 make an app's things `own-service` where 'we' make, upgrade or ship it. I applied them to the App Store's separate apps:
- Shopify Bundles: 'our new, free bundles app' (SH-E-1d272a37) gives CM-SEL-006 and CM-APP-011 `own-service`;
- Search & Discovery: 'We’ve also made it easier for businesses with large catalogs to add, bulk edit, and view search boosts and product recommendations.' (SH-E-9b869699) gives CM-SFR-013, CM-MKT-023 and CM-APP-011 `own-service`. SH-50 placed Search & Discovery `shows` where its card named no maker (E3). This card names one.

A Shopify-branded app with no 'we' or 'our' keeps the ruling after SH-36:
- at its admin address it is `shows`, with CM-APP-007 `core` (Marketplace Connect, Shopify Email; M-10);
- named with no address it is `core` (Shopify Subscriptions, and Shopify Inbox and Shopify Email in the Shopify Magic card).

Shopify POS I read as the platform's own client for in-person selling, as E3 reads the admin's mobile client. SH-50's E12.1 placed Winter '23's POS cards so, and CM-POS-001's cell reads it so ('Shopify sells in person itself').
- So three POS cards stay `core`: 'We're streamlining workflows across POS', 'we're adding what you need to simplify your staff management' and 'We've enhanced our POS inventory management features' (SH-E-4d179e85, SH-E-500cc746, SH-E-e8962bc2).
- POS's devices are separate products. 'POS Go, our all-in-one POS device' (SH-E-fc9fba8c) is CM-POS-002 `own-service`, as E3 reads 'our latest mobile point of sale (POS) device'.
- If the coordinator reads POS as an app Shopify makes, the three POS lines become `own-service`. That changes nothing: CM-POS-001 holds both.

### E23. A card of Commerce Components

E14 gave a collection's cards the scope 'Commerce Components by Shopify' from the collection's lead card. Summer '23's 'Shop Pay can now drive conversion for the biggest brands on external checkouts' (SH-E-6970c2c4) states the offer in its own `productType`, 'Commerce Components'. It is Shop Pay for 'enterprise retailers not on Shopify'.
- Its lines take the scope 'Commerce Components', in the source's words.
- The card takes a line on the new thing Commerce Components by Shopify, since it is one of the components (M-6 refined).
- Shop Pay apart from the platform is a separate product: CM-PAY-014 `own-service`, on the maker evidence the cell holds (the Shop Pay Merchant Terms, SH-S-0411 and SH-S-0413; M-1). In the platform's own checkout, Shop Pay stays `core` (E3; SH-E-79f55e09).

### E24. Developer tools against the developer API

SH-50 and SH-51 placed every CM-DVT-001 and CM-DVT-002 line `core`, and so did I. The tools are the platform's own and no third party makes them, even where the card says they are for building apps (SH-E-7419edbc, SH-E-7c8c57e1). E3's 'extension-point where the card says apps … do the work' I applied to the API. CM-API-001 is `extension-point` where the card's words say apps do the work through it: '20+ new tools and APIs', 'making it easier to build apps that customize any commerce experience' (SH-E-7419edbc), as B-extent's convention has it. This changes CM-API-001 (CHANGES below). A Function API is `extension-point` by its capability's own definition, app-written logic (CM-CHK-005, CM-CHK-006, CM-SHP-005), even where the card names no app (SH-E-70d6289b).

### E25. Quotes from a dialog's text

SH-51 found that the checker reads a quote across a link's markup. For Summer '23's dialogs (`descriptionHtml`) it doesn't: the rendered page holds 2 of the edition's 143 descriptions (the register), so the only held text is the page data's HTML. I quoted each piece within one text node, with the link's own words apart, as in 'Discover quality products' to sell 'from top Shopify brands who will ship directly to your customers'. Eleven quotes were requoted so. A term that crosses markup isn't found either (SH-51), so 'Shop Pay', split as `Shop Pa</a><a …>y` in SH-E-79f55e09, isn't a term there.

## New things

Shopify's Editions are in English only: no Arabic name is held.

| New thing | Entries | Place of its own | Proposed domain, area, parent | Terms searched (`caps --terms`) | Leads read |
| --- | --- | --- | --- | --- | --- |
| Commerce Components by Shopify (SH-51's) | SH-E-5105ac99, Winter '23's Product list heading, which names SH-51's item SH-E-acf42aeb by its words (its collection holds four items and one heading, so E18 maps it by heading, as SH-52 did); SH-E-6970c2c4, by its `productType` (E23) | As SH-51: none held | As SH-51 | As SH-51 | The checker's leads CM-ACC-002, CM-B2B-003, CM-AIA-005 (by name: 'commerce', 'product'): none |
| Quick order lists | SH-E-e06df061: 'Show customers a list of product variants, so they can easily order sizes, colors, and more, all from one section of your product pages', its help link a theme section (`store-contextualization#add-the-quick-order-list-section-to-your-product-page`) | None held: a section of the theme on one help page, with no admin route, API group, plan line or app category. So `shows` | D, B2B, under CM-B2B-001, beside CM-B2B-005 | quick order; quick order list; order form; bulk order; variant list; order list | CM-B2B-005 (a buyer's saved lists to order again: not this); CM-CAT-002 (variants: what the list shows); CM-INV-009 (a false match); the checker's CM-PAY-013, CM-PLN-001, CM-PAY-015, CM-CHK-009 (by name): none. B2B selling, in a later batch, holds its own card 'Quick order lists' (`b2b-quick-order-lists`): name it the same |
| Staff sales attribution (SH-50's) | SH-E-500cc746: 'Easily attribute a sale to a staff member then edit that attribution after an order is completed.' | As SH-50: none held | As SH-50 | sales attribution (CM-MKT-008, crediting orders to marketing: a homonym) | The checker's CM-PAY-021, CM-POS-001, CM-TAX-009, CM-TRU-008, CM-ORD-010: none |
| App versions | SH-E-9e317cee: 'App versioning and unified deployment', 'With app versions, you can now deploy your extensions together in a single package through the CLI' | None held: a shopify.dev guide; the Partner Dashboard's versions page isn't held. So `shows` | F, APP, under CM-APP-001, or beside CM-DVT-002 | app version; deployment; app configuration | CM-API-006 (the platform's API versions: a homonym); the checker's CM-APP-009, CM-APP-011, CM-DVT-001, CM-PAY-003 (by name): none. The CLI part takes CM-DVT-002 `core` |

## The CHANGES lines, and what I decided on each

Each was read again against its entry. Line numbers are the placements file's.
- **CM-AIA-005 gains `own-service`** (line 148, SH-E-28190bfc). Shop's 'AI-driven product recommendations' and 'personalized discovery', its link labelled 'Learn more about AI shopping assistant'. CM-AIA-005 is buyers discovering products through AI on channels the platform operates, and Shop is one; Shop's things are `own-service` (the ruling after SH-34). Kept, open (case 7).
- **CM-API-001 gains `extension-point`** (line 13, SH-E-7419edbc). See E24. Kept.
- **CM-CHN-002 gains `extension-point`** (lines 153 and 154). The Shop Minis SDK, 'now you can extend your Shopify app’s reach in the Shop app', and Shop Minis from Tolstoy and Zipify. SH-50 made the same change (Foursixty, Supergreat), which the coordinator kept; it isn't merged yet. Kept.
- **CM-CUS-007 gains `own-service`** (line 159, SH-E-6d0e118e). 'Lead capture with Shop', Shop's feature (the ruling after SH-34), powered by Klaviyo, its filler. Kept, open (case 4).
- **CM-CUS-009 gains `extension-point`** (lines 47 and 59, SH-E-c6b4dbc1 and SH-E-6242fae0). Apps that 'suggest and correct a buyer’s address' at checkout. CM-CUS-009 holds Shopify's address autocompletion at checkout, an address service of the same kind. Kept, open (case 6).
- **CM-CUS-010 gains `own-service`** (line 158). Sign in with Shop, as SH-50 and SH-51 placed it (kept). Kept.
- **CM-DVT-004 gains `core`** (line 145, SH-E-17542ca4). 'New partner accounts come with a pre-populated development store', as SH-51 read the test-data development stores (kept). Kept.
- **CM-MKS-003 gains `own-service`** (line 122, SH-E-9e3f5c76). 'Our Merchant of Record capability integrates seamlessly with Shopify', for Markets Pro: 'Our' is Shopify speaking of a separate service (E3). The cell holds Managed Markets 'powered by Global-e' as `outside`; each rests on its own statement. Kept, open (case 3).
- **CM-MKT-023 becomes held and gains `own-service`** (line 119, SH-E-9b869699). Search & Discovery's product recommendations, in the app Shopify says it upgrades (E22). SH-50's `core` line, which the coordinator kept, isn't merged yet, so the cell shows as holding nothing. Kept.
- **CM-OPS-005 becomes held and gains `extension-point`** (line 113, SH-E-f0bed13e). 'Exclusive to Shopify Plus, you can now' 'connect your preferred observability service', 'like DataDog, Splunk, or New Relic, to monitor, analyze, and retain logs', through Oxygen's log drains (its link): third parties keep the storefront's logs through the platform's interface. CM-OPS-005 is 'Store logs: the entries the store's logger records (WooCommerce Logs)'. Kept, open (case 5).
- **CM-ORD-008 gains `core`** (line 87, SH-E-4d179e85). POS receipts with 'your own custom QR code', the store's own printed receipts. CM-ORD-008 joins invoices and receipts (its Invoice and receipt apps). Kept.
- **CM-SEL-006 gains `own-service`** (line 15, SH-E-1d272a37). 'our new, free bundles app': Shopify speaking of an app it makes (E22). Kept.
- **CM-SFR-001 gains `own-service`** (lines 78, 107 and 108). 'Our free themes' (E21). Kept, open (case 1).
- **CM-SFR-007 gains `own-service`** (line 109, SH-E-8ca9faf9). The free themes' announcement bar (E21). Kept, open (case 1).
- **CM-SFR-013 gains `own-service`** (line 118, SH-E-9b869699). Search & Discovery's filters, in the app Shopify says it upgrades (E22). Kept.
- **CM-SUP-001 gains `own-service`** (line 156, SH-E-1c09bfc5). Shop's product reviews, as SH-50 placed them (kept). Kept.

## Entries I couldn't tell, placed where they most plainly belong

1. **The free themes (E21), `own-service`.** What would settle it: whether the coordinator reads a theme Shopify makes as a separate product (as CM-APP-011 reads Shopify's apps) or as the online store itself.
2. **'A new, uplifted visual design for the admin' (SH-E-f840803a), CM-ANL-003 `core`,** by its 'single-column layout for the home page' and its link to the admin's home. Its 'Improved settings system' names the admin's settings as a whole and takes no line (the ruling after SA-21). This is SH-51's case 3 again: if an admin-wide design names no capability, the entry is `out`.
3. **Markets Pro (SH-E-9e3f5c76), CM-MKS-003 `core;own-service`.** I placed it by its thing, a merchant of record for cross-border sales, which CM-MKS-003 is. What would settle it: a held statement joining Markets Pro to Managed Markets, and whether 'Our Merchant of Record capability' names Shopify as the merchant of record when the cell's other statements name Global-e.
4. **'Lead capture with Shop', powered by Klaviyo (SH-E-6d0e118e), CM-CUS-007 `own-service`, filler Klaviyo.** If 'Powered by' names Klaviyo as the one that does it, with no interface of the platform named, the line is `outside`. Either way the cell changes.
5. **Oxygen's log drains (SH-E-f0bed13e), CM-OPS-005 `extension-point`.** What would settle it: whether a headless storefront's runtime logs are 'the entries the store's logger records'. If not, the line is `new:Observability` with `shows`.
6. **Address validation by apps (SH-E-c6b4dbc1, SH-E-6242fae0), CM-CUS-009 `extension-point`.** CM-CUS-008's note keeps the order's shipping address out of it. CM-CUS-009, map and location services for addresses, holds Shopify's address autocompletion at checkout. If the coordinator keeps CM-CUS-009 to map services, the lines go, and CM-CHK-004, which both entries hold, carries the API.
7. **Shop's AI (SH-E-28190bfc), CM-AIA-005 `own-service`.** The card names 'AI-driven product recommendations' and 'personalized discovery'; only its link's label says 'AI shopping assistant'. If that is recommendations and not a chat, the line goes, and CM-CHN-002's `own-service` line carries the card. CM-MKT-023 holds recommendations on the store's own storefront, not Shop's.
8. **Shopify Credit, Collective and the Shop Pay Installments premium package (SH-E-1989a3fe, SH-E-bc95abcf, SH-E-7e14298b), `shows`,** for 'Currently available to select businesses in the United States' and 'Available to select businesses in the United States.' (E5), with their admin links ('Check eligibility') in `reading`. If 'select businesses' with an admin link reads as offered, they become `core` with the United States as scope; their cells already hold `core`.
9. **The Help Center's AI assistant (SH-E-123639b0), CM-ONB-003 alone.** CM-AIA-001 and CM-AIA-002 hold AI in the admin, not the help center.
10. **The App Store's AI review summaries (SH-E-c68fccbf), CM-APP-002 alone.** CM-AIA-003 is text written for the merchant's own store (descriptions, blog posts, SEO fields), not summaries of app reviews for the merchant to read.
11. **POS's longer PINs (SH-E-500cc746), on CM-POS-001 as `shows`** ('Currently available to select businesses.'). No capability holds a POS staff PIN: CM-TRU-001 is the admin's sign-in.
12. **POS access granted to staff (SH-E-500cc746), CM-STF-002 `core`, scope Shopify Plus.** The cardBody's 'grant permissions' and the item's 'Grant POS access to staff from the Shopify Plus admin' are the owner managing the staff's access, which CM-STF-002 keeps (the brief's rule on permissions over the staff's permissions).
13. **Shopify Inbox's maker.** CM-SUP-004's cell holds the Inbox app's Google Play publisher, Shopify Inc. (SH-S-2758). Under M-1 a cell's own maker evidence counts, which would make the Inbox lines of SH-E-07f9f89e, SH-E-07fdefcc and SH-E-009f5eab `own-service`. I kept SH-50's `core` (its E12.3, the admin address `inbox/…`) and the ruling after SH-36 (a card naming the app with no maker stated). The cell holds both.

## Structures whose items and sources disagree, or leave things out

- **Featured repeats collection cards under handles of its own** (`-featured`), and those are separate entries: SH-E-07f9f89e and SH-E-07fdefcc (Shopify Magic), SH-E-9aadaf11 and SH-E-5b24cf1e (Sidekick), and SH-E-f439781a and SH-E-76ec33a4 (Marketplace Connect). Featured's SH-E-bc95abcf (Collective) and SH-E-e06df061 (B2B) repeat cards that later batches hold (`shopify-collective`, and B2B selling's volume pricing, quick order lists, PayPal and vaulted cards). Each is placed by its own words, and the pairs in this batch take the same lines. Nothing is lost.
- **The rendered page holds 2 of Summer '23's 143 dialog descriptions** (the register). The dialog text is the page data's only, and it governs (E25).
- **No other disagreement found.** The items match the page data at each locator.

## What the sources state that no entry holds (for the second stage)

- **The collections' descriptions** (`displayCollections[N].description`, `items.jsonl` line 5):
  - AI for commerce: 'Shopify Magic combines cutting-edge AI with our platform's data to help millions of businesses work faster, smarter, and more creatively.';
  - Sell to every customer: 'a fully integrated POS', a lead for E12.1, as Winter '23's 'Fully integrated in-person selling';
  - World's best checkout: 'our world-class checkout that's accelerated with Shop Pay, new one-page checkout, and integrated extensibility platform';
  - App development: 'Shopify is the platform for builders.'
- **The hero** (`heroProps`): 'Shopify Editions Summer ’23', 'With 100+ product updates, you can be more productive, creative, and powerful in commerce than you ever imagined.'
- **The page's own AI chat** (`aiChatContentProps`): 'Search for products, features or updates in this Edition like', 'Search or ask a question'. It is an AI search of the edition's updates on the platform's own news page: a lead for CM-ONB-003 or CM-AIA-001.
- **`bundleCollections`:** one collection, 'Modal bundle - Marketing Tools', with no products.
- **Leads no line takes,** each a homonym or named in passing:
  - CM-LOY-003 (cashback, holds nothing on Shopify): Shopify Credit's 'cashback rewards' are the merchant's, on its card (SH-E-1989a3fe);
  - CM-CAT-005 (brands, holds nothing), the checker's first lead for Collective: 'Shopify brands' are merchants (SH-E-bc95abcf);
  - CM-TRU-004 (bot protection at checkout): 'The Storefront API is protected against bot activity' (SH-E-f9dd4a20), the API's and not the checkout's;
  - CM-MKT-023: Shop's 'AI-driven product recommendations' (SH-E-28190bfc), in Shop and not on the store's storefront;
  - shoppable videos from Tolstoy (SH-E-ee1a4e53): no capability holds shoppable video (CM-CAT-007 is product media);
  - CM-ACC-003 (organizations): 'multiple stores within a Shopify Plus organization' (SH-E-e18a17fc) and the POS staff tools' 'organization settings' (SH-E-500cc746), named as where;
  - CM-APP-009 (custom apps): 'build and deploy custom apps with server-side validation logic' (SH-E-e241d35a), the validation's vehicle;
  - CM-CHK-008 (quick checkout): 'other accelerated checkouts' (SH-E-3739d728);
  - CM-LOY-004: 'loyalty programs' among the apps a theme shows beside the cart (SH-E-8ca9faf9), a list;
  - CM-INV-001: the bundle apps' 'real-time inventory syncing for oversell protection' (SH-E-1d272a37);
  - CM-SHP-007: 'pickup dates, times, and instructions', examples of delivery options (SH-E-29b483a1).

## Problems with the brief or the script

- **`held_entries.py earlier` printed no earlier line for any of the 82 entries.** No batch had placed Summer '23, and Winter '23's last heading names an item by words the item's own heading doesn't hold ('Introducing Commerce Components'). SH-51's E18 mapping by heading settled it.
- **The checker doesn't find a quote across a link's markup in a dialog's text** (E25). Eleven quotes were requoted piece by piece.
- **The checker's brand note fired on 23 `core` lines.** Each line's reading names the words that place it: the ruling after SH-36 for a card naming an app with no maker (Shopify Magic, Inbox, Email, Subscriptions), E3 for the platform's own checkout, App Store, Markets, Functions, help center and POS, and M-10 for the admin's page for an app.
- **`show`'s leads were mostly names' words** ('by name: commerce, product'), as SH-50 found. The useful ones were by identifier: shopify inbox, shop pay installments, admin.shopify.com/apps/shopify-marketplace-connect, pos ui extension.

## Where B-extent and the brief differ

None I relied on. E24 is a reading within B-extent's convention on the platform's own API.

## The coordinator's check (31 October 2026, after the batch)

- **The cell changes stand, but the themes'.** Each was read again:
  - **CM-SEL-006, CM-SFR-013 and CM-MKT-023:** `own-service`, from 'our new, free bundles app' and Search & Discovery's 'We’ve also made it easier…' (the ruling after SH-53).
  - **CM-AIA-005 and CM-CUS-007:** `own-service`, for Shop's things. Klaviyo is the lead capture's filler.
  - **CM-MKS-003:** `own-service`, from 'Our Merchant of Record capability', beside the cell's Global-e `outside`. Both are what the sources say.
  - **CM-OPS-005, CM-CUS-009 and CM-API-001:** gain `extension-point`.
  - **CM-ORD-008:** `core`.
  - **The four repeats** of SH-50's and SH-51's changes stand as they did.
- **Corrected:** 'Our free themes' and their announcement bar are `core` on CM-SFR-001 and CM-SFR-007, not `own-service`. The ruling after SH-53 overturns E21. Four lines are changed.
- **The other new rules stand for SH-54 to SH-67:** E19, E20, E22 (POS the platform's own client, its devices `own-service`), E23, E24 and E25.
- **New things:**
  - Commerce Components by Shopify, again;
  - Quick order lists. A later card's `b2b-quick-order-lists` takes the same name;
  - Staff sales attribution, again;
  - App versions.
- **Cost:** 12.8 million tokens over 59 requests, about 156,000 an entry.
