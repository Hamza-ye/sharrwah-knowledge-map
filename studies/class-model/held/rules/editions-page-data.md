# Shopify's `editions-page-data`: the rules in force

The rules of SH-50 to SH-57's notes as each coordinator's check left them, with the rulings in `review-H-rulings.md` from the one after SH-34 on, for SH-58 to SH-67. Where this digest differs from them, they govern.

## 1. What the entries are

Each entry is one feature card of one edition's Editions page, in observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`, read with the edition and section in its `within` (E1, SH-50). The card's words are its title (`heading`, `title`, `cardTitle`, `headlineTitle`, `shortTitle`), subheading, description (`body`, `bodyHtml`, `description`, `descriptionHtml`, `cardBody`, `richText`, `content`), `highlights`, list items, `bodyLinks`, CTAs and `signUpModal`, tooltips, footnotes, `tags` and the Dev Mode `tray` (E1; E51, SH-57). SH-58 to SH-67 hold the last 874 entries: Summer '24 from its collection 6, "World's best checkout" (line 7), then Winter '25, Summer '25, Winter '26 and Spring '26 (lines 8 to 11).

## 2. The rules in force

### Reading a card and its group

1. No statement is made by `id`, `handle`, `socialShare`, `ariaLabel`, `ctaAriaLabel`, `iconName`, `cardType`, `modalType`, sizes, themes or media, or by a generic CTA label ('Learn more'), whose address says only where the feature is (E1, E7, SH-50; E51, SH-57).
2. `eyebrow`, `productType` and `parentSection` help find a card's capability but give no line unless the card is a kind of what they name (E1, SH-50).
3. A card is read with its section's or collection's title and description, its `productType`, heading and CTAs. A layout group's title ('Conversion - L - Products 2.0') gives no line or scope (E30, SH-54; E51, SH-57).
4. A card under one handle in two sections is one entry (`merge:handle`). One repeated under another handle (Featured, Top 10) is its own entry, and the pair takes the same lines (SH-53; E51, SH-57).
5. The same feature in two pages or editions is placed in each by its own words and edition's date, with the same `cap_id` and terms. A Dev Mode tray is the dev page's card (E10, SH-50).
6. A list repeating an edition's cards under other headings maps each heading to its card by collection and order and takes that card's first line (E18, SH-51; SH-52).
7. Quotes and terms are taken within one text node: neither crosses a link's markup, and `&amp;` doesn't match (E25, SH-53; SH-57).

### Support and makers

8. A card is `core` where it places the feature in the platform: admin words ('in your Shopify admin', 'built-in'), an admin address that isn't an app's page, a plan statement, or the platform's own behaviour (E3, SH-50).
9. The platform itself is `core`: its checkout and Shop Pay there, Shopify Payments, discounts, metafields, the theme editor, the admin's mobile client (CM-SRF-001), Shopify Shipping, Shopify Tax and the App Store (E3, E12.4, SH-50; E17, SH-51; SH-54; SH-56).
10. The platform's free themes are `core` on CM-SFR-001 and CM-SFR-007 (E21, SH-53, overturned after SH-53: 'Our free themes' makes no separate service).
11. Shopify POS is the platform's own client, `core` on CM-POS-001 (E22, SH-53; the ruling after SH-55). SH-50's Summer '22 POS card stays `shows` as placed, for the amendment (E12.1).
12. A card is `own-service` where it or a held statement names Shopify the maker or provider of a separate app, product, device or service ('a new app from Shopify', 'our latest mobile point of sale (POS) device'). 'Our help docs', the page's 'everything that we’ve been building' and 'our official fulfillment partner Flexport' name no maker (E3, SH-50; the ruling after SH-55; E50, SH-56).
13. Shop's things are `own-service`: its Store and Minis (CM-CHN-002), Sign in with Shop (CM-CUS-010), reviews (CM-SUP-001), lead capture (CM-CUS-007), Shop Promise (CM-SHP-018) and AI (CM-AIA-005) (the ruling after SH-34; E3, SH-50; the checks after SH-50 to SH-53). So is Shop Pay on 'external checkouts', CM-PAY-014 (E23, SH-53).
14. A first-party app (from the App Store, at `apps/<handle>`, or 'the X app') is `own-service` on every line about its own features, renames included, 'wherever held words name the platform as its maker' ('we’ve added … to X', 'our … in X', 'first-party', 'from Shopify', a store listing's developer). Its plan lines and admin page (CM-APP-007) stay `core`, third parties' extensions `extension-point` (E3, SH-50, changed by the rulings after SH-35, SH-37, SH-53, SH-2 and SH-55).
15. With no maker statement held, a Shopify-branded app is `shows`, with CM-APP-007 `core`, where the card links its `apps/<handle>` page, and `core`, the maker a gap, where it is named with no address. A plan statement for it is `core` (the ruling after SH-36; E22, SH-53; E28, SH-54).
16. CM-APP-011 `own-service` goes only where the card itself calls the app Shopify's (E3, SH-50; E29, SH-54).
17. A separate device or service whose maker a held card names is `own-service` (POS Go, Managed Markets, Shopify Lending); one with none stays `shows` (POS Terminal) (E35, SH-55; E55, SH-57).
18. A first-party app's feature takes another capability's line only where the app provides that capability's thing: Stocky's transfers stand on CM-INV-006, while Collective's rates, inventory and price lists stay on CM-CHN-005 (E54, SH-57, decided by the ruling after SH-57).
19. The platform's own developer tools (CM-DVT-001, CM-DVT-002) are `core`, even 'built by Shopify' or for building apps (E3, SH-50, and its check; E24, SH-53).
20. An API is `extension-point` where the card says apps or partners do the work through it, `core` as the platform's own API for its own feature, `core;extension-point` where both. A Function API is `extension-point` by definition (E3, SH-50; E24, SH-53).
21. Webhooks the platform sends apps are `core`, on CM-API-008 and the events' capability (E45, SH-56).
22. **Unsettled.** An API card naming an unnamed outside system: SH-51 kept the Inventory States API's 'across external platforms' `core` only (kept at its check); SH-57 placed 'sync cash tracking reports with your accounting software' `extension-point` (case 8, a marked reading).
23. A card is `extension-point` where a third party's app, or one with no maker named, does the feature (its venue the filler), where it links an App Store category or collection, or where it says apps provide it (E3, SH-50). A non-Shopify-branded app at `apps/` (Google & YouTube, TikTok, Faire) adds CM-APP-007 `core` (E33, SH-54; E37, SH-55).
24. `outside` is a third party doing it with no interface of the platform, such as the bank holding Balance's funds (E3, SH-50; SH-54, case 12).
25. `shows` is a separate product named by its brand alone, in no admin, plan or app (Shopify Capital, POS hardware), a topic or claim alone, a case study's features, a stat card's claim, or a partner's permissions (E3, E8, SH-50; E19, E20, SH-53).
26. A new thing's support is what the platform does with it; `shows` is for a thing only named (the check after SH-54; E46, SH-56).
27. An admin section the platform's own words call part of its admin is `core` whatever its route's permission ('track fulfillments without leaving Shopify') (the ruling after SH-2; E50, SH-56).
28. **Unsettled.** The Fulfillment Network's maker: the check after SH-51 kept 'our network of 20+ distribution hubs' as a maker statement, `own-service` on CM-SHP-012 (E16); the ruling after SH-55 lists the Fulfillment Network as having none held, and SH-56 placed Winter '24's card `core` (E50).
29. **Unsettled.** Shopify Balance: SH-51 placed the 'Shopify Balance app' `shows`, named by its brand alone (case 6), which a maker statement would make `own-service` (E35); SH-54 to SH-56 placed it `core` as the platform's own admin service, SH-56 beside held 'we’ve added' posts.

### Scope

30. A plan, in the source's words, is the scope: `plusExclusive: true`, the tag 'Shopify Plus exclusive', 'Exclusive to POS Pro.', 'Basic plan' (E6, SH-50; E27, SH-54).
31. A country is the scope ('(US only)'), and so is 'Currently available to businesses in the United States.', unlike 'select businesses' (E6, SH-50; E27, SH-54).
32. A kind of business the card's words name is the scope ('For businesses using a custom checkout'), as is 'Exclusive to eligible Shopify merchants'; who gains most is not (E27, SH-54; E39, SH-55).
33. A paid offer's own line takes 'only its site' as scope, and a feature that comes with it takes the offer's name in the source's words ('Managed Markets', 'Commerce Components') (the ruling after SH-70; E14, SH-51; E23, SH-53; E39, SH-55; E53, SH-57).
34. **Unsettled.** A line on CM-MKS-003 itself: SH-55 scoped the DHL card's DDP line 'Shopify Markets Pro' (E39, E41); SH-57 left every CM-MKS-003 line unscoped, as the offer itself (E53).
35. An entry's lines share one scope, but a thing stated under its own condition takes its own on its line (the rulings after SH-34 and SH-69; E6, SH-50).
36. No scope comes from a tag such as 'Enterprise', a market's or section's name, or a link's address (E6, SH-50).
37. `;` separates alternatives and ` and ` adds a condition that must also hold; a source's own words holding 'and' are quoted, and 'the UK and Ireland' is `UK;Ireland` (the rulings after SA-53 and SH-38; SH-55).

### Release markers

38. A card is `shows`, the words in `reading`, where it states the feature isn't yet offered to every store ('Coming soon', 'will', 'Sign up for early access', 'Join the waitlist', 'Now in Developer Preview', 'Currently available to select businesses'), whatever its maker (E5, SH-50; E29, SH-54; SH-53, case 8).
39. A preview the merchant can turn on now is `core`, its plans the scope (the ruling after SH-34; the check after SH-50).
40. 'Now available', 'new', 'Now in full release' and 'stable release' go in `reading`; the support is what the words give (E5, SH-50; E43, SH-56).
41. A card inherits the limit its lead card states, but a lead card isn't read with its followers' (E5, SH-50; E31, SH-54; E43, SH-56).
42. An early-access link beside an admin link gives `core;shows` on one line (E5, SH-50).
43. A release state in a link's address (`…-developer-preview`, `unstable`) is no statement and goes in `reading` (E13, SH-51, kept at its check).
44. A `ctaAriaLabel` with empty `ctas` and `signUpModal` is no sign-up, so the Markets cards are `core` (E52, SH-57); Sidekick 'is live on thousands of Shopify stores' is `shows` (E58). Both are marked readings.

### Containers and headings

45. A chapter, collection, section group, `parentSection` or `eyebrow` is what a card is read with, not an entry; a heading with no products goes to the second stage (E4, SH-50; the check after SH-56).
46. An Editions album, and an edition's introduction card, is CM-ONB-003 `core`, its `tagLine` the term (E2, SH-50, a reading; E51, SH-57).
47. An overview or lead card gives each thing it names a line by its own words, not being a list of uses; one with only a title, `productType` and heading is placed by those (E26, E31, SH-54; E36, SH-55).
48. An item holding API groups is CM-API-001 `core`; each API title takes the support of the same edition's card for it, else `core` (E13, SH-51).

### Capabilities that recur

49. CM-ONB-003 `core` holds the platform's own guides; a guide is also `shows` on its topic (SH-55, case 13; E50, SH-56).
50. CM-APP-007 `core` goes with every `admin.shopify.com/apps/<handle>` link (POS's is CM-POS-001's page too), and no other admin address (E7, SH-50; E50, SH-56).
51. CM-APP-002 `core` holds the App Store's own features; its install flow is CM-APP-001, an app's install permissions CM-API-003 `shows` (E50, SH-56; E56, SH-57).
52. CLI commands are CM-DVT-002, other tools CM-DVT-001, development stores CM-DVT-004. A card naming Shopify Functions also takes CM-APP-005 (E44, E50, SH-56; the check after SH-51).
53. A Shopify Shipping carrier is the filler of the CM-SHP-002 `core` line and takes CM-SHP-015 `shows`; the merchant's own carrier account is CM-SHP-015 `core` (E15, SH-51; E50, SH-56).
54. Cards saved for a faster checkout are CM-PAY-014's; cards charged later or kept current are CM-PAY-022's, providers' access to them `extension-point` (E33, SH-54; E38, SH-55).
55. POS devices are CM-POS-002, receipts CM-ORD-008 `core`, staff credited with a sale `new:Staff sales attribution` (E55, SH-57).
56. Managed Markets, formerly Markets Pro, is CM-MKS-003 `own-service` on 'Our Merchant of Record capability' (SH-E-9e3f5c76), `core` too where the card links `settings/markets/pro/apply`. Its duties and restricted products stay there; its other features go on their own capabilities, `core`, scoped 'Managed Markets' (E35, E41, SH-55; E53, SH-57).
57. Collective is CM-CHN-005 `own-service`, its sourcing side CM-CAT-010 `shows` (E35, SH-55; E54, SH-57).
58. A card whose words name business buyers also takes CM-B2B-001 (E58, SH-57); a quote request turned into a draft order is CM-B2B-004 `core` (the check after SH-50).
59. A feature's notices to staff take CM-NTF-002 with its support, address validation at checkout is CM-CUS-009, and what an order edit changes stays on CM-ORD-002 (E42, E48, E49, SH-56).
60. Discounts applied without a code are CM-MKT-003 `core`; a plan's billing currency is CM-PLN-004 and its payment method CM-PLN-005 (the check after SH-54; E57, SH-57).
61. An admin-wide card takes no line, each feature it names taking its own; the admin's own frame is no capability's thing (the ruling after SH-37; E33, SH-54).
62. **Unsettled.** AI for merchants outside the admin: SH-53 put the Help Center's assistant on CM-ONB-003 alone, CM-AIA-001 being the admin's AI (case 9); SH-56 put the App Store's 'AI-powered guidance' on CM-AIA-001 `core` (E50, case 6).

### Other readings

63. A highlight, list item or tray naming a feature of its own takes a line with its own support; a claim takes none (E4, SH-50).
64. No line goes to a list of what may be used ('like', 'such as'), the APIs a thing is built with, or what a card names in passing (E4, SH-50; E58, SH-57; the ruling after SA-41).
65. An entry takes one line per capability, with two supports on it where stated (`core;extension-point`), and a second line only for a thing under its own condition or filler (E4, SH-50; the ruling after SH-34).
66. An App Store address names no maker; a help or shopify.dev address shows which feature is meant, cited in `reading`; a linked page outside the sources isn't read; a card is about the app whose page its link opens (E7, SH-50; the ruling after SH-38).
67. A filler is the third party the card names doing the thing, or its venue, parties after 'like' included where they are its other party. Channels named in passing, the group's companies, Shopify's apps and a case study's merchant are not (E8, SH-50; E15, SH-51; E19, SH-53).
68. A quality is a limit, duration, price, fee, size or count in the card's words, a discount on rates included; conversion and speed claims and a stat card's number are claims (E9, SH-50; E20, SH-53; E33, SH-54; E50, SH-56).
69. A capability's note that sends a thing elsewhere is followed (E41, SH-55).
70. An entry is `out` only where it states no feature: decoration, a bare number, an easter egg, a UI string, or merchandise such as the Shopify Keyboard (E11, SH-50; E58, SH-57).

## 3. The first-party apps

From the ruling after SH-55 and the batches' lines. Each app's plan lines and admin page (CM-APP-007) stay `core`.

| App | Its own features | Maker statement |
| --- | --- | --- |
| Shop | `own-service` | the ruling after SH-34 (SH-S-0056) |
| Shopify Audiences | `own-service` | SH-E-234dcbd7 |
| Shopify Collabs | `own-service` | SH-E-709b37e4 |
| Planet | `own-service` (`new:Planet`) | SH-E-bc581483 |
| Search & Discovery | `own-service` | SH-E-9b869699 |
| Shopify Bundles | `own-service` | SH-E-1d272a37, SH-E-88c8359c |
| Shopify Subscriptions | `own-service` (aligned: `own-service;extension-point`) | SH-E-4c0f3472 |
| Combined Listings | `own-service` | SH-E-dc618719 |
| Shopify Email, now Shopify Messaging | `own-service` | SH-E-32e5ccc3; the rename, SH-E-6be48c3e |
| Shopify Inbox | `own-service` | SH-S-2758, its store listing (the ruling after SH-2); SH-E-4f0c8272 |
| Stocky | `own-service` | SH-E-5b89aa16 |
| Shopify Flow | `own-service` | SH-E-0678ff26 |
| Shopify Collective | `own-service` | SH-E-850b28ae |
| Translate & Adapt | `own-service` | SH-E-04551fad |
| Checkout Blocks | `own-service` | SH-E-a2643162 |
| Shopify Forms, Marketplace Connect, Order Printer, the Fulfillment Network (rule 28) | `core`, the maker a gap (rule 15) | none held |
| Bill Pay | `core` at `finances/billpay`, the maker a gap (provider Melio, on CM-PAY-027's cell); `shows` at `apps/bill-pay` (E28, SH-54) | none held (SH-56) |

Shopify POS and the online store are the platform's own sales channels, `core`. The devices and services with a maker statement are POS Go (SH-E-fc9fba8c), Managed Markets (SH-E-9e3f5c76) and Shopify Lending (SH-E-797024ee). SH-54 kept Shopify Fraud Control, the Privacy & Compliance app and ShopifyQL Notebooks without a maker, 'none being named in a held post I know of', before `makers` existed. `held_entries.py makers --platform shopify NAME …` settles these and any app not listed: it prints the held entries that name the app with a maker's cue, with their lines.

## 4. The new things named so far

The Editions are in English only, so no Arabic name is held. Keep these names:
- Linkpop, Try before you buy, Planet, Sanity integration, Tipping, Staff sales attribution and Quantity rules (SH-50);
- Commerce Components by Shopify (SH-51);
- Quick order lists, which B2B's later card `b2b-quick-order-lists` takes too, and App versions (SH-53);
- 3D Secure (SH-54);
- Web performance dashboard and Shoppable videos, which SH-53's Tolstoy line takes too (SH-55);
- Saved views (SH-35) and Admin search (SH-36), decided with Zid's and Salla's admin search (the ruling after SH-37);
- the admin's own interface language, `العربية / English`, one new thing across the platforms (the ruling after SA-49; Shopify's Admin languages, SH-34).

Planet's lines are `own-service` (the check after SH-54). Batches wrote different supports for Staff sales attribution, Saved views, Admin search, App versions and Sanity integration; each is decided with its thing in `held/new.tsv` (the checks after SH-55 to SH-57).

## 5. Where to look for more

Each batch's notes, `shopify/notes-SH-50.md` to `notes-SH-57.md`, hold the cases behind each rule, the cases left open and the leads no line takes; `review-H-rulings.md` holds each ruling in full. Read a batch's notes only where a case is needed.
