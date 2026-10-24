# Fees and costs

When you sell in local currencies you're charged the regular Shopify Payments processing fee and a currency conversion fee.

You can find the fee values in your [Terms of Service](https://admin.shopify.com/shopify-payments/terms).

You can [view a breakdown](/manual/markets/customizations/catalogs) of how each product price is calculated for each market.

## Shopify Payments fee

Shopify Payments charges a fee for processing each payment, with the rate varying based on card type and location. When you capture the payment for an order, you're charged a Shopify Payments fee (in your payout currency) which covers the cost of processing the payment. The fee amount depends on the type of credit card that is used and the location where the credit card is registered. For example, the amount for a Visa card fee can sometimes be different from the amount for an American Express card fee. The following are the types of processing fees that Shopify Payments charges: 

   * Payment processing fees (Domestic): The cost to process credit cards that are issued in the same country or region as your store.
   * Payment processing fees (Cross border): The cost to process credit cards that are issued in a country or region that is different from the one that is associated with your store.

## Third-party transaction fee

Third-party transaction fees cover the cost for Shopify to provide a secure checkout platform and integrate with external payment providers. Transaction fees vary depending on the [Shopify plan](https://www.shopify.com/pricing) that you choose, and are charged in the following circumstances:

* When you use a [third-party payment provider](/manual/payments/third-party-providers) to accept customer payments.
* When an order includes [store credit](/manual/customers/store-credit) or [gift cards](/manual/products/gift-card-products) as a payment method, on Shopify stores created on or after May 12, 2025. For example, if your store uses Shopify Payments and a customer pays for an order using both a credit card and $10 CAD of store credit, then you're charged third-party transaction fees only on the $10 CAD of store credit.

<aside class="note"><h4>Note</h4><p>For Shopify stores created on or after May 12, 2025, orders that include <a href="/en/manual/customers/store-credit">store credit</a> or <a href="/en/manual/products/gift-card-products">gift cards</a> as a payment method are charged third-party transaction fees on the amount paid for using store credit or gift cards. Store credit and gift card transaction fees don&#39;t apply to Shopify stores created before May 12, 2025.</p>
</aside>

When you use [Shopify Payments](/manual/payments/shopify-payments), you aren't charged third-party transaction fees for orders that are processed using the following payment methods:

* Shopify Payments
* Shop Pay
* Shop Pay Installments
* Manual payment methods such as cash, cash on delivery (COD), and bank transfers.

If you elect to use Shopify Payments as your primary payment provider, then PayPal transactions are exempt from third-party transaction fees.


## Conversion rate and fee

Currency conversion involves both an exchange rate and a fee when you accept payments in a currency different from your payout currency. When you accept payment in a currency that is different from your payout currency, then a currency conversion occurs. The amount that you receive in your customer's local currency (also referred to as the _presentment_ currency) is converted to your payout currency, and you're charged a currency conversion fee:

* **Currency conversion rate** - The market rate at which one currency is exchanged for another. The conversion rate isn't a fee (it's a mid-market rate, without any markup). For example, a conversion rate of USD/EUR `0.8788` means that $1 USD is exchanged for &euro;0.87 EUR.
* **Currency conversion fee** - The fee that Shopify charges (in your payout currency) to convert currencies when you capture a payment. Currency conversion fees and credit card fees are not returned to you when you issue a refund, but you're not charged additional conversion fees when you issue a refund or when you receive a chargeback. 

### Shopify Payments currency conversion fee

The conversion fee amount is based on your store's primary country. If you accept transactions in a non-domestic currency, then a currency conversion fee is applied.

<table>
  <caption>Information about the currency conversion fee that Shopify charges when you capture payment in a non-domestic currency with international sales tools.</caption>
  <thead>
     <tr>
        <th scope="col"></th>
        <th scope="col">United States</th>
        <th scope="col">France</th>
        <th scope="col">All other Shopify Payments regions</th>
     </tr>
  </thead>
  <tbody>
     <tr>
        <td scope="row">Currency conversion fee</td>
        <td>1.5%</td>
        <td>2%</td>
        <td>2%</td>
     </tr>
  </tbody>
</table>


### PayPal Wallet for Shopify Payments currency conversion fee

If you activate PayPal Wallet for [Shopify Payments in the United States](/manual/payments/shopify-payments/supported-countries/united-states/paypal-wallet) or [Shopify Payments France](/manual/payments/shopify-payments/supported-countries/france/paypal-wallet), then a currency conversion rate is applied.

<table>
  <caption>Information about the currency conversion fee that Shopify charges when you capture payment in a non-domestic currency with PayPal Wallet via Shopify Payments.</caption>
  <thead>
     <tr>
        <th scope="col"></th>
        <th scope="col">United States</th>
        <th scope="col">France</th>
        <th scope="col">All other Shopify Payments regions</th>
     </tr>
  </thead>
  <tbody>
     <tr>
        <td scope="row">Currency conversion fee </td>
        <td>3%</td>
        <td>3%</td>
        <td>Not available</td>
     </tr>
  </tbody>
</table>

After the currency conversion fee has been calculated, it's included in your customer's price to help offset your costs.

The currency conversion rate and fee for each order are included in the order's [Timeline](/manual/shopify-admin/productivity-tools/timeline) by clicking the `[payout amount] will be added to your [date] payout` message. Your payout itself displays in your store's payout currency.

<aside class="note"><h4>Note</h4><p>When you accept payment in a currency that is different from your payout currency, the currency conversion fee is charged whether you use <a href="/en/manual/international/pricing/exchange-rates#auto-convert">automatic exchange rates</a> or <a href="/en/manual/international/pricing/exchange-rates#manual-exchange-rate-conversions">set exchange rates manually</a>.</p>
</aside>

### International transaction fee

International transaction fees are charged by banks to customers making cross-border purchases, but these fees aren't charged to you as the merchant. _International transaction fees_ (or _foreign transaction fees_) might be charged to your international customers by their bank or credit card issuer, even when their credit card is charged in their local currency. For example, if your business is based in the United States and a customer in Canada places an order, then their bank might apply an international transaction fee even if their credit card was charged in CAD.

These fees vary and are set and collected by your customer's bank or credit card issuer—they aren't controlled by Shopify in any way. International customers can reach out to their bank or credit card issuer to learn more about these fees.
