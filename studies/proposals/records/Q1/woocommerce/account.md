# Q1 on WooCommerce: a check against Shopify, Salla and BigCommerce

## [1]

- **differs** (role): "Selling location(s)" (`woocommerce_allowed_countries`) and "Shipping location(s)" (`woocommerce_ship_to_countries`) are store-wide: all countries, all except some, or specific countries. Against Shopify [1]: Q1-SH-060; Salla [1]: Q1-SA-019. Q1-WC-K0536, Q1-WC-K0537, Q1-WC-002, Q1-WC-003
- **differs** (role): the store address is "where you are based as a seller"; tax and shipping rates use it. Against BigCommerce [1]: Q1-BC-018. Q1-WC-001, Q1-WC-K0766, Q1-WC-K1060
- **differs** (role): "Default customer location" (shop country/region, none, or "Geolocate" with MaxMind) sets default tax and shipping rates. Against Shopify [1]: Q1-SH-060; Salla [1]: Q1-SA-032. Q1-WC-004, Q1-WC-005, Q1-WC-K0698, Q1-WC-K0701, Q1-WC-K0705
- **differs** (term): "A shipping zone is a geographic region where a certain set of shipping methods and rates apply." A shopper matches one zone by shipping address; "Rest of the world" covers the rest. Against BigCommerce [1]: Q1-BC-K0371; Salla [2]: Q1-SA-081. Q1-WC-025, Q1-WC-026, Q1-WC-027, Q1-WC-K1045, Q1-WC-K1073, Q1-WC-K1074
- **differs** (role): each tax rate takes "A 2 digit country code", blank for all. Against Salla [1]: Q1-SA-K1924; BigCommerce [1]: Q1-BC-128. Q1-WC-024, Q1-WC-K0758, Q1-WC-K0759, Q1-WC-K0760
- **differs** (role): WooCommerce Tax uses the store and customer addresses and does not determine "where your business has a tax obligation"; the merchant pays taxes and "customs charges, import taxes or duties"; customs fields "do not calculate duties". Against Shopify [1]: Q1-SH-K1865. Q1-WC-K0778, Q1-WC-K0781, Q1-WC-K0768, Q1-WC-K0800, Q1-WC-K0801, Q1-WC-K0802
- **differs** (role): WooPayments multi-currency lets customers pick from the merchant's currencies; "Automatically switch customers to their local currency" geolocates them. The customer currency, shown and charged, defaults to the store currency. Against Shopify [1]: Q1-SH-055; Salla [1]: Q1-SA-032; BigCommerce [1]: Q1-BC-063. Q1-WC-006, Q1-WC-010, Q1-WC-013, Q1-WC-K0752, Q1-WC-K0754
- **differs** (role): one base currency per store displays prices, records orders and is what gateways take; Analytics converts into it; the payout currency is separate. Against BigCommerce [1]: Q1-BC-043. Q1-WC-K0745, Q1-WC-K0746, Q1-WC-K0747, Q1-WC-012, Q1-WC-014, Q1-WC-K0737
- **differs** (term): local payment methods show only if the customer's billing country and currency meet requirements; BNPL needs the account country's billing country and currency, with no "cross-border/international transactions". Against Shopify [1]: Q1-SH-055; Shopify [5]: Q1-SH-047; Salla [1]: Q1-SA-019. Q1-WC-032, Q1-WC-028, Q1-WC-030, Q1-WC-K0364
- **goes beyond**: VAT on digital goods follows customer location; EU VAT Number can exempt businesses in the base country. Q1-WC-K1500, Q1-WC-K1496, Q1-WC-K1494
- **goes beyond**: the controlling Automattic company depends on service and the individual's location. Q1-WC-K0502, Q1-WC-K0504
- **not in what was read:** a part of a store holding settings for some places. Shopify [1]: Q1-SH-011, Q1-SH-017, Q1-SH-001, Q1-SH-035, Q1-SH-025; Shopify [2]: Q1-SH-008, Q1-SH-K0175; Salla [1]: Q1-SA-K1976, Q1-SA-004, Q1-SA-026, Q1-SA-064, Q1-SA-027; Salla [2]: Q1-SA-003; Salla [4]: Q1-SA-025, Q1-SA-102; BigCommerce [1]: Q1-BC-010, Q1-BC-001, Q1-BC-002; BigCommerce [2]: Q1-BC-015, Q1-BC-012, Q1-BC-005. Q1-WC-N01
- **not in what was read:** a seller's legal entity per place, taking its payments. Shopify [1]: Q1-SH-041; Shopify [2]: Q1-SH-043; Shopify [4]: Q1-SH-046. Q1-WC-N02
- **not in what was read:** a service selling abroad on the seller's behalf. Shopify [1]: Q1-SH-K1958; Shopify [4]: Q1-SH-074. Q1-WC-N03
- **not in what was read:** data location by region. Shopify [3]: Q1-SH-K2321; BigCommerce [1]: Q1-BC-K0438. Q1-WC-N04
- **not in what was read:** plan-dependent place settings. Shopify [1]: Q1-SH-037; Salla [1]: Q1-SA-104; Salla [5]: Q1-SA-K1640. Q1-WC-N09
- **not in what was read:** store on/off settings naming places. Shopify [1]: Q1-SH-088; Shopify [3]: Q1-SH-090. Q1-WC-N10

## [2]

- **differs** (role): General settings holds the address, regions, taxes and currency for the whole store; the currency needs "access to WooCommerce settings". Against Shopify [2]: Q1-SH-010; Salla [2]: Q1-SA-004; BigCommerce [2]: Q1-BC-023. Q1-WC-K0535, Q1-WC-K0533, Q1-WC-015
- **differs** (role): `woocommerce_tax_based_on`: customer shipping, customer billing or shop base address. Against BigCommerce [2]: Q1-BC-127. Q1-WC-022, Q1-WC-023
- **differs** (role): countries come from `i18n/countries.php`, following "the Unicode CLDR recommendation", through the `woocommerce_countries` filter and route `data-countries`. Against BigCommerce [2]: Q1-BC-K0405. Q1-WC-K1381, Q1-WC-K1382, Q1-WC-K1388, Q1-WC-K1385
- **not in what was read:** per-place prices. BigCommerce [2]: Q1-BC-034. Q1-WC-N05
- **not in what was read:** per-place language, address or currency. Shopify [2]: Q1-SH-062; BigCommerce [2]: Q1-BC-022, Q1-BC-068. Q1-WC-N06

## [3]

- **differs** (role): residents of the "Designated Countries" contract with WooCommerce Ireland Ltd., others with WooCommerce, Inc. Against Shopify [3]: Q1-SH-K1243; BigCommerce [3]: Q1-BC-K0421; Salla [3]: Q1-SA-094. Q1-WC-K0496, Q1-WC-K0498, Q1-WC-K0499
- **differs** (role): California law and San Francisco courts, with consumers' mandatory local provisions kept. Against BigCommerce [3]: Q1-BC-142; Salla [3]: Q1-SA-094. Q1-WC-K0516, Q1-WC-K0517, Q1-WC-K0514
- **differs** (role): WooPayments serves listed countries, a business counting where it "is registered"; some outlying territories are excluded; the UAE has only the Business account type. Against Shopify [3]: Q1-SH-K1535, Q1-SH-K1271, Q1-SH-042; Salla [3]: Q1-SA-075, Q1-SA-099; BigCommerce [3]: Q1-BC-P0068. Q1-WC-K0400, Q1-WC-K0406, Q1-WC-K0402, Q1-WC-K0407, Q1-WC-K0408, Q1-WC-K0409, Q1-WC-K0411, Q1-WC-K0404
- **differs** (role): WooPayments signup binds the seller to Stripe's Connected Account Agreement; the "Stripe Account Country" sets the agreement version and the Stripe entity (UAE: Stripe Payments Europe, Limited; United States: Stripe, LLC). Against Shopify [3]: Q1-SH-K1535. Q1-WC-K0371, Q1-WC-033, Q1-WC-034, Q1-WC-035, Q1-WC-036, Q1-WC-037
- **differs** (role): suggested payment extensions are listed per store country, in priority order (SA: `MASTERCARD`, `PAYMOB`, `PAYPAL_FULL_STACK`, `VISA`, `NGENIUS`, `PAYPAL_WALLET`; YE: `VISA`). Against Shopify [3]: Q1-SH-065. Q1-WC-K0054, Q1-WC-K0055, Q1-WC-K0059, Q1-WC-K0327, Q1-WC-K0331, Q1-WC-K0333
- **differs** (role): WooPayments fees vary with the business's and customer's countries, currency and method. Against Shopify [3]: Q1-SH-057. Q1-WC-K0426, Q1-WC-K0427
- **differs** (role): payout timing follows business location; single-currency countries pay out only to local banks; debit-card payouts only for U.S. accounts. Against Salla [3]: Q1-SA-K1520; Shopify [3]: Q1-SH-071. Q1-WC-K0378, Q1-WC-K0379, Q1-WC-K0380, Q1-WC-K0381
- **differs** (role): BNPL providers and local payment methods depend on the account country. Against Salla [3]: Q1-SA-083. Q1-WC-029, Q1-WC-031
- **differs** (role): WooPay is U.S.-only; In-Person Payments, POS and WooCommerce Tax serve listed countries (POS and card readers in the local currency); WooCommerce Shipping serves U.S. stores using dollars. Against Shopify [3]: Q1-SH-071; BigCommerce [3]: Q1-BC-133. Q1-WC-K0447, Q1-WC-K0439, Q1-WC-K0440, Q1-WC-K1320, Q1-WC-K1321, Q1-WC-K0838, Q1-WC-K0777
- **differs** (role): fee documents follow place: VAT invoices (EU, UK), JCT (Japan), Form 1099-K (U.S.), VAT/GST/CT on fees. Against Shopify [3]: Q1-SH-K1243. Q1-WC-K0486, Q1-WC-K0487, Q1-WC-K0488, Q1-WC-K0491, Q1-WC-K0792
- **differs** (role): setup asks "Where is your business located?"; the country code sets `woocommerce_currency` and units (default USD). Against Salla [3]: Q1-SA-K1989; Shopify [3]: Q1-SH-028; Shopify [4]: Q1-SH-027; BigCommerce [3]: Q1-BC-060. Q1-WC-021, Q1-WC-019, Q1-WC-020, Q1-WC-K0749
- **not in what was read:** offline methods and limits by seller country. Salla [3]: Q1-SA-072, Q1-SA-K1589. Q1-WC-N07
- **not in what was read:** own-price currency by seller country. BigCommerce [3]: Q1-BC-141. Q1-WC-N08

## [4]

- **differs** (role): a place is added in "Selling location(s)", "Shipping location(s)" or a shipping zone. Against Shopify [4]: Q1-SH-030; Salla [4]: Q1-SA-005; BigCommerce [4]: Q1-BC-K0211. Q1-WC-002, Q1-WC-003, Q1-WC-026, Q1-WC-K1073, Q1-WC-K1074
- **differs** (role): WooPayments prioritizes "new countries and currencies" by factors including store owners' requests. Against Shopify [4]: Q1-SH-072; Salla [4]: Q1-SA-077; BigCommerce [4]: Q1-BC-P0030. Q1-WC-K0403, Q1-WC-K0412
- **not in what was read:** a condition before a place goes live. Shopify [4]: Q1-SH-034. Q1-WC-N11

## [5]

- **differs** (role): changing the base currency "does not convert any amounts"; earlier orders keep theirs; unlisted currencies are added as custom ones. Against Shopify [5]: Q1-SH-K1935; Salla [5]: Q1-SA-091; BigCommerce [5]: Q1-BC-062. Q1-WC-K0748, Q1-WC-015, Q1-WC-016, Q1-WC-017
- **differs** (role): more currencies need "a multi-currency extension/plugin"; with WooPayments, "Add/remove currencies", server or manual rates and rounding, but not multi-currency payouts; the Currency Converter Widget changes display only. Against Shopify [5]: Q1-SH-K1935, Q1-SH-K1937; BigCommerce [1]: Q1-BC-043. Q1-WC-K0751, Q1-WC-018, Q1-WC-008, Q1-WC-009, Q1-WC-K0753, Q1-WC-K0755, Q1-WC-011, Q1-WC-007
- **differs** (role): the Stripe plugin needs "a second plugin" for multi-currency; gateways must support the base currency. Against Shopify [5]: Q1-SH-K1937; BigCommerce [5]: Q1-BC-046, Q1-BC-045. Q1-WC-039, Q1-WC-038, Q1-WC-016
- **differs** (role): gateways "can be added through traditional plugins", filed under "Official payments"; WooPayments "is not required". Against Shopify [5]: Q1-SH-K1523; Salla [5]: Q1-SA-K1656; BigCommerce [5]: Q1-BC-P0048. Q1-WC-K0006, Q1-WC-K0007, Q1-WC-K0002, Q1-WC-K0337, Q1-WC-K0338, Q1-WC-K0359
- **differs** (role): BNPL is enabled under Payments > Settings. Against Salla [5]: Q1-SA-088. Q1-WC-040
- **differs** (role): a partner's payments solution needs "a separate agreement". Against Shopify [5]: Q1-SH-K1695. Q1-WC-K0353, Q1-WC-K0354
- **not in what was read:** payment methods per currency. BigCommerce [5]: Q1-BC-053. Q1-WC-N12
