# The qualities pass: its design, for the coordinator (31 October 2026)

**What this is.** The design behind `briefs/QL-qualities.md`, drafted by an agent for the coordinator, from `PLAN.md`, Stage 4A, "The qualities pass", and its section 11 entry of 31 October. It covers:
- the kinds, as the checklist the brief gives the agents;
- where each platform's quality statements are held, counted from the repositories' guides and indexes;
- the rows' form;
- the landing: the script that turns `found` rows into held entries and quality rows, and the changes to the model's tools;
- the relabelling of the plans' terms;
- the split into agents, and an estimate of the cost, an assumption to be measured on the first agent;
- the capture requests that may follow;
- the rulings the brief adds, in plain words, and the open questions.

Nothing here is built yet. `method/ql_qualities.py` and the changes in section 6 come before the brief's inspection, so the inspector can test them on fixtures, as the second stage's were.

**What was read, at which commits:** this repository at `7b618bbf` (`PLAN.md`, `STATE.md`, `founder-decisions.tsv`, the briefs B-extent, H-held, S2-held and its design, `inspection-S2.md`, `architecture/plan.md` and `plan-review.md`, `merged/`, `held/selection.tsv`, the tools named below, `evidence/`); observed-sh at `04de369da`, observed-sa at `b0bd0b163` and other-product-class at `0d79b794f`, their guides, registers, ledgers and runs' indexes, and a few structures' files, as named. The counts below are by scratch scripts kept in the drafting agent's scratchpad. Where a count rests on a pattern over labels or addresses, it is marked as a reading. `S2-held.md` and its tools are being revised from their inspection as this is written, so this design follows their form, not their final wording.

## 1. The design in one view

1. **The labels first.** `ql_qualities.py labels propose --write` labels each of the model's 3,881 quality rows as a `term`, a `quality` or `other`, by rule, in a ledger beside the model (`studies/class-model/qualities/labels.tsv`). The rows the rules can't settle are reviewed once (section 7). The parts' files are never edited.
2. **The part list and the sources.** `ql_qualities.py parts --write` writes `qualities/parts.tsv` (section 8). The coordinator writes `qualities/sources.tsv` from section 4: per platform and kind, the structures, runs and addresses to read first.
3. **The agents** (`QL-qualities.md`), one per part, up to four at once. Each answers its platform's 44 asks, kind by kind, and writes `qualities/<platform>/<part>.tsv` and `.md`. A row is `found` (the passage, its value, kind, form, basis, capability or `platform`, holder, scope, date, source type), `not-found`, `not-held`, `absent`, `unreadable` or `unclear`.
4. **The check.** `ql_qualities.py check --part <part>`, until no problem. Then the coordinator's own check (section 8).
5. **The landing.** `ql_qualities.py land --platform <p>`, after that platform's second-stage batch is in the model (question 1). Each quoted passage becomes a held entry; each row on a capability becomes a quality placement in the batch `QL-<XX>`; each row on `platform` becomes a row of `qualities/platform.tsv`; each `found` row takes its label; the other outcomes go to `qualities/outcomes.tsv`, and the capture leads to `qualities/captures.tsv`.
6. **`held_entries.py check --platform <p> --batch QL-<XX>`**, then **`held_amend.py plan`** and **`apply`**, each with `--batch QL-<XX>`. Then `check_class_part.py` on each part it names, `class_merge.py --complete`, and `ql_qualities.py labels check`.
7. **The page.** `km_page.py` shows qualities and terms apart, and a table of the kinds by platform (section 7.4).
8. **Then:** the capture leads the coordinator takes go to `handoffs/` (section 9); `architecture/plan.md`, section 1's rows on qualities are measured again (APR-7); the rulings go to `reports/GM-rulings.md`.

## 2. What the model holds now

**`merged/qualities.tsv`,** by script at `7b618bbf`:
- **Its columns:** `cap_id`, `platform`, `quality`, `value`, `key`, `part`. A part's own `qualities.tsv` has the first five: `check_class_part.py`'s `HEADS` (line 29) fixes them, and its `table()` refuses any other header (lines 75 to 77). The scope is in each part's `derived-qualities.tsv`, which `check_class_part.py` writes from the key's statement (lines 608 to 613): 3,275 of the 3,881 rows have one. The merge doesn't carry it (`class_merge.py`, lines 241 to 243).
- **By platform:** Shopify 3,297, Salla 358, Zid 111, WooCommerce 72, BigCommerce 43.
- **By key:** 3,654 are held-pass entries (Shopify 3,221, Salla 316, Zid 63, WooCommerce 43, BigCommerce 11), 217 are concern-map statements, and 10 are inventory ids.
- **By structure:** Shopify's `pricing-page-data` gives 2,609; Shopify's `merchant-changelog` 207 and `editions-page-data` 148; Salla's `app-store-tabs` 109 and `shipping-carriers` 74; Shopify's plan pages 72 and 57; Zid's `plans-offered` 50.
- **By area of the capability:** PLN 1,657, PAY 577, POS 502, SHP 182, STF 164; then TRU 28, API 38, OPS 18.
- **The rule that made them.** B-extent, line 125: "a limit, a certification, an uptime or a data location a platform states, on the capability it bears on". H-held, rule 5, widened it: "or a value of the kind the model's `qualities.tsv` records (a maximum, a rate, a fee, a price, a duration), as `<what>: <value in its words>`, by plan where the entry gives one. This follows the model's practice, wider than B-extent.md's list."

**What it holds of the four things,** on the capabilities that hold trust, operations and data matters (`class_slice.py caps`; the rows of TRU, OPS and API):
- uptime: Shopify's "99.9%" (SH-E-de0b90b6), Salla's "100% uptime" (SA-E-cd7d1aa2, SA-E-403ce980), BigCommerce's Cyber Week figure (BC-C-083/where/BC-S-0455), on CM-OPS-001;
- where data lives: one Shopify row (SH-C-181/where/SH-S-0638) and three BigCommerce rows (BC-C-082), on CM-TRU-014;
- card data: Shopify, WooCommerce's payments service and BigCommerce, on CM-TRU-018;
- retention: two Shopify rows on CM-TRU-016, and WooCommerce's 30 days of logs on CM-OPS-005;
- API bounds: Shopify's and BigCommerce's rate limits on CM-API-005, Shopify's bulk operations on CM-API-007, BigCommerce's and Zid's webhook deactivation on CM-API-008, Salla's token validity on CM-API-002;
- identity: Zid's sign-out at the security level High and its Nafath attempts a day, on CM-TRU-001 and CM-TRU-002;
- nothing on how stores are kept apart, and no capability for it.

The cells (`merged/cells.tsv`): CM-TRU-014 holds nothing on Salla, and its reading says Salla's concern for it "has no statement: every placement is 'page not read' (the privacy policy's statements of where data is stored ...)". Salla's privacy policy is held (`observed-sa@b0bd0b163:structures/salla/com-policies/privacy/text.txt`), so this is "captured, not read". CM-TRU-018 holds nothing on Salla or Zid; CM-OPS-001 nothing on Zid. Zid's CM-TRU-014 is `core` on its privacy policy's transfer abroad (ZD-C-041/decides/ZD-S-0794), and its reading says where Zid stores data "is not stated".

**What reads `qualities.tsv`:**
- `check_class_part.py`: each row's `cap_id` a capability of the part's domain, and its key an inventory id or a citable statement of its platform (lines 488 to 501);
- `class_merge.py`: concatenates the parts' rows with their part (lines 241 to 243);
- `held_amend.py`: writes a placement's `quality` (`<what>: <value>`) into the part that holds the cell (lines 118 to 120, 285 to 293);
- `held_entries.py check` and `s2_held.py check`: a mark of inclusion is refused as a quality (`held_entries.MARKS`);
- `km_page.py`: each capability's rows, under the label "quality" (lines 127 to 128; template line 350);
- `review_select.py`: the parts' files, for the coordinator's marks (line 142).

Nothing reads a quality's kind, form or label, because none is recorded.

**The second stage leaves the held cells' qualities unread.** `held/selection.tsv` sends Shopify's `compliance-reports` ("certifications, read as the qualities of the trust and payments cells in the second stage"), `status-page`, `legal-documents` and `dev-changelog`, and Salla's `com-policies` and `partners-legal`, to be read where a cell needs them. The second stage reads only the cells holding nothing, and `inspection-S2.md`, S2I-21, found: "Shopify's compliance reports, sent here for held cells' qualities, aren't read." This pass is the one that reads them.

## 3. The kinds, and what architecture needs from them

The checklist is in the brief, "The kinds: the checklist": 16 kinds, each with its plain name, its ISO/IEC 25010:2023 characteristic, the first decisions it drives, the capability it lands on by default, and 44 asks with their words in English and Arabic.

**Why these kinds.** `PLAN.md` names three: "isolation between stores, where data lives, and identity". The others split the plan's four forms by what architecture's first decisions read (`architecture/plan.md`, section 3), and by the sources the task names: trust and compliance pages, legal terms, status pages, limits, scale claims, accessibility and engineering writing.

**The ISO/IEC 25010:2023 column is a reading.** This repository doesn't hold the standard, and its characteristics are named from memory of the 2023 edition: functional suitability, performance efficiency, compatibility, interaction capability, reliability, security, maintainability, flexibility and safety. Three of the kinds fit no product characteristic well:
- where data lives (`LOC`), nearer ISO/IEC 25012's data quality;
- attestations (`ATT`), which are evidence of a characteristic, not one;
- support (`SUP`), a service's quality, nearer the quality in use the 2023 series moved to ISO/IEC 25019.

The column is the agents' frame for what to look for. It decides no row: a row's `kind` is the checklist's code, and its words are the platform's.

**What each first decision reads** (a reading, from `architecture/plan.md`, sections 1, 3 and 5, and APR-6 and APR-7):

| First decision | Kinds | What the model holds now (section 2) |
| --- | --- | --- |
| D1, how stores are kept apart and where their data lives | `ISO`, `LOC`, `SUB`, `RET`, `ENC`, `AVL`, `CAP`, `ATT`, `PRV`, `STB` | where data lives on Shopify and BigCommerce; nothing on isolation; Salla and Zid nothing on location or card data |
| D2, identity and permissions | `IDN`, `AUD`, `ENC`, `PRV`, `ATT` | Zid's two rows; Shopify's audit log window; Salla's token validity |
| D3, money records and currency | `RET` (`RET-3`), `ATT` (`ATT-1`) | card data on three platforms |
| D4, markets and the seller's country | `LOC` (`LOC-2`, `LOC-3`) | Shopify's EU row |
| D5, events and extension points | `IFB`, `CHG`, `SUB`, `AVL` | rate limits on Shopify and BigCommerce; webhook bounds on BigCommerce and Zid |
| D6, configuration | `STB` | as plan allowances, which are terms |
| Section 5, the quality scenarios | every kind; `SUP` and `ACS` only here | |

Section 5's scenarios are ranked by the founder's quality order (`founder-decisions.tsv`, 29 October: "trustworthiness; then coherence and user experience; then performance; then completeness"). The scale bands engineering states until the founder gives numbers (section 5) read `CAP`.

## 4. Where each platform's quality statements are held

Counted from each repository's guides, registers, ledgers and run indexes, then checked with `held_index.py` for the addresses named. A count by a pattern on addresses is a reading: the pattern finds words in addresses, not things.

**observed-sh, Shopify** (`04de369da`):
- **Trust, security and compliance:**
  - `structures/shopify/compliance-reports/`: 8 documents, 58 page items: two SOC 3 reports, a PCI DSS attestation of compliance for service providers (v4.0.1), and five ASV scan reports (its `documents.jsonl`; its register row: "the SOC 3 reports A1-2026 and A2-2025 (17 pages each ...)").
  - shopify.com's sitemap (`index/ledger/sitemap--shopify-com-sitemap.tsv`, 555 entries): `security/pci-compliant`, `security-response`, `shopify-security.pub` and `security/transparency-report` with its eight yearly reports, all `captured`. `https://www.shopify.com/security` itself is in no sitemap and not held (`held_index.py`).
  - The Help Center: 76 English and Arabic addresses matching privacy or security, 70 matching trust, compliance, GDPR or PCI, all `captured` (a reading, by a pattern on `sitemap--help-shopify-sitemaps.tsv`).
- **Legal terms:** `structures/shopify/legal-documents/`, three runs: `20260930T050139Z-shopify-com-pages` (69 pages, among them `/legal/terms`, `/legal/dpa`, `/legal/processor-list`, `/legal/privacy` and its four audience notices, `/legal/cookies`, `/legal/binding-corporate-rules`, `/legal/gvtaccesspolicy`, `/legal/api-terms`), `20260930T081039Z-shopify-legal-documents` (26) and `20261030T235109Z-legal-payfac-country-compliance` (57); the subprocessor notification page (115 items); the legal index (`shopify-legal-index`, 62 items). No service level document is held or listed: the shopify.com sitemap has no address with "status", "uptime", "sla" or "service-level" (a reading, by a pattern).
- **Status:** `status-page`, "Platform status components and incident history", held only in the fetch archive of run `20260930T080834Z-shopifystatus-api`; `https://www.shopifystatus.com/` in run `20260930T045841Z-published-probe-more`.
- **Developer limits:** shopify.dev's sitemap, 8,868 of 8,871 captured (evidence map); 14 addresses with "limit", "rate-limit" or "quota" (a reading); `/docs/api/usage/limits` held in run `20260930T003705Z-shopify-dev-md` and in this repository's Q1 capture; `admin-graphql-reference-nav`; `dev-changelog` (795 items); `flow-workflow-limits` and `sidekick-quotas`, read by the held pass.
- **Scale and performance:** the pricing pages and Editions, already in the model (section 2); shopify.com's pages.
- **Accessibility:** shopify.com's `/accessibility`, `/accessibility/plan`, `/accessibility/policy` and five conformance reports (`vpat-admin`, `vpat-checkout`, `vpat-shopify-mobile`, `vpat-theme-dawn`, `vpat-theme-debut`), all `captured`; 4 Help Center addresses (a reading).
- **Engineering writing:** `structures/shopify/engineering-blog/` (436 posts, 2010 to 2026, with authors, dates and tags; 7.7 MB of items), `structures/shopify/embedded-videos/` (162 videos' subtitles), and this repository's `evidence/shopify-engineering/` (E001 to E040: 37 web sources and three repositories, captured 10 October 2026; its README: "The detailed write-ups of Shopify's internal payment architecture date from 2019–2022").

**observed-sa, Salla** (`b0bd0b163`):
- **Trust, security and compliance:** no trust or security page in salla.com's four sitemaps (522 to 524 entries each, all held; a reading, by a pattern on `index/ledger/sitemap--com-sitemaps--*.tsv`). docs.salla.dev's `security.md` is held (this repository's capture `20261010T235130Z-q1-salla-sources`, item 010, and observed-sa's run `20261005T234928Z-docs-md`).
- **Legal terms:** `structures/salla/com-policies/` (8 pages: the usage agreement, 623 lines; the privacy policy, 341; payments, shipping, marketing tools, Mushammir AI, `policies/nd96`, the selling policies) and `structures/salla/partners-legal/` (the apps policy, the themes policy, the partners' privacy policy); this repository's captures of 10 `partners.salla.com/legal/` pages (12 addresses, two of them the same page with its Arabic path encoded). The privacy policy states a retention ("يتم الاحتفاظ بالبيانات للفترة اللازمة لتحقيق الغرض من جمعها", line 75) and names Saudi Arabia's law; a reading of a grep: it names no place where data is stored.
- **Status:** `status.salla.sa` and `status.salla.com`, this repository's captures (`held_index.py`).
- **Developer limits:** `docs-index` (816 entries), `docs-operations` (285 operations), `docs-event-lists`; this repository's capture of `docs.salla.dev/rate-limiting.md`.
- **Help:** every article, Arabic and English (`index/ledger/sitemap--help-sitemaps--*.tsv`: 1,669 Arabic and 1,281 English entries `captured`).
- **The dashboard:** `settings-center`, `dashboard-translations`, `portal-settings`, `portal-me`.
- **Scale and performance:** salla.com's pages (`com-llms`, the `com-pages` fetch run), from which the held pass took "100% uptime" and "15 million transactions in one day".
- **Accessibility and engineering writing:** none found in the register or the sitemaps (a reading).

**other-product-class, Zid** (`0d79b794f`), **and this repository:**
- **Trust, security and compliance:** zid.sa's sitemap (this repository's capture `20261012T045101Z-q1-zid-sources`, item 202: 286 addresses) lists no trust, security or status page; it lists `zid-assurance` (captured) and a developer blog post on app security. `status.zid.sa` is not held (`held_index.py`); whether it exists isn't known.
- **Legal terms:** this repository's captures of `zid.sa/{en,ar}/legal/`: the terms, the privacy policy, Zid Pay's terms for Saudi Arabia and Kuwait, the domestic and global shipping terms and the logistics terms; other-product-class's run `20261028T190806Z-terms-pricing-sa-eg` ("zid.sa's and zid.eg's terms, in English and Arabic").
- **Help and docs:** help.zid.sa's sitemaps (held here, 531 addresses) against about 150 of its pages captured (161 help.zid.sa addresses, sitemaps among them, in this repository's runs' manifests); docs.zid.sa's `llms.txt` against 75 pages captured. `zid/GAPS.md`: "Zid's other surfaces: help.zid.sa, docs.zid.sa, zid.sa, the app and theme markets, the mobile apps | not captured here".
- **The dashboard:** `dashboard-locales` (the security levels the model cites, ZD-C-095), `store-plan-policies`, `store-permissions`.
- **Accessibility and engineering writing:** none found (a reading).

**other-product-class, BigCommerce, and this repository:**
- **Trust, security and compliance:** the founder's saves of its company's Trust Center (`evidence/product-class/blocked-evidence-founder/bigcommerce/`): the page (`Commerce Commerce Trust Center ｜ Powered by SafeBase (10_13_2026 ...).html`) and 22 documents, among them the ISO 27001, 27701, 22301, 42001 and 9001 certificates (March 2026), a public statement of applicability (ISO 27001:2022, 27701, 27018, 27017), the EU–US Data Privacy Framework, an international data transfers whitepaper and a transfer impact summary (16 September 2025), a CIO and CISO whitepaper, a PCI compliance guide and the storefront's cookies. `corpus_search.py` reads them through their text. `security.bigcommerce.com` was captured with status 403 (`held_index.py`: "not readable"); `trust.commerce.com` is not held.
- **Legal terms:** runs `20261029T024622Z-legal-pricing-docs` (commerce.com/terms, "Revision: June 1, 2026") and `20261029T025119Z-fees-and-billing`; `structures/contracting-entities`.
- **Status:** `status.bigcommerce.com` not held.
- **Developer limits:** this repository's captures of docs.bigcommerce.com's `rate-limits.md`, `infrastructure-hosting.md`, `pciguide.md` and `pci-compliance.md`, and of support.bigcommerce.com's Platform Limits, PCI Compliance and Security and Privacy Settings articles.
- **Scale and performance:** bigcommerce.com's pages (the uptime the model cites; `product/secure-web-hosting/`).
- **Accessibility:** `www.bigcommerce.com/accessibility/` not held; none other found (a reading).

**WooCommerce** (other-product-class, the release, this repository): the store runs on the merchant's own host, so isolation, location, availability and capacity are mostly the host's (`holder` `merchant`; QL-R7).
- **The release** (`woocommerce-11.2.1`): the bounds its code sets, such as the 30 days of logs the model cites (WC-C-037/decides/WC-S-5373).
- **This repository's captures:** woocommerce.com's `pci-dss-compliance-and-woocommerce`, `marketplace-privacy`, `privacy-payments`, `privacy-shipping`, the WooPayments policies (`pci-compliance`, `know-your-customer`, `reserves`), `support-policy`; developer.woocommerce.com's GDPR and privacy guides, and the Store API's `rate-limiting.md`; Automattic's privacy notice and data processing agreements page.
- **other-product-class:** the `options` structure and the plugins' code (run `20261029T023950Z-plugin-code`).
- **Status:** none held or known.

**In one view** (`held` where a primary source is held and readable; `part` where only some are; `none` where none was found):

| Source | Shopify | Salla | Zid | BigCommerce | WooCommerce |
| --- | --- | --- | --- | --- | --- |
| Trust, security and compliance pages | held | part (developers' security page) | none found | held (founder's saves) | part (payments' PCI) |
| Terms, data processing terms, subprocessors, privacy, retention | held | part (terms, privacy; no data processing terms or subprocessor list found) | part (terms, privacy) | held (terms, transfer papers) | part (Automattic's) |
| Service levels | none listed | none found | none found | none found | none found |
| Status and uptime | held (archive) | held (captures) | none | none | none |
| Developer docs on limits | held | held | part (75 of the docs pages) | held | held (code, docs) |
| Scale and performance claims | held | held | part | held | n/a (merchant's host) |
| Accessibility statements | held | none found | none found | none | none found |
| Engineering writing | held | none found | none found | none found | none found |

## 5. The rows' form

The brief, "The row", has the columns: `subject` (the ask), `outcome`, `kind`, `form`, `basis`, `cap_id`, `holder`, `quality`, `value`, `source`, `locator`, `quote`, `identifier`, `date`, `scope`, `source_type`, `read`, `searched`, `capture`, `could_change`, `reading`.

**One row per quality found.** `found` rows carry the platform (the file's folder), the kind, the capability or `platform`, the value in the platform's words (a verbatim part of the quote), its source at a commit with its locator and quote (or a held id), its scope (plan, market, API), its date, its source type, and a reading.

**A kind searched and not found:** `not-found`, with `read` (the guides' rows, the documents read, at the part's commits, named on the notes' first line) and `searched` (each search, its tool, language and terms; `nothing` where it printed nothing). PLAN's Stage 0 rule applies: "An index or a sitemap doesn't count, and a held corpus left unsearched rules that kind out."

**A kind not held:** `not-held`, with `read` and `searched`, the place that would state it (a ledger row, a sitemap entry not captured, a `GAPS.md` row, or a held page's link), `capture` in the second stage's form, and `could_change` (`D1` to `D6`, `S` or `no`).

**The platform as a whole.** A quality whose words cover the platform or all of a store's data takes `cap_id` `platform` (QL-R2). The model holds these in `studies/class-model/qualities/platform.tsv`, beside the parts:
- columns `cap_id` (`platform`), `platform`, `quality`, `value`, `key`, `kind`, `form`, `basis`, `holder`, `scope`, `date`, `source_type`, `part`, `line`;
- its key is a held entry (the passage's, in `entries-s2.tsv`) or a concern-map statement, so it resolves as every other key does;
- the merge takes its rows into `merged/qualities.tsv` with part `QL`;
- no capability is made for it. B-extent: "**When something becomes a capability:** where at least one platform gives it a place of its own: an admin section or route, an API group, a plan line, or an app category." A trust page or a certificate is none of these. So isolation, encryption, the company's certifications and accessibility, which no capability holds, sit on `platform`.

## 6. The landing

**Reuse or extend.** `s2_held.py land` can't take these rows as they are:
- its subjects are a part's cells and misses;
- its row has no kind, form, basis, holder, value or date;
- it has no target for `platform`;
- a quality on a held cell often cites a key the cell already cites, which `held_amend.py apply` refuses ("a part is refused where a planned row's (`cap_id`, `platform`, `key`) is already in its evidence", S2-held-design, section 3.5).

**Proposed:** a new script, `method/ql_qualities.py`, that imports `s2_held.py`'s source forms, commit and repository tests, the quote test at a locator, and its entry ids, and writes into the same held files. So `class_slice.py`, `check_class_part.py` and `km_page.py` take its entries unchanged, and `held_entries.py` and `held_amend.py` need one small change each.

### 6.1 `method/ql_qualities.py`

**For the agents:**
- `asks --part P [--left]`: the part's asks, each with its kind and question; the model's quality rows of the platform labelled as the kind (`qualities/labels.tsv`); the kind's default capabilities with the platform's cells (held, placed as, reading), and the second stage's rows on them where landed; the places `qualities/sources.tsv` names for the platform and kind. `--left` lists the asks the part's file has no row for.
- `check --part P`:
  - the form: the header, the field counts, no double quote;
  - every ask of the part has its rows: one or more `found`, or exactly one other;
  - the values of `outcome`, `kind`, `form`, `basis`, `holder`, `could_change` and `source_type` (the seed's codes); `subject`'s prefix matches `kind`;
  - `cap_id` a capability of `merged/capabilities.tsv` or `platform`;
  - `quality` holds no colon and isn't a mark of inclusion (`held_entries.MARKS`);
  - `value` is inside `quote`, folded as `quote_check.norm` folds, or inside the held id's text;
  - each source by `s2_held.py`'s tests: its form, the platform's repository, the part's commits, `line N` with the quote's first words within three lines of N, an archive's offset, the quote found;
  - the columns each outcome takes; `capture`'s form on `not-held`; the reading's single-quoted quotes found; the notes' first line;
  - NOTE lines, not problems: a `found` row whose label or value the term rules (section 7) match ("a term? QL-R1"); a `found` row on `platform` whose kind has a default capability ("on the platform, not CM-...?").

**For the coordinator:**
- `parts [--write]`: writes `qualities/parts.tsv` (`part`, `platform`, `kinds`, `asks`, `commits`, `model`, `state`), refusing to rewrite it once a part is checked;
- `mark --part P --state checked|open`;
- `land --platform P [--batch B] [--dry-run]`: lands the platform's parts at `checked`, each checked again first. It refuses a part with a problem, and a batch already applied (a correction lands as `QL-<XX>-R<n>`). For each `found` row:
  - **its entry:** where `source` is a held entry's id, that entry; where it is a concern-map key or a placed inventory id, the key itself; otherwise an entry of `held/<platform>/entries-s2.tsv`, by the second stage's id (`<PREFIX>-E-` and 8 hex digits of `sha1("second-stage\x00" + <repository>:<path> + "\x00" + <locator> + "\x00" + fold(<quote>))`), structure `second-stage`, `labels` the QL part, `section` the row's `identifier`, `text` the quote. The structure is the second stage's so that `held_entries.py check` tests its quote at its source (it does so for `second-stage` entries only), and `class_slice.held_items()` gives it its own citation. The same passage found by the second stage and by this pass is one entry;
  - **on a capability:** a line of `held/<platform>/placements-QL-<XX>.tsv` (H-held's columns): `entry_id`, `placement` `quality`, `cap_id`, `supports` `shows`, `scope`, `terms` and `filler` empty, `quality` `<quality>: <value>`, and `reading` the row's, followed by `(the qualities pass: qualities/<platform>/<part>.tsv line <n>)`. A row whose key is a concern-map statement goes to `held/<platform>/s2-keys.tsv` instead, with `batch` `QL-<XX>`, `supports` `shows` and its `quality`;
  - **on `platform`:** a row of `qualities/platform.tsv`;
  - **its label:** a row of `qualities/labels.tsv` (section 7.1), `label` `quality`, with the row's kind, form, basis, holder, date and source type, `decided_by` `QL-<part> line <n>`.

  It also writes: `held/batches/QL-<XX>.txt` (the batch's entry ids, an existing entry included where a row names it); a row of `held/batches.tsv` (`QL-<XX>`, the platform, the count, `second-stage`); `held/<platform>/notes-QL-<XX>.md` (its first line the parts' commits; the counts by outcome and kind; the rows not landed, and why); `qualities/outcomes.tsv` (the other outcomes: `batch`, `subject`, `kind`, `outcome`, `part`, `line`, `commits`, `read` and `searched` clipped, `capture`, `could_change`, `reading`); `qualities/captures.tsv` (every capture lead, with its row); and `qualities/coverage.tsv` (for each platform and ask: `found` with its count, or its outcome, with the commits). It is idempotent, and refuses to drop an entry of `entries-s2.tsv` that a placements file names, as `s2_held.py land` does.
- `labels propose|review|apply-review|check|clear` (section 7).

### 6.2 What changes in the other tools

- **`held_entries.py check`:** accepts the placement `quality`. Its `cap_id` is a capability, its `supports` is `shows`, and its `quality` is `<what>: <value>` and not a mark of inclusion. The `CHANGES` lines print it as a quality. Everything else stands.
- **`held_amend.py`,** for a `quality` line, and a `QL-<XX>` row of `s2-keys.tsv`:
  - the quality row is written into the part that holds the cell, as today;
  - a `shows` evidence row is written only where the cell doesn't already cite the key;
  - a cell that held nothing becomes held, as for any landed line, and its reading says "Nothing in the concern map; the qualities pass (QL-<XX>) adds <quality>: <value> (<entry>)". `shows` never enters the count (`class_kinds.py`), so no kind changes;
  - with `--batch`, a quality line is refused only where the same row (`cap_id`, `platform`, `quality`, `value`, `key`) is already in the part's `qualities.tsv`, not where the key is already in its evidence.
- **`check_class_part.py`:** no change. Its `HEADS` stand. A landed quality's key resolves: `stmt_index()` reads `citable()`, which includes `held_items()`, which reads `entries-s2.tsv` (`class_slice.py`, lines 175 to 177). The `cap_id` is the part's own capability, since `held_amend.py` writes into the part that holds the cell.
- **`class_merge.py`:**
  - reads each part's `derived-qualities.tsv` beside its `qualities.tsv`, and carries `scope`;
  - gives every row a `row_id`: `QR-` and the first 10 hex digits of `sha1(cap_id \x00 platform \x00 quality \x00 value \x00 key)`, lengthened on a collision. No two of the 3,881 rows share one at `7b618bbf`, by script;
  - takes `qualities/platform.tsv`'s rows, with part `QL`;
  - joins `qualities/labels.tsv` by `row_id`, and writes two files with one header, `cap_id`, `platform`, `quality`, `value`, `key`, `part`, `row_id`, `scope`, `label`, `kind`, `form`, `basis`, `holder`, `date`, `source_type`: `merged/qualities.tsv` for the labels `quality` and `other`, and `merged/terms.tsv` for `term`;
  - a row with no label goes to `qualities.tsv` as `unlabelled`. With `--complete`, an unlabelled row, or a label naming no row, is a problem; without it, a flag.

  Its checks of concerns, cells and rulings don't change.
- **`class_kinds.py`, `review_select.py`:** no change. The kinds count placements, never qualities; the final review's selection reads the parts' own files.
- **`km_page.py`:** section 7.4.
- **`method/README.md`:** a row for `ql_qualities.py`, and the changes above in its rows for the others.

### 6.3 After the landing

`check_class_part.py` on each part `held_amend.py apply` names; `class_merge.py --complete`; `ql_qualities.py labels check`; `km_page.py`. Then `architecture/plan.md`, section 1's row "The qualities the class states" and APR-7's paragraph are measured again from `merged/qualities.tsv` and `qualities/coverage.tsv`, before GM.

## 7. The relabelling

### 7.1 The ledger

`studies/class-model/qualities/labels.tsv`: `row_id`, `cap_id`, `platform`, `quality`, `key` (for reading it), `label` (`term`, `quality` or `other`), `kind`, `form`, `basis`, `holder`, `date`, `source_type`, `decided_by` (`rule:<id>`, `review`, or `QL-<part> line <n>`), `reading`.
- **The labels:**
  - `term`: a price, a fee, a rate charged, a trial, a discount, a credit or reward offered, or a plan allowance, by QL-R1's line (`PLAN.md`: "Prices, fees and plan allowances are the plans' terms, not qualities");
  - `quality`: one of the plan's four forms, with its kind;
  - `other`: neither, such as a feature's own parameter (a payout's day, a carrier's delivery time, a third party's joining conditions). It is kept as it is, beside the qualities (question 3).
- **It is the only place a label lives.** The parts' `qualities.tsv` are never edited, so `check_class_part.py` passes as before on every part, and the merge's other checks don't change.
- **It is reversible.** `labels clear --rule <id>` removes a rule's labels; removing the file leaves every row `unlabelled` in `merged/qualities.tsv`, which is then today's file with more columns. A row whose part is corrected gets a new `row_id`, so its old label names no row, and `labels check` says so.

### 7.2 The rules

`ql_qualities.py labels propose --write` applies these in order, each by patterns on the row's `quality`, its `value`, and the structure of its key's held entry (`held/<platform>/entries.tsv`). It never overwrites a label decided by review or by a QL part.
1. **`Q1`, a measure of the system:** the label names a system measure (uptime, availability, PCI, SOC, ISO, certification, audit, encryption, TLS, hosting, region, residency, subprocessor, retention, deletion, a rate limit, requests, per second, bandwidth, timeout, file size, response time, support, service level, session, token, retries, webhook, logs) and no money word: `quality`, with the kind its words match.
2. **`T1`, money:** the label names a price, a fee, card rates, a trial, a discount, cashback, a promotion, an offer, repayment, interest, commission, a surcharge, billing, a reward, a payout, financing, an annual or monthly price, an add-on or a bundle (and their Arabic: سعر، رسوم، عمولة، خصم، تجربة); or the value states an amount of money and the label names no system measure: `term`.
3. **`T2`, a plan allowance:** the label names a count of something granted (staff, accounts, logins, locations, expansion stores, storefronts, catalogues, products, users, employees, features, "plans that include it"), and the key's structure is a plan structure (`pricing-page-data`, `plan-page-public`, `plan-page-admin`, `plan-comparison-public`, `plan-comparison-admin`, `plan-feature-set`, `billing-plans`, `dev-store-plans`, Salla's `merchant-plans`, Zid's `plans-offered` and `store-plan-policies`, BigCommerce's `plan-comparison`) or its words name a plan: `term`.
4. **`T3`, a plan structure's other line:** any other row from a plan structure: `term`.
5. **Otherwise `unsure`,** for review.

**What they give, at `7b618bbf`** (a reading: a scratch version of these patterns, which the script's will refine): `T1` 2,926 rows, `T2` 282, `T3` 102, `Q1` 136, `unsure` 435. By platform, the `unsure` rows are Shopify 253, Salla 109, WooCommerce 42, Zid 22, BigCommerce 9. Samples show what the review meets:
- real bounds the rules miss: "variants per product | up to 2,000", "execution time | under 5 milliseconds", "lock after inactivity | 10 minutes";
- `other` values: "day withdrawn balance reaches the bank", Salla's carriers' delivery times, Zid's "Jahez joining conditions";
- a rule's errors to watch: T3 holds "funds arrive | within days if approved", a commitment on a payout's timing, and "conversion compared with other platforms", a claim.

### 7.3 The review and the check

- **The review** (`labels review`): the `unsure` rows, printed in chunks with each row's capability, key and structure, go to one agent, `QL-L`, with the brief's "What a quality is, and what it isn't" and the checklist. It writes `qualities/labels-review.tsv` (`row_id`, `label`, `kind`, `form`, `reading`), and `labels apply-review` takes it in, `decided_by` `review`.
- **The coordinator's check of the rules:** a seeded sample of 40 rows from each of `Q1`, `T1`, `T2` and `T3`, read against the row. Where a sample holds more than two wrong labels, the rule's patterns are fixed and the rules are run again, before the review.
- **`labels check`:** every merged row has a label; every label names a row; the rows of `merged/qualities.tsv` and `merged/terms.tsv` together are exactly the parts' rows and `platform.tsv`'s; the counts by label, rule, kind and platform.
- **Its cost:** the rules and checks are scripts. The review is about 435 rows, at an assumed 3 to 8 million tokens.

### 7.4 The Knowledge Map's page

`km_page.py` reads `merged/qualities.tsv` and `merged/terms.tsv`, and `qualities/coverage.tsv`:
- **On each capability,** two lists for each platform's cell: its qualities, each with its kind and form, value and source; and "The plans' terms (n)", folded by default, each with its value and source. Today's single list, each row marked "quality" (template line 350), goes.
- **A new view, "Qualities by kind":** the 16 kinds down, the five platforms across. Each cell shows what is found, with its values; or "searched, not found at `<commit>`", with what was read; or "not held", with its capture request where there is one; or "not read yet". It is never "absent", except where a row is `absent` from a complete list, which shows its list. Under each kind, the qualities on `platform`. This follows Stage 4A: "A cell with nothing held reads as nothing held, never as absent."
- **The counts line** gives the qualities and the terms apart.
- **The data** (`D` in `km_page.py`): `qual` rows gain kind, form, scope and label; `terms` beside them; `qkinds`, the checklist (code, name, characteristic, decisions); `qcover`, the coverage rows. The page still refuses merged files that differ from its commit.

## 8. The split, and the estimate

**The parts,** up to four at once (the founder, 30 October). Every part answers all 44 asks of its kinds:

| Part | Platform | Kinds | Its main sources |
| --- | --- | --- | --- |
| `QL-SA` | Salla | all 16 | com-policies, partners-legal, docs.salla.dev, help articles, status captures, settings centre |
| `QL-ZD` | Zid | all 16 | zid.sa's legal pages and `zid-assurance`, the help and docs captured here, the dashboard's locales and plan policies |
| `QL-BC` | BigCommerce | all 16 | the Trust Center saves, commerce.com's terms, docs and support captures |
| `QL-WC` | WooCommerce | all 16 | the release, woocommerce.com's and Automattic's pages, the plugins' code |
| `QL-SH-1` | Shopify | `LOC`, `SUB`, `RET`, `ENC`, `ATT`, `PRV`, `SUP`, `ACS` | legal-documents, compliance-reports, shopify.com's security and accessibility pages, the Help Center |
| `QL-SH-2` | Shopify | `IDN`, `AUD`, `AVL`, `IFB`, `STB`, `CHG` | shopify.dev, the Help Center, `status-page`, `dev-changelog`, the held entries already in the model |
| `QL-SH-3` | Shopify | `ISO`, `CAP`, and `AVL`'s and `LOC`'s engineering statements | `engineering-blog`, `embedded-videos`, `evidence/shopify-engineering/` |

Shopify is cut in three because its sources are the deepest: about 4.7 MB of legal documents' items in the three runs (3.2 MB of them the payment facilitator's country terms), and 7.7 MB of engineering posts. `QL-SH-3` writes only `found` rows for `AVL` and `LOC` (their asks are `QL-SH-1`'s and `QL-SH-2`'s); its other asks, `ISO` and `CAP`, are its own.

**The order:**
1. `QL-SA` alone first, checked and landed end to end (`land`, `held_entries.py check`, `held_amend.py plan --batch QL-SA`) before the others run, and its cost per row measured. Salla is chosen because two of the three named kinds (where data lives, and the certifications behind it) are most open there (section 2), because its sources need Arabic and English, and because it exercises observed-sa's structures, this repository's captures and a fetch archive in one part.
2. Then four at once: `QL-ZD`, `QL-BC`, `QL-SH-1` and `QL-SH-2`.
3. Then `QL-WC` and `QL-SH-3`, with `QL-L`, the labels' review, which can run at any time after `labels propose`.

**The estimate, an assumption to be measured on `QL-SA`:**
- **The rows assumed:** 44 asks a platform. Shopify about 90 to 140 rows over its three parts; the others about 45 to 80 each, most asks ending at one row. In all, about 290 to 470.
- **The rate a row assumed:** 150,000 to 300,000 tokens. A row here starts from a search, as the second stage's do (assumed there: 150,000 to 350,000 on Shopify and Salla, 100,000 to 250,000 elsewhere, `S2-held-design.md`, section 4), but its documents are long legal and engineering texts, read in parts.

| Item | Rows | Million tokens |
| --- | --- | --- |
| `QL-SA` | 50 to 80 | 8 to 20 |
| `QL-ZD` | 45 to 75 | 7 to 18 |
| `QL-BC` | 50 to 80 | 8 to 20 |
| `QL-WC` | 45 to 75 | 7 to 18 |
| `QL-SH-1` | 40 to 60 | 8 to 18 |
| `QL-SH-2` | 40 to 60 | 8 to 18 |
| `QL-SH-3` | 15 to 40 | 6 to 15 |
| `QL-L`, the labels' review | 435 labels | 3 to 8 |
| The coordinator's checks, at 15 to 19 percent of the agents' (`method-report.md`, section 18, as the second stage's design cites it) | | 9 to 25 |
| The tools built and tested, the inspection, the landing, the amendments and the merge | | 10 to 20 |
| **The qualities pass, in all** | **about 290 to 470 rows** | **about 75 to 180** |

- **Against the plan:** its entry of 31 October assumes about 75 to 150 million. This estimate's top is about 30 million above it, from Shopify's engineering part and the labels' review.
- **The measure:** `QL-SA`'s tokens a row, by outcome (`method/count_tokens.py`), re-project the rest. Shopify's rate is measured again on `QL-SH-1`.
- **What keeps it down:** a kind's words searched in one call per language; the primary document read first, by its headings; the plainest passage, then stop (QL-R4); the model's own rows printed by `asks`, so held passages are named, not quoted again; a fresh agent past about 200,000 tokens of context.

**Effort:** `high`, the founder's floor. `QL-SA`'s check searches again one in three of its `not-found` rows, with other words. If a missed passage turns up, the later parts' `not-found` rows run at `xhigh` (the founder, 30 October: "Where `high` or `xhigh` consistently misses important details for a type of task, evidence review above all, that type runs at `xhigh` or `max`").

**The coordinator's check of each part (proposed):**
- the checker's lines;
- every `found` row of `ISO`, `LOC`, `SUB`, `RET`, `ENC`, `IDN` and `ATT`, read against its source, since D1 and D2 rest on them;
- every row on `platform`, every `absent`, `unreadable` and `unclear`, and every `could_change` of `D1` to `D6`;
- a seeded sample of the other `found` rows (one in five) and of the `not-found` rows (one in three on `QL-SA`, one in five after).

## 9. Capture requests

`PLAN.md`, Stage 4A: "What isn't held becomes a capture request only where it could change an architecture decision." Section 6, Evidence: a request names a run, and "only what no run can capture goes to the founder, with what exactly to capture and why". So a `not-held` row with `could_change` `D1` to `D6` becomes a handoff; one whose `capture` is `none:` becomes a question to the platform, through the founder; `S` goes into the extent report's list of gaps; `no` goes nowhere (QL-R6).

**The likely cases,** from section 4 (a reading, before any part runs):
- **Salla, where data lives and its certifications** (`LOC-1`, `ATT-1`, `ATT-2`). Every salla.com page in its sitemaps, every help article, the policies and the developers' security page are held. If none states them, there is no published page left to capture: the row is `not-found`, not `not-held`, and what Salla doesn't publish goes to the platform as a question, through the founder. No handoff is drafted for it.
- **Zid, where data lives, its certifications and staff sign-in** (`LOC-1`, `ATT-2`, `IDN-1`). zid.sa's sitemap lists no trust page, and its legal pages are held. But most of help.zid.sa (531 addresses in its sitemaps, about 150 captured) and much of docs.zid.sa (its `llms.txt` against 75 pages) aren't held. If `QL-ZD` writes `not-held` on these asks with `could_change` `D1` or `D2`, this request goes out, in `handoffs/`' form, as `H-010`:

> **H-010: Zid's help centre and developer docs, the pages not yet held**
>
> **Repository:** other-product-class, `zid/`. **Instrument:** none: public pages, fetched as the repository's fetch runs are (`docs/OPERATING.md`).
>
> **What to capture:**
> 1. Every address in help.zid.sa's sitemaps (`sitemap_index.xml` and its children, held in sharrwah-knowledge-map's run `20261012T045101Z-q1-zid-sources`) that no run holds, in Arabic and English where both exist.
> 2. Every page docs.zid.sa's `llms.txt` lists that no run holds.
> 3. `zid.sa/en/partners/developers/blog/app-security/` and `zid.sa/ar/partners/developers/blog/app-security/`.
>
> Record each as the repository records a fetch run, with a note in `zid/index/run-notes.tsv`, and add the surfaces to `zid/structures/REGISTER.tsv` and `zid/GAPS.md` as held.
>
> **Stop before:** any sign-in, form or purchase.
>
> **Already held:** the dashboard's runs and structures in other-product-class; in sharrwah-knowledge-map, about 150 help.zid.sa pages, 75 docs.zid.sa pages, zid.sa's legal pages and `zid-assurance`.
>
> **Why:** the class's model, the qualities pass (`studies/class-model/briefs/QL-qualities.md`): Zid's statements on where its data is hosted, its certifications and its staff's sign-in (`qualities/zid/QL-ZD.tsv`, the `not-held` rows named), which bear on architecture's first decisions D1 and D2 (`architecture/plan.md`, section 3).
>
> **Needs:** nothing from the founder.
>
> **Done when:** every address of help.zid.sa's sitemaps and docs.zid.sa's `llms.txt` is held, or listed with the reason it isn't (its status, a redirect, a challenge).
- **BigCommerce:** `security.bigcommerce.com` answered 403, but the founder's saves of the Trust Center hold its documents. A row there is `unreadable` only where a saved document's text can't be read; no run is drafted.
- **Shopify and WooCommerce:** no request is foreseen. Shopify's legal, compliance, status, docs and Help Center pages are held; WooCommerce's hosting qualities are the merchant's.
- **The status pages of Zid and BigCommerce** aren't held, and their addresses aren't known from what is held. A status page reports availability (`AVL-2`): `could_change` `S`, a gap in the extent's report, with no handoff.

## 10. The rulings this brief adds, for the founder's veto

Each is the coordinator's to confirm, and each is listed in plain words at the next report (`PLAN.md`, section 3).
- **QL-R1, where a plan's allowance ends and a quality begins.** *It decides:* a value is one of the plans' terms when it measures money or a quantity the merchant gets with a plan (staff accounts, locations, stores, credits); it is a quality when it measures how the system behaves (requests in a time, a size, a time, a retention window), even when it differs by plan, and its plans become its scope. *Why:* the plan says plan allowances are terms, and API limits by plan are what architecture's events and extension points must design for. *What it risks:* a value that is both, such as a cap on products per plan, is filed by its words, and a reader may file it the other way. *The alternative:* everything stated on a plan table is a term.
- **QL-R2, a quality goes on the narrowest capability it measures, or on the platform as a whole.** *It decides:* where a quality's words cover the whole platform or all of a store's data, it sits on the platform, not on a capability, and no capability is made for it. *Why:* the plan puts each quality "on the capability it bears on", and a certificate of the company bears on no one capability. *What it risks:* the platform's qualities are read apart from the capabilities, so a design reading one capability can miss them; the page shows them under each kind for that reason. *The alternative:* a capability of their own for isolation, encryption and certifications, which the model's rule for a capability ("a place of its own") doesn't support.
- **QL-R3, a reported figure is filed by what it measures.** *It decides:* a past uptime or a peak the platform says it handled is recorded as a commitment or a bound, marked "reported", not promised. *Why:* the plan's four forms have no place for a figure of the past, and architecture's scale bands need such figures. *What it risks:* a reader takes a reported figure for a promise; the `basis` column says which it is. *The alternative:* record only what a platform promises.
- **QL-R4, the plainest passage of the primary document, then stop.** *It decides:* for each question, an agent quotes the passage of the platform's own terms, docs or report that states the value most plainly, and adds another only for a different value, scope, date or holder. *Why:* every further passage costs a read, and one primary statement settles a quality. *What it risks:* a second source that would confirm or date the first isn't collected, so a later reviewer has fewer to cross-check. *The alternative:* cite every passage found.
- **QL-R5, engineering writing and marketing pages are the platform's own account.** *It decides:* they are recorded with their dates and source type, and where the platform's terms or docs state another value, both are recorded and the reading says which is the commitment. *Why:* the architecture plan grades a company's blog as that company's own account, and the engineering posts are the only source on how Shopify keeps stores apart. *What it risks:* an old post describes a design that has since changed; its date is shown beside it. *The alternative:* leave engineering writing to the architecture plan alone.
- **QL-R6, a capture request only for the six first decisions.** *It decides:* a quality not held becomes a capture request only where it could change one of architecture's six first decisions; one that would change only a quality scenario is listed among the extent's gaps. *Why:* the plan asks for a request only "where it could change an architecture decision", and keeps capture the exception. *What it risks:* support and accessibility statements not held stay unrequested, though the founder's quality order ranks user experience second. *The alternative:* a request for every quality not held.
- **QL-R7, who holds the quality.** *It decides:* where the platform says the merchant or the merchant's host holds a quality, as WooCommerce's hosting does, it is recorded as found, held by the merchant. *Why:* the model's rule makes a statement that puts something on the merchant a mention, not a third party's work, and architecture needs to know that the platform promises nothing there. *What it risks:* a reader counts such a row as the platform's quality; the `holder` column says whose it is. *The alternative:* record nothing for it.
- **QL-R8, this pass places nothing.** *It decides:* the pass records qualities only. Where a passage would change how a capability is placed, it is noted for the final review. *Why:* placements are the held pass's and the second stage's, and one reader per placement keeps the counts consistent. *What it risks:* a correction it meets waits for the final review, which reads by risk. *The alternative:* let it add placements too, at the cost of a second check on each.
- **QL-R9, the relabelling's rules and its third label.** *It decides:* the model's existing rows are labelled terms or qualities by stated rules, and the rows the rules can't settle are reviewed once; values that are neither, such as a payout's day or a carrier's delivery time, are labelled "other" and kept. *Why:* the plan asks for the relabelling "by script and kept", and some rows are neither. *What it risks:* a rule's pattern mislabels a row; a sample of each rule is checked, and every label can be undone. *The alternative:* two labels only, with "other" rows kept as qualities.

## 11. Open questions, each with a proposed answer

1. **When this pass lands, against the second stage.** Both read Salla's and Zid's trust cells, some of which hold nothing (CM-TRU-014 and CM-TRU-018 on Salla, CM-TRU-018 and CM-OPS-001 on Zid). *Proposed:* the pass runs beside the second stage, as the plan says, but each platform's `QL-<XX>` lands after that platform's second-stage batch. Its `asks` then prints the second stage's rows on the kinds' cells, so a passage is quoted once. *The alternative:* land as each part is checked, and let `held_amend.py` keep the two batches' lines apart by their keys.
2. **The platform as a whole:** `qualities/platform.tsv` with `cap_id` `platform` (section 5), or capabilities of their own. *Proposed:* the file (QL-R2).
3. **A third label, `other`.** *Proposed:* yes (QL-R9), shown on the page beside the qualities under its own heading.
4. **Who reviews the `unsure` rows.** *Proposed:* one agent, `QL-L`, with the coordinator's sample checks. *The alternative:* the coordinator alone, at about 435 rows.
5. **The merged files:** `merged/terms.tsv` beside `merged/qualities.tsv`, or one file with a label column. *Proposed:* two files, so that a reader who counts `qualities.tsv` counts qualities, as `architecture/plan-review.md`'s APR-7 did by habit.
6. **A cell that held nothing, made held by a quality.** *Proposed:* yes, through its `shows` line, with its reading naming the pass. It never changes a count. *The alternative:* write the quality without an evidence row, leaving the cell `none-held`; but then the model would hold a statement of the thing on a cell that reads as nothing held.
7. **How much of Shopify's engineering writing is read.** *Proposed:* all 436 posts' titles and tags, and the 40 sources' finding aid, searched for the `ISO`, `CAP`, `AVL` and `LOC` words; then up to about 40 posts read in parts, most recent first. *The alternative:* E001 to E040 only.
8. **What Salla and Zid don't publish.** *Proposed:* where a part writes `not-found` on `LOC-1` or `ATT-2` across every published page held, the coordinator brings it to the founder as a question to the platform, and until it is answered the architecture keeps where data lives open as a variation point, bound per market (`architecture/plan.md`, section 4).
9. **The standard itself.** The characteristics are named from memory. *Proposed:* keep them as a reading; they decide no row. If the inspection wants them traced, ISO's public preview of ISO/IEC 25010:2023 (its scope and terms) may be captured into this repository's `evidence/` with its capture tools.
10. **Effort:** `high`, with the re-search sample on `QL-SA`, or `xhigh` for `not-found` rows from the start. *Proposed:* `high` with the sample (section 8).
11. **The existing quality rows.** The 136 rows the rules label `quality`, and the ones the review adds, get their kind by rule or review, not by an agent reading their source again. *Proposed:* `asks` prints them, and an agent who answers an ask with one names its key as the row's source. Their kinds are then confirmed by the part that cites them.
12. **The cost.** The estimate's top, 180 million, is above the plan's 150. *Proposed:* go on, re-project after `QL-SA`, and bring it to the founder only if the extent's projection passes 6.04 billion, the founder's standing rule since 27 October ("The budget must never cost evidence about the references").
13. **`SUP` and `ACS`,** which drive none of the six first decisions. *Proposed:* read, at one ask each, since the quality scenarios need them and the founder's order ranks user experience second.
14. **`STATE.md`.** The second stage's inspection asked it to "say ... who reads the held cells' qualities, since this stage doesn't" (S2I-19). *Proposed:* `STATE.md` names this pass as the reader of `compliance-reports`, `status-page`, `legal-documents` and `dev-changelog` for qualities, and of Salla's `com-policies` and `partners-legal`.

## 12. The coordinator's decisions (31 October)

**On the open questions (section 11):**
1. **Each platform's `QL` batch lands after its second-stage batch,** so a passage the two share is quoted once. Yes.
2. **Platform-wide qualities go in `qualities/platform.tsv`,** not in new capabilities. Yes. The Knowledge Map's page shows them in its "Qualities by kind" table.
3. **The third label, `other`.** Yes.
4. **`QL-L` reviews the rows the rules leave unsettled,** and the coordinator checks a seeded 40 per rule. Yes.
5. **`merged/terms.tsv`, a separate file.** Yes.
6. **A cell that held nothing becomes held through a quality's `shows` row,** where its passage shows the thing exists. Yes: no count changes, and the cell's reading names the quality.
7. **The engineering writing.** Yes: the 436 posts' titles and tags are searched first, then up to about 40 posts are read.
8. **What Salla and Zid don't publish.** It is recorded as `not-found` at its commits. Whether to ask the platform is the founder's, as a commercial contact, and it is listed in the extent's report. Meanwhile, the architecture keeps where data lives open, bound per market (`architecture/plan.md`, section 3).
9. **The ISO/IEC 25010 column stays a reading,** and decides no row. Yes.
10. **Effort.** `high`, with `QL-SA`'s re-search of a third of its `not-found` rows. Yes.
11. **The model's existing quality rows are cited by key,** not quoted again. Yes.
12. **The cost.** Go on, by the founder's standing decision of 27 October. The projection reported at about 21:00 is 6.3 to 6.9 billion (`method-report.md`, section 18). It is re-projected after `QL-SA`. A new projection goes to the founder if its top passes 6.9 billion.
13. **Support and accessibility.** Yes: one ask each.
14. **`STATE.md` names this pass as the reader of the held cells' qualities.** Yes. That covers Shopify's `compliance-reports`, `status-page`, `legal-documents` and `dev-changelog`, and Salla's `com-policies` and `partners-legal`, and answers S2I-19.

**On the rulings (section 10):** `QL-R1` to `QL-R9` are confirmed. Each is listed for the founder's veto in `reports/GM-rulings.md`, in the four parts given here.

**On the capture request:** H-010, for help.zid.sa's and docs.zid.sa's pages not held, stays a draft. It goes out only if `QL-ZD` returns `not-held` on where data lives, attestations or staff sign-in, with first decision 1 or 2 (`QL-R6`).

**Order:**
1. The second stage's fixes are checked and committed.
2. One build agent builds `method/ql_qualities.py` and the changes of section 6 to `held_entries.py`, `held_amend.py`, `class_merge.py` and `km_page.py`. It builds on the second stage's fixed tools and is tested on fixtures. No other agent edits those files while it runs.
3. An agent that made none of them inspects the brief and the tools.
4. `QL-SA` runs alone, after Salla's second-stage batch has landed, and is landed end to end.
