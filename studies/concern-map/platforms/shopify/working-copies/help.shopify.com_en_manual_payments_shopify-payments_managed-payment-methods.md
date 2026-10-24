# Managed payment methods

With managed payment methods on Shopify Payments, you can choose to automatically activate [local payment methods](/manual/payments/shopify-payments/local-payment-methods) and personalize the checkout experience for your customers. Instead of manually activating payment methods in your settings, eligible payment methods are activated based on the regions where you sell. Your customers are offered the most relevant payment options for their location, which can help increase conversion.

When you activate managed payment methods, the following changes are applied to your store:

* **Local payment methods are activated automatically**: Shopify Payments [local payment methods](/manual/payments/shopify-payments/local-payment-methods) that are popular with customers in the regions where you sell are automatically activated. For example, if you have customers in Belgium, then Bancontact is activated on your checkout. If you have customers in Poland, then BLIK is activated.
* **Checkout is personalized for each customer**: The payment methods most likely to result in a completed purchase are displayed most prominently at checkout. This is based on the customer's location, the payment methods available in their region, and aggregated data about payment preferences.
* **Your previous choices are respected**: If you've previously deactivated a local payment method, then managed payment methods doesn't reactivate it. Your manual payment method settings are preserved.

## Requirements for using managed payment methods {#requirements}

To use managed payment methods, your store must meet the following requirements:

* [Shopify Payments](/manual/payments/shopify-payments) is active on your store.
* [Shopify Network Intelligence](/manual/privacy-and-security/privacy/customer-privacy-settings) (SNI) is activated in your [**Customer privacy** settings](https://admin.shopify.com/settings/privacy).

Managed payment methods uses SNI to understand customer payment preferences and personalize checkout. If SNI isn't activated on your store, then you're prompted to activate it when you activate managed payment methods. If you deactivate SNI after activating managed payment methods, then the managed payment methods feature is also deactivated. Any payment methods that were previously activated remain active, and you must manage them manually.

## Checkout personalization {#checkout-personalization}

With managed payment methods activated, your checkout is personalized so that each customer can view the payment methods most likely to result in a completed purchase. Your checkout is personalized for your customers in the following ways:

* **Payment method ordering**: Payment methods are arranged based on what's most relevant for each customer. Relevance is determined using factors such as buyer location, purchase history, and local trends, and this logic is updated regularly. As a result, Bancontact might be displayed prominently for a customer in Belgium, but if a customer in the UK prefers Klarna, then Klarna might be displayed first.
* **Visibility optimization**: The most relevant payment methods are displayed first in the checkout list.
* **Continuous improvement**: Aggregated, anonymized data is used to determine which payment methods convert best for different customer profiles and regions, so your checkout improves over time.
* **Existing customizations are respected**: Any checkout customizations that you currently have in place are preserved and not overwritten. For example, if you've customized your checkout to always display a specific payment method first, then managed payment methods doesn't override this setting.

This personalization applies to all payment methods on your checkout, including credit cards, digital wallets, buy now, pay later options, and local payment methods. For checkout ordering, it applies to payment methods from both Shopify Payments and any third-party local payment methods that you've already enabled. Managed payment methods doesn't enable or disable third-party payment methods, and doesn't change your third-party payment provider integrations.

Checkout personalization applies to both guest checkout and checkout in the Shop app. Managed payment methods adjusts only the order in which payment methods are displayed at checkout. You're still in control of your checkout theme, branding, and layout through the [checkout editor](/manual/checkout-settings/customize-checkout-configurations).

## Automatically activated payment methods {#automatically-activated-payment-methods}

When you activate managed payment methods, local payment methods are automatically activated based on the regions where you sell. As new payment methods become supported, they might be automatically activated for your store if they're relevant to your customers. You're notified when new payment methods are added, including details about applicable fees. Payment methods are activated when they're expected to improve conversion in your customers' regions.

Managed payment methods only turns eligible Shopify Payments local payment methods on or off. You can find these methods in **Settings** > **Payments** > **Payment methods**. Some local payment methods are available in early access. During early access, the payment method might not be available on your store or to all eligible customers yet.

## View your activate payment methods 

You can view your active payment methods in your Shopify admin.

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments).


2. In the **Shopify Payments** section, click **Manage**.
3. Click **More actions**, and then click **Manage payment methods**.
4. In the **Payment methods** section, review your active payment methods.

### Payment methods not included {#payment-methods-not-included}

The following payment methods aren't automatically activated or managed when using managed payment methods:

* Card types (such as Visa, Mastercard, and American Express)
* Cash and cash on delivery (COD)
* Manual payment methods
* Gift cards
* Custom payment apps, including whether they're activated or deactivated
* Third-party payment provider integrations

## Early access local payment methods {#early-access-local-payment-methods}

Some newer local payment methods are available in early access before they're offered more widely. During early access, a payment method might not be available on your store or to all eligible customers yet. You can confirm whether a local payment method is in early access from your [**Payments** settings](https://admin.shopify.com/settings/payments) in the Shopify admin.

Early access works in one of the following ways, depending on the payment method:

* You activate it yourself: The payment method is available to only some eligible stores. When it's available to your store, you activate it from your [**Payments** settings](https://admin.shopify.com/settings/payments) in the same way as any other local payment method.
* Managed payment methods activates it for you: The payment method is active on your store, but it might be displayed at checkout for only some of your customers. You're notified by email when a payment method is activated on your store, including the rate that applies to it.

### Considerations for early access payment methods activated by managed payment methods 

When managed payment methods activates a payment method in early access, review the following considerations:

* The payment method is displayed as active in your [**Payments** settings](https://admin.shopify.com/settings/payments), with a banner that indicates that it's in early access.
* The payment method might be displayed at checkout for only some of your customers. This is expected, and the payment method might not be displayed when you test your own checkout.
* When a local payment method is first activated for your store, it might take a few days to be displayed on all eligible checkouts during gradual rollout.
* The rate that you pay is the rate that's displayed in your payment settings and in the email that you received when the payment method was activated.
* When early access ends, the payment method becomes available to all of your eligible customers.
* You can deactivate any local payment method at any time from your [**Payments** settings](https://admin.shopify.com/settings/payments) in the Shopify admin. If you deactivate a payment method, then managed payment methods doesn't reactivate it.

<aside class="note"><h4>Note</h4><p>If you have a third-party version of a payment method installed, such as Klarna, then the Shopify Payments version isn&#39;t activated automatically. You can manually switch to the Shopify Payments version in the <a href="https://admin.shopify.com/settings/payments"><strong>Payments</strong></a> section of your Shopify admin.</p>
</aside>

## Activating or deactivating managed payment methods {#activate-deactivate-managed-payment-methods}

Managed payment methods works alongside your existing payment method settings. You can continue to manually add or remove payment methods alongside what managed payment methods activates automatically. If you manually deactivate a payment method, then it isn't automatically reactivated.

### Activate managed payment methods

You can activate managed payment methods from your Shopify admin.

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments).


2. In the **Shopify Payments** section, click **Manage**.
3. In the **Managed payment methods** card, activate **Managed payment methods**.
4. If SNI isn't activated, then you're prompted to activate it. Review the information about SNI and then click **Confirm**.

### Deactivate individual payment methods

You can deactivate any individual payment method that was activated by managed payment methods, without deactivating the feature entirely. If you deactivate a payment method, then managed payment methods doesn't reactivate it.

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments).


2. In the **Shopify Payments** section, click **Manage**.
3. Click **More actions**, and then click **Manage payment methods**.
4. Click <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg" alt="Horizontal menu" class="admin-icon" /> for the payment method that you want to deactivate.
5. Click **Disable**.

### Deactivate managed payment methods

Review the following considerations before deactivating managed payment methods:

* Payment methods that were automatically activated remain active. If you no longer want to offer these payment methods, then you can deactivate them individually from the [**Payments**](https://admin.shopify.com/settings/payments) section of your Shopify admin.
* Checkout personalization stops.
* You can activate managed payment methods again at any time.

If you prefer to manage your payment methods manually, then you can deactivate the managed payment methods feature.

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments).


2. In the **Shopify Payments** section, click **Manage**.
3. In the **Managed payment methods** card, deactivate managed payment methods.

## Fees for managed payment methods

Payment methods activated by managed payment methods are processed through Shopify Payments. The same Shopify Payments transaction fees apply as when you manually activate a payment method. There's no additional fee for using managed payment methods.

Transaction fees for local payment methods vary by method and by your Shopify plan. You can view the transaction fees that you pay for local payment method transactions in your Shopify admin.

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments).


2. In the **Payment methods** section, click **View payment rates**.

## Managed payment methods with Managed Markets

If your store uses [Managed Markets](/manual/international/managed-markets), managed payment methods and Managed Markets work alongside each other. When managed payment methods is enabled, eligible Shopify Payments [local payment methods](/manual/payments/shopify-payments/local-payment-methods) are automatically activated for your store.

The following applies when you use both features together:

* **Domestic transactions**: Orders placed by customers in the same country as your store are processed through Shopify Payments. Any local payment methods activated by managed payment methods apply to these transactions.
* **Cross-border transactions**: Orders placed by customers in other countries continue to be processed through [Managed Markets with Shopify Payments](/manual/international/managed-markets/shopify-payments), powered by Global-E. Your Managed Markets setup, fees, and transaction handling are unaffected.
* **Fees**: The rates and fees for payment methods activated by managed payment methods apply to your Shopify Payments transactions only. Your Managed Markets fees and transactions continue to be handled separately by Global-E.
