# Notes: Q1 on Salla

## Selection
26 concerns copied, 3 added (SA-C-026, SA-C-064, SA-C-077), 44 set aside, including S-01. The copy made 422 statements and 43 gaps.

## What was read (held, observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3)
- Help map: categories (ar); category cv3bp6xkppnkt434yitce3ap (الأسواق المتعددة), f9tgx9usfvxntfgbbo7qet7g (متجر جديد), nlmrfbvrh4bdalrikuwpvai0 (الشحن).
- Help articles (ar): wv9wyqrnhwpm6m2rp3cmg653, epj429qolc9kuugn5gqroamo, rvmsx19zkex4wgybruk7ovii, n19t1045mpgtqluk409q2wom, gkq7zm64xnf29y8wew2r8x7h, huvvumstnafaadcw6abpol14, i8d4lq5xfx3sr05m59uwh64d, brz9k255mdsfjeuty7ojte37, d9me3k8vqi09hdiun8r2ngfr (market section), u4s3nz2yd3gxd92e8r4dpwbd.
- Help articles (en): canc11ysqehd3vnepmv9zqyp, f9bsa0insqb43sh6r41i4gfm, mwmsy60840mp73dpv7n0wd4s, era3k5had61w2de5zacmb82w (FAQ), vnmcb3lad5fiwd7xnrmbteql (note and FAQ), wmmkc305vzb52ka2al4zbfrh.
- Dashboard translations: en/localization.json (all keys), en/payments.json (keys on countries, markets and gcc_banner).
- salla.com: structures/salla/com-policies/terms/text.txt; the following fetch-archive records: https://salla.com/ar-ae/terms (com-toplevel offset 3700206), https://salla.com/gcc-ecommerce (com-toplevel offset 14913731), https://salla.com/ai-info (com-states offset 132790), https://salla.com/blog/expand-online-store-to-gcc (com-pages offset 34902179).
- Several of these are pages the copied gaps record as "held, and the run could not read it" (salla.com/terms, salla.com/ar-ae/terms, salla.com/gcc-ecommerce). They read without trouble through `warc_text.py` and the com-policies structure.

## Live pages
- https://salla.com/ar-kw/terms, tried 2026-10-18 with curl. It returned HTTP 403 with a bot challenge ("Just a moment..."), and was not read further. `held_index.py` reports it not held. No other live page was read.

## What could not be read
- No Kuwait version of the usage agreement is held (salla.com/ar-kw/terms, salla.com/en-kw/terms: not held; live: bot challenge). Copied gap Q1-SA-G0213 stays open for Kuwait.

## Observations on sources (as read, without inference)
- The Kuwait store guide (i8d4lq5xfx3sr05m59uwh64d, line 220) has the sentence "وضّح حالة متطلباتك النظامية للبيع في الإمارات, لتوثيق المتجر واستلام المستحقات.", the same sentence as the UAE guide. It was not recorded as a Kuwait statement.
- salla.com/blog/expand-online-store-to-gcc contains the line "ملاحظة للمحرر: لا تُنشر هذه المسودة قبل مراجعة قانونية أو تنظيمية متخصصة في السوق المستهدف" in its published text.
- The help article rvmsx19zkex4wgybruk7ovii says Markets is not shown in the store app. The dashboard translations have settings.active_mobile_scopes ("Store app markets"). Both are recorded (Q1-SA-026, Q1-SA-052, Q1-SA-053).
- f9bsa0insqb43sh6r41i4gfm (en) says "The multiple markets feature is currently available only in Saudi Arabia."

## Copies
- No copy was found wrong. No copy was reported changed.
- Q1-SA-001 records the list that follows Q1-SA-K1976, which the copy stops before.
- Q1-SA-091 records the steps before Q1-SA-K1955.

## Method problems
- The checker requires each statement to be verbatim in a cited source. Dashboard translation values from separate keys cannot be joined into one statement, so they are recorded one key per statement.

## Re-check against the observed runs, 19 October 2026

### What was read (observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3)
- Guides: `README.md`, `docs/READING.md`, whole. `index/rest-endpoints.tsv` (lines on onboarding, persona, countries, currencies and payments).
- Searches:
  - `python3 -I method/corpus_search.py salla "سعر الصرف" "أسعار الصرف" "exchange rate" "تسعير تلقائي" "التسعير التلقائي" --max 10`: no run document listed.
  - `python3 -I method/corpus_search.py salla "according to the current exchange rate" "حسب سعر الصرف الحالي" "Automatic pricing by exchange rate" "تسعير تلقائي حسب سعر الصرف" --max 10`: run documents listed were translation saved responses only.
  - `python3 -I method/held_index.py https://s.salla.sa/localization/settings` and `https://s.salla.sa/localization`: steps of journey-localization-demo and of sweeps.
  - `python3 -I method/corpus_search.py salla "قطر" "عُمان" "عمان" "البحرين" "Qatar" "Oman" "Bahrain" --with "توثيق" "verification" "دولة المتجر" "store country" "onboarding" --max 10`: listed a held help article for Qatar in fetch run 20261009T034955Z-help-sitemap-missing (ar offset 614025, en offset 3143695).
  - `python3 -I method/corpus_search.py salla "توثيق متجرك في عمان" "توثيق متجرك في عُمان" "توثيق متجرك في البحرين" "in Oman" "in Bahrain" "تفعيل مدفوعات سلة في قطر" --max 10`: nothing for Oman or Bahrain.
- Files: run 20261008T180430Z-journey-localization-demo (`run.json`, `actions.jsonl`, `responses.jsonl`, steps 002, 004, 006, 007 to 014, `responses/0140.json`, `responses/0160.json`); run 20261008T125139Z-sweep-merchant-routes-ar (`run.json`, `actions.jsonl`, `responses.jsonl`, steps 023 text and aria, `responses/0535.json`, `responses/0709.json`); run 20261008T122729Z-sweep-merchant-menus-ar (`run.json`, `actions.jsonl` step 71, `responses/1683.json`, GET /admin/v2/gateways/payment, the payments pointer); `raw/runs/20261009T034955Z-help-sitemap-missing/fetch.warc.gz` offset 614025 through `warc_text.py`.
- Store names: journey-localization-demo names its store `demo` and sweep-merchant-menus-ar `merchant` (`run.json` `extra.store`). sweep-merchant-routes-ar's `run.json` has no `extra`; Q1-SA-108 names the store from the same run's `/admin/v2/store/info` (`"id":60460195,"name":"Store 1"`, step 37, cited as Q1-SA-C161).

### Open items
- Q1-SA-N01: narrowed. The Qatar article closes the Qatar part (Q1-SA-110 to Q1-SA-113); the row now asks for Oman and Bahrain only.
- Q1-SA-N02: narrowed, still routed to the founder. The page the old route asked for is held (journey-localization-demo step 8) and recorded (Q1-SA-105, Q1-SA-106). It says only "according to the current exchange rate"; its saved answer (`/admin/v2/settings/fields/scopes.product_prices`) was `{"type":true}`. The route is now a question to Salla on the rate's source.
- Copied gap Q1-SA-G0162: Q1-SA-108 shows part of it (the step where the country is chosen, and its options). It stays open, and the account still cites it.
- Copied gaps Q1-SA-G0135, G0149, G0155, G0158, G0161, G0213, G0214 (clauses of the usage agreement), G0157 (who maintains the countries lists) and G0160 (the page listing countries served): unchanged. The runs hold steps and answers, and none of the documents read shows these.
- Phrase "تسعير تلقائي حسب سعر الصرف" (Q1-SA-N02): not in the files N02 had read. It is in the run's saved response `responses/0140.json`, now in N02's `read` and recorded as Q1-SA-106, so it stays.

### Wording changes
- Q1-SA-N01: "Qatar, Oman or Bahrain" became "Oman or Bahrain", and the Qatar article's title (توثيق متجرك في قطر | سلة) was added as read. The route names عمان and البحرين only.
- Q1-SA-N02: the sentence on what the panel shows was added; the route changed (above). Every name kept in both rows is in what their `read` names or in this folder's records (the article titles in Q1-SA-077 and the copies; the English label in en/localization.json and in step 8).

### New statements
- Q1-SA-105 to Q1-SA-113 (9), citations Q1-SA-C157 to Q1-SA-C166.

### Not read
- The English Qatar article (help-sitemap-missing offset 3143695); the Qatar articles it links (Salla Payments activation, transfers, carriers); `/admin/v2/onboarding/create-store` (`responses/0576.json`); `/admin/v2/settings-center/settings/general/currencies` and `/admin/v2/currencies` answers; the real-merchant sweeps' /localization step (20261012T010906Z-sweep-real-merchant-full-en step 232).

### Problems
- A saved response escapes Arabic as `\uXXXX` (e.g. `responses/0535.json`), so its Arabic values can't be quoted as Salla shows them; Q1-SA-108 is quoted from the step's page text instead.
- The held Qatar article is in a fetch run (20261009T034955Z-help-sitemap-missing), not in `structures/salla/help-articles`.
