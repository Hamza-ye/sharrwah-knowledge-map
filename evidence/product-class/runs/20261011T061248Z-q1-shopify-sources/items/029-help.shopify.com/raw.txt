# Managing high-risk orders with Shopify Flow

[Shopify Flow](/manual/shopify-flow) is a free ecommerce automation platform that enables you to automate tasks and processes within your Shopify store and across your apps. You can use Shopify Flow to automate certain tasks in your Shopify admin, such as your management of high-risk orders.

If you receive a banner in your Shopify admin about installing **Shopify Flow**, then you can click **Install Flow** and immediately activate a workflow that captures payments on low-risk and medium-risk orders automatically. If not, then you can [install Shopify Flow](https://apps.shopify.com/flow) from the Shopify App Store and then either use a pre-made template or create your own workflow.

## Before using Shopify Flow to manage high-risk orders {#before-flow}

When you make or edit a workflow to manage high-risk orders, ensure that you use the [Order risk analyzed](/manual/shopify-flow/reference/triggers/order-risk-analyzed) trigger instead of the [Order created](/manual/shopify-flow/reference/triggers/order-created) trigger. This is because fraud analysis takes some time to process after an order is created. Workflows that start with the **Order risk analyzed** don't run immediately after an order is created, and instead are triggered when the fraud analysis is completed on an order.

After you activate a workflow that determines whether a payment should be captured, ensure that [credit card authorization and capture](/manual/payments/payment-authorization) is set to [capture manually](/manual/payments/payment-authorization#set-up-manual-payment-capture) in your settings. Workflows that manage capturing payments don't function if automatic capture is activated.

## Setting up Shopify Flow workflows  {#setting-up-workflows}

You can automate common tasks performed in Shopify by [creating workflows](/manual/shopify-flow/create/create-workflow) in Shopify Flow that have triggers, conditions, and actions. To use Shopify Flow to manage high-risk orders, you can set up [commonly used workflows](/manual/shopify-flow/getting-started/workflow-examples#risk). For example, you can [capture payment if the order is not high risk](/manual/fulfillment/managing-orders/protecting-orders/shopify-flow#not-high-risk), or [cancel and restock high-risk orders](/manual/fulfillment/managing-orders/protecting-orders/shopify-flow#cancel-and-restock). These workflows operate based on information from Shopify's [fraud analysis](/manual/fulfillment/managing-orders/protecting-orders/fraud-analysis).

<aside class="note sidekick"><h4>Sidekick</h4><p>You can <a href="https://admin.shopify.com/sidekick">ask Sidekick</a> to create a workflow in Shopify Flow to manage high-risk orders. Sidekick creates a draft for you to review and activate. Use a prompt such as <kbd>Create a workflow with the Order risk analyzed trigger that tags high-risk orders for review</kbd>.</p>
</aside>

## Capture an order that is not high fraud risk {#not-high-risk}

This workflow captures payment for risk and medium-risk orders, and avoids capturing payment for high-risk orders. [You can install the template automatically](https://admin.shopify.com/apps/flow/web/editor/templates/f7f8e7d0-c7b4-4ea0-90a0-5be1be7212e7) or you can manually install the template and customize it in the Shopify admin by performing the following steps.

<aside class="note note-caution"><h4>Caution</h4><p>Before you follow these steps, ensure that <a href="/en/manual/payments/payment-authorization">credit card authorization and capture</a> is set to <a href="/en/manual/payments/payment-authorization#set-up-manual-payment-capture">capture manually</a> in your settings. This workflow does not function if automatic capture is activated.</p>
</aside>

#### Steps:


  
      
    


1. From your Shopify admin, go to **Apps** > [**Flow**](https://admin.shopify.com/apps/flow).


2. Click **Create workflow**.
3. Click [**Browse templates**](/manual/shopify-flow/create/create-workflow#create-workflow-using-template).
4. Select **Risk**, and then select **Capture payment if order is not high fraud risk**.
5. Click **Install**.
6. Optional: If you want to track orders that have not been fulfilled, then do the following:
   1. In the **Check if** box, click the `+` indicator next to **Otherwise**.
   2. Click **Action**.
   3. Select an action. For example, you can use the [**Add order tags**](/manual/shopify-flow/reference/actions/add-order-tags) action to add a tag, or the [**Send internal email**](/manual/shopify-flow/reference/actions/send-email) action to send an email to yourself or your staff to indicate payment was not captured.
7. Do one of the following:
   * To save the workflow and start using it, click **Turn on workflow**.
   * To save the workflow without activating it, click **Exit**.

## Cancel and restock high-risk orders {#cancel-and-restock}

This workflow cancels high-risk orders and restocks items in the orders. It also adds a tag to the order, adds a tag to the customer that placed the order, and sends an email indicating that an order was canceled due to high risk. [You can install the template automatically](https://admin.shopify.com/apps/flow/web/editor/templates/5dd999c6-7c63-4416-bf37-68c2a4da4ef9) or you can manually install the template and customize it in the Shopify admin by performing the following steps.

#### Steps:


  
      
    


1. From your Shopify admin, go to **Apps** > [**Flow**](https://admin.shopify.com/apps/flow).


2. Click **Create workflow**.
3. Click [**Browse templates**](/manual/shopify-flow/create/create-workflow#create-workflow-using-template).
4. Select **Risk**, and then select **Cancel and restock high risk orders**.
5. Optional: To edit the actions taken by the workflow, click the action that you want to change. For example, to change the destination of the email, click the **Send internal email** box, and then change `your.email@example.com` to the email address that you want to use.
6. Do one of the following:
   * To save the workflow and start using it, click **Turn on workflow**.
   * To save the workflow without activating it, click **Exit**.


## Cancel orders for customers who frequently return items {#cancel-return-items}

Cancel orders for customers that have returned products five times or more in the last six months. [You can install the template automatically](https://admin.shopify.com/apps/flow/web/editor/templates//eed706da-fe6c-436f-902f-e110faf81c30) or you can manually install the template and customize it in your Shopify admin.

#### Steps:


  
      
    


1. From your Shopify admin, go to **Apps** > [**Flow**](https://admin.shopify.com/apps/flow).


2. Click **Create workflow**.
3. Click [**Browse templates**](/manual/shopify-flow/create/create-workflow#create-workflow-using-template).
4. Select **Risk**, and then select **Cancel orders for customers who frequently return items**.
5. Optional: To edit the actions taken by the workflow, click the action that you want to change. For example, to change the destination of the email, click the **Send internal email** box, and then change `your.email@example.com` to the email address that you want to use.
6. Do one of the following:
   * To save the workflow and start using it, click **Turn on workflow**.
   * To save the workflow without activating it, click **Exit**.


## Cancel and tag orders from known bad email addresses {#cancel-and-tag}

Automatically cancel orders that use an email address used for past fraudulent orders. This can be easy for fraudulent customers to work around, but can help interrupt automated fraud. [You can install the template automatically](https://admin.shopify.com/apps/flow/web/editor/templates/872c0782-7ad6-4082-b321-fc5920c328db) or you can manually install the template and customize in your Shopify admin.

#### Steps:


  
      
    


1. From your Shopify admin, go to **Apps** > [**Flow**](https://admin.shopify.com/apps/flow).


2. Click **Create workflow**.
3. Click [**Browse templates**](/manual/shopify-flow/create/create-workflow#create-workflow-using-template).
4. Select **Risk**, and then select **Cancel and tag orders from known bad email addresses**.
5. Optional: To edit the actions taken by the workflow, click the action that you want to change. For example, to change the destination of the email, click the **Send internal email** box, and then change `your.email@example.com` to the email address that you want to use.
6. Do one of the following:
   * To save the workflow and start using it, click **Turn on workflow**.
   * To save the workflow without activating it, click **Exit**.
