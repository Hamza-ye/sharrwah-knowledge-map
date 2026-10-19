# Q1 on Salla: account

## [1]

- Salla names the per-place version of a store a market (سوق; the feature الأسواق المتعددة, "Markets"; in the API, Store Scopes). It describes it as customised copies of the store for each country, region or city it targets, which can be customised for any Gulf country or region in design, prices, currency, store domain and shipping options. Each copy is run separately, with its own stock and orders handled from the nearest branch. Q1-SA-K1976, Q1-SA-001, Q1-SA-002, Q1-SA-038, Q1-SA-039, Q1-SA-K1979, Q1-SA-K1980
- What a market holds: the countries it is shown to, a name, a default language and other languages (set separately for each market), whether it is shown, a default currency and other currencies, its branches and warehouses, four shipping settings, contact details, a subdomain, login and registration methods, and a store design. Q1-SA-004, Q1-SA-006, Q1-SA-007, Q1-SA-K1977, Q1-SA-008, Q1-SA-009, Q1-SA-010, Q1-SA-011, Q1-SA-012, Q1-SA-065, Q1-SA-066
- Further things that can be set per market: product prices (a custom price per market, or automatic pricing by exchange rate), with option prices edited only in the market pricing section; which markets a product is shown in, with a product hidden until a market is added to it; product order within categories; theme publication; domain redirection; how a customer picks a market (top bar, pop-up, or by IP address with no switching); restricting purchases to the market matching the customer's country; tax by market country, with one country per market; a VAT number linked to the market; maintenance mode; payment methods per market; product restrictions; which markets the store app shows. Q1-SA-019, Q1-SA-020, Q1-SA-048, Q1-SA-049, Q1-SA-K1958, Q1-SA-031, Q1-SA-029, Q1-SA-030, Q1-SA-050, Q1-SA-051, Q1-SA-015, Q1-SA-013, Q1-SA-021, Q1-SA-017, Q1-SA-054, Q1-SA-055, Q1-SA-022, Q1-SA-058, Q1-SA-059, Q1-SA-023, Q1-SA-056, Q1-SA-057, Q1-SA-024, Q1-SA-062, Q1-SA-063, Q1-SA-060, Q1-SA-033, Q1-SA-068, Q1-SA-069, Q1-SA-034, Q1-SA-052, Q1-SA-053
- The help centre says the feature is not shown to customers in the store app; the dashboard has a "Store app markets" setting. Q1-SA-026, Q1-SA-052, Q1-SA-053
- What stays the same across markets, as Salla shows it: login and registration options for all markets are managed in one place in the store settings; a market takes the main store's theme by default; maintenance mode for the whole store overrides a market's setting; the store-settings language setting applies only to the default market. Q1-SA-064, Q1-SA-012, Q1-SA-061, Q1-SA-016
- Orders can be filtered by market, and a staff role can be restricted by market. Q1-SA-027, Q1-SA-028
- Customers choose the market they buy from, and their displayed currency follows their location. Q1-SA-032, Q1-SA-K1956, Q1-SA-K1957
- Taxes: a tax record is created for the country sold to, and is used automatically when selling there. Q1-SA-K1924, Q1-SA-K1925, Q1-SA-K1931
- Salla's blog says capabilities differ by plan, market and coverage; that BNPL services differ in the currencies and markets they serve, by provider; and that rules, taxes, customs and product requirements differ between Gulf markets. Q1-SA-104, Q1-SA-101, Q1-SA-103

## [2]

- Markets are set in the dashboard under المزيد > الأسواق المتعددة (route /localization, with /localization/new and /localization/settings), and their settings under the الإعدادات tab, by the merchant. Q1-SA-004, Q1-SA-018, Q1-SA-037
- Activation runs through المنتجات > الأسواق المتعددة > فعل الآن > تأكيد. It is available on the Special plan, and the `multi-countries` flags show plan limits. Q1-SA-003, Q1-SA-K1978, Q1-SA-K1970, Q1-SA-K1971, Q1-SA-K1973, Q1-SA-K1975
- Shipping companies and couriers are set per country and city in the shipping settings; for stores outside Saudi Arabia these hold local and international shipping settings. Q1-SA-081, Q1-SA-082
- Copied gaps on Markets, currencies, countries and shipping zones stay open: Q1-SA-G0155, Q1-SA-G0157, Q1-SA-G0158, Q1-SA-G0149, Q1-SA-G0135. Where the automatic exchange rate comes from is not in what was read. Q1-SA-N02

## [3]

- Salla's sign-up asks for the store's country, which decides the government documents required, and for the legal entity. Store verification runs in AE, SA, KW, QA, OM and BH (`kyc_new_workflow`). Q1-SA-K1989, Q1-SA-K0088, Q1-SA-K1988, Q1-SA-070
- The UAE store guide asks about the regulatory requirements for selling in the UAE, to verify the store and receive payouts. Verification follows UAE requirements, carriers operating in the UAE are connected, and the help centre files UAE and Kuwait articles for verification, Salla Payments activation, payouts and the merchant's own carriers. Q1-SA-075, Q1-SA-080, Q1-SA-079, Q1-SA-076, Q1-SA-078, Q1-SA-K0090
- Payments and payouts differ by country. In the UAE: Visa, Mastercard and Apple Pay, payouts on Thursdays above 250 AED, and an account at a UAE bank in AED. In Kuwait: KNET as well, next-business-day payouts with a minimum of 1 KWD, and a Kuwaiti bank account in KWD. In Saudi Arabia, Salla Payments receives in SAR. Q1-SA-K1520, Q1-SA-K1521, Q1-SA-K1529, Q1-SA-K1547, Q1-SA-K1548, Q1-SA-K1564, Q1-SA-K1565, Q1-SA-K1963, Q1-SA-K1527, Q1-SA-073, Q1-SA-074
- Outside Saudi Arabia: Tamara and Tabby must be set up directly with the provider, Emkan is only in Saudi Arabia, Madfoo3 is SAR only, and Apple Pay comes with verification and the Tap gateway. Charity stores, the ZATCA app, the international shipping gateway, product restrictions and Markets itself are stated as available only in Saudi Arabia. Q1-SA-083, Q1-SA-084, Q1-SA-087, Q1-SA-085, Q1-SA-086, Q1-SA-K1936, Q1-SA-K1884, Q1-SA-035, Q1-SA-036
- Cash on delivery through Salla labels is "coming soon" in the UAE, and COD tracking in the wallet is not available for UAE stores. Q1-SA-K1589, Q1-SA-K1602
- Bank transfer can be unavailable for a store's country, and transaction limits are listed per country (Saudi Arabia, UAE, Kuwait, Qatar, Bahrain, Oman, other countries). Q1-SA-072, Q1-SA-071
- The usage agreement at salla.com/terms and at salla.com/ar-ae/terms names the same company, شركة تطبيق سلّة لتقنية المعلومات (CR 7011845513, Saudi Arabia). Both are governed by Saudi law, charge all fees in Saudi riyals, and subject fund transfers to the Saudi central bank's authority. No Kuwait version is held. Q1-SA-094, Q1-SA-095, Q1-SA-096, Q1-SA-097, Q1-SA-G0161, Q1-SA-G0213, Q1-SA-G0214
- Salla's site lists "مدعوم في: السعودية الامارات", and its GCC page offers infrastructure supporting currencies, local gateways and regional legislation. Q1-SA-099, Q1-SA-098, Q1-SA-100, Q1-SA-G0160
- No help article was read for stores based in Qatar, Oman or Bahrain. Q1-SA-N01, Q1-SA-G0162

## [4]

- Adding a market: + سوق جديد, enter the details, save, then switch on تفعيل السوق. The dashboard warns that the current market becomes the default market, that browsing and pricing change, and that disabling needs the account manager. Enabling the feature needs the account manager too. The default language cannot be changed after creation, and there is a limit on the number of stores. Q1-SA-005, Q1-SA-014, Q1-SA-040, Q1-SA-041, Q1-SA-042, Q1-SA-043, Q1-SA-044, Q1-SA-045, Q1-SA-046, Q1-SA-047, Q1-SA-K1973
- Markets cannot be activated while the Retail stores app is installed; the account manager removes it. A market's subdomain requires the store domain to be added in Salla first. Q1-SA-025, Q1-SA-067
- On Salla adding a place where it operates, its Kuwait guide says Salla goes from the Saudi market to Kuwait, and its site describes GCC expansion. Q1-SA-077, Q1-SA-098, Q1-SA-K1990, Q1-SA-K1987
- Salla's blog says a separate store per country is not necessarily needed, and points to Markets on the Special plan. Q1-SA-102

## [5]

- Adding a currency: مركز الإعدادات > عام > العملات, then set the current currency, enable available currencies, and add a new one. The default currency can be changed only while there are no customer orders. Q1-SA-091, Q1-SA-092, Q1-SA-K1955, Q1-SA-093
- Adding a payment provider: an external gateway is connected with credentials from the provider account, and payments are then collected through it instead of Salla Payments. Salla Payments cannot be activated while Tap is connected, and KNET via Tap requires Tap. Q1-SA-K1656, Q1-SA-K1655, Q1-SA-K1653, Q1-SA-K1654
- Tabby (UAE guide): connected under Payment Methods with merchant keys. Collection and settlement follow the merchant's agreement with Tabby, the setup supports SAR, AED and KWD, and the store must be verified and on Plus, Pro or Special. Q1-SA-088, Q1-SA-089, Q1-SA-090, Q1-SA-087
- Gateway and BNPL flags are tied to plans plus, pro and special. Q1-SA-K1640, Q1-SA-K1645, Q1-SA-K1617, Q1-SA-K1614
