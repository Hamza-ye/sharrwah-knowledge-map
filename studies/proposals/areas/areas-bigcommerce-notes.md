# BigCommerce (BC): notes on the areas

## Under none

None. Every one of the 88 concerns is under exactly one area.

## Names that were hard to read

- The product lines (`other:product-lines`, BC-I-0497 to BC-I-0541) are listed in an order that looks like sections of the platform's product pages: checkout, then B2B, AI, omnichannel, core commerce, open platform and enterprise. The extract gives no heading for any of these sections, so no area takes a section name. Where an area follows one of these runs, it is marked `agent's own`.
- `Storefront Cookie Consent` (BC-C-037): a Storefront API resource, scoped to Catalyst storefronts. Read from the extract only (its term, description and scope). It is placed with the shopper's records (BC-A-14), not with personal data processing (BC-A-27), because the extract shows it as a storefront resource about a shopper and not as part of the Data Processing Addendum.
- `Third-Party Products` (BC-C-084): a term of the Master Services Agreement. Read from the extract only. It is placed with apps and integrations (BC-A-23), since the agreement's term covers what merchants connect to their stores.
- `Merchant-Client Terms` and `Agents` (BC-C-087): read from the extract only, as terms for agents, such as agencies, acting for a merchant client.
- `Pricing` (BC-C-008): the concern map describes it as storefront pricing. Read from the extract only.
- The contracting-entities entries are long names in three or four `|`-separated fields. They are copied whole. The two Worldwide entries (Feedonomics and Makeswift) are not named in BC-A-28; their concerns are described in BC-A-16 and BC-A-21, which say each has its own contracting company.

No cited passage was opened: every name used could be read from the extract.

## What the extract seemed to lack

- No help-centre or control-panel menu for BigCommerce. The platform's own division comes from its settings list, its product lines, its plan table, its app marketplace categories, its API reference and its legal agreements. The areas lean on those.
- The plan names show only as scopes ("plans Core, Growth, Scale, Performance (columns of the plan comparison table)", "Enterprise plan", "Pro plan", "Plus and Standard plans"). The extract has no list of plans with their prices, so plans get no area of their own; what differs by plan is said in each area's plain line.
- Places show only in a few scopes: the contracting entities by the merchant's country of residence, Unified Billing (US, UK and Canada; India), BigCommerce Payments (US-based merchants), customers domiciled in the EU, UK, Germany or the US. There is no list of countries where the platform operates or where a store may sell.
- Eligibility shows in the sanctions clause, BigCommerce Payments' US-only scope, the closed betas (Checkout Extensions, Page Widgets, Product Recommendations, Powered By) and Enterprise-only features (staging, some rate limits). No rule says who may open a store at all.
- The webhook topics (201), API resources (116) and access scopes (60) are not mapped to concerns in the extract; the areas take only concern terms from them.

## Entries

`method/place_entries.py bigcommerce` placed 555 entries (the 569 in the inventory, less the 14 out of the concern map's scope): 61 fall in more than one area, and none fall in no area. The largest areas by entries are BC-A-13 (B2B Edition, 56), BC-A-22 (Open APIs, 55) and BC-A-01 (Catalog, 53). The smallest are BC-A-30 (Store Terms, 2) and BC-A-29 (Acceptable Use Policy, 3).

The 61 split entries are many, but most follow from how the entries are tied to concerns, not from where the area lines are drawn:
- 27 are metafield webhook topics (such as `store/product/metafield/created`). Each one is tied both to Metafields (BC-C-049, in BC-A-22) and to the resource that holds the metafield (products, categories, brands, carts, customers, orders, inventory locations, the store), so it falls in BC-A-22 and in that resource's area.
- 14 are App Marketplace categories (such as `Checkout`, `Shipping & Fulfillment`, `Accounting & Tax`). Each one is tied both to apps (BC-C-059, in BC-A-23) and to the concern its apps serve.
- 8 are Account API access scopes (`account_users_*`, `account_checkouts_*`, `account_subscriptions_*`, `account_apps_read`), each tied both to the Account API (BC-C-055, in BC-A-22) and to staff accounts, Unified Billing or apps.
- 2 are fulfillment-method scopes, split between pickup (BC-A-08) and shipping and fulfillment (BC-A-07).
- The rest are legal agreements and contracting entities that cover several concerns: the Master Services Agreement falls in five areas (BC-A-11, 23, 27, 28, 29); the Feedonomics and Makeswift privacy policies and contracting entities each fall in their product's area and in BC-A-27 or BC-A-28; the Fees and Billing Terms and the Open Payment Provider Fee fall in BC-A-10 and BC-A-12; the Store Terms fall in BC-A-17 and BC-A-30; and `Customer-specific pricing` and `Provider APIs` each fall in two areas.

Entries that don't fit their area's plain line well:
- In BC-A-22 (Open APIs): `Store Information [rest/admin/management/store-information/v3]`. The concern map ties it to Metafields (BC-C-049, whose terms include `Store Information`), but by its name it reads as the store's profile, which BC-A-18's plain line covers.
- In BC-A-01 (Catalog): `store/product/inventory/updated`, `store/product/inventory/order/updated`, `store/sku/inventory/updated` and `store/sku/inventory/order/updated`. They are tied to products (BC-C-001) only, but they report stock changes, which BC-A-02's plain line covers.
- In BC-A-18 (store settings and email): `store/channel/{channel_id}/socialMediaLinks/updated`. Social media links are not named in the plain line, though they are a store-wide setting like the others there.

## Re-cut after the review

The coordinator re-cut these areas after the review of the areas list (`review.md`, findings 2, 4 and 5), on 18 October 2026. Each area's note says why.
- BC-A-19 keeps currencies. BC-A-31 (Store Locale and Store Translations) and BC-A-34 (Geography) are split from it.
- BC-A-32 holds BigCommerce Payments (from BC-A-10).
- BC-A-33 holds price lists (from BC-A-03).
- The counts of areas and entries given above predate the re-cut. `areas-bigcommerce.tsv` and `areas-bigcommerce-entries.tsv` hold the current areas and placing.
