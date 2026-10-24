# Backup region in Markets

The backup region determines the experience for customers who don't match any of your active markets. Every store is required to have a backup region configured for use with Markets. This backup region isn't a market. Instead, it's a setting that points to a country within one of your active markets. The customer experience for the backup region is based on the settings of the market that contains the backup region country.

For example, if your backup region is set to the United States and the United States is in your North America market, then customers who don't match any market receive the North America market experience (currency, language, theme customizations), but they can't check out.

The backup region experience is displayed in the following situations:

* A customer visits your online store from a country that isn't included in any of your active markets. For example, you have active markets for the United States and Canada, and a customer from Australia visits your store.
* A B2B company location doesn't have an address and isn't part of a specific market, or a market that includes all company locations in all regions.
* A company location has an address in a country that isn't covered by a market matching their customer type. For example, you have active markets for the United States and for company locations in the United States, but a company location has an address in Canada.

When a customer receives the backup region experience, they can browse your store and view products, but they can't complete a purchase. The backup region determines the currency, language, and theme customizations displayed to these customers.

## Configure your backup region

<aside class="note"><h4>Note</h4><p>The backup region must be a country that&#39;s contained within an active market. If you deactivate the market that contains your backup region country, then you need to update your backup region to a country in a different active market.</p>
</aside>

Your backup region is automatically set to your store's home country when you create your store. You can change it to any country that's contained within an active market.

#### Steps:

1. From your Shopify admin, go to **Settings** > [**General**](https://admin.shopify.com/settings/general).

2. In the **Backup Region** section, select the region that you want to display to customers who don't match any existing market.
3. Click **Save**.

## Choosing a backup region

Consider the following when choosing your backup region:

* **Your primary audience**. Set the backup region to the country that represents your most common unmatched visitor. For example, if most of your traffic outside your active markets comes from the United States, then set the backup region to the United States.
* **Currency and language**. The backup region determines the currency and language displayed to unmatched customers. Choose a country whose currency and language make sense as a default. For many stores, this is the store's home country.
* **Theme customizations**. The theme customizations that are configured for the market containing the backup region country are displayed to unmatched customers. If that market has a localized banner or region-specific content, then those customizations are visible to all unmatched visitors.

## Backup region and the domestic market

When you first create your store, your domestic market is created automatically with your home country, and the backup region is set to that same country. This means unmatched customers receive the same experience as your domestic customers, without the ability to complete a checkout.

If you change your backup region to a different country or market, then the default browsing experience for unmatched customers changes accordingly.
