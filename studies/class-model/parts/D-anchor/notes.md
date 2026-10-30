# D-anchor: notes

Domain D, Customers and growth: the anchor part (Shopify and Salla), run in six batches. Each batch appends its section below; earlier batches' rows and notes are not rewritten.

## Batch 1: CUS (customers and buyer accounts)

Concerns landed: SH-C-039, SH-C-040, SH-C-041, SH-C-042, SH-C-043, SH-C-165, SA-C-060, SA-C-061, SA-C-062, SA-C-065. Capabilities CM-CUS-001 to CM-CUS-014.

### How I cut, and the grains

- **Two trees.** CM-CUS-001, customer records, holds what both platforms put in their customers section; CM-CUS-010, customer accounts, holds the buyer's own sign-in and registration. Shopify keeps them apart in its own organization (its Customers section against Settings > Customer accounts and its admin section CustomerAccounts), and Q1's M-018 granularity note says so ("Shopify splits customer records (SH-C-039) from customer accounts (SH-C-041)"). Salla puts both under its customers settings (customers/address, customers/login_methods, customers/recaptcha, customers/whatsapp_otp, SA-S-1714 to SA-S-1717), and its records under the Customers link. Where the groupings differ, the brief says to follow the anchor platforms' admin grouping, and they don't share one here, so CM-CUS-010 has no parent. A reading.
- **M-018 is a difference of grain**, not one capability: it holds SH-C-039 and SH-C-041 on Shopify's side against SA-C-060. SH-C-039 and SA-C-060 land in CM-CUS-001 by the match; SH-C-041 lands in CM-CUS-010, joined on role with SA-C-062 (below). The checker flags that M-018's concerns land in two trees: this is why.
- **Children of customer records.** A sub-part became a capability where at least one platform gives it a place of its own (the dry run's rule): bulk actions (Shopify's route customer:bulk-edit; Salla's plan line and flag), merge (Shopify's route customer:merge), blocking (Salla's plan line حظر العميل), flagging non-serious customers (Salla's plan line كشف العملاء غير الجادين), marketing consent (Shopify's route :id/marketing), addresses (Salla's settings route customers/address). I read a plan line as giving a place of its own only where it names a distinct function. Salla's plan lines for adding, editing and sorting customers (SA-S-2055, SA-S-2057, SA-S-2058) are what a customer record is, so they stay in CM-CUS-001, and so do customer tags, custom fields and metadata, search and the approval permission, which have only flags, webhook topics or permissions.
- **Segments and groups (CM-CUS-002)** join by Q1's M-019. Salla's automatic classification (SA-S-2150) is a plan line of its own, but its description, classifying customers by properties such as the number of orders, is the grouping itself, so it stays in CM-CUS-002. Shopify's customer saved searches (customer_groups/*) stay there too: its webhook topics say they are the same customer groups under an older name (SH-S-5969 "a customer saved search is created").
- **Map and location services (CM-CUS-009)** are a child of addresses because Salla puts them in its addresses concern and gives them an app category, Geolocation (SA-S-1226). What they locate isn't stated beyond the category's title.
- **Children of customer accounts.** Third-party identity providers and single sign-on (CM-CUS-011: Shopify's routes identity_providers and authentication in CustomerAccounts), reCAPTCHA verification (CM-CUS-012: Salla's own settings route), WhatsApp verification (CM-CUS-013: Salla's own settings route), and customer account UI extensions (CM-CUS-014: Shopify's own extension type). Salla's registration form (register_fields_management, نموذج التسجيل) is only a permission, so it stays in CM-CUS-010.

### Joins on role

- **CM-CUS-010, SH-C-041 with SA-C-062.** Shopify calls it Customer accounts, Salla Login & registration options. Both platforms' statements show the buyer signing in to the store with a one-time code: Shopify's default sign-in, "They enter their email address and receive a one-time 6-digit verification code. A password isn't required to sign in." (SH-C-041/decides/SH-S-0743); Salla's events customer.login, "تسجيل دخول عميل للمتجر" (SA-C-062/boundary/SA-S-1609), and customer.otp.request, "طلب كود تحقق تسجيل دخول" (SA-C-062/boundary/SA-S-1610). Salla's statement of the buyer creating an account in the store (SA-C-066/boundary/SA-S-5023, domain A, which names D under also) is cited as shows. A reading.
- **CM-CUS-011, SH-C-042 with Salla's flag sso-login (SA-C-062/decides/SA-S-3168).** It rests on the flag's name alone, which isn't released. A reading, and the weakest join in this batch: a reviewer may prefer to move the flag to CM-CUS-010 and rule U-017's second pair nested:CM-CUS-011.

### Homonyms kept apart

- **Geolocation.** Salla's app category Geolocation / الموقع الجغرافي (SA-C-065/where/SA-S-1226, in its customer addresses concern) against Shopify's Geolocation apps (SH-C-111/where/SH-S-2681, visitor geolocation, domain E, Q1's M-087). U-079 ruled apart.
- **Bot protection against reCAPTCHA verification.** Shopify's Bot protection blocks bots from the checkout (SH-C-051/reason/SH-S-0745, domain A); Salla's reCAPTCHA verification is a customers setting beside login options (SA-C-062/where/SA-S-1715). Kept apart; Shopify's cell for CM-CUS-012 is none-held.
- **WhatsApp.** Shopify's WhatsApp marketing consent (SH-C-043/boundary/SH-S-0884, CM-CUS-007) and the merchant's own sign-up with WhatsApp (SH-I-1755) against Salla's WhatsApp verification for buyers (SA-C-062/where/SA-S-1716, CM-CUS-013).
- **Merging accounts.** Salla's merging of a merchant's own accounts under one email (SA-C-003/boundary/SA-S-5150, domain A) isn't customer merge (CM-CUS-004).
- **Customer disable.** Shopify's customers/disable and customers/enable topics (SH-I-0435, SH-I-0436) aren't defined in the concern map; they stay in CM-CUS-001 and aren't joined with Salla's blocking (CM-CUS-005).

### Strained fits

- **SH-C-041 in CM-CUS-010.** The API resources customerAddressCreate, customerAddressDelete and customerAddressUpdate (SH-I-0114 to SH-I-0116) are placed by Q1 in both SH-C-039 and SH-C-041, and are cited in CM-CUS-008, in the customer records tree. The checker counts them as SH-C-041's, so the landing is strained.

### Concerns read under `also`, and other domains' statements

- SA-C-066 (domain A, names D): SA-S-5023, the privacy policy shown when the buyer registers, cited as shows in CM-CUS-010.
- SA-C-200 (domain D, batch 6, NTF): SA-S-0161, OTP sign-in needs an SMS provider from the app store, cited as extension-point in CM-CUS-010. Batch 6 lands SA-C-200; if it cites SA-S-0161 too, that landing reads it in another tree.
- SA-C-122 (domain C, doesn't name D): SA-S-5052, the definition of the tag عميل غير جاد, cited as shows in CM-CUS-006, because it is the only statement that says what the plan line rests on. The checker flags it. It supports no placement, so no statement supports core in two domains.
- Not cited, other domains: Shopify's address-autocomplete extension targets in checkout (SH-I-1640, SH-I-1641, in SH-C-049, domain C), which might bear on WooCommerce's address autocomplete (WC-C-047, U-079) in the mapping part; Shopify's shipping_addresses/* webhook statements (SH-C-114, SH-C-158), which don't say whose address; Salla's App Snippets (SA-C-198, F), App Functions' User Profile Updated (SA-C-196, F) and the theme's salla-user-profile (SA-C-091, E).

### For later batches

- **SH-C-043/responsible/SH-S-0067** (merchant responsible for consents under Shopify Pixel Manager) is about tracked events, not marketing consent, and isn't cited here. If batch 2 cites it in the pixels capability (SH-C-146, MKT), SH-C-043's landing in CM-CUS-007 becomes strained.
- **SH-C-041/decides/SH-S-7213** (B2B buying by adding customer profiles to a company, Shopify Plus) isn't cited here. If batch 6 cites it in B2B, SH-C-041's landing gains another tree.
- **SA-C-092/boundary/SA-S-1359** (Account Events, Profile Updated) bears on buyer accounts; batch 5 lands SA-C-092 and may cite it in CM-CUS-010 as shows.
- **SA-C-200's SA-S-0161** is cited here (above).
- No ruling pair of this batch's concerns waits on a later batch: U-017 and U-079 are both ruled here. WooCommerce's pairs in them (WC-C-073, WC-C-046, WC-C-047) are for the WooCommerce part.

### Gaps that limit the cells

- Salla: SA-C-060's and SA-C-061's responsible and reason pages, and SA-C-062's responsible page, were not read (Q1 gaps), so who answers for customers, groups and login can't be claimed.
- Shopify: SH-C-040's, SH-C-041's and SH-C-042's responsible placements are stated only in general terms; the reason placements of SH-C-039 to SH-C-043 and SH-C-165 were searched and not found.
- No statement defines Salla's customer_approve (قبول التحاق العملاء), customer-advance-management, its map service flags, reCAPTCHA verification or WhatsApp verification beyond their names; or Shopify's customers/disable, the plan line Unlimited contacts, or what a bulk edit changes.
- No statement names a maker other than the platform for anything in CUS; no own-service cell.

### What the checker flagged, answered

- SA-C-122/boundary/SA-S-5052 from domain C: answered above.
- none-held with matches: CM-CUS-005 Shopify (customers/disable, undefined), CM-CUS-006 Shopify (orders' fraud analysis, SH-C-059, and Shopify Protect, SH-C-073), CM-CUS-007 Salla (plans, availability notifications, privacy consent at registration, partner terms), CM-CUS-009 Shopify (visitor geolocation, checkout address autocomplete, shipping-label address validation), CM-CUS-012 Shopify (checkout bot protection), CM-CUS-013 Shopify (the email one-time code, cited in CM-CUS-010), CM-CUS-014 Salla (the merchant's profile, the theme's profile component, App Functions, App Snippets). Each cell's reading says what was found and why it isn't cited.
- M-018 in two trees: answered under the grains.
- SH-C-041 strained: marked, see above.
