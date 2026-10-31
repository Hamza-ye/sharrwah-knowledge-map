# SH-66: Shopify `editions-page-data`, Spring '26 from Online's B2B to Operations' Shipping

83 entries, observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl` (page 11, `https://www.shopify.com/editions/spring2026`). Effort `high`. The sections are Online > B2B (8), Retail (18, with POS XXL's 1), Marketing (12), Operations > Plugins (3), Admin (21), Inventory (9) and Shipping (11). No earlier batch had placed a Spring '26 entry, so `earlier` found only one key (UPS return labels, SH-34's changelog line).

## What I read

- The brief, the digest `held/rules/editions-page-data.md` whole (section 6 included), and `review-H-rulings.md`'s last section.
- The evidence map, observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md` and `structures/README.md`, `REGISTER.tsv`'s rows 137 and 138, `selection.tsv`'s rows 34 and 35, and B-extent's "Cells and evidence" and "Conventions from the dry run".
- The source: the spring2026 row of `items.jsonl`, for its collections' titles and descriptions. The sections in my range have none: every `descriptionHtml` is empty, so no section text, such as a 'We're rolling out' (E69), limits a card. Three items are spot-checked in `rows.jsonl` (positions 1623, 1694 and 1696).
- Batch notes, only for the cases the digest names and sends to:
  - `notes-SH-58.md`, line 67 (E66);
  - `notes-SH-59.md`'s E74 line;
  - `notes-SH-60.md`, lines 51 to 56 (E80), with its E78 and E81 lines;
  - `notes-SH-63.md`'s E110 line;
  - `notes-SH-64.md`, lines 49, 53 and 54 (E119, E123 and E124);
  - `notes-SH-47.md`, line 9 (R47.3). This digest doesn't hold R47.3, and the Plugins cards needed it (below).
- Other batches' placements, read with `grep` only, for twins and alignment: SH-34, SH-35, SH-41, SH-46, SH-50, SH-53, SH-54 and SH-57 to SH-64. The changelog posts on the same features are twins by meaning (rule 4; E61). I kept their capabilities:
  - SH-E-0840c816, scannable discounts;
  - SH-E-37f4156a, the POS editor;
  - SH-E-dfb5ed05, offline checkout;
  - SH-E-999d121a and SH-E-3f0ff799, WhatsApp in Messaging;
  - SH-E-1cbadabe, WhatsApp consent;
  - SH-E-061b6cea, the sign-in page;
  - SH-E-1f4f9846, Checkout settings;
  - SH-E-b9fc95b9, UPS return labels;
  - SH-E-f1ba98a4, channel discounts;
  - SH-E-7a84be26, customer data permissions;
  - SH-E-2efda9ff, statuses;
  - SH-E-bca897c1, Lovable.

## Counts

- 83 entries: 82 on capabilities, 1 `new` (SH-E-4a75fd05, with two new lines), 0 `out`.
- 159 lines: 157 `capability`, 2 `new`.
- By support: 124 `core`, 18 `own-service`, 11 `shows`, 4 `extension-point`, 1 `outside`, 1 `core;extension-point`.

## The new things

- **`new:Admin search`, `core`** (SH-E-4a75fd05, 'Filtering and saved views from one search bar across admin'). This is the name SH-36 gave the admin's own search (the digest's section 4). It is decided in `held/new.tsv` with Zid's and Salla's admin search (the ruling after SH-37). Its place of its own, domain and parent are as SH-36 proposed. The name is English only, since the Editions are English only. I searched no new terms: the digest keeps the name.
  - Its leads are homonyms: CM-SFR-013 is the storefront's search for buyers, and CM-PAY-014 is buyers' saved checkout details (the checker's NOTE on line 109).
  - `core`: the card offers it now, 'Search, filter, and save views from one search bar across sections in the admin.' (rule 22).
- **`new:Saved views`, `core`** (the same entry). This is the name SH-35 gave, decided with Admin search. It is `core` for the same reason.

Batches wrote both `core` and `shows` for these two before (4 and 6 lines of Admin search, 1 and 5 of Saved views). Mine are `core`.

## Rules I followed that the digest doesn't hold (from E135)

- **E135. Outside AI assistants under the group Plugins.** SH-47's R47.3 applies: the platform's connector or plugin, shown by its words or a held link, is CM-AIA-004 `core`, the assistant its filler. With neither, it is `shows`.
  - 'Store management with agents like Claude, ChatGPT, or Perplexity' (SH-E-43b0ddff) names no connector in its words, and its link (`www.shopify.com/build-with-ai#chat-connectors`) isn't held. It is CM-AIA-004 `shows`, with Claude, ChatGPT and Perplexity as fillers.
  - The eyebrow 'Plugins' repeats its subsection's title, so it is read as the group's title (the digest's rule 2).
  - The platform's own Shopify AI Toolkit (SH-E-80bdfc5c) is CM-DVT-001 `core` (rule 17). It is also CM-AIA-004 `core`, the AI platforms after 'like' its fillers (rule 54).
- **E136. Discounts limited to a sales channel are CM-MKT-001 `core`,** as the Winter ’23 card on the same help page (`discounts/sales-channel-discounts`, SH-E-f1ba98a4). Each kind of discount the card names takes its own line: code-based on CM-MKT-002, automatic on CM-MKT-003 (rule 47). 'In person' takes CM-POS-001 (SH-E-36cdd9b0).
- **E137. Multi-entity selling named as a payment feature's condition** ('Multi-entity businesses on Shopify Payments', 'multi-entity retail setups') is the scope, as a kind of business (rule 27). CM-ACC-005 also takes a line, since the news is the two working together (E74). The cases are SH-E-292ba015 and SH-E-a2706e5e.
- **E138. Analytics cards.**
  - Charts, targets and visualizations 'in analytics' are CM-ANL-001.
  - A card naming reports is CM-ANL-002.
  - The overview's insights are CM-ANL-003, as SH-54's SH-E-708cd142.
  - The subsection's lead card ('Better context for your store's data') takes CM-ANL-001, and CM-ANL-003 for the daily insights it names (rule 38).
  - The help addresses under `custom-reports/` go in `reading` (rule 53).
- **E139. A full audit trail of stock changes is inventory history, CM-INV-002,** not the admin's activity log (CM-TRU-003). The case is SH-E-1e8816b9. A cash drawer's audit trails stay in CM-POS-003 (SH-E-5efa547a).
- **E140. Requests the buyer makes from the order status page.** A cancellation is CM-ORD-004 and a return is CM-RET-003. The order status page takes CM-CHK-001 (E68), as SH-E-8cd6fd65 placed it (SH-E-d38c4e12).
- **E141. Carriers that manual tracking numbers detect** ('DHL, EVRi, Australia Post, and other top carriers') are the fillers of CM-SHP-017 `core`. They take no CM-SHP-015 line, since the card doesn't name them as Shopify Shipping's label carriers (SH-E-80af8898).
- **E142. A bundle published to channels.** It is CM-SEL-006 `core` where its help link is the general `products/bundles/index` page, not the Shopify Bundles app's page (`…/bundles/shopify-bundles`, SH-E-1b3f0ff8). Each venue takes a CM-CHN-004 line:
  - Google's surfaces are `own-service`, as the platform's own Google & YouTube app syncs products there (the corrections after SH-45). This is a reading: the card names only the venues.
  - Facebook and Instagram are `shows`, since `makers` finds no maker statement for Facebook & Instagram (the ruling after SH-43).

  The case is SH-E-d5671a72.
- **E143. Shop Campaigns charges on the Shopify invoice** are CM-MKT-012 `own-service` (rule 11) and CM-PLN-004 `core`, the platform's own bill (SH-E-abd7359f).
- **E144. The admin's app settings page.** It is CM-APP-001 `core`. Its list ('what apps are doing, where extensions and functions run, and what data they access') gives functions CM-APP-005 and data access CM-API-003 (E80). 'Extensions' names no single capability, so it takes no line (SH-E-171f44ac).

## Entries I couldn't tell, and what would settle each

1. **SH-E-736fbd3e, QuickBooks and Mailchimp.** The lines are `extension-point`, with QuickBooks and Mailchimp named as the work's source (E124).
   - If the two are read only as the apps' names, the ruling after SH-43 makes them `shows`, the maker a gap.
   - The CM-CUS-002 line reads 'Create B2B segments to send targeted emails with Mailchimp' as segments made with Mailchimp's app. If they are the admin's own customer segments, it is `core`.
   - The App Store listings (`apps.shopify.com/qbconnector`, `/mailchimp`) would settle both. I didn't read them.
2. **SH-E-43b0ddff and SH-E-a1f29ae9, the Plugins cards.** If the coordinator reads 'Plugins' as naming the platform's plugins, the first becomes CM-AIA-004 `core`. The second becomes CM-SFR-011 `extension-point`, not `outside`. E113's Lovable card (Winter '26, Online) wasn't under Plugins.
   - `www.shopify.com/build-with-ai` would settle it. It isn't held.
   - The held help pages on connecting AI tools (`raw/runs/20261016T213535Z-help-en-ar-html-md`, R47.3's source) name the Shopify connector for Claude and the plugin for ChatGPT. I read them only as R47.3 cites them, and they don't name Perplexity.
3. **SH-E-d5671a72, fixed bundles.** The Google line's `own-service` is a reading (E142). If the venues are read as named in passing, the two CM-CHN-004 lines drop.
4. **SH-E-992a2d7a, 'Pricing on returns and upsells…'.** What an upsell is here isn't stated: an order edit adding items (CM-ORD-002) or an upsell offer (CM-MKT-021). It is CM-MKT-021 `shows`, giving its terms only. The card has no link.
5. **SH-E-acefd612, Collective's tax-inclusive pricing.** Its taxes are kept in CM-CHN-005, as Collective's supplier rates and price lists are (the ruling after SH-57). If the coordinator reads the calculation as the platform's tax engine, it adds CM-TAX-001 `core` ('how its prices show them'). 'B2B taxes' is Collective's trade between suppliers and retailers, so CM-B2B-001 takes no line, as SH-64 read the B2B section's Collective cards.
6. **SH-E-3c0d606f, Verifone Victa Mobile.** It is CM-POS-002 `shows`: no maker is named, and the brand Verifone in its name is no maker statement (E109; B-extent). The countries of the pre-order are its scope, `US;Canada`.
   - Its page, `hardware.shopify.com/products/verifone-victa-mobile`, isn't in the sources.
   - Whether 'Pre-order available' is also a release marker (rule 32) changes nothing, since it is `shows` either way.
7. **SH-E-292ba015 and SH-E-a2706e5e (E137).** If multi-entity is read only as the condition, the CM-ACC-005 lines drop. SH-E-a2706e5e's 'Transaction limits are inherited across all stores.' is recorded as a quality with no value.
8. **SH-E-a220c00b, the 'not required' fulfillment status.** It is CM-SHP-009 and CM-ORD-003, by E119 (SH-E-2efda9ff). The status is the platform's, not one the merchant customizes, so CM-ORD-003 is the weaker of the two.
9. **SH-E-ef3a8e07, POS pickup orders.** 'Notify customers, and mark orders as fulfilled.' gives CM-NTF-001 and CM-SHP-009 their lines (E80; E119). All of the entry's lines are scoped 'POS Pro' (the ruling after SH-70).
10. **SH-E-736fbd3e, SH-E-36b6c265 and SH-E-36cdd9b0.** Their CM-B2B-001 and CM-POS-001 lines rest on rule 46 and on 'in person'. Each is a marked reading.

## The `CHANGES` lines, and what I decided

- **CM-CHN-005 gains `own-service`** (lines 5, 7, 8, 11 and 12). Kept: Collective's maker statement (SH-E-850b28ae; the digest's table and rule 16). The same as SH-57, SH-60 and SH-62 to SH-64, which aren't amended yet.
- **CM-AUT-001 gains `own-service`** (lines 13, 112, 113, 116, 117 and 118). Kept: Flow's maker statement (SH-E-0678ff26).
- **CM-B2B-001 gains `extension-point`** (line 19, QuickBooks and Mailchimp). Kept: apps that serve business buyers (E78), as SH-60 and SH-64 have it. Case 1 above.
- **CM-MKT-003 gains `core` and becomes held** (line 39). Kept: 'Create code-based and automatic discounts that only apply in person' names automatic discounts, which the cell's note says no Shopify statement held names (rule 47).
- **CM-MKT-006 gains `own-service`** (line 65) and **CM-MKT-007 gains `own-service`** (lines 64 and 67). Kept: Shopify Messaging's maker statement (SH-E-32e5ccc3), as the changelog's SH-E-3f0ff799 and SH-E-999d121a.
- **CM-CHN-004 gains `own-service`** (line 75, Google). Kept as a reading (E142; case 3).
- **CM-SFR-011 gains `outside`** (line 81, vibe coding). Kept by E113 (case 2).
- **CM-AIA-004 becomes held** (lines 82 and 84) **and gains `core`** (line 84, the Shopify AI Toolkit). Kept by E135. Line 82, the store managed inside Claude, ChatGPT or Perplexity, is `shows`.
- **CM-ORD-003 gains `core` and becomes held** (line 146). Kept by E119 (case 8).
- I changed one line before the final check: SH-E-992a2d7a's CM-MKT-021 was `core`, and I made it `shows` (case 4). The card doesn't show who offers the upsells or what they are.

The checker's 25 brand NOTEs are all on lines where Shopify POS is the platform's own client (rule 9), on CM-APP-007 admin pages (rule 40), or on the platform's own developer tool, the Shopify AI Toolkit (rule 17).

## Leads not taken

- CM-SFR-016 (the checker's NOTE on line 20): SH-E-397aa200's 'share how they can feel the difference' is a testimonial, not social sharing.
- CM-APP-010 (the NOTE on line 100): an app's own developer-defined settings, a homonym of the admin's 'Redesigned app settings'.
- Two Collective cards:
  - SH-E-b2a37290: CM-SHP-017 and CM-CAT-014, for Collective's Verified Tracking badge;
  - SH-E-bfb699ea: no analytics capability, for Collective's insights. Both are Collective's own (rule 16).
- CM-ACC-008: Collective available in Australia is Collective's offer, not the platform's countries.
- CM-POS-004: the POS's own smart grid actions, not apps' extensions (SH-E-6a8b3728 and SH-E-7559e010), as the changelog's smart grid lines are placed.
- CM-PAY-008, payment terms: SH-E-36b6c265's triggers 'due dates, or invoicing' say when the Flow action runs.
- CM-CUS-002 for SH-E-bde6e97f: Shop Campaigns' bid segments 'like new or lapsed customers' are a list.
- Homonyms:
  - CM-STF-005 (SH-E-2a86b098's collaborators);
  - CM-MKT-016 (SH-E-75de7fac's 'Back-in-stock updates' are stock updates);
  - CM-B2B-001 (purchase orders: SH-E-5a7d3c1f, SH-E-716cd139);
  - CM-PAY-016 (offline checkout);
  - CM-SFR-002 (Liquid in Flow).
- CM-NTF-004 for WhatsApp as a delivery channel (SH-E-7638e868): the changelog's twin takes none, and WhatsApp isn't named as filler there either.
- CM-PAY-002 for Tap to Pay (SH-E-292ba015): 'on Shopify Payments' stays in the scope. The payment's processing is CM-PAY-021's.

## For the second stage

- Retail's nested collection 'Retail Merch' (`retail-merch`; `loaderData.routes/($locale).editions.spring2026.collections[3].nestedCollections[0]`) holds no products. A heading with no products goes to the second stage (the digest's rule 37).
- The nested collection POS XXL (`pos-xxl`, `sceneType: posXXL`) holds one card, SH-E-1794b600, placed on its own words.
- Online and Operations have no products or description of their own, and their subsections (B2B, Plugins, Admin, Inventory, Shipping) have empty descriptions: containers only.

## The structure against its source

The three spot-checked items agree with the rendering. The source holds no-break spaces (`\xa0`) where the rendering shows plain spaces, for example 'boost their\xa0discoverability.'. My quotes use plain spaces, and the checker found them.

Two entries hold straight double quotes:
- SH-E-a220c00b, '"not required"';
- SH-E-fd8506a7, '"on its way."'.

A placements row can't hold them, so those readings quote the text around the double-quoted words and name the words unquoted.

## Problems and notes for the coordinator

- SH-47's R47.3 (outside AI assistants and the platform's connector) isn't in this digest. E135 restates it for the Plugins cards.
- SH-67 holds Spring '26's Developer cards, which may repeat mine (E61, E79). By the section map, Apps + Extensions has a 'Shopify AI Toolkit' card and one on 'WhatsApp marketing consent with Customers and Admin APIs'. They would be twins of SH-E-80bdfc5c and SH-E-aa06fc7c.
- SH-65 runs beside this batch. Its Spring '26 cards end where mine begin, so the two batches share no structure split inside a section.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 83 of 83 entries, no problem.
- **The `CHANGES` stand,** each on the digest's table, its rules or SH-47's R47.3, now in the digest:
  - Collective, Flow and Messaging are `own-service`.
  - The apps that natively support B2B are `extension-point` (E78, E124).
  - Automatic discounts are CM-MKT-003.
  - Fixed bundles on Google are `own-service` by the corrections after SH-45, a marked reading; Meta's channel is `shows`, with no maker held.
  - Vibe-coding tools are `outside` (E113).
  - The Shopify AI Toolkit is CM-AIA-004 `core`, and agents named with no connector `shows`.
  - The 'not required' fulfillment status is CM-ORD-003.
- **The new things** Admin search and Saved views are written `core`, since the card has the platform offer them now. Their supports, which differ between batches, are decided with each thing.
- **'Plugins' is read as its group's title,** as placed.
- **The rules E135 to E144 stand** and join the digest's section 6. SH-65 numbers its own from E125.
- **SH-67's developer twins** of the Shopify AI Toolkit and WhatsApp marketing consent cards are named in its prompt.
- **Cost:** 19.8 million tokens over 93 requests, about 239,000 an entry. The context reached about 377,000 tokens.
