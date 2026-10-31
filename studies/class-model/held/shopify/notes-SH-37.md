# SH-37: Shopify's merchant changelog, posts 391 to 520 (notes)

**The batch:** platform `shopify`, batch `SH-37`, effort `high`. Its 130 entries are posts 391 to 520 of `merchant-changelog` as `@posts` holds them: `structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl`, lines 391 to 520 (positions 390 to 519), at observed-sh `e38dc17e3`. They are dated 19 August 2025 back to 5 March 2025, and all come from the run `20261030T234414Z-merchant-changelog-feed-posts`, in the order SH-34's notes describe.

**What I read:** the brief, and what it names:
- the evidence map;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, and its `REGISTER.tsv` row for `shopify/merchant-changelog`. The changelog has no ledger denominator ('no sitemap: 404'): `index/ledger-summary.tsv` holds no `changelog.shopify.com` row;
- `show --meta`, `selection.tsv`'s row (`placement` `where`, rule `labels:@posts;drop:run,status,class;long:20000`) and `@posts/meta.json`;
- B-extent's "Cells and evidence" and its conventions, with "What a place of its own is";
- the coordinator's rulings, again at the end. The ruling after SH-69 (a line takes its own scope where its thing is stated under its own condition) was new to me at the end: two of my lines then took their own condition as scope, SH-E-ec277bb3's POS line ('POS Pro locations') and SH-E-9dce3280's companies line ('… and Plus merchants'), where I had kept it in reading by SH-34's rule 10. Four rulings were added while I worked: after SH-70 (an add-on's offer and what comes with it), after SA-53 (`;` and ` and ` in a scope), and two after SH-53 (the Editions speak as Shopify; the platform's own free themes are `core`). The last changed two of my lines (rule 1 below); my scopes are lists of alternatives, and the one condition added to a list takes ` and `, as the second asks; the third agrees with rule 14;
- SH-34's, SH-35's and SH-36's notes with the coordinator's checks, and their placements, summed by capability and support, and read by line where an entry of mine was of the same kind.

`held_entries.py earlier` printed no line for any key of the batch, at the start and at the end. No placements of SH-38 to SH-46 existed when I finished.

**Counts:**
- 130 entries on 224 lines: 221 `capability` lines and 3 `new` lines, none `out`. Every entry but two (SH-E-0fcc4288, SH-E-7f9c4c73) has at least one `capability` line.
- By support: `core` 191, `shows` 12, `extension-point` 9, `own-service` 7, `core;extension-point` 5.
- Lines per entry: 66 entries take one line, 42 two, 15 three, 6 four and 1 five (SH-E-402c842a). In all they reach 106 capabilities and 3 new things.
- The checker's final line: `130 of 130 entries placed; 0 problems`.

## The rules my lines follow

I kept to SH-34's rules 1 to 14, SH-35's rules 1 to 10, SH-36's rules 1 to 13, and the rulings after SH-34, SH-35 and SH-36. Every reading begins with the post's date and type tag, then its release words. Every quote is copied from the entry's own text, so none cites a record. Where the quoted words hold an apostrophe, straight or curly, the quote is in “ ”. Text that holds a straight double quote is named unquoted (SH-34's rule 14): the example names of SH-E-9e330a8d and SH-E-5f990a58, the filter of SH-E-c59532b0, SH-E-09f6511b's checkpoint challenge.

Where a kind of post came up that those rules don't cover, I followed the rule below. These are readings, mine, for the coordinator to align with SH-38 to SH-46.

1. **The platform's own free themes are `core` on CM-SFR-001,** by the ruling after SH-53, made while I worked ('The platform's own free themes are `core`, its store's own storefront'). SH-E-1ae5b4cf's title is 'Horizon: 10 new free themes by Shopify.'; SH-E-7845d291 is Horizon's version 1.0.5. My first lines read the title as a maker statement and made both `own-service` (M-1 for the second); the ruling overturns that, and both are now `core`, as SH-35 placed Horizon (SH-E-bc0b515a). The Theme Store, where the themes are listed, takes its own `core` line on CM-SFR-003, and the price 'free' is the first line's quality.
2. **The admin's own frame** (its speed, its navigation, its search). SH-34's admin look took no line because its other things took theirs; the coordinator then read the admin's own look as no capability. A post whose only thing is part of that frame can't take no line, and a post that names a feature is never `out` (SH-34's rule 13). So, as SH-36 did for Admin search (its rule 12), each takes a `new` line with `shows`, named in its own words:
   - SH-E-0fcc4288, 'Smarter, faster admin loading': `new:Admin loading`;
   - SH-E-7f9c4c73, 'Improved admin navigation', back buttons and breadcrumbs: `new:Admin navigation`;
   - SH-E-2a4e0daf, search within Settings: SH-36's `new:Admin search`, the same thing, with a `core` line on CM-SRF-001 for the Shopify app.

   If the coordinator rules the admin's frame no capability, the first two become `out`, read as the admin itself.
3. **A store's CSV export or import that is the post's own thing takes CM-MIG-001,** beside the capability whose data it holds (the ruling after SA-25): the discount CSV export's new column (SH-E-a09481f6), and the CSV import of a transfer (SH-E-f72f1a24, SH-E-d55a7f78). Where the CSV is only the means (SH-E-55193420's ALT text translated 'via csv file imports'), it takes no line.
4. **Store credit as a refund method.** It is `core` on CM-LOY-001. CM-RET-002's note keeps a refund to store credit as `shows` there:
   - a refund to store credit alone takes CM-RET-002 `shows` (SH-E-1e95e157, SH-E-8f3bdc6e);
   - one that names the original payment method too takes CM-RET-002 `core`, as SH-36 placed SH-E-4b61c9b6 (SH-E-99002bf6, SH-E-c98f1185);
   - the flow it is offered in takes its line, the place where the feature is used (SH-34's rule 7(b)): cancellation, CM-ORD-004; returns and exchanges, CM-RET-003.
5. **'You can use Checkout Blocks to …' as a way to customize the post's feature** is named in passing and takes no line: which pickup locations show (SH-E-a9fb0eb9), Apple Pay's availability (SH-E-4fa44da1), each buyer's manual payment methods (SH-E-0e256da5). Each is in its line's reading and listed for the second stage below.
6. **Shop selling a store's subscriptions** (SH-E-bb56c278: 'customers will be able to view and purchase subscriptions directly on Shop') stays on Shop's CM-CHN-002 line. That follows the coordinator's check of SH-36, which kept Shop's indexing of shop.app on CM-CHN-002 alone ('Shop's own channel'). My first draft gave it a CM-SEL-001 `own-service` line, which would have changed that cell; I took it out.
7. **Early access and experiments are `shows`** (the brief's rule 4): B2B pickup in store, 'Once enrolled in early access' and 'Contact Plus Support to enable' (SH-E-a9fb0eb9); Shop's display of discount codes 'during experimentation' to 'some Shop customers' (SH-E-8e4ac5c9, whose sales channel access for codes is `core` on CM-MKT-002).
8. **A kind of market takes CM-MKS-001** beside its own capability: Retail markets with location-specific catalogs, on CM-B2B-003 and CM-POS-001, for POS Pro (SH-E-01e1035c); B2B markets, on CM-B2B-001 (SH-E-ce5da55a, SH-E-0b272f81). SH-E-0b272f81's Plus-only B2B markets take a second CM-MKS-001 line with 'Shopify Plus plans' as their scope (the ruling after SH-34), and its CM-B2B-001 line takes the same scope.
9. **A list of what merchants in new countries 'can now' do** (SH-E-402c842a, Shopify Payments in 15 European countries): each item takes its line, with the countries as scope (SH-34's rule 7(c)): Shop Pay, local payment methods, the buyer's currencies and payouts. The count '130+ currencies' is market data, not a quality (SH-34's rule 12).
10. **A third party's role stated as background, not as the post's change,** goes in `reading`: the marketplace facilitators 'such as Amazon, Etsy, Meta and Tiktok' collecting and remitting tax on their own platforms (SH-E-1766e39f). The post's own thing is Shopify Tax's automated filing reporting those sales.
11. **Retired features** follow SH-34's rule 9, each line on the replacement: AvaTax for US merchants, replaced by Shopify Tax and by Avalara's new app (SH-E-2fdd654e, `core` on CM-TAX-002 and `extension-point` on CM-TAX-004, scope United States); the JS Buy SDK, by the Storefront API Client or its last version (SH-E-8c8273ca, CM-SFR-012); POS dark mode, by colour theming (SH-E-b1c80711); Shopify's own labels from Great Britain to Northern Ireland, by labels through shipping apps, linked to the App Store's category (SH-E-c218e65b, `extension-point` on CM-SHP-002, the Windsor Framework its filler).
12. **Where a POS feature appears** (SH-E-bef8840b, cash rounding): what the post lists as new on another capability takes its line (SH-34's rules 7(c) and 8): the receipts' new amounts (CM-ORD-009) and the payments reports' new metrics (CM-ANL-002). The order details page, which only shows the rounded total, takes none. Cash rounding itself is read as CM-POS-003's, cash at the point of sale (a reading).
13. **The staff's permissions in POS** (SH-E-02382578): each permission is `core` on what it gates (the ruling after ZD-7): creating, editing and deleting customers on CM-CUS-001, customer metafields on CM-CNT-002; POS Channel > Staff, where the roles are set, on CM-POS-001. No line goes on CM-STF-002.
14. **'We' upgrading Shopify Email is a maker statement** (the ruling after SH-35). SH-E-32e5ccc3, on Shopify Email (an app: its link is `admin.shopify.com/apps/shopify-email/template-branding`), says “We've reduced empty space, introduced a new compact layout, and all footer text now supports rich text editing”. So its line on CM-MKT-007 is `own-service`, and so are the batch's two other Shopify Email posts, SH-E-d546e331 and SH-E-a4bd1d9e, whose own words name no maker: the statement is held in another source of the batch (M-1). Shopify Email is an app, a separate product, so the ruling on the platform's free themes doesn't reach it; the ruling after SH-53 on the Editions reads 'we' as Shopify the same way. SH-34 to SH-36 placed Shopify Email and Messaging `core` (CM-MKT-007, 7 lines); the coordinator may align them.
   - **Not read so:** 'We' launching or improving Shopify POS (SH-E-4654eb6a, SH-E-5f66cf1c, SH-E-85f1c81e) stays `core` on CM-POS-001, whose capability is in-person selling 'from the platform's own POS app', as SH-34 to SH-36 placed 42 POS lines; and 'We' improving the Theme Store (SH-E-a17fbfe5) or the App Store's recommendations (SH-E-ef87dd2e) is the platform's own marketplace, `core`.

## The new things

**`new:Admin loading`** (SH-E-0fcc4288, line 115, `shows`): the admin's own speed.
- **The post:** 'With our latest update, the Shopify admin experience is now faster and smarter', with 'a significant reduction in load times'.
- **A place of its own:** none. It is the whole admin's behaviour.
- **Proposed:** no capability, the admin itself, as the coordinator read SH-34's admin look (then `out`); or, if the coordinator makes the admin's frame one thing, under it, beside Admin search, Saved views and Admin navigation (domain F, no parent).
- **Its name:** English, the title's 'admin loading'. No Arabic is held: the admin in Arabic isn't captured (`docs/GAPS.md`).
- **The terms I searched** (`caps --terms`): load time, loading, performance of the admin. The only hit by 'loading' is CM-CNT-001 (files). CM-OPS-001 (platform reliability) holds pods and recovery sites, availability under load, not speed.
- **Its leads:** CM-API-003 and CM-API-005, by name only ('access, data, may'). Neither is it.

**`new:Admin navigation`** (SH-E-7f9c4c73, line 116, `shows`): the admin's back buttons and breadcrumb trails.
- **The post:** 'With our new dynamic back buttons and breadcrumb trails, you can easily maintain context awareness and navigate through your workflows more efficiently', such as 'Products > T-shirt > Blue'.
- **A place of its own:** none. It is the frame of every admin page.
- **Proposed:** as Admin loading.
- **Its name:** English, the title's 'admin navigation'. No Arabic is held.
- **The terms I searched:** breadcrumb, back button, admin navigation. 'admin navigation' finds only the capabilities whose cells cite an admin navigation item (CM-CNT-001, CM-CNT-002, CM-SFR-001), none of them this.
- **Its leads:** CM-CAT-003 (collections, an example), CM-PAY-003 and CM-AIA-004 (by name). None is it.

**`new:Admin search`** (SH-E-2a4e0daf, line 223, `shows`): SH-36's new thing, the admin's own search, here search within Settings, 'on both desktop and in the Shopify app'.
- **A place of its own:** none in the post.
- **Its leads:** CM-NTF-001, CM-STF-001 and CM-ORD-010, by the post's examples ('modify order confirmation emails, add staff members, or manage taxes'), and CM-ONB-003. None is the search.
- It stands with SH-35's Saved views and SH-36's Admin search for the coordinator's decision.

## CHANGES, each read again against its source

- **CM-ORD-014** (reorder) holds nothing and becomes held, `core` (line 165, SH-E-eef79f2d).
  - The post: “A Buy again button displays on your order status page and orders page, to let customers reorder items that they've purchased”, now turned on or off in the checkout and accounts editor.
  - The cell's reading had 'No Shopify statement held shows a past order repeated', and its note says 'Who repeats the order, the buyer or the merchant, isn't stated'. The buyer repeating a past order from their account is the capability's thing (a reading). Kept.
- **CM-ORD-011** (order tags) holds nothing and becomes held, `core` (line 38, SH-E-d9b7f517).
  - The post: 'In your Shopify admin, a draft order now has a limit of 250 tags', created 'manually or automatically by an app', and deleted from the draft order details page.
  - Draft orders are the orders the merchant creates (CM-ORD-005, under CM-ORD-001), so their tags are read as order tags (a reading). The cell's note has 'Shopify's automations that tag orders, if any, would be domain F's CM-AUT-001'. Kept, but unsure: the cell is Salla's automatic tagging, and the post shows tags on draft orders, not on placed orders.
- **CM-MKT-007** (email and SMS marketing) gains `own-service` (lines 66, 100 and 180: SH-E-d546e331, SH-E-a4bd1d9e and SH-E-32e5ccc3). The maker statement is SH-E-32e5ccc3's “We've reduced empty space, introduced a new compact layout …” on the Shopify Email app (rule 14 above). Kept; the first two rest on M-1, and drop to `core` if a 'we' statement counts only in its own post.
- **CM-MKT-003** (automatic discounts) holds nothing and becomes held, `core` (line 34, SH-E-ec277bb3: “We’ve added a new eligibility section for automatic discounts”). SH-34 already makes it held, and the coordinator kept it; the model isn't amended yet. Kept.
- **CM-CHK-005** gains `own-service` (line 179, SH-E-335f447b: 'Checkout Blocks now lets Shopify Plus merchants set order value limits and block checkout'). Checkout Blocks is Shopify's own app by the ruling after SH-35, and the coordinator's check of SH-35 already gives this cell `own-service`. Kept.
- **CM-CUS-010** gains `own-service` (line 210, SH-E-a0e60b40: 'The Sign in with Shop button will be added to the customer account login page'). Shop's sign-in, on SH-S-0056, as SH-34 and SH-35 placed it. Kept.
- **CM-INV-006** (inventory transfers) gains `extension-point` (line 158, SH-E-d55a7f78: 'Gain better visibility of 3P transfers via Transfers APIs'). '3P' read as third parties, whose transfers come through the platform's API (a reading). Kept, the weakest: the post names no third party.
- **CM-MKT-006** (marketing automations) gains `extension-point` (line 136, SH-E-2f490db9: 'find templates that include tasks from specific apps, or to only see templates using apps already installed on your store'). Apps' tasks inside the store's automations. SH-35 gives the cell the same (SH-E-42ecf1fa, weak by the coordinator's check); this post is plainer. Kept.
- **CM-SHP-002** (shipping labels) gains `extension-point` (line 173, SH-E-c218e65b). For orders from Great Britain to Northern Ireland, 'Purchase labels directly from your carrier of choice or through a shipping app', linked to the App Store's shipping solutions category, after Shopify's own labels end there under the Windsor Framework. SH-35 gives the cell the same, from Managed Markets' partners. Kept.
- **CM-SHP-020** gains `core` (line 168, SH-E-14158f15: 'Merchants can edit HS codes and country of origin per product …', and 'merchants can now also set a default country of origin'). SH-34 and SH-36 already give it `core`; the model isn't amended yet. Kept.

## The other NOTEs

- **`own-service`, 7 notes:**
  - Shop (SH-S-0056; the ruling after SH-34): CM-CHN-002 twice (SH-E-bb56c278, SH-E-d2c9b09a) and CM-CUS-010 (SH-E-a0e60b40);
  - Checkout Blocks (the ruling after SH-35): CM-CHK-005 (SH-E-335f447b);
  - Shopify Email, which 'we' upgrade: CM-MKT-007 three times (rule 14 above).
- **Horizon's two lines** (SH-E-1ae5b4cf, SH-E-7845d291) are now `core` by the ruling after SH-53, so the checker prints no CHANGES line for CM-SFR-001.
- **'core on a product named with the platform's brand', 27 notes.** Each is a feature the post shows in Shopify's own admin, POS, checkout, analytics, payments or Flow, or in Shopify Credit, Collective, Forms, Tax, Capital, Bundles, Magic, Catalog, Order Printer or the Theme Store: `core` by what it shows (SH-34's rule 6; the ruling after SH-36 for a branded app with no maker stated). Shopify Order Printer (SH-E-824336c3) is the one new to these batches.
- **The first leads that hold nothing and that no line names:**
  - line 112, SH-E-6e934fa0: CM-DVT-006, by name ('live, update'). The post only announces the Summer '25 Edition, as SH-35's Winter '26 post;
  - line 188, SH-E-b1c80711: CM-ORD-003, by name ('can, customize'). The post's words are POS's colour theming;
  - line 214, SH-E-5f990a58: CM-API-010, by 'conditions'. The words are a smart collection's category conditions.
- **The new things' leads:** above.
- The checker printed no NOTE for a quote it didn't find, an app's embedded page or a container. SH-E-dd79056c's footnote ('*Your store must meet the eligibility criteria for benchmarks.') is read with its entry and quoted in its CM-ANL-001 line.

## Entries I couldn't tell, and what would settle each

1. **SH-E-0fcc4288 and SH-E-7f9c4c73, the admin's speed and navigation:** `new`, or `out` as the admin itself. To settle: the coordinator's decision on the admin's frame, with Admin search and Saved views.
2. **SH-E-d9b7f517, draft order tags, on CM-ORD-011** (the CHANGES). The alternative is CM-ORD-005 alone. To settle: the coordinator's reading of whether CM-ORD-011 is any tags on orders or Salla's automatic tagging.
3. **SH-E-d546e331 and SH-E-a4bd1d9e, Shopify Email `own-service` by another post's 'we'** (rule 14). To settle: the coordinator's reading of M-1 for a 'we' statement held in another post on the same app, and SH-34 to SH-36's Shopify Email lines aligned to it.
4. **SH-E-d55a7f78's '3P transfers'** on CM-INV-006 `extension-point` (the CHANGES). If '3P' doesn't name third parties doing transfers, the line is `core` only.
5. **SH-E-fe4aa8d7, Shopify Magic's theme blocks,** on CM-AIA-003 (Shopify Magic is the cell's own term) and CM-SFR-002. CM-AIA-003 is text the AI writes; a block is code. The alternative is CM-AIA-001. To settle: the coordinator's reading of CM-AIA-003.
6. **SH-E-bef8840b, cash rounding,** on CM-POS-003 (a reading) beside CM-POS-001. The alternative is CM-POS-001 alone, or CM-PAY-016 for cash as a payment method.
7. **SH-E-27376dfb, POS payment controls:** manual card entry on CM-PAY-021, split payments on CM-PAY-020 (a reading) and mark as paid on CM-PAY-016, each an item of the post's list of new controls. The alternative is CM-POS-001 alone, a setting of POS (SH-34's rule 8).
8. **SH-E-d5fbd932, customer data erasure for third-party apps:** `core` on CM-TRU-007. The post says the requests are 'initiated by partners', with no interface named. If that is read as partners requesting erasure through the platform, the line is `core;extension-point`.
9. **SH-E-07fb18c8, a line item split across locations at checkout,** on CM-SHP-005 (order routing, a reading). The alternative is CM-SHP-009.
10. **SH-E-0b272f81's 'view as' in the product section** takes CM-CAT-001 as the place of a Markets feature (SH-34's rule 7(b)). The alternative is no line.
11. **SH-E-124a02ba, PayPal Wallet disputes,** on CM-PAY-009 and CM-PAY-013, PayPal the filler of both; Seller Protection is PayPal's. Its help link is under Shopify Payments in the United States, which the post doesn't state, so it has no scope.

## Items and sources

- **The entries agree with the page I read.** I read entry 1's record whole: `raw/runs/20261030T234414Z-merchant-changelog-feed-posts/fetch.warc.gz@1533673` (from `held_index.py`). Its date 'August 19, 2025', `h2` title, `post__content` and area 'Admin' are the entry's. I read no other page and no run step.
- **`show --meta` prints the feed's descriptive keys** (`changelog.shopify.com@feed`, 1,645 items), not those of `@posts`, as SH-34 to SH-36 found.
- **Some entries' texts end with their links cut** at `--width 3000` (SH-E-3a394a79, SH-E-3535373d): their posts' texts printed whole, and only the list of action links was cut.

## For the second stage: stated, or named in passing, and not placed

- **Checkout Blocks' other jobs,** each named as a way to customize a post's feature (rule 5 above): which pickup locations show to which customers (SH-E-a9fb0eb9), for CM-SHP-013; Apple Pay's availability (SH-E-4fa44da1) and each buyer's manual payment methods (SH-E-0e256da5), for CM-PAY-019. With Checkout Blocks Shopify's own (the ruling after SH-35), either would give its cell `own-service`.
- **Line-item properties** in the POS cart (SH-E-57188961: 'different customizations (through line-item properties)'): a lead for CM-CHK-009, order options and custom fields, which holds nothing on Shopify.
- **Tips on POS's customer display** (SH-E-1bdef4a3: 'Cart, Tips (if enabled), Receipt, and Thank You screens'; SH-E-63c92bd6: 'the Cart and Tips screen'): more leads for SH-35's Tipping, named in passing.
- **The marketplace facilitators' tax** (SH-E-1766e39f): 'Marketplace facilitators such as Amazon, Etsy, Meta and Tiktok are responsible for the collection and remittance of sales tax on behalf of sellers using their platform', a lead for CM-TAX-003 beside SH-36's Meta case (SH-E-bf3916cd).
- **Countries the posts leave to their help pages:** Shopify Collective's '36 additional countries' (SH-E-fbb1ce2f), USDC's 'eligible markets' (SH-E-ff639531), and 'all Shopify Payments countries' for Apple Pay on subscriptions (SH-E-316facbd). The help pages aren't read by this pass. They are for the market subjects.
- **The Flow posts' API changes,** each a developer changelog post linked from it (`dev-changelog`):
  - 2025-07 (SH-E-8cfd3ad5): return quantity tracking, the transactions' device, location and currency exchange fields, the mutations that add or remove an order's customer;
  - 2025-04 (SH-E-9a370a05): discount and subscription contract query filters, the customer's `defaultEmailAddress`, new revocation and rejection reasons, new card brands;
  - 2024-10 (SH-E-15858360): the products query's filters, `Order.statusPageUrl`, the gift card mutations.
- **Flow's templates with SendGrid and Airtable** (SH-E-9efb33c1, SH-E-3535373d): third parties' services reached by Flow's Send HTTP request action, named in a list of templates. A lead for CM-NTF-004 (message delivery providers).
- **App listings that would give maker statements,** each `not-attempted` in `index/ledger/sitemap--apps-shopify-sitemaps.tsv`: `apps.shopify.com/shopify-order-printer` (new in these batches), `shopify-bundles`, `shopify-forms`, `flow`, `collective-supplier` and `checkout-blocks`. `collective` is `captured`. They are exists-not-captured, for the coordinator to decide.
- **Named in passing, with no line:** the Theme Store's 'over 800 industry-inspired themes' (SH-E-a17fbfe5); 'More visual customizations are coming soon' for POS Terminal (SH-E-63c92bd6); 'We will be expanding support to include ShopifyTax' for ship and carry out (SH-E-5f66cf1c), which SH-E-37a51cf5 then states; 'We're working on supporting these requirements in the Shopify admin in the future' for the Windsor Framework (SH-E-c218e65b).
- **Each post's Help Center link** describes its feature further. They aren't read by this pass.

## Problems with the brief or the scripts

1. **`show --meta` prints the feed label's keys** for this structure, not those of `@posts` (as SH-34 to SH-36 found).
2. **The checker's CHANGES repeat cells that SH-34 to SH-36 already change** (CM-MKT-003, CM-CHK-005, CM-CUS-010, CM-MKT-006, CM-SHP-002, CM-SHP-020), since the model isn't amended between batches. They are listed above, kept, with that said.
3. **The brief's rule 4 reads differently from B-extent** for a changelog post that names a branded app ('`extension-point` where it names an app'). B-extent governs, as SH-34's notes said (their problem 4), and the ruling after SH-36 now says the same: such apps are `core` by what the post shows, with the maker a gap.
4. **A row can't hold a straight double quote,** so text that holds one is named unquoted (the rules above).
5. **The rulings changed during the batch** (four, listed above). The one on the platform's free themes changed two lines, which I corrected before the final check.
6. **How I kept the cost down:** chunks of 10 posts, each printed once with its leads; one lookup call for each chunk's cells, printing only their names, notes and placements; one archived page read.

## The coordinator's check (31 October 2026, after the batch)

- **The cell changes stand, each read again:**
  - CM-ORD-014 is `core`, from the customers' Buy again button;
  - CM-ORD-011 is `core`. It is order tags as well as automatic tagging, so draft orders' tags are its thing;
  - CM-MKT-007 is `own-service`;
  - CM-CHK-005 and CM-CUS-010 are `own-service`;
  - CM-MKT-006, CM-SHP-002 and CM-INV-006 gain `extension-point`, the last the weakest, as the notes say.
- **Shopify Messaging, formerly Shopify Email, is Shopify's own app** (the ruling after SH-37). This batch's three lines are `own-service`, and the nine earlier lines on it in SH-34 to SH-36 are aligned.
- **The admin's frame is `out`:** Admin loading (SH-E-0fcc4288) and Admin navigation (SH-E-7f9c4c73), by the ruling after SH-37. Admin search stays a new thing.
- **Kept as the agent corrected them:**
  - the Horizon themes are `core`, by the ruling after SH-53;
  - Shop's subscriptions sit on its channel only;
  - two lines take their own scope, by the ruling after SH-69.
- **Rules 1 to 14 stand for SH-38 to SH-46,** with rule 1 changed by the ruling on the admin's frame.
- **Cost:** 31.8 million tokens over 98 requests, about 245,000 an entry. The context reached about 530,000 tokens, past the prompt's 250,000.
