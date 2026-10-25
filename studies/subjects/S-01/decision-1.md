# Decision 1: who holds sellers' money

**What this file is:** a decision page for the founder, in the plan's form (`PLAN.md`, section 5). It rests on the pilot's register entry ([`entry.md`](entry.md)), unchanged since G1, and on the facts found since, each linked to its source. Links into the pilot and into Stage 1 open them as they stood at G1.

## The question

Between a buyer paying and the seller being paid out, who holds the money? It is yours to decide, because getting it wrong is expensive: "money flows, legal structure and partner contracts" ([the pilot's analysis](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/analysis.tsv?plain=1#L2)).

## The options

From the pilot's entry ([options](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/entry.md?plain=1#L116-L121)):
- **A.** Sharrwah holds the money, in a balance it keeps for each seller.
- **B.** A payment company holds it, in an account the seller opens through Sharrwah.
- **C.** Each payment method's own provider holds it, in the seller's own account with that provider. For cash on delivery, the seller's courier holds it until it settles with the seller. Paid by bank transfer or in cash, it goes to the seller.
- **Defer.** Only the interface is built.

## Recommendation: C, in every market at launch

The pilot recommended "C for Yemen now, behind one interface that can also carry A or B, bound per market" ([entry](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/entry.md?plain=1#L123)). What has been found since makes it C in every market at launch, with A and B switched off until you decide:
1. **The references hold money in several ways at once, set per market, store or plan.** By the plan's rule, that gives one interface, bound per market, with the choice yours ([the pilot's analysis](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/analysis.tsv?plain=1#L2)).
2. **Both references' own payment services come with conditions, market by market.**
   - Shopify Payments "is only available to online stores in" "certain countries and regions" ([Shopify](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/payments/shopify-payments.md?plain=1#L9)). Where it is supported, "Stripe won't be available for you to activate" ([Shopify](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/payments/third-party-providers/payment-gateway-availability.md?plain=1#L17)).
   - Salla Payments needs "all three requirements": "Your store is on Salla Plus, Pro, or Special.", "Your store verification is complete." and "Payments have been enabled for your store by the Salla team." ([Salla, Kuwait](https://help.salla.sa/en/article/how-to-activate-salla-payments-in-kuwait-salla/mjir4s69o8flma11ypfthcsx) (held: record 651 of observed-sa's `structures/salla/help-articles/en/texts.jsonl` at `4ca2e89`); [Salla, UAE](https://help.salla.sa/en/article/enable-payment-methods-in-your-store-uae/z2mys3spo71u3yovhs7lhii4) (held: record 566 of observed-sa's `structures/salla/help-articles/en/texts.jsonl` at `4ca2e89`)).

   *My reading:* so A and B are switches per market, and your guard makes each switch yours.
3. **What every market shares is C.**
   - Both let a seller use its own account with a provider. Shopify: "Select the provider that you want to use from the list." and "Enter your account credentials for the provider that you selected." ([Shopify](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/payments/third-party-providers/configuring-providers.md?plain=1#L30)). Salla, with a gateway the seller connects: "payments flow straight through to your account" ([Salla](https://help.salla.sa/en/article/connect-moyasar-payment-gateway/zm2rkn8lfc8gjd6drybo2tvh) (held: record 318 of observed-sa's `structures/salla/help-articles/en/texts.jsonl` at `4ca2e89`)).
   - Both take payment outside any provider. Shopify: "After you receive payment for a customer's order, you can mark the order as paid" ([Shopify](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/payments/manual-payments.md?plain=1#L10)). Salla: "customers must complete the bank transfer immediately and upload the payment receipt during checkout." ([Salla](https://help.salla.sa/en/article/customize-order-settings-1/v5jrh4oz46bfkh8u0dnnlk8v) (held: record 495 of observed-sa's `structures/salla/help-articles/en/texts.jsonl` at `4ca2e89`)). That article doesn't say whose account receives the transfer.
4. **In Yemen, C is what is shown working.** These facts are from Stage 1, read with [its corrections](../../yemen-cases/corrections.md).
   - The pilot found none of the references' own holding services shown to work there ([its marks](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/yemen-marks.tsv?plain=1#L2-L7)). Stripe, for one, is not supported for a business in Yemen (YA-62, corrected).
   - A courier collects payment on delivery for business accounts ([YK-203](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/constants.tsv?plain=1#L204)). Buyers pay online sellers by money transfer ([YA-131](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L132)). A wallet's own page says the amount is "added to your Cash Wallet account" ([YE-E765](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9d0de523f1852ebf7716f0da01b6b619edc5e8fc/evidence/yemen/runs/20261010T050304Z-cited-sources/items/211-cash.com.ye/text.txt?plain=1#L36)).
   - Holding money there would need a licence. In the internationally recognized government's area, payment services need one from the central bank ([YA-102](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/yemen-cases/axes.tsv?plain=1#L103), read with its caution in the corrections).

**A test, not a source.** Made from the references alone, without Yemen, the decision comes out the same: an agent that never saw Yemen reached C at launch, with A and B off until you decide ([the test of 25 October](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/4923e1c96a0296abdaf3f5bdbd8c155e09acfebf/decisions/checks/M1-blind-decision-1.md)). It adds no fact. *My reading:* Yemen's facts are not what makes the recommendation.

Your guard already keeps A and B from going live without your decision ([`founder-decisions.tsv`](../../../founder-decisions.tsv)).

## Three edges of C, each with a default

These were found after G1, from the platforms' own pages. Each default is recommended for launch.
1. **An account a seller asks for through the platform, but holds under its own agreement with the provider, counts as C.**
   - On Salla, a store can "request a new Tabby Business account through Salla", and "Fees depend on the agreement between the merchant and Tabby" ([Salla](https://help.salla.sa/en/article/enabling-the-bnpl-tabby/dy7yvan3npix92pammram3jv) (held: record 576 of observed-sa's `structures/salla/help-articles/en/texts.jsonl` at `4ca2e89`)).
   - Shopify sets PayPal up with the store's email: "If you already have a PayPal account associated with the email that you use for your store, then you can start receiving payments immediately." ([Shopify](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/payments/paypal/set-up-paypal.md?plain=1#L3)).

   An account where Sharrwah would be party to the money, or to the provider's agreement for it, is B, and comes to you.
2. **Sharrwah's fees are billed apart. They are never taken from sellers' money at a provider.**
   - Shopify deducts from its own payment service: its card fees are "deducted from your payouts rather than billed on your Shopify bill" ([Shopify](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/your-account/manage-billing/billing-charges/types-of-charges.md?plain=1#L12)).
   - Where another provider holds the money, Shopify bills apart: "you're charged third-party transaction fees for all orders that aren't brokered financially by Shopify" ([Shopify](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/help-center/help.shopify.com%40en-ar/md/en/manual/payments/getting-paid.md?plain=1#L11)).
   - Salla's financing collects from the sales Salla holds: "Collection amounts are calculated from net Mada and credit card sales after payment fees and VAT on fees." ([Salla's dashboard text](https://github.com/Hamza-ye/observed-sa/blob/4ca2e896a729215f422a137a364e7e9488610ba3/structures/salla/dashboard-translations/en/payments.json)).

   *My reading:* taking fees from money at a provider would need an agreement Sharrwah is party to, which is B's side.
3. **No balance that sellers pay into, at launch.**
   - Salla's wallet lets sellers "Add funds", and its store balance pays for "Auto-renewing your subscription plan" ([Salla](https://help.salla.sa/en/article/wallet-invoices-saudi-arabia/g36cl2hlsv256gr55vutx5rv) (held: record 1240 of observed-sa's `structures/salla/help-articles/en/texts.jsonl` at `4ca2e89`)).
   - Such a balance would hold the seller's own funds through Sharrwah, like A.
   - Sharrwah bills its own fees by invoice or by card.

## What follows from your answer

Your answer settles the pilot's Decisions 2 to 12 too, as its entry pairs them with each option ([the table](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/entry.md?plain=1#L131-L149)), unless you say you want to answer any of them yourself:
- **C:**
  - each provider or courier settles, pays out and charges its own fees, on its own terms;
  - Sharrwah sends no payouts, is no seller's agent for receiving payments, and takes no security interest in sellers' money;
  - Sharrwah bills its own fees apart.
- **A or B:** Sharrwah, or the payment company, settles, pays out and takes its fees before payout, as the table's column for that letter says. Where you switch either on, it needs what the entry lists for it, such as a licence or a partner that will hold the money ([the options](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/studies/subjects/S-01/entry.md?plain=1#L116-L121)).
- **Defer:** each of them is set per market, when that market is set up, and your guard keeps A and B off meanwhile.

Decision 13, installments, and Decision 14, currency, come with the subjects that cover them.

## Answer

C, with the three defaults / C, with these changes: … / A or B (say which, and where) / defer (only the interface is built, and your guard keeps holding)
