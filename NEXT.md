# Open work, in order

Each item says what it decides and what it needs. Items lower down depend on the ones above.

## 1. Q1, the concern map (built; the founder's review is next)

**Question.** How does the product class (Shopify, Salla, WooCommerce) divide a commerce platform into concerns, and where does it place each one? The full question, rules and output format are in `questions/Q1-concern-map.md`.

**Where it stands.** All three platforms are re-passed: what each states, in its own words, for every concern and placement, or a gap. The matching pass is done, with 88 matches and 84 unclear candidates, and the side-by-side map is in `studies/concern-map/map/`. Detail is in `studies/concern-map/README.md`.

**What the founder is asked for:**
- rulings on the 84 unclear matches (`studies/concern-map/unclear-matches.tsv`);
- a look at matches M-070 and M-064;
- whether an agreement a platform's terms incorporate (such as Stripe's under WooPayments and Shopify Payments) may be read;
- the gaps only the founder can close (`studies/concern-map/gaps-to-close.md`): the salla.com pages, the journeys, a paid Plus store, questions to the platforms.

**How the founder's evidence closes gaps.** The founder closes the gaps that name them by capturing the evidence into observed-sh or observed-sa, in those repositories' own format: saved pages, journeys, store runs. When the founder says it has landed:
1. Fetch the new commit and list what is new against the commits the map cites.
2. Match the new evidence to open gaps by their routes (URL, admin path and role, plan).
3. Run a gap-closing pass per platform. An agent reads only the new evidence, as its own read. It turns a gap into a statement where the evidence states something, quoted verbatim and cited at the new commit. It updates `why_not_held` for every gap still open.
4. Check, commit, and regenerate `gaps-to-close.md`. The pass reports what is still not closed.

The founder's words are never evidence. What the founder captures from the platforms is.

## 2. Q2, the Yemen stress test

Tests the map against the market, case by case, using only Yemen evidence. See `questions/Q2-yemen-stress-test.md`.

Since 11 October, observed-sh's admin answers come from stores registered in Yemen (country `YE`, currency `YER`). They are direct evidence of how Shopify treats such a store.

**Waits for:** item 1 and the founder's go.

## 3. Q3, placing the rows

Places the existing question rows on the map and flags the time bombs. See `questions/Q3-placing-rows.md`.

**Waits for:** items 1 and 2.

**Open for the founder:** which rows to place — the 81 payment rows, the Knowledge Map's 179 questions, or both.

## 4. Yemen sources (continuing)

- `evidence/yemen/to-fetch-from-yemen.md` lists what only the founder can fetch from inside Yemen.
- Founder attestations use `evidence/yemen/attestations/TEMPLATE.md`.

## Superseded

Two items were logged before the three questions were agreed. Their work was in closed pull request #3 and is not used.

- **The payment seam.** The question was whether payments can be its own part of the platform behind a contract. Q1's map records where each payment concern lives and how it meets the rest.
- **The frame sort of the 81 rows.** Q3 takes its place.
