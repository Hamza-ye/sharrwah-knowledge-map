# Managing Multi-Currency Payouts with Shopify Payments

If you have an international customer base, then handling payouts in multiple currencies can help you optimize the payment process. With Multi-Currency Payouts, you can add multiple bank accounts to receive payouts in different currencies and avoid currency exchange fees.

To use Multi-Currency Payouts, your store must meet specific plan and location requirements. You can add one bank account for each supported payout currency available for your region and Shopify plan, and fees apply when you receive payouts in non-domestic currencies.

## Requirements for Multi-Currency Payouts

Before you can use Multi-Currency Payouts, your store must meet specific plan, location, and bank account requirements. If you meet all eligibility requirements, then you can add one bank account for each supported payout currency available for your region and Shopify plan.

### Plan requirements

Multi-Currency Payouts are available only on certain Shopify plans. If your store is on a plan that doesn't support Multi-Currency Payouts, then you can still sell in multiple currencies, but all payouts are converted to your domestic currency. 

If your store is on the Basic, Grow, or Shopify plan, then you aren't eligible for Multi-Currency Payouts. You can sell in multiple currencies, but you receive payouts only in your domestic currency. A currency conversion fee applies when customers pay in a different currency. Learn more about [selling in multiple currencies](/manual/payments/shopify-payments/store-currency/selling-and-getting-paid-in-different-currencies).

If your store is on the Basic or Grow plan, and you're based in Canada, then you can choose USD as your default payout currency instead of CAD. A 1.5% payout fee applies. Learn more about [currency conversion fees](/manual/payments/shopify-payments/store-currency/supported-payout-currencies#shopify-payments-payout-conversion).

<table>
  <caption>Shopify plan eligibility for Multi-Currency Payouts</caption>
  <thead>
    <tr>
      <th scope="col">Plan</th>
      <th scope="col">Multi-Currency Payouts available</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row">Basic</td>
      <td>No, domestic currency only</td>
    </tr>
    <tr>
      <td scope="row">Grow</td>
      <td>No, domestic currency only</td>
    </tr>
    <tr>
      <td scope="row">Shopify</td>
      <td>No, domestic currency only</td>
    </tr>
    <tr>
      <td scope="row">Advanced</td>
      <td>Yes, one bank account per supported payout currency</td>
    </tr>
    <tr>
      <td scope="row">Shopify Plus</td>
      <td>Yes, one bank account per supported payout currency</td>
    </tr>
  </tbody>
</table>

### Additional requirements

Review the following requirements before setting up Multi-Currency Payouts:

* Your store must be on the Advanced or Shopify Plus plan.
* You must have a business entity set up in a region that's eligible to use Multi-Currency Payouts. Learn more about [selling with multiple entities](/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities).
* You must have a bank account set up in a region that's [eligible to use Multi-Currency Payouts](#multi-currency-payouts-eligible-regions).
* You must be listed as the store owner to activate Multi-Currency Payouts.

### Eligible regions {#multi-currency-payouts-eligible-regions}

Multi-Currency Payouts are available only for merchants located in certain regions. Payouts that you receive in your domestic currency aren't charged a Multi-Currency Payout fee. Each additional currency that you add is subject to a fee depending on your plan and region.

To find out what your domestic payout currency is, refer to the [payouts page for your region](/manual/payments/shopify-payments/supported-countries). Learn more about [supported payout currencies](/manual/payments/shopify-payments/store-currency/supported-payout-currencies).

<table>
    <caption>Domestic and international currencies that you can use to receive payouts in</caption>
    <thead>
        <tr>
            <th scope="col">Store location</th>
            <th scope="col">Bank account locations</th>
            <th scope="col">Additional supported payout currencies</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row">Australia</td>
            <td>Australia, Canada (CAD only), Eurozone countries (EUR only), New Zealand (NZD only), United Kingdom (GBP only), United States (USD only)</td>
            <td>CAD, CHF, DKK, EUR, GBP, HKD, JPY, NOK, NZD, SEK, SGD, USD</td>
        </tr>
        <tr>
            <td scope="row">Austria, Belgium, Bulgaria, Croatia, Cyprus, Czechia, Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece, Hungary, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovenia, Spain, Sweden, Switzerland</td>
            <td>Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece, Hungary, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland, United Kingdom, United States (USD only)</td>
            <td>AUD, CAD, CHF, CZK, DKK, GBP, HKD, HUF, JPY, NOK, NZD, PLN, RON, SEK, SGD, USD, ZAR</td>
        </tr>
        <tr>
            <td scope="row">Canada</td>
            <td>Canada, United States</td>
            <td>USD</td>
        </tr>
        <tr>
            <td scope="row">Hong Kong</td>
            <td>Hong Kong</td>
            <td>EUR, GBP, JPY, USD</td>
        </tr>
        <tr>
            <td scope="row">Singapore</td>
            <td>Singapore</td>
            <td>EUR, GBP, JPY, USD</td>
        </tr>
        <tr>
            <td scope="row">United Arab Emirates (Shopify Plus only)</td>
            <td>United Arab Emirates</td>
            <td>USD</td>
        </tr>
        <tr>
            <td scope="row">United Kingdom</td>
            <td>Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece, Hungary, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland, United Kingdom, United States (USD only)</td>
            <td>AUD, CAD, CHF, CZK, DKK, EUR, HKD, HUF, JPY, NOK, NZD, PLN, RON, SEK, SGD, USD, ZAR</td>
        </tr>
        <tr>
            <td scope="row">United States</td>
            <td>United States (USD), Australia (AUD), Canada (CAD), Europe (EUR), United Kingdom (GBP)</td>
            <td>AUD, CAD, EUR, GBP</td>
        </tr>
    </tbody>
</table>

### Bank account requirements

The bank accounts that you can use to receive payouts depend on where you're located and the currency of the account.

<table>
  <caption>Bank account requirements by business entity location</caption>
  <thead>
    <tr>
      <th scope="col">Business entity location</th>
      <th scope="col">Supported bank account locations</th>
      <th scope="col">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row">Europe</td>
      <td>Europe (IBAN), United States (USD only)</td>
      <td>Bank accounts must have a supported International Bank Account Number (IBAN) that can pay out in the selected currency. USD can be added with a US-based bank account or a European IBAN.</td>
    </tr>
    <tr>
      <td scope="row">United Kingdom</td>
      <td>United Kingdom (GBP, USD), Europe (IBAN), United States (USD only)</td>
      <td>GBP payouts can only be issued to a UK-based bank account. USD can be added with a UK IBAN, a European IBAN, or a US-based bank account.</td>
    </tr>
    <tr>
      <td scope="row">Australia</td>
      <td>Australia, Canada (CAD only), Eurozone countries (EUR only), New Zealand (NZD only), United Kingdom (GBP only), United States (USD only)</td>
      <td>AUD, CHF, DKK, HKD, JPY, NOK, SEK, and SGD payouts require an Australia-based bank account. CAD, EUR, GBP, NZD, and USD payouts can use an Australia-based bank account or a bank account in the currency's supported region. If using a non-Australia bank account for EUR payouts, then the bank account must be in a supported Eurozone country.</td>
    </tr>
    <tr>
      <td scope="row">Canada</td>
      <td>Canada, United States</td>
      <td>You can receive CAD and USD payouts using a Canadian bank account, or USD payouts using a US-based bank account.</td>
    </tr>
    <tr>
      <td scope="row">Hong Kong</td>
      <td>Hong Kong</td>
      <td>All payouts, including HKD, USD, EUR, GBP, and JPY, must be issued to a Hong Kong bank account.</td>
    </tr>
    <tr>
      <td scope="row">Singapore</td>
      <td>Singapore</td>
      <td>All payouts, including SGD, USD, EUR, GBP, and JPY, must be issued to a Singapore-based bank account. Foreign bank accounts, including European IBAN, UK-based, and Japan-based bank accounts, aren't supported for Singapore Shopify Payments accounts.</td>
    </tr>
    <tr>
      <td scope="row">United Arab Emirates</td>
      <td>United Arab Emirates</td>
      <td>All payouts, including AED and USD, must be issued to a United Arab Emirates-based bank account.</td>
    </tr>
    <tr>
      <td scope="row">United States</td>
      <td>United States (USD), Australia (AUD), Canada (CAD), Europe (EUR), United Kingdom (GBP)</td>
      <td>USD payouts are issued to a United States-based bank account. Non-USD payouts, such as AUD, CAD, EUR, and GBP payouts, require a bank account outside the United States in the corresponding currency's region. EUR payouts require an IBAN from a supported SEPA country; IBANs issued in Monaco (MC), San Marino (SM), Andorra (AD), and Vatican City (VA) aren't supported.</td>
    </tr>
  </tbody>
</table> 

## Set up Multi-Currency Payouts

If your store is on the Advanced plan or the Shopify Plus plan in an eligible Shopify Payments region, then you can set up more than one bank account with Multi-Currency Payouts. You can add a secondary payout account in a non-domestic currency, and orders paid for in that currency are paid out to that bank account. With this setup, you can receive payouts in that currency without incurring foreign exchange, or FX, fees.

### Add a bank account for Multi-Currency Payouts {#add-multi-currency-bank}

For businesses located in regions such as Canada, where both CAD and USD are commonly used, you can link two bank accounts to receive payouts in each currency. You can add a bank account to receive payouts in a non-domestic currency.

For Shopify Payments accounts in Singapore, Hong Kong, and the United Arab Emirates, payout accounts for non-domestic currencies must still be based in the store's domestic region. For example, a Singapore business adding a EUR payout account must use a Singapore-based bank account that can receive EUR payouts. The bank account form displays the required domestic bank details for Singapore instead of IBAN fields.

<aside class="note"><h4>Note</h4><p>If you add a payout bank account more than 24 hours after completing your Shopify Payments setup, then your payouts are temporarily paused for 3–5 business days. If you use Multi-Currency Payouts, then adding a bank account for a new currency can pause payouts to all of your payout accounts, not only payouts to the new bank account.</p>
</aside>

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments).


2. In the **Shopify Payments** section, click **Manage**.
3. In the **Payout accounts** section, click **Add bank account**.
4. In the **Payout currency** section, select the currency of your bank.
5. In the **Bank account country** section, enter the country that your bank account is located in.
6. In the **Account owner** section, enter the name that's listed on the bank account that you want to add.
7. Add your bank account information. The information that you enter depends on the country that your bank account is located in. For example, if you select Germany as the country your bank account is located in, then you can add an IBAN.
8. Click **Next** to add the bank account.

### Set a default bank account for payouts

If you use Multi-Currency Payouts and add additional bank accounts to your Shopify Payments account, then you must set one of the bank accounts as your default. If you don't set a default account, then the bank account that you added during the setup of Shopify Payments is your default account for payouts.

If you don't have a bank account set up in the currency that was used to pay for an order, then the payout is sent to your default bank account.

The following example demonstrates how payouts are routed:

<table>
  <caption>Example: Payout routing for a UK-based merchant with GBP default and USD secondary accounts</caption>
  <thead>
    <tr>
      <th scope="col">Order currency</th>
      <th scope="col">Bank account used</th>
      <th scope="col">Currency conversion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row">GBP (domestic)</td>
      <td>GBP bank account</td>
      <td>No conversion needed</td>
    </tr>
    <tr>
      <td scope="row">USD</td>
      <td>USD bank account</td>
      <td>No conversion needed</td>
    </tr>
    <tr>
      <td scope="row">CAD (no account)</td>
      <td>GBP bank account (default)</td>
      <td>CAD converted to GBP</td>
    </tr>
  </tbody>
</table>

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments).


2. In the **Shopify Payments** section, click **Manage**.
3. In the **Payout accounts** section, click <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg" alt="Horizontal menu" class="admin-icon" /> next to the bank account that you want to set as the default.
4. Click **Set default**.

### Replace a bank account

You can replace a bank account from your Shopify admin at any time:

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments).


2. In the **Shopify Payments** section, click **Manage**.
3. In the **Payout accounts** section, click <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg" alt="Horizontal menu" class="admin-icon" /> next to the bank account that you want to replace.
4. In the **Confirm old bank account** section, enter the details of the account that you want to replace.

   If you can't complete the **Confirm old bank account** step because the account is closed or the account details are unknown or incorrect, then refer to [Troubleshooting bank account changes](/manual/payments/shopify-payments/configuring-shopify-payments#troubleshoot-bank-account-changes).
5. In the **Bank account** section, enter the **Account owner name** and bank account details for the account that you want to add. You can't change the country or currency of the account that you want to add. The account that you want to add must be in the same currency as the account that you're replacing.
6. Click **Next**.

### Delete a bank account

To stop receiving payouts in a specific currency, you can delete the payout account from your Shopify admin.

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments).


2. In the **Shopify Payments** section, click **Manage**.
3. In the **Payout accounts** section, click <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg" alt="Horizontal menu" class="admin-icon" /> next to the bank account that you want to delete.
4. In the **Delete currency** dialog, review the account where future payouts in this currency are deposited. Payouts are deposited into your default account if an account in that currency isn't added.
5. Click **Confirm** to delete the account.

## Considerations for Multi-Currency Payouts

Several factors affect how your payments, refunds, and chargebacks are processed when you use Multi-Currency Payouts.

### Supported currencies and bank accounts

Each supported currency must have a dedicated bank account. For example, your bank account in CAD currency must be located in Canada, but your bank account in USD currency can be located in either Canada or the United States.

### Payout holds after adding or replacing bank accounts

If you add a payout bank account more than 24 hours after completing your Shopify Payments setup, then your payouts are temporarily paused for 3–5 business days. Replacing an existing bank account also temporarily pauses your payouts for 3–5 business days.

This pause applies to all of your Shopify Payments payouts, including payouts to bank accounts that weren't added or changed. After the pause ends, pending payouts start processing according to your regular [payout schedule](/manual/payments/shopify-payments/payouts/schedule-payouts).

### Handling orders in non-account currencies

If you receive an order in a currency that you don't have a specific bank account for, then the funds are converted to your default account's currency. A [currency conversion fee](/manual/international/pricing/exchange-rates) applies to this conversion.

### Refunds in multiple currencies

Refunds are processed in the same currency as the original order. The refund is deducted from the bank account in that currency.

If you don't have a bank account in the original order's currency, then the refund is deducted from your default bank account in your domestic currency.

For example, if you delete the bank account after the order is placed, then the refund is deducted from your default account.

### Chargebacks in multiple currencies

Chargebacks are handled in the same currency as the original order. If a customer disputes a charge, then the chargeback amount is deducted from the bank account in that currency.

If you don't have a bank account in the original order's currency, then the chargeback is deducted from your default bank account. A currency conversion fee might apply.

Learn more about [refunding orders](/manual/fulfillment/managing-orders/refunding-orders) and [managing chargebacks](/manual/payments/chargebacks).

## Multi-Currency Payout fees {#multi-currency-payout-fees}

Multi-Currency Payout fees apply when you receive payouts in a currency that isn't your domestic currency. Your domestic currency is determined by your Shopify Payments region.

<table>
  <caption>When Multi-Currency Payout fees apply</caption>
  <thead>
    <tr>
      <th scope="col">Scenario</th>
      <th scope="col">Multi-Currency Payout fee</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row">Payout to your domestic currency bank account</td>
      <td>No fee</td>
    </tr>
    <tr>
      <td scope="row">Payout to a non-domestic currency bank account</td>
      <td>Fee applies based on plan and region</td>
    </tr>
  </tbody>
</table>

For example, if you're based in Canada and your domestic currency is CAD:

* Payouts to your CAD bank account aren't charged a Multi-Currency Payout fee.
* Payouts to your USD bank account are charged a Multi-Currency Payout fee.

<aside class="note"><h4>Note</h4><p>The Multi-Currency Payout fee is based on the payout currency, not whether a currency conversion occurs. Even if a customer pays in USD and you receive a payout in USD, the fee applies if USD isn&#39;t your domestic currency.</p>
</aside>

### Fee rates by region

The fee rate depends on your Shopify plan and store location. If your store is on the Shopify Plus plan, then you pay a lower fee rate than merchants on the Advanced plan.

<table>
  <caption>Multi-Currency Payout fee rates by region and plan</caption>
  <thead>
    <tr>
      <th scope="col">Region</th>
      <th scope="col">Advanced plan</th>
      <th scope="col">Shopify Plus plan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row">Global regions</td>
      <td>1.5%</td>
      <td>1%</td>
    </tr>
    <tr>
      <td scope="row">Canada</td>
      <td>1.5%</td>
      <td>1.25%</td>
    </tr>
    <tr>
      <td scope="row">United States</td>
      <td>1%</td>
      <td>0.75%</td>
    </tr>
  </tbody>
</table>

Learn more about [supported payout currencies](/manual/payments/shopify-payments/store-currency/supported-payout-currencies).

## Legal and financial considerations

Before you sell in multiple currencies or set up Multi-Currency Payouts, consult a legal or tax expert to understand any potential implications related to international commerce. Consulting a legal or tax expert helps you understand applicable laws and regulations and make informed decisions about your international sales strategy.
