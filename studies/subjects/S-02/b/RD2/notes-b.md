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
- S02-SA-168 (g): 'هذا الترتيب وأي تعديل عليه تلقائيًا على جميع الأسواق' (my translation, of the unified order: this order, and any change to it, automatically on all markets): a setting that holds for the whole store, RD3's half
- S02-SA-300 (g): '"Passing scope Id will make the products sort is per scope in this category, multi country feature needs to be enabled."': the products' order, a setting, RD3's half
- S02-SA-310 (g): 'it can be set as null or left blank to indicate that the tax rate is intended to apply to all countries': a tax rate for all countries, a setting that holds for the whole store, RD3's half

### zid: statements noted under (e)

- S02-ZD-009 (e): the path to the markets feature ('الاعدادات > الأسواق'); answers none of (e)'s questions
- S02-ZD-024 (e): the theme's customization shown to the customer 'على حسب دولته' (my translation: according to their country): storefront design and market selection, under (f); answers none of (e)'s questions
- S02-ZD-026 (e): 'Retrieve a list of countries where the store operates.': X fails the role test: the statement doesn't call these countries markets or places the store sells into, and rule 1 counts the store's country of operation as its own country
- S02-ZD-027 (e): the API scope 'countries_cities.read'; answers none of (e)'s questions
- S02-ZD-028 (e): 'Retrieve a list of countries where the store operates.': X fails the role test, as for S02-ZD-026
- S02-ZD-029 (e): the country schema's codes ('Two-letter country code according to ISO 3166-1 alpha-2'); answers none of (e)'s questions
- S02-ZD-030 (e): 'The endpoint returns all countries' names, codes, and IDs': a list of all countries; answers none of (e)'s questions
- S02-ZD-031 (e): 'Retrieve a list of cities for a specific country where the store operates or delivers.': the statement doesn't call these cities markets; answers none of (e)'s questions
- S02-ZD-045 (e): 'عند تفعيل عملة دولة يتم تفعيل الشحن إليها' (my translation: when a country's currency is turned on, shipping to it is turned on): currency and shipping, under (f); states no definer, limit or party for a market
- S02-ZD-160 (e): a warehouse's sales channels, 'إما المتجر الإلكتروني أو زد كاشير' (my translation: either the online store or Zid Cashier): locations, under (f); states no definer, limit or party for a market

zid has no statement under (g) in RD2's slice.

### woocommerce: statements noted under (e)

woocommerce has no markets feature. Its selling locations, 'Selling location(s)', the countries the store sells to, pass the role test and are placed (S02-V-448 to S02-V-452). Its shipping locations and shipping zones are shipping, under (f): a shipping zone 'is a geographic region where a certain set of shipping methods and rates apply' (S02-WC-217), and the shipping locations are the countries the store ships to. They fail the role test, as RD2-1 held for shopify's shipping zones (S02-SH-235).

- S02-WC-016 (e): the settings tab's label 'General'; answers none of (e)'s questions
- S02-WC-019 (e): 'Choose which countries you want to ship to, or choose to ship to all locations you sell to.': the shipping locations, shipping under (f); X fails the role test
- S02-WC-020 (e): the filter 'woocommerce_countries_allowed_countries'; a filter alone names no party (rule 4), and it states no definer or limit for a market
- S02-WC-021 (e): the filter 'woocommerce_countries_shipping_countries', on the countries the store ships to: shipping, under (f); a filter alone names no party
- S02-WC-030 (e): 'Returns an array of countries and codes.': the list of all countries; answers none of (e)'s questions
- S02-WC-031 (e): 'Country codes and names should follow the Unicode CLDR recommendation'; answers none of (e)'s questions
- S02-WC-032 (e): the filter 'woocommerce_countries', on the list of all countries; answers none of (e)'s questions
- S02-WC-096 (e): the label 'Shipping zones'; answers none of (e)'s questions
- S02-WC-097 (e): 'The shipping zones API allows you to create, view, update, and delete individual shipping zones.': shipping zones, shipping under (f); X fails the role test
- S02-WC-098 (e): 'The shipping zone locations API allows you to view and batch update locations of a shipping zone.': shipping, under (f); X fails the role test
- S02-WC-124 (e): 'The WooCommerce countries class stores country/state data.'; answers none of (e)'s questions
- S02-WC-131 (e): 'Get countries that the store ships to.': shipping, under (f); X fails the role test
- S02-WC-132 (e): 'If shipping is disabled, return an empty array.': shipping, under (f); X fails the role test
- S02-WC-133 (e): 'Default to selling countries.', the default of the countries the store ships to: shipping, under (f); X fails the role test
- S02-WC-134 (e): the option 'woocommerce_specific_ship_to_countries': shipping, under (f); X fails the role test
- S02-WC-152 (e): the address locales of the allowed and shipping countries ('array_merge( $this->get_allowed_countries(), $this->get_shipping_countries() )'): the buyer's address, under (f); states no definer, limit or party for a market
- S02-WC-156 (e): a code comment on the address's country field, with its reason, and 'Merchants who sell to a single country should use "Sell to specific countries" instead.': the buyer's address, under (f); states no definer, limit or party for a market
- S02-WC-172 (e): 'Shipping location(s): Choose to ship to only the countries you sell to or a subset of countries.': shipping, under (f); X fails the role test
- S02-WC-181 (e): 'you can accept payments from customers anywhere in the world in over 100 supported currencies': WooPayments' payments; states no definer, limit or party for a market
- S02-WC-210 (e): the shipping zone's properties ('Shipping zone name', 'Shipping zone order'): shipping, under (f); X fails the role test
- S02-WC-211 (e): the shipping zone location's properties ('Options: postcode, state, country and continent. Default is country.'): shipping, under (f); X fails the role test
- S02-WC-216 (e): 'A shipping zone consists of the region(s) you'd like to ship to and the shipping method(s) offered.': shipping, under (f); X fails the role test
- S02-WC-217 (e): 'A shipping zone is a geographic region where a certain set of shipping methods and rates apply.': shipping, under (f); X fails the role test
- S02-WC-218 (e): the zone 'Rest of the world', 'An optional zone you can use to set the shipping method(s) available to any regions that have not been listed above.': shipping, under (f); X fails the role test
- S02-WC-219 (e): 'List the regions you\'d like to include in your shipping zone.': shipping, under (f); X fails the role test
- S02-WC-220 (e): a shipping zone that 'will not be matched because "%1$s" covers the same region earlier in the list': shipping, under (f); X fails the role test

### woocommerce: statements noted under (g)

None of woocommerce's statements under (g) says that the platform has no market of the kind in (e). Each says that a setting holds for the whole store, which is RD3's half.

- S02-WC-017 (g): 'select the currency your shop will use for sales': a setting that holds for the whole store, RD3's half
- S02-WC-025 (g): 'If you’d like to display products in different currencies' and 'you will need to add a multi-currency extension/plugin.': currency, a setting that holds for the whole store, RD3's half
- S02-WC-085 (g): 'WooCommerce only allows for one base currency per store.': a setting that holds for the whole store, RD3's half
- S02-WC-086 (g): 'This controls what currency prices are listed at in the catalog and which currency gateways will take payments in.': a setting that holds for the whole store, RD3's half
- S02-WC-087 (g): 'Each WooCommerce store can set one base currency.': a setting that holds for the whole store, RD3's half
- S02-WC-088 (g): 'Changing your base currency changes which currency your store displays and charges in.': a setting that holds for the whole store, RD3's half
- S02-WC-089 (g): the option 'woocommerce_currency', with ''default' => 'USD'': a setting that holds for the whole store, RD3's half
- S02-WC-175 (g): 'Currency: Sets your store’s default currency. Only one currency may be selected.': a setting that holds for the whole store, RD3's half
- S02-WC-176 (g): 'Currency position: Choose the default position of the currency symbol for prices': a setting that holds for the whole store, RD3's half
- S02-WC-177 (g): 'Thousand separator: Choose which symbol to use for the thousand separator': a setting that holds for the whole store, RD3's half
- S02-WC-178 (g): 'Decimal separator': a setting that holds for the whole store, RD3's half
- S02-WC-179 (g): 'Number of decimals': a setting that holds for the whole store, RD3's half
- S02-WC-207 (g): 'taxes are always calculated based on your store’s location, regardless of the customer’s address': a setting that holds for the whole store, RD3's half

### bigcommerce: statements noted under (e)

- S02-BC-001 (e): the API reference's section 'Create and manage sales channels, their sites, and their product listings.'; names no party that creates, changes or removes a channel
- S02-BC-017 (e): 'Group customers into segments to offer them promotions and other customized shopping experiences.': customer segments for promotions, discounts and offers under (f); the statement doesn't call a segment a channel, storefront or market
- S02-BC-055 (e): 'You can configure shipping zones in the control panel or use the API to designate where a merchant ships their products': shipping, under (f); X fails the role test
- S02-BC-158 (e): 'The default country in the drop-down menu is based on the customer’s IP address.': the buyer's address, under (f); answers none of (e)'s questions

### bigcommerce: statements noted under (g)

None of bigcommerce's statements under (g) says that the platform has no market of the kind in (e). Each says that a setting holds for the whole store, which is RD3's half.

- S02-BC-035 (g): 'They are suitable for any global information against the store that is not channel specific.': store metafields, data that holds for the whole store, RD3's half
- S02-BC-100 (g): 'the following settings are inherently global and cannot be modified with channel-specific overrides': settings that hold for the whole store, RD3's half
- S02-BC-142 (g): 'some store functions are global and are shared across storefronts, such as the built-in blog': functions that hold for the whole store, RD3's half
- S02-BC-147 (g): 'All apps are designed to work at a store level and are installed at the store level.': apps that hold for the whole store, RD3's half

### RD2-2: new kinds

None: (e)'s points take no kind (rule 3). The brand in S02-V-457 is none of the things that bullet (e) lists (problems, below).

### RD2-2: searches for earlier platforms' rows

RD2-2 raised no point. Each of its statements under (e) answers one of S02-VP-26 to S02-VP-29, or is noted, and none of its statements under (g) says that the platform has no market of the kind in (e). So no search for shopify's rows was made.

### RD2-2: rows `not covered`, `gap` and `absent`

No row is `not covered`. Every point has a row for every platform. The rows without an answer are:

- S02-V-442: zid, S02-VP-26, `gap` S02-ZD-G06 (what the default market holds), beside zid's answer rows;
- S02-V-447: zid, S02-VP-29, `gap` S02-ZD-G05 (who removes a market);
- S02-V-449: woocommerce, S02-VP-27, `gap` S02-WC-G04 (how many a store can hold);
- S02-V-459: bigcommerce, S02-VP-26, `absent` S02-BC-N01 (a country, region or other place among what defines a channel), beside bigcommerce's answer rows.

### RD2-2: matching (rule 5)

Each point's `raised_by` holds only shopify's statements, so RD2-2's rows were compared with them. Each takes `answers` alone:

- `term`: salla's 'السوق' (translation 'Market') is the same word as shopify's translation of 'market', 'السوق', but their definitions in `terms.tsv` differ: 'السوق هو الدولة أو المنطقة التي تستهدف البيع إليها' and 'A market is a set of customers that you define in your store.' So `term` fails. zid's 'الأسواق (خاصية الأسواق)' has no translation, and a definition other than shopify's. bigcommerce's 'channel' and shopify's 'Channel markets' are different terms, with different definitions. woocommerce has no term for a market.
- `identifiers`: no key, scope, topic, field or entitlement in RD2-2's statements is the same as one in the statements of `raised_by` (S02-SH-077, S02-SH-065, S02-SH-279; S02-SH-111, S02-SH-301, S02-SH-286; S02-SH-115, S02-SH-116, S02-SH-288; S02-SH-061, S02-SH-128).
- `definition`: no statement of RD2-2's gives the same definition as one of those.

### RD2-2: problems with the method

- Salla's feature 'multi-countries' (S02-V-436): its 'limit' of 10 and its 'count' are read as how many markets a store can hold and how many it holds. This is a reading, marked in the row's basis_evidence: the flag's words, 'multi-countries', don't say market. If the reading doesn't hold, S02-SA-187 and S02-SA-234 are to be noted under (e), and the row goes.
- Salla's store scopes: S02-SA-219 holds a store scope whose scope phase A gives as 'its one market after activating multiple markets', and S02-SA-251 is the store scope's schema. They are placed in S02-V-431 and S02-V-432 as a market's countries and cities. S02-SA-251's store scope is read as a market, a reading marked in S02-V-431.
- Enabling and disabling the multiple markets feature: S02-SA-054, S02-SA-055 and S02-SA-059 name the account manager, and S02-SA-026 the seller's controls. They are noted, since the statements don't say that enabling or disabling the feature creates, changes or removes a market. If enabling the feature counts as a gate on creating a market, they belong under S02-VP-28 and S02-VP-29, as RD2-1 said of shopify's page permissions.
- Zid's 'الاسواق المتوفرة' (S02-V-443): the sales channels app calls the selling platforms it reaches (Amazon, Trendyol, Jahez, Mazeed) markets. The row places them as markets defined by a channel. If the role test reads 'الاسواق' there as a homonym, S02-ZD-145 and S02-ZD-146 are to be noted instead, and the row goes.
- Zid's default market: S02-ZD-012 says that the default market appears automatically. It is placed under S02-VP-26 only: it doesn't say who creates the default market (S02-V-446's note).
- WooCommerce has no markets feature. Its selling locations ('Selling location(s)') are placed as its market, and its shipping locations and shipping zones are noted as shipping, under (f), as RD2-1 held for shopify's shipping zones. Phase A's gap S02-WC-G04 asks, under (e)'s how many, about shipping zones and currencies; it is the `gap` row S02-V-449 under S02-VP-27, though by this role test its things are not markets. WooCommerce's rows under S02-VP-28 and S02-VP-29 are for a setting that always exists: the platform's default 'all' (S02-V-451) and the seller (S02-V-450, S02-V-452). No statement says who removes it.
- BigCommerce: a channel is where a store sells (S02-BC-002), so its channels and storefronts are placed as its markets. The rows for a region, a group of customers and a brand (S02-V-455 to S02-V-457) rest on uses the platform suggests ('can help you', 'can be useful', 'may work for some merchants'), and stand beside the `absent` row S02-V-459 (S02-BC-N01). A brand (S02-V-457) is none of the things that bullet (e) lists: a country, region, city, group of customers, location, channel or storefront.
- BigCommerce's default channel (S02-V-466): 'provisioned with one channel out of the box' is read as 'by default', so the platform's (a reading, marked in the row).
- Scopes and permissions: bigcommerce's S02-BC-004, the API scope 'store_channel_settings' at 'modify', 'View and modify a list of channels', is placed under S02-VP-29 as a permission that gates changing channels (S02-V-467). RD2-1 noted shopify's read scopes, which gate no change, and its page permissions; salla's 'branches_management' (S02-SA-255, S02-SA-257) gates a page, and is noted the same way.
- Activation and publishing: salla's activating a market (S02-SA-044) is placed under S02-VP-29, as RD2-1 placed shopify's activating and deactivating (S02-V-428). Zid's creating a market hidden or published (S02-ZD-022) is placed under S02-VP-28, since its identifier puts it among the steps of creating a market.

## Second pass, RD2-S1: every task of RD2's work list, bullets (e) and (g), all five platforms

### Revisits

- S02-V-424 (shopify, S02-VP-27, was `gap` S02-SH-G03). Its leads: S02-SH-689, S02-SH-704 and S02-SH-706 ('unlimited number of country or region markets') joined S02-V-411; S02-SH-707 ('The number of markets that you can create depends on your subscription plan.') joined S02-V-412; S02-SH-689 ('Create B2B markets'), S02-SH-706 and S02-SH-707 ('you can create') joined S02-V-425, the seller, under S02-VP-28. Two answers no row held: S02-V-424 is replaced by 'you can assign up to 3 active catalogs across all your B2B markets' (S02-SH-703, S02-SH-704), and S02-V-470 is added, 'you can create an unlimited number of B2B market catalogs' (S02-SH-703, S02-SH-704), both rules on what B2B markets may hold. S02-SH-G03 was settled by gap-closing and goes; the gap `why` names, S02-SH-G07, stands beside them as S02-V-471.
- S02-V-449 (woocommerce, S02-VP-27, was `gap` S02-WC-G04). Its leads are about shipping zones, which RD2-2 held to be shipping, under (f), not a market; they are noted below. Gap-closing settled S02-WC-G04 and left no gap or absence for the point, so the row is now `not covered` (see "Rows `not covered`").

### Rereads (RD2-2, (e); rule 4 as widened on 27 October 2026)

All four are placed; their earlier notes stay.
- S02-SA-026: the seller's controls that switch the multiple markets feature on ('اضغط (فعل الآن)', 'اضغط (تأكيد)'), joined to the seller's rows S02-V-438 (S02-VP-28) and S02-V-439 (S02-VP-29).
- S02-SA-054: the account manager who enables the feature, a new row S02-V-472 under S02-VP-28, and in the new row S02-V-473 under S02-VP-29.
- S02-SA-055 and S02-SA-059: the account manager who disables it, in S02-V-473 under S02-VP-29.

### Statements noted under (e)

- S02-WC-269 (e): 'You can add as many shipping zones or shipping methods as you need to your shipping settings; there is no limit.': a limit on shipping zones, shipping under (f), not on a market; X fails the role test
- S02-WC-270 (e): 'A shipping zone is a geographical area to which you ship items.': shipping, under (f); X fails the role test
- S02-SA-382 (e): 'Each store decides which countries it ships to and which payment methods it accepts.': the countries a store ships to, shipping under (f), and payment methods; X fails the role test
- S02-SH-628 (e): 'Pre-approved expansion store types', such as 'International stores': an expansion store is a store of its own on a Shopify Plus organization's contract, not a market a store sells into; X fails the role test
- S02-SH-629 (e): 'Shopify Plus plan organizations can have a maximum of ten stores on their contract': a limit on an organization's stores, not on a store's markets; X fails the role test
- S02-SH-783 (e): 'you can restrict access so that only logged-in B2B customers can view your store': who may view the store, a setting under (f); answers none of (e)'s questions
- S02-SH-784 (e): 'restricting access might redirect D2C customers to authentication on some pages': a setting of the store's access, under (f); answers none of (e)'s questions
- S02-SH-927 (e): 'Shipping profiles and shipping rates are gradually moving to shipping options by market': shipping per market, under (f); answers none of (e)'s questions
- S02-SH-939 (e): the shipping zone's countries and regions, with 'Add more countries/regions in Markets': a shipping zone, shipping under (f), not a market; X fails the role test, as RD2-1 held for S02-SH-235

### Statements noted under (g)

- S02-SH-653 (g): 'the Customer information settings apply to every country and market that you sell to': a setting that holds for the whole store, RD3's half

### Shopify's other statements under (e), placed

S02-SH-603, S02-SH-604, S02-SH-606, S02-SH-607, S02-SH-609, S02-SH-611, S02-SH-920, S02-SH-924 and S02-SH-925 joined S02-VP-26's rows S02-V-400, S02-V-401, S02-V-403, S02-V-404 and S02-V-405; S02-SH-605 joined S02-V-420 and S02-SH-937 S02-V-412. New rows: under S02-VP-27, S02-V-474 (S02-SH-604, what a channel market may hold), S02-V-475 (S02-SH-924, locations on Shopify POS Lite) and S02-V-476 (S02-SH-925, retail and online customers within one region); under S02-VP-28 and S02-VP-29, S02-V-477 and S02-V-478, apps (S02-SH-606); under S02-VP-29, S02-V-479, the platform, which deactivates the markets past a new plan's limit (S02-SH-937). S02-SH-609 names market types by their use ('for cross-border selling, wholesale, retail, and selling across sales channels'): only its 'sales channels' names what defines one, so it is placed in S02-V-405 only.

### zid: statements noted under (e)

- S02-ZD-186 (e): 'The endpoint returns all countries' names, codes, and IDs, and is not specific to any particular store's operations': a list of every country, not a market; answers none of (e)'s questions
- S02-ZD-187 (e): 'The **Region & Language popup** allows customers to change the store language, country, and city': the buyer switches region, market selection under (f); answers none of (e)'s questions
- S02-ZD-190 (e): '`zid.store.region.countries`', 'Returns the list of store countries': a theme function's list of countries, which the statement doesn't say define a market; answers none of (e)'s questions
- S02-ZD-191 (e): '`zid.store.region.setRegion`', 'Changes the store language, country, and city': the buyer's region, market selection under (f); answers none of (e)'s questions
- S02-ZD-447 (e): 'نربطك مباشرة بأكبر الأسواق' (my translation: we connect you directly to the biggest markets): names markets without what defines one, a limit, or who creates, changes or removes one; answers none of (e)'s questions

### zid, bigcommerce and salla: statements noted under (g)

None of these says that the platform has no market of the kind in (e), RD2's half of (g) (rule 4). Each is noted with what it says: a setting that holds for the whole store is RD3's half; the rest are neither half.

- S02-ZD-231 (g): 'لا يمكن تفعيل أكثر من نطاق في نفس الوقت.' (my translation: more than one domain can't be activated at the same time): the domain, a setting that holds for the whole store, RD3's half
- S02-BC-176 (g): 'Other features, like tax, belong to the global store': taxes, a setting that holds for the whole store, RD3's half
- S02-BC-185 (g): 'Currently, you cannot have different warehouse locations and inventory service different storefront channels.': locations, a setting that holds for the whole store, RD3's half
- S02-BC-292 (g): 'settings like measurement units and factoring dimension are applied globally': units, a setting that holds for the whole store, RD3's half
- S02-SA-339 (g): the Terms of Use's definition of the consumer, '( المستهلك ) يقصَد بهذه العبارة كل مستهلك يقوم بشراء المنتج أو الخدمة من التاجر' (my translation: the consumer means every consumer who buys the product or service from the merchant): neither half
- S02-SA-340 (g): 'في حال قيام التاجر بالتسجيل كمؤسسة أو شركة' (my translation: where the merchant registers as an establishment or company): the merchant's legal capacity, in the Terms; neither half
- S02-SA-341 (g): 'لا تلتزم منصة سلة بإتمام عمليات بيع المنتجات أو الخدمات بين المستهلك والمتجر' (my translation: Salla doesn't undertake to complete sales between the consumer and the store): who sells, for every store; not RD2's half
- S02-SA-342 (g): 'إن جميع التعاملات التي تتم بين التاجر والمستهلك لا علاقة لها بشخص منصة سلة' (my translation: all dealings between the merchant and the consumer have no relation to Salla itself): who sells, for every store; not RD2's half
- S02-SA-343 (g): 'كافة المتاجر الإلكترونية المسجلة في منصة سلة تمتلك سجل تجاري الكتروني خاص بها' (my translation: every online store registered on Salla holds its own commercial register): who sells, for every store; not RD2's half
- S02-SA-344 (g): 'اتفاقية الاستخدام هذه سارية على كافة المستخدمين لمنصة سلّة' (my translation: these Terms of Use apply to all of Salla's users): the terms, for every user; neither half
- S02-SA-377 (g): 'المتجر الذي اشتريت منه هو من ينفّذ الاسترجاع ويصدر ردّ المبلغ' (my translation: the store you bought from carries out the return and issues the refund): returns, for every store; not RD2's half
- S02-SA-378 (g): 'تختلف تجربة الاسترجاع من متجر لآخر' (my translation: the return experience differs from store to store): returns, which differ by store; not RD2's half
- S02-SA-379 (g): 'As a shopper, you buy from the store itself, not from Salla.': who sells; not RD2's half
- S02-SA-380 (g): 'It owns the product, sets the price and the return policy, prepares and ships your order': who sells, and who sets prices and returns; not RD2's half
- S02-SA-381 (g): 'The seller is the store where you placed the order': who sells; not RD2's half
- S02-SA-386 (g): 'Allow customers to cancel orders before they're processed.': cancellations, a setting of the whole store, RD3's half
- S02-SA-394 (g): 'الطلبات بالعملات المختلفة بعد تحويلها إلى العملة الأساسية للمتجر' (my translation: orders in different currencies after converting them to the store's base currency): reports in the store's base currency, RD3's half
- S02-SA-395 (g): 'converted to the store currency': reports in the store's currency, RD3's half
- S02-SA-401 (g): 'تثبيت تطبيق Google Analytics واختيار حساب المتجر على Google Analytics' (my translation: install the Google Analytics app and choose the store's account on Google Analytics): an app linked for the store; not RD2's half
- S02-SA-402 (g): 'أدخل نطاق/دومين متجرك' (my translation: enter your store's domain), in linking Google Analytics: not RD2's half
- S02-SA-403 (g): 'اختر مصدر بيانات متجرك من القائمة المتاحة' (my translation: choose your store's data source from the list): an app's setting for the store; not RD2's half
- S02-SA-404 (g): 'ويمكنك إعادة الربط مع أي حساب آخر على Google Analytics في أي وقت تريد' (my translation: you can link again with any other Google Analytics account at any time): an app's link for the store; not RD2's half
- S02-SA-405 (g): 'create a Google Tag Manager account and container for your store URL': an app for the store; not RD2's half
- S02-SA-406 (g): 'Keep one container per store.': an app's container for the whole store; not RD2's half
- S02-SA-407 (g): 'The pixel, the Conversions API and your product catalog are all connected automatically when you link your account.': an app's link for the store; not RD2's half
- S02-SA-408 (g): 'Choose the pixel you want, then click (Continue).': a step in linking an app; not RD2's half
- S02-SA-416 (g): 'The Salla App Store is where you browse and install apps that add features to your store': apps for the store; not RD2's half
- S02-SA-417 (g): 'Turn all store notifications on or off.': messages, a setting that holds for the whole store, RD3's half
- S02-SA-418 (g): the notifications table's headers, 'Email' and 'App notifications': messages, RD3's half
- S02-SA-419 (g): the staff permission 'store_notification_settings_management': staff access to the store's notification settings, RD3's half
- S02-SA-420 (g): 'استقبل إشعارات مباشرة على جوالك أو جهازك اللوحي' (my translation: receive notifications directly on your phone or tablet): notifications to the merchant; not RD2's half
- S02-SA-431 (g): 'Saudi Arabia time is currently the only time zone available.': the time zone of booking products, RD3's half
- S02-SA-432 (g): 'Currently, booking times use Saudi Arabia time only.': the time zone of booking products, RD3's half
- S02-SA-433 (g): 'If enabled, Saudi Arabia (Riyadh) time will be used in the order prep list.': the time zone of the order prep list, RD3's half
- S02-SA-434 (g): the weight units, 'Gram', 'Kilogram', 'Pound' and 'Ounce': units, RD3's half
- S02-SA-435 (g): 'Product weight and weight unit': units, per product; not RD2's half
- S02-SA-436 (g): 'Default product weight for shipping': a default for the whole store, RD3's half

### bigcommerce: statements under (e)

Placed: S02-BC-162 in S02-V-453 and S02-V-462; S02-BC-163, S02-BC-164, S02-BC-172, S02-BC-174, S02-BC-177, S02-BC-180 and S02-BC-323 in S02-V-455, S02-BC-323 also in S02-V-456 and S02-V-457; S02-BC-172 and S02-BC-177 in S02-V-465, the merchant. New rows under S02-VP-27: S02-V-480, storefront seats or the plan (S02-BC-178); S02-V-481, a locale in one storefront only (S02-BC-179); S02-V-482, up to five languages a channel (S02-BC-286). Noted:

- S02-BC-173 (e): 'Each locale's subfolder is set in the control panel on your default channel.': a domain subpath for a language on one channel, domain and language under (f); answers none of (e)'s questions
- S02-BC-183 (e): 'The Carts API supports selling in different markets by allowing locale-based overrides for product details.': names markets without what defines one; its overrides are product details per locale, under (f); answers none of (e)'s questions
- S02-BC-204 (e): 'Fires when customer settings that affect the specified channel are updated': a webhook on a channel's settings, under (f); answers none of (e)'s questions

### woocommerce: statements noted under (g)

None of woocommerce's statements under (g) in this work list says that the platform has no market of the kind in (e), RD2's half of (g) (rule 4). Each is noted with what it says: a setting that holds for the whole store is RD3's half; the rest are neither half.

- S02-WC-266 (g): 'customers from all over the world can use the gateway to check out and pay': payment methods, for every buyer, RD3's half
- S02-WC-274 (g): 'you're solely responsible for all of your ecommerce activities': who sells, in the terms; not RD2's half
- S02-WC-275 (g): 'User is solely responsible for, and Stripe disclaims all liability for, the provision of goods and services sold to User's Customers': who sells, in a provider's terms; not RD2's half
- S02-WC-276 (g): 'must maintain fair and legally compliant return, refund, cancellation, and adjustment policies': returns, for every store; not RD2's half
- S02-WC-277 (g): 'are responsible for all products and services you provide, including delivery, support, refunds, returns': who sells; not RD2's half
- S02-WC-281 (g): 'WITHDRAWAL_WINDOW_IN_DAYS           = 14': returns, a value for the whole store, RD3's half
- S02-WC-282 (g): 'Enable the public order withdrawal feature for customer requests.': returns, a setting of the whole store, RD3's half
- S02-WC-283 (g): 'It’s up to you how withdrawal requests are handled': returns, RD3's half
- S02-WC-284 (g): 'The form accepts requests for orders of any age.': returns, RD3's half
- S02-WC-285 (g): 'We have created a sample draft Refund and Returns Policy page for you.': returns, a page of the whole store, RD3's half
- S02-WC-288 (g): '$default_weight_unit = $locale_info['US']['weight_unit'];': the units' default, RD3's half
- S02-WC-289 (g): 'This controls what unit you will define weights in.': units, a setting of the whole store, RD3's half
- S02-WC-290 (g): 'which determines the weight unit used throughout the store': units, a setting that holds for the whole store, RD3's half
- S02-WC-291 (g): 'This controls what unit you will define lengths in.': units, a setting of the whole store, RD3's half
- S02-WC-310 (g): the site's time zone, 'timezone_string': a setting of the whole site, RD3's half
- S02-WC-311 (g): 'The date the order was created, in the site's timezone.': the site's time zone, RD3's half
- S02-WC-312 (g): 'Set your store\'s address, visibility, currency, language, and timezone.': settings of the whole store, RD3's half
- S02-WC-315 (g): 'Choose the currency the store will display on products.': currency, RD3's half
- S02-WC-324 (g): 'Go to WP Admin > Settings > General and adjust the Site Language.': language, RD3's half
- S02-WC-325 (g): 'the shop displays in your locale if the language file exists': language, RD3's half
- S02-WC-329 (g): 'Allows customers to checkout without an account.': checkout and customer accounts, RD3's half
- S02-WC-330 (g): 'Account creation', 'After checkout (recommended)': checkout and customer accounts, RD3's half
- S02-WC-331 (g): 'Customers can create an account before placing their order.': checkout and customer accounts, RD3's half
- S02-WC-332 (g): 'Account creation', 'On "My account" page': customer accounts, RD3's half
- S02-WC-333 (g): 'Set options relating to customer accounts and data privacy.': customer accounts and privacy, RD3's half
- S02-WC-338 (g): 'Go to WooCommerce > Settings and select the Accounts and Privacy tab.': customer accounts and privacy, RD3's half
- S02-WC-339 (g): 'Use these settings to enable or disable guest checkout, control customer account creation': checkout and customer accounts, RD3's half
- S02-WC-340 (g): 'Allow customers to check out without creating an account.': checkout and customer accounts, RD3's half
- S02-WC-341 (g): 'Allow customers to create an account before placing their order.': customer accounts, RD3's half
- S02-WC-346 (g): 'This setting determines which shop pages products will be listed on.': products, RD3's half
- S02-WC-347 (g): the catalog visibility options 'Shop and search results', 'Shop only', 'Search results only' and 'Hidden': products, RD3's half
- S02-WC-348 (g): 'Hide out of stock items from the catalog': products, RD3's half
- S02-WC-361 (g): 'WooCommerce core offers fixed-cart, fixed-product, and percentage-based coupons.': discounts, RD3's half
- S02-WC-362 (g): 'You need an administrator or shop manager account to manage coupons.': discounts and staff access, RD3's half
- S02-WC-364 (g): 'WooCommerce core does not apply coupon codes automatically.': discounts, RD3's half
- S02-WC-366 (g): 'Enable the use of coupon codes': discounts, a setting of the whole store, RD3's half
- S02-WC-368 (g): 'Enable or disable coupons in your store.': discounts, RD3's half
- S02-WC-373 (g): the product's 'Sale price', labelled with 'get_woocommerce_currency_symbol()': prices in the store's one currency, RD3's half
- S02-WC-375 (g): 'select options that apply site-wide for Store Notice, Product Catalog, and Product Images': storefront design, RD3's half
- S02-WC-376 (g): 'Add a store wide alert/banner notice': storefront design, RD3's half
- S02-WC-377 (g): 'If enabled, this text will be shown site-wide.': storefront design, RD3's half
- S02-WC-379 (g): 'The Customize your store task opens a simplified design screen': storefront design, RD3's half
- S02-WC-386 (g): the option '"From" name', 'woocommerce_email_from_name': messages to buyers, RD3's half
- S02-WC-387 (g): the option '"From" address', 'woocommerce_email_from_address': messages to buyers, RD3's half
- S02-WC-395 (g): 'Enable stock management': stock, a setting of the whole store, RD3's half
- S02-WC-396 (g): 'Track stock quantity for this product': stock, a setting per product; not RD2's half
- S02-WC-401 (g): 'Enable this feature to track and credit channels and campaigns that contribute to orders on your site': a feature of the whole site, RD3's half
- S02-WC-404 (g): 'You can enable (or disable) this feature by going to WooCommerce > Settings > Advanced > Features > Order Attribution.': RD3's half
- S02-WC-408 (g): 'All data in your site’s Analytics menu will be converted into your store’s default currency.': reports in the default currency, RD3's half
- S02-WC-411 (g): 'check or uncheck the Enable tracking checkbox': data sharing, a setting of the whole store, RD3's half
- S02-WC-412 (g): 'You can configure GA4 in your store’s WP Admin dashboard': an extension's setting for the whole store, RD3's half
- S02-WC-418 (g): 'Leave this box unchecked if you do not want to pull suggested extensions from WooCommerce.com.': a setting of the admin; not RD2's half
- S02-WC-422 (g): 'One active subscription key can be used on one active (production) site': a WooCommerce.com subscription, the platform's own account; neither half
- S02-WC-423 (g): 'Set the locale to the store locale for customer emails to make sure emails are in the store language.': messages in the store's language, RD3's half
- S02-WC-425 (g): 'For each WooCommerce email listed, it’s possible to configure your settings (optional).': messages, RD3's half
- S02-WC-426 (g): 'use the “From” name and “From” address fields to set the sender identity customers see': messages, RD3's half
- S02-WC-428 (g): 'Let customers sign up to be notified when products in your store are restocked.': messages, RD3's half
- S02-WC-430 (g): 'Enter recipients (comma separated) that will receive this notification.': notifications to the store's own staff; not RD2's half
- S02-WC-431 (g): 'Enable low stock notifications': notifications to the store's own staff; not RD2's half
- S02-WC-432 (g): 'Enter comma-separated recipients for this email.': emails to shop managers and admins; not RD2's half
- S02-WC-440 (g): 'Enable WooCommerce Analytics to track your store\'s key metrics': reports, a feature of the whole store, RD3's half
- S02-WC-441 (g): 'This section controls the display of your website privacy policy.': privacy, RD3's half
- S02-WC-442 (g): 'Optionally add some text about your store privacy policy to show on account registration forms.': privacy, RD3's half
- S02-WC-443 (g): 'Optionally add some text about your store privacy policy to show during checkout.': privacy, RD3's half
- S02-WC-444 (g): 'Choose how long to retain personal data': privacy, RD3's half
- S02-WC-445 (g): 'This section lets you select a privacy policy page': privacy, RD3's half
- S02-WC-446 (g): 'Open Settings > Privacy, where you can select your privacy policy page.': privacy, RD3's half
- S02-WC-447 (g): 'Use this section to decide how long your store keeps order data.': privacy, RD3's half
- S02-WC-451 (g): 'Use these roles to control who can manage products, view reports, and configure store settings.': staff access, RD3's half
- S02-WC-452 (g): 'choose a role from the Role dropdown': staff access, RD3's half
- S02-WC-453 (g): 'WooCommerce adds several capabilities to the existing Administrator role.': staff access, RD3's half
- S02-WC-454 (g): 'Manage WooCommerce — Access to WooCommerce settings and configuration.': staff access, RD3's half
- S02-WC-455 (g): 'View WooCommerce reports — Access to all WooCommerce analytics and reports.': staff access, RD3's half
- S02-WC-456 (g): 'The Shop Manager role allows someone to manage your store without granting full Administrator access.': staff access, RD3's half
- S02-WC-457 (g): 'Manage WooCommerce — Full access to all WooCommerce settings and configuration.': staff access, RD3's half
- S02-WC-458 (g): 'View WooCommerce reports — Access to all WooCommerce analytics and reports.': staff access, RD3's half
- S02-WC-459 (g): 'Manage products — Create, edit, delete, and publish products': staff access, RD3's half
- S02-WC-460 (g): 'Manage orders — View, edit, and delete orders, as well as process refunds.': staff access, RD3's half
- S02-WC-461 (g): 'Manage customers — Shop Managers can view user details for all roles.': staff access, RD3's half
- S02-WC-462 (g): 'Shop Managers also have general WordPress editor capabilities': staff access, RD3's half
- S02-WC-463 (g): 'you can use an extension or plugin to adjust permissions without editing code': staff access, RD3's half
- S02-WC-464 (g): 'A WooCommerce extension that allows you to add, assign, and switch user roles within your store.': staff access, RD3's half
- S02-WC-465 (g): 'A WordPress plugin that provides a detailed interface for editing role capabilities.': staff access, RD3's half
- S02-WC-466 (g): 'A WordPress plugin for managing user roles, capabilities, and content permissions.': staff access, RD3's half
- S02-WC-467 (g): 'A WordPress plugin for managing group-based access control and permissions.': staff access, RD3's half
- S02-WC-468 (g): 'add_role( 'shop_manager', 'Shop manager',': staff access, RD3's half
- S02-WC-469 (g): '$wp_roles->add_cap( 'shop_manager', $cap );': staff access, RD3's half
- S02-WC-470 (g): 'these are assigned to admin/shop manager during installation or reset': staff access, RD3's half
- S02-WC-471 (g): '$capabilities['core'] = array( 'manage_woocommerce', 'create_customers', 'view_woocommerce_reports', );': staff access, RD3's half
- S02-WC-472 (g): '$capability_types = array( 'product', 'shop_order', 'shop_coupon' );': staff access, RD3's half
- S02-WC-473 (g): 'woocommerce_shop_manager_editable_roles': staff access, RD3's half
- S02-WC-474 (g): ''settings' => 'manage_woocommerce'': staff access, RD3's half
- S02-WC-475 (g): ''shipping_methods' => 'manage_woocommerce'': staff access, RD3's half
- S02-WC-476 (g): 'Coming soon mode controls who can visit your site while you prepare it for launch.': store status, a setting of the whole site, RD3's half
- S02-WC-477 (g): 'Go to WooCommerce > Settings > Site visibility to switch between Coming soon and Live.': store status, RD3's half
- S02-WC-478 (g): 'The badge reads Coming soon, Store coming soon, or Live based on your visibility settings.': store status, RD3's half
- S02-WC-479 (g): 'From this screen, choose Coming soon or Live.': store status, RD3's half
- S02-WC-480 (g): 'When Coming soon mode is enabled, your site is in a development state and not accessible to the public.': store status, RD3's half
- S02-WC-481 (g): 'Enabling this option ensures that only store-related pages are protected by Coming soon mode.': store status, RD3's half
- S02-WC-482 (g): 'Visitors will not be able to access store pages without permission': store status, RD3's half
- S02-WC-483 (g): 'the Coming soon landing page is displayed instead of the following WooCommerce store pages': store status, RD3's half
- S02-WC-484 (g): 'Cart (Assigned via WooCommerce > Settings > Advanced).': a store page under Coming soon mode, store status, RD3's half
- S02-WC-485 (g): 'Checkout (Assigned via WooCommerce > Settings > Advanced).': a store page under Coming soon mode, store status, RD3's half
- S02-WC-486 (g): 'Terms and conditions (Assigned via WooCommerce > Settings > Advanced).': a store page under Coming soon mode, store status, RD3's half
- S02-WC-487 (g): 'Shop (Assigned via WooCommerce > Settings > Products > General).': a store page under Coming soon mode, store status, RD3's half
- S02-WC-488 (g): 'Privacy policy (Assigned via Settings > Accounts & Privacy).': a store page under Coming soon mode, store status, RD3's half
- S02-WC-489 (g): 'A private link is generated for you to provide selective access to your site': store status, RD3's half
- S02-WC-490 (g): 'When live mode is enabled, your site is fully accessible to all visitors': store status, RD3's half
- S02-WC-491 (g): 'Stores that are already live will default to live mode': store status, RD3's half
- S02-WC-492 (g): 'Stores that install WooCommerce and complete the onboarding process will default to Coming soon mode.': store status, RD3's half
- S02-WC-493 (g): 'This is the default setting for new sites, determined by the fresh_site WordPress flag.': store status, RD3's half
- S02-WC-494 (g): 'If the first admin user registration date is less than a month ago.': store status, RD3's half
- S02-WC-495 (g): 'the Apply to store pages only toggle is enabled by default': store status, RD3's half
- S02-WC-496 (g): 'This guide provides examples for third-party developers and hosting providers on how to integrate their systems with WooCommerce's coming soon mode.': store status, RD3's half
- S02-WC-497 (g): 'WooCommerce's coming soon mode allows you to temporarily make your site invisible to the public while you work on it.': store status, RD3's half
- S02-WC-498 (g): 'The coming soon mode can be programmatically synced from a plugin or application.': store status, RD3's half
- S02-WC-499 (g): 'Integrating with a maintenance mode plugin.': store status, RD3's half
- S02-WC-500 (g): 'Integrating with a hosting provider's coming soon mode.': store status, RD3's half
- S02-WC-501 (g): 'enable or disable WooCommerce coming soon mode from another plugin by directly updating woocommerce_coming_soon option': store status, RD3's half
- S02-WC-502 (g): 'We could also programmatically bind the coming soon option from another plugin': store status, RD3's half
- S02-WC-503 (g): 'It is possible for developers to add custom exclusions that bypass the coming soon protection.': store status, RD3's half
- S02-WC-504 (g): 'you may want to add a custom page to the list of store pages which will be restricted by coming soon mode': store status, RD3's half
- S02-WC-505 (g): 'Use the Launch your store task when you’re ready to make your store public.': store status, RD3's half
- S02-WC-506 (g): 'From the site visibility settings, you’ll be able to enable Coming soon mode': store status, RD3's half
- S02-WC-507 (g): 'if ( current_user_can( 'manage_woocommerce' ) ) {': store status and staff access, RD3's half
- S02-WC-508 (g): 'apply_filters( 'woocommerce_coming_soon_exclude', false )': store status, RD3's half
- S02-WC-509 (g): ''woocommerce_coming_soon' => array( 'yes', 'no' )': store status, RD3's half

### woocommerce: statements noted under (e)

- S02-WC-359 (e): 'You can only select the countries that you’re targeting on Google Merchant Center. Your target countries must be eligible for both Google Merchant Center and Google Ads.': the countries the Google for WooCommerce extension targets with listings and ads on Google, which the statement doesn't say are a market the store sells into; X fails the role test (WooCommerce's market is its selling locations, as RD2-2 held)

### RD2-S1: rows `not covered`

- S02-V-449: woocommerce, S02-VP-27 (`what limits "market"`), was `gap` S02-WC-G04. Gap-closing settled the gap and left none for the point, and its leads (S02-WC-269, S02-WC-270) are about shipping zones, noted above. No statement, gap or absence of woocommerce answers the point, so the row goes back to woocommerce (rule 4).

### RD2-S1: matching (rule 5)

Each statement placed was compared with the point's `raised_by`. The rows joined are each platform's own, and keep their bases. The new rows of salla (S02-V-472, S02-V-473) and bigcommerce (S02-V-480 to S02-V-482) share no term, identifier or definition with the shopify statements in `raised_by` (S02-SH-111, S02-SH-301, S02-SH-286; S02-SH-115, S02-SH-116, S02-SH-288; S02-SH-061, S02-SH-128, S02-SH-288), so each takes `answers` alone, as do shopify's new rows.

### RD2-S1: new kinds, searches and candidates for a new point

- New kinds: none; (e)'s points take no kind (rule 3).
- Searches for earlier platforms' rows: none; the second pass raised no point.

### Candidates for a new point

None. Every statement of the work list that answers one of (e)'s questions does so for a market a store sells into, the one X of (e)'s points, and none of the (g) statements says that the platform has no market of the kind in (e).

### RD2-S1: problems with the method

- S02-V-449 is now `not covered`, after gap-closing. Phase A's gap S02-WC-G04 asked, under (e), how many shipping zones a store can hold; gap-closing answered it (S02-WC-269: 'there is no limit'), but under the role test, as RD2-2 held, a shipping zone is not a market, so the answer is noted. The row goes back to woocommerce, and A2 has run: the coordinator decides.
- Rule 4, as widened on 27 October 2026, makes the party that switches a feature on its own answer under both `who creates` and `who changes or removes`. S02-SA-054 ('Contact your account manager to enable this feature.') names no feature by name: that it is the multiple markets feature is a reading, marked in S02-V-472 and S02-V-473. S02-SA-059 is in the same list as S02-SA-058, which names the market. S02-SA-026, the seller's own controls, joined the seller's rows.
- S02-SH-703 and S02-SH-704 set limits on the catalogs B2B markets hold. They are placed under S02-VP-27 as rules on what a market may hold (S02-V-424, S02-V-470), as RD2-1 placed what a channel market may hold (S02-V-420). If such rules are read as (f)'s alone, the two rows go.
- S02-SH-604 ('Merchants can't configure web presence, domains, or discounts for channel markets.'), S02-SH-925 and S02-BC-286 ('Each channel can support up to five languages.') are rules on which settings a market may hold. They are placed under S02-VP-27 (S02-V-474, S02-V-476, S02-V-482), whose note holds both limits on how many and on what a market holds; they also bear on RD3's points.
- S02-SH-628 and S02-SH-629, Shopify Plus's expansion stores (including 'International stores' in another region or currency), are noted: an expansion store is a store of its own, not a market of a store.
- S02-WC-359, Google for WooCommerce's target countries, is noted. If a sales channel's target countries count as a market a store sells into, as zid's and bigcommerce's channels do (S02-V-443, S02-V-453), it answers S02-VP-27 for woocommerce, and S02-V-449 would take it in place of `not covered`.

## Second pass, RD2-S2: the last round's tasks of RD2's work list (after A2-T, A2-SH-H, A2-SA-H, A2-SA-S and A3-2), bullets (e) and (g); shopify, salla, woocommerce and bigcommerce

### Revisits

- S02-V-471 (shopify, S02-VP-27, was `gap` S02-SH-G07; RD2-S1 had revisited S02-V-424 into it). Its new lead S02-SH-1024 ('You’ve reached the limit of 100 markets using the “All” condition.', in the admin's code) gives an answer no row held, and replaces S02-V-471. S02-SH-1025 names two error codes: 'SHOP_REACHED_PLAN_MARKETS_LIMIT', a plan's markets limit, joined S02-V-412 ('The number of markets that you can create depends on your subscription plan.'); 'SHOP_REACHED_MARKETS_LIMIT', the same key as S02-SH-286's, joined S02-V-413 ('Can't have more than 50 markets.'), whose evidence now says the admin's code names it with no number. The leads RD2-S1 placed (S02-SH-689, S02-SH-703, S02-SH-704, S02-SH-706, S02-SH-707) stay in S02-V-411, S02-V-412, S02-V-424, S02-V-470 and S02-V-425. S02-SH-G12, which says it is 'in place of S02-SH-G07', stands beside the answers as the new row S02-V-483; S02-SH-G07 goes.
- S02-V-449 (woocommerce, S02-VP-27, was `not covered` after RD2-S1's revisit). Its leads S02-WC-513 ('Sell to all countries, except for&hellip;', 'woocommerce_all_except_countries') and S02-WC-514 ('Sell to specific countries', 'woocommerce_specific_allowed_countries') are the selling locations' two country lists: they say what defines the market, and joined S02-V-448 under S02-VP-26, which already held the two options (S02-WC-129, S02-WC-130). They name no party, so they join no row of S02-VP-28 or S02-VP-29. S02-WC-515 is noted below; S02-WC-269 and S02-WC-270 stay noted, as RD2-S1 noted them. The row is now `absent`, with S02-WC-N01 (kind shipped; A3-2 confirmed it): no settings page caps the countries a store sells to or sets when a selling location applies.

### Statements noted under (e)

- S02-WC-515 (e): 'if ( ! empty( $value['options'] ) ) { $countries = $value['options']; } else { $countries = WC()->countries->countries; }': the countries any 'multi_select_countries' field offers; its words, identifier ('output_fields(), case 'multi_select_countries': the countries a country list offers') and scope name no selling location, so X fails the role test. S02-WC-N01's own words read it with S02-WC-513 and S02-WC-514 (see "Problems")

### Statements placed (`place` tasks)

- S02-SA-440 (salla, (e)): the storefront's settings answer on the store aldakheel-test, whose 'scope' ('"type": "scope"'), named 'متجر السعودية', holds '"countries": ["SA"]'. Joined S02-V-431 under S02-VP-26 (a country defines a market), the scope read as a market as S02-V-431 reads S02-SA-251's store scope (a reading, marked there). Its null 'country_id' and 'city_id' name no city, so it doesn't join S02-V-432. It answers none of (e)'s other questions.
- S02-BC-358 (bigcommerce, (e)): 'Note that many third-party sales channels are apps, which can only be installed by the store owner or users with the Install applications permission.' Two new rows under S02-VP-28, each its own answer by rule 4, as S02-V-427 holds a permission for shopify: S02-V-484 'the store owner' and S02-V-485 'users with the Install applications permission'. That installing a sales channel's app creates the channel in the store is a reading, marked in both rows. 'third-party sales channels' is added to S02-VP-28's x_words for bigcommerce. It names no change or removal, so it isn't placed under S02-VP-29.

### Statements noted under (g)

Each is a statement under (g) on a setting of the store, which each platform's `a2.tsv` names for RD3's points (bigcommerce: S02-VP-92; salla: S02-VP-65, S02-VP-73, S02-VP-74, S02-VP-87 and S02-VP-89). None says that the platform has no market of the kind in (e), RD2's half of (g).
- S02-BC-352 (g): 'To install or update apps and leave reviews, you must be the store owner or have the Install applications permission enabled on your user account.': who may install a store's apps, RD3's half
- S02-BC-353 (g): 'To uninstall apps or cancel an app installation, you must have the Uninstall applications permission enabled.': who may uninstall a store's apps, RD3's half
- S02-BC-354 (g): 'To launch apps, you must be the store owner, have the Launch applications permission, or have been granted access to a multi-user Single Click App.': who may launch a store's apps, RD3's half
- S02-BC-355 (g): 'View a searchable list of your installed apps by going to Apps › My apps in the control panel.': the store's installed apps, managed in its control panel, RD3's half
- S02-BC-356 (g): 'Install applications Install apps from the App Marketplace.': a user permission over the store's apps, RD3's half
- S02-BC-357 (g): 'Uninstall applications Uninstall apps from the store.': a user permission over the store's apps, RD3's half
- S02-SA-437 (g): '"id":"order-cancellation-form","method":"PUT","action":"settings/fields/orders.cancel_order"': the order cancellation setting's form in the settings center, RD3's half
- S02-SA-438 (g): '"id":"all-notifications"', with '/notifications/v1/inbox/preferences/': the notifications section's field, RD3's half
- S02-SA-442 (g): 'storeData:{id:t.id,domain:t.domain,name:t.name,currency:t.currency,kycCountry:n}': the store's data the ads tools send to connect a pixel catalog, RD3's half
- S02-SA-443 (g): 'await rLe.post({endpoint:"ReturnPolicy",payload:{days:x}})': the return policy's days, set from the theme editor, RD3's half
- S02-SA-450 (g): '"action":"settings/fields/scopes.browse_product_method"': the markets section's setting of how products are browsed, RD3's half
- S02-SA-456 (g): '{"status":200,"success":true,"data":{"enabled":false,"hours":48}}': the order cancellation setting's saved value, RD3's half
- S02-SA-457 (g): 'ze="settings/fields/orders.cancel_order"': the order cancellation setting in the dashboard's code, RD3's half
- S02-SA-458 (g): 'fetch(Xt("/inbox/preferences/")': the signed-in user's notification preferences, read in the dashboard's code, RD3's half
- S02-SA-459 (g): '{"level":"global","enabled":true,"channels":{"in_app":true}}': the signed-in user's notification preferences, RD3's half
- S02-SA-460 (g): 'notifications#table.header.in_app' and 'notifications#table.header.email': the notification preferences table's columns, RD3's half

### RD2-S2: rows replaced or removed

- S02-V-471 (shopify, S02-VP-27): `gap` S02-SH-G07, replaced by the answer 'You’ve reached the limit of 100 markets using the “All” condition.' (S02-SH-1024); S02-SH-G12 stands beside it as S02-V-483.
- S02-V-449 (woocommerce, S02-VP-27): `not covered`, replaced by `absent` (S02-WC-N01).
- No row removed.

### RD2-S2: rows `not covered`

None. RD2-S1's one `not covered` row of RD2, S02-V-449, is now `absent`.

### RD2-S2: matching (rule 5)

S02-VP-27's `raised_by` (S02-SH-111, S02-SH-301, S02-SH-286) holds only shopify's statements, so shopify's rows take `answers`. S02-SH-1025 was compared with S02-SH-286, its own platform's, to join S02-V-413: they name the same key, 'SHOP_REACHED_MARKETS_LIMIT'; rechecked, the row keeps `answers`, since rule 5's bases compare with another platform's statement. S02-BC-358 shares no term, identifier or definition with S02-VP-28's `raised_by` (S02-SH-115, S02-SH-116, S02-SH-288), so S02-V-484 and S02-V-485 take `answers` alone. The rows joined (S02-V-412, S02-V-413, S02-V-431, S02-V-448) keep their bases.

### RD2-S2: new kinds and searches

- New kinds: none; (e)'s points take no kind (rule 3).
- Searches for earlier platforms' rows: none; the second pass raised no point.

### Candidates for a new point (RD2-S2)

None. The statements of these tasks that answer one of (e)'s questions do so for a market a store sells into (shopify's markets, woocommerce's selling locations, salla's scope, bigcommerce's sales channels), the one X of (e)'s points; S02-WC-515's X is any country list field, which fails the role test rather than raising another X. None of the (g) statements says that the platform has no market of the kind in (e).

### RD2-S2: problems with the method

- S02-WC-515 is noted, but bears on S02-VP-27. It fills any 'multi_select_countries' field with the field's options or else WooCommerce's countries; its own words, identifier and scope name no selling location. S02-WC-513 and S02-WC-514 give the selling locations' two lists that type ('type' => 'multi_select_countries'), and S02-WC-N01's words read the three together ('its two country lists (S02-WC-513, S02-WC-514) offer the countries WooCommerce lists (S02-WC-515)'). If a reading across two statements may pass the role test, S02-WC-515 answers S02-VP-27 for woocommerce as a rule on what a selling location may hold, as S02-V-417 ('Can't add unsupported country or region.') does for shopify, and it would stand beside the `absent` row, whose absence is of a cap and of a condition on when a selling location applies. The coordinator decides.
- S02-SH-1025's 'SHOP_REACHED_MARKETS_LIMIT' joined S02-V-413 by the same key as S02-SH-286, which the schema marks deprecated ('"isDeprecated":true', 'No longer used'). The admin's code names the key with no number. If the key in the admin's code is read as another limit than the schema's 50, S02-SH-1025 takes a row of its own for it, and stays in S02-V-412.
- S02-BC-358 says the store owner or users with the permission install a third-party sales channel's app. That this creates a channel, S02-VP-28's question, is a reading, marked in S02-V-484 and S02-V-485.
- `place` tasks have no `done` line: the brief's `done` records revisit, reread and note tasks, and `unplaced.tsv` checks the rest. The message's "Record each task with `done` as usual" was read that way.
