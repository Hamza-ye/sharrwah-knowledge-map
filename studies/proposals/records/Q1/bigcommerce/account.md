# Q1 on BigCommerce: places a store sells in or operates from

## [1]

- A channel is "anywhere a merchant sells". A merchant "creates a new channel to sell in a new context", selling from "a single catalog in one BigCommerce store". Q1-BC-010, Q1-BC-011, Q1-BC-K0209, Q1-BC-K0211
- Multi-Storefront (MSF) uses one "store" to power several "storefronts". Each storefront can have "its own unique domain, theme, categories, web pages, social media links, price lists, email templates, and more". The Help Center calls MSF a possible "multi-region or cross-border solution", while some functions "are global and are shared across storefronts". Q1-BC-001, Q1-BC-004, Q1-BC-021
- The catalog is shared across storefronts, and so is the orders area, where orders carry storefront attribution. Apps are installed at the store level, and an "MSF-compatible" app shares its settings across storefronts. Q1-BC-002, Q1-BC-003, Q1-BC-008, Q1-BC-009
- `store_address_type` and `store_country` are "inherently global". All other settings follow the global defaults unless a channel overrides them. Q1-BC-018, Q1-BC-017, Q1-BC-019
- The store's default currency is used for all auto-conversion, for analytics, and for fixed and flat-rate shipping costs. A display-only currency shows prices to shoppers "located in countries that use this currency". A transactional currency is also the currency the shopper is charged in. Q1-BC-043, Q1-BC-052, Q1-BC-050, Q1-BC-042, Q1-BC-K0395
- A currency can be the default for "visitors in these countries", and an IP address that matches a supported country selects it. Q1-BC-063, Q1-BC-057
- Tax zones set "the geographical area where a group of tax rates apply", and a Default Zone applies 0% everywhere else. Tax display can differ by country. An automatic tax provider applies only where an order's origin and destination are both in the selected regions. Q1-BC-128, Q1-BC-130, Q1-BC-132, Q1-BC-134, Q1-BC-047
- Shipping zones designate where a merchant ships and which methods apply "in each geographic region". A storefront's selected country "determines tax and shipping zone settings", a feature marked "still in development". Whether shipping zones are set per storefront is not in what was read. Q1-BC-K0371, Q1-BC-138, Q1-BC-026, Q1-BC-N03
- Personal data may be stored "in regions in which Commerce.com or its Subprocessors operate". Which region holds a store's data remains a gap. Q1-BC-K0438, Q1-BC-G0154

## [2]

- Settings work at the **global** level and as channel-specific **contextual overrides**. Q1-BC-015, Q1-BC-016
- A channel has a `name`, a `type` and a `platform`. A site belongs to one channel and holds its `url`. Q1-BC-012, Q1-BC-014, Q1-BC-K0221
- The Help Center lists what can be set per native storefront and per headless storefront. The lists include domains, themes, currencies, checkout settings, categories, price lists, promotions, customer groups, redirects, and "shipping methods and out of delivery zone messaging". All of it is available via the API. Q1-BC-005, Q1-BC-006, Q1-BC-007
- Per storefront, a merchant can localize the store profile and SEO fields, and "country, language, physical dimensions, date, and timezone". The domain is set in Channel Manager > Domains, and categories, web pages, promotions and emails can also differ. The global versions sit under Settings › Localization. Q1-BC-023, Q1-BC-024, Q1-BC-025, Q1-BC-027, Q1-BC-030, Q1-BC-032, Q1-BC-035, Q1-BC-036
- A storefront's default language drives the translations of the theme, checkout and order statuses. Locales are added per channel, up to 5 per storefront, from a platform list (`supportedLocales`). Locale-level product fields come with International Enhancements for MSF, which serve "Performance plan stores and Partner Sandboxes". Q1-BC-022, Q1-BC-037, Q1-BC-K0263, Q1-BC-K0264, Q1-BC-041, Q1-BC-033, Q1-BC-038, Q1-BC-039
- Channel-specific price lists set "different prices in the same currency per different storefronts". Price Lists are "limited to Performance plans". Q1-BC-034, Q1-BC-058
- A storefront's default currency is set with "Set as Channel default currency" in Channel Manager. Currencies are assigned to storefronts through "Manage channels". Q1-BC-068, Q1-BC-069, Q1-BC-056
- The tax address basis is one of billing address, destination address or shipping origin. Zones are based on country, state or postal code. Provider Targeting limits a tax provider to chosen countries and subdivisions, and only one automatic tax provider can be enabled at a time. Q1-BC-127, Q1-BC-129, Q1-BC-135, Q1-BC-136
- Who sets the Geography API's list of countries and states remains a gap. Q1-BC-K0405, Q1-BC-G0140

## [3]

- The contracting entity follows the merchant's country of residence, with separate entries for the United States, the United Kingdom, the European Union and Australia, and "Any other jurisdiction". Q1-BC-K0421, Q1-BC-K0422, Q1-BC-K0423, Q1-BC-K0424, Q1-BC-K0425
- The Jurisdiction-Specific Terms "supplement, replace or modify" the agreement for customers domiciled in the EU and UK, the EU, France, Germany and Sweden. Examples are dispute resolution, P2B mediation, EU Data Act termination and late payments. Q1-BC-142, Q1-BC-143, Q1-BC-144, Q1-BC-145, Q1-BC-146, Q1-BC-147, Q1-BC-148, Q1-BC-149, Q1-BC-K0427
- At store creation, "your default currency is assigned based on your location". Q1-BC-060
- Several payment services depend on the store's location. BigCommerce Payments needs a store "located in the United Kingdom or the United States". The PayPal Braintree rate needs "a United States-based business". PayPal is not supported for stores based in China. Q1-BC-P0068, Q1-BC-K0146, Q1-BC-125
- The UK pricing page states "Prices are in US Dollars". Q1-BC-141, Q1-BC-K0177
- Basic tax is offered where a location is "outside of our automatic tax providers’ supported areas". Q1-BC-133

## [4]

- A merchant adds a place to sell by creating a channel or storefront. Additional storefronts are priced by plan, and a new storefront gets a default language. The chapters on creating a storefront weren't read. Q1-BC-K0211, Q1-BC-K0217, Q1-BC-022, Q1-BC-N01
- For its own service, BigCommerce says "Additional regions and countries will be launching soon". What that involves isn't in what was read. Q1-BC-P0030, Q1-BC-P0047, Q1-BC-N04

## [5]

- A currency is added under Settings › Currencies, and only with the Manage Settings permission. Transactional currencies "can't be created via API". Q1-BC-062, Q1-BC-061, Q1-BC-K0394, Q1-BC-064, Q1-BC-065
- A transactional currency needs a Stencil theme, Optimized One-Page Checkout and a payment gateway that supports multicurrency. Some features don't support transactional currencies. Q1-BC-046, Q1-BC-048, Q1-BC-049, Q1-BC-070
- Each additional transactional currency needs its own payment methods. Display currencies use the default currency's payment methods. Q1-BC-053, Q1-BC-055, Q1-BC-054
- The Dev Center lists "Stripe Payment Gateway" as supported. The Help Center marks Multicurrency and "MSF Payments" support gateway by gateway, in table rows Q1-BC-078 to Q1-BC-122. Q1-BC-045, Q1-BC-076, Q1-BC-077
- A provider is applied for and underwritten, then added "under Store Setup, Payments". Each gateway's documentation gives its countries and currencies. Q1-BC-P0048, Q1-BC-074, Q1-BC-K0143
- Setting payment methods per storefront was not in what was read. Q1-BC-N02
