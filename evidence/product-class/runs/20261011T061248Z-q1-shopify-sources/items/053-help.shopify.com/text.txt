# Payment authorization and capture

When a payment is captured, your customer is charged. By default, credit card payments and some additional methods of payment are captured automatically, but if it suits your business better, then you can change your store setting to capture payments manually.

In the [credit card payment process](/manual/payments/getting-paid#credit-card-payment-process), payments are authorized and then they must be captured within an [authorization period](/manual/payments/payment-authorization#credit-card-authorization-period). Capturing a payment sends credit card information to the customer’s bank for processing.

[Additional payment methods](/manual/payments/additional-payment-methods) and [Local payment methods](/manual/payments/shopify-payments/local-payment-methods/index) are processed differently than credit cards, but many providers support manual and automatic payment capture. If your store is set up to capture payments manually, but you add an additional payment provider that doesn't support manual payments, then payments on orders processed by that provider are captured automatically.

If you use Shopify Payments, another credit card payment provider, or providers for additional payment methods, then you need to decide how to capture payment from your customers. Payments can be captured in the following ways:

* [**Automatically at checkout**](/manual/payments/payment-authorization#set-up-automatic-payment-capture): Payment is captured at the time of sale or, in the case of additional payment methods, when the provider completes payment processing. Automatic payment capture at checkout is the default setting. This option saves you time when processing orders and is used by most merchants.
* [**Automatically when order is fulfilled**](/manual/payments/payment-authorization#automatic-at-fulfillment): Payment is **Authorized** at checkout and is automatically captured when the entire order is fulfilled before the payment authorization period expires. If you need to capture payment before the authorization expires or at an earlier time, then you can [capture the payment manually](/manual/fulfillment/managing-orders/payments/capturing-payments#capture-payment-early). You can also set a notification email to warn you 1 day before an authorization expires.
* [**Automatically capture per fulfillment (Shopify Plus plan only)**](/manual/payments/payment-authorization#capture-per-fulfillment): Payment is **Authorized** at checkout and payment is automatically captured when line items are fulfilled. This payment capture method is available instead of **Automatically when order is fulfilled**. If you need to capture payment before the authorization expires or at an earlier time, then you can [capture the payment manually](/manual/fulfillment/managing-orders/payments/capturing-payments#capture-payment-early). You can also set a notification email to warn you 1 day before an authorization expires.
* [**Manually**](/manual/payments/payment-authorization#set-up-manual-payment-capture): When an order's payment status is **Authorized**, you need to [capture payment](/manual/fulfillment/managing-orders/payments/capturing-payments) before you're paid for the order. Credit card payments must be captured within the authorization period. Capturing payment manually adds a delay and an extra step to your order processing workflow. You might set up manual payment for the following reasons:
    * Reviewing the [fraud analysis](/manual/fulfillment/managing-orders/protecting-orders/fraud-analysis) of an order before deciding to capture the transaction or cancel the order.
    * Complying with an accounting standard that requires capturing payment upon fulfillment.
    * Complying with a local regulation that prescribes online merchants must offer at least one payment method that allows your customer to pay for the order upon delivery.
    * Capturing [multiple payments](/manual/fulfillment/managing-orders/payments/capturing-payments#capture-payments-manually) using a supported payment provider.
    * Using a third-party app that automatically captures payment. Using an automatic payment capture setting in Shopify and a third-party app for automatically capturing payment can lead to potential conflicts and unexpected behavior.

If you use Shopify Payments, then it automatically routes each payment to the processor most likely to authorize it. This can improve authorization rates without any extra setup from you.

<aside class="note note-caution"><h4>Caution</h4><p>Payment capture settings apply only to orders that are placed in your online store. Point of sale (POS) orders aren&#39;t affected.</p>
</aside>

## What is a credit card authorization period? {#credit-card-authorization-period}

All credit card payment providers have an authorization period to allow a charge to be made to a customer's credit card. The [authorization process](/manual/payments/getting-paid#authorization) first checks that the credit card is valid, and then that the card has enough funds on it for the transaction.

The authorization period ends after a certain amount of time. The length of the authorization period depends on your credit card payment provider. You need to capture a payment within the authorization period to collect money for your order.

[Shopify Payments](/manual/payments/shopify-payments) provides an authorization period of 7 days.

<aside class="note"><h4>Note</h4><p>When you capture a payment made in a foreign currency, the amount is converted using the current conversion rate and <em>not</em> the rate at the time of authorization. The amount that is authorized is the maximum amount that you can capture. <a href="/en/manual/payments/payment-authorization#set-up-manual-payment-capture">Manually capturing a credit card payment</a> creates a time gap between when the credit card was authorized and when the payment is captured. This means that you might lose money depending on currency fluctuations.</p>
</aside>

### Authorization holds on customer bank statements

When a payment is authorized, the customer's bank might display a pending charge or hold on their account. This hold might display on the customer's bank statement up to 30 days after the original authorization, even if the payment was captured or the order was canceled. The timing depends on the customer's bank and card issuer.

If a customer asks about an unexpected charge and you've confirmed that they have a previous order with your store, then you can explain that this is a temporary authorization hold that their bank will release.

### Extended authorization periods

<aside class="note note-plan"><h4>Plan requirement</h4><p>Extended authorization periods are available only to stores on the Shopify Plus plan that use Shopify Payments.</p>
</aside>

Merchants that use the Shopify Plus plan have extended authorization periods when certain credit cards are used at checkout.

Extended authorization periods differ depending on the issuing bank of a credit card. Some cards might not support extended authorization periods, so you should monitor your [**Orders**](https://admin.shopify.com/orders) page for expiring authorizations.

When you manually capture a payment after the standard 7 day period, then a 1.75% charge applies to the transaction in addition to [standard credit card fees](/manual/payments/shopify-payments/onboarding/cost-of-shopify-payments).

<table>
  <caption>Comparison of credit card authorization periods by provider</caption>
  <thead>
    <tr>
      <th scope="col">Card type</th>
      <th scope="col">Authorization period</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row">Visa</td>
      <td>Up to 30 days</td>
    </tr>
    <tr>
      <td scope="row">Mastercard</td>
      <td>Up to 30 days</td>
    </tr>
    <tr>
      <td scope="row">Discover</td>
      <td>Up to 10 days</td>
    </tr>
    <tr>
      <td scope="row">JCB</td>
      <td>Up to 10 days</td>
    </tr>
    <tr>
      <td scope="row">American Express</td>
      <td>Up to 30 days</td>
    </tr>
    <tr>
      <td scope="row">Diners Club</td>
      <td>7 days</td>
    </tr>
    <tr>
      <td scope="row">China Union Pay</td>
      <td>7 days</td>
    </tr>
  </tbody>
</table>

If you have a payment that wasn't captured within 7 days and you don't want to incur this fee, then cancel the order and [create a new one](/manual/fulfillment/managing-orders/create-orders). The authorization expiry date displays on the **Orders** page.

<aside class="note note-caution"><h4>Caution</h4><p>To avoid extra charges, ensure that you capture payments within 7 days. Authorization periods and third-party transaction fees are subject to change.</p>
</aside>

## Set up automatic payment capture at checkout {#set-up-automatic-payment-capture}

Automatic payment capture at checkout is activated by default for new stores. If you're capturing payment manually but want to change the setting for your store, then you can activate automatic payment capture.

When automatic payment capture at checkout is activated, customers that pay with credit cards are automatically charged at the time of sale, and customers that pay with some additional payment methods are charged when the provider completes processing.

<aside class="note"><h4>Note</h4><p>If you allow customers to purchase a product that isn&#39;t available, then you need to refund the order.</p>
</aside>

<aside class="note"><h4>Note</h4><p>If you use a third-party app that automatically captures payments, then <a href="/en/manual/payments/payment-authorization#set-up-manual-payment-capture">set up manual payment capture</a> in your Shopify admin. Using an automatic payment capture setting in Shopify and a third-party app for automatically capturing payment can lead to potential conflicts and unexpected behavior.</p>
</aside>

#### Steps:

<div class="sections"><details open><summary id="desktop">Desktop</summary><ol>
<li><p>From your Shopify admin, go to <strong>Settings</strong> &gt; <a href="https://admin.shopify.com/settings/payments"><strong>Payments</strong></a>.</p>
</li>
<li><p>In the <strong>Payment capture method</strong> section, select <strong>Automatically at checkout</strong>.</p>
</li>
<li><p>Click <strong>Save</strong>.</p>
</li>
</ol>
</details><details><summary id="mobile">Mobile</summary><ol>
<li><p>From the <a href="https://www.shopify.com/install/detect">Shopify app</a>, tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg" alt="Menu" class="admin-icon" />, and then tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIcon.svg" alt="Settings" class="admin-icon" /> <strong>Settings</strong>.</p>
</li>
<li><p>In the <strong>Store settings</strong> section, tap <strong>Payments</strong>.</p>
</li>
<li><p>In the <strong>Payment capture method</strong> section, select <strong>Automatically at checkout</strong>.</p>
</li>
<li><p>Tap <strong>Save</strong> or <strong>&#10003;</strong>.</p>
</li>
</ol>
</details></div>

## Set up automatic payment capture at fulfillment {#automatic-at-fulfillment}

When automatic payment capture at fulfillment is activated, the payment for the order is **Authorized** at checkout. Payment is captured automatically when the entire order is fulfilled within the [authorization period](/manual/payments/payment-authorization#credit-card-authorization-period). Automatic capture at fulfillment only applies to orders placed after the feature is activated. Any orders that are already in progress won't have automatic capture at fulfillment.

If you need to capture payment before the authorization expires or at an earlier time, then you can [capture the payment manually](/manual/fulfillment/managing-orders/payments/capturing-payments#capture-payment-early).

<aside class="note"><h4>Note</h4><p>If you use a third-party app that automatically captures payments, then <a href="/en/manual/payments/payment-authorization#set-up-manual-payment-capture">set up manual payment capture</a> in your Shopify admin. Using an automatic payment capture setting in Shopify and a third-party app for automatically capturing payment can lead to potential conflicts and unexpected behavior.</p>
</aside>

### Limitations

Automatic capture at fulfillment has the following limitations:

* Payment can only be captured within the authorization period.
* The entire order must be fulfilled for automatic capture. Partially fulfilled orders won't be captured.
* Your payment provider must support authorization periods.
* Orders and draft orders with business-to-business (B2B) customers or from the [B2B checkout](/manual/b2b) must be manually captured when they don't have a valid authorization and 'due on fulfillment' payment terms.
* This feature isn't compatible with fulfillment apps that require a paid order status before starting the fulfillment process.

#### Steps:

<div class="sections"><details open><summary id="desktop">Desktop</summary><ol>
<li><p>From your Shopify admin, go to <strong>Settings</strong> &gt; <a href="https://admin.shopify.com/settings/payments"><strong>Payments</strong></a>.</p>
</li>
<li><p>In the <strong>Payment capture method</strong> section, select <strong>Automatically when the entire order is fulfilled</strong>.</p>
</li>
<li><p>Optional: To have a message about the expiration of payment authorization sent to your Shopify account email address, select <strong>Send a warning 1 day before an authorization expires</strong>.</p>
</li>
<li><p>Click <strong>Save</strong>.</p>
</li>
</ol>
</details><details><summary id="mobile">Mobile</summary><ol>
<li><p>From the <a href="https://www.shopify.com/install/detect">Shopify app</a>, tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg" alt="Menu" class="admin-icon" />, and then tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIcon.svg" alt="Settings" class="admin-icon" /> <strong>Settings</strong>.</p>
</li>
<li><p>In the <strong>Store settings</strong> section, tap <strong>Payments</strong>.</p>
</li>
<li><p>In the <strong>Payment capture method</strong> section, select <strong>Automatically when the entire order is fulfilled</strong>.</p>
</li>
<li><p>Optional: To have a message about the expiration of payment authorization sent to your Shopify account email address, select <strong>Send a warning 1 day before an authorization expires</strong>.</p>
</li>
<li><p>Tap <strong>Save</strong> or <strong>&#10003;</strong>.</p>
</li>
</ol>
</details></div>

## Set up automatic payment capture per fulfillment {#capture-per-fulfillment}

<aside class="note note-plan"><h4>Plan requirement</h4><p>Automatic capture per fulfillment is available only on the Shopify Plus plan.</p>
</aside>

When automatic payment capture per fulfillment is activated, payment for the order is **Authorized** at checkout.

Payment is captured automatically for line items and applicable taxes when they're fulfilled within the [authorization period](/manual/payments/payment-authorization#credit-card-authorization-period). Any remaining payment amount, such as shipping, fees, and duties, is automatically captured when the entire order is fulfilled within the authorization period. Automatic payment capture per fulfillment only applies to orders placed after the feature is activated.

If you need to capture payment before the authorization expires or at an earlier time, then you can [capture the payment manually](/manual/fulfillment/managing-orders/payments/capturing-payments#capture-payment-early).

<aside class="note"><h4>Note</h4><p>If you use a third-party app that automatically captures payments, then <a href="/en/manual/payments/payment-authorization#set-up-manual-payment-capture">set up manual payment capture</a> in your Shopify admin. Using an automatic payment capture setting in Shopify and a third-party app for automatically capturing payment can lead to potential conflicts and unexpected behavior.</p>
</aside>

### Limitations and requirements

Automatic capture per fulfillment has the following limitations:

* Payment can only be captured within the authorization period.
* Your payment provider must support authorization periods and multiple captures of an authorization.
* Payment is due when the entire order is fulfilled instead of per fulfillment in the following scenarios:
  * You've added **Due on fulfillment** payment terms to an order.
  * The order was placed by a B2B company with [location payment terms](/manual/b2b/checkout-and-orders/payment-terms) set to **Due on fulfillment**.
* Orders created from B2B checkout without **Due on fulfillment** payment terms must be manually captured.
* Automatic capture per fulfillment isn't compatible with fulfillment apps that require a paid order status before starting the fulfillment process.
* Not all payment methods support [capturing multiple partial payments](/manual/fulfillment/managing-orders/payments/capturing-payments#multiple-partial-payments). If capturing multiple partial payments isn't supported, then payment for the entire order will be captured at the first fulfillment.
* Discounts for capture per fulfillment are applied in the following ways:
  * Item level discounts are already included in the item's subtotal and are accounted for in each fulfillment.
  * Order level discounts are deducted from the order total, and evenly spread across each fulfillment.
  * Shipping discounts are captured during the final fulfillment.

The automation for capture per fulfillment is removed in the following use scenarios:

* fulfillment is canceled
* payment is manually captured
* an item is returned
* the order is partially or fully refunded

#### Steps:

<div class="sections"><details open><summary id="desktop">Desktop</summary><ol>
<li><p>From your Shopify admin, go to <strong>Settings</strong> &gt; <a href="https://admin.shopify.com/settings/payments"><strong>Payments</strong></a>.</p>
</li>
<li><p>In the <strong>Payment capture method</strong> section, select <strong>Automatically when fulfilling</strong>.</p>
</li>
<li><p>Select <strong>Capture payment per fulfillment</strong>.</p>
</li>
<li><p>Optional: To have a message about the expiration of payment authorization sent to your Shopify account email address, select <strong>Send a warning 1 day before an authorization expires</strong>.</p>
</li>
<li><p>Click <strong>Save</strong>.</p>
</li>
</ol>
</details><details><summary id="mobile">Mobile</summary><ol>
<li><p>From the <a href="https://www.shopify.com/install/detect">Shopify app</a>, tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg" alt="Menu" class="admin-icon" />, and then tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIcon.svg" alt="Settings" class="admin-icon" /> <strong>Settings</strong>.</p>
</li>
<li><p>In the <strong>Store settings</strong> section, tap <strong>Payments</strong>.</p>
</li>
<li><p>In the <strong>Payment capture method</strong> section, select <strong>Automatically when fulfilling</strong>.</p>
</li>
<li><p>Select <strong>Capture payment per fulfillment</strong>.</p>
</li>
<li><p>Optional: To have a message about the expiration of payment authorization sent to your Shopify account email address, select <strong>Send a warning 1 day before an authorization expires</strong>.</p>
</li>
<li><p>Tap <strong>Save</strong> or <strong>&#10003;</strong>.</p>
</li>
</ol>
</details></div>

## Set up manual payment capture {#set-up-manual-payment-capture}

When manual payment capture is activated, customers that pay for orders in your online store with credit cards and some additional payment methods aren't automatically charged at the time of sale. To get paid, you need to [capture payment manually](/manual/fulfillment/managing-orders/payments/capturing-payments#capture-payments-manually) within the authorization period.

You can manually capture the full amount for the order, or a [partial payment](/manual/fulfillment/managing-orders/payments/capturing-payments#partial-payment). You can capture [multiple partial payments](/manual/fulfillment/managing-orders/payments/capturing-payments#multiple-partial-payments) when you use a third-party payment provider that supports that functionality, or you're on Shopify Plus.

Activate manual payment capture if it suits your business better than automatic payment capture.

<aside class="note note-caution"><h4>Caution</h4><p>You need to capture payment for an order before the authorization period ends to receive any money from that order.</p>
</aside>

#### Steps:

<div class="sections"><details open><summary id="desktop">Desktop</summary><ol>
<li><p>From your Shopify admin, go to <strong>Settings</strong> &gt; <a href="https://admin.shopify.com/settings/payments"><strong>Payments</strong></a>.</p>
</li>
<li><p>In the <strong>Payment capture method</strong> section, select <strong>Manually</strong>.</p>
</li>
<li><p>Optional: If you use Shopify Payments and you want to receive emails before the authorization period for each order ends, then select <strong>Send a warning 1 day before an authorization expires</strong>. If you select this option but you don&#39;t use Shopify Payments, then you don&#39;t receive warning emails.</p>
</li>
<li><p>Click <strong>Save</strong>.</p>
</li>
</ol>
</details><details><summary id="mobile">Mobile</summary><ol>
<li><p>From the <a href="https://www.shopify.com/install/detect">Shopify app</a>, tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg" alt="Menu" class="admin-icon" />, and then tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIcon.svg" alt="Settings" class="admin-icon" /> <strong>Settings</strong>.</p>
</li>
<li><p>In the <strong>Store settings</strong> section, tap <strong>Payments</strong>.</p>
</li>
<li><p>In the <strong>Payment capture method</strong> section, select <strong>Manually</strong>.</p>
</li>
<li><p>Optional: If you use Shopify Payments and you want to receive emails before the authorization period for each order ends, then select <strong>Send a warning 1 day before an authorization expires</strong>. If you select this option but you don&#39;t use Shopify Payments, then you don&#39;t receive warning emails.</p>
</li>
<li><p>Tap <strong>Save</strong> or <strong>&#10003;</strong>.</p>
</li>
</ol>
</details></div>
