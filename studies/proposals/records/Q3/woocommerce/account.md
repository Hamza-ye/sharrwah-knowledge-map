# Q3, WooCommerce: check against Shopify, Salla and Zid

## [1]

- **differs** (role): Shopify [1]: Q3-SH-012; Salla [1]: Q3-SA-013; Zid [2]: Q3-ZD-P0118. WooPayments' "Know Your Customer" gathers owner and business information, including date of birth and tax ID, verified with Stripe. Q3-WC-K0395; Q3-WC-K0371; Q3-WC-001; Q3-WC-002; Q3-WC-003; Q3-WC-012; Q3-WC-005
- **differs** (role): Shopify [1]: Q3-SH-K1532, Q3-SH-K1539; Salla [1]: Q3-SA-043; Zid [1]: Q3-ZD-041; Zid [2]: Q3-ZD-P0113. WooPayments requires a business in a supported country, HTTPS, recent software and age 18; the country can't be changed later. Q3-WC-010; Q3-WC-K0400; Q3-WC-K0402; Q3-WC-011; Q3-WC-K0407; Q3-WC-K0408; Q3-WC-K0409; Q3-WC-018
- **differs** (role): Salla [1]: Q3-SA-072. UAE: Business account type only. Q3-WC-K0411; Q3-WC-K0405
- **differs** (role): Shopify [1]: Q3-SH-K1238; Zid [1]: Q3-ZD-042. WooPayments and WooCommerce Tax require a WordPress.com account connection. Q3-WC-K0360; Q3-WC-K0725; Q3-WC-K0726; Q3-WC-K0728; Q3-WC-K0730
- **differs** (role): Shopify [1]: Q3-SH-K1719; Salla [2]: Q3-SA-K1532; Zid [2]: Q3-ZD-027. "Finish setup" agrees to the Terms of Service; the Stripe Connected Account Agreement is agreed at signup. Q3-WC-K0369; Q3-WC-K0485; Q3-WC-P0018; Q3-WC-P0103
- **differs** (role): Shopify [1]: Q3-SH-027; Zid [2]: Q3-ZD-033. "Get ready to start selling" ends with LaunchYourStore, complete once `woocommerce_coming_soon` isn't 'yes'. Q3-WC-K1235; Q3-WC-K1236; Q3-WC-036; Q3-WC-037; Q3-WC-038; Q3-WC-039
- **differs** (role): Shopify [1]: Q3-SH-027. Test mode is disabled before live payments. Q3-WC-017; Q3-WC-013
- **differs** (role): Zid [2]: Q3-ZD-P0080. PayPal Standard needs a PayPal Business account's email. Q3-WC-P0099; Q3-WC-P0102; Q3-WC-P0155
- **differs** (role): Shopify [1]: Q3-SH-K1540; Salla [2]: Q3-SA-054; Zid [2]: Q3-ZD-075. Card networks and processors bar some businesses and products from WooPayments. Q3-WC-K0416; Q3-WC-019; Q3-WC-K0422; Q3-WC-K0415
- **differs** (role): Salla [2]: Q3-SA-054. Ecommerce Services must observe the Store Guidelines. Q3-WC-K0495; Q3-WC-K0494
- **differs** (role): Shopify [1]: Q3-SH-049. Alcohol is permitted in some instances; CBD sellers must use Square or Viva Wallet. Q3-WC-020; Q3-WC-K0417; Q3-WC-K0532
- **differs** (role): Shopify [1]: Q3-SH-K2276. Services exclude comprehensively sanctioned countries and listed parties. Q3-WC-K0525; Q3-WC-K0526; Q3-WC-K0528
- **differs** (role): Shopify [1]: Q3-SH-K1301; Salla [1]: Q3-SA-034; Zid [1]: Q3-ZD-K0245; Zid [2]: Q3-ZD-P0116. Alipay, WeChat Pay, iDEAL | Wero and P24 set website requirements. Q3-WC-024; Q3-WC-025; Q3-WC-029; Q3-WC-030; Q3-WC-031; Q3-WC-032
- **differs** (role): Shopify [1]: Q3-SH-011. Some payment methods need support to enable. Q3-WC-023; Q3-WC-035
- **differs** (role): Shopify [1]: Q3-SH-090. Statement descriptor rules. Q3-WC-021
- **differs** (role): Shopify [1]: Q3-SH-009; Salla [1]: Q3-SA-009; Zid [2]: Q3-ZD-P0037. Payouts go to a bank account, or a debit card in the U.S. Q3-WC-P0027; Q3-WC-K0381; Q3-WC-K0379
- **differs** (role): Salla [2]: Q3-SA-P0062; Zid [2]: Q3-ZD-K0025. Minimum payouts by currency; a 7-day first-payout wait. Q3-WC-P0039; Q3-WC-P0038
- **differs** (role): Shopify [1]: Q3-SH-K1816; Zid [2]: Q3-ZD-P0132. Stripe Capital eligibility is reviewed daily. Q3-WC-K0453; Q3-WC-P0078
- **differs** (role): Salla [2]: Q3-SA-K1436. Point of Sale needs a supported country and its currency. Q3-WC-K0439; Q3-WC-K1320; Q3-WC-K1321
- **differs** (role): Salla [2]: Q3-SA-P0072; Zid [2]: Q3-ZD-P0109. WooPay is U.S.-only and excludes Link by Stripe. Q3-WC-K0447; Q3-WC-K0448
- **differs** (role): Shopify [1]: Q3-SH-K1886; Salla [2]: Q3-SA-071. WooCommerce Tax covers stores in listed countries. Q3-WC-K0777; Q3-WC-K0783
- **differs** (role): Salla [1]: Q3-SA-055; Shopify [4]: Q3-SH-086. WooPayments onboarding steps, through `business_verification`. Q3-WC-040; Q3-WC-041
- **differs** (role): Shopify [1]: Q3-SH-002. Before changing the base currency, the payment gateway's support is confirmed; a change converts no amounts, and earlier orders keep theirs. Q3-WC-042; Q3-WC-043; Q3-WC-044
- **differs** (role): Shopify [1]: Q3-SH-075; Zid [2]: Q3-ZD-061. Google for WooCommerce products are approved by Google when the product feed includes required information. Q3-WC-045
- **differs** (role): Zid [2]: Q3-ZD-049. Cash on Delivery is enabled under Take offline payments. Q3-WC-048
- **differs** (role): Zid [1]: Q3-ZD-029. WooPayments signup verifies the phone number before personal and business details. Q3-WC-049
- **goes beyond**: instant payouts need a U.S. account over 90 days old with low disputes. Q3-WC-P0047; Q3-WC-P0046
- **goes beyond**: PCI DSS compliance is the store owner's responsibility. Q3-WC-K0482; Q3-WC-K0480; Q3-WC-K0479
- **goes beyond**: hosting must meet minimum specifications; an existing Stripe account can't be used. Q3-WC-K0564; Q3-WC-K0713
- **goes beyond**: the signup phone number becomes the store's support phone number. Q3-WC-014
- **not in what was read**: Shopify [1]: Q3-SH-K1274. Q3-WC-N01
- **not in what was read**: Shopify [1]: Q3-SH-020; Salla [1]: Q3-SA-K0086. Q3-WC-N02
- **not in what was read**: Shopify [1]: Q3-SH-015; Shopify [1]: Q3-SH-041; Zid [1]: Q3-ZD-037. Q3-WC-N03
- **not in what was read**: Shopify [1]: Q3-SH-027; Salla [2]: Q3-SA-P0060; Zid [1]: Q3-ZD-032. Q3-WC-N04
- **not in what was read**: Shopify [1]: Q3-SH-050; Salla [2]: Q3-SA-047; Zid [2]: Q3-ZD-023. Q3-WC-N05
- **not in what was read**: Salla [1]: Q3-SA-044; Zid [2]: Q3-ZD-P0120. Q3-WC-N06
- **not in what was read**: Zid [2]: Q3-ZD-074. Q3-WC-N10
- **not in what was read**: Salla [2]: Q3-SA-K1617. Q3-WC-N11
- **not in what was read**: Zid [2]: Q3-ZD-P0063. Q3-WC-N12
- **not in what was read**: Shopify [1]: Q3-SH-K1264. Q3-WC-N14
- **not in what was read**: Shopify [1]: Q3-SH-065. Q3-WC-N15
- **not in what was read**: Salla [1]: Q3-SA-032. Q3-WC-N16
- **not in what was read**: Salla [1]: Q3-SA-030. Q3-WC-N17
- **not in what was read**: Salla [2]: Q3-SA-022. Q3-WC-N18
- **not in what was read**: Salla [2]: Q3-SA-029. Q3-WC-N20

## [4]

- **differs** (role): Shopify [4] "Parties named": Q3-SH-012; Salla [4]: Q3-SA-004; Zid [4]: Q3-ZD-P0118. Regulation, Stripe, Alipay, WeChat Pay and Przelewy24 set requirements. Q3-WC-K0395; Q3-WC-K0398; Q3-WC-K0405; Q3-WC-K0388; Q3-WC-026; Q3-WC-035
- **differs** (role): Shopify [4] "Evaluation and re-verification": Q3-SH-K1617; Salla [4]: Q3-SA-021; Zid [4] "Zid Pay: after submitting": Q3-ZD-P0038. Confirmation typically within a couple of days; P24 reviews continuously. Q3-WC-004; Q3-WC-K0394; Q3-WC-015; Q3-WC-016; Q3-WC-028; Q3-WC-033
- **differs** (role): Shopify [4]: Q3-SH-017; Shopify [4]: Q3-SH-044; Zid [4]: Q3-ZD-028. Payments or payouts may be restricted once a deadline for missing information passes; verification problems show on Payments > Overview. Q3-WC-051; Q3-WC-P0055; Q3-WC-007; Q3-WC-K0413; Q3-WC-008; Q3-WC-009
- **differs** (role): Salla [4]: Q3-SA-050; Zid [4]: Q3-ZD-073, Q3-ZD-051, Q3-ZD-040. Accounts may be refused, conditioned or suspended. Q3-WC-P0019; Q3-WC-K0716; Q3-WC-P0052
- **differs** (role): Shopify [4]: Q3-SH-058. Revoked P24 makes P24 orders fail at checkout. Q3-WC-027; Q3-WC-034
- **differs** (role): Shopify [4]: Q3-SH-091. Without a statement descriptor, the site URL is used. Q3-WC-022
- **differs** (role): Zid [2]: Q3-ZD-P0152. A business that moved country can't update it; support handles it. Q3-WC-050
- **differs** (role): Shopify [4]: Q3-SH-030. Google approves Active products for free listings within 3-5 days; products missing required fields aren't synced. Q3-WC-047; Q3-WC-046
- **differs** (role): Salla [4]: Q3-SA-K0073. Stripe may delay or withhold payouts of amounts subject to a Dispute. Q3-WC-P0126
- **goes beyond**: account information may not be changeable once saved. Q3-WC-006
- **goes beyond**: disconnected from WordPress.com, WooPayments can't take payments. Q3-WC-K0731
- **goes beyond**: opting out of an updated Connected Account Agreement ends WooPayments use. Q3-WC-K0714; Q3-WC-K0715
- **not in what was read**: Shopify [4]: Q3-SH-046. Q3-WC-N07
- **not in what was read**: Shopify [4]: Q3-SH-069; Zid [4]: Q3-ZD-P0012. Q3-WC-N08
- **not in what was read**: Shopify [4]: Q3-SH-P0085; Salla [4]: Q3-SA-023. Q3-WC-N09
- **not in what was read**: Shopify [4]: Q3-SH-036. Q3-WC-N13
- **not in what was read**: Zid [4] "Zid Pay may request": Q3-ZD-078. Q3-WC-N19
