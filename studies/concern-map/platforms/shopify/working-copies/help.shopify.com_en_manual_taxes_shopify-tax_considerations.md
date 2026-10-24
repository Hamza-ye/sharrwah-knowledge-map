# Considerations for using Shopify Tax

<aside class="note"><h4>Note</h4><p>This guide is for merchants who use Shopify Tax calculations to sell in the United States, European Union, or United Kingdom. If you set your tax rates manually, then refer to <a href="/en/manual/taxes/manual-tax-settings">Manual tax settings</a>.</p>
<p>It&#39;s your responsibility to consult with local tax authorities or a tax professional to verify that you charge your customers the correct tax rates, and to ensure you file and remit your taxes correctly.</p>
</aside>

Calculations using Shopify Tax are available only for certain transactions, where the order's destination is a location in the United States, European Union, United Kingdom, or Canada.

## Considerations for Shopify Tax in the United States

If a tax calculation can't be performed by Shopify Tax for an order with a destination in the United States, then the tax calculation is performed by using registration-based, non-rooftop accurate calculations. For more information, refer to [US taxes](/manual/taxes/us) or to [Basic Tax service settings](/manual/taxes/registration).

Calculations using Shopify Tax in the United States aren't available in the following scenarios:

* Orders that are shipped to a country other than the United States.
* Third-party app and API-generated orders, such as Amazon orders.
* Orders that contain one or more products with an associated [product or shipping rate tax override](/manual/taxes/tax-overrides#apply-tax-override).
* Resort Tax isn't automatically included in Shopify Tax's calculations. If you need to add Resort Tax to your transactions, then you need to use [Manual Tax](/manual/taxes/manual-tax-settings).

## Considerations for Shopify Tax in the European Union and United Kingdom

If a tax calculation can't be performed by Shopify Tax for an order with a destination in the European Union or United Kingdom, then the tax calculation is performed by using registration-based calculations. For more information, refer to [EU taxes](/manual/taxes/eu).

Calculations using Shopify Tax in the European Union and United Kingdom aren't available in the following scenarios:

* Orders that are shipped to a location other than one within the European Union or United Kingdom.
* Orders where VAT is remitted to Portugal.
* Orders where [VAT invoicing](/manual/taxes/shopify-tax/vat-invoices) isn't activated.
* Orders where VAT isn't collected or calculated. If VAT is calculated but is calculated to be zero, then invoices are still generated.
* Orders where duties are calculated.

If your store is located in Northern Ireland (NI), then [choose the same tax service](/manual/taxes/shopify-tax/choose-tax-service) for both regions to ensure proper cross border VAT collection.

## Considerations for Shopify Tax in Canada

If a tax calculation can't be performed by Shopify Tax for an order with a destination in the Canada, then the tax calculation is performed by using registration-based, non-rooftop accurate calculations. For more information, refer to [Canadian taxes](/manual/taxes/canada) or to [Basic Tax service settings](/manual/taxes/registration).

Calculations using Shopify Tax in Canada aren't available in the following scenarios:

* Orders that are shipped to a country other Canada.
* Third-party app and API-generated orders, such as Buy Button, Facebook, or Amazon orders.
* Orders that contain one or more products with an associated [product or shipping rate tax override](/manual/taxes/tax-overrides#apply-tax-override).
