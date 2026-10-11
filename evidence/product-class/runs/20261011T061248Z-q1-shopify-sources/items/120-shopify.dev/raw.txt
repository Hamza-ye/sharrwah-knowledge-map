---
title: About fulfillment services
description: >-
  Learn about fulfillment services like third-party warehousing, print on
  demand, and services that prepare and ship orders on behalf of a store owner.
source_url:
  html: >-
    https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps
  md: >-
    https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps.md
---

# About fulfillment services

Fulfillment service apps provide third-party warehousing, print on demand, or fulfillment services that prepare and ship orders on behalf of merchants.

This guide describes what fulfillment services are, how they work, use cases for fulfillment service apps, and some considerations before you get started.

**Tip:**

If your app doesn't manage a fulfillment service location, but it assigns orders to be fulfilled by the merchant or by third-party locations, then refer to [Order management apps](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps).

***

## How it works

A fulfillment service fulfills orders that a merchant or another app requests. Each fulfillment service has a dedicated location. When you create a fulfillment service, Shopify automatically creates a new location for it.

Fulfillment services are represented in the GraphQL Admin API by the [`FulfillmentService`](https://shopify.dev/docs/api/admin-graphql/latest/objects/fulfillmentservice) object.

Fulfillment services can accept or reject requests to fulfill orders. After a request is approved, merchants can also submit requests to cancel the fulfillment order before the order is shipped.

**Note:**

Checkouts and orders can include multiple delivery methods, such as shipping and pickup in the same order. When your app uses delivery or fulfillment data, iterate over all delivery groups or fulfillment orders to determine the delivery method for each one. Don't assume one method for the order. For more information, refer to [split carts in checkout](https://shopify.dev/docs/apps/build/orders-fulfillment/split-carts).

The following diagram shows an example lifecycle of fulfilling an order using a fulfillment service app:

![A diagram showing an example lifecycle of fulfilling an order using a fulfillment service app.](https://shopify.dev/assets/assets/images/apps/fulfillments/fulfillment-service-apps/lifecycle-CB2gNMKi.png)

* **Customers** place orders, and receive items after the fulfillment process has completed.
* **Merchants** submit a request to a fulfillment service to fulfill a given order.
* **Fulfillment service apps** receive fulfillment requests and query assigned fulfillment orders to determine the fulfillment order actions that they can take on behalf of the merchant. For example, the app can accept the fulfillment request and create a fulfillment.
* **Third-party fulfillment services** fulfill and prepare orders for shipment.

### API objects and relationships

Before you start building your fulfillment service app, we recommend familiarizing yourself with the following API objects and their relationships.

![A diagram showing the relationships between fulfillment order API objects.](https://shopify.dev/assets/assets/images/apps/fulfillments/order-management-apps/fulfillment-order-api-objects-BoRsIVaA.png)

| GraphQL Admin API object | Description |
| - | - |
| [`Order`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order) | Contains information about an order, including an array of the fulfillment orders which include line items that were purchased. |
| [`FulfillmentOrder`](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder) | An item or a group of items in an order that are to be fulfilled from the same location. There can be more than one fulfillment order for an order at a given location. Use the fulfillment order `deliveryMethod` to identify whether the work is for shipping, pickup, local delivery, or another delivery method type. |
| [`FulfillmentOrderLineItem`](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrderLineItem) | A line item that belongs to a fulfillment order. It associates an order line item with quantities requiring fulfillment from the respective fulfillment order and any warning messages regarding the current fulfillment status. |
| [`Fulfillment`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Fulfillment) | A shipment of one or more items in an order. It includes the line item that the fulfillment applies to, its tracking information, and the location of the fulfillment. |
| [`FulfillmentService`](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentService) | A third-party warehousing service that prepares and ships orders on behalf of the store owner. Each fulfillment service is associated with its own location. When you create a fulfillment service, a new location is automatically created and associated with it. |
| [`Location`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Location) | A geographical location where a line item can be fulfilled from. A fulfillment service always has its own location, and variants managed by the fulfillment service should always be fulfilled from that location. |

***

## Statuses

Each fulfillment order has a [status](https://shopify.dev/docs/api/admin-graphql/latest/enums/FulfillmentOrderStatus) and a [request status](https://shopify.dev/docs/api/admin-graphql/latest/enums/FulfillmentOrderRequestStatus). Similarly, each fulfillment has a [status](https://shopify.dev/docs/api/admin-graphql/latest/enums/FulfillmentStatus).

The following diagram shows how a fulfillment order's status and request status changes, and how a fulfillment's status changes, based on the GraphQL Admin API request that's executed:

![A diagram showing the transition of fulfillment order statuses and request statuses, and fulfillment statuses](https://shopify.dev/assets/assets/images/apps/fulfillments/statuses-BmZNkMbI.png)

***

## Use cases

Common use cases for fulfillment service apps include the following:

* Approving or rejecting requests to fulfill orders
* Automating the order fulfillment process for merchants
* Enabling high-quality communication between fulfillment centers and merchants
* Providing transparent reporting about order status through the Shopify admin

***

## Webhooks

The following table describes the fulfillment order webhooks that your app can subscribe to in API version 2023-01 and higher. For more information, refer to [the payloads for fulfillment order webhooks](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services#webhooks).

| Webhook topic | Description |
| - | - |
| `fulfillment_orders/order_routing_complete` | Occurs when a fulfillment order is created and the order routing has been completed for the order |
| `fulfillment_orders/fulfillment_request_submitted` | Occurs when a merchant requests one or more fulfilment order line items be fulfilled by a fulfilment service |
| `fulfillment_orders/fulfillment_request_accepted` | Occurs when a fulfillment service accepts a merchant's request to fulfill one or more fulfillment order line items |
| `fulfillment_orders/fulfillment_request_rejected` | Occurs when a fulfillment service rejects a merchant's request to fulfill an order |
| `fulfillment_orders/placed_on_hold` | Occurs when a fulfillment order is placed on hold |
| `fulfillment_orders/hold_released` | Occurs when a fulfillment order hold is released |
| `fulfillment_orders/scheduled_fulfillment_order_ready` | Occurs when a scheduled fulfillment order is ready to be fulfilled |
| `fulfillment_orders/rescheduled` | Occurs when a fulfillment order is rescheduled |
| `fulfillment_orders/cancellation_request_submitted` | Occurs when a merchant requests to cancel a fulfillment order after the request was accepted by a fulfillment service |
| `fulfillment_orders/cancellation_request_accepted` | Occurs when a fulfillment service accepts a fulfillment cancellation request from a merchant |
| `fulfillment_orders/cancellation_request_rejected` | Occurs when a fulfillment service rejects a fulfillment cancellation request from a merchant |
| `fulfillment_orders/cancelled` | Occurs when a fulfillment service or merchant cancels a fulfillment order |
| `fulfillment_orders/fulfillment_service_failed_to_complete` | Occurs when a fulfillment service intends to close an assigned fulfillment order that was previously accepted for fulfillment. After this action, the fulfillment order transitions to an incomplete status. To continue the fulfillment process, the merchant or app needs to determine the next course of action. |

***

## Migrating your app

In Shopify, the [`FulfillmentOrder`](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder) object models an end-to-end fulfillment process and is available in the GraphQL Admin API. The `FulfillmentOrder` object enables fulfillment data to sync accurately between Shopify and apps.

**Deprecated:**

By API version 2023-07, all apps should be using the [`FulfillmentOrder`](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder) object to manage fulfillments. Apps using the following GraphQL Admin API objects to fulfill orders are using a legacy workflow that is no longer supported as of API version 2022-07:

* [`Order`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order)
* [`Fulfillment`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Fulfillment)

### Benefits

Migrating your app to the fulfillment orders workflow provides the following benefits:

* You can fetch the assigned location of a given group of unfulfilled line items to determine where fulfillment should occur.
* You no longer need to match SKUs or filter out the items on an order that don’t apply to you before you can determine which items you need to fulfill.
* App users and apps can both add notes to requests, which can improve communication throughout the fulfillment process.
* The process of making fulfillment and cancellation requests is formalized.

### Implementing recommended workflows

If you maintain a third-party app or Shopify Flow workflow that relies on `Order` and `Fulfillment` API resources for order automation, then refer to [Track orders placed through third-party marketplaces](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/track-orders-other-platforms).

***

## Developer tools and resources

Explore the following developer tools and resources to learn more about fulfilling orders.

[FulfillmentService object\
\
](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentService)

[Consult the GraphQL Admin API reference to learn more about the FulfillmentService object.](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentService)

[Split carts in checkout\
\
](https://shopify.dev/docs/apps/build/orders-fulfillment/split-carts)

[Learn how Shopify represents orders that split across multiple shipments or delivery methods.](https://shopify.dev/docs/apps/build/orders-fulfillment/split-carts)

***

## Next steps

* Learn how to [manage fulfillments as a fulfillment service app](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services).

***
