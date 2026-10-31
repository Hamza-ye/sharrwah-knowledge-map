# Held pass, Shopify, batch SH-79: notes

111 entries of `pricing-page-data` (effort high), the structure's last. The evidence is at observed-sh@e38dc17e3, in `structures/shopify/pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl`. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-79`). Every entry is labelled with one site.
- **1, 2:** the last two FAQs of www.shopify.com's POS page (items.jsonl line 162).
- **3 to 8:** www.shopify.com/sa:
  - its international page (line 170): its terms entry and its Shopify Payments processing row (3, 4);
  - its plans page (line 171): the disclaimer and the Credit footnote (5, 6);
  - its POS page (line 172): two FAQs (7, 8).

  Its other entries are in the words that eg's or all three Arabic sites share, placed in earlier batches.
- **9 to 52:** www.shopify.com/sg:
  - its international page (line 175): 9, 10;
  - its plans page (line 176, 11 to 39): the terms entry, the four cards with their card rates and credits, the POS Pro card, and the Agentic card and its rate; twelve comparison rows (Pay monthly, Pay yearly, Earn 1% back, POS Pro, the three online card rates, Bancontact, iDEAL, MB WAY, Bizum and In-person card rates); the disclaimer and the Credit footnote;
  - its POS page (line 177, 40 to 52): the terms entry, the six plan summaries, the two POS Pro plan entries and the four FAQs.
- **53 to 102:** www.shopify.com/uk:
  - its international page (line 196): 53, 54;
  - its plans page (line 197, 55 to 89): the terms entry, the hero, the four cards with their card rates and credits, the POS Pro card, and the Agentic card and its rate; fifteen comparison rows (those of sg, with Klarna, TWINT and USDC rates); one FAQ; the disclaimer with its Credit and Capital footnotes;
  - its POS page (line 198, 90 to 102): the terms entry, the six summaries, the two POS Pro plan entries and the four FAQs.
- **103 to 111:** www.shopify.com/za:
  - its international page (line 202): 103, 104;
  - its plans page (line 203): the terms entry, the Plus card, the disclaimer and the Credit footnote (105 to 108);
  - its POS page (line 204): the terms entry and two FAQs (109 to 111).

  Its other cards, rows and summaries are in id's words (SH-75).

**Placed:** 111 entries in 294 lines. 103 entries are on capabilities and 8 are `new` (SH-68's new thing); none is `out`. 57 entries take more than one line.
- Supports, by line: 249 `core`, 19 `shows`, 21 `outside`, 5 `own-service`; no `extension-point`.
- 31 lines carry fillers and 208 carry qualities.
- The checker raises no `CHANGES`.

**With this batch, all 1,056 entries of the structure are placed,** across SH-68 to SH-79. I checked it by script against every placements file. SH-78 ran beside this batch and finished during it. I read its lines for my twins (nz's POS FAQs, SH-E-5bbca8d3 and SH-E-e09ff3ea) and its readings for Bancontact and iDEAL, and kept to them.

**Sources read:**
- **The brief and what it names:** the evidence map; the rulings, the last section; B-extent.md's "Cells and evidence" and "Conventions from the dry run", with "What a place of its own is"; observed-sh's `README.md`, `docs/READING.md` (runs, fetch runs), `structures/README.md` and `docs/GAPS.md` (searched, nothing on these pages); `structures/REGISTER.tsv` row 141; `index/ledger-summary.tsv`; the ledger `index/ledger/sitemap--shopify-com-sitemaps.tsv` for my twelve pages, all captured by run 20261031T003815Z-shopify-com-pricing-by-country; `selection.tsv`'s row; `show --meta`.
- **The earlier batches:**
  - SH-68's notes whole (R0 to R11);
  - the rules and coordinator's checks of SH-69 to SH-77;
  - SH-78's rules, which ran beside this batch;
  - each twin's lines by number (`earlier`, then `sed` on the placements).
- **items.jsonl, by script, to clarify only:**
  - lines 176, 197 and 203: the comparison tables' headings, sections and marks ¹ ² ³, and `checkAlt` 'Included' and `dashAlt` 'Not included';
  - lines 176, 197 and 203: the disclaimers' list order (Balance, Cashback, Capital) and the Capital footnotes' words;
  - lines 177 and 198: the plan summaries, from which a script wrote their lines (below);
  - line 203: the za Plus card's bytes.

  Every line's terms and quotes are its own entry's, or those of another entry that its reading names by id.
- **The model:**
  - `cells` for the name and note of every capability placed on, and for the new thing's leads (CM-SFR-008, CM-CHK-002, CM-PTN-008, CM-PLN-001, CM-API-001, CM-PAY-025);
  - `land_points.py cell CM-PAY-026 shopify` for the United Kingdom's lender;
  - `entries.tsv`, by grep, for held statements on Bancontact, iDEAL, MB WAY, Bizum, Klarna, TWINT and USDC outside these pages, as the prompt asked.

## Rules followed

**I kept to all the earlier rules and to the rulings since:** SH-68's R0 to R11, SH-69's rules 1 to 7, SH-70's 1 to 9, SH-71's 1 to 3, SH-73's 1 to 8, SH-74's 1 to 5, SH-75's 1 to 7, SH-76's 1 to 3, and SH-77's 1 and 2.
- **R0:** each entry is one site's, so every line takes its site, after its plans.
- **R1:** the ten terms entries (3, 9, 11, 40, 53, 55, 90, 103, 105 and 109; sa's plans and POS terms are other batches'), three `core` lines each. `googleCountryOffer` gives no line.
- **R2:**
  - the cards with their card rates and credits, each on its card's plan;
  - the POS Pro cards (23, 68) on their sites alone (the ruling after SH-70);
  - the Agentic cards and their rates (24, 25, 69, 70). sg and uk are among SH-71's ten sites with an Agentic card.
- **R3:** the rows, each matched to its twin by its heading.
  - No row of mine takes a section line. Each row's capability is the section's own or below it: CM-PLN-001 for Pricing's rows, and CM-PAY-001's children and their children for Accepting payments.
  - Earn 1% back sits under Core features, which names only a grouping.
- **R4, R6, R7, R9:**
  - the POS summaries, lists and FAQs;
  - the qualities, with plans of the same value written together, such as uk's Klarna rates, '4.99% + 30p GBP (Basic, Grow, Advanced), 3.79% + 30p GBP (Plus)';
  - the disclaimers' providers, `outside` with fillers, and WebBank's U.S. joined to the site with ` and ` (the ruling after SA-53).
- **SH-73's rules:**
  - **Rules 1 and 2:** sg's and uk's summaries state `card_rates.in_person` on all six plans, so each takes a CM-PAY-021 line. Their Basic, Grow and Advanced summaries carry the 12-month incentive, each a second CM-POS-001 line scoped `<plan>;<site> and retail_term_commitment_12_months`:
    - sg: 97.0 SGD, offer worth $3,200;
    - uk: 52.0 GBP, offer worth £1,800.
  - **Rule 3:** the rate rows of Bancontact, iDEAL, MB WAY and Bizum go on CM-PAY-017, each with its method as filler (sg's 33 to 36; uk's 79, 80, 82 and 83).
  - **Rule 7:** uk's Capital footnote names Youlend for the United Kingdom (89). This is an `outside` line beside the `shows` one, scoped `www.shopify.com/uk and United Kingdom`. The cell already holds the UK's merchant cash advances issued by YouLend (SH-S-0485).
- **SH-75's rules:**
  - **Rule 1:** uk's USDC rates row goes on CM-PAY-018, with no filler (85).
  - **Rule 2:** za's cards state the third-party fee (SH-75's lines 108 to 118, whose sites include za), so za's processing row says its plans page states no card rate. The plans pages of sg and uk do state card rates.
  - **Rule 6:** no rate of mine is stated 'excl. VAT'.
  - **Rule 7:** the credits popover's rate is read by site. It is 1% on sg and uk (14, 17, 20; 59, 62, 65). The domain credit is $25 on sg and £15 on uk.
- **SH-76's rule 1:** uk's Klarna and TWINT rates rows go on CM-PAY-017, each with the method as filler (78, 81). They cite the held posts the coordinator's check after SH-77 found (SH-E-0ecae440, SH-E-fd124edd).
- **SH-77's rule 2:** each line quotes its own entry's currency.
  - sg's Plus is priced in US dollars on its card (21), in the table's Pay monthly (26) and in its POS summary (44), whose card rates and POS Pro price stay in Singapore dollars.
  - The other sg plans are priced in Singapore dollars.

**Twins, matched by meaning:**
- **1, 2:** www.shopify.com's POS FAQs take ie's lines (SH-76's lines 88, 89, 104 and 105) and nz's (SH-78), which differ only by their links.
- **3 to 8:** sa's entries take eg's lines (SH-74's lines 111, 136 to 142, 184, 185, 200 and 201), which differ only by their links. sa's international terms take ae's and eg's (SH-70's lines 61 to 63), which differ by the variant.
- **sg's and uk's pages:**
  - terms and processing rows: nz's (SH-77's lines 190 to 194);
  - card prices: ca's (SH-73's lines 182 to 199);
  - card rates and credits: nz's and hk-en's (SH-77's lines 197 to 202; SH-74's 212 to 217; SH-75's 4 to 12);
  - rows: hk-en's and ie's (SH-75's lines 13 to 22; SH-76's lines 2 to 18), by heading;
  - uk's hero: no-en's (SH-77's line 73);
  - uk's FAQ, disclaimer and footnotes: ie's (SH-76's lines 19 to 28);
  - sg's disclaimer and Credit footnote: hk-en's (SH-75's lines 25 to 30).
- **sg's and uk's summaries, POS Pro lists and POS FAQs:** ie's (SH-76's lines 32 to 105). ie's `card_rates` also hold online, in-person and third-party rates, with the 12-month incentive on the same three plans.
  - A script wrote the summaries' lines from items.jsonl lines 177 and 198, kind by kind as ie's 51 lines (`/tmp/claude-0/-home-user/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/SH-79/bin/gen_summaries.py`), and I read each one against its entry.
  - A summary's `card_rates.lowest` is named in its CM-PAY-007 reading. It is the in-person rate on most plans, and the online rate on uk's Plus, as SH-76's line 63 has ie's Plus. On sg's Starter it is both rates.
- **103 to 111:** za's entries take id's lines (SH-75's lines 99 to 105, 116, 117, 124 to 134 and 170 to 173). They differ by their links, the Google offer's 'R6,000' and the count of `signupTypes`.

**Rules for kinds the earlier rules don't cover,** for the coordinator:
1. **A terms entry that names no currency for a price is quoted as written.**
   - uk's three terms entries hold no `minimumMonthlyPriceCurrency` key at all. Their quality is 'minimumMonthlyPrice: £5', with no currency in brackets, and their readings say so.
   - sg's terms write the Basic annual price '$29.00' with no currency, beside a minimum price in Singapore dollars.

   This extends SH-78's rule 4, a rate written with no currency.
2. **A separator that the item holds as a no-break space is quoted as the entry's text writes it.** za's Plus card holds 'US$2 300' with a no-break space (U+00A0, items.jsonl line 203), and `entries.tsv` renders it as a plain space.
   - The quality copies the entry's text, which the checker matches.
   - The reading names the item's byte.

   This extends SH-75's rule 5 and SH-76's rule 3. Where the coordinator wants the source's byte instead, the two qualities of line SH-E-c3d06507 change.
3. **A held statement that a payment method is in early access** goes in the reading of the plan row's line, and the line stays `core`. MB WAY's help note is the case: 'MB WAY is in early access, and isn't available to all eligible merchants' (SH-E-413b6623, help.shopify.com's local payment methods page).
   - The help note is an entry of batch SH-31 (help-notes), which hadn't run when this batch ended; SH-30 was running beside it.
   - My MB WAY rows (35, 82) name it. The plan row includes the rates on every plan (SH-73's rule 3; the cell's SH-S-7025).
   - The six earlier MB WAY lines don't name it: SH-73's line 80, SH-74's line 11, SH-75's line 21, SH-76's line 15, SH-77's line 104, and SH-78's line on SH-E-39ecb960. Under the brief's flags ruling, the help note's own line would be `shows` on CM-PAY-017.

## New things

**`new:Earn 1% back on all sales as subscription credits`** (SH-68's), 8 lines:
- **sg's cards (14, 17, 20; SH-E-01b17303, SH-E-d66c10aa, SH-E-cca13015):** 'Earn up to $6,000 in credits', $8,500 and $11,000, with 'Get 1% back on sales' and 'Add a domain, get $25'.
- **sg's table row (28; SH-E-85783cb4):** 'Up to $6,000 SGD', 'Up to $8,500 SGD' and 'Up to $11,000 SGD', with a dash on Plus.
- **uk's cards (59, 62, 65; SH-E-74df85eb, SH-E-455b3480, SH-E-cbd09c50):** 'Earn up to £3,500 in credits', £5,500 and £7,000, with 'Get 1% back on sales' and 'Add a domain, get £15'.
- **uk's table row (73; SH-E-02a7be48):** 'Up to £3,500 GBP', 'Up to £5,500 GBP' and 'Up to £7,000 GBP', with a dash on Plus.

Each row's tooltip is 'Earn 1% back on all sales as subscription credits (0.5% on non-Shopify Payments). Valid for your first 6 months or until you reach the max.'

SH-68's notes give the rest:
- its place of its own: the table's row Earn 1% back on all sales;
- its proposed domain A, area PLN and parent CM-PLN-004, or CM-PLN-001;
- its Arabic words and the terms searched.

**The leads' cells, read:** none holds the platform's credits to the merchant.
- CM-PTN-008 holds nothing on Shopify. It is a referral programme's commission on the plans a member brings.
- CM-PAY-025 is Shopify Credit, a charge card with a credit limit.
- CM-SFR-008 is domains, a way to earn the domain credit.
- CM-CHK-002 is the buyer's cart, a lead by 'add'.
- CM-PLN-001 and CM-API-001 are leads by the plan names.

## Entries I couldn't tell, and what would settle each

- **MB WAY's rows (35, 82):** `core`, as their siblings, or `shows` because a held help note says MB WAY is in early access (rule 3 above). The help note's own placement in SH-31, and the coordinator's alignment of the eight MB WAY lines, would settle it.
- **The POS FAQ's iPad stand (1, 7, 50, 100, 110), `own-service` on CM-POS-002:** this keeps SH-70's rule 4, which the coordinator's check after SH-70 kept. `shows` is the other reading.
- **sg's terms' '$29.00' (9, 11, 40):** its currency isn't stated. The Basic card and summary state $35 SGD and 35 SGD a month paid yearly. Which price is charged, and in which currency, isn't held.

## A structure whose items and sources disagree

- **The terms' Basic annual price doesn't follow the site's own cards and summaries.** Each line quotes its own entry, as SH-72 to SH-78 quote theirs. Which price is charged isn't held.
  - sg: '$29.00', against $35 SGD (12, 27, 41).
  - uk: £19.00, against £22 (57, 72, 91).
  - za: $19.00 USD, against US$22 (SH-75's lines 106 and 134).
- **The Plus price differs between the plans and POS pages.**
  - sg: the plans page starts at $2,300 USD a month (21, 26), and the POS summary's monthly_price is 2500 USD, with 2300 USD its three-year price (44).
  - uk: £1,800 against 1950 GBP, with 1800 GBP the three-year price (66, 71, 94).
  - The readings say so, as SH-76's and SH-77's do.
- **sg's Plus is priced in US dollars** on a page priced in Singapore dollars (SH-77's rule 2).
- **The rendering and the item differ for za's Plus card:** a no-break space in the item, a plain space in the entry's text (rule 2 above). The source governs. The value is the same.
- **uk's terms hold no `minimumMonthlyPriceCurrency`,** where my other sites' terms state it (sa's, sg's and za's), and ie's state it empty (SH-76's notes).
- **The items and the entries otherwise agree.** I didn't print the WARC records (`meta.json`'s source). The items are the source's decoded loader data, by the register.

## What the sources state that no entry holds (for the second stage)

- **The tables' marks:** `compareAllFeatures.checkAlt` 'Included' and `dashAlt` 'Not included' on sg's, uk's and za's plans pages (items.jsonl lines 176, 197 and 203). R3 reads them.
- **The other pruned parts** (the hero's toggle, the sign-up links, the testimonial) are as SH-68 listed them for ae-ar. I didn't read them on these pages.
- **Leads in held entries outside this structure, not placed yet:**
  - the MB WAY help note SH-E-413b6623 (rule 3 above);
  - the admin plan feature set's MB WAY and Bizum rates (SH-E-227b4789, SH-E-0c9e8795, `requiresShopifyPayments: false`, batch SH-89), for CM-PAY-017.

## The checker's lines, read again

- **No `CHANGES`.** Every cell my lines touch already holds the same placement.
- **`NOTE` on `own-service` on CM-POS-002** (1, 7, 50, 100, 110): kept, by SH-70's rule 4 and the cell's own-service (SH-S-7269). The answer names Shopify as the stand's provider, 'Shopify's flexible iPad stand'.
- **`NOTE` on core on a product named with the platform's brand** (lines 9, 23, 146 and 277, the four processing rows): each is `core` by the cell's Shopify Payments rows, not by the brand, as its reading says.
- **`NOTE` on a new thing whose entry has leads** (lines 30, 34, 38, 50, 154, 158, 162 and 174): I read the leads' cells (above). None holds the credits. CM-PTN-008's lead, by 'earn' and 'sale', is a referral commission.
- **`NEW`:** Earn 1% back on all sales as subscription credits, 8 lines.
- No `NOTE` on a quote found nowhere held, and none on a footnote mark.

## Problems with the brief or the script

- **`entries.tsv` renders a no-break space as a plain space** (za's Plus card). A quote copied from the item's bytes would fail the checker. I followed the entry's text and named the byte (rule 2 above).
- **The held search for a payment method** found what the concern map didn't: the MB WAY help note, an entry of batch SH-31, which hasn't run. The prompt's instruction to search the held entries is what found it.
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief itself states (qualities wider than B-extent's list; the rulings).
- **Cost:** I can't measure it from here. The context stayed under about 200,000 tokens. Most lines follow checked twins, and the summaries were written by a script from their items.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 111 of 111 entries, no problem and no `CHANGES`. With this batch, all 1,056 entries of `pricing-page-data` are placed (SH-68 to SH-79).
- **Rules 1 to 3 stand:**
  - a price or rate with no currency is quoted as written;
  - a quote follows the entry's text where the build renders a no-break space as a plain space, the item's byte named in the reading;
  - MB WAY's plan rows stay `core`, the help note named in their readings.

  The coordinator's check after SH-30 gave the help note its own line in SH-31, `shows` on CM-PAY-017. The six earlier MB WAY rows aren't changed: a plan row is `core` whatever the note says.
- **The open choices stay as placed:** the iPad stand's `own-service` (SH-70's rule 4); sg's '$29.00' with no currency.
- **The new thing** (Earn 1% back on all sales as subscription credits) takes eight more lines, sg's and uk's cards and rows. It is decided with the others.
- **For SH-89:** the admin plan feature set's MB WAY and Bizum rates (SH-E-227b4789, SH-E-0c9e8795) take CM-PAY-017's line, as these rows do.
- **Cost:** 33.6 million tokens over 122 requests, about 303,000 an entry. The context reached about 443,000 tokens, not the 200,000 the agent estimated.
