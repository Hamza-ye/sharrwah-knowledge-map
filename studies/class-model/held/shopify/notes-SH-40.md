# SH-40: Shopify's merchant changelog, posts 781 to 910 (notes)

**The batch:** platform `shopify`, batch `SH-40`, effort `high`. Its 130 entries are posts 781 to 910 of `merchant-changelog` as `@posts` holds them: `structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl`, lines 781 to 910, at observed-sh `e38dc17e3`. They are dated 1 March 2024 back to 30 August 2023, and all come from the run `20261030T234414Z-merchant-changelog-feed-posts`.

**What I read:** the brief, and what it names:
- the evidence map;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, and its `REGISTER.tsv` row for `shopify/merchant-changelog`. The changelog has no ledger denominator ('no sitemap: 404');
- `show --meta` (the `@posts` label's keys: 1,646 posts) and `selection.tsv`'s row (`placement` `where`, rule `labels:@posts;drop:run,status,class;long:20000`);
- B-extent's "Cells and evidence" and its conventions, with "What a place of its own is";
- the coordinator's rulings, their last section included (after SH-2 and SH-55);
- SH-34's notes in full, and SH-35's to SH-39's rules and the coordinator's checks. I read earlier batches' placements by line only where an entry of mine was of the same kind: POS custom discounts, test drives, the checkout customizations report, Checkout Extensibility, Shopify Forms, Shopify Bundles, Shopify Audiences, Stocky's extensions, Shop Pay, multiple captures, customs documents, the permissions posts.

`held_entries.py earlier` printed one line for the whole batch: SH-E-0942ae2c's label on CM-EVO-001 `core` (SH-56), and SH-E-980bd959's on CM-MKT-012 `own-service` (SH-55). I kept to both. No placements of SH-41 to SH-46 existed when I finished.

**Counts:**
- 130 entries on 207 lines, all `capability`; none `new`, none `out`.
- By support: `core` 155, `own-service` 33, `shows` 7, `extension-point` 5, `core;extension-point` 3, `own-service;extension-point` 2, `core;own-service` 1, `core;outside` 1.
- Lines per entry: 78 entries take one line, 36 two, 14 three, 1 five (SH-E-9fb7f4c4, Hydrogen's Winter '24 update) and 1 ten (SH-E-b1dcdb77, the 12 order permissions). In all they reach 88 capabilities.
- 33 lines carry a scope, 7 a filler, 12 a quality.
- The checker's final line: `130 of 130 entries placed; 0 problems`.

## The rules my lines follow

I kept to SH-34's rules 1 to 14, SH-35's 1 to 10, SH-36's 1 to 13, SH-37's 1 to 14 (rule 1 as the ruling on the admin's frame changed it), SH-38's 1 to 12, SH-39's 1 to 14, and the rulings after SH-34 to SH-38, SH-2 and SH-55. Every reading begins with the post's date and type tag, then its release words. Every quote is copied from the entry's own text, but three that cite another held entry by its id, which the checker finds: the Shopify Bundles app's maker statements the ruling after SH-38 names (SH-E-88c8359c, SH-E-1d272a37), and SH-E-3598937f of this batch. Where the quoted words hold an apostrophe, straight or curly, or the source's own ‘ ’, the quote is in “ ”. Text that holds a straight double quote is named unquoted (SH-34's rule 14): the price after discount field (SH-E-67574605), Transfer ownership (SH-E-a1fcc950), the Sales Rep role (SH-E-746b5618), Revert to original (SH-E-4b075d53), Log out from store (SH-E-9097d591), More actions (SH-E-8d2e88ff), Buy 2 items, get $10 off (SH-E-eb421742), low stock and Browse templates (SH-E-adfe143f).

**The first-party apps, by the ruling after SH-55:** Flow (8 lines), Collective (8), Search & Discovery (2), Shopify Bundles (3), Shopify Audiences (2), Shopify Subscriptions (2), Inbox (3), Translate & Adapt (1) and Stocky (1) are `own-service`, each reading citing its maker statement. Shop's things (Shop Campaigns, the Shop channel) are `own-service` on SH-S-0056. Shopify Forms stays `core`, its maker a gap (2 lines).

Where a kind of post came up that those rules don't cover, I followed the rule below. These are readings, mine, for the coordinator to align with SH-41 to SH-46.

1. **A limit Managed Markets sets on orders to listed countries** (SH-E-9389043a: 'Markets Pro will limit orders by order value in the following countries') is a quality of CM-MKS-003, its values by country, the countries its scope. I didn't read the values as market data: the platform sets them 'to protect merchants from loss of product'. I didn't place it on CM-CHK-005, whose thing is app-written rules, by its name.
2. **Home's metrics** (SH-E-b281045b, SH-E-8fbf9fe2, SH-E-2274a4df) are CM-ANL-003's, whose cell holds Home > Home. The metrics' names are a list and take no line, the POS ones included.
3. **An export of the platform's own bills** (SH-E-20a1a9a0, the billing charges' CSV) stays on CM-PLN-004 alone. SH-37's rule 3 puts a store's CSV export on CM-MIG-001, but CM-MIG-001's thing is the store's data (products, customers, orders), and a bill is the platform's charge to the merchant. An import of data into a new store (SH-E-a733fafd) does take CM-MIG-001.
4. **Collective's handling of orders between its partners** (SH-E-3500567a's cancellation requests, SH-E-5a5ae6a3's automatic cancellation after 14 days, SH-E-f0da28c6's payment status) takes CM-CHN-005 alone, as SH-39's rule 9 has payment status. The orders are what it acts on. Discovery's search and filters for retailers (SH-E-850b28ae, SH-E-e90a262c) take CM-CAT-010 `shows` beside it (SH-39's rule 9).
5. **A retired app replaced by the platform's own settings, with third-party apps named for one case** (SH-E-f7e7acad, the Geolocation app): one line on the replacement's capability, CM-MKS-004, `core;extension-point`, the case (a store selling to the EU through an EU top-level domain) in `reading`. The app's own words ('Shopify’s Geolocation app') take no line, since it is retired with a replacement (SH-34's rule 9). The Shopify Privacy & Compliance app, folded into the admin's Customer privacy section (SH-E-2a28fcaa), is read the same way.
6. **A gift card sent to a recipient with a personalized message** (SH-E-1b304b2b) is gifting, `core` on CM-LOY-006, beside gift cards (CM-LOY-002). This is a reading: CM-LOY-006's thing is 'buying a product for someone else, with its message and card'. It changes the cell (see "CHANGES").
7. **A gift card's emails or SMS** (SH-E-2115a090, SH-E-d37a4d35) take CM-NTF-001 beside CM-LOY-002: messages the store sends its customers.
8. **A Shop Pay post that names Shop's site** (SH-E-e1c51ac9: 'rendered on shop.app') is `own-service` on CM-PAY-014. That rests on the cell's maker evidence (the Shop Pay Merchant Terms, SH-S-0411, SH-S-0413) and on Shop (SH-S-0056), as SH-34 placed SH-E-eedc9ee3. The conversion tracking it enables takes CM-MKT-009.
9. **Shopify Collabs** (SH-E-8c4c619e) is `own-service` on CM-MKT-015, on the cell's own maker evidence (publisher Shopify Inc., SH-S-2760) and the Editions card that calls it 'our creator platform' (SH-E-709b37e4, SH-50). The ruling after SH-55 doesn't list Collabs; I followed the cell.
10. **A default for one plan** ('Enabled by default for Plus merchants', SH-E-c44a4b92) goes in `reading`, not `scope`, as a flag's value does (the brief's rule 4). The post names no plan the feature is limited to.
11. **A merchant's responsibility a post names** takes a `shows` line on the capability whose terms it gives (M-9): SH-E-db585144's state rules on tax-inclusive pricing (CM-TAX-001), SH-E-05d46f19's duties and label cost on Markets Pro's mark-as-paid orders (CM-TAX-008).
12. **Shopify Tax** is `core` on CM-TAX-002. 'available exclusively for merchants using Shopify Tax' is the store's own setup, in `reading` (SH-34's rule 10). The places its report is reached from take their lines (SH-34's rule 7(b)): the United States tax settings (CM-TAX-001) and Reports (CM-ANL-002). The Tax Platform, through which partners' tax services connect (SH-E-2308aaa9, Vertex, Inc. its filler), is `extension-point` on CM-TAX-004.
13. **The Shopify Subscriptions app's release** (SH-E-720a45b9) takes CM-SEL-001 and CM-APP-011 `own-service`, as SH-54 placed its Editions card (SH-E-4c0f3472). It also takes CM-CUS-010 `core`, for the customer accounts where buyers pause or skip their subscriptions. I first drafted that line `own-service`. I changed it because the customer accounts are the platform's own place; the pausing is the app's, on its CM-SEL-001 line.
14. **A POS device Shopify sells** (POS Terminal, SH-E-dbb979f6; POS Go, SH-E-3c7bd870) is `own-service` on CM-POS-002 (SH-35's rule 6, SH-39's rule 4), its countries the scope. Where the post states the payments it takes (POS Terminal's 'tap, chip, and swipe payments'), it takes CM-PAY-021 and CM-POS-001 too. POS Go's parts are named in a list and take no line.
15. **Checkout Extensibility** (SH-E-78cdebe9, SH-E-99c22731) is `extension-point` on CM-CHK-004, by the capability's own definition, as SH-50 placed it (SH-E-85cba08f). The checkout editor and the customizations report are `core` on CM-CHK-003. The checkout.liquid deadlines are in `reading` (SH-34's rule 9).

## The new things

None. Every post found a capability. The admin's own frame came up nowhere in this batch. The metaobjects' saved views (SH-E-0b0e5c58) are named in a list and take no line, so SH-35's Saved views gains no entry.

## CHANGES, each read again against its source

The checker's CHANGES repeat cells that earlier batches already change, since the model isn't amended between batches:
- CM-AUT-001, CM-CHN-005, CM-MKT-011, CM-SEL-001, CM-SEL-006, CM-SFR-013 and CM-MKS-008 gain `own-service`: Flow, Collective, Audiences, Subscriptions, Bundles, Search & Discovery and Translate & Adapt, by the rulings after SH-35, SH-38 and SH-55, as SH-36 to SH-39, SH-54 and the coordinator's alignments have them;
- CM-INV-006 gains `own-service`: Stocky's transfers extension (line 168), as the Editions batch placed the same extension (SH-E-eddcf8ad);
- CM-MKT-003 becomes held and `core`: the automatic free shipping discount, 'without requiring them to input a code' (line 196), as SH-34's check made the cell;
- CM-SHP-020 gains `core`: Markets Pro's customs documentation (line 103), as earlier batches placed Managed Markets' customs documents.

One CHANGES line is this batch's own:
- **CM-LOY-006 gains `core`** (line 108, SH-E-1b304b2b). 'Customers can now add a recipient and personalized message to gift cards, as well as schedule their gift card to be sent at a specific time, for a more personal, thoughtful and convenient gifting experience.' The buyer buys a gift card for someone else, with a message, through the platform's own gift card fields (rule 6 above). The cell held only `extension-point`, from the App Store's Gift wrap and message apps. I kept the line. If the coordinator reads gifting as a product other than a gift card, it goes.

## The other NOTEs

- **`own-service`** (36 notes): each line's reading cites its maker statement. The statement is the ruling's for Flow, Collective, Search & Discovery and Bundles; a post's 'we' for Audiences; the Editions' 'our' for Subscriptions and Collabs; and the cell's own maker evidence for Inbox (SH-S-2758), the POS hardware (SH-S-7269, SH-S-7251), Shop Pay (SH-S-0411, SH-S-0413) and Shop (SH-S-0056).
- **`core` on a product named with the platform's brand** (20 notes): each is a surface of the platform's own, `core` by what the post shows. They are the App Store, Editions, the Admin API's fixed bundles, the mobile app, Shipping labels, Duties and Import Taxes, Shopify Tax, Balance, Payments' captures, POS, the checkout and Markets. Shopify Forms is `core` with its maker a gap (the ruling after SH-55).
- **Line 193's first lead,** CM-ORD-013 (an order's notes and comments, which hold nothing on Shopify), came by the word 'messages'. Inbox's messages are chats with buyers, not an order's notes, so the entry isn't its thing.

## Entries I couldn't tell, and what would settle each

1. **SH-E-1b304b2b, gifting** (CM-LOY-006): is a gift card sent to a recipient the capability's 'product for someone else'? The coordinator's reading of the definition would settle it.
2. **SH-E-04e0deb0, digital products for B2B** (CM-SEL-002 `shows`): the post shows digital downloads sold to business buyers, but not who delivers the files. Its help page (`help.shopify.com/en/manual/products/digital-service-product`) would settle whether the platform does.
3. **SH-E-6e5c5c9e, fulfillable inventory** (CM-INV-001 `shows`, 'available to select merchants'): the setting's place isn't named. Its help page sits under shipping, which could make it CM-SHP-001's too.
4. **SH-E-3500567a and SH-E-5a5ae6a3, Collective's cancellations:** CM-CHN-005 alone (rule 4 above), or CM-ORD-004 too, since an order is cancelled. A ruling on Collective's order handling would settle it.
5. **SH-E-9389043a, Markets Pro's order value limits:** whether they are a checkout's validation (CM-CHK-005 is app-written rules, by its name) and whether the values per country are qualities or the subjects' market data (rule 1 above).
6. **SH-E-20a1a9a0, the billing export:** CM-PLN-004 alone (rule 3 above), or CM-MIG-001 too, by SH-37's rule 3 read widely.
7. **SH-E-5fa984ca, indexing** (CM-CNT-007, Google its filler): 'non-primary market content is not indexed by search engines to comply with Google guidelines' is read as the SEO capability's thing. The cell otherwise holds no built-in SEO.
8. **SH-E-075f0ce0, Balance's reward** ('a reward provided by Shopify and is not interest'): `core`, as Balance is the platform's own account, not a separate product. If the coordinator reads 'provided by Shopify' as a maker statement for a separate service, it is `own-service`.
9. **SH-E-22b71ca5, '(Shopify Plus)':** the item holds a broken Markdown link, '[Build a custom bundle offering](https://shopify.dev/docs/apps/selling-strategies/bundles (Shopify Plus)'. I read the post's page (`raw/runs/20261030T234414Z-merchant-changelog-feed-posts/fetch.warc.gz@6475069`, line 212 of its text), which holds the same paragraph. I read the mark as the custom offering's condition, as SH-E-3598937f states 'Shopify Plus and Shopify partners only' for 'our APIs'. That is the only post page I read.
10. **SH-E-0942ae2c, test drives:** its scope, Shopify Plus, comes from its title ('… before they rollout in Shopify Plus'), as SH-E-c2e9c92b's line has it. Its area, Plus, isn't read as scope (SH-34's rule 3).

## Items and sources

The one page I read (SH-E-22b71ca5) agrees with its item. Three things in the posts themselves, kept as they stand:
- SH-E-dc107484 (Translate & Adapt) links its two 'Translate & Adapt app' texts, through a Google redirect, to the Search & Discovery app's listing (`apps.shopify.com/search-and-discovery/`). I placed the post by its words and its help link, the Translate & Adapt help page.
- SH-E-a1fcc950's 'Shopify Plus Support' link is `http://https://help.shopify.com/en`.
- SH-E-eb421742's text ends with '? Learn more … -->', an HTML comment's remnant in the post.

## For the second stage: stated, or named in passing, and not placed

- **CM-MKS-005's cell** reads that changing the store currency after the first sale needs Shopify Support (SH-S-0671, SH-S-0370). SH-E-a7a4b8e0 (23 February 2024) says 'Merchants can now make this change themselves from within the Shopify admin'. The cell's reading should be read again against the current help page.
- **Package protection 'using third party apps'** for B2B orders (SH-E-04e0deb0) is named in a list of non-physical products. No capability holds third-party package protection; CM-SHP-003 is insurance on the platform's own labels.
- **A legacy United States POS sales tax service** retired: only SH-E-1faed239's community link names it (`community.shopify.com/c/accounting-and-taxes/retiring-a-legacy-united-states-point-of-sale-sales-tax-service/td-p/2277016`).
- **Returns' accounting for apps:** SH-E-7daf6ca5 links the developer changelog's `return-mutation-will-update-sales-previously-unchanged-until-time-of-refund`, a lead in `dev-changelog`.
- **The server pixel API** (`shopify.dev/docs/api/admin-graphql/2023-04/queries/serverPixel`, SH-E-ecf44c9b), a lead for CM-MKT-009's API.
- **The Checkout Extensibility Hub** (`www.shopify.com/plus/upgrading-to-checkout-extensibility`, SH-E-78cdebe9), a lead for CM-CHK-004.
- **Shop's reach,** 'over 100M engaged buyers who use Shop' (SH-E-710447f0): a count, not a quality, for CM-CHN-002's reading.
- **Things named only in lists** that took no line, each a lead for its cell:
  - Hydrogen v2023.10's API client for the Customer Account API and its stable cart methods (SH-E-f16cd2ea);
  - POS Terminal's tipping and PIN flows (SH-E-dbb979f6);
  - Shop Campaigns' customer cohorts (SH-E-980bd959);
  - Customer privacy's data opt-outs and data storage information (SH-E-2a28fcaa; CM-TRU-005);
  - a Markets Pro order's default country of origin, Taiwan, changed only through Shopify Support (SH-E-ea54f3da; CM-SHP-020).

## Problems with the brief or the scripts

1. **The checker didn't find one quote of another entry cited by its id:** 'our new, free subscriptions app' (SH-E-4c0f3472, `editions-page-data`) was 'found nowhere held', though 'our new, free bundles app' (SH-E-1d272a37, of the same structure) was found. I unquoted it, and Collabs' 'our creator platform' (SH-E-709b37e4) with it, before the checker could test that one.
2. **The checker refused a filler holding parentheses,** 'United States-Mexico-Canada (USMCA) free trade agreement', which the entries' texts hold exactly. 'USMCA' passes, and the full name is in `reading`.
3. **The checker doesn't flag a single-quoted quote that holds an apostrophe** (as SH-39 found). A scan of my own found five, four with a curly apostrophe and one with a straight one, and I changed them to “ ”.
4. **The checker's CHANGES repeat cells earlier batches already change** (see "CHANGES"), and its brand NOTE fires on 20 lines.
5. **How I kept the cost down:** I printed each chunk of 10 posts once, with its leads and `earlier`, and made one lookup call per chunk for its cells and searches. I checked quotes and terms between the checker's runs with a script of my own, against a saved print of the batch. The checker ran seven times before the last. I read one archived page.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 130 of 130 entries, no problem.
- **The cell changes stand, each read again.** All but one repeat earlier batches' changes, which aren't amended yet: the first-party apps' `own-service` (the ruling after SH-55), Stocky's transfers, the automatic free shipping discount, Markets Pro's customs documents. CM-LOY-006's `core` (line 108), a gift card with a recipient, a message and a date, is the gifting SH-55's check kept.
- **Rules 1 to 15 stand for SH-41 to SH-46.** Among them: a default for one plan goes in `reading`, not `scope`; a merchant's responsibility a post names takes a `shows` line.
- **The tools, as this batch and SH-13 asked:**
  - the quote test follows a held entry's id a reading cites (`SH-E-…`), so a quote from another batch's maker statement passes, as 'our new, free subscriptions app' (SH-E-4c0f3472) now does;
  - the filler test takes a filler as written as well as without its parenthesis, so 'United States-Mexico-Canada (USMCA) free trade agreement' passes as the posts hold it.
- **Cost:** 28.6 million tokens over 101 requests, about 220,000 an entry. The context reached about 454,000 tokens.
