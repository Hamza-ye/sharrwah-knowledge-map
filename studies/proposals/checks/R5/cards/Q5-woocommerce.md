# Cards: Q5 on woocommerce

31 records cited by `studies/proposals/drafts/Q5/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - The merchant turns methods on, from those offered to its store: Shopify's buyers pay with "any of the methods that you've activated"; Salla's merchant presses (تفعيل) on its طرق الدفع page; BigCommerce's uses Settings › Payments; WooCommerce's gateways carry an "Enable/Disable" box; Zid's merchant turns networks on in إدارة زد باي. They match by role, on stated pages and WooCommerce's shipped code. Q5-SH-K1524, Q5-SA-017, Q5-BC-066, Q5-WC-K0032, Q5-ZD-K0041
- **section 1, line 8:** - Staff need a payments permission, matching by role: `MANAGE_PAYMENTS_SETTINGS` (Shopify's admin code), `payment_methods_activation` (Salla's partner portal, as captured on 8 October 2026, observed), `manage_woocommerce` (WooCommerce's code), and a right Zid's owner grants (stated); at Shopify "Only the store owner can add a payment provider". Q5-SH-K0193, Q5-SA-K1509, Q5-WC-001, Q5-ZD-002, Q5-SH-009
- **section 1, line 9:** - The merchant's own rules then decide what a buyer sees, matching by role: Salla's قيود الدفع hide a method or reject or review the order by amount, country, customer group or category; Zid's restrictions hide a method; Shopify's Payment Customization lets an app "rename, reorder, hide the payment methods"; WooCommerce keeps cash on delivery to chosen shipping methods (shipped code); BigCommerce's merchant ticks "the countries where this payment method is available at checkout". Q5-SA-043, Q5-SA-046, Q5-ZD-013, Q5-SH-K1761, Q5-WC-004, Q5-BC-P0121
- **section 1, line 10:** - Shopify, Zid and Salla limit methods by the store's country, matching by role: Shopify filters providers "based on your store's address"; Zid offers options "حسب دولتك", and زد باي only in Saudi Arabia and Kuwait; Salla's مدى and فيزا are "مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط". WooCommerce goes by country only in its suggestions, "The payment extension list for each country" (shipped code), and BigCommerce by the shopper's "geolocation" for local methods (stated; not checked on WooCommerce). Q5-SH-012, Q5-ZD-001, Q5-ZD-P0113, Q5-SA-036, Q5-WC-K0054, Q5-BC-081
- **section 1, line 13:** - The own service and other gateways, matching by role: Shopify allows "only one credit card payment provider activated at a time"; Zid's terms say "عند تفعيلك لخدمة زد باي ستتعطل بوابة الدفع الأخرى من المتجر" (official page); Salla's dashboard text, as captured on 8 October 2026, blocks its own service "لوجود ربط فعَّال مع تاب" (observed). WooCommerce differs: WooPayments and the Stripe plugin can run "at the same time", which "does cause a few issues". Q5-SH-008, Q5-ZD-P0109, Q5-SA-K1653, Q5-WC-031
- **section 1, line 23:** - Each platform has a payment service of its own, run through other companies, matching by role: Shopify Payments, processed and settled by "one or more Payment Processors"; WooPayments, "powered by Stripe"; Salla's, provided "عبر شركائها"; BigCommerce Payments, "powered by PayPal"; and زد باي, through "مقدمي خدمات الدفع". These are official pages but BigCommerce's (stated). Q5-SH-K1555, Q5-WC-K0008, Q5-SA-P0079, Q5-BC-P0055, Q5-ZD-P0003
- **section 1, line 24:** - Other companies' gateways, matching by role: Shopify's "over 100 credit card payment providers"; Salla's بوابات الدفع الأخرى (not checked on WooCommerce); Zid's بوابات الدفع الأُخرى; BigCommerce's providers on and off its Embedded list; WooCommerce's gateways, "created as additional plugins". Q5-SH-006, Q5-SA-K1638, Q5-ZD-K0084, Q5-BC-036, Q5-WC-K0007
- **section 1, line 25:** - Methods recorded outside any provider: Shopify's "manual payments"; BigCommerce's "offline payment methods"; WooCommerce's Offline type, where "No online payment is made"; Salla's طرق دفع أخرى; Zid's bank transfer. BigCommerce and WooCommerce match by the same term, offline; the others by role. In Shopify's store ibx5bt-xy (countryCode YE), observed on 30 September 2026, Cash on Delivery (COD), Money Order and Bank Deposit each carried `"group":"MANUAL"`. Q5-SH-027, Q5-BC-060, Q5-WC-016, Q5-SA-015, Q5-ZD-P0075, Q5-SH-083
- **section 1, line 26:** - Providers plug in as add-ons, matching by role: Shopify's "payments extensions"; WooCommerce's gateway classes, added "through traditional plugins"; Zid's Open APIs model for "partners / payment service providers (PSPs)"; BigCommerce's "app payment processors"; Salla's apps, through "the Recurring Payments API". Q5-SH-K1694, Q5-WC-K0006, Q5-ZD-K0077, Q5-BC-031, Q5-SA-064
- **section 1, line 27:** - Where the buyer pays: Shopify's "direct providers and external providers", the latter on a page outside the store; WooCommerce's Direct type, with payment fields "directly on the checkout page"; Zid's Open APIs, where in one checkout type "Zid will draw the payment form"; BigCommerce's gateways that "redirect shoppers to a hosted payment page". Shopify and WooCommerce match by the same term, direct; Zid and BigCommerce by role. Q5-SH-007, Q5-WC-016, Q5-ZD-K0080, Q5-BC-068
- **section 1, line 31:** - The platform may withdraw what it offers, mostly without notice, matching by role: Salla's agreement reserves "الحق في إلغاء أو تعديل أو تغيير أي من وسائل الدفع"; Shopify may disable third-party services "without notice to you", and so may BigCommerce; WooCommerce may "suspend or remove a Product from the Marketplace(s)" (vendor agreement, stated); زد باي "قد توقف أو تلغي الحساب في أي وقت". The others are official pages. Q5-SA-001, Q5-SH-K2168, Q5-BC-K0455, Q5-WC-K0462, Q5-ZD-010
- **section 1, line 33:** - Providers end things too, matching by role: "P24 can no longer be enabled on any WooPayments account that is not already using it", and once revoked, orders "will fail at checkout"; a Shopify merchant whose provider has no updated integration "must select a new payment provider". Q5-WC-013, Q5-WC-015, Q5-SH-022
- **section 1, line 34:** - The earlier provider stays for earlier orders, matching by role: at Shopify it "is available if you need it for cases such as order returns"; in store fake-demo-sharrwah (countryCode YE), observed on 30 September 2026, deactivating ONERWAY (Direct) read "Your existing orders will not be affected"; WooCommerce suggests keeping its plugin active "for at least 6 months after your final transaction". Shopify's point was not checked on Zid. Q5-SH-015, Q5-SH-098, Q5-WC-033
- **section 1, line 37:** - Money held when a merchant leaves the own service is paid out: WooPayments' remaining balance "will still be paid out as per your usual schedule"; Zid's, "يتم تحويل المبلغ المتوفر في رصيد التاجر إلى الحساب البنكي", though not before its financing is repaid. On BigCommerce, what happens to funds when a provider is disconnected was not in what was read. Q5-WC-K0715, Q5-ZD-P0042, Q5-ZD-P0097, Q5-BC-H0040
- **section 1, line 42:** - Through the platform's own service, money goes into a balance, then to the merchant's bank account, matching by role on stated pages and Zid's terms (official): Salla's "رصيد المدفوعات الإلكترونية" comes before the transfer to the bank account; Zid's terms add "المبلغ المستحق لرصيد التاجر" after fees; WooPayments adds the payment "(minus our fees)" to the balance; BigCommerce Payments and Shopify Payments pay out to the merchant's bank account. Q5-SA-P0006, Q5-ZD-P0024, Q5-WC-P0024, Q5-BC-P0074, Q5-SH-P0060
- **section 1, line 43:** - Who holds it in between, matching by role: Shopify's merchant opens "financial accounts and/or cryptocurrency wallets with one or more Payment Processors"; Stripe, as the merchant's agent, holds WooPayments' funds "in one or more Pooled Accounts at one or more Financial Providers"; BigCommerce Payments' transactions "flow through your new BigCommerce Payments account" (stated). For Salla and Zid, the entity, licence or account under which the balance is held was not in what was read. Q5-SH-P0010, Q5-WC-P0121, Q5-BC-P0052, Q5-SA-H0002, Q5-ZD-H0002
- **section 1, line 44:** - When it is paid out, and at what level: Salla by plan, from weekly on Plus to daily on Special; Zid by country; WooPayments daily, "the default for almost all accounts", changeable per account; BigCommerce Payments holds a new account's initial payments "for up to 21 days". They match by role; the level differs. Q5-SA-P0020, Q5-SA-P0022, Q5-ZD-P0041, Q5-WC-P0036, Q5-BC-P0083
- **section 1, line 45:** - Deductions come off first, matching by role, in the own services' terms (official pages): Shopify may hold funds in a Reserve Account; Stripe pays out "net of Fees, Disputes, Refunds, Reversals and other amounts owed to Stripe"; زد باي takes chargebacks "مباشرة من رصيده المتوفر". Services, financing and apps draw on it too: Salla's dashboard text, as captured on 8 October 2026, holds label amounts to pay "نيابةً عنك إلى شركة الشحن", and its financing takes "%25 من صافي المبيعات لكل دفعة" (observed); a dropshipping app may "temporarily withhold a specific amount of money" (Salla's developer docs). Q5-SH-P0028, Q5-WC-P0124, Q5-ZD-P0011, Q5-SA-P0126, Q5-SA-P0131, Q5-SA-K1690
- **section 1, line 46:** - Some keep separate balances, matching by role: in Salla's store real-merchant, observed on 12 October 2026, the wallet summary listed "Wallet", "Electronic Payments" and "Cash on Delivery Payments"; Zid's الاستقطاع للمحفظة moves part of order payments into محفظة زد; Shopify's Shop Cash comes in the same payouts; WooPayments' FROD balance is "a special bucket of funds inside your WooPayments account". Q5-SA-075, Q5-ZD-P0067, Q5-SH-074, Q5-WC-042
- **section 1, line 47:** - Through a gateway the merchant connects, money goes to the merchant's own account with it, matching by role: funds are in "your merchant account with your merchant service provider" (BigCommerce); "the purchase amount is transferred to your merchant account" (Shopify); Salla's dashboard text, as captured on 8 October 2026, collects through the gateway "بدلًا من مدفوعات سلة" (observed); "المدفوعات توصل لحسابك مباشرة" (Zid's Paymob page). Where the money is held between the buyer's payment and its transfer was not in what was read on Shopify. WooCommerce says only that it is "unable to assist with Stripe account issues", payouts among them: a statement of no part, naming no one. Q5-BC-P0089, Q5-SH-P0050, Q5-SA-K1639, Q5-ZD-P0107, Q5-SH-N02, Q5-WC-P0159
- **section 1, line 49:** - Pay-later providers pay the merchant directly, or into the platform's own service: at Salla (UAE help), "تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة"; at Zid, "تقوم تابي بالدفع للمتاجر مباشرة"; with BigCommerce's PayPal Pay Later, "you, the merchant, always get paid"; these match by role. Shopify and WooCommerce differ: Shop Pay Installments payouts "are included with your Shopify Payments payouts", and WooPayments receives "the entire purchase amount immediately". Q5-SA-P0102, Q5-ZD-P0077, Q5-BC-P0095, Q5-SH-K1686, Q5-WC-P0056
- **section 1, line 50:** - With methods outside any provider, the buyer pays the merchant and the order waits, matching by role: Salla's customer transfers "مباشرة من حسابه البنكي إلى حسابك"; BigCommerce's pay "directly into your bank account"; the order is "marked as unpaid" (Shopify), in "Awaiting Payment" (BigCommerce), or on hold, `OrderStatus::ON_HOLD` in WooCommerce's shipped code. In Shopify's store demo-fake-dev-store (countryCode YE), observed on 30 September 2026, the order then read "You manually marked YER699.95 as paid for this order." Q5-SA-P0099, Q5-BC-P0116, Q5-SH-K1736, Q5-BC-P0115, Q5-WC-K0037, Q5-SH-093
- **section 1, line 51:** - Cash on delivery is settled with the merchant, or collected through the platform, matching by role: at Salla, with a carrier outside its labels, it is settled "مباشرة بين التاجر وشركة الشحن", while through its labels "تحوِّل شركة الشحن المبلغ إلى سلة" (dashboard text, as captured on 8 October 2026, observed); through Zid's shipping, "تقوم زد بتحصيل المبلغ نيابة عن التاجر من العميل عند التسليم" (its terms, official); WooCommerce's cash on delivery takes payment "at the time of delivery". Q5-SA-P0092, Q5-SA-P0042, Q5-ZD-P0070, Q5-WC-P0097
- **section 2, line 55:** - **Payment method**: in Sharrwah's proposed design, a way a buyer can pay an order, such as a card network, a wallet, pay later, bank transfer or cash on delivery: either a **provider method**, which a payment provider processes, or a **manual method**, which the buyer pays to the merchant outside any provider and the merchant records; an order paid by a manual method waits, unpaid, until then. Q5-SH-027, Q5-BC-P0115, Q5-WC-016
- **section 2, line 56:** - It draws on the five platforms' split between provider and manual methods, and on the waiting order of Shopify, BigCommerce and WooCommerce. Q5-SH-083, Q5-BC-060, Q5-SA-015, Q5-ZD-P0075, Q5-SH-K1736, Q5-WC-K0037
- **section 2, line 62:** - It draws on BigCommerce's Embedded Providers; Shopify's approved payments extensions, review of new methods and readiness step; Zid's Open APIs and app review; and the direct and hosted payment of Shopify, WooCommerce and BigCommerce. Q5-BC-105, Q5-SH-062, Q5-ZD-K0077, Q5-ZD-K0363, Q5-SH-007, Q5-WC-016, Q5-BC-068
- **section 2, line 64:** - Not taken: payment code a merchant adds to its own store, as with WooCommerce's plugins, because a provider offered at a place is a partner relationship Sharrwah answers for (rule 3); WooCommerce itself asks a separate agreement of a partner offering a "Payments Solution". Q5-WC-K0006, Q5-WC-K0353
- **section 2, line 71:** - Not taken: WooCommerce's country list as suggestions only, which leaves the choice to the merchant, because each provider offered at a place is a partner contract (rule 3). Q5-WC-K0054, Q5-WC-K0353
- **section 2, line 75:** - Not taken: two card gateways at once, which WooCommerce allows though it "does cause a few issues". Q5-WC-031
- **section 2, line 77:** - It draws on Salla's قيود الدفع, Zid's restrictions, Shopify's Payment Customization, WooCommerce's cash on delivery by shipping method and BigCommerce's countries per offline method. Q5-SA-046, Q5-ZD-013, Q5-SH-K1761, Q5-WC-004, Q5-BC-P0121
- **section 2, line 79:** - **Payment record**: each payment on an order, with its method, provider, the provider's reference, amount, currency, state (awaiting, paid, recorded by the merchant, refunded) and money route. A refund goes back through the provider that took the payment, which stays callable for that after it leaves checkout. Q5-SH-015, Q5-WC-033, Q5-BC-085
- **section 2, line 80:** - It draws on BigCommerce's attribution of each order "to the provider that processed it", Shopify's earlier provider kept for returns (and store fake-demo-sharrwah on 30 September 2026, observed), WooCommerce's six months, and Shopify's manual mark as paid. Q5-BC-085, Q5-SH-015, Q5-SH-098, Q5-WC-033, Q5-SH-093
- **section 2, line 81:** - Why: rule 3, the data model; a payment that doesn't name its provider and route can't be refunded or reconciled once that provider has gone. Q5-SH-015, Q5-WC-033
- **section 2, line 83:** - It draws on the direct route the platforms show for gateways the merchant connects, pay-later providers that pay the store, and bank transfer, and on the held route of their own services. Q5-SH-P0050, Q5-ZD-P0107, Q5-ZD-P0077, Q5-SA-P0099, Q5-WC-P0024, Q5-ZD-P0024
- **section 2, line 87:** - **Merchant balance**, with its payouts, on the held route only, and live only by the founder's decision: a ledger, per merchant, holder and currency, of credits from payments and debits for fees, refunds, chargebacks, reserves and other deductions, each debit naming the party it pays and the merchant's authorization for it; and payouts of the amount available to the merchant's own bank account, given at verification, on a schedule. Q5-ZD-P0024, Q5-SA-P0055, Q5-WC-P0124
- **section 2, line 88:** - It draws on the platforms' own balances and their deductions and reserves, Salla's label holds under the merchant's authorization, and the payout account Salla takes at verification. Q5-SH-P0028, Q5-WC-P0124, Q5-ZD-P0011, Q5-SA-P0126, Q5-SA-P0055
- **section 2, line 90:** - Where the platforms differ, one balance with credits folded in (Shopify's Shop Cash; WooPayments' FROD bucket) against several wallets (Salla's observed store; Zid's wallet), typed entries in one ledger can show either; the choice is kept open. Q5-SH-074, Q5-WC-042, Q5-SA-075, Q5-ZD-P0067
- **section 2, line 92:** - It draws on BigCommerce's and Shopify's notice, P24's ending, Shopify's earlier provider kept for returns and its Wind Down Period, WooCommerce's six months, and the payout of the balance left at WooCommerce and Zid. Q5-BC-102, Q5-SH-021, Q5-WC-013, Q5-SH-K1704, Q5-WC-033, Q5-WC-K0715, Q5-ZD-P0042
- **section 2, line 93:** - Why: rule 2, a provider's exit touches only its own part; rule 3, refunds and money held are expensive to get wrong. Q5-SH-015, Q5-WC-015
- **section 2, line 94:** - Not taken: withdrawal without notice, which Shopify's, BigCommerce's and Salla's terms reserve, because a method withdrawn under the merchants leaves orders that "fail at checkout", as P24's did. Q5-SH-K2168, Q5-BC-K0455, Q5-SA-001, Q5-WC-015
- **section 3, line 98:** - Payment providers plug in, through a built-in integration or a payments add-on, as on all five platforms. Q5-SH-K1694, Q5-WC-K0006, Q5-ZD-K0077, Q5-BC-031, Q5-BC-105
- **section 3, line 103:** - Which providers and methods are offered is set per place, by Sharrwah; the records go by the store's address or country, or where the business is registered. Q5-SH-012, Q5-ZD-001, Q5-WC-K0402
- **section 3, line 111:** - On the held route, the payout schedule is set per plan (Salla), per country (Zid) or per account, by the merchant (WooPayments). Q5-SA-P0020, Q5-ZD-P0041, Q5-WC-P0036
- **section 3, line 113:** - Withdrawal is set per provider and place by Sharrwah; per add-on by its developer, within its wind-down terms, or by Sharrwah for a breach; and per method by the provider. Q5-BC-102, Q5-SH-K1704, Q5-SH-066, Q5-WC-013
- **section 5, line 128:** - Whether any held route goes live, and who would hold the money: Sharrwah, or a payment company in an account opened through Sharrwah. The design keeps the route on every payment and the balance as its own part, so no order or checkout code assumes a balance. The founder's decision under the guard settles it. Q5-SA-H0002, Q5-ZD-H0002, Q5-WC-P0121
- **section 5, line 130:** - What a place is: the platforms go by the store's address or country, or where the business is registered. The design keys the place payment list by a place that may be narrower or wider than a country. Q1's proposal settles it. Q5-SH-012, Q5-WC-K0402, Q5-ZD-001
- **section 5, line 136:** - How long a withdrawn provider stays callable for refunds and disputes: "available" at Shopify, at least six months at WooCommerce, while in Yemen an authority that bars a provider can leave 15 days to liquidate balances with it. The design sets the end per place and provider, as data. Each partner contract, and each place's authority, settles it. Q5-SH-015, Q5-WC-033, YK-17 (liquidate within 15 days @ Houthis' area, as of 2025-07-11)
- **section 5, line 137:** - On the held route only, the payout schedule's level (plan, place or account) and whether balances show as one or as several: the design keeps both as data. The holder's terms settle them. Q5-SA-P0020, Q5-ZD-P0041, Q5-WC-P0036, Q5-SA-075
- **section 7, line 159:** - Whether Sharrwah offers a payment service of its own in which sellers' money is held, by Sharrwah or by a payment company in an account opened through Sharrwah, and with which company: for the founder, under the guard. Q5-SH-K1555, Q5-WC-P0121, Q5-BC-P0069, Q5-SA-H0002, Q5-ZD-H0002
- **section 7, line 160:** - Which payment providers Sharrwah works with at each place, and on what terms: notice before withdrawal, refunds after it, settlement time, and service when a provider is down. Q5-BC-102, Q5-SH-064, Q5-WC-033, Q5-BC-G0048
- **section 7, line 161:** - Whether providers and partners may build payments add-ons, and under what agreement and review. Q5-SH-K1696, Q5-SH-063, Q5-WC-K0353, Q5-ZD-K0077
- **section 7, line 167:** - Which company contracts with providers and merchants, and where it is based, since the platforms' processors and contracting entities change with the merchant's country. Q5-SH-K1566, Q5-WC-P0108
- **section 7, line 168:** - Who may take online payments through Sharrwah, since the platforms' own services take only businesses from listed countries, and some methods only some business types. Q5-ZD-P0108, Q5-WC-K0402, Q5-ZD-K0042
- **section 8, line 173:** - Records: Shopify's financial services provider, Stripe's pooled accounts and BigCommerce Payments' account hold it; Salla's (UAE help) and Zid's balances hold sales proceeds before payout, but who holds either balance was not in what was read; a connected gateway pays the merchant's own account. S01-VP-01, Q5-SH-P0033, Q5-WC-P0121, Q5-BC-P0052, Q5-SA-P0057, Q5-ZD-P0035, Q5-SA-H0002, Q5-ZD-H0002, Q5-BC-P0089
- **section 8, line 176:** - Records: Shopify Payments' processors, Stripe for WooPayments, and BigCommerce Payments' PayPal platform account settle; Zid's terms credit "المبلغ المستحق لرصيد التاجر" after fees; who settles Salla's payments was not in what was read. S01-VP-02, Q5-SH-K1555, Q5-WC-P0122, Q5-BC-P0070, Q5-ZD-P0024, Q5-SA-H0004
- **section 8, line 179:** - Records: Shopify sends Shopify Payments' payouts, processed by partners, in the United States and France; WooPayments sends them to a bank account; Salla's dashboard text, as captured on 8 October 2026, lists transfers "من سلة إلى حسابك البنكي" (observed); Zid deposits on set days by country; BigCommerce Payments pays out to a linked bank or PayPal account. S01-VP-03, Q5-SH-P0076, Q5-WC-P0027, Q5-SA-P0040, Q5-ZD-P0041, Q5-BC-P0074
- **section 8, line 185:** - Records: Shopify is the merchant's agent "to deliver information and instructions on your behalf"; Stripe, "for the limited purpose of directing, receiving, holding and settling funds"; Zid executes "payment processes on their behalf" (official pages); Salla passes label amounts on the merchant's behalf (dashboard text as captured on 8 October 2026, observed). BigCommerce's "No agency" statement is one of no part, naming no one; no reading rests on it. S01-VP-06, Q5-SH-P0002, Q5-WC-P0121, Q5-ZD-P0008, Q5-SA-P0126, Q5-BC-P0129
- **section 8, line 188:** - Records: Shopify deducts refunds from the next payout; Stripe pays out net of fees, disputes and refunds; Zid takes fees from amounts collected, and dues by "الخصم الآلي والمباشر"; Salla's dashboard text, as captured on 8 October 2026, takes postpaid label amounts from the wallet or coming dues (observed). S01-VP-09, Q5-SH-P0094, Q5-WC-P0124, Q5-ZD-P0024, Q5-ZD-P0061, Q5-SA-P0129
- **section 8, line 191:** - Records: Shopify's merchant opens accounts with Payment Processors; WooCommerce's Stripe extension uses the merchant's Stripe account; BigCommerce Payments creates a PayPal platform account per store; Zid's pay-later providers need an account with them; in Salla's store real-merchant, observed on 12 October 2026, the wallet listed "Electronic Payments" and "Cash on Delivery Payments". S01-VP-11, Q5-SH-P0010, Q5-WC-P0023, Q5-BC-P0069, Q5-ZD-P0080, Q5-SA-075
- **section 8, line 194:** - Records: by plan at Salla, by country at Zid, by account country for WooPayments' "pending period"; up to 21 days for a new BigCommerce Payments account's first payments; at most 5 days for Shopify's payment apps to settle. S01-VP-15, Q5-SA-P0020, Q5-ZD-P0041, Q5-WC-P0033, Q5-BC-P0083, Q5-SH-064
- **section 8, line 197:** - Records: WooPayments credits payments "(minus our fees)"; Shopify's terms for the EU, EEA and UK settle "net of fees, refunds, chargebacks, reserves, and other amounts owed"; Salla transfers "بعد خصم الرسوم والضريبة" (dashboard text as captured on 8 October 2026, observed), while its store balance is for Salla's subscriptions and services (UAE help); Zid takes fees from amounts collected. S01-VP-19, Q5-WC-P0024, Q5-SH-P0107, Q5-SA-P0037, Q5-SA-P0057, Q5-ZD-P0024
- **section 8, line 200:** - Records: Shopify's funds in custody are paid out "subject to the Payment Processor Terms"; WooPayments' and Zid's balances are paid out, Zid's not before its financing is repaid; Salla may stop the service and close the store for a breach. On BigCommerce, what happens to funds when a provider is disconnected was not in what was read. S01-VP-20, Q5-SH-P0033, Q5-WC-K0715, Q5-ZD-P0042, Q5-ZD-P0097, Q5-SA-P0083, Q5-BC-H0040
- **section 8, line 206:** - Records: Shopify takes "a first priority lien and security interest" over funds processed and deposited; Stripe's terms for the United States have the merchant grant one to SPC. Both are official pages. S01-VP-10, Q5-SH-P0024, Q5-WC-P0113
- **section 8, line 209:** - Records: with BigCommerce's PayPal Pay Later the shopper owes PayPal, while the merchant will "always get paid"; WooPayments receives "the entire purchase amount immediately"; Shop Pay Installments come with Shopify Payments payouts; Tabby pays Zid's stores directly and collects Salla's payments itself (UAE help). S01-VP-22, Q5-BC-P0095, Q5-WC-P0056, Q5-SH-K1686, Q5-ZD-P0077, Q5-SA-P0102
- **section 8, line 211:** - Of the pilot review's open findings: no reading here rests on a statement of no part, nor on WooCommerce's policy pages, whose standing among its terms stays open. S01-VP-06, S01-VP-03, Q5-BC-P0129, Q5-WC-P0159

## The cards

### Q5-WC-K0032

**Cited at:** section 1, line 7

**Record** (`studies/proposals/records/Q5/woocommerce/copied.tsv`):
- concern_id: WC-C-002
- placement: decides
- structure: woocommerce-11.2.1:includes/gateways/bacs/class-wc-gateway-bacs.php
- identifier: woocommerce_bacs_settings: enabled
- statement: 'enabled' => array( 'title' => __( 'Enable/Disable', 'woocommerce' ), 'type' => 'checkbox', 'label' => __( 'Enable bank transfer', 'woocommerce' ), 'default' => 'no',
- scope: Direct bank transfer (bacs)
- cite_ids: WC-S-5001

**Citation WC-S-5001:** `woocommerce-11.2.1:includes/gateways/bacs/class-wc-gateway-bacs.php` | lines 105-109 | 2026-10-09 | kind: shipped | quote check: found
- quote: 'enabled' => array( 'title' => __( 'Enable/Disable', 'woocommerce' ), 'type' => 'checkbox', 'label' => __( 'Enable bank transfer', 'woocommerce' ), 'default' => 'no',
- in context: …ess_admin_options' ) ); add_action( 'woocommerce_update_options_payment_gateways_' . $this->id, array( $this, 'save_account_details' ) ); add_action( 'woocommerce_thankyou_bacs', array( $this, 'thankyou_page' ) ); // Customer Emails. add_action( 'woocommerce_email_before_order_table', array( $this, 'email_instructions' ), 10, 3 ); } /** * Initialise Gateway Settings Form Fields. */ public function init_form_fields() { $this->form_fields = array( ⟪'enabled' => array( 'title' => __( 'Enable/Disable', 'woocommerce' ), 'type' => 'checkbox', 'label' => __( 'Enable bank transfer', 'woocommerce' ), 'default' => 'no',⟫ ), 'title' => array( 'title' => __( 'Title', 'woocommerce' ), 'type' => 'safe_text', 'description' => __( 'This controls the title which the user sees during checkout.', 'woocommerce' ), 'default' => __( 'Direct bank transfer', 'woocommerce' ), 'desc_tip' => true, ), 'description' => array( 'title' => __( 'Description', 'woocommerce' ), 'type' => 'textarea', 'description' => __( 'Payment method description that the customer will see on your chec…

### Q5-WC-001

**Cited at:** section 1, line 8

**Record** (`studies/proposals/records/Q5/woocommerce/statements.tsv`):
- stmt_id: Q5-WC-001
- bears_on: 1;2
- identifier: Payments menu item: manage_woocommerce
- statement: 'manage_woocommerce', // Capability required to see the menu item.
- cite_ids: Q5-WC-C001
- from: held
- note: The menu item links to the Payments settings page (line 72 of the same file).

**Citation Q5-WC-C001:** `woocommerce-11.2.1:src/Internal/Admin/Settings/PaymentsController.php` | line 77 | 2026-10-09 | kind: shipped | quote check: found
- quote: 'manage_woocommerce', // Capability required to see the menu item.
- in context: …waDY4NGM0OCAwIDg0IDM4IDg0IDg2djUxMmMwIDQ4LTM2IDg2LTg0IDg2em0zODQtNTU2djQ0aDg2djg0SDM4MnY0NGgxMjhjMjQgMCA0MiAxOCA0MiA0MnYxMjhjMCAyNC0xOCA0Mi00MiA0MmgtNDR2NDRoLTg0di00NGgtODZ2LTg0aDE3MHYtNDRIMzM4Yy0yNCAwLTQyLTE4LTQyLTQyVjIxNGMwLTI0IDE4LTQyIDQyLTQyaDQ0di00NHoiLz48L3N2Zz4='; // Link to the Payments settings page. $menu_path = 'admin.php?page=wc-settings&tab=checkout&from=' . Payments::FROM_PAYMENTS_MENU_ITEM; add_menu_page( $menu_title, $menu_title, ⟪'manage_woocommerce', // Capability required to see the menu item.⟫ $menu_path, null, $menu_icon, 56, // Position after WooCommerce Product menu item. ); // If there are providers with an active incentive, add a notice badge to the Payments menu item. if ( $this->store_has_providers_with_incentive() ) { $badge = ' <span class="wcpay-menu-badge awaiting-mod count-1"><span class="plugin-count">1</span></span>'; foreach ( $menu as $index => $menu_item ) { // Only add the badge markup if not already present, and the…

### Q5-WC-004

**Cited at:** section 1, line 9; section 2, line 77

**Record** (`studies/proposals/records/Q5/woocommerce/statements.tsv`):
- stmt_id: Q5-WC-004
- bears_on: 1;2
- identifier: woocommerce_cod_settings: enable_for_methods (Enable for shipping methods)
- statement: 'description' => __( 'If COD is only available for certain methods, set it up here. Leave blank to enable for all methods.', 'woocommerce' ),
- scope: Cash on delivery (cod)
- cite_ids: Q5-WC-C004
- from: held

**Citation Q5-WC-C004:** `woocommerce-11.2.1:includes/gateways/cod/class-wc-gateway-cod.php` | line 133 | 2026-10-09 | kind: shipped | quote check: found
- quote: 'description' => __( 'If COD is only available for certain methods, set it up here. Leave blank to enable for all methods.', 'woocommerce' ),
- in context: …'title' => __( 'Instructions', 'woocommerce' ), 'type' => 'textarea', 'description' => __( 'Instructions that will be added to the thank you page.', 'woocommerce' ), 'default' => __( 'Pay with cash upon delivery.', 'woocommerce' ), 'desc_tip' => true, ), 'enable_for_methods' => array( 'title' => __( 'Enable for shipping methods', 'woocommerce' ), 'type' => 'multiselect', 'class' => 'wc-enhanced-select', 'css' => 'width: 400px;', 'default' => '', ⟪'description' => __( 'If COD is only available for certain methods, set it up here. Leave blank to enable for all methods.', 'woocommerce' ),⟫ 'options' => $this->load_shipping_method_options(), 'desc_tip' => true, 'custom_attributes' => array( 'data-placeholder' => __( 'Select shipping methods', 'woocommerce' ), ), ), 'enable_for_virtual' => array( 'title' => __( 'Accept for virtual orders', 'woocommerce' ), 'label' => __( 'Accept COD if the order is virtual', 'woocommerce' ), 'type' => 'checkbox', 'default' => 'yes', ), ); } /** * Check If The Gateway Is Available For Use. * * @since…

### Q5-WC-K0054

**Cited at:** section 1, line 10; section 2, line 71

**The same record as Q1-WC-K0054,** whose card is in `Q1-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: * The payment extension list for each country.
- scope: 

### Q5-WC-031

**Cited at:** section 1, line 13; section 2, line 75

**Record** (`studies/proposals/records/Q5/woocommerce/statements.tsv`):
- stmt_id: Q5-WC-031
- bears_on: 1
- identifier: WooPayments vs. Stripe Plugin Comparison
- statement: It’s also possible to use both gateways at the same time, although this does cause a few issues to be aware of.
- scope: WooPayments and the Stripe plugin
- cite_ids: Q5-WC-C037
- from: held

**Citation Q5-WC-C037:** `https://woocommerce.com/document/woopayments/compatibility/woopayments-vs-stripe-plugin-comparison/` | WooPayments vs. Stripe Plugin Comparison | 2026-09-25 | kind: stated | quote check: found
- quote: It’s also possible to use both gateways at the same time, although this does cause a few issues to be aware of.
- title: WooPayments vs. Stripe Plugin Comparison Documentation - WooCommerce
- in context: …etplace Code Snippets Expand WooPayments / Documentation / WooPayments Documentation / WooPayments: Compatibility / WooPayments vs. Stripe Plugin Comparison WooPayments vs. Stripe Plugin Comparison Because WooPayments is built in partnership with Stripe, it can sometimes be difficult to determine whether to use WooPayments or the Stripe plugin itself. In order to help you choose between the two, we've highlighted some important differences here. ⟪It's also possible to use both gateways at the same time, although this does cause a few issues to be aware of.⟫ WordPress dashboard integration WooPayments is designed to integrate closely with your WordPress website. It does this by displaying all your transaction data, payout records, Capital loan details, and other information right within your site's dashboard. This means you don't need to leave your site's admin interface to perform common business tasks. Bank account payouts inside the WordPress dashboard The regular Stripe plugin is not so closely …

### Q5-WC-K0008

**Cited at:** section 1, line 23

**Record** (`studies/proposals/records/Q5/woocommerce/copied.tsv`):
- concern_id: WC-C-001
- placement: decides
- structure: https://wordpress.com/tos/
- identifier: 8. j. Ecommerce Services: Third-Party Services
- statement: You may decide to use third-party services, like Stripe or PayPal to collect payment or EasyPost to manage shipping. Please note that WooPayments is powered by Stripe.
- cite_ids: WC-S-0651

**Citation WC-S-0651:** `https://wordpress.com/tos/` | 8. j. Ecommerce Services: Third-Party Services | 2026-10-06 | kind: official page | quote check: found
- quote: You may decide to use third-party services, like Stripe or PayPal to collect payment or EasyPost to manage shipping. Please note that WooPayments is powered by Stripe.
- title: WordPress.com
- in context: …Tax laws also differ from jurisdiction to jurisdiction and may be interpreted differently by different authorities. We recommend consulting with a tax professional for your specific tax situation to assess the tax rates you should charge. If we're obligated to pay or collect Taxes on your ecommerce activities or your use of Ecommerce Services, you're responsible for these Taxes, and we may collect payment for them from you. Third-Party Services. ⟪You may decide to use third-party services, like Stripe or PayPal to collect payment or EasyPost to manage shipping. Please note that WooPayments is powered by Stripe.⟫ If you use WooPayments or any third-party services, some of your - and your customers' - data may be submitted directly to or passed to the respective third party, and the respective third party's terms of service, privacy policy, and other policies may apply. For example, Payments requires a Stripe account to manage payments, and when you use Stripe, you agree to their terms and policies. Please note that third-party services may also charge yo…

### Q5-WC-K0007

**Cited at:** section 1, line 24

**Record** (`studies/proposals/records/Q5/woocommerce/copied.tsv`):
- concern_id: WC-C-001
- placement: where
- structure: https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/features/payments/payment-gateway-api.md
- identifier: Creating a basic payment gateway
- statement: Payment gateways should be created as additional plugins that hook into WooCommerce.
- cite_ids: WC-S-0627

**Citation WC-S-0627:** `https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/features/payments/payment-gateway-api.md` | Creating a basic payment gateway | 2026-10-10 | kind: stated | quote check: found
- quote: Payment gateways should be created as additional plugins that hook into WooCommerce.
- title: WooCommerce Payment Gateway API
- the page opens: Payment gateways in WooCommerce are class based and can be added through traditional plugins. This guide provides an intro to gateway development. Types of payment gateway Payment gateways come in several varieties: 1. Form based - This is where the user must click a button on a form that then redirects them to the payment processor on the gateway's own website. _Example_: PayPal standard, Authorize.net DPM 2. iFrame based - This is when the gateway payment system is loaded inside an iframe on y…
- headings: WooCommerce Payment Gateway API > Creating a basic payment gateway
- in context: …of [PCI compliance](https://woocommerce.com/document/pci-dss-compliance-and-woocommerce/). ## Creating a basic payment gateway **Note:** The instructions below are for the default Checkout page. If you're looking to add a custom payment method for the new Checkout block, check out [the payment method integration documentation](/docs/block-development/extensible-blocks/cart-and-checkout-blocks/checkout-payment-methods/payment-method-integration). ⟪Payment gateways should be created as additional plugins that hook into WooCommerce.⟫ Inside the plugin, you need to create a class after plugins are loaded. Example: ```php add_action( 'plugins_loaded', 'init_your_gateway_class' ); ``` It is also important that your gateway class extends the WooCommerce base gateway class, so you have access to important methods and the [settings API](https://developer.woocommerce.com/docs/settings-api/): ```php function init_your_gateway_class() { class WC_Gateway_Your_Gateway extends WC_Paymen…

### Q5-WC-016

**Cited at:** section 1, line 25; section 1, line 27; section 2, line 55; section 2, line 62

**Record** (`studies/proposals/records/Q5/woocommerce/statements.tsv`):
- stmt_id: Q5-WC-016
- bears_on: 3
- identifier: Types of payment gateway
- statement: 1. **Form based** - This is where the user must click a button on a form that then redirects them to the payment processor on the gateway's own website. _Example_: PayPal standard, Authorize.net DPM 2. **iFrame based** - This is when the gateway payment system is loaded inside an iframe on your store. _Example_: SagePay Form, PayPal Advanced 3. **Direct** - This is when the payment fields are shown directly on the checkout page and the payment is made when 'place order' is pressed. _Example_: PayPal Pro, Authorize.net AIM 4. **Offline** - No online payment is made. _Example_: Cheque, Bank Transfer
- cite_ids: Q5-WC-C017;Q5-WC-C018;Q5-WC-C019;Q5-WC-C020
- from: held
- note: Records the whole list; copies Q5-WC-K0005 and Q5-WC-K0031 hold items 1 and 4 in part.

**Citation Q5-WC-C017:** `https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/features/payments/payment-gateway-api.md` | Types of payment gateway: 1 | 2026-10-10 | kind: stated | quote check: found
- quote: 1. **Form based** - This is where the user must click a button on a form that then redirects them to the payment processor on the gateway's own website. _Example_: PayPal standard, Authorize.net DPM
- title: WooCommerce Payment Gateway API
- the page opens: Payment gateways in WooCommerce are class based and can be added through traditional plugins. This guide provides an intro to gateway development. Types of payment gateway Payment gateways come in several varieties: 1. Form based - This is where the user must click a button on a form that then redirects them to the payment processor on the gateway's own website. _Example_: PayPal standard, Authorize.net DPM 2. iFrame based - This is when the gateway payment system is loaded inside an iframe on y…
- headings: WooCommerce Payment Gateway API > Types of payment gateway
- in context: --- post_title: WooCommerce Payment Gateway API sidebar_label: Payment Gateway API sidebar_position: 1 --- # WooCommerce Payment Gateway API Payment gateways in WooCommerce are class based and can be added through traditional plugins. This guide provides an intro to gateway development. ## Types of payment gateway Payment gateways come in several varieties: ⟪1. **Form based** - This is where the user must click a button on a form that then redirects them to the payment processor on the gateway's own website. _Example_: PayPal standard, Authorize.net DPM⟫ 2. **iFrame based** - This is when the gateway payment system is loaded inside an iframe on your store. _Example_: SagePay Form, PayPal Advanced 3. **Direct** - This is when the payment fields are shown directly on the checkout page and the payment is made when 'place order' is pressed. _Example_: PayPal Pro, Authorize.net AIM 4. **Offline** - No online payment is made. _Example_: Cheque, Bank Transfer Form and iFrame based gateways post data of…

**Citation Q5-WC-C018:** `https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/features/payments/payment-gateway-api.md` | Types of payment gateway: 2 | 2026-10-10 | kind: stated | quote check: found
- quote: 2. **iFrame based** - This is when the gateway payment system is loaded inside an iframe on your store. _Example_: SagePay Form, PayPal Advanced
- title: WooCommerce Payment Gateway API
- the page opens: Payment gateways in WooCommerce are class based and can be added through traditional plugins. This guide provides an intro to gateway development. Types of payment gateway Payment gateways come in several varieties: 1. Form based - This is where the user must click a button on a form that then redirects them to the payment processor on the gateway's own website. _Example_: PayPal standard, Authorize.net DPM 2. iFrame based - This is when the gateway payment system is loaded inside an iframe on y…
- headings: WooCommerce Payment Gateway API > Types of payment gateway
- in context: …WooCommerce Payment Gateway API Payment gateways in WooCommerce are class based and can be added through traditional plugins. This guide provides an intro to gateway development. ## Types of payment gateway Payment gateways come in several varieties: 1. **Form based** - This is where the user must click a button on a form that then redirects them to the payment processor on the gateway's own website. _Example_: PayPal standard, Authorize.net DPM ⟪2. **iFrame based** - This is when the gateway payment system is loaded inside an iframe on your store. _Example_: SagePay Form, PayPal Advanced⟫ 3. **Direct** - This is when the payment fields are shown directly on the checkout page and the payment is made when 'place order' is pressed. _Example_: PayPal Pro, Authorize.net AIM 4. **Offline** - No online payment is made. _Example_: Cheque, Bank Transfer Form and iFrame based gateways post data offsite, meaning there are less security issues for you to think about. Direct gateways, however, require server security to be implemented ([SSL c…

**Citation Q5-WC-C019:** `https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/features/payments/payment-gateway-api.md` | Types of payment gateway: 3 | 2026-10-10 | kind: stated | quote check: found
- quote: 3. **Direct** - This is when the payment fields are shown directly on the checkout page and the payment is made when 'place order' is pressed. _Example_: PayPal Pro, Authorize.net AIM
- title: WooCommerce Payment Gateway API
- the page opens: Payment gateways in WooCommerce are class based and can be added through traditional plugins. This guide provides an intro to gateway development. Types of payment gateway Payment gateways come in several varieties: 1. Form based - This is where the user must click a button on a form that then redirects them to the payment processor on the gateway's own website. _Example_: PayPal standard, Authorize.net DPM 2. iFrame based - This is when the gateway payment system is loaded inside an iframe on y…
- headings: WooCommerce Payment Gateway API > Types of payment gateway
- in context: … an intro to gateway development. ## Types of payment gateway Payment gateways come in several varieties: 1. **Form based** - This is where the user must click a button on a form that then redirects them to the payment processor on the gateway's own website. _Example_: PayPal standard, Authorize.net DPM 2. **iFrame based** - This is when the gateway payment system is loaded inside an iframe on your store. _Example_: SagePay Form, PayPal Advanced ⟪3. **Direct** - This is when the payment fields are shown directly on the checkout page and the payment is made when 'place order' is pressed. _Example_: PayPal Pro, Authorize.net AIM⟫ 4. **Offline** - No online payment is made. _Example_: Cheque, Bank Transfer Form and iFrame based gateways post data offsite, meaning there are less security issues for you to think about. Direct gateways, however, require server security to be implemented ([SSL certificates](https://woocommerce.com/document/ssl-and-https/), etc.) and may also require a level of [PCI compliance](https://woocommerce.com/document/pci-dss-compliance-and-woocommerc…

**Citation Q5-WC-C020:** `https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/features/payments/payment-gateway-api.md` | Types of payment gateway: 4 | 2026-10-10 | kind: stated | quote check: found
- quote: 4. **Offline** - No online payment is made. _Example_: Cheque, Bank Transfer
- title: WooCommerce Payment Gateway API
- the page opens: Payment gateways in WooCommerce are class based and can be added through traditional plugins. This guide provides an intro to gateway development. Types of payment gateway Payment gateways come in several varieties: 1. Form based - This is where the user must click a button on a form that then redirects them to the payment processor on the gateway's own website. _Example_: PayPal standard, Authorize.net DPM 2. iFrame based - This is when the gateway payment system is loaded inside an iframe on y…
- headings: WooCommerce Payment Gateway API > Types of payment gateway
- in context: …then redirects them to the payment processor on the gateway's own website. _Example_: PayPal standard, Authorize.net DPM 2. **iFrame based** - This is when the gateway payment system is loaded inside an iframe on your store. _Example_: SagePay Form, PayPal Advanced 3. **Direct** - This is when the payment fields are shown directly on the checkout page and the payment is made when 'place order' is pressed. _Example_: PayPal Pro, Authorize.net AIM ⟪4. **Offline** - No online payment is made. _Example_: Cheque, Bank Transfer⟫ Form and iFrame based gateways post data offsite, meaning there are less security issues for you to think about. Direct gateways, however, require server security to be implemented ([SSL certificates](https://woocommerce.com/document/ssl-and-https/), etc.) and may also require a level of [PCI compliance](https://woocommerce.com/document/pci-dss-compliance-and-woocommerce/). ## Creating a basic payment gateway **Note:** The instructions below are…

### Q5-WC-K0006

**Cited at:** section 1, line 26; section 2, line 64; section 3, line 98

**The same record as Q1-WC-K0006,** whose card is in `Q1-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Payment gateways in WooCommerce are class based and can be added through traditional plugins.
- scope: 

### Q5-WC-K0462

**Cited at:** section 1, line 31

**Record** (`studies/proposals/records/Q5/woocommerce/copied.tsv`):
- concern_id: WC-C-017
- placement: decides
- structure: https://woocommerce.com/woo-vendor-agreement/
- identifier: 3.1
- statement: we reserve the right to suspend or remove a Product from the Marketplace(s) and/or a User’s Website at any time at our discretion
- cite_ids: WC-S-0583

**Citation WC-S-0583:** `https://woocommerce.com/woo-vendor-agreement/` | 3.1 | 2023-06-02 | kind: stated | quote check: found
- quote: we reserve the right to suspend or remove a Product from the Marketplace(s) and/or a User’s Website at any time at our discretion
- title: Marketplace Vendor Agreement - WooCommerce
- in context: …month. 2.3. Partner shall be responsible and liable for all amounts relating to Taxes. We will be responsible for facilitating any User requests or claims related to returns, cancellations, refunds, and/or fraud. We will not be liable and Partner shall have no right to claw back any such amounts relating to the amounts outlined in the preceding sentence. 3. Removal of the Product 3.1. While we do not take on an obligation to monitor the Product, ⟪we reserve the right to suspend or remove a Product from the Marketplace(s) and/or a User's Website at any time at our discretion⟫, and to modify a Product for the purpose of fixing bugs or protecting the security and/or performance of Automattic, WooCommerce, or our Users', systems or Websites. We will give Partner thirty (30) days' notice before we remove a Product from a Marketplace, but we may suspend a Product immediately, including for the reasons listed in Sections 3.3.1 - 3.3.8 below. Once suspended, a Product will not be available for purchase or renewal until/unle…

### Q5-WC-013

**Cited at:** section 1, line 33; section 2, line 92; section 3, line 113

**Record** (`studies/proposals/records/Q5/woocommerce/statements.tsv`):
- stmt_id: Q5-WC-013
- bears_on: 4;1
- identifier: Przelewy24 (P24) additional requirements
- statement: P24 is unavailable to new merchant accounts! As of August 17, 2026, P24 can no longer be enabled on any WooPayments account that is not already using it. This comes directly from Przelewy24 themselves. There are no exceptions.
- scope: Przelewy24 (P24)
- cite_ids: Q5-WC-C014
- from: held

**Citation Q5-WC-C014:** `https://woocommerce.com/document/woopayments/payment-methods/local-payment-methods/` | Przelewy24 (P24) additional requirements | 2026-09-25 | kind: stated | quote check: found
- quote: P24 is unavailable to new merchant accounts! As of August 17, 2026, P24 can no longer be enabled on any WooPayments account that is not already using it. This comes directly from Przelewy24 themselves. There are no exceptions.
- title: Local payment methods Documentation - WooCommerce
- in context: …nabled, please contact support so we can help look into it. iDEAL | Wero additional requirements If your business is based in the Netherlands, iDEAL | Wero requires that your website displays your KVK number on file with the Chamber of Commerce. If you use iDEAL | Wero but are based outside the Netherlands, your website must display your company registration number with the equivalent local official body. Przelewy24 (P24) additional requirements ⟪P24 is unavailable to new merchant accounts! As of August 17, 2026, P24 can no longer be enabled on any WooPayments account that is not already using it. This comes directly from Przelewy24 themselves. There are no exceptions.⟫ If Przelewy24 is already active on your account, you can continue using it provided that you meet the following set of criteria: Your business type must be a company. As of August 6, 2026, Przelewy24 no longer supports individual business types, including sole proprietorships, in any country. This applies regardless of whether you have a valid tax ID or NIP. A valid tax ID, VAT ID, or NIP (for Polish entities) in your Stripe Express account. See…

### Q5-WC-015

**Cited at:** section 1, line 33; section 2, line 93; section 2, line 94

**Record** (`studies/proposals/records/Q5/woocommerce/statements.tsv`):
- stmt_id: Q5-WC-015
- bears_on: 4
- identifier: Przelewy24 (P24) additional requirements
- statement: When access to P24 payments is revoked, orders using it will fail at checkout with an authentication error rather than P24 simply being disabled in your settings. Sadly this is not something that we (WooPayments/Automattic) can control.
- scope: Przelewy24 (P24)
- cite_ids: Q5-WC-C016
- from: held

**Citation Q5-WC-C016:** `https://woocommerce.com/document/woopayments/payment-methods/local-payment-methods/` | Przelewy24 (P24) additional requirements | 2026-09-25 | kind: stated | quote check: found
- quote: When access to P24 payments is revoked, orders using it will fail at checkout with an authentication error rather than P24 simply being disabled in your settings. Sadly this is not something that we (WooPayments/Automattic) can control.
- title: Local payment methods Documentation - WooCommerce
- in context: …our company address, tax number, and registration number. Refund and privacy policies. An MCC that is not one of the prohibited MCCs listed below. If you do not meet these criteria, your ability to accept P24 payments may be removed without warning at any time. P24 reviews merchants on an ongoing basis, not just when you first activate it. This means that your access might be revoked even if you've accepted P24 payments successfully in the past. ⟪When access to P24 payments is revoked, orders using it will fail at checkout with an authentication error rather than P24 simply being disabled in your settings. Sadly this is not something that we (WooPayments/Automattic) can control.⟫ If your P24 payments have started failing unexpectedly, contact our support team. Przelewy24 (P24) prohibited businesses In addition to our general list of prohibited or restricted products, businesses using the following MCCs are not eligible to use Przelewy24. (If you would like to change your MCC to a different one, please see this document.) CATEGORY MCC Airlines and Air Carriers 3000-3350 Lodging - Hotels, Motels, Resorts 3501-3999 Railroad…

### Q5-WC-033

**Cited at:** section 1, line 34; section 2, line 79; section 2, line 80; section 2, line 81; section 2, line 92; section 5, line 136; section 7, line 160

**Record** (`studies/proposals/records/Q5/woocommerce/statements.tsv`):
- stmt_id: Q5-WC-033
- bears_on: 4
- identifier: Stop using WooPayments
- statement: We strongly suggest leaving the plugin itself active for at least 6 months after your final transaction. This is because, if you delete the WooPayments plugin, you will no longer be able to issue refunds or respond to disputes for WooPayments orders.
- scope: WooPayments
- cite_ids: Q5-WC-C039
- from: held

**Citation Q5-WC-C039:** `https://woocommerce.com/document/woopayments/account-management/delete-account/` | Stop using WooPayments | 2026-09-02 | kind: stated | quote check: found
- quote: We strongly suggest leaving the plugin itself active for at least 6 months after your final transaction. This is because, if you delete the WooPayments plugin, you will no longer be able to issue refunds or respond to disputes for WooPayments orders.
- title: How do I delete my WooPayments account? Documentation - WooCommerce
- in context: … Check to confirm that it qualifies for deletion. Ask for your approval to delete the account. Delete the account from our systems. Confirm with you that it's been deleted. Once a WooPayments account is deleted, it is not recoverable. Stop using WooPayments If your WooPayments account does not qualify for deletion, the alternative is to disable WooPayments as a payment gateway on your site. There are a few important things to be aware of though: ⟪We strongly suggest leaving the plugin itself active for at least 6 months after your final transaction. This is because, if you delete the WooPayments plugin, you will no longer be able to issue refunds or respond to disputes for WooPayments orders.⟫ If you don't already have an alternative payment gateway enabled, doing so before disabling WooPayments ensures that customers will still be able to place orders. If you have subscribers using the Stripe Billing engine, their renewals will continue to process even if WooPayments is disabled. To stop their subscription renewals, you will need to cancel their subscriptions before disabling WooPayments. To disable WooPayments as a payment method on…

### Q5-WC-K0715

**Cited at:** section 1, line 37; section 2, line 92; section 8, line 200

**Record** (`studies/proposals/records/Q5/woocommerce/copied.tsv`):
- concern_id: WC-C-048
- placement: decides
- structure: https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/
- identifier: Stripe agreement updates
- statement: Although your remaining account balance will still be paid out as per your usual schedule, you will not be able to:
- cite_ids: WC-S-0509

**Citation WC-S-0509:** `https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/` | Stripe agreement updates | 2026-09-30 | kind: stated | quote check: found
- quote: Although your remaining account balance will still be paid out as per your usual schedule, you will not be able to:
- title: WooPayments built in partnership with Stripe Documentation - WooCommerce
- in context: …. Stripe agreement updates ↑ Back to top Occasionally, Stripe may update their Connected Account Agreement, which contains the terms you agreed to during the WooPayments signup process. When this happens, we are required to send you a notification email. If you wish to opt out of the updated terms, please reply to that email and let us know. Keep in mind that opting out in this way means that you will no longer be able to use WooPayments at all. ⟪Although your remaining account balance will still be paid out as per your usual schedule, you will not be able to:⟫ Have customers place new orders via WooPayments Refund any orders placed with WooPayments Challenge disputes filed for WooPayments orders Log into the WooPayments Stripe Express account etc. In short, opting out will effectively end your usage of WooPayments immediately. On this page Who will provide support Access to the Stripe dashboard Updating account information Existing Stripe Accounts Stripe agreement updates 30-day money-back guarantee S…

### Q5-WC-P0024

**Cited at:** section 1, line 42; section 2, line 83; section 8, line 197

**Record** (`studies/proposals/records/Q5/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-023
- bullet: a;c;end-payment;end-payout
- placement: where
- identifier: What’s the difference between a payout and a deposit in WooPayments?
- statement: After you receive an order via WooPayments, the payment amount (minus our fees) will be added to your account balance. This balance is regularly transferred to your bank account or debit card.
- scope: WooPayments
- cite_ids: S01-WC-C023
- from: index:WC-C-007:WC-S-0529

**Citation S01-WC-C023:** `https://woocommerce.com/document/woopayments/payouts/deposits-and-payouts/` | What’s the difference between a payout and a deposit in WooPayments? | 2024-11-14 | kind: stated | quote check: found
- quote: After you receive an order via WooPayments, the payment amount (minus our fees) will be added to your account balance. This balance is regularly transferred to your bank account or debit card.
- title: What’s the difference between a payout and a deposit in WooPayments? Documentation - WooCommerce
- in context: …Search Log inGet started Documentation Documentation WooCommerceExpand ProductsExpand ExtensionsExpand ThemesExpand WooPayments WooPay WooCommerce Shipping WooCommerce Tax Retired ProductsExpand Woo Marketplace Code SnippetsExpand WooPayments / Documentation / WooPayments Documentation / WooPayments: Payouts / What's the difference between a payout and a deposit in WooPayments? What's the difference between a payout and a deposit in WooPayments? ⟪After you receive an order via WooPayments, the payment amount (minus our fees) will be added to your account balance. This balance is regularly transferred to your bank account or debit card.⟫ These transfers are referred to as "payouts." Prior to WooPayments version 8.5.0 (released on Nov 14, 2024), payouts used to be referred to as "deposits." You may still see that terminology used in a few places while we work on updating things. Was this guide helpful for you? WooPayments by Woo No payment details required • Set up in minutes Install for free You've been here a while. Can I help? 30-day money-back guarantee Support teams across t…

### Q5-WC-P0121

**Cited at:** section 1, line 43; section 5, line 128; section 7, line 159; section 8, line 173; section 8, line 185

**Record** (`studies/proposals/records/Q5/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-120
- bullet: a;b
- placement: responsible
- identifier: Stripe Payments: 4.2 Pooled Accounts.
- statement: User appoints Stripe as User’s agent for the limited purpose of directing, receiving, holding and settling funds under this Agreement. All settlement funds Stripe receives for Transactions are combined with settlement funds for other users and held in one or more Pooled Accounts at one or more Financial Providers.
- cite_ids: S01-WC-C147;S01-WC-C148
- from: new

**Citation S01-WC-C147:** `https://stripe.com/legal/ssa-service-terms` | Stripe Payments: 4.2 Pooled Accounts. | 2026-09-28 | kind: official page | quote check: found
- quote: User appoints Stripe as User’s agent for the limited purpose of directing, receiving, holding and settling funds under this Agreement.
- title: Stripe Services Agreement—Service Terms
- in context: …cates a Transaction that is already subject to a Dispute, or was previously disputed and subsequently resolved in User's favor. Stripe may refuse to process, or condition or suspend any Transaction that Stripe believes (x) may violate this Agreement or other agreement User has with Stripe (if any); (y) is unauthorized, fraudulent or illegal; or (z) exposes, or is likely to expose, Stripe, User or others to unacceptable risk. 4.2 Pooled Accounts. ⟪User appoints Stripe as User's agent for the limited purpose of directing, receiving, holding and settling funds under this Agreement.⟫ All settlement funds Stripe receives for Transactions are combined with settlement funds for other users and held in one or more Pooled Accounts at one or more Financial Providers. Once Stripe receives funds for a Transaction on User's behalf, the relevant Customer has no further obligation to make payments to User with respect to that Transaction, regardless of whether and when Stripe settles those funds to User. If Stripe does not settle funds…

**Citation S01-WC-C148:** `https://stripe.com/legal/ssa-service-terms` | Stripe Payments: 4.2 Pooled Accounts. | 2026-09-28 | kind: official page | quote check: found
- quote: All settlement funds Stripe receives for Transactions are combined with settlement funds for other users and held in one or more Pooled Accounts at one or more Financial Providers.
- title, opening and note boxes: as for this source's citation above
- in context: …may refuse to process, or condition or suspend any Transaction that Stripe believes (x) may violate this Agreement or other agreement User has with Stripe (if any); (y) is unauthorized, fraudulent or illegal; or (z) exposes, or is likely to expose, Stripe, User or others to unacceptable risk. 4.2 Pooled Accounts. User appoints Stripe as User's agent for the limited purpose of directing, receiving, holding and settling funds under this Agreement. ⟪All settlement funds Stripe receives for Transactions are combined with settlement funds for other users and held in one or more Pooled Accounts at one or more Financial Providers.⟫ Once Stripe receives funds for a Transaction on User's behalf, the relevant Customer has no further obligation to make payments to User with respect to that Transaction, regardless of whether and when Stripe settles those funds to User. If Stripe does not settle funds due to User under this Agreement, User will have recourse only against Stripe and not the relevant Customer. Stripe will promptly update User's Stripe Account balance to reflect pr…

### Q5-WC-P0036

**Cited at:** section 1, line 44; section 3, line 111; section 5, line 137

**Record** (`studies/proposals/records/Q5/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-035
- bullet: c
- placement: decides
- identifier: When will I receive payouts for my WooPayments account balance? > Payout schedules
- statement: The chart and examples above assume that your site is on a daily payout schedule, which is the default for almost all accounts. However, it is possible to change your payout schedule to weekly or monthly.
- scope: WooPayments
- cite_ids: S01-WC-C035
- from: new

**Citation S01-WC-C035:** `https://woocommerce.com/document/woopayments/payouts/payout-schedule/` | Payout schedules | 2026-08-21 | kind: stated | quote check: found
- quote: The chart and examples above assume that your site is on a daily payout schedule, which is the default for almost all accounts. However, it is possible to change your payout schedule to weekly or monthly.
- title: When will I receive payouts for my WooPayments account balance? Documentation - WooCommerce
- in context: … to top Payments processed on a non-business day (such as a weekend day or a holiday in your country) will have their pending period start on the next business day. For example, if a U.S. store makes a sale on Saturday, the customer is charged right away, but the pending period doesn't start until Monday. Since the U.S. pending period is 2 business days, the merchant will get those funds on the following Wednesday. Payout schedules ↑ Back to top ⟪The chart and examples above assume that your site is on a daily payout schedule, which is the default for almost all accounts. However, it is possible to change your payout schedule to weekly or monthly.⟫ This will of course affect the payout timing. For example, consider a merchant in New Zealand with their payout schedule set to weekly on Fridays. If a customer orders from their store on Thursday, 4 business days after that would be the following Wednesday. However, due to their "weekly on Fridays" payout schedule, the funds remain in their account for 2 more days, and are paid out on the following Friday. NOTE: Changing your payout schedule mi…

### Q5-WC-P0124

**Cited at:** section 1, line 45; section 2, line 87; section 2, line 88; section 8, line 188

**Record** (`studies/proposals/records/Q5/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-123
- bullet: c;end-payout
- placement: decides
- identifier: Stripe Payments: 4.3 Transaction Settlement Funds.
- statement: Stripe will transfer settlement funds for Transactions, net of Fees, Disputes, Refunds, Reversals and other amounts owed to Stripe, from the applicable Pooled Account to User in accordance with the applicable settlement method as follows, unless a Payout Delay occurs and affects the transfer initiation, or Stripe exercises a right under this Agreement to withhold or delay the transfer:
- cite_ids: S01-WC-C151;S01-WC-C152
- from: new

**Citation S01-WC-C151:** `https://stripe.com/legal/ssa-service-terms` | Stripe Payments: 4.3 Transaction Settlement Funds. | 2026-09-28 | kind: official page | quote check: found
- quote: Stripe will transfer settlement funds for Transactions, net of Fees, Disputes, Refunds, Reversals and other amounts owed to Stripe, from the applicable Pooled Account to User in accordance with the applicable settlement method as follows,
- title: Stripe Services Agreement—Service Terms
- in context: … due to User under this Agreement, User will have recourse only against Stripe and not the relevant Customer. Stripe will promptly update User's Stripe Account balance to reflect processed Transactions. User has no rights to earnings generated by funds held in any Pooled Account and is not entitled to draw funds from any Pooled Account and has no rights to direct transactions into and out of any Pooled Accounts. 4.3 Transaction Settlement Funds. ⟪Stripe will transfer settlement funds for Transactions, net of Fees, Disputes, Refunds, Reversals and other amounts owed to Stripe, from the applicable Pooled Account to User in accordance with the applicable settlement method as follows,⟫ unless a Payout Delay occurs and affects the transfer initiation, or Stripe exercises a right under this Agreement to withhold or delay the transfer: (a) Settlement to User Bank Account. Where Stripe settles funds to a User Bank Account, Stripe will do so in accordance with the Payout Schedule. However, Stripe may impose an additional holding period before making the initial settlement to a User Bank Account. (b) Settlement to a Financial Accoun…

**Citation S01-WC-C152:** `https://stripe.com/legal/ssa-service-terms` | Stripe Payments: 4.3 Transaction Settlement Funds. | 2026-09-28 | kind: official page | quote check: found
- quote: unless a Payout Delay occurs and affects the transfer initiation, or Stripe exercises a right under this Agreement to withhold or delay the transfer:
- title, opening and note boxes: as for this source's citation above
- in context: …ated by funds held in any Pooled Account and is not entitled to draw funds from any Pooled Account and has no rights to direct transactions into and out of any Pooled Accounts. 4.3 Transaction Settlement Funds. Stripe will transfer settlement funds for Transactions, net of Fees, Disputes, Refunds, Reversals and other amounts owed to Stripe, from the applicable Pooled Account to User in accordance with the applicable settlement method as follows, ⟪unless a Payout Delay occurs and affects the transfer initiation, or Stripe exercises a right under this Agreement to withhold or delay the transfer:⟫ (a) Settlement to User Bank Account. Where Stripe settles funds to a User Bank Account, Stripe will do so in accordance with the Payout Schedule. However, Stripe may impose an additional holding period before making the initial settlement to a User Bank Account. (b) Settlement to a Financial Account. Where Stripe settles funds to User's Financial Account, User will be using Stripe Treasury Services subject to the Stripe Treasury Terms. (c) Settl…

### Q5-WC-042

**Cited at:** section 1, line 46; section 2, line 90

**Record** (`studies/proposals/records/Q5/woocommerce/statements.tsv`):
- stmt_id: Q5-WC-042
- bears_on: 5
- identifier: Using the FROD balance
- statement: In brief, the future refunds or disputes (FROD) balance is a special bucket of funds inside your WooPayments account.
- scope: WooPayments
- cite_ids: Q5-WC-C049
- from: held

**Citation Q5-WC-C049:** `https://woocommerce.com/document/woopayments/fees/account-showing-negative-balance/` | Using the FROD balance | 2026-09-25 | kind: stated | quote check: found
- quote: In brief, the future refunds or disputes (FROD) balance is a special bucket of funds inside your WooPayments account.
- title: Why is my account showing a negative balance? Documentation - WooCommerce
- in context: …ds or disputes. For low volume merchants though, negative balances may happen more often, since there are fewer new sales to help offset refunds or disputes. Recovering from a negative balance ↑ Back to top There are two ways to recover from a negative WooPayments account balance: using the future refunds or disputes (FROD) balance feature of your account, or allowing your default payout method to be debited. Using the FROD balance ↑ Back to top ⟪In brief, the future refunds or disputes (FROD) balance is a special bucket of funds inside your WooPayments account.⟫ One of the things it enables you to do is recover quickly from a negative account balance. Please see our guide to adding funds to your FROD balance for more information. Note that, by design, any existing FROD balance will be used up in order to prevent your account balance from going negative. As such, if you notice that your account balance is indeed negative, it's safe to assume that your FROD balance has been zeroed out. Using your default …

### Q5-WC-P0159

**Cited at:** section 1, line 47; section 8, line 211

**Record** (`studies/proposals/records/Q5/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-158
- bullet: d
- placement: responsible
- identifier: Stripe WooCommerce Extension (closing paragraph)
- statement: While we are unable to assist with Stripe account issues (including but not limited to payouts, disputes, and account verification), our amazing Happiness Engineers are standing by and ready to answer any questions.
- scope: Stripe extension
- cite_ids: S01-WC-C232
- from: new
- note: Recorded in the absence audit of S01-WC-G02.

**Citation S01-WC-C232:** `sharrwah-knowledge-map@a041738770887dd218075c8a7622fb28c825279b:evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/041-woocommerce.com/text.txt` | line 194: Stripe WooCommerce Extension (closing paragraph) | 2026-09-25 | kind: stated | quote check: found
- quote: While we are unable to assist with Stripe account issues (including but not limited to payouts, disputes, and account verification), our amazing Happiness Engineers are standing by and ready to answer any questions.
- in context: …form? How do I translate the payment form placeholder text? How do I change which payment icons are used? How can I send product data to Stripe as metadata? What hooks and filters are available for the Stripe payment gateway? How can I clean up the database after changing my Stripe account? Contacting support If you have questions about or problems with the Stripe extension that are not covered in our documentation above, please contact support. ⟪While we are unable to assist with Stripe account issues (including but not limited to payouts, disputes, and account verification), our amazing Happiness Engineers are standing by and ready to answer any questions.⟫ Was this guide helpful for you? Related Products Stripe Tax by Stripe Calculate and collect tax globally in your WooCommerce store, and file returns automatically anywhere you do business. Free download Free download Rated 2.6 out of 5 stars 2.6 (9) Klarna by Klarna Grow your business with increased sales and an enhanced shopping experience - at no extra cost. Free download Free download Rated 3.1 out of 5 stars 3.1 (32) ON THIS PAGE What can th…

### Q5-WC-P0056

**Cited at:** section 1, line 49; section 8, line 209

**Record** (`studies/proposals/records/Q5/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-055
- bullet: a;c
- placement: decides
- identifier: Buy now, pay later with WooPayments > Merchant experience
- statement: When the transaction is complete, your WooPayments account receive the entire purchase amount immediately. The important thing to keep in mind is that the customers are not paying you over time, they are paying the BNPL provider over time.
- scope: buy now, pay later payment methods (Affirm, Afterpay, Klarna) on WooPayments
- cite_ids: S01-WC-C059
- from: new

**Citation S01-WC-C059:** `https://woocommerce.com/document/woopayments/payment-methods/buy-now-pay-later/` | Merchant experience | 2026-09-29 | kind: stated | quote check: found
- quote: When the transaction is complete, your WooPayments account receive the entire purchase amount immediately. The important thing to keep in mind is that the customers are not paying you over time, they are paying the BNPL provider over time.
- title: Buy now, pay later with WooPayments Documentation - WooCommerce
- in context: …nder WooCommerce > Orders and Payments > Transactions, just like orders placed with cards. BNPL order in WooCommerce > Orders BNPL order in Payments > Transactions Orders paid via Klarna will have additional information on the Payments > Transactions page. This information includes: Category, which shares which Klarna payment method the customer chose. Preferred Locale, which provides locale information about the customer's country and language. ⟪When the transaction is complete, your WooPayments account receive the entire purchase amount immediately. The important thing to keep in mind is that the customers are not paying you over time, they are paying the BNPL provider over time.⟫ Customer country and currency WooPayments does not support cross-border/international transactions using BNPL methods. As such, not all of your customers will be able to pay via BNPL. Specifically, for them to be able to use BNPL methods, customers must: Use a billing country that matches your WooPayments account country, and Pay in the national currency of your account country, shown in the chart below. YOUR ACCOUNT COUNTRY TO USE BNPL, CUSTOME…

### Q5-WC-K0037

**Cited at:** section 1, line 50; section 2, line 56

**Record** (`studies/proposals/records/Q5/woocommerce/copied.tsv`):
- concern_id: WC-C-002
- placement: boundary
- structure: woocommerce-11.2.1:includes/gateways/bacs/class-wc-gateway-bacs.php
- identifier: woocommerce_bacs_process_payment_order_status
- statement: $process_payment_status = apply_filters( 'woocommerce_bacs_process_payment_order_status', OrderStatus::ON_HOLD, $order );
- scope: Direct bank transfer (bacs)
- cite_ids: WC-S-5004

**Citation WC-S-5004:** `woocommerce-11.2.1:includes/gateways/bacs/class-wc-gateway-bacs.php` | line 406 | 2026-10-09 | kind: shipped | quote check: found
- quote: $process_payment_status = apply_filters( 'woocommerce_bacs_process_payment_order_status', OrderStatus::ON_HOLD, $order );
- in context: …wp_kses_post( PHP_EOL . $account_html ) . '</section>'; } } } /** * Process the payment and return the result. * * @param int $order_id Order ID. * @return array */ public function process_payment( $order_id ) { $order = wc_get_order( $order_id ); if ( $order->get_total() > 0 ) { /** * Filter the order status for BACS payment. * * @since 3.4.0 * * @param string $default_status The default order status. * @param object $order The order object. */ ⟪$process_payment_status = apply_filters( 'woocommerce_bacs_process_payment_order_status', OrderStatus::ON_HOLD, $order );⟫ // Mark as on-hold (we're awaiting the payment). $order->update_status( $process_payment_status, __( 'Awaiting BACS payment.', 'woocommerce' ) ); } else { $order->payment_complete(); } // Remove cart if it still matches the order being processed. if ( $order instanceof WC_Order && WC()->cart && $order->has_cart_hash( WC()->cart->get_cart_hash() ) ) { WC()->cart->empty_cart(); } // Return thankyou redirect. return array( 'result' => 'success', 'r…

### Q5-WC-P0097

**Cited at:** section 1, line 51

**Record** (`studies/proposals/records/Q5/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-096
- bullet: end-payment
- placement: where
- identifier: Cash on Delivery
- statement: Cash on Delivery (COD) is a payment gateway that lets you take payments at the time of delivery of your customer’s ordered products.
- scope: Cash on delivery (COD)
- cite_ids: S01-WC-C103
- from: new

**Citation S01-WC-C103:** `https://woocommerce.com/document/cash-on-delivery/` | Cash on Delivery | 2025-05-31 | kind: stated | quote check: found
- quote: Cash on Delivery (COD) is a payment gateway that lets you take payments at the time of delivery of your customer’s ordered products.
- title: Cash on Delivery Documentation - WooCommerce
- in context: … Develop on Woo Hire an expert Get support $ USD Find extensions, themes, guides, and more Go to search results page Search Log inGet started WooCommerce WooCommerce Getting started Migrating to WooCommerce ProductsExpand Taxes ShippingExpand Payments Orders Data and reporting Customers Marketing Site administrationExpand Store designExpand Mobile AppExpand Get helpExpand Documentation / WooCommerce / Payments / Cash on Delivery Cash on Delivery ⟪Cash on Delivery (COD) is a payment gateway that lets you take payments at the time of delivery of your customer's ordered products.⟫ WooCommerce sets orders using Cash on Delivery (COD) to "Processing" until payment is collected. You, as the store owner, should confirm that payments for Cash on Delivery orders have been collected before setting orders to "Complete" in WooCommerce. If you are using the WooCommerce mobile app and a card reader to collect In-Person Payments, it marks orders "Complete" automatically at the time of payment. For more information see Managing Orders…

### Q5-WC-K0353

**Cited at:** section 2, line 64; section 2, line 71; section 7, line 161

**The same record as Q1-WC-K0353,** whose card is in `Q1-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: 1.2.10. ensure the Product is not a solution for processing or enabling payment transactions (“Payments Solution”). In order to make a Payments Solution available to Users of the Marketplace(s), Partner must enter into a separate agreement with Automattic and/or WooCommerce, as applicable.
- scope: 

### Q5-WC-K0402

**Cited at:** section 3, line 103; section 5, line 130; section 7, line 168

**The same record as Q1-WC-K0402,** whose card is in `Q1-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: NOTE: If you’re using WooPayments for a business, the relevant country is the one where your business is registered — not the one in which you personally live.
- scope: 

### Q5-WC-P0108

**Cited at:** section 7, line 167

**The same record as Q2-WC-P0108,** whose card is in `Q2-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: “Stripe” means the entity specified below for User's Stripe Account Country. Service Terms may address further additional or deviating Stripe entities for the respective Services. Americas Country / Region Stripe Contracting Entity United States Stripe, LLC Stripe Payments Company* Canada Stripe Payments Canada, Ltd.** Mexico Stripe Payments Mexico, S. de R.L. de C.V.** Brazil Stripe Brasil Soluções de Pagamento - Instituição de Pagamento Ltda** Other countries in the Americas, to the extent Stripe offers Services in these countries Stripe, LLC *This Stripe entity is an additional party to the Agreement if stated in the applicable Stripe Financial Services Terms, or in other applicable Service Terms. **Stripe, LLC is an additional party to this Agreement solely for the purposes of processing Personal Data under Section 4 (Privacy and Data Use) of this Agreement. Europe, Middle East and Africa Country / Region Stripe Contracting Entity Countries in the European Economic Area: Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden Stripe Payments Europe, Limited Stripe Technology Europe, Limited* Gibraltar, Switzerland, United Kingdom Stripe Payments Europe, Limited Stripe Payments UK Ltd* United Arab Emirates Stripe Payments Europe, Limited Other countries in Europe, Middle East and Africa, to the extent Stripe offers Services in these countries Stripe Payments Europe, Limited *This Stripe entity is an additional party to the Agreement if stated in the applicable Stripe Financial Services Terms, or in other applicable Service Terms. Asia Pacific Country / Region Stripe Contracting Entity Australia Stripe Payments Australia Pty Ltd.*** Hong Kong Stripe Payments Europe, Limited India Stripe India Private Ltd.*** Indonesia PT Stripe Payments Indonesia*** Japan Stripe Japan, Inc.*** Malaysia Stripe Payments Malaysia Sdn. Bhd.*** New Zealand Stripe New Zealand Limited*** Singapore Stripe Payments Singapore Pte. Ltd.*** Thailand Stripe Payments (Thailand) Ltd*** Other countries in Asia Pacific, to the extent Stripe offers Services in these countries Stripe Technology Company Limited***
- scope: Stripe Account Country

### Q5-WC-P0122

**Cited at:** section 8, line 176

**Record** (`studies/proposals/records/Q5/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-121
- bullet: a;end-payment
- placement: responsible
- identifier: Stripe Payments: 4.2 Pooled Accounts.
- statement: Once Stripe receives funds for a Transaction on User’s behalf, the relevant Customer has no further obligation to make payments to User with respect to that Transaction, regardless of whether and when Stripe settles those funds to User.
- cite_ids: S01-WC-C149
- from: new

**Citation S01-WC-C149:** `https://stripe.com/legal/ssa-service-terms` | Stripe Payments: 4.2 Pooled Accounts. | 2026-09-28 | kind: official page | quote check: found
- quote: Once Stripe receives funds for a Transaction on User’s behalf, the relevant Customer has no further obligation to make payments to User with respect to that Transaction, regardless of whether and when Stripe settles those funds to User.
- title: Stripe Services Agreement—Service Terms
- in context: …zed, fraudulent or illegal; or (z) exposes, or is likely to expose, Stripe, User or others to unacceptable risk. 4.2 Pooled Accounts. User appoints Stripe as User's agent for the limited purpose of directing, receiving, holding and settling funds under this Agreement. All settlement funds Stripe receives for Transactions are combined with settlement funds for other users and held in one or more Pooled Accounts at one or more Financial Providers. ⟪Once Stripe receives funds for a Transaction on User's behalf, the relevant Customer has no further obligation to make payments to User with respect to that Transaction, regardless of whether and when Stripe settles those funds to User.⟫ If Stripe does not settle funds due to User under this Agreement, User will have recourse only against Stripe and not the relevant Customer. Stripe will promptly update User's Stripe Account balance to reflect processed Transactions. User has no rights to earnings generated by funds held in any Pooled Account and is not entitled to draw funds from any Pooled Account and has no rights to direct transactions into and out of any Pooled Accounts. 4.…

### Q5-WC-P0027

**Cited at:** section 8, line 179

**Record** (`studies/proposals/records/Q5/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-026
- bullet: a;e;end-payout
- placement: decides
- identifier: WooPayments: Payouts > Payout methods
- statement: WooPayments can send payouts to a bank account (all countries) or a debit card (U.S. only).
- scope: WooPayments
- conditions: S01-WC-025
- cite_ids: S01-WC-C026
- from: new

**Citation S01-WC-C026:** `https://woocommerce.com/document/woopayments/payouts/` | Payout methods | 2026-09-25 | kind: stated | quote check: found
- quote: WooPayments can send payouts to a bank account (all countries) or a debit card (U.S. only).
- title: WooPayments: Payouts Documentation - WooCommerce
- in context: …ctsExpand Woo Marketplace Code SnippetsExpand Documentation / Products / WooPayments / WooPayments Documentation / WooPayments: Payouts WooPayments: Payouts This section explains how often your WooPayments account balance is paid out as well as how to manage those payouts. For information on how to view a list of your payouts or download them, please see our Managing Money page. The Payouts page listing past payouts. Payout methods ↑ Back to top ⟪WooPayments can send payouts to a bank account (all countries) or a debit card (U.S. only).⟫ We recommend using a bank account in every country, including the U.S. A bank account is better than a debit card for four reasons: Debit cards do not work outside the U.S. Debit cards have a maximum amount of money ($9,999 USD) that can be paid out at once, whereas bank accounts have no such limit. Debit cards cannot be debited if your account balance goes negative, which could prevent you from issuing timely refunds to your customers. If your …

### Q5-WC-P0023

**Cited at:** section 8, line 191

**Record** (`studies/proposals/records/Q5/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-022
- bullet: b
- placement: where
- identifier: Stripe WooCommerce Extension: What can the Stripe extension do?
- statement: Using a Stripe account, you can accept payments on your WooCommerce site without setup costs or monthly fees.
- scope: Stripe extension
- cite_ids: S01-WC-C022
- from: new

**Citation S01-WC-C022:** `https://woocommerce.com/document/stripe/` | What can the Stripe extension do? | 2026-09-25 | kind: stated | quote check: found
- quote: Using a Stripe account, you can accept payments on your WooCommerce site without setup costs or monthly fees.
- title: Stripe WooCommerce Extension Documentation - WooCommerce
- in context: …rt Product Designer WooCommerce Anti-Fraud Shipment Tracking Expand EU VAT Number Stripe / Documentation / Stripe WooCommerce Extension Stripe WooCommerce Extension Welcome to the documentation for the Stripe WooCommerce Extension! Here you can find all sorts of helpful information about accepting payments on your WooCommerce site via the Stripe extension. Please refer to the sections below for more information. What can the Stripe extension do? ⟪Using a Stripe account, you can accept payments on your WooCommerce site without setup costs or monthly fees.⟫ You can offer the following payment methods: Credit and debit cards (American Express, Visa, MasterCard, and more!) Express checkouts such as Apple Pay, WeChat Pay, and Cash App Pay Local payment methods such as Alipay, Boleto, SEPA, and more Buy now, pay later methods such as Affirm, Afterpay, and Klarna Machine learning to order enabled payment methods using Optimized Checkout Suite for checkout. Customers can pay in their preferred currency v…

### Q5-WC-P0033

**Cited at:** section 8, line 194

**Record** (`studies/proposals/records/Q5/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-032
- bullet: c
- placement: decides
- identifier: When will I receive payouts for my WooPayments account balance? > Pending funds
- statement: The time those funds take to flow through your account is called the “pending period”, and its length depends on your WooPayments account country.
- scope: WooPayments
- cite_ids: S01-WC-C032
- from: new

**Citation S01-WC-C032:** `https://woocommerce.com/document/woopayments/payouts/payout-schedule/` | Pending funds | 2026-08-21 | kind: stated | quote check: found
- quote: The time those funds take to flow through your account is called the “pending period”, and its length depends on your WooPayments account country.
- title: When will I receive payouts for my WooPayments account balance? Documentation - WooCommerce
- in context: …o be paid out yet. In other words, the three balances are calculated like so: Total Balance = Pending Funds + Available Funds See the sections below for more information on each bucket of funds. Pending funds When a WooPayments transaction occurs on your site, the money from that transaction takes some time to process before it becomes available to be paid out. During this time, the money is "pending" and is included in the Pending Funds amount. ⟪The time those funds take to flow through your account is called the "pending period", and its length depends on your WooPayments account country.⟫ This chart shows our standard pending periods. COUNTRY PENDING PERIOD Australia, United States 2 business days Japan, New Zealand 4 business days United Arab Emirates 5 business days Hong Kong, Singapore 7 calendar days All other countries 3 business days To illustrate how this works, consider the following examples: A U.S. merchant makes a sale on a Friday. Their pending period is 2 business days, so the merchant can expect the funds in their b…

### Q5-WC-P0113

**Cited at:** section 8, line 206

**Record** (`studies/proposals/records/Q5/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-112
- bullet: a
- placement: responsible
- identifier: Stripe Financial Services Terms: 5. Regional Terms, United States: 5.2 Reserves and Security Interest.
- statement: For the purposes of Sections 3.3 (Reserve) and 3.4 (Security Interest), Reserve funds are held in Reserve Accounts established by SPC, and User grants the security interest to SPC (as agent for each other Secured Party and for the benefit of itself and the other Secured Parties).
- scope: Users in the United States
- cite_ids: S01-WC-C134
- from: new

**Citation S01-WC-C134:** `https://stripe.com/legal/ssa-service-terms` | Stripe Financial Services Terms: 5. Regional Terms, United States, 5.2 Reserves and Security Interest. | 2026-09-28 | kind: official page | quote check: found
- quote: For the purposes of Sections 3.3 (Reserve) and 3.4 (Security Interest), Reserve funds are held in Reserve Accounts established by SPC, and User grants the security interest to SPC (as agent for each other Secured Party and for the benefit of itself and the other Secured Parties).
- title: Stripe Services Agreement—Service Terms
- in context: …r U.S. Law. To the extent that User's use of the Services involves money transmission or other regulated services under U.S. Law, Stripe's Affiliate, Stripe Payments Company ("SPC") provides those regulated Services, and the SPC terms located on or accessible from the Stripe Legal Page will apply to User, unless the applicable Service Terms specify otherwise. Stripe is not a bank, and does not accept deposits. 5.2 Reserves and Security Interest. ⟪For the purposes of Sections 3.3 (Reserve) and 3.4 (Security Interest), Reserve funds are held in Reserve Accounts established by SPC, and User grants the security interest to SPC (as agent for each other Secured Party and for the benefit of itself and the other Secured Parties).⟫ European Economic Area. The following Regional Terms apply for Users in the European Economic Area. 5.1 Provision of Regulated Financial Services. Stripe Technology Europe, Limited ("Stripe PSP") is an additional party to this Agreement solely for the purposes of (a) providing Regulated Financial Services; and (b) acting as a Payment Method Acquirer. Each reference in this Agreement to "Stripe" means Stripe Payments Europe, Limited, except to th…
