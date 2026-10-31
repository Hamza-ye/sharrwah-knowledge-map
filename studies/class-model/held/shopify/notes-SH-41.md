# SH-41: Shopify's merchant changelog, posts 911 to 1040 (notes)

**The batch:** platform `shopify`, batch `SH-41`, effort `high`. Its 130 entries are posts 911 to 1040 of `merchant-changelog` as `@posts` holds them: `structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl`, lines 911 to 1040 (positions 910 to 1039), at observed-sh `e38dc17e3`. They are dated 28 August 2023 back to 23 March 2023, and all come from the run `20261030T234414Z-merchant-changelog-feed-posts`.

**What I read:** the brief, and what it names:
- the evidence map;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, and its `REGISTER.tsv` row for `shopify/merchant-changelog`. The changelog has no ledger denominator ('no sitemap: 404');
- `show --meta` (the `@posts` label: 1,646 posts) and `selection.tsv`'s row (`placement` `where`, rule `labels:@posts;drop:run,status,class;long:20000`);
- B-extent's "Cells and evidence" and its conventions, with "What a place of its own is";
- the coordinator's rulings, their last section included. One ruling was added while I worked, after SH-57: a first-party app's feature takes another capability's line only where the app itself provides that capability's thing. I applied it to the lines I had written (below);
- SH-34's notes, its rules and its check, and SH-35's to SH-40's rules, new things and checks. I read earlier batches' placements by line only where an entry of mine was of the same kind (the lookups are named in the readings).

I read no post's page and no run file: every entry's own text settled its capability, support and scope, or I list it below as one I couldn't tell.

`held_entries.py earlier` printed one line for the whole batch, at the start and again at the end: the label Shopify Credit, on CM-PAY-025 `core` ×8 and `shows` ×1. My line on it is `own-service` (see "Entries I couldn't tell"). No placements of SH-42 to SH-46 existed when I finished.

**Counts:**
- 130 entries on 213 lines: 208 `capability` lines and 5 `new` lines, none `out`. Every entry has at least one `capability` line; 5 entries also take a `new` line.
- By support: `core` 167, `own-service` 38, `shows` 6, `core;extension-point` 1, `own-service;extension-point` 1.
- Lines per entry: 68 entries take one line, 48 two, 10 three, 3 four (SH-E-527677d7, SH-E-89853a98, SH-E-c1fb121e) and 1 seven (SH-E-3eb039fd, Organization Settings). In all they reach 90 capabilities.
- 41 lines carry a scope, 8 a filler, 14 a quality.
- The checker's final line: `130 of 130 entries placed; 0 problems`.

## The rules my lines follow

I kept to SH-34's rules 1 to 14, SH-35's 1 to 10, SH-36's 1 to 13, SH-37's 1 to 14 (rule 1 as the ruling on the admin's frame changed it), SH-38's 1 to 12, SH-39's 1 to 14, SH-40's 1 to 15, and the rulings after SH-34 to SH-38, SH-2, SH-55 and SH-57. Every reading begins with the post's date and type tag, then its release words. Every quote is copied from the entry's own text, but three that cite another held entry by its id, which the checker finds: Shopify Messaging's maker statement (SH-E-32e5ccc3), Collabs' Editions card (SH-E-709b37e4), and ShopifyQL Notebooks' 'we’ve prepared' (SH-E-3f85908b). Where the quoted words hold an apostrophe, straight or curly, or the source's own single quotes, the quote is in “ ”. Text that holds a straight double quote is named unquoted (SH-34's rule 14): Send Invoice (SH-E-94145c3d), the used_in filter (SH-E-eb446cdc), Access and permissions (SH-E-89853a98), the subject-line examples (SH-E-1cecbf6f).

**The first-party apps, by the ruling after SH-55:** Flow (4 lines), Collective (2), Search & Discovery (4), Shopify Bundles (2), Shopify Audiences (1), Shopify Email (4), Inbox (1), Translate & Adapt (1) and Collabs (11: 6 on CM-MKT-014 and 5 on CM-MKT-015) are `own-service`, each reading citing its maker statement. Shop's things (Sign in with Shop, its pre-filled checkout, Shop Promise's guarantee, the Shop channel) are `own-service` on SH-S-0056. POS Go is `own-service` on CM-POS-002's own maker evidence (SH-40's rule 14). Plan lines stay `core`: Flow's plans (SH-E-2bff15c9, two lines, the second under its own condition, SFN merchants). Marketplace Connect and the Shopify Privacy and Compliance App have no maker statement held (`makers` finds none), so they are `core` by what their posts show, the maker a gap (the ruling after SH-36).

**The ruling after SH-57, applied:**
- I dropped a CM-SFR-012 line from SH-E-69c6bd0e (Search & Discovery 'now compatible with the Storefront API'): the API is the means, and the app's own thing stays on its CM-SFR-013 line.
- I gave no line to Collabs' Shopify bill (SH-E-058c9bf8, CM-PLN-004), to the custom storefronts on Hydrogen (SH-E-f4548e35), or to the subscription apps that Collabs' integration reads (SH-E-17eda0f1, CM-SEL-001). Each is a condition or a means of the app's own thing.
- Search & Discovery's product recommendations (SH-E-e612d2b5) take CM-MKT-023, since the app itself provides them (see "CHANGES").
- Collective's two posts keep their CM-CAT-010 `shows` lines, which that cell's note asks for (SH-39's rule 9; SH-40's rule 4). The ruling names other capabilities (shipping, inventory, price lists), not this note. If the coordinator reads it as covering CM-CAT-010 too, lines 19 and 50 go.

Where a kind of post came up that those rules don't cover, I followed the rule below. These are readings, mine, for the coordinator to align with SH-42 to SH-46.

1. **A first-party app's own release takes CM-APP-011** (SH-E-96109f43, 'our free new app, Shopify Bundles'), as SH-40's rule 13 placed the Shopify Subscriptions app's release. A post on one of the app's features doesn't take it.
2. **A product the post says 'we built' is `own-service`** (SH-E-e3a378a2: “That’s why we built Shopify Credit, a pay in full business credit card”). Shopify Credit is a separate product, not an admin section, and the cell CM-PAY-025 already holds `own-service`. Its admin routes stay `core`, as SH-11 placed them.
3. **A branded tool that 'we' introduce, with no held words calling it an app, is `core`**, the maker a gap. This is the case of SH-E-8f406571, Checkout Rules for Fraud Control, filed under Apps, and follows SH-39's reading of the Pixel Helper.
4. **An app is `own-service` where `makers` finds 'we’ve [done something] in X'**: “we’ve prepared a summary notebook in ShopifyQL Notebooks” (SH-E-3f85908b), which SH-E-22e5d738's 'Any Shopify provided Notebooks or templates' supports. That covers ShopifyQL Notebooks, 'the ShopifyQL Notebooks app' (SH-E-eab82f6c). It is a reading of the ruling's 'we’ve added … to X' (see "CHANGES").
5. **A retired dataset of an app, with admin pages named in its place** (SH-E-22e5d738: ShopifyQL Notebooks' inventory dataset, 'please refer to inventory Reports or inventory adjustment history'). The lines go on the replacements, CM-ANL-002 and CM-INV-002, by SH-34's rule 9.
6. **Collabs' posts:**
   - commissions, affiliate discounts and affiliate links take CM-MKT-014, whose cell holds 'Collabs affiliates';
   - creators, the Collabs Network and Collabs' own pages take CM-MKT-015.
   - A post that names both takes both: SH-E-2288795f, SH-E-27bc1df6, SH-E-c2fa6765. Both cells already hold `own-service`.
   - The app's admin pages in links take no CM-APP-007 line (SH-35's rule 10). The checker's note on line 120 is this case.
7. **A store's eligibility listed as criteria** (SH-E-27bc1df6: Collabs Network for merchants who have a brand profile, have opted into Automatic-Payments, have $10K in sales over 365 days and 'Are not a dropshipping store'):
   - the kind of store is the scope (M-11): 'not a dropshipping store';
   - the sales minimum is a quality;
   - the profile and the opt-in are the store's own data, in `reading`.

   The creators' criteria in SH-E-2288795f (their countries, 1K followers) are partners', not the store's: their countries are in `reading`, the followers a quality.
8. **Granular staff permissions in place of one** (SH-E-527677d7, draft orders). Each permission takes the line of what it gates (the ruling after ZD-7), as SH-40 placed the orders' twelve:
   - View, Create and edit, and Delete draft orders on CM-ORD-005;
   - Apply discounts on CM-MKT-001;
   - Set payment terms on CM-PAY-008;
   - Charge credit card and Mark draft orders as paid on CM-PAY-020.

   The same goes for SH-E-063bc45d's Edit code (CM-SFR-002), Taxes and duties (CM-TAX-001) and Policies (CM-CNT-008). The redesigned permissions selector (SH-E-090f3449) is over permissions themselves: CM-STF-002.
9. **POS access granted through a Plus role** (SH-E-89853a98) takes four lines:
   - the roles, CM-STF-002;
   - the POS access each grants, CM-POS-001;
   - the Plus admin where it is set, CM-ACC-003;
   - Settings > Users and Permissions, where the user reveals the PIN, CM-STF-001.

   Their scope is 'Plus merchants'.
10. **Markets Pro's payouts posts** (SH-E-9192ff8f, SH-E-616b7990, SH-E-3072a8dc, SH-E-e5f09172) take CM-MKS-003 and CM-PAY-005, by SH-39's rule 2. The refunds and the Shopify Payments bank account they name are their conditions. Markets Pro's activation posts take what they configure: the markets (CM-MKS-001), the shipping settings (CM-SHP-001) and its carrier-calculated rates (CM-SHP-004, DHL Express the filler).
11. **A post in one country with a card network named first** (SH-E-f34fd5b0, eftpos in Australia) follows SH-39's rule 4: CM-PAY-021 with eftpos as filler, and CM-POS-001. The other networks and wallets are named in a list ('such as') and take no line.
12. **A destination's states or a buyer's country as scope.** SH-E-83639fe1's seven US states and SH-E-8dfc09fc's Canada are where the feature applies, by the buyer's destination. I put them in `scope`, as SH-34's rule 10 keeps 'Available for US domestic orders'.

## The new things

All four are earlier batches' new things, and keep their names. `caps --terms` ('saved view; saved views; staff attribution; sales attribution; tipping; tips; quantity rules; quantity rule; minimum quantity') finds only CM-MKT-008 (credits orders to marketing), a homonym. So the earlier batches' searches still hold.

- **`new:Saved views`** (SH-E-c79d0322, line 17, `shows`): 'Merchants will also be able to create saved views with custom columns' on the inventory page. It is a second thing the post announces (SH-34's rule 7(a)). It has no place of its own: it is a view inside a list page. Its leads are CM-INV-001 (placed, the inventory page), CM-ONB-003 and CM-ORD-003 (by name); none is saved views. The file selector's 'save views' (SH-E-eb446cdc) is named in a list and takes no line.
- **`new:Staff sales attribution`** (SH-E-1c0bb5d3, line 108; SH-E-6e1e14c1, line 154; both `shows`): editing sales attributions on completed orders; the Cart and Exchange attribution workflows in POS.
  - Each also takes CM-POS-001 `core`, as SH-34 placed Staff attribution in Shopify POS.
  - It has no place of its own in the posts.
  - Its leads are CM-MKT-008 (a homonym), CM-MKT-014 (by 'commission', affiliates' and not staff's), CM-CHK-002, CM-PAY-021, CM-ORD-003, CM-ONB-003 and CM-PTN-010; none is it.
  - SH-50 and SH-53 placed it `shows`, SH-55 and SH-57 `core`; I kept `shows`.
- **`new:Tipping`** (SH-E-c1cc30bf, line 206, `core`): 'customers can now add a tip on the Shop Pay payment page', 'when the tipping option is turned on under Settings > Checkout'.
  - It is `core` as most earlier Tipping lines are, the option a settings item of the platform's own checkout.
  - Its leads are CM-CHK-001 and CM-PAY-014 (both placed), CM-ONB-003, and CM-CHK-009 (order options and custom fields at checkout, not tips).
- **`new:Quantity rules`** (SH-E-cc191d02, line 189, `shows`): 'Quantity rules allows you to set minimum, maximum, and increment quantity rules for product purchasing', a feature of Catalogs.
  - The post's CM-B2B-003 line holds the catalogs, price lists and customer-specific publishing.
  - It has no place of its own in the post.
  - Its leads are CM-B2B-003 (placed), CM-B2B-007, CM-CAT-001, CM-ONB-003 and CM-INV-004 (by name); none is it.

No Arabic name is held for any of them: the admin in Arabic isn't captured (`docs/GAPS.md`).

## CHANGES, each read again against its source

Most repeat cells that earlier batches already change, since the model isn't amended between batches:
- CM-AUT-001, CM-CHN-005, CM-MKS-008, CM-MKT-007, CM-MKT-011, CM-SEL-006 and CM-SFR-013 gain `own-service`. These are Flow, Collective, Translate & Adapt, Shopify Email, Audiences, Bundles and Search & Discovery, by the rulings after SH-35, SH-37, SH-38, SH-53 and SH-55, as SH-36 to SH-40 have them.
- CM-CUS-010 gains `own-service`: Sign in with Shop (lines 167, 186), as SH-35's rule 5 and SH-36's check have Shop's things.
- CM-SHP-018 gains `own-service`: Shop Promise's limited guarantee in the Shop App (line 95), as SH-39's rule 8 placed SH-E-682a2a87, which cites this very post.
- CM-LOY-006 gains `core`: a gift card sent to the recipient with a personal message (line 195), as SH-40's rule 6 and its check have it.

Four are this batch's own:
- **CM-CHK-005 gains `core`** (line 38, SH-E-8f406571). 'Checkout Rules for Fraud Control … empowers you to block orders right in the checkout': rules that block a checkout from going ahead.
  - The cell holds only `extension-point`, from the Function API. Its name says 'app-written rules'.
  - SH-36's check placed Checkout Blocks' order limits here, a first-party app's rules, so I read the capability as rules that block checkout, whoever writes them.
  - I kept the line, `core`, since no held words call Fraud Control an app (rule 3). If they did, it would be `own-service`, as Checkout Blocks is. If the coordinator keeps CM-CHK-005 for apps' Functions, the line goes, and the post stays on CM-ORD-006 alone.
- **CM-ANL-001 gains `own-service`** (line 122, SH-E-eab82f6c), from the ShopifyQL Notebooks app's Python code blocks.
  - The maker statement is “we’ve prepared a summary notebook in ShopifyQL Notebooks” (SH-E-3f85908b, the one sentence `makers` finds), with 'Any Shopify provided Notebooks or templates' (SH-E-22e5d738).
  - I kept it, as a reading of the ruling after SH-55. SH-50 to SH-52 placed the Editions' Notebooks `core`, before the ruling. If the coordinator doesn't read 'we’ve prepared … in X' as naming the app's maker, the line is `core`, and the cell doesn't change.
- **CM-MKT-023 becomes held, `own-service`** (line 205, SH-E-e612d2b5), from 'view and edit all search boosts and product recommendations in the Shopify Search & Discovery app'.
  - The products a merchant chooses to show beside a product are this capability's thing, as SH-34's check read it ('recommendations the merchant curates'). The app itself provides them (the ruling after SH-57).
  - The cell holds nothing yet, because SH-34's `core` isn't amended; with it, the cell is `core;own-service`. I kept it.
- **CM-PAY-025's `own-service`** (line 32, SH-E-e3a378a2) changes no cell, since the cell holds `own-service`. But it differs from the earlier lines on the same label (`earlier`: `core` ×8); see "Entries I couldn't tell".

## The other NOTEs

- **`own-service`** (38 lines): each line's reading cites its maker statement:
  - the ruling's statements for Flow (SH-E-0678ff26, SH-E-aca9896c), Collective (SH-E-850b28ae), Search & Discovery (SH-E-9b869699), Shopify Email (SH-E-32e5ccc3) and Translate & Adapt;
  - the post's own words for Bundles ('our free new app'), Audiences ('We’re releasing … our latest version'), Shopify Credit ('we built') and ShopifyQL Notebooks (with SH-E-3f85908b);
  - the cell's own maker evidence for Inbox (SH-S-2758), Collabs (SH-S-2760; SH-E-709b37e4), POS Go (SH-S-7269, SH-S-7251), Shop (SH-S-0056) and Shop Pay.
- **`core` on a product named with the platform's brand** (31 notes): each is a surface of the platform's own, `core` by what the post shows:
  - Shopify Tax, Shopify Markets Pro, Shopify Payments, Shopify POS, Shopify Shipping, Shopify Protect and Shopify Duties and Import Taxes;
  - Shopify Magic, the App Store and its Built for Shopify badge, the Help Center assistant and Shopify Markets' subfolders;
  - Flow's plan line (the ruling after SH-55);
  - Marketplace Connect and the Shopify Privacy and Compliance App, with their makers a gap.
- **The first leads that hold nothing,** none of them the entry's thing:
  - CM-CAT-005 (brands) on lines 18, 114 and 130: 'quality Shopify brands' are Collective's suppliers, and 'brand settings' is the store's brand assets, not the products' brands. No capability holds Settings > Brand (see the second stage);
  - CM-CNT-010 (URL structure) on line 105: a market's subfolder is CM-MKS-004's web presence, and CM-CNT-010 is the format of product and page addresses;
  - CM-APP-010 (app settings) on lines 110 and 177: 'integrating Shop Pay into Markets Pro' and Collabs' 'subscription integration' are not parameters an app's developer defines;
  - CM-MKS-009 (countries) on line 180: Markets Pro's supported countries are market data.
- **Line 52's footnote mark:** SH-E-5d9852f8's '->* Customer Events* ->' is the post's emphasis around a menu name, not a footnote.
- **Line 120's app page with no CM-APP-007 line:** Collabs' tier page in the post's link, by SH-35's rule 10.

## Entries I couldn't tell, and what would settle each

- **SH-E-8f406571, Fraud Control:**
  - what it is, and whether CM-CHK-005 is its place (above);
  - an App Store listing or a help page that names it an app and its developer would settle the support.
- **SH-E-eab82f6c, ShopifyQL Notebooks:** whether 'we’ve prepared a summary notebook in ShopifyQL Notebooks' names the app's maker. The app's store listing (apps.shopify.com/shopifyql-notebooks), with its developer, would settle it, as SH-S-2758 settles Inbox.
- **SH-E-e3a378a2, Shopify Credit:** 'we built Shopify Credit' read as a maker statement, against SH-35's `core` on SH-E-57887272 (a post on its remittances), which the coordinator may align. The cell's note says the card's credit limit is set 'by the issuing bank' and its Program Terms are with Shopify Capital. So `own-service` (the platform's group) and `outside` (the bank) stand side by side there.
- **SH-E-463eb101, Ireland's postal code at checkout:** I placed it on CM-CHK-001, the checkout's own address form, with scope Republic of Ireland. CM-CUS-009 (an address service, which the coordinator gives address validation) and CM-MKS-009 (a country's address data, as SH-34 placed Italy's provinces) are the alternatives. A capability for the checkout's address fields would settle it.
- **SH-E-866ffee7's CM-SHP-018 line:** expected delivery dates at checkout, calculated from the processing time, read as delivery promises. If the coordinator keeps CM-SHP-018 for promises with their own settings, the dates stay in CM-SHP-001's reading.
- **SH-E-e96126b5, Asset URLs:** no capability holds the storefront's asset delivery (a CDN, its URLs). I placed it on the online store (CM-SFR-001) and the store's domains (CM-SFR-008).
- **SH-E-8dfc09fc, Klarna:** placed on CM-PAY-015, whose cell holds Klarna, though the post says only 'a payment option'.
- **SH-E-1c0bb5d3, SH-E-6e1e14c1:** Staff sales attribution as `shows` or `core` (above).
- **SH-E-5455ac9d:** Markets Pro's support for digital goods in a mixed cart takes no CM-SEL-002 line, since the goods are what it handles. If the coordinator reads it as a change to digital products' selling abroad, CM-SEL-002 takes `core`.

## Items and sources

- I compared no entry with its page, since no entry's text left a column open.
- The items hold '?' where a post seems to have had an emoji: SH-E-f5575b97, SH-E-5a021236, SH-E-8055d9a1, SH-E-41f97b06. I didn't read the pages to see what they hold.
- SH-E-8e417824 links 'Shopify Blog' to the Help Center's finances report, the same address as its Help Center link. That is the item's `href`, not checked against the page.
- SH-E-8e417824 (24 August 2023) and SH-40's SH-E-9ec6f277 (15 January 2024) hold nearly the same text, with different start dates for their report data: orders on or after June 1, 2023, and on or after January 1, 2023.

## For the second stage: stated, or named in passing, and not placed

- **SH-E-cd115073:** 'You can also customize the availability of PayPal as a payment option using Shopify Functions', a way named in passing (SH-37's rule 5). It is a lead for CM-PAY-019, payment customizations through Functions.
- **SH-E-17eda0f1:** Collabs 'works out of the box with any third party app using the' Shopify Subscriptions API. It is a lead for CM-SEL-001's `extension-point`.
- **SH-E-058c9bf8:**
  - creators' commissions 'are added and processed with the safety and security of your regular Shopify bill', a lead for CM-PLN-004's charges;
  - creators are paid 'via PayPal or bank transfer'.
- **SH-E-aaeaa7a1, SH-E-eb446cdc:** the store's Brand Settings, named in passing ('connect to brand settings'; files used in 'Brand Settings'). No capability holds the store's brand assets: a lead for a cell, or a new thing, if a held page places it.
- **SH-E-e3a378a2:** 'Shopify Credit is not available to merchants with active Shopify Capital financings', a condition between CM-PAY-025 and CM-PAY-026.
- **SH-E-5e7de0cd:** 'To comply with local legislation, customers from the European Union (EU) aren't automatically redirected within the EU'. The law is not named.
- **SH-E-463eb101:** 'to align with the requirements of our shipping carriers'. The carriers are not named.
- **SH-E-c0952d00:** Shop Pay Installments on POS. The post names no provider: a lead for CM-PAY-015's `outside`.
- **SH-E-8f21c2d7:** in POS's product details, 'Apps are now better represented within a dedicated section in the list view'. It is a lead for CM-POS-004.
- **SH-E-0a98d448:** Collabs' 'New online store page which works with the theme app extension'. It is a lead for theme app extensions, which a first-party app uses.
- **SH-E-11696f97:** 'Merchants will always have access to the email address associated with the Shop account used to sign in on their customer record'. It is a lead for CM-CUS-001.
- **SH-E-972db8fe:** 'Just request the appropriate access scope(s) be added to your app'. The scopes are not named; the post links shopify.dev's `smartGridLayoutCreate`.
- **SH-E-e96126b5:** the stricter 'content security policies (CSP) and cross-origin resource sharing (CORS) policies' the change allows. It is a lead for the storefront's security.
- **SH-E-ff15a593:** translated URL handles, a lead for CM-CNT-010, if the coordinator reads a product's handle per language as its address's format.

## Problems with the brief or the scripts

- None blocked the batch. The checker's quote test followed the three ids my readings cite.
- The ruling after SH-57 arrived while I worked. I read my 100 lines written by then against it, and dropped one (SH-E-69c6bd0e's CM-SFR-012).

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 130 of 130 entries, no problem, after the changes below.
- **The ruling after SH-41** (`review-H-rulings.md`): the first-party rule holds for a separate product or service too, as B-extent has it.
  - **Fraud Control's lines are `own-service`,** lines 37 and 38. 'We're thrilled to announce the introduction of Checkout Rules for Fraud Control' names Shopify as the feature's maker, and the post is filed under Apps. CM-CHK-005 so gains `own-service`, not `core`, which fits its 'app-written rules'.
  - **Shopify Credit's features are `own-service`,** as line 32 reads 'we built Shopify Credit'. SH-35's, SH-36's, SH-37's and SH-39's five lines are aligned. The admin's Credit routes (SH-11) and the plan rows stay `core`.
- **The other cell changes stand:**
  - CM-ANL-001 gains `own-service` from ShopifyQL Notebooks: 'we’ve prepared a summary notebook in ShopifyQL Notebooks'.
  - CM-MKT-023 is held from Search & Discovery's product recommendations, which the app provides itself (the ruling after SH-57).
  - The repeats stand.
- **Collective's two CM-CAT-010 `shows` lines stand,** as the cell's note asks. The ruling after SH-57 is for `own-service` lines on another capability.
- **The rules this batch wrote stand for SH-42 to SH-46:** a first-party app's release on CM-APP-011; Collabs' posts on CM-MKT-014 and CM-MKT-015; Markets Pro's payouts; a kind of store as scope, a sales minimum as a quality.
- **Cost:** 24.6 million tokens over 96 requests, about 189,000 an entry. The context reached about 424,000 tokens.
