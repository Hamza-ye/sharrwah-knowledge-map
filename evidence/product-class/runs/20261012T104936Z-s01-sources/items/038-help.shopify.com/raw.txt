# Understanding Shopify Payments payout timing

Shopify Payments payout timing determines when funds from your sales are available in your bank account. Payout settlement times vary by country and risk level. 

Settlement time refers to the amount of time between when a customer's payment is captured and those funds are available to be paid out to your bank account. The date and time that a customer's payment is captured is recorded in Coordinated Universal Time (UTC). Funds from payments that are captured on Friday, Saturday, and Sunday are grouped and sent together as one payout.

The minimum settlement time depends on your region, risk level, and the payment method used. Some transactions, such as refunds and chargebacks, can settle faster than charges, and reduce your payout amount. 

After funds are paid out, they might take an additional 1-3 days to display in your bank account. This depends on your bank's processing time and is out of Shopify’s control.

If you're experiencing a payout delay that exceeds what you expect, then begin troubleshooting by checking your Shopify admin for any alerts, banners, or notifications related to your account status. Additionally, check the store owner email address for any correspondence from Shopify regarding payout issues. If you can’t identify the problem, then reach out to Shopify Support. Shopify Support can help you understand the status of your account and provide guidance on how to resolve any issues that might be delaying your payouts.

## Payout schedule

Your payout schedule determines when funds from sales are transferred to your bank account. You can choose daily, weekly, or monthly payouts based on your business needs. Some countries, such as Japan, have requirements that limit available payout options. Learn more about [scheduling your Shopify Payments payouts](/manual/payments/shopify-payments/payouts/schedule-payouts).

## Cutoff times for processing payouts

Payout schedules use business days only. Weekends and holidays don't count toward your settlement time. For example, if you receive an order on Friday (day 0) and your settlement time is three business days, then your payout processes on Wednesday.

### Example: Calculating payout timing for a Friday charge

Review the following example that demonstrates how business days are counted when a charge occurs on a Friday with a three business day settlement time.

* **Friday** : Day 0 (charge date)
* **Saturday and Sunday** : Non-business days (not counted)
* **Monday** : Day 1
* **Tuesday** : Day 2
* **Wednesday** : Day 3, the payout is processed.

Charges from Saturday and Sunday are also processed on Wednesday, because weekend days count as Day 0.

## Regional settlement times {#settlement-times-by-country-shopify-payments}

Settlement times vary by country, risk level, and the transaction type. For countries with a minimum payout threshold, if there's a payout for less than this amount, then the payout stays in a pending state until more funds are available to pay out. 

Payments with automated clearing house (ACH) direct debit can take up to 4 business days to settle and don't follow the same settlement timing of other transactions. After the payment settles, the funds are paid out according to your set payout schedule. Learn more about [ACH Direct Debit payments](/manual/payments/shopify-payments/local-payment-methods/ach).

The following table explains the settlement times for when a charge is processed for selected regions.

<div>
<table>
   <caption>Shopify Payments payout information by country.</caption>
   <thead>
       <tr>
           <th scope="col"><b>Country</b></th>
           <th scope="col"><b>Currency</b></th>
           <th scope="col"><b>Minimum settlement time</b></th>
           <th scope="col"><b>Minimum payout amount</b></th>
           <th scope="col"><b>Relevant Shopify Payments help article</b></th>
       </tr>
   </thead>
   <tbody>
       <tr>
           <th scope="row">Australia</th>
           <td>AUD, CAD, CHF, DKK, EUR, GBP, HKD, JPY, NOK, NZD, SEK, SGD, USD</td>
           <td>2 business days</td>
           <td>None</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/australia/">Shopify Payments for Australia</a></td>
       </tr>
       <tr>
           <th scope="row">Austria</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/austria/">Shopify Payments for Austria</a></td>
       </tr>
       <tr>
           <th scope="row">Belgium</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/belgium/">Shopify Payments for Belgium</a></td>
       </tr>
       <tr>
           <th scope="row">Canada</th>
           <td>CAD ($) or USD ($)</td>
           <td>3 business days</td>
           <td>None</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/canada/">Shopify Payments for Canada</a></td>
       </tr>
       <tr>
           <th scope="row">Croatia</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/croatia/">Shopify Payments for Croatia</a></td>
       </tr>
       <tr>
           <th scope="row">Cyprus</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/cyprus/">Shopify Payments for Cyprus</a></td>
       </tr>
       <tr>
           <th scope="row">Czechia</th>
           <td>EUR (€) or CZK (Kč)</td>
           <td>3 business days</td>
           <td>€1 or 30 Kč</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/czechia/">Shopify Payments for Czechia</a></td>
       </tr>
       <tr>
           <th scope="row">Denmark</th>
           <td>EUR (€) or DKK (kr)</td>
           <td>3 business days</td>
           <td>€1 or 20 kr</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/denmark/">Shopify Payments for Denmark</a></td>
       </tr>
       <tr>
           <th scope="row">Finland</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/finland/">Shopify Payments for Finland</a></td>
       </tr>
       <tr>
           <th scope="row">France</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€10 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/france/">Shopify Payments for France</a></td>
       </tr>
       <tr>
           <th scope="row">Germany</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/germany/">Shopify Payments for Germany</a></td>
       </tr>
       <tr>
           <th scope="row">Hong Kong SAR</th>
           <td>HKD</td>
           <td>4 business days</td>
           <td>10 HKD</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/hong-kong">Shopify Payments for Hong Kong SAR</a></td>
       </tr>
       <tr>
           <th scope="row">Ireland</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/ireland/">Shopify Payments for Ireland</a></td>
       </tr>
       <tr>
           <th scope="row">Italy</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/italy/">Shopify Payments for Italy</a></td>
       </tr>
        <tr>
           <th scope="row">Japan</th>
           <td>JPY (￥)</td>
           <td>5 business days</td>
           <td>5 JPY</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/japan">Shopify Payments for Japan</a></td>
       </tr>
        <tr>
           <th scope="row">Latvia</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€3 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/latvia/">Shopify Payments for Latvia</a></td>
       </tr>
        <tr>
           <th scope="row">Lithuania</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/lithuania/">Shopify Payments for Lithuania</a></td>
       </tr>
        <tr>
           <th scope="row">Malta</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/malta/">Shopify Payments for Malta</a></td>
       </tr>
        <tr>
           <th scope="row">Mexico</th>
           <td>MXN</td>
           <td>7 business days</td>
           <td>10 MXN</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/mexico/">Shopify Payments for Mexico</a></td>
       </tr>
        <tr>
           <th scope="row">Netherlands</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/netherlands/">Shopify Payments for Netherlands</a></td>
       </tr>
        <tr>
           <th scope="row">New Zealand</th>
           <td>NZD</td>
           <td>3 business days</td>
           <td>None</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/new-zealand">Shopify Payments for New Zealand</a></td>
       </tr>
        <tr>
           <th scope="row">Norway</th>
           <td>EUR (€) or NOK</td>
           <td>3 business days</td>
           <td>€1 EUR or 20 NOK</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/norway/">Shopify Payments for Norway</a></td>
       </tr>
        <tr>
           <th scope="row">Poland</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/poland/">Shopify Payments for Poland</a></td>
       </tr>
        <tr>
           <th scope="row">Portugal</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/portugal/">Shopify Payments for Portugal</a></td>
       </tr>
        <tr>
           <th scope="row">Romania</th>
           <td>EUR (€) or RON</td>
           <td>3 business days</td>
           <td>€1 EUR or 5 RON</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/romania">Shopify Payments for Romania</a></td>
       </tr>
        <tr>
           <th scope="row">Singapore</th>
           <td>SGD</td>
           <td>4 business days</td>
           <td>1 SGD</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/singapore/">Shopify Payments for Singapore</a></td>
       </tr>
        <tr>
           <th scope="row">Slovenia</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/slovenia/">Shopify Payments for Slovenia</a></td>
       </tr>
        <tr>
           <th scope="row">Spain</th>
           <td>EUR (€)</td>
           <td>3 business days</td>
           <td>€1 EUR</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/spain/">Shopify Payments for Spain</a></td>
       </tr>
        <tr>
           <th scope="row">Sweden</th>
           <td>EUR (€) or SEK (kr)</td>
           <td>3 business days</td>
           <td>€1 EUR or 20 SEK</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/sweden/">Shopify Payments for Sweden</a></td>
       </tr>
        <tr>
           <th scope="row">Switzerland</th>
           <td>EUR (€) or CHF (Fr)</td>
           <td>3 business days</td>
           <td>€1 EUR or 5 CHF</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/switzerland">Shopify Payments for Switzerland</a></td>
       </tr>
        <tr>
           <th scope="row">United Arab Emirates</th>
           <td>AED</td>
           <td>5 business days</td>
           <td>20 AED</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/united-arab-emirates/">Shopify Payments for the United Arab Emirates</a></td>
       </tr>
        <tr>
           <th scope="row">United Kingdom (UK)</th>
           <td>GBP (£)</td>
           <td>3 business days</td>
           <td>£1 GBP</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/united-kingdom">Shopify Payments for United Kingdom (UK)</a></td>
       </tr>
        <tr>
           <th scope="row">United States (U.S)</th>
           <td>USD ($)</td>
           <td>3 business days</td>
           <td>None</td>
           <td><a href="/manual/payments/shopify-payments/supported-countries/united-states/">Shopify Payments for United States (U.S)</a></td>
       </tr>
      </tbody>
</table>
</div>

### Payouts with Shopify Balance

After you sign up for a Shopify Balance account, your main Balance account is automatically set as your Shopify Payments payout account. This means that using your main Balance account lets you receive money from your Shopify sales up to 7 days earlier than a bank.

Payouts from Shopify Payments can arrive in your Shopify Balance account within 1 business day from the transaction processing date. In some cases, payouts for new merchants can take up to 5 business days. Learn more about [payouts from Shopify Payments arriving in your Shopify Balance account](/manual/finance/shopify-balance/payouts/payout-accounts). 

## Troubleshooting payout delays

If your payouts take longer than expected after fulfilling orders for a few weeks, then multiple factors can contribute to the delay. Check your Shopify admin for alerts, banners, or notifications about your account status. Also check your store owner email for correspondence from Shopify. If you can't identify the issue, contact Shopify Support. Review the following common causes for payout delays.

### Account reviews and holds

Payouts can be temporarily held while your account undergoes review. This review can be influenced by several factors, including the following examples:

* Chargeback disputes
* Compliance checks or potential violations of [Shopify Payments Terms of Service for your country](https://www.shopify.com/ca/legal) 
* Customer complaints
* [High-risk orders](/manual/fulfillment/managing-orders/protecting-orders/fraud-analysis#fraud-recommendations) 
* Fraud or compliance investigations by our financial partners
* Fulfillment issues
* Onboarding processes that require additional documentation or verification

<aside class="note"><h4>Note</h4><p>The store owner receives notifications in their Shopify admin or by email when a payout hold is placed on your account. Review your <a href="/en/manual/your-account/users/roles/permissions/store-permissions#finance-permissions">store role permissions</a> to ensure that the correct users in your business also receive payout-related notifications in their Shopify admin.</p>
</aside>

### Payout destination change

When you change your payout destination to a new external bank account, or add a new payout bank account more than 24 hours after completing your Shopify Payments setup, your payouts are temporarily paused for 3-5 business days. This pause is intended to protect your account from unauthorized access while Shopify verifies the new account.

This pause doesn't apply when you switch your Shopify Payments payout destination to your Shopify Balance account. Other account reviews or security holds can still affect payout timing.

If you use Multi-Currency Payouts, then adding or replacing a bank account for one currency can pause payouts to all of your payout accounts, not only payouts to the bank account that you added or changed.

After the pause is lifted, pending payouts start processing to your new bank account according to your regular [payout schedule](/manual/payments/shopify-payments/payouts/schedule-payouts). For example, if your settlement time is 2 business days, then your next payout is scheduled within 2 business days after the pause ends.

### Failed payouts

A payout can fail due to incorrect bank account information or problems such as a currency mismatch. If this happens, then you might not receive future payouts until you resolve the payout failure by following the instructions provided in the failed payout message. Always check your Shopify admin for notifications regarding failed payouts and follow provided instructions to resolve the issue, such as updating your bank account details.

### Bank account issues

Ensure that your bank account complies with [Shopify Payments’ requirements for your region](/manual/payments/shopify-payments/supported-countries). Problems such as an invalid account type or mismatched currency can lead to further delays.

If you recently [updated your bank account details](/manual/payments/shopify-payments/payouts/lower-or-missing-payouts) and haven't received your payout, then it could be due to the following factors:

* Processing time
* Pending payouts
* Errors in new bank account details
* Account review
* Minimum payout threshold
* Account currency mismatch with the new bank account 

### Issues with your tax details

Financial regulations require Shopify to verify appropriate tax identification numbers and other business details. If there are issues with your business information or tax identification numbers, then a hold on your payouts might be applied. Respond to any requests for updated information that you receive as notifications in your Shopify admin or in your store owner email.

### Reserves in Shopify Payments

When you use Shopify Payments, a portion of your funds might be held as a [reserve](/manual/payments/shopify-payments/payouts/reserves) to cover potential losses from disputes or refunds. While reserves allow you to continue accepting payments, they can affect the timing of when you receive the full amount of your earnings.

### Custom payout schedules

Your account might be placed on a custom payout schedule, which can result in extended payout periods ranging from 5 to 20 business days for [accounts that are deemed higher risk](/manual/payments/shopify-payments/onboarding/acceptable-business-practices#risk-standards-and-network-thresholds).

### Other factors affecting payout timing

The following are examples of other factors that can contribute to payout delays:

* **Adjusting your payout schedule:** If you change your payout frequency, such as changing it from daily to weekly, then pending payouts might be delayed until the next scheduled payout date.
* **Bank processing times:** After a payout is issued by the payment processor, banks need approximately 1-3 business days to process and transfer the funds to your account.
* **Weekends and public holidays:** Payouts aren't processed on weekends or public holidays. If your payout is scheduled during these times, then it's processed on the next business day.
* **Incomplete Shopify Payments setup:** Delays occur if you haven't completed the entire Shopify Payments setup, such as not adding a bank account. 
* **Negative balances:** If your account has a negative **Payout balance** amount due to refunds or chargebacks, then payouts are delayed until this balance is offset by future sales, or if applicable, until your bank account can cover the negative amount.

## Managing Shopify Payments payouts after deactivating your store

If you [deactivate your store](/manual/your-account/manage-orgs-and-stores/manage-pricing-plan/deactivate-store), then any pending Shopify Payments payouts are sent to your linked bank account according to your [preferred payout schedule](/manual/payments/shopify-payments/payouts/schedule-payouts). However, if a payout fails, then you can't troubleshoot the issue or change your payout settings, because you can't access your Shopify admin when your store is deactivated. To make any adjustments to your Shopify Payments settings or resolve failed payouts, you need to [reactivate your store](/manual/your-account/manage-orgs-and-stores/manage-pricing-plan/deactivate-store#reactivate-store).

Additionally, you [can't respond to chargebacks after your store is closed](/manual/payments/chargebacks/chargebacks-in-admin).
