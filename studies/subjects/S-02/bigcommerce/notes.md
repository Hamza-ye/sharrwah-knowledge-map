# S-02, phase A: bigcommerce (BC)

BigCommerce is read "from what is recorded": statements come from `recorded.tsv` and the Q1 index; a page is read further only to close a gap instead of routing it to the founder (when `method/held_index.py` finds it held and readable), or, under rule 5, where a recorded excerpt is too short to show what bears on the subject.

## Documents read, in order

1. `studies/subjects/S-02/briefs/A-one-platform.md` (the brief), in full.
2. `studies/subjects/S-02/bullets.tsv`, in full.
3. `studies/subjects/S-02/bigcommerce/recorded.tsv` (R001 to R081), in full.
4. `studies/subjects/S-02/bigcommerce/recorded-citations.tsv`, in full.
5. `studies/concern-map/platforms/bigcommerce/concerns.tsv`: the concern ids, names and platform terms (columns 1 to 3), all 88 concerns.
6. `studies/concern-map/platforms/bigcommerce/statements.tsv`: by script, not loaded whole. Every statement of BC-C-005, 007, 008, 025, 026, 029, 030, 034, 040, 056, 066, 068, 069, 070, 072, 073, 077, 080 to 087; and, for every other concern, the statements whose identifier, statement or scope holds a word on countries, regions, locations, addresses, jurisdictions, markets, currencies, languages, channels or storefronts. The statements of BC-C-038, 039, 047, 048, 074, 075 and 079 are all in `recorded.tsv`.
7. `studies/concern-map/platforms/bigcommerce/citations.tsv`: by script, the citations of the index statements copied (source, locator, access path) and their notes in `statements.tsv`.
8. `evidence/product-class/runs/*/manifest.tsv`: the addresses on bigcommerce.com, bigcommerce.co.uk and commerce.com that the capture runs hold (an index of what is held, not a reading of the pages).
9. `method/check_subject.py`, `method/held_index.py`, `method/corpus_search.py`, `method/quote_check.py`: their usage notes, and the checker's rules on `from` and `conditions`.

## Recorded statements left out (rule 5: they bear on no bullet)

R011, R012 (partners adapting to multi-storefront; the reason for no breaking changes), R022 and R026 (the Translations API's availability and scope: no statement read ties translations to a market), R033 (settlement currency), R035, R036 (conversion fee and bank rate), R041 (Stripe OCS narrowing the payment methods), R058 (cryptocurrency payments enabled for all merchants), R069 (PayPal Braintree approval), R071 (auto-migration to BigCommerce Payments), R078 (PayPal order sync).

## What couldn't be read

## Problems with the brief or the tools
