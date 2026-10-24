---
title: Shopify API limits
description: >-
  The limits that apply across Shopify's APIs: input array size, pagination
  depth, and how rate limiting works. The rate limit figures for each API are
  documented with that API.
source_url:
  html: 'https://shopify.dev/docs/api/usage/limits'
  md: 'https://shopify.dev/docs/api/usage/limits.md'
---

# Shopify API limits

Some Shopify APIs limit the inputs they accept, and most are rate-limited. This page covers the limits that apply across the APIs, and points to the figures for each one.

***

## Rate limits

Rate limits keep the platform stable and fair for everyone. How a limit is calculated, and the figures that apply to you, vary by API. Use [industry standard techniques](#avoiding-rate-limit-errors) for limiting calls, caching results, and retrying requests responsibly.

### Rate limits by API

Every API applies limits differently, so the figures and the mechanics are documented with each API, including:

| API | Rate limits |
| - | - |
| GraphQL Admin API | [Calculated query cost, by plan](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits) |
| REST Admin API | [Request-based bucket and headers](https://shopify.dev/docs/api/admin-rest/usage/rate-limits) |
| Storefront API | [Bot and crawler limits, checkout throttle](https://shopify.dev/docs/api/storefront#rate-limits) |
| Customer Account API | [Cost points per store and customer, plus 3,000 requests per minute per customer](https://shopify.dev/docs/api/customer#rate-limits) |
| Payments Apps API | [Calculated query cost, by plan](https://shopify.dev/docs/api/payments-apps#rate-limits) |
| Partner API | [Request-based limit per API client](https://shopify.dev/docs/api/partner#rate-limits) |
| App Events API | [Request-based limit per app](https://shopify.dev/docs/api/app-events/latest/creating-events#rate-limits) |

### The leaky bucket algorithm

Most Shopify rate limits are enforced with a [leaky bucket algorithm](https://en.wikipedia.org/wiki/Leaky_bucket). The main points to understand about the leaky bucket metaphor are as follows:

* Each app has access to a bucket. Its size is set by the API and by your plan.
* Each API request tosses some number of marbles into the bucket. How many depends on the API's rate-limiting method.
* The bucket leaks continuously at that API's restore rate, which frees up capacity for more marbles.
* If the bucket fills, you get a throttle error and have to wait for more bucket capacity to become available.

Both the bucket size and the restore rate vary by API and by plan, so refer to [rate limits by API](#rate-limits-by-api) for the figures that apply to you. This model means that apps that manage API calls responsibly keep capacity for bursts: as long as your average stays under the restore rate, a short burst above it still succeeds.

The Storefront API works differently. Buyer traffic isn't rate-limited at all, and the limits it does apply are described in [Storefront API rate limits](https://shopify.dev/docs/api/storefront#rate-limits).

Shopify may temporarily reduce API rate limits to protect platform stability. We will strive to keep these instances brief and rare. However, your application should be built to handle limits gracefully.

### Resource-based rate limits

Once a store has 500,000 product variants, no more than 10,000 new variants can be created per day, on any API.

The resources and mutations that are subject to the throttle are listed with each API's rate limits: [GraphQL Admin API](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits#resource-based-rate-limits) and [REST Admin API](https://shopify.dev/docs/api/admin-rest/usage/rate-limits#resource-based-rate-limits).

**Plus:**

The variant creation throttle doesn't apply to stores on the [Shopify Plus](https://www.shopify.com/plus) plan.

### Avoiding rate limit errors

Designing your app with best practices in mind is the best way to avoid throttling errors. For example, you can stagger API requests in a queue and do other processing tasks while waiting for the next queued job to run. Consider the following best practices when designing your app:

* Optimize your code to only get the data that your app requires.
* Use caching for data that your app uses often.
* Regulate the rate of your requests for smoother distribution.
* Include code that catches errors. If you ignore these errors and keep trying to make requests, then your app won't be able to gracefully recover.
* Use metadata about your app's API usage, included with all API responses, to manage your app's behavior dynamically.
* Your code should stop making additional API requests until enough time has passed to retry. The recommended backoff time is one second.

***

## Input limits

Input arguments that accept an array have a maximum size of 250, on every Shopify API. Requests return an error if an input array exceeds 250 items.

***

## Pagination limits

Pagination of arrays of objects caps at 25,000 objects, and the cap applies to count queries too. For how the limit behaves and what to do when you need to page past it, refer to [GraphQL pagination](https://shopify.dev/docs/api/usage/pagination-graphql#pagination-limits).

***
