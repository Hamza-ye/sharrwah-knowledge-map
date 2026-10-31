# SH-50: Shopify's `editions-page-data`, its first batch (high)

**What the batch is.** 130 entries of `editions-page-data` (observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`):
- entries 1 to 10: the Editions index's `albumsData`, one album per edition, fall 2026 back to summer 2022 (line 1 of `items.jsonl`);
- entries 11 to 46: the Summer '22 Edition's merchant page, its six chapters (Find Customers to Scale and Build) (line 2);
- entries 47 to 63: the Summer '22 developer page, `/editions/summer2022/dev` (line 3);
- entries 64 to 130: 67 of the Winter '23 Edition's 136 solution items, from Boost conversion to Find & engage customers' 'Let shoppers manage orders and returns with new customer accounts' (line 4). SH-51 begins with the next item, 'Create tokengated experiences'.

**No batch had placed this structure before SH-50.** `held_entries.py earlier` prints no line on the entries' own keys. Its few hits are lines of SH-34 and SH-8, both unchecked, on keys such as `markets`, `checkout`, `functions`, `balance` and `metafields`. Those are feature ids, and the lines name other things. The changelog's first batch, SH-34, ran beside this one and isn't checked; I didn't wait for it. The coordinator's rulings after SH-34 and SH-8 were added to `review-H-rulings.md` while I worked, and I applied them:
- a preview the merchant can enable is `core`;
- Shop's own things are `own-service`;
- a second line on one capability is allowed under its own condition;
- what a post names in passing takes no line.

The brief's scope paragraph changed at the same time. Its new exception lets a thing under its own condition take its own scope.

**Count.** 226 lines:
- 217 lines on a capability and 9 `new` lines;
- every entry placed, none `out`;
- 121 entries only on capabilities, 3 only `new` (Linkpop, Sanity integration, Quantity rules), 6 on both.

## The rules these lines follow, for SH-51 to SH-67

These rules apply to every edition of the structure. The later editions carry other fields, and I surveyed their keys and values across all 1,608 entries so that the rules name them. Where a rule rests on a field I didn't meet in my own entries, the rule says so.

### E1. What an entry is, and what to read with it

- **An entry is one feature card of one edition's page.** Its edition is the page in `within`, and the reading names it ("the Winter '23 Edition"). Its section is in `within` too: summer 2022's chapter; winter 2024's `parentSection`; later editions' `within`.
- **Winter 2023's solution items carry no section in `within`** (only `editions-winter2023`). Take it from the locator's `solutions/N/collections/M`. The titles are the page's `nav.navPillSolutions`, `solutionTitleHtml` and `collectionTitles[M]`, which the rendered page shows (`structures/shopify/editions/www.shopify.com_editions_winter2023/items.jsonl`, lines 73 to 112). Read each item with its solution and collection, as rule 1 reads a list item with its heading. Winter 2023's `productList` entries do carry both in `within`.
- **The card's own words:**
  - the title: `heading`, `title`, `cardTitle`, `headlineTitle`, `shortTitle`;
  - the subheading;
  - the description: `body`, `bodyHtml`, `description`, `descriptionHtml`, `cardBody`, `richText`, `content`;
  - the `highlights`, the `listItemsHtml` items and the `bodyLinks`;
  - the CTAs: `ctas`, `ctaTitle` and `ctaUrl`, `ctaAuthTitle` and `ctaAuthUrl`, `authenticatedCta*`, `signupCta`;
  - the tooltips (`headlineTooltip`) and the footnotes (`footnote`, `footNoteRichText`; a footnote is part of the entry, rule 1);
  - the `tags`;
  - the Dev Mode `tray`, the developer side of the feature, whose `heading` names it and whose `devModeSisterProductId` is the dev page's feature.
- **No statement:** `id`, `handle`, `socialShare` (it restates the card), `ariaLabel`, `iconName`, `cardType`, `modalType`, `excludeFromSearch`, `xxlCardRegistryHandle`, `textOnly`, `enterDevMode` and the media fields.
- **`eyebrow`, `productType` and `parentSection` group the card.** They say which product or part the feature belongs to, and they help find its capability. They give the card no line of their own, except where the card is a kind of what they name (M-6 refined).

### E2. The Editions index (`albumsData`)

- **Each album is one edition:** its `tagLine` ('Exponential'), its `description` and its `season`, `year` and `url`, with `isLive` in the reading.
- **Place it on CM-ONB-003 `core`, the term its `tagLine`.** An edition groups the platform's announcements of its features, 'Everything new across Shopify. Every six months.' (the index page's description, `raw/runs/20261030T162210Z-shopify-editions/fetch.warc.gz@1137`). So it goes where the changelog and its categories go (the ruling after SA-2 and SA-5; M-13).
- This is a reading. The ruling after SA-28 would put a title that groups several capabilities' pages `out`, and an edition groups several capabilities' features. I followed the changelog ruling because an edition is an issue of the platform's own news for merchants, as a changelog category is.

### E3. The feature's main line, read as a changelog post (rule 4)

The capability is the one the card's title and description name, read with its section. The support is what the card's words state:
- **`core`** where the card places the feature in the platform:
  - admin words: 'in your Shopify admin', 'built right in the Shopify admin', 'managed directly inside Shopify', 'from your admin', 'all within Shopify', 'built-in';
  - a link to an admin address that isn't an app's page (E7);
  - a plan statement ('available to all merchants on the Shopify plan and above');
  - or a description of the platform's own behaviour: 'We optimize your images', 'our system generates a description', 'now you can combine discounts', 'Choose from our four ready-to-use discounts'.

  The store's own checkout, Shop Pay, Shopify Payments, discounts, metafields, segments, the theme editor and the admin's mobile client (Shopify Mobile, whose routes the router serves to the native client) are the platform itself, not separate products. A card that names them supports `core`.
- **`own-service`** where the card, or a held statement, names Shopify the company as the maker or provider of a separate app, product or service:
  - 'a new app from Shopify';
  - 'Planet—An App From Shopify';
  - 'Shopify’s all-in-one creator management tool', with an App Store link;
  - 'our latest mobile point of sale (POS) device';
  - 'our creator platform' for Collabs, an app.

  'our' and 'we' on Shopify's own page are Shopify speaking, and I read them as a maker statement only where the thing is a separate app, product or device. Where the card calls the thing an app of Shopify's, it also takes CM-APP-011 `own-service` (M-6). The page's general 'everything that we’ve been building' (summer 2022's first paragraph) isn't a maker statement for each card.
- **Shop's things are `own-service`.** Shop is Shopify's own consumer app, and the ruling after SH-34 makes what it does `own-service`: the Shop Store and its customization; sign-in with Shop credentials and passkeys on Shop accounts; Shop Cash and its campaigns; Shop's product reviews; token-gating in the Shop App; the Shop channel's Shop Promise badge and delivery dates; chat on Shop. Shop Pay is the checkout's own (CM-PAY-014, `core`), not the Shop app.
- **The platform's own developer tools and APIs for its own features are `core`:** frameworks (Hydrogen, 'built by Shopify'), hosting (Oxygen), the CLI, docs, templates, the Prettier plugin and theme settings. CM-DVT-001's cell reads them so: a maker statement doesn't make them a separate product. They are `extension-point` where the card says apps, developers' apps or partners do the work: 'build apps that…', 'Publish pixels using Web Pixels Extensions', 'Deliver analytical experiences for your clients', 'Deliver more robust app offerings to the businesses you work with', 'Apps can now use metafields'. A card can state both, as Functions does: 'configure them in the Shopify admin' (`core`), 'lets developers build apps' (`extension-point`). Write `core;extension-point` on one line.
- **`extension-point`:**
  - a third party's app, or one with no maker named, that the card names as doing the feature: 'Install the Twitter App.' (apps.shopify.com/twitter);
  - an App Store category or collection the card links ('Explore discount apps', 'Explore checkout apps');
  - apps the card says provide it ('pre-orders, subscriptions, and “try before you buy” apps'; 'B2B-compatible apps'; 'partner apps Foursixty and Supergreat');
  - third parties' platforms building on the platform's APIs (Marketplace Kit).
- **`outside`:** a third party doing it with no interface of the platform. None in this batch: Flexport's logistics was announced as being built, so it is `shows`.
- **`shows`:**
  - a release marker of not-yet or limited availability (E5);
  - a separate product or service named by its brand alone, which names no maker, and placed in no admin, plan or app by the card: the Summer '22 Shopify Point of Sale card, Shopify POS hardware, Shopify Fulfillment Network, Shopify Capital, the Shop Promise badge of summer 2022, Tokengated Commerce's store side (B-extent: 'A product's name that carries the platform's brand doesn't name its maker');
  - a Shopify-branded app at an app's address with no maker in the card: Search & Discovery, Translate & Adapt, Shopify Forms, Shopify Email at `apps/shopify-email`, Shopify Audiences in winter 2023, Shopify Flow named as an alternative (M-10);
  - a topic or a claim alone.

  The checker's NOTE 'core on a product named with the platform's brand' asks this question of every `core` line whose terms carry the brand. I kept `core` only where E3's first point holds, and each such line's reading names the words that place it.

### E4. Second things: highlights, list items, the tray, tags and links

- **A highlight, list item or tray that names a feature of its own takes a line** on that feature's capability, with its own support from its own words (rule 2). Examples: POS's 'Tap to Pay on iPhone (US only)'; Markets' 'Set price lists and domains by market'; the B2B card's 'Set wholesale pricing and net terms'; the Admin Enhancements highlights; a tray's Pixels, Return APIs or App-Owned Metafields.
- **A highlight that is a claim takes no line:** 'High conversion rates, better performing ads', 'Simple, all-in-one pricing'.
- **A list of what may be used, added or customized takes no line** (the rulings after SA-41 and after SH-34). It is often introduced by 'like', 'such as' or 'things like'. Examples: Flow's tasks; what checkout apps may add; Functions' discounts, shipping and payment; Shop's re-engagement tools (the card's highlights repeat that list); the B2B APIs' example uses; Checkout Extensibility's list of tools. The card's own thing takes the line.
- **One line per capability per entry.** Where an entry states two supports of one capability, write both on that line (`core;extension-point`, `core;shows`). A second line on the same capability is only for a thing under its own condition or with its own filler (the ruling after SH-34). Examples: Shop's own product reviews (`own-service`) beside Supergreat's video reviews (`extension-point`, filler Supergreat); Inbox's Instagram chat (filler Instagram) beside Shop's chat.
- **Tags.**
  - 'Shopify Plus exclusive' is a plan condition, the scope (E6).
  - Every other tag names a topic and gives no line or scope: 'Enterprise', 'Holiday selling', 'Developer updates', 'B2B', 'AI', 'Shop app' and the rest. I counted 34 distinct tags over the structure.
- **A container or section** (a chapter, a solution or collection, `parentSection`, `eyebrow`) is the words the card is read with, not an entry. None of them is an entry in this structure.

### E5. Coming, beta, early access, waitlist, preview, limited

- **`shows`**, the words in `reading`, where the card states the feature isn't yet offered to every store:
  - 'Coming soon', 'soon', 'This year, we’re rolling out', 'will', 'upcoming beta';
  - 'Sign up for early access', 'Sign up to be considered for early access', 'Join the waitlist', 'Sign up to be notified', a CTA typed `beta`;
  - 'We’re building', 'planned acquisition';
  - a developer preview: 'Now in Developer Preview', 'Sign up for developer preview'. The brief reads dev-store previews as `shows`.
- **A preview the merchant can turn on now is `core`,** with its plans as its scope, its preview and release date in `reading` (the ruling after SH-34, 'Feature test drives').
- **'Now available', 'new', 'now' and 'Finally—now you can'** are release markers in `reading`. The support is the one the words give.
- **A card in a collection whose lead card states the limit inherits it.** Winter 2023's Managed Markets cards (entries 100 to 102) name the Managed Markets carrier account, its duties and its localization. They are read with their collection's first card, 'Introducing Managed Markets', 'Join the waitlist': `shows`. This is a reading.
- **Where a card has an early-access link and an admin link too,** give each part its support on one line (`core;shows`). Order routing (entry 98): the rules at `admin.shopify.com/settings/shipping` are `core`; the market-specific routing behind 'Sign up for early access' is `shows`.
- **Where the merchant page and the dev page read differently,** each is placed by its own words. Checkout Extensibility's merchant card says 'Shopify Plus merchants can now customize their checkout using apps' and is `extension-point`, with the tray's 'Now in Developer Preview' in `reading`. The dev card says 'Deploy exclusively for Plus merchants…' and is `extension-point`, with the preview in `reading`. Data Protection's merchant card is `core` on its present tense, 'Take control over which apps access customers' personal data'. The dev card's only statement is 'APIs will redact…', so it is `shows`.

### E6. Scope

- **A plan.** `plusExclusive: true`, which the summer 2022 merchant page renders as 'Shopify Plus exclusive' (`raw/runs/20261030T162210Z-shopify-editions/fetch.warc.gz@16179`). Also the tag 'Shopify Plus exclusive' and a text's 'Exclusive to Shopify Plus.', 'Exclusive to Plus.', 'Exclusive to POS Pro.', 'Shopify Plus merchants', 'available to all merchants on the Shopify plan and above', 'available on all plans in the US and Canada'. Write the plan in the source's words: Shopify Plus, Plus, POS Pro, the Shopify plan and above. The summer 2022 dev page carries `plusExclusive: true` (B2B, ShopifyQL, Checkout Extensibility) and doesn't render it. I took it as the scope, since the page's data states it for the feature and the merchant page renders the same feature's flag; each line says so.
- **A country:** 'Only available in the United States.', 'in France and the UK', 'now including Singapore and Finland', '(US only)', 'for US customers'.
- **An entry's lines share the scope**, except where a highlight states its own condition for its own thing. Then that line takes it (the brief's exception as changed after SH-34, extended here to a thing of another capability): Tap to Pay 'US' (entry 18); free fraud protection 'US customers' (entry 22). The checker accepts it.
- **Not a scope:** 'Enterprise' and the other tags; a market's or section's name; a link's address.

### E7. Links

- **A CTA's generic label names no thing:** 'Learn more', 'Read the blog', 'See it in action', 'Read documentation', 'Read help doc', 'Read dev docs', 'Join Discord', 'Try it now'. Its address tells where the feature is, and nothing else.
- **An admin address** (admin.shopify.com/<path>, including the `authenticated` and `ctaAuth` CTAs) places the feature in the admin: `core` on the feature's capability. Examples: `settings/checkout`, `discounts`, `settings/markets`, `settings/shipping`, `settings/payment_reminders` (the router's own route payment-reminders, 'Payment reminders', section Orders), `marketing/automations/templates`, `customers`, `settings/customer_accounts`, `inbox/integrations`. `settings/channels/install_shop_channel` opens the Shop channel, which is Shop's (E3).
- **An app's page in the admin** (admin.shopify.com/apps/<handle>) takes a CM-APP-007 `core` line, as the admin's page for an app (M-10; the ruling after SA-19). The app's own thing takes the support E3 gives it. This applied to 11 entries. The checker flags only the address with `embedded` in it, and I gave the line to all 11 alike. POS's `apps/point-of-sale-channel` is CM-POS-001's page too (CM-PAY-021's reading).
- **An App Store address** (apps.shopify.com/<handle>) says the feature is an app, and names no maker. An App Store category or collection address is the platform's list of third parties' apps (`extension-point`, M-3, M-7).
- **A help-center or shopify.dev address** clarifies which feature a highlight names. Cite it in the reading: the Bulk editor tool's link is `productivity-tools/bulk-editing`.
- **A linked page outside the entry's sources** (a marketing page, a blog post) isn't read (rule 1's list).

### E8. Partners, third parties, fillers

- **A filler is a third party the card's words name as doing the thing, or its venue (M-3):**
  - Twitter;
  - Twitter, Tik Tok and Spotify (the Marketplace Kit's users);
  - Google (local inventory sync);
  - Facebook, Google and Pinterest (the audiences' ad platforms);
  - YouTube, Roku, Sanity, PayPal, Instagram, Foursixty, Supergreat and Flexport;
  - Visa (the network where Balance's card works);
  - Prettier (the formatter Shopify's plugin extends).
- **Channels named in passing aren't fillers:** 'like Google, Facebook, and Instagram' for channel discounts.
- **No company of the group is a filler.** Deliverr's acquisition was 'planned', so no held statement places it in the group, and it goes in `reading`.
- **A partner's permissions are `shows`** (the ruling on the dry run's S7), and the staff's are `core`: 'New staff and partner permissions' took both lines.

### E9. Qualities

A quality is a limit, a duration, a price or fee, an infrastructure size or a count the card states, in its words:
- 'execute in under 5 milliseconds';
- 'free storage for six months per item';
- 'verified 2-day delivery';
- '270 points of presence around the world';
- 'more than 1,000 retail locations from a single store';
- 'any of our 15 markets';
- 'automatically translate up to two languages completely free';
- 'Only pay for successful sales', 'pay no monthly fees', 'free'.

A conversion or speed claim ('70% higher checkout-to-order rate', '4X faster', 'up to 40% higher conversion rates', 'increase conversion by up to 25%') is the platform's claim, not a quality.

### E10. The same feature in two pages or editions

- **Each entry is placed by its own words and its edition's date,** and neither changes the other. Earlier and later cards keep the same `cap_id` and terms, so the coordinator can join them. A feature an earlier edition announced as coming takes `shows` there. A later edition's 'now available' takes the support its own words give. The cell holds both.
- **Within summer 2022,** the merchant page's tray is the dev page's card (`devModeSisterProductId`). Both took the same capability: Built for Shopify, Functions, Checkout Extensibility, Pre-orders, B2B, ShopifyQL, Data Protection, Hydrogen, Pixels, Marketplace Kit, App-Owned Metafields, Liquid, Embedded App Improvements and Return APIs.
- **Winter 2023 lists each feature twice:** as a solution item (`solutions/N/…/items`, 126 entries) and as a heading of its Product list (`productList/solutions/N/collections/M/products`, 122 entries, all after SH-50). The Product list entry 'One-page checkout' is the solution item 'One-page checkout' (SH-E-96784169). The Product list's 'Storefront Renderer' names the 'Lightning-fast page loads' item's infrastructure, whose link is `/partners/blog/storefront-renderer` (SH-E-df3b3c3a).
  - A Product list entry takes the capability of the item it names, in the same collection.
  - A bare heading supports only what its words state, read with its collection (rule 4's titles).
  - A heading that names a product no item names is placed by its own words.

### E11. `out`

- **No feature card is `out`.** Each states a feature, a programme or a release.
- **An entry would be `out`** only where it states no feature: a decorative card, a stat card's bare number, a demo or easter-egg label ('emoji-easter-egg'), a sign-up form's 'By signing up, you agree to receive marketing emails from Shopify' (a UI string), a video card with no feature words. Say why in `reading`.

### E12. Cases I couldn't settle, placed where they most plainly belong

1. **POS in summer 2022 (entry 18) against winter 2023 (entries 88 to 93).**
   - Summer '22's card names Shopify Point of Sale by its brand only. I placed it `shows`, with its Tap to Pay, hardware, Google sync, locations and metafields.
   - Winter '23's cards sit in the collection 'Fully integrated in-person selling', and one links the admin's POS app page. I placed them `core` (POS Go `own-service`, 'our … device').
   - What would settle it: whether a collection title's 'integrated' places POS's features in the platform, or POS is a separate app whose features are `shows` without a maker statement. The model's CM-POS-001 is `core` on its plan rows, so neither changes the cell.
2. **Tokengated Commerce (entry 26), `own-service;shows`.** The store side names a product by its brand alone. 'Tokengate in your store or Shop App' gives Shop's part. It changes CM-SEL-003, whose `extension-point` rests on the admin's `nft-application` route.
3. **Shopify Inbox (entry 127), `core`.** Its link is `admin.shopify.com/inbox/integrations`, not under `apps/`, but the admin router held doesn't hold an `inbox` route, and the card also links `apps.shopify.com/inbox`. If `/inbox` is the app's page, the line is `shows` with a CM-APP-007 line.
4. **Shopify Payments in France (entry 86), `core`.** The card names no admin place. I read Shopify Payments as the store's own payment service ('Set up Shopify Payments'), as CM-PAY-002 holds it, not as a separate product.
5. **Shopify Email (entries 31, 125, 126).**
   - Entry 31 is `core` on 'all within Shopify'.
   - Entries 125 and 126 are `shows` at the app's address.
   - The model's CM-MKT-007 holds `email/create` and plan lines as `core`, so a later batch should keep to E3: the card's own words decide.
6. **Hydrogen 'built by Shopify' (entries 25, 58), `core`.** E3: the platform's own developer framework. If the coordinator reads a framework as a separate product, the maker statement makes it `own-service` on CM-SFR-011.
7. **Quotes (entry 111).** 'Give your customers the opportunity to request a quote online', with checkout to draft, makes CM-B2B-004 `core`. CM-B2B-004's grain is BigCommerce's Quotes, so the coordinator should confirm that checkout to draft is that thing.
8. **Try before you buy.** I made it `new`. CM-PAY-015 holds 'the buyer pays for an order later' and its terms include 'deferred payment', but its thing is a payment method (BNPL providers). Try before you buy is a purchase option, a selling plan the merchant charges after the trial. If the coordinator joins them, the three lines move to CM-PAY-015.

## New things

Each has no place of its own in its entries: one page states it, with no admin route, API group, plan line or App Store category named. So each is `shows` (rule 2's new). Shopify's Editions are in English only: no Arabic name is held.

| New thing | Entries | Proposed domain, area, parent | Terms searched (`caps --terms`) | Leads read |
| --- | --- | --- | --- | --- |
| Linkpop: a free link-in-bio page, 'powered by Shopify’s fast and secure checkout' | SH-E-c42cc511 | E, CHN, under CM-CHN-001 (a selling page for social bios) | link in bio; social media bio; linkpop | CM-CAT-007, CM-PTN-010, CM-DVT-001, CM-SFR-016: none holds it |
| Try before you buy: the buyer pays after trying, through selling plans and apps | SH-E-f30da721, SH-E-fe6f6586, SH-E-73189988 | B, SEL, beside CM-SEL-005 (or CM-PAY-015, E12.8) | pre-order; try before you buy; selling plan; purchase option; deposit; deferred payment | CM-SEL-001, CM-SEL-005, CM-PAY-015; the App Store category the card links (`merchandising-purchase-options`) holds pre-orders, subscriptions and it together |
| Planet: carbon-neutral delivery, 'Planet—An App From Shopify' (maker on CM-APP-011's line) | SH-E-bc581483 | C, SHP, under CM-SHP-001 | carbon; sustainab; climate; offset | CM-SHP-018, CM-SHP-022, CM-B2B-007, CM-SFR-012: none |
| Sanity integration: a third party's content system connected to the Online Store through an app (filler Sanity) | SH-E-64bfaaff | E, CNT, near CM-CNT-003 | sanity; CMS; content management | CM-CNT-003 (store pages), CM-ANL-003, CM-APP-010: none holds outside content |
| Tipping: buyers' tips at the point of sale, in the Customer View app | SH-E-f70f18b8 | E, POS, under CM-POS-001 | custom line; smart grid; tipping; tip; receipt | CM-POS-001, CM-POS-004, CM-PAY-021: none. Shopify's checkout tipping settings aren't in this entry |
| Staff sales attribution: sales credited to the staff who made them | SH-E-ada073f2 | A, STF, under CM-STF-001 | staff attribution; sales attribution; pos staff | CM-MKT-008 (credits orders to marketing: a homonym), CM-STF-004 (staff targets): neither |
| Quantity rules: minimums, maximums, case packs and increments per product and variant, by customer | SH-E-18baf046 | D, B2B, under CM-B2B-003 (its help link is `b2b/catalogs`) | minimum quantity; maximum quantity; increment; purchase limit; quantity limit | CM-CAT-002, CM-INV-004, CM-CHK-005 (app-written rules), CM-ORD-010: none |

## The CHANGES lines, and what I decided on each

Each line was read again against its source.
- **CM-MKT-011 gains `own-service`** (SH-E-234dcbd7): 'Shopify Audiences is a new app from Shopify'. This is the maker statement the cell's gap says is missing. Kept.
- **CM-ANL-006 gains `extension-point`** (SH-E-6aa48f41's tray, SH-E-c4e3578b): 'Deliver analytical experiences for your clients… The GraphQL Admin API allows you to directly query Shopify’s analytical data', and 'Analyze data and generate insights straight from your app'. The API's statements say apps and partners do the work (B-extent's convention). Kept.
- **CM-MKT-023 becomes held and gains `core`** (SH-E-760fb2b3, with the `shows` of SH-E-a59f92d9 and SH-E-76ffcf8d): 'Better built-in search and recommendations', 'Powered by data across Shopify, now product recommendations offer suggestions'. The platform's own recommendations to buyers on the storefront. Kept.
- **CM-ORD-014 becomes held and gains `core`** (SH-E-8581ba3f): 'Easy reordering', 'making it easy for customers to reorder their favorite products', linking customer accounts. A past order repeated, not CM-LOY-007's reminders nor CM-B2B-005's lists (its note). Kept.
- **CM-B2B-004 gains `core`** (SH-E-973068eb): 'Give your customers the opportunity to request a quote online', with checkout to draft. Kept, with E12.7.
- **CM-B2B-001 gains `extension-point`** (SH-E-6a5ae693): 'Or customize your experience with B2B-compatible apps.' Kept.
- **CM-CHN-002 gains `extension-point`** (SH-E-e700f282): 'Use partner apps Foursixty and Supergreat to host shoppable brand content and video reviews' on the Shop Store. Third parties' apps on Shop. Kept.
- **CM-CUS-010 gains `own-service`** (SH-E-46f1bc0c, SH-E-2692bb65): sign-in with Shop credentials and passkeys on Shop accounts. The ruling after SH-34 names one-tap sign-in among Shop's own things. Kept.
- **CM-SEL-003 gains `own-service`** (SH-E-c552e10f): 'Tokengate in your store or Shop App'. Shop's part. Kept, with E12.2.
- **CM-SHP-018 gains `own-service`** (SH-E-cb5e7062): the Shop Promise badge and delivery dates come 'by installing the Shop channel', with 'smart delivery dates predicted by Shopify that are backed by a limited guarantee'. Kept.
- **CM-SUP-001 gains `own-service`** (SH-E-e700f282): 'Use product reviews…' on the Shop Store, Shop's own (the ruling after SH-34). It agrees with the cell's 'Shop product reviews', there `shows`. Kept.
- **Withdrawn while working:** CM-SFR-011 `own-service` (Hydrogen, E3, E12.6). Not written: CM-SEL-005 `core` for 'Pre-orders and try-before-you-buy now support PayPal' (SH-E-73189988). The card says who accepts the payment, not who provides the pre-orders, so it is `shows` there and `core` on PayPal (CM-PAY-013).

## Structures whose items and sources disagree, or leave things out

- **Winter 2023's solution items carry no section or collection in `within`.** The item's pointer and the page's `nav` hold them (E1). The Product list's entries carry them. Its collection titles differ slightly from the nav's: 'The world’s best checkout keeps getting better' against 'gets even better'.
- **Summer 2022's dev page carries `plusExclusive: true` and doesn't render it** (E6).
- **The rendered summer 2022 page repeats each card's text two or three times** (card and dialog). `merge:handle` makes one entry per feature, as the selection says, and nothing is lost.
- **The tray's text is in the page data only.** The rendered page shows only the button 'Explore more in Dev Mode' (`www.shopify.com_editions_summer2022/items.jsonl`, line 87). The source governs, and the tray is read as the feature's.

## What the sources state that no entry holds (for the second stage)

- **Summer 2022's first paragraph:** 'Welcome to Shopify Editions, where twice a year we show you everything that we’ve been building.' (`structures/shopify/editions/www.shopify.com_editions_summer2022/items.jsonl`, line 1; `fetch.warc.gz@16179`). It is a general statement of who builds the page's features. It is in the rendered page, which the held pass reads only for fall 2026.
- **Winter 2023's solution headers.** Each `solutionHeader.headingHtml` and `subhead` (line 4 of `items.jsonl`), such as Expand with B2B's 'Since launching 6 months ago, we’ve already improved B2B on Shopify with dozens of enhancements', and its video descriptions. The `hero.subheadHtml` too: 'Over 100 product updates to help businesses and developers build for the long-term'.
- **Winter 2023's `productNodeMap`,** the 'Product map' of 'Commerce Components' ('Navigate how the underlying technologies and components that power Shopify are associated to the product, features, and updates that we’ve shipped'). No entry holds it (`entries.tsv` has none). It is a lead for CM-API or the composable stack.
- **The summer 2022 chapters' subheadings,** such as 'Connect with high-value buyers and increase sales—on your own terms'. They are in the rendered page only.
- **Leads no line takes**, all named in passing:
  - CM-CHK-009 (custom fields at checkout, which holds nothing on Shopify): 'things like additional fields' that checkout apps add (SH-E-103a51c0);
  - CM-ORD-013 (order notes, which holds nothing): 'collecting order notes… at checkout' through the B2B APIs (SH-E-6a5ae693);
  - CM-MKT-021 (upsell): Shop's 'post-purchase offers' (SH-E-625ce071);
  - CM-TRU-008: 'Powered by data across Shopify' (SH-E-760fb2b3);
  - CM-ANL-003 or CM-ANL-001: Inbox's 'view live shopping activity in real time from your online store' (SH-E-7428d170).

## Problems with the brief or the script

- **The brief and the rulings changed during the batch** (the rulings after SH-34 and SH-8; the scope paragraph). I re-read their diff and applied them. Lines written before the change were revised to them: Shop Cash campaigns `own-service`, and POS and Shop under the Shop ruling.
- **The checker flags an app's embedded page only where its address holds `embedded`.** Of this batch's 11 links to admin.shopify.com/apps/<handle>, it flagged one. I gave all 11 the CM-APP-007 line (E7).
- **The checker's group note** ('names a company of the platform's group: own-service?') fires on 'Shopify' in Built for Shopify's words: 'a mission-critical goal at Shopify', 'Shopify’s new standards'. That is a programme of the platform, not a separate product of the company, so it stays `core;extension-point`.
- **`show`'s leads for this structure are mostly names' words** ('by name: growth, platform', 'customer, get'). Only the identifiers' leads (shopify audiences, shop app, payment terms) were useful. The checker's note on the fall 2026 album (its first lead CM-PTN-006, 'by name: growth, platform', holds nothing) is such a lead: the album names no agency programme.

## Where B-extent and the brief differ

None I relied on. E3's reading of the platform's own developer tools as `core`, even with a maker statement, follows the model's CM-DVT-001 reading ('none is needed for `core`'), not a rule of either brief. It is listed for the coordinator in E12.6.

## The coordinator's check (31 October 2026, after the batch)

- **The rules E1 to E12 stand for SH-51 to SH-67.** They agree with the rulings made while the batch ran. A feature the merchant can enable before its release is `core`, while one that is coming, in early access, on a waitlist or rolling out is `shows`.
- **The cell changes stand, each read again:**
  - CM-MKT-011 takes `own-service` from 'Shopify Audiences is a new app from Shopify', a maker statement;
  - CM-ANL-006, CM-B2B-001 and CM-CHN-002 gain `extension-point`;
  - CM-MKT-023 and CM-ORD-014 are held, `core`;
  - CM-B2B-004 gains `core`: a request for a quote, turned into a draft order, is the same thing as BigCommerce's Quotes;
  - Shop's things take `own-service` on CM-CUS-010, CM-SEL-003, CM-SHP-018 and CM-SUP-001, by the ruling after SH-34.
- **The two withdrawn changes stay withdrawn:**
  - Hydrogen is `core`, as CM-DVT-001 reads the platform's own developer tools;
  - PayPal for pre-orders is `core` on CM-PAY-013 and `shows` on CM-SEL-005.
- **New things,** decided in `held/new.tsv`: Linkpop, Try before you buy, Planet (with its CM-APP-011 `own-service` line), Sanity integration, Tipping, Staff sales attribution, Quantity rules.
- **Winter '23's Product list repeats each solution item.** It has 122 entries: 23 in SH-51, 98 in SH-52 and 1 in SH-53.
  - Each Product list entry takes the line of the item it names (the notes, under "the same feature on two pages").
  - `held_entries.py earlier` now reads a `heading:` field, so it prints the item's line in one call.
  - SH-52 runs once SH-51, which holds the rest of the solution items, is checked.
- **The eight open cases** (POS in Summer '22 against Winter '23, the Inbox address, Shopify Payments, Shopify Email, Hydrogen and the others) stand as placed, for the amendment.
- **Cost:** 32.4 million tokens over 112 requests, about 249,000 an entry.
