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
