# Held pass, Salla, batch SA-4: notes

130 entries of `com-plans`, its last (effort high), evidence at observed-sa@b0bd0b163. Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-4`).
- 1 to 111: the English pages from Salla Pro's price (en-ae line 40) to the footer's contact details: Salla Pro's card, the Special card, the testimonials, the comparison table (header, its five shared rows and its nine groups), the cards' toggle, the logo carousel, the closing banner, the FAQ's questions and the footer. Locator en-ae; most entries stand on en-sa too;
- 112 to 130: the lines only en-sa holds: its title, the yearly discount, the savings, the SAR prices, the struck price and its period, a testimonial's variant, the four Saudi-only table rows, 'Salla Basic', and its own closing banner and FAQ heading.

**Placed:** 97 entries on capabilities, 0 `new`, 33 `out`, in 120 lines (103 on capabilities, 17 `out`). Six entries take two or three lines: 12, 16 (three), 56, 59, 124, 128. Supports: 74 `core`, 29 `shows`; no `extension-point`, `own-service` or `outside`. Filler: ZATCA (124, on CM-TAX-007, as the cell's filler). Qualities: three annual prices (AED 2,990, SAR 990, SAR 2,990), two yearly savings, the yearly discount '16% off', the struck price '11.88', unlimited products and orders, the 14-day free trial of Salla Plus and of Salla Pro, and the referral commission 'up to SAR 100K'.

## Sources read

- The brief and what it names: observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the register's `com-plans` row; `selection.tsv`'s row; the evidence map; the coordinator's rulings, their last section most.
- SA-2's and SA-3's placements and notes, with the coordinator's checks that end them; SA-6's placements and notes (the English footer of the Special page, as the coordinator corrected SA-5).
- `com-plans/en-ae/text.txt` and `en-sa/text.txt` with their `meta.json`, and, for the Arabic counterparts, `ar-sa/text.txt` and `ar-ae/text.txt` where a reading names them.
- The two English pages' records, printed with `warc_text.py`: en-ae `raw/runs/20261008T133928Z-com-plans/fetch.warc.gz@235115` (sha256 `f88982d6…`, as `meta.json` states) and en-sa `…@555939` (sha256 `df21e677…`). The links' addresses, the blocks' names ('Cards toggle', 'Compare Button', 'Special', 'Partners Carousel'), the struck price's style and the comparison table's marks were read there.
- The FAQ's answers, in the run the register names: `raw/runs/20261028T145011Z-journey-com-plans-faq-en/steps/012.text.txt` (/en-sa/plans, all 11 opened, lines 121 to 155) and `steps/024.text.txt` (/en-ae/plans, lines 107 to 141), and its `index/run-notes.tsv` row. They clarify the questions only (M-12).

## Rules my lines follow

I kept to SA-2's eight rules and SA-3's, as the coordinator corrected them, and to SA-6's English footer lines.

1. **One entry, every place it stands.** Each reading cites its lines in en-ae and en-sa `text.txt`.
2. **Plan scope by card.** Basic's lines take `Basic;Salla Plus;Salla Pro`, Plus's `Salla Plus;Salla Pro`, Pro's `Salla Pro` (its card: 'All of Basic. All of Plus. And more', en-ae line 43). The Special card's lines take `Salla Special`: the card's logo is an image named 'Salla Special' and its button opens salla.com/specialplan/ (`…@235115`).
3. **The comparison table's marks** (the brief's known case), read in each record in the cards' order, Basic, Plus, Pro:

   | Row | en-ae (`…@235115`) | en-sa (`…@555939`) |
   | --- | --- | --- |
   | Unlimited products (33) | ✔✔✔ | ✔✔✔ |
   | Unlimited orders (34) | ✔✔✔ | ✔✔✔ |
   | Lower shipping costs with Salla Shipping Labels (121) | no row | ✔✔✔ |
   | All product types supported (35) | ✘✔✔ | ✘✔✔ |
   | Online & flexible payments (36) | ✘✔✔ | ✘✔✔ |
   | Salla Ads (122) | no row | ✘✔✔ |
   | Sell on Mahally (123) | no row | ✘✔✔ |
   | Built-in SEO (37) | ✘✘✔ | ✘✘✔ |
   | Built-in VAT support with ZATCA integration (124) | no row | ✘✘✔ |

   That is 15 marks on en-ae (11 included, 4 not) and 27 on en-sa (19 and 8), the counts SA-3 found on the Arabic pages. Each row's scope is the plans it is included in. The table is drawn twice; the record holds the marks in its first drawing only (by my reading of the bytes: no `data-framer-name` mark follows the second drawing's rows).
4. **The table's other groups** (38 to 46, Payment to Customers) hold no rows in the held page: their bodies are collapsed. Each is a container (rule 3) on the capability its title names, `core`, no scope, as the cells hold the dashboard's plan groups (aldfaa on CM-PAY-001, alshhn-oaltosyl on CM-SHP-001, the term إدارة المنتجات on CM-CAT-001). 'Key features' (32) is CM-PLN-001's, a container of the plans' lines.
5. **Market in scope (the ruling after SA-3).** A line only the Saudi pages hold takes السعودية; one only the UAE pages hold takes الامارات:
   - 113 to 119 (the discount, savings, struck price and its period, the SAR prices) and 121 to 124 (the four Saudi-only rows) take السعودية;
   - 1, 'AED 2,990', takes الامارات.
   - I used the ruling's Arabic words on the English pages, as the coordinator's message asks. The English footer's words are 'Saudi Arabia' and 'United Arab Emirates' (en-ae lines 244, 245); the coordinator may prefer them.
   - **For alignment:** SA-3's 'AED 990' (SA-E-10a07f5b) has no market in its scope, and the coordinator's check left it so. I read a price in one market's currency as a line only that market's pages hold, so my three prices carry their market. Either SA-3's line takes الامارات, or my three lose theirs; their quality keeps the currency either way.
   - A wording that differs by market, where both pages hold the same thing, takes no market: 'Basic Basket' (47, UAE) and 'Salla Basic' (125, Saudi) for the same toggle button; the two titles (112 and SA-3's SA-E-0d22b81c); the FAQ's heading (57 and 129); the closing banners (52 to 56 and 126 to 128); the testimonial's 'arises' and 'occurs' (27, 120).
6. **The footer, as SA-6's English lines:** About Salla, Careers, Merchant Tools, Industries, 'Explore stores by industry' and the nine sectors `out`; Resources and support, its help centre, academy, community, blog and Salla News CM-ONB-003 `core`; the Prompt Library CM-ONB-003 `shows`; Store Analyst CM-CNT-007 `shows`; the markets CM-ACC-008 `shows`; the rights line CM-ACC-002 `shows`; the contact details `out`. The en-sa footer's links are en-ae's, with /en-sa/ paths for the App Maker, influencers and sectors.
7. **FAQ questions are `shows`** on the capability each names, as SA-3's Arabic lines; each reading quotes the answer that clarifies it.

## New things

None. Every entry's thing has a capability, or is `out` by the rulings.

## Entries I couldn't tell, and what would settle each

- **15, 'Custom pricing that matches your needs'** (Special card): CM-PLN-001 `core`, the plan priced to the merchant's needs, since the card states no price and its button is 'Contact us'. The line's layer in the page is named for the Arabic card's line, 'رسوم دفع مرنة تدعم توسُّع أعمالك' (`…@235115`), which SA-2 placed on CM-PAY-007 (flexible payment gateway fees). SA-6 placed the English by its own words where they differ from the Arabic, and I did the same. CM-PAY-007 `core` is the alternative; the coordinator may want the two languages aligned, as for 'Run discount promotions'.
- **16, 'Tools to manage multiple stores, branches, and teams'**: three lines, CM-ACC-003 (several stores), CM-INV-005 (branches) and CM-STF-001 (teams), `core`, Salla Special. The Arabic card's line names only branches and warehouses (SA-E-a57d64c9, CM-INV-005).
- **12, the Special card's text:** CM-PLN-001 `shows` as SA-2's Arabic, and CM-ONB-003 `shows` for 'dedicated support', a claim beside the card's own line (14, `core`).
- **48 and 49, 'Salla Plus free for 14 days' and 'Salla Pro free for 14 days':** CM-PLN-001 `core`, quality 'free trial: 14 days'. CM-PLN-001's note says 'A free trial and the inactive and pending-termination states are the ONB batch's', but no ONB capability holds a free trial (searched: free trial; trial; تجربة مجانية; فترة تجريبية; free for 14; 14 days; trial period), and CM-PLN-001's Salla cell already holds the flag plan-free-trial, not released (SA-S-3452). Against the line: the Arabic pages' same buttons name only the plans (ar-sa text.txt lines 129 to 131), the FAQ's answer says only that Basic 'is free with no time limit', and the flag isn't released. The register's `com-plans` row names the dashboard's offer to a Basic store (structure `merchant-plans`), which would show whether a trial is offered. If it isn't, the lines are `shows`.
- **124, VAT and ZATCA:** two lines, CM-TAX-001 (VAT support) and CM-TAX-007 (the integration with ZATCA, the cell's Pro plan line and its filler). I gave the CM-TAX-007 line ZATCA as its filler, the entry's own word, as the cell holds 'هيئة الزكاة والضريبة والجمارك (ZATCA)'.
- **121, the labels' row:** Saudi only in the table, though the Basic card on both markets keeps 'Ship with discounted Salla shipping labels' (SA-3's SA-E-c5b7837a, no market). The two lines differ in scope by the ruling's letter.
- **37, Built-in SEO:** marked for Pro only. The cell's plan line تحسين ظهور المتجر على محركات البحث comes from the dashboard's plans; whether its plan agrees isn't read here.
- **59, the developer-or-designer question:** CM-ACC-001 and CM-SFR-001 `shows`, as SA-3's. The English answers name no themes, where the Saudi Arabic answer does.

## The checker's lines, read again

- **No `CHANGES` line.** No line alone changes a cell.
- **`NOTE` on a product named with the brand:** 'Choose Salla Pro', 'Salla Plus free for 14 days', 'Salla Pro free for 14 days', 'Salla Packages' and 'Salla Basic' are Salla's plans; Salla Academy, Salla Community, Salla Blog and Salla News its own learning and news, as the coordinator read SA-6's; 'Salla Shipping Labels' and 'Salla Ads' are Salla's own label service and ad product, whose cells hold them as `core` (CM-SHP-002: labels 'بدفع مباشر من خلال منصة سلة'; CM-MKT-010: 'Salla's product for … digital advertising campaigns'). Each is `core` by what it shows.
- **`NOTE` on first leads that hold nothing:** CM-EVO-001 (9 and 32, by 'features'), CM-OPS-004 (16, by 'tools'), CM-MKT-008 (55, by 'marketing' and 'sale'), CM-AIA-005 (65, by 'product' and 'sell') and CM-SHP-013 (66, by 'shipping options', which there are apps' delivery rules): none is the entry's thing; each reading says so.

## A structure whose items and sources disagree

- None between the items, the text and the records.
- **The English pages differ by market beyond the currency,** as SA-3 found for the Arabic: en-ae draws no discount, saving or struck price, and its table has five rows to en-sa's nine. They also differ in wording: the toggle's Basic button, the title, the carousel's heading ('Partners in Success' on en-ae, 'Over 68,000 brands and counting' on en-sa, lines 229 to 231), the closing banner and the FAQ's heading ('Most Frequently Asked Questions by Merchants' against 'Got questions?').
- **The English cards' toggle adds a 14-day free trial** that the Arabic toggle doesn't state (above).
- **The struck price is cut in the page itself:** '11.88' (en-sa lines 30, 141), as SA-3 found '11,88' on ar-sa; 990 with its saving of 198 is 1,188 (a reading). Pro's '3,588' is whole (SA-3's SA-E-7c083559).
- **Lines with no entry in this batch:** the footer's 'Marketing tools' (en-ae lines 270, 318, 366) and 'Available in' (243, 291, 339). Entry 41 'Marketing Tools' differs from the first by case only; I named the link in its reading. 'Available in' is CM-ACC-008's term and SA-6's entry on the Special page.

## What the sources state that no entry holds (for the second stage)

- **The English FAQ's answers** (`raw/runs/20261028T145011Z-journey-com-plans-faq-en/steps/012.text.txt` lines 125 to 155, /en-sa/plans; `steps/024.text.txt` lines 111 to 141, /en-ae/plans), the same as SA-3 found in Arabic:
  - the markets: /en-sa/plans 'Salla is currently available in Saudi Arabia and the United Arab Emirates, and coming soon to the rest of the GCC.' (line 131); /en-ae/plans 'Salla is currently available in Saudi Arabia, the United Arab Emirates, Kuwait, Oman, Qatar, and Bahrain.' (line 117). For CM-ACC-008;
  - the requirements: /en-sa/plans a Commercial Registration or Freelance Certificate, 'A Saudi mobile number.' and 'A Saudi bank account.' (line 128); /en-ae/plans a legal document and 'a bank account.' (line 114). For CM-ACC-004, CM-PAY-003 and CM-PAY-005;
  - Basic 'is free with no time limit' and upgrading is open at any time (lines 134, 120). For CM-PLN-001, against the 14-day trial lines;
  - the payment methods: 'Mada, cards, Apple Pay, cash on delivery, and Buy Now, Pay Later services' on /en-sa/plans (line 149), the same without Mada on /en-ae/plans (line 135). For CM-PAY-002, CM-PAY-012, CM-PAY-029 and CM-PAY-015;
  - carriers local and international and the merchant's own courier (lines 146, 132), CM-SHP-015; import of products and customer data (152, 138), CM-MIG-001; the store's own iOS and Android app from the dashboard (155, 141), CM-CHN-006; dropshipping partners and marketplaces (143, 129), CM-CAT-010; what may be sold, under 'local laws and Salla’s terms' (140, 126), CM-TRU-009 and CM-TRU-010.
- **The UAE page's table lacks four rows** (above): for the cells of CM-SHP-002, CM-MKT-010, CM-CHN-002, CM-TAX-001 and CM-TAX-007.
- **Framer's layer names in the English pages are Arabic** (`…@235115`, `…@555939`): the Special card's lines carry the Arabic card's words ('رسوم دفع مرنة تدعم توسُّع أعمالك', 'نظام متكامل لإدارة الفروع والمستودعات', 'تكامل مع أنظمة تخطيط الموارد (ERP)'), the Special card's text 'توسَّع بتجارتك وقلِّل التكاليف التشغيلية لمتجرك مع باقة سلة سبيشل.', the testimonials' heading 'تاجر بثقة.. تاجر مع سلة', and the closing banner 'النظام المتكامل لدعم متجرك من أقوي الخبراء في التجارة الإلكترونية'. They are the designer's names and nothing a reader sees, as SA-6 found; I placed nothing on them, and cite them only to clarify 15 and 16.
- **The pages' meta description** (en-sa `…@555939`): 'Join more than 60,000 successful merchants on Salla. Integrated packages for every merchant's launch. Choose the package that suits your business size and start your journey to success today.' A claim; no entry holds it.
- **The footer's app links,** to Google Play (`com.emoney.sallacp`) and Apple's App Store (id1148458340), with no text (`…@235115`): a lead for Salla's merchant app, CM-SRF-001, as SA-6 notes.

## Problems with the brief or the script

- **The ruling's market words are Arabic** ('the words of Salla's footer, مدعوم في: السعودية الامارات'), so the English pages' Saudi-only lines carry an Arabic scope beside English plan names. Said above; the coordinator may want 'Saudi Arabia' there.
- **The checker's brand note** fires on Salla's plan names and its learning sites, as SA-3 and SA-6 said, and here on Salla Shipping Labels and Salla Ads, whose cells already hold them as Salla's own.

The checker's last line, for SA-4: `130 of 130 entries placed; 0 problems` (after this file was written).

## The coordinator's check (30 October 2026, after the batch)

- **'Custom pricing that matches your needs' (15) moves to CM-PAY-007.** Its layer is named for the Arabic card's 'رسوم دفع مرنة تدعم توسُّع أعمالك', so the two are one element, the payment fees SA-2 placed there (the ruling after SA-4). Entry 16 keeps its three lines: the English names multiple stores and teams, and either language is Salla's statement.
- **The market in scope is aligned:** SA-3's 'AED 990' takes الامارات, as this batch's 'AED 2,990' does and its SAR prices take السعودية. The English footer's 'Saudi Arabia' and 'United Arab Emirates' name the same two markets. The scope keeps the Arabic words, so that one market reads the same in every batch.
- **The 14-day trial (48, 49) stands** as `core` on CM-PLN-001, with its quality. Against it stand the features list's unreleased `plan-free-trial` and the Arabic page's silence, so CM-PLN-001's Salla cell is read again at the amendment for whether a trial is offered.
- **The other lines stand:**
  - the comparison table's marks, read from each page's HTML;
  - the nine collapsed groups as containers;
  - the footer as SA-6's corrected lines;
  - the FAQ's questions as `shows`.
- **Cost:** 11.1 million tokens over 65 requests, about 85,000 an entry. No cell changes. `com-plans` is placed.
