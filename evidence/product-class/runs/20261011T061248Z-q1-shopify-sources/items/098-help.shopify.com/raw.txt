# VAT validation in checkout

VAT validation lets your business customers enter a VAT number at checkout to claim the reverse charge exemption on eligible cross-border orders. When the exemption applies, VAT is removed from the order and the customer is responsible for reporting and paying VAT on their own tax return.

## EU/UK reverse charge exemption

<aside class="note"><h4>Note</h4><p>VAT validation for the reverse charge (EU/UK) exemption is available for customers that use guest checkout or Shop Pay checkout. VAT validation isn&#39;t currently available for B2B-specific checkouts.</p>
</aside>

The reverse charge (EU/UK) exemption fully exempts VAT on orders that are shipped to customers within the European Union or the United Kingdom, provided that the destination country is different from the country of the fulfillment location. When the exemption applies, the customer isn't charged VAT for the order.

When a VAT number is added to any [customer](/manual/customers/manage-customers#add-customer-profiles), it's automatically validated. If the number is valid, or if the field is left empty, then the contents of the field are stored in the customer's profile for future orders and for reference.

When the tax exemption is applied, VAT is removed from the order, and is the responsibility of the customer to report and pay. A note stating **Reverse Charge Mechanism: Recipient responsible for VAT** is added to the VAT invoice.

## Considerations for VAT validation in checkout

Before you use VAT validation in checkout, review the following considerations:

* For customers who qualify for the reverse charge exemption, a valid VAT number controls whether VAT is charged. If [dynamic tax-inclusive pricing](/manual/international/pricing/dynamic-tax-inclusive-pricing#how-to-enable) isn't active for the destination market, then the price that's displayed to the customer stays the same.
* If dynamic tax-inclusive pricing is active, then prices adjust by the standard tax rate of the destination market. Reduced rates from product tax categories and tax overrides aren't applied, so an adjusted price can differ from the tax that the customer is charged. Review the [considerations for using dynamic tax-inclusive pricing](/manual/international/pricing/dynamic-tax-inclusive-pricing#considerations-for-using-dynamic-tax-product-pricing) before you rely on the adjusted price.

## Activate VAT validation in checkout

<aside class="note"><h4>Note</h4><p>If you activate the <strong>Company VAT number</strong> option in your checkout, then ensure that you also activate <a href="/en/manual/taxes/shopify-tax/vat-invoices">VAT invoices</a> for your customers.</p>
</aside>

You can display the **Company VAT number** field [in your checkout](/manual/checkout-settings/checkout-form-options#customer-information) for customers to enter their VAT number and apply the reverse charge exemption for eligible EU or UK cross-border orders. The options for this field are **Don't include** and **Optional**. **Don't include** is the default setting. If you sell to customers in the European Union and want to allow customers to provide their VAT number at checkout, then select **Optional**.

VAT validation in checkout is available only for stores that use Shopify Tax to calculate tax in the European Union or the United Kingdom. If you use Shopify Tax for either region, then activating the **Company VAT number** field makes it available for both EU and UK cross-border orders. You don't need Shopify Tax registrations for both regions for the field to apply to buyers in each.

If you don't sell to businesses located in the European Union or the United Kingdom, then select **Don't include** to prevent this field from being displayed during checkout.

## Fulfillment location requirements

The reverse charge exemption is based on your fulfillment location, not the store address in your [**General**](https://admin.shopify.com/settings/general) settings. An active fulfillment location in the European Union is required for the EU/UK reverse charge exemption to work properly.

The exemption applies to the following cross-border combinations:

* European Union fulfillment location to a different EU country
* European Union fulfillment location to the United Kingdom

The exemption doesn't apply to the following combinations:

* United Kingdom to European Union orders
* United Kingdom to United Kingdom orders

If an order is fulfilled from more than one location, then only one of those locations is used as the origin for the reverse charge exemption. Orders that have items stocked at locations in different countries aren't supported, so the exemption might not be applied as expected.

The origin that's used for the exemption is determined when the order is created, and it isn't always the location that the order is fulfilled from. [Changing an order's fulfillment location](/manual/fulfillment/fulfilling-orders/single-fulfillment#change-location) after the order is created doesn't re-evaluate the reverse charge exemption, so the exemption isn't applied to an order that already exists.

## Troubleshooting

### VAT is charged after a customer enters a valid VAT number

Shopify validates VAT numbers in real time through the EU's [VAT Information Exchange System (VIES)](https://ec.europa.eu/taxation_customs/vies/#/vat-validation). If VIES can't complete validation when a customer submits their VAT number during checkout, then the reverse charge exemption isn't applied and VAT is charged by default. This protects you from granting tax exemptions that can't be verified.

VIES can become unavailable for several reasons, including scheduled maintenance by the European Commission or individual EU member state tax authorities, temporary outages due to high traffic, or network connectivity issues. You can check the current availability of VIES on the [European Commission's VIES website](https://ec.europa.eu/taxation_customs/vies/#/vat-validation). If the service returns errors or is unresponsive, then VAT numbers can't be validated until the service recovers. There's no option to manually override VIES validation — the reverse charge exemption requires a successful validation.

If you have B2B customers who should always receive a tax exemption, then you can set their tax status to **Don't collect tax** from their [customer profile](/manual/customers/manage-customers#edit-customer-profiles). This exemption applies to all future orders from that customer without requiring real-time VIES validation, and must be configured before the customer places their order.
