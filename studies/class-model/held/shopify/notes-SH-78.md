# Held pass, Shopify, batch SH-78: notes

80 entries of `pricing-page-data` (effort high), evidence at observed-sh@e38dc17e3, in `structures/shopify/pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl`. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-78`). Every entry is labelled with one site.
- **1 to 11:** the rest of www.shopify.com/nz's plans page (items.jsonl line 146): the Plus card's card rate (1), the Agentic card's rate (2), seven comparison rows under Accepting payments (3 to 9: Online standard, Online Amex and Online international rates, Bancontact, iDEAL, MB WAY and In-person card rates), the disclaimer (10) and the Credit footnote (11).
- **12 to 20:** nz's POS page (line 147): its terms entry, the six plan summaries, two FAQs.
- **21 to 33:** www.shopify.com/ph: its international page (line 149: terms, processing row), its plans page (line 150: terms, the Basic and Grow cards, the disclaimer, the Credit footnote) and its POS page (line 151: terms, the Basic, Grow and Advanced summaries, two FAQs).
- **34 to 45:** www.shopify.com/pk: its international page (line 155: 34, 35), its plans page (line 156: terms, four card features no other read site names, the disclaimer, the Credit footnote: 36 to 42) and its POS page (line 157: terms, two FAQs: 43 to 45).
- **46 to 73:** www.shopify.com's plans page (line 161): its terms entry, the four cards with their card rates and credits, the Grow card's shipping discount, the Agentic card's rate (46 to 59); the Pay yearly row, nine rows under Accepting payments (Online standard, Online premium and Online international rates, PayPal Wallet, MB WAY, Bizum, In-person card, USDC and In-person manual rates) and the Shipping discounts row (60 to 70); the disclaimer with its Credit and Capital footnotes (71 to 73).
- **74 to 80:** www.shopify.com's POS page (line 162): its terms entry and the six plan summaries. SH-79 begins with the same page's FAQs (SH-E-839e5105).

**Placed:** 80 entries in 238 lines. 77 entries are on capabilities and 3 are `new` (SH-68's new thing); none is `out`. 44 entries take more than one line.
- Supports, by line: 204 `core`, 11 `shows`, 20 `outside`, 3 `own-service`; no `extension-point`.
- 27 lines carry fillers and 181 carry qualities.
- The checker raises three `CHANGES`, all from one entry (39), below.

**Sources read:**
- **The brief and what it names:** the evidence map; the rulings, the last section most; B-extent.md's "Cells and evidence" and "Conventions from the dry run", with "What a place of its own is"; observed-sh's `README.md` (Starting points), `docs/READING.md` (fetch runs, structures, indexes), `docs/GAPS.md` (nothing on these pages) and `structures/README.md`; `structures/REGISTER.tsv`'s row 141; `index/ledger-summary.tsv` and `index/ledger/sitemap--shopify-com-sitemaps.tsv` (nz's three pages captured by run 20261031T003815Z-shopify-com-pricing-by-country); `selection.tsv`'s row; `show --meta`.
- **The earlier batches:** SH-68's notes whole (R0 to R11); the rules and coordinator's checks of SH-69 to SH-76; SH-77's notes whole. I read each twin's lines by number (`earlier`, then `awk` on the placements).
- **items.jsonl, by script, to clarify only:** line 146's and line 161's comparison tables (their headings, marks and sections) and disclaimer lists; lines 150 and 156's tables (76 rows, no Accepting payments section); lines 156 and 161's cards with their features; every plans page (the 61) for the four pk feature keys; lines 150, 151, 155 to 157, 161 and 162 for `signupTypes`. Every line's terms and quotes are its own entry's, or another entry's that its reading names by id.
- **The model:** `cells` for every capability placed on (name, note, cell), for CM-MKT-005, CM-MKT-008, CM-CNT-007, CM-SEL-006, CM-MKT-021, CM-MKT-023, CM-MKS-002, CM-MKT-001 and CM-PAY-013 whole, and for the new thing's leads (CM-PTN-008, CM-SFR-008, CM-CHK-002, CM-API-001); `caps --terms` for marketing across channels, track marketing, marketing attribution, attribution, SEO, product recommendations, recommendations, upsell, cross-sell, schedule launches, scheduled, schedule, launch, rollouts, scheduled discounts, PayPal, PayPal Wallet, wallet, manual card entry, manual entry, keyed, premium card, business cards; `merged/evidence.tsv`, `interfaces.tsv`, `qualities.tsv` and `slot-fillers.tsv`, by grep, for the cells that cite the 30 September rows SH-S-7019 to SH-S-7049; and the held entries, by grep over `entries.tsv` and the placements, for PayPal, manual rates, premium card rates and the four pk feature keys.

## Rules followed

**SH-68's R0 to R11, SH-69's rules 1 to 7, SH-70's 1 to 9, SH-71's 1 to 3, SH-73's 1 to 8, SH-74's 1 to 5, SH-75's 1 to 7, SH-76's 1 to 3, SH-77's 1 and 2, and the rulings since, as kept.**
- **R0:** each entry is one site's, so every line takes its site, after its plans.
- **R1:** the nine terms entries (12, 21, 23, 28, 34, 36, 43, 46, 74), three `core` lines each. `googleCountryOffer` gives no line.
- **R2:** the cards with their card rates and credits, each on its card's plan; a feature with no value (37 to 39) takes Basic and the plans above it, and 40 takes Plus; the Agentic rates (2, 59) on 'Agentic' and the site.
- **R3:** the rows, each matched to its twin by its heading, not its pointer (below); no row of mine takes a section line, since each one's capability is the section's own or below it: CM-PLN-001 for Pricing's Pay yearly; CM-PAY-001's children and their children for Accepting payments; CM-SHP-001's child CM-SHP-002 for Shipping.
- **R4, R6, R7, R9:** the POS summaries and FAQs; the qualities; the disclaimers' providers, `outside` with fillers, and WebBank's U.S. joined to the site with ` and ` (the ruling after SA-53).
- **SH-73's rules 1 and 2:** nz's and www.shopify.com's summaries state `card_rates.in_person` on all six plans, so each takes a CM-PAY-021 line; their Basic, Grow and Advanced carry the 12-month incentive (67.0 USD, offer worth $2,400), each a second CM-POS-001 line scoped `<plan>;<site> and retail_term_commitment_12_months`. ph's summaries state neither.
- **SH-73's rule 3:** Bancontact, iDEAL, MB WAY and Bizum rates on CM-PAY-017, each method its filler (6 to 8, 65, 66). Held posts name them among the payment methods through Shopify Payments: SH-E-fd124edd names Bancontact and iDEAL, SH-E-0ecae440 iDeal (both placed in SH-36). 6's and 7's readings cite them, as the coordinator's check after SH-77 asked for Klarna's and TWINT's.
- **SH-73's rule 6:** `shipment_short` on Grow, CM-SHP-002 (52). **Rule 5:** the Shipping discounts row on CM-SHP-002 with its carriers, and CM-SHP-015 `shows` (70).
- **SH-74's rule 5 and SH-75's rule 3:** ph's summaries (29 to 31) hold `card_rates` with `third_party` alone, so they take no CM-PAY-007 line.
- **SH-75's rule 1:** the USDC row on CM-PAY-018, no filler (68). **SH-75's rule 2:** ph's cards give the third-party fee (SH-75's lines 108 to 118); pk's cards name no card rate at all; both tables hold 76 rows with no Accepting payments section, as the processing rows' readings say (22, 35).
- **SH-75's rule 7:** the credits popover's rate by site: 1% on www.shopify.com (49, 53, 56).
- **A summary's `card_rates.lowest`** is named in its CM-PAY-007 reading: the in-person rate on most plans, the online rate on www.shopify.com's Plus (78), as SH-76's line 63 has ie's Plus.
- **SH-77's rule 2:** each line quotes its own currency: nz's card rates in New Zealand dollars beside its prices in US dollars (1, 13 to 18).

**Twins, matched by meaning:**
- **nz's rows 3 to 9** take hk-en's (SH-75's lines 16 to 21) and ie's In-person card rates (SH-76's line 17); `earlier`'s pointer twins for 6 to 9 were other rows (ca's MB WAY, Bizum and Interac rates, ie's Klarna, TWINT and others), and its labels the right ones.
- **nz's and www.shopify.com's summaries** take ie's (SH-76's lines 32 to 82), whose `card_rates` also hold online, in-person and third-party rates, with the 12-month incentive on the same three plans. **ph's** take ng's (SH-77's lines 50 to 61) and id's Advanced (SH-75's lines 146 to 153), whose `card_rates` hold only the third-party fee.
- **ph's, pk's and www.shopify.com's terms, processing rows, disclaimers, footnotes and FAQs** take my's and ng's (SH-77's lines 2 to 65), nz's (SH-77's lines 190 to 202) and ie's (SH-76).
- **www.shopify.com's cards** take ca's (SH-73's lines 182 to 199), and its rows hk-en's, ie's and ca's (SH-75, SH-76, SH-74's lines 16 and 17), by heading.

**Rules for kinds the earlier rules don't cover,** for the coordinator to align with SH-79:
1. **PayPal Wallet rates** (64, www.shopify.com) is CM-PAY-013 `core`, its rate as quality ('Starting at 3.49% + 49¢' on every plan), with no filler.
   - This is the cell's own placement of the 30 September row PayPal Wallet rates (SH-S-7024, `core`, no slot filler; `interfaces.tsv` names it exactly). The cell also holds PayPal Wallet paid through Shopify Payments in France and the United States (SH-S-0312).
   - PayPal Wallet names what the buyer pays with, as the card brands and USDC do (SH-68's R9; SH-75's rule 1), so it fills no slot. The local methods take their method as filler (SH-73's rule 3) because the cell's own placement of their rows does.
   - CM-PAY-013's parent is CM-PAY-012, whose parent is CM-PAY-001, so the row takes no section line.
   - Held entries of other structures state the same row: SH-E-a7f3150f (`plan-feature-set`, type paypal_wallet_rates, 'requiresShopifyPayments: false'), SH-E-169e25e0 and SH-E-36db39e6 (`plan-page-public`). They are SH-88's and SH-89's, not placed yet.
2. **Online premium card rates** (62, www.shopify.com, where the other sites write Online Amex card rates) is CM-PAY-007 `core`, as the cell's SH-S-7022. Its tooltip, 'Includes business cards and American Express.', names the cards the rate is for, so no filler (R9). The buyer's business cards aren't CM-PAY-024's, the merchant's own cards on its money account.
3. **In-person manual rates** (69, www.shopify.com) is CM-PAY-021 `core`, beside In-person card rates, as the cell's own placement of SH-S-7029 and its note ('the plan rows In-person card rates and In-person manual rates'). What manual means isn't stated: card details entered by hand is a reading (below).
4. **A table's rate written with no currency, or as a surcharge,** is quoted as written: www.shopify.com's rows write '2.9% + 30¢' where its cards write 'USD' (61), and its Online international rates row writes '+ 1%' on every plan (63), where the other sites' rows state whole rates.
5. **pk's four card features** (37 to 40), which no other read site's card names (only pk's and the unread pk-ur's, items.jsonl lines 153 and 156), follow SH-68's R11 leads, searched again:
   - 'Track marketing across channels' is CM-MKT-005 `core`, Shopify's Marketing and Campaigns, since a held Editions card says 'Manage and measure your marketing across channels with Campaigns' (SH-E-7a30434a, in SH-61, not run). CM-MKT-008, sales attribution, R11's lead, is the other reading (below).
   - 'Built-in SEO features' is CM-CNT-007 `core`, a plan line that states the SEO built in, which the cell's reading said no held statement showed.
   - 'Upsell with bundles and recommendations' names three things, each with its line, `core`: bundles (CM-SEL-006), upselling (CM-MKT-021) and recommendations (CM-MKT-023). These are the batch's three `CHANGES` (below).
   - 'Schedule launches and discounts' (Plus) is CM-MKS-002 `core`, Rollouts, as a held Editions post says, 'Create and schedule launches, events, or experiments that include your theme, checkout configuration, catalogs, and discounts all as one rollout.' (SH-E-22a4fbbe, in SH-47, not run). Its scheduled discounts also take CM-MKT-001 `core`, as R11 has it. Neither line changes a cell.
6. **A Plus summary with a paid trial** (78, www.shopify.com: 'paid_trial: {price: {amount: 399.00 …}; length: 1}') takes it as a quality of its CM-PLN-001 line, as the other summaries' paid trials. It is the Plus card's '$399 for your first month' (57). ie's and nz's Plus summaries state none.

## New things

**`new:Earn 1% back on all sales as subscription credits`** (SH-68's), 3 lines: www.shopify.com's cards, 49, 53 and 56 (SH-E-16db4bb1, SH-E-9796719e, SH-E-335f36a9): 'Earn up to $5,000 in credits', $7,500 and $10,000, with 'Get 1% back on sales' and 'Add a domain, get $20'. These are the maximums of the table row of il, nz and www.shopify.com (SH-E-3787fad6, SH-76's line 124).

SH-68's notes give the rest: its place of its own (the table's row Earn 1% back on all sales), its proposed domain A, area PLN and parent CM-PLN-004 (or CM-PLN-001), its Arabic words and the terms searched.

**The leads' cells, read:** none holds the platform's credits to the merchant. CM-PTN-008 holds nothing on Shopify: a referral programme's commission on the plans a member brings. CM-SFR-008 is domains, a way to earn the domain credit. CM-CHK-002 is the buyer's cart, a lead by 'add'. CM-PLN-001 and CM-API-001 are leads by the plan names.

No other `new` thing: the four pk features, PayPal Wallet rates, Online premium card rates and In-person manual rates each have a capability whose cell or name holds the same thing.

## Entries I couldn't tell, and what would settle each

- **37, 'Track marketing across channels', on CM-MKT-005:** the card states no more. CM-MKT-008 (crediting orders to marketing, Shopify's Attribution) is the other reading, since tracking marketing can mean attributing its sales. Neither changes a cell. What would settle it: the admin's Marketing or Campaigns page, or SH-61's placement of SH-E-7a30434a, whose words the line borrows.
- **39, 'Upsell with bundles and recommendations', on CM-SEL-006, CM-MKT-021 and CM-MKT-023** (the `CHANGES`): the card names no tooltip, so what the recommendations are, and where buyers see them, isn't stated.
  - The other reading is CM-SEL-006 alone, with upselling as the bundles' purpose and recommendations too general to place.
  - CM-MKT-023's note keeps it apart from CM-MKT-021 because no statement called recommendations a means of upsell; this one does, which bears on the reviewer's nesting.
  - What would settle it: a held help page on Shopify's product recommendations (the Search & Discovery app or the theme's recommendations), or the plan-feature-set's description of the key, if a later structure holds one (the held `plan-feature-set` entries name no such key).
- **40, the CM-MKT-001 line:** a rollout schedules discounts too (CM-MKS-002's note), so the discounts could be Rollouts' alone.
- **64, PayPal Wallet rates with no filler:** rule 1 above. PayPal as filler is the other reading, as SH-73's rule 3 gives the local methods theirs and SH-37's line on the dispute post (SH-E-124a02ba) gives CM-PAY-013 PayPal as filler. 'Starting at' makes the rate a minimum.
- **69, In-person manual rates:** manual isn't defined in the row. The POS app's setting 'Allow manual card entry' (`pos-settings`, SH-E-fb68268b) is a lead, read only to clarify.
- **The twins' doubts carry over,** as SH-73's to SH-77's notes list them:
  - the iPad stand's `own-service` (19, 32, 44; SH-70's rule 4, kept);
  - 'all plans' read as the four plans (20, 33, 45);
  - the Plus summaries' 'POS Pro included' beside `included_in_plan: false` (16, 78).

## A structure whose items and sources disagree

Each line quotes its own entry. Which price is charged isn't held. That the pages' variants are the cause is an assumption, as SH-68's to SH-77's notes have it.
- **www.shopify.com/ph:** the terms state 'basicAnnualPrice: <span>$19.00 USD</span>' on all three pages (21, 23, 28).
  - The plans page's cards state $22, $58 and $359 a month paid yearly (24, 25; SH-E-5e019eb6, the Advanced card of ae and ph), as its table's Pay yearly row does.
  - The POS page's summaries state 19, 49 and 299 USD (29 to 31), which agree with the terms.
  - The POS page was served with no experiment of its own ('f_2e2905455a798fa9df40308c0b8b53ee:true,f_77c8150780b85c85656903fc3fada251:true', signupTypes 'paid_trial_experience' alone, 28), the plans page under the e_0573c3a44a32b9562a4827c286953987 and e_06d1ad5d27d16046cc6d829de669769b treatments (23).
- **www.shopify.com/pk:** the terms' $19.00 USD (34, 36, 43) stands beside the site's Basic card's US$22 (SH-E-74c114a7) and its POS summary's 22 USD (SH-E-bdff9e26), the card and summary of id, my, pk and za.
- **www.shopify.com:** the terms' $24.00 USD (46, 74) stands beside the Basic card's $29 a month paid yearly (47), the Pay yearly row's $29 USD/mo (60) and the Basic summary's 29 USD (75).
- **www.shopify.com/nz:** the POS terms' $29.00 USD (12) stands beside the Basic summary's 35 USD (13) and the Basic card's US$35 (SH-E-54a1b998). Its card rates are in New Zealand dollars, its prices in US dollars.
- **The Plus summaries' monthly 2500 USD** (16, 78) stand beside the cards' 'from' $2,300 (SH-E-1496d20e; 57), which is the summaries' three-year price.
- **ph's and pk's international pages state Shopify Payments' processing rate,** 3.9% per transaction (22, 35), while their plans pages state no card rate: SH-74's eg case again.
- **The items and the entries agree:** the entries are the items' decoded loader data. I didn't print the WARC records.

## What the sources state that no entry holds (for the second stage)

- **The unread pk-ur page** (Urdu, items.jsonl line 153) states pk's four card features in its own words, by the same keys: 'مختلف چینل پر مارکیٹنگ ٹریک کریں', 'بلٹ ان SEO فیچر', 'بنڈل اور تجاویز کے ساتھ اپ سیل کریں', 'لانچ اور ڈسکاؤنٹ شیڈول کریں'.
- **The credits popover's pruned tracking data** (`duxTrackingMetadata`, removed by the selection's rule): www.shopify.com's cards 'free_domain_global,gmvRewardsAcquisition.mainline.sp' with 'Get 1% back on sales' (line 161); pk's 'free_domain_global,gmvRewardsAcquisition.mainline.nonSp' with 'Get 0.5% back on sales' (line 156). This adds to SH-76's and SH-77's lead that `sp` and `nonSp` stand for Shopify Payments and non-Shopify Payments, which is an assumption.
- **For the coordinator to align, not the second stage:** held entries of structures whose batches haven't run state the same things as my lines:
  - `plan-feature-set` and `plan-page-public` (SH-88, SH-89): PayPal Wallet rates (SH-E-a7f3150f, SH-E-169e25e0, SH-E-36db39e6), Online premium card rates (SH-E-b3746d83, SH-E-9a9f6806, SH-E-3897e0ca), In-person manual rates (SH-E-ad79c857, SH-E-e4e28fc7, SH-E-881232d5);
  - Editions (SH-47, SH-61): rollouts' 'schedule launches' (SH-E-22a4fbbe) and Campaigns' 'marketing across channels' (SH-E-7a30434a).
- **Kept from SH-72's to SH-77's leads:** the POS pages' sales contact flow (`posContactModal`); POS Pro's staff performance tracking and the endless aisle, which have no capability.

## The checker's lines, read again

- **`CHANGES CM-MKT-021@shopify gains core, by line 129`** (39): kept. A plan line includes upselling, made with the platform's own bundles and recommendations; what a plan line includes is `core` (M-9). The cell held only the App Store category Upsell and cross-sell apps (`extension-point`). The other reading is under "couldn't tell".
- **`CHANGES CM-MKT-023@shopify gains core` and `holds nothing: becomes held`, by line 130** (39): kept. The same plan line names recommendations as its own thing, a means of upsell, so rule 2 gives them a line. It is the one held Shopify statement of recommendations to buyers; the cell's reading had found only offers. The other reading is under "couldn't tell".
- **`NOTE` own-service on CM-POS-002** (19, 32, 44): SH-70's rule 4, kept by the coordinator. “Shopify's flexible iPad stand” names Shopify as the stand's provider, as the cell's `own-service` holds (SH-S-7269).
- **`NOTE` on a product named with the platform's brand** (lines 78 and 122: entries 22 and 35, ph's and pk's Shopify Payments processing rows): each is `core` by the cell's Shopify Payments rows, not by its name, as SH-77's lines 9 and 29.
- **`NOTE` on a new thing whose entry has leads** (lines 152, 157, 161): the leads' cells are read above. None is the entry's thing.
- **`NEW`:** Earn 1% back on all sales as subscription credits, 3 lines.

## Problems with the brief or the script

- **`class_slice.py search` reads only the concern map**, as SH-77 found, so I searched the held entries by grep for every new kind of row. That found the `plan-feature-set` and `plan-page-public` entries of the same rows, and the two Editions entries that clarify 37 and 40.
- **`earlier` has nothing for the pk feature keys,** since no batch had held them; their capabilities rest on R11's leads, the cells and the two held Editions entries.
- **Quotes:** a quote with a straight apostrophe is written with “ ” (SH-73 to SH-77). A quote from another entry names that entry's id (37, 40, 78).
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief states itself (qualities wider than B-extent's list; the rulings).

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 80 of 80 entries, no problem.
- **The three `CHANGES` stand,** from pk's Basic card feature 'Upsell with bundles and recommendations' (39). A plan line names upsell, so CM-MKT-021 gains `core` beside its App Store category, and recommendations, so CM-MKT-023 becomes held, `core`. That the recommendations are products recommended to buyers is a reading, marked in the line.
  - **Read again when the new things are decided:** CM-MKT-023's note keeps it apart from CM-MKT-021 because no statement called recommendations a means of upsell. This card does, which bears on the reviewer's nesting.
- **One line aligned.** PayPal Wallet rates (64) takes the cell's own filler, PayPal, as every other held line on CM-PAY-013 does. That covers Shopify's, WooCommerce's and BigCommerce's lines, and the model's slot fillers, which name PayPal for each platform. Rule 1's reason for no filler doesn't hold: the 30 September row has no slot filler of its own, but the cell does (SH-S-0023). Salla's one line without the filler, SA-15's line 134, is aligned too.
- **Rules 2 to 6 stand,** for SH-79 and the later batches of the same rows (`plan-feature-set` and `plan-page-public`):
  - Online premium card rates on CM-PAY-007;
  - In-person manual rates on CM-PAY-021;
  - a rate quoted as written;
  - pk's four features on their lines;
  - a Plus paid trial as a quality.
- **The open choices stay as placed:**
  - 'Track marketing across channels' on CM-MKT-005. SH-61 places the Editions card whose words it borrows (SH-E-7a30434a).
  - 'Schedule launches and discounts' on CM-MKS-002 and CM-MKT-001.
- **The new thing** (Earn 1% back on all sales as subscription credits) takes three more lines, the cards' maximums. It is decided with the others.
- **Cost:** 29.4 million tokens over 98 requests, about 368,000 an entry. The context reached about 513,000 tokens.
