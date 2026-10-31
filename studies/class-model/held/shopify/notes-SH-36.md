# SH-36: Shopify's merchant changelog, posts 261 to 390 (notes)

**The batch:** platform `shopify`, batch `SH-36`, effort `high`. Its 130 entries are posts 261 to 390 of `merchant-changelog` as `@posts` holds them: `structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl`, lines 261 to 390 (positions 260 to 389), at observed-sh `e38dc17e3`. They come from two runs:
- entries 1 to 45 (positions 260 to 304): 13 November 2025 back to 7 October 2025, the last posts of the run `20261007T071251Z-published-changelog-posts`;
- entries 46 to 130 (positions 305 to 389): the run `20261030T234414Z-merchant-changelog-feed-posts`. Entries 46 to 83 are its 38 posts of 29 October 2026 back to 8 October 2026; entries 84 to 130 are 47 posts of 3 October 2025 back to 20 August 2025. This is the order SH-34's notes describe.

**What I read:** the brief, and what it names:
- the evidence map;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, and its `REGISTER.tsv` row for `shopify/merchant-changelog`. The changelog has no ledger denominator: `index/ledger-summary.tsv` and the `shopify.com` sitemap ledgers hold no `changelog.shopify.com` row (the register: 'no sitemap: 404');
- `show --meta`, `selection.tsv`'s row (`placement` `where`) and `@posts/meta.json`;
- B-extent's "Cells and evidence" and its conventions, with "What a place of its own is";
- the coordinator's rulings, again at the end (unchanged during the batch);
- SH-34's and SH-35's notes with the coordinator's checks, and their placements, summed by capability and support.

`held_entries.py earlier` printed no line for any key of the batch, at the start and at the end. No placements of SH-37 to SH-46 existed when I finished.

**Counts:**
- 130 entries on 217 lines: 214 `capability` lines and 3 `new` lines, none `out`.
- By support: `core` 187, `extension-point` 11, `shows` 7, `own-service` 6, `core;extension-point` 3, `core;shows` 2, `core;own-service` 1.
- Lines per entry: 70 entries take one line, 40 two, 15 three, 3 four (SH-E-4b61c9b6, SH-E-80b85db9, SH-E-0ecae440) and 2 five (SH-E-5669dc6b, SH-E-3c35603a). In all they reach 99 capabilities and 3 new things.
- The checker's final line: `130 of 130 entries placed; 0 problems`.

## The rules my lines follow

I kept to SH-34's rules 1 to 14, SH-35's rules 1 to 10, and the rulings after SH-34 and SH-35. Every reading begins with the post's date and type tag, then its release words. Every quote is copied from the entry's own text, so none cites a record. Where the quoted words hold an apostrophe, the quote is in “ ”. Text that holds a straight double quote is named unquoted (SH-34's rule 14).

Where a kind of post came up that those rules don't cover, I followed the rule below. These are readings, mine, for the coordinator to align with SH-37 to SH-46.

1. **'We' adding a feature to an app is a maker statement** (the ruling after SH-35: 'we' make, upgrade or ship an app). Translate & Adapt: “we've added automatic translation updates to Translate & Adapt”, and 'Shopify will translate new and updated content automatically each week' (SH-E-04551fad for the United States and Canada, SH-E-d4e7e31f for twelve European countries). Both are `own-service` on CM-MKS-008.
2. **A branded app announced with no 'we'** is `core` by what the post shows, its maker a gap (SH-34's rule 6): Shopify Launch Check (SH-E-25748df9), SimGym (SH-E-08e97b75), the Shopify Subscriptions app (SH-E-cb822f3e), Shopify Forms (SH-E-062d5c52).
   - The Editions batch placed Shopify Forms `shows` on CM-MKT-005 (SH-E-9711be6e, SH-E-37dd43d8), by M-10, since its card links the app's page in the admin. This post links no app page, so it keeps SH-34's rule. The coordinator may align the two.
3. **A third party's role ended by a rule change** (SH-E-bf3916cd: Meta 'is no longer acting as a marketplace facilitator'). By SH-34's rule 9, the line supports what replaces it:
   - the merchant's own responsibility, `shows` (M-9);
   - the order's field `channel_liable`, `core` (the ruling after SA-25).

   Meta's former role, still Meta's for orders before 26 August 2025, is in `reading`, not a filler.
4. **A Flow post that lists an API version's changes** (SH-E-a9d99f63) takes one line, CM-AUT-001. Its list names what Flow can now read (SH-34's rule 7: the data a feature reads). Each item is a developer changelog post: see the second stage.
5. **Sidekick added to another capability's own editor** takes that editor's line, as SH-35's rule 9 does for Flow's editor:
   - the segmentation code editor, CM-CUS-002 (SH-E-a49ce2e8);
   - the analytics query editor, CM-ANL-001 (SH-E-22878974);
   - the checkout and accounts editor, `core`, and the Checkout Blocks app, `own-service` (the ruling after SH-35), on CM-CHK-003 (SH-E-2cea6f44).

   Sidekick doing a task of another capability takes CM-AIA-002 alone: balances (SH-E-282c6100), apps (SH-E-d2733983), images (SH-E-e7d7245c), storefront tests (SH-E-b4e8bc9f).
6. **Early access, then release.**
   - Sidekick's voice mode, 'Early access with support for EN and desktop only' (SH-E-861e9919), is `shows`. Sidekick Voice in the mobile app (SH-E-e8903838) is `core`.
   - Campaign Autopilot, in early access in SH-34 (`shows`), is 'now available to all merchants' (SH-E-577d93a6): `core`.
7. **One export from several pages** (SH-E-80b85db9: users, roles, groups and activity logs). Each page where the Export button appears takes its line (SH-34's rule 7(b)): CM-STF-001, CM-STF-002, CM-STF-003, CM-TRU-003. 'Users > Groups (Plus plan)' is that line's own condition, kept in its reading (SH-34's rule 10).
8. **A cell's note that sends a thing elsewhere is followed** (rule 2):
   - CM-RET-002's note puts a refund to store credit on CM-LOY-001 (SH-E-4b61c9b6);
   - CM-CAT-010's note makes Shopify Collective's statements `shows` there, counting on CM-CHN-005 (SH-E-911018a3);
   - USDC goes to CM-PAY-018, whose terms hold USDC rates, though the post calls it one of 'these local payment methods' (SH-E-0ecae440);
   - CM-ORD-009's cell reads its document routes gated by the store feature `fulfillmentBatchingEligible`, so batch fulfilment's documents take its line (SH-E-95970ba3).
9. **One thing under two conditions** (the ruling after SH-34).
   - DHL's DDP and DDU labels take two CM-SHP-002 lines (SH-E-f61cfb93): the US, for DHL Express and DHL eCommerce, and Canada, for DHL Express.
   - DHL eCommerce labels from the Netherlands and Poland take one line with both countries (SH-E-d4730476): one service, whose destinations differ by country (in `reading`).
10. **The bulk editor**, named in a What's new list as where a feature is used, takes CM-CAT-001's line, whose cell cites the bulk editor (SH-E-a285f61d, SH-E-5669dc6b).
11. **The Knowledge base** (SH-E-a50b68cc) is `core` on CM-AIA-005 (a reading). It is kept at 'Sales channels > Agentic > Knowledge base', the Agentic channel this cell holds. The ruling on a store's llms.txt (CM-CNT-007, `shows` on CM-AIA-005) rests on llms.txt being kept in the SEO pages, which this isn't.
12. **The admin's own search** (SH-E-5d688e6e) takes a `new` line. SH-34's rule 13 gives the admin's whole look no line because the post's other things take theirs; this post's only thing is a feature, and a post that names a feature is never `out`. It stands beside SH-35's Saved views.
13. **A setting named by a post's admin link** takes the line of the capability whose cell cites that place: the Shopify Catalog mapping (`admin.shopify.com/mappings/shopify-catalog-mapping`) is CM-CHN-004's mappings (SH-E-92dbfbaf).

## The new things

**`new:Admin search`** (SH-E-5d688e6e, line 102, `shows`): the admin's own search across its pages.
- **The post:** 'In the redesigned desktop admin, search has been improved to be significantly faster, helping you find admin pages, resources, settings, and installed apps from one seamless flow', opened by command+k or control+k.
- **A place of its own:** none in the post. It is a bar of the admin, opened by a key. Its help page is `help.shopify.com/en/manual/shopify-admin/admin-search` (the link).
- **Proposed:** domain F, beside the admin's AI and SH-35's Saved views, with no parent. Or no capability at all, if the coordinator reads it as the admin itself (the ruling after SA-21), as SH-34's new admin look.
- **Its name:** English 'search', in the post's title 'Improved search for Shopify’s admin'. No Arabic is held: the admin in Arabic isn't captured (`docs/GAPS.md`).
- **The terms I searched** (`caps --terms`): admin search, search the admin, keyboard shortcut, knowledge base (no hit for the first three). `search` alone finds the storefront's search (CM-SFR-013) and customer saved searches (CM-CUS-002), neither of them this.
- **Its leads:** CM-APP-001 (by 'installed apps'), CM-ONB-003 and CM-API-013 (by name). None is the admin's search.

**`new:Protection against unexpected redirects`** (SH-E-c134dd44, line 123, `shows`): the online store asking buyers to confirm before it sends them to another website.
- **The post:** 'Your online store now asks customers to confirm before it sends them to a website outside your store', and, from its 'Update (October 23, 2026)', 'now only blocks links to websites that Shopify has identified as malicious and asks for confirmation for websites that are suspicious'.
- **A place of its own:** none. The post names no setting: it is the online store's built-in behaviour.
- **Proposed:** domain E, near CM-CNT-009 (URL redirects) and CM-SFR-010 (SSL), with no parent; or domain A, beside the trust capabilities.
- **Its name:** English, the title's 'protection against unexpected redirects'. No Arabic is held.
- **The terms I searched:** malicious, external link, outbound, phishing, redirect, buyer protection, storefront security, security, safe, scam, leaving the store, confirm. The hits are CM-CNT-005, CM-CNT-006 and CM-CNT-009 (the store's own links and redirects between them), CM-SFR-010 (SSL), CM-TRU-001, CM-TRU-002, CM-TRU-006, CM-TRU-018 and CM-TRU-019 (sign-in, identity, privacy, card data, security apps). None is this.
- **Its leads:** CM-CNT-005, CM-CNT-007, CM-CNT-009, CM-PAY-010 and CM-CHK-010. I read CM-CNT-009's cell: 'Sending a visitor from one of the store's links to another', not to an outside website.

**`new:Web Bot Auth`** (SH-E-7e85e227, line 189, `shows`): the merchant's own crawlers and tools let through the online store's blocking, by signed requests.
- **The post:** 'Shopify now leverages Web Bot Auth and HTTP message signatures to let you securely authorize your own crawlers, scripts, or tools to access your public Shopify online store', so 'your tools can access your store without being blocked'. Signatures are made 'in the Shopify admin, where you can set custom names and expiration dates'.
- **A place of its own:** the post says the signatures are managed in the admin, but names no page or route. So `shows`. A route of the admin router might hold that page: a lead for the second stage.
- **Proposed:** domain E, parent CM-SFR-001 (the online store), or domain A beside CM-TRU-004.
- **Its name:** English, Web Bot Auth, signatures. No Arabic is held.
- **The terms I searched:** crawler, bot, web bot auth, message signatures, robots. The hits are CM-CNT-007 (by robots), CM-CUS-012 (reCAPTCHA at sign-in) and CM-TRU-004 ('Bot protection at checkout': blocking known bots from the checkout, on Plus). None is this. Its help page sits under SEO (`help.shopify.com/en/manual/promoting-marketing/seo/crawling-your-store`), and SEO audits are one of its use cases, named in a list.
- **Its leads:** CM-OPS-004 (by 'tools': WooCommerce's System status and Tools), CM-SFR-001, CM-API-009 and CM-ORD-003 (by name). None is it.

## CHANGES, each read again against its source

- **CM-CNT-007** (SEO) gains `own-service` (line 28, SH-E-a140a835).
  - The post: 'by default your shop.app storefront can be indexed by search engines like Google and Bing', and 'You can control this in your Shop channel settings'.
  - Search engine indexing is the post's own thing (its title). Shop does it for the merchant's storefront in Shop, so `own-service` (SH-S-0056; the ruling after SH-34). Kept, with the doubt below.
- **CM-MKT-010** (advertising on ad platforms) gains `core` (line 90, SH-E-577d93a6).
  - The post: Autopilot will 'build a marketing campaign that can reach shoppers across channels such as Meta Ads, Microsoft Advertising, Snapchat, Shop, Shopify Messaging, and soon X Ads', and 'It figures out which channels to run on, what to spend where'.
  - Shopify's own tool runs the store's ads on third parties' ad platforms, which are the venues and fillers (M-3). The cell's reading had 'Shopify's own advertising tools are in CM-MKT-011 and CM-MKT-012', which holds for Shopify's own ad products. Kept.
- **CM-MKS-008** (store languages and translation) gains `own-service` (lines 105, 137, SH-E-04551fad, SH-E-d4e7e31f): 'we' adding to Translate & Adapt (rule 1 above). Kept.
- **CM-CHK-003** gains `own-service` (line 135, SH-E-2cea6f44): Sidekick in the Checkout Blocks app. The coordinator's check of SH-35 already makes CM-CHK-003 `own-service` for Checkout Blocks; the model isn't amended yet. Kept.
- **CM-B2B-001** gains `extension-point` (line 149, SH-E-e88b2c4b).
  - The post: 'Use the Payment Customization Function API to implement complex B2B workflows such as requiring review for high-value orders', with 'The new orderReviewAdd operation'.
  - B2B checkout rules are written as functions on the platform's Function API. SH-34's line on B2B APIs and B2B-compatible apps also gives this cell `extension-point`. Kept.
- **CM-ONB-004** (store setup in the admin) holds nothing and becomes held, `core` (line 176, SH-E-25748df9).
  - The post: 'The new Shopify Launch Check app eliminates the guesswork by giving you a comprehensive pre-launch validation in under 2 minutes', with 'personalized recommendations based on your actual store data—covering everything that needs to be in place for a successful launch'.
  - The checks and tasks of a store's setup before its launch are this capability's setup tasks (a reading). The app's maker isn't stated (`apps.shopify.com/launch-check`, `not-attempted`), so `core` by what the post shows (rule 2 above). Kept, with the doubt below.
- **CM-DVT-004** (development stores) gains `core` (line 185, SH-E-3c35603a).
  - The post: 'Create dev stores to build and test your apps using any Shopify plan', managed in the Dev Dashboard.
  - The cell held only a theme guide's mention of 'the development store' (`not-stated`). This shows Shopify giving developers dev stores. Kept.
- **CM-PAY-032** holds nothing and becomes held, `core` (line 47, SH-E-0ecae440: 'pay on their own device with a secure QR code or link'). SH-35 already makes it held; the model isn't amended yet. Kept.
- **CM-SHP-020** gains `core` (lines 60 and 110: SH-E-6f1a6cfc's country-specific HS codes; SH-E-5669dc6b's identifiers on EU customs documents). SH-34 already gives it `core`. Kept.

## The other NOTEs

- **`own-service`, 7 notes:**
  - Shop (SH-S-0056; the ruling after SH-34): CM-CHN-002 three times (SH-E-a140a835, SH-E-e27964da, SH-E-e32e80c8) and CM-CNT-007 once (SH-E-a140a835);
  - Translate & Adapt, CM-MKS-008 twice (rule 1 above);
  - Checkout Blocks, CM-CHK-003 (`core;own-service`).
- **'core on a product named with the platform's brand', 35 lines.** Each is a feature the post shows in Shopify's own admin, POS, analytics, payments, Flow or Email, or in Capital, Credit, Balance, Collective, Shipping, Network Intelligence, Catalog, Forms, Subscriptions and Launch Check: `core` by what it shows (SH-34's rule 6). Launch Check is the one whose `core` rests only on what the post shows of an App Store app (the cases below).
- **The first leads that hold nothing and that no line names:**
  - line 16, SH-E-60e3d641: CM-API-010, conditional webhooks, by 'conditions'. The words are a collection's conditions;
  - line 189, SH-E-7e85e227: CM-OPS-004, by 'tools'. It is WooCommerce's System status and Tools; the post's tools are the merchant's crawlers;
  - line 200, SH-E-f4a5b07d: CM-APP-010, app settings, by 'integration'. The words are Royal Mail's label integration.
- **The new things' leads:** above.
- The checker printed no NOTE for a quote it didn't find, an app's embedded page or a container. SH-E-fd124edd's footnote ('¹', '*1. Payment methods are subject to eligibility requirements.') is read with its entry and quoted in its reading.

## Entries I couldn't tell, and what would settle each

1. **SH-E-a140a835, Shop's search indexing** on CM-CNT-007, `own-service` (the CHANGES). To settle: the coordinator's reading of whether a Shop storefront's indexing is the store's SEO, or Shop's alone (then CM-CHN-002's line only).
2. **SH-E-25748df9, Shopify Launch Check,** on CM-ONB-004 and CM-AIA-001, `core`.
   - CM-ACC-009, the store's launch, is the alternative for the first line.
   - If an App Store app with no maker statement is read by M-10 (`shows` on what it does), CM-ONB-004 stays empty.
   - To settle: the listing `apps.shopify.com/launch-check`, for its maker, and the coordinator's reading of CM-ONB-004's 'in the admin'.
3. **SH-E-5d688e6e, admin search:** `new`, or no capability, like the admin's own look. To settle: the coordinator's decision with SH-35's Saved views.
4. **SH-E-ba6f7728, waived order balances,** on CM-ORD-015, an order's paid or unpaid state (a reading). The alternatives are CM-ORD-001, or a new Waived balances; the post gives it no place of its own, only a control on the order page and a staff permission. Its write-off report is CM-ANL-002's. To settle: the coordinator's reading of CM-ORD-015.
5. **SH-E-0e48bd8a, unit pricing,** on CM-CAT-001, a price kept on the product record (a reading). The alternatives are a new Unit pricing (`shows`, no place of its own), or CM-SFR-015, the storefront's display. CM-CAT-013 is the platform's automatic pricing (the coordinator's check of SH-34). To settle: the coordinator's reading.
6. **SH-E-7f90c4d0, fulfillable inventory,** on CM-SHP-001, the store's shipping zones (a reading). The alternative is CM-INV-001, stock quantities. To settle: the help page `help.shopify.com/manual/fulfillment/setup/fulfillable-inventory`, not read here.
7. **SH-E-1a1ee996, automated fraud settings,** on CM-PAY-002 (Shopify Payments' settings) and CM-ORD-006 ('the new fraud model, which uses over 400 fraud signals'). The alternative is CM-ORD-006 alone. To settle: the coordinator's reading of where payment-level fraud declines belong.
8. **SH-E-bf3916cd, Meta's tax liability:** CM-TAX-001 `core;shows` (rule 3 above). If a third party's role that still holds for older orders is to show, it takes an `outside` line with Meta as filler. CM-TAX-003, 'tracking where it is liable', is the alternative capability. To settle: the coordinator's reading of SH-34's rule 9 for a third party's retired role.
9. **SH-E-577d93a6, Autopilot's ads:** CM-MKT-010 `core` (the CHANGES). If the ad platforms are read as doing the advertising through Shopify's tool, it is `extension-point`. To settle: the coordinator's reading.
10. **SH-E-e46f8f5a, quick count in POS,** on CM-INV-003, an inventory count. The alternative is CM-INV-001, since it updates on-hand quantities. To settle: the help page on changing inventory quantities in POS.
11. **SH-E-062d5c52, Shopify Forms,** CM-MKT-005 `core`, where the Editions batch has `shows` (rule 2 above). To settle: the coordinator's alignment of the two.
12. **SH-E-cc04f755, Checkout Kit on mobile app storefronts:** CM-CHN-006 `shows`, since the merchant's developers build the app. If Checkout Kit is read as the platform's own kit for the store's own mobile app, the line is `core`, and CM-CHN-006, held now as `extension-point` only, gains `core`.
13. **SH-E-d12f2c8f, the Cards section:** its CM-PAY-025 line reads 'Merchants with Credit and/or Balance can also create and manage their own and other staff cards' as Shopify Credit's cards in the same section (a reading). To settle: the Balance cards help page.
14. **SH-E-31608ebe, in-store customers recognized:** its CM-TRU-008 line reads the recognition of shoppers 'who have previously checked out at a store powered by Shopify Payments' as Shopify Network Intelligence's use of buyers' data across merchants. The alternative is to keep it in `reading` as the feature's condition.
15. **SH-E-96689cc1, default packages:** CM-SHP-001, CM-SHP-002 and CM-CAT-002. No capability holds packages (CM-SHP-021 is Salla's packaging materials), so the feature is spread over the shipping rates, the labels and the variant it is set on.

## Items and sources

- **The entries agree with the page I read.** I read one record whole: entry 46's, `raw/runs/20261030T234414Z-merchant-changelog-feed-posts/fetch.warc.gz@529483`. It is the first post of the 30 October run in this batch; SH-34 and SH-35 read only records of the 7 October run. Its `h2` title, `post__content`, status tag 'Improvement' and area 'Admin' are the entry's. I read no other page and no run step.
- **`show --meta` prints the feed's descriptive keys** (`changelog.shopify.com@feed`, 1,645 items), not those of `@posts`, as SH-34 and SH-35 found.
- **SH-E-e8fefbca** links Ireland's help page (`help.shopify.com/en/manual/finance/shopify-capital/ireland`) under the words 'For more information on Shopify Capital in Germany'. Its line keeps the post's words in its reading.

## For the second stage: stated, or named in passing, and not placed

- **The API 2025-10 changes SH-E-a9d99f63 lists,** each a developer changelog post linked from it (`shopify.dev/changelog/...`, the `dev-changelog` structure):
  - the mutation `fulfillmentOrdersReroute`, for CM-SHP-005 (order routing);
  - PaymentSchedule's `balanceDue`, `totalBalance` and `due`, for CM-PAY-008;
  - inventory shipment timestamps, for CM-INV-006;
  - the orders query's `current_total_price` and `total_weight` filters;
  - the `inventoryQuantities` limits on `productSet` and the variant mutations.
- **Shopify Catalog** powering Shop 'along with other AI-powered shopping experiences' (SH-E-e27964da): a lead for CM-AIA-005.
- **Shop Minis:** 'our Shop Minis platform', and 'Some shoppable post providers may become available as new standalone Shop Minis in the future' (SH-E-e32e80c8).
- **Autopilot's channel list** (SH-E-577d93a6): Shop and Shopify Messaging, named in a list; 'soon X Ads'; and SEO updates asked of Sidekick.
- **Coming soon:** 'Support for headless and Hydrogen stores' for the bot traffic filter (SH-E-759b4012).
- **App listings that would give maker statements,** each `not-attempted` in `index/ledger/sitemap--apps-shopify-sitemaps.tsv`: `apps.shopify.com/launch-check`, `translate-and-adapt`, `simgym`, `shopify-subscriptions`, `shopify-forms` and `collective-supplier`.
  - They are exists-not-captured, for the coordinator to decide. They would settle `core` against `own-service` for those apps' lines.
  - Translate & Adapt, Shopify's own by rule 1, is a lead for CM-APP-011, the platform's own apps.
- **Web Bot Auth's admin page** for signatures (SH-E-7e85e227): not named in the post; the admin router may hold it.
- **The order list's custom views** (SH-E-c2f79321: 'These metafield filters can be saved as custom views'): a second post naming SH-35's Saved views.
- **The standard product taxonomy's** 'over 16,000 defined product categories' (SH-E-2a970fb1), for CM-CAT-004. Named as the data a segment filter reads.
- **The US rule** that 'Starting August 29, international postal shipments to the US must be sent as DDP (Delivered Duties Paid)' (SH-E-da6a8538). The post names no law, so no filler. The merchant's required actions there (duty collection, HS codes and countries of origin, a market's duties display, the shipping zone) are named for the merchant to do.
- **Named in passing, with no line:**
  - digital receipts sent to the Shop app (SH-E-31608ebe);
  - Customer View, the buyer-facing display (SH-E-31608ebe);
  - announcement bar extensions 'built by Shopify partners' (SH-E-b0f8d8d4);
  - the App Store's guided search and comparisons, which 'will soon retire' (SH-E-d2733983);
  - payment links in a draft order's invoice, not new (SH-E-54bf3a69).
- **Each post's Help Center link** describes its feature further: requirements, eligibility, plans. They aren't read by this pass.

## Problems with the brief or the scripts

1. **`show --meta` prints the feed label's keys** for this structure, not those of `@posts` (as SH-34 and SH-35 found).
2. **The checker's CHANGES repeat cells that SH-34 and SH-35 already change** (CM-PAY-032, CM-SHP-020, CM-CHK-003), since the model isn't amended between batches. They are listed above, kept, with that said.
3. **The brief's rule 4 reads differently from B-extent** for a changelog post that names a branded app ('`extension-point` where it names an app'). B-extent governs, as SH-34's notes said (their problem 4): such apps are `core` by what the post shows, with the maker a gap.
4. **A row can't hold a straight double quote,** so text that holds one is named unquoted: the option names of SH-E-7f90c4d0, the column name of SH-E-e738b855, Notify customer in SH-E-62f349d4, the preset ranges of SH-E-fb4553ba.
5. **How I kept the cost down:** chunks of 10 posts, each printed once with its leads; one lookup call for each chunk's cells and terms; one archived page read.

## The coordinator's check (31 October 2026, after the batch)

- **The cell changes stand, each read again, but one:**
  - CM-MKT-010 is `core`: Campaign Autopilot, open to all merchants, runs the store's ads, with Meta Ads, Microsoft Advertising and Snapchat as its fillers;
  - CM-MKS-008 is `own-service`, by the ruling after SH-35: 'we've added automatic translation updates to Translate & Adapt';
  - CM-CHK-003 is `own-service`, for Sidekick in Checkout Blocks;
  - CM-B2B-001 gains `extension-point`;
  - CM-ONB-004 is `core`, from the Launch Check app's pre-launch checks, by what the post shows, its maker a gap;
  - CM-DVT-004 is `core`.
- **Dropped:** CM-CNT-007's `own-service` for Shop's indexing of shop.app. That is Shop's own channel, which the entry's CM-CHN-002 line holds, not the store's own search optimisation.
- **The branded apps:**
  - Shopify Forms at `core` here and at `shows` in SH-50 are both right, each by its entry's kind (the ruling after SH-36).
  - The cell takes `core` either way.
- **New things:** Admin search, Protection against unexpected redirects and Web Bot Auth. Admin search is decided with SH-35's Saved views and Salla's quick search, or ruled no capability, as the admin's own look is.
- **Rules 1 to 13 stand** for SH-37 to SH-46.
- **Cost:** 25.1 million tokens over 85 requests, about 193,000 an entry.
