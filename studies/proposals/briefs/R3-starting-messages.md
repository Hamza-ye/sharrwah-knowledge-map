# The messages that start the R3 runs

**18 October 2026.** What the coordinator puts in the message that starts each recording or checking run, beside its brief. The reviews of the areas list asked for some of it (`studies/proposals/areas/review.md`, findings 8 and 25; `review-recheck.md`, finding 5).

## Every run

- the brief: `studies/proposals/briefs/R3-recording.md`, or `R3-checking.md` with the recording brief it follows;
- the question and the platform, and for a checking run the platforms read in depth;
- the scratch directory for working copies;
- the effort: `medium`, or `high` for a re-run.

The selection already holds the concerns the question draws on, the pilot's row, and the single concerns in `studies/proposals/areas/extra-candidates.tsv`. A message names nothing else as a candidate.

## Pointers to where to read

Each says where something is held. None says what it shows.

- **Q8 on Shopify:** Shopify's terms section "9.10 Beta Services" is out of the concern map's scope. Find it with `corpus_search.py shopify "Beta Services"`.
- **Q1 and Q7 on Shopify:** Shopify's store features include keys that are out of the concern map's scope: `perMarketIncoterms`, `landedCostIncoterms`, `multiCurrencyGatewayEnabled`, `subCountryMarketsEnabled`, `marketDeliveryProfiles`, `managedMarkets`, `usingMarketsPro`, `catalogRolloutsEnabled` and `threeDSecureEligibilityForCountry`. They are held in observed-sh's `structures/shopify/shop-request-details/<store>/items.jsonl`, under `features`. The corpus search finds them by name.
- **BigCommerce's runs (Q3, Q4, Q6 and Q7 are checks):** BigCommerce's Help Center couldn't be read from outside in the concern map's runs. Some of its pages are held in this repository's capture runs and in the founder's saves. Find them with `held_index.py` and the corpus search before reading live.
- **Salla's runs:** most of the gaps the copies carry for Salla are pages held but not read in the concern map's runs, because live reading met a bot challenge. Before reading such a page live, run `held_index.py` on its address.
