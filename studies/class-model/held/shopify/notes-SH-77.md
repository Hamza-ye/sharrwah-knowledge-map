# Held pass, Shopify, batch SH-77: notes

81 entries of `pricing-page-data` (effort high), evidence at observed-sh@e38dc17e3, in `structures/shopify/pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl`. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-77`). Every entry is labelled with one site.
- **1, 2:** www.shopify.com's international page (items.jsonl line 114): its terms entry and its Shopify Payments processing row.
- **3 to 10:** www.shopify.com/my: its international page (line 132: terms, processing row), its plans page (line 133: terms, the disclaimer `apyDisclaimer`, the Credit footnote) and its POS page (line 134: terms, two FAQs). Its cards, rows and summaries are other batches' entries, in id's words (SH-75).
- **11 to 24:** www.shopify.com/ng: its international page (line 135: 11, 12); its plans page (line 136: terms, the Basic and Grow cards, the Pay monthly and Pay yearly rows, the disclaimer, the Credit footnote: 13 to 19); its POS page (line 137: terms, the Basic and Grow summaries, two FAQs: 20 to 24).
- **25 to 72:** www.shopify.com/no-en:
  - its international page (line 139: 25, 26);
  - its plans page (line 140: 27 to 59): terms, hero, the four cards with their card rates and credits, the POS Pro card, the Agentic card and its rate; 13 comparison rows (Pay monthly, Pay yearly, Earn 1% back, POS Pro, the three online card rates, Klarna, Mobilepay, MB WAY, Bizum, In-person card and USDC rates); one FAQ; the disclaimer with its Balance and Credit footnotes;
  - its POS page (line 141: 60 to 72): terms, the six plan summaries, the two POS Pro plan entries, the four FAQs.
- **73 to 81:** www.shopify.com/nz: its international page (line 145: 73, 74) and its plans page (line 146: terms, then the Basic, Grow and Advanced cards' card rates and credits). SH-78 begins with nz's Plus card rate (SH-E-33182bfc).

**Placed:** 81 entries in 201 lines. 74 entries are on capabilities and 7 are `new` (SH-68's new thing); none is `out`. 43 entries take more than one line.
- Supports, by line: 171 `core`, 12 `shows`, 15 `outside`, 3 `own-service`; no `extension-point`.
- 19 lines carry fillers and 148 carry qualities.
- The checker raises no `CHANGES`.

**Sources read:**
- **The brief and what it names:** the evidence map; the rulings, the last section most; B-extent.md's "Cells and evidence" and "Conventions from the dry run", with "What a place of its own is"; observed-sh's `README.md`, `docs/READING.md` (fetch runs, structures), `docs/GAPS.md` (nothing on these pages) and `structures/README.md`; `structures/REGISTER.tsv`'s row for this structure; `selection.tsv`'s row; `show --meta`.
- **The earlier batches:** SH-68's notes whole (R0 to R11); the rules and coordinator's checks of SH-69 to SH-75; SH-76's notes whole. I read each twin's lines by number (`earlier`, then a script over the batches' lists and placements).
- **items.jsonl, by script, to clarify only:**
  - lines 133, 136, 140, 146 and 161: the comparison tables' payment rows and the marks ¹ ² ³ of the Balance, Capital and Credit rows;
  - lines 133, 136 and 140: the disclaimers' list order (Balance, Cashback, Capital);
  - lines 85, 140 and 146: the credits popover's pruned `eligibleIncentiveIds`.

  Every line's terms and quotes are its own entry's, or those of another entry its reading names by id.
- **The model:**
  - `cells` for CM-PAY-017 and CM-PAY-015 (Klarna and Mobilepay), for the new thing's leads (CM-PTN-008, CM-PAY-025, CM-SFR-008, CM-CHK-002, CM-APP-012, CM-API-001), and the name and note of every other capability placed on;
  - `caps --terms` for MobilePay, Mobilepay and Vipps, with no hit;
  - every platform's held placements, by grep, for Mobilepay: SH-34's and SH-36's lines on the changelog posts SH-E-0fd1fcfa, SH-E-fd124edd and SH-E-0ecae440.

## Rules followed

**SH-68's R0 to R11, SH-69's rules 1 to 7, SH-70's 1 to 9, SH-71's 1 to 3, SH-73's 1 to 8, SH-74's 1 to 5, SH-75's 1 to 7, SH-76's 1 to 3, and the rulings since, as kept.**
- **R0:** each entry is one site's, so every line takes its site, after its plans.
- **R1:** the twelve terms entries (1, 3, 5, 8, 11, 13, 20, 25, 27, 60, 73, 75), three `core` lines each. `googleCountryOffer` gives no line.
- **R2:**
  - the cards with their card rates and credits, each on its card's plan;
  - the POS Pro card (40) on its site alone (the ruling after SH-70);
  - the Agentic card and its rate (41, 42). no-en is among SH-71's ten sites with an Agentic card.
- **R3:** the rows, each matched to its twin by its heading, not its pointer (below).
- **R4, R6, R7, R9:** the POS summaries, lists and FAQs; the qualities; the disclaimers' providers, `outside` with fillers, and WebBank's U.S. joined to the site with ` and ` (the ruling after SA-53).
- **SH-73's rules 1 and 2:** no-en's summaries state `card_rates.in_person` on Basic, Grow, Advanced, Plus and Retail, so those five take CM-PAY-021 lines. Starter's states no in-person rate, so it takes none, where ie's Starter does. No summary of mine carries the 12-month incentive.
- **SH-74's rule 5 and SH-75's rule 3:** ng's summaries (21, 22) hold `card_rates` with `third_party` alone, so they take no CM-PAY-007 line.
- **SH-75's rule 2:** my's and ng's cards state the third-party fee (SH-75's lines 108 to 118, whose sites include both), so their processing rows' readings say their plans pages state no card rate. www.shopify.com's, no-en's and nz's plans pages do state card rates.
- **SH-73's rule 3 and SH-76's rule 1:** Klarna, MB WAY and Bizum rates go on CM-PAY-017, each with the method as filler (50, 52, 53). Mobilepay rates is placed the same way (rule 1 below).
- **SH-75's rule 1:** the USDC rates row goes on CM-PAY-018, with no filler (55).
- **SH-75's rule 5 and SH-76's rule 3:** numbers are quoted as written:
  - no-en's cards group thousands with a space, '1 030 kr NOK', '4 490 kr NOK' and '3 370 kr NOK' (plain spaces, U+0020), where its table writes 'kr1,030 NOK/mo';
  - its Balance footnote writes '3,54 %' and '2,52 %', with a decimal comma and a space before the sign.
- **SH-75's rule 6:** no-en's and nz's rates aren't stated 'excl. VAT', so their qualities have nothing to keep.
- **SH-75's rule 7:** the credits popover's rate is read by site. nz's cards say 'Get 1% back on sales' (77, 79, 81). no-en's cards have no popover, only the tooltip (31, 34, 37), as au's cards (SH-73's line 47).

**Twins, matched by meaning:**
- **my's and ng's pages** take www.shopify.com/il's lines (SH-76's lines 106 to 149): its terms entries, processing row, disclaimer, Credit footnote and POS FAQs. By script (difflib), each entry differs from il's only by the site's links.
- **ng's cards and rows** (14 to 17) take il's and nz's (SH-76's lines 113 to 123), and differ only by their prices.
- **ng's summaries** (21, 22) take il's (SH-76's lines 134 to 145), whose `card_rates` also hold the third-party fee alone. `earlier` printed ae-ar's, ae's, au's, ca's, eg's and hk-en's twins, but not il's or id's (problems, below).
- **no-en's plans page** takes ie's lines (SH-75's lines 181 to 202; SH-76's lines 2 to 20), for its hero, cards, POS Pro and Agentic cards, rows and FAQ. Its card rates take hk-en's (SH-74's lines 212 and 216; SH-75's lines 4, 8 and 12). Its credits take au's, which also carry the tooltip and no popover (SH-73's lines 47, 52 and 56).
- **no-en's rows 47 to 55:** `earlier`'s pointer twins were other rows: ae's Third-party transaction fees, Built-in fraud analysis, note row, Hosting and Custom domain name, and au's, ca's and hk-en's rows at those places. Its labels found Klarna, MB WAY, Bizum, In-person card and USDC rates. Mobilepay rates had no label line, since no earlier batch held it.
- **no-en's summaries** (61 to 66) take ie's (SH-76's lines 32 to 82), whose `card_rates` also hold online, in-person and third-party rates, but without ie's 12-month incentive. Starter takes hk-en's (SH-75's lines 63 to 69), whose `card_rates` hold no in-person rate. no-en's Balance footnote takes id's and za's (SH-75's line 129).
- **nz's credits** take hk-en's (SH-74's lines 213 and 217; SH-75's line 5), whose popover also says 1%.

**Rules for kinds the earlier rules don't cover,** for the coordinator to align with SH-78 and SH-79:
1. **Mobilepay rates** (51, no-en only) is CM-PAY-017 `core`, with Mobilepay as filler and its rates by plan as quality. This is how its siblings under Accepting payments are placed: Klarna, MB WAY and Bizum rates (SH-73's rule 3; SH-76's rule 1).
   - Held posts name MobilePay among Shopify Payments' local payment methods: 'Now you can activate these local payment methods in Shopify Payments', listing iDeal, Klarna, Swish, Twint and Mobilepay (SH-E-0ecae440, SH-36's line on it). SH-34's line on SH-E-0fd1fcfa places MobilePay, in the 22 countries that post lists, on CM-PAY-017 as filler.
   - The cell's own terms don't name MobilePay yet, so the filler is new to the cell, beside SH-34's and SH-36's.
   - The row writes 'Mobilepay' and SH-34's post 'MobilePay'. The coordinator may align the spelling.
2. **A plans page priced in more than one currency** (no-en): each line quotes the currency its own entry states. The coordinator may want this as a rule for SH-78 and SH-79.
   - Basic, Grow, Advanced, Starter, Retail and POS Pro are priced in kroner (NOK).
   - Plus is priced in euros, on its card (38), in the table's Pay monthly row (43) and in its POS summary (64), whose card rates and POS Pro price stay in kroner.
   - The terms entries state US dollars ($29.00 USD, $5 USD, $1, $89).

   The readings say where the currencies differ. No line converts one into another.

## New things

**`new:Earn 1% back on all sales as subscription credits`** (SH-68's), 7 lines:
- no-en's cards: 31, 34 and 37 (SH-E-06c8fee1, SH-E-0fa8d2d7, SH-E-f95cb295): 'Earn up to kr50,000 in credits', kr75,000 and kr100,000, each with the tooltip 'Earn 1% back on all sales as subscription credits (0.5% on non-Shopify Payments).'. They have no popover and no domain credit.
- no-en's table row: 45 (SH-E-e0b7be4f): 'Up to kr50,000 NOK', 'Up to kr75,000 NOK' and 'Up to kr100,000 NOK', with a dash on Plus. Its tooltip adds 'Valid for your first 6 months or until you reach the max.'.
- nz's cards: 77, 79 and 81 (SH-E-852cf5d2, SH-E-5c7aafa3, SH-E-c8c39102): 'Earn up to $5,000 in credits', $7,500 and $10,000, with 'Get 1% back on sales' and 'Add a domain, get US$20'. These are the maximums of the table row of il, nz and www.shopify.com (SH-E-3787fad6, SH-76's line 124).

SH-68's notes give the rest:
- its place of its own: the table's row Earn 1% back on all sales;
- its proposed domain A, area PLN and parent CM-PLN-004, or CM-PLN-001;
- its Arabic words and the terms searched.

**The leads' cells, read:** none holds the platform's credits to the merchant.
- CM-PTN-008 holds nothing on Shopify. It is a referral programme's commission on the plans a member brings.
- CM-PAY-025 is Shopify Credit, a charge card with a credit limit.
- CM-SFR-008 is domains, a way to earn the nz domain credit.
- CM-CHK-002 is the buyer's cart, a lead by 'add'.
- CM-APP-012 holds nothing on Shopify. It is a marketplace connection, a lead by 'advanced' and 'subscription'.
- CM-PLN-001 and CM-API-001 are leads by the plan names.

## Entries I couldn't tell, and what would settle each

- **51, Mobilepay rates, on CM-PAY-017 (rule 1):** the row names the method only, on www.shopify.com/no-en.
  - SH-E-0fd1fcfa (May 30, 2026) lists MobilePay's countries, and Norway isn't among them; TWINT's and BLIK's lists include Norway.
  - So whether MobilePay is offered to stores in Norway, or the row is the site's list of rates for buyers' methods, isn't stated.
  - A help page on Shopify Payments' local payment methods in Norway would settle it.
- **50, Klarna rates, on CM-PAY-017:** as SH-76's rule 1. A held post names Klarna among Shopify Payments' local payment methods (SH-E-0ecae440). Its role beyond a payment method, buy now, pay later (CM-PAY-015), isn't stated (M-5).
- **The twins' doubts carry over,** as SH-73's to SH-76's notes list them:
  - the iPad stand's `own-service` (9, 23, 70; SH-70's rule 4, kept);
  - 'every paid plan' and 'all plans' read as the four plans (10, 24, 71, 72);
  - the transaction fees on CM-PLN-003 (69);
  - Plus's summary's 'POS Pro included' beside `included_in_plan: false` (64).

## A structure whose items and sources disagree

Each line quotes its own entry. Which price is charged isn't held. That the pages' variants are the cause is an assumption, as SH-68's to SH-76's notes have it.
- **www.shopify.com/my's Basic yearly price:** the terms state 'basicAnnualPrice: <span>$19.00 USD</span>' on all three pages (3, 5, 8). The site's Basic card states US$22 a month paid yearly (SH-E-74c114a7, on id, my, pk and za), and its POS summary states 22 USD (SH-E-bdff9e26).
- **www.shopify.com/ng's prices agree:** the terms' $24.00 USD (11, 13, 20), the Basic card's US$24 (14), the Pay yearly row's $24 USD/mo (17) and the summary's 24 USD (21).
- **www.shopify.com/no-en:**
  - **The terms are in US dollars** on all three pages (25, 27, 60): basicAnnualPrice $29.00 USD, minimum $5 USD, paid trial $1 and posProPriceUsd $89. The plans and POS pages price in kroner: the hero's '9 kr/month' (28), the cards (29 to 37), the POS Pro card's '+920 kr NOK' (40), and the summaries' paid trial of 9.0 NOK and add-on price of 920 NOK (61 to 66).
  - **The yearly prices aren't the summaries' yearly prices.** The cards' and the Pay yearly row's prices (289, 770 and 3 370 kr NOK; 29, 32, 35, 44) are the POS summaries' two- and three-year monthly prices. The summaries' `annual_monthly_price` is 349, 929 and 3999 NOK (61 to 63), their `annual_price` 4188, 11148 and 47988 NOK.
  - **Plus is in euros:** 'from €2,100 EUR' on the card (38) and 'Starts at €2,100 EUR/mo' in the table (43) are the summary's `triennial_monthly_price` 2100 EUR, beside its `monthly_price` 2250 EUR (64).
  - **The plans page's variant:** it was served under 'f_2e2905455a798fa9df40308c0b8b53ee:true,f_77c8150780b85c85656903fc3fada251:true,f_ba4893153541cee32ff1abde10187c02:true', with no `e_` experiment, and signupTypes 'paid_trial_experience' alone (27). Every other plans page of my batch was served with the treatments e_0573c3a44a32b9562a4827c286953987 and e_06d1ad5d27d16046cc6d829de669769b (5, 13, 75).
- **www.shopify.com/nz:** the terms' $29.00 USD (73, 75) stands beside the Basic card's US$35 a month paid yearly (SH-E-54a1b998, on il and nz). The card rates are in New Zealand dollars (76, 78, 80), the card prices in US dollars.
- **www.shopify.com's international terms** state $24.00 USD (1). The site's Basic card, a later batch's entry, states $29 a month paid yearly (SH-E-6e2449a7, items.jsonl line 161).
- **my's and ng's international pages state Shopify Payments' processing rate,** 3.9% per transaction (4, 12), while their plans pages state no card rate. This is SH-74's eg case, SH-75's id case and SH-76's il and in cases again.
- **The items and the entries agree:** the entries are the items' decoded loader data. I didn't print the WARC records.

## What the sources state that no entry holds (for the second stage)

- **The credits popover's pruned tracking data** (`duxTrackingMetadata`, removed by the selection's rule):
  - nz's three cards: 'free_domain_global,gmvRewardsAcquisition.mainline.sp' (items.jsonl line 146), with 'Get 1% back on sales', as on ie's (line 85);
  - no-en's cards: no popover and no `eligibleIncentiveIds` (line 140).

  This adds to SH-76's lead that `sp` and `nonSp` stand for Shopify Payments and non-Shopify Payments, which is an assumption.
- **The held posts on local payment methods** (SH-E-0fd1fcfa, SH-E-fd124edd, SH-E-0ecae440) list MobilePay, Klarna and TWINT with their countries. They are leads for CM-PAY-017's fillers by market, and for Klarna's role (CM-PAY-015 stays a lead).
- **Kept from SH-72's to SH-76's leads:** the POS pages' sales contact flow (`posContactModal`), on my's, ng's and no-en's POS pages too; POS Pro's staff performance tracking and the endless aisle, which have no capability.

## The checker's lines, read again

- **No `CHANGES`.** Every cell my lines touch already holds its support.
- **`NOTE` on a product named with the platform's brand** (lines 5, 9, 29, 69 and 193: entries 2, 4, 12, 26 and 74, the Shopify Payments processing rows): each is `core` by the cell's Shopify Payments rows, not by its name, as SH-76's line 109.
- **`NOTE` own-service on CM-POS-002** (9, 23, 70): SH-70's rule 4, kept by the coordinator. “Shopify's flexible iPad stand” names Shopify as the stand's provider, as the cell's `own-service` holds (SH-S-7269).
- **`NOTE` on a new thing whose entry has leads** (lines 77, 81, 85, 97, 198, 200, 202): the leads' cells are read above. None is the entry's thing.
- **`NOTE` on line 97, whose first lead CM-PTN-008 holds nothing:** it is a referral programme's commission on the plans a member brings, not credits on the merchant's own sales (SH-71's notes).
- **`NEW`:** Earn 1% back on all sales as subscription credits, 7 lines.

## Problems with the brief or the script

- **`earlier` prints at most six twins an entry,** as SH-76 found. For ng's summaries (21, 22), il's and id's twins, whose `card_rates` hold the third-party fee alone, weren't among the six. I found them in SH-76's list by script.
- **`class_slice.py search` reads only the concern map,** so a search there doesn't find the held pass's own entries. SH-76's notes say no held Shopify statement names Klarna or TWINT. Two held changelog posts do, as payment methods through Shopify Payments: SH-E-fd124edd ('Klarna, Bancontact, iDEAL, BLIK, Przelewy24, TWINT, EPS, and MobilePay are available to merchants using Shopify Payments in France.') and SH-E-0ecae440, both placed in SH-36. They support SH-76's CM-PAY-017 lines for Klarna and TWINT (its lines 11 and 14) as they support mine. A grep over the held placements finds them.
- **Quotes:** a quote with a straight apostrophe is written with “ ” (SH-73 to SH-76). A quote from another entry of my batch names that entry's id (32, 35: SH-E-dede197f).
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief states itself (qualities wider than B-extent's list; the rulings).

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 81 of 81 entries, no problem and no `CHANGES`.
- **Rules 1 and 2 stand, for SH-78 and SH-79.** Mobilepay's rate row is CM-PAY-017 `core` with its filler, beside its siblings, as SH-34's line has MobilePay. A page priced in several currencies quotes each entry's own.
- **SH-76's lines are supported.** The two held posts this batch found, naming Klarna and TWINT among the local payment methods through Shopify Payments, are now cited in SH-76's lines, and its notes are corrected. SH-78's prompt asks for the held entries to be searched as well as the concern map.
- **The twins.** `earlier`'s six-twin cap left out il's summaries, the ones ng's match; the agent found them in SH-76's list. A seventh twin is needed where a site's pages repeat another's only in part.
- **The price disagreements** are quoted each in its own line.
- **Cost:** 25.0 million tokens over 104 requests, about 309,000 an entry. The context reached about 408,000 tokens, not the 200,000 the agent estimated.
