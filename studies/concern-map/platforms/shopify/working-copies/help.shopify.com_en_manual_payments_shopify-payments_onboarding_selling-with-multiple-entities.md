# Selling with multiple entities

<aside class="note note-plan"><h4>Plan requirement</h4><p>Selling from multiple entities with Shopify Payments is available only for organizations on the Shopify Plus and Shopify Enterprise Commerce plan.</p>
</aside>

You can sell from multiple entities in a single store both online and [using Shopify POS](/manual/sell-in-person/getting-started/identify-your-pos-needs) with Shopify Payments. This lets you streamline your business operations, operate multiple legal entities within the same country, expand internationally, and manage payouts and orders in the same store.

Supported structures include online and retail entity splits, per-location entities, and separate business-to-business (B2B) and direct-to-consumer (D2C) entities. You must meet eligibility requirements, review compatibility considerations, and connect each entity to Shopify Payments before you can start selling.

## Regional availability of selling from multiple entities with Shopify Payments

To sell from multiple entities with Shopify Payments, your entities must be located in a [country where Shopify Payments is supported](/manual/payments/shopify-payments/supported-countries).

## Key benefits when selling from multiple entities with Shopify Payments

Selling from multiple entities with Shopify Payments offers the following benefits:

* **Simplified operations**: Operate online and retail entities around the world from a single store, with streamlined reporting.
* **Customer location**: Automatically detect and identify customer locations to provide a consistent shopping experience both online and in-store.
* **Domestic card processing**: Process transactions in an entity's domestic currency from a single store, avoiding international and foreign exchange fees.
* **Multiple domestic payout currencies**: Receive payouts to a domestic bank account for each of your entities, in the entity's domestic currency.
* **Same-country multi-entity support**: Sell from multiple legal entities within the same country. Your business can support separate entities for online and retail operations, a distinct entity for each retail location, or different entities for B2B and D2C sales.

## Requirements when selling from multiple entities with Shopify Payments

Before setting up Shopify Payments for multiple entities, review these requirements:

* Selling with multiple entities is available only with Shopify Payments.
* If you want to opt-in to selling from multiple entities with Shopify Payments, then you must use the [New Markets](/manual/markets/getting-started/overview) feature. If you're using New Markets, then you must [set up your business entities](/manual/your-account/business-entities) to start selling from multiple entities.

## Considerations when selling from multiple entities with Shopify Payments

Before setting up Shopify Payments for multiple entities, review these considerations:

* Your main Shopify account is considered your primary entity, and other Shopify accounts that you add are considered your secondary entities. Certain features such as adding a third-party payment method are available only for the primary entity. Learn more about [managing business entities](/manual/your-account/business-entities).
* If a primary entity is using a third-party payment processor, then you can't add Shopify Payments to your secondary entity. To add Shopify Payments to a secondary entity, you must deactivate the third-party payment provider. Learn more about [activating Shopify Payments](/manual/payments/shopify-payments/onboarding/account-setup#set-up-shopify-payments). To use Shopify Payments alongside the third-party provider on the primary entity, learn more about [using Shopify Payments with a third-party provider](/manual/payments/shopify-payments/using-shopify-payments-with-a-third-party-provider).
* You can offer subscription orders when you're selling from multiple entities with Shopify Payments, but all subscription payments are processed through your primary entity. International card fees and foreign exchange (FX) fees might apply depending on where your customer and your primary business entity are located. Learn more about [currency conversion fees with Shopify Payments](/manual/international/pricing/fees#conversion-rate-and-fee).
* Additional third-party payment methods are displayed only on checkouts and for markets associated with the primary entity, with the exception of PayPal.
* You can offer [Shop Pay Installments](/manual/payments/shop-pay-installments) on any of your entities that meet the [Shop Pay Installments eligibility requirements](/manual/payments/shop-pay-installments/eligibility), including secondary entities. Shop Pay Installments is activated and managed separately for each entity's Shopify Payments account. Newly added eligible entities might have Shop Pay Installments activated by default when Shopify Payments is activated.
* Post-purchase apps, such as cross-sell apps, might not work correctly with multi-entity setups. Purchases made through unsupported apps are routed to the primary entity, regardless of the customer's market. If you use post-purchase apps, then choose one of the following options:
      * Deactivate the app.
      * Configure the app to work only in markets served by the primary entity.
      * Manually reconcile your payouts.
* If you're [using managed markets](/manual/international/managed-markets), then you can't sell from multiple entities with Shopify Payments.
* If you're [using automated tax filing](/manual/taxes/shopify-tax/automated-filing), then you can't sell from multiple entities with Shopify Payments.
* If you migrate from a multi-shop setup to a multi-entity setup, then custom Shopify Payments rates aren't preserved. Entities that move to a different shop are assigned standard rates. If you want to restore your prior rates after migrating, then contact [Shopify Support](/manual/your-account/contact-shopify-support).

## Payment method requirements for multi-entity setups

For certain payment methods to be available, the entity processing the transaction must have the required currency set as its **Default** payout currency in Shopify Payments, not just as an available payout currency.

For example, Interac payments in Canada require the Canadian entity to have CAD set as the **Default** payout currency. Having CAD as a secondary payout currency is insufficient.

Payment methods such as Interac are available only when the customer is checking out in the required currency and the entity processing the sale has that currency as its default payout currency. The processing currency is what the customer pays in, whereas the payout currency is what you receive. Your entity's **Default** payout currency affects payment method availability, not just whether the processing currency is available as a payout option.

Learn more about [multi-currency payouts](/manual/payments/shopify-payments/store-currency/payouts-in-multiple-currencies) and [understanding store and payout currencies](/manual/payments/shopify-payments/store-currency/understanding-store-and-payout-currencies).

## Entity selection for transactions

For POS transactions, the physical location where the POS device is logged in determines the entity. Each POS location maps to a specific business entity during setup, and staff can't manually change the entity during checkout. The entity must be in the same country as the POS location.

For online transactions, your market settings and the customer's shipping or billing location determine the entity. Configure this through your Markets settings in Shopify admin, which follows standard market-based entity assignment rules. Learn more about [managing markets](/manual/markets/getting-started/managing-markets).

With Retail markets, you can configure different entities for online and POS transactions within the same country. Online orders can process through your primary entity, whereas POS orders can process through country-specific retail entities. Learn more about [Retail markets considerations](/manual/sell-in-person/markets/overview#considerations).

### Currency in Shopify POS when you use Retail markets

If your store has only your primary business entity, then Shopify POS transactions use your store’s default currency. Your market settings still control catalog and pricing for retail, but they don’t switch POS transactions to another currency without a separate entity for that country and currency.

If you have multiple entities and use Retail markets, then each retail location is tied to an entity. The currency for sales processed using Shopify Payments at that location comes from that entity’s default payout currency, which must meet the [country and currency requirements](/manual/sell-in-person/getting-started/setup-payment-method/compliance#requirements) for the country where the location operates.

To sell in more than one currency across retail locations in different countries with Shopify Payments activated, you need multiple entities. Selling with multiple entities is available only on the [Shopify Plus plan](/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan) and [Shopify Enterprise Commerce plan](https://www.shopify.com/enterprise-commerce).

## Add a Shopify Payments account to a business entity

<aside class="note"><h4>Note</h4><p>If you want to add a business entity to your Shopify account, then learn more about <a href="/en/manual/your-account/business-entities">managing business entities</a>.</p>
</aside>

If you have multiple business entities set up in your Shopify admin, then you can connect your existing business entities to Shopify Payments. You can also change the market that your business entity and the connected Shopify Payments account are associated with. You can choose which Shopify Payments account and customer transaction are processed in depending on their location.

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments).


2. In the **Shopify Payments** section, click **Add Shopify Payments account**.
3. Select the business entity that you want to connect to your Shopify Payments account, and then click **Continue**.
4. In the **Complete account setup** section, click **Submit details**.
5. In the **Set up Shopify Payments** section, choose your business account type. If the business entity that you're adding Shopify Payments to is listed as a **Registered business**, then this field is automatically populated with the business type that you have listed in your [Organization settings](/manual/organization-settings).

## Remove an incomplete or deactivated Shopify Payments account

You can remove a deactivated business entity, or a business entity that isn't fully set up, from the Shopify Payments section of your Shopify admin. If an account is deactivated, then the **Activate** label displays for the business entity in your Shopify admin. If the business entity isn't fully set up, then the **Complete setup** label displays for the business entity in your Shopify admin.

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments).


2. In the **Payment providers** section, click **Shopify Payments**.
3. In the **Shopify Payments account** section, take one of the following actions:
   * If an account has the **Setup incomplete** label, then click <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg" alt="reset" class="admin-icon" />, and then click **Remove from list**.
   * If an account has the **Activate** label, then click <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg" alt="reset" class="admin-icon" />, and then click **Remove from list**.

## Managing the business entity and Shopify Payments account connected to a region market

When you have multiple business entities, you can choose which entity's Shopify Payments account processes transactions for each region market's online and retail sales. Learn more about [creating and customizing markets](/manual/markets/getting-started/managing-markets).

You can connect any of your business entities to process transactions for online and retail sales, including multiple entities within the same country. For example, if you have business entities in Australia and the United States, then you can create regional markets for each country to ensure the domestic entity processes the sales. If you have multiple entities in the same country, such as separate online and retail entities, then you can assign each to the appropriate market.

Online and retail transactions are associated with the same region market and entity, and have the same catalog. For example, if you have a region market set up for Canada, then your online and retail sales share the same catalog. If you add a UK region market, then your UK online and retail sales can have a different catalog from Canada, but your UK online and retail sales must share the same catalog.

## Managing a retail business connected to a region market {#managing-retail}

When managing retail businesses across multiple regions, ensure that you connect your business entities to the appropriate region markets in Shopify.

### Set up separate entities for each country with retail locations

To manage retail businesses across multiple regions, you must have a separate entity for each country with retail locations, including pop-up locations.

Each of your entities must be in a country where Shopify Payments for POS is available. Learn more about the [availability of Shopify Payments for POS](/manual/sell-in-person/getting-started/setup-payment-method/shopify-payments-pos#supported).

#### Example

A US-based merchant sells online globally. The merchant already has a UK region market set up for online sales. They want to run a 5-day retail pop-up in the UK or a permanent retail location in the UK.

**Step 1: Configure markets**

To enable the UK retail, the merchant has the following two options:

* **Option A**: The merchant can use the existing UK market for retail where the same UK market powers both online and retail sales. Product prices appear in GBP at the UK retail location. The merchant can set manual exchange rates for the UK region market to avoid price fluctuations in-store.
* **Option B:** The merchant can create a separate UK retail market with manual exchange rates. This keeps retail prices stable, while allowing dynamic exchange rates for online sales.

**Step 2: Configure business entities**

To accept in-person payments through Shopify Payments for UK retail, the merchant must do the following:

* Add a UK business entity in Shopify.
* Set up a UK Shopify Payments account.

### Considerations when connecting a retail business entity and a region market

* You can't manage multi-currency exchanges when selling from multiple entities with retail locations.
* Shopify gift cards are supported only in the shop currency.
* [Buy X get Y discounts](/manual/discounts/discount-types/buy-x-get-y) are available only for retail locations using [POS Pro](/manual/sell-in-person/getting-started/identify-your-pos-needs#choose-your-shopify-pos-app-subscription) for multi-entity retail locations. If you're using [POS Lite](/manual/sell-in-person/getting-started/identify-your-pos-needs), then these discounts can be applied only in your online store checkout.
* [Automatic discounts](/manual/discounts/discount-methods/automatic-discounts) require POS Pro to be activated for retail locations. For locations using POS Lite, automatic discounts apply only to online store transactions.

### Connect your business entity to a market

When you add Shopify Payments to a business entity, you must connect the entity to a market to have orders processed through the correct entity.

#### Steps:

1. From your Shopify admin, go to [**Markets**](https://admin.shopify.com/markets).


2. Select the market that you want to connect a business entity to.
3. Optional: Click **Add market** to set up a new market. Learn more about [creating markets](/manual/markets/getting-started/managing-markets).
4. Click the <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/PlusCircleIcon.svg" alt="reset" class="admin-icon" /> icon on **Business entity**.
5. Select the business entity that you want to connect to the chosen market.
6. Click **Save**.

## Selling from multiple entities {#selling-multiple-entities}

Setting up multi-entity selling for entities in the same country involves 3 stages:

1. [Registering your entities](/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities#registering-entities).
2. [Connecting each entity to Shopify Payments](/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities#connect-shopify-payments-to-entity)
3. [Assigning each entity to markets](/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities#assign-entities-to-markets).

### Unsupported features when selling with multiple entities

The following features aren't supported when selling from multiple entities:

* **Entity routing by shipping address**: You can't configure a single store to route orders to different entities based on where a customer ships to. Entity assignment is controlled through market configuration, not shipping address.
* **Marketplace or commission structures**: You can't use multi-entity to split payments between businesses or manage commission-based arrangements between separate business owners.
* **B2B rate consolidation for existing shops**: You can't collapse or consolidate rates across existing B2B shops into a multi-entity structure.

### Register your business entities {#registering-entities}

Each legal entity that you want to sell from must be added to your organization settings before you can connect it to Shopify Payments.

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Organization**](https://admin.shopify.com/settings/organization-details).

2. Add each business entity that you want to sell from. Learn more about [adding business entities](/manual/your-account/business-entities).

### Connect Shopify Payments to each entity {#connect-shopify-payments-to-entity}

After adding your entities, connect a Shopify Payments account to each one. Each entity has its own Shopify Payments account, payout currency, and bank account, so you need to complete this process for every entity that you want to activate.

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Payments**](https://admin.shopify.com/settings/payments).


2. In the **Shopify Payments** section, click **Add Shopify Payments account**.
3. Select the business entity, and then complete the account setup.
4. Complete identity verification if prompted.
5. After connecting your entity, repeat the connection process to Shopify Payments for all other business entities.

### Assign entities to markets {#assign-entities-to-markets}

Markets control which entity processes transactions for a given region. You can assign entities to new or existing markets, and configure both online and POS sales through the same market. Until you assign an entity to a market, that entity won't process any transactions.

#### Steps:

1. From your Shopify admin, go to [**Markets**](https://admin.shopify.com/markets).


2. Optional: If you're adding a new POS location, [add the location with its address](/manual/markets/getting-started/managing-markets) before proceeding.
3. Click **Add market**, or select an existing market to configure.
4. Select the POS locations or online store that you want to include in the market.
5. Assign the business entity and its associated Shopify Payments account to the market.
6. Click **Save**.
7. After assigning an entity to a market, repeat the process to connect all other entities to markets. 

## Troubleshooting payment method issues

If a payment method isn't displaying for your multi-entity setup, then the entity likely doesn't have the local currency set as its **Default** payout currency. For example, Interac in Canada requires the processing entity to have CAD as its default payout currency, not just as an available option.

The key difference between processing currency and payout currency in multi-entity setups is that processing currency is what the customer pays in, whereas payout currency is what you receive. For payment method availability, the entity's **Default** payout must match the processing currency for certain domestic payment methods to be offered to customers.

Learn more about [supported payout currencies](/manual/payments/shopify-payments/store-currency/supported-payout-currencies) for your region.
