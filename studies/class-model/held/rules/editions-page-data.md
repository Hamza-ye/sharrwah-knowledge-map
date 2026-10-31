# Shopify's `editions-page-data`: the rules in force

This digest serves SH-58 to SH-67; where it differs from the notes and rulings it draws on, they govern.

## 1. What the entries are

Each entry is one feature card of one edition's Editions page, in observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`, read with the edition and section in its `within` (E1, SH-50). The card's words are its title (`heading`, `title`, `cardTitle`, `headlineTitle`, `shortTitle`), subheading, description (`body`, `bodyHtml`, `description`, `descriptionHtml`, `cardBody`, `richText`), `highlights`, list items, `bodyLinks`, CTAs and `signUpModal`, tooltips, footnotes, `tags` and the Dev Mode `tray` (E51, SH-57). SH-58 to SH-67 hold the last 874 entries: Summer '24 from its collection 6, "World's best checkout" (line 7), then Winter '25, Summer '25, Winter '26 and Spring '26 (lines 8 to 11).

## 2. The rules in force

### Reading a card and its group

1. No statement is made by `id`, `handle`, `socialShare`, `ariaLabel`, `ctaAriaLabel`, `iconName`, `cardType`, sizes, themes or media, or by a generic CTA label ('Learn more'), whose address says only where the feature is (E1, E7, SH-50; E51, SH-57).
2. A card is read with its section's or collection's title and description, heading and CTAs; `eyebrow`, `productType` and `parentSection` give no line unless the card is a kind of what they name, and a layout group's title gives none (E1, SH-50; E30, SH-54; E51, SH-57).
3. A card under one handle in two sections is one entry (`merge:handle`); one repeated under another handle (Featured, Top 10) is its own entry, placed by its own words, and the pair takes the same lines (SH-53; E51, SH-57).
4. The same feature in two pages or editions is placed in each by its own words and edition's date, keeping its `cap_id` and terms, and a Dev Mode tray is the dev page's card (E10, SH-50).
5. Quotes and terms stay within one text node, since neither crosses a link's markup (E25, SH-53).

### Support and makers

6. A card is `core` where it places the feature in the platform: admin words ('in your Shopify admin', 'built-in'), an admin address that isn't an app's page, a plan statement, or the platform's own behaviour (E3, SH-50).
7. The platform itself is `core`: its checkout and Shop Pay there, Shopify Payments, discounts, metafields, the theme editor, the admin's mobile client, Shopify Shipping, Shopify Tax, the App Store (E3, E12.4, SH-50; SH-51, case 4; SH-56).
8. The platform's free themes are `core` on CM-SFR-001, and a free theme's announcement bar on CM-SFR-007 (E21, SH-53, overturned after SH-53: 'Our free themes' makes no separate service; the check after SH-62).
9. Shopify POS is the platform's own client, `core` on CM-POS-001 (E22, SH-53; the ruling after SH-55).
10. A card is `own-service` where it or a held statement names Shopify the maker of a separate app, product, device or service ('a new app from Shopify'); 'our help docs' and 'our official fulfillment partner Flexport' name none (E3, SH-50; the ruling after SH-55; E50, SH-56).
11. Shop's things are `own-service`: its Store (CM-CHN-002, where others' Shop Minis are `extension-point`), sign-in (CM-CUS-010), reviews (CM-SUP-001), lead capture (CM-CUS-007), Shop Promise (CM-SHP-018) and AI (CM-AIA-005) (the ruling after SH-34; E3, SH-50; the checks after SH-50 to SH-53). Shop Pay apart from the platform is CM-PAY-014 `own-service` (E23, SH-53).
12. A first-party app (from the App Store, at `apps/<handle>`, or 'the X app') is `own-service` on every line about its own features, renames included, 'wherever held words name the platform as its maker' ('we’ve added … to X', 'from Shopify', a store listing's developer). Its plan lines and admin page stay `core`, others' extensions of it `extension-point` (E3, SH-50, changed by the rulings after SH-35, SH-37, SH-53, SH-2 and SH-55).
13. With no maker statement held, a Shopify-branded app is `shows` plus CM-APP-007 `core` where the card links its `apps/<handle>` page, and `core`, the maker a gap, where named with no address; a plan statement for it is `core` (the ruling after SH-36; E22, SH-53; E28, SH-54). The ruling after SH-43 makes this hold for any app with no maker statement, whatever its name.
14. CM-APP-011 `own-service` goes only where the card itself calls the app Shopify's (E3, SH-50; E29, SH-54).
15. A separate device or service whose maker a held post names is `own-service` (POS Go; POS Terminal, by the changelog's SH-E-dbb979f6; Shopify Lending); one with none stays `shows` (E35, SH-55; E55, SH-57; the coordinator, settling the changelog digest: four POS Terminal lines aligned). Managed Markets is the admin's service, `core` (rule 45).
16. A first-party app's feature takes another capability's line only where the app provides that thing: Stocky's transfers stand on CM-INV-006, while Collective's rates, inventory and price lists stay in its CM-CHN-005 `own-service` line, its sourcing side CM-CAT-010 `shows` (E35, SH-55; E54, SH-57, decided by the ruling after SH-57).
17. The platform's own developer tools are `core`, even 'built by Shopify' or for building apps. An API is `extension-point` where the card says apps do the work through it, else `core`, a Function API `extension-point` by definition, and webhooks the platform sends apps `core` on CM-API-008 and the events' capability (E3, SH-50, and its check; E24, SH-53; E45, SH-56).
18. **An API naming an unnamed outside system is `core`:** the platform's own API for its own feature, `extension-point` only where its words say apps or partners do the work (B-extent). The Inventory States API's 'across external platforms' (SH-51) and 'using APIs to sync cash tracking reports with your accounting software' (SH-57, aligned) are `core` (decided after the digest).
19. A card is `extension-point` where a third party's app does the feature (its venue the filler), or it links an App Store category or collection (E3, SH-50); a non-Shopify-branded app at `apps/` adds CM-APP-007 `core` (E37, SH-55). An app with no maker named is `shows` on its feature, the maker a gap (the ruling after SH-43).
20. `outside` is a third party doing it with no interface of the platform, such as Balance's bank (E3, SH-50; SH-54, case 12).
21. `shows` is a separate product named by its brand alone in no admin, plan or app (Shopify Capital), a topic or claim alone, a case study's features, a stat card's claim, or a partner's permissions (E3, E8, SH-50; E19, E20, SH-53).
22. A new thing's support is what the platform does with it; `shows` is for a thing only named (the check after SH-54; E46, SH-56).
23. An admin section the platform's own words call part of its admin is `core` whatever its route's permission ('track fulfillments without leaving Shopify') (the ruling after SH-2; E50, SH-56).
24. **The Fulfillment Network is Shopify's own, `own-service`,** on its maker statements 'our network of 20+ distribution hubs and fulfillment centers' and 'our nationwide freight services' (E16, SH-51), and it is installed from the App Store. Its partners' work stays `extension-point` (SH-36). The ruling after SH-55's list, which named it among the apps with no maker held, is corrected; SH-38's and SH-56's lines are aligned (decided after the digest).
25. **Shopify Balance is the admin's own money account, `core`,** as its cell reads it (CM-PAY-023, 'a business account in the admin'). A 'we've added … using Shopify Balance' post about an admin service doesn't make it a separate product, as it doesn't for Shopify Payments; the ruling after SH-41 is for a separate product such as Shopify Credit, whose cell holds `own-service`. SH-51's 'Shopify Balance app' `shows` stands as its own reading (decided after the digest).

### Scope

26. A plan or country in the source's words is the scope (`plusExclusive: true`, the tag 'Shopify Plus exclusive', 'Exclusive to POS Pro.', '(US only)'), as is 'Currently available to businesses in the United States.', unlike 'select businesses' (E6, SH-50; E27, SH-54).
27. A kind of business the card's words name is the scope ('For businesses using a custom checkout'), as is 'Exclusive to eligible Shopify merchants'; who gains most is not (E27, SH-54; E39, SH-55).
28. A paid offer's own line takes 'only its site' as scope, and what comes with it the offer's name in the source's words ('Managed Markets', 'Commerce Components') (the ruling after SH-70; E14, SH-51; E23, SH-53; E39, SH-55; E53, SH-57).
29. **A line on CM-MKS-003 itself is the offer, with no add-on scope** (E53, SH-57; the ruling after SH-70). A Managed Markets feature placed on another capability takes 'Managed Markets' as scope. SH-55's DDP line is aligned (decided after the digest).
30. An entry's lines share one scope, but a thing stated under its own condition takes its own on its line; a topic tag ('Enterprise'), a section's name or a link's address is no scope (the rulings after SH-34 and SH-69; E6, SH-50).
31. In a scope, `;` separates alternatives and ` and ` adds a condition that must also hold; a source's own words holding 'and' are quoted (the rulings after SA-53 and SH-38).

### Release markers

32. A card is `shows`, the words in `reading`, where it states the feature isn't yet offered to every store ('Coming soon', 'Sign up for early access', 'Join the waitlist', 'Now in Developer Preview', 'select businesses'), whatever its maker (E5, SH-50; E29, SH-54; SH-53, case 8).
33. A preview the merchant can turn on now is `core`, its plans the scope (the ruling after SH-34). 'Now available', 'new' and 'stable release' go in `reading`, the support being what the words give (E5, SH-50; E43, SH-56).
34. A card inherits its lead card's limit, but a lead card isn't read with its followers'; an early-access link beside an admin link gives `core;shows` on one line (E5, SH-50; E31, SH-54; E43, SH-56).
35. A release state in a link's address (`…-developer-preview`, `unstable`) is no statement: it goes in `reading`, the support staying the card's (E13, SH-51, kept at its check).
36. A `ctaAriaLabel` with empty `ctas` is no sign-up (E52, SH-57), and Sidekick 'is live on thousands of Shopify stores' is `shows` (E58), both marked readings.

### Containers and headings

37. A chapter, collection, section group, `parentSection` or `eyebrow` is what a card is read with, not an entry, and a heading with no products goes to the second stage (E4, SH-50; the check after SH-56).
38. An overview or lead card gives each thing it names a line by its own words, not being a list of uses; one with only a title, `productType` and heading is placed by those, its maker the product's (E26, E31, SH-54; E36, SH-55).

### Capabilities that recur

39. CM-ONB-003 `core` holds the Editions albums (a reading), introduction cards and the platform's own guides, a guide also `shows` on its topic (E2, SH-50; SH-55, case 13; E50, SH-56; E51, SH-57).
40. CM-APP-007 `core` goes with every `admin.shopify.com/apps/<handle>` link (POS's is CM-POS-001's page too), and no other admin address (E7, SH-50; E50, SH-56). CM-APP-002 `core` holds the App Store's own features (E56, SH-57).
41. CLI commands are CM-DVT-002, other tools CM-DVT-001, development stores CM-DVT-004; a card whose title or `productType` names Shopify Functions also takes CM-APP-005 (E44, E50, SH-56; the check after SH-51).
42. A Shopify Shipping carrier is the filler of the CM-SHP-002 `core` line and takes CM-SHP-015 `shows`; the merchant's own carrier account is CM-SHP-015 `core` (E15, SH-51; E50, SH-56).
43. Cards saved for a faster checkout are CM-PAY-014's; cards charged later or kept current are CM-PAY-022's, providers' access to them `extension-point` (E33, SH-54; E38, SH-55).
44. POS devices are CM-POS-002, receipts CM-ORD-008 `core`, staff credited with a sale `new:Staff sales attribution` (E55, SH-57).
45. Managed Markets (formerly Markets Pro) is CM-MKS-003 `core`, Global-e `outside` where named: 'Our Merchant of Record capability' names an admin service, as the cell reads it, not a separate product (the test the correction on Shopify Balance set; the coordinator, settling the changelog digest: thirteen lines aligned). It holds its duties and restricted products; its other features go on their own capabilities, `core`, scoped 'Managed Markets' (E35, E41, SH-55; E53, SH-57).
46. A card whose words name business buyers also takes CM-B2B-001 (E58, SH-57); a quote request turned into a draft order is CM-B2B-004 `core` (the check after SH-50).
47. A feature's notices to staff are CM-NTF-002, address validation at checkout CM-CUS-009, an order edit's changes CM-ORD-002, discounts without a code CM-MKT-003 `core`, and a plan's billing currency and payment method CM-PLN-004 and CM-PLN-005 (E42, E48, E49, SH-56; the check after SH-54; E57, SH-57).
48. Merchant financing, Shopify Lending's term loans and line of credit included, is CM-PAY-026, its repayment a quality (the check after SH-55).
49. An admin-wide card takes no line, each feature it names taking its own; the admin's own frame is no capability's thing (the ruling after SH-37; E33, SH-54).
50. **AI for merchants outside the admin goes on the place's capability, not CM-AIA-001,** whose thing is the platform's AI in the merchant's admin. The Help Center's assistant is CM-ONB-003 (SH-53); the App Store's 'AI-powered guidance' is CM-APP-002, its CM-AIA-001 line dropped (SH-56, aligned; decided after the digest).

### Other readings

51. A highlight, list item or tray naming a feature of its own takes a line with its own support, but no line goes to a claim, a list of what may be used ('like', 'such as'), the APIs a thing is built with, or what a card names in passing (E4, SH-50; E58, SH-57; the ruling after SA-41).
52. An entry takes one line per capability, two supports on it where stated (`core;extension-point`), and a second line only for a thing under its own condition or filler (E4, SH-50; the ruling after SH-34).
53. An App Store address names no maker; a help or shopify.dev address shows which feature is meant, in `reading`; a page outside the sources isn't read; a card is about the app whose page its link opens, where its words name no other (E7, SH-50; the ruling after SH-38).
54. A filler is the third party the card names doing the thing or its venue, parties after 'like' included where they are its other party; channels named in passing, the group's companies, Shopify's apps and a case study's merchant are not (E8, SH-50; E15, SH-51; E19, SH-53).
55. A quality is a limit, duration, price, fee, size or count in the card's words, a discount on rates included; conversion and speed claims and a stat card's number are claims (E9, SH-50; E20, SH-53; E33, SH-54).
56. A capability's note that sends a thing elsewhere is followed (E41, SH-55).
57. An entry is `out` only where it states no feature: decoration, a bare number, an easter egg, a UI string, or merchandise such as the Shopify Keyboard (E11, SH-50; E58, SH-57).

## 3. The first-party apps

The table follows the ruling after SH-55 and the batches' lines; each app's plan lines and admin page (CM-APP-007) stay `core`.

| App | Own features | Maker statement |
| --- | --- | --- |
| Shop | `own-service` | the ruling after SH-34 |
| Shopify Audiences | `own-service` | SH-E-234dcbd7 |
| Shopify Collabs | `own-service` | SH-E-709b37e4 |
| Planet | `own-service` (`new:Planet`) | SH-E-bc581483 |
| Search & Discovery | `own-service` | SH-E-9b869699 |
| Shopify Bundles | `own-service` | SH-E-1d272a37, SH-E-88c8359c |
| Shopify Subscriptions | `own-service;extension-point`, as aligned | SH-E-4c0f3472 |
| Combined Listings | `own-service` | SH-E-dc618719 |
| Shopify Email (Shopify Messaging) | `own-service` | SH-E-32e5ccc3; the rename, SH-E-6be48c3e |
| Shopify Inbox | `own-service` | SH-S-2758, its store listing; SH-E-4f0c8272 |
| Stocky | `own-service` | SH-E-5b89aa16 |
| Shopify Flow | `own-service` | SH-E-0678ff26 |
| Shopify Collective | `own-service` | SH-E-850b28ae |
| Translate & Adapt | `own-service` | SH-E-04551fad |
| Checkout Blocks | `own-service` | SH-E-a2643162 |
| Shopify Fulfillment Network | `own-service` (rule 24) | 'our network of 20+ distribution hubs…' (E16, SH-51) |
| Fraud Control | `own-service` (the ruling after SH-41) | SH-E-8f406571 |
| ShopifyQL Notebooks | `own-service` | SH-E-3f85908b |
| Shopify Credit | `own-service` on its features; its admin routes and plan rows `core` (the ruling after SH-41) | SH-E-e3a378a2 |
| Shopify Balance | `core`, the admin's own account (rule 25) | not a separate product |
| Shopify Forms, Marketplace Connect, Order Printer | `shows`, the maker a gap; their admin pages and plan lines `core` (the ruling after SH-43) | none held |
| Pixel Helper | `core`, opened from the admin's Customer events (check SH-58) | SH-E-0a66f16d names its maker; a built-in tool, not a separate product |
| Bill Pay | `core` at `finances/billpay`, `shows` at `apps/bill-pay` (E28, SH-54); the maker a gap | none held (SH-56) |

The devices and services with a maker statement are POS Go (SH-E-fc9fba8c), POS Terminal (SH-E-dbb979f6, a changelog post) and Shopify Lending (SH-E-797024ee); Managed Markets' 'Our Merchant of Record capability' names an admin service (rule 45). SH-54 kept Shopify Fraud Control, the Privacy & Compliance app and ShopifyQL Notebooks without a maker, before `makers` existed. `held_entries.py makers --platform shopify NAME …` settles them and any app not listed.

## 4. The new things named so far

The Editions are in English only, so no Arabic name is held. The names to keep:
- Linkpop, Try before you buy, Planet, Sanity integration, Tipping, Staff sales attribution and Quantity rules (SH-50);
- Commerce Components by Shopify (SH-51);
- Quick order lists, the name for B2B's later `b2b-quick-order-lists` too, and App versions (SH-53);
- 3D Secure (SH-54);
- Web performance dashboard, and Shoppable videos, which SH-53's Tolstoy line takes too (SH-55);
- Saved views (SH-35) and Admin search (SH-36), decided with Zid's and Salla's admin search (the ruling after SH-37);
- the admin's own interface language, `العربية / English`, one new thing across the platforms (the ruling after SA-49; SH-34).

Batches wrote different supports for Staff sales attribution, Saved views, Admin search, App versions and Sanity integration; each is decided with its thing in `held/new.tsv` (the checks after SH-55 to SH-57).

## 5. Where to look for more

Each batch's notes (`shopify/notes-SH-50.md` to `notes-SH-57.md`) hold the cases behind its rules, the cases left open and the leads no line takes, and `review-H-rulings.md` holds each ruling in full. Read a batch's notes only where a case is needed.

## 6. Rules added since the digest, as the coordinator kept them

From SH-58 (its notes give the cases):
- **E59:** a Top 10 card repeats a card placed elsewhere and takes its twin's lines, matched by words where the handles differ.
- **E60:** a component's own feature takes its capability, `own-service`, scoped by the component (the ruling after SH-57).
- **E61:** a feature told twice, by a merchant card and a developer card, takes the same capabilities, each line's support and scope by its own words.
- **E62:** a buyer's tax ID at checkout is CM-TAX-005.
- **E63:** payment extensions are CM-PAY-011 `extension-point`.
- **E64:** a partners' protocol for the checkout is CM-CHK-001 `extension-point`, the partners its filler.
- **E65:** a kind of store named as the condition is the scope.
- **E66:** a card's own staff permissions are CM-STF-002 `core`.
- **E67:** an API's field names its thing's capability.
- **E68:** places named in a card's own news take their line, not those named in passing.

From SH-59 (its E59.1 to E59.8):
- **E69:** the summary's 'We're rolling out' makes its cards `shows`.
- **E70:** the App Store's developer features are CM-APP-002, `core;extension-point` where third parties' apps are marked or matched.
- **E71:** Functions' developer tools are CM-DVT-001 and CM-DVT-002, the card's Functions line CM-APP-005.
- **E72:** the Subscription API is `extension-point`, by its own statements.
- **E73:** marketing automations powered by Flow are CM-MKT-006 `own-service`.
- **E74:** in 'X works with Y', each thing takes its line.
- **E75:** Search & Discovery's recommendations are CM-MKT-023 `own-service`.
- **E76:** a Shop Pay Component feature is scoped by the businesses its card names and the component.

From SH-60:
- **E77:** a Managed Markets feature goes on its own capability, scoped 'Managed Markets'. Where the card's title names Managed Markets, it also takes CM-MKS-003 `core`.
- **E78:** a B2B line's support is that of the B2B thing the card shows. Apps that serve business buyers make it `extension-point`.
- **E79:** twins across sections, such as Wholesale against Checkout and developer against merchant, keep the twin's capabilities. Each line's support and scope follow its own words.
- **E80:** a list in a card's news gives each item its line (SH-60's notes).
- **E81:** a first-party app's card is read by its title.
  - The app's own feature takes no line for the platform's thing it acts on.
  - A platform feature the app automates takes `core` beside the app's `own-service`.
- **E82:** Collective's work with third parties stays in its CM-CHN-005 line, and the third parties' apps take their own `extension-point`.
- **E83:** a card whose title names the API it extends takes CM-API-001 `core`, beside the capabilities of what the API now covers.
- **E84:** events the platform sends to pixels are CM-MKT-009 `core`. Pixels that developers build are `extension-point`.
- **E85:** a Hydrogen card takes CM-SFR-011 `core`, and what Hydrogen now supports takes its own line.
- **A third party doing the work with no platform interface named is `outside`, its name the filler** (B-extent; the check after SH-60, for Shipbob's labels).

From SH-61:
- **E86:** the App Store's tools for developers' own ads, attribution and support button are CM-APP-002 `core`. They are `core;extension-point` only where third parties' apps are matched, ranked or marked.
- **E87:** the Partner Dashboard takes CM-PTN-001 `core` where the card's news happens in it.
- **E88:** a developers' forum is CM-DVT-001.
- **E89:** an app at an App Store address with no maker held is `shows` on its feature, the maker a gap (the ruling after SH-43, which replaces this rule's first wording, `extension-point`). The Knowledge Base app is aligned.
- **E90:** a separate tool at its own site, with no maker held, is `shows`.
- **E91:** 'Rolling out now for those new to Shopify' is `shows`, the group its scope.
- **E92:** a condition such as 'select countries without small coins' is a scope, not a release marker.
- **E93:** a feature's POS and Marketing twins each take both cards' capabilities, each line's support by its own words.
- **E94:** Managed Markets' list of duties, taxes, customs and restrictions splits by rule 45.
- **E95:** store credit 'in Liquid' takes a line for each place the card names.

From SH-62:
- **E96:** the records an app syncs or imports take no line.
- **E97:** the Shopify mobile app's own navigation is CM-SRF-001 `core`.
- **E98:** guidance inside an admin flow belongs to that flow's capability, not to a CM-ONB-003 guide.
- **E99:** a 'Get notified' sign-up with no docs or admin link is `shows`; a thing in the same card that links its own docs keeps its own support.
- **E100:** a developer guide's topics take `shows`.
- **E101:** a kind of developer named as the condition is the scope ('Built for Shopify').
- **E102:** Shop's own features stand on their own capabilities, `own-service`.
- **E103:** Checkout Blocks' order limits are CM-CHK-005.
- **E104:** carrier preferences are CM-SHP-015 `core`, and the route the card's link opens takes its own line.

From SH-63:
- **E105:** a card where Sidekick does a task takes CM-AIA-002 `core`, and the feature it builds or edits takes its own line.
- **E106:** a Sidekick card with only a title is placed by that title.
- **E107:** extension APIs go on the extension's capability; the POS Print API also takes CM-ORD-009 `shows`.
- **E108:** in-person payments and payment methods at the POS are CM-PAY-021, CM-PAY-017 and CM-PAY-018.
- **E109:** the POS Hub is `own-service` (SH-E-04dd57d3); its compatible devices, whose makers aren't named, are `shows`.
- **E110:** a refund screen's list gives each item its line.
- **E111:** Uber Direct is CM-SHP-006 `extension-point`, not CM-SHP-008.
- **E112:** AI in an admin flow that isn't Sidekick takes CM-AIA-001.
- **E113:** a third party that builds the store, with no platform interface named (Lovable), is `outside` on CM-SFR-011.
- **E114:** Messaging's planner is CM-MKT-019.

From SH-64:
- **E115:** the merchant's own card disputes and cashback are the account's or the card's (CM-PAY-023, CM-PAY-025), not CM-PAY-009's or CM-LOY-003's.
- **E116:** carriers named each in its own country take one CM-SHP-002 line and one CM-SHP-015 line per country.
- **E117:** a Managed Markets card stated 'US only' takes it as scope, and its features 'Managed Markets and US only'.
- **E118:** the Shopify mobile app's own features are CM-SRF-001 `core`; the payments they take go on their own capabilities.
- **E119:** a fulfillment card's list gives each item its line.
- **E120:** Shop personalizing a store's Shop storefront is CM-MKT-023 `own-service`, beside CM-CHN-002.
- **E121:** Built for Shopify's prioritization, featuring and grace period are CM-APP-002 `core;extension-point`, scoped 'Built for Shopify'.
- **E122:** commerce agents built on the Catalog API, MCP tools or Checkout Kit are CM-AIA-005 `extension-point`.
- **E123:** integrations credited to named third parties, with no platform interface named, are `outside`. One 'leveraging our … features' is `extension-point` (SH-55's Acumatica).
- **E124:** third parties' EDI apps at App Store addresses, the companies named as the work's source, are `extension-point`.

The next batches number their rules from E125.

