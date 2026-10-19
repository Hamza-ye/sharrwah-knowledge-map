# Q3 · BigCommerce: checked against Shopify, Salla and Zid

## [1]

- **differs** (role): Registering an Account takes true, accurate, current and complete information, kept current, possibly a valid means of payment, and Account Credentials; Commerce may refuse or cancel violating accounts. The free trial needs no credit card. The Account's creator is generally deemed the owner. vs Shopify [1]: Q3-SH-K1238 (Opening an account); Salla [1]: Q3-SA-043; Zid [1]: Q3-ZD-042, Q3-ZD-032; Zid [4]: Q3-ZD-071. Q3-BC-002; Q3-BC-009; Q3-BC-004
- **differs** (role): Age of majority and capacity to contract; not for under-18s. vs Shopify [1]: Q3-SH-K1532; Salla [1]: Q3-SA-043; Zid [1]: Q3-ZD-041. Q3-BC-001
- **differs** (role): Neither the seller nor its Relevant Parties and customers may be from comprehensively sanctioned regions; the seller screens and cooperates. vs Shopify [1]: Q3-SH-K1238 (Opening an account), Q3-SH-K1532. Q3-BC-K0428; Q3-BC-K0430; Q3-BC-K0431; Q3-BC-K0432
- **differs** (role): The default currency is assigned from the location at creation; changing it needs the new currency added first, in Settings › Currencies. vs Shopify [1]: Q3-SH-002. Q3-BC-031; Q3-BC-032
- **differs** (role): A privacy policy, an agreement with Your Users, and products complying with all Laws. vs Shopify [1]: Q3-SH-K1301; Salla [1]: Q3-SA-034; Zid [1]: Q3-ZD-K0245, Q3-ZD-K0246. Q3-BC-K0465; Q3-BC-K0466; Q3-BC-005
- **differs** (role): Stripe OCS: the statement descriptor must meet Stripe's requirements. vs Shopify [1]: Q3-SH-088 (United States). Q3-BC-033
- **goes beyond**: PCI DSS: ultimate responsibility lies with the seller; Commerce's role is conditional on an unmodified checkout; payment-page scripts need an SRI hash. Q3-BC-025; Q3-BC-026; Q3-BC-027; Q3-BC-K0155; Q3-BC-K0157
- **goes beyond**: GMV caps per plan, with automatic upgrades. Q3-BC-K0174; Q3-BC-K0175; Q3-BC-K0176
- **not in what was read**: Shopify [1]: Q3-SH-012 (Who and what), Q3-SH-015, Q3-SH-041, Q3-SH-065; Salla [1]: Q3-SA-013, Q3-SA-072; Zid [1]: Q3-ZD-035, Q3-ZD-037, Q3-ZD-039. Q3-BC-N01
- **not in what was read**: Salla [1]: Q3-SA-032; Zid [1]: Q3-ZD-P0120. Q3-BC-N02
- **not in what was read**: Shopify [1]: Q3-SH-K1274. Q3-BC-N03
- **not in what was read**: Shopify [1]: Q3-SH-K1885. Q3-BC-N04
- **not in what was read**: Zid [1]: Q3-ZD-029. Q3-BC-N05
- **not in what was read**: Shopify [1]: Q3-SH-K1794. Q3-BC-N06
- **not in what was read**: Salla [1]: Q3-SA-055. Q3-BC-N13

## [2]

- **differs** (term; role): The free trial allows launching and taking payments once a payments partner is set up; storefront status has prelaunch fields; a test order is advised before launch. vs Shopify [1]: Q3-SH-027, Q3-SH-032; Zid [2]: Q3-ZD-033. Q3-BC-010; Q3-BC-013; Q3-BC-028; Q3-BC-029; Q3-BC-K0256
- **differs** (role): BigCommerce Payments needs a Core, Growth or Scale plan, a supported checkout, a UK or US store and PayPal Business account; earlier pages say US only, Retail plan, or beta plans and terms. vs Shopify [1]: Q3-SH-K1532; Salla [2]: Q3-SA-P0060; Zid [2]: Q3-ZD-P0113. Q3-BC-P0068; Q3-BC-P0087; Q3-BC-P0029; Q3-BC-P0030; Q3-BC-K0132; Q3-BC-K0133; Q3-BC-P0061; Q3-BC-P0060
- **differs** (role): Setup in Settings › Payments creates a PayPal platform account; the seller adds a bank account and confirms the account in the Actions section (profile, bank, KYC status, fund holds) before accepting payments. vs Shopify [1]: Q3-SH-003, Q3-SH-011; Salla [1]: Q3-SA-026; Zid [2]: Q3-ZD-024. Q3-BC-014; Q3-BC-015; Q3-BC-016; Q3-BC-P0069; Q3-BC-P0066; Q3-BC-P0072
- **differs** (role): Payouts go to a linked bank or PayPal account. vs Shopify [1]: Q3-SH-009; Salla [1]: Q3-SA-009; Zid [2]: Q3-ZD-P0037. Q3-BC-P0073; Q3-BC-P0074; Q3-BC-P0075
- **differs** (role): The payment relationship stays with PayPal; the PayPal Braintree rate needs a qualifying plan, an application and a signed Pricing Contract. vs Salla [2]: Q3-SA-K1533; Zid [2]: Q3-ZD-074. Q3-BC-P0040; Q3-BC-012; Q3-BC-P0063
- **differs** (role): Other providers need their own application, underwriting or account, in supported countries. vs Salla [2]: Q3-SA-K1436; Zid [2]: Q3-ZD-058, Q3-ZD-P0080. Q3-BC-P0048; Q3-BC-P0092; Q3-BC-P0064; Q3-BC-P0065; Q3-BC-P0106; Q3-BC-019; Q3-BC-P0062
- **differs** (role): Stored payment methods need Growth or higher; Pay Later, listed countries; a checkout currency, a supporting provider. vs Salla [2]: Q3-SA-K1617; Shopify [1]: Q3-SH-011. Q3-BC-024; Q3-BC-P0113; Q3-BC-030
- **differs** (role): Cash on Delivery is set up by the seller, by country. vs Zid [2]: Q3-ZD-049; Salla [2]: Q3-SA-K1436. Q3-BC-P0117; Q3-BC-P0121
- **differs** (role): The seller warrants and keeps verifying its products' legality, which Commerce doesn't evaluate; PayPal and Stripe list restricted items and businesses. vs Shopify [1]: Q3-SH-049, Q3-SH-K1530; Salla [2]: Q3-SA-054, Q3-SA-047; Zid [1]: Q3-ZD-052; Zid [2]: Q3-ZD-023, Q3-ZD-075; Zid [4]: Q3-ZD-023. Q3-BC-006; Q3-BC-K0459; Q3-BC-K0460; Q3-BC-K0461; Q3-BC-021; Q3-BC-022
- **differs** (role): PayPal Agentic Commerce beta: US, Enterprise Plan, PayPal, non-restricted category. vs Shopify [1]: Q3-SH-075; Salla [2]: Q3-SA-061; Zid [2]: Q3-ZD-061, Q3-ZD-P0144, Q3-ZD-079. Q3-BC-P0039
- **not in what was read**: Salla [2]: Q3-SA-022; Zid [2]: Q3-ZD-K0238. Q3-BC-N02
- **not in what was read**: Zid [2]: Q3-ZD-P0118, Q3-ZD-002, Q3-ZD-012, Q3-ZD-017, Q3-ZD-009, Q3-ZD-008, Q3-ZD-P0117. Q3-BC-N01
- **not in what was read**: Salla [2]: Q3-SA-071. Q3-BC-N04
- **not in what was read**: Zid [2]: Q3-ZD-P0132. Q3-BC-N06
- **not in what was read**: Salla [2]: Q3-SA-029. Q3-BC-N07
- **not in what was read**: Zid [2]: Q3-ZD-P0116. Q3-BC-N08
- **not in what was read**: Salla [2]: Q3-SA-P0072; Zid [2]: Q3-ZD-P0109. Q3-BC-N09
- **not in what was read**: Zid [2]: Q3-ZD-P0159. Q3-BC-N10
- **not in what was read**: Zid [2]: Q3-ZD-K0509. Q3-BC-N11
- **not in what was read**: Zid [2]: Q3-ZD-P0152. Q3-BC-N12

## [4]

- **differs** (role): Payment methods usually follow within one business day of a completed profile; Stripe flags accounts for verification after a processing threshold; PayPal Braintree reviews accounts periodically. vs Shopify [4]: Q3-SH-K1617; Salla [4]: Q3-SA-021; Zid [4]: Q3-ZD-P0038 (Zid Pay: after submitting). Q3-BC-018; Q3-BC-020; Q3-BC-K0145
- **differs** (role): PayPal Braintree decides approval. vs Shopify [4]: Q3-SH-012; Zid [4]: Q3-ZD-P0118. Q3-BC-P0065; Q3-BC-K0145
- **differs** (role): An incomplete profile blocks enabling payment methods; unmet Pay Later requirements are listed; initial payments are held up to 21 days; held funds may need documents or verification. vs Shopify [4]: Q3-SH-017, Q3-SH-064; Salla [4]: Q3-SA-001, Q3-SA-K0073, Q3-SA-062; Zid [2]: Q3-ZD-P0063; Zid [4]: Q3-ZD-P0063. Q3-BC-017; Q3-BC-023; Q3-BC-P0083; Q3-BC-P0084
- **differs** (role): After an unconverted trial customers can't access the store, which is deleted after 90 days; overdue fees may suspend access; paying by PayPal or ACH needs written approval. vs Shopify [4]: Q3-SH-036; Zid [4]: Q3-ZD-040, Q3-ZD-048. Q3-BC-011; Q3-BC-008; Q3-BC-003
- **differs** (role): Breaches allow suspension, termination or Store removal. vs Shopify [4]: Q3-SH-044, Q3-SH-056; Salla [4]: Q3-SA-051; Zid [4]: Q3-ZD-051, Q3-ZD-073. Q3-BC-007; Q3-BC-K0463; Q3-BC-K0429
- **not in what was read**: Shopify [4]: Q3-SH-086. Q3-BC-N13
- **not in what was read**: Shopify [4]: Q3-SH-069; Zid [4]: Q3-ZD-028. Q3-BC-N14; Q3-BC-N16
- **not in what was read**: Salla [4]: Q3-SA-004. Q3-BC-N15
- **not in what was read**: Salla [4]: Q3-SA-023. Q3-BC-N16
- **not in what was read**: Shopify [4]: Q3-SH-030; Zid [4]: Q3-ZD-063, Q3-ZD-065, Q3-ZD-083. Q3-BC-N17
