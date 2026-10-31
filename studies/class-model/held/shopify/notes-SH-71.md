# Held pass, Shopify, batch SH-71: notes

89 entries of `pricing-page-data` (effort high), evidence at observed-sh@e38dc17e3, in `structures/shopify/pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl`. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-71`). All 89 are on www.shopify.com/ae's plans page (items.jsonl line 5, https://www.shopify.com/ae/pricing):
- **1 to 4:** the Agentic card's four features (`thereIsMore.agenticPlanCard.features`);
- **5, 6:** the testimonial block's two figures (`wordOnTheStreet.statCards`);
- **7 to 89:** the comparison table (`compareAllFeatures.table.rows`), rows 0 to 83 of its 84, counted from 0. Row 68, the second note '*Requires Shopify Payments', is entry 42 again (same words as row 35), so the table's 84 rows are 83 entries.

SH-72 begins with the page's FAQs and its disclaimer (`apyDisclaimer`), which hold the footnotes of my rows 76 to 78.

**Placed:** 89 entries in 98 lines: 83 entries on capabilities, 1 `new` (the new thing SH-68 named), 5 `out`; 9 entries take more than one line. Supports: 80 `core`, 13 `shows`; no `own-service`, `extension-point` or `outside`. One filler line (ChatGPT; Gemini, the venues of Sell in AI chats). 32 lines carry qualities.

**Sources read:**
- the brief and what it names: the evidence map; the rulings, the last section; B-extent.md's "Cells and evidence" and "Conventions from the dry run"; observed-sh's `README.md`, `docs/READING.md` (runs, fetch runs, structures, indexes), `docs/GAPS.md` (nothing on these pages), `structures/README.md`; `structures/REGISTER.tsv` row 141; `selection.tsv`'s row; `show --meta`;
- SH-68's, SH-69's and SH-70's notes and placements first, with their coordinator's checks, and kept to their R0 to R11, rules 1 to 7 and rules 1 to 9;
- items.jsonl line 5 for the parts my entries are cut from: the Agentic card, the table's rows 35 and 68, its marks (`checkAlt`, `dashAlt`), and the disclaimer's footnotes; and, to clarify only, lines 10, 27, 67, 85, 91, 112, 133, 136, 140, 146, 150, 156, 161, 176, 197 and 203 (every English site's plans page) for which sites hold the Agentic card, and lines 67, 161 and 197 for the Pay yearly row, the terms' Basic annual price and the footnotes. Every line's terms and quotes are its own entry's, or a footnote of the page its reading cites;
- the model: `earlier` (it finds no Arabic twin, so I joined each entry to its ae-ar twin by its pointer on items.jsonl line 2, which SH-68's R0 aligns row for row, and read the twin's line in SH-68's or SH-69's placements); `cells` for every capability placed on and every lead; `caps --terms` for Shopify Catalog, Catalog, AI channels, agentic plan, Agentic, social, social media, social commerce; and `merged/evidence.tsv`, read by script for which Shopify cells cite each of the 30 September table's rows (SH-S-7001 to SH-S-7079) that my readings cite.

## Rules followed

**SH-68's, SH-69's and SH-70's rules, as kept:**
- **R0:** a line on every read site of its language takes no site. 73 entries are labelled with all 18 English sites and take none: R0's measurement found every such English line's Arabic twin the same on the three Arabic sites. The other 16 take their labels after their plans: 1 to 3 (the ten sites with an Agentic card), 4, 8, 37 to 39 (ae), 9 (ae, hk-en), 11 (ae, hk-en, ng), 30 (eight sites), 35, 36, 40 and 41 (ten sites), 61 (eleven sites, the ones that write '$99/mo'; the other seven write the currency code).
- **R2:** the Agentic card's features, scoped 'Agentic' and their sites, as SH-68's 90 to 93.
- **R3:** the table's rows, each on its twin's capability and support, its marks giving the plans (the page's `checkAlt` 'Included', `dashAlt` 'Not included', items.jsonl line 5); the section headings Pricing, In-person sales, AI features, Accepting payments, Hosting, Marketing, Marketplaces, Sell globally and Just for Plus on their capabilities, `shows`; Core features, Customization and Finance `out`.
- **R7:** the qualities, plans with the same value written together. SH-68's twins write '10 (Basic), 10 (Grow), 10 (Advanced), 200 (Plus)' for Inventory locations and the same for headless storefronts; mine write '10 (Basic, Grow, Advanced), 200 (Plus)', as R7 has it.
- **R9:** Hydrogen and Oxygen `core`, as CM-SFR-011's cell holds them; card brands (Amex, Visa) name no filler.
- **R10:** the testimonial block's figures `out`.

**Every line of 7 to 89 is the English twin of an ae-ar line** (SH-68's lines 97 to 171, SH-69's lines 2 to 17). Each takes its twin's capability, support and plans, its own sites by R0, and its own words for terms, quotes and qualities; its reading names the twin where the twin's reading is cited.

**Rules for kinds the earlier rules don't cover, for the coordinator to align with SH-72 to SH-79:**
1. **A row the model's cells cite on two capabilities takes a line on each.** The brief's rule 2: "Where a cell's reading cites the same page, place or term, the entry is that capability's too." I read, by script, which Shopify cells in `merged/evidence.tsv` cite the 30 September twin of each of my rows. Every one is placed, but one: Build headless storefronts (SH-S-7056) is cited by CM-CHN-007 (several storefronts in one store) beside CM-SFR-011. Its cell reads the row's count, 1 and 25, as how many storefronts the store's plan includes. So 67 takes a CM-CHN-007 line, `core`, which changes nothing in the cell. SH-68's twin (SH-E-09b40c1e) has no such line: the coordinator may add it there too. The other rows cited twice are already placed twice (Pay monthly; Collective) or kept to one by a note (Unlimited web hosting, CM-SFR-010's note).
2. **A footnote mark whose footnote differs by site.** The Capital row (77, on all 18 sites) points with ² to a footnote that www.shopify.com, au, ca, ie and uk state in other words (SH-68's R0). For example, www.shopify.com's is on loans' repayment terms, and uk's names Youlend as the issuer of its merchant cash advances (items.jsonl lines 161 and 197). The row's reading quotes the footnote of the locator's page (ae) and names the sites that state others. The footnotes are their own entries, placed in their own batches.
3. **The Agentic card's features take the sites that hold the card.** Ten English sites hold an Agentic card (ae, au, ca, hk-en, ie, no-en, nz, www.shopify.com, sg, uk); the other eight have `agenticPlanCard` null (items.jsonl). Entries 1 to 3 are stated on the ten in the same words, so they take the ten. 4, the card rate, is ae's alone: each site's card states its own rate and currency.

## New things

**`new:Earn 1% back on all sales as subscription credits`** (SH-68's), 1 line: 11 (SH-E-55f7cd59), the comparison table's row on www.shopify.com/ae, hk-en and ng.
- **English words:** 'Earn 1% back on all sales', 'subscription credits', 'Valid for your first 6 months or until you reach the max'. The maximums are 'Up to $4,500 USD', 'Up to $6,500 USD' and 'Up to $8,000 USD', with a dash on Plus. www.shopify.com states $5,000, $7,500 and $10,000, and uk states £3,500, £5,500 and £7,000 (items.jsonl lines 161 and 197), each in its own entry.
- **Its place of its own:** this row, a plan line (B-extent, "What a place of its own is"). The Arabic words, the proposed domain A, area PLN and parent CM-PLN-004 (or CM-PLN-001), and the terms searched are in SH-68's notes.
- **The leads' cells, read:**
  - CM-PTN-008 (by 'earn', 'sale'; it holds nothing on Shopify) is a referral programme's commission on the plans a member brings, not credits on the merchant's own sales.
  - CM-PAY-025 (by 'credit', 'sale') is Shopify Credit, a charge card with a credit limit. The subscription credits are another thing.

## Entries I couldn't tell, and what would settle each

- **16, Sell on social and marketplaces, on CM-CHN-001 alone,** as its twin and the cell's SH-S-7006. The row also names marketplaces, CM-CHN-003's thing (connecting marketplaces), which a second line could take. Social channels are in CM-CHN-001's own terms. The line would change nothing: CM-CHN-003 is `core`.
- **65's 'Limited data access' on Basic:** the row doesn't say which data Basic's custom apps can't reach. A held statement on custom apps' access by plan would settle whether CM-API-004 (protected customer data) is the row's thing too.
- **33, Millions of tokens, on CM-AIA-001 alone,** as its twin. The tooltip says tokens power 'your AI assistant' (Sidekick, CM-AIA-002), as what they are used for, not as the row's thing.
- **3, 'Only pay when you make a sale', on CM-PLN-003,** as SH-68's line 92, which the coordinator's check kept. CM-PLN-003's note describes Shopify's fee as applying only to orders through other payment providers. The Agentic plan's charge on sales is stated without a rate or a condition. The Agentic plan's own page would settle it: www.shopify.com/agentic-plan, captured outside this structure (SH-68's notes).
- **The rest follow their twins,** whose doubts SH-68's and SH-69's notes list: Unlimited contacts and Capture customer leads `shows`, Collective's sourcing `shows` on CM-CAT-010, the section headings `shows`, and CM-POS-002's `core` (below).

## A structure whose items and sources disagree

- **The Basic annual price** (9): www.shopify.com/ae's and hk-en's Pay yearly row gives Basic '$29 USD/mo'. Their pages' terms give 'basicAnnualPrice' '<span>$24.00 USD</span>' (ae, line 5) and '<span>$25.00 USD</span>' (hk-en, line 67), each with a 25 per cent annual discount. This is SH-68's and SH-70's disagreement again. Each line quotes its own entry.
- **The items and the entries agree:** the entries are the items' decoded loader data, and rows 35 and 68 hold the same note, so one entry stands for both. I didn't print the WARC records.

## What the sources state that no entry holds (for the second stage)

In items.jsonl line 5 (www.shopify.com/ae's plans page), pruned by the selection's rule or not wrapped:
- **The Agentic card's image `alt`:** 'Shopify Agentic dashboard showing AI integration partners including ChatGPT, Perplexity, and Microsoft Copilot'. It names three AI channels as integration partners: a lead for CM-AIA-005's fillers. The table's Sell in AI chats names only ChatGPT and Gemini. The card's button 'Start for free' links /ae/agentic-plan.
- **The table's own marks and caption:** `checkAlt` 'Included', `dashAlt` 'Not included', `captionText` 'Compare features across Shopify plans'. R3 reads the marks.
- **`thereIsMore.headingHtml`, 'But wait, there’s more':** the heading over the POS Pro and Agentic cards. The rendered page's structure holds it (SH-E-77615a2c, `www.shopify.com_pricing`, batch SH-92).
- **`wordOnTheStreet`:** the block's heading 'Word on the street', and a merchant's testimonial, which is `out` in any case.

## The checker's lines, read again

- **`CHANGES CM-POS-002@shopify gains core`, by line 33 (27, SH-E-fb76b578, 'Accept payments with a phone or card reader'):** kept. It is the English twin of SH-68's line 122 (SH-E-848c4325), which the coordinator's check after SH-68 kept: a plan line that includes taking card payments with a phone (Tap to Pay on iPhone or Android) or a paired card reader. SH-69's line 136 gives the same. It names no seller, so it is placed by what it shows.
- **`NOTE` on a product named with the platform's brand** (lines 21, 22, 27, 45, 81, 86 to 89, 92, header as line 1): Shopify B2B, Shopify Collective, Shopify Payments, Shopify Markets, Shopify Balance, Capital, Credit, Bill Pay and Shopify Combined Listings. Each is `core` by its cell's place, not by its name, as SH-68's and SH-69's checks have them:
  - B2B: its admin label and plan row;
  - Collective: its plan row;
  - Shopify Payments: its route and plan rows;
  - Markets: its route and plan row;
  - Balance, Capital, Credit and Bill Pay: their admin sections, routes and plan rows;
  - Combined Listings: its plan row and API object.
- **`NOTE` on footnote marks** (lines 50, 80, 82: 41, 70, 72): each reading quotes its footnote, '*Requires Shopify Payments', the note row (42). The marks ¹ ² ³ of 76 to 78 aren't flagged; their readings quote their footnotes from the page's disclaimer (rule 2 above).
- **`NOTE` on a new thing whose entry has leads, and its first lead CM-PTN-008 holding nothing** (line 14): read, above.
- **Other leads to cells that hold nothing, read, are not the entries' things:** CM-MKT-018, bank offers (3, 78); CM-API-013 (21); CM-PTN-007 (23); CM-APP-012 (30); CM-MKT-003, discounts without a code (56); CM-APP-010 (66); CM-SFR-014, a headless storefront's sites and routes (67); CM-SHP-021 (77); CM-MKS-009, reference lists of countries (71).
- **Homonyms named in readings:** CM-B2B-003's Catalogs (1), CM-CAT-013's product pricing (7), CM-SUP-004's live chat (25), CM-INV-005's locations (29), CM-CHK-007's records of abandoned checkouts, against recovery (55, its note), CM-CHN-004's listings (82).
- **`NEW`:** Earn 1% back on all sales as subscription credits, 1 line.

## Problems with the brief or the script

- **`earlier` prints no Arabic twin.** It keys an English entry by its English label, so the ae-ar line of the same row isn't found. Only labels the two languages share are found: 'Shopify B2B', 'Shopify Payments', 'POS Pro', '24/7 support'. I joined the twins by pointer (items.jsonl line 2 against line 5), which SH-68's R0 aligns row for row. A twin lookup by the item's pointer, on the page of the other language, would serve SH-72 to SH-79.
- **Quotes with a straight apostrophe** ('Shopify's Catalog', 'World's', 'customers'', 'Doesn't') are quoted around those words or not quoted, and my own words use ’. 45's tooltip holds double quotes (".myshopify.com"), so it is quoted only to the comma before them.
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief states (qualities wider than B-extent's list; the rulings).

## The coordinator's check (31 October 2026, after the batch)

- **No cell changes beyond earlier batches'.** CM-POS-002's `core` repeats SH-68's.
- **Each entry takes its Arabic twin's line,** matched by its pointer, as R0 aligns the two pages row for row. The sites follow R0.
- **Rule 1 stands:** a row that two cells cite takes a line on each. SH-68's twin of the headless storefronts row (SH-E-09b40c1e) now takes the same CM-CHN-007 line, added by the coordinator.
- **Rules 2 and 3 stand:** a footnote that differs by site, and the Agentic card's ten sites.
- **Leads:**
  - the Agentic card's image text, which names ChatGPT, Perplexity and Microsoft Copilot, for CM-AIA-005's fillers;
  - the ae and hk-en pages' yearly Basic price against their terms ($29 against $24.00 and $25.00), which stays in `reading`.
- **Cost:** 11.5 million tokens over 61 requests, about 129,000 an entry.
