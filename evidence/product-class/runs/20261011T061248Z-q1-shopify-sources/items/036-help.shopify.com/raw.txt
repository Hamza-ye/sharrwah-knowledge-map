# Payments

Your market settings include a payments card that displays eligible [local payment methods](/manual/international/payments#local-payment-methods), as well as a link to your payment settings where you can activate and customize a variety of payment methods.

## Shopify Payments and other payment providers {#other-payment-providers}

Only stores with [Shopify Payments](/manual/payments/shopify-payments) or [Adyen](/manual/payments/third-party-providers/adyen-gateway) as the primary gateway can process payments in a customer's local currency. The following payment options are compatible with multi-currency processing:

* Shopify Payments credit card payments
* Shop Pay
* Apple Pay and Google Pay
* Paypal Express

If you use a different payment provider, then the local currency feature will only affect how prices are displayed to customers in your store. At checkout, the price will be converted to your store's default currency, and your customer will be charged in that currency.

Here's how the currency conversion process works for customers:

* Prices will display to customers in their local currency
* At checkout, prices will be converted to your store's default currency
* The final charge on their payment method will be in your store's default currency
* They might incur additional currency conversion fees from their payment provider

For example, your store currency is USD, and you sell a T-shirt for $10.00 USD. Your customer chooses to view your store using EUR, and the price of the T-shirt is listed at €8.90 EUR. If your customer checks out using a payment provider other than Shopify Payments or Adyen, then the price of the T-shirt is converted back to USD, and your customer might pay more than $10.00 USD for the T-shirt due to currency conversion fees from their payment provider. There are no currency conversion fees applied by Shopify when the currency is converted from USD to EUR for display purposes, and the **Order** page doesn't indicate that the order is a multi-currency order.

If your customer checks out using Shopify Payments or Adyen with a compatible payment method, then their payment is processed in their local currency. For example:

(**Product price** x **currency conversion rate**) + **currency conversion fee**

($10.00 USD x 0.867519) + 1.5% = €8.81 EUR

If you have rounding rules activated, then Shopify rounds the total up and your customer pays €8.90 EUR.

<aside class="note note-information"><h4>Tip</h4><p>If you want to encourage your customers to use multi-currency compatible payment methods, then use Shopify Scripts to <a href="/en/manual/checkout-settings/script-editor/examples/payment-gateway-scripts">hide other payment providers for customers who have a foreign currency at checkout</a>.</p>
</aside>

## Local payment methods {#local-payment-methods}

When a market contains a country that is eligible for one or more local payment methods, then a payments card is displayed in your market settings with the available local payment methods. For example, you have a market for Europe that only contains Belgium, then Bancontact is available on the payments card. If you have a market for Europe that contains both Belgium and Netherlands, then both Bancontact and iDEAL | Wero are available on the payments card.

From the payments card, you can activate or deactivate an eligible local payment method.

Learn more about [local payment methods](/manual/payments/shopify-payments/local-payment-methods).

## Set a currency for a market in Markets {#currency}

The currency that you select for a market is the currency that's displayed to customers on your online store, and that transactions are performed in. By default, the market's currency is set to the currency for the region that you've selected for your market. For markets that contain more than one region, **Use local currencies** is set as the default instead.

You can customize a market's currency at any time.

#### Steps:

1. From your Shopify admin, go to [**Markets**](https://admin.shopify.com/markets).


2. Click the market that you want to customize.
3. Click the `+` icon next to the **Currency** setting.
4. Click the currency, and then select the currency that you want to set for a market.
5. Select whether prices are rounded up after currency conversion.
6. Click **Done**.
7. In the top bar, click **Save**.
