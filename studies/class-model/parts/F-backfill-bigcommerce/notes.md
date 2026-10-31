# F-backfill-bigcommerce: notes

## What this part did

F-bigcommerce added three capabilities to domain F: CM-API-013 (account-level API, under CM-API-001), CM-DVT-006 (staging environments) and CM-PTN-010 (Commerce-as-a-Service for partners, under CM-PTN-001). This part writes their twelve cells for Shopify, Salla, WooCommerce and Zid. It adds no capabilities, lands no concerns, and writes no rulings, qualities or slot fillers.

For each platform I ran `candidates --domain F --platform P --areas API,DVT,PTN`, read the leads with `key`, then searched further with `search`: Salla and Zid in English and in Arabic, each Arabic term in its singular and its plural, with and without ال. The terms are in each cell's `searched`. All twelve cells are `none-held`, and `evidence.tsv` has only its header. `none-held` means only that the concern map holds nothing found by those terms. It never means the platform lacks the capability. Each judgment that a hit is something else is a reading.

| Capability | Shopify | Salla | WooCommerce | Zid |
|---|---|---|---|---|
| CM-API-013 account-level API | none-held | none-held | none-held | none-held |
| CM-DVT-006 staging environments | none-held | none-held | none-held | none-held |
| CM-PTN-010 Commerce-as-a-Service for partners | none-held | none-held | none-held | none-held |

All three capabilities are BigCommerce's own so far. On the other four platforms, the definition each rests on (BC-S-0299, BC-S-0301; BC-S-0413; BC-S-0360, BC-S-0361) isn't stated.

## Homonyms

- **'Account API'.** Shopify's Customer Account API (SH-C-041/where/SH-S-0836, SH-I-0072) and Zid's API's > Account (ZD-I-0050, placed in ZD-C-075, Storefront APIs) are the buyer's account. WooCommerce's wc/v4 > settings-account (WC-I-0146, WC-C-073/boundary/WC-S-0146) is the store's Accounts & Privacy settings. BigCommerce's Account API is the merchant's account over all its stores (BC-S-0299, BC-S-0301). These are the same word for different things. The candidates found them through 'Account API'.
- **'Powered by'.** Every candidate for CM-PTN-010 on Shopify and WooCommerce is the phrase "powered by" naming a third party behind a product, such as Stripe, Melio, Global-e, Anthropic, OpenAI or WordPress. BigCommerce's Powered By is a programme name.

## Near misses left uncited (readings, for the reviewer)

- **Zid Merchant APIs > Account (ZD-C-077, domain A).** GET /v1/managers/account/me reads the "user account's basic identity information" (ZD-C-077/boundary/ZD-S-0086), and GET /v1/managers/account/store reads the store's core details (ZD-S-0087). Both go through the store's manager token (ZD-C-071/boundary/ZD-S-0875). No statement shows them reaching the account's other stores, managing its users, or using credentials and scopes of their own, which is what CM-API-013's definition rests on. So the cell is `none-held`. If the reviewer reads this group as the account-level API, ZD-C-077's statements would be cited from domain A, which doesn't name F under `also`.
- **Shopify organization settings (domain A).** The admin's settings:organizations:* routes (for example SH-C-003/decides/SH-S-5228, SH-C-010/decides/SH-S-5234) manage stores and users across an organization in the admin, but no statement offers them to apps as an API. The admin's internal operation endpoint (SH-C-004/where/SH-S-7179) is the admin's own.
- **WooCommerce wc/v3 > network-orders (WC-C-070/boundary/WC-S-0089, domain C).** The statement is only an entry in the API's list of resources. It doesn't say which sites the route reaches. The release's code, read as context and not cited, describes it as handling /orders/network requests. It is an orders route, not an API over an account.
- **Salla multi-stores (SA-C-003/decides/SA-S-3085, SA-I-2085).** This is a released dashboard flag. It names no API.
- **Staging.** None of these are a staging environment for a store: Shopify's Oxygen deployment for Hydrogen (SH-C-139/where/SH-S-0710), its Free expansion stores, whose purpose isn't stated (SH-C-003/decides/SH-S-7073), and Lighthouse CI on a development store (SH-S-6300); Salla's theme preview before purchase (SA-C-090/reason/SA-S-5031, a domain-E capability of one theme) and its maintenance mode (SA-C-002/where/SA-S-1726); WooCommerce's coming soon mode (WC-C-082/decides/WC-S-0891) and Blueprint imports (WC-C-094/decides/WC-S-5449, domain G); Zid Payments' testing base URL (ZD-C-010/where/ZD-S-0596).
- **Partners and merchants' stores.** Salla's demo stores (SA-C-209/decides/SA-S-5108, cited in CM-DVT-004), its Ready Stores (CM-DVT-005) and its agency programme (CM-PTN-006) are their own capabilities. Their statements show no partner API that creates stores for the partner's own merchants, changes their plans or bills them. The same holds for Shopify's Partner API and Partner Dashboard Stores, which are labels only (SH-C-168/where/SH-S-0838, SH-I-2086). Zid Agent (وكيل زد, ZD-C-025) is a merchant's service, not a partner programme.

## What the checker flagged

The checker printed no problem. It printed twelve flags, one per cell, of the form "none-held, and N statements match its searched terms or the other platforms' terms". These are the hits I read, and each cell's `reading` names the relevant ones and why none is cited. The large counts come from broad search terms that were needed so the searches would be complete: on Shopify, 'organization' matches eligibility rules and 'client'/'transfer' match unrelated admin routes and access scopes; on WooCommerce, 'Partner' matches the Stripe and Marketplace vendor statements. None of these shows the capability (a reading).

## Gaps

- The concern map holds no statement for any of the three capabilities' definitions on Shopify, Salla, WooCommerce or Zid.
- Shopify's Partner API is held only as a label (SH-S-0838). What it does isn't held, so it can't be checked against CM-PTN-010 or CM-API-013. That would need a page about the Partner API.
- What Shopify's Free expansion stores are for isn't held (SH-S-7073 is a plan line). It can't be checked against CM-DVT-006.
