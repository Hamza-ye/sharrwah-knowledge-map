# SH-45: notes

Shopify's `merchant-changelog`, 130 posts from 15 June 2020 ("The Google Shopping app is now the Google channel") back to 4 April 2019, at observed-sh `e38dc17e3`. Effort `high`.

**What I read.** The brief; the structure's digest, `held/rules/merchant-changelog.md`, whole, and again after it changed on disk during the batch (section 6 gained SH-44's C44.1 to C44.7 and "Makers found since the table"); the last section of `review-H-rulings.md`; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the structure's `REGISTER.tsv` row (no `ledger-summary.tsv` row names the changelog); the structure's `selection.tsv` row and `show --meta`; B-extent's "Cells and evidence" and "Conventions from the dry run"; the evidence map. I read no batch's notes file: the digest covered the cases, and for precedents I used `earlier`, `makers`, `cells` and greps of earlier batches' placements (SH-34 to SH-44, SH-50s, SH-69, SH-72), each cited in the line that follows it. No post's page or run step was read beyond its entry: each post's own text settled its lines, so no source disagreed with an item and no run step adds a lead for the second stage.

**SH-44 ran beside this batch.** Its placements were in progress (193 lines, no notes) when I read them, for six precedents only: Shopify Ping (SH-E-fc4dc41e), Launchpad (SH-E-bd544a27), the Offset app on `new:Planet` (SH-E-fa9039af), a Shop Pay login line (SH-E-cea27e70), the Local Delivery app (SH-E-bddc1876) and a POS recommendations extension (SH-E-9f713b2a). My lines keep to them, except where C45.3 below reads Shop Pay otherwise.

## Rules I followed that the digest doesn't hold (for the coordinator)

- **C45.1: the platform's possessive before an app makes it Shopify's.** Two posts here use it on the Google channel: “Learn more about Shopify's Google channel” (SH-E-5eb470e8, the rename of the Google Shopping app to the Google channel) and “using Shopify's Google Shopping app” (SH-E-5835be14). By the check after SH-43 these are maker statements (`makers` finds both). So the channel's own features are `own-service`, with Google as the venue and filler (M-3): CM-CHN-001 for the channel, CM-CHN-004 for the free listings. **This goes against the digest's table row for the Google & YouTube app** ("none held"; its channel `extension-point`), which was written before the possessive rule and before these posts were read. Earlier `extension-point` lines name "the Google channel" or "the Shopify Google channel": SH-E-dc73c4db and SH-E-49db0469 on CM-CHN-001 and CM-CHN-004, SH-E-51e7df71 on CM-ANL-007. The Editions' Google & YouTube lines are separate. Only one rename is held, Google Shopping app to Google channel; no held statement here links the Google channel to the Google & YouTube app. The coordinator decides whether to align them.
- **C45.2: the Buy Button channel is a first-party app.** Its post SH-E-85d936a5 shows it as one: “Install the Buy Button channel”, which links its App Store listing, apps.shopify.com/buy-button; 'the new full-screen app'; and “we've made the following updates the the Buy Button channel”, a maker statement under rule 10 (the ruling after SH-55: an app installed from the App Store). So its own features are `own-service` (rule 11):
  - its buttons and their settings, CM-CHN-001 (SH-E-85d936a5, SH-E-b9275e37);
  - its checkout links, CM-CHK-008;
  - the discounts shown in its cart, CM-CHK-002;
  - the order notes in its cart, CM-ORD-013.

  The page where the action appears stays `core`: the product details page, CM-CAT-001 (C44.2). So do the platform's own features it reaches: abandoned checkout emails for Buy Button checkouts are CM-MKT-022 `core` (SH-E-e9b855c1). Earlier lines put the "Buy Button sales channel" on CM-CHN-001 `core` from an answer with no maker statement (SH-E-f35bf9c2, SH-E-737a2561, SH-E-728858eb), and the coordinator may align them. I first wrote SH-E-b9275e37 as `core` under rule 8, then corrected it once SH-E-85d936a5 showed the channel's App Store listing.
- **C45.3: Shop Pay (Shopify Pay) inside the store's checkout stays `core`, even under the platform's possessive.** Two posts open with 'Shopify’s fastest way to check out' (SH-E-9712f91d, SH-E-a530d0b5). I kept them `core` because of rule 17 and the table's own-service row, "Shop Pay apart from the platform", whose maker statements are already held (SH-S-0411, SH-S-0413): the posts' features run in the store's one-step checkout and name no Shop site. 'Our ongoing effort' in the rename post (SH-E-6a94e28f) names no separate product (rule 10). If the possessive governs here as it does in C45.1, rule 11 would make six lines `own-service`: the CM-PAY-014 lines of SH-E-6a94e28f, SH-E-8030aebd, SH-E-9712f91d, SH-E-0550703a, SH-E-a530d0b5 and SH-E-78e521ec. The lines on what is redeemed or chosen in its checkout would stay `core`, since they are the platform's own discount codes, gift cards and shipping rates (rule 14): CM-MKT-002 twice, CM-LOY-002 and CM-SHP-001.
- **C45.4: a carrier for marking orders fulfilled.** A carrier added to the list used when marking orders fulfilled, with its tracking address filled in automatically, is CM-SHP-017 `core`, the carriers its fillers and the country its scope. The cell's "Tracking carriers" value list is CM-SHP-017's, not CM-SHP-015's. The order fulfillment page where it is done takes CM-SHP-009 `core` (rule 5; C44.2). Cases: Japan (SH-E-fb2b5c10, SH-E-64041eb6) and Deutsche Post in Germany (SH-E-9aea8a57).
- **C45.5: a store's own currency limit is a quality.** 'sell in up to 10 currencies … from a single store' is a quality on CM-MKS-006 (SH-E-6ce82d77, SH-E-b72b53c8). I read rule 52's "counts of currencies" as the size of a supported list, such as '133 global currencies' (SH-E-5170c6b2), which gets no quality, not as one store's limit. If the coordinator reads rule 52 more strictly, both qualities are dropped.
- **C45.6: the platform's service status page.** A store-specific status page (shopifystatus.com) is CM-OPS-002 `core`. Status subscriptions the same post removes are `shows` on the same line, as `core;shows` (SH-E-622014ac). CM-OPS-004's note names the status page as a homonym that belongs on CM-OPS-002, which held nothing on Shopify.
- **C45.7: taxes on the platform's bills.** A country's tax on the platform's own bills is CM-PLN-007 `core`, the country its scope. The law requiring it isn't named, so it has no filler (SH-E-03efd856, South Africa; SH-E-b3d3fa43, Singapore).
- **C45.8: Shopify Ping and Shopify Chat.** The digest now lists both as `own-service`, on CM-SUP-004. The rest:
  - Apple Business Chat, connected through Ping, is the filler. SH-E-1d26678d names no Shopify app, but its only link opens Ping's help page on Apple Business Chat (rule 7).
  - Orders that Ping or Chat creates or sends in a conversation are draft orders, CM-ORD-005 `own-service`, as Stocky's transfers are stock transfers (the ruling after SH-57): SH-E-abbac630, SH-E-340a90f2.
  - 'apps that work with Ping' are `extension-point` (SH-E-ac2b4041).
  - A launch or new-device release takes CM-APP-011: the Android version (SH-E-7da656d8) and 'Announcing Shopify Chat' (SH-E-340a90f2). A post on a version's features does not (rule 15; Ping 2.0, SH-E-ac2b4041).
- **C45.9: Kit has no maker statement held.** `makers` finds only Retail Kit and Marketplace Kit. SH-E-29f4d991 is `shows` on CM-MKT-005 (rule 13), read through SH-E-78436754's 'you can use Kit or another app for social media marketing', which is an SH-46 entry. Facebook's limit on Messenger is a third party's role ended by its own rule, so it goes in `reading` (rule 33). Shopify Ping and SMS are named as the ways to keep talking to Kit, so they take no line.
- **C45.10: a third party's tool retired from the admin, then replaced.** A third party's tool removed from the admin, its replacement only promised, is `shows`, and the App Store collection named as the way is `extension-point`, on one line as `shows;extension-point` (SH-E-8c17ae8f; C43.1, rule 30). The later post with the replacement takes the `core` line (SH-E-655c626a).

## The new things

No Arabic names are held, because the admin in Arabic isn't captured (`docs/GAPS.md`).

- **`new:Storefront Signage Maker`** (SH-E-ab656ca5, `shows`):
  - **What it is:** a tool on the platform's public site, www.shopify.com/tools/signage-maker, for making a printed sign for the merchant's physical storefront ('open, available for curbside pickup, delivery, online and more'), from templates.
  - **Place of its own:** none. It is a public-site page, not an admin route or section, an API group, a plan line or an app category.
  - **Maker:** none held (`makers`: 0 entries). It is `shows` under rule 13, the maker a gap. A held statement on whether the tool is the platform's own, like the Pixel Helper, would make it `core`.
  - **Proposed:** domain D, area MKT, parent none, or CM-MKT-005 if the coordinator reads printed signage as a marketing activity.
  - **Searched:** signage; sign; sign maker; logo maker; business tools; free tools; flyer; poster; marketing materials; the MKT and ONB capability lists; no earlier placement cites shopify.com/tools.
- **`new:Tipping`** (SH-E-26377713, `core`): online tipping turned on for the checkout. It keeps the digest's name and is `core`, as SH-E-c1cc30bf's line is; the digest leaves its support to be decided with the thing.
- **`new:Saved views`** (SH-E-0842fb4f, `shows`): 'the saved searches that you create in Shopify', reached from the Shopify app. I gave it the digest's name, since a saved search on a list is a saved view (SH-E-1dc0cd80), and `shows` like that line. The post's own term is "saved searches", kept in `terms`.
- **`new:Planet`** (SH-E-39234b62, `own-service`): Offset (by Shopify), which the digest calls Planet's forerunner. It is placed on `new:Planet`, as SH-44 placed the Offset app.
- **`new:Admin languages`** (SH-E-c4c8d76b, `core`): the admin available in seven more languages, `core` as SH-E-19b0178e's line is.
- **`new:Staff sales attribution`** (SH-E-599b970e, `core`): POS sales credited to staff by line item, beside CM-POS-001 and a report on CM-ANL-002.

## Entries I couldn't tell, and what would settle each

- **SH-E-655c626a and SH-E-8c17ae8f, the image editor, are on CM-CAT-007.** The retirement post says the editor was on 'the Files, Products, and Online Store pages', so it may be CM-CNT-001 (Files) as well, or a thing of its own; no capability holds an image editor (searched image editor, image editing, crop, files, photo editor). A held statement of where the returned tool opens would settle it.
- **SH-E-85d936a5's CM-ORD-013 line** makes a cell that held nothing hold `own-service` only, on the Buy Button cart's order notes. A held statement of order notes in the platform's own cart or order page would add `core` beside it.
- **SH-E-c2ef851a and SH-E-90874717, paying the platform's bills with the balance.** The balance is named only as the means, so it takes no line. 'Don't wait for payouts' reads as the payments' balance (CM-PAY-005), though the area is Balance (CM-PAY-023). Neither is placed: CM-PLN-005 is the post's thing.
- **SH-E-c68ea76e, order editing in November 2019.** It is `shows` by C43.4 ('This feature is not yet available for all stores', no reason given), with each item of its list `shows` too: CM-ORD-002, CM-NTF-001, CM-ANL-002. If the coordinator reads 'not yet available for all stores' as a gradual rollout, which the rules treat as a release, its three lines become `core`.
- **SH-E-e1135220, the product recommendations API.** The post says 'we’re beta testing' but also 'released as a JSON API for our Plus merchants and Plus Partners', so I read a beta released to a plan: `core`, scope Plus (rule 29). If it is early access for some merchants, it is `shows`.
- **SH-E-c87b082c, support requests to apps' developers from the mobile app.** No capability holds an app's support (searched app support, support request, app developer). I placed it on CM-APP-001 as `extension-point`: the developers support their apps through the platform's request.
- **SH-E-96eb6d89, Arrive renamed Shop, takes CM-SHP-017 `own-service`** for 'Shopify's delivery tracking app', which 'goes beyond tracking' (SH-E-f2a9be20's line holds Shop's tracking). If the tracking is read as the old name's description only, the line is dropped and CM-CHN-002 stays.

## Leads to empty cells

- **Set aside after reading:** CM-ORD-013 for the Orders list's columns, a list of fields (SH-E-6d51862d), and for 'messages' in the chat posts; CM-OPS-004 for 'order status page' and 'status', which its note sends elsewhere; CM-ORD-003 for 'failed' (SH-E-1de7d2a1).
- **Given lines:** CM-OPS-002, CM-CUS-012, CM-MKT-003 (three posts), CM-MKT-023 (three posts) and CM-ORD-013 (C45.2).

## Problems with the brief or the script

- **The checker's notes on the platform's brand.** "core on a product named with the platform's brand" flags 27 lines whose brand names the platform's own feature: POS, Shopify Payments, Shopify Shipping, Shopify Mobile, Shop Pay within checkout, Shopify Marketing, Shopify Scripts, the Shopify Community and Help Center, the Experts Marketplace. I read each, and each is `core` under rule 8 or 13.
- **`makers` and 'from Shopify'.** `makers` counts 'from Shopify' as a cue in "post to your Facebook Page from Shopify" (SH-E-e6e2697f), where it names the admin. That is no maker statement for the Facebook Marketing app, so its maker stays a gap.
- **`earlier` printed no lines for 129 of the 130 entries:** these posts' titles are cited nowhere. The one hit, a label on SH-E-00ce92c1, is another entry's line.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 130 of 130 entries, no problem.
- **C45.1 is ruled as read** (the corrections after SH-45). The Google app is Shopify's own on two possessive maker statements, its features `own-service`, the venue the filler. The check after SH-42's `extension-point` is overturned and ten earlier lines are aligned. Google's own services through the app stay `extension-point`.
- **C45.2 is ruled as read:** the Buy Button channel is `own-service` on 'we've made the following updates [to] the Buy Button channel'. The three earlier `core` lines the batch named are the pricing pages' plan rows, and they stay `core`.
- **C45.3 is ruled as read:** a possessive on a part of the platform, such as 'Shopify's fastest way to check out', names the platform's own checkout, `core`.
- **The other `CHANGES` stand,** each on the digest's rules, as the batch decided them. CM-ORD-013's `own-service` order notes and CM-SHP-017's tracking in Arrive (renamed Shop) stay open as placed.
- **The new thing** Storefront Signage Maker is `shows`, with no place of its own and no maker held. The others keep their names.
- **The rules C45.1 to C45.10 stand** and join the digest's section 6.
- **Cost:** 26.0 million tokens over 110 requests, about 200,000 an entry. The context reached about 436,000 tokens.
