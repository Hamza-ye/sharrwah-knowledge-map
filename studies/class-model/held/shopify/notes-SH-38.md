# SH-38: Shopify's merchant changelog, posts 521 to 650 (notes)

**The batch:** platform `shopify`, batch `SH-38`, effort `high`. Its 130 entries are posts 521 to 650 of `merchant-changelog` as `@posts` holds them: `structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl`, lines 521 to 650 (positions 520 to 649), at observed-sh `e38dc17e3`. They are dated 5 March 2025 back to 28 August 2024, and all come from the run `20261030T234414Z-merchant-changelog-feed-posts`, in the order SH-34's notes describe.

**What I read:** the brief, and what it names:
- the evidence map;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, and its `REGISTER.tsv` row for `shopify/merchant-changelog`. The changelog has no ledger denominator ('no sitemap: 404');
- `show --meta`, `selection.tsv`'s row (`placement` `where`, rule `labels:@posts;drop:run,status,class;long:20000`);
- B-extent's "Cells and evidence" and its conventions, with "What a place of its own is";
- the coordinator's rulings, at the start and again when the file changed during the batch: the ruling after SA-56 (nested gates joined with ` and `) was added. It bears only on one scope of mine (SH-E-e2c5a7f4, below);
- SH-34's, SH-35's, SH-36's and SH-37's notes with the coordinator's checks, and their placements, summed by capability and support, and read by line where an entry of mine was of the same kind (SFN, Shop Campaigns, Shopify Forms, the Customer View app, Search & Discovery, Shopify Bundles, Audiences, carriers, the checkout and accounts editor).

`held_entries.py earlier` printed no line for any key of the batch, chunk by chunk. No placements of SH-39 to SH-46 existed when I finished.

**Counts:**
- 130 entries on 226 lines: 224 `capability` lines and 2 `new` lines, none `out`. Every entry has at least one `capability` line.
- By support: `core` 191, `own-service` 12, `extension-point` 11, `shows` 8, `core;extension-point` 3, `own-service;extension-point` 1.
- Lines per entry: 58 entries take one line, 57 two, 11 three, 2 four, 1 six (SH-E-5d1e473e) and 1 seven (SH-E-8f8659e7). In all they reach 108 capabilities and 1 new thing.
- The checker's final line: `130 of 130 entries placed; 0 problems`.

## The rules my lines follow

I kept to SH-34's rules 1 to 14, SH-35's rules 1 to 10, SH-36's rules 1 to 13, SH-37's rules 1 to 14 (rule 1 as the ruling on the admin's frame changed it), and the rulings after SH-34 to SH-37. Every reading begins with the post's date and type tag, then its release words. Every quote is copied from the entry's own text, but one: SH-E-51678dcb's line quotes its twin's title (SH-E-85dd0058), and cites the page I read by its record. Where the quoted words hold an apostrophe, straight or curly, the quote is in “ ”. Text that holds a straight double quote is named unquoted (SH-34's rule 14): the Lock pricing action (SH-E-e7a458e6), Flow's Cancel order action (SH-E-0d3a3c6d), the Don't collect tax option (SH-E-b05bdc80), the add from URL field (SH-E-be338d5c), the Legacy access badge (SH-E-87bff36a).

Where a kind of post came up that those rules don't cover, I followed the rule below. These are readings, mine, for the coordinator to align with SH-39 to SH-46.

1. **A post with a title only.** Two posts of 15 October 2024 hold no text: their items' `html` is empty. SH-E-85dd0058's title names Shopify POS, so it takes CM-POS-001. SH-E-51678dcb's title, 'Android USB Reader Connectivity', doesn't, so I read its page (`raw/runs/20261030T234414Z-merchant-changelog-feed-posts/fetch.warc.gz@4240356`). Its `post__content` is empty too. I read it as the same feature as its twin of the same date and area (a reading), on CM-POS-001.
2. **An app whose maker a held statement names takes `own-service` on every line about it** (the ruling after SH-37), its maker statement cited in `reading`:
   - Search & Discovery, by SH-E-9b869699 (SH-53, the ruling after SH-53): four lines on CM-SFR-013;
   - Shopify Bundles, by SH-E-1d272a37's 'our new, free bundles app' and this post's 'first-party': CM-SEL-006 (SH-E-88c8359c);
   - Shopify Audiences, by 'We’re releasing Shopify Audiences v2.4' and SH-50's line: CM-MKT-011 (SH-E-afff8d1c);
   - Shopify Email, now Messaging: CM-MKT-007 (SH-E-d3a97b36);
   - Checkout Blocks: CM-PAY-019 (SH-E-d41524a3), CM-CHK-003 (SH-E-58939e82), CM-APP-011 (SH-E-aa25195b).

   SH-35 placed two Shopify Bundles posts `core` (SH-E-1b3f0ff8, SH-E-90b81d95). The coordinator may align them, as the Messaging lines were.
3. **A retired feature with no replacement, where the capability isn't the feature's alone.** SH-34's rule 9 makes the line `shows` where the capability is the feature's alone. I made it `shows` here too, since the post shows the feature and its end:
   - Shop's chat in the Shop app, on CM-SUP-004, where Shopify Inbox keeps the online store's chats (SH-E-607889e1);
   - Meta Pay, removed as an accelerated checkout, on CM-PAY-012 (SH-E-0f205672).
4. **A setting retired from an app, with third-party apps named as the way to do it now** (SH-E-df152980). The retired setting, auto-adding products in Checkout Blocks' checkbox upsell blocks, is `shows` on CM-MKT-021. The replacement, 'third-party apps available in the Shopify App Store' for 'auto-added free gift promotions', is `extension-point` on CM-MKT-003. Reading a free gift added without a code as a special offer is mine.
5. **The platform's own app using an extension interface** (SH-E-d3a97b36: Shopify Email's new 'app extensions on the product index page and the product details page'). `own-service` on CM-APP-008 would read the extension interface as a separate Shopify product, and `extension-point` needs a third party. So the line is `shows`: it shows admin UI extensions on the admin's own pages, and supports no placement. The email campaigns themselves are `own-service` on CM-MKT-007.
6. **A list of the admin's index tables whose default sort changed** (SH-E-594a13aa). Each list page is part of its capability (rule 3), so each takes its line: products, purchase orders, transfers, files. I didn't read this as the admin's own frame (the ruling after SH-37), which is its loading, navigation and look, not a list's own order.
7. **'All plans'.** A post that opens a feature to 'all Shopify plans' after it 'previously required' Advanced or Plus (SH-E-5d1e473e), or makes it possible 'for merchants on all plans' (SH-E-7d8425b4), keeps those words in `reading`, as SH-34's rule 10 keeps 'available to all merchants'. A post naming a plan floor keeps it as scope: 'basic plan and up' (SH-E-60f56793), 'Shopify plan or above' (SH-E-f64dc5b2).
8. **An organization's features** (SH-E-8f8659e7, Organizations and store transfers). Each item the post says the organization manages across its stores takes its line (SH-34's rule 7(c)): the organization (CM-ACC-003), store transfers (CM-ACC-001), billing summary (CM-PLN-004), a shared payment method (CM-PLN-005), users (CM-STF-001), roles (CM-STF-002) and two-step authentication (CM-TRU-001). Seven lines, which the coordinator may prefer fewer.
9. **Each headless or Hydrogen storefront as its own channel** (SH-E-9f7d561a, SH-E-2ff862f1) takes:
   - CM-SFR-011, the storefronts;
   - CM-CHN-001, publishing to each as a channel, with `publishablePublish`;
   - CM-CHN-007, several storefronts in one store, each with its own products, as that cell's Build headless storefronts holds.

   Showing each storefront's name on the Orders page (the title's 'order attribution') stays in CM-CHN-001's reading. CM-MKT-008 is crediting orders to marketing, not to a channel.
10. **Address validation** has no capability of its own. Validating the buyers' and companies' addresses in the admin (SH-E-7183e0b6) and Managed Markets' correction of label addresses (SH-E-1a244cc9) both take CM-CUS-008, the nearest (a reading). A location's own addresses stay on CM-INV-005 (SH-E-67205477).
11. **The Customer View app.** SH-E-5db19f86 says “We’ve released an update to POS Terminal and the Customer View app”. I kept its line `core` on CM-POS-001, as SH-37 placed the same app's 'we' post (SH-E-63c92bd6, by its rule 14) and as SH-E-4f933f80 is placed. By the ruling after SH-35, 'we' updating a separate app is a maker statement, and Customer View is a separate app on Google Play. If the coordinator reads it so, these lines are `own-service`. CM-POS-001's cell already holds `own-service`, so no cell changes.
12. **Countries and plans that must both hold** (SH-E-e2c5a7f4, multi-currency payouts in seven countries for Advanced, Plus and Enterprise). I wrote the scope `Australia;UK;Spain;Italy;Netherlands;Germany;Austria and Advanced;Plus;Enterprise`, meaning one of the countries with one of the plans. The ruling after SA-53 has one list before ` and ` and one condition after it, so a list after ` and ` is a case it doesn't settle (problem 4 below).

## The new thing

**`new:Admin search`** (SH-E-ac213bcc, line 12; SH-E-5b666070, line 80; both `shows`): SH-36's new thing, the admin's own search, which the ruling after SH-37 keeps as a new thing.
- **The posts:**
  - 26 February 2025: 'You can now use admin search to quickly find and navigate to' markets, draft orders, discounts, marketing automations, purchase orders, locations, company locations and catalogs. The same post's Sidekick takes its own line, on CM-AIA-002.
  - 11 December 2024: “We've made searching in Shopify a consistent experience across desktop and the Shopify app”, with 'All filters available on desktop'. Its Shopify app takes CM-SRF-001, as SH-37 placed search in Settings.
- **A place of its own:** none in the posts. The search is a bar of the admin, and the things searched are named in a list.
- **Proposed:** as SH-36 proposed, domain F, beside Saved views, with no parent.
- **Its name:** English, 'admin search', 'Search in the Shopify app'. No Arabic is held: the admin in Arabic isn't captured (`docs/GAPS.md`).
- **Its leads,** which the checker's NOTE lists:
  - for line 12: CM-ACC-002 (by 'commerce'), CM-ACC-004 (by 'company'), CM-AIA-002 (placed, Sidekick), and CM-STF-005 and CM-ORD-003 (by name);
  - for line 80: CM-APP-002 (the App Store, named as a link to search it), CM-ANL-003 (by 'overview screens'), CM-APP-001 (by 'Uninstalled apps'), and CM-ONB-003 and CM-APP-011 (by name).

  None is the admin's search. The terms SH-36 searched hold.

## CHANGES, each read again against its source

- **CM-ONB-004** (store setup in the admin) holds nothing, and becomes held, `core` (line 4, SH-E-60f56793).
  - The post: the 'AI Store Setup Tool' will 'help new business owners overcome the daunting challenge of designing an online store'.
  - Its own thing is generating custom themes, which take CM-AIA-001 and CM-SFR-001. 'Store setup' is in the tool's name.
  - SH-36's Launch Check gives the cell `core` already, and the coordinator kept it. Kept, but weak: if the coordinator reads ONB-004 as setup tasks and checks only, this line goes.
- **CM-PAY-019** (payment method rules) gains `own-service` (line 7, SH-E-d41524a3).
  - The post: 'Checkout Blocks now lets Shopify Plus merchants disable gift cards during specific checkout scenarios', and hide wallet payments by cart and customer conditions.
  - Checkout Blocks is Shopify's own app (the ruling after SH-35). SH-37's notes listed the same job as a lead. Kept.
- **CM-SHP-012** (fulfillment network) gains `core` (line 14, SH-E-369acb9a).
  - The post: 'The new Shopify Fulfillment Network (SFN) dashboard allows you to monitor and compare metrics like order-to-delivery time and in-transit time'.
  - The post names no partner and no maker. So the line is `core` by what it shows, with the maker a gap (the ruling after SH-36).
  - The cell's `extension-point` rests on SFN's App Store install and its route gated by the apps permission. SH-37's partners line is `extension-point`. Kept, with the doubt below.
- **CM-INV-004** (low stock alerts) holds nothing, and becomes held, `core` (line 15, SH-E-369acb9a).
  - The post: the dashboard gives 'quick access to alerts for low inventory, orders on hold, and in-progress transfers'.
  - An alert to the store on low stock is the cell's own thing, Salla's product.quantity.low (a reading).
  - Kept, the weakest. The alerts are named in a list of what the dashboard shows. If the coordinator reads them as named in passing, the line goes.
- **CM-MKT-003** (automatic discounts and special offers) gains `extension-point` (lines 24 and 144).
  - SH-E-e3ffcda9: “We've increased the number of active automatic app-based discounts per shop”, so promotions become 'individual automatic discounts when using apps and Shopify Functions'. Plain.
  - SH-E-df152980: free gift promotions now 'require third-party apps available in the Shopify App Store' (rule 4 above). A reading.
  - The cell 'holds nothing' only until SH-34's and SH-37's `core` lines are amended. Kept.
- **CM-SHP-002** (shipping labels) gains `extension-point` (line 29, SH-E-5d1e473e).
  - The post: 'Duty prepaid labels must be purchased outside of Shopify Shipping', and 'Purchase duty prepaid shipping labels using third-party apps from the Shopify App Store'.
  - SH-35 and SH-37 give the cell the same. Kept.
- **CM-SHP-020** gains `core` (line 60, SH-E-eaf2688c: Managed Markets adds the buyer's tax ID to commercial invoices for Brazil, China and South Korea). SH-34, SH-36 and SH-37 already give it `core`; the model isn't amended yet. Kept.
- **CM-SFR-013** (storefront search and filtering) gains `own-service` (lines 72, 161, 196, 207). These are the Search & Discovery app's category filter order, combined listings in search, category metafield filters and multilingual Semantic Search. The app's maker statement is SH-E-9b869699's, which SH-53 placed `own-service`. Kept.
- **CM-CHK-003** gains `own-service` (line 76, SH-E-58939e82: 'All merchants can now install Checkout Blocks to enhance their Thank You and Order Status Pages'). The coordinator's checks of SH-35 and SH-36 already give it. Kept.
- **CM-MKT-011** (audiences for advertising) gains `own-service` (line 132, SH-E-afff8d1c).
  - The post: “We’re releasing Shopify Audiences v2.4 with a new audience type”.
  - It is a maker statement by the ruling after SH-35, which names Audiences as its case, and SH-50 placed it so (SH-E-234dcbd7). Kept.
- **CM-MKT-006** gains `extension-point` (line 147, SH-E-08c26174: 'Marketing automation templates built by Shopify and partners'). SH-35 and SH-37 give it the same. Kept.
- **CM-MKT-007** gains `own-service` (line 202, SH-E-d3a97b36). By the ruling after SH-37, which SH-37's lines already carry. Kept.
- **CM-SEL-006** (bundles) gains `own-service` (line 213, SH-E-88c8359c): Shopify Bundles, 'a free first-party bundles app'. SH-53 already places it (SH-E-1d272a37). Kept.
- **CM-SHP-022** (shipping complaints and carrier ratings) holds nothing, and becomes held, `core` (line 218, SH-E-adb7f346).
  - The post: 'You can now initiate a shipping claim for lost, damaged and late packages with labels purchased in Shopify from your order details page in admin', with the claims form prefilled 'For carrier claims supported by Shopify'.
  - The capability is the merchant's complaints about the carriers of the platform's labels, raised through the platform, defined from Salla's. A claim against the carrier for a label bought in Shopify is that (a reading). Kept.

## The other NOTEs

- **`own-service`, 13 notes:**
  - Shop (SH-S-0056; the ruling after SH-34): CM-CHN-002 twice (SH-E-c6baa18e, SH-E-d37e4c3d) and Shop Campaigns on CM-MKT-012 (SH-E-583d51bb: 'let Shop do the rest');
  - Checkout Blocks: CM-PAY-019, CM-CHK-003 and CM-APP-011. The last is the app made by Shopify, 'We updated the Checkout Blocks app', where Apps is only a group it sits under;
  - Search & Discovery four times, Audiences, Shopify Email and Shopify Bundles (rule 2 above).
- **'core on a product named with the platform's brand', 22 notes.** Each is a feature the post shows in Shopify's own admin, POS, checkout, Flow, Tax, Shipping, Payments or the Shopify app, or in Shopify Fulfillment Network, Collective, Subscriptions, Forms, Combined Listings, Magic or the App Store: `core` by what it shows (SH-34's rule 6; the ruling after SH-36). SFN (line 14) is in the CHANGES.
- **The first leads that hold nothing and that no line names:**
  - line 76, SH-E-58939e82: CM-OPS-004, by 'status, tools'. The words are the Order Status Pages and the blocks as 'tools';
  - line 135, SH-E-1a244cc9: CM-ORD-003, by 'on hold, processing'. The words are orders held for address review and 'order processing', not an order's statuses.
- **The new thing's leads:** above.
- The checker printed no NOTE for a footnote mark, an app's embedded page or a container. Its one note for a quote it didn't find was mine: I had quoted a ruling's words ('a new app from Shopify'), which no held source holds. That line now cites SH-50's entry instead.

## Entries I couldn't tell, and what would settle each

1. **SH-E-369acb9a, the SFN dashboard:** `core` on CM-SHP-012 and CM-INV-004 (the CHANGES). To settle:
   - SFN's maker. Its admin route is named for the app and gated by the apps permission, so the dry run's convention would make it `extension-point`;
   - the coordinator's reading of a dashboard's alert list.
2. **SH-E-60f56793, the AI store setup tool, on CM-ONB-004** (the CHANGES). To settle: the coordinator's reading of ONB-004.
3. **SH-E-df152980, Checkout Blocks' auto-add removed:** `shows` on CM-MKT-021 and `extension-point` on CM-MKT-003 (rule 4 above). The alternative is one line on CM-MKT-021, `shows;extension-point`.
4. **SH-E-e4278b2b, Mexico's RFC at checkout,** on CM-TAX-005 (as SH-34 placed Brazil's CNPJ) and CM-CHK-001, the Mexican government its filler. The alternative is CM-SHP-020, since the RFC is required 'on orders under $2,500 USD shipping into Mexico', as SH-E-eaf2688c's tax IDs are for customs. To settle: the help section the post links ('additional tax fields in checkout').
5. **SH-E-1a244cc9 and SH-E-7183e0b6, address validation, on CM-CUS-008** (rule 10 above). The alternative is a new Address validation, with no place of its own in these posts, or CM-CHK-005 where it happens at checkout.
6. **SH-E-d3a97b36, Shopify Email's admin extensions, `shows` on CM-APP-008** (rule 5 above). The alternatives are `own-service`, the ruling after SH-37 read literally, or no line.
7. **SH-E-607889e1, Shop's chat retired,** on CM-SUP-004 alone. A `shows` line on CM-CHN-002 for Shop would change nothing.
8. **SH-E-f95655fd, Collective's 2-minute delay for fraud checks:** a CM-ORD-006 line as well as CM-CHN-005 (a reading). The alternative is CM-CHN-005 alone. The fraud checks are the retailer's own automations, Flow an example.
9. **SH-E-b7156c7b, segment triggers:** CM-AUT-001, CM-MKT-006 and CM-CUS-002. The last reads the segments' joins and leaves as the segments' own new events (the post's area Customers). The alternative is no CM-CUS-002 line, the segments being the data the triggers read.
10. **SH-E-594a13aa, default sort orders,** four lines (rule 6 above). If the coordinator reads a list's sort as the admin's own frame, they are `out`.
11. **SH-E-4551569c, ShipSurance:** the title names it for the insurance, with no maker or role stated, so it is in `reading` and not a filler (the brief's rule for a named company that no held statement places).
12. **SH-E-e2c5a7f4's scope** (rule 12 above, and problem 4 below).
13. **SH-E-5db19f86, the Customer View app** (rule 11 above): `core` here, `own-service` if 'we' updating that app is read as a maker statement.

## Items and sources

- **The entries agree with the page I read.** I read one record: SH-E-51678dcb's, at `raw/runs/20261030T234414Z-merchant-changelog-feed-posts/fetch.warc.gz@4240356` (`held_index.py`). It holds the date 'October 15, 2024', the `h2` title, an empty `post__content`, the status tag 'New' and the area 'Admin', as the entry does. SH-E-85dd0058's item is empty the same way (`items.jsonl`, line 620). I read no run step.
- **`show --meta` prints the feed's descriptive keys** (`changelog.shopify.com@feed`, 1,645 items), not those of `@posts`, as SH-34 to SH-37 found.

## For the second stage: stated, or named in passing, and not placed

- **The App Store listings that would give maker statements,** each `not-attempted` in `index/ledger/sitemap--apps-shopify-sitemaps.tsv`:
  - `apps.shopify.com/shopify-subscriptions`, `shopify-forms`, `flow` and `combined-listings`, whose lines here are `core` by what the posts show;
  - `search-and-discovery`, `shopify-bundles`, `shopify-audiences`, `shopify-messaging` and `checkout-blocks`, already Shopify's own by held statements.

  `collective` is `captured`. They are exists-not-captured, for the coordinator to decide.
- **The Customer View app's package** is held, `raw/runs/20261005T020136Z-android-apks/apks/com.shopify.pos.customerview/` (`manifest.txt`, `package.txt`, `badging.txt`). Read with its Google Play listing, it may settle rule 11's maker question. I didn't read it.
- **Apple's role in Tap to Pay on iPhone** (SH-E-87bff36a): “Apple doesn’t store card numbers or PIN information on the device or Apple servers”. This is a lead for CM-POS-002 or CM-TRU-018 (`outside`, Apple). Its line keeps it in `reading`, since the post names it as a property of the feature.
- **Tap to Pay's fees** (SH-E-07684036, SH-E-87bff36a): 'subject to standard credit card processing fees', with no value. A lead for CM-PAY-007.
- **Tipping on POS Terminal** (SH-E-5db19f86: 'a refreshed design to cart, payment, tipping and receipt screens'): a further lead for SH-35's Tipping, named in a list.
- **Multipass** (SH-E-7d8425b4): 'multipass, which is limited to Shopify Plus plans and legacy customer accounts'. A plan line for CM-CUS-011's Multipass, named only as the way things were before.
- **The Checkout Sheet Kit guide** for mobile apps (SH-E-7d8425b4), a lead for CM-CHN-006, linked only.
- **Help Center Assistant** (SH-E-f4e2626f: 'Help Center Assistant now uses this updated content to answer questions faster'): the Help Center's own assistant, kept in CM-ONB-003's reading. It is a lead for the AI capabilities, if the coordinator counts it there.
- **Shopify Finance's products in the Shopify app** (SH-E-3efa7510): Balance, Capital, Credit, Payouts, Taxes and Bill Pay, named in a list, 'in all Shopify Payments-eligible countries', which the post doesn't list.
- **Market facts, for the subjects:**
  - Mexico's RFC rule on orders under $2,500 USD (SH-E-e4278b2b);
  - Canada's GST/HST holiday (SH-E-1bd1873b, SH-E-b5603037);
  - the customs rule on tax IDs in Brazil, China and South Korea (SH-E-eaf2688c);
  - Bancontact as Belgium's most popular debit method (SH-E-608f40a4).
- **Named in passing, with no line:**
  - the Translate & Adapt app for product pages in Shop (SH-E-c6baa18e);
  - Shopify Forms, for birthdays and for forms that trigger Flow (SH-E-b7156c7b, SH-E-ff3f62c2);
  - Flow's Airtable template (SH-E-b2b8bcbc);
  - the 40 launch partner apps for customer account extensions, unnamed (SH-E-d67161c0);
  - Shopify's inbox to be rebuilt, 'as part of upcoming platform enhancements' (SH-E-607889e1);
  - Upserts to 'expand for more object types in the future' (SH-E-444c0ebe).
- **Each post's Help Center link** describes its feature further. They aren't read by this pass.

## Problems with the brief or the scripts

1. **`show --meta` prints the feed label's keys** for this structure, not those of `@posts` (as SH-34 to SH-37 found).
2. **The checker's CHANGES repeat cells that earlier batches already change,** since the model isn't amended between batches: CM-CHK-003, CM-MKT-003, CM-MKT-006, CM-MKT-007, CM-MKT-011, CM-ONB-004, CM-SEL-006, CM-SFR-013, CM-SHP-002 and CM-SHP-020. They are listed above, kept, with that said.
3. **The brief's rule 4 reads differently from B-extent** for a changelog post that names a branded app ('`extension-point` where it names an app'). B-extent governs, as SH-34 to SH-37 said, and the ruling after SH-36 says the same.
4. **The scope grammar has no form for two lists that must both hold** (SH-E-e2c5a7f4: seven countries, three plans). The ruling after SA-53 has one list before ` and ` and a single condition after. I wrote the plans as a `;` list after ` and `, read as alternatives among themselves. The coordinator may choose the form.
5. **A maker statement cited from another batch's entry can't be quoted from the rulings.** The checker looks for a quote in held sources, and `review-H-rulings.md` isn't one. I cite such statements by their entry (SH-E-9b869699, SH-E-1d272a37, SH-E-234dcbd7).
6. **The rulings file changed during the batch** (after SA-56). It changes no line here but the scope form in problem 4.
7. **How I kept the cost down:** chunks of 10 posts, each printed once with its leads and `earlier`, with one lookup call for each chunk's cells (names, notes and Shopify placement only). I read one archived page.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 130 of 130 entries, no problem, after the one change below.
- **The cell changes stand, each read again, but one:**
  - **CM-INV-004's line is dropped** (line 15). The SFN dashboard's 'quick access to alerts for low inventory, orders on hold, and in-progress transfers' names three things in a list, and the batch gave the other two no line (the ruling after SA-41). The low-inventory alerts are a lead for CM-INV-004 in the second stage. The cell holds nothing still.
  - CM-SHP-022 is held, `core`. A shipping claim for lost, damaged or late packages with labels bought in Shopify is its definition's own thing: the merchant's complaints about the carriers of the platform's labels, raised through the platform.
  - CM-MKT-003 is held, `extension-point`, from apps' and Functions' automatic discounts. The free gift promotions that 'now require third-party apps' are a marked reading.
  - CM-SHP-012's `core` is by what the post shows, with the maker a gap (the ruling after SH-36).
  - CM-ONB-004's 'AI Store Setup Tool' line stays a marked reading. SH-1's setup tasks make the cell held in any case.
- **Rulings after SH-38** (`review-H-rulings.md`):
  - ` and ` joins two lists, each read as it is alone, so line 142's scope stands. A post's own words that hold 'and' are quoted: nine lines of SH-34 to SH-38 and SH-50 now read `'Basic plans and above'` and the like.
  - A post is about the app whose page its own link opens. SH-35's two lines and SH-37's one on the Shopify Bundles app are aligned to `own-service` (SH-35's line 139 to `core;own-service`, beside the bundles product API).
- **The Customer View app stays `core`** on CM-POS-001. It is part of Shopify POS, which the cell holds as the platform's own, and SH-37 placed it so.
- **The rules this batch wrote** for title-only posts, retired features, the platform's own app on an extension interface, 'all plans', the organizations post, headless storefronts, address validation and default sort orders stand for SH-39 to SH-46.
- **The tools:**
  - `show --meta` now prints the meta of the label the entries are read under (`@posts`, 1,646 posts), not the feed's;
  - the brief's line on a post's support follows B-extent: `own-service` where held words name the platform as an app's maker, `extension-point` where third parties do it through what the platform provides.
- **Cost:** 18.7 million tokens over 72 requests, about 144,000 an entry. The context reached about 442,000 tokens.
