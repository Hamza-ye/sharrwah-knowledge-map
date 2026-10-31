# Held pass, Shopify, batch SH-76: notes

82 entries of `pricing-page-data` (effort high), evidence at observed-sh@e38dc17e3, in `structures/shopify/pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl`. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-76`).
- **1 to 19:** the rest of www.shopify.com/ie's plans page (items.jsonl line 85):
  - 15 comparison rows whose words are ie's alone (1 to 15, of the table's 97): Pay monthly, Pay yearly, Earn 1% back, POS Pro, the three online card rates, Klarna, Bancontact, iDEAL, TWINT, MB WAY, Bizum, In-person card and USDC rates;
  - one FAQ (16), the disclaimer (17) and the Credit and Capital footnotes (18, 19).
- **20 to 32:** ie's POS page (line 86): its terms entry, the six plan summaries, the two POS Pro plan entries, the four FAQs.
- **33, 34:** www.shopify.com/il's international page (line 90): its terms entry and its processing row.
- **35 to 45:** il's plans page (line 91), with nz's and www.shopify.com's where the words are the same: its terms entry, the Basic and Grow cards (il, nz), the three cards' credits (il), the Pay monthly, Pay yearly and Earn 1% back rows, the disclaimer and the Credit footnote.
- **46 to 50:** il's POS page (line 92): its terms entry, the Basic and Grow summaries, two FAQs.
- **51, 52:** www.shopify.com/in's international page (line 111): its terms entry and its processing row.
- **53 to 69:** in's plans page (line 112): its terms entry, the hero, the four cards with their credits, the POS Pro card, the Pay monthly, Pay yearly, Earn 1% back and POS Pro rows, one FAQ, the disclaimer and the Credit footnote.
- **70 to 82:** in's POS page (line 113): its terms entry, the six plan summaries, the two POS Pro plan entries, the four FAQs.

**Placed:** 82 entries in 244 lines: 73 entries on capabilities, 9 `new` (SH-68's new thing), none `out`; 49 entries take more than one line. Supports, by line: 208 `core`, 17 `shows`, 16 `outside`, 3 `own-service`; no `extension-point`. 22 lines carry fillers; 169 carry qualities. The checker raises no `CHANGES`.

**Sources read:**
- the brief and what it names: the evidence map; the rulings, the last section most; B-extent.md's "Cells and evidence" and "Conventions from the dry run", with "What a place of its own is"; observed-sh's `README.md`, `docs/READING.md` (fetch runs, structures, indexes), `docs/GAPS.md` (nothing on these pages), `structures/README.md`; `structures/REGISTER.tsv`'s row for this structure; `index/ledger-summary.tsv`; `selection.tsv`'s row; `show --meta`;
- SH-68's notes whole (R0 to R11), SH-69's to SH-75's rules and coordinator's checks, SH-75's notes whole; the twins' lines by number (`earlier`, then `sed` on SH-74's and SH-75's placements);
- items.jsonl, by script: line 85's comparison table (its 97 headings in order, its sections, and its disclaimer list's order: Balance, Cashback, Capital); lines 91 and 112's tables (76 rows each, no Accepting payments section) and disclaimer lists; lines 84 to 86, 90 to 92 and 111 to 113 for `minimumMonthlyPriceCurrency` (empty on ie's three pages, `USD` on il's, `INR` on in's); every read site's plans page for which tables hold the rows Klarna rates, TWINT rates, USDC rates and In-person card rates (below); lines 85, 91 and 112 for the credits popover's pruned `eligibleIncentiveIds`. Every line's terms and quotes are its own entry's, or a twin entry's that its reading names;
- the model: `cells` for CM-PAY-015, CM-PAY-017, CM-PAY-007, CM-PAY-018, CM-PAY-021, CM-PAY-026 and the new thing's leads (CM-PTN-008, CM-PAY-025, CM-SFR-008, CM-CHK-002); `caps --terms` and `search` for Klarna, TWINT, pay later, buy now; `merged/evidence.tsv`, by grep, for Klarna, TWINT and YouLend; `merged/capabilities.tsv` for CM-PAY-017's place.

## Rules followed

**SH-68's R0 to R11, SH-69's rules 1 to 7, SH-70's rules 1 to 9, SH-71's rules 1 to 3, SH-73's rules 1 to 8, SH-74's rules 1 to 5, SH-75's rules 1 to 7, and the rulings since, as kept.**
- **R0:** no entry of mine is on every read site of its language, so every line takes its labels, after its plans. The widest are on three English sites (41 and 43: il, nz and www.shopify.com); 36, 38 and 42 are on il and nz; every other entry is one site's.
- **R1:** the seven terms entries (20, 33, 35, 46, 51, 53, 70), three `core` lines each. `googleCountryOffer` gives no line.
- **R2:** the cards, their credits and the POS Pro card (62) on its site alone (the ruling after SH-70). The il and in cards' `card_rates_short` (the third-party fee) are SH-75's lines 108, 112, 114 and 118, whose sites include il and in.
- **R3:** the rows, each on its twin's capability, matched by its heading (below).
- **R4, R6, R7, R9:** the POS summaries, lists and FAQs; the qualities; the disclaimers' providers (`outside`, with fillers), WebBank's U.S. joined to the site with ` and ` (the ruling after SA-53).
- **SH-73's rules 1 and 2:** ie's six summaries state `card_rates.in_person`, so they take CM-PAY-021 lines (21 to 26); Basic, Grow and Advanced carry the 12-month incentive (21 to 23), each a second CM-POS-001 line scoped `<plan>;www.shopify.com/ie and retail_term_commitment_12_months`. il's and in's summaries hold neither.
- **SH-73's rule 3:** Bancontact, iDEAL, MB WAY and Bizum rates on CM-PAY-017, the method as filler (9, 10, 12, 13). **SH-73's rule 7:** ie's Capital footnote names its issuer for Ireland (19).
- **SH-74's rule 5 and SH-75's rule 3:** il's and in's summaries hold `card_rates` with `third_party` alone (47, 48, 71 to 76) and take no CM-PAY-007 line.
- **SH-75's rule 1:** ie's USDC rates on CM-PAY-018, no filler (15). **Rule 5:** numbers quoted as written (61, below). **Rule 6:** ie's rates stated 'excl. VAT' keep it in their qualities (5 to 15, and the summaries' rates). **Rule 7:** the popover's rate by site: 0.5% on il and in (37, 39, 40, 56, 58, 60).
- **Twins, by meaning:**
  - **ie's rows:** `earlier`'s pointer twins for 8 to 15 were other rows (ae's Third-party transaction fees, Built-in fraud analysis, note row, Hosting, Unlimited web hosting, Custom domain name, Free SSL certificate and Marketing, and au's, ca's and hk-en's rows at those places). Its labels found the right ones for Bancontact, iDEAL, MB WAY, Bizum, In-person card and USDC rates. Klarna and TWINT rates had no label line, since no earlier batch held them.
  - **ie's summaries (21 to 26)** take www.shopify.com/ca's lines (SH-74's 37 to 87), whose `card_rates` also hold online, in-person and third-party rates, with the 12-month incentive on the same three plans.
  - **il's and in's summaries (47, 48, 71 to 76)** take www.shopify.com/id's lines (SH-75's 134 to 169), whose `card_rates` hold only the third-party fee. `earlier` didn't print id's summaries among their twins (below).
  - **The cards, rows, FAQs and disclaimers** take hk-en's, id's or ie's lines (SH-75), and ca's (SH-74) where no SH-75 line holds the kind: Bizum rates, the POS lists and FAQs.

**Rules for kinds the earlier rules don't cover,** for the coordinator to align with SH-77 to SH-79:
1. **A payment method's rate row that no held Shopify statement explains** (Klarna rates, 8; TWINT rates, 11) is CM-PAY-017 `core`, the method as filler, as its siblings under Accepting payments (SH-73's rule 3). Its rates by plan are its quality.
   - The row names the method only, with no tooltip, between the online card rates and the in-person rates. Klarna's row comes before Bancontact's; TWINT's sits between iDEAL's and MB WAY's.
   - No held Shopify statement names Klarna or TWINT: `class_slice.py search --platform shopify --terms "Klarna; TWINT"` finds none, and no Shopify cell's evidence names either.
   - CM-PAY-015 (instalments and buy now, pay later) is the other reading for Klarna. Its Salla, WooCommerce and BigCommerce cells name Klarna, but a provider's role known only from another platform's cell is a lead, not evidence (M-5). Shopify's CM-PAY-015 cell holds Shop Pay Installments with Affirm, and no Klarna.
   - Either line changes no cell: CM-PAY-017 is `core` already. The fillers are new to the cell.
   - Among the read sites, Klarna rates stand on ie, no-en and uk (items.jsonl lines 85, 140, 197), and TWINT rates on ie and uk (lines 85, 197). SH-77 to SH-79 hold no-en's and uk's.
2. **A POS Pro row whose Plus cell names no Shopify Payments condition** ('Includes 20 locations.', on in, 66) takes the row's line as written, with no condition. The sites whose tables hold Shopify Payments rows add 'Up to 200 with Shopify Payments.' (4). in's table holds no Accepting payments section, and its cards and summaries state only the third-party fee.
3. **A number grouped by the site's own convention is quoted as written** (61): in's Plus card writes '₹1,75,000' where its table writes 'Starts at ₹175,000 INR/mo' (63). This extends SH-75's rule 5, on a decimal comma or a thousands point, to the Indian grouping.

## New things

**`new:Earn 1% back on all sales as subscription credits`** (SH-68's), 9 lines:
- ie's table row: 3 (SH-E-7e17a4a4), 'Up to €4,000 EUR', 'Up to €6,000 EUR' and 'Up to €8,000 EUR', a dash on Plus, the maximums of ie's cards (SH-75's lines 188, 191 and 194);
- il's cards: 37, 39 and 40 (SH-E-64ac8b3d, SH-E-616473e4, SH-E-7f85b50b), 'Earn up to $5,000 in credits', $7,500 and $10,000, with 'Get 0.5% back on sales' and 'Add a domain, get US$20';
- the table row of il, nz and www.shopify.com: 43 (SH-E-3787fad6), 'Up to $5,000 USD', 'Up to $7,500 USD' and 'Up to $10,000 USD', a dash on Plus;
- in's cards: 56, 58 and 60 (SH-E-c09f3685, SH-E-506dbd3c, SH-E-65b9718f), 'Earn up to ₹110,000 in credits', ₹170,000 and ₹230,000, with 'Get 0.5% back on sales' and 'Add a domain, get ₹2,000';
- in's table row: 65 (SH-E-1a41d8e4), 'Up to ₹110,000 INR', 'Up to ₹170,000 INR' and 'Up to ₹230,000 INR', a dash on Plus.

Each row's tooltip is 'Earn 1% back on all sales as subscription credits (0.5% on non-Shopify Payments). Valid for your first 6 months or until you reach the max.' Its place of its own (the table's row Earn 1% back on all sales), proposed domain A, area PLN, parent CM-PLN-004 (or CM-PLN-001), its Arabic words and the terms searched are in SH-68's notes.

**The leads' cells, read:** none holds the platform's credits to the merchant.
- CM-PTN-008 (holds nothing on Shopify): a referral programme's commission on the plans a member brings.
- CM-PAY-025: Shopify Credit, a charge card with a credit limit.
- CM-SFR-008: domains, a way to earn the domain credit.
- CM-CHK-002: the buyer's cart, by 'add'.
- CM-PLN-001 and CM-API-001: by the plan names.

## Entries I couldn't tell, and what would settle each

- **8, Klarna rates, on CM-PAY-017 (rule 1):** what Klarna is on Shopify isn't held. A help page on the payment methods Shopify Payments offers in Ireland or the UK would settle whether it is a local payment method (CM-PAY-017) or buy now, pay later (CM-PAY-015), and whether Klarna fills the slot as the method's provider or only as its name.
- **11, TWINT rates, on CM-PAY-017 (rule 1):** the same page would say which market TWINT serves. The row names none, so the line takes the site alone.
- **The twins' doubts carry over,** as SH-73's to SH-75's notes list them:
  - the iPad stand's `own-service` (30, 49, 80; SH-70's rule 4, kept);
  - 'every paid plan' and 'all plans' as the four plans (31, 32, 50, 81, 82);
  - the transaction fees on CM-PLN-003 (29, 79);
  - the Plus summaries' 'POS Pro included' with `included_in_plan: false` (24, 74).

## A structure whose items and sources disagree

Each line quotes its own entry. Which price is charged isn't held. That the pages' different variants are the cause is an assumption, as SH-68's to SH-75's notes have it.
- **www.shopify.com/ie's Basic yearly price:** the table's Pay yearly €29 EUR/mo (2), the card's €29 (SH-75's line 182) and the POS summary's `annual_monthly_price` 29 EUR (21) stand beside the terms' 'basicAnnualPrice: <span>€24.00</span>' on its three pages (20; SH-75's lines 174, 178).
- **ie's Plus price:** the table's 'Starts at €2,100 EUR/mo' (1) and the card's 'from' €2,100 are the summary's `triennial_monthly_price` 2100; its `monthly_price` is 2250 EUR (24).
- **ie's POS Pro price:** the lists' '+ €79 EUR/month/location' (27, 28) and the summaries' `add_on_price` 79 EUR against the terms' 'posProPriceUsd: $89' (20), a price the key names in US dollars.
- **ie's terms leave `minimumMonthlyPriceCurrency` empty** on all three pages (items.jsonl lines 84 to 86), as SH-75's notes found for its other two: the minimum price's currency is only its sign, '€5'.
- **www.shopify.com/il's Basic yearly price:** the card's US$35 (36), the Pay yearly row's $35 USD/mo (42) and the summary's 35 USD (47) stand beside the terms' 'basicAnnualPrice: <span>$29.00 USD</span>' on its three pages (33, 35, 46).
- **www.shopify.com/in's Basic yearly price:** the card's ₹1,800 (55), the row's ₹1,800 INR/mo (64) and the summary's 1800 INR (71) stand beside the terms' 'basicAnnualPrice: <span>₹1,499.00</span>' on its three pages (51, 53, 70).
- **in's Plus price:** the card's 'from' ₹1,75,000 (61) and the table's 'Starts at ₹175,000 INR/mo' (63) are the summary's `triennial_monthly_price` 175000; its `monthly_price` is 190000 INR (74). The card and the table group the same number differently (rule 3).
- **in's POS Pro price:** '+₹7,000' (62) and '+ ₹7,000 INR/month/location' (77, 78) against the terms' 'posProPriceUsd: $89' (51, 53, 70).
- **il's and in's international pages state Shopify Payments' processing rate,** 3.9% per transaction (34, 52), while their plans pages state no card rate. Their cards and POS summaries give only the third-party fee, and their tables have no Accepting payments section (items.jsonl lines 91, 112). This is SH-74's eg case and SH-75's id case again. Whether Shopify Payments is offered in Israel or India isn't stated in these entries.
- **The items and the entries agree:** the entries are the items' decoded loader data. I didn't print the WARC records.

## What the sources state that no entry holds (for the second stage)

- **The credits popover's pruned tracking data** (`duxTrackingMetadata`, removed by the selection's rule):
  - ie's cards: 'eligibleIncentiveIds': 'free_domain_global,gmvRewardsAcquisition.mainline.sp' (items.jsonl line 85), with 'Get 1% back on sales';
  - il's and in's cards: 'free_domain_global,gmvRewardsAcquisition.mainline.nonSp' (lines 91, 112), with 'Get 0.5% back on sales'.

  That `sp` and `nonSp` stand for Shopify Payments and non-Shopify Payments, matching the tooltip's '(0.5% on non-Shopify Payments)', is an assumption. If it holds, the popover's rate follows whether the site's stores use Shopify Payments: a lead for the new thing's terms and for SH-75's rule 7.
- **A help page on Klarna and TWINT in Shopify Payments** would settle rule 1 (above). None is in this structure.
- **Kept from SH-72's to SH-75's leads:** the POS pages' sales contact flow (`posContactModal`), on ie's, il's and in's POS pages too; POS Pro's staff performance tracking and the endless aisle, which have no capability.

## The checker's lines, read again

- **No `CHANGES`.** Every cell my lines touch already holds its support. CM-PAY-017 was `core` from the 30 September rows MB WAY and Bizum rates (SH-S-7025, SH-S-7026). CM-PAY-026's `outside` for Ireland repeats the cell's own SH-S-0494, 'Ireland: merchant cash advances issued by YouLend'.
- **`NOTE` own-service on CM-POS-002 (30, 49, 80):** SH-70's rule 4, kept by the coordinator. “Shopify's flexible iPad stand” names Shopify as the stand's provider, as the cell's own-service (SH-S-7269).
- **`NOTE` on a product named with the platform's brand (lines 109 and 153: 34 and 52, Shopify Payments processing):** each is `core` by the cell's Shopify Payments route and plan rows, not by its name, as SH-75's line 102.
- **`NOTE` on a new thing whose entry has leads (lines 6, 115, 118, 119, 124, 160, 163, 166, 174):** the leads' cells are read above. None is the entry's thing.
- **`NOTE` on lines 6, 124 and 174: their first lead CM-PTN-008 holds nothing.** It is a referral programme's commission on the plans a member brings, not credits on the merchant's own sales (SH-71's notes).
- **`NEW`:** Earn 1% back on all sales as subscription credits, 9 lines.

## Problems with the brief or the script

- **`earlier` prints at most six twins an entry.** For il's and in's summaries (47, 48, 71 to 76) it printed ae-ar's, ae's, au's, ca's, eg's and hk-en's lines, but not id's (SH-75's lines 134 to 169). Those are the only English twins whose `card_rates` hold the third-party fee alone. I found them by grep. Printing the twins that share the entry's `card_rates` keys first would serve SH-77 to SH-79.
- **`earlier`'s pointer twins still mislead where a site's table holds rows others lack** (8 to 15). Its labels found the rows earlier batches held. Klarna and TWINT rates had no label line.
- **A quote with a straight apostrophe** (“Shopify's flexible iPad stand…”) is quoted with “ ”, as SH-73 to SH-75 did.
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief states (qualities wider than B-extent's list; the rulings).

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 82 of 82 entries, no problem and no `CHANGES`.
- **Rules 1 to 3 stand, for SH-77 to SH-79.**
  - Klarna's and TWINT's rate rows are CM-PAY-017 `core`, each method its filler, beside their siblings under Accepting payments (SH-73's rule 3). No held Shopify statement names Klarna as a way to pay later, so CM-PAY-015 stays a lead (M-5), not a line.
  - in's POS Pro row and its digit grouping ('₹1,75,000') are placed and quoted as written.
- **Two fillers new to their cell:** Klarna and TWINT, on CM-PAY-017.
- **The twins.** `earlier` prints at most six twins an entry, and il's and in's summaries matched id's beyond them. The twins now carry their words and card rates, so the agent found the right ones, and a seventh twin is rarely the needed one.
- **The price disagreements** are quoted each in its own line.
- **Cost:** 16.7 million tokens over 74 requests, about 204,000 an entry. The context reached about 425,000 tokens.
