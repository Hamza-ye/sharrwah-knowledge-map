observed-sh@04de369da; observed-sa@b0bd0b163; other-product-class@0d79b794f; sharrwah-knowledge-map@3391c0ec6; woocommerce-11.2.1

# S2-ZD-1: Zid, domains A to C, the held pass's second stage

Part S2-ZD-1 (`held/s2-parts.tsv`): 72 cells and 16 parts of 9 of Q3's misses (M-01, M-02, M-05, M-06, M-07, M-10, M-11, M-12, M-13). Effort: high. 90 rows: found 24, not-found 54, unclear 10, absent 2; no not-held, no unreadable, no new thing.

## What I read

- **The brief,** `briefs/S2-held.md`, whole; `s2_held.py leads --part S2-ZD-1` (8 naming a cell, 23 naming none) and `leads --held` (105), grepped with each chunk's terms; the evidence map, its Zid fault (the page index drops 18 pages; their titles are in `dashboard-locales`, which I read directly).
- **The guides, whole:** other-product-class's `README.md`, `docs/OPERATING.md`, `zid/README.md`, `zid/GAPS.md`.
- **The model's rules:** B-extent.md's "Build capabilities", "Cells and evidence", "Conventions from the dry run" (with "What a place of its own is"); H-held.md's "For each entry" rules 1 to 7 and "Rules"; `held/review-H-rulings.md`'s "Who does it, and `supports`" and "What an entry is, and where its other things go".
- **Grepped, by each cell's terms in English and Arabic** (folded: case, diacritics, alef, ta marbuta, alef maqsura, with a helper of my own over the files): `zid/structures/dashboard-locales/items.jsonl` (both languages), `dashboard-page-index`, `dashboard-route-manifest`, `store-plan-policies`, `store-permissions`, `structures/REGISTER.tsv`, `index/runs.tsv`, `index/run-notes.tsv`, `index/ledger/dashboard-routes.tsv`, the feature-flags answers, and `held/zid/entries.tsv` with its placements (to name held entries by id). Zid has no `index/instruments.json` entry that bore on a cell.
- **Searched:** `corpus_search.py zid --brief`, one call per language per chunk (six chunks), every term of the chunk in one call; `class_slice.py search --platform zid` for each passage I cite, to name a concern-map statement where one holds it (none did, apart from those the rows name); `class_slice.py caps --terms` for the misses' proposals.
- **Read in part, as sources:** zid.sa's and zid.eg's Terms and Conditions and pricing pages in run `20261028T190806Z-terms-pricing-sa-eg` (`fetch.warc.gz`, en at offsets 1196 and 224975, ar at 100420 and 325877, pricing at 453524), through `warc_text.py`; the steps of runs `20261028T144855Z-dashboard-routes-en` (002), `20261028T150740Z-settings-gaps-en` (006, 009, 022, 038, 043), `20261028T160128Z-dashboard-routes-rest-en` (134, 155), `20261028T170107Z-devstore-markets-en` (024); this repository's captures of help.zid.sa (orders-properties, zidpos-paymentpage, checkout-page-options, gcc-merchants, bank-accounts, return-order, tax settings), docs.zid.sa (create-a-new-product, the API index) and zid.sa's privacy policy (`20261027T112044Z-zid-rerender`, item 009; zid.eg's, `20261027T121854Z-s02-a2-sources-batch-3`, item 016).

The Arabic Terms (zid.sa/ar, offset 100420) are newer than the English (offset 1196): their direct shipping section (الشحن المباشر, lines 237 to 290 of the page's text) has no English counterpart held. Several rows rest on it.

## New things

None. No passage I read named a thing no capability holds with a place of its own that my cells or misses needed.

## The misses

- **M-01** (tipping), both parts not-found: the checkout page options as captured (settings-gaps-en step 6) list every option of the page, and none adds a tip; no tip, tipping or gratuity in English or Arabic in the dashboard's strings or the point of sale's. Proposal: none. CM-CHK-012's row is the same.
- **M-02** (payment test mode): part 1 unclear, part 2 not-found. The help centre tells the merchant to place a test order (طلب تجريبي) to check the buyer's experience, but not whether it runs in a test mode with simulated payment outcomes; nothing names test cards, a sandbox or a test mode for Zid Payments. Proposal: none (nothing found). Capture lead, `decision: pay:PAY-36`.
- **M-05** (scheduled delivery): found, core. A local delivery method's time slot settings (`logistics:expectedDeliveryDate.timeSlotSettings.*`) let the buyer choose a delivery time slot and day at checkout, up to five days ahead. Proposal: feature of **CM-SHP-008** (local delivery), where Zid places it; no place of its own (settings inside a delivery method). CM-SHP-018 (delivery promises) is the alternative: the same namespace's 'Show dynamic delivery date' is a delivery promise, which the buyer doesn't choose.
- **M-06** (saved package dimensions): not-found. The Arabic Terms compute volumetric weight from a shipment's dimensions; no saved packages or box sizes. Proposal: none.
- **M-07** (return rules), all four parts not-found: the return policy is a text the merchant writes (CM-CNT-008's), returns are reversals with a reason; no return window, return fee, restocking fee or final-sale setting. Proposal: none.
- **M-10** (try before you buy): not-found. Proposal: none.
- **M-11** (refusal at the door): both parts found, core, from the Arabic Terms' direct shipping section: the status رجيع is an order 'the end customer refused to receive', on any order Zid's shipping carries; on it the cash on delivery fee is refunded to the merchant and the base shipping fee is not, and the merchant bears the return shipment's fees. Proposal: feature of **CM-SHP-002** (shipping bought through the platform), whose terms these are; no place of its own (a status and a clause in the terms). The miss's 'as a way to contest a payment' is the buyer's act; the Terms state its outcome for the shipment and the charges.
- **M-12** (3D Secure and liability): part 1 found, core, the same passage as CM-PAY-033's row (Zid Pay's payment step sends the buyer to 3D Secure verification); part 2 unclear: the Terms speak of '3D Secure protection', which some Apple Pay payments lack, without saying whose loss it protects, and make the merchant responsible for chargebacks and fraud claims. Proposal: feature of **CM-PAY-033**. Capture lead, `decision: pay:PAY-31`.
- **M-13** (the buyer's proof of payment): unclear. An order's page shows its 'Transfer receipt' and lets the merchant upload one; who submits it isn't stated. Proposal: none. Capture lead, `decision: pay:PAY-75`.

## Capture leads whose could_change is kind or decision

None is `not-held`; the three are `unclear` rows, for the coordinator:
- M-02, test orders: `decision: pay:PAY-36`; a Zid page on test orders and Zid Payments' testing.
- M-12, the liability shift: `decision: pay:PAY-31`; a Zid Pay statement on who bears a fraud chargeback on a 3D Secure payment.
- M-13, the transfer receipt: `decision: pay:PAY-75`; a journey on development store 3277610: the storefront's checkout with bank transfer chosen, and the order page for such an order.

The other unclear rows (CM-ACC-011, CM-TRU-008, CM-CAT-009, CM-PAY-023, CM-PAY-031, CM-SHP-012, CM-TAX-005) are `count` or `no`.

## What would change a held cell's placement (S2-R2), and leads for other parts

- **CM-ACC-002 and the group list:** the confirmation email's footer names '© Zid Holding' / '© زد القابضة', 'Riyadh, Saudi Arabia' (`dashboard-locales/items.jsonl` lines 11366, 11367; 28231, 28232): a company name of Zid's, which the checker's `GROUP` list may lack.
- **CM-ACC-007** (maintenance mode), another part's: the working times' 'Close store completely' and 'Stop receiving orders' (`settings:workTime.*`, lines 3236 to 3265) close a live store for chosen periods.
- **CM-ACC-003:** the route `:lang/stores` (ZD-E-31b8d07e), placed on CM-ACC-001 'unsure', is likely the account menu's Manage stores; my row cites the menu string.
- **CM-SHP-018** (delivery promises): `logistics:expectedDeliveryDate.*` (lines 9230 to 9300), the expected delivery date shown at checkout, with cut-off time and daily limit.
- **CM-CHK-001:** the minimum and maximum order limits (settings-gaps-en step 9, lines 42 and 44), and the checkout's sign-in options and customer type 'company' (step 6).
- **CM-PAY-009:** the chargebacks page, `payments:chargebacks.*` (lines 4871 to 4882), with its evidence form.
- **CM-POS-002 / CM-PAY-021:** the POS features table's 'Nearpay Integration' (line 490), under Payment Methods; Nearpay's role isn't stated, so I gave it no filler.
- **CM-ORD-005:** 'Duplicate order' copies an order into a draft (`orders:details.duplicateOrder`, line 6223; ZD-11's lead).
- **CM-SHP-022:** the Arabic Terms' compensation for damaged shipments in direct shipping (lines 316 to 355 of the page's text).

## Problems with the brief or the scripts

- **A locale string's quote form.** The brief says to quote it 'with its key as “key”: “value”', but `quote_check.py` doesn't find that form in `items.jsonl`, whose line is `{"language": …, "namespace": …, "key": "<key>", "value": "<value>"}`. I quoted `“key”: “<key>”, “value”: “<value>”`, which the checker reads as the file's text, and put the namespace in `identifier`.
- **A reading's file.** The checker finds a reading's quote in a file only where the reading names it as the platform folder's path (`dashboard-locales/items.jsonl`, `<run>/steps/NNN.text.txt`, `raw/runs/…/fetch.warc.gz@<offset>`) or as a full source (`sharrwah-knowledge-map@<commit>:evidence/…`); a bare `evidence/…` path or a held entry's placement isn't read.
- **corpus_search's commit.** It printed this repository's moving commit (c7224109, 9195b096, 5ba8a4e6, 11c1f31e, ba032715 over the run); I wrote 3391c0ec6 throughout, as the part fixes.
- **An absence for some plans.** CM-PLN-003's FAQ states no fee on sales for Rise, Growth and Professional, not for Starter: I wrote `absent` and said so in its reading; the coordinator may prefer `found`, `shows`, as Salla's like line is held.
- **Combined searches.** One `corpus_search` per language with 20 to 30 terms lists the densest documents first, so pages that repeat the sidebar and footer (every dashboard step) crowd the first 40 of each corpus. Grepping the locales and structures directly, then reading the captures the search names, cost less.
