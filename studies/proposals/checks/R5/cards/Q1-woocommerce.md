# Cards: Q1 on woocommerce

19 records cited by `studies/proposals/drafts/Q1/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 11:** - WooCommerce's reading showed no part of a store holding its own settings for some of its places: its "Selling location(s)" is one setting for the store. Q1-WC-N01, Q1-WC-K0536
- **section 1, line 14:** - Tax: on Salla "ستُفعَّل الضريبة حسب الدولة المحددة في السوق، ويشترط أن يكون لكل سوق دولة واحدة فقط"; BigCommerce and WooCommerce set rates by geography, in zones "based on country, state, or postal code" and, in WooCommerce's shipped code, by a rate's "2 digit country code". Q1-SA-023, Q1-BC-129, Q1-WC-024
- **section 1, line 17:** - What stays one for the whole store: on Shopify, "Staff permissions can't be assigned per market", while Salla can restrict a role "بحسب السوق المطلوب"; on BigCommerce, orders arrive in one area with "storefront attribution", and the store's address type and country are "inherently global" (not checked on Zid), as WooCommerce's store address, "the location where you are based as a seller", is one, a match on role (basis 4). Q1-SH-035, Q1-SA-028, Q1-BC-003, Q1-BC-018, Q1-WC-001
- **section 1, line 18:** - Placing a buyer, matching on role (basis 4): Shopify uses the IP address or "a market-specific domain, subdomain, or subfolder"; Salla's buyer picks the market; WooCommerce offers "Geolocate". Q1-SH-060, Q1-SH-061, Q1-SA-032, Q1-WC-005
- **section 1, line 19:** - Buyers outside the store's places, matching on role (basis 4): on Shopify they "can browse your store, but can't complete a purchase"; Salla's merchant can confine buying "على السوق المطابق لدولة العميل"; WooCommerce's shipped code has an optional zone for "any regions that have not been listed above". Q1-SH-018, Q1-SA-022, Q1-WC-027
- **section 1, line 27:** - Lists of places, matching on role (basis 4): in WooCommerce's shipped code, country codes and names "should follow the Unicode CLDR recommendation"; BigCommerce's Geography API gives "countries, states, and provinces". Q1-WC-K1382, Q1-BC-K0405
- **section 1, line 31:** - Who contracts with the seller follows the seller's place in three platforms' terms, matching on role (basis 4): Shopify contracts "based on the billing address of your Store"; BigCommerce's table runs by the merchant's country of residence down to "Any other jurisdiction"; WooCommerce names "WooCommerce Ireland Ltd." for residents of its "Designated Countries". Q1-SH-K1243, Q1-BC-K0425, Q1-WC-K0499
- **section 1, line 34:** - The platform's own payment product depends on where the seller is based, matching on role (basis 4), Shopify's in its payments terms and the others in help pages: Shopify Payments needs "a business located in your Designated Country"; Zid Pay is "متاح لتجار المملكة العربية السعودية و دولة الكويت"; WooPayments counts the country "where your business is registered — not the one in which you personally live"; BigCommerce Payments needs a store "located in the United Kingdom or the United States"; Salla pays UAE stores "كل يوم خميس" once their balance passes 250 dirhams. Q1-SH-K1536, Q1-ZD-K0005, Q1-WC-K0402, Q1-BC-P0068, Q1-SA-K1547
- **section 1, line 37:** - What is offered depends on the seller's place, matching on role (basis 4): where Shopify Payments "isn't available in your country", the seller chooses another provider; WooCommerce's code (shipped) keeps "The payment extension list for each country"; Salla's multiple markets feature "is currently available only in Saudi Arabia". Shopify's admin code (shipped) gates Shopify Balance on `"regions":["US"]`, and one Salla session's feature list (observed, 9 October 2026) gives `kyc_new_workflow` the list `"countries": ["AE", "SA", "KW", "QA", "OM", "BH"]`. Q1-SH-065, Q1-WC-K0054, Q1-SA-036, Q1-SH-K0041, Q1-SA-K1988
- **section 1, line 39:** - Yemen, as observed on Shopify: for capture-gb-plus on 5 October 2026, with a business entity address of `"countryCode":"YE"`, Shopify Payments was `"eligible":false` and Stripe `"available":false,"eligible":false`; fake-demo-sharrwah, with a Sanaa address, was listed third-party providers that day, Tap Payments and Cybersource among them; and ibx5bt-xy, billed at `"countryCodeV2":"YE"` (29 September 2026), had "Choose a provider" in its saved Payments step text of 30 September 2026. WooCommerce's code (shipped) suggests only `VISA` for store country YE. Q1-SH-094, Q1-SH-098, Q1-SH-095, Q1-SH-103, Q1-SH-092, Q1-SH-123, Q1-WC-K0333
- **section 1, line 43:** - A seller adds a place to sell to, matching on role (basis 4): on Shopify, a market with a Regions condition; on Salla, "+ سوق جديد"; on Zid, a market published or kept "كسوق مخفي"; on BigCommerce, a merchant "creates a new channel to sell in a new context"; on WooCommerce, a country added to the shipped setting "Selling location(s)". Q1-SH-031, Q1-SA-005, Q1-ZD-012, Q1-BC-K0211, Q1-WC-K0536
- **section 1, line 48:** - Shopify's payments terms let it "add a new Designated Country"; BigCommerce says "Additional regions and countries will be launching soon"; WooCommerce ranks "new countries and currencies" partly by store owners' requests. What adding a country involves on the platform's side was not in what was read for Shopify or BigCommerce. Q1-SH-K1604, Q1-BC-P0030, Q1-WC-K0403, Q1-SH-N02, Q1-BC-N04
- **section 1, line 52:** - Changing the store's currency, matching on role (basis 4): on Shopify, where it is "used within your Shopify admin for pricing products and running reports", a change after the first sale goes through Shopify Support, and a store currency dialog's markup in capture-advanced's saved step text (4 October 2026), with nothing to show it was open, lists "Testing payment processors not available in current currency" among reasons for a change; on Salla, "بشرط أن لا يكون هناك طلبات شراء للعملاء"; on Zid, prices are converted "بناءً على سعر الصرف في وقت التغيير"; on WooCommerce, "Your product prices keep the same numbers", and earlier orders keep their currency. Q1-SH-K1935, Q1-SH-K1936, Q1-SH-121, Q1-SA-093, Q1-ZD-K0302, Q1-WC-016
- **section 1, line 53:** - Adding a currency for buyers, matching on role (basis 4): on BigCommerce it takes "the Manage Settings permission"; on WooCommerce, "a multi-currency extension/plugin"; Shopify sets one per market, and with manual rates the conversion fee "is deducted from your payout". Q1-BC-061, Q1-WC-K0751, Q1-SH-058
- **section 1, line 54:** - Shown or charged, matching on role (basis 4): on BigCommerce, for a currency to be transactional "a payment gateway that supports the currency must be enabled", and each added transactional currency gets its own payment methods; on Shopify only Shopify Payments or Adyen "as the primary gateway can process payments in a customer's local currency"; Zid Pay charges in the store's العملة الأساسية, except through K-Net; WooCommerce's Currency Converter Widget "changes the display of prices only". Q1-BC-049, Q1-BC-053, Q1-SH-K1937, Q1-ZD-K0300, Q1-WC-018
- **section 1, line 55:** - Connecting a payment provider, matching on role (basis 4): on Shopify "Only the store owner can add a payment provider"; on Salla the seller copies credentials from their own gateway account (dashboard text, observed 8 October 2026), and for Tabby "Your settlement terms and merchant fees follow your agreement with Tabby"; on Zid the seller enters "مفاتيح الربط"; on BigCommerce, the seller applies to the provider and must "complete underwriting" first; on WooCommerce, gateways "can be added through traditional plugins". Q1-SH-064, Q1-SA-K1656, Q1-SA-089, Q1-ZD-K0094, Q1-BC-P0048, Q1-WC-K0006
- **section 1, line 57:** - Admitting a provider to the platform, matching on role (basis 4): Shopify's payments apps "must be approved by Shopify"; Zid's providers supply "a file for each country where the payment provider operates"; WooCommerce's vendor agreement, a stated source, requires "a separate agreement with Automattic and/or WooCommerce". Q1-SH-K1697, Q1-ZD-K0082, Q1-WC-K0353
- **section 2, line 61:** - **Place register**, proposed: Sharrwah's one list of places: every country and, under it, the areas a setting needs, such as a region, a governorate or a city, each with its parent and a code. Markets, delivery zones, tax rates, addresses and operating places name their places from it. Q1-WC-K1382, Q1-BC-K0405
- **section 2, line 62:** - It draws on WooCommerce's standard country list and BigCommerce's countries, states and provinces, with levels below country from Shopify's sub-region markets, Salla's markets for an "منطقة أو مدينة" and BigCommerce's tax zones. Why: places are data (rule 1) behind their own part (rule 2), with levels below country from the start, since adding them later changes every record naming a place (rule 3). Not taken: countries only, as in WooCommerce's selling locations, since Shopify and BigCommerce set delivery and tax below a country. Q1-WC-K1382, Q1-SH-022, Q1-SA-K1976, Q1-BC-129, Q1-WC-K0536
- **section 2, line 64:** - It takes the seller's place as the key, with a set-up for all other places, from Shopify's, BigCommerce's and WooCommerce's contracting parties; a per-country set of verification, payments, payouts and carriers from Salla's country articles; and an ordered provider list from WooCommerce's suggestions. Why: a new place is a new set-up, not new code (rule 1); terms per place change most, so this part hides them (rule 2); legal structure and partner contracts cost most to change, so the slots are fixed now and filled by company decisions (rule 3, section 7). Salla's and Zid's one set of terms is one value it can hold. Q1-WC-K0499, Q1-SA-076, Q1-WC-K0054, Q1-SA-094
- **section 2, line 66:** - **Seller entity**, proposed: the person or company that sells: its kind, its country of registration (for a person, of residence), its address, documents and bank account. Its country is the store's **home place**, which picks the operating place; the store's own address, in that country, serves tax and delivery. Q1-WC-K0402, Q1-WC-001, Q1-SH-117
- **section 2, line 67:** - It takes the country of registration from WooPayments; the entity apart from the store, used "for financial products, markets, apps, and taxes in this shop" (capture-gb-plus, observed 5 October 2026), with the store's address in its country (capture-advanced's saved step text, 4 October 2026), from Shopify; and the sign-up country from Salla. Sharrwah verifies it, and it changes only by a controlled change acting on new orders, as Shopify asks a seller to "promptly update your location", a market's entity change "affects only new orders", and Zid wants an empty wallet before a store changes country. Why: apart from the store, it lets one seller run several stores, and a market later use another entity, without changing stored records (rule 3). Q1-WC-K0402, Q1-SH-100, Q1-SH-117, Q1-SA-K1989, Q1-SH-K1271, Q1-SH-043, Q1-ZD-K0230
- **section 2, line 68:** - Not taken: the seller's country as a store setting alone, like Salla's store country, since BigCommerce's contract follows the merchant's country of residence and WooPayments the business's registration. Q1-SA-K1989, Q1-BC-K0425, Q1-WC-K0402
- **section 2, line 70:** - It takes the default from BigCommerce and Zid, the lock after orders from Shopify and Salla, and past orders kept from WooCommerce; converting prices at the day's rate, as Zid does, or keeping the numbers, as WooCommerce does, is the seller's choice. Q1-ZD-015, Q1-SH-K1936, Q1-SA-093, Q1-WC-016, Q1-ZD-K0302
- **section 2, line 74:** - **Market selection**, proposed: a buyer is placed by the market's web address, else by choice, else by location; the seller can confine checkout to the market's places, and chooses the **fallback** for a buyer in no market, browsing only or buying in the home market, since Shopify blocks such buying while Salla and WooCommerce make it optional. The rest is left to the build (rule 3). Q1-SH-061, Q1-SA-032, Q1-SH-018, Q1-SA-022, Q1-WC-027
- **section 2, line 78:** - It takes the offer by the seller's place from Shopify and WooCommerce, the seller's own credentials from Salla and Zid, the provider's underwriting from BigCommerce, methods per market from Shopify and Salla, and per currency from BigCommerce. Why: providers change, so they sit behind one interface (rule 2); and the seller contracts with the provider, which settles under that contract, as Salla's page on Tabby says, so no seller money is held through Sharrwah (rule 3, the guard). Q1-WC-K0054, Q1-ZD-K0094, Q1-SH-051, Q1-SA-033, Q1-SA-089
- **section 2, line 81:** - **Tax by place** and **delivery zone**, proposed and left to the build (rule 3): tax rates per place, as in BigCommerce's zones and WooCommerce's country codes; delivery zones as sets of places with methods, a market going live only where its places have one, since on Shopify no checkout runs without shipping rates, and one store's saved step text (capture-grow, 4 October 2026) says that to sell to a zone's countries, "include them in a market". Q1-BC-129, Q1-WC-024, Q1-SH-034, Q1-SH-108, Q1-SH-110
- **section 3, line 86:** - Plugs in: payment providers, through Sharrwah's payments interface after Sharrwah's approval and an agreement, as Shopify approves payments apps, Zid asks for a file per country and WooCommerce for a separate agreement. Q1-SH-K1697, Q1-ZD-K0082, Q1-WC-K0353
- **section 3, line 87:** - Plugs in: the rate source, as WooPayments' rates are "regularly retrieved from the WooPayments server" and Shopify's can be set by hand; and a location lookup, as WooCommerce's "Geolocate". Q1-WC-K0755, Q1-SH-058, Q1-WC-005
- **section 3, line 92:** - Set per buyer's place within a market: the tax rate, the delivery zone, and which local payment methods show, as on WooPayments only if "the customer billing country and the customer currency meet the requirements". Q1-WC-032
- **section 3, line 95:** - Set by Sharrwah: the place register, operating places, the provider catalogue and availability rules, as Shopify keeps its Designated Countries in its terms and WooCommerce its suggestions in code. Q1-SH-K1604, Q1-WC-K0054
- **section 5, line 118:** - Arrangements that hold sellers' money. Salla pays UAE stores every Thursday, Zid Pay serves merchants in Saudi Arabia and Kuwait, and WooPayments' signup "creates a Stripe Express account that is connected to the WooPayments service". Keep the provider interface able to carry a Sharrwah payment product or an account opened through Sharrwah, and each operating place's payout slot empty, until the founder decides under the guard, with a licence decision (section 7). Q1-SA-K1547, Q1-ZD-K0005, Q1-WC-K0371
- **section 5, line 122:** - The rate source. Where Salla's automatic prices take their rate was not in what was read (not checked on Zid); WooPayments takes its rates from its server, and Shopify's automatic rates carry a fee by the store's location. Keep the rate source its own part and each order's rate on the order; a company decision on a rate provider settles it, with section 6. Q1-SA-N02, Q1-WC-K0755, Q1-SH-057
- **section 7, line 140:** - Where Sharrwah's company is based, and which entity contracts with sellers in each operating place, under which law and terms. Q1-SH-K1243, Q1-BC-K0425, Q1-WC-K0499, Q1-SA-095
- **section 7, line 141:** - Whether Sharrwah offers a payment product of its own or opens payment accounts for sellers, and under which licence; the platforms' terms tie such products to a regulator, as Salla's transfers to "سلطة وصلاحيات البنك المركزي" and Shopify's Canadian payments entity to the Bank of Canada. Q1-SA-097, Q1-SH-K1614, Q1-WC-K0371, YA-102 (banks and licensed non-bank institutions @ the internationally recognized government's area, as of 2026-02)
- **section 7, line 142:** - Which payment providers Sharrwah works with in each place, and on what agreement. Q1-SH-K1550, Q1-ZD-K0082, Q1-WC-K0353
- **section 7, line 148:** - Which exchange-rate provider Sharrwah uses, if any. Q1-WC-K0755, Q1-SH-057

## The cards

### Q1-WC-K0536

**Cited at:** section 1, line 11; section 1, line 43; section 2, line 62

**Record** (`studies/proposals/records/Q1/woocommerce/copied.tsv`):
- concern_id: WC-C-030
- placement: decides
- structure: woocommerce-11.2.1:includes/admin/settings/class-wc-settings-general.php
- identifier: woocommerce_allowed_countries
- statement: 'title' => __( 'Selling location(s)', 'woocommerce' ), 'desc' => __( 'This option lets you limit which countries you are willing to sell to.', 'woocommerce' ), 'id' => 'woocommerce_allowed_countries', 'default' => 'all', 'type' => 'select',
- cite_ids: WC-S-5354

**Citation WC-S-5354:** `woocommerce-11.2.1:includes/admin/settings/class-wc-settings-general.php` | lines 194-198 | 2026-10-09 | kind: shipped | quote check: found
- quote: 'title' => __( 'Selling location(s)', 'woocommerce' ), 'desc' => __( 'This option lets you limit which countries you are willing to sell to.', 'woocommerce' ), 'id' => 'woocommerce_allowed_countries', 'default' => 'all', 'type' => 'select',
- in context: …code / ZIP', 'woocommerce' ), 'desc' => __( 'The postal code, if any, in which your business is located.', 'woocommerce' ), 'id' => 'woocommerce_store_postcode', 'css' => 'min-width:50px;', 'default' => '', 'type' => 'text', 'desc_tip' => true, ), array( 'type' => 'sectionend', 'id' => 'store_address', ), array( 'title' => __( 'General options', 'woocommerce' ), 'type' => 'title', 'desc' => '', 'id' => 'general_options', 'order' => 20, ), array( ⟪'title' => __( 'Selling location(s)', 'woocommerce' ), 'desc' => __( 'This option lets you limit which countries you are willing to sell to.', 'woocommerce' ), 'id' => 'woocommerce_allowed_countries', 'default' => 'all', 'type' => 'select',⟫ 'class' => 'wc-enhanced-select', 'css' => 'min-width: 350px;', 'desc_tip' => true, 'options' => array( 'all' => __( 'Sell to all countries', 'woocommerce' ), 'all_except' => __( 'Sell to all countries, except for...', 'woocommerce' ), 'specific' => __( 'Sell to specific countries', 'woocommerce' ), ), ), array( 'title' => __( 'Sell to all countries, except for...', 'woocommerce' ), 'desc' => '', 'id' => 'woocommerce_all_except_countries', 'css' …

### Q1-WC-024

**Cited at:** section 1, line 14; section 2, line 81

**Record** (`studies/proposals/records/Q1/woocommerce/statements.tsv`):
- stmt_id: Q1-WC-024
- bears_on: 1
- identifier: Tax rates: Country code
- statement: A 2 digit country code, e.g. US. Leave blank to apply to all.
- cite_ids: Q1-WC-C032
- from: held

**Citation Q1-WC-C032:** `woocommerce-11.2.1:includes/admin/settings/views/html-settings-tax.php` | line 32 | 2026-10-09 | kind: shipped | quote check: found
- quote: A 2 digit country code, e.g. US. Leave blank to apply to all.
- in context: … id="rates-pagination"></div> <h3> <?php /* translators: %s: tax rate */ printf( __( '"%s" tax rates', 'woocommerce' ), $current_class ? esc_html( $current_class ) : __( 'Standard', 'woocommerce' ) ); ?> </h3> <table class="wc_tax_rates wc_input_table widefat"> <thead> <tr> <th width="8%"><a href="https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes" target="_blank"><?php _e( 'Country code', 'woocommerce' ); ?></a> <?php echo wc_help_tip( __( '⟪A 2 digit country code, e.g. US. Leave blank to apply to all.⟫', 'woocommerce' ) ); ?></th> <th width="8%"><?php _e( 'State code', 'woocommerce' ); ?> <?php echo wc_help_tip( __( 'A 2 digit state code, e.g. AL. Leave blank to apply to all.', 'woocommerce' ) ); ?></th> <th><?php _e( 'Postcode / ZIP', 'woocommerce' ); ?> <?php echo wc_help_tip( __( 'Postcode for this rule. Semi-colon (;) separate multiple values. Leave blank to apply to all areas. Wildcards (*) and ranges for numeric postcodes (e.g. 12345...1…

### Q1-WC-001

**Cited at:** section 1, line 17; section 2, line 66

**Record** (`studies/proposals/records/Q1/woocommerce/statements.tsv`):
- stmt_id: Q1-WC-001
- bears_on: 1
- identifier: Store address
- statement: This is where you set your business’s physical address — the location where you are based as a seller. Many tax and shipping configurations use this address for determining rates.
- cite_ids: Q1-WC-C001
- from: held

**Citation Q1-WC-C001:** `https://woocommerce.com/document/configuring-woocommerce-settings/general/` | Store address | 2026-10-09 | kind: stated | quote check: found
- quote: This is where you set your business’s physical address — the location where you are based as a seller. Many tax and shipping configurations use this address for determining rates.
- title: General settings: documentation - WooCommerce
- in context: …ge, you can enter your business address, define the regions you will sell and ship orders to, enable tax calculations and coupons, and select the currency your shop will use for sales. To edit these settings, go to WooCommerce > Settings > General in your WordPress dashboard. The page has the following sections: Store address General options Taxes and coupons Currency options Below, you'll find explanations of the options for each. Store address ⟪This is where you set your business's physical address - the location where you are based as a seller. Many tax and shipping configurations use this address for determining rates.⟫ General options Selling location(s): Specify whether you'd like to sell to: All countries All countries, except for... Specific countries Shipping location(s): Choose to ship to only the countries you sell to or a subset of countries. You can also disable shipping and all shipping-related functionality. Default customer location: Choose how to determine a customer's default location. This is used help calculate default tax and shipping rates. Op…

### Q1-WC-005

**Cited at:** section 1, line 18; section 3, line 87

**Record** (`studies/proposals/records/Q1/woocommerce/statements.tsv`):
- stmt_id: Q1-WC-005
- bears_on: 1
- identifier: Default customer location: Options include
- statement: Shop country/region: This tells the system to assume customers are in the same location as your shop. No location by default: Taxes and shipping aren’t calculated until a customer enters their address. Geolocate: Uses MaxMind Geolocation to verify the customer’s current location and calculates taxes and shipping accordingly. Geolocate (with page caching support): The same as above, but using AJAX geolocation. When this option is selected, you may notice characters similar to ?v=xxxxx appended to your website URLs. This is normal and prevents static caching of prices.
- cite_ids: Q1-WC-C006;Q1-WC-C007;Q1-WC-C008
- from: held

**Citation Q1-WC-C006:** `https://woocommerce.com/document/configuring-woocommerce-settings/general/` | General options: Options include | 2026-10-09 | kind: stated | quote check: found
- quote: Shop country/region: This tells the system to assume customers are in the same location as your shop. No location by default: Taxes and shipping aren’t calculated until a customer enters their address.
- title: General settings: documentation - WooCommerce
- in context: …p Selling location(s): Specify whether you'd like to sell to: All countries All countries, except for... Specific countries Shipping location(s): Choose to ship to only the countries you sell to or a subset of countries. You can also disable shipping and all shipping-related functionality. Default customer location: Choose how to determine a customer's default location. This is used help calculate default tax and shipping rates. Options include: ⟪Shop country/region: This tells the system to assume customers are in the same location as your shop. No location by default: Taxes and shipping aren't calculated until a customer enters their address.⟫ Geolocate: Uses MaxMind Geolocation to verify the customer's current location and calculates taxes and shipping accordingly. Geolocate (with page caching support): The same as above, but using AJAX geolocation. When this option is selected, you may notice characters similar to ?v=xxxxx appended to your website URLs. This is normal and prevents static caching of prices. Taxes and coupons ↑ Back to top These settings enable taxes and coupons and c…

**Citation Q1-WC-C007:** `https://woocommerce.com/document/configuring-woocommerce-settings/general/` | General options: Options include | 2026-10-09 | kind: stated | quote check: found
- quote: Geolocate: Uses MaxMind Geolocation to verify the customer’s current location and calculates taxes and shipping accordingly.
- title, opening and note boxes: as for this source's citation above
- in context: …bset of countries. You can also disable shipping and all shipping-related functionality. Default customer location: Choose how to determine a customer's default location. This is used help calculate default tax and shipping rates. Options include: Shop country/region: This tells the system to assume customers are in the same location as your shop. No location by default: Taxes and shipping aren't calculated until a customer enters their address. ⟪Geolocate: Uses MaxMind Geolocation to verify the customer's current location and calculates taxes and shipping accordingly.⟫ Geolocate (with page caching support): The same as above, but using AJAX geolocation. When this option is selected, you may notice characters similar to ?v=xxxxx appended to your website URLs. This is normal and prevents static caching of prices. Taxes and coupons These settings enable taxes and coupons and control how WooCommerce calculates them. Enable taxes: Select Enable tax rates and calculations to calculate taxes during checkout and show …

**Citation Q1-WC-C008:** `https://woocommerce.com/document/configuring-woocommerce-settings/general/` | General options: Options include | 2026-10-09 | kind: stated | quote check: found
- quote: Geolocate (with page caching support): The same as above, but using AJAX geolocation.
- title, opening and note boxes: as for this source's citation above
- in context: …w to determine a customer's default location. This is used help calculate default tax and shipping rates. Options include: Shop country/region: This tells the system to assume customers are in the same location as your shop. No location by default: Taxes and shipping aren't calculated until a customer enters their address. Geolocate: Uses MaxMind Geolocation to verify the customer's current location and calculates taxes and shipping accordingly. ⟪Geolocate (with page caching support): The same as above, but using AJAX geolocation.⟫ When this option is selected, you may notice characters similar to ?v=xxxxx appended to your website URLs. This is normal and prevents static caching of prices. Taxes and coupons These settings enable taxes and coupons and control how WooCommerce calculates them. Enable taxes: Select Enable tax rates and calculations to calculate taxes during checkout and show the Tax settings page. Clear it to disable taxes and hide the Tax settings. Enable cou…

### Q1-WC-027

**Cited at:** section 1, line 19; section 2, line 74

**Record** (`studies/proposals/records/Q1/woocommerce/statements.tsv`):
- stmt_id: Q1-WC-027
- bears_on: 1
- identifier: Rest of the world
- statement: An optional zone you can use to set the shipping method(s) available to any regions that have not been listed above.
- cite_ids: Q1-WC-C035
- from: held

**Citation Q1-WC-C035:** `woocommerce-11.2.1:includes/admin/settings/views/html-admin-page-shipping-zones.php` | line 57 | 2026-10-09 | kind: shipped | quote check: found
- quote: An optional zone you can use to set the shipping method(s) available to any regions that have not been listed above.
- in context: … esc_html_e( 'Shipping method(s)', 'woocommerce' ); ?></th> <th></th> </tr> </thead> <tbody class="wc-shipping-zone-rows wc-shipping-tables-tbody"></tbody> <tfoot data-id="0" class="wc-shipping-zone-worldwide wc-shipping-zone-rows-tfoot"> <td width="1%" class="wc-shipping-zone-worldwide"></td> <td class="wc-shipping-zone-name"> <?php esc_html_e( 'Rest of the world', 'woocommerce' ); ?> </td> <td class="wc-shipping-zone-region"><?php esc_html_e( '⟪An optional zone you can use to set the shipping method(s) available to any regions that have not been listed above.⟫', 'woocommerce' ); ?></td> <td class="wc-shipping-zone-methods"> <ul> <?php $worldwide = new WC_Shipping_Zone( 0 ); $methods = $worldwide->get_shipping_methods(); uasort( $methods, 'wc_shipping_zone_method_order_uasort_comparison' ); if ( ! empty( $methods ) ) { foreach ( $methods as $method ) { $class_name = 'yes' === $method->enabled ? 'method_enabled' : 'method_disabled'; echo '<li class="wc-shipping-zone-method ' . esc_attr( $class_name ) . …

### Q1-WC-K1382

**Cited at:** section 1, line 27; section 2, line 61; section 2, line 62

**Record** (`studies/proposals/records/Q1/woocommerce/copied.tsv`):
- concern_id: WC-C-099
- placement: decides
- structure: woocommerce-11.2.1:i18n/countries.php
- identifier: i18n/countries.php
- statement: * Country codes and names should follow the Unicode CLDR recommendation (https://cldr.unicode.org/translation/displaynames/countryregion-territory-names).
- cite_ids: WC-S-5460

**Citation WC-S-5460:** `woocommerce-11.2.1:i18n/countries.php` | line 6 | 2026-10-09 | kind: shipped | quote check: found
- quote: * Country codes and names should follow the Unicode CLDR recommendation (https://cldr.unicode.org/translation/displaynames/countryregion-territory-names).
- in context: <?php /** * Countries * * Returns an array of countries and codes. ⟪* Country codes and names should follow the Unicode CLDR recommendation (https://cldr.unicode.org/translation/displaynames/countryregion-territory-names).⟫ * * See https://github.com/unicode-org/cldr/blob/master/common/subdivisions/en.xml * * @package WooCommerce\i18n * @version 3.8.0 */ defined( 'ABSPATH' ) || exit; return array( 'AF' => __( 'Afghanistan', 'woocommerce' ), 'AX' => __( 'Åland Islands', 'woocommerce' ), 'AL' => __( 'Albania', 'woocommerce' ), 'DZ' => __( 'Algeria', 'woocommerce' ), 'AS' => __( 'American Samoa', 'woocommerce' ), 'AD' => __( 'Andorra', 'woocommerce' ), 'AO' => __( 'An…

### Q1-WC-K0499

**Cited at:** section 1, line 31; section 2, line 64; section 7, line 140

**Record** (`studies/proposals/records/Q1/woocommerce/copied.tsv`):
- concern_id: WC-C-023
- placement: responsible
- structure: https://wordpress.com/tos/
- identifier: 1. Who's Who: Woo Services
- statement: If you reside in the Designated Countries: WooCommerce Ireland Ltd.
- scope: residents of the Designated Countries
- cite_ids: WC-S-0460

**Citation WC-S-0460:** `https://wordpress.com/tos/` | 1. Who's Who: Woo Services | 2026-10-06 | kind: official page | quote check: found
- quote: If you reside in the Designated Countries: WooCommerce Ireland Ltd.
- title: WordPress.com
- in context: …nated Countries: Automattic Inc. If you reside in the Designated Countries: Aut O'Mattic A8C Ireland Ltd. Woo Services Woo services include WooCommerce, WooPayments, WooCommerce Shipping, WooCommerce Tax, MailPoet, and other products or services available at WooCommerce.com. (Please note that for the use of Third-Party Services - as defined below - additional terms may govern). If you reside outside of the Designated Countries: WooCommerce, Inc. ⟪If you reside in the Designated Countries: WooCommerce Ireland Ltd.⟫ We refer to Automattic Inc., Aut O'Mattic A8C Ireland Ltd., WooCommerce, Inc., and WooCommerce Ireland Ltd. collectively as "Automattic," "us," or "we" throughout these Terms. 2. Your Use of Our Services and Your Account When using our Services requires an account, you agree to provide us with complete and accurate information and to keep the information current so that we can communicate with you about your account. We may need to send you emai…

### Q1-WC-K0402

**Cited at:** section 1, line 34; section 2, line 66; section 2, line 67; section 2, line 68

**Record** (`studies/proposals/records/Q1/woocommerce/copied.tsv`):
- concern_id: WC-C-010
- placement: decides
- structure: https://woocommerce.com/document/woopayments/compatibility/countries/
- identifier: Supported countries
- statement: NOTE: If you’re using WooPayments for a business, the relevant country is the one where your business is registered — not the one in which you personally live.
- cite_ids: WC-S-0512

**Citation WC-S-0512:** `https://woocommerce.com/document/woopayments/compatibility/countries/` | Supported countries | 2026-09-25 | kind: stated | quote check: found
- quote: NOTE: If you’re using WooPayments for a business, the relevant country is the one where your business is registered — not the one in which you personally live.
- title: WooPayments in Your Country Documentation - WooCommerce
- in context: … 🇦🇹 Austria 🇧🇪 Belgium 🇧🇬 Bulgaria 🇨🇦 Canada 🇭🇷 Croatia 🇨🇾 Cyprus 🇨🇿 Czech Republic 🇩🇰 Denmark 🇪🇪 Estonia 🇫🇮 Finland 🇫🇷 France 🇩🇪 Germany 🇬🇷 Greece 🇭🇰 Hong Kong 🇭🇺 Hungary 🇮🇪 Ireland 🇮🇹 Italy 🇯🇵 Japan 🇱🇻 Latvia 🇱🇹 Lithuania 🇱🇺 Luxembourg 🇲🇹 Malta 🇳🇱 Netherlands 🇳🇿 New Zealand 🇳🇴 Norway 🇵🇱 Poland 🇵🇹 Portugal 🇷🇴 Romania 🇸🇬 Singapore 🇸🇰 Slovakia 🇸🇮 Slovenia 🇪🇸 Spain 🇸🇪 Sweden 🇨🇭 Switzerland 🇦🇪 United Arab Emirates 🇬🇧 United Kingdom 🇺🇸 United States ⟪NOTE: If you're using WooPayments for a business, the relevant country is the one where your business is registered - not the one in which you personally live.⟫ For example, if you live in South Africa but your business is registered in the Sweden, you can use WooPayments for that business by selecting Sweden when signing up. Outlying territories of France ↑ Back to top A business must be located in Metropolitan France or within a French overseas region or territory that is within the European Economic Area to sign up with WooPayments as a French business. Businesses based in Martinique, Guadeloupe, Fre…

### Q1-WC-K0054

**Cited at:** section 1, line 37; section 2, line 64; section 2, line 78; section 3, line 95

**Record** (`studies/proposals/records/Q1/woocommerce/copied.tsv`):
- concern_id: WC-C-004
- placement: decides
- structure: woocommerce-11.2.1:src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php
- identifier: PaymentsExtensionSuggestions::$country_extensions
- statement: * The payment extension list for each country.
- cite_ids: WC-S-0618

**Citation WC-S-0618:** `woocommerce-11.2.1:src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php` | line 125 | 2026-10-09 | kind: shipped | quote check: found
- quote: * The payment extension list for each country.
- in context: …urther emphasized. /** * The memoized extensions base details to avoid computing them multiple times during a request. * * @var array|null */ private ?array $extensions_base_details_memo = null; /** * The memoized processed country extensions to avoid rebuilding the list multiple times during a request. * * Keyed by user, country code, and context. Cleared via clear_cache(). * * @var array */ private array $country_extensions_memo = array(); /** ⟪* The payment extension list for each country.⟫ * * The order is important as it will be used to determine the priority of the suggestions. * * Each entry is keyed by the two-letter country code and consists of a list of payment extensions. * Each payment extension can be identified by its ID (the shorthand version) or by an array with the following format: * array( * 'id' => 'woopayments', // This is required. * '_type' => 'provider', // Overrides the '_type' key. * // Special entry that ins…

### Q1-WC-K0333

**Cited at:** section 1, line 39

**Record** (`studies/proposals/records/Q1/woocommerce/copied.tsv`):
- concern_id: WC-C-004
- placement: decides
- structure: woocommerce-11.2.1:src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php
- identifier: $country_extensions['YE']
- statement: 'YE' => array( self::VISA => array( '_append' => array( 'tags' => array( self::TAG_PREFERRED ), ), ), ),
- scope: store country YE
- cite_ids: WC-S-5288

**Citation WC-S-5288:** `woocommerce-11.2.1:src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php` | lines 2826-2832 | 2026-10-09 | kind: shipped | quote check: found
- quote: 'YE' => array( self::VISA => array( '_append' => array( 'tags' => array( self::TAG_PREFERRED ), ), ), ),
- in context: … array( self::VISA => array( '_append' => array( 'tags' => array( self::TAG_PREFERRED ), ), ), ), 'AE' => array( self::WOOPAYMENTS, self::PAYPAL_FULL_STACK, self::STRIPE, self::MASTERCARD => array( '_remove' => array( 'tags' => array( self::TAG_PREFERRED ), ), ), self::PAYONEER, self::PAYMOB, self::VISA, self::NGENIUS, self::PAYPAL_WALLET, ), 'UZ' => array( self::VISA => array( '_append' => array( 'tags' => array( self::TAG_PREFERRED ), ), ), ), ⟪'YE' => array( self::VISA => array( '_append' => array( 'tags' => array( self::TAG_PREFERRED ), ), ), ),⟫ ); /** * The context to incentive type map. * * @var array|string[] */ private array $context_to_incentive_type_map = array( Payments::SUGGESTIONS_CONTEXT => 'wc_settings_payments', ); /** * The suggestion incentives provider. * * @var PaymentsExtensionSuggestionIncentives */ private PaymentsExtensionSuggestionIncentives $suggestion_incentives; /** * Initialize the class instance. * * @param PaymentsExtensionSuggestionIncentives $suggestion_ince…

### Q1-WC-K0403

**Cited at:** section 1, line 48

**Record** (`studies/proposals/records/Q1/woocommerce/copied.tsv`):
- concern_id: WC-C-010
- placement: decides
- structure: https://woocommerce.com/document/woopayments/compatibility/countries/
- identifier: Other countries
- statement: We prioritize new countries and currencies based on a number of factors, including the number of requests by WooCommerce store owners in that country.
- cite_ids: WC-S-0515

**Citation WC-S-0515:** `https://woocommerce.com/document/woopayments/compatibility/countries/` | Other countries | 2026-09-25 | kind: stated | quote check: found
- quote: We prioritize new countries and currencies based on a number of factors, including the number of requests by WooCommerce store owners in that country.
- title: WooPayments in Your Country Documentation - WooCommerce
- in context: …count is based in. Businesses in the United Arab Emirates (UAE) do not have access to the Individual account type. Engaging in any commercial activities typically requires a trade license or permit in the UAE. Therefore, only the Business account type is available for the UAE. Other countries ↑ Back to top In support of creating a global commerce platform, the WooCommerce team is actively working to make WooPayments available to other countries. ⟪We prioritize new countries and currencies based on a number of factors, including the number of requests by WooCommerce store owners in that country.⟫ If you want to use WooPayments, but it's not available in your country, please vote for your country to be supported on the WooPayments feature requests page. On this page Supported countries Outlying territories of France Outlying territories of the Netherlands Outlying territories of the UK Outlying territories of the U.S. Restrictions on account types Other countries 30-day money-back guarantee Support teams across the world Safe and secure o…

### Q1-WC-016

**Cited at:** section 1, line 52; section 2, line 70

**Record** (`studies/proposals/records/Q1/woocommerce/statements.tsv`):
- stmt_id: Q1-WC-016
- bears_on: 5
- identifier: Changing the base currency
- statement: Your product prices keep the same numbers. A product priced at 10 will show as 10 in the new currency, not a converted amount — update your prices yourself if you need to. Orders placed before the change keep the currency and symbol they were placed in, and their totals stay the same. Check that your payment gateway supports the new currency before you switch.
- cite_ids: Q1-WC-C020;Q1-WC-C021
- from: held

**Citation Q1-WC-C020:** `https://woocommerce.com/document/shop-currency/` | Changing the base currency | 2026-10-09 | kind: stated | quote check: found
- quote: Your product prices keep the same numbers. A product priced at 10 will show as 10 in the new currency, not a converted amount — update your prices yourself if you need to.
- title: Shop currency: documentation - WooCommerce
- in context: … a custom currency to your store. Scope of support: We are unable to provide support for customizations under our Support Policy. If you need to customize a snippet or extend its functionality, we recommend working with a Woo Agency Partner or a WooCommerce developer on Codeable. Changing the base currency ↑ Back to top Changing your base currency changes which currency your store displays and charges in. It does not convert any amounts for you. ⟪Your product prices keep the same numbers. A product priced at 10 will show as 10 in the new currency, not a converted amount - update your prices yourself if you need to.⟫ Orders placed before the change keep the currency and symbol they were placed in, and their totals stay the same. Check that your payment gateway supports the new currency before you switch. Multiple currencies ↑ Back to top WooCommerce only allows for one base currency per store. If you'd like to display products in different currencies (or allow customers to pay in a currency that differs from your shop's base currency), you will need to add a…

**Citation Q1-WC-C021:** `https://woocommerce.com/document/shop-currency/` | Changing the base currency | 2026-10-09 | kind: stated | quote check: found
- quote: Orders placed before the change keep the currency and symbol they were placed in, and their totals stay the same. Check that your payment gateway supports the new currency before you switch.
- title, opening and note boxes: as for this source's citation above
- in context: …nd its functionality, we recommend working with a Woo Agency Partner or a WooCommerce developer on Codeable. Changing the base currency ↑ Back to top Changing your base currency changes which currency your store displays and charges in. It does not convert any amounts for you. Your product prices keep the same numbers. A product priced at 10 will show as 10 in the new currency, not a converted amount - update your prices yourself if you need to. ⟪Orders placed before the change keep the currency and symbol they were placed in, and their totals stay the same. Check that your payment gateway supports the new currency before you switch.⟫ Multiple currencies ↑ Back to top WooCommerce only allows for one base currency per store. If you'd like to display products in different currencies (or allow customers to pay in a currency that differs from your shop's base currency), you will need to add a multi-currency extension/plugin. We urge you to evaluate the reasons for opting for a multi-currency setup to help choose the right extension(s) to help achieve your goals. Here are some opt…

### Q1-WC-K0751

**Cited at:** section 1, line 53

**Record** (`studies/proposals/records/Q1/woocommerce/copied.tsv`):
- concern_id: WC-C-053
- placement: where
- structure: https://woocommerce.com/document/shop-currency/
- identifier: Shop currency
- statement: If you’d like to display products in different currencies (or allow customers to pay in a currency that differs from your shop’s base currency), you will need to add a multi-currency extension/plugin.
- cite_ids: WC-S-0875

**Citation WC-S-0875:** `https://woocommerce.com/document/shop-currency/` | Shop currency | 2026-10-09 | kind: stated | quote check: found
- quote: If you’d like to display products in different currencies (or allow customers to pay in a currency that differs from your shop’s base currency), you will need to add a multi-currency extension/plugin.
- title: Shop currency: documentation - WooCommerce
- in context: … for you. Your product prices keep the same numbers. A product priced at 10 will show as 10 in the new currency, not a converted amount - update your prices yourself if you need to. Orders placed before the change keep the currency and symbol they were placed in, and their totals stay the same. Check that your payment gateway supports the new currency before you switch. Multiple currencies WooCommerce only allows for one base currency per store. ⟪If you'd like to display products in different currencies (or allow customers to pay in a currency that differs from your shop's base currency), you will need to add a multi-currency extension/plugin.⟫ We urge you to evaluate the reasons for opting for a multi-currency setup to help choose the right extension(s) to help achieve your goals. Here are some options for additional currencies: WooPayments gives you free access to multi-currency functionality, enabling customers to view and pay for products in their preferred currency. Currency Converter Widget changes the display of prices only. It will not change the currency you charge customers -…

### Q1-WC-018

**Cited at:** section 1, line 54

**Record** (`studies/proposals/records/Q1/woocommerce/statements.tsv`):
- stmt_id: Q1-WC-018
- bears_on: 5
- identifier: Multiple currencies: options for additional currencies
- statement: WooPayments gives you free access to multi-currency functionality, enabling customers to view and pay for products in their preferred currency. Currency Converter Widget changes the display of prices only. It will not change the currency you charge customers — your store’s base currency is still used. Using the Currency Converter Widget enables your store to run on a single currency, which simplifies store administration, accounting, and general maintenance; and helps customers to view your product catalog in their native currency. TIV Multi-Currency for WooCommerce allows customers to pay in the currency of their choice. MultilingualPress can display your content, products, and prices in multiple languages and currencies. Currency Switcher for WooCommerce adds a widget to your site that allows your customers to switch currencies.
- cite_ids: Q1-WC-C023;Q1-WC-C024;Q1-WC-C025;Q1-WC-C026
- from: held

**Citation Q1-WC-C023:** `https://woocommerce.com/document/shop-currency/` | Multiple currencies | 2026-10-09 | kind: stated | quote check: found
- quote: WooPayments gives you free access to multi-currency functionality, enabling customers to view and pay for products in their preferred currency.
- title: Shop currency: documentation - WooCommerce
- in context: …es WooCommerce only allows for one base currency per store. If you'd like to display products in different currencies (or allow customers to pay in a currency that differs from your shop's base currency), you will need to add a multi-currency extension/plugin. We urge you to evaluate the reasons for opting for a multi-currency setup to help choose the right extension(s) to help achieve your goals. Here are some options for additional currencies: ⟪WooPayments gives you free access to multi-currency functionality, enabling customers to view and pay for products in their preferred currency.⟫ Currency Converter Widget changes the display of prices only. It will not change the currency you charge customers - your store's base currency is still used. Using the Currency Converter Widget enables your store to run on a single currency, which simplifies store administration, accounting, and general maintenance; and helps customers to view your product catalog in their native currency. TIV Multi-Currency for WooCommerce allows customers to …

**Citation Q1-WC-C024:** `https://woocommerce.com/document/shop-currency/` | Multiple currencies | 2026-10-09 | kind: stated | quote check: found
- quote: Currency Converter Widget changes the display of prices only. It will not change the currency you charge customers — your store’s base currency is still used.
- title, opening and note boxes: as for this source's citation above
- in context: … in a currency that differs from your shop's base currency), you will need to add a multi-currency extension/plugin. We urge you to evaluate the reasons for opting for a multi-currency setup to help choose the right extension(s) to help achieve your goals. Here are some options for additional currencies: WooPayments gives you free access to multi-currency functionality, enabling customers to view and pay for products in their preferred currency. ⟪Currency Converter Widget changes the display of prices only. It will not change the currency you charge customers - your store's base currency is still used.⟫ Using the Currency Converter Widget enables your store to run on a single currency, which simplifies store administration, accounting, and general maintenance; and helps customers to view your product catalog in their native currency. TIV Multi-Currency for WooCommerce allows customers to pay in the currency of their choice. MultilingualPress can display your content, products, and prices in multiple languages and currencies. Currency Switcher f…

**Citation Q1-WC-C025:** `https://woocommerce.com/document/shop-currency/` | Multiple currencies | 2026-10-09 | kind: stated | quote check: found
- quote: TIV Multi-Currency for WooCommerce allows customers to pay in the currency of their choice. MultilingualPress can display your content, products, and prices in multiple languages and currencies.
- title, opening and note boxes: as for this source's citation above
- in context: … view and pay for products in their preferred currency. Currency Converter Widget changes the display of prices only. It will not change the currency you charge customers - your store's base currency is still used. Using the Currency Converter Widget enables your store to run on a single currency, which simplifies store administration, accounting, and general maintenance; and helps customers to view your product catalog in their native currency. ⟪TIV Multi-Currency for WooCommerce allows customers to pay in the currency of their choice. MultilingualPress can display your content, products, and prices in multiple languages and currencies.⟫ Currency Switcher for WooCommerce adds a widget to your site that allows your customers to switch currencies. Note: We are unable to help provide support for third-party extensions/plugins that are not created or maintained by Woo. Please contact the extension/plugin developer with any questions or support requests. Currency exchange rates and extra charges Always do due diligence regarding exchange rates (or any additional fees you may incur) b…

**Citation Q1-WC-C026:** `https://woocommerce.com/document/shop-currency/` | Multiple currencies | 2026-10-09 | kind: stated | quote check: found
- quote: Currency Switcher for WooCommerce adds a widget to your site that allows your customers to switch currencies.
- title, opening and note boxes: as for this source's citation above
- in context: …ency is still used. Using the Currency Converter Widget enables your store to run on a single currency, which simplifies store administration, accounting, and general maintenance; and helps customers to view your product catalog in their native currency. TIV Multi-Currency for WooCommerce allows customers to pay in the currency of their choice. MultilingualPress can display your content, products, and prices in multiple languages and currencies. ⟪Currency Switcher for WooCommerce adds a widget to your site that allows your customers to switch currencies.⟫ Note: We are unable to help provide support for third-party extensions/plugins that are not created or maintained by Woo. Please contact the extension/plugin developer with any questions or support requests. Currency exchange rates and extra charges Always do due diligence regarding exchange rates (or any additional fees you may incur) before selling to customers in currencies other than your store's base currency. Your customers' card issuers m…

### Q1-WC-K0006

**Cited at:** section 1, line 55

**Record** (`studies/proposals/records/Q1/woocommerce/copied.tsv`):
- concern_id: WC-C-001
- placement: where
- structure: https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/features/payments/payment-gateway-api.md
- identifier: WooCommerce Payment Gateway API
- statement: Payment gateways in WooCommerce are class based and can be added through traditional plugins.
- cite_ids: WC-S-0623

**Citation WC-S-0623:** `https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/features/payments/payment-gateway-api.md` | WooCommerce Payment Gateway API | 2026-10-10 | kind: stated | quote check: found
- quote: Payment gateways in WooCommerce are class based and can be added through traditional plugins.
- title: WooCommerce Payment Gateway API
- the page opens: Payment gateways in WooCommerce are class based and can be added through traditional plugins. This guide provides an intro to gateway development. Types of payment gateway Payment gateways come in several varieties: 1. Form based - This is where the user must click a button on a form that then redirects them to the payment processor on the gateway's own website. _Example_: PayPal standard, Authorize.net DPM 2. iFrame based - This is when the gateway payment system is loaded inside an iframe on y…
- headings: WooCommerce Payment Gateway API
- in context: --- post_title: WooCommerce Payment Gateway API sidebar_label: Payment Gateway API sidebar_position: 1 --- # WooCommerce Payment Gateway API ⟪Payment gateways in WooCommerce are class based and can be added through traditional plugins.⟫ This guide provides an intro to gateway development. ## Types of payment gateway Payment gateways come in several varieties: 1. **Form based** - This is where the user must click a button on a form that then redirects them to the payment processor on the gateway's own website. _Example_: PayPal standard, Authorize.net DPM 2. **iFrame based** - This is when the gateway payment system is loaded inside an iframe on your store. _Example_: SagePay Fo…

### Q1-WC-K0353

**Cited at:** section 1, line 57; section 3, line 86; section 7, line 142

**Record** (`studies/proposals/records/Q1/woocommerce/copied.tsv`):
- concern_id: WC-C-005
- placement: responsible
- structure: https://woocommerce.com/woo-vendor-agreement/
- identifier: 1.2.10
- statement: 1.2.10. ensure the Product is not a solution for processing or enabling payment transactions (“Payments Solution”). In order to make a Payments Solution available to Users of the Marketplace(s), Partner must enter into a separate agreement with Automattic and/or WooCommerce, as applicable.
- cite_ids: WC-S-0578

**Citation WC-S-0578:** `https://woocommerce.com/woo-vendor-agreement/` | 1.2.10 | 2023-06-02 | kind: stated | quote check: found
- quote: 1.2.10. ensure the Product is not a solution for processing or enabling payment transactions (“Payments Solution”). In order to make a Payments Solution available to Users of the Marketplace(s), Partner must enter into a separate agreement with Automattic and/or WooCommerce, as applicable.
- title: Marketplace Vendor Agreement - WooCommerce
- in context: …rting spam links, upselling services that do not involve the WordPress ecosystem, utilizing tracking about Users' usage of WordPress. 1.2.9. not collect any revenue based on the total value of payments completed using the Product or features available within the Product (also known as Total Payment Volume). Partner must enter into a separate agreement with Automattic and/or WooCommerce for any revenue collection related to Total Payments Volume. ⟪1.2.10. ensure the Product is not a solution for processing or enabling payment transactions ("Payments Solution"). In order to make a Payments Solution available to Users of the Marketplace(s), Partner must enter into a separate agreement with Automattic and/or WooCommerce, as applicable.⟫ 1.2.11. not collect any revenue based on the total amount of payments transacted using the Product. To collect any such revenue from the Product, Partner must enter into a separate agreement with Automattic and/or WooCommerce, as applicable. 1.2.12. abide by the following additional terms and conditions for Products on the Woo Marketplace: (a) Partner shall not create branded top level menus for Products listed on the Woo Marketplace. (b) The Pr…

### Q1-WC-K0755

**Cited at:** section 3, line 87; section 5, line 122; section 7, line 148

**Record** (`studies/proposals/records/Q1/woocommerce/copied.tsv`):
- concern_id: WC-C-053
- placement: boundary
- structure: https://woocommerce.com/document/woopayments/currencies/multi-currency-setup/
- identifier: Exchange rate
- statement: By default, exchange rates are regularly retrieved from the WooPayments server.
- scope: WooPayments
- cite_ids: WC-S-0543

**Citation WC-S-0543:** `https://woocommerce.com/document/woopayments/currencies/multi-currency-setup/` | Exchange rate | 2026-09-25 | kind: stated | quote check: found
- quote: By default, exchange rates are regularly retrieved from the WooPayments server.
- title: Multi-currency with WooPayments Documentation - WooCommerce
- in context: … Storefront theme active, you'll see a second option: Add a currency switcher to the Storefront theme. Enabling this setting will put a small currency switcher widget in the breadcrumbs section of Storefront, or any child theme of Storefront. Managing currencies ↑ Back to top You can manage individual currencies in the Enabled currencies list by clicking the Manage link next to the one you want to manage settings for. Exchange rate ↑ Back to top ⟪By default, exchange rates are regularly retrieved from the WooPayments server.⟫ The last update time shown under the Fetch rates automatically option. If needed, you can force WooPayments to pull fresh exchange rates by temporarily switching your WooCommerce store currency (under WooCommerce > Settings > General), and then switching it back to the original setting. NOTE: Exchange rates are not accurate to the minute and may differ slightly from historical exchange rate listings on third-party services. If you wish, you can …

### Q1-WC-032

**Cited at:** section 3, line 92

**Record** (`studies/proposals/records/Q1/woocommerce/statements.tsv`):
- stmt_id: Q1-WC-032
- bears_on: 1
- identifier: Country and currency requirements
- statement: Local payment methods will only show in checkout if the customer billing country and the customer currency meet the requirements shown below.
- scope: WooPayments
- cite_ids: Q1-WC-C040
- from: held

**Citation Q1-WC-C040:** `https://woocommerce.com/document/woopayments/payment-methods/local-payment-methods/` | Country and currency requirements | 2026-09-25 | kind: stated | quote check: found
- quote: Local payment methods will only show in checkout if the customer billing country and the customer currency meet the requirements shown below.
- title: Local payment methods Documentation - WooCommerce
- in context: …Political organizations 8651 Religious organizations 8661 Associations, memberships - not elsewhere classified (e.g. labor unions, condominium associations) 8699 Testing laboratories (non-medical) 8734 Collection of taxes and penalties (e.g. tax assessors' offices, customs bureaus) 9311 Government services - not elsewhere classified 9399 Government-owned lotteries (Norway, Poland, Sweden only) 9406 Country and currency requirements ↑ Back to top ⟪Local payment methods will only show in checkout if the customer billing country and the customer currency meet the requirements shown below.⟫ Payment Method Customer Billing Country Customer Currency Alipay No restrictions Varies, see below Bancontact Belgium EUR EPS Austria EUR GrabPay Singapore SGD iDEAL | Wero Netherlands EUR Multibanco Portugal EUR Przelewy24 (P24) Poland EUR or PLN SEPA Direct Debit Any SEPA country EUR WeChat Pay Varies, see below Varies, see below If these requirements are not met, the payment method will be hidden since the customer cannot use it anyway. Alipa…

### Q1-WC-K0371

**Cited at:** section 5, line 118; section 7, line 141

**Record** (`studies/proposals/records/Q1/woocommerce/copied.tsv`):
- concern_id: WC-C-006
- placement: boundary
- structure: https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/
- identifier: WooPayments built in partnership with Stripe
- statement: When you sign up for WooPayments, you verify your personal and business information with Stripe. This creates a Stripe Express account that is connected to the WooPayments service.
- cite_ids: WC-S-0504

**Citation WC-S-0504:** `https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/` | WooPayments built in partnership with Stripe | 2026-09-30 | kind: stated | quote check: found
- quote: When you sign up for WooPayments, you verify your personal and business information with Stripe. This creates a Stripe Express account that is connected to the WooPayments service.
- title: WooPayments built in partnership with Stripe Documentation - WooCommerce
- in context: …Expand Themes Expand WooPayments WooPay WooCommerce Shipping WooCommerce Tax Retired Products Expand Woo Marketplace Code Snippets Expand WooPayments / Documentation / WooPayments Documentation / WooPayments: Account Management / WooPayments built in partnership with Stripe WooPayments built in partnership with Stripe WooPayments is built in partnership with Stripe. This document provides more information and an overview of how we work together. ⟪When you sign up for WooPayments, you verify your personal and business information with Stripe. This creates a Stripe Express account that is connected to the WooPayments service.⟫ The Express account is what's used in the background for managing your business account information and activity with WooPayments. Who will provide support Our Happiness Engineers are here to help you set up and manage your store and usage of WooPayments. The support team will assist you with all payment processing issues and other operational questions, such as why one of your customer's payments failed, or why a payout has not been received. A…
