# Notes: Q1 on Zid (checking run, R3)

## What was read

All held, from this repository's capture runs (commit 98f560e89dc72be24b539513a8a7e59f19d096b8), read 2026-10-19. No live page was read.

- Topic search (`"الأسواق" "سوق جديد" "market" "markets" "دولة المتجر" "store country" "العملات" "currencies" --max 10`): help.zid.sa/markets/, help.zid.sa/zidpay_staff_and_currencies/, help.zid.sa/store-language/, zid.sa/en/uae/ (raw page, searched by term), help.zid.sa/gcc-merchants/.
- Sentence [1]: docs.zid.sa/list-store-locations.md, help.zid.sa FAQ for sales channels (الأسئلة الشائعة لقنوات البيع), zid.sa/en/legal/global-shipping-terms/ (raw page), help.zid.sa/domain/ (searched by term).
- Sentence [2]: docs.zid.sa/retrieve-store-operating-countries.md, docs.zid.sa/localization-33664641e0.md.
- Sentence [3]: docs.zid.sa/list-store-delivery-options.md (searched by term), help.zid.sa/zid-wallet/, help.zid.sa/senderid/, help.zid.sa/faq-zid-warranty/, help.zid.sa/saudi-merchants/. Searched with `--with` for rows N03 and N04: help.zid.sa/activate-online-payments/, zid.sa/ar/legal/zidpay-terms-conditions-kw/ (raw page), zid.sa/ar/solutions/payments/ (raw page).
- Sentence [4]: help.zid.sa/about-zid-egypt/, zid.sa/ar/paymob/ (raw page), help.zid.sa FAQ (زد يخدم التجار في السعودية فقط؟ هل يخدم الخليج؟), zid.sa/en/syria/ (raw page).
- Sentence [5]: help.zid.sa/store-language/, help.zid.sa/markets/.

The text files of zid.sa/en/uae/, zid.sa/en/syria/, zid.sa/en/legal/global-shipping-terms/, zid.sa/ar/paymob/, zid.sa/ar/solutions/payments/ and zid.sa/ar/legal/zidpay-terms-conditions-kw/ hold only the error page. Their text was read in raw.html.

## What couldn't be read

- zid.sa/en/kuwait/ is not held.
- zid.sa/en/uae/ shows plans and partners only in page data. Nothing from it was recorded.
- The rows routed to the founder (N05, N07, N08, N12) name the dashboard page الاعدادات > الأسواق, which Zid's markets article names. No dashboard address is held (`held_index.py` reports https://dashboard.zid.sa/ and https://web.zid.sa/ as not held).

## Account points not checked

These points were left out of the not-found rows (17 recorded, under the cap of 20). They are not in `account.md`.

- Shopify [1]: store feature flags named for markets (Q1-SH-088).
- Shopify [3]: the `threeDSecureEligibilityForCountry` flag (Q1-SH-090).
- Salla [1]: the store app markets setting (Q1-SA-026); login options shared across markets (Q1-SA-064); the blog's statements (Q1-SA-104).
- Salla [3]: cash on delivery through Salla labels in the UAE (Q1-SA-K1589).
- Salla [4]: Markets and the Retail stores app; a market's subdomain needing the store domain (Q1-SA-025); separate stores per country (Q1-SA-102).
- BigCommerce [1]: `store_address_type` and `store_country` as global settings (Q1-BC-018); personal data regions (Q1-BC-K0438).
- BigCommerce [2]: channel attributes (Q1-BC-012); tax address basis and provider targeting (Q1-BC-127).
- BigCommerce [3]: Jurisdiction-Specific Terms (Q1-BC-142); basic tax (Q1-BC-133).
- BigCommerce [5]: transactional currencies that can't be created via API (Q1-BC-062).

Points resting only on N, G or H ids were not sorted against, as the brief says: Shopify [2] Q1-SH-G0132 and the others; Salla [2] Q1-SA-G0155 and Q1-SA-N02; Salla [3] Q1-SA-N01; BigCommerce [2] Q1-BC-G0140; BigCommerce [4] Q1-BC-N01; BigCommerce [5] Q1-BC-N02.

## Copies

- 18 concerns were copied, and 32 rows were set aside, S-01 among them.
- No copy was found wrong.
- The wallet article's "لتجار دول الخليج في حال رغبتك بنقل متجرك من دولة إلى دولة أخرى، يجب أولًا تصفير رصيد المحفظة." says what copy Q1-ZD-K0230 says. It was not recorded again.

## Problems with the method

- The brief caps `account.md` at about 800 words, not counting ids. The checker warns past 900 `\w+` words with ids removed, and counts the names of the points sorted against. Naming every point by platform, section and id took a large share of the length, so the points' text had to be cut short.
- Some Zid statements come from page data in raw.html, where quotes are escaped (Q1-ZD-026). The statement copies that text verbatim, backslashes included, because the checker reads the raw page as written.
