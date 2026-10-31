# SH-34: Shopify's merchant changelog, posts 1 to 130 (notes)

**The batch:** platform `shopify`, batch `SH-34`, effort `high`. Its 130 entries are the first 130 posts of `merchant-changelog` as `@posts` holds them: `structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl`, lines 1 to 130 (positions 0 to 129), at observed-sh `e38dc17e3`. They are dated 6 October 2026 back to 28 April 2026, and all come from the run `20261007T071251Z-published-changelog-posts`.

**No batch had placed this structure before this one.** No placements of `merchant-changelog` existed. `held_entries.py earlier` printed no line for any key of the batch, at the start and again at the end, when SH-8's placements had appeared. So the rules below were made here. SH-35 to SH-46 hold the rest of the structure (about 1,500 posts, since 2018), and these rules are written for them.

**What I read:** the brief, and what it names:
- the evidence map;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, its `REGISTER.tsv` row for `shopify/merchant-changelog` and its ledger summary;
- `show --meta`;
- `selection.tsv`'s row (`placement` `where`, rule `labels:@posts;drop:run,status,class;long:20000`);
- `@posts/meta.json`;
- B-extent's "Cells and evidence" and its conventions;
- the coordinator's rulings, again at the end of the batch.

  Three rulings were added while I worked: after SH-8, on routes that only redirect, on a route's own gates and on documented intents. None bears on a changelog post.

**Counts:**
- 130 entries, on 222 lines: 221 `capability` lines and 1 `new` line, none `out`.
- By support: `core` 194, `own-service` 6, `extension-point` 6, `shows` 6, `core;outside` 3, `core;shows` 3, `core;extension-point` 2, `outside` 2.
- Lines per entry: 65 entries take one line, 47 two, 13 three, 3 four, 1 five (SH-E-eedc9ee3) and 1 seven (SH-E-f595384d). In all they reach 99 capabilities.
- The checker's final line: `130 of 130 entries placed; 0 problems`.

## The rules my lines follow, for SH-35 to SH-46

These are readings, mine, made under the brief's rule 4 for "a changelog post" and its known case for this structure. Where they settle a case the rulings leave open, they are listed for the coordinator to confirm or correct.

**1. What an entry is.** An entry is one post, as its page states it: date, title, type tags, area, text, links, media.
- The page is a record of its run's archive. A quote taken from the page beyond the entry is cited `raw/runs/<run>/fetch.warc.gz@<offset>`. The offset is the 9th field of the run's `fetch.cdx`; `held_index.py <uri>` gives it too, at about 8 seconds a post. Entry 1, for example, is `raw/runs/20261007T071251Z-published-changelog-posts/fetch.warc.gz@1170`.
- Every quote in my lines is from the entry's own text, so none cites a record.

**2. The post's own thing.** It is what its title and text state as new, changed or removed. Where the text narrows the title, the text governs (B-extent).
- The post's line goes on that thing's capability, found with the brief's lookups: leads, `caps --terms`, and the cells' readings for the place it names.
- A lead to a capability whose cell holds nothing is read before it is set aside. Five cells that held nothing are this batch's (see "CHANGES").

**3. The area** is the changelog's grouping of posts: Admin, POS, Analytics, Apps, Payments, Customer accounts, Checkout, International, Balance, Orders, Products, Discounts, Inventory, Collective, Shop, Online Store, Channels, Shipping, Marketing, Mobile and B2B in this batch.
- It says where the post is filed, not what it is. It gives the post no line, since it is a group the post only sits under (M-6, refined). "Admin" says nothing at all.
- It may help choose between two capabilities the text leaves open. A post in Apps names an app: Flow, Shopify Forms, Checkout Blocks, the Developer Dashboard.

**4. The type tag** (New, Feature, Improvement, Changed, Removed) is a release marker.
- It goes in `reading` with the date. Posts from 2018 to 2021 have none (the register).
- It never sets the support, except as rule 9 says for a post that retires a feature.

**5. Every reading begins with the date and the tag,** in the post's words, then any release words, then why: `September 25, 2026, Improvement, effective 'Starting October 23, 2026': …`.
- Release words are the post's own: 'rolls out gradually', 'rolling out to existing stores over the coming days', 'Starting October 1, 2026', 'in POS v11.14', 'first release'. They stay in `reading` (the brief's rule 4).

**6. Support.**
- **`core`:** the post states a feature of Shopify's own admin, POS app, checkout, customer accounts, analytics, settings or API: 'You can now…', 'We've released…'.
  - A product named with the platform's brand names no maker (B-extent). That covers Shopify Analytics, Shopify POS, Shopify Payments, Shopify Tax, Shopify Messaging, Flow, Shopify Collective, Shopify Forms, Checkout Blocks, the Shopify Mobile App and the Balance mobile app. Each is `core` by what the post shows.
  - This answers the checker's NOTE 'core on a product named with the platform's brand' on 113 lines. Every one is a feature the post shows in the admin, POS, checkout or analytics.
- **`own-service`:** only where a held statement names Shopify, or its group, as the maker of a separate product that does the thing (M-1).
  - The one in this batch is Shop: 'Shop is a Shopify application that is available to Eligible Merchants' (SH-S-0056, the maker statement CM-CHN-002's cell cites). So what a post says Shop does is `own-service`, citing SH-S-0056: the Shop app, Shop accounts, shop.com, carts synced via Shop, Shop's reminders.
  - Shop Pay and Shop Campaigns have `own-service` in their cells already. My lines on them keep to what each post shows.
  - The other branded apps have no maker statement in the cells or in the batch (see "For the second stage").
- **`extension-point`:** the post states apps or third parties doing it through something the platform provides. In this batch:
  - apps adding annotations to the charts;
  - analytics apps pulling data through ShopifyQL;
  - apps' extensions in customer accounts and in POS;
  - a third party's AI channel through Agentic Storefronts and Shopify Catalog (Meta; ChatGPT and Copilot; M-3);
  - a carrier's own service named in the platform's listing (DHL On Demand Delivery, M-8).
- **`outside`:** a third party named as doing it, with no interface of the platform named.
  - In this batch that is only Global-e's role in Managed Markets, as CM-MKS-003's and CM-TAX-003's cells read it: merchant of record, tax registration, remitting duty, using the CPSC inputs.
  - Where the post also names Shopify's own surface for the same thing, the line is `core`, with Global-e as its filler (CM-RET-004, SH-E-6888cb05).
- **`shows`:**
  - what the post states is in early access ('Campaign Autopilot is available in early access');
  - a feature offered as a preview before its release date (SH-E-5e991683: enabled 'through Feature test drives', and 'The feature auto-releases to all eligible checkouts on July 2027');
  - the merchant's responsibility ('Merchants are responsible for…', M-9);
  - the merchant's own team doing it with outside tools (SH-E-9f019906's Power BI line);
  - a retired feature with no replacement (rule 9).

**7. A second thing.** A post takes a further line where its text states something new or changed about another capability's own thing. That is one of three:
- **(a) a second feature it announces.** The Purchase Orders page's new metrics in an Analytics post; an Analytics section on the POS channel page; Sidekick doing a new task (collections, test events, store edits in Canvas); a cart that 'converts to a draft order'.
- **(b) the admin place where the feature is set or enabled,** where that place is another capability's, as its cell's reading shows:
  - Checkout settings, CM-CHK-001;
  - Settings > Policies > Return and cancellation rules, CM-CNT-008, whose cell cites `setting:legal:cancel_return_policy_create`;
  - Settings > Metafields and metaobjects, CM-CNT-002;
  - Feature test drives at `settings/test-drive`, CM-EVO-001;
  - product disclosures, CM-TRU-010;
  - the Developer Dashboard, which CM-PTN-001's cell cites as the Partner Dashboard's Dev dashboard.
- **(c) each item of a list that states what the platform or a named party does on another capability.** Such lists are headed What this means for you, What's included, What you get, What's new or Highlights. Examples: Shop's cart sync and its reminders; DHL Express labels' customs documents; Managed Markets' HS codes, tax registration, labels, payouts and local currency.

A thing the post names only as the data its feature reads takes no line. Examples: category metafields as dimensions; order routing's fulfilment location; a location's physical storefront flag; inventory transfers as a trigger's event; the variants' barcodes POS reads. Nor does a thing named in a list of places, fields, report names, supported things, use cases or examples (the ruling after SA-41). A learn-more link (Help Center, community, docs, a video) gives no line.

**8. POS.** A post on a feature of the POS app takes a CM-POS-001 line. It takes a second where the thing it does there is another capability's own:
- local delivery, CM-SHP-008;
- stock counts, CM-INV-003;
- pickup, CM-SHP-007;
- abandoned checkouts, CM-CHK-007;
- receipts and packing slips, CM-ORD-009;
- draft orders, CM-ORD-005;
- transfers, CM-INV-006;
- reports, CM-ANL-002 and CM-ANL-003;
- POS app extensions, CM-POS-004.

A screen or setting of POS alone takes CM-POS-001 only (connectivity, devices, cart button, editor). Homonym: POS's 'persistent cart button' and 'Cart sharing' are staff carts, not CM-CHK-010's buyer's cart kept with their account.

**9. A post that retires, replaces or renames.**
- **Where it names what replaces the feature,** the line supports the replacement, by the rules above. Its reading says what is retired and from when, in the post's words:
  - SH-E-945c8f6a: DDU ends 'On August 24, 2026', and DDP is kept (CM-TAX-008 `core`);
  - SH-E-9aa1c2ef: 'The Checkout Blocks Address Blocker is now deprecated and will sunset on August 31, 2026', replaced by address format validation;
  - SH-E-49ad236d: Benchmark Comparisons 'fully removed on May 19, 2026', replaced by Metric Targets and Sidekick;
  - SH-E-15840b75: Liquid receipt templates until 'January 1, 2027';
  - SH-E-6cfdee51: the 8-currency limit removed.
- **Where it names no replacement,** and the capability is that feature's alone, the line is `shows`: it shows the feature and its end. The date goes in `reading`. No post of this batch is such a case.
- **A rename** is the renamed thing's line, `core`, with the old name in `reading`: the Marketing tab to Growth, shop.app to shop.com, To be paid to Payout balance.
- **A post the feed no longer lists** (SH-E-36f98b81, the register's 'no longer in the feed') is placed as its page states it, with that fact in `reading`.

**10. Scope.** The post's own words for the plan, country, store, market or subscription it states the feature for: 'for the US', 'Merchants on the Advanced plan in the United Arab Emirates', 'POS Pro', 'Plus and Enterprise plans', 'Basic plans and above', 'Available for US domestic orders'.
- An entry's lines share one scope. A condition that holds for one line only goes in that line's reading: SH-E-5e20deab's EU withdrawal policy.
- These go in `reading`: 'eligible merchants' with no eligibility stated, an app version, a store's own settings ('Both stores must … have Shopify Payments activated'), and 'available to all merchants'.
- A staff permission the post names as a requirement is a gate on the user, in `reading`. A post that announces permissions places each on what it gates (the ruling after ZD-7, SH-E-77d9a236). Only a permission over roles themselves goes on CM-STF-002 (SH-E-dcd446ae).
- **Several items with their own conditions in one post** (SH-E-0fd1fcfa's four payment methods, each with its own countries): the checker refuses two lines of one entry on one capability. So the line takes the union of the countries as its scope and each method as a filler, and its reading says how many countries each method has (the problems, below).

**11. Fillers.**
- A third party the post names as doing it:
  - DHL Express, UPS, FedEx;
  - Meta, ChatGPT, Copilot;
  - Triple Whale, Northbeam, Elevar;
  - Okta, Auth0, Microsoft Entra ID;
  - Global-e;
  - Microsoft Advertising;
  - the local payment methods' brands, as the model's slot fillers hold MB WAY and Bizum.
- A law or authority setting its terms: EU regulation, Consumer Product Safety Commission (CPSC), California Proposition 65, Receita Federal, EU right to withdraw regulation.
- Tools the merchant's own team uses (Power BI, Tableau, Looker Studio) are named in `reading`, not as fillers.
- Shop is never a filler: it is the group's own product.

**12. Qualities.** A limit, fee, duration or minimum the post states for the platform's feature:
- 'up to 20 barcodes to a variant';
- 'no monthly fee, and pay per label';
- unused return labels expiring 'after six months at no charge';
- 'one bank account per supported payout currency';
- 'a reusable palette of up to 20 colors';
- 'Android 11 or later';
- the EU's €3 duty per tariff line;
- the 14-day withdrawal and cancellation rules;
- 'only paying for the messages you send'.

Not qualities: example values (a 14-day window for seasonal items), counts of currencies (they are market data), and app versions (they are release markers).

**13. `out`.** No post of this batch is `out`.
- A post that names a feature of the platform is never `out`. A post that names only an announcement, such as the Spring Edition (SH-E-79328285), goes on CM-ONB-003, `core`, as Salla's changelog categories and updates centre do (the rulings after SA-2 and SA-5, M-13). Each Edition feature is placed from its own `editions-page-data` entry.
- A post whose thing is one country's own values (Italy's provinces, SH-E-e0214acd) I placed on CM-MKS-009 with the country as its scope (the cases below).
- A post about the whole admin's look (SH-E-b3afcfc9) names the admin itself, which no capability holds (the ruling after SA-21). It takes no line for that, and its other things take theirs (Sidekick's move).

**14. Quotes.** A quote is copied exactly from the entry's text. Where the quoted words hold an apostrophe, I quote with “ ”. The text's own straight double quotes ('"Set To"', '"Generate test events"', '"View abandoned checkouts"') can't be quoted, so those words are named unquoted. Typos stay as the post has them ('disclousure', 'thier', 'sPOS', 'acess').

## The new thing

**`new:Admin languages`** (SH-E-946bf2fd, line 10, `shows`): the language the admin itself shows its users in.
- **The post:** 'We’ve released improved support for 3 right-to-left languages (Arabic, Urdu, and Hebrew) in both Admin and Storefronts', and 'Display language is determined based on the user’s device settings, if available'. The storefront side is CM-MKS-008's, its own line.
- **A place of its own:** none in the post. It names no setting or route for the admin's language, so the line is `shows`. The user's language preference would be its place, and this batch doesn't hold it.
- **Proposed:** domain A, area ACC, parent CM-ACC-001 (the merchant's account), or no parent.
- **Its name in each language:** English, Admin languages, display language. The post names Arabic but gives no Arabic term. Shopify's admin in Arabic isn't held (`docs/GAPS.md`: 'Admin in Arabic … Decided with the founder when it is reached').
- **The terms I searched** (`caps --terms`): admin language, display language, right-to-left, RTL, language of the admin, user language, preferred language, dashboard language, interface language, لغة, locale. The only hits were CM-MKS-008 (store languages), CM-MKS-006, CM-NTF-001 and CM-PLN-004, none of them the admin's own language.
- **The checker's NOTE** lists the entry's leads. I read each: CM-CNT-002 (by 'merchant-owned'), CM-CNT-003 (content, pages), CM-CUS-010 (customer accounts), CM-LOY-008 and CM-INV-010 (by name). None is the admin's language.
- **A lead for Sharrwah's subjects:** the admin in Arabic, right to left, released on 2 October 2026 by this post.

## CHANGES, each read again against its source

- **CM-CHK-010** (persistent cart) holds nothing and becomes held, `own-service` (line 6, SH-E-eedc9ee3).
  - The post: 'Carts follow shoppers - carts sync and stay up to date across a shopper's devices', and 'carts started in the Shop app carry over to your storefront, and vice versa', via Shop.
  - The cell's own words for the capability are 'the buyer's cart saved to their account, so it is still there when they switch devices'. The post's carts are kept with the buyer's Shop account. I keep it. `own-service` rests on SH-S-0056 (rule 6). Read Shop's features as the platform's own and it would be `core`.
- **CM-MKT-003** (automatic discounts) holds nothing and becomes held, `core` (line 96, SH-E-e685e3aa).
  - The post: 'Combine discount codes with automatic product discounts on the same item', and 'Discounts apply automatically at checkout, following your rules'. Two other posts of the batch name the same thing: SH-E-6c271033's 'create automatic discounts and discount codes' and SH-E-9bfd722a's 'any code-based or automatic discount'.
  - The cell's reading had 'No Shopify statement held names a discount applied without a code.' 'Automatic', set against codes, is that (a reading). I keep it.
- **CM-MKT-023** (product recommendations) holds nothing and becomes held, `core` (line 155, SH-E-ba79302c).
  - The post: 'Customers with no orders can see product recommendations you curate, instead of an empty state'.
  - Kept, but unsure. The cell's only statement is BigCommerce's, recommendations the platform makes through Google Vertex AI. These the merchant curates and the platform shows on the account pages (the cases below).
- **CM-MKS-009** (countries, cities and districts reference data) holds nothing and becomes held, `core`, scope Italy (line 186, SH-E-e0214acd).
  - The post: “We've updated Italy's province definitions…”. A province is 'now a selectable province', 'Merchants shipping to Sardinia may notice updated province names in checkout', and 'Partners using the address validation or autocomplete APIs will get more accurate province assignments'.
  - The cell's note had 'no Shopify statement holds such lists'. This shows Shopify keeps a country's provinces as reference data, used in checkout and in its address APIs. Kept, against the brief's `out` for 'one country's own values' (the cases below).
- **CM-ANL-007** (commerce data in outside analytics platforms) holds nothing and becomes held, with `shows` only (line 69, SH-E-9f019906).
  - The post: 'If your team builds custom reports in tools like Power BI, Tableau, or Looker Studio, you can connect to this data through ShopifyQL'. These are the outside platforms BigCommerce's statement names.
  - The merchant's team makes the connection, so `shows` (M-9). Kept (the cases below).
- **CM-ANL-006** gains `extension-point` (line 68, SH-E-9f019906). The post: 'your analytics and reporting apps can pull Shop Campaigns data directly' through ShopifyQL, and 'your provider can now integrate Shop Campaigns data into their dashboards'. These are apps doing the work through the platform's API (B-extent). Kept.
- **CM-CHK-005** (cart and checkout validation) gains `core` (line 157, SH-E-9aa1c2ef).
  - The post: 'Use the new checkout rule to block non‑compliant shipping addresses', at 'Settings → Checkout → Checkout rules → Address format validation', 'available to all merchants'.
  - The setting is in the admin's own checkout settings, so `core` by what the entry shows. Checkout Blocks is an app whose maker isn't stated: the model holds only its help section, 'Checkout Blocks app' (SH-I-2122). The cell's `extension-point` is apps writing validations. Kept, with the doubt below.
- **CM-SHP-020** (international shipping readiness and customs data) gains `core` (lines 61, 92, 103).
  - SH-E-2ae24465: 'Customs documentation generated automatically for international orders', with DHL Express labels.
  - SH-E-f595384d: 'Managed Markets classifies your products and assigns Harmonized System codes for your products', the HS codes the cell found no Shopify statement for.
  - SH-E-5f5a9d1d: CPSC eFiling certificate data for crossing U.S. customs, a reading.
  - Kept. The third is the weakest.
- **CM-CUS-010** gains `own-service` (line 9) and **CM-MKT-022** gains `own-service` (line 8), both SH-E-eedc9ee3.
  - 'One-tap sign-in - for Shop users signing into their customer accounts', and 'Built-in recovery - Shop reminds shoppers to finish carts they left behind': Shop does each, on SH-S-0056.
  - Kept. Both disappear if Shop's features are read as `core`.
- **Not kept: CM-RET-004 gaining `outside`.** My first line gave SH-E-6888cb05 `core;outside`. Read again, the post names Shopify's own surfaces ('supported Shopify buyer surfaces') for the same requests. B-extent's `outside` needs 'no interface of the platform named', so the line is now `core`, with Global-e as its filler. Its role ('managed by Shopify’s Merchant of Record (MOR) partner Global-e') stays on the CM-MKS-003 line.

**The other NOTEs.**
- **`own-service`, 6 lines:** Shop, on SH-S-0056 (rule 6).
- **The new thing's leads:** above.
- **The first leads that hold nothing and that no line names,** four of them, beyond the checker's cap. I saw them by checking the batch in two halves. None is the post's thing:
  - CM-OPS-004, store status (by 'status'), on SH-E-4dcd74f5 (POS connectivity status) and SH-E-f3ac718f (delivery status);
  - CM-API-010, conditional webhooks (by 'conditions'), on SH-E-699b03b8 (a workflow's condition steps);
  - CM-DVT-006, staging environments (by 'live, update'), on SH-E-79328285.
- The checker printed no NOTE for a footnote mark, a quote it didn't find, an app's embedded page or a container.

## Entries I couldn't tell, and what would settle each

1. **SH-E-b3afcfc9, a new look for the admin.** Its own thing is the whole admin's look and frame: color, type, spacing, icons, and search, notifications and the store picker in the side navigation. No capability holds it. Only Sidekick's move to 'a floating chat at the bottom of every page' takes a line, on CM-AIA-002. To settle: the coordinator decides whether the admin's own look or navigation is ever a capability. The ruling after SA-21 says the class holds none.
2. **SH-E-1c31a003, the Developer Dashboard's logs for custom apps.** It is on CM-APP-009 and CM-PTN-001; CM-PTN-001's cell cites the Partner Dashboard's item Dev dashboard (SH-I-2094). CM-DVT-001, developer tools, would fit as well. To settle: a held statement of what the Developer Dashboard is and whose it is, or the coordinator's choice between CM-PTN-001 and CM-DVT-001.
3. **SH-E-9aa1c2ef, Checkout Blocks' address validation:** `core` on CM-CHK-005 (the CHANGES above). To settle: the maker of Checkout Blocks. Its listing, `apps.shopify.com/checkout-blocks`, is `not-attempted`. If a held statement names Shopify, the line is `own-service`. If the rule is shown to be an app's function, `extension-point`, as the cell is.
4. **SH-E-ba79302c, 'product recommendations you curate':** CM-MKT-023, `core`. The capability's name is 'products the platform recommends'; these the merchant curates. The alternatives are `shows`, or no line, the recommendations being the account page's content. To settle: the coordinator's reading of CM-MKT-023.
5. **SH-E-e0214acd, Italy's provinces:** CM-MKS-009, `core`, scope Italy. The brief makes 'one country's own values' `out`. I read the province names as Italy's values, the subjects', and Shopify's keeping a country's provinces, used in checkout and its address APIs, as CM-MKS-009's thing. The same holds for SH-E-861b8676's localized address fields, placed on CM-CUS-008 with the five countries as scope. To settle: the coordinator's reading of CM-MKS-009 against the market-data rule.
6. **SH-E-3fc0ef0c, Brazil's CNPJ validation:** CM-TAX-005, a reading, a business's tax identifier validated as VAT numbers are, with Receita Federal as filler and Brazil as scope. Where the CNPJ is entered isn't stated beyond the area Checkout. The alternative is CM-CHK-001. To settle: the help page on Brazil's checkout identifiers, not read here.
7. **SH-E-5f5a9d1d, CPSC eFiling fields:** on CM-TRU-010, since product disclosures are its place (SH-S-7257); on CM-SHP-020, a reading of customs data on products; and on CM-MKS-003 for Global-e's use of them. To settle: whether the coordinator counts product-safety filing data as CM-SHP-020's customs data.
8. **SH-E-53d52ef0, Managed Markets' managed international pricing:** CM-MKS-006 is the nearest capability, a reading. CM-CAT-013, product pricing, would gain `core`: its Shopify cell is `extension-point` only and reads 'No statement shows Shopify's own pricing of products'. To settle: whether a market's adapted prices are product pricing or prices in the buyer's currency.
9. **SH-E-2ae24465, 'DHL On Demand Delivery':** CM-SHP-017, `extension-point`, the nearest capability (M-8). No capability holds a buyer's options to reschedule or redirect a delivery. To settle: the coordinator's decision whether that is part of shipment tracking.
10. **SH-E-9f019906, Power BI, Tableau, Looker Studio:** CM-ANL-007, `shows`. CM-ANL-007's note keeps reading through the API apart, as CM-ANL-006's. These tools connect through ShopifyQL, so they could be CM-ANL-006, or `extension-point` on CM-ANL-007. To settle: the coordinator's reading of the two notes.
11. **SH-E-5e991683, ship and pickup in one order:** `shows` on CM-SHP-007 and CM-SHP-009 (a preview through Feature test drives, auto-released in July 2027), on Plus and Enterprise. Its Feature test drives line is `core` on CM-EVO-001. If the coordinator reads a test drive as released to those plans, the two lines are `core`.
12. **Shop's features** (SH-E-eedc9ee3, SH-E-c1b85416): `own-service` on SH-S-0056. If Shop's features are read as the platform's own, `core`, three CHANGES fall away and CM-CHK-010 becomes `core`.
13. **Activity logs:** SH-E-30e0a63c's app pixel activity log and SH-E-c2bf4573's POS activity log each take a CM-TRU-003 line, as kinds of the admin's audit log (a reading). SH-E-4517a726's workflow version history, logged 'with the staff member and timestamp', takes none: it is the workflow's version history, CM-AUT-001's. To settle: whether CM-TRU-003 is any log of staff or app actions or only the admin's audit log.
14. **SH-E-6888cb05's Global-e:** see the CHANGES above. If Global-e's role is to show on CM-RET-004 too, it is `extension-point` (it works within Managed Markets) rather than `outside`.

## Items and sources

- **`@posts`' order isn't date order across its two runs.**
  - Positions 0 to 304 are the run of 7 October 2026: 6 October 2026 back to 7 October 2025.
  - Positions 305 to 1645 are the run of 30 October 2026: 29 October 2026 back to 3 August 2018, the posts not held before.
  - So the batches after this one hold the posts of 7 to 30 October 2026 (from position 305), after the ones from 2025 (positions 130 to 304). A batch that reads 'the latest' should know it.
- **`show --meta` prints the feed's descriptive keys** (`changelog.shopify.com@feed`, 1,645 items), not those of `@posts`, which this structure is read under. `@posts/meta.json` gives 1,646 posts, all read, 1,279 with tags and 45 with media. Its `source.warc_records` lists each post's record.
- **SH-E-36f98b81** (inventory-reports-now-show-on-hand-quantity) is held in the 7 October run, and the feed of 30 October no longer lists it (`structures/REGISTER.tsv`, `shopify/merchant-changelog`). Its line says so.
- **The entries agree with the pages I read.** I read one page whole, entry 1's record at `@1170`. Its `post__content`, status tag 'New' and area 'Analytics' are the entry's. I didn't read the other 129 pages: the items' text is each page's `post__content`, by the extractor's shape.

## For the second stage: stated, or named in passing, and not placed

- **Shopify service status shown in POS's connectivity screen** (SH-E-49f989d0: 'internet connection, Shopify service status, and hardware connection health'). CM-OPS-002, the service status page, holds nothing on Shopify. Named in a list, so no line.
- **CM-ANL-005, smart analytics,** holds nothing, and Salla's is a link only. SH-E-25e3fb9b's daily insights ('Shopify's analytics insights are run daily…') would be read against it if Salla's were defined.
- **The app listings that would give maker statements** for the branded apps the posts name. Their App Store listings are `not-attempted` in `index/ledger/sitemap--apps-shopify-sitemaps.tsv`: `apps.shopify.com/shopify-forms`, `shopify-messaging`, `flow`, `checkout-blocks` and `translate-and-adapt`. `collective` and `shop` are `captured`. They are exists-not-captured, for the coordinator to decide, since they would settle `core` against `own-service` for those apps' lines.
- **Named only as alternatives or in passing, undefined:**
  - Tax Platform (SH-E-2938709a: 'merchants using Shopify Tax or Tax Platform');
  - Stocky (SH-E-561b3073: 'if you moved off Stocky');
  - Campaign Autopilot's Microsoft Advertising account creation (SH-E-a4d34645);
  - the Translate & Adapt app (SH-E-946bf2fd).
- **SH-E-15840b75 links a YouTube overview video.** Its subtitles and metadata are in `structures/shopify/embedded-videos/` (the register), not read here.
- **Each post's Help Center link** (help.shopify.com/en/manual/…) describes its feature further: requirements, eligibility, plans. They aren't read by this pass.
- **Places named in passing that no line takes:**
  - the Shopify app on the phone (SH-E-2e225666: 'from the Shopify app on your phone');
  - Tap to Pay and Shop Pay in the POS Editor (SH-E-1802a8e9);
  - the 'physical storefront' flag on a location (SH-E-bf44e39e);
  - Shopify Catalog (SH-E-c7698fdf, SH-E-2178ade3);
  - the inventory counts route, which `docs/GAPS.md` lists behind beta `4d3efaac`. SH-E-92bd917a states stock counts released on 28 September 2026, with POS Pro.

## Problems with the brief or the scripts

1. **The checker refuses a second line of one entry on the same capability.** Rule 5's exception lets 'an entry [that] stands for several items whose conditions differ' give each line its own scope. A post that lists items with their own conditions (SH-E-0fd1fcfa's MobilePay, TWINT, BLIK and Przelewy24, each with its own countries) can't. I merged the four into one line, its scope the union of 31 countries and its fillers the four methods, which loses which method is offered where. The reading gives the count of countries for each.
2. **The checker caps its NOTE lines** ('… and 4 more'). With 113 brand NOTEs, the four NOTEs past the cap, the first leads that hold nothing, showed only when I checked the batch in two halves; I rebuilt the full file after. The brand NOTE also fires on nearly every changelog post, since nearly every one names 'Shopify …'.
3. **`show --meta` prints the feed label's keys for this structure,** not the keys of `@posts`, which `selection.tsv` reads.
4. **The brief's rule 4 reads differently from B-extent.** For a changelog post it says '`extension-point` where it names an app'. For an app named with the platform's brand and with no maker statement held (Shopify Forms, Shopify Messaging, Flow, Checkout Blocks), that reads differently from B-extent's `extension-point` ('the statement shows third parties doing it') and from the brief's own rule for a named company with no maker statement ('place the line by what the entry shows, and note the missing maker statement as a gap'). B-extent governs, so these are `core` by what each post shows, with the maker a gap.
5. **The rulings file changed during the batch:** three rulings after SH-8, on routes. None changes a line of this batch.

## The coordinator's check (31 October 2026, after the batch)

- **The rules for SH-35 to SH-46 stand,** with the cases below settled and four rulings made after this batch (`review-H-rulings.md`).
- **Nine cells change, each read again and kept:**
  - CM-CHK-010, CM-CUS-010 and CM-MKT-022 take Shop's `own-service`, by the ruling after SH-34;
  - CM-MKT-003, automatic discounts, held nothing on Shopify and is `core`;
  - CM-MKT-023 is `core`. Its capability is the products shown beside a product that the merchant may choose (made from Zid's), so recommendations the merchant curates are its thing;
  - CM-MKS-009 is `core`, scope Italy. The platform keeps a country's provinces for checkout and its address APIs; the values are the subjects';
  - CM-CHK-005 and CM-SHP-020 gain `core`. CPSC eFiling's fields are import data on the product, as customs data are;
  - CM-ANL-006 gains `extension-point`.
- **Corrected:**
  - CM-ANL-007 is `extension-point`, not `shows`. The post names the platform's interface the outside tools connect through, ShopifyQL. The reports the team builds are the merchant's (M-9), but the connection is the platform's.
  - The ship-and-pickup preview's two lines (SH-E-5e991683, CM-SHP-007 and CM-SHP-009) are `core` with scope Plus and Enterprise, by the ruling on features enabled before release.
- **The other open cases stand as placed:**
  - the admin's new look takes only Sidekick's line, since the admin's own look is no capability;
  - the Developer Dashboard's logs;
  - Checkout Blocks `core`, its maker a gap;
  - Brazil's CNPJ on CM-TAX-005;
  - Managed Markets' prices on CM-MKS-006, since a market's adapted prices aren't the platform's automatic pricing (CM-CAT-013);
  - DHL On Demand on CM-SHP-017;
  - the activity logs on CM-TRU-003;
  - Global-e on CM-MKS-003.
- **New thing: Admin languages** (SH-E-946bf2fd). Its post of 2 October 2026 adds right-to-left Arabic, Urdu and Hebrew to the admin and storefronts. It is decided with Salla's portal interface language (العربية / English) in `held/new.tsv`.
- **The checker:**
  - it allows a second line on one capability with another scope or filler;
  - its brand note reads the line's own terms, not every name a post mentions;
  - it prints up to 400 notes.
- **Cost:** 28.3 million tokens over 99 requests, about 218,000 an entry. A post is long and every request reads the context again; it reached 516,000 tokens.
