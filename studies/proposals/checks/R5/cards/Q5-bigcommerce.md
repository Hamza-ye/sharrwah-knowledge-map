# Cards: Q5 on bigcommerce

29 records cited by `studies/proposals/drafts/Q5/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - The merchant turns methods on, from those offered to its store: Shopify's buyers pay with "any of the methods that you've activated"; Salla's merchant presses (تفعيل) on its طرق الدفع page; BigCommerce's uses Settings › Payments; WooCommerce's gateways carry an "Enable/Disable" box; Zid's merchant turns networks on in إدارة زد باي. They match by role, on stated pages and WooCommerce's shipped code. Q5-SH-K1524, Q5-SA-017, Q5-BC-066, Q5-WC-K0032, Q5-ZD-K0041
- **section 1, line 9:** - The merchant's own rules then decide what a buyer sees, matching by role: Salla's قيود الدفع hide a method or reject or review the order by amount, country, customer group or category; Zid's restrictions hide a method; Shopify's Payment Customization lets an app "rename, reorder, hide the payment methods"; WooCommerce keeps cash on delivery to chosen shipping methods (shipped code); BigCommerce's merchant ticks "the countries where this payment method is available at checkout". Q5-SA-043, Q5-SA-046, Q5-ZD-013, Q5-SH-K1761, Q5-WC-004, Q5-BC-P0121
- **section 1, line 10:** - Shopify, Zid and Salla limit methods by the store's country, matching by role: Shopify filters providers "based on your store's address"; Zid offers options "حسب دولتك", and زد باي only in Saudi Arabia and Kuwait; Salla's مدى and فيزا are "مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط". WooCommerce goes by country only in its suggestions, "The payment extension list for each country" (shipped code), and BigCommerce by the shopper's "geolocation" for local methods (stated; not checked on WooCommerce). Q5-SH-012, Q5-ZD-001, Q5-ZD-P0113, Q5-SA-036, Q5-WC-K0054, Q5-BC-081
- **section 1, line 14:** - The platform approves what plugs in, matching by role: at Shopify "Only approved Partners can build payments extensions", and a new method "must be submitted for review and approval"; Zid reviews apps "before publishing it to the public"; "The Marketplace team reviews all app submissions" (BigCommerce). These are stated pages but Shopify's partner terms (official). Q5-SH-K1696, Q5-SH-062, Q5-SH-058, Q5-ZD-K0363, Q5-BC-K0316
- **section 1, line 15:** - Fees can follow the provider: BigCommerce's Open Payment Provider fee falls on orders not processed through its Embedded list; in Shopify's store fake-demo-sharrwah (countryCode YE), observed on 5 October 2026, ONERWAY (Direct) in test mode showed a "0.6% transaction fee". A fee that depends on the provider was not in what was read on WooCommerce or Zid. Q5-BC-085, Q5-SH-086, Q5-WC-N08, Q5-ZD-N10
- **section 1, line 17:** - Providers decide on the merchant and the buyer, matching by role: at BigCommerce "Each provider has its own application process"; at Salla a provider can reject the merchant's request (dashboard text as captured on 8 October 2026, observed), and "تحدد تابي أهلية العميل أو الطلب لاستخدام الخدمة"; Zid's electronic payment needs the gateway's approval; Shopify's Adyen needs "an existing Adyen approval". Q5-BC-P0048, Q5-SA-057, Q5-SA-066, Q5-ZD-K0003, Q5-SH-071
- **section 1, line 23:** - Each platform has a payment service of its own, run through other companies, matching by role: Shopify Payments, processed and settled by "one or more Payment Processors"; WooPayments, "powered by Stripe"; Salla's, provided "عبر شركائها"; BigCommerce Payments, "powered by PayPal"; and زد باي, through "مقدمي خدمات الدفع". These are official pages but BigCommerce's (stated). Q5-SH-K1555, Q5-WC-K0008, Q5-SA-P0079, Q5-BC-P0055, Q5-ZD-P0003
- **section 1, line 24:** - Other companies' gateways, matching by role: Shopify's "over 100 credit card payment providers"; Salla's بوابات الدفع الأخرى (not checked on WooCommerce); Zid's بوابات الدفع الأُخرى; BigCommerce's providers on and off its Embedded list; WooCommerce's gateways, "created as additional plugins". Q5-SH-006, Q5-SA-K1638, Q5-ZD-K0084, Q5-BC-036, Q5-WC-K0007
- **section 1, line 25:** - Methods recorded outside any provider: Shopify's "manual payments"; BigCommerce's "offline payment methods"; WooCommerce's Offline type, where "No online payment is made"; Salla's طرق دفع أخرى; Zid's bank transfer. BigCommerce and WooCommerce match by the same term, offline; the others by role. In Shopify's store ibx5bt-xy (countryCode YE), observed on 30 September 2026, Cash on Delivery (COD), Money Order and Bank Deposit each carried `"group":"MANUAL"`. Q5-SH-027, Q5-BC-060, Q5-WC-016, Q5-SA-015, Q5-ZD-P0075, Q5-SH-083
- **section 1, line 26:** - Providers plug in as add-ons, matching by role: Shopify's "payments extensions"; WooCommerce's gateway classes, added "through traditional plugins"; Zid's Open APIs model for "partners / payment service providers (PSPs)"; BigCommerce's "app payment processors"; Salla's apps, through "the Recurring Payments API". Q5-SH-K1694, Q5-WC-K0006, Q5-ZD-K0077, Q5-BC-031, Q5-SA-064
- **section 1, line 27:** - Where the buyer pays: Shopify's "direct providers and external providers", the latter on a page outside the store; WooCommerce's Direct type, with payment fields "directly on the checkout page"; Zid's Open APIs, where in one checkout type "Zid will draw the payment form"; BigCommerce's gateways that "redirect shoppers to a hosted payment page". Shopify and WooCommerce match by the same term, direct; Zid and BigCommerce by role. Q5-SH-007, Q5-WC-016, Q5-ZD-K0080, Q5-BC-068
- **section 1, line 31:** - The platform may withdraw what it offers, mostly without notice, matching by role: Salla's agreement reserves "الحق في إلغاء أو تعديل أو تغيير أي من وسائل الدفع"; Shopify may disable third-party services "without notice to you", and so may BigCommerce; WooCommerce may "suspend or remove a Product from the Marketplace(s)" (vendor agreement, stated); زد باي "قد توقف أو تلغي الحساب في أي وقت". The others are official pages. Q5-SA-001, Q5-SH-K2168, Q5-BC-K0455, Q5-WC-K0462, Q5-ZD-010
- **section 1, line 32:** - Some give notice: BigCommerce's Embedded list changes with "advance notice of any changes"; Shopify's merchants moving to new integrations get "a notification and a banner in your admin" (not checked on WooCommerce). Q5-BC-102, Q5-SH-021
- **section 1, line 42:** - Through the platform's own service, money goes into a balance, then to the merchant's bank account, matching by role on stated pages and Zid's terms (official): Salla's "رصيد المدفوعات الإلكترونية" comes before the transfer to the bank account; Zid's terms add "المبلغ المستحق لرصيد التاجر" after fees; WooPayments adds the payment "(minus our fees)" to the balance; BigCommerce Payments and Shopify Payments pay out to the merchant's bank account. Q5-SA-P0006, Q5-ZD-P0024, Q5-WC-P0024, Q5-BC-P0074, Q5-SH-P0060
- **section 1, line 43:** - Who holds it in between, matching by role: Shopify's merchant opens "financial accounts and/or cryptocurrency wallets with one or more Payment Processors"; Stripe, as the merchant's agent, holds WooPayments' funds "in one or more Pooled Accounts at one or more Financial Providers"; BigCommerce Payments' transactions "flow through your new BigCommerce Payments account" (stated). For Salla and Zid, the entity, licence or account under which the balance is held was not in what was read. Q5-SH-P0010, Q5-WC-P0121, Q5-BC-P0052, Q5-SA-H0002, Q5-ZD-H0002
- **section 1, line 44:** - When it is paid out, and at what level: Salla by plan, from weekly on Plus to daily on Special; Zid by country; WooPayments daily, "the default for almost all accounts", changeable per account; BigCommerce Payments holds a new account's initial payments "for up to 21 days". They match by role; the level differs. Q5-SA-P0020, Q5-SA-P0022, Q5-ZD-P0041, Q5-WC-P0036, Q5-BC-P0083
- **section 1, line 47:** - Through a gateway the merchant connects, money goes to the merchant's own account with it, matching by role: funds are in "your merchant account with your merchant service provider" (BigCommerce); "the purchase amount is transferred to your merchant account" (Shopify); Salla's dashboard text, as captured on 8 October 2026, collects through the gateway "بدلًا من مدفوعات سلة" (observed); "المدفوعات توصل لحسابك مباشرة" (Zid's Paymob page). Where the money is held between the buyer's payment and its transfer was not in what was read on Shopify. WooCommerce says only that it is "unable to assist with Stripe account issues", payouts among them: a statement of no part, naming no one. Q5-BC-P0089, Q5-SH-P0050, Q5-SA-K1639, Q5-ZD-P0107, Q5-SH-N02, Q5-WC-P0159
- **section 1, line 49:** - Pay-later providers pay the merchant directly, or into the platform's own service: at Salla (UAE help), "تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة"; at Zid, "تقوم تابي بالدفع للمتاجر مباشرة"; with BigCommerce's PayPal Pay Later, "you, the merchant, always get paid"; these match by role. Shopify and WooCommerce differ: Shop Pay Installments payouts "are included with your Shopify Payments payouts", and WooPayments receives "the entire purchase amount immediately". Q5-SA-P0102, Q5-ZD-P0077, Q5-BC-P0095, Q5-SH-K1686, Q5-WC-P0056
- **section 1, line 50:** - With methods outside any provider, the buyer pays the merchant and the order waits, matching by role: Salla's customer transfers "مباشرة من حسابه البنكي إلى حسابك"; BigCommerce's pay "directly into your bank account"; the order is "marked as unpaid" (Shopify), in "Awaiting Payment" (BigCommerce), or on hold, `OrderStatus::ON_HOLD` in WooCommerce's shipped code. In Shopify's store demo-fake-dev-store (countryCode YE), observed on 30 September 2026, the order then read "You manually marked YER699.95 as paid for this order." Q5-SA-P0099, Q5-BC-P0116, Q5-SH-K1736, Q5-BC-P0115, Q5-WC-K0037, Q5-SH-093
- **section 2, line 55:** - **Payment method**: in Sharrwah's proposed design, a way a buyer can pay an order, such as a card network, a wallet, pay later, bank transfer or cash on delivery: either a **provider method**, which a payment provider processes, or a **manual method**, which the buyer pays to the merchant outside any provider and the merchant records; an order paid by a manual method waits, unpaid, until then. Q5-SH-027, Q5-BC-P0115, Q5-WC-016
- **section 2, line 56:** - It draws on the five platforms' split between provider and manual methods, and on the waiting order of Shopify, BigCommerce and WooCommerce. Q5-SH-083, Q5-BC-060, Q5-SA-015, Q5-ZD-P0075, Q5-SH-K1736, Q5-WC-K0037
- **section 2, line 57:** - Why: rule 3; an order's payment state depends on its method's kind, so the kind is in the data model from the start. Q5-SH-K1736, Q5-BC-P0115
- **section 2, line 58:** - **Payment provider**: a company that processes provider methods and pays the money out, recorded once with the methods it carries, the places it serves, its money route and its terms. A method may come from several providers, a provider carry several methods. Q5-SH-001, Q5-BC-079, Q5-SA-K1654
- **section 2, line 59:** - It draws on Shopify's cards through "Shopify Payments, a third-party provider, or both together", BigCommerce's alternative methods offered "through a cooperating payment gateway", and Salla's K net, which hangs on Tap. Q5-SH-001, Q5-BC-079, Q5-SA-K1654
- **section 2, line 61:** - **Provider integration**: the code through which a provider plugs into Sharrwah, behind one payments interface: a **built-in integration**, which Sharrwah builds and keeps, or a **payments add-on**, which a provider or partner builds to Sharrwah's published interface, and which merchants can activate only once Sharrwah has reviewed it and it reports itself ready, a new method in it being reviewed again. The interface serves payment on Sharrwah's checkout and on the provider's page. Q5-BC-105, Q5-SH-K1696, Q5-SH-058
- **section 2, line 62:** - It draws on BigCommerce's Embedded Providers; Shopify's approved payments extensions, review of new methods and readiness step; Zid's Open APIs and app review; and the direct and hosted payment of Shopify, WooCommerce and BigCommerce. Q5-BC-105, Q5-SH-062, Q5-ZD-K0077, Q5-ZD-K0363, Q5-SH-007, Q5-WC-016, Q5-BC-068
- **section 2, line 65:** - **Provider account**: the merchant's own account with a provider, connected with the credentials of an account it holds, or applied for through Sharrwah. The provider decides each application; Sharrwah shows its state: applied, approved, rejected or connected. Q5-SA-053, Q5-SA-057, Q5-BC-P0048
- **section 2, line 66:** - It draws on Salla's choice between an existing account and a request the provider may reject, the own account Zid's pay-later providers need, BigCommerce's application and underwriting, and Shopify's apps, where the merchant may "log in or create an account with the payment provider". Q5-SA-053, Q5-SA-057, Q5-ZD-P0080, Q5-BC-P0048, Q5-SH-053
- **section 2, line 67:** - Why: rule 3; whose account receives the money fixes the money route and the contract. An account applied for through Sharrwah may count as one opened through Sharrwah, under the guard (section 5). Q5-BC-P0048, Q5-SA-053
- **section 2, line 73:** - It draws on the activation and payments permissions the platforms show, Shopify's owner-only provider change and one card provider at a time, BigCommerce's change log, Salla's market selector and BigCommerce's methods per currency. Q5-SH-K0193, Q5-SA-K1509, Q5-BC-072, Q5-SA-016, Q5-BC-074
- **section 2, line 77:** - It draws on Salla's قيود الدفع, Zid's restrictions, Shopify's Payment Customization, WooCommerce's cash on delivery by shipping method and BigCommerce's countries per offline method. Q5-SA-046, Q5-ZD-013, Q5-SH-K1761, Q5-WC-004, Q5-BC-P0121
- **section 2, line 79:** - **Payment record**: each payment on an order, with its method, provider, the provider's reference, amount, currency, state (awaiting, paid, recorded by the merchant, refunded) and money route. A refund goes back through the provider that took the payment, which stays callable for that after it leaves checkout. Q5-SH-015, Q5-WC-033, Q5-BC-085
- **section 2, line 80:** - It draws on BigCommerce's attribution of each order "to the provider that processed it", Shopify's earlier provider kept for returns (and store fake-demo-sharrwah on 30 September 2026, observed), WooCommerce's six months, and Shopify's manual mark as paid. Q5-BC-085, Q5-SH-015, Q5-SH-098, Q5-WC-033, Q5-SH-093
- **section 2, line 82:** - **Money route**: for each provider, and for manual methods, the path the buyer's money takes to the merchant's own bank account. On the **direct route**, it goes to the merchant's own account with the provider, or straight from buyer to merchant; Sharrwah never holds it, and its records show the payment, not the payout. On the **held route**, it waits in a **merchant balance**, held before payout by a payment company in an account opened through Sharrwah, or by Sharrwah itself. This proposal provides for the held route, in its data model and as a later part; under the founder's guard, it goes live nowhere without the founder's decision. Q5-BC-P0089, Q5-SA-K1639, Q5-SA-P0006
- **section 2, line 91:** - **Provider withdrawal**: what Sharrwah does when a provider or method stops at a place. Sharrwah removes it from the place's list and checkout after notice to the stores using it, unless the provider or a regulator ends it at once; methods carried only by that provider go with it; the merchant is asked to choose another provider; the integration stays callable for refunds and disputes on earlier payments; an add-on's developer keeps it working through a wind-down period; and, on a held route, the balance left is paid out. Q5-BC-102, Q5-SH-015, Q5-SA-K1654
- **section 2, line 92:** - It draws on BigCommerce's and Shopify's notice, P24's ending, Shopify's earlier provider kept for returns and its Wind Down Period, WooCommerce's six months, and the payout of the balance left at WooCommerce and Zid. Q5-BC-102, Q5-SH-021, Q5-WC-013, Q5-SH-K1704, Q5-WC-033, Q5-WC-K0715, Q5-ZD-P0042
- **section 2, line 94:** - Not taken: withdrawal without notice, which Shopify's, BigCommerce's and Salla's terms reserve, because a method withdrawn under the merchants leaves orders that "fail at checkout", as P24's did. Q5-SH-K2168, Q5-BC-K0455, Q5-SA-001, Q5-WC-015
- **section 3, line 98:** - Payment providers plug in, through a built-in integration or a payments add-on, as on all five platforms. Q5-SH-K1694, Q5-WC-K0006, Q5-ZD-K0077, Q5-BC-031, Q5-BC-105
- **section 3, line 99:** - Methods plug in through the providers that carry them. Q5-BC-079, Q5-SH-001
- **section 3, line 105:** - Approval of the merchant is set per provider account, and a buyer's or order's eligibility per order, by the provider. Q5-BC-P0048, Q5-SA-066
- **section 3, line 107:** - Activated methods, and the one provider for each, are set per store, and per market or currency where the store has them, by staff holding the payments permission. Q5-SH-K1524, Q5-SA-016, Q5-BC-074, Q5-SH-K0193
- **section 3, line 110:** - A provider's money route is set by its own terms; which routes may run at a place, by Sharrwah, and any held route by the founder. Q5-BC-P0089, Q5-SA-K1639
- **section 3, line 112:** - A fee that depends on the provider would be set by Sharrwah, if it decides on one, per order, by the provider that processed it. Q5-BC-085
- **section 3, line 113:** - Withdrawal is set per provider and place by Sharrwah; per add-on by its developer, within its wind-down terms, or by Sharrwah for a breach; and per method by the provider. Q5-BC-102, Q5-SH-K1704, Q5-SH-066, Q5-WC-013
- **section 5, line 129:** - Whether a provider account applied for through Sharrwah is one opened through Sharrwah under the guard, where that provider holds the merchant's money before paying it out. The design records how each account was opened. The founder settles it. Q5-SA-053, Q5-BC-P0048
- **section 5, line 132:** - How a payment is completed: on Sharrwah's checkout, on the provider's page, or, as at YemenPay, by a transfer the buyer makes from its own wallet, matched afterwards. The design keeps the payments interface open to a payment confirmed after checkout. The providers chosen for each place (section 7) settle it. YA-112 (the buyer's own transfer, matched by an app on the merchant's phone @ YemenPay's service, as of 2026-08-22), Q5-SH-007, Q5-BC-068
- **section 5, line 134:** - A fee that depends on the provider: the design keeps the provider on every payment record. A company decision settles it. Q5-BC-085, Q5-WC-N08
- **section 7, line 159:** - Whether Sharrwah offers a payment service of its own in which sellers' money is held, by Sharrwah or by a payment company in an account opened through Sharrwah, and with which company: for the founder, under the guard. Q5-SH-K1555, Q5-WC-P0121, Q5-BC-P0069, Q5-SA-H0002, Q5-ZD-H0002
- **section 7, line 160:** - Which payment providers Sharrwah works with at each place, and on what terms: notice before withdrawal, refunds after it, settlement time, and service when a provider is down. Q5-BC-102, Q5-SH-064, Q5-WC-033, Q5-BC-G0048
- **section 7, line 162:** - Whether Sharrwah charges a fee that depends on the provider an order was paid through, and whether its fees are taken from payments or billed apart. Q5-BC-085, Q5-SH-086, Q5-WC-N08, Q5-ZD-N10
- **section 7, line 166:** - Sharrwah's own terms with merchants and providers, for the founder with a lawyer: whether a merchant's dealings with a provider are a contract of their own, whether Sharrwah acts for the merchant in any part of a payment, any security interest over sellers' money on a held route, and who answers for card data security. The platforms' terms show only what each requires of its sellers. Q5-SA-005, Q5-BC-K0453, Q5-BC-099, Q5-SH-P0002, Q5-SH-P0024
- **section 8, line 173:** - Records: Shopify's financial services provider, Stripe's pooled accounts and BigCommerce Payments' account hold it; Salla's (UAE help) and Zid's balances hold sales proceeds before payout, but who holds either balance was not in what was read; a connected gateway pays the merchant's own account. S01-VP-01, Q5-SH-P0033, Q5-WC-P0121, Q5-BC-P0052, Q5-SA-P0057, Q5-ZD-P0035, Q5-SA-H0002, Q5-ZD-H0002, Q5-BC-P0089
- **section 8, line 176:** - Records: Shopify Payments' processors, Stripe for WooPayments, and BigCommerce Payments' PayPal platform account settle; Zid's terms credit "المبلغ المستحق لرصيد التاجر" after fees; who settles Salla's payments was not in what was read. S01-VP-02, Q5-SH-K1555, Q5-WC-P0122, Q5-BC-P0070, Q5-ZD-P0024, Q5-SA-H0004
- **section 8, line 179:** - Records: Shopify sends Shopify Payments' payouts, processed by partners, in the United States and France; WooPayments sends them to a bank account; Salla's dashboard text, as captured on 8 October 2026, lists transfers "من سلة إلى حسابك البنكي" (observed); Zid deposits on set days by country; BigCommerce Payments pays out to a linked bank or PayPal account. S01-VP-03, Q5-SH-P0076, Q5-WC-P0027, Q5-SA-P0040, Q5-ZD-P0041, Q5-BC-P0074
- **section 8, line 182:** - Records: the own services' processors (Shopify Payments; BigCommerce Payments, "powered by PayPal"); a connected gateway, at Salla "بدلًا من مدفوعات سلة" (dashboard text as captured on 8 October 2026, observed); the merchant, for Salla's bank transfer; and Zid, for cash on delivery through its shipping. S01-VP-04, Q5-SH-K1555, Q5-BC-P0055, Q5-SA-K1639, Q5-SA-P0099, Q5-ZD-P0070
- **section 8, line 185:** - Records: Shopify is the merchant's agent "to deliver information and instructions on your behalf"; Stripe, "for the limited purpose of directing, receiving, holding and settling funds"; Zid executes "payment processes on their behalf" (official pages); Salla passes label amounts on the merchant's behalf (dashboard text as captured on 8 October 2026, observed). BigCommerce's "No agency" statement is one of no part, naming no one; no reading rests on it. S01-VP-06, Q5-SH-P0002, Q5-WC-P0121, Q5-ZD-P0008, Q5-SA-P0126, Q5-BC-P0129
- **section 8, line 191:** - Records: Shopify's merchant opens accounts with Payment Processors; WooCommerce's Stripe extension uses the merchant's Stripe account; BigCommerce Payments creates a PayPal platform account per store; Zid's pay-later providers need an account with them; in Salla's store real-merchant, observed on 12 October 2026, the wallet listed "Electronic Payments" and "Cash on Delivery Payments". S01-VP-11, Q5-SH-P0010, Q5-WC-P0023, Q5-BC-P0069, Q5-ZD-P0080, Q5-SA-075
- **section 8, line 194:** - Records: by plan at Salla, by country at Zid, by account country for WooPayments' "pending period"; up to 21 days for a new BigCommerce Payments account's first payments; at most 5 days for Shopify's payment apps to settle. S01-VP-15, Q5-SA-P0020, Q5-ZD-P0041, Q5-WC-P0033, Q5-BC-P0083, Q5-SH-064
- **section 8, line 209:** - Records: with BigCommerce's PayPal Pay Later the shopper owes PayPal, while the merchant will "always get paid"; WooPayments receives "the entire purchase amount immediately"; Shop Pay Installments come with Shopify Payments payouts; Tabby pays Zid's stores directly and collects Salla's payments itself (UAE help). S01-VP-22, Q5-BC-P0095, Q5-WC-P0056, Q5-SH-K1686, Q5-ZD-P0077, Q5-SA-P0102
- **section 8, line 211:** - Of the pilot review's open findings: no reading here rests on a statement of no part, nor on WooCommerce's policy pages, whose standing among its terms stays open. S01-VP-06, S01-VP-03, Q5-BC-P0129, Q5-WC-P0159

## The cards

### Q5-BC-066

**Cited at:** section 1, line 7

**Record** (`studies/proposals/records/Q5/bigcommerce/statements.tsv`):
- stmt_id: Q5-BC-066
- bears_on: 1;3
- identifier: Digital Wallets; Settings › Payments
- statement: Note that the Amazon Pay, Apple Pay, and Google Pay digital wallets have a unique setup experience and are found under the Digital Wallets section of Settings › Payments.
- cite_ids: Q5-BC-C068
- from: held

**Citation Q5-BC-C068:** `https://support.bigcommerce.com/s/article/Available-Payment-Gateways?language=en_US` | Alternative Payment Methods and Digital Wallets | 2026-10-13 | kind: stated | quote check: found
- quote: Note that the Amazon Pay, Apple Pay, and Google Pay digital wallets have a unique setup experience and are found under the Digital Wallets section of Settings › Payments.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …ment gateway, APMs can include payment types such as: bank transfers "buy now, pay later" (BNPL) cash payments digital wallets direct debit mobile payments Digital wallet APMs allow shoppers to complete purchases by signing into a third-party account, bypassing the need to create a separate account or re-enter payment information. This streamlines the checkout experience, boosts conversion rates, and provides a better mobile shopping experience. ⟪Note that the Amazon Pay, Apple Pay, and Google Pay digital wallets have a unique setup experience and are found under the Digital Wallets section of Settings › Payments.⟫ For a full list of available APMs, digital wallets, and their supported gateways, see Introduction to Alternative Payment Methods. Accelerated Checkout Solutions Accelerated Checkout solutions remove friction from checkout by offering a passwordless checkout experience. When using an Accelerated Checkout, shoppers are prompted to securely save their information with the provider. Once they have an account, shoppers receive a one-time passcode to…

### Q5-BC-P0121

**Cited at:** section 1, line 9; section 2, line 77

**The same record as Q4-BC-P0121,** whose card is in `Q4-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Available Countries — Check the box for the countries where this payment method is available at checkout.
- scope: the countries the merchant checks for each offline payment method

### Q5-BC-081

**Cited at:** section 1, line 10

**Record** (`studies/proposals/records/Q5/bigcommerce/statements.tsv`):
- stmt_id: Q5-BC-081
- bears_on: 1
- identifier: local payment methods
- statement: Once enabled, local payment methods have country and currency prerequisites that ensure shoppers will see only the local payment methods applicable for their geolocation.
- cite_ids: Q5-BC-C085
- from: held

**Citation Q5-BC-C085:** `https://support.bigcommerce.com/s/article/Intro-to-APMs` | Benefits of Alternative Payment Methods: SELLING INTERNATIONALLY | 2026-10-13 | kind: stated | quote check: found
- quote: Once enabled, local payment methods have country and currency prerequisites that ensure shoppers will see only the local payment methods applicable for their geolocation.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: … by auto-filling their credentials and billing information. By enabling APMs alongside your existing payment gateways, you enhance the variety of options and ease-of-use of your store's customer experience. SELLING INTERNATIONALLY APMs are a valuable tool when selling your products outside the US. The popularity of payment gateways differs greatly by region and country, and many shoppers expect to see region-specific payment options at checkout. ⟪Once enabled, local payment methods have country and currency prerequisites that ensure shoppers will see only the local payment methods applicable for their geolocation.⟫ Including region-specific APMs that shoppers both recognize and trust will help you expand your global customer base. Types of APMs "Alternative payment methods" is a blanket term that covers a variety of payment methods. Each APM can be classified as one of the following types, each with its own distinct advantages: Bank transfers - Bank transfer APMs allow shoppers to complete transactions from a bank account instead of entering in credit card…

### Q5-BC-K0316

**Cited at:** section 1, line 14

**Record** (`studies/proposals/records/Q5/bigcommerce/copied.tsv`):
- concern_id: BC-C-059
- placement: decides
- structure: Developer docs: App Store Approval Requirements
- identifier: Marketplace team
- statement: The Marketplace team reviews all app submissions and tests apps to verify they meet App Marketplace listing standards.
- cite_ids: BC-S-0325

**Citation BC-S-0325:** `https://docs.bigcommerce.com/developer/docs/integrations/apps/guide/approval-requirements.md` | App Store Approval Requirements | 2026-10-12 | kind: stated | quote check: found (markup removed)
- quote: The Marketplace team reviews all app submissions and tests apps to verify they meet App Marketplace listing standards.
- title: App Store Approval Requirements
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. The Marketplace team reviews all app submissions and tests apps to verify they meet App Marketplace listing standards. Verify your app meets the requirements below before submitting it for approval. G…
- headings: App Store Approval Requirements
- in context: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. App Store Approval Requirements ⟪The Marketplace team reviews all app submissions and tests apps to verify they meet App Marketplace listing standards.⟫ Verify your app meets the requirements below before submitting it for approval. General requirements * Make support resources available throughout the app, like during onboarding and on the app's dashboard within the BigCommerce iframe. * Follow branding guidelines when referencing BigCommerce (see our Media Kit for more information). Don't reference competitor platforms in the app's listing information or dashboard. - Use the same app name in a…  (matched markup removed)

### Q5-BC-085

**Cited at:** section 1, line 15; section 2, line 79; section 2, line 80; section 3, line 112; section 5, line 134; section 7, line 162

**Record** (`studies/proposals/records/Q5/bigcommerce/statements.tsv`):
- stmt_id: Q5-BC-085
- bears_on: 1;3
- identifier: OPEN PAYMENT PROVIDER FEES
- statement: On self-serve plans, an Open Payment Provider fee is applied to orders, both online and offline, that are not processed through providers on the Embedded Payment Providers list. The fee is determined at the order level, meaning each order is attributed to the provider that processed it. Stores on a contracted Performance plan and orders processed through an Embedded Payment Provider are not subject to the fee.
- cite_ids: Q5-BC-C096;Q5-BC-C097
- from: held

**Citation Q5-BC-C096:** `https://support.bigcommerce.com/s/article/Pricing` | OPEN PAYMENT PROVIDER FEES | 2026-10-13 | kind: official page | quote check: found
- quote: On self-serve plans, an Open Payment Provider fee is applied to orders, both online and offline, that are not processed through providers on the Embedded Payment Providers list. The fee is determined at the order level, meaning each order is attributed to the provider that processed it.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …MV exceeding the threshold, not your total GMV for the month. This means costs scale predictably with your sales volume, which is particularly useful for businesses with seasonal variability. Fees are billed monthly in arrears (after the service period) as a separate line item on your invoice. Core and Growth plans automatically upgrade when you reach their GMV threshold, so there are no overage charges on these plans. OPEN PAYMENT PROVIDER FEES ⟪On self-serve plans, an Open Payment Provider fee is applied to orders, both online and offline, that are not processed through providers on the Embedded Payment Providers list. The fee is determined at the order level, meaning each order is attributed to the provider that processed it.⟫ Stores on a contracted Performance plan and orders processed through an Embedded Payment Provider are not subject to the fee. Orders processed externally to the BigCommerce platform are also subject to the fee. This includes orders placed using offline payment methods, orders originating from marketplaces like eBay or Etsy, orders processed through a point-of-sale (POS) app, and orders created via the API. Note that custom integrations to proces…

**Citation Q5-BC-C097:** `https://support.bigcommerce.com/s/article/Pricing` | OPEN PAYMENT PROVIDER FEES | 2026-10-13 | kind: official page | quote check: found
- quote: Stores on a contracted Performance plan and orders processed through an Embedded Payment Provider are not subject to the fee.
- title, opening and note boxes: as for this source's citation above
- in context: …voice. Core and Growth plans automatically upgrade when you reach their GMV threshold, so there are no overage charges on these plans. OPEN PAYMENT PROVIDER FEES On self-serve plans, an Open Payment Provider fee is applied to orders, both online and offline, that are not processed through providers on the Embedded Payment Providers list. The fee is determined at the order level, meaning each order is attributed to the provider that processed it. ⟪Stores on a contracted Performance plan and orders processed through an Embedded Payment Provider are not subject to the fee.⟫ Orders processed externally to the BigCommerce platform are also subject to the fee. This includes orders placed using offline payment methods, orders originating from marketplaces like eBay or Etsy, orders processed through a point-of-sale (POS) app, and orders created via the API. Note that custom integrations to processors on the Embedded Payment Provider list, including those connected via third-party apps, will also incur Open Payment Provi…

### Q5-BC-P0048

**Cited at:** section 1, line 17; section 2, line 65; section 2, line 66; section 2, line 67; section 3, line 105; section 5, line 129

**The same record as Q1-BC-P0048,** whose card is in `Q1-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Each provider has its own application process. 3. Apply and configure Apply with your chosen provider, complete underwriting, then add them in your BigCommerce dashboard under Store Setup, Payments.
- scope: 

### Q5-BC-P0055

**Cited at:** section 1, line 23; section 8, line 182

**Record** (`studies/proposals/records/Q5/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-054
- bullet: e
- placement: decides
- identifier: BigCommerce Payments: US customers on Core, Growth, and Scale plans
- statement: BigCommerce Payments is here: an embedded payment solution, powered by PayPal, now available directly in your BigCommerce control panel for US customers on Core, Growth, and Scale plans.
- scope: US customers on Core, Growth, and Scale plans
- conditions: S01-BC-051
- cite_ids: S01-BC-C071
- from: new

**Citation S01-BC-C071:** `https://www.bigcommerce.com/blog/bigcommerce-payments-announcement/` | introduction after Key highlights | 2026-03-31 | kind: stated | quote check: found
- quote: BigCommerce Payments is here: an embedded payment solution, powered by PayPal, now available directly in your BigCommerce control panel for US customers on Core, Growth, and Scale plans.
- title: BigCommerce Payments Announcement | BigCommerce | BigCommerce
- in context: …an start accepting payments without adding another tool. Manage your balances, payouts, and bank connections with PayPal from a single dashboard inside BigCommerce. Give customers more ways to pay with cards: PayPal and Venmo ready at checkout. Offer flexible Buy Now, Pay Later options with PayPal Pay Later, Klarna, and Afterpay, built right in. Let shoppers check out faster with Apple Pay, Google Pay, and Fastlane by PayPal included by default. ⟪BigCommerce Payments is here: an embedded payment solution, powered by PayPal, now available directly in your BigCommerce control panel for US customers on Core, Growth, and Scale plans.⟫ For the first time, manage payments natively in BigCommerce. Accept payments, manage payouts, track your balance, and handle bank connections with PayPal without ever leaving your store. Payments and your store, finally in one place From the perspective of most customers, payments live outside your storefront. You process an order in BigCommerce, then open a separate tab to check your balance, issue a payout, or investigate a transaction. Contex…

### Q5-BC-036

**Cited at:** section 1, line 24

**Record** (`studies/proposals/records/Q5/bigcommerce/statements.tsv`):
- stmt_id: Q5-BC-036
- bears_on: 1;3
- identifier: Open Payment Providers
- statement: Processing payments through methods outside of the Embedded Payment Provider list will incur Open Payment Provider fees for stores on self-serve plans. Performance plan stores operating under contracted terms are not subject to this fee.
- cite_ids: Q5-BC-C038
- from: held

**Citation Q5-BC-C038:** `https://support.bigcommerce.com/s/article/Available-Payment-Gateways?language=en_US` | Open Payment Providers | 2026-10-13 | kind: stated | quote check: found
- quote: Processing payments through methods outside of the Embedded Payment Provider list will incur Open Payment Provider fees for stores on self-serve plans. Performance plan stores operating under contracted terms are not subject to this fee.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: … ✔ PayPal ✔ ✔ ✔ ✔ ✔ ✔ Sezzle ✔ ✔ ✔ Stripe UPE ✔ ✔ ✔ ✔ ✔ Stripe OCS ✔ ✔ ✔ ✔ ✔ TD Online Mart ✔ ✔ ✔ ✔ ✔ Worldpay B2B Payments ✔ ✔ ✔ Worldpay Ecomm ✔ ✔ Worldpay Core ✔ ✔ Zip ✔ ✔ ✔ APP PAYMENT PROCESSORS In addition to the above payment gateway integrations, the following app payment processors are also Embedded Payment Providers: Acumatica Payments Payfabric (Global Payments) Bankful Sezzle Fortis Worldpay WPG Klarna Checkout Open Payment Providers ⟪Processing payments through methods outside of the Embedded Payment Provider list will incur Open Payment Provider fees for stores on self-serve plans. Performance plan stores operating under contracted terms are not subject to this fee.⟫ See each gateway's documentation for details such as requirements, limitations, setup instructions, supported countries and currencies, and additional features. Using a "Powered By" store? If you were onboarded to BigCommerce through a partner, you may not have access to all listed payment gateways. Manual Capture - Authorized payments can be captured manually at a later date. 3D Secure - An additional security layer that helps prevent unauthori…

### Q5-BC-060

**Cited at:** section 1, line 25; section 2, line 56

**Record** (`studies/proposals/records/Q5/bigcommerce/statements.tsv`):
- stmt_id: Q5-BC-060
- bears_on: 3
- identifier: OFFLINE PAYMENT METHODS
- statement: In addition to the above payment gateway integrations, orders processed using offline payment methods are also subject to the Open Payment Provider fee.
- cite_ids: Q5-BC-C062
- from: held

**Citation Q5-BC-C062:** `https://support.bigcommerce.com/s/article/Available-Payment-Gateways?language=en_US` | Open Payment Providers: OFFLINE PAYMENT METHODS | 2026-10-13 | kind: stated | quote check: found
- quote: In addition to the above payment gateway integrations, orders processed using offline payment methods are also subject to the Open Payment Provider fee.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …nce ✔ ✔ ✔ ✔ ✔ ✔ BitPay ✔ ✔ Chase Merchant Services ✔ ✔ ✔ ✔ ✔ Clover Payments ✔ Commonwealth Bank ✔ ✔ ✔ ✔ Cybersource ✔ ✔ ✔ ✔ ✔ ✔ Electronic Payment Exchange (EPX) ✔ ✔ Eway Rapid ✔ ✔ Mercado Pago ✔ ✔ ✔ Moneris ✔ ✔ ✔ MyVirtualMerchant ✔ ✔ Nexi XPay ✔ ✔ ✔ ✔ ✔ NMI ✔ ✔ Opayo by Elavon ✔ ✔ ✔ ✔ ✔ Optty ✔ ✔ QuickBooks Payments ✔ ✔ Serve First ✔ Square ✔ ✔ ✔ ✔ Tilopay ✔ ✔ ✔ ✔ ✔ USAePay ✔ Windcave ✔ ✔* ✔ ✔ *See article for details. OFFLINE PAYMENT METHODS ⟪In addition to the above payment gateway integrations, orders processed using offline payment methods are also subject to the Open Payment Provider fee.⟫ Bank deposit Money order Cash on delivery Pay in-store Check* *B2B Edition adopts the Check offline payment method to enable the Purchase Order (PO) payment method. Note that Performance plan stores operating under contracted terms are not subject to the Open Payment Provider fee. Alternative Payment Methods and Digital Wallets Alternative Payment Methods (APMs) are payment options that often do not require a major credit card scheme such as Vis…

### Q5-BC-031

**Cited at:** section 1, line 26; section 3, line 98

**Record** (`studies/proposals/records/Q5/bigcommerce/statements.tsv`):
- stmt_id: Q5-BC-031
- bears_on: 3
- identifier: APP PAYMENT PROCESSORS
- statement: In addition to the above payment gateway integrations, the following app payment processors are also Embedded Payment Providers:
- cite_ids: Q5-BC-C033
- from: held

**Citation Q5-BC-C033:** `https://support.bigcommerce.com/s/article/Available-Payment-Gateways?language=en_US` | Embedded Payment Providers: APP PAYMENT PROCESSORS | 2026-10-13 | kind: stated | quote check: found
- quote: In addition to the above payment gateway integrations, the following app payment processors are also Embedded Payment Providers:
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: … Affirm ✔ ✔ Afterpay ✔ ✔ ✔ Amazon Pay ✔ ✔ ✔ ✔ Bankful ✔ ✔ Bank of New Zealand ✔ ✔ ✔ ✔ BigCommerce Payments ✔ ✔ ✔ ✔ ✔ BlueSnap Direct ✔ ✔ ✔ ✔ ✔ ✔ Braintree ✔ ✔ ✔ ✔ ✔ ✔ Checkout.com ✔ ✔ ✔ ✔ ✔ Clearpay ✔ Heartland Payment Systems ✔ ✔ Klarna Payments ✔ ✔ ✔ PayPal ✔ ✔ ✔ ✔ ✔ ✔ Sezzle ✔ ✔ ✔ Stripe UPE ✔ ✔ ✔ ✔ ✔ Stripe OCS ✔ ✔ ✔ ✔ ✔ TD Online Mart ✔ ✔ ✔ ✔ ✔ Worldpay B2B Payments ✔ ✔ ✔ Worldpay Ecomm ✔ ✔ Worldpay Core ✔ ✔ Zip ✔ ✔ ✔ APP PAYMENT PROCESSORS ⟪In addition to the above payment gateway integrations, the following app payment processors are also Embedded Payment Providers:⟫ Acumatica Payments Payfabric (Global Payments) Bankful Sezzle Fortis Worldpay WPG Klarna Checkout Open Payment Providers Processing payments through methods outside of the Embedded Payment Provider list will incur Open Payment Provider fees for stores on self-serve plans. Performance plan stores operating under contracted terms are not subject to this fee. See each gateway's documentation for details such as requirements, limitations, setup inst…

### Q5-BC-068

**Cited at:** section 1, line 27; section 2, line 62; section 5, line 132

**Record** (`studies/proposals/records/Q5/bigcommerce/statements.tsv`):
- stmt_id: Q5-BC-068
- bears_on: 3
- identifier: Embedded Checkout; hosted gateways
- statement: Note that hosted gateways are not compatible with Embedded Checkout on headless storefronts. In addition, most APMs and digital wallets do not support Embedded Checkout as they redirect shoppers to a hosted payment page.
- cite_ids: Q5-BC-C071
- from: held

**Citation Q5-BC-C071:** `https://support.bigcommerce.com/s/article/Available-Payment-Gateways?language=en_US` | FAQ: What is a hosted payment gateway? | 2026-10-13 | kind: stated | quote check: found
- quote: Note that hosted gateways are not compatible with Embedded Checkout on headless storefronts. In addition, most APMs and digital wallets do not support Embedded Checkout as they redirect shoppers to a hosted payment page.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …s is where you will connect to your bank account or perform refunds external to BigCommerce. What is a hosted payment gateway? Hosted payment gateways navigate shoppers away from your checkout to the payment service provider's page. After entering their payment details and completing the transaction, they are redirected back to your storefront. Hosted payment gateways: Afterpay Amazon Pay BitPay Klarna Mercado Pago Opayo Optty Serve First Sezzle ⟪Note that hosted gateways are not compatible with Embedded Checkout on headless storefronts. In addition, most APMs and digital wallets do not support Embedded Checkout as they redirect shoppers to a hosted payment page.⟫ APMs and digital wallets that support Embedded Checkout: Google Pay PayPal Pay Later Do any payment gateways support Level 2 and Level 3 data? Yes, several gateways support the use of Level 2 and Level 3 data. For more information, see Using Level 2 and Level 3 Data in BigCommerce. Do any payment gateways support the selling of regulated products, such as firearms, e-cigs, or CBD? The following gateways may allow the sale of regulated items. Bef…

### Q5-BC-K0455

**Cited at:** section 1, line 31; section 2, line 94

**Record** (`studies/proposals/records/Q5/bigcommerce/copied.tsv`):
- concern_id: BC-C-084
- placement: decides
- structure: Master Services Agreement
- identifier: Third-Party Products
- statement: Commerce does not guarantee the availability of Third-Party Products and you acknowledge that Commerce may disable access to any Third-Party Products at any time and for any reason in its sole discretion without notice to you.
- cite_ids: BC-S-0462

**Citation BC-S-0462:** `https://www.commerce.com/terms/` | Third-Party Product Integration | 2026-06-01 | kind: official page | quote check: found
- quote: Commerce does not guarantee the availability of Third-Party Products and you acknowledge that Commerce may disable access to any Third-Party Products at any time and for any reason in its sole discretion without notice to you.
- title: Master Services Agreement | Commerce
- in context: …rovider. In some instances, Commerce may receive revenue from third-parties that Commerce recommends or that you otherwise engage with through the use of our services. We provide no warranties and make no representations with respect to any third-party. The availability of Third-Party Products on Commerce's mobile application and Services does not constitute or imply an endorsement, authorization, sponsorship, or affiliation by or with Commerce. ⟪Commerce does not guarantee the availability of Third-Party Products and you acknowledge that Commerce may disable access to any Third-Party Products at any time and for any reason in its sole discretion without notice to you.⟫ Commerce is not responsible or liable to anyone for discontinuation of the Third-Party Products. Hosting Services. Commerce has entered into arrangements with one or more third parties for hosting services that are essential to the Services, incorporated within the Services and without which the Services could not be provided to you. Entire Agreement. This Agreement is the entire agreement between Commerce and Customer regarding Customer's use o…

### Q5-BC-102

**Cited at:** section 1, line 32; section 2, line 91; section 2, line 92; section 3, line 113; section 7, line 160

**Record** (`studies/proposals/records/Q5/bigcommerce/statements.tsv`):
- stmt_id: Q5-BC-102
- bears_on: 4
- identifier: 21 Embedded Payment Providers
- statement: The list may evolve over time. Your business will receive advance notice of any changes.
- cite_ids: Q5-BC-C121
- from: held
- note: The copy Q5-BC-K0144 says of the list on the pricing page that it "may change over time".

**Citation Q5-BC-C121:** `https://www.bigcommerce.com/payments/embedded-payment-providers/` | 21 Embedded Payment Providers | 2026-10-13 | kind: stated | quote check: found
- quote: The list may evolve over time. Your business will receive advance notice of any changes.
- title: Embedded Payment Providers | BigCommerce
- in context: …ower rates. The fee applies only to GMV processed through Open Payment Providers. Plan Open Payment Provider Fee Core 2.0% on Open Payment Provider GMV Growth 1.0% on Open Payment Provider GMV Scale 0.6% on Open Payment Provider GMV Performance Zero Open Payment Provider Fees 21 Embedded Payment Providers Orders processed through any of these 21 providers are not subject to the Open Payment Provider Fee, based on current partner classifications. ⟪The list may evolve over time. Your business will receive advance notice of any changes.⟫ Adyen Affirm Afterpay Amazon Pay Bank of New Zealand Bankful (Pinwheel) BigCommerce Payments BlueSnap (powered by Payroc) Checkout.com Clearpay Fortis (Acumatica Payments) Global Payments Klarna PayPal Braintree PayPal Complete Payments PayPal Wallet Sezzle Stripe TD Online Mart Worldpay Zip Money 1Visit FAQs for more details 2Open Payment Provider Fee rates apply once your store moves to the new plan structure (as early as June 1, 2026). Your p…

### Q5-BC-P0074

**Cited at:** section 1, line 42; section 8, line 179

**Record** (`studies/proposals/records/Q5/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-073
- bullet: c;end-payout
- placement: decides
- identifier: Balance Dashboard: Automatic payouts
- statement: You can enable automatic payouts from your BigCommerce Payments balance to a linked bank account or PayPal account. To begin, click Set up auto payments in the upper-right of the dashboard or at the top of the Payouts section. In the pop-up window, select a payout frequency. By default, automatic payouts are transferred to your PayPal account. To switch to a bank account, click Change and link a new account or select an existing one. Note that your entire balance transfers when using automatic payouts. To transfer specific values, perform a manual payout.
- cite_ids: S01-BC-C104;S01-BC-C105;S01-BC-C106
- from: new

**Citation S01-BC-C104:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 348: Balance Dashboard, Automatic payouts | 2026-10-13 | kind: stated | quote check: found
- quote: You can enable automatic payouts from your BigCommerce Payments balance to a linked bank account or PayPal account. To begin, click Set up auto payments in the upper-right of the dashboard or at the top of the Payouts section.
- in context: … five business days. VIEWING PAYOUTS In the Payouts section, you can view your payouts and manage manual and automatic payouts. The payouts list shows your most recent payouts, click Load More to display additional lines. To change which payouts are displayed, click Filter. In the pop-up window, you can select a different time frame (past 7, 30, 90, and 365 days), select a specific currency, and set a minimum or maximum amount. AUTOMATIC PAYOUTS ⟪You can enable automatic payouts from your BigCommerce Payments balance to a linked bank account or PayPal account. To begin, click Set up auto payments in the upper-right of the dashboard or at the top of the Payouts section.⟫ In the pop-up window, select a payout frequency. By default, automatic payouts are transferred to your PayPal account. To switch to a bank account, click Change and link a new account or select an existing one. Note that your entire balance transfers when using automatic payouts. To transfer specific values, perform a manual payout. Refunds are issued from your BigCommerce Payments balance. Payouts may reduce your available balance below the amo…

**Citation S01-BC-C105:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 350: Balance Dashboard, Automatic payouts | 2026-10-13 | kind: stated | quote check: found
- quote: In the pop-up window, select a payout frequency. By default, automatic payouts are transferred to your PayPal account. To switch to a bank account, click Change and link a new account or select an existing one.
- in context: …ange which payouts are displayed, click Filter. In the pop-up window, you can select a different time frame (past 7, 30, 90, and 365 days), select a specific currency, and set a minimum or maximum amount. AUTOMATIC PAYOUTS You can enable automatic payouts from your BigCommerce Payments balance to a linked bank account or PayPal account. To begin, click Set up auto payments in the upper-right of the dashboard or at the top of the Payouts section. ⟪In the pop-up window, select a payout frequency. By default, automatic payouts are transferred to your PayPal account. To switch to a bank account, click Change and link a new account or select an existing one.⟫ Note that your entire balance transfers when using automatic payouts. To transfer specific values, perform a manual payout. Refunds are issued from your BigCommerce Payments balance. Payouts may reduce your available balance below the amount to be refunded. Before performing a refund, check the Balance dashboard to ensure that you have sufficient funds. MANUAL PAYOUTS You can perform manual payouts from your BigCommerce Payments balance to a lin…

**Citation S01-BC-C106:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 352: Balance Dashboard, Automatic payouts | 2026-10-13 | kind: stated | quote check: found
- quote: Note that your entire balance transfers when using automatic payouts. To transfer specific values, perform a manual payout.
- in context: …TIC PAYOUTS You can enable automatic payouts from your BigCommerce Payments balance to a linked bank account or PayPal account. To begin, click Set up auto payments in the upper-right of the dashboard or at the top of the Payouts section. In the pop-up window, select a payout frequency. By default, automatic payouts are transferred to your PayPal account. To switch to a bank account, click Change and link a new account or select an existing one. ⟪Note that your entire balance transfers when using automatic payouts. To transfer specific values, perform a manual payout.⟫ Refunds are issued from your BigCommerce Payments balance. Payouts may reduce your available balance below the amount to be refunded. Before performing a refund, check the Balance dashboard to ensure that you have sufficient funds. MANUAL PAYOUTS You can perform manual payouts from your BigCommerce Payments balance to a linked bank account. To begin, click Payout Now in the upper-right of the dashboard or at the top of the Payouts section. In th…

### Q5-BC-P0052

**Cited at:** section 1, line 43; section 8, line 173

**Record** (`studies/proposals/records/Q5/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-051
- bullet: a;b
- placement: where
- identifier: BigCommerce Payments account; linked PayPal account
- statement: When you connect to BigCommerce Payments, you create a new BigCommerce Payments account. Your all-in-one Money Dashboard. PayPal powers the payment processing behind the scenes through your linked PayPal account, but all transactions made through BigCommerce Payments flow through your new BigCommerce Payments account for simplified management.
- cite_ids: S01-BC-C067;S01-BC-C068
- from: new

**Citation S01-BC-C067:** `https://www.bigcommerce.com/blog/bigcommerce-payments-announcement/` | Payments and your store, finally in one place | 2026-03-31 | kind: stated | quote check: found
- quote: When you connect to BigCommerce Payments, you create a new BigCommerce Payments account.
- title: BigCommerce Payments Announcement | BigCommerce | BigCommerce
- in context: … BigCommerce, then open a separate tab to check your balance, issue a payout, or investigate a transaction. Context switching adds up quickly and can create blind spots in knowing your business. BigCommerce Payments is built to close that gap. Powered by PayPal, it brings payment processing directly into the BigCommerce control panel through a co-branded integration that builds on more than a decade of partnership between BigCommerce and PayPal. ⟪When you connect to BigCommerce Payments, you create a new BigCommerce Payments account.⟫ Your all-in-one Money Dashboard. PayPal powers the payment processing behind the scenes through your linked PayPal account, but all transactions made through BigCommerce Payments flow through your new BigCommerce Payments account for simplified management. The centerpiece of that experience is a new Money dashboard, which gives you real-time access to balance insights, top-ups, payouts, bank connections, and currency management. Everything inclu…

**Citation S01-BC-C068:** `https://www.bigcommerce.com/blog/bigcommerce-payments-announcement/` | Payments and your store, finally in one place | 2026-03-31 | kind: stated | quote check: found
- quote: PayPal powers the payment processing behind the scenes through your linked PayPal account, but all transactions made through BigCommerce Payments flow through your new BigCommerce Payments account for simplified management.
- title, opening and note boxes: as for this source's citation above
- in context: …ing adds up quickly and can create blind spots in knowing your business. BigCommerce Payments is built to close that gap. Powered by PayPal, it brings payment processing directly into the BigCommerce control panel through a co-branded integration that builds on more than a decade of partnership between BigCommerce and PayPal. When you connect to BigCommerce Payments, you create a new BigCommerce Payments account. Your all-in-one Money Dashboard. ⟪PayPal powers the payment processing behind the scenes through your linked PayPal account, but all transactions made through BigCommerce Payments flow through your new BigCommerce Payments account for simplified management.⟫ The centerpiece of that experience is a new Money dashboard, which gives you real-time access to balance insights, top-ups, payouts, bank connections, and currency management. Everything included in BigCommerce Payments BigCommerce Payments is designed to match the full capabilities customers already rely on with PayPal - everything accessible from a single interface. Here is what's included at launch: Supported payment methods. Credit and debit…

### Q5-BC-P0083

**Cited at:** section 1, line 44; section 8, line 194

**Record** (`studies/proposals/records/Q5/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-082
- bullet: c
- placement: decides
- identifier: FAQ: Note: initial payments are held for up to 21 days
- statement: Note: For new BigCommerce Payments accounts, initial payments are held for up to 21 days before being available for payout. For more information, see PayPal’s New PayPal account – payments on hold and accessing your money quicker.
- scope: new BigCommerce Payments accounts
- cite_ids: S01-BC-C122;S01-BC-C123
- from: new
- note: The same note is at lines 463, 593 and 637.

**Citation S01-BC-C122:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 593: FAQ, Transactions (also at line 463, General) | 2026-10-13 | kind: stated | quote check: found
- quote: Note: For new BigCommerce Payments accounts, initial payments are held for up to 21 days before being available for payout. For more information, see PayPal’s New PayPal account – payments on hold and accessing your money quicker.
- in context: …al. Nothing about it changes. Your new BigCommerce Payments account is what processes and settles all transactions made through your BigCommerce store going forward. You can view your BigCommerce Payments account through your Balance dashboard. You can also access it by logging in to your PayPal account, clicking your business name in the upper left, and in the pop-up window, clicking on your BigCommerce Payments account under Platform accounts. ⟪Note: For new BigCommerce Payments accounts, initial payments are held for up to 21 days before being available for payout. For more information, see PayPal's New PayPal account - payments on hold and accessing your money quicker.⟫ I linked the wrong PayPal account. How do I switch my configuration to the correct account? To switch the PayPal account that is linked to BigCommerce Payments, you must disconnect your current configuration and reconnect the BigCommerce Payments integration. To disconnect BigCommerce Payments, go to Settings › Payments and select the appropriate currency from the drop-down list. Under the Embedded tab, click Online Payment Methods, then click t…

**Citation S01-BC-C123:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 637: FAQ, Troubleshooting and support | 2026-10-13 | kind: stated | quote check: found
- quote: For new BigCommerce Payments accounts, initial payments are held for up to 21 days before being available for payout. For more information, see PayPal’s New PayPal account – payments on hold and accessing your money quicker.
- in context: …thing about it changes. Your new BigCommerce Payments account is what processes and settles all transactions made through your BigCommerce store going forward. You can view your BigCommerce Payments account through your Balance dashboard. You can also access it by logging in to your PayPal account, clicking your business name in the upper left, and in the pop-up window, clicking on your BigCommerce Payments account under Platform accounts. Note: ⟪For new BigCommerce Payments accounts, initial payments are held for up to 21 days before being available for payout. For more information, see PayPal's New PayPal account - payments on hold and accessing your money quicker.⟫ I linked the wrong PayPal account. How do I switch my configuration to the correct account? To switch the PayPal account that is linked to BigCommerce Payments, you must disconnect your current configuration and reconnect the BigCommerce Payments integration. To disconnect BigCommerce Payments, go to Settings › Payments and select the appropriate currency from the drop-down list. Under the Embedded tab, click Online Payment Methods, then click t…

### Q5-BC-P0089

**Cited at:** section 1, line 47; section 2, line 82; section 3, line 110; section 8, line 173

**Record** (`studies/proposals/records/Q5/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-088
- bullet: a;b
- placement: where
- identifier: FAQ: Where do I manage my funds?
- statement: Where do I manage my funds? You will control and direct funds in your merchant account with your merchant service provider. Usually, this is where you will connect to your bank account or perform refunds external to BigCommerce.
- cite_ids: S01-BC-C138;S01-BC-C139
- from: new

**Citation S01-BC-C138:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/002-support.bigcommerce.com/text.txt` | line 231: FAQ | 2026-10-13 | kind: stated | quote check: found
- quote: Where do I manage my funds?
- in context: …t their payments will be speedy and secure. This can encourage repeat purchases and increase your conversion rate. The following Accelerated Checkout solutions are available in BigCommerce: Stripe Link - Supported by the Stripe payment gateways; offer a streamlined checkout experience for any shopper with a Link profile. Fastlane by PayPal - Fastlane by PayPal provides merchants with a fast, passwordless checkout solution for guest shoppers. FAQ ⟪Where do I manage my funds?⟫ You will control and direct funds in your merchant account with your merchant service provider. Usually, this is where you will connect to your bank account or perform refunds external to BigCommerce. What is a hosted payment gateway? Hosted payment gateways navigate shoppers away from your checkout to the payment service provider's page. After entering their payment details and completing the transaction, they are redirected back to your storef…

**Citation S01-BC-C139:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/002-support.bigcommerce.com/text.txt` | line 233: FAQ | 2026-10-13 | kind: stated | quote check: found
- quote: You will control and direct funds in your merchant account with your merchant service provider. Usually, this is where you will connect to your bank account or perform refunds external to BigCommerce.
- in context: …edy and secure. This can encourage repeat purchases and increase your conversion rate. The following Accelerated Checkout solutions are available in BigCommerce: Stripe Link - Supported by the Stripe payment gateways; offer a streamlined checkout experience for any shopper with a Link profile. Fastlane by PayPal - Fastlane by PayPal provides merchants with a fast, passwordless checkout solution for guest shoppers. FAQ Where do I manage my funds? ⟪You will control and direct funds in your merchant account with your merchant service provider. Usually, this is where you will connect to your bank account or perform refunds external to BigCommerce.⟫ What is a hosted payment gateway? Hosted payment gateways navigate shoppers away from your checkout to the payment service provider's page. After entering their payment details and completing the transaction, they are redirected back to your storefront. Hosted payment gateways: Afterpay Amazon Pay BitPay Klarna Mercado Pago Opayo Optty Serve First Sezzle Note that hosted gateways are not compatible with Embedded Checkout on headless storefronts.…

### Q5-BC-P0095

**Cited at:** section 1, line 49; section 8, line 209

**Record** (`studies/proposals/records/Q5/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-094
- bullet: c;end-payment;end-payout
- placement: decides
- identifier: PayPal Pay Later
- statement: PayPal Pay Later lets customers buy now and pay over time. This feature means that the shopper will owe the money to PayPal while you, the merchant, always get paid.
- scope: PayPal Pay Later
- cite_ids: S01-BC-C151;S01-BC-C152;S01-BC-C153
- from: new
- note: The same words are in the PayPal, BigCommerce Payments and Braintree articles.

**Citation S01-BC-C151:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/003-support.bigcommerce.com/text.txt` | line 200: PayPal Pay Later | 2026-10-13 | kind: stated | quote check: found
- quote: PayPal Pay Later lets customers buy now and pay over time. This feature means that the shopper will owe the money to PayPal while you, the merchant, always get paid.
- in context: …log into your PayPal sandbox account. Note that this account is separate from your PayPal business account. If you don't have one already, you'll need to create one. Enable test mode on store - Check to use PayPal's sandbox to test transactions on your store. To return to processing live transactions, uncheck the box and click Save. If you need to switch to a different PayPal sandbox account, click Change PayPal sandbox account. PayPal Pay Later ⟪PayPal Pay Later lets customers buy now and pay over time. This feature means that the shopper will owe the money to PayPal while you, the merchant, always get paid.⟫ PayPay Pay Later also includes messaging banners that inform your customers of the installment options available at checkout. This can encourage larger purchases and increase your average order value (AOV). Note that PayPal Pay Later is displayed as PayPal Pay in 4 for AU stores, PayPal Pay in 4X for FR stores, PayPal Pay in 3 for UK, IT, and ES stores, and PayPal Ratenzahlung for DE stores. Requirements Pay Later button Customizing Pay Later me…

**Citation S01-BC-C152:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 269: PayPal Pay Later | 2026-10-13 | kind: stated | quote check: found
- quote: PayPal Pay Later lets customers buy now and pay over time. This feature means that the shopper will owe the money to PayPal while you, the merchant, always get paid.
- in context: …y the color of error messaging. Form fields Background Color - Enter a hex code to specify the color of input fields. Text Color Base - Enter a hex code to specify the color of input text. Border Color - Enter a hex code to specify the color of the input field borders. Focus Border Base - Enter a hex code to specify the color of the input field borders when highlighted. PayPal Pay Later Customizing Pay Later messaging Pay Later messaging preview ⟪PayPal Pay Later lets customers buy now and pay over time. This feature means that the shopper will owe the money to PayPal while you, the merchant, always get paid.⟫ PayPay Pay Later also includes messaging banners that inform your customers of the installment options available at checkout. This can encourage larger purchases and increase your average order value (AOV). Did you know? On stores based in the United Kingdom, PayPal Pay Later will be displayed to shoppers as PayPal Pay in 3. Under Buy Now, Pay Later, click Configure Pay Later messaging to customize the appearance of the Pay Later banners and the…

**Citation S01-BC-C153:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/005-support.bigcommerce.com/text.txt` | line 275: PayPal Pay Later | 2026-10-13 | kind: stated | quote check: found
- quote: PayPal Pay Later lets customers buy now and pay over time. This feature means that the shopper will owe the money to PayPal while you, the merchant, always get paid.
- in context: …l Fastlane by PayPal provides merchants with a fast, passwordless checkout solution for guest shoppers. With Fastlane, shoppers create a payment profile after making a credit card or PayPal payment, then use that profile on future orders to complete checkout with a single click. See Fastlane by PayPal to learn more about Fastlane's requirements and setup instructions. PayPal Pay Later Requirements Pay Later button Customizing Pay Later messaging ⟪PayPal Pay Later lets customers buy now and pay over time. This feature means that the shopper will owe the money to PayPal while you, the merchant, always get paid.⟫ PayPay Pay Later also includes messaging banners that inform your customers of the installment options available at checkout. This can encourage larger purchases and increase your average order value (AOV). Note that PayPal Pay Later is displayed as PayPal Pay in 4 for AU stores, PayPal Pay in 4X for FR stores, PayPal Pay in 3 for UK, IT, and ES stores, and PayPal Ratenzahlung for DE stores. REQUIREMENTS Store requirements Your store must be loc…

### Q5-BC-P0116

**Cited at:** section 1, line 50

**Record** (`studies/proposals/records/Q5/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-115
- bullet: a;end-payment
- placement: where
- identifier: Configuring Offline Payment Methods: Bank deposit
- statement: You can set up your store to allow your customers to make a payment directly into your bank account by setting up a Bank Deposit payment method. This payment method displays your bank account information and instructions to your customer after their order is complete.
- cite_ids: S01-BC-C200
- from: new

**Citation S01-BC-C200:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/006-support.bigcommerce.com/text.txt` | line 125: Configuring Offline Payment Methods, Bank deposit | 2026-10-13 | kind: stated | quote check: found
- quote: You can set up your store to allow your customers to make a payment directly into your bank account by setting up a Bank Deposit payment method. This payment method displays your bank account information and instructions to your customer after their order is complete.
- in context: … account. Enabling Offline Payment Methods To set up an offline payment method, go to Settings › Payments and select a currency from the drop-down list. Click the Open tab, and expand Offline Payment Methods. Click the Set up button next to the offline method that you want to use. On the next page, configure your selected payment method. Configuring Offline Payment Methods Bank deposit Cash on delivery Check Money order Pay in store BANK DEPOSIT ⟪You can set up your store to allow your customers to make a payment directly into your bank account by setting up a Bank Deposit payment method. This payment method displays your bank account information and instructions to your customer after their order is complete.⟫ In the Bank Deposit tab, enter your preferences in the fields below. Display Name - Enter what will your customers see this option called during checkout. Available Countries - Check the box for the countries where this payment method is available at checkout. Account Information - Enter all the bank account information necessary for the shopper to make a bank deposit payment. This text will appear on the order confirmation page and in the confi…

### Q5-BC-P0115

**Cited at:** section 1, line 50; section 2, line 55; section 2, line 57

**The same record as Q4-BC-P0115,** whose card is in `Q4-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Orders placed using an offline payment method are placed in Awaiting Payment order status. After receiving the payment, you can manually set the order to the Awaiting Fulfillment or another order status as you process the order.
- scope: 

### Q5-BC-079

**Cited at:** section 2, line 58; section 2, line 59; section 3, line 99

**Record** (`studies/proposals/records/Q5/bigcommerce/statements.tsv`):
- stmt_id: Q5-BC-079
- bears_on: 3
- identifier: alternative payment methods (APMs)
- statement: In contrast with traditional payment methods, APMs are typically offered through a cooperating payment gateway. For example, ACH Direct Debit is enabled through Adyen or BlueSnap Direct as opposed to a standalone integration.
- cite_ids: Q5-BC-C082
- from: held

**Citation Q5-BC-C082:** `https://support.bigcommerce.com/s/article/Intro-to-APMs` | Introduction to Alternative Payment Methods | 2026-10-13 | kind: stated | quote check: found
- quote: In contrast with traditional payment methods, APMs are typically offered through a cooperating payment gateway. For example, ACH Direct Debit is enabled through Adyen or BlueSnap Direct as opposed to a standalone integration.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: … global audience and improve international conversions. APMs range from digital wallets available around the world, such as Apple Pay and Google Pay, to region-specific payment options like iDEAL in the Netherlands or SEPA in the European Union. Just as seeing PayPal on checkout can help American consumers feel more comfortable about a purchase, seeing these offerings can make your customers feel more comfortable with purchasing from your store. ⟪In contrast with traditional payment methods, APMs are typically offered through a cooperating payment gateway. For example, ACH Direct Debit is enabled through Adyen or BlueSnap Direct as opposed to a standalone integration.⟫ In this guide, we will cover the benefits of offering APMs at checkout, explain the different types of APMs, walk through the typical order flow, and provide a breakdown of supported gateways and countries for each APM available in BigCommerce. What is an Open Payment Provider fee? For stores on self-serve plans, transactions processed with APMs through a payment provider that is not on our Embedded Payment Provider list are assessed an Open Pay…

### Q5-BC-105

**Cited at:** section 2, line 61; section 2, line 62; section 3, line 98

**Record** (`studies/proposals/records/Q5/bigcommerce/statements.tsv`):
- stmt_id: Q5-BC-105
- bears_on: 3
- identifier: Deep BigCommerce integration
- statement: Embedded Providers integrate directly with the BigCommerce platform. Setup and ongoing support run through the same dashboard as your store.
- cite_ids: Q5-BC-C124
- from: held

**Citation Q5-BC-C124:** `https://www.bigcommerce.com/payments/embedded-payment-providers/` | Why choose Embedded Payment Providers: Deep BigCommerce integration | 2026-10-13 | kind: stated | quote check: found
- quote: Embedded Providers integrate directly with the BigCommerce platform. Setup and ongoing support run through the same dashboard as your store.
- title: Embedded Payment Providers | BigCommerce
- in context: … Providers. ✅ If your business uses offline orders, that offline GMV counts as Open Payment Provider volume. ✅ The fee is charged to your business by BigCommerce. It must not be passed through to shoppers at checkout. Compliance note: Payment network rules and local laws restrict shopper-facing surcharges in many jurisdictions. Your business is responsible for its own compliance. Why choose Embedded Payment Providers Deep BigCommerce integration ⟪Embedded Providers integrate directly with the BigCommerce platform. Setup and ongoing support run through the same dashboard as your store.⟫ Optimized for conversion Embedded providers are optimized for the BigCommerce checkout experience - fewer friction points, faster load times, and payment methods shoppers already trust. Built to keep getting better BigCommerce continuously develops and improves the Embedded Provider experience. Choosing one means you're always on the road we're paving. Your plan determines your rate The Open Payment Provider Fee rate is set by your plan.2 Higher…

### Q5-BC-072

**Cited at:** section 2, line 73

**Record** (`studies/proposals/records/Q5/bigcommerce/statements.tsv`):
- stmt_id: Q5-BC-072
- bears_on: 1
- identifier: Staff Action Logs
- statement: When a payment method is enabled, disabled, or has settings updated, a notification will appear in the control panel dashboard. You can also see records of changes to your payment methods in the Staff Action Logs.
- cite_ids: Q5-BC-C075
- from: held

**Citation Q5-BC-C075:** `https://support.bigcommerce.com/s/article/Available-Payment-Gateways?language=en_US` | FAQ: How will I know if changes are made to my payment methods in the control panel? | 2026-10-13 | kind: stated | quote check: found
- quote: When a payment method is enabled, disabled, or has settings updated, a notification will appear in the control panel dashboard. You can also see records of changes to your payment methods in the Staff Action Logs.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …rmitted in their terms of service. Bankful NMI Sezzle USA ePay* Worldpay *You must use Paysafe as your Merchant Services Provider (MSP). Are there other payment processors outside of payment gateways? Yes, you can find additional payment processors on our App Marketplace. Note that Open Payment Provider fees may apply. For more details, see About BigCommerce Pricing. How will I know if changes are made to my payment methods in the control panel? ⟪When a payment method is enabled, disabled, or has settings updated, a notification will appear in the control panel dashboard. You can also see records of changes to your payment methods in the Staff Action Logs.⟫ Additional Resources 3D Secure Enabling Stored Payment Methods Introduction to Alternative Payment Methods Manually Capturing Transactions (Authorize Only) Multi-Storefront Payment Methods Optimized One-Page Checkout Recurring Billing Using Multiple Currencies BigCommerce Embedded Payment Providers (bigcommerce.com) BigCommerce Pricing and Plan Information (bigcommerce.com) Don't see what you're looking for? Ask the Community ASK A QUESTION Look…

### Q5-BC-074

**Cited at:** section 2, line 73; section 3, line 107

**Record** (`studies/proposals/records/Q5/bigcommerce/statements.tsv`):
- stmt_id: Q5-BC-074
- bears_on: 1
- identifier: Currency
- statement: To allow shoppers to check out with a currency, you must first set up a payment provider that supports it.
- cite_ids: Q5-BC-C077
- from: held

**Citation Q5-BC-C077:** `https://support.bigcommerce.com/s/article/Getting-Started-Payments` | Currency | 2026-10-13 | kind: stated | quote check: found
- quote: To allow shoppers to check out with a currency, you must first set up a payment provider that supports it.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …-time login link sent by request to their account email. Customizable form fields - Add, remove, and make address fields required during customer account creation with the built-in account signup form editor. See Adding and Editing Fields in the Account Signup Form. Currency With BigCommerce, you can control which currencies are shown on the storefront, and which ones can be used for payment. Set up multiple display and transactional currencies. ⟪To allow shoppers to check out with a currency, you must first set up a payment provider that supports it.⟫ Maintain price expectations throughout the storefront experience and encourage conversion by allowing shoppers to browse and transact in their native currency. Offering local currencies allows shoppers to avoid currency conversion fees that can be charged by their financial institution. Order details include the currency the order was transacted in, giving you greater transparency and insights into your customers. See Managing Currencies to lear…

### Q5-BC-P0069

**Cited at:** section 7, line 159; section 8, line 191

**Record** (`studies/proposals/records/Q5/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-068
- bullet: a;b
- placement: where
- identifier: Setting up BigCommerce Payments: PayPal platform account
- statement: When you connect BigCommerce Payments, a brand new PayPal platform account dedicated to your BigCommerce store is created. The BigCommerce Payments account is automatically linked to your PayPal Business account.
- cite_ids: S01-BC-C092
- from: new

**Citation S01-BC-C092:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 87: Setting up BigCommerce Payments | 2026-10-13 | kind: stated | quote check: found
- quote: When you connect BigCommerce Payments, a brand new PayPal platform account dedicated to your BigCommerce store is created. The BigCommerce Payments account is automatically linked to your PayPal Business account.
- in context: …t up and manage payment methods, the Manage Payments and Manage Settings permissions must be enabled on your user account. Setting up BigCommerce Payments To connect BigCommerce Payments with your store, go to Settings › Payments, and select a supported currency from the drop-down list. Under the Embedded tab, expand Online Payment Methods and click Set up next to BigCommerce Payments. On the next page, click Set up to begin the onboarding flow. ⟪When you connect BigCommerce Payments, a brand new PayPal platform account dedicated to your BigCommerce store is created. The BigCommerce Payments account is automatically linked to your PayPal Business account.⟫ See our FAQ for more details. Set up faster and easier - Select to use details from an existing PayPal Business account to create and link a new BigCommerce Payments account. Add info on your own - Select to create new PayPal Business and BigCommerce Payments accounts and link them together. Settings Actions Account Cards Digital wallets Buy Now, Pay Later Local payment methods Transaction settings Post-purchase & operations Once you have connec…

### Q5-BC-K0453

**Cited at:** section 7, line 166

**Record** (`studies/proposals/records/Q5/bigcommerce/copied.tsv`):
- concern_id: BC-C-084
- placement: where
- structure: Master Services Agreement
- identifier: Scope
- statement: Except as otherwise specified, this Agreement does not apply to Third-Party Products, which are governed by their own terms of service.
- cite_ids: BC-S-0460

**Citation BC-S-0460:** `https://www.commerce.com/terms/` | Scope and Definitions: Scope | 2026-06-01 | kind: official page | quote check: found
- quote: Except as otherwise specified, this Agreement does not apply to Third-Party Products, which are governed by their own terms of service.
- title: Master Services Agreement | Commerce
- in context: … our explicit prior written approval. Commerce reserves the right to update or modify this Agreement at any time, with updates taking immediate effect upon posting to our website or notification to you. By engaging with Commerce's Services, you acknowledge that you have read, understood, and agree to be bound by this Agreement between you and Commerce. Scope and Definitions Scope. This Agreement governs your use of the websites and the Services. ⟪Except as otherwise specified, this Agreement does not apply to Third-Party Products, which are governed by their own terms of service.⟫ Incorporated Terms. The following policies, guidelines, and agreements ("Incorporated Terms") are hereby incorporated into, and form an integral part of, the Agreement to which you are agreeing to be bound: Privacy Policy (Commerce.com Specific) (Feedonomics Specific) (Makeswift Specific) Acceptable Use Policy API Terms Fees and Billing Terms Infringing Materials Protocol Jurisdiction-Specific Terms Merchant-Client Terms Mobile App Terms Store T…

### Q5-BC-099

**Cited at:** section 7, line 166

**Record** (`studies/proposals/records/Q5/bigcommerce/statements.tsv`):
- stmt_id: Q5-BC-099
- bears_on: 2;3
- identifier: Checkout Environment; PCI
- statement: For example, you will be solely liable for PCI compliance with respect to modifications to the checkout environment, including modifications via apps or a developer, modifications of Commerce’s distributed open source checkout code in any manner that could result in or contribute to PCI noncompliance, use of a checkout environment not provided by Commerce, or use of a payment provider for which Commerce does not provide an integration.
- cite_ids: Q5-BC-C116;Q5-BC-C117
- from: held

**Citation Q5-BC-C116:** `https://www.commerce.com/terms/` | Checkout Environment; PCI | 2026-06-01 | kind: official page | quote check: found
- quote: For example, you will be solely liable for PCI compliance with respect to modifications to the checkout environment, including modifications via apps or a developer,
- title: Master Services Agreement | Commerce
- in context: …Condition"): (i) you comply with Commerce documentation and in-product notifications, and (ii) you use a Commerce checkout environment that has not been modified except through the Commerce control panel. To the extent permitted by applicable law, Commerce excludes and disclaims any liability related to the unauthorized use of Customer Data, including liability due to PCI noncompliance, in the event any PCI Compliance Condition is not satisfied. ⟪For example, you will be solely liable for PCI compliance with respect to modifications to the checkout environment, including modifications via apps or a developer,⟫ modifications of Commerce's distributed open source checkout code in any manner that could result in or contribute to PCI noncompliance, use of a checkout environment not provided by Commerce, or use of a payment provider for which Commerce does not provide an integration. Use Restrictions. This is an agreement for Services, and you are not granted a license to any software by this Agreement. Except as permitted and non-excludable under applicab…

**Citation Q5-BC-C117:** `https://www.commerce.com/terms/` | Checkout Environment; PCI | 2026-06-01 | kind: official page | quote check: found
- quote: use of a checkout environment not provided by Commerce, or use of a payment provider for which Commerce does not provide an integration.
- title, opening and note boxes: as for this source's citation above
- in context: …o the unauthorized use of Customer Data, including liability due to PCI noncompliance, in the event any PCI Compliance Condition is not satisfied. For example, you will be solely liable for PCI compliance with respect to modifications to the checkout environment, including modifications via apps or a developer, modifications of Commerce's distributed open source checkout code in any manner that could result in or contribute to PCI noncompliance, ⟪use of a checkout environment not provided by Commerce, or use of a payment provider for which Commerce does not provide an integration.⟫ Use Restrictions. This is an agreement for Services, and you are not granted a license to any software by this Agreement. Except as permitted and non-excludable under applicable law, you will not, directly or indirectly: reverse engineer, decompile, disassemble, or otherwise attempt to discover the source code, object code, or underlying structure, ideas, or algorithms of or included in the Services or any software, documentation or data related…

### Q5-BC-P0070

**Cited at:** section 8, line 176

**Record** (`studies/proposals/records/Q5/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-069
- bullet: a;b;end-payout
- placement: where
- identifier: FAQ: Auto-migration to BigCommerce Payments: What happens to my existing PayPal account if I migrate to BigCommerce Payments?
- statement: What happens to my existing PayPal account if I migrate to BigCommerce Payments? When you move to BigCommerce Payments, a brand new PayPal platform account dedicated to your BigCommerce store is created and will handle all settlement from your BigCommerce store going forward. The BigCommerce Payments account is automatically linked to your PayPal Business account, which remains fully operational, and you retain full access to it.
- scope: stores that automatically migrated to BigCommerce Payments after receiving communications from BigCommerce and PayPal
- cite_ids: S01-BC-C093;S01-BC-C094;S01-BC-C095
- from: new
- note: The FAQ's Auto-migration section says it "only pertains to stores that automatically migrated to BigCommerce Payments after receiving communications from BigCommerce and PayPal" (line 384).

**Citation S01-BC-C093:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 404: FAQ, Auto-migration to BigCommerce Payments | 2026-10-13 | kind: stated | quote check: found
- quote: What happens to my existing PayPal account if I migrate to BigCommerce Payments?
- in context: …t setup. If I opt out of auto-migration, can I set up BigCommerce Payments later? Yes. If you opt out of the migration, you can set up BigCommerce Payments at any time from your BigCommerce control panel under Settings › Payments. Note that stores that are migrated to BigCommerce Payments are subject to the fees listed here. Stores that set up BigCommerce Payments at a later date follow the fee structure listed in the FAQ under Pricing and Fees. ⟪What happens to my existing PayPal account if I migrate to BigCommerce Payments?⟫ When you move to BigCommerce Payments, a brand new PayPal platform account dedicated to your BigCommerce store is created and will handle all settlement from your BigCommerce store going forward. The BigCommerce Payments account is automatically linked to your PayPal Business account, which remains fully operational, and you retain full access to it. You can view your BigCommerce Payments account through your Balance dashboard. You can also acce…

**Citation S01-BC-C094:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 406: FAQ, Auto-migration to BigCommerce Payments | 2026-10-13 | kind: stated | quote check: found
- quote: When you move to BigCommerce Payments, a brand new PayPal platform account dedicated to your BigCommerce store is created and will handle all settlement from your BigCommerce store going forward.
- in context: … Yes. If you opt out of the migration, you can set up BigCommerce Payments at any time from your BigCommerce control panel under Settings › Payments. Note that stores that are migrated to BigCommerce Payments are subject to the fees listed here. Stores that set up BigCommerce Payments at a later date follow the fee structure listed in the FAQ under Pricing and Fees. What happens to my existing PayPal account if I migrate to BigCommerce Payments? ⟪When you move to BigCommerce Payments, a brand new PayPal platform account dedicated to your BigCommerce store is created and will handle all settlement from your BigCommerce store going forward.⟫ The BigCommerce Payments account is automatically linked to your PayPal Business account, which remains fully operational, and you retain full access to it. You can view your BigCommerce Payments account through your Balance dashboard. You can also access it by logging in to your PayPal account, clicking your business name in the upper left, and in the pop-up window, clicking on your BigCommerce Payments account under Platform accounts. Will the…

**Citation S01-BC-C095:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 406: FAQ, Auto-migration to BigCommerce Payments | 2026-10-13 | kind: stated | quote check: found
- quote: The BigCommerce Payments account is automatically linked to your PayPal Business account, which remains fully operational, and you retain full access to it.
- title, opening and note boxes: as for this source's citation above
- in context: …rce Payments are subject to the fees listed here. Stores that set up BigCommerce Payments at a later date follow the fee structure listed in the FAQ under Pricing and Fees. What happens to my existing PayPal account if I migrate to BigCommerce Payments? When you move to BigCommerce Payments, a brand new PayPal platform account dedicated to your BigCommerce store is created and will handle all settlement from your BigCommerce store going forward. ⟪The BigCommerce Payments account is automatically linked to your PayPal Business account, which remains fully operational, and you retain full access to it.⟫ You can view your BigCommerce Payments account through your Balance dashboard. You can also access it by logging in to your PayPal account, clicking your business name in the upper left, and in the pop-up window, clicking on your BigCommerce Payments account under Platform accounts. Will the migration cause any disruption to my store? Your store will continue to accept payments throughout the migration process, and your customers' checkout exper…

### Q5-BC-P0129

**Cited at:** section 8, line 185; section 8, line 211

**Record** (`studies/proposals/records/Q5/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-128
- bullet: a
- placement: responsible
- identifier: Master Services Agreement: Miscellaneous: Independent Contractors
- statement: Independent Contractors. No agency, partnership, joint venture or employment relationship is created by this Agreement or your use of the Services, and you do not have any authority of any kind to bind Commerce in any respect whatsoever.
- cite_ids: S01-BC-C222
- from: new
- note: Phase A3 (absence audit of S01-BC-G25).

**Citation S01-BC-C222:** `sharrwah-knowledge-map@7611d459e3e09c1503a27d4f02f57850e82e9ffb:evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/108-commerce.com/text.txt` | line 275: Miscellaneous, Independent Contractors | 2026-06-01 | kind: official page | quote check: found
- quote: Independent Contractors. No agency, partnership, joint venture or employment relationship is created by this Agreement or your use of the Services, and you do not have any authority of any kind to bind Commerce in any respect whatsoever.
- in context: …delivered when sent to the email address you provide to us. All notices from both parties shall be made in the English language. Notices to Commerce must be sent to: trustandsafety@commerce.com. Section Headings. The section headings and titles in this Agreement are for convenience only and have no legal or contractual effect. The Agreement will be interpreted without application of any strict construction in favor of or against you or Commerce. ⟪Independent Contractors. No agency, partnership, joint venture or employment relationship is created by this Agreement or your use of the Services, and you do not have any authority of any kind to bind Commerce in any respect whatsoever.⟫ Marks. Commerce shall have the non-exclusive right and license to use the names, trademarks, service marks and logos associated with your store(s) to promote the Services. Force Majeure. Commerce will have no liability to you, your users, or any third party for any failure by Commerce to perform its obligations under this Agreement in the event that such non-performance arises as a result of the occurrence of an event beyond the reasonable contr…
