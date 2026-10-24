# Cards: Q5 on shopify

29 records cited by `studies/proposals/drafts/Q5/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 31:** - The platform may withdraw what it offers, mostly without notice, matching by role: Salla's agreement reserves "الحق في إلغاء أو تعديل أو تغيير أي من وسائل الدفع"; Shopify may disable third-party services "without notice to you", and so may BigCommerce; WooCommerce may "suspend or remove a Product from the Marketplace(s)" (vendor agreement, stated); زد باي "قد توقف أو تلغي الحساب في أي وقت". The others are official pages. Q5-SA-001, Q5-SH-K2168, Q5-BC-K0455, Q5-WC-K0462, Q5-ZD-010
- **section 1, line 32:** - Some give notice: BigCommerce's Embedded list changes with "advance notice of any changes"; Shopify's merchants moving to new integrations get "a notification and a banner in your admin" (not checked on WooCommerce). Q5-BC-102, Q5-SH-021
- **section 1, line 33:** - Providers end things too, matching by role: "P24 can no longer be enabled on any WooPayments account that is not already using it", and once revoked, orders "will fail at checkout"; a Shopify merchant whose provider has no updated integration "must select a new payment provider". Q5-WC-013, Q5-WC-015, Q5-SH-022
- **section 1, line 34:** - The earlier provider stays for earlier orders, matching by role: at Shopify it "is available if you need it for cases such as order returns"; in store fake-demo-sharrwah (countryCode YE), observed on 30 September 2026, deactivating ONERWAY (Direct) read "Your existing orders will not be affected"; WooCommerce suggests keeping its plugin active "for at least 6 months after your final transaction". Shopify's point was not checked on Zid. Q5-SH-015, Q5-SH-098, Q5-WC-033
- **section 1, line 36:** - Shopify's partner terms bind an add-on's developer: merchants must be able to "terminate their agreement with the payment provider within 7 days", a developer that stops supporting one enters a "Wind Down Period" of up to six months, and Shopify may remove an app for a breach. Q5-SH-063, Q5-SH-K1704, Q5-SH-066
- **section 1, line 38:** - What checkout does when a provider is down was not in what was read on BigCommerce or Salla. Shopify routes cards to a third-party provider, with Shopify Payments as backup, when the two run alongside. Q5-BC-G0048, Q5-SA-G0224, Q5-SH-041
- **section 1, line 42:** - Through the platform's own service, money goes into a balance, then to the merchant's bank account, matching by role on stated pages and Zid's terms (official): Salla's "رصيد المدفوعات الإلكترونية" comes before the transfer to the bank account; Zid's terms add "المبلغ المستحق لرصيد التاجر" after fees; WooPayments adds the payment "(minus our fees)" to the balance; BigCommerce Payments and Shopify Payments pay out to the merchant's bank account. Q5-SA-P0006, Q5-ZD-P0024, Q5-WC-P0024, Q5-BC-P0074, Q5-SH-P0060
- **section 1, line 43:** - Who holds it in between, matching by role: Shopify's merchant opens "financial accounts and/or cryptocurrency wallets with one or more Payment Processors"; Stripe, as the merchant's agent, holds WooPayments' funds "in one or more Pooled Accounts at one or more Financial Providers"; BigCommerce Payments' transactions "flow through your new BigCommerce Payments account" (stated). For Salla and Zid, the entity, licence or account under which the balance is held was not in what was read. Q5-SH-P0010, Q5-WC-P0121, Q5-BC-P0052, Q5-SA-H0002, Q5-ZD-H0002
- **section 1, line 45:** - Deductions come off first, matching by role, in the own services' terms (official pages): Shopify may hold funds in a Reserve Account; Stripe pays out "net of Fees, Disputes, Refunds, Reversals and other amounts owed to Stripe"; زد باي takes chargebacks "مباشرة من رصيده المتوفر". Services, financing and apps draw on it too: Salla's dashboard text, as captured on 8 October 2026, holds label amounts to pay "نيابةً عنك إلى شركة الشحن", and its financing takes "%25 من صافي المبيعات لكل دفعة" (observed); a dropshipping app may "temporarily withhold a specific amount of money" (Salla's developer docs). Q5-SH-P0028, Q5-WC-P0124, Q5-ZD-P0011, Q5-SA-P0126, Q5-SA-P0131, Q5-SA-K1690
- **section 1, line 46:** - Some keep separate balances, matching by role: in Salla's store real-merchant, observed on 12 October 2026, the wallet summary listed "Wallet", "Electronic Payments" and "Cash on Delivery Payments"; Zid's الاستقطاع للمحفظة moves part of order payments into محفظة زد; Shopify's Shop Cash comes in the same payouts; WooPayments' FROD balance is "a special bucket of funds inside your WooPayments account". Q5-SA-075, Q5-ZD-P0067, Q5-SH-074, Q5-WC-042
- **section 1, line 47:** - Through a gateway the merchant connects, money goes to the merchant's own account with it, matching by role: funds are in "your merchant account with your merchant service provider" (BigCommerce); "the purchase amount is transferred to your merchant account" (Shopify); Salla's dashboard text, as captured on 8 October 2026, collects through the gateway "بدلًا من مدفوعات سلة" (observed); "المدفوعات توصل لحسابك مباشرة" (Zid's Paymob page). Where the money is held between the buyer's payment and its transfer was not in what was read on Shopify. WooCommerce says only that it is "unable to assist with Stripe account issues", payouts among them: a statement of no part, naming no one. Q5-BC-P0089, Q5-SH-P0050, Q5-SA-K1639, Q5-ZD-P0107, Q5-SH-N02, Q5-WC-P0159
- **section 1, line 49:** - Pay-later providers pay the merchant directly, or into the platform's own service: at Salla (UAE help), "تُحصّل المدفوعات التي تتم عبر تابي من خلال تابي وليس من خلال مدفوعات سلة"; at Zid, "تقوم تابي بالدفع للمتاجر مباشرة"; with BigCommerce's PayPal Pay Later, "you, the merchant, always get paid"; these match by role. Shopify and WooCommerce differ: Shop Pay Installments payouts "are included with your Shopify Payments payouts", and WooPayments receives "the entire purchase amount immediately". Q5-SA-P0102, Q5-ZD-P0077, Q5-BC-P0095, Q5-SH-K1686, Q5-WC-P0056
- **section 1, line 50:** - With methods outside any provider, the buyer pays the merchant and the order waits, matching by role: Salla's customer transfers "مباشرة من حسابه البنكي إلى حسابك"; BigCommerce's pay "directly into your bank account"; the order is "marked as unpaid" (Shopify), in "Awaiting Payment" (BigCommerce), or on hold, `OrderStatus::ON_HOLD` in WooCommerce's shipped code. In Shopify's store demo-fake-dev-store (countryCode YE), observed on 30 September 2026, the order then read "You manually marked YER699.95 as paid for this order." Q5-SA-P0099, Q5-BC-P0116, Q5-SH-K1736, Q5-BC-P0115, Q5-WC-K0037, Q5-SH-093
- **section 2, line 56:** - It draws on the five platforms' split between provider and manual methods, and on the waiting order of Shopify, BigCommerce and WooCommerce. Q5-SH-083, Q5-BC-060, Q5-SA-015, Q5-ZD-P0075, Q5-SH-K1736, Q5-WC-K0037
- **section 2, line 57:** - Why: rule 3; an order's payment state depends on its method's kind, so the kind is in the data model from the start. Q5-SH-K1736, Q5-BC-P0115
- **section 2, line 58:** - **Payment provider**: a company that processes provider methods and pays the money out, recorded once with the methods it carries, the places it serves, its money route and its terms. A method may come from several providers, a provider carry several methods. Q5-SH-001, Q5-BC-079, Q5-SA-K1654
- **section 2, line 59:** - It draws on Shopify's cards through "Shopify Payments, a third-party provider, or both together", BigCommerce's alternative methods offered "through a cooperating payment gateway", and Salla's K net, which hangs on Tap. Q5-SH-001, Q5-BC-079, Q5-SA-K1654
- **section 2, line 60:** - Why: rule 2; a provider's arrival or exit changes only its own record and its methods. Q5-SH-022, Q5-SA-K1654
- **section 2, line 66:** - It draws on Salla's choice between an existing account and a request the provider may reject, the own account Zid's pay-later providers need, BigCommerce's application and underwriting, and Shopify's apps, where the merchant may "log in or create an account with the payment provider". Q5-SA-053, Q5-SA-057, Q5-ZD-P0080, Q5-BC-P0048, Q5-SH-053
- **section 2, line 74:** - Why: rule 2; one provider per method tells checkout and refunds which provider holds each payment. Q5-SH-040, Q5-SH-015
- **section 2, line 79:** - **Payment record**: each payment on an order, with its method, provider, the provider's reference, amount, currency, state (awaiting, paid, recorded by the merchant, refunded) and money route. A refund goes back through the provider that took the payment, which stays callable for that after it leaves checkout. Q5-SH-015, Q5-WC-033, Q5-BC-085
- **section 2, line 80:** - It draws on BigCommerce's attribution of each order "to the provider that processed it", Shopify's earlier provider kept for returns (and store fake-demo-sharrwah on 30 September 2026, observed), WooCommerce's six months, and Shopify's manual mark as paid. Q5-BC-085, Q5-SH-015, Q5-SH-098, Q5-WC-033, Q5-SH-093
- **section 2, line 81:** - Why: rule 3, the data model; a payment that doesn't name its provider and route can't be refunded or reconciled once that provider has gone. Q5-SH-015, Q5-WC-033
- **section 2, line 83:** - It draws on the direct route the platforms show for gateways the merchant connects, pay-later providers that pay the store, and bank transfer, and on the held route of their own services. Q5-SH-P0050, Q5-ZD-P0107, Q5-ZD-P0077, Q5-SA-P0099, Q5-WC-P0024, Q5-ZD-P0024
- **section 2, line 85:** - Why: rule 3, money flows are expensive to change after launch, and what a platform's records hold differs by route, so every payment carries its route from the start; rule 4, whether a held route goes live stays open. Q5-SA-A0002, Q5-SH-026
- **section 2, line 88:** - It draws on the platforms' own balances and their deductions and reserves, Salla's label holds under the merchant's authorization, and the payout account Salla takes at verification. Q5-SH-P0028, Q5-WC-P0124, Q5-ZD-P0011, Q5-SA-P0126, Q5-SA-P0055
- **section 2, line 90:** - Where the platforms differ, one balance with credits folded in (Shopify's Shop Cash; WooPayments' FROD bucket) against several wallets (Salla's observed store; Zid's wallet), typed entries in one ledger can show either; the choice is kept open. Q5-SH-074, Q5-WC-042, Q5-SA-075, Q5-ZD-P0067
- **section 2, line 91:** - **Provider withdrawal**: what Sharrwah does when a provider or method stops at a place. Sharrwah removes it from the place's list and checkout after notice to the stores using it, unless the provider or a regulator ends it at once; methods carried only by that provider go with it; the merchant is asked to choose another provider; the integration stays callable for refunds and disputes on earlier payments; an add-on's developer keeps it working through a wind-down period; and, on a held route, the balance left is paid out. Q5-BC-102, Q5-SH-015, Q5-SA-K1654
- **section 2, line 92:** - It draws on BigCommerce's and Shopify's notice, P24's ending, Shopify's earlier provider kept for returns and its Wind Down Period, WooCommerce's six months, and the payout of the balance left at WooCommerce and Zid. Q5-BC-102, Q5-SH-021, Q5-WC-013, Q5-SH-K1704, Q5-WC-033, Q5-WC-K0715, Q5-ZD-P0042
- **section 2, line 93:** - Why: rule 2, a provider's exit touches only its own part; rule 3, refunds and money held are expensive to get wrong. Q5-SH-015, Q5-WC-015
- **section 2, line 94:** - Not taken: withdrawal without notice, which Shopify's, BigCommerce's and Salla's terms reserve, because a method withdrawn under the merchants leaves orders that "fail at checkout", as P24's did. Q5-SH-K2168, Q5-BC-K0455, Q5-SA-001, Q5-WC-015
- **section 3, line 99:** - Methods plug in through the providers that carry them. Q5-BC-079, Q5-SH-001
- **section 3, line 113:** - Withdrawal is set per provider and place by Sharrwah; per add-on by its developer, within its wind-down terms, or by Sharrwah for a breach; and per method by the provider. Q5-BC-102, Q5-SH-K1704, Q5-SH-066, Q5-WC-013
- **section 5, line 135:** - What checkout does when a provider is down, which was not in what was read on BigCommerce or Salla: the design keeps room for a backup provider per method, as Shopify has. Providers' service terms and testing settle it. Q5-BC-G0048, Q5-SA-G0224, Q5-SH-041
- **section 5, line 136:** - How long a withdrawn provider stays callable for refunds and disputes: "available" at Shopify, at least six months at WooCommerce, while in Yemen an authority that bars a provider can leave 15 days to liquidate balances with it. The design sets the end per place and provider, as data. Each partner contract, and each place's authority, settles it. Q5-SH-015, Q5-WC-033, YK-17 (liquidate within 15 days @ Houthis' area, as of 2025-07-11)
- **section 7, line 160:** - Which payment providers Sharrwah works with at each place, and on what terms: notice before withdrawal, refunds after it, settlement time, and service when a provider is down. Q5-BC-102, Q5-SH-064, Q5-WC-033, Q5-BC-G0048
- **section 7, line 161:** - Whether providers and partners may build payments add-ons, and under what agreement and review. Q5-SH-K1696, Q5-SH-063, Q5-WC-K0353, Q5-ZD-K0077
- **section 7, line 166:** - Sharrwah's own terms with merchants and providers, for the founder with a lawyer: whether a merchant's dealings with a provider are a contract of their own, whether Sharrwah acts for the merchant in any part of a payment, any security interest over sellers' money on a held route, and who answers for card data security. The platforms' terms show only what each requires of its sellers. Q5-SA-005, Q5-BC-K0453, Q5-BC-099, Q5-SH-P0002, Q5-SH-P0024
- **section 7, line 167:** - Which company contracts with providers and merchants, and where it is based, since the platforms' processors and contracting entities change with the merchant's country. Q5-SH-K1566, Q5-WC-P0108
- **section 8, line 173:** - Records: Shopify's financial services provider, Stripe's pooled accounts and BigCommerce Payments' account hold it; Salla's (UAE help) and Zid's balances hold sales proceeds before payout, but who holds either balance was not in what was read; a connected gateway pays the merchant's own account. S01-VP-01, Q5-SH-P0033, Q5-WC-P0121, Q5-BC-P0052, Q5-SA-P0057, Q5-ZD-P0035, Q5-SA-H0002, Q5-ZD-H0002, Q5-BC-P0089
- **section 8, line 179:** - Records: Shopify sends Shopify Payments' payouts, processed by partners, in the United States and France; WooPayments sends them to a bank account; Salla's dashboard text, as captured on 8 October 2026, lists transfers "من سلة إلى حسابك البنكي" (observed); Zid deposits on set days by country; BigCommerce Payments pays out to a linked bank or PayPal account. S01-VP-03, Q5-SH-P0076, Q5-WC-P0027, Q5-SA-P0040, Q5-ZD-P0041, Q5-BC-P0074
- **section 8, line 185:** - Records: Shopify is the merchant's agent "to deliver information and instructions on your behalf"; Stripe, "for the limited purpose of directing, receiving, holding and settling funds"; Zid executes "payment processes on their behalf" (official pages); Salla passes label amounts on the merchant's behalf (dashboard text as captured on 8 October 2026, observed). BigCommerce's "No agency" statement is one of no part, naming no one; no reading rests on it. S01-VP-06, Q5-SH-P0002, Q5-WC-P0121, Q5-ZD-P0008, Q5-SA-P0126, Q5-BC-P0129
- **section 8, line 188:** - Records: Shopify deducts refunds from the next payout; Stripe pays out net of fees, disputes and refunds; Zid takes fees from amounts collected, and dues by "الخصم الآلي والمباشر"; Salla's dashboard text, as captured on 8 October 2026, takes postpaid label amounts from the wallet or coming dues (observed). S01-VP-09, Q5-SH-P0094, Q5-WC-P0124, Q5-ZD-P0024, Q5-ZD-P0061, Q5-SA-P0129
- **section 8, line 191:** - Records: Shopify's merchant opens accounts with Payment Processors; WooCommerce's Stripe extension uses the merchant's Stripe account; BigCommerce Payments creates a PayPal platform account per store; Zid's pay-later providers need an account with them; in Salla's store real-merchant, observed on 12 October 2026, the wallet listed "Electronic Payments" and "Cash on Delivery Payments". S01-VP-11, Q5-SH-P0010, Q5-WC-P0023, Q5-BC-P0069, Q5-ZD-P0080, Q5-SA-075
- **section 8, line 194:** - Records: by plan at Salla, by country at Zid, by account country for WooPayments' "pending period"; up to 21 days for a new BigCommerce Payments account's first payments; at most 5 days for Shopify's payment apps to settle. S01-VP-15, Q5-SA-P0020, Q5-ZD-P0041, Q5-WC-P0033, Q5-BC-P0083, Q5-SH-064
- **section 8, line 197:** - Records: WooPayments credits payments "(minus our fees)"; Shopify's terms for the EU, EEA and UK settle "net of fees, refunds, chargebacks, reserves, and other amounts owed"; Salla transfers "بعد خصم الرسوم والضريبة" (dashboard text as captured on 8 October 2026, observed), while its store balance is for Salla's subscriptions and services (UAE help); Zid takes fees from amounts collected. S01-VP-19, Q5-WC-P0024, Q5-SH-P0107, Q5-SA-P0037, Q5-SA-P0057, Q5-ZD-P0024
- **section 8, line 200:** - Records: Shopify's funds in custody are paid out "subject to the Payment Processor Terms"; WooPayments' and Zid's balances are paid out, Zid's not before its financing is repaid; Salla may stop the service and close the store for a breach. On BigCommerce, what happens to funds when a provider is disconnected was not in what was read. S01-VP-20, Q5-SH-P0033, Q5-WC-K0715, Q5-ZD-P0042, Q5-ZD-P0097, Q5-SA-P0083, Q5-BC-H0040
- **section 8, line 203:** - Records: Shopify's terms for the EU, EEA and UK, if the merchant fails its checks, "funds may be held or refunded to your customers"; Zid's terms, after 14 days of uncorrected activation data, "إعادة جميع المبالغ للعملاء النهائيين"; Salla's terms, for a breach, "إعادة أي مبالغ معلقة في المدفوعات الإلكترونية للمستهلكين". S01-VP-21, Q5-SH-P0107, Q5-ZD-P0012, Q5-SA-P0083
- **section 8, line 206:** - Records: Shopify takes "a first priority lien and security interest" over funds processed and deposited; Stripe's terms for the United States have the merchant grant one to SPC. Both are official pages. S01-VP-10, Q5-SH-P0024, Q5-WC-P0113
- **section 8, line 209:** - Records: with BigCommerce's PayPal Pay Later the shopper owes PayPal, while the merchant will "always get paid"; WooPayments receives "the entire purchase amount immediately"; Shop Pay Installments come with Shopify Payments payouts; Tabby pays Zid's stores directly and collects Salla's payments itself (UAE help). S01-VP-22, Q5-BC-P0095, Q5-WC-P0056, Q5-SH-K1686, Q5-ZD-P0077, Q5-SA-P0102

## The cards

### Q5-SH-K2168

**Cited at:** section 1, line 31; section 2, line 94

**Record** (`studies/proposals/records/Q5/shopify/copied.tsv`):
- concern_id: SH-C-156
- placement: decides
- structure: https://www.shopify.com/legal/terms
- identifier: 9.9 Third Party Services and Third Party Partners
- statement: Shopify does not guarantee the availability of Third Party Services and you acknowledge that Shopify may disable access to any Third Party Services at any time in its sole discretion and without notice to you.
- cite_ids: SH-S-0060
- note: first run's citation

**Citation SH-S-0060:** `https://www.shopify.com/legal/terms` | 9.9 Third Party Services and Third Party Partners | 2026-08-01 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/143-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/117-shopify.com/text.txt` (fetched 2026-10-12T10:51:23Z, captured)
- quote: Shopify does not guarantee the availability of Third Party Services and you acknowledge that Shopify may disable access to any Third Party Services at any time in its sole discretion and without notice to you.
- title: Shopify Terms of Service - Shopify
- in context: …Providers. You acknowledge that Shopify has no control over Third Party Services or Third Party Providers and will not be responsible or liable to you or anyone else for such Third Party Services or Third Party Providers. The availability of Third Party Services, or the integration or enabling of such Third Party Services with the Services does not constitute or imply an endorsement, authorization, sponsorship, or affiliation by or with Shopify. ⟪Shopify does not guarantee the availability of Third Party Services and you acknowledge that Shopify may disable access to any Third Party Services at any time in its sole discretion and without notice to you.⟫ Shopify is not responsible or liable to anyone for discontinuation or suspension of access to, or disablement of, any Third Party Service. Shopify strongly recommends that you seek specialist advice before using or relying on Third Party Services or Third Party Providers to ensure they will meet your needs. In particular, tax calculators should be used for reference only and not as a substitute for independent tax advice, when assessing whether …

### Q5-SH-021

**Cited at:** section 1, line 32; section 2, line 92

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-021
- bears_on: 4
- identifier: Updating a third party payment provider
- statement: The method used to integrate third party providers with the Shopify platform is being updated to provide you with continuous service. If you’re using a third party payment provider and haven't completed an update yet, then you receive a notification and a banner in your admin explaining that you need to update the integration to continue.
- cite_ids: Q5-SH-C024;Q5-SH-C025
- from: held

**Citation Q5-SH-C024:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/updating-third-party-providers.md` | Updating a third party payment provider | undated | kind: stated | quote check: found
- quote: The method used to integrate third party providers with the Shopify platform is being updated to provide you with continuous service.
- title: Updating a third party payment provider
- the page opens: Note The way that third-party payment providers integrate with the Shopify platform is being updated. If you haven't completed your update yet, then check the Payments section of your Shopify admin for notifications or banners, and follow the steps to avoid any interruption to your payment processing. The method used to integrate third party providers with the Shopify platform is being updated to provide you with continuous service. If you're using a third party payment provider and haven't comp…
- a note box: Note The way that third-party payment providers integrate with the Shopify platform is being updated. If you haven't completed your update yet, then check the Payments section of your Shopify admin for notifications or banners, and follow the steps to avoid any interruption to your payment processin
- a note box: Note You must have an active Braintree account to complete this migration. If you don't have an active Braintree account, then contact PayPal Braintree Sales before attempting to update your payment gateway.
- headings: Updating a third party payment provider
- in context: # Updating a third party payment provider <aside class="note"><h4>Note</h4><p>The way that third-party payment providers integrate with the Shopify platform is being updated. If you haven't completed your update yet, then check the <a href="https://admin.shopify.com/payments">Payments</a> section of your Shopify admin for notifications or banners, and follow the steps to avoid any interruption to your payment processing.</p> </aside> ⟪The method used to integrate third party providers with the Shopify platform is being updated to provide you with continuous service.⟫ If you're using a third party payment provider and haven't completed an update yet, then you receive a notification and a banner in your admin explaining that you need to update the integration to continue. Most payment providers have new integrations that you can easily connect to your Shopify account. If you're using a payment provider that doesn't offer an updated integration, then you must select a new payment provider. ## Considerations whe…

**Citation Q5-SH-C025:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/updating-third-party-providers.md` | Updating a third party payment provider | undated | kind: stated | quote check: found
- quote: If you’re using a third party payment provider and haven't completed an update yet, then you receive a notification and a banner in your admin explaining that you need to update the integration to continue.
- title, opening and note boxes: as for this source's citation above
- headings: Updating a third party payment provider
- in context: …ntegrate with the Shopify platform is being updated. If you haven't completed your update yet, then check the <a href="https://admin.shopify.com/payments">Payments</a> section of your Shopify admin for notifications or banners, and follow the steps to avoid any interruption to your payment processing.</p> </aside> The method used to integrate third party providers with the Shopify platform is being updated to provide you with continuous service. ⟪If you're using a third party payment provider and haven't completed an update yet, then you receive a notification and a banner in your admin explaining that you need to update the integration to continue.⟫ Most payment providers have new integrations that you can easily connect to your Shopify account. If you're using a payment provider that doesn't offer an updated integration, then you must select a new payment provider. ## Considerations when updating a third party payment provider When updating your third party payment provider, you should take the following into consideration: * **Third-party apps and tools**: Minimal impact to third-party ap…

### Q5-SH-022

**Cited at:** section 1, line 33; section 2, line 60

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-022
- bears_on: 4
- identifier: Updating a third party payment provider
- statement: Most payment providers have new integrations that you can easily connect to your Shopify account. If you’re using a payment provider that doesn't offer an updated integration, then you must select a new payment provider.
- cite_ids: Q5-SH-C026
- from: held

**Citation Q5-SH-C026:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/updating-third-party-providers.md` | Updating a third party payment provider | undated | kind: stated | quote check: found
- quote: Most payment providers have new integrations that you can easily connect to your Shopify account. If you’re using a payment provider that doesn't offer an updated integration, then you must select a new payment provider.
- title: Updating a third party payment provider
- the page opens: Note The way that third-party payment providers integrate with the Shopify platform is being updated. If you haven't completed your update yet, then check the Payments section of your Shopify admin for notifications or banners, and follow the steps to avoid any interruption to your payment processing. The method used to integrate third party providers with the Shopify platform is being updated to provide you with continuous service. If you're using a third party payment provider and haven't comp…
- a note box: Note The way that third-party payment providers integrate with the Shopify platform is being updated. If you haven't completed your update yet, then check the Payments section of your Shopify admin for notifications or banners, and follow the steps to avoid any interruption to your payment processin
- a note box: Note You must have an active Braintree account to complete this migration. If you don't have an active Braintree account, then contact PayPal Braintree Sales before attempting to update your payment gateway.
- headings: Updating a third party payment provider
- in context: …ications or banners, and follow the steps to avoid any interruption to your payment processing.</p> </aside> The method used to integrate third party providers with the Shopify platform is being updated to provide you with continuous service. If you're using a third party payment provider and haven't completed an update yet, then you receive a notification and a banner in your admin explaining that you need to update the integration to continue. ⟪Most payment providers have new integrations that you can easily connect to your Shopify account. If you're using a payment provider that doesn't offer an updated integration, then you must select a new payment provider.⟫ ## Considerations when updating a third party payment provider When updating your third party payment provider, you should take the following into consideration: * **Third-party apps and tools**: Minimal impact to third-party apps and tools is expected when you update your payment provider. It's recommended that you test any apps or tools - for example, subscription apps or enterprise resource planning (ERP) tools - that you're using to manage y…

### Q5-SH-015

**Cited at:** section 1, line 34; section 2, line 74; section 2, line 79; section 2, line 80; section 2, line 81; section 2, line 91; section 2, line 93; section 5, line 136

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-015
- bears_on: 4
- identifier: Change your credit card payment provider
- statement: When you change your payment provider, your previous provider will be removed from your payment settings, but is available if you need it for cases such as order returns.
- cite_ids: Q5-SH-C018
- from: held

**Citation Q5-SH-C018:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/configuring-providers.md` | Change your credit card payment provider | undated | kind: stated | quote check: found
- quote: When you change your payment provider, your previous provider will be removed from your payment settings, but is available if you need it for cases such as order returns.
- title: Configuring third-party payment providers
- the page opens: If you're not using Shopify Payments and you want to accept credit cards, then you can choose from over 100 credit card payment providers for your Shopify store. You can activate or change a payment provider from the Payments page of your Shopify admin. Depending on the requirements of the payment provider, you might be required to submit and verify your bank account information with them so that your store can complete transactions. Contact your payment provider to confirm whether or not you ca…
- a note box: Grow your business If you need help setting up a third-party payment provider, then you can hire a Shopify Partner. Learn more about hiring a Shopify Partner.
- a note box: Note Only the store owner can add a payment provider.
- a note box: Note Before you use Shopify Payments, review the following requirements: Shopify Payments is only available to online stores in certain countries and regions. If you operate a retail store, then check the list of countries that support Shopify Payments for in-person selling. To use Shopify Payments,
- headings: Configuring third-party payment providers > Change your credit card payment provider {#change-credit-card-provider} > Steps:
- in context: …/strong>.</p> </li> <li><p>Tap <strong>Choose another provider</strong>.</p> </li> <li><p>Select the provider that you want to use from the list.</p> </li> <li><p>Enter your account credentials for the provider that you selected.</p> </li> <li><p>Tap <strong>Activate</strong>.</p> </li> <li><p>Tap <strong>Save</strong> or <strong>✓</strong>.</p> </li> </ol> </details></div> The payment provider that you selected will now be active on your store. ⟪When you change your payment provider, your previous provider will be removed from your payment settings, but is available if you need it for cases such as order returns.⟫ If you want to process returns for orders placed using your previous payment provider, then don't remove your account credentials from the **Payments** page of your Shopify admin before switching providers. ## Updating a third party payment provider If you're currently using a third party payment provider, then you might need to update the connection between the provider and your Shopify account. Learn more about [updating your payment provider]…

### Q5-SH-098

**Cited at:** section 1, line 34; section 2, line 80

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-098
- bears_on: 4
- identifier: ONERWAY (Direct): Deactivate ONERWAY (Direct)
- statement: If you deactivate ONERWAY (Direct), it will be removed as a payment option from your checkout. Your existing orders will not be affected and can still be managed from the orders page.
- scope: store fake-demo-sharrwah, observed 2026-09-30; countryCode YE, currencyCode YER
- cite_ids: Q5-SH-C156;Q5-SH-C128
- from: held
- note: In the saved HTML of step 388 of run 20260930T002940Z-sweep-trial: a dialog's text in the markup, not shown as open. The step's aria.yaml has the page's Deactivate button but not this dialog's words.

**Citation Q5-SH-C156:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T002940Z-sweep-trial/388.html.txt` | run 20260930T002940Z-sweep-trial, step 388 | 2026-09-30 | kind: observed | quote check: found
- step 388: visit route payments:settings:third-party-providers:active (path from router; computed segment written as "settings" (hypothesis from settings-nav urls)) | https://admin.shopify.com/store/fake-demo-sharrwah/settings/payments/third-party-providers/41156609 | "My Store · Payments · Third-party payment providers · ONERWAY (Direct) · Shopify" | 2026-09-30T03:05:08.129Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T002940Z-sweep-trial/steps/388.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T002940Z-sweep-trial/steps/388.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T002940Z-sweep-trial/388.html.txt`
- quote: [heading: Deactivate ONERWAY (Direct)] Deactivate Cancel If you deactivate ONERWAY (Direct), it will be removed as a payment option from your checkout. Your existing orders will not be affected and can still be managed from the orders page.
- in context: … account. Two-step authentication helps secure your important details. Once it's turned on, it's much more difficult for unauthorized persons to access your account. With two-step authentication, you can login more securely by using methods such as fingerprint sensor or push notifications. If two-step authentication isn't turned on, your account may be less secure. You may also have your payouts paused. Learn more about two-step authentication . ⟪[heading: Deactivate ONERWAY (Direct)] Deactivate Cancel If you deactivate ONERWAY (Direct), it will be removed as a payment option from your checkout. Your existing orders will not be affected and can still be managed from the orders page.⟫

**Citation Q5-SH-C128:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/answers/admin.shopify.com/PaymentProviders/cc5519fabb7661cc9b8bdb071e16e1af58ad4ab46536df9a12a0e37f20c3ba5a.json` | operation PaymentProviders, store fake-demo-sharrwah, step 376 | 2026-10-05 | kind: observed | quote check: found
- quote: "url":"https://fake-demo-sharrwah.myshopify.com","countryCode":"YE","currencyCode":"YER"
- in context: …tedOrderAction":"NOT_SET","__typename":"FraudProtectSettings"},"features":{"highRiskOrdersWithFlow":{"onboardingStage":"NEEDS_FLOW","__typename":"HighRiskOrdersWithFlow"},"__typename":"ShopFeatures","threeDSecureEligibilityForCountry":false,"sellsSubscriptions":false,"bankAccountChangesLocked":false},"checkoutSettings":{"shippingBehaviour":"GIFT_CARDS_ONLY","__typename":"CheckoutSettings"},"__typename":"Shop","name":"My Store","description":null,⟪"url":"https://fake-demo-sharrwah.myshopify.com","countryCode":"YE","currencyCode":"YER"⟫,"checkoutExtensibilityMigrationStatus":"FORCED_MIGRATION","accountOwner":{"id":"gid://shopify/StaffMember/165290082519","name":"Demo-name demo-last-name","email":"7amza.it@gmail.com","__typename":"StaffMember"},"plan":{"trial":false,"shopifyPlus":false,"__typename":"ShopPlan"},"entitlements":{"multiPrimaryGateways":true,"__typename":"EntitlementsType"},"developmentShop":false,"multiLegalEntitiesPhase":"INELIGIBLE"},"paymentAuthorizationSettings"…

### Q5-SH-063

**Cited at:** section 1, line 36; section 7, line 161

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-063
- bears_on: 4
- identifier: Merchant Flexibility
- statement: Merchant Flexibility. Payments Applications must allow for Shopify Merchants to terminate their agreement with the payment provider within 7 days’ notice, without any penalty, fine, or other consequence.
- cite_ids: Q5-SH-C098
- from: held

**Citation Q5-SH-C098:** `https://www.shopify.com/partners/terms` | C.4. Additional Terms Applicable to Payments Developers, Merchant Flexibility | 2026-02-27 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/152-shopify.com/text.txt` (fetched 2026-10-11T06:13:12Z, captured)
- quote: Merchant Flexibility. Payments Applications must allow for Shopify Merchants to terminate their agreement with the payment provider within 7 days’ notice, without any penalty, fine, or other consequence.
- title: Shopify Partner Program - Partner Program Agreement - Shopify
- in context: …hat it describes. Sync Data to Shopify. All payments and order data received from transactions processed on the Payments Application must be automatically synced to Shopify as specified in the Payments Platform Developer Guidelines. New Payments Application Feature Approval. Any updates or changes to an existing Payments Application, including the addition of new product features or new payment methods, must be submitted for review and approval. ⟪Merchant Flexibility. Payments Applications must allow for Shopify Merchants to terminate their agreement with the payment provider within 7 days' notice, without any penalty, fine, or other consequence.⟫ Settlements. All Payments Applications must settle transactions for the Merchants within a maximum of 5 days, as outlined in the Payments Platform Developer Guidelines. Wind Down Period. If Payments Developer wishes to no longer support the Payments Application, the Parties agree to the following arrangement for a period not to exceed six (6) months following the effective date of termination (the "Wind Down Period"). Notwithstanding the foregoi…

### Q5-SH-K1704

**Cited at:** section 1, line 36; section 2, line 92; section 3, line 113

**Record** (`studies/proposals/records/Q5/shopify/copied.tsv`):
- concern_id: SH-C-076
- placement: responsible
- structure: https://www.shopify.com/partners/terms
- identifier: C.4. Additional Terms Applicable to Payments Developers, Wind Down Period
- statement: If Payments Developer wishes to no longer support the Payments Application, the Parties agree to the following arrangement for a period not to exceed six (6) months following the effective date of termination (the “Wind Down Period”).
- cite_ids: SH-S-0293
- note: first run's citation

**Citation SH-S-0293:** `https://www.shopify.com/partners/terms` | C.4. Additional Terms Applicable to Payments Developers, Wind Down Period | 2026-02-27 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/152-shopify.com/text.txt` (fetched 2026-10-11T06:13:12Z, captured)
- quote: If Payments Developer wishes to no longer support the Payments Application, the Parties agree to the following arrangement for a period not to exceed six (6) months following the effective date of termination (the “Wind Down Period”).
- title: Shopify Partner Program - Partner Program Agreement - Shopify
- in context: …ayment methods, must be submitted for review and approval. Merchant Flexibility. Payments Applications must allow for Shopify Merchants to terminate their agreement with the payment provider within 7 days' notice, without any penalty, fine, or other consequence. Settlements. All Payments Applications must settle transactions for the Merchants within a maximum of 5 days, as outlined in the Payments Platform Developer Guidelines. Wind Down Period. ⟪If Payments Developer wishes to no longer support the Payments Application, the Parties agree to the following arrangement for a period not to exceed six (6) months following the effective date of termination (the "Wind Down Period").⟫ Notwithstanding the foregoing, if the Agreement is terminated as a result of a material breach by Payments Developer, then the Wind Down Period will not exceed a period of one (1) month, or such other length of time as determined by Shopify in its sole discretion and communicated to Payments Developer in writing (email accepted). During the Wind Down Period, both Parties will continue to perform their obligations under this agreement and Payment…

### Q5-SH-066

**Cited at:** section 1, line 36; section 3, line 113

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-066
- bears_on: 4
- identifier: 6. Termination, Suspension and Removal from the Payments Platform
- statement: Shopify may at its sole discretion remove your Payments Application from Shopify’s public list of payment gateways, suspend or terminate your access to the Payments Platform and your participation in Shopify’s payments ecosystem, or take any other action that we deem necessary for the violation of any clause in this Section “Additional Terms Applicable to Payments Developers.”
- cite_ids: Q5-SH-C103;Q5-SH-C104
- from: held

**Citation Q5-SH-C103:** `https://www.shopify.com/partners/terms` | C.4. Additional Terms Applicable to Payments Developers, 6. Termination, Suspension and Removal from the Payments Platform | 2026-02-27 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/152-shopify.com/text.txt` (fetched 2026-10-11T06:13:12Z, captured)
- quote: Shopify may at its sole discretion remove your Payments Application from Shopify’s public list of payment gateways, suspend or terminate your access to the Payments Platform and your participation in Shopify’s payments ecosystem,
- title: Shopify Partner Program - Partner Program Agreement - Shopify
- in context: …in which Payments Developer collects and uses Merchant data. Payments Developer must provide Shopify with any changes or updates to how they collect and use data in connection with their Payments Application. Payments Developer acknowledges that Shopify may share a summary of how data is collected and shared by the Payments Application in our communications with Shopify Merchants. 6. Termination, Suspension and Removal from the Payments Platform ⟪Shopify may at its sole discretion remove your Payments Application from Shopify's public list of payment gateways, suspend or terminate your access to the Payments Platform and your participation in Shopify's payments ecosystem,⟫ or take any other action that we deem necessary for the violation of any clause in this Section "Additional Terms Applicable to Payments Developers." For the avoidance of doubt, this Section does not preclude the termination rights set forth in Section 4 "Termination" of this Agreement. C.5. Additional Terms Applicable to Blockchain Developers 1. App Requirements Blockchain Developers are permitted to develop Blockchain Applications that integra…

**Citation Q5-SH-C104:** `https://www.shopify.com/partners/terms` | C.4. Additional Terms Applicable to Payments Developers, 6. Termination, Suspension and Removal from the Payments Platform | 2026-02-27 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/152-shopify.com/text.txt` (fetched 2026-10-11T06:13:12Z, captured)
- quote: or take any other action that we deem necessary for the violation of any clause in this Section “Additional Terms Applicable to Payments Developers.”
- title, opening and note boxes: as for this source's citation above
- in context: …knowledges that Shopify may share a summary of how data is collected and shared by the Payments Application in our communications with Shopify Merchants. 6. Termination, Suspension and Removal from the Payments Platform Shopify may at its sole discretion remove your Payments Application from Shopify's public list of payment gateways, suspend or terminate your access to the Payments Platform and your participation in Shopify's payments ecosystem, ⟪or take any other action that we deem necessary for the violation of any clause in this Section "Additional Terms Applicable to Payments Developers."⟫ For the avoidance of doubt, this Section does not preclude the termination rights set forth in Section 4 "Termination" of this Agreement. C.5. Additional Terms Applicable to Blockchain Developers 1. App Requirements Blockchain Developers are permitted to develop Blockchain Applications that integrate blockchain-based functionalities and the Service. Applications that constitute both a Blockchain Application and another type of Application (inclu…

### Q5-SH-041

**Cited at:** section 1, line 38; section 5, line 135

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-041
- bears_on: 3;5
- identifier: Payment method routing
- statement: Credit and debit cards Third-party provider Shopify Payments
- scope: when you use Shopify Payments alongside a third-party provider
- cite_ids: Q5-SH-C051
- from: held

**Citation Q5-SH-C051:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/using-shopify-payments-with-a-third-party-provider.md` | Payment method routing, table (Payment method, Primary provider, Backup provider), row Credit and debit cards | undated | kind: stated | quote check: found (markup removed)
- quote: Credit and debit cards Third-party provider Shopify Payments
- title: Using Shopify Payments with a third-party provider
- the page opens: You can use Shopify Payments alongside a direct third-party payment provider in the same store. In this setup, your third-party provider is the primary processor for credit and debit card transactions, and Shopify Payments handles additional payment methods your third-party provider doesn't support, such as Shop Pay and local payment methods. You can also use Shopify Payments to recover failed card transactions from your third-party provider, helping to reduce lost sales. Note Before you use Sho…
- a note box: Note Before you use Shopify Payments, review the following requirements: Shopify Payments is only available to online stores in certain countries and regions. If you operate a retail store, then check the list of countries that support Shopify Payments for in-person selling. To use Shopify Payments,
- in context: …t covers only transactions processed through Shopify Payments. * Shopify Balance remains available regardless of which provider processes the majority of transactions. Payment method routing When you use Shopify Payments alongside a third-party provider, each payment method is routed to a specific provider. How payment methods are routed when using Shopify Payments alongside a third-party provider. Payment method Primary provider Backup provider ⟪Credit and debit cards Third-party provider Shopify Payments⟫ Wallets offered by the third-party provider Third-party provider None Wallets not offered by the third-party provider Shopify Payments None Shop Pay Shopify Payments None Local payment methods Shopify Payments None Your third-party provider remains the primary provider for credit and debit card transactions. You can offer any payment methods that your third-party provider doesn't support through Shopify Payments, giving your customers more ways …  (matched markup removed)

### Q5-SH-P0060

**Cited at:** section 1, line 42

**Record** (`studies/proposals/records/Q5/shopify/copied-pilot.tsv`):
- stmt_id: S01-SH-059
- bullet: end-payment;end-payout
- placement: where
- identifier: help.shopify.com/en/manual/payments/shopify-payments/payouts
- statement: After a customer pays for an order using Shopify Payments and specific accelerated checkouts, the funds are transferred to the payout bank account that you set up with Shopify Payments.
- cite_ids: S01-SH-C082
- from: new

**Citation S01-SH-C082:** `https://help.shopify.com/en/manual/payments/shopify-payments/payouts.md` | introduction | 2026-10-12 | kind: stated | quote check: found (markup removed)
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/067-help.shopify.com/text.txt` (fetched 2026-10-11T06:13:02Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/035-help.shopify.com/text.txt` (fetched 2026-10-12T10:50:13Z, captured)
- quote: After a customer pays for an order using Shopify Payments and specific accelerated checkouts, the funds are transferred to the payout bank account that you set up with Shopify Payments.
- title: Getting paid with Shopify Payments
- the page opens: After a customer pays for an order using Shopify Payments and specific accelerated checkouts, the funds are transferred to the payout bank account that you set up with Shopify Payments. The following types of accounts can accept Shopify Payments payouts: * a checking account that meets the bank account requirements for Shopify Payments in your country * a Shopify Balance account In certain countries, there's a minimum payout amount for Shopify Payments. To check whether your country has a minimu…
- headings: Getting paid with Shopify Payments
- in context: Getting paid with Shopify Payments ⟪After a customer pays for an order using Shopify Payments and specific accelerated checkouts, the funds are transferred to the payout bank account that you set up with Shopify Payments.⟫ The following types of accounts can accept Shopify Payments payouts: * a checking account that meets the bank account requirements for Shopify Payments in your country * a Shopify Balance account In certain countries, there's a minimum payout amount for Shopify Payments. To check whether your country has a minimum payout amount, review the Minimum payout amounts section of the Shopify Payments country where your store is based. With Shopify Paym…  (matched markup removed)

### Q5-SH-P0010

**Cited at:** section 1, line 43; section 8, line 191

**Record** (`studies/proposals/records/Q5/shopify/copied-pilot.tsv`):
- stmt_id: S01-SH-009
- bullet: a;b
- placement: responsible
- identifier: Part I, A. The Payment Processor
- statement: By accepting this Agreement and the Payment Processor Terms for your Designated Country you are agreeing to open financial accounts and/or cryptocurrency wallets with one or more Payment Processors for Payment Processing (each a "Payment Processor Account").
- cite_ids: S01-SH-C011
- from: new

**Citation S01-SH-C011:** `https://www.shopify.com/legal/terms-shopify-payments` | Part I, A. The Payment Processor | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/149-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/119-shopify.com/text.txt` (fetched 2026-10-12T10:51:25Z, captured)
- quote: By accepting this Agreement and the Payment Processor Terms for your Designated Country you are agreeing to open financial accounts and/or cryptocurrency wallets with one or more Payment Processors for Payment Processing (each a "Payment Processor Account").
- title: Shopify Payments Terms of Service - Shopify
- in context: …parate terms of service identified in the Payment Processor List (the "Payment Processor Terms"). By accepting this Agreement, you are also accepting and agreeing to be bound by all of the Payment Processor Terms applicable in your Designated Country, which, in each case, is a legal agreement between you and the applicable Payment Processor. Shopify is not a party to any of the Payment Processor Terms and is not liable to you in respect thereof. ⟪By accepting this Agreement and the Payment Processor Terms for your Designated Country you are agreeing to open financial accounts and/or cryptocurrency wallets with one or more Payment Processors for Payment Processing (each a "Payment Processor Account").⟫ You authorize Shopify to determine which Payment Processor Account(s) we will facilitate opening on your behalf, and where you have multiple Payment Processor Accounts, which Payment Processor shall perform Payment Processing services for each Transaction. We reserve the right to change the Payment Processors, subject to the terms of our agreement with each Payment Processor. In the event of any inconsistency between this Agreement and any of th…

### Q5-SH-P0028

**Cited at:** section 1, line 45; section 2, line 88

**Record** (`studies/proposals/records/Q5/shopify/copied-pilot.tsv`):
- stmt_id: S01-SH-027
- bullet: a;c
- placement: decides
- identifier: Part I, C. Reserves
- statement: We, in our discretion, will set the terms of any Reserve Account and notify you of such terms, which may require that a certain amount (including the full amount) of the funds received for a Transaction are held for a period of time
- cite_ids: S01-SH-C039
- from: index:SH-C-070:SH-S-0112

**Citation S01-SH-C039:** `https://www.shopify.com/legal/terms-shopify-payments` | Part I, C. Reserves | 2026-10-10 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/149-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/119-shopify.com/text.txt` (fetched 2026-10-12T10:51:25Z, captured)
- quote: We, in our discretion, will set the terms of any Reserve Account and notify you of such terms, which may require that a certain amount (including the full amount) of the funds received for a Transaction are held for a period of time
- title: Shopify Payments Terms of Service - Shopify
- in context: …citly agree that all communication in relation to delinquent accounts will be made by electronic mail or by phone, as provided to Shopify by you. Such communication may be made by Shopify or by anyone on its behalf, including, but not limited to, a third-party collection agent. Reserves. Funds held in reserves are amounts set aside to cover chargebacks, refunds, disputes, or other payment obligations under this Agreement (the "Reserve Account"). ⟪We, in our discretion, will set the terms of any Reserve Account and notify you of such terms, which may require that a certain amount (including the full amount) of the funds received for a Transaction are held for a period of time⟫, or that additional amounts are held in the Reserve Account. We, in our discretion, may elect to change the terms of a Reserve Account at any time, for any reason, based on your payment processing history or as requested by the Payment Processors. We may require you to fund the Reserve Account by means of: (i) any funds payouts made or due to you for Transactions submitted to the Payments Services; or, (ii) amounts available in your Payout Accou…

### Q5-SH-074

**Cited at:** section 1, line 46; section 2, line 90

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-074
- bears_on: 5
- identifier: Shop Cash credit
- statement: Shop Cash credits are included in your Shopify Payments payouts. There isn't a separate Shop Cash payout account or separate bank deposit for Shop Cash.
- cite_ids: Q5-SH-C113
- from: held

**Citation Q5-SH-C113:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shop-cash/payouts-and-reconciliation.md` | Payout timing for Shop Cash payments | undated | kind: stated | quote check: found
- quote: Shop Cash credits are included in your Shopify Payments payouts. There isn't a separate Shop Cash payout account or separate bank deposit for Shop Cash.
- title: Reconciling Shop Cash payouts
- the page opens: Shop Cash payout transactions are included in Shopify Payments payout activity. You can use payout details, payout exports, transaction types, and order IDs to reconcile money movement for orders that include Shop Cash. Shop Cash transactions can settle separately from the card or Shop Pay Installments portion of the same order. If your store uses accounting software, an enterprise resource planning (ERP) system, or payout exports, then confirm that your reconciliation workflow accounts for Shop…
- headings: Reconciling Shop Cash payouts > Payout timing for Shop Cash payments {#payout-timing-for-shop-cash-payments}
- in context: …created as a balance transaction on your Shopify Payments balance. 6. The next eligible [Shopify Payments payout](/manual/payments/shopify-payments/payouts) includes that balance transaction. The remaining order balance, when there is one, is paid with Shop Pay or Shop Pay Installments and reconciled through the payment transactions that apply to that payment method. ## Payout timing for Shop Cash payments {#payout-timing-for-shop-cash-payments} ⟪Shop Cash credits are included in your Shopify Payments payouts. There isn't a separate Shop Cash payout account or separate bank deposit for Shop Cash.⟫ Shop Cash payments are processed 4 times daily, at 12:00 am, 6:00 am, 12:00 pm, and 6:00 pm Eastern Time (ET). Depending on how many Shop Cash orders were placed after the last processing time, each **Shop Cash credit** payout transaction might cover one or multiple orders. The Shop Cash portion and the other payment method on the same order can be included in different payouts. For example, the card portion can post as a charge at capture time,…

### Q5-SH-P0050

**Cited at:** section 1, line 47; section 2, line 83

**Record** (`studies/proposals/records/Q5/shopify/copied-pilot.tsv`):
- stmt_id: S01-SH-049
- bullet: c;end-payment;end-payout
- placement: where
- identifier: How you get paid
- statement: When you set up a payment provider to accept credit card payments, each payment must be processed, so there's usually a delay between when the customer pays for their order and when you receive the payment. After the payment is processed, the purchase amount is transferred to your merchant account.
- cite_ids: S01-SH-C064
- from: new

**Citation S01-SH-C064:** `https://help.shopify.com/en/manual/payments/getting-paid.md` | How you get paid | 2026-10-12 | kind: stated | quote check: found (markup removed)
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/051-help.shopify.com/text.txt` (fetched 2026-10-11T06:13:00Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/030-help.shopify.com/text.txt` (fetched 2026-10-12T10:50:08Z, captured)
- quote: When you set up a payment provider to accept credit card payments, each payment must be processed, so there's usually a delay between when the customer pays for their order and when you receive the payment. After the payment is processed, the purchase amount is transferred to your merchant account.
- title: Getting paid
- the page opens: All Shopify-supported payment methods rely on third-party providers to process your transactions. These providers might charge extra fees and enforce rules about what products you can sell using their service. When you set up a payment method, check with the company providing the service to make sure you understand their rules and fees. How you get paid When you set up a payment provider to accept credit card payments, each payment must be processed, so there's usually a delay between when the c…
- a note box: Note Payouts aren't sent on bank holidays.
- headings: Getting paid
- in context: Getting paid All Shopify-supported payment methods rely on third-party providers to process your transactions. These providers might charge extra fees and enforce rules about what products you can sell using their service. When you set up a payment method, check with the company providing the service to make sure you understand their rules and fees. How you get paid ⟪When you set up a payment provider to accept credit card payments, each payment must be processed, so there's usually a delay between when the customer pays for their order and when you receive the payment. After the payment is processed, the purchase amount is transferred to your merchant account.⟫ Some payment providers, such as PayPal Express Checkout, have their own methods of transferring funds from your customer to you. Check with the payment provider that you're using to confirm how they pay you. You can accept manual payments outside of your online checkout, such as money orders or bank transfers. If you don't activate Shopify Payments as your payment provider, then you're charged third-party transaction fees for all orders that are…  (matched markup removed)

### Q5-SH-K1686

**Cited at:** section 1, line 49; section 8, line 209

**Record** (`studies/proposals/records/Q5/shopify/copied.tsv`):
- concern_id: SH-C-075
- placement: boundary
- structure: https://help.shopify.com/en/manual/payments/getting-paid.md
- identifier: Shop Pay Installments
- statement: Payouts for these orders are included with your Shopify Payments payouts.
- cite_ids: SH-S-0317
- note: first run's citation, moved from where: the sentence states how Shop Pay Installments orders meet payouts, which is a boundary

**Citation SH-S-0317:** `https://help.shopify.com/en/manual/payments/getting-paid.md` | Shop Pay Installments | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/051-help.shopify.com/text.txt` (fetched 2026-10-11T06:13:00Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/030-help.shopify.com/text.txt` (fetched 2026-10-12T10:50:08Z, captured)
- quote: Payouts for these orders are included with your Shopify Payments payouts.
- title: Getting paid
- the page opens: All Shopify-supported payment methods rely on third-party providers to process your transactions. These providers might charge extra fees and enforce rules about what products you can sell using their service. When you set up a payment method, check with the company providing the service to make sure you understand their rules and fees. How you get paid When you set up a payment provider to accept credit card payments, each payment must be processed, so there's usually a delay between when the c…
- a note box: Note Payouts aren't sent on bank holidays.
- headings: Getting paid > How often you get paid with Shopify Payments > Shop Pay Installments
- in context: …k holidays.</p> </aside> ### Shop Pay Installments After you [capture the payment](/manual/fulfillment/managing-orders/payments/capturing-payments) for an order placed using Shop Pay Installments, you receive full payment for your order with your other Shopify Payments transactions excluding [the fee incurred for using Shop Pay Installments](/manual/payments/shop-pay-installments/getting-paid#processing-rates-and-fees-for-shop-pay-installments). ⟪Payouts for these orders are included with your Shopify Payments payouts.⟫ The Shop Pay Installments fee includes the standard Shopify Payments credit card rate. You don't have to collect payments from your customers. Learn more about [Shop Pay Installments](/manual/payments/shop-pay-installments). ## How much you get paid You can be charged several third-party transaction fees for online transactions. For credit card transactions, the issuer, the acquirer, and the credit card company all charge a small fee for using t…

### Q5-SH-K1736

**Cited at:** section 1, line 50; section 2, line 56; section 2, line 57

**Record** (`studies/proposals/records/Q5/shopify/copied.tsv`):
- concern_id: SH-C-079
- placement: boundary
- structure: https://help.shopify.com/en/manual/payments/manual-payments.md
- identifier: help.shopify.com/en/manual/payments/manual-payments.md
- statement: Orders that accept manual payments are marked as unpaid on the **Orders** page.
- cite_ids: SH-S-0386
- note: first run's citation, moved from where: the sentence states how manual payments meet orders (marked as unpaid), which is a boundary

**Citation SH-S-0386:** `https://help.shopify.com/en/manual/payments/manual-payments.md` | introduction | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/052-help.shopify.com/text.txt` (fetched 2026-10-11T06:13:01Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/031-help.shopify.com/text.txt` (fetched 2026-10-12T10:50:09Z, captured)
- quote: Orders that accept manual payments are marked as unpaid on the **Orders** page.
- title: Manual payment methods
- the page opens: Some customers don't want to pay for their orders using a credit card. These customers can still place their orders online if you set up a manual payment method. When your customers use a manual payment method, you can arrange to receive their payment in a way that works best for them. You can send an invoice to your customer. After you receive the payment, you can then manually approve the order. Common types of manual payments include cash on delivery (COD), money orders, and bank transfers. I…
- a note box: Note You aren't charged third-party transaction fees for manual payments.
- headings: Manual payment methods
- in context: …he order. Common types of manual payments include cash on delivery (COD), money orders, and bank transfers. If your store and your customers are based in Canada, then you can accept [email money transfers](/manual/payments/manual-payments/email-money-transfers). <aside class="note"><h4>Note</h4><p>You aren't charged <a href="/en/manual/your-account/manage-billing/billing-charges">third-party transaction fees</a> for manual payments.</p> </aside> ⟪Orders that accept manual payments are marked as unpaid on the **Orders** page.⟫ After you receive payment for a customer's order, you can mark the order as paid on the order details page and fulfill the order as you would if they had made an online payment. To begin using manual payments, you have two options: you can either utilize a suggested manual payment method or create a custom manual payment method. ## Use a suggested manual payment method You can choose from a list of suggested manual payment methods on the **Payme…

### Q5-SH-093

**Cited at:** section 1, line 50; section 2, line 80

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-093
- bears_on: 5
- identifier: Orders · #1004
- statement: You manually marked YER699.95 as paid for this order.
- scope: store demo-fake-dev-store, observed 2026-09-30; countryCode YE, currencyCode YER
- cite_ids: Q5-SH-C140;Q5-SH-C141
- from: held

**Citation Q5-SH-C140:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T014656Z-journey-order-lifecycle/steps/011.aria.yaml` | step 11 | 2026-09-30 | kind: observed | quote check: found
- step 11: open More fulfillment options | https://admin.shopify.com/store/demo-fake-dev-store/orders/6406748504199?newlyCreated=true | "demo fake dev store · Orders · #1004 · Shopify" | 2026-09-30T01:50:45.931Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T014656Z-journey-order-lifecycle/steps/011.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T014656Z-journey-order-lifecycle/steps/011.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T014656Z-journey-order-lifecycle/011.html.txt`
- quote: You manually marked YER699.95 as paid for this order.
- in context: …al YER699.95 Paid YER699.95 - heading "Timeline" [level=2] - text: Comment - button "Comment" - text: Comment - textbox "Comment": - /placeholder: Leave a comment... - text: Leave a comment... - button "Add emoji" - button "Mention staff" - button "Reference page" - button "Attach file" - button "Post" [disabled] - paragraph: Only you and other staff can see comments - heading "Today" [level=3] - list: - listitem - listitem - listitem: - button "⟪You manually marked YER699.95 as paid for this order.⟫" - paragraph: Just now - listitem: - paragraph: "Confirmation #KACCWWG8Q was generated for this order." - paragraph: Just now - listitem: - paragraph: - text: You created this order from draft order - link "#D16": - /url: /store/demo-fake-dev-store/draft_orders/1074296881287 - text: . - paragraph: Just now - complementary: - heading "Notes" [level=2] - group "Customer section": - heading "Customer" [level=2] - heading "Shipping address" [level=2…

**Citation Q5-SH-C141:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T024857Z-buyer-prereq/answers/admin.shopify.com/PaymentProviders/9775ff01e35806e60ce7a40e2bcae1e94f7d62bc4df43c9f7cfbf1fee80dcc6b.json` | operation PaymentProviders, store demo-fake-dev-store, step 2 | 2026-09-30 | kind: stated | quote check: found
- quote: "url":"https://demo-fake-dev-store.myshopify.com","countryCode":"YE","currencyCode":"YER"
- in context: …,"__typename":"FraudProtectSettings"},"features":{"highRiskOrdersWithFlow":{"onboardingStage":"NEEDS_FLOW","__typename":"HighRiskOrdersWithFlow"},"__typename":"ShopFeatures","threeDSecureEligibilityForCountry":false,"sellsSubscriptions":true,"bankAccountChangesLocked":false},"checkoutSettings":{"shippingBehaviour":"MANUAL","__typename":"CheckoutSettings"},"__typename":"Shop","name":"demo fake dev store","description":"Fake demo meta description",⟪"url":"https://demo-fake-dev-store.myshopify.com","countryCode":"YE","currencyCode":"YER"⟫,"checkoutExtensibilityMigrationStatus":"MIGRATED","accountOwner":{"id":"gid://shopify/StaffMember/103047463047","name":"Demo-name demo-last-name","email":"7amza.it@gmail.com","__typename":"StaffMember"},"plan":{"trial":false,"shopifyPlus":false,"__typename":"ShopPlan"},"entitlements":{"multiPrimaryGateways":true,"__typename":"EntitlementsType"},"developmentShop":true,"multiLegalEntitiesPhase":"INELIGIBLE"},"paymentAuthorizationSettings":{"id":"g…

### Q5-SH-001

**Cited at:** section 2, line 58; section 2, line 59; section 3, line 99

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-001
- bears_on: 1;3
- identifier: Payments
- statement: If you want to let your customers pay using a credit card, then you can use Shopify Payments, a third-party provider, or both together.
- cite_ids: Q5-SH-C001
- from: held

**Citation Q5-SH-C001:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments.md` | Payments (introduction) | undated | kind: stated | quote check: found (markup removed)
- quote: If you want to let your customers pay using a credit card, then you can use Shopify Payments, a third-party provider, or both together.
- title: Payments
- the page opens: Make sure that you understand the payment process. When a customer checks out, they can choose to pay for their order using any of the methods that you've activated in the Payment providers area of your Shopify admin. You can activate a variety of payment methods using Shopify. If you want to let your customers pay using a credit card, then you can use Shopify Payments, a third-party provider, or both together. There are also several ways for customers to pay online without using a credit card, …
- a note box: Note For customers based in Finland, a payment method won't be selected by default during checkout to comply with regulations.
- a note box: Note If you sell subscription products, then you need to use Shopify Payments as your primary payment gateway. To learn more about subscriptions, refer to Subscriptions.
- headings: Payments
- in context: Payments Make sure that you understand the payment process. When a customer checks out, they can choose to pay for their order using any of the methods that you've activated in the Payment providers area of your Shopify admin. You can activate a variety of payment methods using Shopify. ⟪If you want to let your customers pay using a credit card, then you can use Shopify Payments, a third-party provider, or both together.⟫ There are also several ways for customers to pay online without using a credit card, such as PayPal, Amazon Pay, and Apple Pay. You might also want to accept additional methods of payment such as cryptocurrency. If you use Shopify Payments, then you can activate Shop Pay to allow customers to save their shipping and payment information to help them check out faster. Some other payment providers, such as Paypal, Amazon Pay, Apple Pay, and Google …  (matched markup removed)

### Q5-SH-053

**Cited at:** section 2, line 66

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-053
- bears_on: 1
- identifier: Additional payment method apps
- statement: Each additional payment method app has its own requirements for authentication and configuration, but typically, you're asked to log in or create an account with the payment provider.
- cite_ids: Q5-SH-C066
- from: held

**Citation Q5-SH-C066:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/additional-payment-methods/activate-payment-methods.md` | Configure and activate your additional payment method app | undated | kind: stated | quote check: found
- quote: Each additional payment method app has its own requirements for authentication and configuration, but typically, you're asked to log in or create an account with the payment provider.
- title: Activating additional payment methods
- the page opens: To provide your customers with more payment options at checkout, you can activate additional payment methods on your Shopify store. Additional payment methods include options such as PayPal Express Checkout, buy now, pay later services, and regional payment methods. These are separate from the credit card provider configured through the Shopify Payments or Payment providers sections of Settings > Payments. To set up a credit card provider, refer to configure a third-party payment provider. Activ…
- a note box: Note Support for ActiveMerchant payment providers can either be found on their website, or using the link provided in their About section.
- headings: Activating additional payment methods > Additional payment method apps {#additional-payment-method-apps} > Configure and activate your additional payment method app {#configure-activate-additional-payment-method-app}
- in context: …ion, click **Add payment methods**. 3. Search and select by payment methods or by provider. 4. Choose a provider from the search results, and then click **Activate**. 5. Click **Install app** to install the additional payment method app. ### Configure and activate your additional payment method app {#configure-activate-additional-payment-method-app} You need to configure and then activate your additional payment method app before you can use it. ⟪Each additional payment method app has its own requirements for authentication and configuration, but typically, you're asked to log in or create an account with the payment provider.⟫ After you activate the additional payment method app, the payment method is visible on checkout. #### Steps: 1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments). 2. In the **Additional payment methods** section, click **Add payment methods**. 3. Search and select by payment methods or by provider. 4. Choose a provider from the search results, and then click **Activate**. 5. Click **Manage*…

### Q5-SH-040

**Cited at:** section 2, line 74

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-040
- bears_on: 3;5
- identifier: Payment method routing
- statement: When you use Shopify Payments alongside a third-party provider, each payment method is routed to a specific provider.
- cite_ids: Q5-SH-C050
- from: held

**Citation Q5-SH-C050:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/using-shopify-payments-with-a-third-party-provider.md` | Payment method routing | undated | kind: stated | quote check: found
- quote: When you use Shopify Payments alongside a third-party provider, each payment method is routed to a specific provider.
- title: Using Shopify Payments with a third-party provider
- the page opens: You can use Shopify Payments alongside a direct third-party payment provider in the same store. In this setup, your third-party provider is the primary processor for credit and debit card transactions, and Shopify Payments handles additional payment methods your third-party provider doesn't support, such as Shop Pay and local payment methods. You can also use Shopify Payments to recover failed card transactions from your third-party provider, helping to reduce lost sales. Note Before you use Sho…
- a note box: Note Before you use Shopify Payments, review the following requirements: Shopify Payments is only available to online stores in certain countries and regions. If you operate a retail store, then check the list of countries that support Shopify Payments for in-person selling. To use Shopify Payments,
- headings: Using Shopify Payments with a third-party provider > Payment method routing
- in context: …elling-with-multiple-entities). * [Shopify Capital](/manual/finance/shopify-capital/index) eligibility is based on total sales from both providers. * [Shopify Protect](/manual/payments/shop-pay/shopify-protect/index) covers only transactions processed through Shopify Payments. * [Shopify Balance](/manual/finance/shopify-balance/index) remains available regardless of which provider processes the majority of transactions. ## Payment method routing ⟪When you use Shopify Payments alongside a third-party provider, each payment method is routed to a specific provider.⟫ <div> <table> <caption>How payment methods are routed when using Shopify Payments alongside a third-party provider.</caption> <thead> <tr> <th scope="col">Payment method</th> <th scope="col">Primary provider</th> <th scope="col">Backup provider</th> </tr> </thead> <tbody> <tr> <td scope="row">Credit and debit cards</td> <td>Third-party provider</td> <td>Shopify Payments</td> </tr> <tr> <td scope="row">Wallets offered by the third-party provider<…

### Q5-SH-026

**Cited at:** section 2, line 85

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-026
- bears_on: 5
- identifier: How you get paid
- statement: If customers pay using third-party payment gateways, then you can't view payout information in your Shopify admin.
- cite_ids: Q5-SH-C030
- from: held

**Citation Q5-SH-C030:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/getting-paid.md` | How you get paid | undated | kind: stated | quote check: found
- quote: If customers pay using third-party payment gateways, then you can't view payout information in your Shopify admin.
- title: Getting paid
- the page opens: All Shopify-supported payment methods rely on third-party providers to process your transactions. These providers might charge extra fees and enforce rules about what products you can sell using their service. When you set up a payment method, check with the company providing the service to make sure you understand their rules and fees. How you get paid When you set up a payment provider to accept credit card payments, each payment must be processed, so there's usually a delay between when the c…
- a note box: Note Payouts aren't sent on bank holidays.
- headings: Getting paid > How you get paid
- in context: …de of your online checkout, such as money orders or bank transfers. If you don't activate Shopify Payments as your payment provider, then you're charged third-party transaction fees for all orders that aren't brokered financially by Shopify. This includes all orders that go through Shopify's checkout system. If you've activated Shopify Payments, then you receive payouts when customers pay using Shopify Payments or specific accelerated checkouts. ⟪If customers pay using third-party payment gateways, then you can't view payout information in your Shopify admin.⟫ <div> <table> <caption>Descriptions of different payment providers and their types, how customers make payments with each provider, and how you get paid with each provider.</caption> <thead> <tr> <th scope="col">Payment provider</th> <th scope="col">Provider type</th> <th scope="col">How the customer pays</th> <th scope="col">How you get paid</th> </tr> </thead> <tbody> <tr> <td scope="row">Shopify Payments</td> <td>Payment gateway</td> <td>Usin…

### Q5-SH-064

**Cited at:** section 7, line 160; section 8, line 194

**Record** (`studies/proposals/records/Q5/shopify/statements.tsv`):
- stmt_id: Q5-SH-064
- bears_on: 5
- identifier: Settlements
- statement: Settlements. All Payments Applications must settle transactions for the Merchants within a maximum of 5 days, as outlined in the Payments Platform Developer Guidelines.
- cite_ids: Q5-SH-C099
- from: held

**Citation Q5-SH-C099:** `https://www.shopify.com/partners/terms` | C.4. Additional Terms Applicable to Payments Developers, Settlements | 2026-02-27 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/152-shopify.com/text.txt` (fetched 2026-10-11T06:13:12Z, captured)
- quote: Settlements. All Payments Applications must settle transactions for the Merchants within a maximum of 5 days, as outlined in the Payments Platform Developer Guidelines.
- title: Shopify Partner Program - Partner Program Agreement - Shopify
- in context: …atform Developer Guidelines. New Payments Application Feature Approval. Any updates or changes to an existing Payments Application, including the addition of new product features or new payment methods, must be submitted for review and approval. Merchant Flexibility. Payments Applications must allow for Shopify Merchants to terminate their agreement with the payment provider within 7 days' notice, without any penalty, fine, or other consequence. ⟪Settlements. All Payments Applications must settle transactions for the Merchants within a maximum of 5 days, as outlined in the Payments Platform Developer Guidelines.⟫ Wind Down Period. If Payments Developer wishes to no longer support the Payments Application, the Parties agree to the following arrangement for a period not to exceed six (6) months following the effective date of termination (the "Wind Down Period"). Notwithstanding the foregoing, if the Agreement is terminated as a result of a material breach by Payments Developer, then the Wind Down Period will not exceed a period of one (1) month, or such o…

### Q5-SH-P0002

**Cited at:** section 7, line 166; section 8, line 185

**Record** (`studies/proposals/records/Q5/shopify/copied-pilot.tsv`):
- stmt_id: S01-SH-001
- bullet: a
- placement: responsible
- identifier: Part I, A. The Shopify Payments Service, Our Role
- statement: You hereby appoint us as your agent to deliver information and instructions on your behalf to one or more payment processors that provide such financial services (each a "Payment Processor") or other service providers
- cite_ids: S01-SH-C001
- from: index:SH-C-064:SH-S-0079

**Citation S01-SH-C001:** `https://www.shopify.com/legal/terms-shopify-payments` | Part I, A. The Shopify Payments Service, Our Role | 2026-10-10 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/149-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/119-shopify.com/text.txt` (fetched 2026-10-12T10:51:25Z, captured)
- quote: You hereby appoint us as your agent to deliver information and instructions on your behalf to one or more payment processors that provide such financial services (each a "Payment Processor") or other service providers
- title: Shopify Payments Terms of Service - Shopify
- in context: …gnated Country supplement, and where expressly stated, modify, the Global Terms. Part I (Global Terms) A. The Shopify Payments Service Our Role. The Shopify Payments service ("Shopify Payments" or the "Payments Services") is Shopify's integrated payments solution that arranges for the financial services you need to accept payments, and allows you to manage your payments directly on Shopify, in each case as more fully described in this Agreement. ⟪You hereby appoint us as your agent to deliver information and instructions on your behalf to one or more payment processors that provide such financial services (each a "Payment Processor") or other service providers⟫, in each case, in connection with the Payments Services. Under the separate Shopify Terms of Service (the "Shopify Platform Terms"), the applicable Shopify Contracting Party (as defined therein) provides you with its online storefront, shopping cart, store management, marketing, and other services (collectively, the "Shopify Platform Services"). The Shopify Platform Terms are incorporated herein by reference and by accepting this Agreement you a…

### Q5-SH-P0024

**Cited at:** section 7, line 166; section 8, line 206

**Record** (`studies/proposals/records/Q5/shopify/copied-pilot.tsv`):
- stmt_id: S01-SH-023
- bullet: a;end-payout
- placement: responsible
- identifier: Part I, C. Security Interest
- statement: As security for performance of your obligations under this Agreement, you grant us a first priority lien and security interest on all funds processed and deposited into all bank accounts, cryptocurrency wallets, or other financial accounts designated in your Shopify Admin to receive funds from the settlement of Transactions (the "Payout Account"), and any other bank accounts, cryptocurrency wallets, or other financial accounts associated with your Shopify Payments Account, and in any funds processed using the Payment Processing services.
- cite_ids: S01-SH-C033;S01-SH-C032
- from: index:SH-C-065:SH-S-0111
- note: The index excerpt ends before the definition of the Payout Account; the rest of the sentence was read again on 2026-10-12 and is cited separately.

**Citation S01-SH-C033:** `https://www.shopify.com/legal/terms-shopify-payments` | Part I, C. Security Interest | 2026-10-10 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/149-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/119-shopify.com/text.txt` (fetched 2026-10-12T10:51:25Z, captured)
- quote: As security for performance of your obligations under this Agreement, you grant us a first priority lien and security interest on all funds processed and deposited into all bank accounts, cryptocurrency wallets, or other financial accounts designated in your Shopify Admin
- title: Shopify Payments Terms of Service - Shopify
- in context: … Shopify Payments again, the then current Fees shall apply to you. In addition to the Fees, you are also responsible for any penalties and fines imposed on you or on us by any bank, money services business, payment network, financial institution, or other financial intermediary resulting from your use of the Payments Services in a manner not permitted by this Agreement or by such financial intermediary's rules and regulations. Security Interest. ⟪As security for performance of your obligations under this Agreement, you grant us a first priority lien and security interest on all funds processed and deposited into all bank accounts, cryptocurrency wallets, or other financial accounts designated in your Shopify Admin⟫ to receive funds from the settlement of Transactions (the "Payout Account"), and any other bank accounts, cryptocurrency wallets, or other financial accounts associated with your Shopify Payments Account, and in any funds processed using the Payment Processing services. These security interests and liens will secure payment and performance of all of your obligations under this Agreement and any other agreements now existing or later entered into…

**Citation S01-SH-C032:** `https://www.shopify.com/legal/terms-shopify-payments` | Part I, C. Security Interest | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/149-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/119-shopify.com/text.txt` (fetched 2026-10-12T10:51:25Z, captured)
- quote: to receive funds from the settlement of Transactions (the "Payout Account"), and any other bank accounts, cryptocurrency wallets, or other financial accounts associated with your Shopify Payments Account, and in any funds processed using the Payment Processing services.
- title, opening and note boxes: as for this source's citation above
- in context: …diary resulting from your use of the Payments Services in a manner not permitted by this Agreement or by such financial intermediary's rules and regulations. Security Interest. As security for performance of your obligations under this Agreement, you grant us a first priority lien and security interest on all funds processed and deposited into all bank accounts, cryptocurrency wallets, or other financial accounts designated in your Shopify Admin ⟪to receive funds from the settlement of Transactions (the "Payout Account"), and any other bank accounts, cryptocurrency wallets, or other financial accounts associated with your Shopify Payments Account, and in any funds processed using the Payment Processing services.⟫ These security interests and liens will secure payment and performance of all of your obligations under this Agreement and any other agreements now existing or later entered into between us and you, including, without limitation, your obligation to pay any amounts due and owing to us. You will execute, deliver and pay the fees for any documents we request, and authorize Shopify to take any other action necessary including registering notice of s…

### Q5-SH-K1566

**Cited at:** section 7, line 167

**Record** (`studies/proposals/records/Q5/shopify/copied.tsv`):
- concern_id: SH-C-064
- placement: responsible
- structure: https://www.shopify.com/legal/processor-list
- identifier: B. North America, row United States
- statement: Stripe, Inc.
- scope: Designated Country United States
- cite_ids: SH-S-0152
- note: first run's citation

**Citation SH-S-0152:** `https://www.shopify.com/legal/processor-list` | B. North America, row United States | 2026-10-10 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/139-shopify.com/text.txt` (fetched 2026-10-11T06:13:10Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/116-shopify.com/text.txt` (fetched 2026-10-12T10:51:22Z, captured)
- quote: Stripe, Inc.
- title: Payment Processors for Shopify Payments - Shopify
- in context: …inesses Stripe Prohibited and Restricted Businesses Debit Authorization User Bank Account Debit Authorization Mexico Stripe Payments Mexico, S. de RL de CV. Account Terms Stripe Connected Account Agreement Stripe Services Agreement Stripe Payment Method Terms Privacy Policy Stripe Privacy Policy Prohibited and Restricted Businesses Stripe Prohibited and Restricted Businesses Debit Authorization User Bank Account Debit Authorization United States ⟪Stripe, Inc.⟫ Account Terms Stripe Connected Account Agreement Stripe Services Agreement Stripe Payment Method Terms Privacy Policy Stripe Privacy Policy Prohibited and Restricted Businesses Stripe Prohibited and Restricted Businesses Debit Authorization User Bank Account Debit Authorization United States PayPal, Inc. Account Terms PayPal User Agreement Privacy Policy PayPal Privacy Statement Prohibited and Restricted Businesses PayPal Acceptable Use Policy D…

### Q5-SH-P0033

**Cited at:** section 8, line 173; section 8, line 200

**Record** (`studies/proposals/records/Q5/shopify/copied-pilot.tsv`):
- stmt_id: S01-SH-032
- bullet: a;b;c
- placement: responsible
- identifier: Part I, D. Effects of Termination
- statement: Any funds in the Financial Services Provider's custody will be paid out to you subject to the Payment Processor Terms.
- cite_ids: S01-SH-C045
- from: index:SH-C-065:SH-S-0118

**Citation S01-SH-C045:** `https://www.shopify.com/legal/terms-shopify-payments` | Part I, D. Effects of Termination | 2026-10-10 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/149-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/119-shopify.com/text.txt` (fetched 2026-10-12T10:51:25Z, captured)
- quote: Any funds in the Financial Services Provider's custody will be paid out to you subject to the Payment Processor Terms.
- title: Shopify Payments Terms of Service - Shopify
- in context: …tion and closing of your Shopify Payments Account, we will immediately discontinue your access to the Payments Services. You agree to complete all pending Transactions, immediately remove all logos for Cards, and stop accepting new Transactions through the Payments Services. You will not be refunded the remainder of any Fees that you have paid for the Payments Services if your access to or use of the Payments Services is terminated or suspended. ⟪Any funds in the Financial Services Provider's custody will be paid out to you subject to the Payment Processor Terms.⟫ Termination does not relieve you of your obligations as defined in this Agreement, and a Payment Processor may elect to continue to hold any funds deemed necessary, pending resolution of any other terms or obligations defined in this Agreement, including, but not limited to, chargebacks, disputes, fees, refunds, or other investigations or proceedings. Termination of this Agreement will not necessarily terminate your Shopify Platform Terms, unles…

### Q5-SH-P0076

**Cited at:** section 8, line 179

**Record** (`studies/proposals/records/Q5/shopify/copied-pilot.tsv`):
- stmt_id: S01-SH-075
- bullet: a;c;end-payout
- placement: responsible
- identifier: Scheduling your Shopify Payments payouts, note
- statement: Shopify Payments in the United States and France uses multiple payment processing partners to ensure that your payments and payouts are processed seamlessly. Although your payouts are sent from Shopify, they're processed by these partners. You might receive some payouts sooner than the scheduled payout date, and more than one payout per day.
- scope: Shopify Payments in the United States and France
- cite_ids: S01-SH-C112;S01-SH-C113
- from: new

**Citation S01-SH-C112:** `https://help.shopify.com/en/manual/payments/shopify-payments/payouts/schedule-payouts.md` | note | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/041-help.shopify.com/text.txt` (fetched 2026-10-12T10:50:19Z, captured)
- quote: Shopify Payments in the United States and France uses multiple payment processing partners to ensure that your payments and payouts are processed seamlessly. Although your payouts are sent from Shopify, they're processed by these partners.
- title: Scheduling your Shopify Payments payouts
- the page opens: Deciding when and how often to get your payouts can be an important part of managing your finances. With Shopify Payments, you can choose a daily, weekly, or monthly payouts schedule. There are no extra charges when you switch from one payouts schedule to another payouts schedule. If you have active Shopify Capital, or Shopify Credit, then your payout schedule options might be different. For merchants in Japan, you can choose a weekly or monthly payouts schedule, but you can't have a daily payou…
- a note box: Note Shopify Payments in the United States and France uses multiple payment processing partners to ensure that your payments and payouts are processed seamlessly. Although your payouts are sent from Shopify, they're processed by these partners. You might receive some payouts sooner than the schedule
- headings: Scheduling your Shopify Payments payouts
- in context: …outs schedule. There are no extra charges when you switch from one payouts schedule to another payouts schedule. If you have active [Shopify Capital](/manual/finance/shopify-capital/), or [Shopify Credit](/manual/finance/shopify-credit), then your payout schedule options might be different. For merchants in Japan, you can choose a weekly or monthly payouts schedule, but you can't have a daily payouts schedule. <aside class="note"><h4>Note</h4><p>⟪Shopify Payments in the United States and France uses multiple payment processing partners to ensure that your payments and payouts are processed seamlessly. Although your payouts are sent from Shopify, they're processed by these partners.⟫ You might receive some payouts sooner than the scheduled payout date, and more than one payout per day.</p> </aside> Understanding how monthly payouts are adapted for certain months helps with cash flow management. Specifically, monthly payouts originally set for a date beyond the current month's end are instead processed on the final day of that month, ensuring that you get timely payments. For example, if your monthly schedule is set to the 30…

**Citation S01-SH-C113:** `https://help.shopify.com/en/manual/payments/shopify-payments/payouts/schedule-payouts.md` | note | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/041-help.shopify.com/text.txt` (fetched 2026-10-12T10:50:19Z, captured)
- quote: You might receive some payouts sooner than the scheduled payout date, and more than one payout per day.
- title, opening and note boxes: as for this source's citation above
- headings: Scheduling your Shopify Payments payouts
- in context: …en your payout schedule options might be different. For merchants in Japan, you can choose a weekly or monthly payouts schedule, but you can't have a daily payouts schedule. <aside class="note"><h4>Note</h4><p>Shopify Payments in the United States and France uses multiple payment processing partners to ensure that your payments and payouts are processed seamlessly. Although your payouts are sent from Shopify, they're processed by these partners. ⟪You might receive some payouts sooner than the scheduled payout date, and more than one payout per day.⟫</p> </aside> Understanding how monthly payouts are adapted for certain months helps with cash flow management. Specifically, monthly payouts originally set for a date beyond the current month's end are instead processed on the final day of that month, ensuring that you get timely payments. For example, if your monthly schedule is set to the 30th of every month, then for the month of February in 2023, you would have been paid on February 28. Payo…

### Q5-SH-P0094

**Cited at:** section 8, line 188

**Record** (`studies/proposals/records/Q5/shopify/copied-pilot.tsv`):
- stmt_id: S01-SH-093
- bullet: c
- placement: decides
- identifier: Shopify Payments refunds
- statement: When you issue a refund through Shopify Payments, the refunded amount is deducted from your next available payout.
- cite_ids: S01-SH-C144
- from: new

**Citation S01-SH-C144:** `https://help.shopify.com/en/manual/payments/shopify-payments/payouts/refunds.md` | introduction | 2026-10-12 | kind: stated | quote check: found (markup removed)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/039-help.shopify.com/text.txt` (fetched 2026-10-12T10:50:17Z, captured)
- quote: When you issue a refund through Shopify Payments, the refunded amount is deducted from your next available payout.
- title: Shopify Payments refunds
- the page opens: When you issue a refund through Shopify Payments, the refunded amount is deducted from your next available payout. The refund status is marked as Pending for up to 2 business days. During this time, the funds are processed back to your customer. Due to varying processing times at your customer's bank, it might take up to 10 business days for the refunded amount to be received. Refunds are processed in accordance with your payout schedule, and are typically scheduled for the next payout. You can'…
- headings: Shopify Payments refunds
- in context: Shopify Payments refunds ⟪When you issue a refund through Shopify Payments, the refunded amount is deducted from your next available payout.⟫ The refund status is marked as Pending for up to 2 business days. During this time, the funds are processed back to your customer. Due to varying processing times at your customer's bank, it might take up to 10 business days for the refunded amount to be received. Refunds are processed in accordance with your payout schedule, and are typically scheduled for the next payout. You can't cancel or reverse a refund after you initiate a refund from yo…  (matched markup removed)

### Q5-SH-P0107

**Cited at:** section 8, line 197; section 8, line 203

**Record** (`studies/proposals/records/Q5/shopify/copied-pilot.tsv`):
- stmt_id: S01-SH-106
- bullet: c;end-payout
- placement: decides
- identifier: Part I, C. Processing Transactions and Receiving Your Funds, Settlement
- statement: Settlement. You get paid only after you pass our onboarding, KYC and underwriting checks. Settlement of your valid Transactions, net of fees, refunds, chargebacks, reserves, and other amounts owed, will be paid to your Payout Account. Payouts from your sales may be held until you pass all of our onboarding, identity and KYC checks. Once you pass, funds owed will be paid into your Payout Account. If you do not pass, funds may be held or refunded to your customers, in accordance with applicable law and Network Rules.
- scope: Designated Countries where the Payment Facilitator Terms apply (Part II: EU / EEA; United Kingdom)
- cite_ids: S01-SH-C168;S01-SH-C169
- from: new

**Citation S01-SH-C168:** `https://www.shopify.com/legal/terms-payfac` | Part I, C. Processing Transactions and Receiving Your Funds, Settlement | 2026-09-22 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/147-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/118-shopify.com/text.txt` (fetched 2026-10-12T10:51:24Z, captured)
- quote: Settlement. You get paid only after you pass our onboarding, KYC and underwriting checks. Settlement of your valid Transactions, net of fees, refunds, chargebacks, reserves, and other amounts owed, will be paid to your Payout Account.
- title: Shopify Payments Facilitator Terms (Merchant Agreement) - Shopify
- in context: …use the Payments Services for any business or activity on the Acquirer's prohibited/restricted list, or otherwise prohibited by Payment Network Rules. Compliance with Payment Network Rules and PCI-DSS. You will comply with all applicable Payment Network Rules and maintain PCI-DSS compliance. The Payment Networks are third-party beneficiaries of this obligation to the extent their rules require. C. Processing Transactions and Receiving Your Funds ⟪Settlement. You get paid only after you pass our onboarding, KYC and underwriting checks. Settlement of your valid Transactions, net of fees, refunds, chargebacks, reserves, and other amounts owed, will be paid to your Payout Account.⟫ Payouts from your sales may be held until you pass all of our onboarding, identity and KYC checks. Once you pass, funds owed will be paid into your Payout Account. If you do not pass, funds may be held or refunded to your customers, in accordance with applicable law and Network Rules. Fees. You owe the fees disclosed to you in the Shopify Admin for the Payments Services. Applicable fees will be withheld from your payouts. We may instead appoint …

**Citation S01-SH-C169:** `https://www.shopify.com/legal/terms-payfac` | Part I, C. Processing Transactions and Receiving Your Funds, Settlement | 2026-09-22 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/147-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/118-shopify.com/text.txt` (fetched 2026-10-12T10:51:24Z, captured)
- quote: Payouts from your sales may be held until you pass all of our onboarding, identity and KYC checks. Once you pass, funds owed will be paid into your Payout Account. If you do not pass, funds may be held or refunded to your customers, in accordance with applicable law and Network Rules.
- title, opening and note boxes: as for this source's citation above
- in context: …le Payment Network Rules and maintain PCI-DSS compliance. The Payment Networks are third-party beneficiaries of this obligation to the extent their rules require. C. Processing Transactions and Receiving Your Funds Settlement. You get paid only after you pass our onboarding, KYC and underwriting checks. Settlement of your valid Transactions, net of fees, refunds, chargebacks, reserves, and other amounts owed, will be paid to your Payout Account. ⟪Payouts from your sales may be held until you pass all of our onboarding, identity and KYC checks. Once you pass, funds owed will be paid into your Payout Account. If you do not pass, funds may be held or refunded to your customers, in accordance with applicable law and Network Rules.⟫ Fees. You owe the fees disclosed to you in the Shopify Admin for the Payments Services. Applicable fees will be withheld from your payouts. We may instead appoint one or more of our affiliates to invoice and collect, on our behalf, the fees and other amounts you owe under this Supplement, and you authorize each affiliate we appoint to do so. Reserves. Shopify may impose a Reserve and may set off amounts you owe. Chargebacks and payments disputes…
