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

## Batch 2: MKT (marketing, discounts and promotions), Shopify's concerns

Concerns landed: SH-C-127, SH-C-128, SH-C-129, SH-C-130, SH-C-131, SH-C-132, SH-C-133, SH-C-134, SH-C-146, SH-C-194. Capabilities CM-MKT-001 to CM-MKT-015, with a Salla cell for each, found by searching Salla's statements; Salla's MKT concerns land in batch 3.

### How I cut, and the grains

- **Discounts (CM-MKT-001) as a parent** of discount codes and coupons (002), automatic discounts and special offers (003) and discount functions (004). Shopify gives discounts one section (route discounts, SH-S-5150; section Discounts, SH-S-1522); Salla gives coupons and offers a link each (SA-S-1815, SA-S-1817) and one settings route for their priority (coupons/discount-priorities, SA-S-1712). Their groupings differ; the parent follows Shopify's, the anchor's shared reading being that coupons and offers are kinds of discount (Salla's bank offers, "نوع خصم جديد", SA-S-5028). SH-C-127 holds discount codes too, so it lands in the parent: a grain.
- **No Shopify statement held names automatic discounts** (searched in CM-MKT-003's cell). CM-MKT-003 is Salla's place of its own; batch 3 may find Shopify's cell should cite something I missed.
- **Marketing campaigns (CM-MKT-005)** is a parent of automations (006: Shopify's staff permission names automations under Marketing, SH-I-0936) and email and SMS campaigns (007: both platforms call them campaigns, a reading). Sales attribution (008) has no parent: no held statement puts Attribution under Campaigns, though both are Growth entries in Shopify's navigation (inventory only).
- **Capture customer leads** (Shopify's plan line, SH-I-1187) has no definition in any held statement, so it stays in CM-MKT-005 as shows, not a capability of its own. The same for Autopilot, which stays in CM-MKT-006.
- **Customer events and pixels (CM-MKT-009)** takes M-055's events and pixels; product feeds stay with domain E (SH-C-138). Salla's SA-C-074 holds both pixels and feeds, so batch 3 lands it here strained, or the feeds' statements go to domain E's model.
- **Advertising (CM-MKT-010)** is the parent of audiences (011) by Salla's grouping: the audience manager is a route of Salla Ads (SA-S-3572). Shop Campaigns (012) has no parent: Shopify's help puts it under the Shop sales channel (SH-S-0726's page), and no held statement groups it with advertising apps.
- **Affiliate and creator marketing (CM-MKT-013)** is the parent of store-run affiliate marketing (014) and influencer and creator marketing (015), by Salla's grouping: one dashboard app holds marketing/referrals, affiliates, experts, influencers and marketplace (SA-S-3550). Shopify Collabs does both children's things (SH-S-0731, SH-S-0732), so SH-C-134 lands in the parent.
- **SH-C-194 is two things**, advertising apps and affiliate program apps. It lands in CM-MKT-010 by its `where` (Advertising apps, SH-S-2573), strained, since its Affiliate program apps (SH-I-1812) are cited in CM-MKT-014. A reviewer may split the concern.

### Joins on role, and weak joins

- **CM-MKT-007, Shopify Messaging with Salla's SMS campaigns and communication apps.** Shopify sends its email and SMS campaigns with its own services (SH-S-7037, SH-S-7038, SH-S-0055); Salla's plan line names marketing campaigns by SMS and app notifications (SA-S-2010), and its campaigns are broadcast through communication apps (marketing.campaign.broadcast, SA-S-1673, cited under SA-C-075 and SA-C-200). A join on role, a reading (U-067, ruled joined for SA-C-200).
- **CM-MKT-011, Shopify Audiences with Salla Ads' audiences.** Rests on the term inside advertising on both platforms; no Salla statement defines its audiences. The weakest join in this batch: a reviewer may prefer Salla's audience statements in CM-MKT-010 and a none-held cell here.
- **CM-MKT-014 and CM-MKT-015** join on the terms affiliate and creators or influencers; neither platform defines them beyond the statements cited.

### Homonyms kept apart

- **Functions.** Shopify's Discount Function API (SH-C-128, apps' discount logic invoked by Shopify, SH-S-0683) against Salla's App Functions (SA-C-196/reason/SA-S-0187, serverless functions on store events, domain F). CM-MKT-004's Salla cell is none-held.
- **Affiliate programmes.** Salla's own affiliate programme for Salla (اتفاقية استخدام برنامج التسويق بالعمولة, SA-C-173/responsible/SA-S-0019, domain F) isn't the store's affiliate marketing (CM-MKT-014).
- **Campaigns.** Salla's Pre-order campaigns (SA-C-029/where/SA-S-1799, domain B) and influencers' Campaign Orders (SA-S-1922) aren't marketing campaigns (CM-MKT-005); Shopify's Shop Campaigns (CM-MKT-012) isn't its Campaigns section (CM-MKT-005).
- **Advertisements.** Salla's Advertisements (شريط إعلاني أعلى المتجر, SA-C-083, domain E) is a storefront announcement bar, not advertising on ad platforms (CM-MKT-010).
- **Marketing.** Salla's Marketing link opens /coupons (SA-S-1694), while Shopify's marketing route is its campaigns (SH-S-5176); both are cited in CM-MKT-005 as each platform's Marketing section, and Salla's link is a reading.

### Rulings, and those left for batch 3

- Ruled here: U-056 for SA-C-206's pairs (joined:CM-MKT-015 with SH-C-134; joined:CM-MKT-014 with SH-C-194), since SA-C-206 is domain F and no batch lands it; U-067 for SH-C-130's pairs (apart with SA-C-011; joined:CM-MKT-007 with SA-C-200). Batch 6 rules SH-C-150's pairs in U-067.
- **Left for batch 3, as my message says:** U-055, U-057, U-058, and U-056's pairs with SA-C-072 and SA-C-076. The checker prints the first three as problems until batch 3 rules them. What my cells imply, for batch 3 to test against its own cells:
  - U-058, SH-C-127 × SA-C-070: CM-MKT-002 cites SH-C-127/decides/SH-S-7042 and SA-C-070/decides/SA-S-2001: joined:CM-MKT-002.
  - U-057, SH-C-127 × SA-C-071: Shopify's Discounts are in CM-MKT-001 (SH-C-127/where/SH-S-5150), Salla's special offers in its child CM-MKT-003 (SA-C-071/where/SA-S-1817): nested:CM-MKT-003. SH-C-188 × SA-C-071: SH-C-188 is domain B and no cell here cites it: apart, unless batch 3 cites its upsell apps.
  - U-055, SH-C-132 × SA-C-073: joined:CM-MKT-011 (SH-C-132/decides/SH-S-7072; SA-C-073/decides/SA-S-2594). SH-C-133 × SA-C-073: apart (CM-MKT-012's Salla cell is none-held). SH-C-194 × SA-C-073: joined:CM-MKT-010 (SH-C-194/where/SH-S-2573; SA-C-073/where/SA-S-1812).
  - U-056, SH-C-134 × SA-C-072: joined:CM-MKT-014 (SH-C-134/decides/SH-S-0732; SA-C-072/where/SA-S-1821). SH-C-134 × SA-C-076: joined:CM-MKT-015 (SH-C-134/where/SH-S-0731; SA-C-076/where/SA-S-1816). SH-C-194 × SA-C-072: joined:CM-MKT-014 (SH-I-1812; SA-C-072/where/SA-S-1821). SH-C-194 × SA-C-076: apart.

### Match landings written as terms and identifier

- SH-C-129 (M-051) and SH-C-146 (M-055) land by `terms` and `identifier`, with keys of both sides, not by `match:`: the checker tests a match landing against the match's other concerns already landed, and their Salla concerns land in later batches. Each reading names the match. Batch 3 (and batch 5 for SA-C-092) can land the Salla side by `match:` once these are in place.

### For later batches

- **Batch 3** lands SA-C-070 to SA-C-076 and SA-C-080. Salla-only things found and not made capabilities here: Marketing calendar (link SA-S-1819, plan line SA-S-2013, released flag SA-S-3254), bank offers (SA-C-080, a kind of discount: CM-MKT-001 or a child), the plan line تسويق واسع عبر واتساب وتويتر وانستجرام وجوجل (SA-S-2151), Salla Ads' other dashboard apps (WhatsApp, app-notification ads, engage, smart campaigns, marketing credits), Salla's product feeds and google-site-verification in SA-C-074 (Shopify's feeds are domain E's SH-C-138), and the unreleased flag utm-campaign.
- **SA-C-074's pixels** are cited in CM-MKT-009 and **SA-C-092's events** too (SA-S-1164, SA-S-5149, SA-S-1082, SA-S-1083, SA-S-1341, SA-S-1343); whichever batch lands SA-C-092 lands it there by M-055, or reads it as strained.
- **SA-C-200's SA-S-1673** is cited in CM-MKT-007 (U-067 joined). If batch 6 lands SA-C-200 in a notifications capability, that landing reads it in another tree: strained.
- **SH-C-043/responsible/SH-S-0067** (batch 1's note): I cited SH-C-146's key for the same statement in CM-MKT-009, not SH-C-043's; the checker didn't flag SH-C-043's landing.

### Gaps that limit the cells

- Shopify: reason placements searched and not found for every concern of this batch; responsible stated only in general terms for SH-C-127, SH-C-129 and SH-C-131. No held statement defines Capture customer leads, marketing automations or Autopilot, how attribution credits orders, or what a discount code reduces. No statement names Shopify's company as maker of Shopify Audiences or of the "Shopify Messaging app" (SH-I-2056), so those cells rest on core.
- Salla: no statement defines Salla Ads' audiences, marketing credits (xio), engage or app-notification ads; who Sweply is isn't stated (SA-S-5133's own note); the makers of the apps behind the flags facebook-conversion, snapchat-conversion and tiktok-conversion aren't stated. No held statement names email marketing campaigns.

### What the checker flagged, answered

- **own-service on SH-S-7482 and SH-S-7478 (Shop Campaigns):** both are Shopify's own Shop Campaigns Merchant Terms. SH-S-7482 names Shopify as the one that determines eligible buyers and ads targeting; SH-S-7478 says the terms supplement the merchant's agreements "with Shopify". A reading that they name the company as provider of a separate service; a reviewer may hold that "Shopify" here names the platform, and move them to core or shows.
- **own-service on SH-S-2760 (three rows) and SH-S-7479 (Collabs):** SH-S-2760's scope names the Google Play publisher "Shopify Inc.", the company; SH-S-7479's Shopify Collabs Terms govern "the Shopify Collabs application" and supplement the merchant's agreements with Shopify. Both name the company, not only the brand.
- **none-held with matches:** CM-MKT-003 Shopify (the matches are other uses of "automatic" and "offers": payments, domains, apps' pricing); CM-MKT-004 Salla (the matches are coupons and offers, cited in CM-MKT-001 to 003, and abandoned-cart discount messages, SA-C-048, domain C; App Functions are the homonym above); CM-MKT-006 Salla (other uses of تلقائي: wallets, customer groups, order assignment, SEO, and the features named in the cell); CM-MKT-008 Salla (order and shipping assignment, إسناد, a homonym; reports of visit sources; the two flags named in the cell); CM-MKT-012 Salla (Salla Ads' undefined dashboard apps and the unreleased webengage flag, SA-C-194/decides/SA-S-3222, an app integration).
- **Remaining problems:** the three missing rulings, U-055, U-057 and U-058, left for batch 3 as my message says (above).

### Slot fillers

- CM-MKT-007, Shopify: SendGrid (SH-S-0054, its Email Services' provider) and Twilio (SH-S-0051, whose Acceptable Use Policy sets the SMS Services' terms).
- CM-MKT-010, Salla: the ad services its plan line names for linking the store (Google Ads, Snapchat, TikTok, Twitter, Facebook, Pinterest, AdRoll; SA-S-2149, plan سلة برو), and Sweply (SA-S-5135, the ads wallet for Salla Ads on Meta). That Sweply is a third party is a reading: who it is isn't stated, and a reviewer may drop the row.
