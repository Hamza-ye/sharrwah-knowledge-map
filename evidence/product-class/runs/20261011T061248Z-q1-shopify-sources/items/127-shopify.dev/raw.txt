---
title: About billing for your app
description: >-
  Learn how to monetize an app with Shopify App Pricing, the default for new
  public apps and the recommended path for existing apps with supported pricing
  models.
source_url:
  html: 'https://shopify.dev/docs/apps/launch/billing'
  md: 'https://shopify.dev/docs/apps/launch/billing.md'
---

# About billing for your app

Use Shopify App Pricing to monetize apps distributed through the Shopify App Store when it supports their pricing model. It's the default for new public apps and the recommended path for existing apps moving from Manual Pricing. Shopify App Pricing creates a predictable, trustworthy, and standardized experience for app users and makes pricing easier to set up and maintain.

***

## Which billing method should you use?

Use the following rules to choose how to charge merchants for your app:

* **New public apps**: Use [Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing). It's the default when you submit a new public app, and you configure subscription plans, usage-based pricing, and free trials in the Partner Dashboard instead of writing billing code.
* **Existing public apps with supported pricing models**: Shopify App Pricing is the recommended path. Learn about [migrating to Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing/migrating-to-shopify-app-pricing).
* **Existing Billing API integrations you're not migrating**: [Manual Pricing](https://shopify.dev/docs/apps/launch/billing/manual-pricing) remains supported. You don't need to migrate to keep an existing `billing.request` or `appSubscriptionCreate` integration running.
* **One-time purchases and unsupported pricing models**: Use [Manual Pricing](https://shopify.dev/docs/apps/launch/billing/manual-pricing) with the Billing API. Shopify App Pricing doesn't support [one-time app purchases](https://shopify.dev/docs/apps/launch/billing/manual-pricing/support-one-time-purchases).
* **Subscriptions for merchant products**: Selling your merchant's products on a recurring basis isn't app billing. Use [purchase options](https://shopify.dev/docs/apps/build/purchase-options) with selling plans and subscription contracts instead.

***

## How Shopify App Pricing helps

Shopify App Pricing provides the following benefits:

* **Simplified payment process**: Charges are directly added to the merchant's Shopify invoice.

* **Increased conversion rates**: Apps that use Shopify App Pricing experience higher rates of customers transitioning from free to paid versions, because of higher trust and charges originating directly from Shopify.

* **Revenue sharing**: Shopify collects the charge and automatically pays out your share, as defined in [Shopify Partner earnings](https://help.shopify.com/en/partners/partner-program/how-to-earn#apps).

* **Chargeback handling**: Shopify handles all chargeback-related processes.

* **Flexible pricing models**: Shopify supports a wide range of common pricing models that merchants have come to expect.

***

## Shopify App Pricing

Shopify App Pricing is the default for new public apps and the recommended approach for existing apps with supported pricing models. Define plans in the app submission form and let Shopify host your plan selection page and automate billing, trials, proration, upgrades, and downgrades. Shopify App Pricing supports recurring and usage charges, enabling you to send billable usage events via the [App Events API](https://shopify.dev/docs/api/app-events). Learn more about [Shopify App Pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing).

**Important:**

All apps published on the Shopify App Store are required to use a Shopify provided billing solution and adhere to the terms and conditions of the [Shopify Partner Program Agreement](https://www.shopify.com/partners/terms).

![Shopify App Pricing flow: Merchant initiates upgrade, App redirects to Shopify admin, Shopify processes charge and redirects to welcome link, App verifies subscription and optionally sends usage charges.](https://shopify.dev/assets/assets/images/apps/billing/managed-pricing-summary-BYoj8xhA.png)

Shopify App Pricing is available for free, monthly and annual recurring, and various usage-based plan types.

***

## Manual Pricing (Legacy)

Manual pricing is still supported but is the legacy method for handling app billing. With manual pricing, you build your own billing logic and pricing page using the Billing API to create recurring, usage, or one-time charges.

This option remains available for apps that have specific requirements not covered by Shopify App Pricing yet, and for existing app developers who are using it. Learn more about [manual pricing](https://shopify.dev/docs/apps/launch/billing/manual-pricing).

***

## Supported currencies

You can match your app charges to a merchant's local billing currency if they use one of the [supported currencies](https://help.shopify.com/manual/your-account/manage-billing/your-invoice/local-currency).

Retrieve the merchant's local billing currency with the GraphQL Admin API's [`shopBillingPreferences`](https://shopify.dev/docs/api/admin-graphql/latest/queries/shopBillingPreferences) query, passing the currency value as input.

***

## Best practices

Consider the following best practices when developing your app's pricing model:

| Practice | Benefit | Example |
| - | - | - |
| **Provide simple and intuitive pricing** | Makes it easier for merchants to understand the pricing model and encourages adoption. Merchants are more confident where costs are clear. | If your app provides a single set of features for all merchants, then consider setting up time-based subscriptions at 30 or 365-day intervals. |
| **Limit the number of plans** | Makes it easier for merchants to compare plans and identify which plan works best for them. Merchants want to quickly find the right plan and less options helps with that. | If your app provides tiered features, then consider setting up a basic plan and a pro planUse usage based pricing where appropriate to differentiate plans. |
| **Offer free trials** | Encourages merchants and Partners that develop stores for merchants to try your app before they pay for it. This helps users learn your app's value and recommend the app to others. | Align with Shopify's free trial or $1 plan to encourage merchants to fully try your apps. |
| **Create charges in the merchant's local billing currency** | Enables merchants to better budget their app spend, which prevents confusion and provides a better app experience. | If a merchant is in India, then bill them in Indian Rupees (INR). If they're in Canada, then bill them in Canadian Dollars (CAD). |

***
