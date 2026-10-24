# Cards: what the proposals cite as not found or absent, on salla

8 records, from Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8.

## The points cited

- **Q1, section 5, line 122:** - The rate source. Where Salla's automatic prices take their rate was not in what was read (not checked on Zid); WooPayments takes its rates from its server, and Shopify's automatic rates carry a fee by the store's location. Keep the rate source its own part and each order's rate on the order; a company decision on a rate provider settles it, with section 6. Q1-SA-N02, Q1-WC-K0755, Q1-SH-057
- **Q2, section 1, line 10:** - Salla's reading didn't show a statement on sanctions screening, or on countries refused for sanctions. Q2-SA-N01
- **Q2, section 1, line 12:** - The payment company behind the service is set by place too. Shopify identifies, "for each Designated Country, (a) the Payment Processor(s)", and may change them; Stripe's contracting entity is "the entity specified below for User's Stripe Account Country"; Zid may switch its payment processors; Salla provides payments "عبر شركائها", and which company processes them was not in what was read (the page is held, not read). Shopify's processors and Stripe's entity match by role. Q2-SH-K1563; Q2-SH-K1561; Q2-WC-P0108; Q2-ZD-002; Q2-SA-P0079; Q2-SA-G0113
- **Q2, section 1, line 33:** - Salla's agreement names one Saudi company under Saudi law, and its en-ae page the same company and registration (not checked on Zid); whether a clause names a company per market was not in what was read (the page is held, not read). Zid's terms name one Saudi company, its Kuwaiti Zid Pay terms apply Saudi law with Riyadh's courts, and Zid Egypt has its own commercial registration. Q2-SA-P0076; Q2-SA-033; Q2-SA-020; Q2-SA-G0213; Q2-ZD-K0214; Q2-ZD-K0212; Q2-ZD-K0221
- **Q2, section 1, line 38:** - Which Automattic company controls WooCommerce data depends "on the particular service and the location of the individual"; BigCommerce processes shoppers' information as processor, the merchant being controller. Salla's privacy policy is held but not read on storage. Zid may transfer data abroad "if appropriate safeguards are in place"; where it stores data was not in what was read. Q2-WC-K0502; Q2-BC-K0436; Q2-SA-G0218; Q2-ZD-K0283; Q2-ZD-G0060
- **Q2, section 5, line 114:** - Whether Sharrwah is a party to any payment arrangement, and whether any arrangement holds sellers' money through it. Keep each **Provider agreement** direct by default, and any holding arrangement as an option left off until the founder decides. Settled by the founder, with the company decisions in section 7. The parties of Salla's payment services contract were not in what was read. Q2-SH-K1580; Q2-SH-K1603; Q2-SA-G0177
- **Q3, section 1, line 37:** - Salla's agreement and Zid's terms carry the same clause for products needing an official licence, "بالإفصاح عن الترخيص وكافة بياناته": the same term, both official pages. Neither platform's full list of such products was in what was read; Zid decides the need after reviewing the data, with books and the Ministry of Media as its example. Q3-SA-047; Q3-ZD-K0247; Q3-SA-N02; Q3-ZD-N04; Q3-ZD-023
- **Q3, section 1, line 74:** - Zid Pay gives 14 days to correct wrong data, then disables the account and returns all amounts to end customers. Salla suspends payments and settlement "بعد انتهاء المهلة", a period whose length was not in what was read. WooPayments may restrict payments or payouts once a deadline for missing information passes. Q3-ZD-P0012; Q3-SA-002; Q3-SA-N01; Q3-WC-P0055
- **Q3, section 5, line 146:** - What unmet requirements do to money: holding payouts, blocking withdrawals, returning payments to buyers, and the days between, as Shopify, Zid and Salla show them; Salla's period was not in what was read. Keep open, as a money flow: a restriction type for each, with schedules per place, all off until decided. Settled by the founder's decision under the guard, Q5's proposal and providers' terms. Q3-SH-072; Q3-ZD-P0012; Q3-SA-002; Q3-SA-N01
- **Q3, section 5, line 148:** - Which products need a licence in a place, and when it is checked: no full list for Salla or Zid, and no time Shopify checks, was in what was read. Keep open: product rules as data per place, including an area within a country, as a ban at one area of Yemen needs; licence fields on products; and the timing of any check. Settled by legal advice for each place. Q3-SA-N02; Q3-ZD-N04; Q3-SH-N02; YK-247 (American goods banned @ Houthis' area, as of 2025-10-05)
- **Q6, section 1, line 15:** - Salla's agreement, as served at its UAE address, names a company registered in Saudi Arabia, and which Salla company contracts in each market was not found. Zid's terms name one Saudi company and Saudi law. Q6-SA-023; Q6-SA-G0213; Q6-ZD-K0214; Q6-ZD-K0211

## The cards

### Q1-SA-N02

**Cited at:** Q1, section 5, line 122

**Record** (`studies/proposals/records/Q1/salla/not-found.tsv`):
- nf_id: Q1-SA-N02
- bears_on: 2
- what_is_missing: Where the exchange rate used by Automatic pricing by exchange rate (تسعير تلقائي حسب سعر الصرف) comes from, and who sets or can change it. The setting's panel, as one store's page showed it, says only that product prices are set automatically according to the current exchange rate.
- kind: not in what was read
- read: observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl line 756 (article epj429qolc9kuugn5gqroamo); observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/en/localization.json (settings.product_prices); observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T121631Z-com-pages/fetch.warc.gz offset 34902179 (https://salla.com/blog/expand-online-store-to-gcc); observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T180430Z-journey-localization-demo/steps/008.text.txt (https://s.salla.sa/localization/settings, Customize Product pricing); observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T180430Z-journey-localization-demo/responses/0140.json (GET /v2/translations/ar/localization)
- searched: python3 -I method/corpus_search.py salla "سعر الصرف" "أسعار الصرف" "exchange rate" "exchange rates" --max 10; opened: the article تخصيص إعدادات الأسواق المتعددة, dashboard-translations/en/localization.json, salla.com/blog/expand-online-store-to-gcc; not read: the article صفحة أداء المتجر (ar position 1160), docs.salla.dev records in raw/runs/20261005T234928Z-docs-md (offsets 1523861, 1540447, 1547246, 1557521, 1577680, 1589939), com-pages offsets 21776610 and 66365062, dashboard-translations/en/settings.json; re-check 2026-10-19: python3 -I method/corpus_search.py salla "سعر الصرف" "أسعار الصرف" "exchange rate" "تسعير تلقائي" "التسعير التلقائي" --max 10; python3 -I method/corpus_search.py salla "according to the current exchange rate" "حسب سعر الصرف الحالي" "Automatic pricing by exchange rate" "تسعير تلقائي حسب سعر الصرف" --max 10 (run documents listed: translation saved responses only); python3 -I method/held_index.py https://s.salla.sa/localization/settings; opened: journey-localization-demo steps 7 and 8, responses/0140.json and responses/0160.json (GET /admin/v2/settings/fields/scopes.product_prices: {"type":true})
- who_can: founder
- route: Question to Salla's merchant support: which exchange rate source Automatic pricing by exchange rate (تسعير تلقائي حسب سعر الصرف) uses in Markets, how often it is updated, and whether a merchant can set or change the rate

### Q2-SA-N01

**Cited at:** Q2, section 1, line 10

**Record** (`studies/proposals/records/Q2/salla/not-found.tsv`):
- nf_id: Q2-SA-N01
- bears_on: 1;3
- what_is_missing: A statement that Salla restricts or withholds its platform, Salla Payments or stores for a country, person or customer because of sanctions or a sanctions list, with the list it applies and its reason; the held KYC schema names a check CheckSallaBlacklisted ('ID suspended due to compliance or terms violations') without naming what it checks against
- kind: not in what was read
- read: observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt; observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/privacy/text.txt; observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/policies-selling/text.txt; observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/payments/text.txt; observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz@3700206 (https://salla.com/ar-ae/terms); observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz@20448927 (https://salla.com/en-ae/terms); observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/kyc-schema/demo@en/source.json; observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl line 302 (article g0cbvwqncrfmptexs580y6f7)
- searched: python3 -I method/corpus_search.py salla "sanction" "OFAC" "embargo" "العقوبات الدولية" "الحظر الاقتصادي" "قوائم العقوبات" "غسل الأموال" "money laundering" --max 10: no document matched; python3 -I method/corpus_search.py salla "غير متاحة حاليًا" "غير متاح حاليا" "not available in" "sanctions" "عقوبات دولية" "الدول المحظورة" "restricted countries" "غير مدعومة في" --max 10: hits concern themes, features, carriers and per-country wallet features (UAE, Kuwait COD tracking, bank transfer country_not_supported, already copied); none names sanctions; documents opened: none beyond the snippets, since no title or snippet could show it; re-check against the observed runs, 19 October 2026: python3 -I method/corpus_search.py salla "sanction" "OFAC" "embargo" "العقوبات" "قوائم العقوبات" "blacklist" "محظور" "غسل الأموال" --max 10: the run documents listed (saved responses of customers/blacklist, the payments, users and customers translations, writes.jsonl lines 37 and 44 of run 20261008T205113Z-journey-customers-demo) concern banning a store's customers; none names sanctions; no run document opened beyond its snippet
- who_can: founder
- route: Question to Salla merchant support, asked from the merchant dashboard: does Salla screen merchants, owners or payments against sanctions lists, which lists, and which countries are refused

### Q2-SA-G0113

**Cited at:** Q2, section 1, line 12

**Record** (`studies/proposals/records/Q2/salla/copied-gaps.tsv`):
- concern_id: SA-C-114
- placement: where
- what_would_show_it: The page where Salla names who processes and acquires Salla Payments transactions, and under which licence
- means: read the held page
- who_can: agent
- route: https://salla.com/payments held at observed-sa@4ca2e896:structures/salla/com-policies/payments (structure, 200) and observed-sa@4ca2e896:raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz@8607584 (warc, 200)
- why_not_held: Stage 0, 12 October 2026: the page is held, and the run could not read it. Before: observation needed, founder, save a page from a browser. salla.com answers 403 with a bot challenge to this session (tested on https://salla.com/terms, 2026-10-10); the help articles read name only the payment services contract (عقد خدمات الدفع), not its parties: help.salla.sa/article/تحويلات-مدفوعات-سلة-والتسويات-في-الإمارات-سلة/nvs6bt51hvlweulqzayp3o76; help.salla.sa/article/تحويلات-مدفوعات-سلة-والتسويات-في-الكويت-سلة/oklj5eoidm82h73hfra94dv2
- gap_kind: page not read

### Q2-SA-G0213

**Cited at:** Q2, section 1, line 33; Q6, section 1, line 15

**The same record, cited as:** Q6-SA-G0213

**Record** (`studies/proposals/records/Q2/salla/copied-gaps.tsv`):
- concern_id: SA-C-230
- placement: where
- what_would_show_it: The usage agreement's party clause naming the Salla entity for each market (Saudi Arabia, UAE, Kuwait)
- means: read the held page
- who_can: agent
- route: https://salla.com/terms held at observed-sa@4ca2e896:structures/salla/com-policies/terms (structure, 200) and observed-sa@4ca2e896:raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz@11978142 (warc, 200)
- why_not_held: Stage 0, 12 October 2026: the page is held, and the run could not read it. Before: observation needed, founder, save a page from a browser. salla.com answers 403 with a bot challenge to this session (tested on https://salla.com/terms, 2026-10-10); no other held page carries its text.
- gap_kind: page not read

### Q2-SA-G0218

**Cited at:** Q2, section 1, line 38

**Record** (`studies/proposals/records/Q2/salla/copied-gaps.tsv`):
- concern_id: SA-C-233
- placement: where
- what_would_show_it: The privacy policy's statement of where personal data is stored and processed (country, hosting provider)
- means: read the held page
- who_can: agent
- route: https://salla.com/privacy held at observed-sa@4ca2e896:structures/salla/com-policies/privacy (structure, 200) and observed-sa@4ca2e896:raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz@12104866 (warc, 200)
- why_not_held: Stage 0, 12 October 2026: the page is held, and the run could not read it. Before: observation needed, founder, save a page from a browser. salla.com answers 403 with a bot challenge to this session (tested on https://salla.com/terms, 2026-10-10); no other held page carries its text.
- gap_kind: page not read

### Q2-SA-G0177

**Cited at:** Q2, section 5, line 114

**Record** (`studies/proposals/records/Q2/salla/copied-gaps.tsv`):
- concern_id: SA-C-177
- placement: responsible
- what_would_show_it: The contract's party clause: which Salla entity or payment company signs with the merchant
- means: read the held structure
- who_can: agent
- route: observed-sa@4ca2e896:structures/salla/kyc-schema (a candidate: structures/REGISTER.tsv describes it as the store verification in the merchant dashboard); then Merchant dashboard https://s.salla.sa/payments/kyc (توثيق المتجر), as the owner of a store going through verification: open and save the payment services contract (عقد خدمات الدفع) presented there
- why_not_held: Stage 0, 12 October 2026: a held structure may show it. Before: observation needed, founder, record a journey. The contract is not public and no held journey shows it.
- gap_kind: page not read

### Q3-SA-N02

**Cited at:** Q3, section 1, line 37; Q3, section 5, line 148

**Record** (`studies/proposals/records/Q3/salla/not-found.tsv`):
- nf_id: Q3-SA-N02
- bears_on: 1;2;4
- what_is_missing: A list of the products or activities for which Salla requires a licence before they are sold, or a statement of whether, when and how Salla checks such a licence.
- kind: not in what was read
- read: observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt (المادة الرابعة, المادة العشرون); observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/policies-selling/text.txt; observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl line 1401 (article c7kvq9bm0bxjtef4yf5us13q), line 30 (article ndz1k0tts5p7gfnqqxcubspl), line 302 (article g0cbvwqncrfmptexs580y6f7), line 177 (article v6ymzcrb4i7euybyuta4cfad); observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T121631Z-com-pages/fetch.warc.gz offsets 65748829 (https://salla.com/en-sa/blog/online-store-license-saudi-arabia) and 64784169 (https://salla.com/en-sa/blog/ecommerce-for-pharmacies)
- searched: python3 -I method/corpus_search.py salla "تتطلب ترخيص" "تحتاج ترخيص" "منتجات تتطلب" "رخصة مزاولة" "require a license" "requires a licence" "licensed products" --max 10; earlier, python3 -I method/corpus_search.py salla "المنتجات المحظورة" "المنتجات الممنوعة" "يمنع بيع" "يحظر بيع" "prohibited products" "restricted products" "prohibited items" --max 10. Opened: the usage agreement (structures/salla/com-policies/terms), https://salla.com/en-sa/blog/online-store-license-saudi-arabia, https://salla.com/en-sa/blog/ecommerce-for-pharmacies. Not read: help articles k0odb96jwj77rugq5o0cg4jq (shipping routes), act1fbl4q70qca3kx6tcp55q (business bank account), by5x09rk8rl2kw7w5at0egye (Deliverist), the dashboard translations orders.json, products.json and themes-marketplace-monorepo.json, the blog pages on supply chains and bank transfer for abayas, the other held copies of the usage agreement (en-sa, ar-ae, en-ae, /policies/terms), partners.salla.com/legal/themes-policy.; re-check 2026-10-19: python3 -I method/corpus_search.py salla "تتطلب ترخيص" "رخصة" "ترخيص" "license" "licence" "permit" --max 10. The run documents it lists concern the freelance work permit in the KYC schema, influencers' licences, a calendar component's licence key and a store's product description; none was opened, since none could show a product licence Salla requires.
- who_can: founder
- route: Question to Salla merchant support (dashboard help): which products or activities need a licence before they can be sold on Salla, and whether and when Salla checks it.

### Q3-SA-N01

**Cited at:** Q3, section 1, line 74; Q3, section 5, line 146

**Record** (`studies/proposals/records/Q3/salla/not-found.tsv`):
- nf_id: Q3-SA-N01
- bears_on: 4
- what_is_missing: The length of the period (المهلة) after which payment and settlement operations (عمليات الدفع والسداد) of a store that is not verified are suspended, and when that period starts.
- kind: not in what was read
- read: observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl line 23 (article zbcnt9hu9kf8lfh2gmf1vccr), line 24 (article iparbtoxqor7rjnuhg9ppnrh), line 1346 (article evrib312myg7282hjg7nlrje), line 926 (article ig4b4l5hc542j4bcd2tp82bz), line 30 (article ndz1k0tts5p7gfnqqxcubspl); observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt; re-check 2026-10-19: observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T122729Z-sweep-merchant-menus-ar/steps/076.text.txt (https://s.salla.sa/payments/kyc, store merchant, not verified); observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T122729Z-sweep-merchant-menus-ar/responses/1722.json (wallet summary, step 72); observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261008T122729Z-sweep-merchant-menus-ar/responses/1683.json (gateways, step 71)
- searched: python3 -I method/corpus_search.py salla "مهلة التوثيق" "انتهاء المهلة" "مهلة لتوثيق" "verification deadline" "grace period" --max 10. Opened: help articles zbcnt9hu9kf8lfh2gmf1vccr and iparbtoxqor7rjnuhg9ppnrh (both say only "بعد انتهاء المهلة"). Not read: docs.salla.dev/partner-apis/app-snippet.md and html-js-migration.md (held and in evidence/product-class), and the three affiliate-agreement pages on salla.com (en-ae, en-sa, en-ae/policies); their snippets concern an app migration period and affiliate marketers.; re-check 2026-10-19: python3 -I method/corpus_search.py salla "المهلة" "مهلة" "توثيق المتجر" "grace period" "verify your store" --max 10. Opened the three run documents named in read; none states the period. The KYC schema answer of the same step (responses/1818.json) has no match for مهلة, grace, period or deadline.
- who_can: founder
- route: Question to Salla merchant support (dashboard help): how long the period (المهلة) is after which payment and settlement operations (عمليات الدفع والسداد) of a store that is not verified are suspended, and when it starts.
