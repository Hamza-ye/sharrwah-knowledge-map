# Held pass, Shopify, batch SH-92: notes

74 entries of `plan-page-public` (effort high), evidence at observed-sh@e38dc17e3, in `structures/shopify/plan-page-public/www.shopify.com_pricing/items.jsonl`, lines 1 to 93. The structure is read from its `source.html`: the WARC record `<urn:uuid:f99eeb48-c5ed-41b2-896a-c48a8f20db04>` of https://www.shopify.com/pricing, run `20260930T001507Z-published-indexes`, as served on 30 September 2026. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-92`).
- **1 to 4:** the hero: its heading, the trial, the switch Pay yearly and the link Compare all features.
- **5 to 41:** the four plan cards, each as its name, price, description, button and features: Basic 5 to 13, Grow 14 to 21, Advanced 22 to 30, Plus 31 to 41.
- **42 to 58:** the block Always included: its heading, and five cards, each an image, a heading and a text, with the assistant's greeting (49, 50).
- **59 to 74:** the heading “But wait, there’s more”, the POS Pro card (60 to 69) and the Agentic card up to its button (70 to 74). SH-93 begins with the Agentic card's four features (items.jsonl lines 94 to 97).

**Items with no entry of their own:** items.jsonl lines 17 and 26 (the Grow and Advanced cards' 'Start for free', entry 8's words and link), line 44 (the second link Compare all features, entry 4's) and lines 62 to 77 (the always-included block a second time, entries 43 to 58's words). The build makes one entry of a repeated text, and `entries.tsv` names its first line only. That an entry stands for each of its places is a reading.

**Placed:** 74 entries in 90 lines. 67 entries are on capabilities, 3 are `new` (SH-68's new thing) and 4 are `out`. 14 entries take more than one line.
- Supports, by line: 75 `core`, 11 `shows`, 1 `extension-point` (the Agentic image, `core;extension-point`); no `own-service` or `outside`.
- 1 line carries fillers and 30 carry qualities.
- The checker raises no `CHANGES`.

**Sources read:**
- **The brief and what it names:** the evidence map; the rulings, the last section most; B-extent.md's "Cells and evidence" and "Conventions from the dry run", with "What a place of its own is"; observed-sh's `README.md` (Starting points), `docs/READING.md` (fetch runs, structures, indexes), `docs/GAPS.md` (nothing on this page) and `structures/README.md`; `structures/REGISTER.tsv`'s rows 40 (`plan-comparison-public`) and 129 (this structure); `index/ledger-summary.tsv` and `index/ledger/sitemap--shopify-com-sitemap.tsv`, line 405 (https://www.shopify.com/pricing, captured, its evidence the 31 October run); `selection.tsv`'s row 47; `show --meta` and `meta.json`'s source.
- **The earlier batches:** SH-68's rules R0 to R11 and SH-78's notes, whole. The twins' lines, by number: SH-70's lines 95 to 148, SH-71's 2 to 12, SH-73's 2 to 5 and 44 to 68, SH-74's 4, 5 and 209, SH-75's 181, SH-78's 146 to 170, and SH-68's lines on SH-E-39133966 and SH-E-3add0529. Also SH-34's line on SH-E-2178ade3 and SH-1's on SH-E-093e0005. The twins' texts in `entries.tsv`: SH-E-f44f3d56, SH-E-fcfc1ed1, SH-E-6e2449a7, SH-E-f5f29b9a, SH-E-b4d10049, SH-E-ebb0a3a5, SH-E-bd947ff2.
- **`source.html`, by script, to clarify only:**
  - the hero's and the cards' HTML (line 4): the switch's `aria-checked` and label, and the features' `data-tooltip`;
  - the always-included region and the images' `alt`;
  - the loader data (line 120): the cards' prices, `promoText` and feature names;
  - the comparison table's tooltips for Millions of tokens and Earn 1% back on all sales, and its POS Pro row.

  Every line's terms and fillers are its own entry's words.
- **The model:**
  - `cells` for every capability placed on, and for the leads CM-PAY-021, CM-INV-005, CM-SFR-003, CM-POS-002, and for CM-ACC-003, CM-AIA-003, CM-AIA-004 and CM-ONB-004;
  - `caps --terms` for signup, sign up, sign-up, create store, free trial, trial, prompt, website builder, store builder and tokens;
  - `class_slice.py key` for SH-S-7018 and SH-S-7007, and `search` for 'Earn 1% back', 'Millions of tokens' and 'Tokens power';
  - the held entries, by grep over `entries.tsv` and the placements, for the twins, the tooltips' words, 'Included in every plan', the cards' buttons and the toggle (no `pricing-page-data` entry holds the cards' buttons or the switch).

## Rules my lines follow, for SH-93 and SH-94

**P1. Scope.** Every line takes its plans, in the page's words, then the site, `www.shopify.com`, as the pricing batches write it (SH-68's R0).
- A card's line takes its card's plan: `Basic;www.shopify.com`. A feature with no value also takes the plans above it: `Basic;Grow;Advanced;Plus;www.shopify.com`.
- The page is one site's, so every line takes the site, unlike R0's lines that every read site states.
- The hero, the page's frame and the always-included block take the site alone (R2: 'Always included' names no plan).
- The POS Pro card's own entries take the site alone: its title, badge, price, description and features heading are the offer itself (the ruling after SH-70). A feature that comes with POS Pro takes `POS Pro;www.shopify.com`.
- The Agentic card's entries take `Agentic;www.shopify.com`.
- An `out` line takes none.

**P2. Twins.** The page's elements are those of the 31 October www.shopify.com plans page, which SH-68 to SH-79 placed (`pricing-page-data`, items.jsonl line 161):
- the hero, SH-E-f44f3d56;
- the cards, SH-E-6e2449a7, SH-E-bf25ae76, SH-E-bffc37bf and SH-E-f5f29b9a, and their features (SH-70's and SH-78's lines);
- the always-included block, SH-E-fcfc1ed1;
- the POS Pro card, SH-E-b4d10049, and its features;
- the Agentic card, SH-E-ebb0a3a5.

An entry takes its twin's lines (capability, support, scope by plan), quoting its own words, and its reading names the twin and the twin's line. A twin is the same element: the same card, or the same card of the block. A label alone isn't one: `earlier`'s 'Start for free' is the POS page's block (SH-73's lines 3 and 4), not a card's button. `earlier` prints no twin across the two structures, since this structure's items have no `name` key, so I matched the twins by hand.

**P3. A card split into its parts.** The 31 October card is one entry. Here its name, price, description, button and features are entries of their own.
- **The name and the description** take the card's CM-PLN-001 `core` line, its plan as scope.
- **The price** takes CM-PLN-001 and CM-PLN-002 `core`, with the price as quality: 'price per month paid yearly: <its words>'. The page serves the switch Pay yearly checked (P11). The loader data's monthly and yearly prices go in `reading` only; they are the twins'.
- **A sign-up button** takes two lines:
  - CM-ACC-001 `shows`: the page its link opens, admin.shopify.com/signup, the merchant's account (the ruling after SA-19). Its term is `signup`, from the link.
  - the line its words state: 'Start for free' is CM-PLN-001 `shows`, quality 'start: free' (SH-68's R4; SH-73's line 4); 'Try for $399' is CM-PLN-001 `core`, quality 'trial price: $399', the card's `promoText` (SH-68's R2).

  A button that stands on several cards is one entry, and the cards' plans are its scope (entry 8).
- **The Agentic card:** its title takes CM-PLN-001 and CM-AIA-005 `core`, as its twin's two lines. Its price takes CM-PLN-001, and its description both.

**P4. Features:** SH-68's R2 and R11. A feature with a value takes its card's plan; one with none takes its plan and the plans above it; a feature that names several things takes a line for each (entry 9).

**P5. Tooltips.** A feature's or a row's tooltip, the HTML's `data-tooltip`, is part of its entry, as R3 reads the table's tooltips. The credits' tooltip gives the quality 'back on sales: 1%, 0.5% on non-Shopify Payments'. Its words are quoted from `source.html`, or with the id of an entry that holds them.

**P6. Always included.** Each card's heading and text take the twin's line on the card's capability, `core`, the site alone.
- A text that names two things takes both: entry 48, on CM-SFR-001 and CM-AIA-001.
- The phone, card reader and counter of entry 55 are named in a list of what may be used: no line (the ruling after SA-41), as in the twin.

**P7. Images.** An image's item is its `img alt`.
- It is `shows` on the capability its alt names, with its card's scope; the card's heading and text carry the `core` line.
- Where the alt states more than its card's topic, its words are placed. The Agentic image names the platform's Agentic dashboard and its AI integration partners:
  - `core`, the admin's own Agentic page (the ruling after SH-2);
  - `extension-point`, with the venues as fillers (M-3), as SH-34's line on SH-E-2178ade3.

**P8. UI strings.** A greeting, a prompt or a label that names nothing ('Hi there!', 'How can I help?') is `out` (SH-68's R10; the twins' readings).

**P9. Headings.**
- A heading over several capabilities' cards ('Always included', “But wait, there’s more”) names only a grouping: `out` (SH-68's R3; the ruling after SA-28).
- A heading over one capability's things takes its line: the POS Pro card's 'Level up your stores with:' is CM-POS-001 `core`, as its twin's `featuresHeading`.

**P10. Links.** A link takes the line of the page or place it opens, as SH-1's link to a help page (SH-E-093e0005) and the ruling after SA-19.
- 'Learn more', to /pos/pricing, is CM-POS-001 `shows`, its address's words its term.
- The hero's 'Compare all features' (#compare-all-features) takes its twin's line, CM-PLN-001 `core`: the plans' comparison table, whose header row is CM-PLN-001 `core` (R3's table entry).
- The sign-up buttons are P3's.

**P11. The switch Pay yearly** is CM-PLN-002 `core`, the yearly billing period. The page serves it checked ('Show Plan Prices as Pay yearly Subscription Rate', its `aria-checked` true), so the cards' prices are per month paid yearly.

**P12. Where the page differs from its twin**, each line quotes its own words and its reading says how. I compared the cards: their prices, card rates, staff counts, shipping discount, the credits' maximums, the POS Pro price and features, and the Agentic price are the same on both dates. The credits' tooltip differs (below).

## New things

**`new:Earn 1% back on all sales as subscription credits`** (SH-68's), 3 lines: the cards' credits, entries 13, 21 and 30 (SH-E-0daeae51, SH-E-6e469dbb, SH-E-5b99fa04).
- **Values:** 'Earn up to $5,000 in credits', $7,500 and $10,000, each with the tooltip 'Earn 1% back on all sales as subscription credits (0.5% on non-Shopify Payments).'.
- **The table's row:** the same page's row (the concern map's inventory entries SH-I-1141 and SH-I-1243; SH-E-3787fad6 on 31 October) adds 'Valid for your first 6 months or until you reach the max.' (`source.html`).
- SH-68's notes give the rest: its place of its own, its proposed domain, area and parent, and the terms searched.

No other `new` thing: every other entry's thing has a capability whose cell holds the same plan line or place.

## Entries I couldn't tell, and what would settle each

- **4, 'Compare all features', on CM-PLN-001 `core`:** placed by its twin's line. The twin's reading gives the link no line of its own (SH-70's line 96, 'neither gives a line'). The other readings:
  - `shows`, as P10's other link;
  - `out`, by SH-68's hero rule.

  What would settle it: the coordinator's reading of "takes the line its twin takes" for a link that its twin holds with no line. No cell changes either way.
- **42, 'Always included', `out`:** CM-PLN-001 `shows` is the other reading. SH-68's R4 places the POS page's 'Included in every plan' (SH-E-bd947ff2) so: a page's container that names what every plan includes.
- **The images:**
  - 43, 46, 53, 56 and 60 are `shows`. `core` is the other reading, since the twin card's one line covers its `imageAlt`; their words differ from the 31 October alts, though (P7).
  - 70 is `core;extension-point`. `shows` alone is the other reading, since it is an image's description.
- **8, 34 and 74, the sign-up buttons:** their CM-ACC-001 `shows` rests on the page their link opens (the ruling after SA-19), since the buttons' words name no account. Without it, each keeps only its CM-PLN-001 line.
- **65, 'Learn more', CM-POS-001 `shows`:** `out` is the other reading, as the brief's example of a UI string. Its address names a page, which the brief's 'names no place' leaves open.
- **3, Pay yearly, on CM-PLN-002 alone:** the label's earlier lines are the table's row Pay yearly, whose prices also take CM-PLN-001. The switch states no price.

## A structure whose items and sources disagree

- **What the items hold:** the rendered text inside `<main>`, in order, with repeats (the buttons, the link, the always-included block twice). The entries hold each repeated text once (above).
- **The images:** a `picture` item's text is its `img`'s `alt` (`source.html`, line 4). The item doesn't say so.
- **What only the loader data holds** (line 120):
  - the cards' monthly prices, under the switch's other state ('Show Plan Prices as Pay monthly Subscription Rate'): $39, $105, $399, $2,300;
  - the cards' promotions, '$1/month for 3 months' and, on Plus, '$399 for your first month'.

  The rendered cards show the yearly price only. The item and the source don't differ; the source holds more.
- **The credits:** this page's tooltip states 0.5% on non-Shopify Payments and no domain credit. The 31 October popover states 'Get 1% back on sales' and 'Add a domain, get $20' (SH-78's lines 152, 157 and 161). Each line quotes its own. That the page changed between the two dates is a reading: these are two captures, one the HTML's attribute and the other the loader data's popover.

## What the sources state that no entry holds (for the second stage)

- **The page's terms object** (`source.html`, line 120): `basicAnnualPrice` '$24.00 USD', `annualDiscountPercentage` 25, `googleCountryOffer` '$500 USD', `minimumMonthlyPrice` '$5' USD, `paidTrialAmount` '$1', `paidTrialMonths` 3, `posProPriceUsd` '$89', `posRetailLocations` '1,000', and `signupTypes` with paid_trial_experience and the control and treatment of e_06d1ad5d27d16046cc6d829de669769b. These are the 31 October terms entry's values (SH-E-b51ec61c, SH-78's lines 146 to 148): a lead only for a subject that compares prices over time.
- **The Agentic card's link** to /agentic-plan (line 120), which the rendered card doesn't give as an address. The 31 October data prunes it too (SH-68's R10).
- **Translations for a Starter plan card** (line 120), which the page doesn't render (`starterPlanCard` null): 'plans2.plans.0.displayName' 'Starter', 'Sell instantly through social media and messaging apps or a simple online store'. The Starter plan is held as the POS page's summaries (SH-68's R4).
- **The always-included region's label**, Always included features (line 4).

## For SH-93 and SH-94, and the coordinator

- **Kinds my rules cover that the later batches meet:**
  - the table's header cells with their buttons ('Basic Start for free' to 'Plus Try for $399', items.jsonl lines 214 to 217), P3 and P10;
  - the mobile table's header, 'Basic Grow Advanced Plus' (line 107), and its button (line 108);
  - the image 'Smiling store owner at a retail counter' (line 101), P7;
  - the closing block 'Turn plans into progress', with its trial and credits (line 678), its email label (679) and its button (680);
  - the disclaimer 'You agree to receive Shopify marketing emails' (682), to which the 31 October hero's lines give no line (SH-70's line 96).
- **The table's second rendering:** the selection's rule (`drop-match:^tag: td;read-as:plan-comparison-public th`) drops the table's cells and reads its row headings as `plan-comparison-public`'s. It doesn't drop the page's second, div-based rendering of the table: items.jsonl lines 107 to 211, such as 'Pay monthly $39 USD/mo', 'Pay yearly $29 USD/mo' and 'Earn 1% back on all sales Up to $5,000 USD'. Each such div holds a row's heading with one plan's value, Basic's where I looked. So SH-93 holds about 100 entries that repeat rows the model read. That they are the mobile table is a reading of the items. The coordinator decides whether SH-93 places them, by the rows' cells, or the rule drops them.

## The checker's lines, read again

- **No `CHANGES`:** every line is on a cell that already holds its support, or on the new thing.
- **`NOTE`, lines 66 and 68** (entries 56 and 58): their first lead, CM-APP-010 (App settings), holds nothing on Shopify. It leads by the word integration alone and isn't the entries' thing, as their readings say.
- **Two `NOTE`s fixed while writing:**
  - a quote found nowhere held (line 51): it now names SH-E-bd947ff2;
  - the brand note on the Agentic image (line 84): its term is now 'Agentic dashboard', and its reading says it is `core` by the admin's own Agentic page (the ruling after SH-2), not by the brand.
- **`NEW`:** Earn 1% back on all sales as subscription credits, 3 lines.

## Problems with the brief or the script

- **`earlier` finds no twin across structures.** This structure's items have no `name` or `within`, so the 31 October twins were matched by hand, by element (P2). Its label lookup needs two words or more, so the plan names and prices had no lead; I found the cards' lines by SH-78's line numbers.
- **`entries.tsv` gives a repeated text's first line only,** so an entry's other places are read from items.jsonl: entry 8's three cards, for instance.
- **The selection's rule leaves the table's second rendering in** (above).
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief states itself.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 74 of 74 entries, no problem and no `CHANGES`.
- **The rules P1 to P12 stand for SH-93 and SH-94.** Each line quotes the page's own words of 30 September, where they differ from the twin's of 31 October (P12). The credits tooltip states no domain credit.
- **The page's mobile copy of the comparison table is read,** as the batch found. Its 84 row lines (a heading with a plan's value) and 14 section headings repeat rows the concern map cites from the same record. The selection's `read-as` rule now reads them so, `th,div`, and the build dropped 98 entries of SH-93 and SH-94. The 50 left are cut 25 and 25.
- **The open choices stay as placed:** 'Compare all features' and 'Always included' as the twins' lines and P9; the images `shows`; the sign-up buttons' CM-ACC-001 `shows` by the page their link opens, as SH-73 placed them.
- **Cost:** 14.0 million tokens over 69 requests, about 189,000 an entry. The context reached about 331,000 tokens.
