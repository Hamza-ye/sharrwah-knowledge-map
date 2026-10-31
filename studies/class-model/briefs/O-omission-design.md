# The omission review: its design, for the coordinator (31 October 2026)

**What this is.** The design behind `briefs/O-omission.md`, drafted by an agent that made none of the model, for the review `PLAN.md`, Stage 4A sets after the held pass and before the final review. It covers:
- what stays unread, per platform and group, counted from the files (section 2);
- the sampling plan, the measure of the rate, and an estimate of the cost, an assumption to be measured on the first agent (section 3);
- the walk from the evidence's side, and where it differs from what the held pass read (section 4);
- the findings' form and their landing (section 5);
- the split into agents, and how each is assured to have made none of the model (section 6);
- what it hands the final review (section 7);
- the tooling, specified for a build agent (section 8);
- the rulings it adds, for the founder's veto (section 9), and the open questions, each with a proposed answer (section 10).

Nothing here is built yet. `method/om_sample.py` and the changes in section 8 come before the brief's inspection, so the inspector can test them on fixtures, as `inspection-Q3M.md` tested `q3_misses.py` and the second stage's inspection tests `s2_held.py`.

**What was read, at which commits:** this repository at `0c1b3ad6` (`PLAN.md` sections 3, 6, Stage 4A and 11; `STATE.md`; `founder-decisions.tsv`; `held-vs-read.md` and `.tsv`; `held/selection.tsv`; `method-report.md` sections 17 and 18; the briefs `B-extent.md`, `S2-held.md`, `S2-held-design.md`, `R-extent.md`, `N-new.md`; `handoffs/README.md`; `evidence-map.md`; `held/shopify/amendment-notes.md`; `inspection-S2.md` as committed at `0c1b3ad6`, "in progress, not yet checked"; and the tools' headers and `--help`). observed-sh at `04de369da`, observed-sa at `b0bd0b163` and other-product-class at `0d79b794f`: their guides, registers, `index/` and ledgers, by grep. The counts below come from those files by scratch scripts that import `held_entries.py` and `held_vs_read.py` read-only (`held_entries.py registers`, `items_of` with and without the selection's cutting rules); `om_sample.py groups` recomputes every one of them at the review's commits.

**The reading this design rests on.** The held pass and its second stage read from the model's side: each entry was given a capability, each empty cell was searched for. An omission is what that direction can't see: a piece of evidence nobody turned into an entry or a search, or one that was turned into the wrong one. So the review takes each group of what stays unread, draws from it by seed, and asks of each piece whether the model holds its thing. And it walks the platforms' own top-level lists, place by place, against the model's capabilities. That is a reading of Stage 4A's sentence; the plan's own words are quoted in the brief.

## 1. The design in one view

1. **The groups and the draw.** After the second stage is landed (every `S2-<XX>` batch applied, and `S2-NEW` if it runs), `om_sample.py groups --write` counts what stays unread per platform and group at fixed commits, and `draw --write` draws phase 1 by seed (section 3). `assign --write` cuts the sample and the walk into parts (section 6), and `s2_held.py om-parts --write` adds each part to `held/s2-parts.tsv`, so the finding rows land through the second stage's script.
2. **The agents** (`O-omission.md`), each fresh, given the brief alone. Each writes `omission/<part>-items.tsv` (one row per item: its verdict, and its miss), `held/<platform>/s2/<part>.tsv` (the finding rows, in the second stage's form) and `held/<platform>/s2/<part>.md` (its notes).
3. **The check.** `om_sample.py check --part <part>` until no problem, which runs `s2_held.py check --part <part>` too. Then the coordinator's check (section 5.4).
4. **The landing.** `s2_held.py land --platform <p> --batch S2-<XX>-R<n>`, then `held_entries.py check` and `held_amend.py plan` and `apply --batch S2-<XX>-R<n>`, then `check_class_part.py` and `class_merge.py --complete`, as for the second stage's later rows. New things go to `held/new.tsv` and the amendment parts; captures to `handoffs/`.
5. **The rates.** `om_sample.py rates --write` over every part; phase 2 is drawn in each stratum where phase 1 found a miss, read by the same parts' brief, and measured again.
6. **Then the final review.** `review_select.py` takes the review's findings that didn't land as items of reason `omission` (section 7), and the coordinator corrects them with the final review's own findings.

## 2. What stays unread, per platform, by group

"Unread" means cited by nothing the model reads: not by the concern map, a landed subject's statement, a held entry of any batch (the held pass's `entries.tsv`, the second stage's `entries-s2.tsv`), nor, for a run's page, a structure built from it (section 8.1, `read()`). The counts in 2.3 and 2.4 come from `held-vs-read.tsv` and the run folders, which count as read only what the concern map and the subjects cite: they are upper bounds until `groups` credits the held pass's and the second stage's entries. The second stage's own counts (group 5) don't exist until it lands.

### 2.1 Group 1: the structures the held pass didn't select, or read as already read

Two kinds:
- **1a, `read: no` in `held/selection.tsv`** (121 structures), each with its reason. Fifteen of the reasons send the structure to the second stage "where a cell needs it", or name this review: Shopify's `dev-changelog` ("sampled by the omission review"), `help-section-children` ("Help titles are read in the second stage, by cell, on every platform, and sampled by the omission review"), `status-page`, `legal-documents`, `compliance-reports`, `dev-mcp-instructions` and `admin-translations` ("searched by the omission review"); Salla's `help-articles` ("sampled by the omission review"), `help-tree`, `help-embedded-tree`, `marketplace-apps`, `com-policies` and `partners-legal`; Zid's `dashboard-locales`; BigCommerce's `standard-formats`. The second stage reads them only for the cells holding nothing, so a thing they show that no capability holds reaches no one but this review.
- **1b, not in the selection, as read by the concern map** (`held_entries.py registers`: the register's structures the model's citations already cite). Most are cited whole. Four are cited in part, and twelve have no items file the register counts, so the measure can't say what was read:

| Structure | Items | Cited | Uncited |
| --- | --- | --- | --- |
| Shopify `app-store-taxonomy` (categories 161, cited whole; `category-features` 2,612 pages, none cited) | 2,795 | 161 | 2,634 |
| Shopify `app-store-listing` | 113 | 0 | 113 |
| Shopify `plan-comparison-public` | 105 | 102 | 3 |
| Shopify `account-destinations` | 10 | 9 | 1 |
| Shopify, no items file: `help-sitemaps`, `dev-section-children`, `webhook-topics`, `theme-store`, `dev-dashboard`, `community`, `polaris-site`, `legal`, `storefront-sitemap`, `storefront-ucp-profile`, `ucp-agent-profile`; Salla `portal-report-builder-reports` | | | read by file |

| Platform | Structures | Items not cited (every label) | The largest |
| --- | --- | --- | --- |
| Shopify | 69 (54 of 1a, 15 of 1b) | 200,812 | `admin-translations` 97,550; `admin-graphql-schema` 28,271; `shopify-com-translations` 18,515; `web-route-manifests` 8,414; `docs-front-matter` 7,992; `help-center` 5,412; `open-source` 4,656; `storefront-graphql-schema` 3,468; `flow-step-environment` 2,948; `app-store-taxonomy` 2,634; `dev-access-lines` 2,460; `help-section-children` 2,317; `checkout-translations` 2,170; `sidekick-message-streams` 1,823; `dev-changelog` 1,570 |
| Salla | 61 (60, 1) | 19,991 | `help-sitemaps` 3,669; `help-articles` 2,938; `com-policies` 2,578; `com-sitemaps` 2,094; `mahally-sitemaps` 1,192 |
| Zid | 2 | 33,722 | `dashboard-locales` 33,722 |
| BigCommerce | 2 | 490 | `standard-formats` 245; `localization-countries` 245 |
| WooCommerce | 3 | 343 | `countries-states` 250 |
| **In all** | **137** | **255,358** | |

An item is a line of a structure's items, in every label it is held under (`held-vs-read.md`, "How to read the measure"), so a string held in two languages counts twice: a reading, that the counts overstate the distinct things.

### 2.2 Group 2: the items of a selected structure it cut

Three kinds, counted as distinct renderings (the build's own `render` and `fold`), each against the renderings the rule keeps:
- **2a, a rule that leaves items out** (`where:`, `labels:`, `latest:`, `drop-match:`, `new-vs:`, `read-as:`):

| Platform | Structure | Rule | Renderings left out |
| --- | --- | --- | --- |
| Shopify | `help-notes` | `where:class=note note-plan|…;labels:en` | 7,467 |
| Shopify | `pricing-page-data` | `labels:` 21 of 61 sites (method report, section 18: "All 61 sites would have given 8,230") | 7,174 |
| Shopify | `merchant-changelog` | `labels:@posts` (the feed and home page: "list the same posts") | 2,452 |
| Shopify | `editions` | `labels:fall2026` (the other editions read from `editions-page-data`) | 2,096 |
| Shopify | `admin-router-versions` | `new-vs:admin-router` | 1,364 |
| Shopify | `app-store-built-in-features` | `where:tag=h3|h4|h5|span` | 754 |
| Shopify | `shopify-cli-commands` | `latest:id,topic` | 122 |
| Shopify | `ui-extension-targets` | `latest:target` | 77 |
| Shopify | `plan-page-public` | `drop-match:^tag: td;read-as:…` | 66 |
| Shopify | `dev-docs-nav`, `editions-page-data` | `drop-match:`, `labels:` | 4, 1 |
| Salla | `docs-sidebar` | `where:type=apiDetailFolder|folder` | 756 |
| Salla | `dashboard-app-routes`, `portal-app-routes` | `where:path!=;drop-match:…` | 372, 18 |
| Salla | `com-plans`, `com-specialplan` | `labels:^en` | 0, 0 (no rendering beyond those kept) |
| | **In all** | | **Shopify 21,577; Salla 1,146** |

  Many of these are the same things in another form, by the selection's own reasons (the same posts, the same routes in an older version, the same lines in another language). A reading: they will mostly come back `held`, cheaply, and that is what a measured rate should show.
- **2b, a `drop:` rule that leaves words out of an item:** the items whose dropped fields hold words their rendering lacks, counted the same way. Shopify `admin-router` 121 (`intent`, `action`, `model`, `form`; `held/rules/admin-router.md`, rule 1, has them read in `items.jsonl`) and `admin-router-versions` 2; Salla `changelog-entries` 20 (`content`, every entry), `dashboard-restrictions` 14, `design-page-types` 2, `app-categories` 1; BigCommerce `plan-comparison` 6 (`feature`); WooCommerce `payments-providers` 82 (`onboarding`, `management`, `links` and the rest) and `woopayments-onboarding` 4. 252 in all. Left out of the count as the capture's or the page's own apparatus, a reading: `merchant-changelog`'s `run`, `status` and `class` (1,646), `editions-page-data`'s media fields (840), `dev-docs-nav`'s `children` (84, which `nested:` renders as items of their own).
- **2c, what an extractor dropped from its source,** named by the evidence map and the amendment notes, read whole (a census):
  - Zid `dashboard-page-index`: 18 of its source's 137 page objects, among them the charity store's titles, which "would make CM-SEL-007's Zid cell held" (`evidence-map.md`);
  - BigCommerce `contracting-entities`: the Feedonomics and Makeswift rows (the concern map holds both);
  - Shopify `admin-home-setup`: the ARIA lines its source writes in single quotes (the B2B guide's card, the dropshipping lesson);
  - Shopify `shopify-cli-commands`: each command's first paragraph only, no flag descriptions (110 of 138 commands in 5.0.0, 51 of 133 in 4.8.3; "The omission review reads what the items leave out", `amendment-notes.md`). Not a census: 161 commands, drawn as a stratum;
  - Shopify: three settings items and one node with no entry ("Items the build leaves without an entry, for the omission review", `amendment-notes.md`).

### 2.3 Group 3: the help centres', docs' and sites' pages no cell cites

Addresses held readable as a published page (a fetch archive's record, or this repository's capture runs), from `held-vs-read.tsv` at `d116b43f`, by host:

| Platform | Unread | By host (the largest) |
| --- | --- | --- |
| Shopify | 20,902 | shopify.dev 9,714; help.shopify.com 5,538; themes.shopify.com 1,730; changelog.shopify.com 1,648; shopify.com 1,587; apps.shopify.com 598; community 37 |
| Salla | 7,396 | help.salla.sa 2,954; salla.com 2,094; api.salla.dev 1,151; docs.salla.dev 833; apps.salla.sa 135; partners.salla.com 103; community 70; mahally.com 28 |
| Zid | 82 | help.zid.sa 51; zid.sa 19; zid.eg 6; docs.zid.sa 5 |
| BigCommerce | 209 | bigcommerce.com 104; support.bigcommerce.com 73; docs.bigcommerce.com 27 |
| WooCommerce | 41 | woocommerce.com 30; wordpress.com 5; developer.woocommerce.com 3 |
| **In all** | **28,630** | |

These count as read only what the concern map and the subjects cite. The held pass's entries read many of these pages through structures (`merchant-changelog` names each post's address, `help-notes` each help page's), so `groups` will count fewer: changelog.shopify.com's 1,648 should mostly drop out. Which form an address is held in decides its group, by `held_index.py`'s forms: `warc` and `capture` here, `step` and `answer` in group 4, `structure` in groups 1 and 2.

### 2.4 Group 4: the runs' pages

Every browser step's page text and every saved answer, per run of `index/runs.tsv`, whatever its host (the measure's host filter misses BigCommerce's and WooCommerce's own store hosts, so they are counted from the run folders):

| Platform | Runs (unread of all) | Step texts | Saved answers |
| --- | --- | --- | --- |
| Shopify | 438 of 446 | 11,523 (and 23,330 ARIA files) | 113,774 lines of `answers.jsonl` |
| Salla | 213 of 215 | 4,973 | 85,701 response files |
| Zid | 18 of 20 | 1,354 | 26,346 lines |
| BigCommerce | 14 of 15 | 540 | 1,729 lines |
| WooCommerce | 13 of 14 | 843 | 881 lines |

These are files, with repeats. `groups` counts distinct pages (a step's text, folded, once per run kind) and distinct answers (an address and its body's hash), leaves out a step or answer that is a selected structure's source (its `meta.json` names it) or that the model cites, and keeps only the platform's own hosts for answers (`held_vs_read.HOSTS`, with the store's own host from `instruments.json`).

### 2.5 Group 5: the second stage's `not-found` and `not-held` rows

Its population, once the second stage is landed: the rows of `held/<platform>/s2-outcomes.tsv` of outcome `not-found` or `not-held` whose cell is still `none-held` in `merged/cells.tsv`, and the rows of Q3's misses' parts of those outcomes. Before it runs, a bound: at most 620 cells (Shopify 56, Salla 86, Zid 138, WooCommerce 161, BigCommerce 179; `s2_held.py parts`) and 26 miss parts on each platform, 130 in all. Assumed: 250 to 430 cell rows and 70 to 110 miss-part rows, from the held pass's yield (method report, section 18: the batches after the first changed few cells) — an assumption, replaced by the count when it lands.

Two findings of the second stage's inspection, in progress, bear on this group (`inspection-S2.md` at `0c1b3ad6`):
- **S2I-2:** "the omission review samples this stage's `not-found` rows (the coordinator's decision 9), so a cell written `not-held` leaves its sample". So group 5 takes `not-held` rows too (question 1).
- **S2I-22:** a cell corrected from `not-found` to `found` "kept its `not-found` row ... in `s2-outcomes.tsv`. That is the file the omission review samples." So the population is filtered by the cell's state in the merged model, not by the outcome row alone.

### 2.6 Group 6: what the held pass placed `out` (proposed, question 2)

The held pass's own claim that something isn't the model's: the lines of `placement` `out` in `held/<platform>/placements-*.tsv`, each entry once: Shopify 414, Salla 380, Zid 1, WooCommerce 74, BigCommerce 0, 869 in all; and the 18 rows of `held/new.tsv` decided `out`. The task's list doesn't name this group. A reading: an `out` line is the most direct omission the held pass could make, and nothing after it reads them again.

### 2.7 Group 7: what isn't held at all, from the repositories' own lists (proposed, question 3)

Stage 4A: "What isn't held at all, it names as capture requests." The repositories' ledgers list what each platform lists and isn't captured. Distinct entries, by the ledgers at the commits above:
- **Shopify:** admin routes no store visited, 339 of the router's 1,364 (needs an instance 281, splat 37, no path 21; `index/ledger/admin-route.tsv`, the best status across stores); journey units not attempted, 34; Help Center pages in English or Arabic not attempted, 7,839; shopify.com pages in English or Arabic not attempted, 63,171; app store listings not attempted, 44,653 (third parties' listings);
- **Salla:** reports not reached 34, dashboard apps not reached 75, partners portal apps not reached 6, settings fields not reached 3, navigation pages reached but not rendered 3;
- **Zid:** dashboard routes not opened, 107 (`zid/index/ledger/dashboard-routes.tsv`);
- **every platform:** each `GAPS.md` row, read whole (a census; BigCommerce and WooCommerce keep no ledger).

Left out, a reading: the community sitemaps (340,642, members' posts, not the platform's account of itself), the theme store's (50,048), and the Help Center's and shopify.com's other languages (75,744 and 250,353), which state what the English and Arabic pages state, as the coordinator measured for pricing (method report, section 18).

### 2.8 The walk's lists

Not a group, a census (section 4). Its size is counted by `walk` from the lists. Assumed, from the registers' item counts: 1,500 to 2,500 top-level places across the five platforms.

## 3. The sampling plan, and the estimate

### 3.1 The draw

- **The unit** is one item of a group's population: a structure's item (or file), a cut rendering, a page, a step or answer, a second-stage row, an `out` line, a ledger entry.
- **The strata:** group 1 and 2a/2b, each structure; group 3, platform and host; group 4, platform and form (step or answer); group 5, platform and kind (cell or miss part); group 6, platform; group 7, platform and denominator.
- **The seed** is `20261031`. Each stratum's population is sorted by its item id (section 8.1), and shuffled with `random.Random("20261031:<group>:<platform>:<stratum>")`, a string seed, which Python hashes the same way on every run. Phase 1 takes the first n of that order, phase 2 the next n. So a stratum's draw never depends on another stratum's, and phase 2 extends phase 1.
- **The commits:** the evidence repositories at the commits the second stage's parts fixed (`held/s2-parts.tsv`, `commits`), and this repository at the commit of the merged model after the second stage's last batch is applied. `sample.tsv` records them, and the agents' messages name them. What a repository holds that is newer than those commits goes to the held pass's selection first, as `PLAN.md`, section 6 asks (question 7).

### 3.2 The sizes, phase 1 (ruling, proposed: `O-R4`)

One rule for the strata of groups 1, 2, 3 and 7, by the stratum's size N: 1 item where N is at most 20 (and in group 1, where N is at most 1,000); 3 to 1,000; 6 to 10,000; 10 above. A structure group 1a's reason sends to the second stage or to this review takes 10, or all where it has fewer. Groups 4 to 6 take a fixed number per stratum, since their strata are few and their value per item high: group 4, 10 per platform and form; group 5, 20 cells and 5 miss parts per platform; group 6, 10 per platform, and all 18 of `new.tsv`'s `out` rows. Each, or all where the stratum holds fewer.

| Group | Population (2) | Strata | Phase 1 items | 95% bound on the rate with no miss, pooled (1 − 0.05^(1/n), about 3/n) |
| --- | --- | --- | --- | --- |
| 1 | 137 structures, 255,358 items | 137 | 290 (Shopify 144, Salla 121, Zid 11, BigCommerce 11, WooCommerce 3) | 1.0% |
| 2 | 22,723 cut renderings; 252 items with dropped words; 2c's census | 24, and the census | about 96 (2a 51, 2b 13, 2c about 32) | 3.1% |
| 3 | 28,630 pages, before the held pass's credit | about 35 | 100 (Shopify 41, Salla 34, Zid 7, BigCommerce 12, WooCommerce 6) | 3.0% |
| 4 | 19,233 step texts and 228,431 answers, files | 10 | 100 | 3.0% |
| 5 | assumed 320 to 540 rows | 10 | 125 | 2.4% |
| 6 | 869 lines and 18 decisions | 5 | 49 | 5.9% |
| 7 | 116,264 ledger entries kept, and the `GAPS.md` rows | 11, and the census | 44 (Shopify 32, Salla 9, Zid 3), and every `GAPS.md` row | 6.6% |
| **In all** | | | **about 800, with the walk beside it** | |

Why these sizes, a reading: about 100 items a group puts the bound on a group's rate near 3%, which says whether a group needs a full read. One item from every structure tests the held pass's reason for not reading it, the claim most likely to hide a thing. The fixed sizes for groups 4 to 6 keep a platform's rate there worth knowing (a bound near 14% at 20 items with no miss), where a miss changes a cell.

### 3.3 What an agent does with each item

The brief, "For each item": read it whole at its source; say what it states in the platform's words; say whether it is a thing (B-extent: "A capability is something a store or the platform can have or not have"); only then look it up in the model (`O-R1`); write the verdict (`held` with its basis, `not a thing`, `miss` of its kind, or `unclear`), and for a miss that can land, a finding row (section 5).

A **miss** is an item whose thing the model doesn't hold as it should: `cell` (a capability holds it, the platform's cell holds nothing), `support` (the cell is held without a support value the item shows), `new` and `no place` (no capability holds it, with or without a place of its own), `out` (a line placed out that is a thing of the class) and `capture` (only a place not held would show it). `held`, `not a thing` and `unclear` aren't misses; `unclear` is reported beside the rate.

### 3.4 The rate and its bound

`om_sample.py rates` reports, per group, platform and stratum:
- N, n, and k by miss kind, with `cell`, `support` and `new` (those that change a cell, a count or the model's structure) counted apart from the others;
- the rate k/n, and its one-sided 95% upper bound by Clopper and Pearson: the p at which the binomial chance of k or fewer misses in n is 5%. With k = 0 it is 1 − 0.05^(1/n), about 3/n. Where n is more than a tenth of N, the hypergeometric bound on the misses in N replaces it;
- the misses the group holds, estimated as the sum over its strata of N·k/n, a reading, since the strata's sampling fractions differ; and a conservative bound, the sum of N times each stratum's bound;
- for group 5, the second stage's own miss rate: misses among its rows read, which says how many of its `not-found` rows would be found by a second reader. `cause` counts why.

The pooled rate of a group (all its k over all its n) is the rate per item read across its strata. It equals the group's rate only where its strata share one rate: a reading, stated in the report.

### 3.5 Phase 2 (`O-R4`)

In each stratum where phase 1 finds a miss of kind `cell`, `support`, `new` or `out`, or a `capture` whose `could_change` is `kind` or `decision`, `draw --phase 2` takes as many items again, the next in its seeded order, for the same part's brief. Where phase 2 finds another such miss in the stratum, the coordinator decides how the stratum is read whole: by the held pass's brief where it is a list, by cell where it is pages. Before the final review where its misses could change a kind or a decision; otherwise listed in the extent's report, with its rate, for after GM.

### 3.6 The estimate, an assumption to be measured on the first agent

**The rates assumed per item:**
- a list's item (groups 1, 2, 6, 7): 30,000 to 80,000 tokens. The held pass's light lists cost 38,000 to 76,000 an entry (ZD-4, WC-1, WC-2; method report, section 18), and an item here adds the model's lookup;
- a page (groups 3 and 4): 80,000 to 200,000. The calibration's pages with descriptions cost about 190,000 an entry (method report, section 18);
- a second-stage row (group 5): 100,000 to 300,000, the second stage's own assumption per row (`S2-held-design.md`, section 4), since the agent searches the cell afresh;
- a walked place: 5,000 to 10,000 for each place in the compact view, and 30,000 to 80,000 for each one read whole (flagged or sampled).

| Item | Count | Million tokens |
| --- | --- | --- |
| Lists' items | 290 + 96 + 49 + 44 = 479 | 14 to 38 |
| Pages | 200 | 16 to 40 |
| Second-stage rows | 125 | 13 to 38 |
| The walk: every place in the compact view, and those read whole | 1,500 to 2,500, of which 300 to 500 read whole | 17 to 60 |
| The `GAPS.md` census | about 60 rows | 1 to 3 |
| The coordinator's checks, at 20 to 30 percent of the agents' (method report, section 18) | | 12 to 54 |
| The sampler and the script changes, built and tested; the brief's inspection | | 5 to 15 |
| **Phase 1, in all** | | **about 80 to 250** |

Phase 2 adds as many items as phase 1 drew in the strata with a miss; with misses in a tenth of the strata, about 10 percent more.

- **Against the plan's figures:** `PLAN.md`, section 11, 30 October, put the held pass and the omission review at "about 80 to 180 million agent tokens in all, an assumption to be measured on the first batches"; the method report's projection at 21:40 put the omission review at about 50 million. Both came before the held pass was measured at about ten times its estimate. A reading: at this design's top, the extent's projection rises.
- **The measure:** `OM-ZD`'s tokens per item by group (`method/count_tokens.py` and its transcript), then Shopify's and Salla's on their first parts. They re-project the rest.
- **The lean alternative** (question 4): 5 items for a delegated structure, groups 3 and 4 halved, group 5 at 10 cells and 3 miss parts per platform, group 6 at 5 per platform, and 1 in 10 of the walk's unflagged places: about 550 items and about 50 to 150 million, the bounds about 1.4 times wider.

## 4. The walk from the evidence's side

**What it reads.** Each platform's own top-level lists, through its guides, each place against the model's capabilities. The lists, from the guides and registers (`om_sample.py`'s `WALK` table, section 8.1):

| Platform | Admin sections and routes | API groups | Plan lines | App categories | Read beside them (no place of their own) |
| --- | --- | --- | --- | --- | --- |
| Shopify | `admin-main-nav`, `admin-settings-nav`, `settings-panel`; `admin-router`, by its first path segment; `partner-dashboard-nav`, `dev-dashboard-nav`; `mobile-app-navigation`, `pos-app-navigation`, top level | `admin-graphql-reference-nav`; `dev-docs-nav` | `plan-comparison-public`, `plan-comparison-admin`, `plan-feature-set` | `app-store-taxonomy`, its categories to the second level | `help-section-children`'s top sections; `admin-translations`' namespaces (125 with no English twin, `amendment-notes.md`) |
| Salla | `dashboard-main-navigation`, `dashboard-settings-menu`, `dashboard-menu-*`, `settings-center`'s sections, `partners-portal-navigation`; `dashboard-app-routes`, by first segment | `docs-navigation`; `docs-sidebar`'s folders | `com-plans`, `com-specialplan`, `plan-gates` | `app-categories`, `portal-categories`, `app-store-tabs` | `help-tree`'s categories |
| Zid | `dashboard-page-index`, with the 18 pages its extractor dropped (2c); `dashboard-route-manifest`, by first segment | none held (`zid/GAPS.md`: docs.zid.sa "not captured here"; this repository's pages where held) | `store-plan-policies`, `plans-offered` | none held (`zid/GAPS.md`: "the app and theme markets ... not captured here") | `dashboard-locales`' `navbar` namespace; `store-permissions`' groups |
| BigCommerce | `settings-list` (its addresses shifted, H-009); the control panel's menu, where `bigcommerce/README.md`'s runs hold it | the API reference's navigation, in this repository's docs pages | `plan-comparison` | `channel-catalog`'s categories | `payment-gateways`, `tax-services` |
| WooCommerce | `release-admin-menus`, `release-settings` (tabs and sections) | `release-rest-controllers`, `release-webhook-topics` | none held | `core-profiler-free-extensions`' bundles; `payments-providers`' suggestion categories | `release-features` (flags) |

A list the agent's guides show and the table lacks goes in its notes, and the coordinator adds it.

**How it differs from what the held pass read.**
1. **Direction.** The held pass took each entry and gave it a capability, under B-extent's convention "A place whose thing a capability already holds, as its cells' readings show, is that capability's evidence, not a new one." A wide capability could take a place with a thing of its own. The walk asks the converse for each place: is its thing the thing the capability's definition names?
2. **Whole lists.** The held pass's batches cut a list at about 100 entries, and each batch saw its own. The walk sees a list's top level at once, so a capability that takes several places of one list shows (`absorbed`).
3. **Lists the held pass didn't read:** `app-store-taxonomy`'s category features, the help trees' sections, the vocabularies' namespaces, the extractor's dropped pages. These are not places of their own by B-extent's five kinds, or are read as such only where the platform names them so; they are read beside the places, for a thing the model lacks.
4. **Flags, mechanical,** so that only the places most likely to be missed are read whole (`O-R3`): `unread`, `out`, `shows`, `no shared word` and `absorbed` (the brief, "The walk"). The unflagged places are sampled, 1 in 5 by the seed and at least 3 per list, so the flags' own miss rate is measured.

## 5. The findings' form, and their landing

### 5.1 A cell that holds nothing but should

A `found` row of the second stage's form in `held/<platform>/s2/<part>.tsv`, its subject the cell's cap_id, its `read` beginning `item <id>`, so it traces to its item. It lands as the second stage's later rows do (S2-held-design, section 3.2): a held entry in `entries-s2.tsv` (structure `second-stage`, its id the same hash), a placement in the next correction batch `S2-<XX>-R<n>`, `held_entries.py check`, then `held_amend.py apply --batch S2-<XX>-R<n>`. The cell then cites the passage as it cites any held entry.

Where the cell's reading already holds the second stage's `not-found` sentence, `apply` replaces it with both: "The held pass's second stage (S2-ZD) read the held pages at <commits> (held/zid/s2/S2-ZD-1.tsv, line <n>) and found nothing; the omission review (S2-ZD-R<n>, held/zid/s2/OM-ZD.tsv, line <m>) found it in <source>." So the second stage's miss stays visible in the model, where the rate counts it (section 8.3). This needs the fix S2I-22 proposes, that a correction batch replaces a cell's sentence.

### 5.2 A new thing

A `new` row (subject `new`, outcome `found`, cap_id `new:<name>`, `place` its place of its own or `none`), as `S2-held.md`, "What takes a row", writes one, with the notes' entry for it. It lands as the held pass's `new:` lines are decided: the coordinator decides it across the platforms in `held/new.tsv` (as `briefs/N-new.md` proposes: an existing capability, a new capability made in an amendment part, or out), and the amendment part makes the capability with every platform's cell (`briefs/M-amend.md`). Those cells are read against the held pages by one more part of the second stage before the final review, as the coordinator's decision 8 on the second stage set for its own new capabilities (question 10).

### 5.3 A capture request

Only where it could change the model or a decision. `PLAN.md`, section 6: "exists but isn't captured: a capture request, where the thing could change the model or a decision". The second stage's triage holds (its decision 6): "`kind` and `decision` go to a handoff in `handoffs/`, `count` into the extent report's list of gaps, `no` to neither."
- **On a cell:** a `not-held` finding row, with `capture` in its form and `could_change`. It lands in `held/s2-captures.tsv`, from which the coordinator writes the handoff.
- **For a thing no capability holds** (a list not held whose places the model may lack, such as Zid's app market): the notes give it in `handoffs/README.md`'s parts ("Repository and instrument", "What to capture, step by step, and where to stop", "Already held", "Why", "Needs", "Done when"), with its `could_change`. The coordinator writes the handoff file.
- Before either goes out, the coordinator checks it against what is held, as `handoffs/README.md`, step 1, asks.

### 5.4 What doesn't land, and the coordinator's check

- `support`, `out` (where no finding row carries it), `unclear`, and the walk's `absorbed` capabilities stay in the items file, each with its passage. They go to the final review (section 7).
- **The coordinator's check of each part:** the checker's lines; every finding row against its source, since each `found` changes a cell; every `support`, `out` and `unclear` row; each new thing and each capture with `could_change` `kind` or `decision`; and a seeded tenth of the `held` and `not a thing` rows read again, since a wrong `held` is a miss of this review, which the rate would hide.

## 6. The split into agents, and how each made none of the model

**Parts,** each of one platform, so the landing's batch is one platform's, and each agent reads one repository's guides once:

| Part | Platform | Takes | Items, phase 1 (about) |
| --- | --- | --- | --- |
| `OM-ZD` | Zid | every group, the walk | 11 + 18 + 7 + 20 + 25 + 1 + 3 = 85, the walk, `GAPS.md` |
| `OM-SH-1` | Shopify | groups 1, 2, 6, 7, the walk | 144 + about 60 + 10 + 32 |
| `OM-SH-2` | Shopify | groups 3, 4, 5 | 41 + 20 + 25 |
| `OM-SA-1` | Salla | groups 1, 2, 6, 7, the walk | 121 + 11 + 10 + 9 |
| `OM-SA-2` | Salla | groups 3, 4, 5 | 34 + 20 + 25 |
| `OM-BC` | BigCommerce | every group, the walk | 11 + about 3 + 12 + 20 + 25 + 0 + census |
| `OM-WC` | WooCommerce | every group, the walk | 3 + 4 + 6 + 20 + 25 + 10 + census |

An agent past about 200,000 tokens of context stops at the end of a chunk; a fresh agent continues the part from its files (`show --left`). `OM-BC` and `OM-WC` may be one agent in turn, since both read other-product-class's guides.

**The order,** up to four at once (the founder, 30 October: "Up to four agents at once ... If agents start being stopped mid-run, the coordinator runs fewer"):
1. `OM-ZD` alone. It is checked and landed end to end (`land --batch S2-ZD-R<n>`, `held_entries.py check`, `held_amend.py plan`), and its tokens per item measured, before the others run, as the second stage's `S2-ZD-1` went first.
2. `OM-SH-1`, `OM-SH-2`, `OM-SA-1` and `OM-BC` with `OM-WC`.
3. `OM-SA-2`.

**How each is assured to have made none of the model:**
- **By construction.** Each agent is spawned new, with the brief alone in its message. No agent that wrote a part, a batch, a second-stage row, an amendment, a ruling or the veto list's drafts is resumed or sent the task, and the coordinator, who made the model, only checks.
- **By record.** `omission/parts.tsv` holds each part's agent id and the time it was spawned, the coordinator's entry; the notes' second line says "made none of the model: a fresh agent, given only briefs/O-omission.md". `method/count_tokens.py` lists the session's agents by transcript, so the coordinator can show that no omission agent's transcript is one that wrote a file under `studies/class-model/parts/` or `held/`.
- **By method.** The agent reads the evidence first and decides what an item states before it reads the model (`O-R1`). For group 5, `reveal` shows the second stage's row only after the agent's own verdict is written, so its search isn't the second stage's again.

**Effort:** `high`, the founder's floor (question 5). Group 5 runs at the level the second stage's `not-found` rows ended at: the second stage's decision 4 moves them to `xhigh` "if a missed passage turns up". A reader less careful than the one it checks would understate the rate.

## 7. What it hands the final review

1. **The model with the findings landed.** The final review's selection (`review_select.py`) runs after the omission review's batches are applied, so a cell this review made held is read by its usual reasons, `kind` and `count` among them.
2. **Items of a new reason, `omission`** (section 8.4): every items row of miss `support` or `out`, every `unclear`, every `absorbed` capability of the walk, and every finding row that gives a cell `core` or `own-service`, each with its passage. The reviewer answers whether the passage shows what the row says, and what the cell's placement, or the capability, should be. The coordinator corrects them with the final review's own findings: a reading of Stage 4A's "Its findings are corrected with the final review's" (question 6).
3. **The rates** (`omission/rates.tsv` and `omission/report.md`): per group, platform and stratum, with their bounds, and the second stage's own miss rate with its causes. They go into the extent's report at GM, so the founder sees what was missed as a measure, not an assumption.
4. **The captures** raised, in `handoffs/`, and the `count` gaps for the extent report's list.
5. **The new things** decided, with the amendment parts that make them and the part of the second stage that reads their cells.

## 8. The tooling

### 8.1 `method/om_sample.py`, new

**Inputs:** `held/selection.tsv`; each repository's `structures/REGISTER.tsv` through `held_vs_read.structures()`; `held_entries.items_of()`, `rules()`, `render()`, `fold()`, `says_something()`, `strings_of()`, `candidate_index()`, `candidates()` and `earlier_keys()`; `held/<platform>/entries.tsv`, `entries-s2.tsv`, `placements-*.tsv`, `s2-outcomes.tsv`; `held/new.tsv`; `held/batches.tsv`; `merged/cells.tsv`, `evidence.tsv`, `capabilities.tsv`; `held_vs_read.read_sources()` and `held_index.Held` for addresses and their forms; each repository's `index/runs.tsv`, `index/ledger/*.tsv`, `index/instruments.json`, `GAPS.md` and run folders; this repository's `evidence/product-class/runs/`. The repositories' roots are `q3_misses.py`'s `ROOTS`. The model's folder is `studies/class-model`, or `CLASS_MODEL_DIR` for tests. It writes only under `studies/class-model/omission/`.

**`read()`, what counts as read** (`O-R5`): an item is read where the concern map or a landed subject cites its file and line or its address (`held_vs_read.read_sources()`); where a held entry of any batch, or of `entries-s2.tsv`, has its file and line as `source` and `locator`, or names its address in its text or locator; or, for a run's step or answer, where it is the source a selected structure's `meta.json` names.

**Item ids:** `<group>-<PREFIX>-<8 hex>`, the hex the first of `sha1(<group> + "\x00" + <repository>:<path without commit> + "\x00" + <locator or pointer>)`, lengthened on a collision as `held_entries.stable_id` does. A group 5 item's locator is `<part> line <n>` of `s2/<part>.tsv`; a group 6 item's is its placements file and line; a walked place's id is `W-<PREFIX>-<8 hex>` of its list and words.

**Commands:**
- `groups [--platform P] [--write]`: each group's and stratum's population N, at the commits; `--write` writes `omission/groups.tsv` (`group`, `platform`, `stratum`, `N`, `unit`, `note`). It prints problems where a selected structure's rule can't be read with its cutting rules removed, or a ledger's column is missing.
  - group 1: per structure of `selection.tsv` with `read` `no`, and per registered structure not in the selection whose items aren't all cited; the unit an items line not cited, or a file of the structure's folder (but `meta.json`) where it has no items;
  - group 2a: per selected structure with a cutting rule, the renderings of `items_of()` with the rules `where`, `labels`, `latest`, `drop-match`, `new-vs` and `read-as` removed that no rendering with them holds (folded); 2b: per selected structure with `drop:`, the items whose dropped fields hold a string of three or more characters that their rendering lacks, leaving out the fields named in `DROP_APPARATUS` (`run`, `status`, `class`, `children`, and the media keys of `editions-page-data`'s rule); 2c: the list `EXTRACTOR_CUTS`, each entry a file and its lines or items, from `evidence-map.md` and `amendment-notes.md` (section 2.2);
  - group 3: the addresses `held_index` holds as `warc` or `capture`, on the platform's hosts (`held_vs_read.HOSTS`), not read, one per `page_key`, the stratum its host;
  - group 4: each run's step page texts (`steps/NNN.text.txt`, or observed-sh's `derived/step-text-from-html/`) and saved answers (`answers.jsonl` lines, observed-sa's `responses/NNNN.json`) on the platform's hosts and its store's own host from `instruments.json`, not read; a step once per folded text within its run kind, an answer once per address and body hash; the stratum `step` or `answer`;
  - group 5: `s2-outcomes.tsv` rows of outcome `not-found` or `not-held` whose cell is `none-held` in `merged/cells.tsv` now, and the miss parts' rows of those outcomes; the stratum `cell` or `miss`;
  - group 6: the placements' `out` lines, each entry once (its first batch), and `new.tsv`'s rows decided `out`;
  - group 7: per denominator of `GAPS7` (section 2.7), each distinct entry whose best status across stores is one of `not-attempted`, `not opened`, `not-reached`, `reached-not-rendered`, `needs-instance`, `splat` or `no-path`, the help and shopify.com sitemaps kept to English and Arabic addresses; and each row of each `GAPS.md` (a census).
- `draw [--phase 1|2] [--seed 20261031] [--write]`: the sample, by section 3.2's sizes (`SIZES`, one table in the script) and 3.1's seeding. `--phase 2` draws only in the strata `rates` names. `--write` writes `omission/sample.tsv` (`item`, `group`, `platform`, `stratum`, `N`, `phase`, `rank`, `repository`, `path`, `locator`, `form`, `text` clipped to 300, `commits`), refusing to change a row an items file has answered.
- `walk --platform P | --part P [--write]`: the `WALK` table's lists (section 4), each list's top level by its rule (`top:` the items with no parent, or at depth one or two by the list's own `parent`, `depth` or nesting; `segment:` the first path segment of a route manifest; `all:` every row of a plan table), each place with its words in each language held, its kind, its entries (by file and line), each placement line of every batch, the capabilities' definitions, the platform's cells and supports, and its flags. `--write` writes `omission/walk.tsv`, with the seeded fifth of each list's unflagged places marked `sampled` (at least 3).
- `assign [--write]`: cuts `sample.tsv` and `walk.tsv` into the parts of section 6, writing `omission/parts.tsv` (`part`, `platform`, `groups`, `items`, `walk`, `commits`, `model`, `agent`, `spawned`, `state`). The coordinator fills `agent` and `spawned`.
- `show --part P [--from I --to J] [--left]`: each item, by section 3.3's needs: its group and stratum; where it is held and its readable form (`held_index.py`'s), with how to read it whole (the `quote_check.py --text`, `warc_text.py` or `sed -n` call); its text, clipped; its leads (by identifier, `earlier_keys()` over the model's lines and the placements; by term, `candidates()`). For a group 5 item, the cell as `s2_held.py cells` prints it, without the second stage's row. For a group 1 item, the structure's `reason`. `--left` lists the items the items file has no row for.
- `reveal --part P --item ID`: a group 5 item's second-stage row, refused while the items file has no verdict for it.
- `check --part P`: the items file's form (header, field count, no `"`, no empty `;` piece); one row per item and per walked place `sampled` or flagged; the values of `verdict`, `miss` and `cause`; `miss` only on `miss`; `cause` on group 5 rows only, and filled; `basis` on `held` resolving to an evidence key, an entry id at a listed batch, or a subject's statement, on the item's platform; `cap_id` a merged capability or `new:<name>`; on `miss` and `unclear`, a source of the second stage's forms with its quote found (`s2_held.source_problems()`); `finding` on the kinds that take one, naming a row of `held/<platform>/s2/<part>.tsv` whose subject is the item's cell or `new` and whose `read` begins `item <id>`; every finding row named by one item; `read` and `reading` not empty, and the reading's single-quoted quotes found in the item, its source or a named file. Then `s2_held.py check --part P`. It prints a `NOTE` for each `support`, `out` and `unclear` row, and each item read in under 30 characters of `reading`.
- `rates [--part P] [--write]`: section 3.4's table; `--write` writes `omission/rates.tsv` (`group`, `platform`, `stratum`, `N`, `n`, `k_cell`, `k_support`, `k_new`, `k_no_place`, `k_out`, `k_capture`, `unclear`, `rate`, `bound`, `estimate`, `phase2`) and names the strata for phase 2. The bound is computed by bisection on the binomial distribution, in the standard library alone; the hypergeometric bound where n is more than a tenth of N.

**Tests,** on fixtures in a scratch copy of `studies/class-model` (`CLASS_MODEL_DIR`), citing real held files: a draw that reproduces itself; a phase 2 that extends phase 1; a part with a row of each verdict and miss kind, and its one-fault variants; `reveal`'s refusal; the bound against known values (k = 0, n = 100: 2.95%; k = 1, n = 100: 4.66%).

### 8.2 `method/s2_held.py`

- **`om-parts [--write]`:** reads `omission/parts.tsv`, and adds each part to `held/s2-parts.tsv`: `part` as named, `platform`, `domains` `A to G`, `cells` every cap_id of the platform `none-held` in `merged/cells.tsv` at the model's commit, `misses` empty, `commits` the sample's, `model`, `state` `open`. It never rewrites an S2 row, and refuses an `OM-` part already `checked` or `landed`. **`parts --write`** keeps every `OM-` row as it is.
- **`check_part()` for a part named `OM-`:**
  - no coverage test of the cells or misses: a row's subject is a cap_id of the part's `cells`, or `new`; a miss subject is refused;
  - outcomes `found`, `not-held`, `absent` and `unclear`; `not-found`, `unreadable` refused, with "the items file records what you read";
  - a cell's rows: one or more `found`, or exactly one other, as now;
  - `as` empty;
  - each row's `read` begins `item <id>`, an id of `omission/sample.tsv` or `walk.tsv` assigned to the part;
  - a `found` row's cell is still `none-held` in the merged model at check time, or a problem: "held now: write it in the items file as `support`";
  - the notes are `held/<platform>/s2/<part>.md`, as now; their second line names the review.
- **`land`:** an `OM-` part lands only once every S2 part of its platform is `landed`, and only in a correction batch, `S2-<XX>-R<n>`, under the rule that exists. A placement's reading ends "(the omission review: s2/<part>.tsv line <n>)" for an `OM-` part. The evidence rows' `why` keeps its prefix "(the held pass's second stage, <batch>, <part> line <n>)", which `land`'s test for a batch already applied reads. The batch's notes name the omission review's parts on their second line. `s2-captures.tsv` takes the column `batch`, as S2I-22 proposes.

### 8.3 `method/held_amend.py`

- A cell's reading names the review where the batch's lines come from `OM-` parts: "The omission review (S2-ZD-R1) adds ...".
- Where a cell that an earlier batch wrote as read and not found becomes held, `apply` replaces that sentence, as section 5.1 gives, keeping the second stage's reference and adding the omission review's.
- An `OM-` part's `not-held` or `unclear` outcome on a cell still holding nothing adds its sentence beside the second stage's, as "The omission review (S2-ZD-R1) read <item> at <commits> ...".

### 8.4 `method/review_select.py`, and `R-extent.md`

- **A reason `omission`:** for each `omission/*-items.tsv` row of miss `support` or `out`, of verdict `unclear`, or naming an `absorbed` capability, an item on its cell (`cap_id`, platform), or on the capability for `absorbed`, with "<part> <item>: <miss>: <reading, clipped>"; and for each `OM-` finding row that gives a cell `core` or `own-service`, an item on that cell. The share is the capability's domain's (`share_of`).
- **`R-extent.md`,** under "What each reason asks": "**omission:** a finding of the omission review (`studies/class-model/omission/`, the items file's row and its passage). Does the passage state what the row says? For `support`, is the cell's placement right with it, by B-extent's supports? For `out`, is the thing a thing of the class, and on which capability? For `absorbed`, is each place a capability of its own by B-extent's convention 'When something becomes a capability'? For a landed `core` or `own-service`, does the passage show it?" The brief's reading list gains `briefs/O-omission.md` and `studies/class-model/omission/`.

### 8.5 `method/README.md`

A row for `om_sample.py`, in the form of `s2_held.py`'s: the groups, the draw and its seed, the walk, `show`, `reveal`, `check` and `rates`.

## 9. The rulings this brief adds, for the founder's veto

Each is the coordinator's to confirm, and listed in one plain line at the next report (`PLAN.md`, section 3), in plain words as the founder asked on 31 October.
- **`O-R1`: the evidence first.** *Decides:* the reviewer reads each piece of evidence and says what it states before looking at the model; for a cell the second stage found nothing for, it sees the second stage's search only after its own. *Why:* a reviewer shown the model's answer first tends to agree with it. *Risks:* more reading per item, and a reviewer who searches with weaker words than the second stage did. *Instead:* show the model's lines with each item, at less cost.
- **`O-R2`: a held cell's missing support goes to the final review.** *Decides:* where the review finds that a cell already held should be placed more strongly, it records the passage for the final review, and doesn't change the cell itself. *Why:* the second stage's decision 7 does the same, and the final review rules on placements. *Risks:* a correction the final review doesn't reach waits. *Instead:* land it here, as a finding row on a held cell.
- **`O-R3`: the walk's flags.** *Decides:* each place of a platform's top-level lists is read whole only where a flag marks it (no line, only `out`, only `shows`, no word shared with its capability, or one capability taking three or more places), and a fifth of the rest by seed. *Why:* reading every place whole repeats the held pass at its cost. *Risks:* a forced fit whose words happen to overlap passes unread, at the rate the sampled fifth measures. *Instead:* read every place whole.
- **`O-R4`: the sizes and the second phase.** *Decides:* section 3.2's sizes, and doubling a stratum's sample where it shows a miss, before deciding whether it is read whole. *Why:* about 100 items a group gives a bound near 3%, and more reading goes where misses are. *Risks:* a group whose misses cluster in strata of one item each is measured loosely. *Instead:* the lean sizes, or a fixed share of every stratum.
- **`O-R5`: what counts as read.** *Decides:* a piece of evidence is read where the concern map, a subject, a held entry or a structure built from it cites it; everything else is in a group to sample. *Why:* it is the measure `held_vs_read.py` makes, extended to the held pass. *Risks:* a page read through a structure that kept only its title counts as read. *Instead:* count as read only what a cell's evidence cites.

## 10. Open questions, each with a proposed answer

1. **Group 5's `not-held` rows, and the misses' parts.** *Proposed:* both in the group, the `not-held` rows with `not-found` (S2I-2: otherwise a cell written `not-held` "leaves its sample"), and the misses' parts as their own stratum.
2. **Group 6, the held pass's `out` lines** (869, and 18 decisions). Not in the task's list. *Proposed:* sampled, 10 per platform, the decisions read whole: they are the held pass's own claims of omission, and nothing reads them again.
3. **Group 7, what isn't held at all.** *Proposed:* sampled from the ledgers' not-attempted entries in English and Arabic, and every `GAPS.md` row read: Stage 4A asks for capture requests from "what isn't held at all", and these are where each repository lists it.
4. **The sizes:** section 3.2's (about 800 items, about 80 to 250 million) or the lean ones (about 550, about 50 to 150). *Proposed:* section 3.2's for `OM-ZD`; the coordinator re-projects from its measure, and moves the rest to the lean sizes if the projection's top passes about 150 million. The cost goes to the founder only past the standing threshold (the second stage's decision 10: "only if its projection's top moves past 6.04 billion").
5. **Effort.** *Proposed:* `high`, and group 5 at the level the second stage's `not-found` rows ended at (its decision 4).
6. **When the findings land.** "Its findings are corrected with the final review's" (Stage 4A) could mean that nothing lands before the final review. *Proposed:* what lands by the second stage's script (a `found` row on a cell holding nothing, a capture) lands before the final review's selection, so the review reads the model with it; the rest is corrected with the final review's findings. *The alternative:* hold everything for the final review's correction round, which leaves cells the review never selects unread at GM.
7. **The commits.** *Proposed:* the second stage's fixed commits for the evidence. A repository's later captures join the held pass's selection first, as section 6 of the plan asks, and the omission review samples them only if they land before its draw.
8. **Phase 2's trigger.** *Proposed:* a miss of kind `cell`, `support`, `new` or `out`, or a capture of `kind` or `decision`, in a stratum. A `no place` miss alone doesn't trigger it: it changes no cell.
9. **A high rate.** *Proposed:* a stratum whose phase 2 finds another miss is read whole before the final review where its misses could change a kind or a decision, and listed in the extent's report otherwise (section 3.5).
10. **New capabilities from this review.** *Proposed:* their cells are read against the held pages by one more part of the second stage before the final review, as decision 8 set for the second stage's own.
11. **The coordinator's re-read of `held` verdicts.** *Proposed:* a seeded tenth, counted as the review's own miss rate, beside its rates.
12. **The second stage's inspection.** S2I-2, S2I-10 (a row's `searched` records "only this cell's terms") and S2I-22 (a correction batch replaces a cell's outcome) bear on group 5 and on this landing, which uses the correction batch. *Proposed:* this review's tools are built after those fixes are taken, and `om-parts` is tested against them.
13. **The final review's sample.** *Proposed:* no change to `review_select.py`'s `--sample` by default. Where a platform's group 5 bound passes 10% after phase 2, the coordinator raises that platform's sample of cells for the final review, and says so in the extent's report.
14. **What the second stage leaves of the structures sent to it** (S2I-19, `inspection-S2.md` at `0c1b3ad6`): Shopify's `compliance-reports` serves "the qualities of the trust and payments cells", and CM-TRU-018 is held on Shopify, so the second stage's S2-R2 puts it out of reach; and `pricing-page-data`'s 40 other sites leave "which of the 103 comparison rows each of those 40 sites lists ... a gap for the second stage". *Proposed:* `compliance-reports` is read whole by `OM-SH-1` (58 items), each quality a held cell lacks noted for the final review, outside the rate; the 40 sites' rows are group 2a's `pricing-page-data` stratum, sampled, and a row a site lists that no English or Arabic site does is a miss of kind `new` or `cell`.
