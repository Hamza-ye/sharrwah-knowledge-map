# Held pass, BigCommerce, batch BC-1: notes

147 entries from six structures of other-product-class at `0d79b794f`: channel-catalog (1 to 19), contracting-entities (20 to 24), payment-gateways (25 to 81), plan-comparison (82 to 100), settings-list (101 to 140) and tax-services (141 to 147). Every entry is placed: 143 on capabilities, 4 new, none out. Where an entry is several capabilities' at once, it has several lines, so `placements-BC-1.tsv` has 175 lines. No batch before this one splits these structures.

Every placement is a reading of the entry, unless the line says it is a fact. Addresses and page text cited below are facts at `other-product-class@0d79b794f`, at the run and step named.

## New things

All four are sections of the control panel's own Settings list (`bigcommerce/structures/settings-list`; source `bigcommerce/raw/runs/20261029T012951Z-store-settings-en/steps/002.frame-0.aria.yaml`). Each has a **place of its own** of the kind "an admin section": a settings item the platform's Settings list names with its own title and its own address. BigCommerce states them in English only, so each has one name. Three of them are tabs of one page, `/admin/index.php?ToDo=viewSettings`, under the group General. That page's other tabs are placed on existing capabilities: Website, Search, Security & Privacy and Miscellaneous.

| New thing | Entry | Address (source step) | Proposed domain, area, parent | Terms searched (`class_slice.py caps`, every domain) |
| --- | --- | --- | --- | --- |
| `new:Display`: "Settings related to displaying products, categories, control panel etc." | 110, BC-E-812a36d2 | `viewSettings#DisplaySettingsTab` | E, SFR; parent CM-ACC-006, following BigCommerce's grouping (General), or CM-SFR-001 | display settings; display; product display; breadcrumbs; storefront display; show prices; product page settings; category page |
| `new:Share`: "Social sharing settings on product pages and blog posts" | 111, BC-E-ba87a83d | `viewSettings#SocialSettingsTab` | E, SFR or D, MKT; parent CM-ACC-006 (General), or CM-SFR-001 | social sharing; share; sharing; share buttons; social buttons; like button; social media; social media posts |
| `new:URL structure`: "Product, category and web pages URL settings" | 112, BC-E-9087905a | `viewSettings#URLStructure` | E, CNT; parent CM-CNT-007 (SEO) or CM-ACC-006 (General) | URL structure; URL settings; custom URLs; permalinks; URL; permalink; slug; URL format; product URL |
| `new:File access (WebDAV)`: "Application that allows uploading files to store's server" | 133, BC-E-8dec1b9a | `/admin/index.php?ToDo=viewFileAccess` (group Advanced) | E, CNT; parent CM-CNT-001 (Files) | WebDAV; file access; file upload; FTP; SFTP; server; uploading files; file manager; image manager |

- **URL structure:** I didn't place it on CM-CNT-006 Custom URLs. That capability is Salla's, and no statement defines what a custom URL is (CM-CNT-006's note). Joining on the word "URL" would decide the thing from its name. If the coordinator reads Salla's Custom URLs as the format of product and page URLs, it belongs there.
- **File access (WebDAV):** CM-CNT-001's BigCommerce cell already meets WebDAV once: "files added to digital products via the control panel or WebDav" (BC-S-0023, cited in CM-SEL-002). That statement names no place.

## Entries I couldn't tell, and what would settle each

1. **Payment gateway rows (25 to 47, 55 to 76).** These are rows of a Help Center table naming a third-party gateway. I placed them on CM-PAY-011 as `shows`, by the brief's rule for help pages: `shows` where the page names only a third party. Each gateway is its slot filler and each feature mark is a quality. Two other readings are possible:
   - `outside`: the gateway is named as doing the processing;
   - `core`: the article calls them "BigCommerce gateway integrations".

   What would settle it is a ruling on a help-page table of third-party providers. The same rule applied gives:
   - the offline methods (77 to 81) and the BigCommerce Payments row (32): `core`, as the platform's own built-in features;
   - the "app payment processors" (48 to 54): `extension-point`, as apps.

   One difference with the existing cell: CM-PAY-002's cell reads a similar row, BC-S-0148, as `shows`.
2. **Gateways not given a second capability.** The entries don't say that Affirm, Afterpay, Clearpay, Klarna Payments, Sezzle and Zip are instalments or buy now, pay later, or that BitPay is cryptocurrency. So they aren't placed on CM-PAY-015 or CM-PAY-018, though CM-PAY-015's cell reads them that way by their names. Amazon Pay (29) has a second line on CM-PAY-012 because the article itself calls it one of the "leading digital wallets" (run `20261029T024758Z-help-center-en`, step 001). PayPal (39) has a second line on CM-PAY-013.
3. **The Feedonomics channel cards (1 to 5, and 9 to 13).**
   - Entries 1 to 5 sit in the region "Featured channels by Feedonomics". I placed them as `extension-point`, with Feedonomics and the channel as fillers.
   - Entries 9 to 13 are the same five cards in "Ads and social". Their own text doesn't name Feedonomics, but the source gives each the same Learn more article, `support.bigcommerce.com/s/article/Feedonomics-for-<channel>` (run `20261029T023811Z-channels-en`, step 002.frame-0). So I placed them the same way, on the page read as a whole. A stricter reading of the entry text alone would make 9 to 13 `core`.
   - Not `own-service`: no entry names Feedonomics as a company of Commerce's group. CM-CHN-004's cell reads BC-S-0366, the terms' row for Feedonomics Holdings, LLC, as maker evidence. If the coordinator keeps that reading, these cards could support `own-service`.
4. **Amazon, Walmart, eBay (16 to 18) and Buy Buttons (14).** I placed them `core`: cards of the Channel Manager's own catalog, with no maker of the connection named. Who builds these connections isn't stated, as CM-CHN-003's cell already says. A statement naming the connector's maker would settle it. Buy Buttons has no capability of its own, so it is on CM-CHN-001. Its Learn more slug, `Buy-Buttons-app`, isn't words naming an app.
5. **PayPal Zettle POS (15), DEITY (8), impact.com (19).** I placed them `extension-point` and not `core`. Each names a third party's solution doing the work through the catalog, and `core` would claim the platform does POS, storefront or affiliate marketing itself. impact.com is the first BigCommerce entry on CM-MKT-013, which was none-held.
6. **Contracting entities (20 to 24).**
   - On CM-ACC-002 as `shows`, as that cell reads its other rows. Each row's governing law is its filler.
   - A second line on CM-APP-011 as `own-service`, because each row names a Commerce entity as the provider of "Extensions", as that cell reads BC-S-0428 and BC-S-0432. What an Extension is isn't in the entries. The terms' definition would settle it; the cell cites BC-S-0464.
   - "Certain Professional Services" is left unplaced. No capability is the platform company's own professional services: CM-PTN-005 is partners' services.
7. **Comments (121).** On CM-SUP-001 because CM-SUP-001's cell has product reviews going "through the built-in comment system" (BC-S-0072). The Comments settings page itself isn't read, and it would settle whether this is reviews or a separate comment system.
8. **Miscellaneous (115).** On CM-ACC-006, as a tab of the store's general settings page that holds fields only: email settings, advanced store settings, order settings, throttler. It could instead be a new thing, or its fields could be placed one by one. CM-MKT-022's cell already cites a setting under Settings > General > Miscellaneous.
9. **Security & Privacy (114).**
   - CM-TRU-006, the storefront's privacy settings, rests on CM-TRU-006's cell, which holds cookie consent under Security Settings (BC-S-0216).
   - The second line, CM-TRU-001, reads "security settings for ... control panel" as the admin's sign-in security. The tab's fields aren't held; reading them would settle it.
10. **Website (109).** On CM-CNT-007 (SEO and robots) and CM-SFR-010 (HTTPS). Its "Physical dimension settings" are fields of the tab, and no capability holds them.
11. **MCP (140).** On CM-AIA-004, an MCP the platform provides that the merchant configures. CM-AIA-005's cell has BigCommerce's Storefront MCP as a buyer's agent. If `/manage/microapps/ai-labs-ui/mcp-settings` configures the Storefront MCP, the entry is CM-AIA-005's. That page would settle it. The source marks the section "new" (a release marker), and Search (113) too.
12. **Storefront API Playground (136).** On CM-SFR-012, as a tool for that API. It could be CM-DVT-001's, developer tools. I left out a second line there, so the entry isn't `core` in two domains.
13. **Account sign up form (130).** On CM-CUS-010 (sign-up form fields), plus a line on CM-CHK-009 for "addresses on checkout". CM-CHK-009's BigCommerce cell was none-held. The second line rests only on the description's words.
14. **Accounting (127).** I placed it `core`, as the platform's own Settings section for connecting accounting software. Its address, `/admin/apps/accounting`, is under `apps`, but it is named for no one app. If a route under `apps` counts as an app's page, it would be `extension-point`, as CM-PAY-028's cell has the App Marketplace categories.
15. **Tax services (141, 143 to 147).** I placed them `extension-point` on CM-TAX-004:
    - each has an `app_id`;
    - the page offers each with "Install";
    - the recommended one is "An automated solution for sales tax calculation, integrated with BigCommerce." (step 043.text.txt, step 045.text.txt).

    Every provider, Basic Tax included, carries `type: platform`, and its meaning isn't stated. If it means the platform integrates them itself, they would be `core`. Basic Tax (142), with no `app_id`, is the platform's own and is on CM-TAX-001.

    Avalara (141) has a second line on CM-TAX-006 for "automatic return filing". CM-TAX-006 is a child of the platform's own tax service, so the coordinator may prefer only CM-TAX-004.

    For scope, each takes its `supported_countries`. These entries are the answer with the store's default country set to the United States (steps 43 to 45). The register says the list is the same for four default countries; I didn't read the other answers.
16. **Surcharge rate (94).** The row doesn't say what the rate is charged on. I read it as the platform's fee on sales by plan, CM-PLN-003, whose cell has the same values (BC-S-0152). The article's Open Payment Provider fee would settle it.
17. **Full-featured storefront included (82).** One plan line naming four things, so four lines: CM-SFR-001, CM-CHK-001, CM-PAY-012 and CM-ANL-001.
18. **Values in the plan rows I left out as qualities:** "convert 15% of abandoned carts into sales on average" (89) and "Improve conversion by as much as 10%" (96). These are claims of effect, not limits.

## Where the entries differ from what the model's cells say

- **Storefronts that can be added (83).** The table states 4 (Core), 5 (Growth), 8 (Scale), 15 (Performance). CM-CHN-007's cell cites "max. 3" for $30/mo (BC-S-0228). Possibly one counts the first storefront and the other doesn't; neither statement says.
- **Inventory locations (98).** The table states "Up to 50" for Performance. CM-INV-005's cell reads "Custom" for Performance (BC-S-0038).
- **Payments (104).** CM-PAY-001's cell says no control panel page where the merchant activates payment methods is held. The Settings list holds one: Payments, `/manage/microapps/payments-settings-ui`.
- **Cells that were none-held and gain a placement:**
  - CM-EVO-001 (Early access, 135);
  - CM-MIG-003 (Export templates, 131);
  - CM-CHK-009 (130);
  - CM-AIA-004 (140);
  - CM-MKT-013 (19).
- **Cells that were not-stated and gain `core`:**
  - CM-ONB-003 (Phone support, 95);
  - CM-ACC-002 stays `shows`.

## Structures whose items and source disagree

- **settings-list.** As the brief says (handoff H-009): each item pairs its section with the next section's address. For example, item 1, Store profile, carries `/manage/microapps/localization-settings-ui`, while the source step gives it `/manage/microapps/store-profile-ui`. Every address in my readings is the section's own, taken from `steps/002.frame-0.aria.yaml`. The source also marks Search and MCP "new", which the items leave out.
- **plan-comparison.** I checked every row against `source.html`. The entries, rendered from `feature_text` and the cells, match the source's rows. The items' `feature` field is wrong for rows 8 to 13, as the brief says. Each `[image]` is an SVG check mark in the source.
- **channel-catalog.** The items leave out each card's Learn more link, which is what ties entries 9 to 13 to Feedonomics. They also leave out the Storefronts region's "Create more storefronts with paid plan" block and its "Upgrade plan" button, which has no entry, and the "View more storefront platforms" link (`developer.bigcommerce.com/tools-resources#headless-integrations`).
- **payment-gateways.** The items hold the tables only. The article's prose around them isn't an entry, though it bears on several of them:
  - its fee rules: no Open Payment Provider fees through Embedded Payment Provider integrations; Open Payment Provider fees for self-serve plans, offline methods included; Performance plan stores under contract exempt;
  - "Powered By" stores may not have every gateway;
  - the Check footnote on B2B Edition's Purchase Order method;
  - the wallets' place under Settings › Payments;
  - the hosted gateways list.

  That prose is CM-PLN-003's, CM-PAY-012's and CM-PAY-008's to read.

## Problems with the brief or the script

- **The brief's two rules give different answers for a help page's list of third-party providers.** The help-page rule says `shows` where a page names only a third party. The `outside` rule says `outside` for a third party named as doing it with no interface named. I followed the help-page rule (item 1 above).
- **The supports rules don't cover a catalog card in the platform's own admin that names a third party as the venue or the provider.** Channel Manager's catalog is close to an app category. I used `core` where the third party is only the venue (a marketplace) and `extension-point` where it is named as the provider (Feedonomics, PayPal Zettle, DEITY, impact.com).
- **`show --candidates` drops a word's first letter when it matches inside a longer word.** Examples:
  - "igCommerce" from BigCommerce;
  - "ikTok" from TikTok;
  - "ayPal" from PayPal;
  - "ebDAV" from WebDAV.

  Those substrings then match unrelated capabilities, such as CM-PAY-019, CM-OPS-001 and CM-API-005 on every entry naming BigCommerce. Most leads in this batch were noise for that reason. None was taken without reading the cell.
- **Several values can't be separated within one quality piece.** `;` separates fillers and qualities, so a value by plan is written in one piece as "<what>: <value> (<plan>), ...".

## Corrections after the review (the coordinator, 30 October 2026)

The review (`held/review-H.md`, parts R1 to R3) and the coordinator's rulings (`held/review-H-rulings.md`) corrected this batch. 156 verdicts were applied as they stand, with the review's own values; the coordinator's hand pass did the rest. Line numbers below are the review's, at `ff50bbee`.
- **`own-service`:** the 16 Feedonomics card lines (2 to 9, 14 to 21). The terms page names Feedonomics Holdings, LLC among Commerce's affiliates and subsidiaries (M-1). Feedonomics is no filler; each card's channel is.
- **`core`:** the 44 gateway rows of tables 1 and 3, the platform's own integrations (M-4), and Amazon Pay's wallet line, set up in Settings › Payments.
- **`shows`:** BigCommerce Payments' row: a product named with the platform's brand names no maker.
- **`extension-point`:** the Tax section's recommended services, and the accounting software section (M-7).
- **Moved:** MCP to CM-AIA-005, whose cell cites the same place; the sign-up form's address fields to CM-CUS-008; File access (WebDAV) to CM-CNT-001, not new.
- **Lines added:**
  - recurring payments on CM-SEL-001, for the 15 gateway rows that mark them;
  - CM-PAY-016 for Bank deposit and Cash on delivery, under its offline methods;
  - CM-B2B-001 for Check's footnote;
  - the loyalty program, order settings and coupon limits that three descriptions name;
  - Apple Pay and Amazon Pay as CM-PAY-012's fillers.
- **New things with no place of their own:** `new:Extensions` on the five contracting rows (M-2: an Extension is a service a third party develops and Commerce provides, not an app its company makes), and `new:Professional Services` on the same rows.
- **Marks:** every ✔ and `true` mark moved from `quality` to `reading`. Custom SSL's and Shipper HQ's plans are their scope.
- **The misquote** 'outside the Embedded Payment Provider list' is corrected to the article's words on 22 lines.
- **The plans' prices** (BC-E-f167af9a, added to the batch by the `meta:` rule): CM-PLN-001, with each plan's price as a quality, and CM-PLN-002, the billing period, which held nothing.
- **Kept as placed, can't tell,** with what would settle each in the review's rows:
  - whether Google's "AI-powered experiences" are CM-AIA-005's (R1);
  - which PayPal the PayPal row is (R2);
  - which capability "regional settings" is, and whether the security tab is sign-in security (R3).
