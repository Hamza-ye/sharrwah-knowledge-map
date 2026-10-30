# Held pass, Zid, batch ZD-5: notes

194 entries, all of Zid's `dashboard-route-manifest`, every one a child route of the store (`$lang.stores.$storeId`). They include the sections' own index routes (marketing, customers, catalog, settings, services, checkout, channels, support, finance, orders, apps), the store's index and its catch-all `*`, and the routes under services, marketing, channels, catalog, analytics, settings, finance, customers, orders, apps, support and checkout that ZD-4 left. Evidence at other-product-class@0d79b794f.

**Placed:** 191 entries on capabilities, 2 `new`, 1 `out`, in 227 lines. 33 entries take two lines. Every line supports `core`. No `own-service`: no entry names Zid's company as a maker. No `extension-point`: the apps' embedded page (140) takes CM-APP-007 `core`, as ZD-1's corrected lines do. No line has a scope (see "Scope"). Slot fillers, each named in the route's own path: Emkan (15), mis-pay (54, written as the path spells it, since the checker takes a filler only from the entry's text), Tamara (70), Tabby (81), Madfu (82), Qitaf (18, 126, 165), Mokafaa (57, 146), ZATCA (31, 96), WhatsApp (14, 34, 69).

Entry numbers below are the batch's order (`held_entries.py show --batch ZD-5`).

## How I read the entries

As in ZD-1 and ZD-4, a route entry gives only its id, parent, path and index flag. Where the path left the thing unclear, I read:
- the route's item in `zid/structures/dashboard-route-manifest/items.jsonl`, for its `module` and `imports`. Readings cite these as "module imports ...". Every line was decided from the module, the page and the cells. The leads (`--candidates`) now read a route's path segments, as the coordinator's check of ZD-4 added, and I read each one. I left out the leads that came only from a word every route of a section holds.
- the page as a run opened it, through `zid/index/ledger/dashboard-routes.tsv`, cited as "page text <run>#<step>", meaning `zid/raw/runs/<run>/steps/<NNN>.text.txt`. The run labels are ZD-1's and ZD-4's (`rest-en`, `gaps-en`, `en`, `en-2`, `en-3`, `devstore-markets-en`), and also:
  - `devstore-billing-en`: 20261028T190230Z-devstore-billing-en;
  - `devstore-tracking-apps-en`: 20261028T185150Z-devstore-tracking-apps-en;
- for four routes, strings of `zid/structures/dashboard-locales/items.jsonl`, cited by namespace and key: charity fostering (20), the five sales journey (134), the App Market's solution page (150), and the Services and Search names (164, 183).

Where ZD-1 (the page index) or ZD-4 placed the same page or a sibling route, I kept to its capability, its second lines and its filler. The reading says so ("ZD-1's ...", "as ZD-4's ..."). Where the review corrected a ZD-1 line by adding a second capability, the same page's route here takes that second line too: SHP-009 for shipments, NTF-001 for automated messages, ACC-007 for hours of operation, MKT-022 for abandoned carts, MKT-002 for discounts, PAY-012 for Qitaf and Mokafaa, ACC-004 for store information, STF-002 for team, and INV-001 for the Inventory container. Several CHANGES lines come only from this: ZD-1's corrections aren't amended into the model yet.

**Scope.** No line has a scope. No module of this batch imports a guard (I searched every import's name for `guard`), and the brief says a module an item imports isn't a condition by being imported. ZD-1's page-index lines for several of these pages took a store condition from `source.js`, which isn't these entries' source, so I left those conditions out, as ZD-4 did:
- `showNewZones` for zones (72), which opened as 'This feature is not enabled for your store.' (rest-en#169);
- `hasNewGifting` for gifting settings (48 to 52) and `not hasNewGifting` for gift options (154);
- `customerWallets` for the customer wallet (158) and cashback offers (58);
- `mustUseMarketsPricing` for markets (67, 152);
- `hasPos or subscription.is_trial` for the POS (109, 111, 120, 138);
- `not an NGO store` for the inventory report, preorders, inventories, options, filters and logistics analytics.

The coordinator may want the route lines aligned with the page-index lines.

## The new things

**`new:Services`.** Entry 164, ZD-E-5f1a1e80, `services` (the index route `$lang.stores.$storeId.services._index`).
- **What it is:** the dashboard's Services section, a container (M-13). Its children are `services/payments`, `services/logistics`, `services/whatsapp`, `services/financing` and `services/growth`, placed in ZD-1, ZD-4 and here on CM-PAY-002, CM-SHP-001, CM-NTF-004, CM-PAY-026 and CM-PTN-005. Its own page (rest-en#218) promotes three of them: 'One Gateway, Multiple Payment Options', 'Get up to SAR 5 Million in Financing!' and '35+ Shipping Providers in One Digital Agreement'.
- **Why new:** its title, Services, names no capability, and no cell's reading shows it as a place. `class_slice.py caps --terms "Services; الخدمات"` finds only capabilities whose terms hold the word in another sense, such as CM-MKT-010's Salla term الربط مع الخدمات الإعلانية. Its page shows three capabilities, not one. The cells cite it only as the prefix of a path, such as CM-PAY-032's الخدمات > المدفوعات > روابط الدفع.
- **Its place of its own:** an admin route, the manifest's `services`, and a sidebar section.
- **Proposed home:** domain A, as a grouping of the admin. `out` is the alternative, if the coordinator holds that a container whose children are all placed adds nothing.
- **Names:** English Services, Arabic الخدمات (dashboard-locales, `navbar:services`).

**`new:Search`.** Entry 183, ZD-E-01ed3f06, `search` (index route).
- **What it is:** the dashboard's own search. The module imports `use-initial-search-category`, `navbar-new-product-dialog` and `template-dialog`. The page broke when opened ('Oops! Something broke', rest-en#232). The sidebar shows '[Search]' with 'Ctrl + K' on every page.
- **Its place of its own:** an admin route, `search`.
- **Proposed home:** domain A, area ACC, parent CM-ACC-006 (the admin's own settings and places), or `out` if the coordinator reads an admin search as a UI tool rather than something the platform does for the merchant.
- **Not CM-SFR-013:** the checker's lead. That capability is the storefront's search and filters for buyers.
- **Names:** English Search, Arabic بحث (dashboard-locales, `navbar:search`).
- **Searched:** `caps --terms "admin search; search the admin; global search; البحث"`. It finds only CM-ACC-006 (Salla's settings search), CM-CNT-007 (search engines) and CM-SFR-013.

## Entries I couldn't tell, and what would settle each

- **The BNPL providers' pages: 15 Emkan, 54 MISpay, 70 Tamara, 81 Tabby, 82 Madfu.** Each page's header reads 'By: Zid' under the provider's name (rest-en#124, #154, #167, #172, #173), like an App Market card. I placed each on CM-PAY-015 `core`, with the provider as its filler, as ZD-4 placed the other payment providers. I read 'By: Zid' as naming Zid as the maker of the connection, not of the instalment service: the pages name the provider as the one that lends and bears the risk ('Emkan absorbs the risk associated with customer payments.', rest-en#124; 'We assume credit and fraud risk', rest-en#154). If the coordinator reads 'By: Zid' as maker evidence, the lines would be `own-service` for the connection. A statement of what 'By:' means on these cards would settle it.
- **8, `checkout/request-vat-invoice`.** Two lines: CM-PLN-004 (Zid's invoice) and CM-PLN-007 (VAT on Zid's charge). The store's `checkout` route is the checkout of its purchases from Zid: the development store reached it from a plan, `checkout?filters.package_code=rise.monthly` (devstore-billing-en, actions.jsonl, steps 5 and 6). I placed nothing on CM-TAX-005, which its note keeps for buyers' VAT numbers.
- **20, `marketing/charity-fostering`.** Placed on CM-SEL-007 (Donations), whose Zid cell holds nothing. The page lists charity opportunities, with 'Item cost', 'Supported units' and 'Remaining units' (rest-en#127). The dashboard's strings invite the store's customers 'to participate in the donation in partnership with the {{name}} association' (`charity-fostering:form.placeholder`), by a 'Charity campaign information' message (`form.dialogTitle`) sent under the store's sender name (`senderNameUnderReview.description`). Two alternatives:
  - CM-MKT-007, if the coordinator reads it as a message campaign;
  - `new:Charity fostering` (دعم الجمعيات الخيرية), if the store's sponsoring of an association isn't buyers' donations.

  The page opened with no opportunity, so a run on a store whose sender name is approved would settle it.
- **40, `channels/mobile-app/banner`.** Two lines: CM-CHN-006 and CM-SFR-007. CM-SFR-007's Zid cell holds nothing. The page: 'App download advertisement from the store', 'Use this feature to show the app download ad on your store' (rest-en#143). I read it as an ad the storefront shows. If the coordinator reads SFR-007 as only announcement bars and pop-ups, CHN-006 alone remains.
- **47, `analytics/insights/analyst`.** Placed on CM-ANL-001 with ZD-1's Zid Insights. The page is a chat: 'Ask Zid Insights about sales, products, or customers and get an answer grounded in your store data.', with 'New chat' and 'Conversation history' (rest-en#148). It doesn't say AI, so I gave it no CM-AIA-002 line. A statement that Zid Insights' answers are an AI's would make it CM-AIA-002's too. This is ZD-1's open question on Zid Insights.
- **63, `catalog/products/arrange`.** Placed on CM-CAT-001. 'Product sorting' sets each product's position (rest-en#162). Where that order shows, presumably the storefront, isn't stated. If it is the storefront's order, it is CM-SFR-015's too, a cell that holds nothing. 28, `categories/arrange`, takes CM-CAT-003 alone, as ZD-4's `categories/:id/arrange` did.
- **72, `services/logistics/zones`.** Placed on CM-SHP-001 with no scope, since the route imports no guard, though ZD-1 gives the page `showNewZones` from `source.js` (above).
- **73, `services/growth/services`.** Placed on CM-PTN-005 `core`. The list names services and their prices, but no provider (rest-en#170). CM-PTN-005's Zid cell holds `extension-point` from each service's partners, which this page doesn't show.
- **88, `finance/billing/addons`.** Placed on CM-PLN-004, the cell's Value Added Services. Each add-on on the page is another capability's, and I didn't place them, since no entry holds them (M-12). They are listed under the second stage below.
- **89, `catalog/inventories/:id`.** A second line on CM-SHP-007 (pickup), resting only on the module's imports `pickup-option-create-dialog` and `pickup-option-edit-dialog`. Not opened. ZD-4's `services/logistics/store-pickup` already places pickup.
- **99, `finance/wallet/verify`.** Two lines: CM-PLN-006 (the wallet) and CM-TRU-002 (verifying the person by 'ID number' and 'Business type', rest-en#184). CM-TRU-002 may be meant only for the store owner's checks before payments. The coordinator may keep the wallet alone.
- **101, `channels/pos/subscribe`.** A second line on CM-POS-002, since the subscription's packages list a 'Tablet' and a 'Tablet stand' beside 'Software Only' (rest-en#185). If the packages are software licences only, CM-POS-001 alone remains.
- **106, 124, the order summaries.** Placed on CM-ORD-008, since that cell cites Zid's order summary (ZD-S-0823) and CM-ORD-009's reading says Zid's summary is issued and emailed in place of an invoice, not stated as printed. The modules import `printable-components` and `printable-barcode`, which suggests they are printed: CM-ORD-009 is the alternative, a cell that holds nothing (the checker's lead).
- **123, `settings/team/logs`.** Placed on CM-TRU-003 (Audit log), which holds nothing: 'Audit Log': 'Only actions from the last 30 days are shown below.' (gaps-en#32). This is no store logger (CM-OPS-005, the checker's lead).
- **150, `apps/solution/:id`.** Placed on CM-APP-002 (the App Market). The page is titled 'Solution' (`pages:marketAppSolution.title`). Not opened, so what a solution is isn't held.
- **172, `apps/:id/plans`.** Placed on CM-APP-003, read as an app's pricing plans that the merchant pays through Zid (module imports `use-plan-period-filter`, `is-sar`). Not opened. CM-APP-002 is the alternative.
- **173, 174, 188, Support.** Placed on CM-ONB-003, the platform's support for merchants: 'Merchant support' and 'Create ticket' are the store's tickets to Zid (rest-en#224, #225). They are not the customers' tickets (CM-SUP-005, `customers/support`).
- **181, `notifications`.** Placed on CM-NTF-002: the dashboard's 'Notification center', by orders, abandoned carts, payments, logistics, store activity and subscriptions (rest-en#231). It is no webhook (CM-API-009, the checker's lead).
- **Containers.** Each is placed on the capability its title names or its page opens (M-13), with its children named here:
  - **157 Marketing:** CM-MKT-005 (ZD-1).
  - **161 Customers:** CM-CUS-001 ('Customer list'). Its children: groups, wallet, questions, reviews, support and stock notifications.
  - **163 Settings:** CM-ACC-006 (ZD-1).
  - **164 Services:** new (above).
  - **169 Channels:** CM-CHN-001. Its page shows only untranslated keys such as 'landing.sales.title' (rest-en#221).
  - **174 Support:** CM-ONB-003.
  - **176 Finance:** CM-PLN-006 and CM-PAY-005, by its page's two balances (rest-en#227). Its children: billing, wallet, credits and invoice-not-ready.
  - **178 Catalog:** CM-CAT-001, redirected to products. Its children: products, categories, brands, inventories, options, filters, custom fields and preorder campaigns.
  - **185 Orders:** CM-ORD-001.
  - **190 Apps:** CM-APP-001 and CM-APP-002 (ZD-1).
  - **193, the store's index:** CM-ANL-003, as ZD-4's store route.
  - **23 Pages:** CM-CNT-003. Its children are custom (24) and legal (26). Legal also takes CM-CNT-003, being a tab of the store's Pages (M-6).
- **194, `*`.** `out`: the catch-all route shows 'Oops! This page took a detour' (rest-en#235), a not-found page that names no place.

## A structure whose items and sources disagree

None. Three entries are index routes with no `path` (25, 52, 193). Their text holds only the id, so their terms come from the id's words (`pages`, `gifting-settings`, `stores`).

## What a source or run step states that no entry holds (for the second stage)

All the files below are `zid/raw/runs/<run>/steps/<NNN>.text.txt` unless another file is named.

- **CM-PAY-007, CM-PAY-005:** Zid Payments' fees and collection (rest-en#114):
  - 'Payments fees depend on your current package in Zid, upgrade your package for lower fees', with the rates per package, such as Rise '1% + 1 SAR';
  - 'Every sunday - tuesday - thursday of every week';
  - 'The minimum collection is 100 riyals';
  - 'The deposit fee is 3 riyals on the total collection process'.
- **CM-PAY-015:** who bears the risk:
  - 'Emkan, a subsidiary of Al Rajhi Bank, offers the Sharia-compliant "Pay Later" service' and 'Emkan absorbs the risk associated with customer payments.' (rest-en#124);
  - MISpay's 'We assume credit and fraud risk, so you can focus on running a successful business.' (rest-en#154);
  - each page's 'By: Zid' (above).
- **CM-POS-001, CM-PAY-015:** POS Go's 'Support for multiple payment methods like cash, Tabby, Tamara, and payment links, all synced and ready to use.' (rest-en#189).
- **CM-PAY-026:**
  - 'Zid Financing requires your store sales to exceed 40,000  in the past 3 months' (rest-en#156);
  - 'Get up to SAR 5 Million in Financing!' (rest-en#218), against ZD-1's note of "up to 10m".
- **CM-SHP-015:** '35+ Shipping Providers in One Digital Agreement' (rest-en#218).
- **CM-PLN-006, qualities:**
  - 'A fee of SAR 9 will be deducted from the amount to be withdrawn' and 'The amount will reach your bank account within 2 to 5 business days' (en-3#3);
  - the wallet's 'Set a percentage or fixed amount of each transaction for wallet expenses, such as shipping, add-ons, or internal costs.' (rest-en#226).
- **CM-PLN-004, CM-TAX-007:**
  - Zid's invoice 'is being processed in the tax system (Fatora platform)': 'It might take up to 15 days to proceed.' (rest-en#159);
  - the VAT invoice 'usually takes up to 1 hour' (rest-en#120).
- **CM-PLN-002:**
  - 'Auto-renews every month on November 28th' (devstore-billing-en#5);
  - 'Monthly payment plan', 'Annual payment plan', 'Save 16%' (en#18).
- **CM-PTN-008:** the Billing page's '30% commission': 'Tell merchants about Zid and get a reward for every new subscription to Zid packages' (gaps-en#41), a referral of Zid's own plans.
- **The add-ons** (gaps-en#43), each for its own capability:
  - 'Campaign text messages': CM-MKT-007, CM-NTF-004;
  - 'Domain Renewal', 'New Domain', 'Domain Change', 'Domain Transfer': CM-SFR-008;
  - 'SoftPOS - Yearly', 'Tablet Stand', 'iMin (Dual Screen with NFC)', 'Cash Drawer', 'NFC Tablet', 'Epson TM-M30II Printer': CM-POS-002;
  - 'Team Members': CM-STF-001;
  - 'Mazeed Package': CM-CHN-002;
  - 'Add Inventory': CM-INV-005;
  - 'Hosting Store's Customer Data in Saudi Arabia': CM-TRU-014, a data location.
- **CM-PTN-005:**
  - the growth services' prices, such as 'Switch store service' 'Starts from 2,500.10' (a lead for CM-MIG-005), 'Zid Ads Packages' and 'Amazon - Basic package' (rest-en#170);
  - the relationship manager, 'available only for merchants with over 2,500 lifetime orders or professional and enterprise merchants.' (rest-en#182).
- **CM-LOY-004:** Qitaf's 'Submitting requests to activate the Qitaf program is currently suspended.' (rest-en#219).
- **CM-CAT-001, a quality:** deleted products are kept 'from the last 60 days' (rest-en#161).
- **CM-TRU-003, a quality:** the audit log shows 'Only actions from the last 30 days' (gaps-en#32).
- **CM-LOY-006, a quality:** the gift card's message, 'Number of characters: 240 maximum' (rest-en#136).
- **CM-MKS-001:** 'You can assign a different theme to each market for a localized storefront experience' (gaps-en#10).
- **CM-AIA-004, CM-MKT-021, CM-APP-011:**
  - the App Market's 'Zid AI Connector | MCP', 'Enable your AI assistant to manage your Zid store through a simple, secure connection.', and 'Ziadah AI Upsell' under 'Cross-sell & Upsell' (gaps-en#38);
  - the category 'Made for Zid' (gaps-en#37), a lead for apps by Zid's company, whose maker isn't stated.
- **CM-AIA-003, CM-ONB-004:** the five sales journey's 'Enhance your store with Zid AI: better descriptions, sharper visuals, and a persuasive tone.' (rest-en#203).
- **CM-SEL-007:** charity fostering's strings, above (dashboard-locales, namespace `charity-fostering`).
- **CM-CUS-008, CM-SHP-001:** 'The short national address is now required for shipping within Saudi Arabia.' (rest-en#145), as ZD-4 noted from another page.

## Problems with the brief or the script

- **Containers by path.** The checker's container note sees only `channels/online-store/pages` and `settings/gifting-settings`, whose children name them as `parentId`. Most of this batch's containers are the sections' index routes (`marketing._index`, `customers._index`, `catalog._index`, `finance._index`, `services._index`, `support._index`, `orders._index`, `apps._index`, `settings._index`, `channels._index`), whose children hold them by path, so the checker doesn't flag them. I placed each by rule 3 (above).
- **A filler spelled by the path.** The checker takes a filler only from the entry's text, so MISpay's filler is written `mis-pay`, as its path spells it. The page spells it 'MiS Pay', 'Mispay' and 'MISpay' (rest-en#154).
- **ZD-6** hasn't run. It holds the rest of the manifest.
- No rule of the brief read differently from B-extent.md for this batch.
- The checker's final line: see the report.

## The coordinator's check (30 October 2026, after the batch)

- **The three cells this batch makes held stand:** charity fostering, a list of charity opportunities with 'Item cost', 'Supported units' and 'Remaining units', is CM-SEL-007's, donations; the app download ad the storefront shows is CM-SFR-007's, banners; and the team's 'Audit Log' is CM-TRU-003's. CM-LOY-008, customer referrals, is the capability made from ZD-1's new thing.
- **'By: Zid' on the instalment providers' pages** (Emkan, MISpay, Tamara, Tabby, Madfu) names Zid as the maker of the integration in the dashboard's own Payments section. The instalments are the provider's, so the lines stay `core` on CM-PAY-015, each provider its filler (M-4). They aren't `own-service`, since no separate product of Zid's company does the instalments.
- **The two new things wait for Zid's other batches** and are decided with them before Zid's amendment: Search, the dashboard's own search, which the model holds nowhere (the storefront's search is CM-SFR-013); and Services, the section that groups Zid's own services, a container (rule 3).
- **The store conditions** ZD-1 took from the page index's `source.js` (`showNewZones`, `hasNewGifting`, `customerWallets`, `mustUseMarketsPricing`, `hasPos or subscription.is_trial`, not an NGO store) are the page index's listing conditions, in its source's identifiers. The route lines rightly carry none, since their own items state no guard. Both sets of lines stand as their sources state them.
