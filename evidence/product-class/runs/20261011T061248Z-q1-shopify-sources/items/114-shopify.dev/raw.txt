---
title: Apps in checkout
description: >-
  Learn how you can use extensions to customize many parts of the Shopify
  checkout experience.
source_url:
  html: 'https://shopify.dev/docs/apps/build/checkout'
  md: 'https://shopify.dev/docs/apps/build/checkout.md'
api_name: checkout-ui-extensions
---

# Apps in checkout

Merchants use [Shopify checkout](https://help.shopify.com/manual/checkout-settings) to accept orders and receive payments wherever they sell online. To augment Shopify checkout with new functionality, build an app with extensions.

***

## How it works

After a customer adds products to a cart, they use Shopify checkout to enter their customer, shipping, and payment information before placing the order.

To extend checkout, apps can use extensions. For example, apps can use extensions to offer a customer free shipping or other discounts, depending on the contents of their cart.

To install apps on their store, merchants can use the Shopify admin. There, they can can use the [checkout editor](https://shopify.dev/docs/apps/build/checkout/test-checkout-ui-extensions#test-the-extension-in-the-checkout-editor) to place a block for a [checkout UI extension](https://shopify.dev/docs/api/checkout-ui-extensions) in the checkout experience.

![Actions that a developer, customer, and merchant take in connection to Shopify checkout](https://shopify.dev/assets/assets/images/apps/checkout/what-is-checkout-BFffD-s0.png)

***

## Customization options

There are various types of Shopify Extensions that you can use to customize checkout:

* UI extensions
* Functions
* Web pixel extensions
* Payments extensions

All customization options are easy to install and upgrade-safe, enabling merchants to benefit from Shopify releases new products such as [Shop Pay](https://shopify.dev/docs/apps/build/checkout/test-checkout-ui-extensions#test-with-shop-pay), or features such as [One-page checkout](https://shopify.dev/docs/apps/build/checkout/test-checkout-ui-extensions#one-page-checkout).

For a detailed breakdown of the technologies that can be used to customize checkout, and the ways that you can extend checkout, refer to the [options for customizing Shopify checkout](https://shopify.dev/docs/apps/build/checkout/technologies).

If your extension sends data to your own app backend, such as storing records in your own database, build that backend with one of [Shopify's official libraries](https://shopify.dev/docs/api/libraries-and-templates). Shopify provides libraries for Node.js, Ruby on Rails, PHP frameworks like Laravel and Symfony (`shopify-app-php`), and Python frameworks like Django, Flask, and FastAPI (`shopify-app-python`).

**Note:**

Checkout apps and extensions have [design requirements](https://shopify.dev/docs/apps/launch/app-requirements-checklist#design-requirements-for-checkout-apps) that apply to custom apps as well as public apps. Be sure that your app meets [all requirements](https://shopify.dev/docs/apps/launch/app-requirements-checklist) for its functionality and distribution type.

***

## Getting started

To learn how to customize and extend checkout, read the following tutorials.

### Checkout UI extensions tutorials

[Pre-purchase product offers\
\
](https://shopify.dev/docs/apps/build/checkout/product-offers/build-a-pre-purchase-offer)

[Build a pre-purchase upsell offer that prompts the customer to add a product to their order.](https://shopify.dev/docs/apps/build/checkout/product-offers/build-a-pre-purchase-offer)

[Post-purchase checkout extensions\
\
](https://shopify.dev/docs/apps/build/checkout/product-offers/build-a-post-purchase-offer)

[Create a basic example of a post-purchase checkout extension.](https://shopify.dev/docs/apps/build/checkout/product-offers/build-a-post-purchase-offer)

[Thank you and order status extensions\
\
](https://shopify.dev/docs/apps/build/checkout/thank-you-order-status/add-survey)

[Build a survey that asks customers how they heard about the store after they made a purchase.](https://shopify.dev/docs/apps/build/checkout/thank-you-order-status/add-survey)

[Custom banners\
\
](https://shopify.dev/docs/apps/build/checkout/fields-banners/add-banner)

[Learn how to add a custom banner to checkout.](https://shopify.dev/docs/apps/build/checkout/fields-banners/add-banner)

[Custom fields\
\
](https://shopify.dev/docs/apps/build/checkout/fields-banners/add-field)

[Learn how to add custom fields to checkout that customers can use to add delivery instructions to their order.](https://shopify.dev/docs/apps/build/checkout/fields-banners/add-field)

[Client-side validation\
\
](https://shopify.dev/docs/apps/build/checkout/cart-checkout-validation/create-client-side-validation)

[Use a checkout UI extension to validate fields at checkout and block customer progress.](https://shopify.dev/docs/apps/build/checkout/cart-checkout-validation/create-client-side-validation)

[Header\
\
](https://shopify.dev/docs/apps/build/checkout/customize-header)

[Use a checkout UI extension and the GraphQL Admin API's checkout branding types to customize the checkout header with custom images, including the back to cart link.](https://shopify.dev/docs/apps/build/checkout/customize-header)

[Footer\
\
](https://shopify.dev/docs/apps/build/checkout/customize-footer)

[Use a checkout UI extension and the GraphQL Admin API's checkout branding types to customize the checkout footer with store policies.](https://shopify.dev/docs/apps/build/checkout/customize-footer)

[Address autocomplete\
\
](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/address-autocomplete/build-autocomplete)

[Build an extension to customize the address autocomplete provider for the delivery and billing address forms in checkout.](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/address-autocomplete/build-autocomplete)

### Shopify Functions tutorials

[Build a discount function\
\
](https://shopify.dev/docs/apps/build/discounts/build-discount-function)

[Use Shopify Functions to create a new discount type for users.](https://shopify.dev/docs/apps/build/discounts/build-discount-function)

[Create a payments function\
\
](https://shopify.dev/docs/apps/build/checkout/payments/create-payments-function)

[Use Shopify Functions to hide a payment option offered to customers at checkout.](https://shopify.dev/docs/apps/build/checkout/payments/create-payments-function)

[Build a delivery options function\
\
](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-options/build-function)

[Use Shopify Functions to rename a delivery option offered to customers at checkout.](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-options/build-function)

[Create a server-side validation function\
\
](https://shopify.dev/docs/apps/build/checkout/cart-checkout-validation/create-server-side-validation-function)

[Use Shopify Functions to block progress on a checkout when the cart line quantities exceed a limit.](https://shopify.dev/docs/apps/build/checkout/cart-checkout-validation/create-server-side-validation-function)

[Build a location rule function\
\
](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/location-rules/build-location-rule-function)

[Use Shopify Functions to choose a different order location during checkout.](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/location-rules/build-location-rule-function)

[Add a customized bundle function\
\
](https://shopify.dev/docs/apps/build/product-merchandising/bundles/add-customized-bundle-function)

[Use Shopify Functions to group products together and sell them as a single unit.](https://shopify.dev/docs/apps/build/product-merchandising/bundles/add-customized-bundle-function)

[Build a fulfillment constraints function\
\
](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/build-fulfillment-constraints-function)

[Use Shopify Functions to customize fulfillment and delivery strategies.](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/build-fulfillment-constraints-function)

[Build a local pickup options function\
\
](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/build-local-pickup-options-function)

[Use Shopify Functions to generate local pickup delivery options at checkout.](https://shopify.dev/docs/apps/build/orders-fulfillment/order-routing-apps/build-local-pickup-options-function)

[Create a local pickup charges function\
\
](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-methods/create-local-pickup-charges-function)

[Use Shopify Functions to create local pickup charges at checkout.](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-methods/create-local-pickup-charges-function)

[Generate a pickup points function\
\
](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-methods/generate-pickup-points)

[Use Shopify Functions to generate pickup point delivery options at checkout.](https://shopify.dev/docs/apps/build/checkout/delivery-shipping/delivery-methods/generate-pickup-points)

***

## Build for checkout

Checkout is where merchants solve a range of cross-cutting problems. Explore the hubs below for guides grouped by topic.

[Discounts\
\
](https://shopify.dev/docs/apps/build/discounts)

[Build custom discount types with Shopify Functions and configure them from the admin or customer accounts.](https://shopify.dev/docs/apps/build/discounts)

[Payments\
\
](https://shopify.dev/docs/apps/build/payments)

[Provide customized payment processing for merchants on checkout.](https://shopify.dev/docs/apps/build/payments)

[Product bundles\
\
](https://shopify.dev/docs/apps/build/product-merchandising/bundles)

[Group products together and sell them as a single unit.](https://shopify.dev/docs/apps/build/product-merchandising/bundles)

[Purchase options\
\
](https://shopify.dev/docs/apps/build/purchase-options)

[Offer subscriptions, pre-orders, and Try Before You Buy.](https://shopify.dev/docs/apps/build/purchase-options)

***

## Upgrade

**Deprecated:**

`checkout.liquid` is now unsupported for the Information, Shipping, and Payment checkout steps. `checkout.liquid` and additional scripts were sunset for the **Thank you** and **Order status** pages on August 28, 2025. Script tags were sunset on those pages on August 28, 2025 for Plus stores, and are sunset for non-Plus stores on August 26, 2026.

Stores that still use `checkout.liquid` for the **Thank you** and **Order status** pages must [upgrade to Shopify Extensions in Checkout](https://www.shopify.com/checkout#advanced-customizations).

A report identifying your current checkout customizations is available in the Shopify admin. The report provides high-level guidance to map customizations to Shopify Extensions in Checkout. Use this report to simplify your review of your existing customizations and to help you upgrade to Shopify Extensions in Checkout faster. [Learn more](https://help.shopify.com/en/manual/checkout-settings/checkout-extensibility/checkout-upgrade).

To upgrade a `checkout.liquid` customization to Shopify Extensions in Checkout, take one or more of the following actions:

1. Use a public app that's built using extensions.

   We're adding new checkout apps to the Shopify App Store on a regular basis. If there currently isn't a suitable public app for your customization, then consider simplifying your checkout temporarily and adding new apps to your store as they become available.

2. Build a custom app using extensions, or [hire a service partner](https://www.shopify.com/plus/partners/service?type=service\&services%5B%5D=141) to build one for you.

In some cases, after you've upgraded you can [revert to `checkout.liquid`](https://help.shopify.com/manual/checkout-settings/checkout-extensibility/checkout-upgrade#revert-to-checkout-liquid) until its sunset dates.

If you're upgrading a store to Shopify Extensions in Checkout, we recommend planning your in-checkout, **Thank you** page, and **Order status** page upgrades together, when possible, for the following benefits:

* Avoid maintaining multiple tech stacks, like UI extensions and `checkout.liquid`.

* Apply styling once to the entire experience.

* Manage one sunset date for `checkout.liquid` rather than one date for pre-purchase pages and another for **Thank you** and **Order status** pages.

  If this isn't possible, then we recommend prioritizing the upgrade for in-checkout pages first and upgrading after-purchase pages after that.

***

## Best practices

To optimize your app development experience, Shopify has established a set of best practices that you can refer to when developing an app that extends checkout.

**Tip:**

We also recommend getting familiar with Polaris [accessibility](https://polaris.shopify.com/foundations/accessibility) and [content](https://polaris.shopify.com/content/merchant-to-customer) guidelines.

[Checkout performance\
\
](https://shopify.dev/docs/apps/build/checkout/extension-performance/applying-changes)

[Learn best practices for applying changes to checkout.](https://shopify.dev/docs/apps/build/checkout/extension-performance/applying-changes)

[Create multi-page extensions\
\
](https://shopify.dev/docs/apps/build/checkout/create-multi-page-extensions)

[Learn more about building extensions that can render on any checkout page.](https://shopify.dev/docs/apps/build/checkout/create-multi-page-extensions)

[UX for checkout\
\
](https://shopify.dev/docs/apps/build/checkout/ux-for-checkout)

[Learn how to improve the quality of checkout experiences by following our UX guidelines for checkout.](https://shopify.dev/docs/apps/build/checkout/ux-for-checkout)

[Network requests from extensions\
\
](https://shopify.dev/docs/api/checkout-ui-extensions/latest/configuration#network-access)

[Learn about Cross-Origin Resource Sharing (CORS) and other security considerations when making network requests to your own server.](https://shopify.dev/docs/api/checkout-ui-extensions/latest/configuration#network-access)

[App Design Guidelines\
\
](https://shopify.dev/docs/apps/design-guidelines/)

[Get practical guidance on how to design a user interface for the Shopify admin.](https://shopify.dev/docs/apps/design-guidelines/)

***

## Product roadmap

Some checkout customization features are in development and will be released later this year. The following are the features on our roadmap and our estimated launch dates:

**Note:**

This roadmap is being shared for informational purposes and is subject to change. Bug fixes and improvements will be added as we hear from the community. Share your feedback or request new features by creating a new issue in the [Shopify developer community forum](https://community.shopify.dev/).

### Shopify Functions

We'll continue to add new Shopify Functions APIs to further customize checkout business logic.

| Milestone | Target |
| - | - |
| Introduced a new [Discount API](https://shopify.dev/docs/api/functions/reference/discount) that supports any combination of product, order, and shipping savings from a single function extension | April 2025 (shipped) |
| Support for cart metafields on function input queries | July 2025 (shipped) |
| Optionally reject discount codes and return custom messages when discounts shouldn't be applied [(Discount API)](https://shopify.dev/docs/api/functions/latest/discount) | Q4 2025 (shipped) |
| Support complex conditions for "Buy X Get Y" discounts [(Discount API)](https://shopify.dev/docs/api/functions/latest/discount) | Q1 2026 (shipped) |
| Changes to the [Discount API](https://shopify.dev/docs/api/functions/reference/discount) to stack multiple discounts on the same product line item | Q1 2026 (shipped) |

***
