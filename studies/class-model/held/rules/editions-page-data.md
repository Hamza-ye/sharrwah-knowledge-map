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
8. The platform's free themes are `core` on CM-SFR-001 and CM-SFR-007 (E21, SH-53, overturned after SH-53: 'Our free themes' makes no separate service).
9. Shopify POS is the platform's own client, `core` on CM-POS-001 (E22, SH-53; the ruling after SH-55).
10. A card is `own-service` where it or a held statement names Shopify the maker of a separate app, product, device or service ('a new app from Shopify'); 'our help docs' and 'our official fulfillment partner Flexport' name none (E3, SH-50; the ruling after SH-55; E50, SH-56).
11. Shop's things are `own-service`: its Store (CM-CHN-002, where others' Shop Minis are `extension-point`), sign-in (CM-CUS-010), reviews (CM-SUP-001), lead capture (CM-CUS-007), Shop Promise (CM-SHP-018) and AI (CM-AIA-005) (the ruling after SH-34; E3, SH-50; the checks after SH-50 to SH-53). Shop Pay apart from the platform is CM-PAY-014 `own-service` (E23, SH-53).
12. A first-party app (from the App Store, at `apps/<handle>`, or 'the X app') is `own-service` on every line about its own features, renames included, 'wherever held words name the platform as its maker' ('we’ve added … to X', 'from Shopify', a store listing's developer). Its plan lines and admin page stay `core`, others' extensions of it `extension-point` (E3, SH-50, changed by the rulings after SH-35, SH-37, SH-53, SH-2 and SH-55).
13. With no maker statement held, a Shopify-branded app is `shows` plus CM-APP-007 `core` where the card links its `apps/<handle>` page, and `core`, the maker a gap, where named with no address; a plan statement for it is `core` (the ruling after SH-36; E22, SH-53; E28, SH-54).
14. CM-APP-011 `own-service` goes only where the card itself calls the app Shopify's (E3, SH-50; E29, SH-54).
15. A separate device or service whose maker a held card names is `own-service` (POS Go, Managed Markets, Shopify Lending); one with none stays `shows` (POS Terminal) (E35, SH-55; E55, SH-57).
16. A first-party app's feature takes another capability's line only where the app provides that thing: Stocky's transfers stand on CM-INV-006, while Collective's rates, inventory and price lists stay in its CM-CHN-005 `own-service` line, its sourcing side CM-CAT-010 `shows` (E35, SH-55; E54, SH-57, decided by the ruling after SH-57).
17. The platform's own developer tools are `core`, even 'built by Shopify' or for building apps. An API is `extension-point` where the card says apps do the work through it, else `core`, a Function API `extension-point` by definition, and webhooks the platform sends apps `core` on CM-API-008 and the events' capability (E3, SH-50, and its check; E24, SH-53; E45, SH-56).
18. **An API naming an unnamed outside system is `core`:** the platform's own API for its own feature, `extension-point` only where its words say apps or partners do the work (B-extent). The Inventory States API's 'across external platforms' (SH-51) and 'using APIs to sync cash tracking reports with your accounting software' (SH-57, aligned) are `core` (decided after the digest).
19. A card is `extension-point` where a third party's app, or one with no maker named, does the feature (its venue the filler), or it links an App Store category or collection (E3, SH-50); a non-Shopify-branded app at `apps/` adds CM-APP-007 `core` (E37, SH-55).
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
45. Managed Markets (formerly Markets Pro) is CM-MKS-003 `own-service` on 'Our Merchant of Record capability', `core` too where the card links `settings/markets/pro/apply`, and holds its duties and restricted products; its other features go on their own capabilities, `core`, scoped 'Managed Markets' (E35, E41, SH-55; E53, SH-57).
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
| Shopify Forms, Marketplace Connect, Order Printer, the Pixel Helper | `core`, the maker a gap (rule 13) | none held |
| Bill Pay | `core` at `finances/billpay`, `shows` at `apps/bill-pay` (E28, SH-54); the maker a gap | none held (SH-56) |

The devices and services with a maker statement are POS Go (SH-E-fc9fba8c), Managed Markets (SH-E-9e3f5c76) and Shopify Lending (SH-E-797024ee). SH-54 kept Shopify Fraud Control, the Privacy & Compliance app and ShopifyQL Notebooks without a maker, before `makers` existed. `held_entries.py makers --platform shopify NAME …` settles them and any app not listed.

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
