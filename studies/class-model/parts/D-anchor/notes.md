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

## Batch 3: MKT (marketing, discounts and promotions), Salla's concerns

Concerns landed: SA-C-032, SA-C-070, SA-C-071, SA-C-072, SA-C-073, SA-C-074, SA-C-075, SA-C-076, SA-C-080. Seven landed in batch 2's capabilities, two in new ones. Capabilities CM-MKT-016 to CM-MKT-021, with a Shopify cell for each. Evidence added to batch 2's Salla cells CM-MKT-002, 003, 005, 007, 009, 010, 011, 014 and 015, from my concerns' statements; their cells' readings are batch 2's and don't name the rows added, so each row's `why` says what it shows.

### Where each concern landed

- SA-C-070 Coupons in CM-MKT-002 (terms, with Shopify's discount codes); SA-C-071 Special and Promotional Offers in CM-MKT-003 (single: Shopify's cell is none-held); SA-C-072 Affiliate marketing in CM-MKT-014 (terms); SA-C-073 Salla Ads in CM-MKT-010 (role); SA-C-074 Pixels & feeds in CM-MKT-009 (M-055); SA-C-075 Campaigns and Marketing calendar in CM-MKT-005 (M-051); SA-C-076 Influencers in CM-MKT-015 (role).
- New: SA-C-032 in CM-MKT-016 (back-in-stock alerts, with Shopify's Stock alert apps); SA-C-080 in CM-MKT-018 (bank offers, Salla only).

### How I cut, and the grains

- **Back-in-stock alerts (016) and wishlist notifications (017)** are apart: Salla gives each a settings route of its own (products/notify_availability, SA-S-1754; products/wishlist-notifications, SA-S-1761), and Q1's M-080 joins only the back-in-stock side with WooCommerce. SA-C-032 lands in 016, its main subject and M-080's basis, strained for 017. The wishlist itself (SA-C-091's Wishlist API, Shopify's Wishlist apps in SH-C-187) isn't cited: it is for the LOY batch that lands SH-C-187, and for domain E.
- **Bank offers (018)** under CM-MKT-003, by Salla's grouping: its offers dashboard app holds offers, conditional, banks and cashback (SA-S-3589). Cashback is SA-C-063's (LOY) and isn't cited.
- **Marketing calendar (019)** under CM-MKT-005: SA-C-075 holds campaigns and the calendar together. The navigation list both links sit in holds every marketing link, so it doesn't decide the parent; a reading.
- **Ads wallet (020)** under CM-MKT-010: its permissions and its payment app are inside Salla Ads (/marketing/ads/payment). Salla Ads' other dashboard apps (YouTube, Meta, media, smart campaigns, tools, engage, WhatsApp, template, marketing credits / xio) aren't defined anywhere held, so they stay in CM-MKT-010 as core, not capabilities of their own; app notifications go to CM-MKT-007, whose Salla plan line names campaigns by app notifications (SA-S-2010). A reviewer may hold that WhatsApp ads (SA-S-3582) are messaging campaigns too.
- **Upsell and cross-sell (021)** has an App Store category on both (Shopify's Upsell and cross-sell apps, SH-I-1846, of SH-C-188; Salla's Cross/up sell, SA-S-1188), so it is a capability by the dry run's rule. No parent: nothing held puts it under offers or discounts. Shopify's parent category page, Upsell and bundle apps (SH-S-2604), is cited in domain B's CM-SEL-006 and not here.
- **Product feeds stay out of this model.** SA-C-074's feed flags (google-merchant-feed, facebook-catalog-feed, snapchat-catalog-feed) and google-site-verification aren't pixels, and Shopify's product feeds are SH-C-138, which scope.tsv gives domain E. SA-C-074 names E under also, so domain E's part may cite them. SA-C-074 lands strained.
- **SA-S-2151** (plan line تسويق واسع عبر واتساب وتويتر وانستجرام وجوجل): its title reads as broad marketing, but its description is a link or code for the affiliate marketer to share. The description governs (dry-run convention), so it is cited in CM-MKT-014, and SA-C-075 is strained for it.

### Joins on role, and weak joins

- **SA-C-073 with SH-C-194 (CM-MKT-010):** Salla Ads, Salla's own product for digital advertising campaigns (SA-S-0007), against Shopify's Advertising apps (SH-S-2573). The same role, advertising on ad platforms, done by the platform on Salla and by apps on Shopify.
- **SA-C-076 with SH-C-134 (CM-MKT-015):** Salla's influencers against Shopify Collabs' creators (SH-S-0731).
- **Weak:** SA-C-032 with Shopify's Stock alert apps rests on an inventory entry's name; CM-MKT-021 rests on two categories' names on both sides.

### Homonyms kept apart

- **Wallet.** Salla's ads wallet (CM-MKT-020, محفظة إعلانات, SA-S-5134, SA-S-5135) isn't its customer wallet (محفظة العميل, SA-C-063, LOY), and Shopify Balance (SH-C-088, domain C) is neither.
- **Campaign.** Salla's influencer Campaign Orders (SA-S-1922, SA-S-5137) are orders an influencer takes on, cited in CM-MKT-015, not marketing campaigns (CM-MKT-005); Salla Ads' campaign permissions (salla_ads_campaigns_*) are ad campaigns, cited in CM-MKT-010.
- **Bank.** Salla's bank offers (a discount, CM-MKT-018) against Shopify's banking statements (Shopify Balance, payouts, chargebacks; domain C).

### Rulings

- U-058: joined:CM-MKT-002. U-057: nested:CM-MKT-003 for SH-C-127 × SA-C-071; joined:CM-MKT-021 for SH-C-188 × SA-C-071. U-055: joined:CM-MKT-011 (SH-C-132), apart (SH-C-133), joined:CM-MKT-010 (SH-C-194). U-056: joined:CM-MKT-014 (SH-C-134 × SA-C-072 and SH-C-194 × SA-C-072), joined:CM-MKT-015 (SH-C-134 × SA-C-076), apart (SH-C-194 × SA-C-076). U-060: joined:CM-MKT-016 for SH-C-188 × SA-C-032. Each as batch 2's notes foresaw, but for U-057, whose SH-C-188 pair is joined, not apart, since CM-MKT-021 now cites its upsell apps.
- **Left for later:** U-060's pair SH-C-187 × SA-C-032, for the batch that lands SH-C-187 (LOY). What my cells give it: no capability here cites SH-C-187; its Wishlist apps (SH-I-1821) are named, not cited, in CM-MKT-017's Shopify cell. Apart, unless that batch's wishlist capability cites SA-C-032's wishlist notifications.

### Gaps that limit the cells

- Salla: no statement held defines its wishlist notifications, its marketing calendar, its Cross/up sell category, its ads wallet beyond SA-S-5134 and SA-S-5135, or Salla Ads' dashboard apps other than audiences. The makers of the apps behind the flags mailchimp-marketing, snapchat-conversion and tiktok-conversion aren't stated, so those flags are shows, as batch 2 did for facebook-conversion. Q1's gaps: responsible and reason not read for most of these concerns (page not read), so no cell here says who answers for coupons, offers, affiliates, pixels, campaigns or bank offers.
- Shopify: its Stock alert apps and Upsell and cross-sell apps are inventory entries only; no statement defines them.

### A correction for the reviewer

- Batch 2 cited SA-S-2565 and SA-S-2566 (coupon_browse, coupon_management) in CM-MKT-002, and SA-S-2592 and SA-S-2593 (salla_ads_campaigns_*) in CM-MKT-010, as core, with SA-S-2565's `why` reading "staff permission". Their notes say they are permissions "a partner can request on a merchant's store". By the dry run's convention the staff permission is core and the partner's shows an interface for apps. I added the staff permissions (SA-S-2348, 2349, 2375, 2376 and others) as core and didn't rewrite batch 2's rows; the reviewer may move those four to extension-point. The same may hold for SA-S-2571, 2572, 2577, 2578, 2589, 2590, 2594 and 2595, which I didn't check.

### What the checker flagged, answered

- **none-held with matches,** my cells: CM-MKT-017 Shopify (SH-I-1821, Wishlist apps, named in the cell: a wishlist, not notifications); CM-MKT-018 Shopify (Shopify Balance, Payments, payouts and payment-method statements of domain C, none a discount, named in the cell); CM-MKT-019 Shopify (calendar months in Shopify Credit's and partners' payment terms); CM-MKT-020 Shopify (Shop Campaigns' per-conversion charge, SH-S-0726, cited in CM-MKT-012: how Shopify charges, not a wallet).
- **CM-MKT-017 and CM-MKT-021 have no concern landed in their trees.** SA-C-032 lands in CM-MKT-016 (strained for 017); SA-C-071 lands in CM-MKT-003 (strained for 021), and SH-C-188, whose upsell apps 021 cites, is domain B's. Both are capabilities because a platform gives them a place of their own (a settings route; an App Store category on both). A reviewer may make them children, or land the concerns differently.
- The other flags (SA-C-122's statement, Shopify's own-service rows, batch 1's and batch 2's none-held cells, M-018) are earlier batches', answered in their sections.


## The coordinator's sweep of partner permissions (30 October)

- CM-MKT-002: SA-C-070/decides/SA-S-2565 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.
- CM-MKT-002: SA-C-070/decides/SA-S-2566 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.
- CM-MKT-003: SA-C-071/decides/SA-S-2571 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.
- CM-MKT-003: SA-C-071/decides/SA-S-2572 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.
- CM-MKT-005: SA-C-075/decides/SA-S-2567 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.
- CM-MKT-005: SA-C-075/decides/SA-S-2568 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.
- CM-MKT-010: SA-C-073/decides/SA-S-2592 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.
- CM-MKT-010: SA-C-073/decides/SA-S-2593 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.
- CM-MKT-011: SA-C-073/decides/SA-S-2594 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.
- CM-MKT-011: SA-C-073/decides/SA-S-2595 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.
- CM-MKT-014: SA-C-072/decides/SA-S-2577 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.
- CM-MKT-014: SA-C-072/decides/SA-S-2578 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.
- CM-MKT-015: SA-C-076/decides/SA-S-2589 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.
- CM-MKT-015: SA-C-076/decides/SA-S-2590 was `core`; it is a permission a partner can request (the statement's note), so `shows`, by the dry run's S7.

## Batch 4: LOY (loyalty, wallet and gifting)

Concerns landed: SH-C-025, SH-C-026, SH-C-082, SH-C-187, SA-C-063, SA-C-064, SA-C-077, SA-C-078. Capabilities CM-LOY-001 to CM-LOY-007, with both platforms' cells. LOY had no capabilities before this batch, so every concern landed in a new one; none joined an earlier batch's capability.

### Where each concern landed

- CM-LOY-001, store credit and customer wallet: SH-C-026 (role, with SA-C-063) and SA-C-063 (role; it holds the wallet, cashback and gift cards, so it lands in the parent).
- CM-LOY-002, gift cards: SH-C-025 (M-013).
- CM-LOY-004, loyalty programmes and rewards: SH-C-187 (M-075, strained), SA-C-064 (M-075), SH-C-082 Shop Cash (role, strained).
- CM-LOY-006, gifting: SA-C-077 (role, with Shopify's Gift wrap and message apps).
- CM-LOY-007, reorder reminders: SA-C-078 (single).
- No concern lands in CM-LOY-003 (cashback, a child of 001, in SA-C-063's tree) or CM-LOY-005 (wishlists).

### How I cut, and the grains

- **The wallet as parent (001) of gift cards (002) and cashback (003).** Salla puts gift cards in its customer wallet's settings (wallet/gift-card, SA-S-1767) and its wallet's notifications are Wallet & Cashback Notifications (SA-S-1768); it credits cashback to the customer's wallet and takes it back from there (SA-S-5019). Shopify's admin keeps gift cards a section of their own (gift_cards) and store credit in its Customers section, but its one Gift Card and Store Credit Terms govern both (SH-S-0676, SH-S-0677). The parent follows Salla's grouping, which Shopify's terms don't contradict; a reading. A reviewer may prefer gift cards with no parent, as batch 1 did for customer accounts: SA-C-063 would then land strained.
- **M-013 is a difference of grain:** SH-C-025 is gift cards alone, SA-C-063 the wallet with cashback and gift cards (the match's granularity note). SH-C-025 lands in the child by the match; SA-C-063 in the parent. Its cashback statements make the cashback child, since Salla gives cashback a plan line (عروض الكاش باك, SA-S-2007), a settings route (coupons/cashback-eligibility, SA-S-1713) and a path in its offers dashboard app (/marketing/cashback, SA-S-3589).
- **Cashback's parent** follows the wallet, not Salla's offers dashboard app, which holds offers, conditional offers, banks and cashback (SA-S-3589) and which batch 3 followed for bank offers (CM-MKT-018 under CM-MKT-003). A reviewer may move CM-LOY-003 under CM-MKT-003; SA-S-5019 and SA-S-1768 are why I didn't.
- **Salla's sub-settings stay in their capability:** the wallet's Maximum Credit Usage Limit and notifications, the loyalty program's Program details, Points settings, Rewards banner and Markets, and the gifting system's Selected markets, Product type customization and Messages & cards customization each configure the one thing they sit in, so none is a capability of its own (batch 1's reading of plan lines, applied to settings routes).
- **SH-C-187 is three things:** loyalty and reward apps (CM-LOY-004), wishlist apps (CM-LOY-005) and donation apps (domain B's CM-SEL-007, which already cites SH-S-2583; scope.tsv names B under also for it). It lands in 004 by M-075, strained. No statement shows Shopify putting Wishlist apps under Customer loyalty apps, so 005 has no parent.
- **Wishlists (005)** are a capability because Shopify gives them an App Store category (SH-I-1821). Its area is LOY, where its only landed concern's other parts sit, a reading; domain E's model may hold the storefront's wishlist through SA-C-091 (the Twilight SDK), and the coordinator may move it there. Batch 3's CM-MKT-017 (wishlist notifications) may become a child of 005: both cite SA-S-1761 (flagged below).
- **Shop Cash (SH-C-082)** has a help page and a help-center section but no admin route, API group, plan line or app category, so it isn't a capability (the dry run's rule). It lands in 004 on role: "a Shopify-funded rewards program for Shop app customers" (SH-S-0437). Strained: it is Shopify's own programme across the Shop app (SH-C-136, domain E), not a store's, and nothing held says what its rewards are. A reviewer may hold that it belongs to domain E with the Shop app, or to CM-LOY-003 as cash back; no held statement says it is credited as cash.
- **Donations** aren't a capability here: domain B's CM-SEL-007 holds them, citing SH-C-187's Donation apps and SA-C-020's quick donation. U-082 is ruled apart here for that reason.

### Joins on role, and weak joins

- **CM-LOY-001, Shopify store credit with Salla's customer wallet** (U-004, joined). Shopify's store credit is a payment method on an order (SH-C-018/decides/SH-S-0275) with a balance staff can edit (SH-S-5147, SH-S-7086); Salla's wallet has a Maximum Credit Usage Limit (SA-S-1766), a deposit operation (SA-S-0183), cashback credited to it (SA-S-5019) and is listed as a payment method, customer_wallet (SA-I-1694). Both a balance the store holds for a buyer, who pays with it. Q1 asked for a Salla statement defining the wallet as credit for future purchases; none is held, so the join rests on these.
- **CM-LOY-004, Shop Cash with Salla's loyalty rewards:** above.
- **CM-LOY-006, Salla's gifting with Shopify's Gift wrap and message apps** (SH-I-1824): rests on the category's name against Salla's Messages & cards customization (SA-S-1729) and its gift order event (SA-S-1663). The weakest join in this batch.
- **CM-LOY-005** rests on the term wishlist on both sides; neither defines it beyond Salla's events ("Customer adds a product to wishlist", SA-S-1387).

### Homonyms kept apart

- **Wallet.** Salla's customer wallet (محفظة العميل, CM-LOY-001) against its store wallet (Wallet, /payments/wallet; محفظة متجرك, SA-C-005, Salla's billing of the merchant, domain A) and its ads wallet (CM-MKT-020); Shopify Balance (SH-C-088) is the merchant's money too. Salla's Apple Wallet order tracking (SA-S-1995, SA-C-040) is Apple's wallet.
- **Gift.** Gift cards (CM-LOY-002, stored value) against gifting (CM-LOY-006, a product bought for someone else). Shopify's App Store categories Gift apps and Gifts - Other (SH-I-1822, SH-I-1825, placed in SH-C-025) don't say which they hold and aren't cited. Shopify Collabs' gifts (SH-S-0732) are a business's gifts to its creators (CM-MKT-014). Salla's flag salla-policies-free-shipping-gift (SA-S-3049, domain C) is a shipping policy.
- **Reward.** Salla's مكافأة الراجحي (SA-S-1966, SA-C-119, a payment method, domain C), Shopify Balance's rewards (SH-S-5058) and the Cryptocurrency Credit Reward Program (SH-I-1368) aren't a store's rewards to its buyers; Shopify Credit's card cash back (SH-S-7064) isn't cashback to buyers.
- **Reorder.** Salla's Reorder setting (orders/reorder, SA-S-1746, flag order-reorder, SA-C-040, domain C) lets a buyer repeat an order; its reorder reminders (CM-LOY-007) remind a buyer. Shopify's payment customization reorders payment methods (SH-S-0589), and its target admin.product-details.reorder.render (SH-I-1509) is undefined.
- **Points.** Salla Point (سلة بوينت, SA-S-2094, SA-C-095) is point of sale, not loyalty points.

### Strained fits

- SH-C-187 in CM-LOY-004: its Wishlist apps (SH-I-1821) are cited in CM-LOY-005, and its Donation apps (SH-S-2583) in domain B's CM-SEL-007.
- SH-C-082 in CM-LOY-004: Shopify's programme for the Shop app's buyers, not a store's loyalty programme (above).
- Not marked strained, for the reviewer: SH-C-025's terms (SH-S-0676 to SH-S-0678) are cited under SH-C-026's keys in CM-LOY-001, its parent, so in its tree.

### Rulings

- U-004: joined:CM-LOY-001 (SH-C-026 × SA-C-063).
- U-059: apart for SH-C-188 × SA-C-077 (none of SH-C-188's statements or entries names gifts); joined:CM-LOY-006 for SH-C-189 × SA-C-077. **For the coordinator:** SH-I-1824, Gift wrap and message apps, is an entry Q1 placed in SH-C-189, which scope.tsv gives domain B without naming D. The brief says such a pair is apart, and also that a ruling follows the cells and no statement is left uncited to keep a ruling apart. The checker reads the cells, so I ruled joined; the coordinator may instead drop SH-I-1824 from CM-LOY-006 (Shopify's cell would be none-held) and rule apart, or add D to SH-C-189's `also`. I first read SH-I-1824 as SH-C-188's; my rows now name SH-C-189.
- U-060: joined:CM-LOY-005 for SH-C-187 × SA-C-032, the pair batch 3 left. CM-LOY-005 cites Shopify's Wishlist apps (SH-I-1821) and Salla's settings route Wishlist Notifications (SA-S-1761) as naming the wishlist. Batch 3 foresaw this ("apart, unless that batch's wishlist capability cites SA-C-032's wishlist notifications").
- U-078: joined:CM-LOY-004 (SH-C-187 × SA-C-064). WC-C-105's pairs are the WooCommerce part's.
- U-082: apart (SH-C-187 × SA-C-020): donations are domain B's CM-SEL-007, where B-anchor ruled the candidate joined.

### For the coordinator: earlier batches' rows

- **CM-MKT-017's Shopify cell** (batch 3) names Wishlist apps (SH-I-1821) as found and not cited, "the batch that lands SH-C-187 places it": it is now cited in CM-LOY-005. That cell still holds: wishlist apps aren't notifications.
- **CM-MKT-017's Salla reading** says Salla's wishlist itself (SA-C-091, SA-C-092, SA-C-196, SA-C-220) isn't cited there; CM-LOY-005 now cites SA-C-091's Wishlist API folder and SA-C-092's Product Added to Wishlist. SA-S-1761 is cited in both 017 and 005, so the checker asks whether one is the other's parent: I'd make CM-MKT-017 a child of CM-LOY-005 (a notification about the wishlist), a reading; the move is the coordinator's.
- **SA-C-032's landing** (batch 3, CM-MKT-016, strained for 017) is now also cited in CM-LOY-005; its reading could name that tree too.
- **Batch 3's note on bank offers** says cashback is SA-C-063's and isn't cited; CM-LOY-003 now cites the same dashboard app (SA-S-3589) under SA-C-063's key, for /marketing/cashback.

### Concerns read under `also`, and other domains' statements

- SH-C-188 (domain B, names D): read for U-059; nothing cited.
- SA-C-020 (domain B, names D): read for U-082; nothing cited (domain B cites its donation statements).
- SA-C-092 (domain D, batch 5): SA-S-1387, Product Added to Wishlist, cited as shows in CM-LOY-005. If batch 5 lands SA-C-092 in CM-MKT-009 by M-055, that landing reads it in another tree: strained.
- SA-C-032 (domain D, batch 3): SA-S-1761 cited as shows in CM-LOY-005.
- SH-C-018 (domain A, doesn't name D): SH-S-0275, store credit or gift cards as a payment method on an order, cited as shows in CM-LOY-001, because it is the only held statement that says store credit pays for an order. Flagged.
- SA-C-091 (domain E, doesn't name D): SA-S-1140, the Twilight SDK's Wishlist API folder, cited as core in CM-LOY-005, because it is the only place of its own Salla gives the wishlist. Flagged. If domain E cites it as core too, the merge flags it, and one of the two should move it to shows.
- SH-C-189 (domain B, doesn't name D): SH-I-1824, cited as extension-point in CM-LOY-006 (above). Flagged.
- Not cited: Salla's storefront components for the wallet, gift card redeem, cashback banner and loyalty (salla-wallet, salla-gift-card-redeem, salla-cashback-banner, salla-loyalty and others, SA-C-091, domain E); Salla's wishlist reports (report_customers_wishlist, customer-wishlists-reports, SA-C-220, ANL, batch 5) and App Functions' wishlist events (SA-C-196, F); Shopify's notification templates Store credit, Store credit issued and Gift cards (SH-I-2013, SH-I-2014, SH-I-2010) and its checkout target Checkout::GiftCard::Render (SH-I-1603), which aren't placed in my concerns: batch 6 (NTF) may cite the templates; SA-C-200's copies of SA-S-1663 and SA-S-1672 (batch 6), which I cite under SA-C-077's and SA-C-078's keys.

### Gaps that limit the cells

- Salla: responsible not read for SA-C-063, SA-C-064, SA-C-077 and SA-C-078, and reason not read for SA-C-064 and SA-C-077 (Q1 gaps), so no cell says who answers for the wallet, loyalty, gifting or reminders. No statement held defines the wallet as credit, how cashback or points are earned or spent, gift cards beyond their settings route, or what a gift order holds. **Maker gap:** the deposit operation needs "the Customer Wallet application installed" (SA-S-0183), an application on apps.salla.sa whose maker no statement names; the cell cites it as shows, and own-service or extension-point can't be claimed. The plan lines محفظة العميل and نظام ولاء العملاء carry "*برسوم إضافية" (extra charge) on plan سلة بلس, with no amount stated.
- Shopify: reason searched, not found for SH-C-025, SH-C-026, SH-C-082 and SH-C-187; Shop Cash's boundary searched, not found. No statement defines a loyalty programme, a wishlist or gift wrap and messages beyond the App Store categories' names, or says how a store takes part in Shop Cash. No statement names Shopify's company as the maker of anything here except, as a reading, Shop Cash's funding.
- No qualities or slot fillers: no statement names a third party or a law doing or setting the terms of a LOY capability. Shopify's "Applicable Laws" (SH-S-0677, escrow where required) names no law.

### What the checker flagged, answered

- **own-service on SH-C-082/where/SH-S-0437:** "Shopify-funded" names Shopify as the funder of a programme for the Shop app's customers, a separate product; a reading. A reviewer may hold that it names the platform, and move it to core.
- **Statements of other domains** (SH-S-0275, SA-S-1140, SH-I-1824): answered above.
- **CM-LOY-005, Salla, core rests only on boundary statements:** the one core row is the Wishlist API folder of Salla's own Twilight SDK, the storefront's SDK, which I read as Salla's own API for its own feature (the dry run's convention). A reviewer may move it to shows, leaving the cell with shows only.
- **SA-S-1761 in two trees** (CM-LOY-005 and CM-MKT-017): answered above; one should be the other's parent.
- **CM-LOY-005 has no concern landed in its tree:** SH-C-187 lands in CM-LOY-004, and SA-C-091 is domain E's. It is a capability because Shopify gives it an App Store category.
- **none-held with matches:** CM-LOY-003 Shopify (Shop Cash, cited in 004; Shopify Balance's rewards, the crypto credit reward terms and Shopify Credit's cash back, the merchant's own; Loyalty and reward apps, cited in 004; each named in the cell); CM-LOY-007 Shopify (payment customization, the undefined admin target, the payment reminder template; named in the cell).
- The other flags are earlier batches', answered in their sections.

- **After batch 4 (the coordinator):** CM-MKT-017, wishlist notifications, is now a child of CM-LOY-005, wishlists. `scope.tsv` names D under SH-C-189's `also`, so U-059's SH-C-189 pair stays `joined:CM-LOY-006` on the evidence.
