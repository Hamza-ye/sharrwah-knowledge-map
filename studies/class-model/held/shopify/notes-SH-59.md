# SH-59: notes

**The batch.** 80 entries of Shopify's `editions-page-data` (observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`):
- the Summer 2024 Edition (line 7): collection 13, Developer: Growth (6 cards, entries 1 to 6), and collection 14, Developer: Tools (1 card and 11 list items, entries 7 to 18);
- the Winter 2025 Edition (line 8): Online (17, entries 19 to 35), Retail (10, entries 36 to 45), Checkout (14, entries 46 to 59) and Marketing up to its 21st product (entries 60 to 80).

None of these collections has a description of its own (`descriptionHtml` is empty), so each card is read by its own words, its links and its section's title.

**What I read.** The brief; the digest `held/rules/editions-page-data.md`; the last section of `held/review-H-rulings.md`; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md` (its Published section: nothing on the Editions), `structures/README.md`, and the `REGISTER.tsv` rows for `shopify/editions` and `shopify/editions-page-data`; the selection row; B-extent's "Cells and evidence" and "Conventions from the dry run"; the evidence map's observed-sh section. From the batches' notes, only `notes-SH-57.md`'s E58 (lines 69 to 80), for the digest's rule 46 (a B2B card) and E58's 'such as' list (entry 29). Earlier lines were read through `earlier` and with `grep` of the placements on a feature's name: Built for Shopify, the App Store's ads, Flow's Run code, Functions, the Subscription APIs, Checkout Blocks (SH-58's SH-E-e65e8929 and SH-E-1efb0d23), Shopify Forms, Shop Campaigns, Tap to Pay, Shop Pay Installments and the Shop Pay Component (SH-58's SH-E-7ee1751d), and Inbox's suggested replies.

**Count.** 80 entries: 79 `capability` (128 lines), 1 `out` (the Boring t-shirt, entry 59), no `new`. By support, the 128 lines are:
- `core` 73;
- `own-service` 31;
- `extension-point` 13;
- `core;extension-point` 6;
- `shows` 3;
- `core;shows` 1;
- `core;own-service` 1.

## New things

None. Each thing the entries name is held by a capability, as the cells' readings show. The two nearest to a new thing:
- **Split shipping** (entry 57, SH-E-89750b1d): no capability names it. Its card links help.shopify.com's `checkout-settings/split-shipping` and the admin's `settings/shipping`, the store's shipping settings. A help page isn't a place of its own, so it is placed on CM-SHP-001 `core`, by its settings page. Terms searched: 'split shipping; multiple shipments; ship separately; multiple shipping rates'. A route or settings section of its own in the admin router would make it a capability.
- **The App Store's search ads for developers** (entries 1 and 6: 'search ad targeting', the 'ads metrics dashboard'): no capability holds them. CM-MKT-010 is the merchant's advertising. SH-53 placed the App Store's geotargeted ads on CM-APP-002 (SH-E-a9161e4a), and I kept to it. Terms searched: 'app store ads; app ads; advertis; search ad'.

## Rules I followed that the digest doesn't hold (E59)

- **E59.1. The Winter 2025 page's summary.** Collection 0, Top updates (`isSummary: true`, no products), is a list of what the edition calls its top updates. Each item names cards by their anchors.
  - Where it says 'We're rolling out' a card's feature, the card is `shows` (rule 32), even where the card's own words state no limit. The features named so are Sidekick (#sidekick-rolling-out), Markets (#markets-rolling-out-soon), the new analytics (#new-analytics-rolling-out) and customer account extensions (#customer-account-extensions).
  - In this batch that makes Customer account extensions (entry 60) CM-CUS-014 `shows`. Its own words, 'Personalize customer accounts without code using apps', would make it `extension-point`. Markets (entry 29) is `shows` by its own words too.
  - Its other items ('Draft orders work with functions, bundles, and checkout extensions'; 'We've increased loading speeds across cart and checkout and the admin') state nothing the cards don't.
  - The summary is a heading with no products, so it goes to the second stage (rule 37). The coordinator may prefer to read a rollout only from a card's own words. If so, entry 60 is `extension-point`.
- **E59.2. The App Store's features for developers are CM-APP-002's** (Built for Shopify's criteria and search filter, the search ads and their metrics, app review, the app taxonomy).
  - They are `core` where the thing is the platform's own tool or review: app review (as the cell reads SH-S-0698) and the ads' metrics dashboard.
  - They are `core;extension-point` where third parties' apps are marked, filtered or matched: Built for Shopify, its filter, ad targeting and the taxonomy. This follows SH-41, SH-50, SH-51 and SH-53.
  - Managing an app's pricing in the Partner Dashboard is CM-APP-003 `core`, as the cell reads 'plans, usage pricing and free trials set in the Partner Dashboard'.
  - Speed figures ('30% faster', 'reduced latency by 50%', 'up to 58.8% faster') are claims (rule 55).
- **E59.3. Functions' developer tools.**
  - The tools are the platform's: CLI commands go on CM-DVT-002 (logs and replay) and libraries on CM-DVT-001. Both are `core`, and the libraries are `core;shows` because 'soon JavaScript' is a coming state (rule 32).
  - The card's Functions line (rule 41) is CM-APP-005 `extension-point`, for apps' functions.
  - Where the card states the platform's own running of functions, CM-APP-005 is `core;extension-point`: batch execution, the merchant's sharing of Function logs (entry 13), and functions applied to draft orders (entry 53).
- **E59.4. The Subscription API's billing-attempt error codes** (entry 18, 'New error codes for subscription billing') are CM-SEL-001 `extension-point`.
  - The cell's reading says subscription apps build on that API, and the earlier batches placed the Subscription APIs so (SH-E-7a77cb5d, SH-E-b229dc80).
  - The digest's rule 18 says an API is `core` unless its words say apps do the work. B-extent says "the API's statements", and the held statements on this API say apps use it, so B-extent governs.
  - The card's title, 'Detailed cart errors', is narrowed by its words to subscription billing (B-extent: the description governs). So CM-CHK-002 takes no line.
- **E59.5. Marketing automations powered by Flow.** 'All marketing automation templates are now powered by Shopify Flow' (entry 70) makes the store's marketing automations Flow's. So CM-MKT-006 is `own-service` beside Flow's CM-AUT-001 `own-service`, for entries 69 and 70. CM-MKT-006's plan line, Create marketing automations, stays `core`. Entry 69's title is 'Marketing automation with segments', so it takes the CM-MKT-006 line too.
- **E59.6. 'X works with Y'.** Where a card's title or own sentence names both things, each takes its line:
  - 'Bundles work with POS', 'Shopify POS now supports Shopify Bundles' (entry 38): CM-SEL-006 and CM-POS-001;
  - 'Extensions work with draft orders' (52) and 'Functions work with draft orders' (53): CM-CHK-004 or CM-APP-005, and CM-ORD-005.

  A thing a description names only as supported takes no line (rule 51). The case is the accelerated checkout buttons' 'and support functions and bundles' (entry 50).
- **E59.7. Search & Discovery's product recommendations.** 'Choose if parent or child products should appear in search and product recommendations with' Search & Discovery (entry 19) puts the app's recommendations on CM-MKT-023 `own-service`, a cell that held nothing on Shopify. The combined listings are the products the setting governs, not the app's thing (rule 16), so CM-CAT-008 takes no line.
- **E59.8. The Shop Pay Component's features.**
  - The component itself is CM-PAY-014 `own-service`: Shop Pay apart from the platform (SH-53's E23).
  - A feature that comes with it is `own-service` on its own capability, scoped by the businesses the card names and the component, `US-based enterprise businesses and Shop Pay Component` (rules 27 and 28). In this batch that is Shop Pay Installments (entry 58), on CM-PAY-015.
  - The component's own line takes `US-based enterprise businesses`. SH-58's pickup line (SH-E-7ee1751d) took 'Commerce Components', which its card named. Mine doesn't name it, so no Commerce Components line.

## Entries I couldn't tell, and what would settle each

- **Entry 60** (SH-E-61794cc2): `shows` or `extension-point`, by E59.1. The coordinator's reading of the summary settles it.
- **Entry 30** (SH-E-a4fcd072, 'Reporting for bundles'): its 'metrics in the new analytics' name the new analytics, which the summary says 'We're rolling out'.
  - I kept CM-ANL-001 and CM-SEL-006 `core`. The summary names the new analytics' own card (#new-analytics-rolling-out, in a later batch), not this card.
  - If the coordinator reads a feature that rests on a rolling-out one as limited too, both lines are `shows`.
- **Entry 32** (SH-E-f853c446, 'Accurate bundle inventory'): its scope is `Managed Markets;fulfillable inventory`, from 'when using Managed Markets or fulfillable inventory'. What 'fulfillable inventory' is isn't stated in the entry. If it is one of the store's own inventory settings rather than a feature, it belongs in `reading`, not `scope`. The changelog post the card links would settle it.
- **Entry 36** (SH-E-fb331580, 'Unverified retail returns'): besides CM-RET-003, CM-RET-002 and CM-POS-001, I gave 'refund to a gift card' a CM-LOY-002 `core` line, the gift card being issued as the refund. If a refund's destination is only the refund's, the CM-LOY-002 line drops.
- **Entry 1** (SH-E-14e13b40): the search ad targeting is 'exclusive' to Built for Shopify apps. That is an app's standing, not a plan, store or account, so it is in `reading`, not `scope`.
- **Entry 71** (SH-E-3b1a8815): 'English only.' bounds the suggested replies' language. No scope rule covers a language, so it is in `reading`.
- **Entry 35** (SH-E-78a1e4eb, 'Returns in Shop'): placed `own-service` on CM-RET-003 and CM-CHN-002 by its words. Its links, apps.shopify.com/stories/guide-apps-in-shop and the Shop channel's install with `onboardingRedirect=minis`, suggest the returns may come through apps' Shop Minis. That would be `extension-point` (the digest's rule 11). The links only say where it is set up (rule 1), so they are in `reading`.
- **Entry 72** (SH-E-1993ae93, 'Shoppable ads on Roku'):
  - It is CM-MKT-010 `extension-point`, with Roku its venue and 'no additional fees or minimums' its quality.
  - Its 'analyze your ROI within Shopify' takes CM-MKT-005 `core`, as entry 64's marketing analytics dashboard does.
  - 'Turn your TV ads into shoppable experiences' is near SH-55's new thing Shoppable videos. I didn't use that name: these are ads on a third party's TV platform, not videos on the storefront.
- **Entry 7** (SH-E-f81055fc): its '.dev assistant' and 'more complete reference pages' take CM-DVT-001 `core`, by the digest's rule 50 (AI outside the admin goes on the place's capability). **Entry 9**'s 'references with sample payloads' takes the same line.

## Leads, for the coordinator and the second stage

- **CM-OPS-005** (Store logs, WooCommerce only so far) for 'Function logs', which merchants share with an app's developer (entry 13, SH-E-6256cac2; its help page help.shopify.com's `manual/apps/getting-support#sharing-function-logs`). These are the store's logs of an app's functions, which the platform records. I didn't place them there, since the cell's thing is the store's logger.
- **CM-MKT-023** (Product recommendations) for Shop's feed, which 'features personalized recommendations to engage app customers' (entry 80, SH-E-76b709c7). They are Shop's recommendations in its app, not the storefront's, so they stay in the CM-CHN-002 line.
- **CM-MKT-008** (Sales attribution) for Shopify Email's 'custom UTM parameters' that 'work with third-party reporting tools' (entry 63, SH-E-1382cfda). They stay in Shopify Email's CM-MKT-007 line.
- **The Winter 2025 summary, Top updates** (items.jsonl line 8, `collections[0]`): a heading with no products, for the second stage (rule 37). Its 'the admin' (#faster-loading-admin) is the admin's loading speed. That is the admin's own frame, no capability's thing (the digest's rule 49).
- **Twins in other batches:**
  - SH-58 holds Summer 2024's 'send-admin-api-in-flow' (Centralize operations), under another handle than entry 17's 'send-admin-api' (Developer: Tools). I placed entry 17 on CM-AUT-001 `own-service` and CM-APP-007 `core`.
  - SH-60 holds Winter 2025's Wholesale 'extensions-work-with-draft-orders-wholesale' and 'functions-work-with-draft-orders-wholesale', the twins of entries 52 and 53.
  - SH-58's Customer account extensions (SH-E-f5fe7487, CM-CUS-014 `shows`) is entry 60's twin by its label. I kept its `cap_id` and term (rule 4).

## The checker's notes, read again

- **Brand notes** ('core on a product named with the platform's brand'): each line is the platform's own client or tool: the Shopify App Store, the Shopify CLI, Shopify Functions and its libraries, and Shopify POS (the digest's rules 7, 9, 17 and 41). Line 38 is CM-SEL-001 `core;own-service`: its `core` is the admin's product details page and its `own-service` the Shopify Subscriptions app.
- **First leads that hold nothing:**
  - CM-OPS-004 (lines 10 and 17) is led only by the word 'tools', the section's name.
  - CM-API-013 (line 78) is led only by 'one', 'than'.

  Neither is a lead.

## Problems with the brief or the script

None that changed a placement.
- A card's anchor text can hold an HTML entity (`Shopify Search &amp; Discovery.`). I didn't quote such text: the app's name stands in my own words.
- The quotes I took from other entries name those entries' ids. They pass the checker, and so does the summary's 'We're rolling out', which isn't an entry.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 80 of 80 entries, no problem. Its `CHANGES` stand. Each rests on the digest's first-party table or on the rules below. CM-MKT-023 had already become held, from SH-78's plan line.
- **One line aligned:** POS Terminal's line (entry 62) is `own-service`, by the corrections with the changelog digest. A held post names its maker (SH-E-dbb979f6).
- **The rules E59.1 to E59.8 stand,** and go into the digest's section 6 as E69 to E76, since SH-58 had used E59 to E68:
  - **E69:** the summary's 'We're rolling out' makes its cards `shows`. The edition's own words state the rollout, so entry 60 stays `shows`.
  - **E70:** the App Store's developer features are CM-APP-002.
  - **E71:** Functions' developer tools are CM-DVT-001 and CM-DVT-002, and the card's Functions line is CM-APP-005.
  - **E72:** the Subscription API is `extension-point`, by its own statements (B-extent).
  - **E73:** Flow-powered marketing automations are `own-service`.
  - **E74:** in 'X works with Y', each thing takes its line.
  - **E75:** Search & Discovery's recommendations are CM-MKT-023 `own-service`.
  - **E76:** a Shop Pay Component feature takes its businesses and the component as its scope.
- **Cost:** 16.7 million tokens over 86 requests, about 209,000 an entry. The context reached about 340,000 tokens.
