# Held pass, Shopify, batch SH-75: notes

80 entries of `pricing-page-data` (effort high), evidence at observed-sh@e38dc17e3, in `structures/shopify/pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl`. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-75`).
- **1 to 20:** the rest of www.shopify.com/hk-en's plans page (items.jsonl line 67):
  - the Advanced and Plus cards with their card rates and credits (1 to 5);
  - the POS Pro card (6), the Agentic card and its rate (7, 8);
  - nine comparison rows: Pay monthly, POS Pro, the three online card rates, Bancontact, iDEAL, MB WAY and USDC rates (9 to 17);
  - one FAQ (18), the disclaimer and the Credit footnote (19, 20).
- **21 to 33:** hk-en's POS page (line 68): its terms entry, the six plan summaries, the two POS Pro plan entries, the four FAQs.
- **34, 35:** www.shopify.com/id's international page (line 81): its terms entry and its processing row.
- **36 to 52:** id's plans page (line 82), with my, pk, za and others where the words are the same: its terms entry, the Basic, Grow and Plus cards with their third-party fees and credits, the Pay monthly, Pay yearly and Earn 1% back rows, the disclaimer and two footnotes.
- **53 to 61:** id's POS page (line 83): its terms entry, the six plan summaries, two FAQs.
- **62, 63:** www.shopify.com/ie's international page (line 84): its terms entry and its processing row.
- **64 to 80:** ie's plans page (line 85): its terms entry, the hero, the four cards with their prices, the five features no other site's card names, the credits, the POS Pro card, the Agentic card and its rate. SH-76 begins with ie's comparison table.

**Placed:** 80 entries in 201 lines: 72 entries on capabilities (one of them, 67, also takes a `new` line), 8 entries `new` (SH-68's new thing), none `out`; 42 entries take more than one line. Supports, by line: 178 `core`, 11 `shows`, 10 `outside`, 2 `own-service`; no `extension-point`. 13 lines carry fillers; 146 carry qualities. The checker raises no `CHANGES`.

**Sources read:**
- the brief and what it names: the evidence map; the rulings, the last section most (the two added after SH-2 were read too; neither bears on these pages); B-extent.md's "Cells and evidence" and "Conventions from the dry run", with "What a place of its own is"; observed-sh's `README.md`, `docs/READING.md` (fetch runs, structures, indexes), `docs/GAPS.md` (nothing on these pages), `structures/README.md`; `structures/REGISTER.tsv`'s row for this structure; `selection.tsv`'s row; `show --meta`;
- SH-68's notes whole, SH-69's to SH-72's rules and coordinator's checks, SH-73's and SH-74's notes whole; the twins' lines by number (`earlier`, then `sed` on the placements);
- items.jsonl, by script: line 67's Advanced and Plus cards, comparison table (88 rows) and disclaimer list; line 82's table (76 rows) and hero; line 85's cards, Agentic and POS Pro cards and the table rows on payments, tax and bot protection; and every read site's plans page (lines 2 to 203), for which sites hold an Accepting payments section, a USDC rates row, an Agentic card, a `card_rates_short` that states the third-party fee, and the five ie feature keys. Every line's terms and quotes are its own entry's;
- the model: `cells` for every capability placed on and for the leads; `land_points.py cell CM-PAY-018 shopify`; `caps --terms` for 3D Secure, 3DS, 3-D Secure, card authentication, strong customer authentication, Secure checkout, fraud protection, GDPR, data protection, privacy, compliance, VAT, VAT collection, automatic VAT, tax collection, automated tax, General Data Protection Regulation, bot protection, business entity, business entities, entities, legal entity, manage businesses, Manage businesses by market, by market; `merged/evidence.tsv` and every platform's held placements, by grep, for USDC, 3D Secure, GDPR, bot protection and business entities.

## Rules followed

**SH-68's R0 to R11, SH-69's rules 1 to 7, SH-70's rules 1 to 9, SH-71's rules 1 to 3, SH-73's rules 1 to 8, SH-74's rules 1 to 5, and the rulings since, as kept.**
- **R0:** no entry of mine is on every read site of its language, so every line takes its labels, after its plans. The widest are on eight English sites (hk-en, id, il, my, ng, nz, pk, za: the Advanced and POS Pro cards, the POS Pro plan entries and three FAQs, 18, 30 and 32).
- **R1:** the six terms entries (21, 34, 36, 53, 62, 64; hk-en's plans and international pages' are SH-74's), three `core` lines each. `googleCountryOffer` gives no line.
- **R2:** the cards and their features; the POS Pro cards (6, 78) take their sites alone (the ruling after SH-70); a feature with no value takes its plan and the plans above it (67 to 69 on Basic: the four plans).
- **R3:** the rows, each on its twin's capability, matched by its heading: `earlier`'s pointer twins for 14 to 17 were other rows (ae's Third-party transaction fees, Built-in fraud analysis, note row and Hosting), its labels the right ones for Bancontact, iDEAL and MB WAY.
- **R4, R6, R7, R9:** the POS summaries, lists and FAQs; the qualities; the disclaimers' providers (`outside`, with fillers), WebBank's U.S. joined to the site with ` and ` (the ruling after SA-53).
- **SH-73's rule 1:** hk-en's and id's summaries hold no `card_rates.in_person`, so they take no CM-PAY-021 line; neither carries the 12-month incentive (rule 2).
- **SH-73's rule 3:** Bancontact, iDEAL and MB WAY rates on CM-PAY-017, the method as filler (14 to 16).
- **SH-74's rules 4 and 5:** the cards whose `card_rates_short` states the third-party fee (38, 41, 43, 46) are CM-PLN-003 `core`; the summaries whose `card_rates` hold only `third_party` (54 to 59) take no CM-PAY-007 line.
- **Twins, by meaning:** the hk-en summaries (22 to 27) take www.shopify.com/ae's lines (SH-72's), whose `card_rates` also hold an online rate and no in-person rate; the id summaries (54 to 59) take eg's and sa's (SH-74's), whose `card_rates` hold only the third-party fee. `earlier`'s pointer twins for them were ae-ar's, ca's and eg's alike.

**Rules for kinds the earlier rules don't cover,** for the coordinator to align with SH-76 to SH-79:
1. **A USDC rates row** (17) is CM-PAY-018 `core`, its rates by plan as quality, as the cell's own placement of the 30 September row USDC rates (SH-S-7028, `core`, no slot filler). It sits under Accepting payments, whose CM-PAY-001 is CM-PAY-018's parent, so it takes no section line (R3). USDC names the coin the buyer pays with, not who processes it, so it fills no slot, as the card brands in R9; the cell's fillers (Coinbase, Bridge) rest on other statements. Among the read sites, the tables of hk-en, ie, no-en, www.shopify.com and uk hold the row (items.jsonl lines 67, 85, 140, 161, 197).
2. **SH-74's rule 4 holds on English cards too.** Seven English sites' cards state the third-party providers' fee in `card_rates_short` ('2% 3rd-party payment providers' on Basic): id, il, in, my, ng, ph and za. Their tables hold 76 rows, with no Accepting payments section and no card rate row (items.jsonl lines 82, 91, 112, 133, 136, 150, 203). pk's cards hold no `card_rates_short` at all. So the twin with the same name key states another thing on these sites, as eg's and sa's do.
3. **SH-74's rule 5 holds on English POS pages too:** id's summaries (and my, pk, za, il, ng, ph's, by their labels) hold `card_rates` with `third_party` alone, and take no CM-PAY-007 line.
4. **ie's five card features,** which no other site's card names (the 61 plans pages, by script):
   - 'Fraud protection and 3D Secure checkout' (Basic) names two things. Fraud protection is CM-ORD-006 `core`, the fraud check its name says (`fraud_check_and_3d_secure_checkout`), as the cell holds the plan row Built-in fraud analysis*. 3D Secure checkout is the new thing below.
   - 'Tools for GDPR compliance' (Basic) is CM-TRU-005 `core`, a plan line that includes the platform's tools for the customers' personal data (R11's lead). The GDPR is the tools' subject, not their terms, so it fills no slot (R9).
   - 'Automatic VAT collection' (Basic) is CM-TAX-002 `core`, as its cell holds Shopify Tax for the EU and the UK, which automatically calculates and collects VAT (R11's lead).
   - 'Bot protection' (Plus) is CM-TRU-004 `core`, as the cell's plan row Bot protection, Plus only (SH-S-7074).
   - 'Manage businesses by market' (Plus) is CM-ACC-005 `core`: several business entities in one store, assigned to markets, which the cell holds for organizations on Plus and Enterprise (SH-S-0253, SH-S-0255).

   Each has no value, so it takes its plan and the plans above it (R2).
5. **A number written with a decimal comma or a thousands point is quoted as written,** as SH-68's check keeps the Arabic-Indic digits: id's Plus card 'US$2.300' (45), and id's and za's Balance footnote '3,54%' and '2,52%' (51), where the same table's row writes '2.52% earnings rate'.
6. **A rate stated without VAT keeps it in its quality:** ie's Agentic card, 'Card rates from 2% + €0.25 EUR online excl. VAT' (80), as ie's table rows write 'excl. VAT'.
7. **The credits' popover states its own rate by site:** 'Get 0.5% back on sales' on id, my, ph, pk and za (39, 42, 44), as on ae; 'Get 1% back on sales' on hk-en (3) and ie (70, 72, 74), as on ca. ie's domain credit is €15. Each line's quality gives its own.

## New things

**`new:3D Secure checkout`,** 1 line: 67's second line (SH-E-c82212c3), www.shopify.com/ie's Basic card.
- **What it is:** the buyer's card authenticated with 3D Secure at checkout, which the Basic plan includes: 'Fraud protection and 3D Secure checkout', name key `fraud_check_and_3d_secure_checkout`. The card states no more.
- **Its place of its own:** the plan's own list of what it includes, the card's `planFeatures`, read as a plan line ("a policy in the plan's own list", B-extent). Only ie's card states it; no comparison table of the 61 plans pages names it. If the coordinator reads a card's feature as no plan line, it has no place of its own, and the line is `shows`.
- **Its names:** English only, '3D Secure checkout'. No Arabic site states it.
- **Proposed:** domain C, area PAY or CHK. Parent CM-PAY-002 (the platform's own payment service, which processes the card) or CM-CHK-001 (checkout, where the buyer meets it). Their cells name no 3D Secure.
- **Searched:** `caps --terms` 3D Secure, 3-D Secure, 3DS, card authentication, strong customer authentication, Secure checkout, fraud protection (CM-ORD-006, CM-PAY-010, CM-SUP-001: fraud, not authentication); `merged/evidence.tsv` and every platform's placements, by grep: BigCommerce's gateway rows name 3D Secure among a provider's marks, on CM-PAY-011, and no Shopify cell names it.
- **The leads' cells, read:** CM-ORD-006 (fraud analysis: flags orders for review) and CM-TRU-004 (bot protection, by 'checkout' and 'protection'). Neither holds the card's authentication.

**`new:Earn 1% back on all sales as subscription credits`** (SH-68's), 8 lines:
- hk-en's Advanced card: 3 (SH-E-80a02d05), 'Earn up to $8,000 in credits';
- the id cards (on id, my, ph, pk and za): 39, 42 and 44 (SH-E-d5fa6b4c, SH-E-73583ce2, SH-E-603769c7), $3,500, $5,000 and $7,000, with 'Get 0.5% back on sales' and 'Add a domain, get US$20';
- the id table's row (the same five sites): 49 (SH-E-02e8e184), 'Up to $3,500 USD', 'Up to $5,000 USD' and 'Up to $7,000 USD', a dash on Plus;
- the ie cards: 70, 72 and 74 (SH-E-c05ae6b2, SH-E-3017fcb9, SH-E-9afa7ce0), €4,000, €6,000 and €8,000, with 'Get 1% back on sales' and 'Add a domain, get €15'.

Its place of its own (the table's row Earn 1% back on all sales), proposed domain A, area PLN, parent CM-PLN-004 (or CM-PLN-001), its Arabic words and the terms searched are in SH-68's notes. The leads' cells, read: CM-PTN-008 (holds nothing on Shopify; a referral programme's commission on plans a member brings), CM-PAY-025 (Shopify Credit, a charge card), CM-SFR-008 (domains, a way to earn the credit), CM-CHK-002 (the buyer's cart, by 'add'), CM-PLN-001 and CM-API-001 (by the plan names). None holds the platform's credits to the merchant.

## Entries I couldn't tell, and what would settle each

- **67, fraud protection on CM-ORD-006:** the card names a fraud check, which the cell's plan row Built-in fraud analysis* holds on every plan. CM-PAY-010 (Shopify Protect, cover against fraudulent chargebacks) is the other reading; its cell scopes it to businesses in the United States, and this is Ireland's card. A help page on what the Basic plan's fraud protection is in Ireland would settle it.
- **67, 3D Secure as new:** the other readings are a part of CM-ORD-006 (one line for the whole feature), or CM-PAY-002 or CM-CHK-001 `core`. A help page on 3D Secure in Shopify Payments or checkout would settle its parent; whether a card's feature is a plan line settles its support (above).
- **68 on CM-TRU-005, not a child:** 'Tools for GDPR compliance' names no tool; CM-TRU-006 (privacy settings, cookie consent) and CM-TRU-007 (data requests, erasure) are the children such tools would be. A help page on the GDPR tools would settle it. The line changes no cell either way.
- **77, no CM-MKS-001 line:** 'by market' is read as how the entities are divided, which CM-ACC-005's note holds ('assigned to markets'). If the coordinator reads markets as a thing the feature names, CM-MKS-001 `core` (Plus) is a second line; it changes no cell.
- **17, USDC with no filler:** the row names the coin, not its issuer or processor (rule 1).
- **The twins' doubts carry over,** as SH-73's and SH-74's notes list them: the iPad stand's `own-service` (31, 60; SH-70's rule 4, kept); 'every paid plan' and 'all plans' as the four plans (32, 33, 61); the transaction fees on CM-PLN-003 (30); the Plus summaries' 'POS Pro included' with `included_in_plan: false` (25, 57).

## A structure whose items and sources disagree

Each line quotes its own entry. Which price is charged isn't held. That the pages' different variants are the cause is an assumption, as SH-68's to SH-74's notes have it.
- **www.shopify.com/hk-en's Basic yearly price:** its plans page's card US$29 a month paid yearly (SH-74's line 210) and its POS page's summary `annual_monthly_price` 29 USD (22) stand beside the terms' 'basicAnnualPrice: <span>$25.00 USD</span>' on all three of its pages (21; SH-74's lines 202, 206). The plans page was served under 'e_0573c3a44a32b9562a4827c286953987:treatment,…', the POS page under 'e_06d1ad5d27d16046cc6d829de669769b:treatment,f_2e2905455a798fa9df40308c0b8b53ee:true,f_77c8150780b85c85656903fc3fada251:true'.
- **hk-en's Plus price:** the card 'from' US$2,300 (4) and the table 'Starts at $2,300 USD/mo' (9) are the summary's `triennial_monthly_price` 2300; its `monthly_price` is 2500 USD (25).
- **www.shopify.com/id's Basic yearly price:** the card US$22 (37), the Pay yearly row $22 USD/mo (48) and the summary 22 USD (54) stand beside the terms' 'basicAnnualPrice: <span>$19.00 USD</span>' on its three pages (34, 36, 53).
- **id's Plus card writes 'US$2.300'** (45) with a point, its table 'Starts at $2,300 USD/mo' (47) with a comma.
- **id's and za's Balance footnote writes '3,54%' and '2,52%'** (51), the id table's row '2.52% earnings rate' (items.jsonl line 82, row 62).
- **id's international page states Shopify Payments' processing rate, 3.9% per transaction (35),** while id's plans page states no card rate: its cards and POS summaries give only the third-party fee, and its table has no Accepting payments section. This is SH-74's eg case again; whether Shopify Payments is offered in Indonesia isn't stated in these entries.
- **www.shopify.com/ie's Basic yearly price:** the card €29 (66) against the terms' 'basicAnnualPrice: <span>€24.00</span>' (62, 64).
- **ie's POS Pro price:** the card '+€79' (78) against the terms' 'posProPriceUsd: $89' (62, 64), a price the key names in US dollars.
- **ie's terms leave `minimumMonthlyPriceCurrency` empty** (62, 64), as uk's pages and the euro sites' do (items.jsonl lines 84 to 86, 196 to 198), where hk-en's and id's name the currency: no disagreement, but the minimum price's currency is only its sign, '€5'.
- **The items and the entries agree:** the entries are the items' decoded loader data. I didn't print the WARC records.

## What the sources state that no entry holds (for the second stage)

- **The credits popover's tracking data,** pruned by the selection's rule (`duxTrackingMetadata`): on hk-en's Advanced card, 'eligibleIncentiveIds': 'free_domain_global,gmvRewardsAcquisition.mainline.sp', with 'plan': 'unlimited' (items.jsonl line 67, `hero.pricingCards[2].planFeatures[5].creditsPopover`). These are the incentives' own identifiers: a lead for the new thing's name and for the domain credit (CM-SFR-008).
- **A help page on 3D Secure, and on the fraud protection and GDPR tools of ie's Basic plan,** would settle 67 and 68 (above). None is in this structure.
- **Kept from SH-72's to SH-74's leads:** the POS pages' sales contact flow (`posContactModal`), on hk-en's and id's POS pages too; POS Pro's staff performance tracking and the endless aisle, which have no capability.

## The checker's lines, read again

- **No `CHANGES`.** Every cell my lines touch already holds its support. CM-PAY-018 was `core` from the 30 September row USDC rates (SH-S-7028); CM-ORD-006, CM-TRU-004, CM-TRU-005, CM-TAX-002 and CM-ACC-005, which ie's five features reach, were `core` already.
- **`NOTE` own-service on CM-POS-002 (31 and 60):** SH-70's rule 4, kept by the coordinator: “Shopify's flexible iPad stand” names Shopify as the stand's provider, as the cell's own-service (SH-S-7269).
- **`NOTE` on a product named with the platform's brand (lines 102 and 177: 35 and 63, Shopify Payments processing):** each is `core` by the cell's Shopify Payments route and plan rows, not by its name, as SH-74's line 205.
- **`NOTE` on a new thing whose entry has leads (lines 5, 109, 113, 115, 123, 188, 191, 194: the credits; line 184: 3D Secure):** the leads' cells are read above. None is the entry's thing.
- **`NOTE line 123`: its first lead CM-PTN-008 holds nothing.** It is a referral programme's commission on the plans a member brings, not credits on the merchant's own sales (SH-71's notes).
- **`NOTE line 186`: its first lead CM-OPS-004 holds nothing.** It is WooCommerce's store status report and tools, a lead by the word 'tools' only; 68's GDPR tools are CM-TRU-005's.
- **`NEW`:** 3D Secure checkout, 1 line; Earn 1% back on all sales as subscription credits, 8 lines.

## Problems with the brief or the script

- **`earlier`'s pointer twins still mislead where a site's table holds rows others lack:** for 14 to 17 the pointer twins were other rows; the labels found Bancontact, iDEAL and MB WAY. USDC rates had no label line, since no earlier batch held the row.
- **`earlier`'s twins of a POS summary mix kinds:** for each summary it prints ae-ar's, ae's, au's, ca's and eg's lines, with and without online and in-person rates. A note of which `card_rates` keys each twin holds would serve SH-76 to SH-79.
- **A quote with a straight apostrophe** (“What's included in POS Pro”, “Shopify's flexible iPad stand…”) is quoted with “ ”, as SH-73 and SH-74 did.
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief states (qualities wider than B-extent's list; the rulings).

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 80 of 80 entries, no problem and no `CHANGES`.
- **Rules 1 to 7 stand, for SH-76 to SH-79.** Rule 1's USDC rows follow the cell's own placement of the 30 September row, CM-PAY-018 `core` (SH-S-7028).
- **The new thing takes SH-54's name.** Line 67's `new:3D Secure checkout` is now `new:3D Secure`, the same new thing SH-54 named. A card feature is a plan line (SH-68's R2), so it stays `core`.
- **The open calls, decided:**
  - 67's fraud protection stays on CM-ORD-006, as the plan row Built-in fraud analysis is placed there. CM-PAY-010's Shopify Protect is scoped to the United States.
  - 68's GDPR tools stay on CM-TRU-005, since the card names no one of its children's things.
  - 77 takes no CM-MKS-001 line. Neither changes a cell.
- **The twins.** `held_entries.py earlier` now prints which `card_rates` a plan summary twin holds (online, in-person, third-party), so a summary with fewer rates is told from its twin at a glance.
- **The price disagreements** are quoted each in its own line, as SH-72's to SH-74's were.
- **Cost:** 20.2 million tokens over 84 requests, about 253,000 an entry. The context reached about 416,000 tokens, not the 230,000 the agent estimated.
