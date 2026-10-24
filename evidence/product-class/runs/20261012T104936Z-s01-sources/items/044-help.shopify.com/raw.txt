# Understanding payment gateway availability

When setting up payments on your Shopify store, select payment gateways and providers that are compatible and available in your region. Use the [Shopify payment gateways page](https://www.shopify.com/payment-gateways) as your primary resource for up-to-date information about which payment solutions are available for your store.

## Check payment gateway availability by country

You can [filter available payment providers](https://www.shopify.com/payment-gateways) by country or region to find detailed and updated information about which payment gateways are available in your store's location.

#### Steps:

1. Go to [Shopify's payment gateways](https://www.shopify.com/payment-gateways) page.
2. Choose your location using the filter.
3. View the list of available payment gateways for your selected location.

## Stripe availability in Shopify Payments regions {#stripe-in-shopify-payments-regions}

Shopify Payments is the only payment gateway designed and operated by Shopify. If it's [supported in the country](/manual/payments/shopify-payments/supported-countries) where your business is located, then Stripe won't be available for you to activate. This is because Stripe is Shopify Payments' banking partner, and all payment reporting and management takes place in your Shopify admin.

If you can't activate Shopify Payments in a supported country, for example, because of [what you sell](/manual/payments/shopify-payments/onboarding/eligibility#prohibited-businesses), then standalone Stripe isn't available as an alternative. Instead, [add a third-party payment provider](/manual/payments/third-party-providers) that supports your business type.

## Frequently asked questions about payment gateway availability

<div class="accordion-faq">

  <details>
    <summary id="stripe-not-available">Why isn't Stripe available as a payment gateway?</summary>

In countries where Shopify Payments is available, Stripe isn't listed as a separate third-party payment gateway, for the reason described in <a href="#stripe-in-shopify-payments-regions">Stripe availability in Shopify Payments regions</a>. If you're in a Shopify Payments region and can't activate Shopify Payments, then standalone Stripe isn't available as an alternative. Add a <a href="/manual/payments/third-party-providers">third-party payment provider</a> instead.

  </details>

  <details>
    <summary id="check-provider-availability">How can I find out if a specific payment provider is supported in my country?</summary>

While specific details about each payment provider's availability can vary, the best source for accurate and real-time updates is the <a href="https://www.shopify.com/payment-gateways">Shopify payment gateways page</a>.

  </details>

  <details>
    <summary id="new-gateways-added">Are new payment gateways frequently added to Shopify?</summary>

Yes, Shopify consistently updates its list of available payment gateways to include new options and geographic expansions. Always check the <a href="https://www.shopify.com/payment-gateways">Shopify payment gateways page</a> for the most recent updates and additions.

  </details>

  <details>
    <summary id="gateway-not-listed">What should I do if the payment gateway I want isn't listed for my region?</summary>

If a desired <a href="https://www.shopify.com/payment-gateways">payment gateway isn't listed for your region</a>, then it might not be supported by Shopify at this time. You can consider alternative payment gateways that are listed as available in your region.

  </details>

  <details>
    <summary id="set-up-gateway">How do I set up a new payment gateway on my Shopify store?</summary>

Refer to <a href="/manual/payments/third-party-providers/configuring-providers">Configuring third-party payment providers</a> for detailed instructions on how to set up a new payment gateway on your Shopify store.

  </details>

  <details>
    <summary id="provider-not-accessible">What should I do if a provider is listed on the payment gateways page but isn't accessible in my admin?</summary>

The payment gateways page lists providers by region, but the options available in your store's admin also depend on your current payment configuration. For example, some providers are configured in the **Additional payment methods** section rather than the third-party provider list, and the path to add a credit card provider varies depending on whether Shopify Payments is active. To identify the correct location in your Shopify admin, follow the steps to <a href="/manual/payments/third-party-providers/configuring-providers#troubleshoot-missing-provider">troubleshoot a missing payment provider</a>.

  </details>
</div>
