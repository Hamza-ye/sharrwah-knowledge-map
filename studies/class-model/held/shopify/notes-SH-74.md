# Held pass, Shopify, batch SH-74: notes

80 entries of `pricing-page-data` (effort high), evidence at observed-sh@e38dc17e3, in `structures/shopify/pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl`. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-74`).
- **1 to 24:** the rest of www.shopify.com/ca's plans page (items.jsonl line 27):
  - 20 comparison rows whose words are ca's, or ca's and a few other sites' (1 to 20: `compareAllFeatures.table.rows`, of its 101 rows);
  - the disclaimer `apyDisclaimer` and its three footnotes (21 to 24).
- **25 to 37:** www.shopify.com/ca's POS page (line 28): its terms entry, the six plan summaries, the two POS Pro lists' plan entries, the four FAQs.
- **38:** www.shopify.com/eg's international page (line 42): its Shopify Payments processing row.
- **39 to 58:** www.shopify.com/eg's plans page (line 43), with sa's where the words are the same: the hero, the four cards' prices, their features whose words are eg's and sa's, the POS Pro card, the Pay monthly and Pay yearly rows, one FAQ, the disclaimer and two footnotes.
- **59 to 70:** www.shopify.com/eg's POS page (line 44), with sa's: the six plan summaries, the two POS Pro lists' plan entries, the four FAQs.
- **71, 72:** www.shopify.com/hk-en's international page (line 66): its terms entry and its processing row.
- **73 to 80:** www.shopify.com/hk-en's plans page (line 67): its terms entry, the hero (on eight sites), the Basic and Grow cards with their card rates and credits. SH-75 begins with the hk-en Advanced card.

**Placed:** 80 entries in 216 lines: 74 entries on capabilities, 6 `new` (SH-68's new thing), none `out`; 38 entries take more than one line. Supports, by line: 184 `core`, 19 `shows`, 11 `outside`, 2 `own-service`; no `extension-point`. 15 lines carry fillers; 146 carry qualities. The checker raises no `CHANGES`.

**Sources read:**
- the brief and what it names: the evidence map; the rulings, the last section most; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md` (nothing on these pages), `structures/README.md`; `structures/REGISTER.tsv` row 141; `selection.tsv`'s row; `show --meta`;
- SH-68's notes whole, SH-69's to SH-72's rules and coordinator's checks, SH-73's notes whole, and the earlier placements of each twin (`earlier`, then the twin's lines by number);
- items.jsonl, by script: line 27's comparison table (its 101 headings in order, its marks `checkAlt` 'Included' and `dashAlt` 'Not included', and the note rows 39, 61 and 79, '*Requires Shopify Payments'); lines 28 and 44's plan summaries (`card_rates`, `incentives`); lines 43 and 67's cards with their features; and every read site's plans page (lines 2, 5, 10, 27, 43, 67, 82, 85, 91, 112, 133, 136, 140, 146, 150, 156, 161, 171, 176, 197, 203), for which tables hold the rows Shop Campaigns, Shipping insurance, Tax and its rows, Interac and Audiences. Every line's terms and quotes are its own entry's, but for the footnote '*Requires Shopify Payments' that 14's reading quotes from line 27;
- each entry against its twin's text, by script (difflib): every one differs from its twin only by its site's links, prices or digits, the date's form (22), or the lender and the financing's name (24);
- the model: `cells` for every capability placed on and for the new thing's leads; `land_points.py cell` for CM-TAX-004 and CM-PAY-026; `class_slice.py key` for SH-S-7069 and SH-S-0588; `caps --terms` for Interac and debit (no hit); `merged/evidence.tsv`, by grep, for the cells that cite the 30 September rows of my new kinds of row (SH-S-7044, SH-S-7047, SH-S-7066 to SH-S-7069, SH-S-7072) and for Interac (SH-S-0588).

## Rules followed

**SH-68's R0 to R11, SH-69's rules 1 to 7, SH-70's rules 1 to 9, SH-71's rules 1 to 3, SH-73's rules 1 to 8, and the rulings since, as kept.**
- **R0:** no entry of mine is on every read site of its language, so every line takes its labels, after its plans. The hero 74 is on eight English sites; the footnote 22 on three; the Tax rows on four; Shop Campaigns, Shipping insurance and Audiences on two (ca and www.shopify.com); the Arabic entries on eg and sa, or on eg alone (38, 56, 58, 68, 70), of the three Arabic sites.
- **R1:** the three terms entries (25, 71, 73), three `core` lines each. `googleCountryOffer` gives no line.
- **R2:** the cards and their features; the POS Pro cards (52) take their sites alone, the offer itself (the ruling after SH-70).
- **R3:** the rows, each on its twin's capability, matched by its heading, not its pointer (below); the section heading Tax (below).
- **R4, R6, R7, R9:** the POS summaries and lists, the FAQs, the qualities, the disclaimers' providers (`outside`, with fillers).
- **SH-73's rules 1 and 2:** ca's summaries state `card_rates.in_person` and the 12-month incentive on Basic, Grow and Advanced, so they take those lines (26 to 31). The eg and sa summaries state neither.
- **SH-73's rule 7:** ca's Capital footnote names its lender for Canada (24, below).
- **Twins, by meaning:** `earlier`'s pointer twins were right for the POS and international pages, the terms entries, the disclaimers and the FAQs. They were wrong in two places:
  - **ca's rows from 33 on:** ca's table holds rows au's and ae's lack, so from MB WAY rates (row 33) on, the pointer twin is another row. 8's are ae's Third-party transaction fees and au's Bancontact rates; 10's, ae's note row and au's MB WAY rates; 14's, ae's API rate limits and au's 3rd-party calculated shipping rates. I matched each row by its heading, as `earlier`'s labels also show.
  - **eg's and sa's `card_rates_short`** (41, 44, 47, 50): the pointer twins are card rates (CM-PAY-007), but these cards state the third-party providers' fee (rule 4 below).

**Rules for kinds the earlier rules don't cover, for the coordinator to align with SH-75 to SH-79:**
1. **In-person Interac rates** (11, on ca alone) is CM-PAY-021 `core`, its rates by plan as quality ('0% + 15¢ CAD' on Basic, Grow and Advanced, '0% + 10¢ CAD' on Plus), with no filler.
   - It is the sibling of In-person card rates (SH-73's rule 4), under Accepting payments, so it takes no section line.
   - CM-PAY-021's cell already holds Interac card payments, in its statement that Canadian businesses can't take them offline (SH-S-0588).
   - Interac names the cards the buyer pays with, as Amex does in the Amex rates' row (R9), so it fills no slot. No other held statement says who processes Interac payments.
   - The other reading: CM-PAY-017, a local payment method with Interac as filler, as SH-73's rule 3 has Bancontact and the others online. Neither reading changes a cell.
2. **Rows the 30 September table held, which ae's and au's tables don't,** take the capability whose cell cites that row (R3), each `core` but the add-on:
   - Acquire customers risk-free with Shop Campaigns (12): CM-MKT-012 (SH-S-7044). Under Marketing, so no section line.
   - Shipping insurance* (14): CM-SHP-003 (SH-S-7047). Its tooltip's 'Up to $200 coverage per eligible label' is a quality; its mark's footnote is the note row after the Shipping section, '*Requires Shopify Payments', quoted in reading as SH-71 quotes it for Built-in fraud analysis.
   - Optimize ads with Shopify Audiences (20): CM-MKT-011 (SH-S-7072), scope Plus. Under Just for Plus, whose rows take only their own lines (SH-71's lines 91 and 92).
3. **The Tax section** (15 to 19, on ca, ie, www.shopify.com and uk):
   - The heading names the store's taxes: CM-TAX-001 `shows`, the parent of its rows' capabilities, as SH-73's Shipping heading. Its rows take no section line.
   - Automated sales tax calculations, CM-TAX-002 `core` (SH-S-7066); Tax liability tracking, CM-TAX-003 `core` (SH-S-7067); VAT validation, exemptions, and invoicing, CM-TAX-005 `core` (SH-S-7068), whose note keeps the three together.
   - Advanced tax platform (19), 'Add on' on every plan, is CM-TAX-004 `shows`, as the cell's own placement of the same row (SH-S-7069). The four plans are its scope, since a plan's mark gives the scope (SH-73's rule 5).
4. **A card feature `card_rates_short` that states the third-party providers' fee** ('%2 لمزودي دفع من جهات خارجية' on eg's and sa's Basic card) is CM-PLN-003 `core`, as R2 has it. Its plan and sites are its scope and its fee is its quality. No earlier batch placed such a feature: every earlier card stated a card rate.
5. **A plan summary whose `card_rates` hold only `third_party`** (eg's and sa's six, 59 to 64) takes no CM-PAY-007 line, where its ae-ar twin, which states an online rate, has one. Its other lines are its twin's.

## New things

**`new:Earn 1% back on all sales as subscription credits`** (SH-68's), 6 lines:
- ca's table row: 3 (SH-E-5e3142a7), 'Up to $6,000 CAD', 'Up to $9,500 CAD' and 'Up to $13,000 CAD', a dash on Plus, with the tooltip of au's row;
- eg's and sa's cards: 42, 45 and 48 (SH-E-4bfdfaa6, SH-E-1d04e28f, SH-E-f38098be), the words of ae-ar's cards but for the domain credit's digits ('‏٢٠ US$');
- hk-en's cards: 77 and 80 (SH-E-d01ae743, SH-E-d7a8f229), 'Earn up to $4,500 in credits' and 'Earn up to $6,500 in credits', with 'Get 1% back on sales' and 'Add a domain, get US$20'.

Its place of its own (the table's row Earn 1% back on all sales), proposed domain A, area PLN, parent CM-PLN-004 (or CM-PLN-001), its Arabic words and the terms searched are in SH-68's notes. The leads' cells, read: CM-PTN-008 (holds nothing; a referral programme's commission), CM-PAY-025 (Shopify Credit), CM-SFR-008 (domains, a way to earn the credit), CM-PLN-001 and CM-API-001 (by the plan names), CM-CHK-002 (the buyer's cart). None holds the platform's credits to the merchant.

## Entries I couldn't tell, and what would settle each

- **11, Interac:** CM-PAY-021 against CM-PAY-017 (rule 1). A help page on Interac in Shopify Payments would settle whether Shopify calls it a local method.
- **19, Advanced tax platform `shows`:** kept to the cell's placement of the same row (SH-S-7069), since the row names no provider and the plans don't include it. `core` is the other reading, if 'Add on' is read as the platform offering the add-on itself, as SH-73's rule 5 reads Grow's 'Add on' for calculated rates. The cell's 'Avalara add-on fees' (SH-I-1325) is a lead to its provider, not a statement of this row. CM-TAX-002, by the tooltip's 'Calculate accurate taxes', is a third reading. None would change a cell.
- **18, the EU and UK:** the tooltip says the row's tools serve 'EU and UK sales'. I read that as the sales they apply to, not a condition on the store, so it stays in reading. If the coordinator reads it as the line's market, the scope would be the plans and sites with ` and EU;UK`, and the ruling after SA-53 doesn't say how ` and ` reads a list after it.
- **14, the labels named in passing:** 'per eligible label' names Shopify's labels (CM-SHP-002) as what the insurance covers. CM-SHP-003 is CM-SHP-002's child and holds the same statement, so I gave no CM-SHP-002 line.
- **41, 44, 47 and 50:** rule 4 rests on R2. The eg and sa plans pages state no card rate anywhere I read: their cards and POS summaries give only the third-party fee, and their table (76 rows, items.jsonl line 43) has no Accepting payments section, though it keeps 'قبول طرق الدفع المحلية*'. Whether Shopify Payments is offered on those sites isn't stated in these entries. The eg international page's processing row (38) names Shopify Payments' 3.9% beside Managed Markets, which is another statement.
- **The twins' doubts carry over,** as SH-73's notes list them: the FAQs' 'every paid plan' read as the four plans (36, 69); the iPad stand's `own-service` (35, 68); the transaction fees on CM-PLN-003 (34, 67); the incentive's 'free hardware and more' (26 to 28).

## A structure whose items and sources disagree

Each line quotes its own entry. Which price is charged isn't held. That the pages' different variants are the cause is an assumption, as SH-68's to SH-73's notes have it.
- **www.shopify.com/ca states three yearly prices for Basic:** the plans page's card and Pay yearly row $44 (SH-73's line 182; entry 2), its terms 'basicAnnualPrice: <span>$38.00</span>' (SH-E-3dd120ae, and the POS page's terms, 25), and the POS page's summary `annual_monthly_price` 37 CAD (`annual_price` 441, 26). Grow and Advanced differ the same way: $120 and $465 on the plans page (2), 99 and 389 CAD in the summaries (27, 28).
  - The plans page was served under 'e_0573c3a44a32b9562a4827c286953987:treatment,e_06d1ad5d27d16046cc6d829de669769b:treatment,f_2e2905455a798fa9df40308c0b8b53ee:true,f_77c8150780b85c85656903fc3fada251:true,f_ba4893153541cee32ff1abde10187c02:true' (SH-73's line 179), the POS page under 'f_2e2905455a798fa9df40308c0b8b53ee:true,f_77c8150780b85c85656903fc3fada251:true' (25).
- **ca's Plus price:** the table's 'Starts at $3,400 CAD/mo' (1) is the summary's `triennial_monthly_price`; its `monthly_price` is 3650 CAD (29). The summary states a paid trial on Plus, 517.00 CAD for one month, which the au and ae summaries don't.
- **ca's Grow shipping discount:** the table and the card give up to 50% off (13; SH-73's line 189), the POS summary's description up to 87% (27), the words of every site's summary.
- **ca's and eg's Plus summaries** are titled 'POS Pro included' and 'يشتمل على POS Pro' with `included_in_plan: false` (29, 62), while Retail's has `true` (31, 64), as SH-69's and SH-73's.
- **www.shopify.com/hk-en's terms** give 'basicAnnualPrice: <span>$25.00 USD</span>' (71, 73), its Basic card US$29 a month paid yearly (75), as SH-71's check noted. Its terms write the currency '美元' (`minimumMonthlyPriceCurrency`, `usd`), on an English page.
- **eg's and sa's prices agree with each other:** their plans page's cards and Pay yearly row give Basic 24 a month paid yearly (40, 54), as their terms (SH-E-e8884dfd) and their POS summary (59) do. ae-ar's states 29 beside the same terms (SH-68's notes).
- **The items and the entries agree:** the entries are the items' decoded loader data. I didn't print the WARC records.

## What the sources state that no entry holds (for the second stage)

- **ca's table's marks** `checkAlt` 'Included' and `dashAlt` 'Not included' and its `captionText` 'Compare features across Shopify plans' (items.jsonl line 27), which R3 reads for the scopes. They are pruned, as on ae-ar's (SH-68's notes).
- **ca's three note rows** (rows 39, 61 and 79) read '*Requires Shopify Payments', one after Accepting payments, one after Shipping and one after Sell globally: the same words as the note entries of other batches. That the note after Shipping is Shipping insurance's footnote is a reading of its place.
- **Kept from SH-72's and SH-73's leads:** the POS pages' sales contact flow (`posContactModal`), on ca's and eg's POS pages too; the incentive's own offer terms ('offer worth $3,200' on ca), not held in this structure.

## The checker's lines, read again

- **No `CHANGES`.** Every cell my lines touch already holds its support. The only new slot filler is Peoples Bank, `outside` on CM-PAY-026, for Canada (24), beside the cell's WebBank, YouLend and SH-73's Westpac.
- **`NOTE` footnote mark (line 18: 14, Shipping insurance*):** its reading quotes its footnote, the note row after the Shipping section.
- **`NOTE` own-service on CM-POS-002 (35 and 68):** SH-70's rule 4, kept by the coordinator: “Shopify's flexible iPad stand” and 'حامل iPad المرن من Shopify' name Shopify as the stand's provider, as the cell's own-service (SH-S-7269).
- **`NOTE` on a product named with the platform's brand (lines 24, 111 and 205):**
  - 20, Shopify Audiences, is `core` by the cell's plan row (SH-S-7072);
  - 38 and 72, Shopify Payments processing, are `core` by the cell's Shopify Payments route and plan rows, as SH-70's line 67 and SH-73's lines 40 and 178.
- **`NOTE` on a new thing whose entry has leads (lines 6, 116, 120, 124, 213 and 217):** the leads' cells are read above. CM-PTN-008, the first lead of 3, holds nothing on Shopify and isn't the entry's thing: it is a referral programme.
- **`NEW`:** Earn 1% back on all sales as subscription credits, 6 lines.

## Problems with the brief or the script

- **`earlier`'s twins by pointer still mislead on the plans pages** (above): on ca's rows past au's last shared row, and on eg's and sa's card rates, whose `name` key agrees with ae-ar's while the summary states another thing. Its labels found the right rows. A twin by heading for the rows, and a warning where the twin's summary and the entry's differ in kind, would serve SH-75 to SH-79.
- **A quote with a straight apostrophe** (“Shopify's flexible iPad stand…”) is quoted with “ ”, as SH-73 did. The readings' “and”, from the rulings' wording, is read by my own check as a quote not in 56's Arabic text; it is the earlier batches' phrasing, kept.
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief states (qualities wider than B-extent's list; the rulings).
