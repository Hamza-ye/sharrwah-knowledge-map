# The evidence map: where to start reading what is held (30 October 2026)

**What this is:** the entry point for every agent that reads the held evidence (`PLAN.md`, section 6, Evidence). It doesn't restate the repositories' own descriptions of their evidence. It points to them, in the order to read them, and adds three things:
- the repositories' own coverage counts;
- what the class's model has read;
- the faults the tools have shown.

**The counts** are in `held-vs-read.tsv`, by `python3 -I method/held_vs_read.py`. Its kind `ledger` gives each repository's own denominators (what the platform lists as existing) by status, as its ledger counts them. Its other kinds give the structures, addresses and runs, against what the model reads. `held-vs-read.md` sums them up.

## Where to start, per repository

**observed-sh, Shopify** (`/home/user/observed-sh`, at `9b047b08c`, which added `shopify/editions`; now at `e38dc17e3`, with the founder's eight new kinds of evidence, `held-vs-read.tsv`):
1. `README.md`, its "Starting points";
2. `docs/READING.md`, for what each kind of file holds and how it reads;
3. `docs/GAPS.md`, for what isn't held and why;
4. `structures/REGISTER.tsv`;
5. `index/ledger-summary.tsv`, then `index/ledger/*.tsv` and `index/denominators/SUMMARY.tsv`;
6. `index/runs.tsv` and `index/run-notes.tsv`.

Its denominators, by the ledger's own statuses:

| Denominator | Statuses |
| --- | --- |
| Admin routes per store | 5,326 visited; 4,747 needing an instance; 3,726 with a computed path; 2,774 not attempted; 659 splat; 280 without a path; 220 visited, not rendered |
| Admin mutations | 422 observed; 908 visited, not fired; 192 not attempted |
| Journey units | 160 journeyed; 117 swept; 34 not attempted |
| `shopify.dev` sitemap | 8,868 of 8,871 captured |
| Help Center sitemaps, 47 locales | 5,173 captured, English and Arabic among them; 83,583 not attempted |
| App store sitemaps | 3,068 captured; 44,653 not attempted |
| Themes sitemaps | 1,564 captured; 50,048 not attempted |
| `shopify.com` sitemap | 530 captured |
| Community sitemaps | 340,642 not attempted |

**Shopify's prices by country** are held at observed-sh `e38dc17e3`, in `structures/shopify/pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl`. It has 207 pages from 61 country sites: plans, POS and international.
- **What the pages hold:** each page's `loaderData.*.pricing` states its prices and terms: the Basic annual price, the minimum monthly price and its currency, the paid trial, the POS Pro price and the trial length. Each plan page's cards hold the plans' monthly prices.
- **What the held pass reads:** the 18 English-language sites and the 3 Arabic ones (`held/selection.tsv`). The other 40 sites state the same lines in their own languages, as the coordinator measured on 31 October.
- **Where the sites differ:** the comparison table has 103 rows on `www.shopify.com` and fewer on the other sites. The rows of the 40 sites in other languages aren't matched to the English ones.
- **For a subject comparing prices across markets:** read every site's prices and terms from this file, as a table.

**observed-sa, Salla** (`/home/user/observed-sa`, at `b0bd0b163`): the same files and order. Its denominators:

| Denominator | Statuses |
| --- | --- |
| Dashboard navigation pages | 365 swept; 97 journeyed; 3 not rendered |
| Features | 213 reached; 1,500 with no navigation entry |
| Settings fields | 231 shown; 63 saved; 3 not reached |
| Reports | 35 swept; 33 journeyed; 34 not reached |
| Dashboard apps | 177 served; 75 not reached |
| Partners portal apps | 10 served; 6 not reached |
| API operations in the docs | 190 documented; 95 called by the dashboard |
| Webhook events | 72 listed; 7 delivered |
| Journey units | 60 journeyed |
| Help centre sitemaps | every article captured, in Arabic and English, with the taxonomy |
| `salla.com` sitemaps, four markets and languages | captured |

**other-product-class, Zid, BigCommerce and WooCommerce** (`/home/user/other-product-class`, at `0d79b794f`):
- read `README.md` and `docs/OPERATING.md`;
- then each platform folder's `README.md`, `GAPS.md`, `structures/REGISTER.tsv` and `index/runs.tsv`;
- Zid keeps a ledger of its dashboard's routes: 267 opened, 107 not opened, 63 redirected (`zid/index/ledger/dashboard-routes.tsv`);
- BigCommerce and WooCommerce keep none, so their coverage is counted from their runs and structures.

**This repository's own evidence:**
- `evidence/product-class/runs/`: the public pages of Zid, BigCommerce and WooCommerce that the concern map read, by URL in each run's `manifest.tsv`;
- `evidence/product-class/blocked-evidence-founder/`: the founder's saves;
- `evidence/product-class/woocommerce-11.2.1/`: the release, unpacked at `/home/user/woocommerce-release/11.2.1`;
- `evidence/shopify-engineering/`: Shopify's own engineering writing, for the architecture plan. It says nothing of what merchants get.

## Coverage, at three levels, each with its remedy

| Level | What it means | Remedy |
| --- | --- | --- |
| Exists, not captured | a denominator's entry `not attempted`, or a surface no run reached | a capture request in `handoffs/`, only where the thing could change the model or a decision. The coordinator names it; the founder's local agent runs it, if the founder hands it on |
| Captured, not read | held, readable, and cited by nothing the model reads | an agent reads it: the held pass |
| Read, not placed, or placed wrongly | cited, with a placement in doubt | the review |

A thing is `absent` only where a complete list the platform publishes leaves it out, or the platform states it doesn't do it (`PLAN.md`, section 6, the test form). Otherwise nothing held is a gap at one of the three levels.

## What the tools read, and what they miss

| Tool | What it reads | What it misses or costs |
| --- | --- | --- |
| `held_index.py` | What every repository holds, by address: archives (archives held in parts at the part `fetch.cdx` names), structures, browser steps, saved answers, this repository's captures | An address it doesn't know isn't proof of absence: grep the platform's `fetch.cdx` and `answers.jsonl` too |
| `corpus_search.py` | Each platform's held text in every language, with case, diacritics and Arabic letter forms folded | Slow on Shopify: about 2 minutes a search. `--brief` keeps the output short. It finds words, not things, so a title that doesn't hold the term is missed: read the denominators first. WooCommerce's structures come through their saved answers |
| `quote_check.py` | A quote in its source, at a commit | `--text` needs a record's offset for an archive, and the capture run's folder for an address |
| `class_slice.py` | The concern map, the landed subjects' statements and the held pass's entries | `search` reads only the concern map's statements and inventories, not the repositories |
| `held_entries.py` | The selected structures' entries, each cited at its file and line | Only the structures `held/selection.tsv` reads |

**Found in the held pass:**
- BigCommerce's `settings-list` structure pairs each section with the next one's address. Its source step holds the right one (handoff H-009).
- Shopify's beta flags are held under hashed names, so nothing can be placed from them.
- BigCommerce's `contracting-entities` holds 5 of its page's 7 rows: its segment ends where the Feedonomics row begins, so the Feedonomics and Makeswift rows have no item (the review's R1). The concern map holds both rows (BC-S-0366, BC-S-0285), so no cell loses them. Its page, `https://www.commerce.com/terms/` in the `legal-pricing-docs` run, also names Feedonomics Holdings, LLC among Commerce's affiliates and subsidiaries, which three cells had read as a gap.
- WooCommerce's `core-profiler-free-extensions` has an item labelled EG that is the YE store's answer again. The run set the store's country in turn, and `EG` was refused (`rest_setting_value_invalid`, 400), so the store stayed at YE. SA, OM, YE and "EG" share one answer file (`raw/runs/20261029T024814Z-free-extensions-en/answers.jsonl`). Egypt's list isn't held, and the run's own note, 'SA, OM, YE and EG PayPal Payments in full', is wrong about EG. The held pass places the item's entries as YE's (WC-2, WC-3). A capture that sets a state, such as `EG:C`, would hold Egypt's list: a gap for the market subjects, not the model's extent. The payments providers' structure is another run, and its EG is Egypt's own list, with its own answer and a request for `{"location":"EG"}`.
- observed-sa's register says Salla's Mushammir panel wasn't opened. Later runs opened it, and it answers as an AI assistant ('Responses are AI-generated…'; the held pass's SA-7).
- Zid's `dashboard-page-index` holds 119 of its source's 137 page objects. Its extractor's pattern (`capture/structure_zid_dashboard_page_index.py`, line 24) needs a literal path followed by a literal title, so it drops the pages with an empty or computed path, a conditional title, or a key between path and title (ZD-1's notes; the review's R4). Each dropped page's route is in `dashboard-route-manifest` (ZD-2, ZD-3), so no request goes out. But the routes carry no titles, so two things reach no entry:
  - the pages' own titles, in English and Arabic, such as "Manual orders" / "الطلبات اليدوية";
  - the charity store's titles (Donations / التبرعات, Donation opportunities / فرص التبرع, Donors / المتبرعون), which would make CM-SEL-007's Zid cell held.

  Both are in `source.js` and in `dashboard-locales`' `navbar` strings. The second stage reads them for the cells that hold nothing. The items also leave out each page's permission, sidebar badge and listing condition, which `source.js` holds.
- observed-sa's `derived/plan-gates.tsv` keys the edu rows by address without the query string (`capture/gates.py`, line 148), so the last `/products/new?type=` row overwrites `/products/new`'s own plans: the row shows `plus, team, special` where the edu row says `basic, plus, team, special` (the held pass's SA-15). The source governs; the derived table could be fixed by its owner.
- Shopify's `admin-home-setup` leaves out every ARIA line its source writes in single quotes, the form YAML takes for a name holding a colon (`capture/structure_aria_subtree.py`, by the register). The B2B guide's card button ('3 of 6 tasks completed Sell B2B and DTC, in one place Next task: …', `capture-gb-plus@2026-10-07-plus-dev/source.aria.yaml`, line 110) and the lesson's 'Watch now: Learn the dropshipping basics' on four stores have no item. Their parts are entries, so no cell loses a thing (the held pass's SH-1). The source governs; the extractor could be fixed by its owner.
- Salla's `portal-private-settings` holds the partner account's 68 features of 8 October. The same account's answer of 28 October lists 74, among them `temp-services-redesign` and `temp-influencer-redesign` (`raw/runs/20261028T160451Z-journey-portal-demo-store-new-en/responses/0006.json`). The held pass reads the later answer for those two (SA-44's check).
