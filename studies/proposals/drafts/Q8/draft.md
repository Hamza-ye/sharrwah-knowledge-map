# Q8: How the platform organizes what it offers, and how that grows, a draft proposal

## 1. How the platforms handle it

### [1]

- Shopify's Terms call all it offers the "Service(s)", and "Any new features or tools which are added to the current Services will also be subject to the Terms of Service". BigCommerce's agreement defines "Services" as "all products, services, and materials offered by Commerce or its Affiliates". Same term (basis 1; official pages). Q8-SH-054; Q8-BC-018
- Four grow by plan. Shopify has "several plans to help your business grow at every stage"; on Salla "تختلف باقات سلة لتناسب مراحل نمو متجرك"; Zid's merchants "start on a free-forever plan and upgrade as they grow"; on BigCommerce "moving into a higher-tier plan comes with access to additional features". They match on role, plans a store moves up as it grows (basis 4; BigCommerce's an official page, the others stated). Q8-SH-001; Q8-SA-001; Q8-ZD-001; Q8-BC-002
- WooCommerce grows through extensions: "Grow your business with hundreds of free and paid extensions". Q8-WC-042
- Shopify gathers what is new as Editions, "150+ updates to Shopify, twice a year". One Salla store's تحديثات المنصة page showed updates "حسب التصنيفات المحددة" (store real-merchant, observed 12 October 2026). Q8-SH-064; Q8-SA-038

### [2]

- Plans fix numbers. Shopify's pricing table gives additional staff accounts as "Not included", 5, 15 and "Unlimited" by plan; in one plan-choice step's saved markup on store capture-plus (observed 2 October 2026), Grow holds "Everything in Basic" and "Up to 5 staff accounts", Advanced "Everything in Grow" and "Up to 15 staff accounts". One Salla store's answer gave each plan a `features_count` (store merchant@en, observed 9 October 2026). Same role (basis 4; mixed kinds: Shopify's an official page and observed, Salla's observed). Q8-SH-K2743; Q8-SH-107; Q8-SA-K0055
- Units are sold on top of a plan. One Salla store's answer (store real-merchant, plan Pro, observed 12 October 2026) listed "Warehouses & branches" and "Staff accounts", each with `type` "addon". Zid's الإضافات let a merchant buy "ميزات جديدة". BigCommerce sells added storefronts by plan, as "Add storefront $30/mo (max. 3)". Same role (basis 4; mixed kinds: Salla's observed, Zid's stated, BigCommerce's an official page). Q8-SA-043; Q8-ZD-009; Q8-BC-K0217
- Some units carry terms of their own. Shopify's "Additional Services" may be subject to "Additional Service Terms"; BigCommerce adds "additional guidelines or rules applicable to such Services or features"; Zid's زد باي has terms that form the contract "بين مستخدمي زد باي وشركة زد". Same role (basis 4; official pages). Q8-SH-058; Q8-BC-024; Q8-ZD-K0009
- On BigCommerce a provider's service can be the platform's own: "an Extension is a Service and is not a Third-Party Product". Q8-BC-K0457
- Shopify's admin routes, in shipped code, open on conditions named "entitlements", "regions", "betas", "plans", "features", "permissions" and "organizationFeatures", combined as alternatives ("oneOf") and exclusions ("excluded"). Q8-SH-K0041; Q8-SH-K0175; Q8-SH-K0191
- Entitlement values come in a store's own answer: the admin answers of six trial stores (2jiwxs-gr, ctcbwa-r1, fake-demo-sharrwah, ibx5bt-xy, ts15uk-ug and zyd38b-ze, observed 21 September 2026) each gave `maximumLocations` 2. Q8-SH-K2591
- One Salla store's dashboard answer (store merchant@en, observed 9 October 2026) gave each feature setting `enabled`, `released`, `plans`, `countries` and `type`, "feature" or "app". `multi-countries` names plans special and pro, with `limit` 10. Q8-SA-K1973; Q8-SA-K2105
- WooCommerce's shipped FeaturesController defines "the WooCommerce features that can be enabled and disabled by admin users". Q8-WC-K1310
- Shopify's "plans" and Salla's `plans` are the same identifier, the store's plan (basis 2); Shopify's "regions" and Salla's `countries` fill one role, the place (basis 4). Kinds: Shopify's shipped, Salla's observed. Q8-SH-K0175; Q8-SH-K0041; Q8-SA-K1973
- Named conditions of this kind were not in what was read on Zid or BigCommerce. Q8-ZD-N03; Q8-BC-N05
- Shopify Plus expansion stores are "additional .myshopify.com stores that fall under the same organization and contract", with "centralized organization-level management for users and billing". Q8-SH-046
- One Salla store's قائمة المتاجر (store merchant, observed 8 October 2026) let a user move between stores "دون الحاجة لتسجيل الدخول في كل مرة", each with its own الباقة. BigCommerce's "Account-level API credentials provide direct access to all the account's stores". Q8-SA-050; Q8-BC-K0292
- A Shopify sales channel app "connects a merchant's online store to surfaces outside Shopify", and "Each sales channel connects to your Shopify admin"; on BigCommerce "A channel is anywhere a merchant sells their products". Same role (basis 4). Q8-SH-K2063; Q8-SH-014; Q8-BC-K0209
- Within one store, Shopify's Markets vary the store "based on their location, customer group, retail location, or sales channel"; Salla's الأسواق المتعددة make copies of a store "لكل دولة تستهدفها أو منطقة أو مدينة"; أسواق زد set products and prices per market "من متجر واحد". Same role (basis 4). Q8-SH-K1930; Q8-SA-K1976; Q8-ZD-026
- Shopify's apps are public, "listed and unlisted", or custom, built "exclusively for your Shopify store". Zid's Private apps install only "by stores explicitly granted access". Salla's apps are "من تطوير سلة أو مطور آخر من مجتمع تطوير سلة". Q8-SH-029; Q8-SH-033; Q8-ZD-K0400; Q8-SA-018
- Shopify's custom apps and Zid's Private apps fill one role, an app for named stores only (basis 4). Shopify's unlisted public apps and BigCommerce's Unlisted apps, "submitted and approved but not listed", share the term (basis 1). Q8-SH-029; Q8-ZD-K0400; Q8-BC-075
- On Shopify "An app extension isn't an app" but adds features to defined parts of Shopify's interfaces. Its table of app extensions, by area, marks some, the payments extension among them, as needing review and approval. Q8-SH-081; Q8-SH-085; Q8-SH-095
- Salla's apps add to its dashboard through the Embedded SDK, to merchant stores through App Snippets, and to "the lifecycle of merchant and customer activities" through App Functions. Q8-SA-K2243; Q8-SA-K2253; Q8-SA-030
- Zid's embedded apps open in the dashboard "through an iframe"; places an app can add to beyond that were not in what was read. Q8-ZD-K0388; Q8-ZD-N12
- A BigCommerce checkout extension "is a web app hosted outside of BigCommerce" that extends a checkout step; the Tax Provider API can "integrate a tax calculation engine". Q8-BC-042; Q8-BC-077
- WooCommerce's payment gateways "are class based and can be added through traditional plugins", loaded through the `woocommerce_payment_gateways` filter in shipped code; plugins add shipping rates through a "Shipping Method API". Q8-WC-K0006; Q8-WC-K0014; Q8-WC-K0856
- Shopify's Functions, which "customize your store's backend logic", and Salla's App Functions fill one role (basis 4; both stated). Q8-SH-040; Q8-SA-030
- WooCommerce's Marketplace offers "Discover Extensions Themes Business services"; BigCommerce's App Marketplace, "Apps & Integrations Themes Partner Services". Both use the term Themes (basis 1). Q8-WC-038; Q8-BC-045
- Salla's partners' terms define a service provider as "الشريك الذي يقدم خدماته لتجار سلة من خلال منصة الشركاء". Q8-SA-K2364
- Two list their own units beside partners'. Shopify's App Store has pages for built-in features, as B2B, "Included with Shopify Plus"; WooCommerce groups products "crafted by WooCommerce". Same role (basis 4; both stated). Q8-SH-K2696; Q8-WC-040

### [3]

- A WooCommerce extension declares the version it needs ("WC requires at least") and its compatibility with features through `declare_compatibility`. Q8-WC-032; Q8-WC-K1272
- Zid's financing service needs "تفعيل واعتماد زد باي", and turning زد باي on disables other gateways "باستثناء تمارا و تابي". Q8-ZD-K0178; Q8-ZD-K0089
- Shopify's expansion stores "don't share data by default"; أسواق زد keep markets in one store, "بدون الحاجة لمتاجر منفصلة". Q8-SH-047; Q8-ZD-026
- In one step's saved markup on store capture-grow (observed 2 October 2026), once on Shopify's Plus plan after its trial, the store "will move out of the My Store organization into a new organization", carrying over its "payment method and user roles". Q8-SH-109
- All five set a third party's unit apart under that party's terms. Shopify's Third Party Services are "solely between you and" their provider; WooCommerce's "Extensions may have their own requirements"; Salla's third-party services have "أحكامها المستقلة التي تتم بين التاجر وبين الطرف الثالث"; on Zid "الشريك هو المقدم للخدمة"; BigCommerce's Third-Party Products "are governed by their own terms of service". Same role (basis 4; all official pages). Q8-SH-K2169; Q8-WC-K0830; Q8-SA-035; Q8-ZD-K0366; Q8-BC-K0453
- WooCommerce grows its core by merging packages into it: once a package is merged, "the feature plugin is disabled" (shipped). Not checked on Zid. Q8-WC-007
- App makers join under an agreement. Shopify's register "for a Partner Account" under the "Partner Program Agreement"; Zid's sign a partnership agreement; BigCommerce's sign "the Commerce Partner Agreement". Same role (basis 4; mixed kinds: Shopify's an official page, the others stated). Q8-SH-K2183; Q8-ZD-018; Q8-BC-062
- Apps are reviewed. Shopify's public apps "undergo Shopify's app review process"; WooCommerce's review runs from "Business review" to "Launch preparations"; on BigCommerce "The Marketplace team reviews all app submissions". Same role (basis 4). Q8-SH-029; Q8-WC-071; Q8-BC-K0316
- Payment integrations are held apart. Shopify's payments extension needs review and approval; WooCommerce requires "a separate agreement" for a "Payments Solution"; BigCommerce has "paused all new externally built payment integrations"; Zid Payments assigns a provider's ID "upfront before starting the integration". Same role (basis 4; all stated). Q8-SH-095; Q8-WC-K0353; Q8-BC-058; Q8-ZD-K0079
- App charges go through the platform. On Shopify "Most app charges are billed through Shopify"; on Zid "Any required app-plan payment is completed through Zid before activation becomes available"; BigCommerce's partners have "appointed Commerce as agent for the collection and disbursement of monies". Same role (basis 4; mixed kinds: BigCommerce's an official page, the others stated). Q8-SH-030; Q8-ZD-K0167; Q8-BC-K0168
  - Salla pays developers after "عادة 15 يومًا" (official page); WooCommerce pays a vendor "70% of the Product Net Revenue" (stated). Q8-SA-K2146; Q8-WC-K0461
- A Zid app's plans are each "Recurring" or "Usage-Based". Q8-ZD-014
- Shopify releases API versions every three months, each working for a year; deprecations are "announced in the developer changelog", and an app still using unsupported resources is "delisted from the Shopify App Store". Q8-SH-036; Q8-SH-069; Q8-SH-070
- On Salla "APIs should only be versioned up when a breaking change occurs", under "URI versioning". Q8-SA-K2318; Q8-SA-K2321
- Plans set features in tables. Shopify lists bot protection for Plus only; Salla turns on electronic payment from its second plan; Zid gives "Advanced Payment Methods" from its second. Same role (basis 4; mixed kinds: Shopify's an official page, Salla's stated, Zid's shipped). Q8-SH-K2812; Q8-SA-007; Q8-ZD-K0097
- Plans gate other units. Shopify's sales channel eligibility "will be based on your plan as well as other requirements", and Custom Level 2 PII apps need "the Grow plan or higher". A Zid private app needs "a Professional or Enterprise plan subscription", or API Access activated. Same role (basis 4; all stated). Q8-SH-015; Q8-SH-035; Q8-ZD-K0394
- Three platforms change plans in different ways. Zid may change its "خطط الاشتراك" with at least seven days' notice, and a lower plan loses the higher's features. Salla returns a lapsed store to the settings of its plan البيسك. On BigCommerce, past a GMV threshold "your plan is automatically upgraded". Q8-ZD-K0157; Q8-ZD-008; Q8-SA-033; Q8-BC-009
- Shopify's Terms say "Not all Services or features will be available to all Merchants at all times". Q8-SH-055
- Shopify's "Contracting Party" is set "based on the billing address of your Store". BigCommerce's "Contracting Entity" comes from a table of jurisdictions, and its Jurisdiction-Specific Terms "supplement, replace or modify" its terms for customers domiciled there. Same role (basis 4; official pages); what sets the place differs. Q8-SH-K1243; Q8-BC-025; Q8-BC-030
- WooCommerce's shipped code keeps "The payment extension list for each country", in which "The order is important as it will be used to determine the priority of the suggestions". Q8-WC-K0054; Q8-WC-K0055
- One Salla store's set-up said "اختيارك للدولة يحدِّد المتطلبات القانونية اللازمة لمتجرك", asking for the country that issues the merchant's documents (store Store 1, observed 8 October 2026). One Salla store's feature settings carry `countries`, empty in those copied, and an `apps-country-filter` (store merchant@en, observed 9 October 2026). Q8-SA-051; Q8-SA-K2126
- Shopify may invite merchants to "pre-release or beta features that are in development and not yet available to all merchants", which "are not part of the Services"; the additional terms they may carry were not in what was read. Q8-SH-060; Q8-SH-061; Q8-SH-N01
- One step's saved markup on store capture-grow (observed 2 October 2026) marks Shopify's Campaign Autopilot "Early access", without calling it a Beta Service. Q8-SH-111
- BigCommerce's "Pre-release Services" are "pre-release, early access, trial, or beta features, products, or functionality as part of the Services that are not yet generally available". The definitions match in part (basis 3; both quoted, both official pages), and differ on whether these are part of the Services. Q8-BC-028; Q8-SH-061
- In WooCommerce's shipped feature definitions, `is_experimental` puts a feature under "Experimental" and "Defaults to true"; `enabled_by_default` makes it "opt-out instead of opt-in"; `deprecated_since` forces its value. Q8-WC-012; Q8-WC-011; Q8-WC-013
  - One feature is "Hidden while incomplete so it can't ship merchant-toggleable". When, or by what steps, a feature moves between these states was not in what was read. Q8-WC-025; Q8-WC-N02
- In one Salla store's answer `enable-special-plan-purchase` had `enabled` true and `released` false (store merchant@en, observed 9 October 2026). Q8-SA-K0052
- BigCommerce's closed betas "are not available by default". Q8-BC-K0064
- Shopify's feature test drives let a Plus organization "activate upcoming Shopify features on specific stores", with "auto-release timelines". Its feature previews open on dev stores: "Only one feature preview may be enabled on a dev store". Q8-SH-043; Q8-SH-044; Q8-SH-073
- One step's saved markup on Shopify's Create a dev store page of organization 238086467 (the run names no store; observed 30 September 2026) holds Basic, Grow, Advanced and Plus as options of a "Shopify plan" field to "Preview plan-specific features". Q8-SH-108
- Shopify's dev stores "can't process transactions"; Salla's developers may make "متاجر تجريبية مجانية بحد أقصى ١٠ متاجر" (a help article one partner session showed on 8 October 2026); Zid's partners "test them on demo stores". Same role (basis 4; Salla's observed, the others stated). Q8-SH-051; Q8-SA-K2405; Q8-ZD-011
- WooCommerce's betas are "Meant to be used by plugin authors and early adopters"; Shopify publishes an API release candidate with each stable version. Q8-WC-056; Q8-SH-068

## 2. Proposed: names, structure and behaviour

- **Offer catalogue**: Sharrwah would keep one catalogue of every unit it offers sellers. Each **Offer** has a kind, a maker (Sharrwah or a named partner), the terms it falls under, the offers it needs, an **Availability rule** and a **Release stage**; Sharrwah's terms would cover offers added later. Q8-SH-054; Q8-BC-018
  - It takes one term for all offers, Shopify's and BigCommerce's "Services", and features and apps under one set of fields in one Salla store's answer (store merchant@en, observed 9 October 2026). Q8-SH-054; Q8-SA-K2105
  - Why: each place is set up as data in one catalogue, not built apart (rule 1); a new offer is an entry that changes no other part (rule 2); which terms cover later offers is legal structure, decided now (rule 3). Q8-SH-054; Q8-BC-018
  - Alternative not taken: separate mechanisms for features and for partners' units, as WooCommerce's features class and its Marketplace; one catalogue lets plan, place and stage gate every kind alike (rule 1). Q8-WC-K1310; Q8-WC-038
- **Offer kinds**: a **Feature**, built into Sharrwah; an **Additional service**, Sharrwah's own with terms of its own, which a provider may run; an **App**, **Theme** or **Partner service**, a partner's under the partner's terms; a **Sales channel**, a surface outside the store tied to its admin; a **Market**, a place's set-up within one store. Q8-SH-058; Q8-ZD-K0366; Q8-SH-014; Q8-ZD-026
  - A provider's offer may be Sharrwah's own, as BigCommerce's Extension is a Service, or the provider's, as Shopify's Third Party Services are. The kind decides who answers to the merchant, so it is fixed per offer now (rule 3). Q8-BC-K0457; Q8-SH-K2169
  - Where an offer would hold sellers' money, such as a payment service or a balance a seller tops up, the catalogue can list it as an **Additional service**, and it goes live only by the founder's decision. Q8-ZD-K0130
- **Entitlement**: a value each store holds, on or off or a number, from its plan, add-ons and place; offers test entitlements, never a plan's name. Q8-SH-K2591; Q8-SH-K0041
  - It takes Shopify's entitlement values in trial stores' answers (observed 21 September 2026), read by route conditions (shipped), and `limit` on a setting in one Salla store's answer (store merchant@en, observed 9 October 2026). Q8-SH-K2591; Q8-SH-K0041; Q8-SA-K1973
  - Alternative not taken: naming plans in each offer, as the `plans` on one Salla store's settings (observed 9 October 2026) and Shopify's "plans" condition do. A new or renamed plan would then change every offer naming it (rule 2). Q8-SA-K1973; Q8-SH-K0175
- **Availability rule**: on each offer, the conditions a store must meet: entitlements, place, release stage, staff permission, and the offers it needs. They combine as alternatives and exclusions, per store, or per account for account offers. The admin shows, and the API allows, only what the rule opens. Q8-SH-K0175; Q8-SA-K1973
  - It takes Shopify's condition types, alternatives, exclusions and organization conditions (shipped), and, from one Salla store's answer (store merchant@en, observed 9 October 2026), `countries` on each setting and `released` apart from `enabled`. Q8-SH-K0191; Q8-SA-K0052
  - Needs between offers become conditions, as Zid's financing needs زد باي, and زد باي turns other gateways off. Q8-ZD-K0178; Q8-ZD-K0089
  - The merchant's own switch, as WooCommerce's features "can be enabled and disabled by admin users", is one of the rule's conditions, where it lets the merchant choose (rule 1). Q8-WC-K1310
- **Plan**: a named, priced set of entitlements. A store holds one at a time, chosen and changed by the merchant; Sharrwah defines plans and their contents and may change them with notice. Q8-ZD-001; Q8-ZD-K0157
  - Per store, as one Salla store's list of stores gave each its own الباقة (store merchant, observed 8 October 2026). Q8-SA-050
  - When a paid plan lapses, the store falls to the lowest plan's entitlements (Salla), and offers above the new plan stop (Zid). Q8-SA-033; Q8-ZD-008
  - Alternative not taken now: BigCommerce's automatic upgrade by sales volume, kept open (section 5; rule 4). Q8-BC-009
- **Add-on**: an entitlement a store buys on top of its plan, a higher number or an offer the plan lacks, as the `addon` entries in one Salla store's answer (store real-merchant, observed 12 October 2026), Zid's الإضافات and BigCommerce's added storefronts. It changes no offer (rule 2). Q8-SA-043; Q8-ZD-009; Q8-BC-K0217
- **Release stage**: each offer is hidden (built, not switchable), preview (by invitation, on request or on test stores, marked as such, under preview terms), released (opt-in, or on by default with opt-out), or retired (held at one value, then removed). The stage is a condition of the rule, and moving an offer is a catalogue change, so code ships behind it (rule 2). Q8-WC-025; Q8-WC-011; Q8-WC-013; Q8-SH-111
  - It takes WooCommerce's states (shipped) and `released` in one Salla store's answer (store merchant@en, observed 9 October 2026), and for preview Shopify's invitations and BigCommerce's closed betas. Q8-SA-K0052; Q8-SH-060; Q8-BC-K0064
  - Whether preview offers fall inside Sharrwah's services, as on BigCommerce, or outside, as on Shopify, is a company decision (section 7). Q8-SH-061; Q8-BC-028
  - Alternative not taken now: Shopify's test drives, a Plus organization's early switch-on with an auto-release date; the stage allows it later (rule 4). Q8-SH-043; Q8-SH-044
  - When an offer moves stage is Sharrwah's call; WooCommerce's steps were not in what was read (rule 4). Q8-WC-N02
- **Test store**: a store that takes no real payments, for partners' building and for previews, set to any plan to preview it, as Shopify's dev stores, Salla's متاجر تجريبية (in a help article one partner session showed on 8 October 2026) and Zid's demo stores. Left to the build (rule 3). Q8-SH-051; Q8-SH-108; Q8-SA-K2405; Q8-ZD-011
- **App**: an offer a partner or Sharrwah makes, installed on one store by the merchant, who approves its scopes at install. It is listed, unlisted, or private to stores its maker names, and adds to Sharrwah only through **Extension points** and the versioned API. Q8-ZD-K0400; Q8-ZD-K0372
  - It takes listed and unlisted from Shopify and BigCommerce, private apps from Zid and Shopify's custom apps, and scope approval from Zid. Q8-SH-029; Q8-BC-075; Q8-ZD-K0400
  - Entitlements may gate apps by the data they reach, as Shopify's Level 2 PII apps and Zid's private apps. Q8-SH-035; Q8-ZD-K0394
  - Alternative not taken: extensions inside the core through its hooks, as WooCommerce's plugins, which must then declare compatibility with its changes. Through defined points the core and apps change apart (rule 2). Q8-WC-K0014; Q8-WC-K1272
- **Extension point**: a named place an app may add to: an admin page or block, a storefront snippet, a checkout step, a function in a named server flow, and **Provider interfaces** for payment methods, shipping rates, tax and sales channels. Each says whether additions need Sharrwah's review. Partners' contracts rest on these, so they are costly to change after launch (rule 3). Q8-SH-081; Q8-SH-085
  - It combines the points Shopify, Salla, BigCommerce and WooCommerce show, with Shopify's review flags. Q8-SA-K2253; Q8-BC-077; Q8-WC-K0856
  - The **Payment provider interface** opens only to providers Sharrwah has agreed with, after review, as four platforms hold payment integrations apart. Q8-WC-K0353; Q8-BC-058
  - Alternative not taken: embedding a whole app as the only point, as in Zid's iframe (other places were not in what was read); checkout and server additions need points of their own. Q8-ZD-K0388; Q8-ZD-N12
- **API version**: every interface apps use carries a version from the first release (rule 3). A version is retired only after a stated support period, with the change and its date announced, and an app still on it is unlisted; partners get pre-release versions. Q8-SH-036; Q8-SH-070; Q8-SA-K2321
  - It takes Salla's version in each call, Shopify's support period and delisting, and Shopify's release candidates and WooCommerce's betas for partners. Q8-SH-068; Q8-WC-056
  - The cadence, Shopify's fixed one or Salla's at each breaking change, is kept open (section 5; rule 4). Q8-SA-K2318
- **Partner**: a party registered under a signed **Partner agreement**, as app maker, theme maker or service provider. Sharrwah reviews each app, theme and partner service before listing it, and may suspend or remove it. Partner terms are decided now (rule 3). Q8-ZD-018; Q8-WC-071; Q8-ZD-K0364
- **Marketplace**: Sharrwah's listing of apps, themes and partner services, with its own offers listed and marked as its own, filtered by the store's place (rule 1). Q8-BC-045; Q8-SH-K2696; Q8-SA-K2126
- **App charges**: listed apps and themes are billed on the merchant's Sharrwah bill, and Sharrwah pays the partner its share after a set period. The app's maker sets its plans, recurring or by use. Q8-SH-030; Q8-ZD-K0167; Q8-ZD-014
  - These charges are the merchant's payment for an app, not sales proceeds; the partner's share waits for payout. Whether Sharrwah collects as the partners' agent, as on BigCommerce, is a company decision (section 7; rule 4). Q8-BC-K0168; Q8-SA-K2146
  - Alternative not taken: charging fees from a top-up balance, as on Zid, where fees are charged "باستخدام المحفظة"; it would hold sellers' money, under the guard. Q8-ZD-K0629
- **Place profile**: Sharrwah's set-up for one place: which offers open there, which providers fill each provider interface and in what order they are suggested, the contracting entity, terms that supplement Sharrwah's there, and defaults. A store holds one place, with the basis it was set on. Q8-WC-K0054; Q8-WC-K0055; Q8-BC-030
  - It takes WooCommerce's ordered list per country (shipped), and Shopify's and BigCommerce's contracting party by place and place terms. Q8-SH-K1243; Q8-BC-025
  - Why: this is where each place is set up (rule 1). It holds nothing for a place other than Yemen until the founder decides to enter it. Q8-SH-055
- **Account** and **Store**: an account holds one or more stores, with users and billing at the account; each store has its own plan, settings, apps and data, shares none unless linked, and can move to another account with its payment method and user roles. An account above stores, and a store's move between accounts, are costly to add to the data model after launch (rule 3). Q8-SH-046; Q8-SH-047; Q8-SA-050; Q8-SH-109
  - It takes Shopify's organization, the stores one Salla store's list linked, each with its own plan (store merchant, observed 8 October 2026), and BigCommerce's credentials across an account's stores. Q8-SH-046; Q8-SA-050; Q8-BC-K0292
- **Updates feed**: a dated list of new offers and changes, by area, for merchants and partners; left to the build (rule 3). Q8-SH-064; Q8-SA-038

## 3. What can plug in, what is set per what, and who sets it

- Plugs in: apps, themes and partner services, by partners. Q8-SH-029; Q8-ZD-K0400
- Plugs in: payment providers, through gateways or apps. Q8-WC-K0006; Q8-ZD-K0079
- Plugs in: shipping rates and carriers. Q8-WC-K0856
- Plugs in: tax calculation engines. Q8-BC-077
- Plugs in: sales channels, surfaces outside the store. Q8-SH-K2063; Q8-BC-K0209
- Plugs in: financing bodies, whose offers Zid's financing service carries. Q8-ZD-K0176
- Set per platform: terms, extension points, API versions and review rules. Q8-SH-054; Q8-SH-036
- Set per place: which offers open there, the suggested providers and their order, the contracting entity and place terms. Q8-SH-K0041; Q8-WC-K0054; Q8-BC-030
- Set per plan: entitlements, features and numbers. Q8-SH-K2743; Q8-SA-K0055
- Set per account: users and billing, credentials across stores, and early access. Q8-SH-046; Q8-BC-K0292; Q8-SH-K0191
- Set per store: plan, add-ons, apps and their scopes, the merchant's switches, and one preview on a dev store. Q8-SA-050; Q8-SH-073
- Set per market within a store: products and prices. Q8-ZD-026
- Set per app: its pricing plans and the scopes it asks. Q8-ZD-014; Q8-ZD-K0372
- Set per partner: its share. Q8-WC-K0461
- Proposed: Sharrwah would set things at these levels, as the platforms show them. Q8-SH-K0175; Q8-SA-K1973
- Set by Sharrwah: the catalogue, plans and prices, availability by place, stages, extension points, versions, review and partner terms. Q8-ZD-K0157; Q8-BC-K0316
- Set by the merchant: plan, add-ons, apps and the scopes it approves, its own switches where the rule allows, and the facts that set its place. Q8-ZD-K0372; Q8-WC-K1310
- Set by the partner: its app's plans and the scopes it asks. Q8-ZD-014
- Set by the provider: its own terms with the merchant. Q8-SH-K2169
- Set by the account's administrator: account-wide features, as Shopify's organization permission for test drives. Q8-SH-K0191

## 4. Parts, in the order they can be built

1. **Account** and **Store**, with the store's place: needs nothing before it.
2. **Offer catalogue**, **Entitlement** and **Availability rule**: needs part 1.
3. **Plan** and **Add-on**, with billing of Sharrwah's own fees: needs part 2.
4. **Release stage** and **Test store**: needs part 2.
5. **Place profile** for Yemen, or for each area of it (section 5): needs parts 1 and 2; each **Provider interface** is filled as each provider is agreed.
6. **API version** and **Extension point**: needs parts 2 and 4.
7. **App**, its install and scopes: needs part 6.
8. **Partner**, review and **Marketplace**: needs part 7.
9. **App charges**: needs parts 3 and 8, and the company decision on collecting for partners.
10. Each **Additional service**, **Sales channel** and **Market**: needs parts 2 and 5; one that holds sellers' money goes live only by the founder's decision.
11. **Updates feed**: any time after part 2.

## 5. What the design must keep open

- The basis that sets a store's place: Shopify's Store billing address, BigCommerce's domicile, the country of the merchant's documents in one Salla store's set-up (store Store 1, observed 8 October 2026). Keep the place and its basis as recorded fields; a company decision, with a lawyer, settles it. Q8-SH-K1243; Q8-BC-030; Q8-SA-051
- The contracting entity and place terms: keep them as place-profile data, never in code; settled by the company decision on where Sharrwah is based. Q8-BC-025; Q8-SH-K1243
- Preview offers' terms, inside or outside Sharrwah's services: keep a terms reference on each stage; the additional terms Shopify gives for its Beta Services were not in what was read. Settled by a company decision. Q8-SH-061; Q8-BC-028; Q8-SH-N01
- App charges: whether Sharrwah collects as partners' agent, the share and the payout period. Keep **App charges** a part of its own, its share and period as data. Q8-BC-K0168; Q8-SA-K2146
- Offers that hold sellers' money, such as a top-up balance or financing repaid from sales: the catalogue keeps room for them; none goes live without the founder's decision. Q8-ZD-K0130; Q8-ZD-K0176
- The API's cadence: keep a version in every call from the first release; settle the cadence when the first partner agreement is drafted. Q8-SH-036; Q8-SA-K2318
- Plans that move with sales volume: keep a plan change as an event on the store, whatever starts it; settled by the company decision on pricing. Q8-BC-009
- Who may plug in payment methods: keep the **Payment provider interface** closed to all but agreed providers; settled by a company decision and any licence it needs. Q8-BC-058; Q8-WC-K0353
- Offers without an online store, as Shopify's Agentic plan: keep the storefront an offer in the catalogue, not a condition of every other offer. Q8-SH-016
- The level of a place: Yemen's currency and central bank are split, and a payment provider works in the other area only with separate infrastructure. Keep a place profile able to cover an area within a country, not only a country, as Salla's الأسواق المتعددة can target "منطقة أو مدينة"; the founder's decision on where Sharrwah serves first settles it. Q8-SA-K1976; YK-12 (split @ Sana'a and Aden, as of 2026); YK-124 (only with separate infrastructure in the other area @ Aden, as of 2024-04-05)

## 6. Yemen: what its evidence allows, forbids or doesn't show

- **Place profile**: Yemen's currency and central bank are split, and a payment provider from one area may work in the other only with separate infrastructure there. This forbids taking a provider set up for one area as set up for the other, at Aden as of 2024-04-05. YK-12 (split @ Sana'a and Aden, as of 2026); YK-124 (only with separate infrastructure in the other area @ Aden, as of 2024-04-05)
- **Additional service** holding sellers' money: e-money and electronic payment services may be provided only by the institutions each fact names, at its place and date, so such an offer of Sharrwah's own is allowed there only if Sharrwah is one; the guard applies in any case. YA-102 (banks and licensed non-bank institutions @ the internationally recognized government's area, as of 2026-02); YA-102 (banks and non-bank institutions @ Houthis' area, as of 2026-02-11)
- **Payment provider interface**: at E-Pay's service a merchant can take online payments through its payment API, which allows the interface to be filled with E-Pay for Yemen, as of 2026-10-10. YK-131 (available @ E-Pay (Kuraimi Islamic Microfinance Bank)'s service, as of 2026-10-10)
  - WooPayments, which "is powered by Stripe", is not available in Yemen, a request to add it open, and nor is Stripe, both as of 2026-10-10. Q8-WC-K0008; YA-62 (Not available, a request to add it open @ WooPayments's service, as of 2026-10-10); YA-62 (Unavailable @ Stripe's service, as of 2026-10-10)
- **Availability rule**: a financial service provider may not make exclusive arrangements with merchants, in the internationally recognized government's area as of 2023-08-20. There this forbids an exclusion that serves such an arrangement, one payment provider shutting others out of a store, as زد باي turns other gateways off on Zid. Q8-ZD-K0089; YK-128 (not allowed @ the internationally recognized government's area, as of 2023-08-20)
- **Provider interface** for shipping: at Torod's service, linking an online store to the courier is not available, being developed, as of 2026-10-10, so Torod cannot yet fill the interface. YK-206 (not available, being developed @ Torod's service, as of 2026-10-10)
- **Offer catalogue** and **Partner agreement**: an offer or acceptance may be made by electronic message, in the unified Republic's area as of 2006-12-28, which allows sellers and partners to accept Sharrwah's terms online there. YK-344 (accepted @ the unified Republic's area, as of 2006-12-28)
- **Plan** and **App charges**: domestic sales and contracts are paid in the rial only, in the internationally recognized government's area as of 2026-04-24. There, where Sharrwah's contract with a seller is domestic, this forbids taking payment for plans and app charges in another currency. YA-21 (rial only @ the internationally recognized government's area, as of 2026-04-24)
- **App charges**: collections are among the services a licensed payment service provider may offer, in the internationally recognized government's area as of 2022-09-13. Yemen's evidence doesn't show whether collecting app makers' charges for them, as **App charges** would, is such a service, there or in the Houthis' area; a rule, or a central bank's answer, on collecting for third parties would show it. YK-87 (Transfers, collections, prepaid cards, remittances, payment instruments and e-money @ the internationally recognized government's area, as of 2022-09-13)
- **Sales channel**: merchants can sell through an online marketplace, registration free, at Bab Al-Mandab's service as of 2026-10-10. Yemen's evidence doesn't show whether it, or another marketplace there, takes a store's listings through an interface a **Sales channel** could use; the marketplace's own page for sellers or developers would show it. YK-199 (available, registration free @ Bab Al-Mandab's service, as of 2026-10-10)

## 7. Company decisions it raises

- Which company contracts with sellers in each place, and what sets a seller's place. Q8-SH-K1243; Q8-BC-025
- Whether Sharrwah bills partners' app charges as their agent, whether that needs a licence in each area, and the partners' share and payout period. Q8-BC-K0168; Q8-WC-K0461; YK-87 (Transfers, collections, prepaid cards, remittances, payment instruments and e-money @ the internationally recognized government's area, as of 2022-09-13)
- Who may register as a partner, and from where. Q8-BC-062; Q8-ZD-018
- Which providers Sharrwah works with behind each additional service, and on what agreement. Q8-WC-K0008; Q8-BC-K0129
- The terms for preview offers. Q8-SH-061; Q8-BC-028
- Whether third parties may plug in payment methods, and under what review. Q8-BC-058; Q8-SH-095
- How many plans, their prices and the currency they are priced in for each place, whether fees grow with sales, and whether one is free. Q8-ZD-001; Q8-BC-002; Q8-SH-110
- Whether any offer holds sellers' money, which is the founder's decision under the guard. Q8-ZD-K0130
- Whether Sharrwah serves Yemen as one place, or each area as a place of its own, for providers, prices and terms. YK-12 (split @ Sana'a and Aden, as of 2026); YK-124 (only with separate infrastructure in the other area @ Aden, as of 2024-04-05)
