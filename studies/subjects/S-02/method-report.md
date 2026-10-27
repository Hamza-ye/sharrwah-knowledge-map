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

