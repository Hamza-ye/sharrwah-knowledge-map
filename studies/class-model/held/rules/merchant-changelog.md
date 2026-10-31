# Shopify's `merchant-changelog`: the rules in force

This digest serves SH-42 to SH-46; where it differs from the notes and rulings it draws on, they govern. In its brackets, `SH-36/8` is rule 8 of SH-36's notes, "SH-36 case 5" an entry those notes couldn't tell, "check SH-36" the coordinator's check at their end, "ruling SH-55" the ruling after SH-55 in `review-H-rulings.md`, and "the corrections" that file's corrections made with the Editions digest.

## 1. What the entries are

Each entry is one post as its page states it: date, title, type tags, area, text, links and media (SH-34/1), in observed-sh at `e38dc17e3`, `structures/shopify/merchant-changelog/changelog.shopify.com@posts/items.jsonl`. SH-42 to SH-46 hold its last 606 posts, lines 1041 to 1646, from 22 March 2023 back to 3 August 2018, all from the run `20261030T234414Z-merchant-changelog-feed-posts`. 367 of them have no type tag, as the register says of posts from 2018 to 2021.

## 2. The rules in force

### Reading a post

1. A post's own thing is what its title and text state as new, changed or removed, the text governing where it narrows the title. A lead to an empty cell is read before it is set aside (SH-34/2).
2. The area (Admin, Apps, Plus …) gives no line and no scope; it only chooses between two capabilities the text leaves open (SH-34/3; SH-35/3).
3. A reading begins with the date and type tag, then the post's own release words ('rolls out gradually', 'Starting October 1, 2026'), then why. The tag sets no support (SH-34/4, 5).
4. A title-only post is placed by its title, else by its page, else as its twin of the same date and area, a marked reading (SH-38/1).
5. Quotes are exact, typos included. Words holding an apostrophe or the source's single quotes go in “ ”, which the checker doesn't test; words holding a straight double quote are named unquoted. A quote beyond the entry cites `raw/runs/<run>/fetch.warc.gz@<offset>`, or another held entry's id (SH-34/1, 14; SH-39; check SH-40).
6. A further line goes to another capability's thing the text states as new or changed: a second feature; the admin place, another capability's, where the feature is set; each item of a list ('What's included', 'What's new') stating what is done there; each list page a post changes; each page an export appears on (SH-34/7; SH-36/7; SH-38/6).
7. No line goes to what is named in passing: the data a feature reads; a list of places, fields, metrics, uses or examples; the features a section gains; what a dashboard lists; a way to customize the feature ('You can use Checkout Blocks to …') (SH-34/7; ruling SA-41; SH-37/5; SH-39/7; check SH-38).
8. A learn-more link gives no line and isn't read. A post is about the app whose page its link opens, where its words name no other, and about Shop's feature if it links a Shop help page. A setting an admin link names takes the line of the cell citing that place; an app's admin page takes no CM-APP-007 line (ruling SH-38; SH-39/8; SH-36/13; SH-35/10).
9. A cell's note that sends a thing elsewhere is followed (SH-36/8).

### Support and makers

10. `core` is a feature of Shopify's own admin, POS, checkout, customer accounts, analytics, settings or API. Its brand names no maker, and 'we' improving the platform's own (POS and its Customer View app, the Theme Store, App Store, free themes, the Shopify app, Payments, Tax, Shopify Magic in an app) leaves it `core` (SH-34/6; SH-37/14; check SH-38; SH-39; rulings SA-41, SH-53).
11. An admin section the platform's words call part of its admin is `core` whatever its route's permission. Shopify Balance is the admin's own account, `core`, whatever 'we've added … using Shopify Balance' says (ruling SH-2; the corrections).
12. `own-service` needs held words naming Shopify the maker of a separate app, product or service: 'we' making, upgrading or shipping it, 'we’ve added … to X', 'our … in X', 'first-party', 'from Shopify', 'we built', or a store listing naming its company as developer. Naming an app, or 'our help docs', is none (rulings SH-35, SH-2, SH-55, SH-41; SH-41/4).
13. Such words in any held post make every line on the app's own features `own-service`, renames included; its plan lines, admin page and the plans' sales channels stay `core`, others' extensions of it `extension-point` (rulings SH-37, SH-55).
14. This holds for a separate product or service too: Shopify Credit's features are `own-service`, its admin routes and plan rows `core`, its issuers `outside`. A post filed under Apps naming Shopify its feature's maker makes the app Shopify's: Fraud Control (ruling SH-41, overturning SH-41/3).
15. A Shopify-branded app or tool with no maker statement held is `core` by what the post shows, the maker a gap (ruling SH-36; SH-36/2).
16. A first-party app's feature takes another capability's `own-service` line only where the app provides that thing (Search & Discovery's recommendations, CM-MKT-023); a means or condition of its own thing (an API it uses, its bill) takes none (ruling SH-57; check SH-41).
17. A first-party app's own release takes CM-APP-011, a post on its features none; its use of an extension interface is `shows` there (CM-APP-008, CM-POS-004) (SH-41/1; SH-38/5; SH-39/3).
18. Shop's things are `own-service` on SH-S-0056: its app, accounts and shop.com, Sign in with Shop, leads captured through it, synced carts, reminders, pickup screens, Posts, Shop Cash, Shop Campaigns. What it does in its own channel stays on CM-CHN-002, and it is no filler (ruling SH-34; SH-35/5; checks SH-36, SH-37).
19. Shop Promise is `core;own-service` on CM-SHP-018, the date the platform's, the guarantee Shop's; a Shop Pay post naming Shop's site is CM-PAY-014 `own-service` (SH-39/8; SH-40/8).
20. Hardware Shopify sells (POS Hub, card readers, POS Terminal, POS Go) is CM-POS-002 `own-service`, on the cell's maker evidence (SH-S-7269, SH-S-7251), its countries the scope (SH-35/6; SH-39/4; SH-40/14).
21. `extension-point` is apps or third parties doing it through what the platform provides: ShopifyQL (outside tools too, CM-ANL-007), extensions, a carrier's listed service, App Store apps named as the way. An API naming an unnamed outside system is `core` unless apps or partners do the work (SH-34/6; check SH-34; SH-38/4; the corrections).
22. `outside` is a third party named doing it with no interface of the platform named (Global-e as merchant of record); naming Shopify's surface too makes it `core`, the party the filler (SH-34/6).

### Scope

23. Scope is the post's words for plan, country, store, market or subscription ('POS Pro', 'basic plan and up'), quoted where they hold 'and' (SH-34/10; SH-38/7; ruling SH-38).
24. In `reading`: 'all Shopify plans', 'available to all merchants', 'eligible merchants' unexplained, a plan's default ('Enabled by default for Plus merchants'), an app version, the store's own setup, a required permission (SH-34/10; SH-38/7; SH-40/10, 12).
25. Listed countries are a feature's scope, not market data, as are a destination's states or a buyer's country (SH-35/4; SH-41/12).
26. A line takes its own scope where its thing is stated under its own condition, a second line on one capability if need be; one service whose destinations differ keeps one line. This replaces SH-34/10's one scope per entry (rulings SH-34, SH-69; SH-36/9).
27. Features opened to more plans take those plans, and what is said to 'remain exclusive to Plus' a second line scoped Plus (SH-35/2).
28. A kind of store a post's criteria name is scope ('not a dropshipping store'), a sales minimum a quality; the store's own data and partners' criteria go in `reading` (SH-41/7).
29. `;` separates alternatives and ` and ` adds a condition, joining two lists each read alone (rulings SA-53, SH-38).
30. A paid add-on's offer takes its site as scope, a feature coming with it the add-on ('POS Pro'); a line on CM-MKS-003 itself has no add-on scope (ruling SH-70; the corrections).

### Release markers and retired features

31. A feature the merchant can enable before release is `core`, its plans the scope, the preview in `reading`: Feature test drives (CM-EVO-001), SimGym's 'AI Research Preview' open to all eligible merchants (ruling SH-34; checks SH-34, SH-35).
32. Early access and experiments for some merchants are `shows` ('Contact Plus Support to enable', 'during experimentation'), a release to all `core` (SH-34/6; SH-36/6; SH-37/7).
33. A post that retires, replaces or renames takes the replacement's or renamed thing's line, the old one and its dates in `reading`: Scripts to Functions, Markets Pro to Managed Markets (SH-34/9; SH-35/3; SH-39/2).
34. A retired feature with no replacement is `shows`, its capability its alone or not (SH-34/9; SH-38/3).
35. A setting retired from an app for third-party apps: the setting `shows`, the apps `extension-point`. A retired app replaced by the platform's settings, apps named for one case: one `core;extension-point` line on the replacement (SH-38/4; SH-40/5).
36. A feature withdrawn in one country for a named way: the feature `shows`, the country its scope, the authority its filler, the way `core` (SH-39/1).
37. A third party's role ended by a rule change: the line supports what replaces it, the former role in `reading`, as a role stated as background is (SH-36/3; SH-37/10).

### Capabilities that recur

38. A POS app feature takes CM-POS-001, and a second line for another capability's thing: local delivery CM-SHP-008, counts CM-INV-003, pickup CM-SHP-007, abandoned checkouts CM-CHK-007, receipts CM-ORD-009, draft orders CM-ORD-005, transfers CM-INV-006, reports CM-ANL-002 and CM-ANL-003, extensions CM-POS-004. POS's staff carts aren't CM-CHK-010 (SH-34/8; SH-37/12).
39. A card network for POS payments takes CM-PAY-021, the network its filler and the countries its scope, beside CM-POS-001; cash rounding is CM-POS-003; quick sale in the Shopify app is CM-SRF-001 (SH-39/4; SH-41/11; SH-37/12; SH-35/1).
40. The web admin's frame (look, loading, navigation) is `out`, a post's other things taking their lines; its search and saved views stay new things; the Shopify app's navigation is CM-SRF-001 `core` (ruling SH-37, changing SH-37/2; SH-39/6).
41. Sidekick doing a task takes CM-AIA-002 alone, added to another capability's editor that editor's line; AI for merchants outside the admin goes on the place's capability, not CM-AIA-001 (SH-35/9; SH-36/5; the corrections).
42. A post announcing only an Edition is CM-ONB-003 `core` (SH-34/13).
43. Places where a feature is set take their line: Checkout settings CM-CHK-001, metafields CM-CNT-002, return rules CM-CNT-008, test drives CM-EVO-001, product disclosures CM-TRU-010, the Developer Dashboard CM-PTN-001, the bulk editor CM-CAT-001; Home's metrics are CM-ANL-003 (SH-34/7; SH-36/10; SH-40/2).
44. A checkout or theme by market and a kind of market take CM-MKS-001 too; a country's provinces are CM-MKS-009, the country the scope; a market's adapted prices CM-MKS-006 (SH-35/7; SH-37/8; check SH-34).
45. A Markets Pro or Managed Markets post is CM-MKS-003 `core`, Global-e unnamed, with lines for what it names elsewhere (labels and pickups CM-SHP-002, zones CM-SHP-001, payouts CM-PAY-005); its order limits for listed countries are CM-MKS-003's quality (SH-39/2; SH-40/1; SH-41/10). **Unsettled:** the Editions make CM-MKS-003 `own-service` on 'Our Merchant of Record capability' (SH-E-9e3f5c76; E35, SH-55); no check says if changelog lines follow.
46. Customs data (HS codes, origin, customs documents, CPSC eFiling fields, tax IDs on invoices) is CM-SHP-020 `core`; a buyer's tax ID at checkout (Brazil's CNPJ) is CM-TAX-005 (check SH-34).
47. A claim on a label bought in Shopify is CM-SHP-022, DHL On Demand Delivery CM-SHP-017 `extension-point`, a carrier's pickup of parcels CM-SHP-002 (checks SH-34, SH-38; SH-39/11).
48. Address validation has no capability of its own: buyers', companies' and orders' addresses go on CM-CUS-008, a location's on CM-INV-005, autocompletion on CM-CUS-009; the storefront's CAPTCHA is CM-CUS-012, a marked reading (SH-38/10; SH-39/12, 14). **Unsettled:** a country's address fields at checkout: CM-CUS-008 in SH-34 (case 5), CM-CHK-001 in SH-41, which names CM-CUS-009 (the Editions' validation at checkout) and CM-MKS-009 as alternatives.
49. Shopify Tax is CM-TAX-002 `core`, its report's places taking theirs; the Tax Platform's partners are CM-TAX-004 `extension-point` (SH-40/12).
50. A discount without a code is CM-MKT-003 `core`, apps' and Functions' automatic discounts `extension-point`; curated or platform recommendations are CM-MKT-023; payment links CM-PAY-032 (checks SH-34, SH-35, SH-38).
51. Rules that block a checkout (Checkout Blocks', Fraud Control's) are CM-CHK-005 `own-service`; apps' blocks are CM-CHK-004 `shows`, Checkout Extensibility `extension-point` there, the checkout editor CM-CHK-003 `core` (checks SH-35, SH-41; SH-40/15).
52. Store credit as a refund is CM-LOY-001 `core`; CM-RET-002 takes `shows`, or `core` where the original payment method is named too, and the flow it is offered in its line (cancellation CM-ORD-004, returns CM-RET-003) (SH-37/4).
53. A gift card sent to a recipient with a message is gifting, CM-LOY-006 `core` beside CM-LOY-002; its emails take CM-NTF-001 (SH-40/6, 7).
54. Each permission a post announces is `core` on what it gates; only one over roles or permissions themselves goes on CM-STF-002 (ruling ZD-7; SH-37/13; SH-41/8, 9).
55. An organization's features take each its line (the organization CM-ACC-003, store transfers CM-ACC-001, billing CM-PLN-004 and CM-PLN-005, users CM-STF-001, roles CM-STF-002, two-step CM-TRU-001); a headless or Hydrogen storefront as a channel takes CM-SFR-011, CM-CHN-001 and CM-CHN-007 (SH-38/8, 9).
56. A CSV export or import that is the post's own thing takes CM-MIG-001 too, not where it is only the means, nor for the platform's bills (CM-PLN-004) (SH-37/3; SH-40/3).
57. Logs of staff's or apps' actions are CM-TRU-003; custom apps CM-APP-009; development stores CM-DVT-004 (checks SH-34, SH-36).
58. Collective's orders, price lists, payment status and margins take CM-CHN-005 alone, retailers' sourcing CM-CAT-010 `shows` beside it, as its note asks (SH-39/9; SH-40/4; check SH-41). **Unsettled:** SH-39/9 adds CM-SHP-001 for shipping profiles, while ruling SH-57 keeps Collective's supplier shipping rates in CM-CHN-005.
59. Stocky's purchase orders are CM-INV-007 `own-service`, its transfers CM-INV-006; Collabs' commissions and affiliate links CM-MKT-014, its creators CM-MKT-015; the Subscriptions app's features CM-SEL-001 `own-service`, the accounts where buyers pause them CM-CUS-010 `core` (SH-39/3; SH-41/6; SH-40/13).
60. The Theme Store is CM-SFR-003 `core`; the Finance section is `new:Finance` `core`, the products it lists no line (SH-37/1; SH-39/5).
61. **Unsettled:** unit pricing is CM-CAT-001 in SH-36 (case 5) and CM-CAT-013 in SH-39, a marked reading sent to the final review; fulfillable inventory is CM-SHP-001 in SH-36 (case 6) and CM-INV-001 `shows` in SH-40 (case 3).

### Other readings

62. A filler is a third party the post names doing it (carriers, ad platforms, identity providers, Global-e, a payment method's brand) or a law or authority setting its terms (CPSC, the Windsor Framework); Shop, the merchant's own tools and a company named with no role are none (SH-34/11; SH-38 case 11).
63. A quality is a limit, fee, duration or minimum stated for the feature ('up to 20 barcodes to a variant', the price 'free'); example values, counts of currencies or categories and app versions are not (SH-34/12; SH-37/1, 9).
64. A merchant's responsibility a post names takes `shows` on the capability whose terms it gives, as a how-to does on what the merchant does there (SH-40/11; SH-35/8).
65. A post that names a feature is never `out` (SH-34/13).

## 3. The first-party apps and products

The Editions digest's table, with the changelog's additions; each app's plan lines and admin page stay `core`.

| App or product | Own features | Maker statement |
| --- | --- | --- |
| Shop | `own-service` | SH-S-0056; ruling SH-34 |
| Shopify Audiences | `own-service` | SH-E-234dcbd7 |
| Shopify Collabs | `own-service` | SH-E-709b37e4; SH-S-2760 |
| Planet | `own-service` (`new:Planet`) | SH-E-bc581483 |
| Search & Discovery | `own-service` | SH-E-9b869699 |
| Shopify Bundles | `own-service` | SH-E-1d272a37, SH-E-88c8359c |
| Shopify Subscriptions | `own-service;extension-point`, as aligned | SH-E-4c0f3472 |
| Combined Listings | `own-service` in the Editions, `core` with the maker a gap in the changelog (check SH-39): **unsettled** | SH-E-dc618719 |
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
| Shopify Credit | `own-service`; routes and plan rows `core` | SH-E-e3a378a2 |
| Shop Pay apart from the platform | `own-service`, CM-PAY-014 | SH-S-0411, SH-S-0413 |
| POS hardware (POS Hub, card readers, POS Terminal, POS Go) | `own-service`, CM-POS-002 | SH-S-7269, SH-S-7251; POS Go SH-E-fc9fba8c |
| Shopify Balance | `core`, the admin's own account | not a separate product |
| Customer View app | `core`, part of POS (check SH-38) | not a separate app |
| Shopify Capital | `core` by what the post shows (SH-35) | none held here |
| Forms, Marketplace Connect, Order Printer, the Pixel Helper, Privacy & Compliance, Launch Check, SimGym, Product Network, Google & YouTube | `core`, the maker a gap (rule 15); the YouTube programme `extension-point` | none held |
| Bill Pay | `core` at `finances/billpay`, `shows` at `apps/bill-pay` | none held |

The Editions hold maker statements for Managed Markets (SH-E-9e3f5c76; rule 45) and Shopify Lending (SH-E-797024ee), and keep POS Terminal `shows` where its card names no maker (their rule 15). `held_entries.py makers --platform shopify NAME …` settles any app not listed.

## 4. The new things named so far

No Arabic name is held: the admin in Arabic isn't captured (`docs/GAPS.md`). The names to keep:
- Admin languages (SH-34): the admin's own interface language, one new thing with Salla's `العربية / English`, decided in `held/new.tsv` (ruling SA-49);
- Saved views (SH-35) and Admin search (SH-36), decided with Zid's and Salla's admin search (ruling SH-37);
- Tipping (SH-35's Tips, given SH-50's name at its check);
- Protection against unexpected redirects and Web Bot Auth (SH-36);
- Finance (SH-39), the admin's section over Capital, Credit, Balance, Payments, Bill Pay and Taxes (M-13);
- Staff sales attribution and Quantity rules, the Editions' names (SH-50), which SH-41 kept.

The Editions' other new things keep their names here (Editions digest, section 4). SH-37's Admin loading and Admin navigation are `out` (ruling SH-37). Batches wrote different supports for Tipping (`shows` SH-35, `core` SH-41) and Staff sales attribution; each is decided with its thing in `held/new.tsv` (check SH-35). **Unsettled:** a POS post on staff credited with a sale takes CM-POS-001 alone in SH-34 and SH-39 (case 12), and `new:Staff sales attribution` beside it in SH-41.

## 5. Where to look for more

Each batch's notes (`shopify/notes-SH-34.md` to `notes-SH-41.md`) hold the cases behind its rules, the entries left open, the leads no line takes and the tools' problems; `review-H-rulings.md` holds each ruling in full. Read a batch's notes only where a case is needed. The checker's CHANGES repeat cells earlier batches changed, the model not being amended between batches; such repeats stand (check SH-41).
