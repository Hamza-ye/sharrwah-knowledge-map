# Pass 1, part D: notes

Part D is the cited-sources run, `evidence/yemen/runs/20261010T050304Z-cited-sources/`, items 1 to 131 by the `n` column of its `manifest.tsv`. The run's README says it was fetched outside Yemen, so every citation has `fetched_from` = `outside Yemen`. Every `source` uses commit 9d0de523f1852ebf7716f0da01b6b619edc5e8fc.

## Status

In progress. Items read so far, in order: 1 to 6.

## The part

- The manifest has 115 rows with `n` from 1 to 131. The numbers 29, 30 and 94 to 107 have no row in `manifest.tsv` and no folder in `items/`.

## Read, by item

| n | result | text read | conditions recorded |
| --- | --- | --- | --- |
| 1 | captured | text.txt | 1 |
| 2 | gone (404) | text.txt holds only the 404 page | 0 |
| 3 | captured | text.txt | 8 |
| 4 | captured | text.txt | 9 |
| 5 | captured | text.txt; the page also carries three later, unrelated articles (Gaza, a military operation, blood drives), with no condition | 4 |
| 6 | captured | text.txt; the page also carries later, unrelated articles (Iran, US, Sudan), with no condition | 8 |

## Conventions used in this part

- `date_basis` in `conditions-D.tsv`: `stated` (the source says when it held); `still holds (source date)`; `range end`; `source date (effective)`, `source date (published)`, `source date (shown)`; `live page (capture date)`; `no date`.
- `date_basis` in `citations-D.tsv` says what `source_date` is: `effective`, `published`, `shown`, `capture date (live page)`, or `none`.
- `locator` is the line in the cited file where the quote starts.

## Identifications within the part

(Rows given the same `condition` wording.)

## Place groupings within the part

## Could not be read
