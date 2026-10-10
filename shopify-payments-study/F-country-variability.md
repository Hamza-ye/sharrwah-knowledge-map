# F — What varies between markets in Shopify Payments (per-country pages)

Reader F. Slice: Shopify Payments per-country pages. 40 countries, 167 files.

**Path abbreviations** (all paths are relative to the corpus root):
- `SC/` = `help/manual/payments/shopify-payments/supported-countries/`
- `SP/` = `help/manual/payments/shopify-payments/`

**Method.** I read every file for UAE, Japan, Mexico, US, Singapore and Hong Kong in full. I also read Germany, France, Canada, Australia, UK, NZ, Portugal and Slovenia payment pages, and the payout and requirements pages for Germany, Romania, Sweden and Switzerland in part or in full. For the other countries I tabulated the pages with a script (card brands, local methods, POS, settlement, minimum payout, payout currencies, bank rails, business types, liveness, keywords), then checked the results with greps and spot reads. Cross-references: `SP/payouts/payout-timing.md`, `SP/payouts/pay-periods-and-fees.md`, `SP/payouts/reserves.md`, `SP/store-currency/supported-payout-currencies.md`, `SP/store-currency/payouts-in-multiple-currencies.md`, `SP/configuring-shopify-payments.md`, and briefly `SP/local-payment-methods/{mb-way,multibanco}.md`.

---

## 0. Headlines

1. **Every country page has the same structure:** requirements, payment methods and payouts, plus optional tax-reporting, PayPal and bank-connection pages. Most sentences are the same text with the country name swapped in. What changes between countries is a fairly small set of values. Each value is keyed on more than the merchant's country: often on the pair (country, currency), the triple (method, customer country, currency), (country, plan), (business type), or the merchant's risk state.
2. **Accepting a payment method depends on the *customer's* location and currency, not only the merchant's.** A merchant country enables a set of methods. Each method then applies only to buyers in particular countries paying in particular currencies (`SC/*/payment-methods.md`, the "Customer location" tables).
3. **Settlement and payout have a fixed shape with per-market numbers.** The shape: capture time stamped in UTC, then a settlement delay in business days, then the payout balance, a minimum-payout threshold, the payout schedule, and the payout to an account on a named domestic payment rail. The numbers vary by market, and settlement also tightens or relaxes with risk.
4. **Onboarding (KYC/KYB) varies more than anything else.** It changes the business-type taxonomy, the registry identifier, the accepted documents and how fresh they must be, residency rules, script and name rules, liveness checks, and statutory deadlines.
5. **Tax obligations come in three different kinds.** (a) Information reporting on the merchant's gross sales (US 1099-K). (b) Indirect tax on the processor's *fees* (GST/VAT). (c) Merchant-facing statutory disclosures (Japan's Specified Commercial Transactions Act). None of the three is mentioned on the UAE pages.

---

## 1. Dimensions of variation

### 1.1 Card brands (and how a brand is tied to currency)

- **Baseline:** Visa and Mastercard are accepted everywhere. American Express is listed for every market except UAE (Visa, Mastercard, Maestro only: `SC/united-arab-emirates/payment-methods.md`) and Mexico. In Mexico, Amex must be switched on manually and works **only when the buyer pays in MXN**. Otherwise "their transaction fails" (`SC/mexico/payment-methods.md`).
- **Domestic and regional schemes:**
  - JCB in Japan works only in JPY ("limited to domestic customers in Japan"). Each application is reviewed manually and activation can take up to 3 weeks. Accepting JCB also enables Discover and Diners Club (`SC/japan/payment-methods.md`).
  - Cartes Bancaires in France (`SC/france/payment-methods.md`).
  - Maestro is listed in 16 markets, mostly in Europe, plus UAE.
  - UnionPay is listed in most markets but not CA (enabled through Discover), FR, JP, UAE or US.
  - Canada: accepting Discover also enables UnionPay, and accepting Amex also enables JCB (`SC/canada/payment-methods.md`).
  - Debit schemes in POS only: EFTPOS in Australia (all EFTPOS cards) and New Zealand (only when co-branded with Visa or Mastercard); Interac in Canada.
- **Brand eligibility gated by vertical:** US HSA/FSA cards require ≥90% of sales to be medical products in IRS-approved categories, plus a manual review (`SC/united-states/payment-methods.md`).

### 1.2 Wallets

- Apple Pay, Google Pay and Shop Pay are switched on automatically everywhere, **except that Google Pay isn't available to merchants in France** (`SC/france/payment-methods.md`).
- **PayPal as a wallet inside Shopify Payments** exists only in the US and France (`SC/united-states/paypal-wallet.md`, `SC/france/paypal-wallet.md`):
  - PayPal can then no longer be added as an "additional" method. Its refunds, disputes, reports and payouts all move into Shopify.
  - Disputed transactions can be refunded only in full, after a 20-day inquiry window, with no appeal.
  - Settlement is pinned per market: always USD in the US (`SC/united-states/payouts.md`); in France, non-EUR transactions are excluded from multi-currency payouts (`SC/france/payouts.md`).
  - In the US, Venmo comes bundled with PayPal Wallet.

### 1.3 Local (alternative) methods

- **19 distinct methods** appear across the 40 countries: Bancontact, BLIK, EPS, iDEAL | Wero, Klarna, MB WAY, Multibanco, MobilePay, Przelewy24, Satispay, Swish, TWINT, OXXO, Meses sin intereses, GrabPay, Alipay, WeChat Pay, plus USDC listed separately. **UAE has none.**
- **Two keys decide whether a method appears.** The merchant's country decides whether the method can be switched on at all. The customer's location (and often currency) decides whether it shows at checkout. Examples:
  - MB WAY: customers in Portugal, paying in EUR, with their registered phone number.
  - TWINT: customers in Switzerland paying in CHF.
  - MobilePay: customers in Denmark or Finland, choosing DKK, EUR, NOK or SEK.
  - EPS: customers in Austria paying in EUR.
  - GrabPay: customers in Singapore paying in SGD; early access only.
  - Alipay and WeChat Pay: customers in "any country", for Hong Kong merchants.
- **Gates on the merchant side:**
  - iDEAL | Wero needs ≥100 Shopify Payments orders in most markets. From Mexico it also needs the Netherlands set up as an active market.
  - Swish is available only on the Shopify Plus plan (`SC/sweden/payment-methods.md`).
  - OXXO requires a merchant located in Mexico, a buyer in Mexico paying MXN, and an amount of 10–10,000 MXN.
- **Different ways of confirming a payment, stated or nearly stated in the slice:**
  - *Push approval:* MB WAY. The buyer approves in an app, within 4 minutes according to `SP/local-payment-methods/mb-way.md`. Capture is automatic and manual capture isn't supported.
  - *Pay later against a reference:* Multibanco and OXXO. The order shows "Payment pending" for up to 7 days and is then cancelled. Multibanco allows no chargebacks. Maximum amounts differ: €5,000 for MB WAY versus €99,999 for Multibanco (`SC/portugal/payment-methods.md`). The Multibanco page says payment is "authorized" when the order is placed, but "funds aren't guaranteed". The merchant chooses whether to fulfil before the funds arrive (`SP/local-payment-methods/multibanco.md`).
  - Portugal's requirements page warns that Multibanco and Klarna "can leave orders in a pending state" (`SC/portugal/requirements.md`).
- **USDC (stablecoin)** is listed in 27 countries. In the US it is excluded for merchants in Arkansas, New York, Pennsylvania and Texas, so availability can depend on a *region within a country* (`SC/united-states/payment-methods.md`). Credits go either to payouts or to a separate USDC balance.

### 1.4 BNPL and instalments

- **Klarna** is listed for 26 merchant countries in Europe plus the UK. It isn't listed for BG, HU, LI or RO, or for any non-European market. Buyers can be in 19 countries and pay in 8 currencies. Klarna is switched off by default in some markets (`SC/croatia/payment-methods.md`, `SC/slovenia/payment-methods.md`).
- **Klarna has its own dispute rules** (`SC/slovenia/payment-methods.md`):
  - The buyer has 180 days to open an inquiry, and an unresolved inquiry becomes a dispute after 13 days.
  - Evidence is submitted once, and Klarna decides within about a month.
  - The buyer can still file a bank chargeback, which follows the card process instead.
- **Meses sin intereses** (Mexico) is interest-free monthly instalments, only for credit cards in MXN (`SC/mexico/payment-methods.md`).
- Shop Pay Installments appears only in the US 1099-K page, where its negative balances or holds can make the 1099-K export disagree with the form.
- UAE, Japan, Hong Kong, Singapore, Canada, Australia and New Zealand list no BNPL in this slice.

### 1.5 Currency the buyer pays in

- Every payouts page has the same sentence: the buyer's currency can differ from the payout currency.
- Conversion happens at capture. Refunds use the current rate and carry no conversion fee (`SP/store-currency/supported-payout-currencies.md`).
- What varies is **which currencies each method allows** (JCB JPY, Amex-MX MXN, MSI MXN, OXXO MXN, TWINT CHF, MB WAY EUR…). Allowed presentment currency is therefore a property of each method, not of the market.

### 1.6 Payout currency and multi-currency payouts

- **Domestic payout currency:** usually one, but **9 markets have two domestic currencies.** These are CZ (CZK/EUR), DK (DKK/EUR), HU (HUF/EUR), LI and CH (CHF/EUR), NO (NOK/EUR), PL (PLN/EUR), RO (RON/EUR) and SE (SEK/EUR). In each case EUR is also domestic and carries no multi-currency payout fee (`SP/store-currency/supported-payout-currencies.md`, `SC/romania/payouts.md`).
- **Which plans can receive payouts in several currencies:**
  - Advanced or Plus in most markets.
  - **UAE: Plus only** (`SC/united-arab-emirates/payouts.md`).
  - Japan and Mexico: not available.
  - Canada on Basic or Grow can make USD the default payout currency, for a 1.5% fee (`SP/store-currency/payouts-in-multiple-currencies.md`).
  - US: USD is always the default and can't be changed. AUD, CAD, EUR and GBP are secondary only.
- **Where the bank account may be, per payout currency:**
  - Singapore, Hong Kong and UAE require every payout account, *including foreign-currency ones*, to be held with a domestic bank.
  - EU and UK merchants can use any listed SEPA country.
  - US merchants must use a bank in the currency's own region for AUD, CAD, EUR and GBP. EUR IBANs from Monaco, San Marino, Andorra and the Vatican are rejected.
  - Australia lists bank locations per currency, for example EUR in 22 countries.
- **Available currency lists:** AED+USD (UAE); SGD, HKD and JPY markets each get USD, EUR, GBP and JPY (5 currencies); about 17 for EU and UK; AUD + 12 for Australia; USD only for Canada.
- **How fees work** is the same everywhere: payouts in the domestic currency are free, and non-domestic payouts pay a fee that depends on plan and region. The fee is "based on the payout currency, not whether a currency conversion occurs" (`SP/store-currency/payouts-in-multiple-currencies.md`). Orders in a currency with no matching payout account go to the default account.

### 1.7 Settlement time and payout schedule

- **Minimum settlement time:**
  - 2 business days: Australia, and Austria according to `SC/austria/payouts.md`. `SP/payouts/payout-timing.md` says 3 for Austria, which is an inconsistency.
  - 3: most of the EU, UK, US, Canada and NZ.
  - 4: Hong Kong and Singapore.
  - 5: UAE and Japan.
  - 7: Mexico.
- **New merchants start slower:** "When you begin receiving payouts, your settlement time is longer, but as you reliably fulfill orders on time, your settlement time can decrease" (the same sentence on every page). Higher-risk accounts can get "custom payout schedules" of 5–20 business days (`SP/payouts/payout-timing.md`). Settlement time therefore depends on (market, risk, method). ACH direct debit takes up to 4 business days to settle.
- **Schedule:**
  - Daily, weekly or monthly in most markets.
  - **Japan: weekly or monthly only**, on a chosen weekday, with no daily payouts. Settlement = "5 days plus the number of days remaining until your payout day" (`SC/japan/payouts.md`).
  - No payouts on weekends or public holidays (stated for CA, FR, DE and SG). Changing the schedule delays pending payouts.
- **Calendar rules that never change:** captures are stamped in UTC, and Fri/Sat/Sun captures are combined into one payout. This text is identical everywhere, **UAE included** (`SC/united-arab-emirates/payouts.md`).
- **Several processors:** in the US and France, payments go through "multiple payment processing partners". A merchant can receive more than one payout a day, sometimes earlier than scheduled. In France the bank statement may show the partner's name (`SC/united-states/payouts.md`, `SC/france/payouts.md`).
- **Faster rails:** in the US, payouts to Shopify Balance arrive in about 1 business day (`SP/payouts/payout-timing.md`).
- **Payout freezes:** changing the payout account pauses payouts for 3–5 business days (Japan also states this). With multiple currencies, changing one account can pause *all* payout accounts.

### 1.8 Minimum payout

- None: US, Canada, Australia, New Zealand.
- Typically €1, but €3 in Latvia and **€10 in France**.
- £1 (UK and Gibraltar), 5 JPY, 10 MXN, 10 HKD, 1 SGD, **20 AED**.
- Markets with two domestic currencies have a threshold per currency: 20 DKK/NOK/SEK, 30 CZK, 360 HUF, 5 CHF, 5 RON.
- Below the threshold the payout "stays in a pending state". The rule is the same everywhere; only the amount varies.

### 1.9 Negative balances and the right to debit the merchant's bank

- **No debit; the balance is carried until future sales cover it:**
  - Japan: refunds can show "pending", and payouts stop until new sales clear the balance (`SC/japan/payouts.md`).
  - Romania (`SC/romania/payouts.md`).
- **Depends on the bank account's currency:** Sweden's SEK and Switzerland's CHF accounts aren't debited, but EUR accounts "are debited normally" (`SC/sweden/requirements.md`, `SC/switzerland/requirements.md`).
- **Being debitable is an onboarding requirement elsewhere:**
  - Croatia: the bank account must be able to "accept debits" (`SC/croatia/requirements.md`).
  - US manual bank connection: the merchant agrees to a "bank debit authorization" (`SC/united-states/connecting-bank-accounts.md`).
- **Only Japan states a chargeback fee:** ¥1,300, refunded if the merchant wins.

### 1.10 Reserves

- **The country pages never mention reserves.** `SP/payouts/reserves.md` describes them in terms of risk only: fixed or percentage-based (for example 10% held for 120 days), triggered by chargebacks, refund rate, long delivery times or volume spikes.
- So reserves are a parameter of the merchant's risk state, not of the market.

### 1.11 Onboarding requirements (the dimension that varies most)

- **Business-type taxonomy written in local legal forms.** Examples: UAE has LLC, Free Zone LLC, Sole Establishment and Free Zone Sole Establishment. The US has 9 types. Germany uses GmbH/UG, OHG/KG, GbR and e.V./n.e.V. Japan maps a godo kaisha to Corporation and a 任意団体 (voluntary association) to Individual. France has a "Government entity" type; Singapore government bodies file as non-profit with a letter of authorization. Hong Kong reads the type from the certificate's 法律地位 field.
- **Registry identifier and registry matching.** EIN, SSN or ITIN (US); RFC from the SAT (MX); UEN from ACRA (SG); BRN plus HKID (HK); CRN plus Emirates ID (UAE); 13-digit Corporate Number (JP); ABN/ACN (AU); KVK (NL); SIRET/SIREN (FR); REGON/KRS (PL); Organisationsnummer from Bolagsverket (SE); UID (CH); CRN from Companies House (UK). Several pages require an exact match to the registry, "including letter case, punctuation, and symbols" (MX, SG, HK).
- **A tier for unregistered individuals.** Most markets let someone without a registry number sign up as "Individual" (US SSN only; MX without RFC; SG without UEN; HK without BRN; JP without Corporate Number). **UAE does not:** a CRN is mandatory and non-profits are ineligible (`SC/united-arab-emirates/requirements.md`).
- **Residency:**
  - Individuals and sole proprietors must live in the country (JP, MX, SG, HK, US, DE…). Companies need only local registration and a local business address.
  - Japan accepts only representative ID *issued by the Japanese government*. Hong Kong accepts a passport from a mainland-China resident who holds an HK BRN.
  - US: non-resident representatives may give a passport instead of an SSN, except for Individual and Sole Proprietor accounts. Coverage is the 50 states plus Puerto Rico. PO boxes and APO/FPO addresses are rejected (Canada also rejects PO boxes).
- **Accepted documents and how recent they must be:** UAE bank proof ≤6 months old. Singapore address proof ≤3 months and business documents ≤12 months. Mexico utility bills ≤6 months and government letters ≤12 months. US address documents ≤6 months. Local document types include Touki (JP), the Transparenzregister (DE), and a MUIS letter (SG).
- **Beneficial ownership:** the 25% threshold is the same everywhere. Nested holding companies must be broken down to individuals (UAE asks for an ownership flowchart as a cover page). The Singapore constitution rules add controllers who hold no equity.
- **Liveness:** 33 markets (EU, UK, CA, SG) offer a selfie with photo ID. Singapore *requires* Proof of Liveness, either through Singpass MyInfo or a selfie. It isn't stated for US, MX, JP, HK, UAE, AU or NZ.
- **Script and name rules:**
  - Japan: names in Kanji and Kana; registered name in Kanji, Kana and Romaji; bank and branch names in full-width Kanji; dates given in Japanese era years converted to the Western calendar.
  - Hong Kong: Chinese or English, exactly as shown on the document.
  - Singapore: names on the letter of authorization in English.
- **Statutory deadline:** Singapore accounts must be verified within **120 days** under the Payment Services Act 2019, or checkout stops for good. Verifying late releases held payouts but doesn't turn checkout back on (`SC/singapore/requirements.md`).
- **Ongoing duty:** every requirements page says verification can be requested again at any time as rules change ("Why am I being asked to provide new information?").

### 1.12 Bank account and payout rail

- **The rail is named per market:** ACH (US, CA), SPEI (MX), FAST/RTGS (SG), Zengin (JP), BECS (AU, NZ), Faster Payments (UK), SEPA with an allowed list of IBAN country prefixes (EU, CH, NO, GI), an IBAN starting "AE" (UAE). The US also offers Plaid for connecting the account.
- **Account types:** the same exclusion list everywhere (savings accounts, wire-only accounts, flex-currency accounts and money-transfer services aren't supported, and virtual accounts fail more often). Japan adds Futsu-only accounts, with Toza accounts configured manually in up to a month.
- **Format quirks:** Japan bank 4 / branch 3 / account 7 digits, padding a leading 0; Hong Kong 3/3/6–9 digits; Citibank Hong Kong must use the 8-digit number.
- **Name on the account must match the entity type:** UAE LLCs need a business account and sole establishments a personal account; Hong Kong works the same way. Japan: "banks are extremely particular about names", and name mismatches are the main cause of failed payouts.

### 1.13 Statement descriptors

- **Customer statement name:** 2–19 characters, and must contain the shop, legal, DBA name or URL. Shopify *corrects it on the merchant's behalf* and emails them (`SC/united-states/requirements.md`, `SP/configuring-shopify-payments.md`).
- **Payout statement name:** 5–22 characters, Latin letters only. In the UK and Ireland it appears as "Earthport PLC Shopify". In France the partner's name may override it.
- **Not found:** no kana or kanji descriptor rules appear anywhere in the corpus. Japan's Kana requirement covers the merchant's identity, and JCB activation can ask for "business name verification in Kana" (`SC/japan/payment-methods.md`).
- Several FAQs warn that the business name, phone and address may appear on buyers' card statements.

### 1.14 Tax reporting

- **(a) Information reporting on gross sales — US Form 1099-K** (`SC/united-states/tax-reporting.md`):
  - The federal threshold changes by tax year: >$20k and >200 transactions for 2023 and 2025, >$5k for 2024.
  - **11 state or district thresholds** are lower, for example $600 in MA, MD, VA and VT, and $1,000 with ≥4 transactions in IL. California's $600 applies to app-based drivers only.
  - Reporting is per tax ID, combining all accounts with the same TIN. It reports *gross* amounts by *posting date in UTC*, before refunds and fees.
  - Payouts can be paused if tax information can't be verified. Details can be corrected until July 15.
  - Tax-ID routing depends on business type: Individual, Sole Proprietor and single-member LLC report under the person's SSN/ITIN; other types under the EIN.
- **(b) Indirect tax on the processor's fees:**
  - Australia: 10% GST included. Singapore: 9% GST included (`SC/australia/tax-reporting.md`, `SC/singapore/tax-reporting.md`).
  - Ireland: 23% VAT *added*.
  - Rest of EU and UK: 0% reverse charge. France: 0%, with the VAT number written as FR plus 11 digits. Germany: no VAT on fees (`SP/payouts/pay-periods-and-fees.md`, `SC/france/tax-reporting.md`, `SC/germany/requirements.md`).
  - A monthly invoice is generated **on the 5th of the following month, in UTC**, and the CSV export has a GST or VAT column.
- **(c) Generic statement:** "Shopify Payments might also be required to report your sales to the local tax authorities" (JP, HK, UK, NZ, EU payouts pages).
- **DAC7 and PSD2/SCA appear nowhere in this slice.** 3-D Secure is only a link that every page repeats.

### 1.15 Market-specific regulation and consumer protection

- Japan: the Specified Commercial Transactions Act requires a public legal notice (`SC/japan/requirements.md`).
- Singapore: the Payment Services Act 120-day deadline.
- US: HSA/FSA rules tied to IRS categories; USDC excluded in some states.
- Each country has its own prohibited-business list, linked to a country-specific Terms of Service URL (for example `terms-payments/ae#prohibited-businesses`).
- France: merchants onboarded before 12 Nov 2024 must re-verify before they can use in-person payments, which shows that requirements are versioned by date.

### 1.16 Channel scope

- **In-person (POS) payments through Shopify Payments:** 18 markets. **Online-only:** 22 markets, including UAE, JP, MX and HK and much of the EU.
- Mexico: card details can be keyed in manually (MOTO) on POS but are processed as card-not-present.
- NZ: UnionPay works online but not at POS.

---

## 2. Compact table (17 representative markets)

Abbreviations: **MCP** = multi-currency payouts. **A/P** = Advanced or Plus plan. "selfie" = selfie with ID offered when automatic verification fails. "LPMs" = local payment methods for *domestic* buyers. "fee-tax" = indirect tax charged on processing fees.

| Market | Cards beyond V/MC | Domestic LPMs / BNPL | POS | Domestic payout ccy | MCP (plan; bank location) | Min settle | Min payout | Schedule | Negative balance | Key onboarding traits | Tax artefacts |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UAE | Maestro only | none / none | no | AED | USD only; **Plus**; UAE bank | 5 bd | 20 AED | not stated | not stated | CRN mandatory; 4 entity types; Emirates ID / passport; trade licence; MoA; IBAN AE | none stated |
| US | Amex, Discover, Diners; HSA/FSA | PayPal+Venmo wallet; USDC (state exclusions) | yes | USD (fixed) | AUD/CAD/EUR/GBP; A/P; foreign banks | 3 bd | none | default + multi-partner extra payouts | debit authorization | SSN/ITIN/EIN; 9 types; Plaid; 50 states+PR | 1099-K federal + state thresholds |
| Canada | Amex, Discover (→UnionPay, JCB); Interac POS | none domestic | yes | CAD | USD; A/P (Basic/Grow USD default 1.5%); CA/US bank | 3 d | none | D/W/M | — | CRA BN/NEQ; selfie; no PO box | — |
| Mexico | Amex (MXN only), UnionPay | OXXO (10–10k MXN), MSI instalments | no (MOTO only) | MXN | none | **7 bd** | 10 MXN | not stated | — | RFC from SAT; exact registry match | — |
| UK | Amex, Diners, Discover, Maestro, UnionPay | Klarna | yes | GBP | ~17 ccys; A/P; SEPA list | 3 bd | £1 | — | — | Companies House CRN; selfie | 0% reverse charge |
| Germany | Amex, Maestro, UnionPay | Klarna | yes | EUR | ~17; A/P | 3 bd | €1 | D/W/M | — | HRB/HRA; Transparenzregister; selfie | no VAT on fees; monthly invoice |
| France | Amex, **Cartes Bancaires**; no Google Pay | Klarna; PayPal wallet | yes | EUR | ~17; A/P; PayPal non-EUR excluded | 3 d pay period | **€10** | D/W/M; multi-partner | — | SIRET/SIREN; Government entity type | FR VAT no.; 0% on fees |
| Netherlands | Amex, Maestro, UnionPay | iDEAL, Klarna | yes | EUR | ~17; A/P | 3 bd | €1 | — | — | KVK; selfie | reverse charge |
| Portugal | Amex, Maestro, UnionPay | MB WAY (app approval), Multibanco (7-day pending, no chargebacks), Klarna | no | EUR | ~17; A/P | 3 bd | €1 | — | — | NIF/NIPC; selfie | reverse charge |
| Sweden | Amex, UnionPay | Swish (Plus only), Klarna | no | SEK **or** EUR | A/P | 3 bd | €1 / 20 SEK | — | **SEK not debited; EUR debited** | Bolagsverket org no.; selfie | reverse charge |
| Switzerland | Amex, Maestro, UnionPay | TWINT (CHF), Klarna | yes | CHF **or** EUR | A/P | 3 bd | €1 / 5 CHF | — | **CHF not debited; EUR debited** | UID; selfie | fee-tax applies |
| Romania | Amex, Maestro, UnionPay | none domestic (no Klarna) | no | RON **or** EUR | A/P | 3 bd | €1 / 5 RON | — | **not debited** | company tax ID; selfie | reverse charge |
| Japan | Amex, **JCB (JPY only, 3-wk review)** | none domestic | no | JPY | none | 5 d + days to payout day | 5 JPY | **weekly/monthly only** | **not debited**; ¥1,300 CB fee | Kanji/Kana/Romaji; JP-government ID only; Futsu/Zengin; SCT notice | generic |
| Singapore | Amex, UnionPay | GrabPay (early access) | yes | SGD | USD/EUR/GBP/JPY; A/P; **SG bank only** | 4 bd | 1 SGD | D/W/M | — | UEN/ACRA; **liveness (Singpass)**; **120-day PSA deadline** | 9% GST on fees |
| Hong Kong | Amex, UnionPay | Alipay, WeChat Pay (any buyer country) | no | HKD | USD/EUR/GBP/JPY; A/P; **HK bank only** | 4 bd | 10 HKD | — | — | BRN+HKID; 法律地位 mapping; 3/3/6–9-digit account | generic |
| Australia | Amex, UnionPay; EFTPOS POS | none domestic | yes | AUD | 12 ccys; A/P; foreign banks per ccy | **2 bd** | none | — | — | ABN/ACN; trusts mapped to company | 10% GST on fees |
| New Zealand | Amex, UnionPay (online only); co-branded EFTPOS | none domestic | yes | NZD | page says A/P; currency table says none (inconsistent) | 3 bd | none | — | — | NZBN; BECS | generic |

(bd = business days. "—" = not stated in the slice.)

---

## 3. What is fixed and what is parameterised

**Fixed: identical meaning across all 40 markets.**

- **Payment lifecycle vocabulary.** Capture, then "settlement time", then payout balance, then payout with status *pending / in transit / paid / failed*.
- **Calendar rules.** Captures stamped in UTC, Fri–Sun consolidation, bank lag of 24–72h, no payouts on weekends or holidays.
- **Minimum-payout rule:** a payout below the threshold stays pending.
- **Risk ladder:** settlement starts long and shortens with good fulfilment. Reserves are fixed or percentage-based.
- **Multi-currency payout algebra:** domestic currency is free and non-domestic payouts pay a fee. The fee is keyed on the *payout* currency. Unmatched currencies go to the default account.
- **Bank account rules:** the list of unsupported account types, and the 3–5-day pause after an account change.
- **Verification rules:** document-quality rules (accurate, legible, complete, an original photo, still valid), "update your account to match documents", 25% beneficial ownership, re-verification at any time, and data passed to "banking partners".
- **Payment methods:** cards and accelerated checkouts switch on automatically; local methods are switched on manually and shown by *customer* location.
- **Fees:** published on a per-country pricing page and shown in the admin. Fees always depend on (market, plan), with separate domestic and rest-of-world card rates (`SP/payouts/pay-periods-and-fees.md`).

**Parameterised: per market, often on finer keys.**

| Parameter | Actual key observed |
|---|---|
| Card brands, plus brand-to-currency coupling and activation mode (auto / manual / review) | (market, brand) → currency constraint, activation workflow |
| Local methods | (merchant market, method) enablement × (method → customer countries, currencies, amount bounds, merchant gates: order count, plan, early access) |
| Confirmation mode (sync card / app approval / async voucher) and pending window | method |
| Dispute regime (card chargeback / PayPal 20 days / Klarna 180+13 days / none) | method |
| Domestic payout currency set (1 or 2) | market |
| Multi-currency payouts: eligibility, currency list, allowed bank locations | (market, plan, payout currency) |
| Minimum settlement time | (market, risk tier, method) |
| Payout schedule options and weekday | market (Japan restricts) |
| Minimum payout amount | (market, payout currency) |
| Negative-balance recovery (debit vs offset) | **(market, bank-account currency)** |
| Bank rail, account format, account type, IBAN prefixes | market |
| Business-type taxonomy, required persons/roles, identifiers | (market, business type) |
| Residency rule | (market, business type) |
| Documents and freshness windows | (market, document class) |
| Liveness method (Singpass, selfie, none) | market |
| Verification deadline (120 days) | market |
| Name script rules (Kanji/Kana/Romaji; English/Chinese) | market |
| Descriptor length and charset | global, with a per-market processor override of the payout name (UK/IE, FR) |
| Tax: information-reporting thresholds | **(jurisdiction, sub-jurisdiction, tax year)**, aggregated per tax ID |
| Tax on fees: rate, included or added, reverse charge | market |
| Channel (online / POS / MOTO) | market |
| Statutory merchant disclosures (SCT legal notice) | market |
| Prohibited businesses | market (country ToS URL) |

**Inference:**
- Shopify's model looks like a fixed *capability catalogue* (methods, rails, document types, tax artefacts) combined with a *market profile*, a *merchant tier* (plan), a *merchant risk state* and *time*.
- The pages read as if generated from templates, because the same sentences recur with the country name swapped in. The parameters stored per market are fewer than the prose suggests. The disagreements between pages suggest the values are not all kept in one place:
  - Austria: 2 vs 3 business days of settlement.
  - Japan: "5 business days" vs "5 days + days to payout day".
  - NZ: multi-currency payouts on the country page but "—" in the currency table.
  - UAE: missing from `SP/store-currency/supported-payout-currencies.md` but present in `payouts-in-multiple-currencies.md`.
  - Canada: "3 days" vs "3 business days".
- Lesson: a platform should give each market parameter one source of truth and generate the documentation from it.
- **Several parameters are not per-country.** They are per (country, currency), per (method, buyer country, currency), per (jurisdiction, year) or per (merchant risk). A flat "market settings" record would be the wrong shape.
- **The UTC/Fri–Sun calendar is *fixed* even where local working weeks differ.** That works for Shopify's markets but would be wrong for Gulf or Yemeni working weeks. The business-day calendar should be a parameter.

---

## 4. UAE: the nearest MENA reference

**What Shopify states** (`SC/united-arab-emirates.md`, `SC/united-arab-emirates/{payment-methods,payouts,requirements}.md`, plus cross-references):

- **Channel:** online only. In-person sales need an external terminal from a third-party provider.
- **Cards:** Visa, Mastercard and Maestro, switched on automatically. 3-D Secure is linked in the same text as elsewhere.
- **Wallets:** Apple Pay, Google Pay and Shop Pay, switched on automatically.
- **Local methods, BNPL, USDC, PayPal:** none.
- **Payout currency:** AED on all plans. USD is the only extra currency, through multi-currency payouts, **for Shopify Plus only**. The USD account must also be a UAE bank (`SP/store-currency/payouts-in-multiple-currencies.md`).
- **Fees:** AED payouts carry no multi-currency payout fee. A USD default pays the fee, and a non-domestic default account pays an FX fee. Domestic-currency orders paid to a domestic bank are free even if AED isn't the default.
- **Settlement and payout:** minimum settlement 5 business days, starting longer for new merchants. Minimum payout 20 AED. Captures are stamped in UTC and Fri–Sun captures combined into one payout. Fees are on shopify.com/ae/pricing and in the admin.
- **Bank account:**
  - A checking account with a UAE bank in AED, able to receive *domestic and international* transfers, with an IBAN starting "AE".
  - LLC and Free Zone LLC must use a business account in the business name. Sole Establishments must use a personal account in the owner's legal name.
  - Wire-only, savings, flex-currency and money-transfer accounts aren't supported.
- **Eligibility:**
  - A company registration number is mandatory and non-profits are ineligible.
  - Only 4 business types: LLC, Free Zone LLC, Sole Establishment, Free Zone Sole Establishment.
  - Companies, civil companies, partnerships and single-member LLCs all file as LLC.
  - The manager of a sole establishment can be the representative if the licence lists no owners.
- **People:**
  - Representative details: legal name, date of birth, Emirates ID (or passport if living outside the UAE), citizenship (must match the passport), email, phone, residential address, job title.
  - LLCs must add every manager on the trade licence as "Executive". Owners with ≥25% must match the Memorandum of Association one-to-one.
  - Holding companies must be broken down through nested MoAs, combined into one file with an ownership flowchart cover page.
  - A power of attorney on letterhead is needed if the representative isn't named on the MoA or trade licence.
- **Identity documents:** UAE and GCC nationals living in the UAE give passport and Emirates ID. Foreign residents give passport, Emirates ID and residence visa. Non-residents give a passport.
- **Business documents:** sole establishments give a trade licence or freelancer permit. LLCs give a trade licence, MoA and proof of bank account (≤6 months old). The licence must be UAE-issued and show name, CRN, address and managers.
- **Ongoing:** re-verification may be requested as UAE rules change. Business name, phone and address may appear on buyers' card statements.

**What is absent from the UAE pages** (useful for Sharrwah):
- No local or domestic schemes (no national debit scheme), no BNPL, no PayPal, no Amex, no cash-voucher method.
- No tax-reporting page and no statement on VAT charged on fees, although Singapore and Australia have one for GST.
- No negative-balance or debit statement, and no payout-schedule options (daily/weekly/monthly isn't stated).
- No liveness check or selfie option.
- No "Individual" tier for unregistered sellers.
- No Arabic name or script handling (contrast Japan's Kana rules).
- No adjustment of the business-day calendar for the Gulf.
- No consumer-protection or e-commerce law reference (contrast Japan's SCT Act and Singapore's PSA).
- UAE is missing from the payout-currency table in `SP/store-currency/supported-payout-currencies.md`.

**Inference:**
- UAE is Shopify's thinnest market profile: card acquiring through banking partners plus strict company KYB. It carries little local payment knowledge.
- For MENA, Shopify gives a template for *entity KYB* (free zones, trade licences, MoAs, managers, beneficial-owner chains) and *IBAN payout rules*. It gives no template for how MENA buyers actually pay.

---

## 5. Implications for a market with no card acquiring (Yemen-like)

*All of section 5 is inference*, built on precedents in the slice.

1. **Confirmation mode and finality become the main payment parameter.** Shopify's slice already has three types:
   - Synchronous card authorization.
   - App or push approval within a time limit (MB WAY: phone number, then approval within 4 minutes, then automatic capture).
   - Asynchronous reference payment (Multibanco and OXXO: "authorized" at order but "funds aren't guaranteed", pending up to 7 days, then cancelled).

   Wallet-plus-OTP maps onto the second type. Bank transfer maps onto the third. Cash on delivery is a fourth type that Shopify's slice lacks: settlement happens *after fulfilment*, by a courier acting as collection agent. The model needs per-arrangement settings for: the confirmation step (OTP, app approval, reference, cash handover), the time limit and what happens when it expires, the point at which the obligation counts as met, whether a transaction can be reversed or disputed (Multibanco: no chargebacks), and amount limits (OXXO 10–10k MXN; MB WAY €5k vs Multibanco €99,999).
2. **Whether to fulfil before the money arrives must be a policy.** Multibanco leaves this to the merchant. With COD and transfers it is the core risk decision, and it should be configurable per merchant, method, amount and customer history.
3. **Settlement has several custodians, not one processor balance.** Couriers, wallet operators and banks each hold money and remit on their own schedules. The "payout" concept splits into collection remittance (courier to platform or merchant) and onward payout. So "settlement time" and "minimum payout" must be set per custodian and rail, not per market. The US and France already show more than one processor partner per market.
4. **Currencies and exchange regimes.** Shopify has *two domestic currencies* in 9 markets and allowed currencies per method. Yemen needs more:
   - Several domestic currencies, each tied to a region.
   - Exchange-rate *sources* that differ by region (a split rate regime), versioned in time.
   - A rule for when to convert: at order, at capture/collection, or at payout. Shopify converts at capture.
   - A rule for refunds: Shopify refunds at the current rate, which under volatile split rates is a real policy choice.
   - Currency must be recorded on every amount, and a ledger entry needs a rate reference.
5. **Netting without debit authority should be the default.** Japan, Romania and Swedish/Swiss local-currency accounts show "carry a negative balance and offset future receivables". With wallets and COD there is usually no mandate to debit the merchant's account, so offsetting is the norm. The platform needs a balance per (merchant, currency, custodian) and rules for clawback order.
6. **Onboarding evidence follows what the local registry can do.** Shopify's tiers (Individual without registration vs registered entity), ID rules by residency and nationality (the UAE GCC/foreign/non-resident split), exact-match registry checks, document freshness windows and liveness options must all be data. Where no registry can be queried, verification is mostly document review, and liveness may come from phone OTP or a wallet KYC tier (compare Singpass MyInfo as a delegated identity source). Transliterating Arabic names for matching is the analogue of Japan's Kanji/Kana rules.
7. **The business-day calendar is a hard parameter.** Shopify's fixed Fri–Sun consolidation and UTC capture day would be wrong for a Fri/Sat or Thu/Fri working week. Settlement counts, cut-off times and holiday calendars (including Hijri-dated holidays) need to be data per market.
8. **Dispute and refund regimes are per arrangement.** Cards are absent, so there is no network chargeback system. The platform has to supply the inquiry and dispute process itself. The PayPal (20 days) and Klarna (180 + 13 days) timelines are templates for such a process.
9. **Dimensions that matter less:** card brands, 3DS/SCA, statement descriptor length, multi-currency-payout fee algebra. **Dimensions that matter more:** custodian and rail settings, cash handling and reconciliation, exchange-rate provenance, and identity evidence.
10. **Tax.** Expect indirect tax on platform fees first (the AU/SG/IE pattern) and information reporting later (the US 1099-K pattern: thresholds by tax year and sub-jurisdiction, aggregated per tax ID, gross amounts by posting date). Build reporting thresholds as versioned rules from the start.

---

## 6. Class-level questions (provider-agnostic)

1. Which properties of a payment arrangement are market parameters (allowed currencies, amount bounds, confirmation mode, pending window, reversibility), and which are properties of the arrangement wherever it is offered? Where does the platform keep each? *[variability]*
2. Is a method's availability decided by the merchant's market, the buyer's location, the transaction currency, or all three? How is that relation stored and evaluated at checkout? *[rules]*
3. For each arrangement, at what event is the buyer's obligation counted as met: authorization, approval, capture, voucher payment, courier handover or remittance? What does an order show while it waits? *[lifecycle]*
4. What happens when an arrangement's time limit expires (approval timeout, voucher expiry, COD refusal)? Which side effects follow: order cancellation, inventory release, notifications? *[events]*
5. Who holds the funds between payment and payout (processor, wallet operator, bank, courier)? How does the platform reconcile each custodian's remittances against orders and the merchant balance? *[actors]*
6. Which settlement and payout values (settlement delay, schedule options, minimum payout, business-day calendar, cut-off time zone) are set per market, per custodian or rail, or per merchant risk state? Can they change over the merchant's life? *[variability]*
7. When a merchant's balance goes negative, does the platform have the right to debit them? If not, what offset and clawback order applies, and does it depend on the account's currency or rail? *[rules]*
8. How are several domestic currencies and region-specific exchange-rate sources represented? At which lifecycle points (order, capture/collection, payout, refund) is a rate fixed and recorded? *[information]*
9. What evidence does onboarding require per (market, business type), including identifiers, documents, freshness windows, residency, liveness and script or transliteration rules? How is that requirement set versioned and re-applied when rules change? *[information]*
10. Which statutory deadlines or regulatory events (verification deadlines, re-verification requests, tax-information failures) can suspend checkout or payouts? How are they modelled as states rather than ad-hoc flags? *[lifecycle]*
11. Which reporting duties fall on the platform (information reporting on gross sales, tax on its own fees, merchant disclosures)? How are thresholds keyed by jurisdiction, sub-jurisdiction and period, and aggregated across accounts with the same tax identity? *[rules]*
12. What dispute or inquiry process applies to each arrangement (network chargeback, wallet inquiry, BNPL dispute, none)? Who decides, within what windows, and how do outcomes post to the ledger? *[lifecycle]*
13. How can a new arrangement (a new wallet, a courier COD partner, a stablecoin) be added as data plus an adapter without changing core order and ledger code? *[extension]*
14. Which values must have a single source of truth so that documentation, checkout and payout behaviour can't drift apart, given that Shopify's own pages disagree on settlement days and currency availability? *[quality]*
15. Which capabilities are deliberately left out of a market at launch (POS, BNPL, multi-currency payouts, crypto)? How is that limitation made explicit to merchants rather than implied by absence? *[scope]*
