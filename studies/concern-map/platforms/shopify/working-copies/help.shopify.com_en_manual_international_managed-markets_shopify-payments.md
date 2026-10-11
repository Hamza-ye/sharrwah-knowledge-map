# Managed Markets with Shopify Payments

Shopify Payments is used for all Managed Markets transactions and payouts. Managed Markets with Shopify Payments includes the following changes:

* Your Managed Markets transactions are processed through Shopify Payments.
* Payouts for Managed Markets orders are daily. The same as for any Shopify Payments transactions.
* All eligible Managed Markets orders are automatically protected with [Shopify Protect](/manual/payments/shop-pay/shopify-protect) (United States only).
* Different local payment methods are available for your customers.
* Shop Pay, Apple Pay, and Google Pay are supported. PayPal isn't supported.

All Managed Markets questions go to Shopify Support, regardless of the role that Global-e plays in the service. Global-e is your [merchant of record](/manual/international/managed-markets/overview#merchant-of-record) and handles parts of your Managed Markets orders, including duties, tax remittance, commercial invoices, and carrier arrangements. Requests about your orders, payouts, shipping labels, returns, and tax or customs documents still go through [Shopify Support](/manual/your-account/contact-shopify-support), and not to Global-e directly.

Global-e also has a standalone third-party app, which is different from Managed Markets. If you use the standalone Global-e app instead of Managed Markets, then Global-e supports you directly. You can't use Managed Markets and the Global-e app at the same time.


## Foreign exchange rates

When Managed Markets converts your prices into a customer’s local currency, the exchange rate that’s used is stabilized and guaranteed for a 30-day period with each order. Shopify stabilizes exchange rates so that your prices change less frequently, and to reduce currency volatility to help ensure that your payouts are more consistent. Rates are typically updated every 7 days. However, during periods of extreme market volatility where market rates move more than 5% from the stabilized rate, Shopify might update exchange rates (and as a result your prices) more frequently.

In addition, the stabilized exchange rate will differ from the current mid‑market rate to account for historical volatility and market fluctuations. When you receive an order, the exchange rate that’s active at the time the order is placed is guaranteed for 30 days. This ensures that you aren’t affected by rate fluctuations if you issue a refund during the 30-day period following the order.

## Pricing for Managed Markets {#pricing}

Managed Markets has the following fees for international orders that apply to the order total:

* A Shopify Payments processing fee that can vary based on your Shopify plan and the payment method used by your customer. You can view your Shopify Payments fees in the [**Payments**](https://admin.shopify.com/payments) page in your Shopify admin.
* A Managed Markets transaction fee:
   * 3.25% for stores on the Shopify Plus plan.
   * 3.5% for stores that are on the Basic, Grow, or Advanced plan.
* A [currency conversion fee](/manual/international/pricing/fees), also known as the foreign exchange (FX) fee. You can adjust your product prices for international markets to be higher or lower based on your preferences.

<aside class="note"><h4>Note</h4><p>When your prices are automatically converted to local currencies, they&#39;re increased to cover the conversion fee, which is a percentage of the gross order total deducted from your payout. For example, in the United States, this factor is determined using the formula <code>1 / (1 - 1.5%) = 1.0152</code> to ensure that the conversion fee is fully covered by the customer.</p>
</aside>

Managed Markets doesn't have a monthly fee, and there's no set time period that you need to commit to using Managed Markets. You can stop using Managed Markets at any time.

<aside class="note"><h4>Note</h4><p>Using an external fulfillment service might incur additional fees. Contact your fulfillment service for information if you&#39;re not sure whether your service charges additional fees.</p>
</aside>

If you use B2B, then the transaction fee isn't applied to your international B2B orders. [B2B orders aren't compatible with Managed Markets](/manual/international/managed-markets/fulfillment#b2b-orders-with-managed-markets).

## Flow of funds

Managed Markets features are powered by Global-e. After an international Managed Markets order is placed in your store, Shopify Payments processes the transaction and holds the money in a Global-e account.

When you ship cross-border with Global-e, they act as your merchant of record. Global-e holds the funds to remit the costs to proper authorities that are involved in the cross-border commerce transaction.

## Getting paid

You receive payouts for Managed Markets orders daily. The length of time between the date that a customer's payment is captured and the date that your payout is sent to your bank account depends on the country that your store is based in.

Managed Markets transactions are displayed as Shopify Payments on your bank account and credit card statements.

### Calculating Managed Markets payouts without international pricing

You can use the following calculation to calculate Managed Markets payouts:

`Total order cost` – `(remitted tax/VAT + remitted duty + Shopify Payments processing fee + Managed Markets fee + currency conversion fee)` = `Amount paid`

For example, suppose that an order is placed for a shirt with a total cost of €150 EUR. The currency conversion rate on the day of the transaction is used to calculate your payout amount into your currency. For this example, your store is based in the United States, and €150 EUR is a converted total of $158.97 USD ($1 USD = €0.94364EUR). The following is the total breakdown of the order:

**What the customer pays**

* a shirt costs €120 EUR
* duties cost €5 EUR ($5.30 USD withheld)
* taxes and VAT cost €10 EUR ($10.60 USD withheld)
* international shipping costs €15 EUR

In this example, your customer pays €150 EUR to Global-e. Global-e remits the following costs:

* the cost of €10 EUR tax/VAT to the government
* the cost of €5 EUR duties to the customs agencies

**What you pay**

* Shopify Payments processing fees of $6.50 USD (3.9% + $0.30 USD of the total order value)
  * The Shopify Payments fees depend on your Shopify plan, and the payment method used by your customer in the transaction. You can view your current fees in the [**Payments**](https://admin.shopify.com/payments) page in your Shopify admin.
* Managed Markets fee of $5.56 USD (3.5% of the total order value)
  * The Managed Markets fee for Shopify Plus is 3.25%
* The currency FX fee of $2.38 USD is paid for currency conversion. The FX fee is calculated on the total order value ($158.97 USD).

You can add these amounts to what the customer pays by making [price adjustments](/manual/markets/customizations/catalogs).

After all these costs are taken out, you receive $128.63 USD.

You need to decide how much you want to charge your customer for shipping. Managed Markets includes [shipping rates recommendations](/manual/international/managed-markets/shipping/set-up-shipping#shipping-rates) for better conversion. The shipping fee that you collect from your customer is included in your payout. The cost of the shipping label that you purchase is charged to the credit card that's on file for your Shopify account.

### Calculating Managed Markets payouts with international pricing {#adaptive-pricing}

For example, suppose you have a shirt on your US store that's priced at $180 USD in your local currency, and sell to a customer in the United Kingdom. The following is a breakdown of calculations for an order for this shirt:

* Duties and import taxes are $57.68 USD.
* The 3.25% Managed Markets fee is $8.11 USD.
* The 1.5% currency conversion fee is $3.74 USD.
* The subtotal for your item is $249.53 USD.
* After currency conversion and rounding, the price of the item in your store for your customer is £185 GBP.

Your customer purchases the shirt and pays for shipping with DHL eCommerce Parcel Direct. Your customer has already paid for duties, import taxes, and fees, so your payout is calculated using the following formula:

`Total order cost` – `Shopify Payments fee` = `Amount paid`

In this example, the following is a breakdown of how your payout is calculated:

* Your payout for your product is $180 USD.
* Your payout for shipping fees is $14.58 USD.
* Your gross payout is $194.58 USD.
* Your Shopify Payments fee is $9.04 USD.

The net amount added to your payouts is $185.54 USD (`194.58` – `9.04` = `185.54`).

## Fraud and chargebacks

Eligible Managed Markets orders are automatically protected with [Shopify Protect](/manual/payments/shop-pay/shopify-protect) for stores based in the United States. Shopify Protect offers chargeback protection from fraud, such as fraudulent and unrecognized chargebacks.

## Local payment methods with Managed Markets {#local-payment-methods}

With Managed Markets, you can use more local payment methods for markets worldwide. For example, if you're selling products to customers in Denmark, then those customers can pay for products with Klarna using DKK currency.

New local payment methods are continuously being added to Managed Markets.

Review the following tables to learn more about currently available local payment methods with Shopify Payments, their geographic coverage, and available currencies.

### Local payment methods available for Managed Markets in the United States

<table>
  <caption>List of US Managed Markets local payment methods and their corresponding regions and currencies.</caption>
  <thead>
     <tr>
        <th scope="col">Payment method</th>
        <th scope="col">Country</th>
        <th scope="col">Currency</th>
     </tr>
  </thead>
  <tbody>
     <tr>
        <td scope="row" rowspan="6">Klarna</td>
        <td>Austria, Belgium, Czechia, Finland, France, Germany, Greece, Ireland, Italy, Netherlands, Poland, Portugal, Romania, Spain, and Switzerland</td>
        <td>EUR</td>
     </tr>
     <tr>
        <td scope="row">United Kingdom</td>
        <td>GBP</td>
     </tr>
     <tr>
        <td scope="row">Denmark</td>
        <td>DKK</td>
     </tr>
     <tr>
        <td scope="row">Norway</td>
        <td>NOK</td>
     </tr>
     <tr>
        <td scope="row">Sweden</td>
        <td>SEK</td>
     </tr>
     <tr>
        <td scope="row">Poland</td>
        <td>PLN</td>
     </tr>
     <tr>
        <td scope="row">MobilePay</td>
        <td>Denmark and Finland</td>
        <td>EUR, DKK, SEK, and NOK</td>
     </tr>
     <tr>
        <td scope="row">Blik</td>
        <td>Poland</td>
        <td>PLN</td>
     </tr>
     <tr>
        <td scope="row">EPS</td>
        <td>Austria</td>
        <td>EUR</td>
     </tr>
     <tr>
        <td scope="row">Multibanco</td>
        <td>Portugal</td>
        <td>EUR</td>
     </tr>
          <tr>
        <td scope="row">Bancontact</td>
        <td>Belgium</td>
        <td>EUR</td>
     </tr>
  </tbody>
</table>

### Local payment methods available for Managed Markets in the United Kingdom

<table>
  <caption>List of UK Managed Markets local payment methods and their corresponding regions and currencies.</caption>
  <thead>
     <tr>
        <th scope="col">Payment method</th>
        <th scope="col">Country</th>
        <th scope="col">Currency</th>
     </tr>
  </thead>
  <tbody>
     <tr>
        <td scope="row" rowspan="6">Klarna</td>
        <td>Austria, Belgium, Czechia, Finland, France, Germany, Greece, Ireland, Italy, Netherlands, Poland, Portugal, Romania, Spain, and Switzerland</td>
        <td>EUR</td>
     </tr>
     <tr>
        <td scope="row">United Kingdom</td>
        <td>GBP</td>
     </tr>
     <tr>
        <td scope="row">Denmark</td>
        <td>DKK</td>
     </tr>
     <tr>
        <td scope="row">Norway</td>
        <td>NOK</td>
     </tr>
     <tr>
        <td scope="row">Sweden</td>
        <td>SEK</td>
     </tr>
     <tr>
        <td scope="row">Poland</td>
        <td>PLN</td>
     </tr>
     <tr>
        <td scope="row">MobilePay</td>
        <td>Denmark and Finland</td>
        <td>EUR, DKK, SEK, and NOK</td>
     </tr>
     <tr>
        <td scope="row">Blik</td>
        <td>Poland</td>
        <td>PLN</td>
     </tr>
     <tr>
        <td scope="row">EPS</td>
        <td>Austria</td>
        <td>EUR</td>
     </tr>
     <tr>
        <td scope="row">Multibanco</td>
        <td>Portugal</td>
        <td>EUR</td>
     </tr>
          <tr>
        <td scope="row">Bancontact</td>
        <td>Belgium</td>
        <td>EUR</td>
     </tr>
  </tbody>
</table>

### Local payment methods available for Managed Markets in Canada

<table>
  <caption>List of Canadian Managed Markets local payment methods and their corresponding regions and currencies.</caption>
  <thead>
     <tr>
        <th scope="col">Payment method</th>
        <th scope="col">Country</th>
        <th scope="col">Currency</th>
     </tr>
  </thead>
  <tbody>
     <tr>
        <td scope="row">MobilePay</td>
        <td>Denmark and Finland</td>
        <td>EUR, DKK, SEK, and NOK</td>
     </tr>
     <tr>
        <td scope="row">Blik</td>
        <td>Poland</td>
        <td>PLN</td>
     </tr>
     <tr>
        <td scope="row">EPS</td>
        <td>Austria</td>
        <td>EUR</td>
     </tr>
     <tr>
        <td scope="row">Multibanco</td>
        <td>Portugal</td>
        <td>EUR</td>
     </tr>
          <tr>
        <td scope="row">Bancontact</td>
        <td>Belgium</td>
        <td>EUR</td>
     </tr>
  </tbody>
</table>
