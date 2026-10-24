# Shopify areas: notes

## Under none

None. Every one of the extract's 198 concerns is placed under one area.

## Names that were hard to read

- `Trust` (admin-navigation, SH-I-0844, concern SH-C-008). The name alone does not say what the admin section holds. I read its cite id SH-S-1608 in `studies/concern-map/platforms/shopify/citations.tsv`, which points to `observed-sh@b46731d0:structures/shopify/admin-router/items.jsonl` line 1341. That line gives only `"section":"Trust","resource":"trust","sliceName":"trust-section"`, so it does not settle the meaning. I placed SH-C-008 by its own terms (identity-verification; Profile Assessment) under SH-A-01, and did not use `Trust` as an area name.
- `Foundation` (admin-navigation, SH-I-0807, concern SH-C-014), `ProfileAssessment` and `Intents`. I read the cite rows for SH-S-1571, SH-S-1594 and SH-S-1575 in `citations.tsv`; they quote only the admin router's section names (first routes `authentication-challenge-callback`, `profile-assessment:root`, `intents:parent`). I did not use these names for areas; their concerns are placed by their terms.
- `PlusContractDetails` / `contractmanagement` (SH-C-201). The cite row SH-S-7176 in `citations.tsv` shows an admin API endpoint for store ctcbwa-r1. That was enough with the concern's terms (Shopify Plus Terms; Switch to 3-year term) to place it under plans and billing (SH-A-04).
- `Online Store` and `Online store` both appear as Help Center menu names (manual menu and locale home). I used `Online Store`, the manual menu's spelling.

## What the extract seemed to lack

- The extract gives no list or term that names a single place for the merchant's sign-up location and the countries Shopify does not support. SH-A-29 is my own grouping of the sign-up country list, the Help Center page on unsupported countries and regions, and the sanctions terms.
- Country differences are spread across many lists (Shopify Payments by country, Capital by country, POS equipment agreements by country, contracting parties by billing region, data hosting locations). The extract has no one country list for Shopify itself, other than the sign-up list (233 options) and the business entity country list (237 options), whose values it does not show.
- Many store-features and store-entitlements keys are out of the concern map's scope ("no Shopify source held ties this key to a concern"), so eligibility by plan or store can be read only through the concerns' scopes, not through those keys.
- The extract's concerns end at SH-C-196 and then go to SH-C-201 and SH-C-202; SH-C-197 to SH-C-200 do not appear.
- After the checker was widened (parts of an entry's path, entries out of scope, halves of English / Arabic pairs), I checked each of my own groupings (SH-A-03, 04, 07, 08, 20, 23, 24, 25, 28, 29) for a heading the platform itself gives to that same group. None fits. The nearest headings each cover a different set: the staff permission headings `Finance`, `Store settings` and `Online store`; the plan-features group headings `AI features`, `Hosting` and `Customization`; the App Store category `Store management apps`; and the Help Center menus `Compliance` and `AI-powered tools`. They are either wider than my group or leave out part of it, so all ten stay `agent's own`.

## Entries

`method/place_entries.py shopify` placed 2493 entries, 0 under none, and 1054 split across more than one area. That is many splits, and nearly all of them come from a few kinds of list whose entries carry a second concern alongside the concern for their subject:
- `webhook-topics` (327 split), `access-scopes` (219), `api-resources` (57) and `extension-points` (38): each entry carries a developer concern (webhooks SH-C-162, access scopes SH-C-158, and so on, in SH-A-25) plus the concern for what it is about (orders, inventory, customers and so on). The most common pairs are SH-A-12 with SH-A-25 (84), SH-A-06 with SH-A-25 (67), and SH-A-08 and SH-A-11 with SH-A-25 (53 each).
- `other:staff-permissions` (277 split) and `other:staff-roles` (12): each permission carries roles and permissions (SH-C-010, in SH-A-01) plus the concern of the admin section it opens, for example SH-A-01 with SH-A-07 for the 37 `Content > …` permissions.
- `other:ucp` (35): each entry carries agentic commerce (SH-C-140, SH-A-20) plus checkout, cart, orders or products.
- `other:billing-charge-categories` (24): each charge carries Shopify bills (SH-C-016, SH-A-04) plus the service charged for.

These splits follow from how entries were given concerns, not from where areas were drawn. No grouping of the 198 concerns would remove them, short of joining the developer area or the account area to every other area.

Area sizes: SH-A-25 holds 742 entries, most of them webhook topics, access scopes and extension points, which fit its plain line. SH-A-01 holds 348, most of them staff permissions and roles. SH-A-03 holds the 68 notification templates (order confirmation, shipping and pickup messages, and so on), which fit its plain line on the notifications the store sends. SH-A-23 holds the Flow connectors listed under extension points (Asana, Trello, Slack, Google Sheets for Shopify Flow, OpenAI) and the plan features `Website builder` and `Millions of tokens`, which fit as Flow and Sidekick entries. SH-A-28 holds the Help Center pages `Dropshipping` and `Product fulfillment documentation`, because their concern is SH-C-175 (merchant compliance). SH-A-29 holds only 3 entries. I saw no area whose entries fall outside its plain line.

## Re-cut after the review

The coordinator re-cut these areas after the review of the areas list (`review.md`, findings 4 to 6), on 18 October 2026. Each area's note says why.
- SH-A-17 keeps Markets, Managed Markets, rollouts, the backup region, and international domains and geolocation. It is now marked as a grouping of our own.
- SH-A-30 (Languages) and SH-A-31 (the currency pages of International sales tools, with the store currency) are split from it.
- SH-A-32 joins gift cards (from SH-A-05) and store credit (from SH-A-08).
- SH-A-33 holds catalogs (from SH-A-09).
- The counts of areas and entries given above predate the re-cut. `areas-shopify.tsv` and `areas-shopify-entries.tsv` hold the current areas and placing.
