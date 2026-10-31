# Held pass, Shopify, batch SH-73: notes

80 entries of `pricing-page-data` (effort high), evidence at observed-sh@e38dc17e3, in `structures/shopify/pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl`. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-73`).
- **1 to 11:** the rest of www.shopify.com/ae's POS page (items.jsonl line 6): 'How to get started' and its three blocks (1 to 4), the two promo cards (5, 6), the five FAQs (7 to 11). Most are stated in the same words on all 18 English sites; 7 and 9 on ae, ph and www.shopify.com, 8 and 10 on ae alone.
- **12, 13:** www.shopify.com/au's international pricing page (line 9): its terms entry and its Shopify Payments processing row. The page's other entries are in other sites' words.
- **14 to 50:** www.shopify.com/au's plans page (line 10): its terms entry, the four cards with the features whose words are au's (or shared with a few sites), the always-included block of the six sites whose fourth card is in-person sales (28), the POS Pro card, the Agentic card's rate, 17 comparison rows (31 to 47) and the disclaimer with two footnotes (48 to 50).
- **51 to 63:** www.shopify.com/au's POS page (line 11): its terms entry, the six plan summaries, the two POS Pro lists' plan entries, the four FAQs whose words are au's.
- **64, 65:** www.shopify.com/ca's international page (line 26): its terms entry and its processing row.
- **66 to 80:** www.shopify.com/ca's plans page (line 27): its terms entry, the cards with their site-specific features, the POS Pro card and the Agentic card's rate. SH-74 begins with the ca page's comparison table.

**Placed:** 80 entries in 198 lines: 72 entries on capabilities, 7 `new` (SH-68's new thing), 1 `out` (the heading 'How to get started'); 38 entries take more than one line. Supports, by line: 163 `core` (one of them `core;extension-point`), 26 `shows`, 6 `outside`, 2 `own-service`. 12 lines carry fillers; 129 carry qualities.

**Sources read:**
- the brief and what it names: the evidence map; the rulings, the last section most; B-extent.md's "Cells and evidence" and "Conventions from the dry run"; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md` (nothing on these pages), `structures/README.md`; `structures/REGISTER.tsv`'s row; `selection.tsv`'s row; `show --meta`;
- SH-68's to SH-72's notes, with their coordinator's checks, first, and their placements for each twin;
- items.jsonl lines 5, 6, 10, 11 and 27, by script, for the cards' features (by `name`), the comparison tables' headings (ae against au), and the POS summaries' `card_rates` and `incentives` on every read site's POS page (line 3, 6, 11, 28, 44, 68, 83, 86, 92, 113, 134, 137, 141, 147, 151, 157, 162, 172, 177, 198, 204). Every line's terms and quotes are its own entry's;
- the model: `earlier`; `cells` for every capability placed on and the leads; `land_points.py cell` for CM-PAY-017, CM-SHP-002 and CM-PAY-026; `caps --terms` for Bancontact, iDEAL, MB WAY, Bizum, in-person card rates, shipping discounts, shipping labels, calculated shipping rates; `merged/evidence.tsv`, by grep, for which cells cite the 30 September rows MB WAY rates, Bizum rates, In-person card rates, Shipping discounts, Buy and print shipping labels and 3rd-party calculated shipping rates (SH-S-7025 to SH-S-7027, SH-S-7045, SH-S-7046, SH-S-7048); `class_slice.py key` for SH-S-7024, SH-S-7044, SH-S-7045, SH-S-7047.

## Rules followed

**SH-68's R0 to R11, SH-69's rules 1 to 7, SH-70's rules 1 to 9, SH-71's rules 1 to 3, and the rulings after SH-69, SH-70 and SA-53, as kept.**
- **R0:** entries 1 to 6 and 11 are on all 18 English sites and take no site. Every other line takes its labels, after its plans.
- **R1:** the five terms entries (12, 14, 51, 64, 66), three `core` lines each. `googleCountryOffer` gives no line.
- **R2:** the cards, their features, the always-included block, the POS Pro and Agentic cards.
- **R3:** the rows, with the Shipping section (below).
- **R4:** the POS page's blocks, cards, summaries and lists.
- **R6:** the FAQs.
- **R7:** the qualities.
- **R9:** the disclaimer's providers, `outside` with fillers.

**Each entry takes its twin's line, matched by meaning, not by pointer.** `earlier` prints twins at the same pointer. That holds on the POS and international pages, whose shape is the same on every site. It fails on the plans pages, where au's and ca's cards and table differ from ae's:
- **Card features:** au's and ca's Basic card has no inventory locations or support line, so its credits stand at `planFeatures/4`, where ae's inventory locations stand. 17's pointer twin is SH-70's CM-INV-005 line, 20's (Grow's shipping discount) the credits, 24's (Advanced's credits) Tailor your store by region. I matched each feature by its card's `planType` and its `name`, as SH-68's R0 measured twins.
- **Comparison rows:** au's table holds 94 rows, ae's 84. au adds Bancontact, iDEAL, MB WAY, Bizum and In-person card rates after row 32, and a Shipping section of four rows after row 55. From row 33 on, au's pointer twin is another row: 38's is Third-party transaction fees, 43's Integrate with 1000s of apps. I matched each row by its heading.
- The terms entries' pointer twins are right: every page's terms are at the same pointer.

**Rules for kinds the earlier rules don't cover,** for the coordinator to align with SH-74 to SH-79:
1. **A plan summary's `card_rates.in_person`, where it isn't null,** is CM-PAY-021 `core`, its rate as quality. This follows R4's `local_payment_methods` "where it isn't null". au's six summaries state it ('1.85% + 0¢ AUD in person' on Basic). Eight read sites' POS pages state it: au, ca, ie, no-en, nz, www.shopify.com, sg and uk. Thirteen hold `in_person: null`: ae-ar, ae, eg, hk-en, id, il, in, my, ng, ph, pk, sa and za. So SH-69's and SH-72's twins rightly have no such line.
2. **A plan summary's `incentives.retail_term_commitment_12_months`** takes a second CM-POS-001 `core` line (52, 53, 54). Its scope is the summary's own, joined with ` and ` to the condition in the source's identifier: `Basic;www.shopify.com/au and retail_term_commitment_12_months`. Its price, '97.0 AUD', and its 'overall_savings' (3500.0 AUD) are qualities. Its disclaimer goes in reading: 'Get free hardware and more with 1 year of POS Pro — offer worth $3,500.'
   - 'free hardware and more' ends in 'and more', so it names examples, which take no line (SH-69's rule 5).
   - Basic, Grow and Advanced carry it on au, ca, ie, nz, www.shopify.com, sg and uk. Plus, Starter and Retail don't, and neither does any summary of the other read sites.
   - Other readings: CM-POS-002 `core` for the free hardware, as SH-69's line 136 has the plans' 'access to … POS hardware'; and CM-PLN-002 for the 12-month term. Neither would change a cell.
3. **A local payment method's rate row** (Bancontact, iDEAL, MB WAY and Bizum rates, 38 to 41) is CM-PAY-017 `core`. The method is its filler and the rates by plan are qualities. This follows the cell's own placement of the 30 September rows MB WAY rates and Bizum rates (SH-S-7025, SH-S-7026), each with its method as slot filler, as SH-36's France post did for Bancontact and iDEAL. The row names the method only; none of the four is cited on CM-PAY-007.
4. **In-person card rates** (42) is CM-PAY-021 `core`, as the cell's SH-S-7027. It sits under Accepting payments, whose CM-PAY-001 is CM-PAY-021's parent, so it takes no section line (R3).
5. **The Shipping section** (43 to 46, on au, ca and www.shopify.com):
   - The heading names the store's shipping: CM-SHP-001 `shows`, the parent of its rows' capabilities.
   - Shipping discounts is CM-SHP-002 `core` (SH-S-7045). Its tooltip's carriers, 'USPS, UPS, FedEx, and DHL', are its fillers, and they take a CM-SHP-015 `shows` line too, as SH-51's rule E15 has.
   - Buy and print shipping labels is CM-SHP-002 `core` (SH-S-7046). Its tooltip's 'up to 250 shipping labels at once' is a quality.
   - 3rd-party calculated shipping rates is CM-SHP-004 `core;extension-point`: the plan line (SH-S-7048), and its tooltip's 'third-party apps' showing the rates at checkout. Grow's 'Add on' is in reading, and Grow in scope, since a plan's mark gives the scope (R7). The tooltip's 'your own account', the merchant's own carrier account, is CM-SHP-015 `core`, as SH-51's rule E15 has a carrier under the merchant's own account.
   - www.shopify.com/ae's table has no Shipping section, so no earlier line holds these rows.
6. **The card features `shipment_short` and `pos_pro_locations`,** which ae's cards don't carry, follow R11's leads:
   - `shipment_short` is CM-SHP-002 `core` on Grow (20, 72);
   - `pos_pro_locations` is CM-POS-001 `core` on Plus (27), 'Up to 200' as quality.

   Each has a value, so it takes its own card's plan only (R2).
7. **A footnote that names a lender for one country** takes an `outside` line beside its `shows` one. Entry 50 states 'All loans in Australia through Shopify Capital are issued by Westpac.', so CM-PAY-026 takes `outside` with the filler Westpac. Its scope is `www.shopify.com/au and Australia`, as SH-72's line 21 writes WebBank's U.S. The cell holds no Westpac.
8. **An FAQ's POS Pro, with its price, is the offer itself,** so its sites alone are its scope (9 and 62; the ruling after SH-70). The features the Pro subscription adds take 'POS Pro'. SH-70's line 46, the ae-ar twin, written before the ruling, still writes `POS Pro;www.shopify.com/ae-ar`: the coordinator may align it.

## New things

**`new:Earn 1% back on all sales as subscription credits`** (SH-68's), 7 lines:
- the au cards' credits: 17, 21 and 24 (SH-E-8a4a7a99, SH-E-bc05f80d, SH-E-e7494cd0);
- the au table's row: 33 (SH-E-4fe607d5);
- the ca cards' credits: 69, 73 and 76 (SH-E-e641306d, SH-E-83821423, SH-E-f3456211).

What the entries add:
- **English words, au:** 'Earn up to $7,000 in credits', 'Earn up to $11,000 in credits' and 'Earn up to $15,000 in credits'. The cards' tooltip is the table's: 'Earn 1% back on all sales as subscription credits (0.5% on non-Shopify Payments).' The au cards have no `creditsPopover` and no domain credit.
- **English words, ca:** $6,000, $9,500 and $13,000. Their popover reads 'Get 1% back on sales' (ae's: 0.5%) and 'Add a domain, get $30'.
- **The au table's maximums:** 'Up to $7,000 AUD', 'Up to $11,000 AUD' and 'Up to $15,000 AUD', with a dash on Plus.
- Its place of its own (the table's row Earn 1% back on all sales), the proposed domain A, area PLN and parent CM-PLN-004 (or CM-PLN-001), its Arabic words and the terms searched are in SH-68's notes.

**The leads' cells, read:** none holds the platform's credits to the merchant.
- CM-PLN-001 and CM-API-001: by the plan names.
- CM-PTN-008 (holds nothing on Shopify): a referral programme's commission on plans a member brings.
- CM-PAY-025: Shopify Credit, a charge card.
- CM-APP-012: a marketplace connection, by 'advanced' and 'subscription'.
- CM-SFR-008: domains, a way to earn the ca credit.
- CM-CHK-002: the buyer's cart, by 'add'.

## Entries I couldn't tell, and what would settle each

- **The twins' doubts carry over.** SH-68's to SH-72's notes give what would settle each:
  - 1, the heading, `out`;
  - 3's CM-ONB-004 `shows` (a CHANGES line, below);
  - 4's CM-POS-004 beside CM-APP-001;
  - 6's figure as a quality;
  - 7's and 60's transaction fees on CM-PLN-003;
  - 8's and 61's CM-POS-002 `own-service` (SH-70's rule 4, kept by the coordinator: “Shopify's flexible iPad stand”);
  - 9's, 62's, 10's and 63's 'every paid plan' and 'all plans' as the four plans;
  - 34's and 27's Plus counts;
  - 53's and 54's loyalty and analytics.
- **46's `extension-point`:** the tooltip names 'third-party apps' with no interface. `core` alone is the other reading. The cell is `core;extension-point` either way.
- **46's CM-SHP-015 line:** 'your own account' read as the merchant's own carrier account. The row's name, 3rd-party calculated, makes the third party the carrier or an app. A help page on calculated rates would settle it.
- **38 to 41 as local payment methods:** the rows name Bancontact, iDEAL, MB WAY and Bizum only, not as local methods. They stand on an Australian site, though all four are European schemes, which is a reading of no held statement. The placement rests on the cell's placement of the 30 September MB WAY and Bizum rows. CM-PAY-007 (the service's processing fees) is the other reading; it wouldn't change a cell.
- **52 to 54's incentive** (rule 2 above). What 'free hardware and more' holds isn't stated; the page's own disclaimer or offer terms would settle it.
- **28's devices** ('your phone, a card reader, or the sales counter'): read as a list of what may be used, with no line (the ruling after SA-41). SH-68 gave the table's row 'Accept payments with a phone or card reader' a CM-POS-002 line because the row's own title names the devices.

## A structure whose items and sources disagree

Each line quotes its own entry. Which price is charged isn't held, and that the pages' different variants are the cause is an assumption, as SH-68's to SH-72's notes have it.
- **www.shopify.com/au's two pages state different yearly prices.**
  - The plans page's cards and Pay yearly row give $42, $114 and $431 a month paid yearly (15, 18, 22, 32). Its terms give 'basicAnnualPrice: <span>$42.00</span>' with a 25 per cent discount (14).
  - The POS page's summaries give `annual_monthly_price` 50, 134 and 519 AUD (`annual_price` 600, 1608, 6228), beside the same page's terms' $42.00 (51, 52 to 54).
  - The plans page was served under 'f_2e2905455a798fa9df40308c0b8b53ee:true,f_77c8150780b85c85656903fc3fada251:true,f_ba4893153541cee32ff1abde10187c02:true', the POS page under 'e_06d1ad5d27d16046cc6d829de669769b:treatment,f_2e2905455a798fa9df40308c0b8b53ee:true,f_77c8150780b85c85656903fc3fada251:true'.
  - This is SH-72's ae disagreement the other way round: there the POS page's yearly prices were the lower ones.
- **au's Plus price:** the card says 'from' $3,700 and the table 'Starts at $3,700 AUD/mo' (25, 31). The POS summary gives `monthly_price` 4000 AUD, with 3700 as its `triennial_monthly_price` (55).
- **au's Grow shipping discount:** the card and the table give 'Up to 44.2% off' (20, 44). The POS summary's description gives 'up to 87% shipping discount' (53), the words of every site's summary.
- **www.shopify.com/ca's terms** give 'basicAnnualPrice: <span>$38.00</span>' with a 25 per cent discount (64, 66). The ca Basic card gives $44 a month paid yearly against $49 monthly (67).
- **Plus's POS Pro add-on** (55) is titled 'POS Pro included' with `included_in_plan: false`, while Retail's (57) has `true`: SH-69's and SH-72's disagreement again.
- **The items and the entries agree:** the entries are the items' decoded loader data. I didn't print the WARC records.

## What the sources state that no entry holds (for the second stage)

- **The au and ca POS summaries' `upsell_title` and `upsell_mobile_title`** ('Regularly sell in-person? Try [[POS Pro]] free for 3 months ($129/mo after)'). They are in the entries, and are UI strings over the add-on's free three months, which the lines hold.
- **Kept from SH-72's leads:**
  - the POS page's sales contact flow (`posContactModal`), on every POS page, au's (line 11) among them;
  - POS Pro's staff performance tracking and the endless aisle, which have no capability.
- **The incentive's offer** ('offer worth $3,500', 'free hardware and more'): its own terms aren't held in this structure. A lead for CM-POS-002 and CM-POS-001.

## The checker's lines, read again

- **`CHANGES CM-ONB-004@shopify holds nothing: becomes held`, by line 5** (3, SH-E-f27fdc5f, 'Set up your store'): kept. It is the English twin of SH-70's line 29, which the coordinator's check after SH-70 kept under SH-68's R4. The line is `shows`, so the cell becomes held with no placement. The cell still holds nothing because the amendment hasn't run.
- **`NOTE own-service on CM-POS-002`** (8 and 61): SH-70's rule 4, kept by the coordinator. “Shopify's flexible iPad stand” names Shopify as the stand's provider, as the cell's own-service (SH-S-7269).
- **`NOTE` on a product named with the platform's brand** (lines 40 and 178: 13 and 65, Shopify Payments processing): each is `core` by its cell's place, Shopify Payments' route and plan rows, not by its name, as SH-70's line 67.
- **`NOTE` on a new thing whose entry has leads** (lines 47, 52, 56, 73, 185, 190, 194): the leads' cells are read above.
- **`NOTE line 73`: its first lead CM-PTN-008 holds nothing.** It is a referral programme, not the entry's thing (SH-71's notes).
- **The other leads to cells that hold nothing were read too, and none is its entry's thing.** Each is by name or by a common word:
  - CM-LOY-008 (3, 11);
  - CM-CHK-010 and CM-CHK-009 (8, 61, 46);
  - CM-API-013 (9, 62);
  - CM-APP-012 (7, 24, 34, 60);
  - CM-ORD-003 (13, 65);
  - CM-SHP-022 (45);
  - CM-PTN-007 (48, 54);
  - CM-PTN-009 (49);
  - CM-MKT-003 (53).
- **`NEW`:** Earn 1% back on all sales as subscription credits, 7 lines.

## Problems with the brief or the script

- **`earlier`'s twins are by pointer, and the plans pages' pointers don't align across English sites.** For au's and ca's card features and table rows, the twin it prints is often another feature or row (above). A twin by the card's `planType` and `name`, and by the row's heading, would serve SH-74 to SH-79. On the POS and international pages, and for the terms entries, the pointer twins were right.
- **Quotes with a straight apostrophe** ('Shopify's', 'you'll', 'World's') are quoted with “ ” or around those words. 49's footnote holds double quotes ("Cashback"), so its term is Cashback, as SH-72's line 24.
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief states (qualities wider than B-extent's list; the rulings).

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 80 of 80 entries, no problem. Its one `CHANGES`, CM-ONB-004 becoming held by a `shows` line, repeats SH-70's line 29, kept after SH-70.
- **Rules 1 to 8 stand,** for SH-74 to SH-79. Rules 3 to 5 follow the cells' own placements of the 30 September plan rows, read in `merged/evidence.tsv`: MB WAY and Bizum on CM-PAY-017 (SH-S-7025, SH-S-7026), in-person card rates on CM-PAY-021 (SH-S-7027), shipping discounts and labels on CM-SHP-002 (SH-S-7045, SH-S-7046), calculated rates on CM-SHP-004 (SH-S-7048).
- **One filler new to its cell:** Westpac, `outside` on CM-PAY-026, for Australia (rule 7).
- **Rule 8's alignment is made.** SH-70's line 46, the ae-ar POS Pro offer, now writes `www.shopify.com/ae-ar` only.
- **The twins.** `held_entries.py earlier` now counts a twin at the same place only where the two entries' `name` keys agree, where either has one. It also prints twins by the `name` key under the same `within`, wherever they stand on their page. The table rows' headings are found as labels, as before.
- **The yearly-price disagreements** are quoted each in its own line, as SH-72's were. Which price is charged isn't held.
- **Cost:** 16.1 million tokens over 64 requests, about 201,000 an entry.
