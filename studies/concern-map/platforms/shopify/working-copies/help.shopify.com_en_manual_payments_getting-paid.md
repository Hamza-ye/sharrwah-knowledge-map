# Getting paid

All Shopify-supported payment methods rely on third-party providers to process your transactions. These providers might charge extra fees and enforce rules about what products you can sell using their service. When you set up a payment method, check with the company providing the service to make sure you understand their rules and fees.

## How you get paid

When you set up a payment provider to accept credit card payments, each [payment must be processed](/manual/payments/getting-paid#credit-card-payment-process), so there's usually a delay between when the customer pays for their order and when you receive the payment. After the payment is processed, the purchase amount is transferred to your merchant account.

Some payment providers, such as [PayPal Express Checkout](/manual/payments/paypal), have their own methods of transferring funds from your customer to you. Check with the payment provider that you're using to confirm how they pay you. 

You can accept [manual payments](/manual/payments/manual-payments) outside of your online checkout, such as money orders or bank transfers. If you don't activate Shopify Payments as your payment provider, then you're charged third-party transaction fees for all orders that aren't brokered financially by Shopify. This includes all orders that go through Shopify's checkout system.

If you've activated Shopify Payments, then you receive payouts when customers pay using Shopify Payments or specific accelerated checkouts. If customers pay using third-party payment gateways, then you can't view payout information in your Shopify admin.

<div>
<table>
  <caption>Descriptions of different payment providers and their types, how customers make payments with each provider, and how you get paid with each provider.</caption>
  <thead>
  <tr>
    <th scope="col">Payment provider</th>
    <th scope="col">Provider type</th>
    <th scope="col">How the customer pays</th>
    <th scope="col">How you get paid</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td scope="row">Shopify Payments</td>
    <td>Payment gateway</td>
    <td>Using Shopify Payments</td>
    <td>Through Shopify Payments</td>
  </tr>
    <tr>
    <td scope="row">Apple Pay</td>
    <td>Accelerated checkout</td>
    <td>Using Apple Pay</td>
    <td>Through Shopify Payments</td>
  </tr>
  <tr>
    <td scope="row">Amazon Pay</td>
    <td>Payment gateway</td>
    <td>Using Amazon Pay</td>
    <td>By Amazon</td>
  </tr>
   <tr>
    <td scope="row">Amazon Pay on Shopify Payments</td>
    <td>Accelerated checkout</td>
    <td>Using Amazon Pay</td>
    <td>Through Shopify Payments</td>
  </tr>
    <tr>
    <td scope="row">Google Pay</td>
    <td>Accelerated checkout</td>
    <td>Using Google Pay</td>
    <td>Through Shopify Payments</td>
  </tr>
    <tr>
    <td scope="row">PayPal Express Checkout</td>
    <td>Accelerated checkout</td>
    <td>Using PayPal</td>
    <td>By PayPal</td>
  </tr>
     <tr>
    <td scope="row">PayPal Wallet</td>
    <td>Accelerated checkout</td>
    <td>Using PayPal</td>
    <td>Through Shopify Payments for only France and the United States</td>
  </tr>
    <tr>
    <td scope="row">Shop Pay</td>
    <td>Accelerated checkout</td>
    <td>Using Shop Pay</td>
    <td>Through Shopify Payments</td>
  </tr>
  <tr>
    <td scope="row">Shop Pay Installments</td>
    <td>Payment gateway</td>
    <td>Using Shop Pay</td>
    <td>Through Shopify Payments</td>
  </tr>
  </tbody>
</table>
</div>

## How often you get paid with Shopify Payments

If you use Shopify Payments, then you can check your [payout timing](/manual/payments/shopify-payments/payouts/payout-timing) to view and configure when you receive payouts from Shopify Payments orders. Other payment providers have their own rules on when you receive payouts for credit card orders. Check with your provider to confirm how often you're paid.

After the payout is sent, it might not be received by your bank right away. It can take up to five days after the payout is sent for your bank to deposit it into your bank account. Shopify doesn't control the length of time between payouts arriving at your bank and your bank moving those funds into your account. Contact your bank if your payouts are delayed.

If you change banks or if your bank account details change, then you can update the information in your Shopify Payments settings. Learn more about [editing your bank account information](/manual/payments/shopify-payments/configuring-shopify-payments#edit-bank-account-information).

<aside class="note"><h4>Note</h4><p>Payouts aren&#39;t sent on bank holidays.</p>
</aside>

### Shop Pay Installments

After you [capture the payment](/manual/fulfillment/managing-orders/payments/capturing-payments) for an order placed using Shop Pay Installments, you receive full payment for your order with your other Shopify Payments transactions excluding [the fee incurred for using Shop Pay Installments](/manual/payments/shop-pay-installments/getting-paid#processing-rates-and-fees-for-shop-pay-installments). 

Payouts for these orders are included with your Shopify Payments payouts. The Shop Pay Installments fee includes the standard Shopify Payments credit card rate. You don't have to collect payments from your customers.

Learn more about [Shop Pay Installments](/manual/payments/shop-pay-installments).

## How much you get paid

You can be charged several third-party transaction fees for online transactions. For credit card transactions, the issuer, the acquirer, and the credit card company all charge a small fee for using their services.

You aren't charged third-party transaction fees for orders processed through [Shopify Payments](/manual/payments/shopify-payments). You pay [credit card processing fees](/manual/payments/shopify-payments/onboarding/), depending on your Shopify subscription plan. If you're using a third-party payment provider with Shopify, then you're charged a third-party transaction fee. If you [use Shopify Payments alongside a third-party provider](/manual/payments/shopify-payments/using-shopify-payments-with-a-third-party-provider), then fees vary depending on which provider processes each transaction.

## How a credit card payment gets processed {#credit-card-payment-process}

When a customer pays for their online order using a credit card, the payment has to be processed before the funds are added to your merchant account. Credit card processing is done for you by your payment provider.

This process has four stages: authorization, capture, clearing, and funding.

### Authorization

The customer uses their credit card to pay for the order on your store. The payment provider that you set up checks with the credit card issuer to make sure that the credit card is valid. If the card is valid and has enough funds, then the issuer authorizes the payment. No funds are transferred at this stage.

### Capture

After the payment is authorized, it must be captured. Capturing a payment sends the transaction details to the acquirer, which is a bank or financial institution that processes credit card transactions on behalf of your business.

### Clearing

The acquirer reviews the payment details, and then requests the necessary funds from the company that processes the customer's credit card.

The credit card company sends the transaction information to the issuer. The issuer subtracts a small fee from the total transaction amount, and then sends the remaining amount back to the credit card company. The card company subtracts their fee, and then sends the remaining amount to the acquirer.

### Funding

The acquirer subtracts a small fee from the amount, and then transfers the final amount to your merchant account.
