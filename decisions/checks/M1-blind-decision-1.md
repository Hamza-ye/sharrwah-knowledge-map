# M1 blind decision 1: who holds the money

Evidence: `observed-sh` at `febbf6c98a1f`, `observed-sa` at `4ca2e896a729` (assumption: working trees unmodified). `HC` = `observed-sh/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/`; `SAT` = `observed-sa/structures/salla/help-articles/en/texts.jsonl`.

## 1. The question

Between a buyer's payment and the seller's payout, who holds the money? Guarded forms: A, Sharrwah holds it; B, a payment company holds it in an account opened through Sharrwah.

## 2. What the references show

1. Shopify's own service has a payment company behind it: "the only payment gateway designed and operated by Shopify" … "Stripe is Shopify Payments' banking partner" (`HC/third-party-providers/payment-gateway-availability.md:17`).
2. Its money waits in a balance: "funds between a merchant's Shopify Payments balance and their [`ShopifyPaymentsBankAccount`]" (`observed-sh/structures/shopify/admin-graphql-schema/2026-10/items.jsonl:3223`).
3. It is conditional: "only available to online stores in <a href="/en/manual/payments/shopify-payments/supported-countries">certain countries and regions</a>" (`HC/shopify-payments.md:9`).
4. Shopify sellers can use their own provider accounts: "Enter your account credentials for the provider that you selected." (`HC/third-party-providers/configuring-providers.md:32`).
5. Shopify then charges a fee and shows no payouts: "third-party transaction fees for all orders that aren't brokered financially by Shopify" (`HC/getting-paid.md:11`); "you can't view payout information" (`HC/getting-paid.md:13`).
6. Both offer offline payment: "After you receive payment for a customer's order" (`HC/manual-payments.md:10`); "complete the bank transfer immediately" (`SAT:496`).
7. Salla's own service keeps the money in a balance: "Electronic Payments is a service provided by Salla"; "Funds go into your Electronic Payments balance" (`SAT:25`).
8. Salla takes from that balance itself: "its value is automatically held from your electronic payments balance"; "Salla settles the amounts with the carrier after deducting Salla's commission" (`observed-sa/structures/salla/dashboard-translations/en/apps.json:1`, `apps.managed_settlement.how_it_works`).
9. It is conditional: "only start using electronic payment gateways after your store verification is complete" (`SAT:448`); two linked activation articles name different markets: "Activate Salla payments in" (`SAT:1047`, `SAT:1081`).
10. Salla sellers can connect their own provider accounts: "payments flow straight through to your account" (`SAT:319`).

## 3. Options

- **O1, seller's own provider account:** the seller's provider settles to the seller; Sharrwah holds nothing. Shopify (4–5), Salla (10).
- **O2, offline:** the buyer pays the seller outside checkout. Both (6; Salla's payee is interpretation).
- **O3, form B:** a payment company holds the seller's balance, in an account opened through the platform. Shopify Payments (1–3; interpretation: "banking partner" does not say who legally holds it).
- **O4, form A:** the platform holds the balance, takes from it, pays out. Salla's service as presented (7–9; interpretation: a partner behind it, making it B, is not excluded).

## 4. Decision

**Every market gets, built once:** O1 (the seller's credentials for a provider account they opened directly; Sharrwah records payment status); O2 (seller-defined offline methods; orders unpaid until marked paid); a per-market switch each for O3 and O4, off until a recorded founder's decision, with nothing built behind it. Interpretation: an account created through a Sharrwah sign-up flow is opened through Sharrwah (O3).

**Varies by market:** the market's row states O1's providers (only those whose own published coverage includes it) and the allowed offline methods; the founder alone binds O3 and O4, only where the row states their conditions.

**Recommendation for launch:** O1 and O2 everywhere; O3 and O4 off everywhere.

## 5. Consequences

All interpretation.
- Sharrwah holds no balance, payout or reserve; refunds and disputes stay between seller and provider.
- Sharrwah cannot take fees from the money or show payouts; it bills sellers separately, as Shopify does (fact 5).
- A market with no listed provider gets offline methods only.
- Switching O3 on adds a payment-company contract, seller verification through Sharrwah (fact 9), a balance and payout ledger, reserves and disputes; O4 adds these with Sharrwah holding the money. Neither moves sellers off O1.
- Cash on delivery stays O2 only while the courier pays the seller.

## 6. The market row

- **O1:** a provider integrated with Sharrwah serves sellers established there and settles to them directly.
- **O2:** each listed offline method may be accepted there, paid to the seller or the seller's own courier.
- **O3:** a payment company permitted there to hold sellers' funds in platform-opened accounts accepts Sharrwah; sellers can pass its verification; the founder has decided.
- **O4:** Sharrwah holds any authorisation required there to hold others' funds; the founder has decided.

## 7. Open

- Who legally holds the balance under Shopify Payments (Shopify or Stripe) and Salla's service (Salla or a partner). Not found in: `observed-sh/index/attempts.jsonl` (77 rows naming `shopify.com/legal`, none `legal/terms-payment`); `SAT` or its Arabic original (licensing or partnership wording); Salla's held `salla.com/terms` (holding, collection, agency, escrow wording: only a liability disclaimer naming payment gateways). Work: capture and read both platforms' payment-service terms.
- Whether Salla's "Cash on Delivery Balance" (`SAT:25`) is courier-collected money Salla holds. Work: read its cash-on-delivery articles.
- Salla's eligibility per provider, and Shopify's per-location provider lists (`HC/third-party-providers/payment-gateway-availability.md:7`), are unread. Work: capture both.
