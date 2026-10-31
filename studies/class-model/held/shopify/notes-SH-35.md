# SH-35: Shopify's merchant changelog, posts 131 to 260 (notes)

**The batch:** platform `shopify`, batch `SH-35`, effort `high`. Its 130 entries are posts 131 to 260 of `merchant-changelog` as `@posts` holds them: `structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl`, lines 131 to 260 (positions 130 to 259), at observed-sh `e38dc17e3`. They are dated 27 April 2026 back to 20 November 2025, and all come from the run `20261007T071251Z-published-changelog-posts`.

**What I read:** the brief, and what it names:
- the evidence map;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, and its `REGISTER.tsv` row for `shopify/merchant-changelog`. The changelog has no ledger file: it has no sitemap (the register: 'no sitemap: 404');
- `show --meta`, `selection.tsv`'s row (`placement` `where`) and `@posts/meta.json`;
- B-extent's "Cells and evidence" and its conventions;
- the coordinator's rulings. They changed during the batch: three rulings were added after SA-49 (a settings tree's gate nodes, a settings redirect, the admin's own interface language). None of them changes a line here: no post of this batch is about the admin's language;
- SH-34's notes, with the coordinator's check, and its placements, summed by capability and support.

`held_entries.py earlier` printed no line for any key of the batch, at the start and at the end.

**Counts:**
- 130 entries on 220 lines: 218 `capability` lines, 2 `new` lines, none `out`. Every entry has at least one `capability` line, and two of them also take a `new` line.
- By support: `core` 191, `own-service` 8, `extension-point` 8, `shows` 5, `core;extension-point` 4, `core;shows` 3, `own-service;extension-point` 1.
- Lines per entry: 73 entries take one line, 36 take two, 17 three, 1 four, 2 six (SH-E-9869aa49, SH-E-a4400856) and 1 eight (SH-E-86c0c5a9). In all they reach 90 capabilities and 2 new things.
- The checker's final line: `130 of 130 entries placed; 0 problems`.

## The rules my lines follow

I kept to SH-34's rules 1 to 14 and the four rulings made after SH-34. Every reading begins with the post's date and type tag, then its release words. Each quote is copied from the entry's own text. Where the quoted words hold a straight apostrophe, the quote is in “ ”.

Where a kind of post came up that those rules don't cover, I followed the rule below. These are readings, mine, for the coordinator to align with SH-36 to SH-46.

1. **Quick sale.** Five posts: SH-E-9b6c4e51, SH-E-e502c9c0, SH-E-61408991, SH-E-9f73b5ba and SH-E-91cf823c.
   - Quick sale is in-person selling 'in the Shopify mobile app', not in the POS app. So its line is on CM-SRF-001, the mobile app for managing the store (a reading). CM-POS-001's name is the platform's own POS app.
   - The things a quick sale does take their own lines:
     - payment links, CM-PAY-032;
     - cash and change due, CM-PAY-016 (Shopify's manual payment methods name cash, SH-S-0322; a reading);
     - Tap to Pay, CM-PAY-021;
     - shipping, CM-SHP-001;
     - tips, `new:Tips`.
2. **A list of features opened to more plans** (SH-E-86c0c5a9, key B2B features on Basic, Grow and Advanced).
   - Each feature the list names takes its line, with the three plans as its scope (SH-34's rule 7(c)).
   - What is said to 'remain exclusive to Plus' takes a second line on the same capability, with Plus as its scope (the ruling after SH-34): unlimited catalogs and direct catalog assignment on CM-B2B-003; partial payments and deposits on CM-PAY-008.
   - 'ACH payments (U.S. only)' is alone on CM-PAY-017, so its country stays in its reading (SH-34's rule 10).
3. **A post that retires a feature and names what replaces it** (SH-34's rule 9). Three posts:
   - SH-E-677df824, Shopify Scripts. The line goes on the replacement, Shopify Functions (CM-APP-005), `core;extension-point`, since 'public apps' are also named. The changelog's area is Plus. It isn't taken as scope, since SH-34's rule 3 has the area give the post nothing; it is named in `reading`;
   - SH-E-df7e6e9c, legacy customer accounts. The line goes on the new customer accounts, CM-CUS-010;
   - SH-E-42ecf1fa, Marketing > Automations. Its automations move to the Shopify Messaging app and the Flow app.
4. **A feature offered for listed countries takes them as its scope** (the brief's rule 2: a thing the platform offers for a country). It isn't `out` as market data.
   - SH-E-299f53f7: dynamic tax-inclusive pricing, with 17 countries added, Saudi Arabia, the UAE, Egypt and Qatar among them.
   - SH-E-daaa483d: Bulgaria's markets switched from BGN to EUR, `core` on CM-MKS-006 with Bulgaria as its scope. The coordinator kept SH-34's Italian provinces the same way.
5. **Shop** does its things as `own-service`, on SH-S-0056 (the ruling after SH-34):
   - Posts and the Shop Editor (CM-CHN-002);
   - Sign in with Shop (CM-CUS-010), and leads captured through Shop (CM-MKT-005);
   - Shop's pickup screens (CM-SHP-007);
   - Shop's languages (CM-CHN-002).
6. **POS hardware sold on the Hardware Store** (SH-E-04dd57d3, the POS Hub) is `own-service` on CM-POS-002. It rests on that cell's own maker evidence, Shopify's company selling the POS Equipment (SH-S-7269, SH-S-7251; M-1). The brand alone names no maker.
7. **Customizing by market** (SH-E-b342cf39, the checkout and accounts editor; SH-E-d02463ae, theme settings and app embeds). Each takes a second line on CM-MKS-001: a market's own version of the checkout or the storefront (a reading).
8. **A how-to inside a post** (SH-E-d63b361f, editing the Order Confirmation template's code at Settings > Notifications) is `shows` on what the merchant does there, CM-NTF-001.
9. **Sidekick doing a new task** takes only CM-AIA-002, as in SH-34, even where the task is another capability's. Examples are creating customers and companies, Flow workflows, theme changes, email edits and ShopifyQL queries.
   - Two exceptions take a second line, where the post states a second thing as new:
     - Flow's editor gains Sidekick (SH-E-efd43ecc, CM-AUT-001);
     - the apps Sidekick generates are custom apps (SH-E-1067df03, CM-APP-009).
10. **An app's admin page named in a post's link** (Shop's Posts and Shop Editor, at `admin.shopify.com/apps/shop-72/…`) takes no CM-APP-007 line. The post isn't a route entry, and the checker printed no note for it.

## The new things

**`new:Saved views`** (SH-E-1dc0cd80, line 24, `shows`): the admin's own search bar and named views over its list pages.
- **The post:** 'Filters, search, and saved views now work together in one bar on your Orders, Products, Customers, Discounts, Collections, and Metaobjects pages', and 'Save any filter, column, and sort configuration as a named view'. Its Sidekick item takes its own line, on CM-AIA-002.
- **A place of its own:** none in the post. It is a bar inside each list page, and the pages are a list of places (the ruling after SA-41).
- **Proposed:** domain F, near the admin's AI and tools, with no parent. Or no capability at all, if the coordinator reads it as the admin itself, as SH-34's new admin look was read (the ruling after SA-21).
- **Its name:** English 'saved views'. No Arabic is held: the admin in Arabic isn't captured (`docs/GAPS.md`).
- **The terms I searched** (`caps --terms`): saved view, saved search, search bar, filter.
  - CM-CUS-002's 'customer saved searches' are customer segments, not this.
  - CM-SFR-013 is the storefront's search.
- **Its leads:** CM-CAT-003 (by collection), CM-AIA-002 (placed), CM-B2B-004 (by 'quotes', which here are the search syntax's 'quotes for exact match', a homonym), CM-ONB-003 and CM-CHK-010. None is saved views.

**`new:Tips`** (SH-E-9f73b5ba, line 210, `shows`): a tip the buyer adds to the payment.
- **The post:** 'You can now enable tips in quick sale settings so that when completing a quick sale order, customers can add tips before payment'.
- **A place of its own:** none in the post. It is a setting of quick sale.
- **Proposed:** domain C (payments), parent CM-PAY-001, or under the point of sale.
- **Its name:** English 'tips'. No Arabic is held.
- **The terms I searched** (`caps --terms`): tips, tipping, tip, gratuity. There were no hits. `class_slice.py search` finds only the help section 'Setting up tipping options for online orders' (SH-I-2109), which no cell of the model cites.
- **Its leads:** CM-PAY-021, CM-POS-001 (both by 'in-person'), CM-PTN-003, CM-PAY-029 and CM-CHK-009. None is tips.

## CHANGES, each read again against its source

- **CM-PAY-032** (payment links) holds nothing, and becomes held, `core` (lines 65, 83, 148, 212).
  - SH-E-9b6c4e51: from a quick sale, the merchant can 'send a link for the customer to pay from their phone'.
  - SH-E-e502c9c0: 'Payment links now support shipping'.
  - SH-E-d72a6686: buyers pay 'via the payment link in email', Plus only.
  - SH-E-91cf823c: 'Payment links are unique, shareable URLs that let you accept payments instantly'.

  The cell's note had read that Shopify's invoices aren't stated to carry a link to pay. These posts state such links (a reading of the capability's name: 'a link to pay for an order that the merchant sends the buyer'). Kept.
- **CM-MKT-023** (product recommendations) holds nothing, and becomes held, `core` (line 196, SH-E-c801d763).
  - The post: in the Shopify Product Network, 'they see personalized recommendations alongside your own inventory—powered by data from hundreds of millions of buyers'.
  - These are products the platform recommends to buyers, the capability's own words. SH-34's line on it was kept by the coordinator. Kept.
  - The app's maker isn't stated, a gap.
- **CM-CHK-005** gains `core` (line 26, SH-E-673a419b). The post: Checkout Blocks' 'Order value limits … are now available on Basic, Grow, Advanced, and Plus plans', 'to enforce order limits in checkout'. This is the same reading as SH-34's address rule, which the coordinator kept. Kept.
- **CM-POS-003** gains `extension-point` (line 36, SH-E-683cb064). The post: 'New POS targets let apps plug into open/close procedures, show alerts when balances exceed float/min/max thresholds, and enrich session details'. Apps do cash management's work through Shopify's targets. Kept.
- **CM-CHN-002** gains `extension-point` (line 27, SH-E-dbb09a4d). The post: 'Connect apps like Tolstoy, Videowise, and others to automatically sync shoppable video content' to Shop's Posts, from the Posts page. Kept.
- **CM-CUS-010** gains `own-service` (line 79, SH-E-a603e0a5). The post: 'Completing a lead capture form now creates a storefront session, so buyers are already signed in when they reach checkout', through Sign in with Shop. This is the ruling after SH-34. Kept.
- **CM-MKT-005** gains `own-service` (line 80, SH-E-a603e0a5).
  - The post: 'Recognized buyers with an existing Shop account can subscribe instantly without filling out form fields'.
  - CM-MKT-005 holds the plan line Capture customer leads, so leads captured through Shop are its thing (a reading). Kept, with the doubt below.
- **CM-SHP-007** gains `own-service` (line 181, SH-E-b7bd0730). The post: 'In the Shop app, we’ve added preparation status, clearer pickup instructions and a QR code'. Shop does part of the buyer's pickup. This is the ruling after SH-34. Kept.
- **CM-MKT-006** gains `extension-point` (line 102, SH-E-42ecf1fa).
  - The post: 'Automations that have marketing activities from other apps will be available in the Shopify Flow app'.
  - Other apps' activities run inside the store's automations (a reading). Kept, but weak: the post says where they move, not what the apps do.
- **CM-SHP-002** gains `extension-point` (line 112, SH-E-a4400856).
  - The post: Managed Markets' FedEx labels 'are available for purchase in Shopify Admin and via our integrated external fulfillment partners'.
  - Third parties buy the platform's labels through its integration (a reading). Kept, the weakest: the partners aren't named in the post, only on its linked help page.

## The other NOTEs

- **`own-service`, 9 notes:**
  - Shop, on SH-S-0056, 8 lines: CM-CHN-002 five times, CM-CUS-010, CM-MKT-005 and CM-SHP-007;
  - the POS Hub, on CM-POS-002's own maker evidence (rule 6 above).
- **'core on a product named with the platform's brand', 26 lines.** Each is a feature the post shows in the admin, POS, checkout, Flow or Messaging, and each is `core` by what it shows (SH-34's rule 6). The brands are:
  - Shopify POS, Collective, B2B, Capital, Credit, Balance, Tax, Functions, Messaging, Flow, Bundles and Product Network;
  - Shopify Capital and Shopify Credit: their lenders, on which the cells' `outside` and `own-service` rest, aren't named in these posts.
- **The first leads that hold nothing and that no line names:**
  - line 53, SH-E-d42a6221: CM-API-010, conditional webhooks, led by 'conditions'. The words are a shipping option's 'weight or price range conditions', not webhooks;
  - line 197, SH-E-b15ef0cf: CM-DVT-006, led by name ('live, update'). The post only announces the Winter '26 Edition.
- **The new things' leads:** above.
- After I took one quote out of quotes (a help section's title cited by its inventory id, problem 2 below), the checker printed no note for a footnote mark, a quote it didn't find, an app's embedded page or a container.

## Entries I couldn't tell, and what would settle each

1. **Quick sale on CM-SRF-001** (rule 1 above). The alternative is CM-POS-001, in-person selling. To settle: the coordinator's reading of whether CM-POS-001 is only the POS app, or any in-person selling the platform does.
2. **SH-E-1dc0cd80, saved views:** `new`, or no capability, like the admin's own look. To settle: the coordinator's decision whether the admin's list tools are a capability.
3. **SH-E-a2643162, the Checkout Blocks app:** `core` on CM-CHK-003, and `shows` on CM-CHK-004 for the app's own blocks.
   - The post says 'we’re upgrading the Checkout Blocks app to the latest API version'. In Shopify's own changelog, 'we' is Shopify, so this may be a maker statement. B-extent asks for 'a statement naming the company', and 'we' doesn't name it.
   - To settle: the coordinator's reading of 'we', or the listing `apps.shopify.com/checkout-blocks` (`not-attempted`). If Shopify is the maker, this line and SH-E-673a419b's are `own-service`, and SH-34's too.
4. **SH-E-a603e0a5, CM-MKT-005 `own-service`:** subscribing through Shop's recognition is lead capture done by Shop (a reading). The forms themselves are the Shopify Forms app's, whose maker isn't stated. The alternative is CM-CUS-007, marketing consent. To settle: the coordinator's reading of what CM-MKT-005's 'Capture customer leads' covers.
5. **SH-E-eda9f84c and SH-E-a8864b63, SimGym:** `core` on CM-AIA-001, an AI tool for the merchant.
   - The second post's 'AI Research Preview' is offered 'to all eligible merchants with no waitlist required'. I read that as a badge with no limit stated, so `core` (D1). If the coordinator reads a research preview as a preview for some merchants only, both lines are `shows`.
   - The maker isn't stated: `apps.shopify.com/simgym` is `not-attempted`.
6. **SH-E-e4ed9ee3, AI-powered defense:** on CM-AIA-003, text the platform's AI writes ('AI-enhanced PDF documents'), a reading. The alternative is CM-AIA-001 alone.
7. **SH-E-c7c17cbb, the US sales tax reports:** on CM-ANL-002 alone. The alternative is CM-TAX-001, whose own reports these are. To settle: whether tax reports are the reports' capability or the taxes'.
8. **SH-E-da68e961, app activity:**
   - 'Admin API activity' (requests per app) and 'App history' (staff granting app permissions) are on CM-TRU-003, as that cell's `audit_events/admin_api_activity` (a reading).
   - The alternatives are CM-API-001 for the API activity, and CM-API-003, access scopes, for the grants.
9. **SH-E-9869aa49, adaptive pricing:** on CM-MKS-006, as the coordinator placed Managed Markets' prices. It also takes CM-TAX-008, CM-MKS-007, CM-MKS-003, CM-MKS-001 (the market's toggle) and CM-PAY-005 (the payout breakdown). Six lines, by SH-34's rule 7. The coordinator may prefer fewer.
10. **SH-E-f26e209f, Avalara Tax Compliance:** `extension-point` on CM-TAX-004, Avalara the filler. M-8 would also place Avalara's return filing on CM-TAX-006, but the post doesn't state what 'Avalara Tax Compliance' does beyond the orders being 'recalculated'. To settle: a held statement of that product.
11. **SH-E-1b3f0ff8, SH-E-90b81d95, bundles:** on CM-SEL-006 `core`. Shopify Bundles' maker isn't stated: `apps.shopify.com/shopify-bundles` is `not-attempted`.
12. **SH-E-90b81d95, publishing to Google:** CM-CHN-001 `core`, Google the venue and filler (M-3). The Google & YouTube app's maker isn't stated: `apps.shopify.com/google` is `not-attempted`.

## Items and sources

- **The entries agree with the pages I read.** I read two records whole:
  - entry 1's at `raw/runs/20261007T071251Z-published-changelog-posts/fetch.warc.gz@1573281`;
  - entry 130's at `…@3130125`.

  Their date, title, content and status tag are the entries'. I didn't read the other 128 pages.
- **`show --meta` prints the feed's descriptive keys** (`changelog.shopify.com@feed`, 1,645 items), as SH-34 found, not those of `@posts`.
- **SH-E-d63b361f's text is longer than `--width 4000`.** Its end, the order confirmation template's Liquid, prints only at a wider width.

## For the second stage: stated, or named in passing, and not placed

- **Tipping:** the help section 'Setting up tipping options for online orders' (SH-I-2109) is held, and no cell cites it. It is the lead for `new:Tips`.
- **CM-ANL-005, smart analytics,** holds nothing on Shopify. Two posts would be read against it:
  - SH-E-578fcd32's Analytics insights ('automated data summaries', 'over 80 new data combinations'), placed on CM-ANL-003 as SH-34 placed insights;
  - SH-E-b2b09e1f's Sidekick Pulse.
- **CM-TRU-008,** the platform's own use of customer data across merchants: SH-E-c801d763's recommendations are 'powered by data from hundreds of millions of buyers'. This is named in passing, so it takes no line.
- **App listings that would give maker statements,** each `not-attempted` in `index/ledger/sitemap--apps-shopify-sitemaps.tsv`:
  - `apps.shopify.com/simgym`, `product-network`, `shopify-bundles`, `google`, `checkout-blocks`, `flow` and `shopify-forms`.

  They are exists-not-captured, for the coordinator to decide. They would settle `core` against `own-service` for those apps' lines.
- **The Shopify Scripts customizations report** at `admin.shopify.com/settings/checkout/customizations-report` (SH-E-677df824's link) is an admin address. I didn't look it up in the router.
- **Two posts link YouTube walkthroughs:** SH-E-7f303534 (returns in the POS cart) and SH-E-bb18c07a (custom discounts per item). Their subtitles are in `structures/shopify/embedded-videos/` (the register), not read here.
- **Each post's Help Center link** describes its feature further. They aren't read by this pass.
- **Named in passing, with no line:**
  - Visa's Rapid Dispute Resolution (SH-E-9e761fef);
  - the EU's VIES service (SH-E-4e11e1ea);
  - Stocky (SH-E-1bc04fa3);
  - the Translate & Adapt app (SH-E-0a22a7a5, as in SH-34);
  - Loop, Recharge and Matrixify, as examples of apps (SH-E-f26e209f);
  - the 'physical storefront' locations shown in Shop (SH-E-a4710dbd).

## Problems with the brief or the scripts

1. **`show --meta` prints the feed label's keys** for this structure, not those of `@posts` (as SH-34 found).
2. **The checker didn't find a quote of an inventory entry's title** cited by its id in `reading` (SH-I-2109, 'Setting up tipping options for online orders', which `class_slice.py search` prints). I took it out of quotes.
3. **The rulings file changed during the batch.** The three rulings after SA-49 change no line here.
4. **Cost:** I kept to chunks of 10 posts, with one lookup call for each chunk's cells and terms.
