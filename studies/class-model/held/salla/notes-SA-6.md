# Notes: SA-6, Salla's `com-specialplan`, entries 1 to 112 (30 October 2026)

**What I read** (effort `high`):
- the brief and what it names:
  - observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md` and `structures/README.md`;
  - the register's rows for `com-specialplan` and `com-plans`, and `selection.tsv`'s row;
  - the evidence map, and the coordinator's rulings, their last section most closely;
- SA-5's placements and notes, with the coordinator's check that ends them. My lines keep to SA-5's corrected lines wherever the English is the same thing;
- the four labels' `meta.json` and `text.txt`. en-ae and en-sa differ only in the KPI block's currency (en-ae lines 56, 58 and 60: 'AED'; en-sa: 'SAR', 'Saudi Riyal'). So the readings cite en-ae, the locator of most entries, and en-sa only for its own two entries (111, 112);
- the page itself, the archive record its `meta.json` names: en-ae at `raw/runs/20261008T133928Z-com-plans/fetch.warc.gz@367339` (sha256 `80016716…`, as `meta.json` states), printed with `warc_text.py`. I read its links, the comparison table's marks, the button under the table and the FAQ's state there. They are the same as in SA-5's Arabic record:
  - the hero's 'Get in touch' and the banner's 'Apply now' open the same share.hsforms.com form, tagged `utm_content=hero_book_appointment` and `cta_apply_now`;
  - the rows Integration with global shopping platforms, Dedicated Account Manager and Full store customization without code are marked `Included (Check)` in both columns, Salla and Other;
  - 'View all comparisons' is a `<button>` with no address;
  - the nine FAQ questions are `Closed`;
  - the footer's links go to the same addresses as the Arabic footer's, with `/en-ae/` paths for the App Maker, marketing, influencers and the sectors.

## The batch

- My batch is the English page from the hero's button (en-ae line 17) to the footer. SA-5 placed the Arabic page and the English header and hero.
- The English lines that equal an Arabic or English line SA-5 holds aren't entries here: the counters ('+', '0', '%'), the language switch 'Ar', 'Solutions' and 'Salla Special' in the footer, the FAQ's numbers and the email address. So the footer has no 'Solutions' or 'Salla Special' entry in this batch.
- **No `new` thing.** Every thing the entries name is a capability's that SA-5 or its corrections already placed, or `out` by the ruling after SA-2 and SA-5.

## Where my lines follow SA-5, and where the English differs

- **The same things, the same lines:** the card and row headings (rule 2 of SA-5's notes), the card and row texts, the comparison's Salla and Other values, the buttons, the FAQ's questions, the footer's markets, links and rights line, and the KPI labels. Each reading names the Arabic entry it follows.
- **Corrected as the coordinator corrected SA-5:**
  - the data migration card (23) is `own-service` on CM-MIG-005, on the migration service's terms (SA-S-5121);
  - Salla News (87) is CM-ONB-003 `core`, and the Prompt Library (89) CM-ONB-003 `shows`;
  - About Salla (70), Merchant Tools (88), Industries (97), 'Explore stores by industry' (98) and the nine sectors (99 to 107) are `out`, Digital products with them.
- **Where the English words differ from the Arabic, I placed them by their own words:**
  - **19,** 'Everything you need to run smoother, scale faster, and stay ahead': `out`. Its Arabic (SA-E-339b2266) names lower operating costs, which SA-5 placed as a claim on CM-PLN-001 `shows`. The English names no cost, plan line or feature. The page's English meta description names the costs ('reduce the operational costs of your store with the Salla Special package', `…@367339`), but no entry holds it.
  - **32,** 'Commerce that keeps up. And stays ahead.': `out`. Its Arabic (SA-E-906f85f4) names the merchant's financial dealings, which SA-5 placed on CM-PAY-005 `shows`. The English names nothing.
  - **37,** 'Everything you need to sell, scale, and stay ahead.': `out`. Its Arabic (SA-E-49cecf59) names lower cost, which SA-5 placed on CM-PLN-001 `shows`.
  - **33,** the card text under 'Commerce that keeps up' (en-ae lines 100, 102). Its Arabic is the concern map's SA-S-2193, not an entry, so this is the first entry of the card's text. It names payments, shipping and daily sales deposits, placed as SA-5 placed the same things where they run on into the support card (SA-E-a6b6746b): CM-PAY-001, CM-SHP-001 and CM-PAY-005 `core`, with the quality 'sales deposits: daily'. It also says 'ship globally', which the Arabic doesn't: CM-SHP-020 `shows`, as a claim with no place or feature.
  - **35,** the support card's text: 'From day one, Salla’s experts are here to help you scale smarter…'. CM-ONB-003 `core`, as the Arabic. Unlike the Arabic, it names no merchant success team, no technical team and no languages, and it doesn't run on with the card above.
- **36,** 'Built to give your business the advantage', the comparison table's heading: CM-PLN-001 `core`, as a container of the plan's lines, as SA-5's Arabic SA-E-e1467b15. Its English names no plan, but the table is the plan's comparison by its blocks and rows.
- **82,** 'Resources and support', the footer's heading. The English header says Resources (SA-5's SA-E-4b28f823), the footer this, so it is an entry of its own. CM-ONB-003 `core`, by the ruling: its links are the platform's help and learning for merchants.
- **Scope:** `Salla Special` on the plan page's body, as SA-5's rule 3. The account manager's row adds 'advanced plans' (41). The header, footer, KPI block, testimonial and FAQ take none.

## Entries I couldn't tell, and what would settle each

These are SA-5's open cases, in their English:
- **9,** 'A company providing its services to Salla merchants': CM-PTN-005 `shows`. It could be read as `out`, a statistic. Its count isn't held.
- **21,** the integration card: CM-PAY-028 `shows`. It names no accounting system or ERP.
- **39,** Amazon and Noon through the App Store: CM-CHN-003 `core`, with the venues as fillers, by M-3. It names no maker of the integrations. The App Store's listings for Amazon and Noon would settle whether it is `extension-point`.
- **64,** SKU codes: CM-CAT-001 `shows`. If 'track my products' means stock, it is CM-INV-001's.
- **65,** minimum order quantity or minimum purchase value: CM-ACC-006 `shows`, as SA-5's SA-E-197d1164. If a minimum order is its own thing, it is `new:minimum order quantity or minimum purchase value`, with no place of its own.
- **78** and **80,** Partner program and Partner Resources: placed by their words on CM-PTN-001. Their addresses are apps.salla.sa/ar/categories and docs.salla.dev.
- **90,** Store Analyst: CM-CNT-007 `shows`, by its address SEO-GEO-checker. What it checks isn't held. GEO may also bear on CM-AIA-005.

## The checker's lines, read again

- **`CHANGES` CM-SHP-003 becomes held, by 60's `shows` line.** The question 'And up to what amount does the insurance coverage go?' (en-ae line 150) names insurance cover on shipments of valuable items. Its answer is closed. The line is the same as SA-5's SA-E-a9743b1c, which the coordinator let stand. The checker reports it again because SA-5 isn't amended into the model yet. Kept.
- **`NOTE` own-service on CM-MIG-005 (23).** It rests on the cell's maker evidence (SA-S-5121), as the coordinator's correction of SA-5 reads it. Kept.
- **`NOTE` 'core on a product named with the platform's brand':**
  - for 33's three lines, the brand is the plan's name ('With Salla Special'), and the lines are plan lines;
  - for Salla Academy, Salla Community, Salla Blog and Salla News (84 to 87), they are the platform's own help and learning, as SA-5's Arabic lines and the ruling place them.

  `core` by what each shows.
- **`NOTE` on 59 and 60's first lead, CM-B2B-002 (companies as business buyers):** the lead matched 'companies'. The questions' companies are shipping carriers, so the lead isn't the entries' thing.

## A structure whose items and sources disagree

- None between the items, the text and the record.
- The English text doesn't run on as the Arabic support card does (SA-5's notes): en-ae lines 104 and 106 end with the card's own sentence.
- The KPI block's currency differs by market (above). The en-sa page names 'Saudi Riyal' and the en-ae page 'AED'. The ar-ae page names the Saudi riyal (SA-5's notes).

## What the sources state that no entry holds (for the second stage)

- **The page's meta description** (`…@367339`): 'Expand your business and reduce the operational costs of your store with the Salla Special package, specially designed to meet the needs of major companies and leading brands.' It is a statement of the plan's purpose, and no entry holds it.
- **The FAQ's answers** (nine questions, `Closed` in `…@367339`): not held, as in the Arabic. They would bear on CM-SHP-003, CM-SHP-015, CM-ACC-006 or a new minimum-order thing, CM-CAT-001, CM-CAT-003, CM-SUP-001 and CM-SFR-001.
- **The KPI values,** filled by the counter script the record names (`AnimatedNumberCounter`): not held. The stability rate would be a quality of CM-OPS-001.
- **The comparison's column Other:** a logo with no text (`…@367339`, the blocks named `Other` and `Others`). Its values name the Mazeed platform.
- **The footer's app links,** to Google Play (`com.emoney.sallacp`) and Apple's App Store (id1148458340), with no text: a lead for Salla's mobile apps, as SA-5 notes.
- **Framer's layer names in the English page** are still Arabic (for example `منصة المقترحات`, `خاصية البيع بالجملة و للشركات`, `ماهي المدة لتجهيز التطبيق؟`). They are the designer's names, and nothing a reader sees. I placed nothing on them.

## Problems with the brief or the script

- The checker's brand note fires on the platform's own learning sites (Salla Academy, Salla Community, Salla Blog, Salla News) and on a plan's name, where no separate product is meant.
- The checker's CHANGES line for CM-SHP-003 repeats SA-5's, since batches are checked against the model before the earlier batch is amended. The coordinator decides the two together.

## The coordinator's check (30 October 2026, after the batch)

- **The corrections to SA-5 are carried over as its check reads them:**
  - the public site's headings and the sector links are `out`;
  - Salla News and the footer's Resources and support are CM-ONB-003 `core`, and the Prompt Library is CM-ONB-003 `shows`;
  - the data migration card is `own-service` on CM-MIG-005.
- **The ruling after SA-3 gives no line here a market.** The Special page's Saudi and UAE texts are the same but for one counter's currency, '1 Billion SAR +' against '1 Billion AED +' (`com-specialplan/en-sa` and `en-ae/text.txt`).
- **The English page's own lines stand:** the three slogans `out`, and the card text's `shows` on CM-SHP-020 for 'ship globally', which the Arabic doesn't say.
- **The checker's brand NOTE** on the plan's name and on Salla's learning sites asks a question these lines answer: a plan line and the platform's own learning are `core`.
- **Cost:** 5.0 million tokens over 37 requests, about 45,000 an entry, the cheapest Salla batch so far: its entries are the English of SA-5's. No cell changes beyond SA-5's.
