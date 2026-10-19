# Q6 on Shopify: who can register as a seller, and from where

## [1]

### Opening an account

- Shopify's Terms of Service require a Shopify account ("Account") to use the Services. To register, you give your full legal name, business address, phone number and email address. Shopify "may reject your application for an Account, or cancel an existing Account, for any reason, at our sole discretion." The Help Center repeats these items and says they are used to verify your identity when registering. Q6-SH-K1238; Q6-SH-005
- Age: "You must be the older of: (i) 18 years, or (ii) at least the age of majority in the jurisdiction where you reside and from which you use the Services to open an Account." The Help Center's checklist says someone under 18 should have a parent or guardian set up the account using their own details, and that accounts set up under the details of anyone under 18 "may potentially be closed". Q6-SH-001; Q6-SH-004
- Purpose: the person opening the account confirms they receive the Services "for the purposes of carrying on a business activity and not for any personal, household or family purpose". Q6-SH-002
- The person who signs up becomes the "Store Owner", the contracting party. A store has one Store Owner, and a Store Owner may have several stores. If you sign up on behalf of your employer, your employer is the Store Owner. Q6-SH-K1237; Q6-SH-K1239; Q6-SH-K1240; Q6-SH-003
- Signing up or using the Services binds the seller to the Terms of Service. Those terms incorporate the AUP and the Privacy Policy, and, where they apply, the EU Terms, the API Terms and the DPA. Q6-SH-K1241; Q6-SH-K1242

### Where the seller says they are

- The free trial steps include "3. Specify your business location." Q6-SH-007
- The sign-up page has a combobox labelled "I'm located in:". The captured page lists 233 options, with Yemen marked [selected]. Q6-SH-K2662; Q6-SH-010
- A store was created from that sign-up with `country=YE`. `storeCreate` returned no `userErrors`, and the store's billing address has `"countryCode":"YE"`. For the organization of another store, ctcbwa-r1, the admin's legal entity record holds `"countryCode":"YE"`, with entity types Individual, Company and Non-Profit. Q6-SH-011; Q6-SH-012; Q6-SH-K2674; Q6-SH-K2675; Q6-SH-K2676; Q6-SH-K2677
- On 6 October 2026 the sign-up page, with "[Yemen]" in its location field, showed "Start your free trial" and "3 days free, then 3 months for $1/month". Q6-SH-043
- The seller must keep an accurate location in the admin and update it after changing jurisdictions. To change the store's country, the seller must first deactivate all financial services: Shopify Payments, Balance, Capital and Credit. Q6-SH-K1271; Q6-SH-006
- No words were found that present the "I'm located in:" options as the full set of places a seller can register from. Q6-SH-N03

### Places Shopify does not support

- Shopify says it "is unable to support business involving certain regions due to local regulatory requirements, commercial partnerships, and/or other pertinent factors". Its list "contains the countries and regions that aren't supported by Shopify": Cuba, Iran, North Korea, Syria, and the Crimea region of Ukraine with the so-called Donetsk and Luhansk People's Republics. Q6-SH-K2270; Q6-SH-018; Q6-SH-K2271; Q6-SH-K2272; Q6-SH-K2273; Q6-SH-K2274; Q6-SH-K2275
- On those places, the list says: individuals and businesses within them are prohibited from creating a Shopify account; access to storefronts and accounts is prohibited within them; products originating from them are prohibited; and orders shipping to them are prohibited. Q6-SH-K1270; Q6-SH-K2276; Q6-SH-K2277; Q6-SH-K2278; Q6-SH-K2279
- Where on the platform these restrictions take effect, and the screening interface behind the sanctions checks, were not found. Q6-SH-G0216; Q6-SH-G0217

### Contracting entity, billing address and business entity

- The seller contracts with a "Shopify Contracting Party" chosen by the store's billing address: Shopify Inc. and Shopify Technology (USA) Inc. for the United States or Canada; Shopify Commerce Singapore Pte. Ltd for Asia Pacific; and Shopify International Limited (Ireland) for "All other jurisdictions". Elsewhere Shopify describes this entity as contracting with merchants in EMEA and LATAM. The terms are governed by the laws of Ontario. Q6-SH-K1243; Q6-SH-K1244; Q6-SH-K1246; Q6-SH-K1247; Q6-SH-K1248; Q6-SH-K1249; Q6-SH-K1250; Q6-SH-K1253
- The billing address determines the billing taxes, the payment methods and billing currencies available, and "the Shopify company that issues your bill". Its country must match one of the seller's active business entities, and you can't enter a country you have no entity in. To use an unlisted country, you first add a business entity for it. Q6-SH-013; Q6-SH-K1259; Q6-SH-014; Q6-SH-015
- A business entity is "the registered business, or the individual, that your store operates as". It is used to verify the business, and it sets what must be provided for financial services. Q6-SH-K1260
- In store ts15uk-ug (My Store 8), observed 7 October 2026, Settings > General showed, under Business details, "Business entity used for financial products, markets, apps, and taxes in this shop", with "My Store 8 - entity" in Yemen. The store's own answer gives `"countryCode":"YE","currencyCode":"YER"`. Q6-SH-035
- In store capture-advanced, observed 4 October 2026, saving business details with Country code "United States" and "Individual / Sole proprietorship" was refused: "Couldn't save changes", "Capture Entity is already associated with an individual business entity in this country. Add someone else or switch entities in Settings > General." Q6-SH-042
- In store ibx5bt-xy (My Store), observed 30 September 2026, the saved HTML of Settings > General holds, under Business details, "My Second Demo Store - entity" in Yemen; its General page gives Store address Yemen and Yemeni Rial (YER). The saved HTML of its Organization page lists two business entities: "My Second Demo Store - entity", Yemen, Company; and "demo fake dev store - entity", Al-Janad, Al-Janad, Yemen, Individual. Its Billing address page's saved HTML holds Legal entities "nmv - YE" and "fake first name fake last name - YE", and Country/region [Yemen]; its accessibility tree marks that Country/region field disabled, with Yemen as its one option. Q6-SH-044; Q6-SH-045; Q6-SH-046
- Selling with several entities is available only with Shopify Payments, and only for organizations on the Shopify Plus and Shopify Enterprise Commerce plans. For store ts15uk-ug, whose business entity is in Yemen, the admin's answer gave `"multiLegalEntitiesPhase":"INELIGIBLE"`. Q6-SH-K1264; Q6-SH-K1265; Q6-SH-035; Q6-SH-039
- No clause was found that names who is responsible when a store sells with several entities. Q6-SH-G0009

### Paying for a plan

- The payment methods for paying Shopify bills depend on the store's region and billing currency. Credit cards from Mastercard, Visa, American Express, Diners Club or Discover are accepted. "Prepaid and virtual credit cards aren't accepted." Q6-SH-016; Q6-SH-017
- To sell and accept orders during the free trial, you need to set up a payment provider. Trial length and pricing "might vary by store location". Q6-SH-008; Q6-SH-009

### Identity verification

- In most cases the store owner completes identity verification. Certain account features might be restricted until it is complete. It is required, for example, when applying for Shopify Capital or Credit. Q6-SH-K1281; Q6-SH-K1280; Q6-SH-K1279

### Shopify Payments: who qualifies

- To be eligible for Shopify Payments, the business must be located in a supported country, its business type and products must not be prohibited, and it must comply with the laws and the Shopify Payments terms. The person setting it up must be at least 18. Under 18, a parent or guardian is the account representative, and other listed owners, directors or executives must be at least 13. Q6-SH-019; Q6-SH-K1539
- The Shopify Payments terms say: "To utilize the Payments Services, you must be a business located in your Designated Country". You "need to pass our identity and KYC checks". You may not use the service if you reside in a country or region under US, Canadian or EU sanctions or embargo. Q6-SH-K1536; Q6-SH-K1622; Q6-SH-K2268; Q6-SH-K2269
- Before activating, check that your business type is eligible and that you have the documents your country requires: "personal identification, proof of address, and business registration documents". Q6-SH-021
- The list of prohibited products and services "isn't exhaustive and it varies depending on your region". Q6-SH-K2261; Q6-SH-K2265

## [2]

### When Shopify Payments isn't available

- Shopify Payments can be used at checkout "if your business is located in one of the supported countries listed on this page". The held page lists 41 "Shopify Payments for <country>" pages, from Australia to the United States, including China. The copied pilot list has no China item. Q6-SH-P0096; Q6-SH-023; Q6-SH-P0097; Q6-SH-A0002
- In Shopify's own words: "If your country isn't listed, or if Shopify Payments doesn't support your business category, then you need to use a third-party payment provider." Its eligibility page says: "If you aren't eligible for Shopify Payments, then you can add a third-party payment provider." Q6-SH-022; Q6-SH-020
- The pricing overview says: "If Shopify Payments isn't available in your country, or if you prefer not to use it", the seller can activate a third-party provider. Shopify then charges third-party transaction fees that depend on the plan, and the provider charges its own rates. Q6-SH-024
- In the admin: "If Shopify Payments isn't available in your country, then in the Payment providers section, click Choose a provider." Q6-SH-025
- For store ts15uk-ug, observed 7 October 2026, `ShopifyPaymentsData` also gave Shopify Payments `"eligible":false`. Its `PaymentProviders` answer gave the business entity `"countryCode":"YE"`, with `"thirdPartyDirectEligible":true`, and Stripe `"available":false,"eligible":false`. Q6-SH-036; Q6-SH-037; Q6-SH-038
- That store's Payments settings page showed "Payment providers": "Providers that enable you to accept payment methods at a rate set by the third-party. An additional fee will apply to new orders once you select a plan.", with "Choose a provider". Its Third-party payment providers page listed (for testing) Bogus Gateway, Cybersource, Integration-UseePay, ONERWAY (Direct), PagBrasil - Cartão de crédito and Tap Payments. Q6-SH-040; Q6-SH-041
- In store ibx5bt-xy, whose General page gives Store address Yemen, the saved HTML of the Payments settings page, observed 30 September 2026, holds the same "Payment providers" text with "Choose a provider", and "Additional payment providers": "Offer methods processed offsite or through custom checkout integrations". Its Third-party payment providers page holds the same six providers: (for testing) Bogus Gateway, Cybersource, Integration-UseePay, ONERWAY (Direct), PagBrasil - Cartão de crédito and Tap Payments. Q6-SH-047; Q6-SH-048
- What the same pages show in store 2jiwxs-gr, created with `country=YE`, was not read. Q6-SH-N02
- For the store created with `country=YE`, the admin's `ShopifyPaymentsData` answer gives Shopify Payments `"eligible":false` and `"cardPresentSupported":false`, with `localPaymentMethodsForMerchantCountry` and `shopifyPaymentsRates` empty. Q6-SH-033; Q6-SH-034
- Shopify points sellers to its payment gateways page, which it describes as "Third-party payment providers for countries where Shopify Payments is unavailable". There you can filter providers by country or region. Q6-SH-029; Q6-SH-027
- What the payment gateways page lists for a given country was not read. Q6-SH-N01
- If a gateway isn't listed for your region, "it might not be supported by Shopify at this time", and you can consider alternatives listed as available. A provider's listing there "doesn't guarantee it's accessible in your specific store's admin due to factors such as your store's location, plan, or payment configuration". Q6-SH-028; Q6-SH-026
- Sellers are told to "select payment gateways and providers that are compatible and available in your region". In Shopify Payments countries, standalone Stripe isn't available as an alternative. Q6-SH-K1526; Q6-SH-K1527; Q6-SH-K1528

### Other parts offered only in some places

- Shopify Balance is "available only to merchants with a physical residential address in the United States or Puerto Rico", and needs a US SSN or ITIN. Q6-SH-K1793; Q6-SH-K1794
- Shopify Capital is open to eligible businesses based in Australia, Canada, France, Germany, Ireland, the Netherlands, Spain, the United Kingdom and the United States. The principal place of business and the bank account must be in that country. Q6-SH-K1815; Q6-SH-K1816
- Shopify Bill Pay "is available only to merchants in the United States". Q6-SH-K1852
- Shop Pay Installments is available to eligible stores in the United States, Canada and the United Kingdom. Q6-SH-K1688; Q6-SH-K1689
- Cryptocurrency payments require a Shopify Payments account open in the United States, Canada, Mexico or Hong Kong. Q6-SH-K1751
- Managed Markets is "only available to merchants based in the continental United States, and to certain stores in Canada and the United Kingdom". Q6-SH-K1956
- The tax services a store can use "depend on the location of your business". Automated filing is "available only for stores in the United States that use Shopify Tax". Q6-SH-K1865; Q6-SH-K1909
- POS card payments are available only in countries where Shopify Payments supports both online and in-person processing. POS hardware and Tap to Pay "vary by country". Q6-SH-K1783; Q6-SH-031
- Sales channel eligibility "depends on your region, product types, and sometimes your subscription plan". TikTok, for example, is available in select countries. Q6-SH-030; Q6-SH-032
- No sentence was found in which Shopify says why merchant location at sign-up is handled as it is. Q6-SH-G0011
