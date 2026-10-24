# Primary gateways for international and local pricing support

On this page you can find a breakdown of payment methods supporting local pricing within Shopify Payments, as well as details on Adyen's integration with international sales tools for currency processing.

## Shopify Payments support for local pricing

The following table lists the payment methods for Shopify Payments and their level of support for local pricing.

<table>
   <caption>Payment methods for Shopify Payments</caption>
   <thead>
      <tr>
         <th scope="col">Payment category</th>
         <th scope="col">Payment method</th>
         <th scope="col">Support</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td>Credit card</td>
         <td>Credit card checkout</td>
         <td>Fully supported</td>
      </tr>
      <tr>
         <td rowspan='3' colspan='1'>Accelerated checkout</td>
         <td>Shop Pay</td>
         <td>Fully supported</td>
      </tr>
      <tr>
         <td scope="row">Apple Pay</td>
         <td>Supported but without checkout restrictions</td>
      </tr>
      <tr>
         <td scope="row">Google Pay</td>
         <td>Supported but without checkout restrictions</td>
      </tr>
      <tr>
         <td scope="row">Amazon Pay</td>
         <td>Unsupported and prices convert to shop currency</td>
      </tr>
      <tr>
         <td rowspan='4' colspan='1'>Local payment methods</td>
         <td>Klarna</td>
         <td>Fully supported</td>
      </tr>
      <tr>
         <td scope="row">iDEAL | Wero</td>
         <td>Fully supported</td>
      </tr>
      <tr>
         <td scope="row">EPS Payments</td>
         <td>Fully supported</td>
      </tr>
      <tr>
         <td scope="row">Bancontact</td>
         <td>Fully supported</td>
      </tr>
      <tr>
         <td rowspan='3' colspan='1'>Additional payment methods</td>
         <td>PayPal Express</td>
         <td>Supported but without checkout restrictions</td>
      </tr>
      <tr>
         <td scope="row">Others</td>
         <td>Unsupported and prices convert to shop currency</td>
      </tr>
   </tbody>
</table>

## Adyen's compatibility with international sales tools

Adyen is a third-party payment gateway available for enterprise-level businesses. It can be used with international sales tools to sell in local currencies. Transactions are processed in the currency sent by Shopify to Adyen when international sales tools are activated. You need to configure the currencies of your markets within Adyen. If the currency matches one of Adyen's settlement currencies for the region, then payouts are settled in that currency accordingly. Learn more about [Adyen](/manual/payments/third-party-providers/adyen-gateway).
