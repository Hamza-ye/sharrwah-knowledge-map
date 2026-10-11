# Protecting your store from selling to bots

<aside class="note note-plan"><h4>Plan requirement</h4><p>The bot protection feature is available only for merchants on a Shopify Plus plan.</p>
</aside>

You can activate bot protection to help prevent product inventories from primarily being sold to auto-checkout bots. Bot protection acts as a fairness control by blocking known bots from your checkout, and slowing down bot activity so that your customers have the opportunity to purchase scarce products during flash sales.

If you want to request the bot protection feature for your online store, then contact Shopify Plus Support.

Learn more about [understanding bots at Shopify](/manual/intro-to-shopify/bots).

## Considerations for using bot protection {#considerations}

Review the following requirements and limitations before using the bot protection feature:

* This feature is meant only to limit the effectiveness of auto-checkout bots and isn't meant to combat forms of fraud that are related to bot activity.
* Bot protection is available in your Shopify admin only after it's been activated. To activate bot protection for your online store, contact Shopify Plus Support.
* The bot protection feature is available only for the **Online Store** sales channel. Bot protection for other [sales channels](/manual/online-sales-channels) isn't supported.
* Bot protection can be applied to up to 500 individual products, or to all the products in your store. You can’t add bot protection to a collection of products.
* Only one bot protection event can be scheduled at a time.
* The maximum duration for a bot protection event is 60 minutes.
* After a bot protection event is active, it can't be edited. It can only be deactivated.
* When scheduling a bot protection event, you must select a checkpoint challenge.

## Bot protection options

When scheduling bot protection, you can choose the challenge option that you want to activate. You have the following options available:

* [reCAPTCHA](https://developers.google.com/recaptcha), powered by Google.
* [hCaptcha](https://www.hcaptcha.com/), powered by Intuition Machines Inc. hCaptcha provides additional customizable challenge settings, including a choice between selecting a correct image from a set, or drawing a box around an object. You can also choose to include additional custom skill-testing questions and answers written by you.

The setting to stop bots from auto-completing the checkout is active by default, which can help prevent products with limited inventory from quickly selling out. However, you can choose to deactivate this setting.

## Schedule bot protection {#schedule-bot-protection}

You can schedule bot protection to start at a specific time and date. Your scheduled event begins at the time you select according to your [store’s time zone](/manual/intro-to-shopify/initial-setup/setup-business-settings#set-or-change-your-store-time-zone), not your browser's time zone.

The maximum duration for a bot protection event is 60 minutes. To maximize the effectiveness of bot protection, you can schedule it at the same time as your flash sale. When you schedule bot protection, you can choose to protect all published products, or you can select up to 500 individual products that you want to protect.

#### Steps:

1. If you haven't already activated bot protection for your online store, then contact Shopify Plus Support to activate the feature.
2. From your Shopify admin, go to **Settings** > [**Bot protection**](https://admin.shopify.com/settings/bot-protection).
3. Click **Schedule protection**.
4. Enter a title, date, start time, and duration.
5. In the **Bot protection options** section, set your bot protection preferences:
    1. Select either **reCAPTCHA** or **hCaptcha**. If you select **hCaptcha**, then configure your additional challenge settings.
    2. Optional: Click **Preview** to open an example of the checkpoint challenge in your online store.
    3. Optional: If you want to allow bots to auto-complete checkouts, then deselect **Don't allow bots to auto-complete checkouts**.
6. In the **Products** section, select which products you want to protect:
    * If you want to protect all published products, then select **Protect all products that have been published**.
    * If you want to protect specific products, then select **Select specific products to protect**, and then use the **Search Protect products** field to add your products to the list of protected products. You can add a maximum of 500 individual products.
7. Click **Submit**.

## Customize the checkpoint page {#customize-checkpoint-page}

You can customize the look of your checkpoint page by editing your theme code.

<aside class="note"><h4>Note</h4><p>Checkpoint only uses the default <code>checkpoint.liquid</code> template. Using alternate templates isn&#39;t supported.</p>
</aside>

Learn more about [customizing your checkout](/manual/checkout-settings/customize-checkout-configurations).

#### Steps:

1. From your Shopify admin, go to [**Online Store**](https://admin.shopify.com/themes).


2. Click the <img src="https://cdn.shopify.com/shopifycloud/help-center/manual/admin-icons/MenuHorizontalIcon.svg" alt="Horizontal menu" class="admin-icon" /> button > **Edit code**.
3. If this is your first time customizing the checkpoint page, then create a checkpoint template:
   1. Click **Add a new template**.
   2. Select **checkpoint**.
4. In the **Templates** section, click **checkpoint.liquid**.
5. Make changes to the template code.
6. Click **Save**.

You can preview your custom checkout page by creating a new event and clicking **Preview what your customers will see**.

## Deactivate bot protection {#deactivate-bot-protection}

Bot protection deactivates automatically when the scheduled time ends. If enough customers have already purchased from your store, then you can manually deactivate bot protection. To determine this, you need to track your order volume and decide whether you want to deactivate bot protection.

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Bot protection**](https://admin.shopify.com/settings/bot-protection).
2. Click the active event.
3. Click **Deactivate**.
