# Shopify's `merchant-changelog`: the rules in force

This digest serves SH-42 to SH-46; where it differs from the notes and rulings it draws on, they govern. In brackets, `SH-36/8` is SH-36's rule 8 and "case 5" an entry its notes left open; "check" and "ruling" name the coordinator's after a batch, and "the corrections" the rulings' corrections made with the Editions digest.

## 1. What the entries are

Each entry is one post as its page states it: date, title, type tags, area, text, links and media (SH-34/1), in observed-sh at `e38dc17e3`, `structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl`. SH-42 to SH-46 hold its last 606 posts, lines 1041 to 1646, from 22 March 2023 back to 3 August 2018, all from the run `20261030T234414Z-merchant-changelog-feed-posts`; the 367 from 2018 to 2021 have no type tag, as the register says.

## 2. The rules in force

### Reading a post

1. A post's own thing is what its title and text state as new, changed or removed, the text governing where it narrows the title. A lead to an empty cell is read before it is set aside, and a cell's note sending a thing elsewhere is followed (SH-34/2; SH-36/8).
2. The area gives no line and no scope; it only chooses between two capabilities the text leaves open (SH-34/3; SH-35/3).
3. A reading begins with the date and type tag, if any, then the post's own release words ('rolls out gradually'), then why; the tag sets no support but for a retired feature (SH-34/4, 5).
4. Quotes are exact, typos included: words holding an apostrophe or single quotes go in “ ” (the checker doesn't flag one left in single quotes), those holding a straight double quote are named unquoted; a quote beyond the entry cites its WARC record or the other entry's id (SH-34/1, 14; check SH-40).
5. A further line goes to another capability's thing the text states as new or changed: a second feature; the admin place where it is set, if another capability's; each item of a list stating what is done there; each list page it changes; each page an export appears on (SH-34/7; SH-36/7; SH-38/6).
6. No line goes to what is named in passing: the data a feature reads; a list of places, fields, metrics, uses or examples; what a section or dashboard lists; a way named to customize the feature (SH-34/7; ruling SA-41; SH-37/5; check SH-38).
7. A learn-more link gives no line and isn't read; a post is about the app whose page its link opens, where its words name no other (Shop's, for a Shop help page); a setting an admin link names takes the line of the cell citing that place, an app's admin page no CM-APP-007 line (ruling SH-38; SH-39/8; SH-36/13; SH-35/10).

### Support and makers

8. `core` is a feature of Shopify's own admin, POS, checkout, customer accounts, analytics, settings or API; its brand names no maker. 'We' improving the platform's own (POS, Payments, the Theme Store, App Store, free themes, the Shopify app) leaves it `core` (SH-34/6; SH-37/14; ruling SH-53).
9. An admin section the platform's words call part of its admin is `core` whatever its route's permission, as is Shopify Balance, the admin's own account (ruling SH-2; the corrections).
10. `own-service` needs held words naming Shopify the maker of a separate app, product or service: 'we' making, upgrading or shipping it, 'we’ve added … to X', 'our … in X', 'first-party', 'from Shopify', 'we built', a store listing's developer. Naming an app, or 'our help docs', is none (rulings SH-35, SH-2, SH-55, SH-41).
11. Such words in any held post make every line on the app's own features `own-service`, renames included; its plan lines, admin page and the plans' sales channels stay `core`, others' extensions `extension-point` (rulings SH-37, SH-55).
12. This holds for a separate product or service too, its admin routes and plan rows `core`, and a post filed under Apps naming Shopify its feature's maker makes the app Shopify's (ruling SH-41, overturning SH-41/3).
13. An app or a separate product with no maker statement held is `shows` on its feature's capability, the maker a gap, whatever its name; its admin page (CM-APP-007), its admin route or section and a plan line that includes it are `core`; it is `extension-point` only where a third party is shown making it (the ruling after SH-43, which replaces ruling SH-36's 'core by what the post shows'). A built-in tool no held words call an app, such as the Pixel Helper, is the admin's own, `core` (check SH-58).
14. A first-party app's feature takes another capability's `own-service` line only where the app provides that thing, not for a means such as an API it uses (ruling SH-57; check SH-41).
15. A first-party app's own release takes CM-APP-011, a post on its features none; its use of an extension interface is `shows` on that interface's capability (SH-41/1; SH-38/5).
16. Shop's things are `own-service` on SH-S-0056 (its app, sign-in, synced carts, Shop Cash, Shop Campaigns); what it does in its own channel stays on CM-CHN-002, and it is no filler (ruling SH-34; SH-34/11; checks SH-36, SH-37).
17. Shop Promise is `core;own-service` on CM-SHP-018, the date the platform's, the guarantee Shop's; a Shop Pay post naming Shop's site is CM-PAY-014 `own-service` (SH-39/8; SH-40/8).
18. Hardware Shopify sells (card readers, POS Terminal, POS Go, the POS Hub) is CM-POS-002 `own-service` on the cell's maker evidence, its countries the scope (SH-35/6; SH-40/14).
19. `extension-point` is apps or third parties doing it through what the platform provides (ShopifyQL, extensions, App Store apps named as the way); an API naming an unnamed outside system is `core` unless apps or partners do the work (SH-34/6; check SH-34; the corrections).
20. `outside` is a third party named doing it with no interface of the platform named; naming Shopify's surface too makes it `core`, the party the filler (SH-34/6).

### Scope

21. Scope is the post's words for plan, country, store, market or subscription ('POS Pro', 'basic plan and up'), quoted where they hold 'and' (SH-34/10; ruling SH-38).
22. In `reading`: 'all Shopify plans', 'available to all merchants', 'eligible merchants' unexplained, a plan's default, an app version, the store's own setup, a required permission (SH-34/10; SH-38/7; SH-40/10).
23. Listed countries are a feature's scope, not market data, as are a destination's states or a buyer's country (SH-35/4; SH-41/12).
24. A line takes its own scope where its thing is stated under its own condition, a second line on one capability if need be; one service whose destinations differ keeps one line. This replaces SH-34/10's keeping such a condition in `reading` (rulings SH-34, SH-69; SH-36/9).
25. Features opened to more plans take those plans, and what is said to 'remain exclusive to Plus' a second line scoped Plus (SH-35/2).
26. A kind of store the criteria name is scope ('not a dropshipping store'), a sales minimum or follower count a quality, the store's own data and partners' other criteria `reading` (SH-41/7).
27. `;` separates alternatives and ` and ` adds a condition, joining two lists each read alone (rulings SA-53, SH-38).
28. A paid add-on's offer takes its site as scope, a feature coming with it the add-on ('POS Pro'); a line on CM-MKS-003 itself takes no add-on scope (ruling SH-70; the corrections).

### Release markers and retired features

29. A feature the merchant can enable before release is `core`, its plans the scope, the preview in `reading`; early access and experiments for some merchants are `shows`, a release to all `core` (ruling SH-34; SH-34/6; SH-36/6; SH-37/7).
30. A post that retires, replaces or renames takes the replacement's or renamed thing's line, the old one and its dates in `reading`; a retired feature with no replacement is `shows`, its capability its alone or not (SH-34/9; SH-38/3).
31. A setting retired from an app for third-party apps is `shows`, the apps `extension-point`; a retired app replaced by the platform's settings, apps named for one case, takes one `core;extension-point` line on the replacement (SH-38/4; SH-40/5).
32. A feature withdrawn in one country is `shows`, the country its scope, the authority that ended it its filler; a way named in its place takes a `core` line (SH-39/1).
33. A third party's role ended by a rule change goes in `reading`, not a filler, the line supporting what replaces it; so does a role stated only as background (SH-36/3; SH-37/10).

### Capabilities that recur

34. A POS app feature takes CM-POS-001, and a line for another capability's thing (local delivery CM-SHP-008, counts CM-INV-003, pickup CM-SHP-007, abandoned checkouts CM-CHK-007, receipts CM-ORD-009, draft orders CM-ORD-005, transfers CM-INV-006, reports CM-ANL-002, CM-ANL-003, extensions CM-POS-004); its staff carts aren't CM-CHK-010 (SH-34/8).
35. A card network for POS payments takes CM-PAY-021 (the network the filler, the countries the scope) beside CM-POS-001; cash rounding is CM-POS-003 (SH-39/4; SH-37/12).
36. The web admin's frame (look, loading, navigation) is `out`, its search and saved views new things, the Shopify app's navigation CM-SRF-001 `core`; any other post that names a feature is never `out` (ruling SH-37, changing SH-37/2; SH-34/13; SH-39/6).
37. A post announcing only an Edition is CM-ONB-003 `core`. Checkout settings are CM-CHK-001, metafields CM-CNT-002, the bulk editor CM-CAT-001 and Home's metrics CM-ANL-003 (SH-34/7, 13; SH-36/10; SH-40/2).
38. A checkout or theme by market and a kind of market take CM-MKS-001 too; a country's provinces are CM-MKS-009, a market's adapted prices CM-MKS-006 (SH-35/7; SH-37/8; check SH-34).
39. A Markets Pro or Managed Markets post is CM-MKS-003 `core`, Global-e `outside` where named, with lines for what it names elsewhere, its order limits by country a quality (SH-39/2; SH-40/1). 'Our Merchant of Record capability' (SH-E-9e3f5c76) names an admin service, as the cell reads Managed Markets, not a separate product, so it is not `own-service` (the coordinator, settling this digest; the Editions' lines aligned).
40. Customs data (HS codes, origin, customs documents, CPSC eFiling fields) is CM-SHP-020 `core`, a buyer's tax ID at checkout CM-TAX-005 (check SH-34); Shopify Tax is CM-TAX-002 `core`, the Tax Platform's partners CM-TAX-004 `extension-point` (SH-40/12).
41. A claim on a label bought in Shopify is CM-SHP-022, a carrier's parcel pickup CM-SHP-002 (check SH-38; SH-39/11).
42. Address validation and autocompletion are CM-CUS-009, a location's address CM-INV-005, the storefront's CAPTCHA CM-CUS-012 (SH-38/10; SH-39/12, 14). A country's address fields or postcode rules are CM-CUS-008, with CM-CHK-001 where the post says at checkout (SH-34 case 5; SH-37; the coordinator, settling this digest: SH-41's line aligned).
43. A discount without a code is CM-MKT-003 `core`, apps' and Functions' automatic discounts `extension-point`; recommendations the merchant curates or the platform makes are CM-MKT-023 (checks SH-34, SH-35, SH-38).
44. Checkout Extensibility is CM-CHK-004 `extension-point`, the checkout editor and customizations report CM-CHK-003 `core`; rules that block a checkout are CM-CHK-005 (SH-40/15; checks SH-35, SH-41).
45. A gift card sent with a message is gifting, CM-LOY-006 `core` beside CM-LOY-002, its emails CM-NTF-001 (SH-40/6, 7).
46. Each permission a post announces is `core` on what it gates, only one over roles or permissions themselves on CM-STF-002; logs of staff's or apps' actions are CM-TRU-003 (ruling ZD-7; SH-41/8; check SH-34).
47. An organization's features take each its line (SH-38/8). A CSV export or import that is the post's own thing also takes CM-MIG-001, not as a mere means nor for the platform's bills (SH-37/3; SH-40/3).
48. Collabs' commissions and affiliate links take CM-MKT-014, its creators CM-MKT-015; the Subscriptions app is CM-SEL-001 `own-service`, buyers pausing in their accounts CM-CUS-010 `core` (SH-41/6; SH-40/13).
49. The Theme Store is CM-SFR-003; the Finance section `new:Finance` `core`, its products no line (SH-37/1; SH-39/5).
50. Unit pricing, a price kept on the product record, is CM-CAT-001 `core`; CM-CAT-013 is the platform's automatic pricing (check SH-34; the ruling after SA-25; the coordinator, settling this digest: SH-39's line aligned).

### Other readings

51. A filler is a third party the post names doing it or a law or authority setting its terms (CPSC); Shop, the merchant's own tools and a company named with no role are none (SH-34/11; SH-38 case 11).
52. A quality is a limit, fee, duration or minimum stated for the feature ('up to 20 barcodes to a variant', the price 'free'); example values, counts of currencies or categories and app versions are not (SH-34/12; SH-37/1, 9).
53. A merchant's responsibility a post names takes `shows` on the capability whose terms it gives, as a how-to does on what the merchant does there (SH-40/11; SH-35/8).

## 3. The first-party apps and products

The Editions digest's table, with the changelog's additions; each app's plan lines and admin page stay `core`.

| App or product | Own features | Maker statement |
| --- | --- | --- |
| Shop | `own-service` | SH-S-0056 |
| Shopify Audiences | `own-service` | SH-E-234dcbd7 |
| Shopify Collabs | `own-service` | SH-E-709b37e4; SH-S-2760 |
| Planet | `own-service` (`new:Planet`) | SH-E-bc581483 |
| Search & Discovery | `own-service` | SH-E-9b869699 |
| Shopify Bundles | `own-service` | SH-E-1d272a37, SH-E-88c8359c |
| Shopify Subscriptions | `own-service;extension-point`, as aligned | SH-E-4c0f3472 |
| Combined Listings | `own-service`; its plan rows `core` | SH-E-dc618719: 'We’ve improved how all products … are listed', 'From a new app for merchandising products' (the changelog's lines aligned) |
| Shopify Email (Messaging) | `own-service` | SH-E-32e5ccc3; rename SH-E-6be48c3e |
| Shopify Inbox | `own-service` | SH-S-2758; SH-E-4f0c8272 |
| Stocky | `own-service` | SH-E-5b89aa16 |
| Shopify Flow | `own-service` | SH-E-0678ff26, SH-E-aca9896c |
| Shopify Collective | `own-service` | SH-E-850b28ae |
| Translate & Adapt | `own-service` | SH-E-04551fad |
| Checkout Blocks | `own-service` | SH-E-a2643162 |
| Fulfillment Network | `own-service`, its partners `extension-point` | 'our network of 20+ distribution hubs…' (E16, SH-51) |
| Fraud Control | `own-service` | SH-E-8f406571 |
| ShopifyQL Notebooks | `own-service` | SH-E-3f85908b |
| Shopify Credit | `own-service`; routes and plan rows `core`, issuers `outside` | SH-E-e3a378a2 |
| Shop Pay apart from the platform | `own-service`, CM-PAY-014 | SH-S-0411, SH-S-0413 |
| POS hardware | `own-service`, CM-POS-002 | SH-S-7269, SH-S-7251 |
| POS Terminal | `own-service`, CM-POS-002 | SH-E-dbb979f6: 'POS Terminal, Shopify’s newest, most powerful payment device' (the Editions' lines aligned) |
| Shopify Balance | `core`, the admin's own account | not a separate product |
| Customer View app | `core`, part of POS (check SH-38) | not a separate app |
| Pixel Helper | `core`, opened from the admin's Customer events (check SH-58) | SH-E-0a66f16d names its maker; a built-in tool, not a separate product |
| Forms, Marketplace Connect, Order Printer, Privacy & Compliance, Launch Check, SimGym, Product Network, Shopify Capital | `core` by what the post shows, the maker a gap (rule 13; SH-35) | none held |
| Google & YouTube app | its channel `extension-point`, YouTube or Google the venue (filler); the admin's Publishing section `core` | none held; the Editions' and SH-39's lines (the check after SH-42) |
| Bill Pay | `core` at `finances/billpay`, `shows` at `apps/bill-pay` | none held |

The Editions also hold a maker statement for Shopify Lending (SH-E-797024ee). Managed Markets is `core`, Global-e `outside` (rule 39), and POS Terminal `own-service` on every line (the row above). `held_entries.py makers --platform shopify NAME …` settles any other app, such as Oberlo or Shopify Chat.

## 4. The new things named so far

No Arabic name is held: the admin in Arabic isn't captured (`docs/GAPS.md`). The names to keep:
- Admin languages (SH-34), the admin's interface language, one new thing with Salla's `العربية / English` (ruling SA-49);
- Saved views (SH-35) and Admin search (SH-36), decided with Zid's and Salla's admin search (ruling SH-37);
- Tipping (SH-35's Tips, given SH-50's name at its check);
- Protection against unexpected redirects and Web Bot Auth (SH-36);
- Finance (SH-39), the admin's money section (M-13);
- Staff sales attribution and Quantity rules, the Editions' names (SH-50), which SH-41 kept.

The Editions' other new things keep their names (Editions digest). Batches wrote different supports for Tipping (`shows` SH-35, `core` SH-41) and Staff sales attribution; each is decided with its thing in `held/new.tsv` (check SH-35; Editions digest). A post that credits a sale to a staff member takes `new:Staff sales attribution` beside CM-POS-001 (SH-41; the coordinator, settling this digest: SH-34's and SH-39's posts aligned).

## 5. Where to look for more

Each batch's notes (`shopify/notes-SH-34.md` to `notes-SH-41.md`) hold the cases behind its rules and its open entries, and `review-H-rulings.md` each ruling in full; read them only where a case is needed. The notes also hold the rules left out here, on what no remaining post has: title-only posts, Sidekick, quick sale, Collective, Stocky, store credit, headless storefronts.

## 6. Rules added since the digest, as the coordinator kept them

From SH-42 (its notes give the cases):
- **C42.1:** a post making Shopify Payments available in a country is CM-PAY-002 `core`, scoped to the country, and each local method it names CM-PAY-017 `core`, the method its filler.
- **C42.2:** Payments for POS on a card reader takes CM-PAY-021 `core`, CM-POS-002 `own-service` and CM-POS-001 `core`.
- **C42.3:** an API field, object or topic is `core` on its feature's capability, `extension-point` where its words say apps do the work.
- **C42.4:** an API version's support notice is CM-API-006 `core`; the breaking changes it lists take no line.
- **C42.5:** the admin's own address is its frame and takes no line; embedded apps that must update take CM-APP-007 `extension-point`.
- **C42.6:** a first-party app's launch post takes CM-APP-011 and an `own-service` line for each feature it names.
- **C42.7:** analytics an app gives about its own feature are CM-ANL-001 `own-service`.
- **C42.8:** a country's subdivisions added to shipping zones take CM-SHP-001, CM-MKS-009, CM-CUS-008 and CM-CHK-001.
- **C42.9:** SCIM provisioning: the roles are CM-STF-002 `core`, the identity providers that assign them `extension-point`, and their fillers.
- **C42.10:** a capability's note governs over a shared word: a draft order's invoice email is CM-ORD-005.
- **A third party that syncs the store's data from its own admin, through the platform's sign-in, is `extension-point`**, as QuickBooks with Shopify Balance (the check after SH-42; B-extent).

From SH-43:
- **C43.1:** a customer notification option retired, with third parties' apps named as the way to keep it, takes those apps' `extension-point` line.
- **C43.2:** a refund paid as a gift card is CM-LOY-002 `core` and CM-RET-002 `shows`.
- **C43.3:** Handshake's posts have no maker statement held, so they are `shows` on their capabilities: the suppliers' side CM-B2B-001, the retailers' side CM-CAT-010, its own listings CM-CHN-004, its discounts CM-MKT-003 (the ruling after SH-43).
- **C43.4:** a feature available only 'on some stores', with no reason given, is `shows`. The words go in `reading`.
- **C43.5:** an App Store app with no maker held is `shows` on its feature's capability, the maker a gap. The cases are the Store Importer and the Customer Privacy app (the ruling after SH-43).
- **C43.6:** third parties' financial apps that reach Balance through the platform's partner take CM-PAY-023 `core;extension-point`, the partner and the apps its fillers.
- **C43.7:** a free theme's launch, or a version of one, is CM-SFR-001 `core`.
- **C43.8:** card networks that Shopify Payments starts taking in a country are CM-PAY-002 `core`, the networks its fillers.
- **C43.9:** a post that names only some of the tasks new staff permissions delegate gives each named permission a `core` line on what it gates.
- **C43.10:** a post making Flow available on more plans is a plan line, `core`. Flow's own features stay `own-service`.
- **The platform's possessive before a thing ('Shopify's Geolocation app') names it as the provider:** `own-service` (the check after SH-43).

The next batches number their rules C44.1 and on, by batch.

