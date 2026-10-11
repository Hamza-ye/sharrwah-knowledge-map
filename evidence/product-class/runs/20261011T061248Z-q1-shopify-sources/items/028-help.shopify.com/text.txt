# Reviewing orders with fraud analysis

You can use fraud analysis to identify orders that can be fraudulent and review them in your Shopify admin before you fulfill them. Review high-risk orders to avoid potential [chargebacks](/manual/payments/chargebacks). Fulfilling high-risk orders can result in a higher number of chargebacks, which can result in disabling payment processing and removal from Shopify Payments.

Credit card companies can reverse funds for stolen cards after orders are fulfilled. You can gather evidence for any disputed charges. However, the decision to reverse funds is made by the bank that issued the credit card, not by Shopify. Shopify does not cover charge reversals from banks.

## Considerations for using fraud analysis

Before you use fraud analysis, review the following considerations:

* [Fraud indicators](#fraud-analysis-indicators) and support for third-party fraud prevention apps are available on the [Basic plan](localized-pricing-page) or higher.
* [Fraud recommendations](#fraud-recommendations) are available on the [Grow plan or higher](/manual/intro-to-shopify/pricing-plans/plans-features), or if you use [Shopify Payments](/manual/payments/shopify-payments).
* Fraud analysis works with online credit card orders that Shopify can verify.
* Shopify Payments can block some [high-risk checkout attempts](#blocked-high-risk-checkout-attempts) before an order is created.
* Some orders don't receive a fraud recommendation, including test orders, free orders, orders paid in full with a gift card, Point of Sale orders, B2B orders, and subscription renewal orders. You can still [simulate a fraud recommendation](#testing-fraud-analysis) on a test order. For in-person sales, review [fraud prevention practices for Shopify POS](/manual/payments/chargebacks/preventing-chargebacks#pos-fraud-prevention).
* If you use a third-party payment processor, then check with them about any fraud analysis limitations.

## Understanding fraud analysis

Fraud analysis includes fraud indicators and, for eligible orders, a fraud recommendation. Use the fraud indicators to investigate the order yourself. Use the fraud recommendation to check the order's overall risk and recommended next step.

<div class="video-embed-wrapper">
    <figure>
      <iframe src="https://www.youtube.com/embed/U7kMNfa2eA4?cc_lang_pref=en&cc_load_policy=1&hl=en" width="800" height="450" allowfullscreen></iframe>
    </figure>
  </div>
  <aside class="note tip">
      <h4>Tip</h4>
      <p>
      To see more videos, visit our <a href="https://www.youtube.com/channel/UCSG_dVp-hi_hWP-Z7DlpRgQ">YouTube channel</a>.
      </p>
    </aside>

### Fraud indicators for an order {#fraud-analysis-indicators}

Fraud indicators are individual details about an order. They can describe address and payment checks or patterns associated with customer, location, device, and network activity. The available indicators can differ between orders.

You can use these details to [investigate an order](/manual/payments/fraud-prevention) that you think might be fraudulent. Fraud indicators can include:

* Whether the credit card used for the order passes Address Verification System (AVS) checks
* Whether the customer provided the correct Card Verification Value (CVV) code
* Whether the customer's location matches the payment method
* Whether there is unusual device or network activity
* Whether the customer tried to use more than one credit card

In the revised **Order risk evaluation** view for a Shopify assessment, the available fraud indicators are listed together in a shaded panel. Indicator icons distinguish details associated with fraudulent behavior, details associated with legitimate behavior, and neutral details. Orders without newer indicators can still display existing address and payment checks.

An available IP address is listed separately from the indicators in this view. Some views also list an available location description as separate metadata, including when the IP address isn't available. Location-related risk indicators, such as a mismatch between customer location and payment method, remain in the list. An IP address or location description by itself isn't a fraud recommendation.

Other versions of the details view, including mobile versions, can group indicators under **High risk signals**, **Low risk signals**, and **Other details**, or use red, green, and gray icons. Grouped views omit empty groups and can omit headings when all indicators belong to one group. The presentation can also differ for third-party assessments.

Individual indicators and group headings don't represent the order's overall risk level. Review the [fraud recommendation](#fraud-recommendations) instead of deciding whether to fulfill an order from one indicator or the number of indicators.

For orders with [Shopify Protect](/manual/payments/shop-pay/shopify-protect) information, review the protection status separately from the fraud indicators.

<aside class="note"><h4>Note</h4><p>If you want time to investigate orders before you accept payment for them, then you can <a href="/en/manual/payments/payment-authorization#set-up-manual-payment-capture">set up manual payment captures</a>.</p>
</aside>

### Fraud analysis recommendations {#fraud-recommendations}

For eligible online credit card orders, the fraud recommendation indicates whether an order has a low, medium, or high risk of a [chargeback](/manual/payments/chargebacks) due to fraud. If an order has a medium or high risk, then it's flagged on the **Orders** page with a warning symbol next to the order number. Flagged orders are also highlighted in [order notification emails](/manual/fulfillment/setup/notifications/staff-notifications) when you subscribe to them.

Fraud recommendations are powered by machine learning algorithms that are trained on historical transactions across all Shopify stores. These algorithms are continuously improved to better identify fraudulent orders.

Review both the risk level and the recommended next step for the order. The **Order risk evaluation** view can include the guidance **You can fulfill this order**, **Confirm with the customer before fulfilling**, or **Consider canceling this order**. The guidance follows the order's recommendation, not an individual indicator.

If an order is at a high risk of fraud, then you can attempt to [verify the order](/manual/payments/fraud-prevention), [cancel the order](/manual/fulfillment/managing-orders/canceling-orders), or [refund the order](/manual/fulfillment/managing-orders/refunding-orders).

### Blocked high-risk checkout attempts {#blocked-high-risk-checkout-attempts}

Shopify Payments can block some high-risk checkout attempts before an order is created. These checkout attempts don't become orders, so they don't have an order fraud recommendation.

You can review blocked checkout attempts in the **Blocked** view of **Orders** > **Abandoned checkouts**. If you know the customer and want to complete the sale, then you can create a [draft order](/manual/fulfillment/managing-orders/create-orders/create-draft) and send the customer an invoice.

## View an order's fraud analysis {#view-the-fraud-analysis-for-an-order}

You can review an order's risk level, recommendation, and available indicators in the **Order risk** section on the order details page. Suspicious orders are flagged with an exclamation mark icon.

The full analysis can be labeled **Order risk evaluation** or **About this order**, depending on the available view. When an order has assessments from multiple providers, select the provider whose assessment you want to review.

In the revised Shopify assessment on desktop, a **Contact customer** action can be available when the recommendation is to investigate the order. The action requires an email address on the order. It opens an email dialog without sending a message automatically.

#### Steps:

<div class="sections"><details open><summary id="desktop">Desktop</summary><ol>
<li><p>From your Shopify admin, go to <a href="https://admin.shopify.com/orders"><strong>Orders</strong></a>.</p>
</li>
<li><p>Click the order that you want to review for fraud.</p>
</li>
<li><p>In the <strong>Order risk</strong> section, click the icon labeled <strong>Order risk evaluation</strong> or <strong>About this order</strong>.</p>
</li>
<li><p>Review the risk level, recommended next step, and available fraud indicators. Select another provider&#39;s tab to review additional assessments, when available.</p>
</li>
<li><p>Optional: If <strong>Contact customer</strong> is available, then click it to open the email dialog. Review the recipient and message before sending.</p>
</li>
</ol>
</details><details><summary id="mobile">Mobile</summary><ol>
<li>From the <a href="https://www.shopify.com/install/detect">Shopify app</a>, tap the <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/OrderIcon.svg" alt="Orders" class="admin-icon" /> icon
.</li>
<li>Tap the order that you want to review for fraud.</li>
<li>In the <strong>Order risk</strong> section, open the order&#39;s risk summary.</li>
<li>Tap <strong>About this order</strong> or <strong>Order risk evaluation</strong> to open the full analysis, depending on your app version.</li>
<li>Review the risk level and available fraud indicators. Select another provider to review additional assessments, when available.</li>
</ol>
</details></div>

## Third-party fraud apps

You can download apps that help with fraud prevention from the [Shopify App Store](https://apps.shopify.com/categories/store-management-privacy-and-security). You can view the fraud indicators and recommendations from these apps together with fraud analysis for each order.

## Automating your fraud prevention strategies using Shopify Flow

Reviewing orders for potential fraud can be time-consuming. You can use fraud analysis to decide whether to fulfill an order. You can [create fraud prevention workflows using Shopify Flow](/manual/fulfillment/managing-orders/protecting-orders/shopify-flow) to automatically check your orders for potential fraud.

If the orders triggering your fraud analysis suggest card testing or repeat fraud, then review the guidance on [responding to card testing and reducing chargeback risk](/manual/payments/fraud-prevention/preventing-fraud#card-testing-repeat-fraud).

## Testing fraud analysis

You can test fraud analysis on your store and simulate an order with high, medium, or low risk. Test orders don't receive a real fraud recommendation, but you can use the following values to simulate one. To simulate a risk level, the order must have a total value greater than zero. You must also have the [Shopify Payments gateway in test mode](/manual/payments/shopify-payments/testing-shopify-payments#activate-test-mode-for-shopify-payments) to create test orders that simulate risk level. If you use another payment gateway for your test, then your store must be on the Grow plan or higher.

Use the following email addresses to simulate an order:

* shopify.test.high@shopify.com to create high-risk recommendations
* shopify.test.medium@shopify.com to create medium-risk recommendations
* shopify.test.low@shopify.com to create low-risk recommendations

You can also use the following test values in the **Apartment, suite, etc.** field of the shipping address:

* shopify.test.high to create high-risk recommendations
* shopify.test.medium to create medium-risk recommendations
* shopify.test.low to create low-risk recommendations

## Troubleshooting fraud analysis

<div class="accordion-troubleshooting">
  <details>
    <summary id="fraud-analysis-pending">Fraud analysis is pending</summary>

Fraud analysis typically happens immediately, but in rare cases it can take a few minutes. If an order has a `fraud analysis isn't available yet` message, then refresh the page or check back in a few minutes. Wait for the fraud analysis to finish before you fulfill the order.

  </details>
  <details>
    <summary>A customer's IP address is on a temporary blocklist</summary>

If the abandoned checkout indicates that the customer's IP address is on a temporary blocklist, then fraud analysis has temporarily blocked that IP address. This can happen when many orders or failed payment attempts come from the same IP address in a short time.

The block is temporary and is removed automatically within 6 to 24 hours. There's no way to remove it sooner, so the person placing the order needs to wait. If they try to place another order before the block is removed, then the timer resets.

To place orders before the block is removed:

* Create a [draft order](/manual/fulfillment/managing-orders/create-orders) instead of using your storefront checkout.
* For in-person sales, use [Shopify Point of Sale](/manual/sell-in-person/getting-started).

  </details>
  <details>
    <summary>A high-risk checkout attempt is blocked</summary>

If the abandoned checkout's **Timeline** includes **Blocked due to high risk of fraud**, then Shopify Payments blocked the payment before an order was created. No payment is captured.

Shopify Payments evaluates risk each time the customer submits checkout. If the customer tries again with different payment or billing details, then the payment might not be blocked.

If you know the customer and want to complete the sale, then create a [draft order](/manual/fulfillment/managing-orders/create-orders/create-draft) and send the customer an invoice.


  </details>
  <details>
    <summary>A third-party gateway is reviewing an order</summary>

If your third-party payment gateway is reviewing an order for fraud, then the review status might not update in your Shopify admin, because some gateways don't send review updates back to Shopify.

To check the status of the order, contact your payment gateway directly, or review the order in your gateway's dashboard.

  </details>
</div>
