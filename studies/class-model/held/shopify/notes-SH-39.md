# SH-39: Shopify's merchant changelog, posts 651 to 780 (notes)

**The batch:** platform `shopify`, batch `SH-39`, effort `high`. Its 130 entries are posts 651 to 780 of `merchant-changelog` as `@posts` holds them: `structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl`, lines 651 to 780, at observed-sh `e38dc17e3`. They are dated 28 August 2024 back to 4 March 2024, and all come from the run `20261030T234414Z-merchant-changelog-feed-posts`, in the order SH-34's notes describe.

**What I read:** the brief, and what it names:
- the evidence map;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, and its `REGISTER.tsv` row for `shopify/merchant-changelog`. The changelog has no ledger denominator ('no sitemap: 404');
- `show --meta` (now the `@posts` label's keys: 1,646 posts) and `selection.tsv`'s row (`placement` `where`, rule `labels:@posts;drop:run,status,class;long:20000`);
- B-extent's "Cells and evidence" and its conventions, with "What a place of its own is";
- the coordinator's rulings, at the start and again at the end. Three were added while I worked: after SH-2 (a store listing that names the company is a maker statement, so Shopify Inbox is `own-service`; an admin section the platform calls part of its admin is `core`) and after SH-55 (a first-party app's own features are `own-service`, its plan lines `core`; Shopify Flow and Shopify Collective aligned). I aligned my lines to them before finishing (below);
- SH-34's to SH-38's notes with the coordinator's checks, and their placements, summed by capability and support, and read by line where an entry of mine was of the same kind (Collective's shipping, Search & Discovery, Shopify Forms, Inbox, Tap to Pay, the POS Hub, DHL's labels, address validation, the checkout and accounts editor, AI image editing, the Finance section in the Shopify app, Stocky in the Editions).

`held_entries.py earlier` printed no line for any key of the batch, chunk by chunk. No placements of SH-40 to SH-46 existed when I finished.

**Counts:**
- 130 entries on 225 lines: 224 `capability` lines and 1 `new` line, none `out`. Every entry but one (SH-E-44c35194, the Finance section) has at least one `capability` line.
- By support: `core` 163, `own-service` 42, `extension-point` 8, `shows` 8, `core;own-service` 2, `core;extension-point` 1, `core;outside` 1.
- Lines per entry: 59 entries take one line, 54 two, 13 three, 2 four (SH-E-fbee6206, SH-E-f2616edb), 1 five (SH-E-35e5b666) and 1 six (SH-E-448d7a8f). In all they reach 86 capabilities and 1 new thing.
- The checker's final line: `130 of 130 entries placed; 0 problems`.

## The rules my lines follow

I kept to SH-34's rules 1 to 14, SH-35's rules 1 to 10, SH-36's rules 1 to 13, SH-37's rules 1 to 14 (rule 1 as the ruling on the admin's frame changed it), SH-38's rules 1 to 12, and the rulings after SH-34 to SH-38, SH-2 and SH-55. Every reading begins with the post's date and type tag, then its release words. Every quote is copied from the entry's own text, so none cites a record. Where the quoted words hold an apostrophe, straight or curly, or the source's own ‘ ’, the quote is in “ ”. Text that holds a straight double quote is named unquoted (SH-34's rule 14): the More actions menu (SH-E-6218a81f), the Add to Cart button (SH-E-4ab2a77d), the Imported products status (SH-E-4d5c8759), the template names of SH-E-735a19e3, the typical margin of SH-E-126d2a7e, the Errors tab of SH-E-26827e6a.

**Aligned to the rulings made while I worked:**
- **Shopify Flow** (11 lines on CM-AUT-001) and **Shopify Collective** (14 lines on CM-CHN-005) are `own-service`, by the ruling after SH-55, each reading citing the maker statements the coordinator named: SH-E-0678ff26 and SH-E-aca9896c for Flow; SH-E-850b28ae and 'the Collective app' for Collective. SH-E-735a19e3's own 'We have released three new fulfillment related tasks in Flow' is a maker statement too. The Collective lines on CM-SHP-001 (shipping profiles) and CM-CAT-010 (`shows`, its note) stay as SH-38's are.
- **Shopify Inbox** is `own-service` on CM-SUP-004 (SH-E-6a30460f), on the cell's own maker evidence (SH-S-2758), as the ruling after SH-2 now has it. Its Shopify Magic line on CM-AIA-003 stays `core`, as SH-38's Shopify Magic line in Search & Discovery (SH-E-dcab6e7d) stayed `core` after the coordinator's alignment: the platform's own AI, the app's feature taking the app's line.
- **Not aligned, no maker statement of an app of its own held:** Shopify Forms and the Shopify Combined Listings app stay `core`, the maker a gap (the ruling after SH-55 names Forms; `makers` finds nothing for Combined Listings). The Shopify Pixel Helper has 'we' (“We've added error messages to the Shopify Pixel Helper”, SH-E-0a66f16d), but no held words call it an app or say it is installed: SH-E-5f4f200c says merchants 'launch the Pixel Helper from the Shopify admin'. So it is `core` on CM-MKT-009, and what it is stays a gap. The Shopify app (mobile) stays `core` on CM-SRF-001, as every earlier batch's lines on it still are.

Where a kind of post came up that those rules don't cover, I followed the rule below. These are readings, mine, for the coordinator to align with SH-40 to SH-46.

1. **A feature withdrawn for one country, with a way named in its place** (SH-E-f438f3d7, Managed Markets no longer supporting Turkiye). The feature's line is `shows`, the country its scope, as the ruling after WC-5 has an offer stated unavailable where it is listed, and SH-38's rule 3 a retired feature with no replacement where the capability isn't its alone. The way the post names in its place (draft orders, the merchant as the merchant of record) takes its own `core` line, as SH-34's rule 9 has a replacement. The authority whose rule ended it (Turkish authorities) is the first line's filler; its value (30 euros) is the subjects'.
2. **Markets Pro is Managed Markets.** SH-E-dc501d64 states the rename ('Starting June 24'). Every Markets Pro post (SH-E-61b4af23, SH-E-80582147, SH-E-ab22e66d, SH-E-7ea7c76b, SH-E-097c67f5) is `core` on CM-MKS-003, Global-e not named, and takes further lines only for what it names on another capability: labels and pickups (CM-SHP-002), shipping zones (CM-SHP-001), payouts (CM-PAY-005), the Orders page (CM-ORD-001), the product pages (CM-CAT-001). The rename's 'Shopify Markets will be renamed International in the Help Center' takes CM-MKS-001's line (SH-34's rule 9).
3. **Stocky is Shopify's own app.** SH-E-5b89aa16, “We’ve introduced the option to 'Edit' purchase orders in Stocky”, is the maker statement the Editions batch already read for Stocky (SH-E-eddcf8ad, on CM-INV-006), and SH-E-15f4f14d's “we’re leveraging Shopify’s POS UI extensions technology” builds its extension. So Stocky's purchase orders are `own-service` on CM-INV-007 (three lines). The admin's and POS's own inventory surfaces that show Stocky's data stay `core` (CM-INV-001, CM-POS-001). Stocky's extension on the Smart Grid is `shows` on CM-POS-004, by SH-38's rule 5, as the Editions placed its transfers extension.
4. **Card readers named in a payments post** (SH-E-c887d470, SH-E-a4d8576f: JCB and UnionPay on 'Shopify card readers'). Three lines: the card payment, `core` on CM-PAY-021 with the card network as filler and the countries as scope (as SH-38 placed Tap to Pay); Shopify POS, `core` on CM-POS-001 (SH-34's rule 8); and the readers, `own-service` on CM-POS-002, on the cell's maker evidence that the merchant 'may elect to purchase POS Equipment from Shopify' (SH-S-7269, SH-S-7251), as SH-35's rule 6 placed the POS Hub.
5. **The Finance section, a container with no capability** (SH-E-44c35194): `new:Finance`, `core` (M-13). Its title names no capability: CM-PAY-023's note says no capability holds the Finance suite as such, though that cell cites the suite (SH-S-0454) as where Balance sits. The products it holds are named in a list and take no line.
6. **The Shopify app's own navigation** (SH-E-4439a797: a sidebar in place of the tab bar on tablet) is `core` on CM-SRF-001. The ruling after SH-37 makes the web admin's frame `out` because no capability is the admin itself. CM-SRF-001 is the mobile app itself, so a change to the app's own frame is a change to its thing. If the coordinator reads it as the admin's frame, the line is `out`.
7. **The Shopify app's list screens** (SH-E-448d7a8f: long press and bulk actions on five lists): each list page takes its capability's line, by SH-38's rule 6, which the coordinator kept for these batches: abandoned checkouts (CM-CHK-007), collections (CM-CAT-003), customers (CM-CUS-003, since the change is bulk actions), customer addresses (CM-CUS-008), segments (CM-CUS-002), with the app's own line (CM-SRF-001). A list of *features* the app gains (SH-E-3da2c81a's draft orders, SH-E-ceca7de2's company details) takes no line per feature, by the ruling after SA-41: the section's own capability takes the line.
8. **A post whose link opens a Shop help page** (SH-E-682a2a87, Shop Promise, linking `help.shopify.com/en/manual/online-sales-channels/shop/shop-promise`) is about Shop's feature, by the ruling after SH-38. Two other held posts say what Shop does in it: 'Delivery dates are automatically predicted by Shopify and are backed by Shop with a limited guarantee' (SH-E-36918e68) and the 'Shop Promise limited guarantees in the Shop App' (SH-E-3911a36e). So the line on CM-SHP-018 is `core;own-service`: the platform's predicted date `core`, Shop's guarantee `own-service` on SH-S-0056.
9. **Collective's sourcing posts.** Where retailers import or find suppliers' products (SH-E-5e341d35, SH-E-ee2a7e1d, SH-E-2be90ff5, SH-E-2b1e99e9, SH-E-ffba21cf), the post takes CM-CAT-010 `shows` beside CM-CHN-005, as SH-36's rule 8 and SH-37's lines have it. Posts on the supplier's price lists, payment status or margins take CM-CHN-005 alone; on shipping profiles, CM-SHP-001 beside it, as SH-38 placed SH-E-453aad5e.
10. **A further line on one capability under its own condition** (the rulings after SH-34 and SH-69):
    - Audiences included on 'Shopify Plus or enterprise plans', and its 45-day free trial for “merchants who aren't on Shopify Plus” (SH-E-fb4f952d), two CM-MKT-011 lines;
    - multiple captures for Plus merchants in Australia and Romania, and the finalCapture parameter 'For all eligible merchants' (SH-E-08e08a77), two CM-PAY-020 lines;
    - shipping to Evri's points in the UK and to Correos's in Spain (SH-E-fbee6206), two lines each on CM-SHP-019 and CM-SHP-002;
    - functions in public apps on any plan, and in custom apps 'Only' on Shopify Plus (SH-E-35e5b666), two CM-APP-005 lines;
    - the Trade theme on all plans, and its B2B features 'exclusive to Plus' (SH-E-e070c1ae), the latter on CM-B2B-001 with Plus as its own scope.
11. **Carrier pickups** (SH-E-ab22e66d, DHL Express pickups scheduled in the admin): no capability holds a carrier's pickup of the merchant's parcels. I placed it on CM-SHP-002, the labels bought through the platform, whose Shopify Shipping pickups the post names, `core;outside`: recurrent pickups 'should continue to be scheduled via the DHL Express website'. CM-SHP-007 (local pickup) is the buyer's, a homonym.
12. **Order shipping address validation** (SH-E-8de93795) takes CM-CUS-008, by SH-38's rule 10. **Address autocompletion** (SH-E-dd5a9ed9) takes CM-CUS-009, whose Shopify cell holds 'address autocompletion' (S02-SH-240), and the checkout and accounts editor, where the setting moved (CM-CHK-003).
13. **The Order Status Page's sign-in** (SH-E-34bc5e79) is CM-CUS-010, as SH-36 placed the Order Status page among the customer account pages (SH-E-a267afc6).
14. **The storefront's CAPTCHA** (SH-E-a275a8ff, SH-E-15b24a07: hCaptcha in place of Google reCAPTCHA on 'a protected form' and the /challenge page) takes CM-CUS-012, the nearest capability, hCaptcha its filler. The posts don't name which forms are protected (see "Entries I couldn't tell").

## The new thing

**`new:Finance`** (SH-E-44c35194, line 8, `core`): the admin's Finance section, 'one place to view all your money products'.
- **The post:** 'The Finance section has been redesigned for US merchants and is now also available to merchants in all Shopify Payments-eligible countries in the left-hand navigation', holding 'Capital, Credit, Balance, Payments, Bill Pay, or Taxes'.
- **A place of its own:** an admin section, a navigation item with its own title ('in the left-hand navigation'; B-extent, "What a place of its own is"). Other posts name pages under it: 'Finance > Documents' (SH-E-827e9042), 'Finances > Payouts > Payout Details' (SH-E-314ed779), 'Finances / Payouts / Transactions' (SH-E-097c67f5, this batch), and the Shopify app's 'Finance section' (SH-E-3efa7510, SH-38, placed on CM-SRF-001 alone).
- **Its children, as the post names them:** Capital (CM-PAY-026), Credit (CM-PAY-025), Balance (CM-PAY-023), Payments (CM-PAY-002, CM-PAY-005), Bill Pay (CM-PAY-027), Taxes (the post doesn't say which; CM-TAX-009, the tax forms the platform issues, or CM-TAX-002).
- **Proposed:** domain C, area PAY, as the parent of CM-PAY-023, CM-PAY-025, CM-PAY-026 and CM-PAY-027, which CM-PAY-023's and CM-PAY-027's notes leave with no parent; or no capability, if the coordinator reads it as a grouping only (the rulings after SA-22 and SA-28). It is a container over one part of the admin, so M-13 keeps it.
- **Its name:** English 'Finance' (also 'Finances' in other posts). No Arabic is held: the admin in Arabic isn't captured (`docs/GAPS.md`).
- **The terms I searched** (`caps --terms`): Finance, finances, money products. The hits are the cells that name a finance product (CM-PAY-003, CM-PAY-009, CM-PAY-023 to CM-PAY-028, CM-APP-003, CM-TAX-009); none is the section.
- **Its leads,** which the checker's NOTE lists: CM-PTN-003 (partner payouts, by 'transactions'), CM-MKS-009 (by 'countries'), CM-PAY-005 (payouts, by 'account balance', a child), CM-PAY-024 (cards, by name) and CM-API-013 (by name). None is the section.

## CHANGES, each read again against its source

- **CM-CUS-012** (reCAPTCHA verification at buyers' sign-in and registration) holds nothing and becomes held, `core` (lines 21, 35: SH-E-15b24a07, SH-E-a275a8ff). The posts: “We’ve started migrating our CAPTCHA implementation on Storefronts to hCaptcha from Google reCAPTCHA as part of our ongoing effort to reduce form abuse”, the badge loading 'when a customer interacts with a protected form'; and the /challenge page's fallback challenge moving to hCaptcha. Kept, as a marked reading: the platform's own CAPTCHA on its storefront's forms is the thing, and sign-in and registration forms are the forms the capability names, though the posts name none. The alternative is `new:Storefront CAPTCHA`, `shows`, with no place of its own.
- **CM-CAT-013** (product pricing) gains `core` (line 61, SH-E-4d3e3dea, Unit Pricing for the EU and Switzerland). The cell held only `extension-point` (pricing apps), and its note says no platform defines product pricing. Unit pricing displays 'the price per unit for products sold in quantities or measurements', a product's own price information (a reading; its help link's path is `products/details/product-pricing/unit-pricing`). Kept, with doubt. The alternative is `new:Unit pricing`, `shows`, no place of its own (a product field), scope EU;Switzerland.
- **CM-INV-007** (purchase orders) gains `own-service` (lines 83, 86, 122): Stocky's purchase orders, on SH-E-5b89aa16's 'we' (rule 3 above). Kept.
- **CM-MKT-015** (creator and influencer marketing) gains `extension-point` (line 6, SH-E-0bbdd469): 'All eligible US Shopify Plus and Advanced merchants can now join the YouTube Shopping affiliate program through the Google & YouTube app on Shopify', so 'eligible creators can tag your products at scale in their videos'. YouTube's own programme through an app on the platform (M-8), YouTube the filler. Kept. The app's maker isn't stated (`apps.shopify.com/google` is `not-attempted`).
- **CM-SHP-018** (delivery promises) gains `own-service` (line 226, SH-E-682a2a87, Shop Promise), by rule 8 above. Kept, with the `core` the cell already holds beside it.
- **CM-AUT-001** and **CM-CHN-005** gain `own-service` (11 and 14 lines): the ruling after SH-55, which aligned the earlier batches the same way. Kept.
- **Repeated from earlier batches,** whose own lines already change these cells (the model isn't amended between batches), each kept: CM-SHP-020 `core` (customs forms, line 12; SH-34), CM-MKS-008 `own-service` (Translate & Adapt, line 206; SH-36), CM-MKT-007 `own-service` (Shopify Email, line 98; SH-37), CM-MKT-011 `own-service` (Audiences, lines 72 and 73; SH-38), CM-SEL-006 `own-service` (the Shopify Bundles app, line 102; SH-38), CM-SFR-013 `own-service` (Search & Discovery, lines 64, 65, 99, 155; SH-38).
- **Not kept:** my first line on SH-E-6a30460f's suggested replies gave CM-AIA-003 `own-service`. I set it to `core`, as the coordinator kept Shopify Magic `core` inside Shopify's own Search & Discovery app (SH-E-dcab6e7d) after the ruling after SH-55; the app's own line is CM-SUP-004's.

## The other NOTEs

- **`own-service`, 42 lines, and 2 `core;own-service`:** Flow and Collective (the ruling after SH-55); Search & Discovery (SH-E-9b869699); Shopify Email (SH-E-32e5ccc3); Audiences ('We’re releasing Shopify Audiences v2.3'); Translate & Adapt (SH-E-04551fad); the Shopify Bundles app (SH-E-1d272a37, SH-E-88c8359c); Stocky (SH-E-5b89aa16); Shopify Inbox (SH-S-2758); POS hardware (SH-S-7269, SH-S-7251); Shop Cash, Shop Campaigns, Shop Pay and Shop Promise (SH-S-0056, and the cells' own Shop Pay and Shop Campaigns terms).
- **`core` on a product named with the platform's brand, 41 lines:** each is a feature the post shows in Shopify's own admin, POS, mobile app, checkout, Theme Store or billing (Shopify POS, the Shopify app, Shopify Payments, Shopify Shipping, Shopify Magic, Shopify Balance, Shopify Credit, Shopify Markets, Shopify Account Credits, Shopify Function APIs), or a branded app with no maker statement held (Shopify Forms, the Shopify Combined Listings app, the Shopify Pixel Helper).
- **The new thing's leads:** above.
- **First leads that hold nothing and that no line names,** six, none the post's thing:
  - CM-OPS-004 (store status), by 'Order status pages' (line 125, SH-E-7053ec17), 'product status' (line 195, SH-E-4d5c8759) and 'toggling tools' (line 218, SH-E-d5e9541b);
  - CM-CAT-005 (product brands), by 'gave brands more power', the merchants (line 174, SH-E-937cfee3), and 'new brands to collaborate with', the suppliers (line 223, SH-E-ffba21cf).
- The checker printed no NOTE for a footnote mark, an app's embedded page or a container.

## Entries I couldn't tell, and what would settle each

1. **SH-E-44c35194, the Finance section:** `new:Finance` (above). To settle: the coordinator's choice between a new container, CM-PAY-023 (whose cell cites the finance suite, SH-S-0454), and no capability.
2. **SH-E-a275a8ff and SH-E-15b24a07, the storefront's CAPTCHA, on CM-CUS-012** (the CHANGES). To settle: the developer docs page the first post links (`shopify.dev/docs/storefronts/themes/trust-security/captcha`), which would name the protected forms. The shopify.dev sitemap is held, but this pass doesn't read a post's links.
3. **SH-E-4d3e3dea, Unit Pricing, on CM-CAT-013** (the CHANGES). To settle: the coordinator's reading of product pricing, or the help page `products/details/product-pricing/unit-pricing`.
4. **SH-E-0bbdd469, the YouTube Shopping affiliate program:** CM-MKT-015 (creators tagging products) and CM-CHN-004 (products synced to YouTube), `extension-point`. The alternatives are CM-MKT-013, the parent of affiliate and creator marketing, or CM-MKT-014; but that is affiliate marketing run by the store, and YouTube runs this one.
5. **SH-E-ab22e66d, DHL Express pickups, on CM-SHP-002** (rule 11 above). To settle: the coordinator's decision whether carrier pickups are part of the labels service or a new thing (`new:Carrier pickups`, `shows`).
6. **SH-E-682a2a87, Shop Promise, `core;own-service`** (rule 8). The alternative is `core` alone, on the cell's own Shipping route (`shop-promise-examples`).
7. **SH-E-4439a797, the Shopify app's navigation, `core` on CM-SRF-001** (rule 6). The alternative is `out`, as the web admin's frame is.
8. **SH-E-448d7a8f, six lines** for the Shopify app's lists (rule 7). If the coordinator reads the ruling after SA-41 over SH-38's rule 6 here, only the CM-SRF-001 line stays.
9. **SH-E-35e5b666, Discount Functions on POS, five lines.** The two CM-APP-005 lines rest on the post's 'Important information: Limitations', which restate the functions' plan conditions the cell already holds (SH-S-0682, SH-S-7076). If the coordinator reads them as background, they go, and the post keeps CM-MKT-004, CM-POS-001 and CM-MKT-001.
10. **SH-E-e680a8ac, customs forms of Managed Markets orders:** a CM-MKS-003 line beside CM-SHP-020 and CM-SHP-002. The alternative is no CM-MKS-003 line, Managed Markets being the orders the forms are for.
11. **SH-E-adc6508a, customer receipt selection:** CM-POS-001, CM-ORD-009 (receipts) and CM-CUS-001 (customer emails). POS's matching of 'payments from POS transactions to buyers in the Shop Pay network' is kept in reading. It may be a lead for CM-TRU-008, the platform's own use of customers' data across merchants, or a Shop Pay `own-service` line on CM-PAY-014.
12. **SH-E-03c207ce, POS checkout validation:** its staff attribution stays on CM-POS-001, as SH-34 placed POS's staff attribution (SH-E-ced38862). The Editions batch made `new:Staff sales attribution` (SH-E-ada073f2); the coordinator may align the two.

## Items and sources

- **The entries agree with their items.** Every post's text was whole in its item. I printed the rest of two long ones (`--width 6000`), SH-E-0d34d7bd and SH-E-7ea7c76b, cut in the chunk's print; SH-E-35e5b666 and SH-E-adae1474 were cut only in their links. I read no archived page and no run step.
- **`show --meta` now prints the `@posts` label's keys** (1,646 posts, 1,279 with tags, 45 with media), as the coordinator's check after SH-38 said it would.

## For the second stage: stated, or named in passing, and not placed

- **The App Store listings that would give maker statements,** each `not-attempted` in `index/ledger/sitemap--apps-shopify-sitemaps.tsv`: `apps.shopify.com/google` (the Google & YouTube app), `combined-listings`, `inbox` and `translate-and-adapt`. Stocky has no row in that ledger.
- **What the Shopify Pixel Helper is** (SH-E-0a66f16d, SH-E-5f4f200c): launched 'from the Shopify admin'; its help page is `promoting-marketing/pixels/custom-pixels/testing`.
- **Leads for Sharrwah's subjects in Arabic:**
  - 'You can now use auto-translation for Arabic and Hebrew in Translate & Adapt' (SH-E-78f7cb40, 27 March 2024), with 'Make sure your theme supports right-to-left text direction' and the Theme Store's filter Features > Right-to-left;
  - restriction reasons 'fully localized, supporting all languages available in the Shopify admin' (SH-E-61b4af23), a lead for SH-34's `new:Admin languages`.
- **Market facts, for the subjects:**
  - Turkey's limit on goods imported 'with a simplified clearance procedure to 30 euros' (SH-E-f438f3d7);
  - paperless trade: 'Most countries support paperless trade' (SH-E-e680a8ac);
  - Unit Pricing 'previously available only to French and German merchants' (SH-E-4d3e3dea);
  - Evri's 'over 7,000' pickup points in the UK (SH-E-fbee6206);
  - IFRS standards named as a reason for multiple captures (SH-E-08e08a77).
- **Stated, kept in reading:**
  - Markets Pro payouts 'delivered to you on the 1, 8, 15, or 22 of the month', once the order is 'fulfilled, having a tracking number, and being scanned by the carrier' (SH-E-097c67f5);
  - DHL Express 'might contact the merchant or buyer directly' about undeliverable packages (SH-E-7ea7c76b);
  - the cookie banner's 'default banner text in 32 languages' (SH-E-594e342a);
  - the 'Ship to customer permission' overriding the add and manage customers permissions (SH-E-0d34d7bd);
  - barcode formats the Shopify app's scanner can't read on Android or iPhone 12 (SH-E-691c7965);
  - the Shopify Standard Product Taxonomy's 'over 10K product categories and 2K associated product attributes' (SH-E-8d5e55c1), a size, not a quality of the model's kinds.
- **Named in passing, with no line:**
  - Collective's 'weekly emails highlighting unsellable products' (SH-E-26827e6a), a lead for CM-NTF-002;
  - quantity rules and volume pricing as Trade's examples (SH-E-e070c1ae), for the Editions' `new:Quantity rules`;
  - Google Merchant Center, where the YouTube programme is managed (SH-E-0bbdd469);
  - Slack, in a Flow template's name (SH-E-d8e1b68e);
  - the Admin API that Flow's Send Admin API request action calls (SH-E-b875f96f);
  - the list items of the Shopify app's draft orders and company details (SH-E-3da2c81a, SH-E-ceca7de2), Web pixels' new fields (SH-E-a129f81b), Collective's synced attributes, the HS code among them (SH-E-2b1e99e9), and the Smart Grid's default tiles (SH-E-8e89e850).
- **Each post's Help Center link** describes its feature further. They aren't read by this pass.

## Problems with the brief or the scripts

1. **The rulings changed during the batch** (after SH-2 and after SH-55). The second aligned 25 of my lines; I made the change before checking, so the coordinator's alignment of SH-39, which the ruling announces, should find them done.
2. **The checker's brand NOTE fires on 41 lines,** nearly every post that isn't an app's, since nearly every post names 'Shopify …'.
3. **The checker doesn't flag a single-quoted quote that holds an apostrophe.** SH-34's rule 14 puts such quotes in “ ”. I found 17 in my readings with a scan of my own and changed them.
4. **How I kept the cost down:** chunks of 10 posts, each printed once with its leads and `earlier`, and one lookup call per chunk for its cells and searches.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 130 of 130 entries, no problem.
- **The rulings after SH-2 and SH-55 are already kept,** as the agent aligned to them before its last check:
  - Flow's 11 lines and Collective's 14 are `own-service`;
  - Shopify Inbox is `own-service`;
  - Forms, the Combined Listings app and the Pixel Helper stay `core`, since no held words call the Pixel Helper an app.
- **The cell changes stand, each read again:**
  - CM-CUS-012 is held, `core`, a marked reading. The storefront's CAPTCHA moved from reCAPTCHA to hCaptcha, its filler; the posts don't name which forms it guards, and the cell's thing is buyers' sign-in and registration.
  - CM-CAT-013 gains `core` from Unit Pricing, scope EU and Switzerland, a marked reading. With SH-3's Edit price, it goes to the final review, since no platform defines what 'product pricing' does.
  - CM-INV-007 gains `own-service`, from Stocky's purchase orders ('We’ve introduced the option to 'Edit' purchase orders in Stocky').
  - CM-MKT-015 gains `extension-point`, from YouTube's affiliate programme through the Google & YouTube app.
  - CM-SHP-018 gains `own-service` beside `core`, from Shop Promise: dates 'predicted by Shopify' and 'backed by Shop'.
- **New thing:** Finance, the admin's section over Capital, Credit, Balance, Payments, Bill Pay and Taxes (M-13), decided with the others.
- **Rules 1 to 14 stand for SH-40 to SH-46.** Among them: Markets Pro is Managed Markets, by the rename SH-E-dc501d64 states; a post whose link opens a Shop help page is about Shop's feature, by the ruling after SH-38.
- **Cost:** 29.9 million tokens over 102 requests, about 230,000 an entry. The context reached about 504,000 tokens, with 20 runs of the checker.
- **Aligned with the changelog digest (31 October, the corrections in the rulings):** Combined Listings `own-service` (SH-E-56c538c6); unit pricing on CM-CAT-001 (SH-E-4d3e3dea); SH-E-03c207ce also takes `new:Staff sales attribution`; Collective's two CM-SHP-001 lines dropped (SH-E-2b8f1068, SH-E-c0c04479).
