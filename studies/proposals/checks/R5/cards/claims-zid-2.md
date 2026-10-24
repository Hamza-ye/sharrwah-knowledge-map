# Cards: what the proposals cite as not found or absent, on zid

6 records, from Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8.

## The points cited

- **Q5, section 1, line 43:** - Who holds it in between, matching by role: Shopify's merchant opens "financial accounts and/or cryptocurrency wallets with one or more Payment Processors"; Stripe, as the merchant's agent, holds WooPayments' funds "in one or more Pooled Accounts at one or more Financial Providers"; BigCommerce Payments' transactions "flow through your new BigCommerce Payments account" (stated). For Salla and Zid, the entity, licence or account under which the balance is held was not in what was read. Q5-SH-P0010, Q5-WC-P0121, Q5-BC-P0052, Q5-SA-H0002, Q5-ZD-H0002
- **Q5, section 5, line 128:** - Whether any held route goes live, and who would hold the money: Sharrwah, or a payment company in an account opened through Sharrwah. The design keeps the route on every payment and the balance as its own part, so no order or checkout code assumes a balance. The founder's decision under the guard settles it. Q5-SA-H0002, Q5-ZD-H0002, Q5-WC-P0121
- **Q5, section 6, line 143:** - The international services behind the platforms are closed to Yemen, which forbids them on Yemen's lists as of 2026-10-10: Stripe is unavailable, WooPayments not available (a request to add it is open), and a PayPal account in Yemen cannot receive money. WooPayments for businesses outside its listed countries, and زد باي outside Saudi Arabia and Kuwait, are absent. YA-62 (Unavailable @ Stripe's service, as of 2026-10-10), YA-62 (Not available, a request to add it open @ WooPayments's service, as of 2026-10-10), YK-514 (cannot receive money @ PayPal's service, as of 2026-10-10), Q5-WC-A0002, Q5-ZD-A0002
- **Q5, section 7, line 159:** - Whether Sharrwah offers a payment service of its own in which sellers' money is held, by Sharrwah or by a payment company in an account opened through Sharrwah, and with which company: for the founder, under the guard. Q5-SH-K1555, Q5-WC-P0121, Q5-BC-P0069, Q5-SA-H0002, Q5-ZD-H0002
- **Q5, section 8, line 173:** - Records: Shopify's financial services provider, Stripe's pooled accounts and BigCommerce Payments' account hold it; Salla's (UAE help) and Zid's balances hold sales proceeds before payout, but who holds either balance was not in what was read; a connected gateway pays the merchant's own account. S01-VP-01, Q5-SH-P0033, Q5-WC-P0121, Q5-BC-P0052, Q5-SA-P0057, Q5-ZD-P0035, Q5-SA-H0002, Q5-ZD-H0002, Q5-BC-P0089
- **Q7, section 1, line 23:** - The pages read don't name the currency of Zid Pay's deposits to the seller's bank account (not checked on BigCommerce). Q7-ZD-N02
- **Q7, section 1, line 52:** - Zid: Zid Pay may add the amount due to the merchant's balance, "إضافة المبلغ المستحق لرصيد التاجر"; the pages read don't name that balance's currency (not checked on BigCommerce). For cash on delivery through its shipping service, Zid collects from buyers and transfers "إجمالي المستحقات إلى محفظة التاجر". Its terms say the wallet is "محددة بالريال السعودي كعملة أساسية" for merchants outside Saudi Arabia, while Gulf merchants use it "بالعملة المحلية لبلدهم". Q7-ZD-K0033 Q7-ZD-N01 Q7-ZD-K0117 Q7-ZD-P0122
- **Q7, section 8, line 159:** - What the records show: Shopify and WooCommerce define the payout currency in the same terms, and BigCommerce's settlement currency matches it on role (basis 4). It is set for the payment account: by region or business entity on Shopify, with more currencies on some plans; by country on WooCommerce; through the provider on BigCommerce; by the country's banks on Salla. Balances before payout are kept per currency on Shopify, WooCommerce and BigCommerce. Salla's balance holds sales proceeds before transfer; the page naming its currency wasn't read, and the run on store real-merchant gave the store's wallets in SAR (12 October 2026, observed). Zid's terms set its wallet's currency by the merchant's country; the currency of Zid Pay's balance and deposits, and of Shopify's reserved funds, wasn't in what was read. S01-VP-23 Q7-SH-004 Q7-WC-004 Q7-BC-P0014 Q7-SH-012 Q7-SH-K1268 Q7-SH-P0155 Q7-WC-K0739 Q7-BC-P0016 Q7-SA-K1964 Q7-SH-131 Q7-WC-048 Q7-BC-058 Q7-SA-K1560 Q7-SA-G0151 Q7-SA-022 Q7-ZD-P0122 Q7-ZD-N01 Q7-ZD-N02 Q7-SH-N01
- **Q8, section 1, line 23:** - Named conditions of this kind were not in what was read on Zid or BigCommerce. Q8-ZD-N03; Q8-BC-N05
- **Q8, section 1, line 32:** - Zid's embedded apps open in the dashboard "through an iframe"; places an app can add to beyond that were not in what was read. Q8-ZD-K0388; Q8-ZD-N12
- **Q8, section 2, line 109:** - Alternative not taken: embedding a whole app as the only point, as in Zid's iframe (other places were not in what was read); checkout and server additions need points of their own. Q8-ZD-K0388; Q8-ZD-N12

## The cards

### Q5-ZD-H0002

**Cited at:** Q5, section 1, line 43; Q5, section 5, line 128; Q5, section 7, line 159; Q5, section 8, line 173

**Record** (`studies/proposals/records/Q5/zid/copied-pilot-gaps.tsv`):
- gap_id: S01-ZD-G01
- bullet: b
- what_is_missing: The name and licence of the payment service provider (مزود الخدمة; مقدمي خدمات الدفع) under whose account or licence the merchant's Zid Pay balance (رصيد حسابك في زد باي) is held between the buyer's payment and the deposit, in Saudi Arabia and in Kuwait. The pages read speak of مزود الخدمة without naming it.
- read: https://zid.sa/ar/legal/zidpay-terms-conditions-sa/ (read 2026-10-12); https://zid.sa/en/legal/zidpay-terms-conditions-sa/ (read 2026-10-12); https://zid.sa/ar/legal/zidpay-terms-conditions-kw/ (read 2026-10-12); https://zid.sa/en/legal/zidpay-terms-conditions-kw/ (read 2026-10-12); https://zid.sa/ar/legal/terms-conditions/ (read 2026-10-12); https://zid.sa/en/legal/terms-conditions/ (read 2026-10-12); https://zid.sa/en/solutions/payments/ (read 2026-10-12); https://zid.sa/ar/solutions/payments/ (read 2026-10-12); https://help.zid.sa/about_zidpay/ (read 2026-10-12); https://help.zid.sa/deposits_zidpay/ (read 2026-10-12); https://help.zid.sa/activate-online-payments/ (read 2026-10-12); https://help.zid.sa/payment-requirements/ (read 2026-10-12); https://help.zid.sa/nafath_verification/ (read 2026-10-12); https://docs.zid.sa/overview-1340225m0.md (read 2026-10-12); https://docs.zid.sa/merchant-activation.md (read 2026-10-12)
- gap_kind: observation needed
- who_can: founder
- route: Zid Pay activation in a store dashboard, https://web.zid.sa/ (المدفوعات > تفعيل الدفع الالكتروني; the Nafath request, stated to be باسم مزود الخدمة; the separate terms reached at activation), not held; or a question to Zid

### Q5-ZD-A0002

**Cited at:** Q5, section 6, line 143

**Record** (`studies/proposals/records/Q5/zid/copied-pilot-absences.tsv`):
- absence_id: S01-ZD-N01
- bullet: e
- what_is_absent: Any country other than المملكة العربية السعودية and دولة الكويت, for مدفوعات زد (زد باي)
- list_cite_ids: S01-ZD-C280
- complete_cite_ids: S01-ZD-C280
- note: The list and the word فقط are in the same answer to هل تتوفر هذه الخدمة في دول الخليج؟ (S01-ZD-113), held in the page's embedded data.

**Citation S01-ZD-C280 (the list):** `https://zid.sa/ar/solutions/payments/` | لأننا نعرف أنك تحب تستكشف، هل تتوفر هذه الخدمة في دول الخليج؟ (answer held in the page's embedded data) | 2026-10-12 | kind: stated | quote check: found
- quote: تتوفر حاليًا في المملكة العربية السعودية ودولة الكويت فقط.
- title: حلول الدفع وسائل دفع إلكتروني سهلة وآمنة لمتجرك | زد
- in context: …\":\"ما هي البنوك المدعومة؟\",\"answer\":\"جميع البنوك في المملكة العربية السعودية.\\n\",\"languages_id\":{\"name\":\"ar\"}}]}},{\"id\":33,\"questions_id\":{\"id\":\"d33ba529-3854-4bc0-a147-f9dd662be86b\",\"translations\":[{\"id\":58,\"question\":\"Is this available across the GCC?\",\"answer\":\"Currently in Saudi Arabia and Kuwait.\",\"languages_id\":{\"name\":\"en\"}},{\"id\":59,\"question\":\"هل تتوفر هذه الخدمة في دول الخليج؟\",\"answer\":\"⟪تتوفر حاليًا في المملكة العربية السعودية ودولة الكويت فقط.⟫\\n\",\"languages_id\":{\"name\":\"ar\"}}]}},{\"id\":34,\"questions_id\":{\"id\":\"6a199de4-585e-4c29-b49f-d51cce133fa8\",\"translations\":[{\"id\":60,\"question\":\"What's the max fee for Mada?\",\"answer\":\"200 SAR (excluding VAT).\",\"languages_id\":{\"name\":\"en\"}},{\"id\":61,\"question\":\"ماهو الحد الأقصى لنسبة رسوم شبكة الدفع مدى؟\",\"answer\":\"الحد الأقصى لنسبة رسوم شبكة الدفع مدى هو 200 ريال. (غير شاملة لضريبة القيمة المضافة)\\n\",\"…

**Citation S01-ZD-C280 (the list):** `https://zid.sa/ar/solutions/payments/` | لأننا نعرف أنك تحب تستكشف، هل تتوفر هذه الخدمة في دول الخليج؟ (answer held in the page's embedded data) | 2026-10-12 | kind: stated | quote check: found
- quote: تتوفر حاليًا في المملكة العربية السعودية ودولة الكويت فقط.
- title, opening and note boxes: as for this source's citation above
- in context: …\":\"ما هي البنوك المدعومة؟\",\"answer\":\"جميع البنوك في المملكة العربية السعودية.\\n\",\"languages_id\":{\"name\":\"ar\"}}]}},{\"id\":33,\"questions_id\":{\"id\":\"d33ba529-3854-4bc0-a147-f9dd662be86b\",\"translations\":[{\"id\":58,\"question\":\"Is this available across the GCC?\",\"answer\":\"Currently in Saudi Arabia and Kuwait.\",\"languages_id\":{\"name\":\"en\"}},{\"id\":59,\"question\":\"هل تتوفر هذه الخدمة في دول الخليج؟\",\"answer\":\"⟪تتوفر حاليًا في المملكة العربية السعودية ودولة الكويت فقط.⟫\\n\",\"languages_id\":{\"name\":\"ar\"}}]}},{\"id\":34,\"questions_id\":{\"id\":\"6a199de4-585e-4c29-b49f-d51cce133fa8\",\"translations\":[{\"id\":60,\"question\":\"What's the max fee for Mada?\",\"answer\":\"200 SAR (excluding VAT).\",\"languages_id\":{\"name\":\"en\"}},{\"id\":61,\"question\":\"ماهو الحد الأقصى لنسبة رسوم شبكة الدفع مدى؟\",\"answer\":\"الحد الأقصى لنسبة رسوم شبكة الدفع مدى هو 200 ريال. (غير شاملة لضريبة القيمة المضافة)\\n\",\"…

### Q7-ZD-N02

**Cited at:** Q7, section 1, line 23; Q7, section 8, line 159

**Record** (`studies/proposals/records/Q7/zid/not-found.tsv`):
- nf_id: Q7-ZD-N02
- bears_on: 1
- what_is_missing: The currency in which Zid Pay deposits (الإيداعات) are paid into the seller's bank account, named as a currency rather than as the amounts of the minimum and fee
- kind: not in what was read
- read: https://help.zid.sa/deposits_zidpay/ (held sharrwah-knowledge-map@2677850336579cbaf596be177c40a97a832bb60c:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/110-help.zid.sa/text.txt); https://zid.sa/ar/legal/zidpay-terms-conditions-sa/ and -kw/ (held raw pages 189 and 188); https://help.zid.sa/store-language/ (held sharrwah-knowledge-map@2677850336579cbaf596be177c40a97a832bb60c:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/159-help.zid.sa/text.txt), all read 2026-10-19
- searched: python3 -I method/corpus_search.py zid "إيداع المبالغ" "الإيداع" "deposit" --with "عملة" "العملة" "currency" --max 10 (14 documents; opened help.zid.sa/store-language/, help.zid.sa/markets/, help.zid.sa/transactions/, help.zid.sa/refund-requests/ (currency line), docs.zid.sa/get-manager-profile.md (balance and currency fields); not read: help.zid.sa/abandonment-cart/, help.zid.sa/customer-wallet/, help.zid.sa/payment-links/, help.zid.sa/senderid/, zid.sa/ar/legal/terms-conditions/ and the 4 not listed)
- who_can: either
- route: Ask Zid; or read the held pages again after a new capture

### Q7-ZD-N01

**Cited at:** Q7, section 1, line 52; Q7, section 8, line 159

**Record** (`studies/proposals/records/Q7/zid/not-found.tsv`):
- nf_id: Q7-ZD-N01
- bears_on: 4
- what_is_missing: The currency in which the balance in Zid Pay (رصيد حسابك في زد باي; رصيد قيد المعالجة; لم يتم الإيداع) is held before deposit
- kind: not in what was read
- read: https://help.zid.sa/deposits_zidpay/ (held sharrwah-knowledge-map@2677850336579cbaf596be177c40a97a832bb60c:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/110-help.zid.sa/text.txt); https://zid.sa/ar/legal/zidpay-terms-conditions-sa/ (held sharrwah-knowledge-map@2677850336579cbaf596be177c40a97a832bb60c:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html); https://zid.sa/ar/legal/zidpay-terms-conditions-kw/ (held sharrwah-knowledge-map@2677850336579cbaf596be177c40a97a832bb60c:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/raw.html); https://help.zid.sa/transactions/ (held sharrwah-knowledge-map@2677850336579cbaf596be177c40a97a832bb60c:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/166-help.zid.sa/text.txt), all read 2026-10-19
- searched: python3 -I method/corpus_search.py zid "رصيد حسابك في زد باي" "رصيد التاجر" "رصيد قيد المعالجة" --with "عملة" "بالريال" "بالدينار" "currency" --max 10 (4 documents: help.zid.sa/refund-requests/, zid.sa/ar/legal/terms-conditions/, zid.sa/ar/legal/zidpay-terms-conditions-kw/, zid.sa/ar/legal/zidpay-terms-conditions-sa/; opened the two Zid Pay terms and help.zid.sa/refund-requests/ (its currency line only); zid.sa/ar/legal/terms-conditions/ not read for this row)
- who_can: either
- route: Ask Zid; or read the held pages again after a new capture

### Q8-ZD-N03

**Cited at:** Q8, section 1, line 23

**Record** (`studies/proposals/records/Q8/zid/not-found.tsv`):
- nf_id: Q8-ZD-N03
- bears_on: 2
- what_is_missing: Named store-level conditions that switch platform features on for a store, beyond the plan comparison
- kind: not in what was read
- read: sharrwah-knowledge-map@8d4e787a826d283fd28735114b60e0a2932a5092:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/201-zid.sa/text.txt (https://zid.sa/llms.txt); sharrwah-knowledge-map@8d4e787a826d283fd28735114b60e0a2932a5092:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/161-help.zid.sa/text.txt (https://help.zid.sa/subscription/); sharrwah-knowledge-map@8d4e787a826d283fd28735114b60e0a2932a5092:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/018-docs.zid.sa/text.txt (https://docs.zid.sa/create-first-app.md); sharrwah-knowledge-map@8d4e787a826d283fd28735114b60e0a2932a5092:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/197-zid.sa/raw.html (https://zid.sa/en/pricing/); sharrwah-knowledge-map@8d4e787a826d283fd28735114b60e0a2932a5092:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/073-help-partner.zid.sa/text.txt; sharrwah-knowledge-map@3ca083a8f87c7640ac650906132caf20a3b42697:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/010-docs.zid.sa/text.txt (https://docs.zid.sa/authorization.md); https://changelog.partner.zid.sa/ read 2026-10-19; https://changelog.zid.sa/ar read 2026-10-19; https://zid.sa/en/enterprise/ read 2026-10-19
- searched: python3 -I method/corpus_search.py zid "الطرف المتعاقد" "ميزات جديدة" "تحديثات" "شارة" "موثق" "contracting" "organization" "organizations" "extension" "extensions" "SDK" "version" "versions" "compatibility" "compatible" "release" "releases" "new features" "new feature" "entitlement" "entitlements" "verified" --max 10 (opened docs.zid.sa/authorization.md, and from the zid.sa/ar/paymob/ footer link changelog.zid.sa/ar live; the other listed documents, OpenAPI version headers or footers by snippet, not read)
- who_can: agent

### Q8-ZD-N12

**Cited at:** Q8, section 1, line 32; Q8, section 2, line 109

**Record** (`studies/proposals/records/Q8/zid/not-found.tsv`):
- nf_id: Q8-ZD-N12
- bears_on: 2
- what_is_missing: A list of the places in the dashboard, checkout or storefront that an app can add to, other than embedding the whole app
- kind: not in what was read
- read: sharrwah-knowledge-map@8d4e787a826d283fd28735114b60e0a2932a5092:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/201-zid.sa/text.txt (https://zid.sa/llms.txt); sharrwah-knowledge-map@8d4e787a826d283fd28735114b60e0a2932a5092:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/161-help.zid.sa/text.txt (https://help.zid.sa/subscription/); sharrwah-knowledge-map@8d4e787a826d283fd28735114b60e0a2932a5092:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/018-docs.zid.sa/text.txt (https://docs.zid.sa/create-first-app.md); sharrwah-knowledge-map@8d4e787a826d283fd28735114b60e0a2932a5092:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/197-zid.sa/raw.html (https://zid.sa/en/pricing/); sharrwah-knowledge-map@8d4e787a826d283fd28735114b60e0a2932a5092:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/073-help-partner.zid.sa/text.txt; sharrwah-knowledge-map@3ca083a8f87c7640ac650906132caf20a3b42697:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/010-docs.zid.sa/text.txt (https://docs.zid.sa/authorization.md); https://changelog.partner.zid.sa/ read 2026-10-19; https://changelog.zid.sa/ar read 2026-10-19; https://zid.sa/en/enterprise/ read 2026-10-19
- searched: python3 -I method/corpus_search.py zid "الطرف المتعاقد" "ميزات جديدة" "تحديثات" "شارة" "موثق" "contracting" "organization" "organizations" "extension" "extensions" "SDK" "version" "versions" "compatibility" "compatible" "release" "releases" "new features" "new feature" "entitlement" "entitlements" "verified" --max 10 (opened docs.zid.sa/authorization.md, and from the zid.sa/ar/paymob/ footer link changelog.zid.sa/ar live; the other listed documents, OpenAPI version headers or footers by snippet, not read)
- who_can: agent
