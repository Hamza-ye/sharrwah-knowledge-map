# Notes: Q1, shopify

## What was read

All of it was held, at observed-sh `c8b5fbee25966372a0475e6ed81f0b7760ac2921`. No live page was read.

- Help Center pages, through `method/help_map.py` (English):
  - markets/customizations/overview;
  - markets/getting-started/overview, market-types, set-up-markets, requirements-and-considerations, localization and submarkets (submarkets was opened and skimmed, and added nothing new);
  - markets/customizations/local-currencies and business-entities;
  - international/payments;
  - international/pricing/supported-currencies;
  - payments/third-party-providers, plus its configuring-providers and payment-gateway-availability pages.
- Fetch-archive records, through `method/warc_text.py`:
  - shopify.dev ShopFeatures.md (`raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz@8632954`);
  - www.shopify.com/international/managed (`raw/runs/20260930T050139Z-shopify-com-pages/fetch.warc.gz@17135260`);
  - www.shopify.com/payment-gateways (`…/fetch.warc.gz@41642451`);
  - the changelog post on multi-currency payouts in Australia and France (`raw/runs/20261007T071251Z-published-changelog-posts/fetch.warc.gz@267183`).
- `structures/shopify/shop-request-details/<store>/items.jsonl` for all 14 stores. These were read for the nine feature keys the coordinator named: perMarketIncoterms, landedCostIncoterms, multiCurrencyGatewayEnabled, subCountryMarketsEnabled, marketDeliveryProfiles, managedMarkets, usingMarketsPro, catalogRolloutsEnabled and threeDSecureEligibilityForCountry. `meta.json` and `sets.jsonl` were read for capture-gb-plus.

## How the store-feature statements are built

- There is one statement per key and value: Q1-SH-081 to Q1-SH-091.
- Each statement's text is the first store's JSON line.
- Its scope lists every store and set with that value.
- Each store is cited at the first set where it has that value.
- `marketDeliveryProfiles` appears only for store zyd38b-ze.
- Some stores lack some keys at some sets. For example, perMarketIncoterms is absent at 2jiwxs-gr set 1.

## What couldn't be read

- The payment-gateways page's filter by country. The held text stops before any country is chosen (Q1-SH-N03).
- Each captured store's country. RequestDetails doesn't hold it, and admin Settings > General isn't held (Q1-SH-N04, routed to the founder).

## Copies

- No copy was found wrong.
- Q1-SH-071, from www.shopify.com/international/managed, states Managed Markets eligibility in different words from Q1-SH-K1956. The managed page says "based in the United States, Canada, or the United Kingdom". The Help Center copy says "continental United States, and to certain stores in Canada and the United Kingdom".

## Problems with the method

- Two quotes failed at first because the source puts a sentence's closing period right after a `</strong>` or `</a>` tag. The quote check then doesn't match the period. Those two statements end just before the period: Q1-SH-065 and Q1-SH-070.
- Each Help Center citation carries the REGISTER date-seen for help-center, 2026-10-16, since the pages are undated.
- One corpus search ran past the 120-second tool timeout and finished in the background.
- The brief asks for help pages to be cited by "the source help_map.py prints". Those sources were used as given.
