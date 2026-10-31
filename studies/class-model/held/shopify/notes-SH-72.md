# Held pass, Shopify, batch SH-72: notes

80 entries of `pricing-page-data` (effort high), evidence at observed-sh@e38dc17e3, in `structures/shopify/pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl`. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-72`).
- **1 to 12:** the rest of www.shopify.com/ae's plans page (items.jsonl line 5, https://www.shopify.com/ae/pricing):
  - the eight FAQs (`content.faqs.accordion.accordionItems`, 1 to 8);
  - the disclaimer `apyDisclaimer` (9) and its list of three footnotes (10 Balance, 11 Credit, 12 Capital).
- **13 to 80:** www.shopify.com/ae's POS page (line 6, https://www.shopify.com/ae/pos/pricing):
  - its terms entry (13);
  - the six plan summaries with their features (`planSummaries.mainPlans`, `alternatePlans`: 14 to 40);
  - the section 'Included in every plan' (`sideBySideGridContent`) with its six items (41 to 47);
  - the section on what POS Pro is (`posLiteVsProContent`) with its six items (48 to 54);
  - the casual in-person selling and POS Pro lists, twice: `posLiteVsProContent.plans` (55 to 67) and `posLiteVsProPlans` (68 to 80).

  SH-73 begins with the same page's `howToGetStartedContent`.

**Placed:** 80 entries in 187 lines, all on capabilities: no `new`, no `out`. 65 entries take more than one line. Supports: 168 `core`, 14 `shows`, 5 `outside`; no `own-service` or `extension-point`. Five filler lines, the disclaimer's providers. 61 lines carry qualities.

**Sources read:**
- the brief and what it names: the evidence map; the rulings, the last section; B-extent.md's "Cells and evidence" and "Conventions from the dry run"; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md` (nothing on these pages), `structures/README.md`; `structures/REGISTER.tsv` row 141; the ledger `index/ledger/sitemap--shopify-com-sitemaps.tsv` (the ae pages /pricing, /pos/pricing and /international/pricing captured by run 20261031T003815Z-shopify-com-pricing-by-country); `selection.tsv`'s row; `show --meta`;
- SH-68's, SH-69's, SH-70's and SH-71's notes and placements first, with their coordinator's checks, and kept to their R0 to R11, SH-69's rules 1 to 7, SH-70's rules 1 to 9 and SH-71's rules 1 to 3;
- items.jsonl lines 5 and 6 only for the parts of my sections that no entry holds (below). Every line's terms and quotes are its own entry's;
- the model: `earlier`; `cells` (name, note and cell) for every capability placed on and for the leads; no `caps --terms` search was needed, since every entry has a twin placed and checked.

## Rules followed

**Every entry is the English twin of an ae-ar entry, matched by its pointer.** `earlier` found the FAQs' twins by their ids (`pricing-faq-0` to `-7`) and the lists' by `PosLite` and `PosPro`, and no other. As SH-71 did, I joined each entry to the ae-ar entry at the same pointer, on the ae-ar page of the same kind: line 5 against line 2 (the plans pages), line 6 against line 3 (the POS pages). All 80 pointers match, checked by script:
- 1 to 67 are SH-69's 17 to 83 (its placement lines 18 to 180);
- 68 to 80 are SH-70's 1 to 13 (its lines 2 to 25).

Each line takes its twin's capability, support and plans, and its own sites (R0), English terms, quotes and qualities. Its reading names the twin's line.

**R0, the sites:** 66 entries are labelled with all 18 English sites and take no site. The other 14 take their labels after their plans:
- 2 (six sites: ae, au, ca, ph, www.shopify.com, sg);
- 9, 11 and 13 (ae);
- 10 (twelve sites);
- 12 (thirteen sites);
- the six plan summaries (ae);
- 59 and 72 (ae, ph, www.shopify.com).

**Two departures from the twins, both by rulings made after them**, for the coordinator to align:
1. **The POS Pro plan is the offer itself, so its sites alone are its scope** (59, 72; the ruling after SH-70). These lists' 'POS Pro' with its badge 'Add on' and its price '+ $89 USD/month/location' is the offer, as the plans page's POS Pro card is. Their features take 'POS Pro' (60 to 67, 73 to 80).
   - The ae-ar twins, SH-69's line 164 (SH-E-abc35c09) and SH-70's line 9 (SH-E-f7de5f1c), write 'POS Pro;www.shopify.com/ae-ar'.
   - SH-70's rule 9 had asked for this alignment, and the coordinator's check answered it with the ruling.
2. **WebBank's country is joined to the site with ` and `** (9's CM-PAY-026 line: 'www.shopify.com/ae and U.S.'). The ruling after SH-69 gives the line its own scope, the United States, where the disclaimer states WebBank issues Shopify Capital's funding. The ruling after SA-53 then writes a condition that must also hold with ` and `, since `;` separates alternatives.
   - The ae-ar twin, SH-69's line 37, writes 'www.shopify.com/ae-ar;الولايات المتحدة'.
   - The site and the plans of every other line are a list, which needs no ` and ` (the same ruling).

**The rest, as the twins:**
- **R1:** the POS page's terms entry (13), three `core` lines.
- **R4, the POS page:**
  - the plan summaries' fields as qualities, with their description's things as lines (SH-69's rule 4);
  - each feature on its own capability and on CM-POS-001, its plan as scope;
  - Starter's POS Pro add-on, `is_available: false`, `shows` (SH-69's rule 6);
  - the items under 'Included in every plan' scoped to the four plans (SH-69's rule 3);
  - the items on POS Pro scoped 'POS Pro' (R8).
- **R6:** the FAQs. 3's annual or 3-year term takes Plus (the ruling after SH-69).
- **R7:** the qualities.
- **R9:** the disclaimer's providers `outside`, with fillers.
- **SH-69's rules:**
  - rule 1: the footnotes joined to their rows by their words, `shows`;
  - rule 5: the lists ending 'and more' give examples, which take no line (44, 54);
  - rule 7: loyalty insights are CM-ANL-001's.

## New things

None: every entry's twin is placed on a capability.

## Entries I couldn't tell, and what would settle each

The twins' doubts carry over. SH-69's notes give what would settle each:
- **1, what Shopify is, on CM-CHN-001 `core`.** `out` is the other reading.
- **3's account cancellation on CM-ONB-002 `shows`.**
- **10 to 12, the footnotes, `shows`.** 10's 'a reward provided by Shopify' could read as `core`. The cells are `core` either way.
- **43's CM-INV-005 line.**
- **45 on CM-PAY-021 alone.** Its lead CM-PAY-004 (processing, acquiring and holding funds behind the payment service, by 'payment processing') names the acquirer's side, which the item doesn't name. CM-PAY-002 is the other reading.
- **46 on CM-POS-002 `core`** (a CHANGES line, below).
- **47 on CM-POS-001 `core` and CM-POS-004 `shows`.**
- **31, 52, 63, 76 on CM-ANL-001,** SH-69's rule 7.

Two of mine:
- **48, the section heading on what POS Pro is, takes 'POS Pro',** as its twin (SH-69's line 139). It is neither the priced offer nor a feature: it heads POS Pro's features, and its subhead names both the paid plans' casual selling and the upgrade. If the coordinator reads it as the offer, its scope is empty, since it is on all 18 sites.
- **9's WebBank scope** (rule 2 above): 'www.shopify.com/ae;U.S.' is the twin's form, if the ruling after SA-53 isn't meant for a site and a country.

## A structure whose items and sources disagree

- **www.shopify.com/ae's two pages state different yearly prices.**
  - The POS page's summaries give the yearly prices at 25 per cent off the monthly ones: Basic `annual_monthly_price` 24 USD (`annual_price` 288), Grow 69 (828), Advanced 299 (3588). They are entries 14, 18 and 22.
  - These follow the page's terms, 'basicAnnualPrice: <span>$24.00 USD</span>' with `annualDiscountPercentage` 25 (entry 13).
  - The same site's plans page states $29, $83 and $359 a month paid yearly: its cards (SH-70's lines for SH-E-a7f5c34f, SH-E-23fc01de, SH-E-5e019eb6) and its Pay yearly row (SH-71's SH-E-3ee1b1f1).
  - The ae-ar POS page's summaries also state 29, 83 and 359 (SH-69's lines 45, 58, 71).
  - Each line quotes its own entry. Which price is charged isn't held. The ae POS page was served under the variant 'f_2e2905455a798fa9df40308c0b8b53ee:true,f_77c8150780b85c85656903fc3fada251:true', the ae-ar POS page's adds 'e_06d1ad5d27d16046cc6d829de669769b:treatment', and the ae plans page's adds two more experiments. That the variant is the cause is an assumption.
- **Plus's POS Pro add-on** (26) is titled 'POS Pro included' with `included_in_plan: false`, while Retail's (38) has the same title with `true`. This is SH-69's disagreement again, in English. The line quotes the title and names the flag.
- **The footnotes' order** (SH-69's rule 1): the list holds Balance, Credit and Capital, while the rows' marks are ¹ Balance, ² Capital and ³ Credit (SH-71's 76 to 78).
- **The items and the entries agree:** the entries are the items' decoded loader data, and their pointers are the ae-ar entries' own (above). I didn't print the WARC records.

## What the sources state that no entry holds (for the second stage)

- **The POS page's sales contact flow,** `loaderData.*.content.posContactModal`, items.jsonl line 6 (www.shopify.com/ae/pos/pricing).
  - Its words: “Let's talk about Shopify Point of Sale”; 'Answer a few questions about your business to learn if you qualify for sales support.'; 'A member of our sales team will reach out within one business day.'; 'Share your store address for customized market support.'
  - Its heading names the point of sale, and its other cards offer a free trial.
  - No entry holds it: no locator in `entries.tsv` points into `posContactModal`, on any site. Every one of the 62 POS pages carries it, the ae-ar one included.
  - It is a lead for CM-ONB-003 (the platform's support and sales help for merchants) and CM-POS-001. The selection's rule (`selection.tsv`, `wrap:` and `nested:`) names none of its keys.
- **The plans page's FAQ heading,** `content.faqs.headingHtml` 'FAQs' (line 5): CM-ONB-003 `shows` elsewhere (SH-68's R6).
- **The POS page's image text,** `sideBySideGridContent.image.alt` and `sideBySideProps.image.alt` 'Woman using POS device' (line 6), pruned (`image`): `out` in any case.
- **The footnotes' and disclaimer's links** (in the entries; their pages aren't in this structure): help.shopify.com/en/manual/finance/shopify-balance/rewards/earning-rewards ('Reward Terms', 10); /ae/legal/shopify-credit-program-terms (11, 9) and /ae/legal/shopify-credit-issuing-bank-terms (9). They are leads for CM-PAY-023's and CM-PAY-025's terms, which the cells already cite, as SH-69 noted for ae-ar.
- **Kept from SH-69's leads:** POS Pro's staff performance tracking (49, 'track performance') and the endless aisle (54) have no capability. CM-STF-004 (staff targets) is the lead for the first.

## The checker's lines, read again

- **`CHANGES CM-INV-004@shopify gains core` and `holds nothing: becomes held`, by line 130 (50, SH-E-13b3afb3):** kept.
  - The POS Pro item states 'get low stock alerts from a single place', the twin of SH-69's line 146, which the coordinator's check after SH-69 kept: CM-INV-004 `core`, scope POS Pro.
  - The cell still holds nothing on Shopify because the amendment hasn't run.
- **`CHANGES CM-POS-002@shopify gains core`, by line 120 (46, SH-E-2143a92c):** kept.
  - Every plan includes 'Access to reliable, modern POS hardware', hardware 'that staff can use at the counter or on the floor', with no seller named. This is the twin of SH-69's line 136.
  - SH-68's line 122, the plan line that includes card payments with a phone or card reader, gives the cell the same `core`, which the coordinator's check kept.
- **`NOTE` on a product named with the platform's brand** (lines 17, 114 and 119, header as line 1): each is `core` by its cell's place, not by its name, as SH-69's check has them.
  - 17 is Shopify Checkout (8): its settings route checkout-settings.
  - 114 is Shopify POS (42): its plan rows and its POS app.
  - 119 is Shopify Payments for POS (45): CM-PAY-021's plan rows In-person card rates.
- **`NOTE line 119`: its first lead CM-ORD-003 holds nothing.** That lead is order statuses, by the word 'processing' only. It is not the entry's thing, which is the processing of payments at the point of sale.
- **The other leads to cells that hold nothing were read too, and none is its entry's thing.** Each is by name or by a common word:
  - CM-SFR-016, social sharing (1, 8);
  - CM-APP-012 (2);
  - CM-PTN-010 (3, 6, 10, 12);
  - CM-CHK-010 (4);
  - CM-MKS-009, reference lists of countries (5);
  - CM-TRU-021 (7);
  - CM-PTN-007 (9, 22);
  - CM-PTN-009 (11);
  - CM-API-013 (49);
  - CM-OPS-004 (51).

  CM-CHK-008 (8, by 'buy' and 'button') is accelerated checkout buttons, not the Buy Button channel. CM-LOY-004 (31, 52, 63, 76, by 'loyalty') is SH-69's rule 7's other reading.
- **The checker's last line:** '80 of 80 entries placed; 0 problems'.

## Problems with the brief or the script

- **`earlier` finds a twin only by a key the two languages share:** the FAQs' ids and the lists' names. The plan summaries carry `display_name` and English-only feature keys, and the sections' items carry no key at all, so their twins aren't found. A lookup by pointer, on the other language's page of the same kind, found all 80 here, as SH-71 asked.
- **Quotes with a straight apostrophe** (“What's POS Pro?”, “What's included”, “isn't”, “don't”) are quoted around those words in the placements, or the words are given in mine.
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief states (qualities wider than B-extent's list; the rulings).

## The coordinator's check (31 October 2026, after the batch)

- **No cell changes beyond earlier batches'.** CM-INV-004 and CM-POS-002 repeat SH-69's.
- **Every entry takes its Arabic twin's line,** matched by pointer, all 80 confirmed. The agent's two departures follow the rulings made after the twins, so the twins are aligned to them:
  - **The POS Pro plan itself** takes only its site (the ruling after SH-70). SH-69's line 164 and SH-70's line 9 now write `www.shopify.com/ae-ar`.
  - **WebBank's country** is a condition that must also hold (the ruling after SA-53). SH-69's line 37 now writes `www.shopify.com/ae-ar and الولايات المتحدة`.
- **`held_entries.py earlier` now prints an entry's twins:** the platform's other entries at the same place in their own source, with their lines. SH-73 to SH-79 find their twins with it, and the brief names it.
- **Leads:**
  - the POS page's sales-contact flow (`posContactModal`), for CM-ONB-003 and CM-POS-001;
  - the ae POS page's yearly prices against the plans page's, served under different variants, each quoted in its own line.
- **Cost:** 11.8 million tokens over 60 requests, about 148,000 an entry.
