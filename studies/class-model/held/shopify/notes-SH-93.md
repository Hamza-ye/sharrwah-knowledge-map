# Held pass, Shopify, batch SH-93: notes

25 entries of `plan-page-public` (effort high), evidence at observed-sh@e38dc17e3, in `structures/shopify/plan-page-public/www.shopify.com_pricing/items.jsonl`, lines 94 to 661. The structure is read from its `source.html`: the WARC record `<urn:uuid:f99eeb48-c5ed-41b2-896a-c48a8f20db04>` of https://www.shopify.com/pricing, run `20260930T001507Z-published-indexes`, as served on 30 September 2026. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-93`).
- **1 to 4:** the Agentic card's four features (items.jsonl lines 94 to 97), after SH-92's card up to its button.
- **5 to 12:** the testimonial block: its heading 'Word on the street', a merchant's quote, its author and photo, and two figures with their texts (lines 98 to 105).
- **13 to 17:** what the selection's `read-as` rule leaves of the comparison table's mobile copy: its heading (106), its plan switcher (107), its button (108), the note row '*Requires Shopify Payments' (149) and the row heading 'Advanced tax platform' (199).
- **18 to 23:** the table's caption and header row (212 to 217).
- **24, 25:** the heading FAQs and the first question (660, 661). SH-94 begins with that question's answer (662).

**Placed:** 25 entries in 28 lines. 16 entries are on capabilities and 9 are `out`; none is `new`. 5 entries take more than one line.
- Supports, by line: 9 `core`, 9 `shows`, 3 `core;shows` (the column headers Basic, Grow and Advanced); no `own-service`, `extension-point` or `outside`.
- No line carries a filler; 6 carry qualities.
- The checker raises no `CHANGES`.

**Sources read:**
- **The brief and what it names:** the evidence map; the rulings, the last section; B-extent.md's "Cells and evidence" and "Conventions from the dry run", with "What a place of its own is"; observed-sh's `README.md` (Starting points), `docs/READING.md` (fetch runs, structures, indexes), `docs/GAPS.md` (nothing on this page) and `structures/README.md`; `structures/REGISTER.tsv`'s rows 40 and 129; `index/ledger-summary.tsv` and `index/ledger/sitemap--shopify-com-sitemap.tsv`, line 405; `selection.tsv`'s row 47; `show --meta` and `meta.json`.
- **The structure's rules:** SH-92's notes whole (P1 to P12 and the coordinator's check); SH-68's R3, R6 to R10 and its list of what no entry holds; SH-71's notes on `wordOnTheStreet` (by grep).
- **The twins:** found by grep of `entries.tsv` for each entry's words, then their lines by id: SH-71's lines 2, 3, 4, 6, 7 and 51, SH-74's line 23, SH-78's line 165, SH-68's line 96 (the table, SH-E-907c9d89), SH-70's line 96 (the hero), SH-72's line 2 (the first FAQ), and SH-92's lines 2, 3, 5, 6, 10, 11, 19, 28, 37, 38, 42, 43 and 89. The 31 October item itself (`pricing-page-data/.../items.jsonl`, line 161), by its keys, for what its page holds that no entry does.
- **`source.html`, to clarify only:** the Agentic features' markup (no tooltip); the testimonial photo's `img alt`; the comparison section's mobile copy (`comparison-table-mobile block md:hidden`, line 4), its switcher's `aria-pressed` and its button; the note rows' places; the row Advanced tax platform in both copies, with its tooltip and badge; the table's `caption` (`sr-only`) and `thead`; the asterisks the table's row headings carry; the loader data's `ctaTexts` (line 120).
- **The model:** `cells` for every capability placed on, and for CM-CHK-008 and CM-ANL-003 (leads of SH-94); the capabilities' notes, for homonyms.

## Rules my lines follow, beyond SH-92's P1 to P12

**P13. A FAQ split into its question and answer.** The 31 October twin is one accordion item, its heading and content together (SH-72's lines 2 to 17). Here the question (h3) and its answer (div) are two entries.
- **The answer** takes its twin's lines, each thing the answer names on its own capability (SH-68's R6), quoting its own words, with P1's scope: the site, after the plan a line states (Plus, on CM-PLN-002).
- **The question** takes the twin's line on the capability it asks about, with the twin's support, its own words its terms, and no plan unless the question names one. This follows rule 4's FAQ (`core` where its words name a built-in feature, `shows` where they name only a topic or terms), which gives the same support as the twin in all seven cases: PCI compliance, the domain and hosting are `core`; the cost, the cancellation, the fees and the countries `shows`.
- **A question that names only the platform as a whole** ('What is Shopify and how does it work?', entry 25) names no capability: `out`, its answer carrying the twin's line. The twin's line, CM-CHN-001, rests on the answer's words alone.
- **The FAQ's heading** (entry 24) is CM-ONB-003 `shows`, as SH-68's R6 and SA-3 place a FAQ heading.

**P14. What the `read-as` rule leaves of the table's mobile copy.** The rule reads the copy's row divs as the table's rows and drops them. The copy's other items are placed by what they state, each as the table's element it repeats:
- the heading 'Compare all features' (13) and the switcher of the four plans (14) take the table's line, CM-PLN-001 `core` (R3's table entry, SH-E-907c9d89);
- the button under the switcher (15) takes P3's two lines, for the plan pressed as served, Basic;
- the note row (16) is CM-PAY-002 `shows`, as its twin and R3;
- the row heading Advanced tax platform (17), which the rule misses because its value is a badge `p` beside a `span` (items.jsonl lines 199 and 200), takes its twin row's line.

**P15. The testimonial block** (entries 5 to 12) is `out`: its heading names only a grouping (P9), a merchant's quote and its author are a merchant's own words and data, the photo is the quote's, and the figures are SH-68's R10. P7's images are the cards' images, whose alt names the card's capability. SH-71's notes keep the 31 October block's heading and testimonial, which no entry holds, `out` in any case.

**P16. The closing banner** is SH-94's (its notes).

**P17. The table's own frame:**
- its caption (18), which only screen readers read, and its corner cell (19) take the table's line, CM-PLN-001 `core` (R3);
- each column header names a plan with its button (20 to 23):
  - the plan takes the table's column line, CM-PLN-001 `core`, its plan as scope, as P3 takes a card's name;
  - the button takes P3's lines;
  - where both fall on CM-PLN-001 with one scope ('Start for free', `shows`), they are one line, `core;shows`, since the checker allows an entry one line per capability and scope;
  - Plus's 'Try for $399' is `core` too, so its column takes one CM-PLN-001 line with the trial price.

## New things

None. Every entry's thing has a capability whose cell holds the same plan line or element, or its twin's line.

## Entries I couldn't tell, and what would settle each

- **25, 'What is Shopify and how does it work?', `out`** (P13). The other reading is the twin's line, CM-CHN-001 `core`, with no term, as SH-92's P3 gives a card's name its card's line. What would settle it: the coordinator's reading of "take its twin's line" for a question whose twin's only line rests on its answer. No cell changes either way.
- **8, the testimonial photo, `out`** (P15). The other reading is P7: `shows` on CM-POS-001 by 'retail counter'. The alt names a person in a shop, not selling in person.
- **13 and 19, 'Compare all features', CM-PLN-001 `core`.** These are the table's heading and corner cell. The other reading is `out` by P9, a heading over many capabilities' rows. SH-92's entry 4, the hero's link in the same words, was kept on CM-PLN-001 at the coordinator's check.
- **15, the mobile button, scope Basic.** It is served under Basic pressed. The loader data's `ctaTexts` give Grow and Advanced the same words, so `Basic;Grow;Advanced` is the other scope, as SH-92's entry 8 has it. No cell changes.
- **17, Advanced tax platform, CM-TAX-004 `shows`, as its twin.** The rule's intent was to drop the mobile copy's rows as read. If the coordinator extends `read-as` to this `span`, the entry drops; its line is the twin's either way.
- **20 to 22, `core;shows` on one CM-PLN-001 line.** The column's `core` and the button's `shows` would be two lines by rule 2, but the checker refuses a second line with the same capability and scope. Two lines would need the checker to allow it, as it does for a second line under its own condition (the ruling after SH-34).

## A structure whose items and sources disagree

- **The mobile copy and the table** are both in `<main>`: the copy in a region shown only below medium widths (`comparison-table-mobile block md:hidden`), the table in one shown from them up (`hidden md:block`, source.html line 4). The items don't say which copy an item is in.
- **A row split in two:** the mobile copy's row Advanced tax platform is two items, its heading `span` (line 199) and its badge 'Add on' (line 200, a `p`). The other rows are one `div` each, a heading with its value.
- **The note row** stands three times in each copy, as `div`s in the mobile copy and as `td`s in the table, under the sections with marked rows. The entry names the first. The selection's `drop-match` drops the `td`s; the `div`s stay.
- **The caption** is `sr-only`: the page doesn't show it, screen readers read it.
- **The column headers** (lines 214 to 217) hold each plan's name and its button as one item.

## What the sources state that no entry holds (for the second stage)

- **The loader data's table keys** (source.html, line 120): `planNames`, `ctaTexts` (Basic, Grow and Advanced 'Start for free', Plus 'Try for $399') and `ctaHrefs`, `captionText`, `checkAlt` 'Included' and `dashAlt` 'Not included'. These are the same page's table, held as its items.
- **The table rows the asterisk marks:** Built-in fraud analysis, Shipping insurance, Show prices in local currencies and Accept local payment methods (source.html, line 4). The 31 October twin's reading (SH-71's line 51) names fraud analysis and the local currencies and local payment methods rows, not Shipping insurance. Whether the 31 October tables still mark Shipping insurance wasn't read.
- **A hero variant in the loader data's translations** (line 120): 'Start for free, stay for {{paidTrialAmount}}', which the page doesn't render. Read it as SH-92's Starter plan translations: a lead only.

## Problems with the brief or the script

- **`earlier` finds no FAQ twin.** It printed no earlier line for any question, though SH-72 placed their twins: the twins' readings cite `pricing-faq-N`, not the questions' words. I found the twins by grep of `entries.tsv` for each question.
- **The checker allows one line per capability and scope for an entry,** where rule 2 gives each thing an entry names its own line, even on a cell that already holds the placement (20 to 22, above).
- **The selection's `read-as` rule misses a row heading split from its badge** (17, above).
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief states itself.

## The checker's lines, read again

- **No `CHANGES`:** every line is on a cell that already holds its support.
- **`NOTE`:** none on this batch.
- **`NEW`:** none.

## The coordinator's check (31 October 2026, after the batch, with SH-94)

- **The checker passes** on both batches, 25 of 25 entries each, with no problem and no `CHANGES`. With them, all of `plan-page-public` is placed: 124 entries in SH-92 to SH-94, after the selection read 197 as the model's own.
- **The rules P13 to P17 stand:**
  - a FAQ's answer takes its twin's lines, and its question the capability it asks about;
  - the mobile copy's leftovers are placed as the rows they repeat;
  - the testimonial is `out`;
  - the closing banner repeats the hero;
  - the table's frame takes the table's line.
- **A column header's plan and its button** share one CM-PLN-001 line, `core;shows`. The checker holds one line to a capability and scope, and the brief joins their supports.
- **The mobile row 'Advanced tax platform'** is a `span` the `read-as` rule doesn't read. It is placed as its twin row. One entry doesn't justify widening the rule.
- **The open choices stay as placed.** None changes a cell.
- **Cost of both batches:** 11.7 million tokens over 62 requests, about 234,000 an entry. The context reached about 298,000 tokens.
