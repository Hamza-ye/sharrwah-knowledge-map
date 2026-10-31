# Notes: designs beyond the references, D8 and D9

From the brief `briefs/H-designs.md`. Rows are in `designs.tsv`; the run is `evidence/designs/runs/20261029T023737Z-s02-designs/` (10 items, all captured, HTTP 2xx, rendered).

## What was searched

Candidates were chosen from known standards and documentation, not from a web search. Each was first read as a working copy with `method/capture/page_text.mjs`, then captured in the run.

- **D8 (an area within a country):** ISO 3166 (iso.org, refused); Unicode TR35 subdivision codes, their change rules and the `rg` key (captured); Google's `PostalAddress` type (captured); Stripe Tax registrations (captured); OpenStreetMap `admin_level` (captured); Fowler, Temporal Property (captured). Five sources used.
- **D9 (two currency areas under one code):** ISO 4217 (iso.org page and standard preview, refused); the ISO 4217 Maintenance Agency's page at SIX (captured), and its "maintenance-agency-guidelines.pdf" (read as a working copy: it turned out to be the guidelines for ISO 10962, CFI codes, not ISO 4217, so it is not used or captured); SIX amendment PDFs 170 and 171 (URLs guessed from the amendment list; they returned HTML, not PDFs, so not used); SIX's amendment overview spreadsheet (read as a working copy: it lists amendments by country and date only, with no rule text; not used); Fowler, Money (captured); Unicode TR35 currency codes (captured, same item as D8); Java `Currency` (captured); Stripe PaymentIntent (captured); TigerBeetle data modelling (captured); JSR 354 `CurrencyUnit` (read as a working copy, left out to keep to six sources per question: it says the same as Java's `Currency` on identity by code, and adds that a unit may be non-ISO). Six sources used.

Requests: about 30 (working copies, curl checks and the run of 10).

## What could not be fetched

- `https://www.iso.org/iso-3166-country-codes.html`, `https://www.iso.org/iso-4217-currency-codes.html`, `https://www.iso.org/standard/64758.html` and the ISO Online Browsing Platform for ISO 4217: HTTP 403, a bot challenge ("Just a moment..."). Not got around, per the capture README. For the founder to save from a normal browser if the coordinator needs them.
- So **the brief's question "What does the standard for currency codes do when one currency's units differ in value?" is not answered from the standard's own text.** The maintenance agency's page says only that lists change "if a currency is created, withdrawn or parts thereof altered" (`designs.tsv`, D9, SIX row). The agency's historical list (List Three) would show the practice through particular countries' revaluations, but only by naming those countries' currencies, which the brief's rule on market names keeps from being a reason; it was not captured. The closest captured evidence is TigerBeetle's: a change to a currency's unit is a new ledger number.

## Problems with the brief

- **Market names in sources.** Several captured pages name countries in their examples (TR35, the PostalAddress type, Stripe, SIX's current amendment). The rows quote only what bears on the design, and no reading uses a country's facts as a reason; where a quoted example names a country (the PostalAddress lines, Stripe's JSON example, TR35's `en-GB-u-rg-uszzzz`), the name is part of the example, not the reason.
- **"Bears on" takes one option letter.** Several sources bear on (b) and (c) alike (D8) or on what all options share (D9: a currency on every amount). Each row names the letter it bears on most directly, and the reading says when it does not choose between options.
- **D8's (c) bundles two things:** which rules key on an area, and a dated area whose change runs checks. Sources bear on the two parts separately (TR35 and OSM on the key; Fowler on the dating), and the readings say which part.
- **Quotes across lines.** For the PostalAddress and Stripe rows, a quote spans several lines of the captured file; ` / ` marks each line break, and the locator gives the line range.
- **Kind of OpenStreetMap's wiki:** a community-maintained data project's documentation; it fits none of the brief's four kinds exactly, and is marked as such.
