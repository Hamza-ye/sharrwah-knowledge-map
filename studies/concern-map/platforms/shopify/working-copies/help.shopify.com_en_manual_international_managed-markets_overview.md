# Overview of Managed Markets

You can use Managed Markets to sell to customers in other countries without registering a business, registering for tax, or arranging customs clearance in each destination. Your customers buy from your store, in your brand's checkout, and pay in their own currency. Their order arrives without a surprise bill at the door.

Managed Markets builds on [Shopify Markets](/manual/markets), the tools built into every store for selling in other countries, including localized domains and [store translation](/manual/international/languages). With Shopify Markets on its own, you remain the [merchant of record](#merchant-of-record), so tax registration, duties, and customs compliance stay your responsibility. Managed Markets adds Global-e as the merchant of record and takes those responsibilities on for a per-order fee. To compare the two feature by feature, refer to [Comparing International and Managed Markets features](/manual/international/managed-markets/compare). To have duties and import taxes calculated at checkout and remain the merchant of record, refer to [charging duties and import taxes](/manual/international/duties-and-import-taxes/charging-duties) instead.

To use Managed Markets, your store needs to be on the Basic plan or higher, have an online store, and use [Shopify Payments](/manual/payments/shopify-payments). Managed Markets is available to businesses based in the continental United States, and to certain stores in Canada and the United Kingdom. Refer to [requirements and considerations](/manual/international/managed-markets/requirements-and-considerations) before you activate it.

All Managed Markets questions go to Shopify Support, regardless of the role that Global-e plays in the service. Global-e is your [merchant of record](/manual/international/managed-markets/overview#merchant-of-record) and handles parts of your Managed Markets orders, including duties, tax remittance, commercial invoices, and carrier arrangements. Requests about your orders, payouts, shipping labels, returns, and tax or customs documents still go through [Shopify Support](/manual/your-account/contact-shopify-support), and not to Global-e directly.

Global-e also has a standalone third-party app, which is different from Managed Markets. If you use the standalone Global-e app instead of Managed Markets, then Global-e supports you directly. You can't use Managed Markets and the Global-e app at the same time.


## Managed Markets benefits {#benefits}

Managed Markets takes on the parts of international selling that otherwise need country-by-country expertise:

* **Tax registration and remittance**: Global-e registers for tax in the countries that you sell to and remits duties and taxes to local authorities on your behalf, which removes the need for you to register for tax filing in those destinations.
* **Local laws and product restrictions**: Managed Markets complies with local laws for cross-border products, restricts certain products to specific destinations, and creates commercial invoices and remits them where they're needed. To learn more, refer to the [Managed Markets Merchant Service Terms](https://content.global-e.com/merchant-terms-v3).
* **Customs classification**: Harmonized System (HS) codes are assigned to your products automatically and adjusted for each destination's restrictions, which is what lets an order clear customs with duties already paid.
* **Guaranteed duty and tax amounts**: The duty and tax amounts displayed to your customer at checkout are guaranteed. When the amount charged by customs is different, Managed Markets covers the difference, and you don't have to pay any additional fees.
* **Delivered duty paid (DDP) shipping**: Discounted shipping labels ship with duties prepaid to most destinations, so your customer isn't asked for money at the time of delivery. Stores in the United States can buy DHL Express, DHL eCommerce, and FedEx labels. Stores in Canada and the United Kingdom can buy DHL Express and FedEx labels. You can also use these carriers for delivered duty unpaid (DDU) shipments to the destinations where duties and import taxes can't be calculated.
* **Local currency and local payment methods**: Your customers can pay in their own currency, using the payment methods they expect in their own country, which can help to increase your conversion rate.
* **A guaranteed conversion rate on refunds**: Refunds made within 30 days of the transaction use the [currency conversion rate](/manual/international/pricing/fees) that was given at the time of purchase, so currency fluctuations don't affect them.
* **Address validation**: Managed Markets checks whether the address that your customer adds during checkout is valid, which reduces failed deliveries.
* **Fraud protection**: Orders on Managed Markets in the United States are automatically reviewed and given protection for fraud chargebacks.

### Fraud and chargebacks {#fraud}

If your store is based in the United States, then your Managed Markets orders are automatically reviewed for fraud, and eligible orders are protected from fraud chargebacks with Shopify Protect. Refer to [Shopify Protect](/manual/payments/shop-pay/shopify-protect) to learn more. There are some chargeback cases that aren't covered by Managed Markets, and you're responsible for handling those yourself.

## Duties and taxes {#duties-display}

Managed Markets orders ship [delivered duty paid (DDP)](/manual/international/duties-and-import-taxes/carriers-and-shipping-terms#carriers) to most destinations, which means that duties, import taxes, and customs fees are settled before the parcel arrives, and the carrier doesn't ask your customer for money at the door. This helps to prevent the surprise charges that lead to refused and returned international packages.

A small number of destinations ship delivered duty unpaid (DDU), because Managed Markets can't calculate duties and import taxes for them. For those destinations, your customer might be asked to pay duties and import taxes on delivery.

The **Include duties and taxes in prices dynamically by region** setting controls how this cost is presented to your customer:

* **Turned on (the default)**: Your product prices for a market are adjusted to include import tax, duties, and Managed Markets fees, and your customer views a single price with a note that duties and taxes are included. No duty line is added at checkout, and your payout stays consistent with your domestic orders. The **Duties and taxes** row then reads *Included in prices dynamically by region*. Refer to [international pricing for Managed Markets](/manual/international/managed-markets/adaptive-pricing) to learn more.
* **Turned off**: You choose how duties and taxes are presented to your customer. They can be added to the total at checkout, or treated as already included in your product prices.

To change this setting, go to the [**Markets**](https://admin.shopify.com/markets) page in your Shopify admin, open a market, and then edit its Managed Markets settings.

## Merchant of record {#merchant-of-record}

A merchant of record is the legal entity responsible for selling products to a customer, and for adhering to local laws and regulations in another region or country. Unless another party such as Global-e is hired to take on these responsibilities, most merchants act as their own merchant of record. When you act as your own merchant of record, you're responsible for registering for and remitting taxes, arranging to accept local methods of payment, and organizing shipping and fulfillment. Getting it wrong results in parcels held at the border, unexpected charges for your customer, or penalties for you.

With Managed Markets, Global-e manages the complexities of selling to other countries or regions on your behalf, including remitting tax to local authorities, accepting local methods of payment, and managing duties and import tax, allowing you to start selling to new international markets quickly. When using Managed Markets, you don't need tax registrations in the countries you sell to. Global-e provides the tax registrations, allowing you to comply when selling internationally. You keep your storefront, your brand, your prices, and your relationship with your customer.

### Merchant of record disclaimer at checkout {#mor-disclaimer}

When you use Managed Markets, Global-e is the merchant of record. A disclaimer is displayed at checkout on your Managed Markets orders which states that your customer is purchasing from Global-e, and provides a link to Global-e's terms and conditions and privacy policy. The disclaimer is displayed only to customers in the markets that are managed by Managed Markets. Your domestic checkout remains unchanged.

The disclaimer is a required part of the merchant of record arrangement. You can't hide or reword it, and no setting in your Shopify admin or your theme turns it off. The only way to remove it for a market is to [deactivate Managed Markets](/manual/international/managed-markets/deactivation) for that market and act as your own merchant of record.

### Flow of funds {#flow-of-funds}

Managed Markets features are powered by Global-e. After an international Managed Markets order is placed in your store, Shopify Payments processes the transaction and holds the money in a Global-e account. When Global-e goes across the border, they act as your merchant of record. Global-e holds the funds to remit the costs to proper authorities that are involved in the cross-border commerce transaction.

## Pricing {#pricing}

Managed Markets has the following fees for international orders:
* A transaction fee:
   * 3.25% for stores on the Shopify Plus plan.
   * 3.5% for stores that are on the Basic, Grow, or Advanced plan.
* A [currency conversion fee](/manual/international/pricing/fees#conversion-rate-and-fee), also known as the foreign exchange (FX) fee. The rate is the same as your Shopify Payments currency conversion fee, which varies by region. You can adjust your product prices for international markets to be higher or lower based on your preferences.
* A Shopify Payments processing fee that can vary based on your Shopify plan and the card type used by your customer.

Refer to [Managed Markets with Shopify Payments](/manual/international/managed-markets/shopify-payments) for more information on pricing.

### Determining tax on the Managed Markets fee {#fee-tax}

In some countries, the Managed Markets fee is taxable. Whether the fee is taxed depends on the address associated with the legal business name on your store. This address determines both whether tax is added to the fee, and which tax applies:

* If your legal business address is in the United States, then no tax is added to the Managed Markets fee.
* If your legal business address is in the United Kingdom, then VAT is added to the Managed Markets fee.
* If your legal business address is in Canada, then GST, HST, QST, PST, or RST is added to the Managed Markets fee, depending on your province.

When [duties and taxes are included in your prices](/manual/international/managed-markets/adaptive-pricing), any applicable tax on the Managed Markets fee is built into your product prices, so your customers cover it. The tax isn't listed separately to your customers. When they aren't included in your prices, any applicable tax is charged to you directly and recorded on your merchant fee invoice.

## Harmonized System (HS) codes {#hs-code}

In Managed Markets, Harmonized System (HS) codes are automatically assigned to your products and might differ from the ones that you initially entered. These codes are adjusted based on country-specific restrictions to comply with import regulations. You can review both your manually entered HS codes and the HS codes that Managed Markets assigns to your products in your Shopify admin. For more information about HS codes, refer to [adding HS codes to your products](/manual/international/duties-and-import-taxes/charging-duties#add-hs-codes).

To review the HS codes that have been assigned to your products, go to an individual product's page and refer to the information in the **Shipping** section. If HS codes aren't displayed, then they haven’t been assigned yet. However, [duty guarantee at checkout](/manual/international/managed-markets/overview#benefits) is still in place to ensure smooth delivery.

## Payment methods {#local-payment-methods}

With Managed Markets you can use more local payment methods for markets worldwide. For example, if you're selling products to customers in Denmark, then those customers can pay for products with Klarna using DKK currency.

New local payment methods are continuously being added to Managed Markets. To learn more, refer to [local payment methods with Managed Markets](/manual/international/managed-markets/shopify-payments#local-payment-methods).

### Shop Pay {#shop-pay}

If you have [an upgraded checkout](/manual/checkout-settings/customize-checkout-configurations/upgrade-thank-you-order-status/upgrade-guide) activated on your store, then you can use [Shop Pay](/manual/payments/shop-pay) for your international markets with Managed Markets. Your international customers can use their Shop accounts for express checkout.

## Getting paid {#getting-paid}

When you use Managed Markets, your payouts are processed daily by Shopify Payments. Refer to [Managed Markets with Shopify Payments](/manual/international/managed-markets/shopify-payments) to learn more.
