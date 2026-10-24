# Using Shopify Payments with a third-party provider

You can use Shopify Payments alongside a direct third-party payment provider in the same store. In this setup, your third-party provider is the primary processor for credit and debit card transactions, and Shopify Payments handles additional payment methods your third-party provider doesn't support, such as [Shop Pay](/manual/payments/shop-pay/shop-pay) and [local payment methods](/manual/payments/shopify-payments/local-payment-methods/index). You can also use Shopify Payments to recover failed card transactions from your third-party provider, helping to reduce lost sales.

<aside class="note"><h4>Note</h4><p>Before you use Shopify Payments, review the following requirements:</p>
<ul>
<li>Shopify Payments is only available to online stores in <a href="/en/manual/payments/shopify-payments/supported-countries">certain countries and regions</a>. If you operate a retail store, then check the <a href="/en/manual/sell-in-person/getting-started/setup-payment-method/shopify-payments-pos#supported">list of countries that support Shopify Payments for in-person selling</a>.</li>
<li>To use Shopify Payments, you must secure your account with <a href="/en/manual/your-account/logging-in/secure-sign-in">two-step authentication</a>. Learn more about <a href="/en/manual/privacy-and-security/account-security">account security</a>. If you deactivate two-step authentication in the future, then you expose your account and financial information to potential criminal attacks.</li>
</ul>
</aside>


## Requirements

Before you set up Shopify Payments alongside a third-party provider, review the following requirements:

* Your store must be in a [country where Shopify Payments is supported](/manual/payments/shopify-payments/supported-countries).
* You must have an active direct third-party payment provider configured in your store.
* Merchants on the Shopify Plus plan who already use Shop Pay Express can continue using Shop Pay Express until their Plus contract becomes eligible for Shopify Payments alongside a third-party provider. Merchants on the Shopify Plus plan with signed contracts, including new merchants and merchants renewing their contracts, aren't eligible to use Shopify Payments alongside a third-party provider at this time.
* This feature isn't available in multi-entity setups. Only Shopify Payments can be used as a direct provider in multi-entity setups.

## Considerations

Before setting up Shopify Payments alongside a third-party provider, review the following considerations:

* You can use only one direct third-party payment provider alongside Shopify Payments at a time.
* Payment recovery applies only to credit and debit card transactions. Wallet and local payment method transactions aren't retried through Shopify Payments.
* If your store uses subscription products, then recurring charges are processed through your third-party provider by default. Payment recovery doesn't apply to recurring subscription charges. If a subscription charge fails, then it isn't retried through Shopify Payments.
* Multi-entity stores can use only Shopify Payments as a direct provider. Learn more about [selling with multiple entities](/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities).
* [Shopify Capital](/manual/finance/shopify-capital/index) eligibility is based on total sales from both providers.
* [Shopify Protect](/manual/payments/shop-pay/shopify-protect/index) covers only transactions processed through Shopify Payments.
* [Shopify Balance](/manual/finance/shopify-balance/index) remains available regardless of which provider processes the majority of transactions.

## Payment method routing

When you use Shopify Payments alongside a third-party provider, each payment method is routed to a specific provider.

<div>
<table>
  <caption>How payment methods are routed when using Shopify Payments alongside a third-party provider.</caption>
  <thead>
  <tr>
    <th scope="col">Payment method</th>
    <th scope="col">Primary provider</th>
    <th scope="col">Backup provider</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td scope="row">Credit and debit cards</td>
    <td>Third-party provider</td>
    <td>Shopify Payments</td>
  </tr>
  <tr>
    <td scope="row">Wallets offered by the third-party provider</td>
    <td>Third-party provider</td>
    <td>None</td>
  </tr>
  <tr>
    <td scope="row">Wallets not offered by the third-party provider</td>
    <td>Shopify Payments</td>
    <td>None</td>
  </tr>
  <tr>
    <td scope="row">Shop Pay</td>
    <td>Shopify Payments</td>
    <td>None</td>
  </tr>
  <tr>
    <td scope="row">Local payment methods</td>
    <td>Shopify Payments</td>
    <td>None</td>
  </tr>
  </tbody>
</table>
</div>

Your third-party provider remains the primary provider for credit and debit card transactions. You can offer any payment methods that your third-party provider doesn't support through Shopify Payments, giving your customers more ways to pay at checkout.

## Pricing and fees

When you use Shopify Payments alongside a third-party provider, the following fees apply:

* **Third-party transaction fees**: You're charged third-party transaction fees for transactions processed by your third-party provider, based on your Shopify plan.
* **Shopify Payments fees**: Transactions processed through Shopify Payments, such as Shop Pay and local payment methods, are charged at standard Shopify Payments rates plus a 1.25% premium. Shopify Payments rates vary by plan type and market.
* **Payment recovery fees**: When a failed transaction from your third-party provider is recovered through Shopify Payments, the standard Shopify Payments rate plus the 1.25% premium applies.

Review the full list of pricing for each plan on the [Shopify pricing page](localized-pricing-page).

## Verify and activate Shopify Payments alongside a third-party provider {#set-up-shopify-payments-alongside-a-third-party-provider}

If you already have a third-party payment provider active, then you can add Shopify Payments alongside it without any interruption to your store's checkout.

### Submit your Shopify Payments details for verification

Before you can activate Shopify Payments alongside a third-party provider, you need to submit your Shopify Payments details for verification.

#### Steps:

<div class="sections"><details open><summary id="desktop">Desktop</summary><ol>
<li><p>From your Shopify admin, go to <strong>Settings</strong> &gt; <a href="https://admin.shopify.com/settings/payments"><strong>Payments</strong></a>.</p>
</li>
<li><p>In the <strong>Shopify Payments</strong> card, click <strong>Activate Shopify Payments</strong>.</p>
</li>
<li><p>Complete the required personal, business, address, identification, and statement descriptor information.</p>
</li>
<li><p>Click <strong>Submit for verification</strong>.</p>
</li>
</ol>
</details><details><summary id="mobile">Mobile</summary><ol>
<li><p>From the <a href="https://www.shopify.com/install/detect">Shopify app</a>, tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg" alt="Menu" class="admin-icon" />, and then tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIcon.svg" alt="Settings" class="admin-icon" /> <strong>Settings</strong>.</p>
</li>
<li><p>In the <strong>Store settings</strong> section, tap <strong>Payments</strong>.</p>
</li>
<li><p>In the <strong>Shopify Payments</strong> card, tap <strong>Activate Shopify Payments</strong>.</p>
</li>
<li><p>Complete the required personal, business, address, identification, and statement descriptor information.</p>
</li>
<li><p>Tap <strong>Submit for verification</strong>.</p>
</li>
</ol>
</details></div>

### Activate Shopify Payments as an additional provider

After your details are verified, you can activate Shopify Payments alongside your third-party provider.

#### Steps:

<div class="sections"><details open><summary id="desktop">Desktop</summary><ol>
<li><p>From your Shopify admin, go to <strong>Settings</strong> &gt; <a href="https://admin.shopify.com/settings/payments"><strong>Payments</strong></a>.</p>
</li>
<li><p>In the <strong>Shopify Payments</strong> section, click <strong>Activate Shopify Payments</strong>.</p>
</li>
<li><p>In the <strong>Activate Shopify Payments</strong> dialog, deselect <strong>Use as primary provider and deactivate [third-party provider]</strong>.</p>
</li>
<li><p>Review the transaction fee, card rates, and processing details.</p>
</li>
<li><p>Click <strong>Activate</strong>.</p>
</li>
</ol>
</details><details><summary id="mobile">Mobile</summary><ol>
<li><p>From the <a href="https://www.shopify.com/install/detect">Shopify app</a>, tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuIcon.svg" alt="Menu" class="admin-icon" />, and then tap <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/SettingsIcon.svg" alt="Settings" class="admin-icon" /> <strong>Settings</strong>.</p>
</li>
<li><p>In the <strong>Store settings</strong> section, tap <strong>Payments</strong>.</p>
</li>
<li><p>In the <strong>Shopify Payments</strong> card, tap <strong>Activate Shopify Payments</strong>.</p>
</li>
<li><p>In the <strong>Activate Shopify Payments</strong> dialog, deselect <strong>Use as primary provider and deactivate [third-party provider]</strong>.</p>
</li>
<li><p>Review the transaction fee, card rates, and processing details.</p>
</li>
<li><p>Tap <strong>Activate</strong>.</p>
</li>
</ol>
</details></div>

## Manage Shopify Payments with a third-party provider

After Shopify Payments is activated alongside a third-party provider, your third-party provider remains the primary provider for credit and debit card transactions. Shopify Payments automatically acts as a backup for eligible failed card transactions. If you want Shopify Payments to process all credit and debit card transactions, then you can switch to Shopify Payments as your sole provider.

### Payment recovery

Payment recovery is automatically activated when you use Shopify Payments alongside a direct third-party payment provider. It isn't configurable and can't be deactivated. If a customer's card payment is declined or encounters an error through the third-party provider, then the transaction is retried through Shopify Payments to help complete the sale.

Payment recovery applies only to credit and debit card payments. Local payment methods and wallet transactions aren't retried through a backup provider.

### Switch to Shopify Payments as your sole provider

To use Shopify Payments as your sole payment provider, you can deactivate the third-party provider at any time. After you switch to Shopify Payments as the sole provider, all credit and debit card transactions are processed through Shopify Payments, and third-party transaction fees no longer apply.

Learn more about [switching to Shopify Payments](/manual/payments/shopify-payments/onboarding/account-setup#set-up-shopify-payments).

## Shop Pay Express migration

Shop Pay Express is being replaced by the ability to use Shopify Payments alongside your third-party provider. What happens depends on your Shopify plan:

* **The Basic, Shopify, and Advanced plans**: Your store is automatically migrated to the new model. Your rates decrease and you gain access to additional Shopify Payments features, including wallet and local payment methods not offered by your third-party provider. Payment recovery is automatically activated for eligible card transactions. Wallet and local payment methods aren't automatically activated after migration. No action is required to maintain access to Shop Pay.
* **The Shopify Plus plan, terms of service**: You need to opt in through your Shopify admin and accept updated terms before migration is complete.
* **The Shopify Plus plan, contract**: You retain access to Shop Pay Express until your Plus contract becomes eligible for this feature.
