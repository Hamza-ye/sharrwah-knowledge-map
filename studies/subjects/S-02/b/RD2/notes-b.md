## RD2-1: shopify, bullets (e) and (g)

RD2-1 raised S02-VP-26 to S02-VP-29, one point per question of (e) (rule 3), and wrote S02-V-400 to S02-V-430, all of them shopify's. The later part, RD2-2, gives the rows of salla, zid, woocommerce and bigcommerce.

### Statements noted under (e)

- S02-SH-038 (e): a link to the Markets admin page ('[**Markets**](https://admin.shopify.com/markets)'); answers none of (e)'s questions
- S02-SH-039 (e): the admin's navigation label 'Markets'; answers none of (e)'s questions
- S02-SH-040 (e): the API reference's navigation label 'Shopify Markets'; answers none of (e)'s questions
- S02-SH-041 (e): the admin route's path 'markets'; answers none of (e)'s questions
- S02-SH-042 (e): the markets route's eligibility, the permissions to view it ('VIEW_MARKETS'); it gates viewing a page, and the statement doesn't say it gates creating, changing or removing a market
- S02-SH-043 (e): an app access scope to read markets ('customer_read_markets'); answers none of (e)'s questions
- S02-SH-044, S02-SH-045, S02-SH-046 (e): webhook topics for a market's creation, deletion and update ('Occurs when a new market is created'); they name no party that creates, changes or removes a market, and a hook alone names no party (rule 4)
- S02-SH-047 (e): the access scope's name 'read_markets'; answers none of (e)'s questions
- S02-SH-048 (e): the webhook topic's value 'markets/create', in the platform's code; a hook alone names no party (rule 4), so it names no party that creates a market
- S02-SH-049 (e): a captured request with the variables '"action": "create", "type": "market"'; its words, identifier and scope name no party that creates a market
- S02-SH-050, S02-SH-051, S02-SH-052, S02-SH-053, S02-SH-054 (e): the backup region, which S02-SH-190 says 'isn't a market': X fails the role test (S02-VP-26's note)
- S02-SH-067, S02-SH-190, S02-SH-192, S02-SH-283, S02-SH-455 (e): the backup region, which S02-SH-190 says 'isn't a market': X fails the role test (S02-VP-26's note)
- S02-SH-063 (e): how a customer is matched to a market ('automatically match customers to the right market'), market selection, a setting under (f); answers none of (e)'s questions
- S02-SH-079 (e): how a customer's market is determined ('it's determined which market they belong to'), market selection; answers none of (e)'s questions
- S02-SH-120 (e): how a customer's market is determined ('Markets for a customer are automatically determined'), market selection; answers none of (e)'s questions
- S02-SH-122 (e): automatic redirection ('You can choose whether you want to automatically or manually localize your customers'), market selection; answers none of (e)'s questions
- S02-SH-123 (e): the market a shipping address gives at checkout ('A customer's shipping address determines the final experience they receive'), market selection; answers none of (e)'s questions
- S02-SH-229 (e): deep links ('You can create a parameter that sends customers to the correct country or region'), market selection; answers none of (e)'s questions
- S02-SH-553 (e): the markets a company location matches ('determined by the markets that they match'), market selection; answers none of (e)'s questions
- S02-SH-563 (e): the market associated with an order ('determined by the shipping address of the customer'), market selection; answers none of (e)'s questions
- S02-SH-093 (e): the permissions a staff member needs 'To access the Markets page'; it gates access to a page, and the statement doesn't say it gates creating, changing or removing a market
- S02-SH-127 (e): 'Deleting a market is permanent. Deleted markets can't be recovered': names no party that changes or removes a market
- S02-SH-196 (e): a link to the General settings page; answers none of (e)'s questions
- S02-SH-235 (e): 'Countries and regions can be added to your shipping zones in your Shipping and delivery settings only when those countries and regions belong to a market': a limit on shipping zones (shipping, under (f)), not on a market
- S02-SH-284 (e): 'marketCreate Creates a Market': the schema's mutation names no party that calls it, and sets no value or default (rule 4); the rest names a market's settings, under (f)
- S02-SH-302 (e): the Markets page's tree ('Store default', 'Regions'); states no definer, limit or party for a market
- S02-SH-306 (e): a market without shipping rates ('there are no shipping rates for this market'): checkout and shipping in a market, under (f); states no definer, limit or party for a market
- S02-SH-307 (e): a market's 'Parent market' ('Store default') and its links to shipping and customer privacy, under (f); states no definer, limit or party for a market
- S02-SH-362 (e): the setup task 'Review shipping rates' ('Look over the defaults set up for you based on your location'): shipping defaults, under (f); states no definer, limit or party for a market
- S02-SH-366, S02-SH-375 (e): the checkout's 'Country/Region' options (the buyer's address and checkout, under (f)); they state no definer, limit or party for a market
- S02-SH-377 (e): the markets using a domain, when a language is assigned to it ('Markets using this domain'): domain and language, under (f); states no definer, limit or party for a market
- S02-SH-378 (e): the permission gate on the Managed Markets route ('MANAGE_PAYMENTS_SETTINGS', 'markets/managed'); it gates a page, and the statement doesn't say it gates creating, changing or removing a market
- S02-SH-379 (e): the permission gate on the route 'markets/managed/deactivate', which deactivates Managed Markets, a setting of a market (S02-SH-488: 'deactivate Managed Markets for that market'), under (f); not a gate on creating, changing or removing a market
- S02-SH-380 (e): the gate on the route 'markets/shipping-option/update', a market's shipping option (shipping, under (f)); not a gate on creating, changing or removing a market
- S02-SH-434 (e): 'You need permission to view this feature': a staff account without access to the Markets page; it gates viewing a page, and the statement doesn't say it gates creating, changing or removing a market
- S02-SH-488 (e): 'deactivate Managed Markets for that market': Managed Markets is a setting of the market, under (f); states no definer, limit or party for a market
- S02-SH-319, S02-SH-332, S02-SH-345 (e): the store's defaults and its backup region ('Determines settings for customers outside of your markets'); state no definer, limit or party for a market, and S02-SH-190 says the backup region 'isn't a market'
- S02-SH-398 (e): the General settings page's controls, a link to Markets and the select 'Backup Region' ('currency.backupRegion'); states no definer, limit or party for a market
- S02-SH-399, S02-SH-400, S02-SH-401, S02-SH-402, S02-SH-403, S02-SH-404 (e): the store's business entity, address and defaults, and its backup region; they state no definer, limit or party for a market

### Statements noted under (g)

None of shopify's statements under (g) says that the platform has no market of the kind in (e). Each says that a setting holds for the whole store, which is RD3's half: noted here (rule 4), and placed by RD3's parts.

- S02-SH-058 (g): 'Discounts and gift cards work across markets': a setting that holds for the whole store, RD3's half
- S02-SH-088 (g): 'Fixed amount discounts can be created only in your store's default currency': a setting that holds for the whole store, RD3's half
- S02-SH-089 (g): 'Staff permissions can't be assigned per market': a setting that holds for the whole store, RD3's half
- S02-SH-090 (g): 'Only one theme can be published at a time': a setting that holds for the whole store, RD3's half
- S02-SH-091 (g): 'Post-purchase apps work only in your store's default currency': a setting that holds for the whole store, RD3's half
- S02-SH-094 (g): 'customers in all markets pay in your store's default currency': a setting that holds for the whole store, RD3's half
- S02-SH-095 (g): 'On other plans, all markets share the same theme customization': a setting that holds for the whole store, RD3's half
- S02-SH-152 (g): 'You can add any product to a draft order regardless of market restrictions': a setting that holds for the whole store, RD3's half
- S02-SH-171 (g): 'Before you can assign a language to a market, the language must be added to your store': a setting that holds for the whole store, RD3's half
- S02-SH-186 (g): 'The following theme elements can't be customized for your markets on any plan': a setting that holds for the whole store, RD3's half
- S02-SH-187 (g): 'Homepage banners, announcement bars, and block content can't differ between markets on the Basic or Grow plans': a setting that holds for the whole store, RD3's half
- S02-SH-188 (g): 'By default, discount codes work across all markets': a setting that holds for the whole store, RD3's half
- S02-SH-189 (g): 'Gift cards are created and denominated in your store's default currency': a setting that holds for the whole store, RD3's half
- S02-SH-198 (g): 'A discount that applies to a customer segment or to specific customers applies to all markets': a setting that holds for the whole store, RD3's half
- S02-SH-227 (g): 'Because all markets use the same store URL, you can't customize which languages are available to each market': a setting that holds for the whole store, RD3's half
- S02-SH-231 (g): 'change your store's default language': a setting that holds for the whole store, RD3's half
- S02-SH-244 (g): 'Address validations at checkout ... apply to all regions': a setting that holds for the whole store, RD3's half
- S02-SH-246 (g): 'Store defaults: Manage your default currency, currency formatting, measurement and weight units, and time zone': settings that hold for the whole store, RD3's half
- S02-SH-272 (g): 'If you need to change your store currency after making your first sale, then contact Shopify Support': the store currency, a setting that holds for the whole store, RD3's half
- S02-SH-291 (g): 'The primary market must use the shop currency': the shop currency, a setting that holds for the whole store, RD3's half
- S02-SH-319, S02-SH-332, S02-SH-345 (g): the store's defaults ('Currency display To manage the currencies customers see, go to Markets'): settings that hold for the whole store, RD3's half
- S02-SH-398 (g): the store's defaults ('currency.unitSystem', 'currency.weightUnit', 'currency.timeZone'): settings that hold for the whole store, RD3's half
- S02-SH-399, S02-SH-400, S02-SH-401, S02-SH-402, S02-SH-403, S02-SH-404 (g): the store's defaults ('Currency display To manage the currencies customers see, go to Markets'): settings that hold for the whole store, RD3's half

### The brief's change on a platform's code (rule 4)

The coordinator's message during this run says the sentence on a platform's code applies to Shopify's shipped schema, under `who creates "market"` and `who changes or removes "market"`. Shopify's shipped statements under (e) were read again against it, and no row changed:

* placed under S02-VP-28 or S02-VP-29: S02-SH-278, whose words name the merchant ('A merchant-defined group of buyers'), the seller, in S02-V-425; S02-SH-288, whose words name the user and a permission ('The user doesn't have permission access to create or edit markets'), in S02-V-427 and S02-V-429; S02-SH-287, whose words say no one can ('Can’t delete, disable, or change the type of the last region market'), in S02-V-430; and the admin's controls S02-SH-386, S02-SH-387, S02-SH-391, S02-SH-392 and S02-SH-393, the seller's, in S02-V-425 and S02-V-428;
* noted: S02-SH-041, a route's path; S02-SH-042, a route's permissions to view it; S02-SH-048 and S02-SH-054, hooks, which alone name no party; S02-SH-283, the backup region's mutation; S02-SH-284, the mutation that creates a market, which names no party and sets no value or default; S02-SH-398, the General settings page's controls.

None of them sets a value or default for who creates, changes or removes a market. The suggested markets in S02-SH-387 are listed by the platform's code, but the seller creates each one, through its link (S02-V-425's note).

### New kinds

None: (e)'s points take no kind (rule 3).

### Searches for earlier platforms' rows

S02-VP-26, S02-VP-27, S02-VP-28 and S02-VP-29: no platform was placed under (e) before these points. RD2-1 is RD2's first part and shopify its first platform, so no search was made. Their rows for salla, zid, woocommerce and bigcommerce are RD2-2's.

### Rows `not covered`

None: shopify answers each of the four points.

### Problems with the method

- S02-VP-27, `what limits "market"`: bullet (e) asks how many markets a store can hold, while the question's form is wider. Its rows hold both: limits on the number (S02-V-411 to S02-V-414, S02-V-423 and the gap S02-V-424) and limits on what a market holds or when it can be active (S02-V-415 to S02-V-422). Rule 3 gives each question of (e) one point, so they share it.
- Permission gates. Rule 4 counts a permission that the statement says gates creating or changing a market. S02-SH-288 says so ('permission access to create or edit markets'), and is placed. S02-SH-042, S02-SH-093, S02-SH-378 and S02-SH-434 gate a page or route, and are noted. If access to the Markets page counts as gating creation, they belong in S02-V-427 and S02-V-429.
- S02-V-404 rests in part on a reading, marked in its basis_evidence: S02-SH-279's enum value 'LOCATION' is read as the retail (POS) location condition. The same API's Market object (S02-SH-278) names 'their region, retail location, or company location'.
- S02-V-407: the domestic market is defined by 'Your store's home country or region'. The point's X is the market, one of those the platform creates for the store to sell to (S02-SH-116), so it passes the role test. The variant names the store's own country as what defines it.
- S02-V-409 ('customer group', 'customer segments', from help pages) and the absent row S02-V-410 (S02-SH-N03: no condition type for a group of customers other than a company location) stand side by side, as their statements give them.

## RD2-2: salla, zid, woocommerce and bigcommerce, bullets (e) and (g)

RD2-2 places its platforms' statements under S02-VP-26 to S02-VP-29 and writes S02-V-431 onwards. It is RD2's last part.

### salla: statements noted under (e)

- S02-SA-001 (e): the label 'Market selection' ('"markets/browse_product_method":"Market selection"'); answers none of (e)'s questions
- S02-SA-002 (e): the label 'Markets' ('"markets":"Markets"'); answers none of (e)'s questions
- S02-SA-003 (e): the API docs' folder 'Store Scopes'; answers none of (e)'s questions
- S02-SA-007 (e): the API docs' folder 'Store Scopes'; answers none of (e)'s questions
- S02-SA-004 (e): the feature flag 'multi-market-origin-country-filter'; its words name a filter, and state no definer, limit or party for a market
- S02-SA-008 (e): 'This endpoint allows you to list store scopes for multi-country functionality.': an endpoint that lists store scopes; states no definer, limit or party for a market
- S02-SA-025 (e): each copy of the store 'تُدار بشكل مستقل' (my translation: is managed independently), with delivery from the branch nearest the customer: locations, under (f); names no party, and states no definer or limit for a market
- S02-SA-026 (e): the steps that activate the multiple markets feature ('اضغط (فعل الآن)', 'اضغط (تأكيد)'); the statement doesn't say they create, change or remove a market
- S02-SA-027 (e): the path to the multiple markets page; answers none of (e)'s questions
- S02-SA-028 (e): the multiple markets page's list of markets, with each market's information ('العملات', 'الفروع والمستودعات', 'الشحن', 'الدومين', 'تصميم المتجر'): a market's settings, under (f); states no definer, limit or party for a market
- S02-SA-029 (e): the tasks of managing multiple markets ('1- إضافة أسواق جديدة', '5- حذف السوق'); names no party that adds or deletes a market
- S02-SA-037 (e): the customer's country, shown in an order under the market's name; states no definer, limit or party for a market
- S02-SA-046 (e): searching the multiple markets page by a market's name or country ('يمكنك البحث باسم السوق أو دولته'); states no definer, limit or party for a market
- S02-SA-049 (e): languages per market ('ويمكنك تحديد اللغات لكل سوق إضافي بشكل مستقل'): language, under (f); states no definer, limit or party for a market
- S02-SA-054 (e): 'Contact your account manager to enable this feature.': who enables the feature; the statement doesn't say this creates a market
- S02-SA-055 (e): 'To disable it later, you'll need to contact your account manager.': who disables the feature; the statement doesn't say this changes or removes a market
- S02-SA-057 (e): 'Managing multiple branches/warehouses for my current market': locations, under (f); states no definer, limit or party for a market
- S02-SA-059 (e): 'Disabling can only be done by contacting the account manager': who disables the feature; the statement doesn't say this changes or removes a market
- S02-SA-065 (e): 'Run all your markets from one dashboard with independent settings for each market.': a market's settings, under (f); states no definer, limit or party for a market
- S02-SA-071 (e): 'Customers will be automatically redirected to their local market based on their IP address': market selection, under (f); answers none of (e)'s questions
- S02-SA-072 (e): 'Choose how customers select a market when visiting your store for the first time.': market selection, under (f); answers none of (e)'s questions
- S02-SA-073 (e): 'Set the market automatically using the customer’s IP address': market selection, under (f); answers none of (e)'s questions
- S02-SA-074 (e): 'Show customers a prompt to select their market before browsing the store.': market selection, under (f); answers none of (e)'s questions
- S02-SA-075 (e): 'Display a top bar where customers can switch markets.': market selection, under (f); answers none of (e)'s questions
- S02-SA-076 (e): 'Customers can only shop in the market that matches their country': market selection, under (f); answers none of (e)'s questions
- S02-SA-102 (e): redirection to a market's own domain ('ae.example.com'), an example: domain and market selection, under (f); answers none of (e)'s questions
- S02-SA-104 (e): restricting moves between markets ('يمنع التنقل'), an example with its reason: market selection, under (f); answers none of (e)'s questions
- S02-SA-106 (e): the customer selects the market to buy from ('يمكنه تحديد السوق الذي يرغب بالشراء منه'): market selection, under (f); answers none of (e)'s questions
- S02-SA-235 (e): the taxes page, for selling 'لأي دولة في العالم' (my translation: to any country in the world): taxes, under (f); states no definer, limit or party for a market
- S02-SA-250 (e): an endpoint that fetches 'the associated store scope details of a specific branch (scope)'; states no definer, limit or party for a market
- S02-SA-255 (e): the navigation item 'Multi Market', with '"permission": ["branches_management"]'; it gates a page, and the statement doesn't say it gates creating, changing or removing a market
- S02-SA-257 (e): the staff permission 'branches_management'; the statement doesn't say it gates creating, changing or removing a market
- S02-SA-278 (e): 'كل متجر يحدد الدول التي يشحن إليها' (my translation: each store sets the countries it ships to): shipping, under (f); states no definer, limit or party for a market
- S02-SA-286 (e): the label 'Country' ('"stores.country":"Country"'); answers none of (e)'s questions

### salla: statements noted under (g)

None of salla's statements under (g) says that the platform has no market of the kind in (e). Each says that a setting holds for the whole store, or for every market, which is RD3's half.

- S02-SA-064 (g): 'Your whole store is in maintenance mode, which overrides this market's settings.': store status, a setting that holds for the whole store, RD3's half
- S02-SA-156 (g): 'ولا يمكن تخصيص ذلك لسوق معينة' (my translation: and this can't be customized for a given market), on removing a product's category: a setting that holds for the whole store, RD3's half
- S02-SA-168 (g): 'يُطبَّق هذا الترتيب وأي تعديل عليه تلقائيًا على جميع الأسواق' (my translation: this order, and any change to it, applies automatically to all markets): a setting that holds for the whole store, RD3's half
- S02-SA-300 (g): '"Passing scope Id will make the products sort is per scope in this category, multi country feature needs to be enabled."': the products' order, a setting, RD3's half
- S02-SA-310 (g): 'it can be set as null or left blank to indicate that the tax rate is intended to apply to all countries': a tax rate for all countries, a setting that holds for the whole store, RD3's half
