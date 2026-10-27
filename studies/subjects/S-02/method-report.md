# S-02: what each run taught

**What this file is:** what each of S-02's runs taught about running the agents and planning the work, and what changed for the next run (`PLAN.md`, Stage 4, "Each run's lessons"). Costs are by `method/count_tokens.py`, on the agents' transcripts.

## 1. The briefs' inspection (26 October)

- **Cost:** 27.9 million tokens over two rounds (112 requests), against the 5 million the frame set.
- **What it found before any agent ran:** three must-fix points in phase A's brief and one in phase B's, among them held evidence the reading lists missed: nine of Shopify's runs and Salla's markets sweep. The coordinator had built the lists from searches; the inspector went through each repository's run notes and ledgers.
- **What changed:** a reading list starts from each repository's `index/run-notes.tsv` and ledgers, not from searches alone.

## 2. Phase A, Shopify and Salla (26 October, 22:21 to 23:30 UTC)

**What it produced:** 319 statements for Shopify and 304 for Salla, 216 and 220 of them from new reading; every quote found, and no checker error on either.

**What it cost:** 104.7 million tokens for Shopify (226 requests) and 117.8 million for Salla (276), against the 60 million the frame set for both. S-02 stopped at 250.4 million (`PLAN.md`, section 8), and the founder said to continue (`founder-decisions.tsv`, 27 October).

**What it taught:**
- **An agent's context is what it costs.** Each request reads the whole context again. Shopify's context grew from 183 thousand tokens to 746 thousand, with a median of 477 thousand; Salla's reached 781 thousand. An average request cost 0.45 million.
- **A long reading list in one agent grows its context without end.** Both agents passed their stop at 300 statements, and resuming either meant re-reading a context of 750 thousand tokens on every turn.
- **Two agents at once didn't hit the usage limit.** They ran for about an hour together; in the pilot, five at once stopped within 35 minutes (S-01's method report, section 12).
- **Agents copy what is recorded selectively,** and say why: Shopify left out 52 of its 139 recorded rows, each with its reason in its notes.
- **The agents found faults in the tools,** each fixed in the run:
  - Shopify's held schema cuts descriptions at their first line break (`method/schema_type.py` reads them in full);
  - quotes from JSON in a fetch archive didn't match (`method/quote_check.py`);
  - the search listed help articles by a position one less than their line (`method/corpus_search.py`);
  - each check against the schema read the 7 MB record again (`method/quote_check.py` keeps it by offset).
- **Gaps that only an observation would close** went to the founder (Salla's four). Each is a run the local agent could make, so each became a handoff (`handoffs/`; the founder, 27 October).

**What changed for the next runs:**
- **Each remaining reading list is split into parts,** each read by a fresh agent that continues from the files and notes, so no context grows past a few hundred thousand tokens. The paused agents' work is in their files, so nothing is read twice.
- **Phases B and C and the review run per root decision,** three agents each, each reading only the statements its decision's bullets hold.
- **Agents look up rows in large files with scripts,** instead of loading them whole.
- **The budget is 700 million tokens** for S-02 (the founder, 27 October), and it never costs evidence.

## 3. Phase A finished by fresh agents (27 October)

**What it produced:**
- **Salla:** 310 statements, 585 citations; no checker error.
- **Shopify part 1:** 85 new observed statements, from seven runs, the admin's route ledger and controls, and six more stores' general settings. That makes 404 statements and 880 citations, with no checker error.

**What it cost:** Salla's finisher 8.0 million (65 requests). Shopify's part 1, 59.8 million (237 requests).

**What it taught:**
- **A fresh agent with a short task costs far less per request:** Salla's finisher about 0.12 million, against 0.43 million before.
- **A long run still grows its context,** even from a fresh start, because every tool output stays in it. Shopify's part 1 ran 237 requests at about 0.25 million each. So each part is kept to about a hundred requests.
- **A container restart stopped two agents.** Both had written as they went, so nothing was lost, and both were resumed from their transcripts.
- **Agents shared one scratch folder,** and one overwrote another's script. That one had already finished. Each agent now gets its own folder (phase A brief, rule 12).
- **The quote tester read a large file again for each quote,** nine seconds a call on Shopify's 8.8 MB admin controls. It now tests a batch in one process (`method/quote_check.py --batch`).
- **"No ellipses" turned away the platform's own text,** such as a field's "Search countries…". An ellipsis is now refused only where its source doesn't hold it (`method/check_subject.py`). The pilot's check is unchanged.

**What changed for the next runs:**
- Shopify's remaining reading is split in two parts: the observed runs not yet read, then the plan tables, the leads and the gaps' re-check.
- Each agent writes only in its own scratch folder.

## 4. Phase A finished: Shopify parts 2 and 3, Zid, WooCommerce and BigCommerce (27 October)

**What it produced:** phase A for all five platforms, 1,458 statements: Shopify 588, Salla 310, WooCommerce 227, Zid 172 and BigCommerce 161. The checker found every quote, 3,193 of them, and no error. Seven gaps that only an observation would close went to the local agent as capture requests (`handoffs/`, H-001 to H-007).

**What it cost:**

| Run | Requests | Millions | Per request |
| --- | --- | --- | --- |
| Shopify, part 2 | 168 | 39.6 | 0.24 |
| Shopify, part 3 | 112 | 27.8 | 0.25 |
| Zid | 198 | 74.7 | 0.38 |
| WooCommerce | 137 | 47.6 | 0.35 |
| BigCommerce | 98 | 23.1 | 0.24 |

Phase A cost 504 million in all, against the 325 to 375 million the frame set for it. The coordinating session processed 144 million more over the same time, outside the budget, which counts the agents.

**What it taught:**
- **Parts of about a hundred requests held their cost at about 0.25 million a request** (Shopify's parts 2 and 3, and BigCommerce).
- **Zid and WooCommerce each ran in one agent,** and their contexts grew: 0.38 and 0.35 million a request.
- **Reading "from what is recorded" went well past the recorded rows,** to the held pages their gaps needed: Zid wrote 172 statements from 72 recorded rows, WooCommerce 227 from 87, and BigCommerce 161 from 81.
- **The frame's estimates were low.** It set 45 to 75 million for Zid, WooCommerce and BigCommerce, which cost 145 million, and 30 to 50 million to finish Shopify and Salla, which cost 135 million.

**What changed for the next runs:**
- **Phase B runs in parts** (`b/parts.tsv`), each a root decision's bullets, or one bullet for some of its platforms. Each part's size is counted in statement-bullet pairs before it runs, and its cost is measured after it.
- **An inspector tries each brief on a sample before it runs.** For phase B, a dry run of 30 statements gives the rate each part's size is checked against.

## 5. Phase B's brief, inspected twice, with a dry run (27 October)

**What it cost:** the first inspection 2.3 million (22 requests), the second 4.8 million (38 requests).

**What the second one found, by trying the brief on 29 of Salla's statement-bullet pairs:**
- **The rules matched a question's X by its words.** Under (d), Salla's statements give one variation point or six, by how a reader takes "متاحة حاليًا في", "مدعوم في", "Primary markets" and "للعمل في". Under (a) they give three or about nine. About 23 of the 29 pairs needed a call the rules didn't settle. Two agents would not have reached the same points, and RD1's cap would have depended on the agent.
- **A point raised in a later part needed rows for the earlier parts' platforms,** and the brief had the agent read their statements whole: up to 382 statements for the last part of RD3, uncounted in `parts.tsv`.
- **A rule and the checker disagreed** on how a statement that a setting holds for the whole store is written as a variant.
- **The dry run's rate** was about three statement-bullet pairs a request, all in.

**What changed:**
- **X matches by its role,** which each question fixes: one variation point per question under (a), (b), (d) and (e), and one per bound thing or setting under (c) and (f). Each platform's own words go in `x_words`. The brief now defines the store's own country, a setting of the store, and a market a store sells into, with what each excludes.
- **What a value is taken per is named in one of four phrases,** which the checker reads, so the answers compare across platforms.
- **Earlier parts' rows are found by search,** since each earlier part placed its statements under every question they answer. The searches are named in `notes-b.md`.
- **The caps were set again** for points that match by role (`b/ranges.tsv`), and RD3's last part was split in two: ten parts.
- **The slice printer refuses an empty or unknown option,** where it had printed the whole slice; the join writes nothing unless every file joins.

## 6. The third check of phase B's brief, and the absence audit's inspection (27 October)

**What they cost:** the third check of phase B's brief, 3.8 million (28 requests); the absence audit's inspection, 4.5 million (33 requests).

**What the third check found, by dry runs on Salla's (a), (d) and (f):**
- **Under (a), (b), (d) and (e), two agents now reach the same variation points:** one per question. The calls the rules left open fell from about 23 of 29 statement-bullet pairs to about 8, all of them about rows, not points.
- **Under (c) and (f), whether two statements name "the same setting" was still a call:** Salla's first 22 (f) statements raised 22 points for 13 settings. Under (c), Zid's payment services gave one point or four.
- **The search for an earlier platform's rows, by X's words alone, missed answers that reading finds:** a point on the currency of Zid's fees found none of Shopify's statements on billing currencies.
- **A rule merged unrelated points** answered by the same list statement, such as prices with shipping options.

**What changed:**
- **(c) and (f) take X from a list of kinds:** under (c), from (c)'s own words in `bullets.tsv`; under (f), from the platforms' own groupings of a market's settings (Shopify's market page, Salla's sections for a market, BigCommerce's channel-specific settings). A new kind is raised only where none fits.
- **The search reads the earlier platforms' identifiers first,** then searches their words and the point's `x_words`, and logs the words used.
- **Notes count only on lines that start with the id and its bullet,** so a search log can't mark a statement as noted.
- **Answers that rest only on a statement that a platform has no market of the kind say `no market`,** which the checker reads.

**What the absence audit's inspection found, on Zid's gap S02-ZD-G01:**
- **The search tool hid matches:** past its cap it named 30 addresses, then only a count, and the one document holding the field the gap names was among the unnamed. Zid's help-centre menu, on every page, made 25 of the first 40 matches.
- **The brief didn't say whether Zid, WooCommerce and BigCommerce may read live,** so two agents would read different sources.
- **The checker let some of phase A's searched gaps through without an audit row.**

**What changed:**
- `method/corpus_search.py` names every address past its cap, matches a Zid help page on its article alone, and shows a captured page's title.
- The brief names the live hosts for each platform, how to run each search, and what to record whatever the result.
- The checker asks for a row for every claim except the gaps phase A2 leaves after its own searches.

**The fourth check of phase B's brief** (the third checker resumed: 2.9 million, 11 requests) found nothing that must change. Under the kinds, Salla's 22 (f) statements raise 23 points (11 kinds, two questions each, and one new kind), and Zid's payment services fall under two kinds. What it left was at the margin, and went into the brief:
- a (c) kind for the store's own taxes;
- the (f) kinds widened for settings at the margin (gifting, loyalty, the store's app, cookie consent, maintenance, how a buyer's market is chosen), and RD3's cap raised to 59;
- a tax registration that the platform ties to a market isn't the store's own country;
- under (c), "offered to every store" answers with its excerpt;
- the checker refuses two points that share a question and a kind.

## 7. Phase B's parts (27 October)

| Part | Statement-bullet pairs | Requests | Millions | Pairs a request | Variation points | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| RD1-1: (a) and (d), all five platforms | 205 | 74 | 17.8 | 2.8 | 3 | 52 |
| RD3-1: (f) and (g), Shopify | 264 | 65 | 15.2 | 4.1 | 37 | 76 |
| RD1-2: (b), all five platforms, with its re-read of 12 statements | 128 | 48 | 9.8 | 2.7 | 4 | 47 |
| RD3-2: (f) and (g), Salla | 133 | 65 | 15.8 | 2.0 | 7 more (44) | 75 |
| RD1-3: (c), Shopify and Salla | 216 | 59 | 15.0 | 3.7 | 11 more (18) | 69 |
| RD1-4: (c), Zid, WooCommerce and BigCommerce | 198 | 72 | 17.5 | 2.8 | 1 more (19) | 72 |
| RD3-3: (f) and (g), Zid and BigCommerce | 126 | 78 | 22.5 | 1.6 | 6 more (50) | 142 |
| RD3-4: (f) and (g), WooCommerce | 98 | 57 | 12.2 | 1.7 | none (50) | 68 |
| RD2-1: (e) and (g), Shopify | 184 | 46 | 8.1 | 4.0 | 4 | 31 |
| RD2-2: (e) and (g), Salla, Zid, WooCommerce and BigCommerce | 163 | 67 | 12.0 | 2.4 | none (4) | 39 |
| **Phase B's first pass** | **1,715** | **631** | **145.9** | **2.7** | **73** | **671** |

**What RD1-1 taught:**
- **One point per question held:** the five platforms' answers to "what fills the store's own country" fell under one variation point, as 30 fields and records and one gap, and the countries served and kept out under one each.
- **The brief changed during the run,** and the coordinator's message named only one change. The agent found the others and applied them. A message to a running agent now lists every change.
- **Two rules were narrower than needed,** and were widened: a statement's identifier or scope may name what fills X under any bullet, not only (c) and (f); and a `gap` row may stand beside a platform's answers. Six statements the part noted under the narrower rule are read again in the second pass: S02-SH-259, S02-SH-260, S02-SH-396, S02-SA-249, S02-ZD-148 and S02-ZD-149.

**What RD3-1 taught:**
- **The kinds held:** Shopify's settings fell under 19 of the listed kinds, two questions each where Shopify states both, and two new kinds (the store's address, and units and time zone): 37 points.
- **Who sets a value is not only the platform or the seller.** Shopify names Managed Markets with Global-e, Avalara, an app and the buyer. The brief now takes the party the statement names.
- **Conventions the part chose, now in the brief** so the later parts read alike: a control in the store's admin means the seller sets the value; "automatically" or "by default" means the platform; a catalog goes under both products and prices.
- **Its rows quoted every statement in `basis_evidence`,** up to 10,000 characters. The brief now asks for the words that show the basis from the statements that show it best.

**What RD1-2 taught:**
- **Each of (b)'s four questions made one point,** as rule 3 says: who sets, who checks and who changes the store's country, and what must hold before it changes.
- **"Who checks" was read too narrowly.** The part noted 12 statements on verifying a business's information or its address, because their words don't name the country. The store's own country includes where the merchant is registered, and (a)'s answers name the records that hold it, so a check of those records is a check of the country. The brief now says so, and the part re-reads the 12.
- **The admin-control convention covered only `who sets`;** it now covers `who changes` too. A permission or role that gates a change, and the account's owner, stay their own answers, beside the seller's.

**What RD3-2 taught:**
- **A later platform mostly fills the earlier points:** Salla's statements gave rows under 31 of RD3-1's 37 points, and raised 7, for kinds Shopify had stated only one question of, or not at all. Its rows also cost more per pair (2.0), since each point needs Salla's row under it, answer or not.
- **The search for Shopify's rows under the new points found one answer that reading had missed:** RD3-1 had noted S02-SH-374, whose words say the visitor accepts cookies; it now answers `who sets` under privacy and consent.
- **Two calls the part made are now in the brief,** so that the later parts make them alike: a flag or key that says "country" without saying whose fails the role test, and a party that requires a value without setting it isn't who sets it.
- **Each part's own script rebuilt its root decision's files,** from a copy of the earlier part's. A later part that ran an earlier part's script would drop rows, so each part is told to write to the files directly.

**What RD1-3 taught:**
- **(c)'s kinds held:** Shopify's and Salla's statements fell under 11 of its 12 kinds, one point each; none raised a new kind.
- **The flag rule met the scope rule.** Nine Shopify API calls by country code were noted under the flag rule, although their scope names the store's business entity as whose country it is. The rule now counts a flag's identifier and scope too, and the nine are read again in the second pass. The admin forms that carry the same answers were placed.
- **Payment methods had no (c) kind,** and were placed under other payment providers. That kind now names them.
- **The absence audit ran beside the part,** and added Salla statements its slice didn't hold. The part left them for the second pass, as the coordinator's message and now the brief say.

**What RD1-4 taught:**
- **The last part of a root decision closes every point's rows:** all twelve (c) points now have a row for each platform. Of its own platforms' rows, 9 are `not covered` and go to gap-closing (phase A2).
- **The one point it raised, the store's data, found Zid's answer by the search,** in a statement the part had first placed under the contracting party; it moved it.
- **Stripe's entity under WooPayments isn't the platform's company,** so it went under the platform's own payment service, as Shopify's acquirer does: a reading, marked as one.

**What RD3-3 taught:**
- **A later part's cost is in its rows under the earlier points, not its statements:** 126 pairs gave 142 rows, since Zid and BigCommerce each needed a row under every one of the 44 earlier points, 35 of them `not covered`. That made it the costliest part per pair (1.6).
- **The kinds needed four new ones** where BigCommerce's channel settings go past them: the store's country as a channel's setting, apps, analytics, and notifications to the merchant.
- **Rules widened after a part ran leave its notes on the older rule.** RD3-1 noted Shopify's permission statements as conditions of access, and its "you can't change" statements as kept out, before rule 4 took a permission, and "no one can", as answers; RD3-3 read BigCommerce's alike under the new rule. The statements to read again are in `b/second-pass.md`, which the second pass now reads.

**What RD3-4 taught:**
- **RD3's first pass is complete:** 50 points, each with a row for all five platforms; 361 rows.
- **Code needs its own reading of "who sets":** much of WooCommerce's evidence is its release's code. The part read a value or default the code sets as the platform's, and named parties, such as developers, as their own; the brief now says so.
- **A rule lost an answer:** a statement under (g) that names who sets a whole-store setting could answer only "what it takes its value per", so WooCommerce's row for who sets discounts came out `not covered`. The brief and the checker now let it answer `who sets` too, and its statements are on the second pass's list.

**What RD2-1 taught:**
- **(e)'s four questions made four points,** as the brief asks. Shopify defines a market by ten things, from conditions over a set of customers to its sales channels, and its absences rule out three more (a city, a storefront, other groups of customers).
- **"What limits a market" took both how many a store can hold and the rules on what one may hold,** such as a country in more than one market, or a primary market of one country. Both bear on the root decision; the question now names both.
- **Shopify's backup region "isn't a market",** in its own words, so its ten statements failed the role test under (e). They are kept in the point's note.

**What RD2-2 taught, and the first pass as a whole:**
- **Phase B's first pass is complete:** 73 variation points (RD1 19, RD2 4, RD3 50), each with a row for every platform; 671 rows; every statement-bullet pair placed or noted; no checker error in any part.
- **It cost 146 million tokens over 631 requests,** about 2.7 pairs a request, within the 150 to 300 million the frame set for phase B with its second pass.
- **Parts kept to their size:** none passed 80 requests, and none stopped short. Parts that placed a platform under many earlier points cost more per pair (RD3-3, RD2-2); the first parts of each root decision cost least.
- **Each part's lessons went into the brief before the next,** 14 rulings in all, and the statements earlier parts noted under a narrower rule are listed for the second pass (`b/second-pass.md`).

## 8. Phase A3, the absence audit (27 October)

**The absence audit's brief, re-checked** (the inspector resumed, 9 requests): ready to run. The first search for Zid's gap S02-ZD-G01 now matches 31 documents, against 128, all listed with snippets, the field the gap names among them. All 159 help-page passages Zid's citations quote fall inside the article text the search now reads. Zid's 11 claims are split between two agents run one after the other, by topic, so that each keeps its shared sources: the store's country, its checks, the contracting party and payments; then the countries served, and markets.

| Platform | Claims | Results | Statements added | Requests | Millions |
| --- | --- | --- | --- | --- | --- |
| Salla | 4 gaps | 3 confirmed; G03 contradicted | 8 | 62 | 12.1 |
| Shopify | 2 gaps, 3 absences | 4 confirmed; G01 partly contradicted | 23 | 86 | 17.2 |
| Zid, part 1 | 3 gaps, 3 absences | all 6 confirmed | 10 | 51 | 9.2 |
| Zid, part 2 | 4 gaps, 1 absence | 4 confirmed; N04 contradicted | 9 | 58 | 9.8 |
| WooCommerce | 2 gaps | G01 and G03 partly contradicted | 29 | 60 | 10.9 |
| BigCommerce | 2 absences | both confirmed | 43 | 46 | 6.5 |

**What it taught:**
- **Two of the six gaps routed to capture requests were answered, in whole or in part, by what is held.** Salla's onboarding list of countries is in two runs, as the page and as the API's saved answer. `method/held_index.py` didn't list saved answers, so the gap had gone to capture. It lists them now, and H-002 is narrowed. Shopify's Help Center page on business entities, not read before, says who verifies an entity and what changes with the store's country, so H-007's second step is narrowed.
- **The absence audit can run beside phase B,** since it adds statements the slices don't hold. Each part leaves them for the second pass, as the brief now says.
- **A Shopify search took 10 to 15 minutes with three running at once,** against 3 minutes alone. Searching by names with `--with` returned thousands of the runs' saved answers. The auditor narrowed them by more searches and read the Help Center documents by title and snippet, as its notes say.
- **The held corpus doesn't hold every Zid help page:** Zid's first part found Zid Pay's and Zid Financing's requirement pages, the national address article and the financing page only through the help centre's sitemaps, read live as indexes. It read twelve pages live; the coordinator captured them afterwards.
- **One lead was left unread:** the Help Center's `organization-settings/expansion-stores.md`, for how a store made inside an organization takes its country (S02-SH-G02). It goes to gap-closing (phase A2).

**What WooCommerce's audit taught:**
- **A held page was taken for unheld.** WordPress.com's Terms, which name WooCommerce's contracting entity, are held whole by the raw fetch in three runs. The browser was refused, and `method/held_index.py` judged the capture by the browser's status alone, so the auditor read them as unreadable. The tool now lists the raw body as readable, and the auditor reads the Terms for S02-WC-G01.
- **A slip of the coordinator's:** a message to the auditor named a commit from memory, not from git; it was corrected in the next message. Commits are named only from `git rev-parse`.

**What BigCommerce's audit taught, and the audit as a whole:**
- **Every claim of absence is now audited:** 24 across the five platforms; 2 contradicted and 3 partly contradicted, about one claim in five. The audit added 122 statements.
- **An audit that confirms its claims still adds evidence:** BigCommerce's two absences stand, and the pages read to test them added 43 statements on what a storefront channel holds per country.
- **Markdown escapes hid an identifier from the search:** `store\_country` didn't match `store_country`. `method/corpus_search.py` now reads Markdown's escapes as the characters they escape.

## 9. Phase A2, gap-closing (27 October)

| Part | Rows | Rows given statements | Rows with no gap left | Statements added | Gaps it leaves | Requests | Millions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WC-1: documents and checks; other payment providers; the store's own country; a market; who sells to the buyer; returns and cancellations | 8 | 8 | 6 | 31 | G06, in place of G02, whose pages it read; G07 | 108 | 22.2 |
| ZD-1: taxes on the platform's fees; the countries served; who sells to the buyer; returns and cancellations; the store's address; the store's country | 8 | 7 | 5 | 35 | G08, G09; G01 stands | 74 | 14.2 |
| WC-2: currency; language; the buyer's address; units and time zone (the rows of G05); domain; checkout and customer accounts | 10 | 8 | 8 | 58 | G08; G05 doesn't remain | 92 | 20.2 |
| ZD-2: checkout and customer accounts; contact information shown to buyers; domain; language; locations; market selection | 11 | 11 | 6 | 66 | G10 to G13 | 117 | 29.6 |
| SA-1: the store's data; the store's defaults; the store's taxes; who sells to the buyer; returns and cancellations | 7 | 7 | 4 | 82 | G05 to G07 | 63 | 15.7 |
| SH-1: the countries served; the store's data; a market; the buyer's address; and two leads | 4 | 4 | 2 | 107 | G06, G07 and G08, in place of G04, G03 and G05, whose pages it read | 180 | 53.5 |
| BC-1: the store's own country (who sets, checks and changes it); documents and checks; payouts; taxes on the platform's fees; the store's data; the store's defaults; the store's taxes | 9 | 9 | 3 | 46 | G04 to G08, four of them on Help Center articles that rendered empty | 79 | 14.6 |
| WC-3: products; discounts and offers; storefront design; contact information shown to buyers; locations; market selection | 10 | 10 | 10 | 55 | none | 98 | 18.9 |
| BC-1b: the Help Center articles behind BC-1's gaps G04, G05, G07 and G08 | 5 | 5 | 2 | 45 | G09, G10 and G11, in place of G04, G07 and G08; G05 answered | 41 | 6.4 |
| ZD-3: analytics and tracking; apps; notifications to the merchant; privacy and consent; staff access; store status; units and time zone; and the pricing pages as a lead | 12 | 12 | 3 | 74 | G14 to G21 | 72 | 15.6 |
| BC-2: contact information shown to buyers; market selection; returns and cancellations; staff access; the buyer's address; who sells to the buyer | 10 | 10 | 6 | 56 | G12, in place of G03, whose pages it read; G13, G14 | 84 | 14.5 |
| ZD-4: the absence audit's S02-ZD-G03 again, from zid.eg's Terms as shown | 1 claim | 1 | 0 | 29 | G03 partly contradicted: Egypt answered | 43 | 7.5 |
| SH-2a: analytics and tracking; notifications to the merchant; store status | 6 | 6 | 6 | 86 | none | 97 | 20.7 |
| WC-4a: analytics and tracking; apps; messages to buyers; notifications to the merchant | 7 | 7 | 7 | 40 | none | 75 | 12.5 |
| WC-4b: privacy and consent; staff access; store status | 6 | 6 | 6 | 70 | none | 65 | 12.0 |
| SH-2b: contact information shown to buyers; locations; messages to buyers; and SH-2a's lead | 4 | 4 | 4 | 75 | none | 76 | 14.4 |
| SH-2c: SH-2b's searches past 300, narrowed and read | 4, again | 4 | 4 | 72 | none | 67 | 13.8 |
| SA-2: analytics and tracking; apps; notifications to the merchant; the store's address; the store's country; units and time zone | 8 | 8 | 4 | 36 | G08 to G11 | 80 | 16.8 |
| ZD-5: what a click shows on Zid's pages, and zid.sa's Arabic country pages | leads | 6 points updated, and the `none` row | — | 52 | none | 28 | 4.4 |
| SH-2d: the documents SH-2c named: SMS marketing's rules by region and its countries, WhatsApp's prices by country, and the duties journey's later steps | leads | 2 points updated, and the `none` row | — | 43 | none | 33 | 4.3 |
| WC-5: WooPayments' testing and troubleshooting page, which WC-1 named and left unread | a lead | 1 point updated | — | 2 | none; G06 and G07 stand | 29 | 3.1 |
| SH-2e: the page SH-2d left unread, Shopify Messaging's requirements, and the Arabic of its four pages | leads | 2 points updated | — | 5 | none | 21 | 2.4 |
| **Gap-closing** | **121 rows** | **118** | **83** | **1,165** | **49 gaps open** | **1,622** | **337.3** |

After the second pass:

| Part | Rows | Rows given statements | Rows with no gap left | Statements added | Gaps it leaves | Requests | Millions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A2-T: the nine rows the second pass left `not covered`, on BigCommerce, Salla, Zid and WooCommerce | 9 | 1 | 5, by an absence or statements | 4 | BC-G15, SA-G12, ZD-G22, ZD-G23; WooCommerce's absences N01 to N04, to be audited | 32 | 4.4 |
| A2-SH-H: Shopify's five open gaps and capture request H-006, from held files the founder's local agent pointed to | 5 gaps, 1 request | 5 | none: each narrowed | 35 | G09 to G13, in place of G01, G02 and G06 to G08 | 83 | 17.0 |
| A2-SA-H: Salla's twelve open gaps, from held files, before its capture requests run; and BigCommerce's apps row | 12 gaps, 1 row | 4 | 2: Salla's onboarding countries (G03), from the audit's statements, and BigCommerce's apps | 14 | SA-G13 and G14, in place of G06 and G10; Salla's absences N01 and N02, to be audited | 92 | 18.6 |

**What WC-1 taught:**
- **Our labels aren't the platform's words.** The brief said to search a kind's own name, and the part asked whether "who sells to the buyer" was one. The brief now says the kind's head word is searched, such as `domain` or `currency`, and our longer labels aren't.
- **Code holds the calls, not the checks.** WooPayments' business verification runs on its own server and Stripe's. The release holds only its calls and strings, so what is checked, and against what documents, can't be read from it. G06 and G07 go to WooCommerce as questions.
- **A `page not read` gap ends once its pages are read.** G04's page answered with statements. G02's two release files gave way to G06, of kind `searched, not found`.

**What ZD-1 taught:**
- **The help centre's sitemaps found what the held corpus lacked.** Its nine sitemaps list 656 addresses. The two FAQs on the entities Zid Financing takes (S02-ZD-210, S02-ZD-211) came from them. The coordinator captured them with the pages read (run `20261027T092047Z-s02-a2-zid-sources`). ZD-2 starts from ZD-1's decoded list, with the one FAQ it left unread as a lead.
- **A page whose content a script loads can't be quoted from its capture.** zid.sa's and zid.eg's pricing pages render only Zid's error text, and their raw HTML holds no prices.
- **Pointing to a statement under another bullet doesn't place it.** ZD-1 named statements under (a), (b) and (c) as bearing on (f) points: the store's country in the store's settings for S02-VP-85, and the business details for S02-VP-63 and S02-VP-64. Phase B places a statement only under its own bullets, and it has placed these under RD1's points: the store's country (S02-VP-01, S02-VP-06 and S02-VP-07), and documents and checks (S02-VP-10). Zid's row under S02-VP-85 stays the gap S02-ZD-G01, which the absence audit confirmed. So these statements aren't on the second pass's list.

**What WC-2 taught:**
- **Reading a gap's route in full answers more than the gap asked.** G05's five release files and the setup wizard's page gave 41 statements under six points: the currency and units the setup wizard sets from the store's country, the site's language, and where the postcode rules apply.
- **A route can name values that nothing applies.** G05 named locale-info's `direction` and `default_locale`, which no file of the release reads by name. The language points are answered by the site's language, which the merchant sets, so the coordinator judged that no gap takes G05's place for them. The continents route returns each country's locale information whole, so the two values are served as data, and no setting takes them. That is the coordinator's reading of `woocommerce-11.2.1:includes/rest-api/Controllers/Version3/class-wc-rest-data-continents-controller.php`, lines 118 to 134.
- **Code names and site chrome flood the searches.** `domain` matched the namespace `Automattic\WooCommerce\Blocks\Domain` in 239 release files. woocommerce.com's header selectors for the site's currency and language matched most of its pages. The part narrowed its first search from 982 files to 170 by dropping single words, as the brief says.

**What ZD-2 taught:**
- **Half its groups had no head word.** "Checkout and customer accounts", "contact information shown to buyers" and "market selection" are our names, so the part searched Zid's own phrases from `x_words` and its terms. The brief now says that a kind whose name is all ours is searched by its phrases.
- **A setting documented for the whole store leaves "per market?" open.** All eleven rows were given statements, from the domain to the warehouses. But for five of them, none of Zid's pages says whether the setting takes a value per market, and its markets pages don't name these settings. The four gaps go to an observation of a store on a plan with markets, or to a question to Zid.
- **Six groups cost the most so far:** 117 requests and 29.6 million, against about 60 requests by the sizing rule, which counts groups. Its rows each yielded six statements. Rows predict the cost better: the first four parts cost 1.8 to 2.8 million a row, 2.3 on average. At that rate, gap-closing comes to about 280 million, at the top of the frame's range ([the frame's budget](frame.md#budget)).

**What SA-1 taught:**
- **A generic head word swamps the search.** Salla's head words, such as البيانات (data), الافتراضي (default), ضريب (tax) and الاسترجاع (return), matched most of its corpus. Every group's searches passed 300 documents. The part narrowed them by dropping the bare head words and keeping the phrases, as the brief's narrowing rule says. The head word helps only where it is distinctive, as `domain` was for WooCommerce.
- **Statements that name no market were tagged (g):** among them the Terms' statements that the merchant, not Salla, sells to the consumer (S02-SA-339 to S02-SA-344). In the second pass, phase B's role test decides whether their words hold the setting for the whole store, whatever the market.
- **A new gap can extend a capture request already written.** G07 asks whether the store's country chosen at onboarding sets its default currency or language. That is the step after the one H-002 asks the local agent to capture. The coordinator decides after gap-closing whether H-002 takes it.

**What SH-1 taught:**
- **It ran past its stop, to 180 requests and 53.5 million, the costliest part so far.** Every request of a long run reads its whole context again, here about 300 thousand tokens a request on average. The launch message's stop, "after about 110 requests", wasn't counted. The coordinator asked it to finish and report, and it had written every row by then. Launch messages now ask each part to count its tool calls and to stop at about 100, leaving the rest to a fresh agent.
- **A route can hold less than its gap needs.** G04 named the address service's answer of every country's address fields, which the part recorded in full, as 23 statements. That answer came from an admin page. The checkout's own call returns only each country's name, code and phone prefix. So the format the checkout applies to a buyer's address stays a gap (G06), which a checkout per buyer country would close on a capture store. That is work for the local agent; the coordinator decides after gap-closing.
- **Leads and gaps under (h) had no row in `a2.tsv`.** The checker counts a gap as searched by gap-closing only when an `a2.tsv` row names it, and G08, under (h), has no variation point. The part filed it under S02-VP-27 to clear the error. `a2.tsv` now takes a row whose `vp_id` is `none` for a lead's statements and an (h) gap; the checker and the brief say so, and G08 moved there.

**What BC-1 and WC-3 taught:**
- **A platform whose documents cover its settings answers every row.** WC-3 gave all ten of WooCommerce's rows statements and left no gap: products, coupons, design, contact details, pickup locations, and the customer's default location.
- **A route may name pages that don't exist.** G01's and G02's routes named endpoint pages missing from BigCommerce's docs index. BC-1 found the real ones through `llms.txt`.

**The render failed some sites, not only the pages it was blamed on** (the coordinator, 27 October):
- **What happened.** BC-1 found that every BigCommerce Help Center article not held rendered as an empty page, and ZD-1 had found that Zid's pricing pages rendered only Zid's error text. In this session the browser's own requests for those sites' scripts came back as HTTP 400, or aborted, while the same requests made outside the browser succeeded. So the pages never ran their scripts.
- **The fix.** `method/capture/render.mjs` and `page_text.mjs` now fetch every request with Playwright's own request client and hand its answer to the page. Pages that rendered before render the same, and the Help Center article went from 0 characters to 17,870, Zid's pricing page from 50 to 4,725.
- **What it had hidden.** 32 pages are now held as they render with the fix:
  - BigCommerce's five Help Center articles behind G04, G05, G07 and G08, now read by a short part, BC-1b;
  - Zid's pricing pages, read by ZD-3;
  - 24 zid.sa and zid.eg pages held until then only as an error text.
- **What agents had read in its place.** Agents had read those pages' raw HTML. 130 of the 135 Zid quotes from them are in the pages as shown, and three more are FAQ answers shown on a click. But zid.eg's Terms page holds the Saudi Terms in its raw HTML, and its scripts replace them with the Terms of شركة زد مصر, under Egyptian law, in Egyptian pounds. So S02-ZD-179 and S02-ZD-180 quote text the page doesn't show. The absence audit confirmed S02-ZD-G03 (who contracts with a merchant outside Saudi Arabia) on them, and is to be redone.
- **The rule now in phase A's brief:** quote a raw file only for what the rendered page shows, or shows on a click; a page that renders empty or as an error isn't read from its raw file instead.
- **A slip of the coordinator's, again:** a message to an agent named the new run from memory, and was corrected in the next message. Run names, like commits, are named only from the file system.
- **The correction of S02-ZD-179 and S02-ZD-180:** the coordinator added a dated note to each, and listed them in `b/second-pass.md` as statements the second pass notes and doesn't place. ZD-4 redoes the audit of S02-ZD-G03 from the page as shown. The coordinator made the change while ZD-3 was appending to the same file; ZD-3's rows came through whole, but a platform's files are changed only between its parts.
- **Runs without a README.** BC-1b found that its capture run had none, though `method/capture/README.md` asks every run for one, saying where it was fetched from and when. 37 of the 43 runs had none, all made in cloud sessions since 10 October. The coordinator wrote each one from the run's own files, marked as written afterwards, and changed nothing else in the runs. Each says whether its render fetched requests outside the browser.

**What BC-1b taught:**
- **Reading what the tool had failed closed gaps cheaply:** six gaps for 6.4 million. The articles answer who may change the store's country (the Manage Settings permission, and a channel's Edit Channels, which only the store owner grants) and the default language a new store takes from its country.
- **Two sources can disagree, and both stand.** The Help Center says a store's default country can be set "separately per channel" (S02-BC-256). The API says `store_country` "cannot be modified with channel-specific overrides" (S02-BC-100). Phase C weighs the two; neither is dropped.

**What ZD-3 taught:**
- **Zid states its settings for the store, never per market.** Every page read says what a setting is and who sets it, and none names a market. So each of the "what it takes its value per" points ZD-2 and ZD-3 took keeps a gap: eleven, S02-ZD-G10 to S02-ZD-G18, G20 and G21. One observation would close most of them: a Zid store on a plan with markets, showing which settings vary by market. Zid is in neither observed repository, so it goes to the founder after gap-closing.
- **The render fix showed Zid's prices by country:** Rise is 99 riyals a month on zid.sa and 1,128 Egyptian pounds on zid.eg, and each site's footer names its own company's registration and tax numbers (S02-ZD-347 to S02-ZD-355). Phase A had recorded neither, since the pages showed only an error text.

**What BC-2 taught:**
- **BigCommerce's gap-closing is complete:** three parts, 19 rows, 147 statements (S02-BC-205 to S02-BC-351), for 35.5 million. The Help Center, readable since the fix, answered most of BC-1b's and BC-2's rows.
- **A platform that states its settings' scope answers the "per market" questions in its own words.** Multi-Storefront sets contact details, checkout settings and the storefront a shopper sees per storefront, each "Use global" by default.
- **Counts written from memory, a slip of the coordinator's.** Three counts in this section were wrong as first written: the pages the fix recovered, Zid's per-market gaps, and BigCommerce's totals. Each was corrected from the files, and counts are now taken from the files before they are written.

**What ZD-4 taught:**
- **The audit's result moved from confirmed to partly contradicted.** For a merchant in Egypt, the contract is with شركة زد مصر, under Egyptian law and courts, with fees in Egyptian pounds and VAT (S02-ZD-367 to S02-ZD-382), and zid.eg's privacy policy names Zid Egypt as data controller. For the UAE, Oman, Bahrain, Qatar, Syria, and Kuwait outside Zid Pay, nothing read names the contracting party; their country pages link to zid.sa's Terms.
- **The tools now tell a page's source from what it shows.** ZD-4 found that `corpus_search.py` searched a page's rendered text and its source together, and that the checker passed a quote found only in the source. Both are changed:
  - `quote_check.py` reports a quote found only in a page's source (its body as served, or its markup's scripts and data) while a capture renders the page without it;
  - the checker lists such a quote for review;
  - `corpus_search.py` lists the source's extra text as its own document, labelled as text the rendered page doesn't show, and drops a capture that rendered nothing where another rendered the page.

  On Zid's files, exactly five quotes come up for review: S02-ZD-C313 and C314, the Saudi Terms in zid.eg's source, and three FAQ answers held in pages' data, shown on a click.
- **Some answers show only on a click.** The Syria page's FAQ answers after the first, and the payments pages' answers, are in neither the rendered text nor the source: the render doesn't click. They wait on a capture that opens them.
- **Opening what a click shows.** The capture tools now open each closed part of a page in turn (`CAPTURE_EXPAND=1`) and keep the lines that appear in `expanded.txt`; opening them all at once failed, since an FAQ closes one answer as it opens the next. Captured so, zid.sa's Syria page shows all ten of its FAQ answers, among them that no commercial registration is needed to open a store, and zid.sa has no Bahrain or Qatar page. ZD-5 reads what these pages add.
- **The coordinator's ruling on S02-ZD-C008 and C086:** their quotes keep the page data's punctuation (`","answer":"`), so the checker lists them for review. Their answers, "Currently in Saudi Arabia and Kuwait." and "K-Net, Apple Pay, Visa, American Express.", are shown on a click (run `20261027T121854Z-s02-a2-sources-batch-3`, item 023, `expanded.txt`), so the statements stand.

**What SH-2a taught:**
- **Shopify's own words answered every row, with no gap.** Its documents say what a setting holds for, even where that is the whole store: private mode is for the online store as a whole, and staff notifications are per recipient and per point-of-sale location. A market changes what consent allows: in markets set to require consent, web pixels run only with the visitor's permission (S02-SH-731).
- **Searches run at once slow each other down.** The part ran six of its own searches at once, which took 10 to 18 minutes each. Launch messages now ask for at most two at once.

**What WC-4a taught, and the coordinator's ruling on eight WooCommerce quotes:**
- **The store's country reaches WooCommerce's suggestions, not its settings.** The extensions suggested at setup, and two inbox notes, follow the store's base country (S02-WC-419 to S02-WC-421, S02-WC-433, S02-WC-434). Analytics follows the visitor's consent and region. Customer emails go out in the store's language.
- **Eight quotes the checker lists as only in the page's source stand:** S02-WC-C117 to C119 and C266 to C270, from WooCommerce's legacy REST API reference at woocommerce.github.io. That address serves the whole reference as static HTML. A browser is sent on by script to developer.woocommerce.com's overview page, which is what the capture of 10 October rendered (its `render.json` names it as `final_url`). The text is WooCommerce's own documentation, served at the address cited. So the statements stand, read with the release's code for the same endpoints.

**What WC-4b taught, and WooCommerce's gap-closing as a whole:**
- **WooCommerce's gap-closing is complete:** five parts, 41 rows, 37 of them with no gap left, and 254 statements (S02-WC-257 to S02-WC-510), for 85.8 million. Three gaps remain on four of its rows, each routed to the founder: who checks the store's country (G06) and which documents its payments' verification asks for (G07), as questions to WooCommerce; and the domain (G08), a question or a look at a test store's admin. Phase A's G01 and G03 stand as the absence audit left them.
- **Store-wide by design.** Roles and capabilities, Coming soon mode and the privacy texts each take one value for the whole site; no role, capability or setting is tied to a market. Consent comes from the visitor, through the WP Consent API.

**What SH-2b and SH-2c taught:**
- **A search left past 300 hides evidence.** SH-2b answered its four points and stopped before narrowing six searches. Narrowed, they gave SH-2c 72 more statements, as many as SH-2b's own. Among them:
  - a changelog post of 22 January 2026: "Your store’s currency is now set based on the business country selected in Business details" (S02-SH-883);
  - the Contact information policy's template, which fills "Physical address: Yemen" from the store's settings, on a store made in Yemen (S02-SH-899).

  The brief's narrowing step isn't optional, and a part that stops before it leaves a follow-up.
- **Narrowing by terms can't thin a corpus of duplicates.** Most of the fetch archives' records past 300 are Help Center fetches, the same pages as the Help Center corpus, and could only be narrowed by address.
- **Named documents left unread get a part of their own:** SMS marketing's rules by region and its list of countries, WhatsApp's prices by country, and the duties journey's later steps go to SH-2d.

**What SA-2 taught, and Salla's gap-closing as a whole:**
- **Salla's gap-closing is complete:** two parts, 15 rows, 8 of them with no gap left, and 118 statements (S02-SA-319 to S02-SA-436), for 32.5 million. Everything read was held in observed-sa, so nothing needed capturing.
- **Some of Salla's settings take a value per country of their own,** apart from its markets: an app's supported countries, from seven (S02-SA-409 to S02-SA-412), and a digital card's codes per "store country" (S02-SA-426 to S02-SA-429). Whether an app's supported countries are matched against the store's country or its markets is one of the four gaps (G09).
- **A kind whose words are country words makes the second search repeat the first.** For the store's country, `--with country countries` returned the first search's documents, so the part ran it with the market words only.

**What ZD-5 taught:**
- **The FAQ answers a click shows are Zid's statements on each country.** Zid Pay in Saudi Arabia and Kuwait gives its own banks, deposit fees, payout schedules and minimums, and Mada's cap. Zid Syria needs no commercial registration and takes payments through Bemira (S02-ZD-396 to S02-ZD-423). Zid's plans by country add branches, warehouses and features (S02-ZD-425 to S02-ZD-443).
- **Opening each part in turn wasn't enough while a repeated line was dropped.** The step kept only lines not yet seen on the page, so the Arabic Syria page's answers were lost, and an answer was tied to its question only by click order. Each click's new lines are now kept under the control's label. Captured so, the Arabic Syria page gives all six of its closed answers, which match the English ones recorded (run `20261027T135846Z-s02-a2-sources-batch-4`).


**What SH-2d, WC-5 and SH-2e taught:**
- **SH-2d read what SH-2c named,** in 43 statements: SMS marketing's rules by region and its prices for 12 countries, WhatsApp's prices by country and the countries it excludes, and the duties journey's later steps. Two figures disagree, and both stand: the store's `transactionRate` for duties is 0.0085 (S02-SH-461), and the same store's duties pages show "0.5% transaction fee" (S02-SH-982, S02-SH-986). Phase C weighs them.
- **Leads left unread are closed before a phase ends.** After the twenty parts, the coordinator read each part's notes for what it left. Three leads remained: Shopify Messaging's requirements page and the Arabic twins of four Help Center pages, from SH-2d; and WooPayments' troubleshooting page, which WC-1 listed as "not held and not read". Two short parts read them, for 5.5 million:
  - SH-2e recorded five statements under (h): Shopify Messaging needs an active, paid plan, the Online Store channel and a payment provider, and on a trial, campaigns go only to the merchant. The Arabic pages say what the English ones do, and gave the Arabic of five terms.
  - WC-5 recorded two statements: at sign-up, WooPayments verifies "information about you and your business" through Stripe's embedded form, and a test account "requires no personal information". Neither names a country, so G06 and G07 stand.
  - The other address in G06's `read`, WooPayments' onboarding troubleshooting page, answers with HTTP 404 (run `20261027T141859Z-s02-a2-sources-batch-5`, item 2).
- **From now on,** a phase closes only after the coordinator has read each part's list of what it left, and given each lead a part or a reason.

**What A2-T taught.** WooCommerce's settings pages in its release are read as the complete list of a store's core settings. They hold four absences: no limit on how many countries a store sells to, no business entity, nothing that places a buyer in a market, and nothing that sets extensions per country. But the part noted two caveats. The release lets other code add settings pages through a filter, and some settings sit outside the 13 files, such as the tax options' view and the shipping zones. So each absence is audited before phase C reads it.

**What the founder's local agent showed: a search that couldn't read code** (27 October, evening).
- **What happened.** The local agent read the observed-sh capture requests before running them. Much of what H-006 to H-008 ask is already held in tracked files of observed-sh: the admin's other answers, the admin's code bundles, and the sign-up bundle.
- **Why the searches missed it.** `method/corpus_search.py` read only the text, HTML and JSON records of the fetch archives, so JavaScript bundles were never searched. The admin's and sign-up's own code was searched by no one.
- **What changed.** The tool now reads JavaScript records too, in pieces of 200,000 characters. A new part, A2-SH-H, reads the held files the local agent points to, as leads, before any run goes ahead.
- **The lesson.** `CLAUDE.md` already says to look evidence up through each evidence repository's own guide (`docs/READING.md`). Before a gap goes to a capture request, every surface that guide lists is searched, and the tool is checked to reach it.

**What A2-SH-H and A2-SA-H taught: held evidence first** (27 October, evening).
- **Of the leads A2-SH-H read, every one was borne out but one.** Six it left unread, each named in `shopify/notes.md`. The admin's answers and code hold:
  - Managed Markets refused on every store held, for two reasons: an unsupported region, and no Shopify Payments;
  - which kinds of market each plan enables, and the limit on B2B catalogs;
  - the 100-market limit on the "All" condition;
  - the business types per country, 3 for Yemen and 11 for the US;
  - the checkout's address forms for four countries;
  - what the sign-up sends as the store's country, with "US" when none.

  The one lead not borne out: the API's limit error does carry a number in the schema ("Can't have more than 50 markets", deprecated). Each of the five gaps narrowed to what only a run can show, which is what the local agent's runs now in progress ask (H-006 to H-008).
- **Salla's dashboard code states, setting by setting, which settings take a value per market.** The settings center's definitions give a market field, enabled with the feature `multi-countries`, to 11 of its 94 sections. A2-SA-H recorded guest checkout's; a part of its own, A2-SA-S, records the rest. For Salla's capture requests, the held files answer two steps of H-005 (the order cancellation setting, and the merchant's notification settings), once the audit accepts their absences. The rest still need runs.
- **Two parts handled a narrowed gap differently.** One kept the old gap and replaced it in `a2.tsv`; the other rewrote the old gap in place. A gap now stays in `gaps.tsv` as history, and the new one says "in place of" the old. The checker reads that: the old gap needs no audit, and a phase B row that names it is flagged until a revisit names the new one.
- **Ids past 999.** Shopify's statements reached S02-SH-1000. The checker's id patterns now take three or four digits.

**Gap-closing as a whole** (the coordinator, 27 October):
- **What it did.** 22 parts read the pages behind 121 rows: the rows of S-02's points that were `not covered`, or whose gaps named a page not read. 118 rows were given statements, and 83 have no gap left. It added 1,165 statements: Shopify 388, Salla 118, Zid 256, WooCommerce 256 and BigCommerce 147. It cost 337.3 million, against the 350 projected at 10:30 ([the frame's budget](frame.md#budget)).
- **What it leaves.** 49 gaps: Shopify 5, Salla 11, Zid 21, WooCommerce 5 and BigCommerce 7. None stops the second pass.
  - **15 go to the local agent** as capture requests ([`handoffs/`](../../../handoffs/README.md)). H-008 is new, for Shopify's three on its dev stores. H-002 and H-005 are extended, for six of Salla's.
  - **34 go to the founder** ([`reports/S-02-evidence-requests.md`](../../../reports/S-02-evidence-requests.md)). Zid's, WooCommerce's and BigCommerce's need a store on the platform, or a question to it. One of Salla's is a question.
- **What it taught for the next subject:**
  - **Rows predict the cost:** most parts cost 1.8 to 2.8 million a row.
  - **Documents rarely say whether a setting differs by market.** That is what most of the gaps left ask: 11 of Zid's, 5 of Salla's, and some of BigCommerce's. Only a store with two markets answers them. So at the next subject's framing, the coordinator lists the points that only an observation can answer, and raises their capture requests before phase A, so that the captures run while the agents read.
  - **A search left past 300 hides evidence:** SH-2c's narrowed searches gave as many statements as the part before it.
  - **A site is checked to render before agents read it.** The render fault was found only after agents had read raw pages, and it cost an audit done again.
  - **The coordinator's own quotes are checked as an agent's are.** In the founder's request, the coordinator first quoted Zid's developer blog from a search's snippet. The snippet came from that page's raw HTML, and the page, rendered again after the fix, shows "Oops! Page not found" (run `20261027T112044Z-zid-rerender`, item 012). The request quotes Zid's developer documentation instead, as its capture shows it.

## 10. Phase B's second pass (27 October)

**The dry run of its brief** (5.4 million, 39 requests) did 35 tasks on a copy, in two small parts: Zid's (c) under RD1 and WooCommerce's (f) under RD3. Its check passed, and its tasks left `unplaced.tsv`. It found eleven defects:
- **Two would have failed every part's check:**
  - joining a statement to a row must also take the row's `kind` again, which the brief didn't say;
  - the work lists' folder, `b/second-pass/`, made `merge_slices.py` refuse the copy.
- **Seven would have made two agents differ:**
  - a `place` task could answer a point that a later `revisit` replaces: 738 of RD3's `place` rows were leads of its revisits;
  - revisits named statements outside the root decision's slice, which the printer dropped in silence;
  - nothing said what a revisit does when its answers all join rows already there, or which gaps a `gap` row keeps;
  - a reread row carried every bullet of its statement;
  - nothing said whether a placed reread keeps its earlier note;
  - under (c), nothing said what to do with a decider outside rule 1's table, such as a payment method, or with a statement naming none, and Zid's fees and their VAT turn on it.
- **The rest:** noise in a one-decision check, and no record of the revisit and reread tasks' outcomes.
- **Its rate was about one task a request,** a third of the first pass's, mostly spent editing long rows by hand.

**What changed:**
- **The work lists** (`method/second_pass_list.py`) put revisits first. Each revisit names its leads, the statements gap-closing found for the point under its bullet, which it places or notes; those leads have no `place` row of their own. Statements outside the decision's slice are named apart. A reread has one row per bullet of the decision.
- **A tool writes the rows** (`method/variants_edit.py`): join, add, replace, remove, the ledger of outcomes, and `x_words`. It takes `kind` and `scope` again from the statements, gives the next free id, checks that an excerpt is in its statements, and holds a lock while it writes, so that two parts of one root decision can work on different platforms at once.
- **The ledger:** each revisit, reread and note task's outcome goes in `b/<root decision>/done.tsv`, and `second_pass_list.py --check` lists what has none.
- **The checker** refuses a `not covered` row beside another row of its platform, and a copy that holds one root decision no longer flags the others' points. `merge_slices.py` skips the work lists' folder. The slice printer names on its standard error each id it doesn't hold.
- **The brief's second-pass section** says how a revisit ends (replace, join and remove, `absent`, or `gap` with only the gaps gap-closing left) and how to write. Rule 4 now says what an answer under (c) names: a decider from rule 1's table, or `every store` where the statement applies the thing to all stores and names no country, site or region. A statement with another decider, or none, is noted.
- **The parts were cut again:** ten parts, sized by their tasks with each revisit's leads counted. Parts of RD3 work one platform each.

**The second pass's parts:**

| Part | Tasks | Statements, with revisits' leads | Requests | Millions | Statements a request |
| --- | --- | --- | --- | --- | --- |
| RD1-S2: (c), Shopify and Salla | 83 | 138 | 48 | 7.5 | 2.9 |
| RD3-S5: (f) and (g), BigCommerce | 72 | 157 | 52 | 7.8 | 3.0 |
| RD3-S1: (f) and (g), Shopify | 66 | 487 | 71 | 14.7 | 6.9 |
| RD3-S2: (f), WooCommerce | 41 | 321 | 38 | 6.6 | 8.4 |
| RD3-S3: (g), WooCommerce | 134 | 134 | 48 | 7.7 | 2.8 |
| RD3-S4: (f) and (g), Zid | 40 | 269 | 61 | 12.6 | 4.4 |
| RD2-S1: (e) and (g), all five | 210 | 217 | 45 | 6.6 | 4.8 |
| RD1-S1: (a), (b) and (d), all five | 158 | 198 | 54 | 10.8 | 3.7 |
| RD1-S3: (c), Zid, WooCommerce and BigCommerce | 106 | 168 | 65 | 12.8 | 2.6 |
| RD3-S6: (f) and (g), Salla | 67 | 90 | 44 | 7.1 | 2.0 |
| RD1-S4: (c), Zid, 51 rereads | 51 | 51 | 35 | 6.2 | 1.5 |
| RD3-S7: (g), Salla and WooCommerce, 14 rereads | 14 | 14 | 24 | 2.5 | 0.6 |
| RD3-S8: the coordinator's rulings: two new points for all five platforms, and 24 rereads | 26 | 40 | 47 | 7.1 | 0.9 |

**What the two pilots taught:**
- **The tool and the order tripled the rate:** about three statements a request, against about one in the dry run, at about 0.05 million a statement. At that rate the second pass comes to about 115 million in all, inside the frame's 100 to 160.
- **Some statements answer a question no point asks:** under (c), statements on returns and on Salla's national address; under (f), BigCommerce's order statuses, and who sets units or the store's country. The second pass raises no point, so they are noted. From RD3-S1 on, each part lists them under "Candidates for a new point" in `notes-b.md`, and the coordinator decides on them when the pass ends.
- **Matching the first pass's deciders took new rows:** RD1's first parts split the store's country finely (its country, its location, where the business is based), so RD1-S2 gave six new answer rows to keep to the same split.
- **Each part marks its readings in the row** (`basis_evidence`): for example, a law named only as its country's own is read as part of X, not as a limit on which stores, so Salla's and Shopify's privacy statements answer `every store`.

**What RD3-S2 and RD3-S3 taught:**
- **A revisit's leads may answer nothing.** Six of WooCommerce's revisited rows had leads that answered other points, and no gap or absence, so they stayed `not covered`. RD3-S3's statements under (g) answered two: who sells to the buyer, and returns, each for the whole store. The four left (who sets the business entity, market selection's two points, and apps) take a gap when the pass ends, so that phase C reads what is missing rather than a blank.
- **A checker rule split one answer into two rows.** It wanted `answers` alone on any row holding a statement under (g), so RD3-S3 could not join such statements to rows that also match by `term`, and wrote two rows that repeat answers already held. The rule now binds only rows that rest on statements under (g) alone, as rule 4 meant, and the coordinator joined the two rows to the rows they repeat (`b/RD3/notes-b.md`).

**What RD1-S3 taught: a rule that hid the evidence it was meant to sort.** The clause added to rule 4 after the dry run kept a statement whose scope names a site from answering `every store`. Read with rule 1's table of deciders, it also kept zid.eg's Terms and Privacy Policy, both sites' prices, Zid's country pages and Zid Payments' sections for Saudi and Kuwaiti merchants from answering anything: 51 statements were noted, among them that a merchant in Egypt contracts with Zid Egypt, under Egyptian law, paying in Egyptian pounds with VAT. That is what RD1 asks: what a store's country decides. The part applied the rule as written, and said so. Rule 4 now says that the merchant's country is the decider where the platform's own words tie the site, page or section to one country and address it to merchants. The 51 statements are read again in a part of their own, RD1-S4, through the second pass's `reread` task (`b/second-pass.md`). The coordinator's lesson: a rule that narrows what counts as an answer is checked against the evidence it would exclude before parts run on it.

**What RD3-S6 taught: a second rule that left answers out.** Rule 4 let a statement under (g) answer a `who sets` point only beside its own whole-store answer. So statements that name only who sets a setting were noted: on Salla, the pixel the platform connects "automatically", and a staff permission over notification settings; on WooCommerce, who maintains return policies, who applies coupons, and which roles may change what. Fourteen statements in all. Rule 4 now lets them answer the `who sets` point, and they are read again in RD3-S7. With RD3-S6, the ten parts first planned are done.

**What RD1-S4 taught.** It placed 45 of the 51 statements that the narrower rule had kept out, and left six noted. Zid's answers under (c) now name the country a site, page or section is tied to:
- the contracting party, Zid Egypt (S02-V-298);
- the terms, under Egypt's law and courts;
- the fees, in each country's currency, with VAT on zid.eg's fees and on Zid Payments' (S02-V-299);
- Zid Egypt as the controller of the store's data (S02-V-300).

Four points now hold both `every store`, from zid.sa's own pages, and a country's answer, from zid.eg's: the contracting party, the terms, taxes on the fees, and the store's data. Each point's note says so, and phase C compares them by scope.
- **The coordinator's list missed six statements.** Six statements from zid.sa's one-country pages were noted under the same rule, but their notes gave other reasons as well, so the list left them out (S02-ZD-420, S02-ZD-436, S02-ZD-440, S02-ZD-443, S02-ZD-445, S02-ZD-446). They are read again in RD1-S5. The lesson: when a rule widens, list every statement whose note cites it, whatever other reasons the note gives.
- **A row's own note could go stale,** since the tool couldn't change it. S02-V-177's note still said S02-ZD-112 was noted. `method/variants_edit.py` now has `rownote`, which appends to a row's note, and S02-V-177's note now says what changed.
- **Two of Zid's gaps stand beside new answers:** which Zid company contracts in each country (S02-ZD-G03), and which tax its fees carry (S02-ZD-G08). zid.eg now answers both for Egypt. They stay open for the other countries.
- **Four of its calls are readings,** marked in their rows:
  - `where the merchant is` and `the merchant's country` read as one decider;
  - zid.sa's own pricing page read as tied to no one country;
  - the payment methods for zid.eg's plans read as how the fees are billed (S02-ZD-370, under S02-VP-14);
  - S02-ZD-112 placed, while its English twin, S02-ZD-008, recorded only at the page's level, stays noted.

**What RD3-S7 taught.**
- **Six of its 14 rereads changed nothing.** RD3-S2 had already placed them, from (f), in rows of the points the widened rule places them under. The coordinator listed the rereads from the parts' notes without checking for that. The lesson: before listing a reread, check whether its statement already stands in a row of the point the new rule would place it under.
- **The coordinator changed RD3's points while RD3-S7 ran.** It added the two new `who sets` points, below, then took them out again until the part had finished. So the part's first check flagged twelve errors on them, none on its own ids, and it checked a second copy. The lesson: the coordinator changes a root decision's folder only while no part of that decision runs.
- **Five of its calls are readings,** for phase C to weigh, each marked in its row: handling withdrawal requests read as setting the store's returns (S02-WC-283, S02-VP-66); a staff permission over the store's notification settings placed under notifications to the merchant, not messages to buyers (S02-SA-419); the Meta pixel's connection as the platform's, the seller's part being to link the account (S02-SA-407); the Shop Manager role's default editable role, `customer`, read as what it is kept out of (S02-WC-473); and RD3-S2's split between who gives access while the store is in coming soon mode and whom that mode lets through (S02-WC-489, S02-WC-507).

**The coordinator's rulings when the parts ended** (`b/second-pass.md`). The parts listed 35 statements that answer a question of their bullet for an X no point asks it of. Under (f) each setting has two points, so the coordinator raised the two missing `who sets` twins: S02-VP-91 for units and time zone, and S02-VP-92 for apps. RD3 now has 52 points, within its cap of 59. Personal data retention and a store's other legal pages are read under kinds that have their points: privacy and consent, and storefront design. The rest stay noted, each with its reason. Part RD3-S8 gives the two new points a row for every platform and reads the 24 statements again. 

**What RD3-S8 taught.**
- **The two new points needed no search.** Every platform's answer came from the rereads or from the statements already placed under the twin points. S02-VP-91 has a row on all five platforms. S02-VP-92 has one on four. BigCommerce's only statement on apps names no one who installs them, so its row is `not covered` and goes to gap-closing (A2-SA-H).
- **A point the coordinator raises must quote its X from a statement in `raised_by`.** Neither point did, and the checker refused both. The part added the statements their X is quoted from (S02-SH-246, S02-ZD-306).
- **The coordinator's launch message reached the part unexpanded,** as the text of a shell command naming its file. The part read the file. The lesson: pass the message's text itself.
- **Its readings,** for phase C to weigh:
  - Salla's booking products' only time zone read as no one setting it (S02-V-1102);
  - Shopify's permission to manage and install apps placed under apps by its own name (S02-SH-766);
  - Zid's `manage.app.market.settings` read as a permission from the page it is listed on (S02-ZD-330).
