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
| A2-SA-S: which of Salla's settings take a value per market, from its settings center's definitions | 6 gaps | 1 | none: G09 narrowed | 12 | SA-G15, in place of G09; Salla's absence N03, to be audited | 47 | 7.4 |

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

**What A2-SA-S taught.** Salla's settings center gives a market field to 7 of its 94 sections, not 11: the four others are parent pages, or hold one value for the store. The seven are:
- guest checkout;
- the order of offers;
- the sign-in methods;
- WhatsApp verification;
- gifting;
- loyalty;
- how much store credit an order may use.

Each takes markets only where the store has the feature `multi-countries`, which every held store's feature list gives to the Special and Pro plans. Among the four is the setting for how a customer picks a market, which holds one value for the store. Analytics, the store's address, the return policy and the merchant app's notifications have no section, so their gaps stay. The apps list has no market field, an absence for the audit.

**What the second audit (A3-2) taught** (13.2 million, 65 requests). It audited the seven absences the late parts recorded:
- **Five are confirmed:** WooCommerce has no cap on the countries a store sells to, and nothing that places a buyer in a selling location. Salla's order cancellation setting, the merchant's notification preferences and its installed-apps list name no market. No market's own record holds those settings either.
- **Two are partly contradicted,** both on WooCommerce's Payments page, whose settings live in its scripts rather than in the PHP files A2-T read:
  - WooPayments' onboarding asks the business's type of legal entity and where it is located;
  - the page lists payment providers, and their recommended methods, per business location.

  Neither is set per selling location, so what the absences say about markets still stands.
- **One answers part of a gap:** a Salla market can have its own login settings, with an OTP provider chosen from the store's installed SMS apps (S02-SA-461). This answers S02-SA-G15, and H-005's step 6, for SMS apps.
- **The coordinator's own slip:** at A2-SA-S's suggestion, the coordinator had added a statement under (g) to three statements' `conditions`, where only statements under (a) to (f) may go. The audit's check found it, and it is undone.

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
| RD3-S9: the last round, Salla | 27 | 40 | 53 | 8.2 | 0.8 |
| RD3-S10: the last round, Zid, WooCommerce, BigCommerce and Shopify | 19 | 35 | 51 | 6.3 | 0.7 |
| RD2-S2: the last round, RD2 | 20 | 30 | 34 | 4.3 | 0.9 |
| RD1-S5: the last round, RD1, and six rereads RD1-S4 missed | 28 | 32 | 48 | 7.3 | 0.7 |

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


**The second pass as a whole** (27 October, 21:00 UTC). Its dry run and 18 parts cost 141.5 million, inside the frame's 100 to 160.
- **Where phase B now stands:** 75 variation points and 904 rows. Every statement under the three root decisions' bullets is placed or noted (`unplaced.tsv` is empty), and every revisit, reread and note task has its outcome in its ledger.
- **The full check:** no error, 17 warnings on phase A's citations, and 12 review lines on quotes found only in a page's source.
- **What stays open, by design:**
  - the gaps the capture requests and the founder's questions would close;
  - Shopify's S02-SH-G10, which narrowed G02 and gives no row of its own until the local agent's sign-up run arrives;
  - the readings each part marked, which phase C weighs.

## 11. Phase C: its brief and its dry runs (27 October)

**The first dry run** (3.4 million, 25 requests) ran the brief on six points of the three root decisions, on a copy. All six came out `vendor choice`, each with a founder item and the rules of letters A and B. The cause is the comparison, not the evidence:
- **Whole sets almost never agree.** The pilot's rule compared each platform's whole set of answers. On S-02's points a platform holds refinements beside its main answer, such as currency per market beside a default for the whole store and a display in the buyer's currency. Each refinement makes the sets unequal, so every point differed.
- **The letters' rules applied everywhere.** A letter's rule applies when any platform has the letter, so every point took the rules of A and B.

It also found 16 smaller defects in the brief and the tools: files the brief relied on without listing them, gaps and absences the printer couldn't print, a gap rule that blocked tests it couldn't change, and checks the tool lacked.

**What changed: the platforms are compared on each answer of a point, one at a time.** Mill's methods compare one phenomenon at a time. So each answer row now takes a key, the answer it gives, in a vocabulary per question. The tool works out what each platform does on each key: `gives`, `lacks`, `open` or `not stated`. It proposes the mechanical cause, and the agent checks it and adds named rules and maturity. Tried on currency, the keys tell the answers apart:
- all five platforms show prices in the buyer's currency: no difference;
- the four hosted platforms set currency per market, and WooCommerce's core doesn't: business model;
- a default from the store's country, and a single value for the whole store: vendor choice.

The letters' rules moved to a row per point. Expense is judged per key, so a payment provider that converts currency is expensive while the seller choosing a currency is cheap. A key whose value belongs to another subject goes to it: payments to S-04, taxes to S-05, the countries served to S-07, currency to S-09. The second dry run tests the redesign.


**The second dry run** (on seven points, of all three root decisions) tested the redesign.
- **The per-answer comparison tells the answers apart on the settings and on what decides the contracting party.** Currency, payment methods and the contracting party each mixed `no difference`, `business model`, `market, pattern` and `vendor choice`.
- **On the two points about markets themselves it didn't.**
  - **What defines a market** gave nine `vendor choice` founder items, which are one decision: what may define a market.
  - **What limits a market** gave 31 limits, none shared, because each was a number in the platform's own words.
- **What changed:**
  - **Vocabularies for both points.** Under what defines a market, `several countries`, `a company` and the rest. Under what limits one, kinds of limit, with the numbers in notes.
  - **One founder item for what defines a market.**
  - **No circular rule.** Under (d) and (e), a market cause follows as vendor choice does, since binding a market per market would be circular.
  - **Expense is judged by what a key's party does.** Moving money or acting under contract is expensive; naming or translating is cheap.
  - **The tool tries each way an open platform could go,** and asks for `blocked_by` only where a gap could change the cause.
  - **The tool flags a platform that both gives and lacks a key.**
  - **It refuses `D` for a platform with two answers,** and `maturity` without a marker.
  - **A `batch` command** writes a point's answers in one call, where a key a call would have passed the budget.
  - **The printer shows one platform at a time,** and each condition once per point.

**Phase C's parts** (from 27 October, evening):

| Part | Points | Keys | Requests | Millions |
| --- | --- | --- | --- | --- |
| C-RD2: what defines a market, what limits one, who creates and who changes or removes one | 4 | 43 | 24 | 4.1 |
| C-RD3-1: currency, language, domains, product availability, prices, discounts, storefront design (both questions of each) | 14 | 52 | 50 | 9.5 |
| C-RD3-2: checkout, taxes and duties, shipping, payment methods, who sells to the buyer, returns (both questions of each) | 12 | 52 | 38 | 7.4 |
| C-RD3-3: locations, contact details, the buyer's address, staff access, market selection, privacy, the store's address, units and time zone | 13 | 45 | 47 | 9.5 |
| C-RD3-4: store status, messages to buyers, privacy's who-sets, the store's country, apps, analytics, notifications to the merchant, units' who-sets | 13 | 52 | 39 | 6.5 |

**What C-RD2 taught.**
- **What defines a market** splits the references four ways, all `vendor choice` but one key:
  - Salla and Zid define markets by place: a country, several, a region, a city;
  - Shopify by conditions: places, companies, locations, channels;
  - BigCommerce by channel and storefront, and lacks a country;
  - WooCommerce has one store-wide list of selling locations.

  The one commonality: every platform makes a default market for the store. The eleven vendor-choice keys go to the founder as one question: what may define a market in Sharrwah.
- **What limits a market** raises five founder questions, each depending on what defines one:
  - may a market hold more than one country;
  - may a country, a site or a locale belong to more than one market;
  - which settings a market of each kind may hold;
  - may online and in-store buyers of one region take different settings.

  A sixth goes to S-07: may a market hold only the countries Sharrwah serves.
- **Who creates and who changes a market** raises none. Every key there is cheap, a screen or a permission.
- **A tool fault, fixed:** a platform whose only row is `absent` was counted `open` on every key it didn't exclude. It now counts as `not stated` there, as the brief says. RD2's rows were refreshed (`analysis_edit.py refresh`), and their check still gives no problem. Three keys keep a cause the mechanical tests don't give, each by a reading the brief allows: Shopify's customer groups, which its absence S02-SH-N03 excludes; and two limits tied to plans, by test 4's addition.

**What C-RD3-1 taught.**
- **The settings split cleanly by key:**
  - **Commonalities:** a currency shown in the buyer's currency, and a whole-store default, on every platform. The seller sets currency, language, product availability, prices, discounts and theme content everywhere.
  - **`business model`** where WooCommerce's core lacks what the four hosted platforms hold per market: currency, product availability, prices, discounts and theme content.
  - **`vendor choice`** where the hosted platforms themselves differ: languages per market, domains per market.
- **Its founder items are one question asked seven times:** whether each setting takes a value per market. Each depends on S02-VP-26, what defines a market. Six whole-store questions stand beside them. The register asks them once, as a standing decision, rather than setting by setting.
- **Two limits of the tool, worked around by readings:**
  - it reads one point's rows, so a statement phase B placed under one twin point but not the other is missed on the other. The next parts' messages say to weigh the twin's rows;
  - it proposes `market, pattern` without asking whether the two platforms' statements are of comparable kinds. On discounts per buyer's country, Salla's observed statement against Zid's shipped one, the part wrote `unknown` instead.

**The usage limit** (27 October, about 20:40 UTC). Parts C-RD3-2 and C-RD3-3 stopped mid-point when the account reached its plan's usage limit. Each had written its finished points, and the point in hand was half-written. The founder moved from Max x5 to Max x20, and both parts were resumed with a message, from their transcripts. Each was told to run `check` on its points first, to see what was done. The rule that each part writes as it goes is what kept this from costing anything but time.

**What C-RD3-2 taught.**
- **The first market cause by a named rule:** returns per the buyer's country, and the platform's part in them, follow the EU's right of withdrawal as Shopify's Managed Markets states it (S02-SH-491). So that key binds per market.
- **Most founder items again ask one question:** whether a setting takes a value per market, or once for the whole store. Five more go to other subjects:
  - Global-e as merchant of record, to S-03;
  - Avalara's duty calculation, to S-05;
  - carriers' cash on delivery, to S-10.
- **What stays open for want of evidence:** whether checkout, business entities and returns can take a value per market on Zid, BigCommerce and Salla. Each is held open by its gap (`blocked_by`), and each is one of the questions to the platforms ([`reports/S-02-evidence-requests.md`](../../../reports/S-02-evidence-requests.md)).
- **Its overrides of the tool are each a rule the tool can't apply:**
  - like with like, where one platform's answer rests only on observations;
  - test 4's need for a WooCommerce statement;
  - a named rule read in a statement's heading.
- **A reading the later parts share:** a store-level default that markets inherit or override is a default beside a value per market (letter A), not the key `the whole store`. C-RD3-4's message says so.

**What C-RD3-3 taught.**
- **Zid's open questions hold most of its keys open.** Six of Zid's gaps hold a key `unknown`: per-market inventory, contact details, staff permissions, market selection, privacy, and units and time zone. Each is a question in Zid's section of [`reports/S-02-evidence-requests.md`](../../../reports/S-02-evidence-requests.md). Zid's answers would settle them; nothing else now can.
- **Its seven founder items:** six of S-02's own and one for S-10. All but one again ask whether a setting takes a value per market, or once for the whole store. The new one is how a buyer is placed in a market: by their country, or by which customers the market lets in.
- **The tool can't take a twin's statement as giving a key.** Where a statement under the twin point would make a key `no difference`, the part kept the tool's tag and said so in its reading.

**What C-RD3-4 taught.**
- **A second named rule:** messages to buyers depend on the buyer's country, and on the store's own, by the UK's Privacy and Electronic Communications Regulations, which Shopify names (S02-SH-954). So they bind per market.
- **Its five founder items ask the same question as the other parts', for its settings:** per market, for the whole store, or both. It adds two: whether Sharrwah itself may set a store's status, and whether a market holds a country of its own beside the store's.
- **Analytics, apps and the store's country stay open on Salla and Zid,** each for a gap that is a question to them.

**RD2 and RD3, as a whole** (56 points, 247 keys; 46.4 million in five parts, and 7.2 million for the dry runs):
- **Causes:** vendor choice 137, unknown 37, no difference 31, business model 28, market pattern 8, a named rule 4, maturity 2.
- **What follows:**
  - left to the build: 111;
  - a decision for the founder: 71, of which 11 belong to other subjects (S-03, S-04, S-05, S-07, S-10);
  - a commonality: 31;
  - kept open: 24;
  - bound per market: 10.
- **S-02's own founder items:** 60, in 45 distinct wordings. Most ask one question, setting by setting: does it take a value per market, or once for the whole store, or both? The register asks it once, as a standing decision, with the settings where the references differ listed under it. What defines a market (S02-VP-26) comes first, since most items depend on it.
- **What `unknown` waits on:** in most cases, a gap that is a question to Zid, Salla or BigCommerce, named in each key's `blocked_by`. The founder's questions to the platforms ([`reports/S-02-evidence-requests.md`](../../../reports/S-02-evidence-requests.md)) would settle them.

## 12. The capture round: the local agent's runs for H-006 to H-008 (27 October)

**What arrived.** The founder's local agent pushed observed-sh to `19a5f6435`. It holds eleven runs from the Yemen line, each with its `trace.zip`, and the founder relayed the agent's notes:
- what the runs found, per capture request;
- pointers to held evidence, a Help Center passage or the schema, for five keys phase C had kept open.

The notes went to the parts as leads. The parts recorded only what the run files and pages show, and left the notes' readings out.

**Before the parts, three things the coordinator found:**
- **The joined phase B files were behind their folders.** The subject's `variants.tsv` lacked the last round's ten rows, and 45 rows differed, because the folders had not been joined after the last round. The gap-closing brief reads the joined files, so they were joined again. Phase C reads the folders, so it wasn't affected.
- **The full check needs the capture runs.** Run without `evidence/product-class/runs/*` as arguments, every web quote reads "not captured", and a quote with an ellipsis becomes an error. Run with them, the subject had no error, and every quote was found.
- **The search tool's caches are rebuilt per commit:** about six and a half minutes for observed-sh's fetch archives. The coordinator built them before the first part ran.

**A2-SH-R1** (82 requests, 14.1 million): the runs on the sign-up, the business entity's country, Shopify Payments and business types.
- **S02-SH-G10 answered.** A sign-up that chose the United States, from a network traced to Yemen, sent country US. It made a store that is American in its country, addresses, business entity, currency and backup region (S02-SH-1035 to S02-SH-1047). Its time zone was Riyadh's.
- **S02-SH-G09 narrowed to G14.** A switch of capture-gb-plus's business entity to a US one saved with no step asking for verification (S02-SH-1060 to S02-SH-1073). Whether a check follows later can't be seen in a run.
- **S02-SH-G13 narrowed to G15.** A Single Member LLC needs a legal name and exactly one account representative, and saving one creates a new legal entity. Switched to it, the store's Managed Markets eligibility names no business type (S02-SH-1081 to S02-SH-1091). The other types, and anything past Shopify Payments' set-up, which stops at its step 2 without a valid SSN or ITIN, aren't held.
- **What it taught: a gap a run answers in full had no way to be settled.** The checker counted it as a claim of absence nobody had audited. Now the statement that answers a gap says "answers S02-XX-Gnn" in its note, as a narrowed gap is settled by "in place of" in its successor. The gap-closing brief and the checker say so.
- **The leads' readings were tested, not copied.** "Isn't checked" became the steps between the confirmation and the saved page, with the reading in a note. "The same minute" became arithmetic on the mail's time, also in a note.

**A2-SH-R2** (78 requests, 13.6 million): the runs on markets and the checkout, and the five pointers.
- **S02-SH-G11 answered:** the checkout's address form and its CountryDetails answer for Saudi Arabia, the United Arab Emirates, Japan, Brazil and Italy (S02-SH-1122 to S02-SH-1137).
- **S02-SH-G12 narrowed to G16.** On Basic, a second B2B market, a second retail market and a submarket three levels deep each saved Active, with no limit shown. The paid Advanced store offers no POS locations condition. The Grow, Advanced and Plus dev stores, channel markets and a number per plan aren't held.
- **The five pointers,** recorded from the Help Center and the runs:
  - S02-VP-57's duty and tax settings: S02-SH-1138 to S02-SH-1143;
  - S02-VP-63's business entities: S02-SH-1144 to S02-SH-1154;
  - S02-VP-61's local payment methods: S02-SH-1155 and S02-SH-1156;
  - S02-VP-62's Shop Pay Installments, powered by Affirm: S02-SH-1157 to S02-SH-1159;
  - S02-VP-26's condition types on three stores: S02-SH-1094, S02-SH-1101 and S02-SH-1113.

**A ruling on phase C's method** (C-RD2's problem 3, and the local agent's recommendation). Step 3 had no tag for a key that no platform gives, which happens once a contradiction is weighed toward an absence. A platform that doesn't state a key already counts as not giving it in every test. So a key that every platform lacks or doesn't state is now `no difference`, and follows as a commonality the references don't carry. The tool and the brief say so. A key some platform leaves `open` isn't one of these: the tool tries both ways.

**Phase B's capture round** (three parts, 26.9 million): Shopify's 125 new statements placed in RD1, RD2 and RD3, and the rows naming a settled gap revisited.

| Part | Tasks | Requests | Millions |
| --- | --- | --- | --- |
| RD1-S6 | 71 | 64 | 10.5 |
| RD3-S11 | 39 | 67 | 11.0 |
| RD2-S3 | 9 (and 3 found) | 40 | 5.4 |

- **What it changed:**
  - S02-V-058 (who checks, S02-VP-05) names G14.
  - S02-V-483 (what limits a market, S02-VP-27) names G16. The new statements show markets one store held, which is no limit or rule, so they joined S02-VP-26's rows.
  - S02-V-662, the address form's gap row, was removed: its answer joined S02-V-660, the buyer's country.
  - Four rows are new: S02-V-302 under S02-VP-07, S02-V-1121 under S02-VP-62 and S02-V-1122 under S02-VP-86, and S02-V-303, which the coordinator's ruling removed.
  - The subject holds 906 rows. The full check finds no error and nothing unplaced, and every ledger task is recorded.
- **Three slips of the coordinator's, which the parts worked around:**
  - **The slices weren't cut again after gap-closing,** so `variants_edit.py` refused every new statement. RD1-S6 and RD3-S11 each cut a copy's slices and wrote through the tool into the real folder, under its lock. The coordinator then cut the real slices again, before RD2-S3 started. The slicer's own instructions say to cut again after anything adds to phase A's files, after the full check has written `kinds.tsv`. The coordinator had skipped that step.
  - **The task builder dropped a revisit's leads.** It appended only the revisits of rows naming a settled gap. A revisit it didn't append, of a gap row under S02-VP-26, took three statements as its leads, so they had no task (S02-SH-1092, S02-SH-1094, S02-SH-1095). RD2-S3 found them unplaced in its slice and placed them by the brief's last step.
  - **The parts' message pointed to Shopify's `notes.md`,** which the phase B brief forbids, a slip made once before. The parts read only what the brief allows. RD2-S3's message no longer names it.
- **The coordinator's rulings** are in `b/second-pass.md`:
  - **S02-V-303 removed.** A form's required fields aren't a check of who checks: S02-VP-05's "new information" is what Shopify's banking partners verify. The two statements joined the seller's row, as the same form's others had.
  - **The Backup Region control's two placements are left as they are,** since neither changes a key.
  - **The other readings stand.**
- **The checker,** run on a copy holding one root decision, listed every other root decision's phase C rows as errors, which hid a part's own. It now skips them, as it already did for `a2.tsv`.

**Phase C again on the keys the capture round touched** (C-R: 38 requests, 4.8 million; 11 points of RD2 and RD3). Four keys changed:
- **S02-VP-57 and S02-VP-63, `the whole store`: `unknown` to `no difference`.** Both had been held by like with like, since Shopify's statements giving the key were observations only. The Help Center's statements now declare it: the store's tax and duty settings, and the primary entity for every market's subscription payments.
- **S02-VP-26, `a group of customers`: `unknown` to `no difference`,** not carried. Under the ruling above, S02-V-409 is keyed as C-RD2's reading reads it, `a company`. The key then stands on Shopify's absence alone, and the new-market pages on three stores offer no customer group.
- **S02-VP-86, `a market the store sells into`: `unknown` to `vendor choice`,** a founder item that depends on S02-VP-26. Shopify's new row has an app configured per market. BigCommerce installs every app for the whole store.
- **Unchanged after a check:**
  - `Affirm` (S02-VP-62). Shopify names Affirm reviewing the store, not setting the method, so the key stays open. Phase B and phase C read it the same way.
  - S02-VP-61's `the whole store`, S02-VP-63's `a market the store sells into`, and S02-VP-27 to S02-VP-29.

After C-R, RD2's and RD3's 247 keys stand as follows.
- **Causes:** vendor choice 138, no difference 34, unknown 33, business model 28, market pattern 8, a named rule 4, maturity 2.
- **What follows:**
  - left to the build: 111;
  - a decision for the founder: 72, 61 of them S-02's own, in 46 wordings;
  - a commonality: 34;
  - kept open: 20;
  - bound per market: 10.

**What C-R taught about the tool:**
- **A row written again lost its earlier note.** The phase C brief doesn't let an agent read notes, and the tool wrote the whole row. Six notes were lost, two of them the reasons for each platform's letters. The coordinator restored them from the files before C-R, and the tool now keeps a row's note and adds the new one after it.
- **`show` printed no readings.** A re-run weighs a key's reading, basis and scopes again, so the agent printed those columns with its own script. `show --full` now prints them, never a note.
- **A gap that asks only for a number within a key its platform gives can't be marked open.** An example is S02-SH-G16, how many markets per plan, under `a number of markets per store, set by plan`. The tool notes it, and the gap stands as a question to the platform.

## 13. Salla and Zid: the local agent's captures of 28 October

**What arrived.**
- **Salla:** observed-sa at `b0bd0b16` holds the runs for H-001 to H-005. H-004 stopped at Salla's review, and H-005 at Salla's gate.
- **Zid:** a new repository, `other-product-class`, folder `zid/`. It holds a public demo store and a development store, both with Zid's feature flag `must_use_markets_pricing` false, so neither shows Zid's markets screens. It also holds the dashboard's route manifest, page index, strings and code.
- **Access:** this session's GitHub access couldn't reach the new repository. The founder's local agent pushed it to this repository's branch `evidence/other-product-class`, which the session reads as a detached worktree (`CLAUDE.md`).

**The founder's rule for what remains:** pursue a gap only if closing it could change an S-02 decision and a proportionate route exists. Otherwise leave it open, or close it. [`gap-assessment.tsv`](gap-assessment.tsv) gives each gap's verdict.

**A2-SA-R** (65 requests, 9.7 million): Salla's runs.
- **Answered:** S02-SA-G03 and G04.
- **Narrowed:** G01, G05 and G07, into G16 to G18.
- **Left:** seven. Salla refused the multi-market activation, and the UAE verification waits on Salla's review.
- **G16 needed no agent.** The held help article it named was read in full by the coordinator, and it doesn't say who may change the store's country. G16 stays open for RD1's analysis.

**A2-ZD-R** (69 requests, 12.3 million): Zid's captures.
- **Recorded:** 39 statements and 13 absences.
- **Answered:** 10 gaps, seven of them on absences from the dashboard's complete route list.
- **Narrowed:** 10, into G24 to G33. Only G30 (who checks a store's country after it changes) can still change an S-02 decision. The others go to their subjects (S-03, S-05, S-07) or are closed.
- **Left:** 3, which can't change a decision, so they are closed.

**A3-ZD-R** (66 requests, 10.9 million): the 13 absences audited by an agent that didn't record them.
- **N05 to N16 confirmed,** by four tests:
  1. **The market's own page:** its code saves only a market's name, countries, currency and publication.
  2. **Each setting's own page:** none names a market.
  3. **The manifest's completeness:** the dashboard is a single-page app whose routes are all declared at start, and all 119 page-index paths are in the manifest.
  4. **Zid's own word:** its help and changelog name only a market's countries, currency, products, prices and theme.
- **N17 contradicted:** Zid's cities answer holds 173 countries, among them the five the Business address list of 162 lacks. What still stands is that the Business address list holds none of the five.
- **What it taught:** an absence from a list of routes rests on two things, that the list is complete and that the thing would need a route of its own. A page can hold a field without a route, so the audit tested the pages' own code too. A brief that relies on a route list should ask for that test.

**Phase B's round** (five parts, 36.8 million): every new statement placed or noted, and the rows naming a settled gap revisited.

| Part | Tasks | Requests | Millions |
| --- | --- | --- | --- |
| RD1-S7 (Salla) | 37 | 61 | 8.8 |
| RD2-S4 (Salla and Zid) | 17 | 57 | 7.4 |
| RD3-S12 (Zid) | 20 | 49 | 6.3 |
| RD3-S13 (Salla) | 10 | 49 | 5.3 |
| RD1-S8 (Zid, a Salla revisit, and the rulings' six tasks) | 19 | 65 | 9.0 |

- **What it changed:** twelve of Zid's gap rows under RD3 now give `the whole store`. Each is a reading of a setting shown once, with no market field, on the two-market store, beside the audited absence. Where gap-closing narrowed a gap, a gap row stands beside the answer.
- **The full check:** the subject holds 923 rows under 75 points. It finds no error and nothing unplaced, and every quote is found.
- **The coordinator's rulings** are in `b/second-pass.md`. Two change rows:
  - **An answer the platform's own assistant generates is a lead, not an answer.** Salla's dashboard assistant answers under the notice "Responses are AI-generated. Verify what matters most."
  - **Salla's default currency gets its row:** the store whose onboarding answered the UAE holds currency AED.

**What the round taught about the tools.** The coordinator fixed each before the next part ran:
- **The task builder dropped a revisit's leads again,** the slip of section 12. It is now `method/round_tasks.py`. It appends every revisit whose leads have no other task, and dedupes within a round. Run again, it found the 13 Salla statements the round's first list had dropped.
- **`variants_edit.py add` gave a removed row's id to a new row** (S02-V-303). It now skips every id the ledger, notes or rulings name, and the new row is renumbered S02-V-307.
- **JSONL was split with Python's `splitlines()`,** which also breaks on U+2028 inside a JSON string, and so dropped records: 13 of Zid's `answers.jsonl` and one Salla structure, of 2,531 held JSONL files. The search, run and quote tools now split on newlines alone, so their line numbers are the files' own.
- **Zid's fetch archives were outside the search.** `corpus_search.py zid` now reads them, so the dashboard's code is searched.
- **The dashboard's strings had no kind.** Their structure names its source in another field. `source_kinds.py` now reads it, so they are `shipped`.
- **The slices were cut again while parts ran,** to carry those kinds. Each file was replaced whole and at once, so a part read either the old file or the new one.
- **`xwords` added duplicates.** It no longer does.

**Cost of the round:** 69.7 million: gap-closing and the audit 32.9, phase B 36.8.

## 14. Phase C after the Salla and Zid round, and RD1's first run (28 and 29 October)

**What ran:**

| Part | Points | Requests | Millions |
| --- | --- | --- | --- |
| C-R2a: RD2 and part of RD3 again | 8 | 31 | 3.8 |
| C-R2b: the rest of RD3 again, then a ruling applied | 9 | 24 | 4.3 |
| C-RD1-1: RD1's first comparison, points 1 to 10 | 10 | 42 | 9.6 |
| C-RD1-2: points 11 to 19 | 9 | 38 | 7.3 |

Phase C is complete for all three root decisions, and the full check finds no error.
- **Keys:** 361. **Causes:** vendor choice 208, no difference 53, unknown 43, business model 33, market pattern 13, a named rule 8, maturity 3.
- **What follows:**
  - a decision for the founder: 142, in 90 wordings;
  - left to the build: 116;
  - a commonality: 53;
  - kept open: 33;
  - bound per market: 17.

**Before the re-run, a refresh.** It showed only 6 keys whose states had changed, because the stored keys still marked Zid's old gap rows as open. `check` named the rest: 13 answer rows with no key, and the keys whose `blocked_by` named one of them. So the re-run keyed those rows, marked the new gap rows' keys open, and wrote again every key that moved. It changed no other key.

**Two rulings on like with like,** now in the phase C brief:
- **Agreement on an observed act** (C-R2a's problem 4). Like with like guards a difference, and a reading of what a page doesn't show: a store may lack what its platform offers. Where every platform gives a key, and one gives it by an observed act, such as the seller setting a value in the admin, that is enough for `no difference`. Six commonalities rested on such observations of Salla's. The literal rule would have made them `unknown`, which the evidence doesn't support.
- **A reading backed by shipped code** (C-R2b's problem 1). A reading of `the whole store` that also rests on a confirmed absence from the platform's shipped code is weighed with that absence's kind, `shipped`. Zid's development-store rows cite such absences, and the audit also read each setting's own code. C-R2b had held three keys `unknown` on the stricter reading. Once applied, they became two vendor choices and a market pattern.

**No note was lost.** Each part rewrote rows whose earlier notes the brief doesn't let it read. A comparison with the files before the re-run found every earlier note kept, with the new one after it (25 rows), so the tool's fix of section 12 holds.

**Two container restarts** (28 October, about 23:22 and 23:47 UTC) stopped two parts each time.
- **What the logs show:** the platform restored the session onto a new VM, which booted fresh with the session's disk. Both times the main session was idle.
- **What they rule out:** memory (16 GB, a peak of 1.5 GB, no out-of-memory kills), and a full disk (5.5 GB was free).
- **What we did:**
  - each stopped part was resumed from its own transcript, ran `show` and `check` first, and redid nothing;
  - the coordinator committed the parts' rows before resuming them, and after each part;
  - 4.2 GB of obsolete scratch copies and search caches for old commits were deleted, so the disk is at 76% of the allowance, from 86%.
- **The lesson:** commit a running part's rows when its neighbour finishes, and keep scratch copies of the subject short-lived. The full check copies the subject each time it runs.

**RD1's calls worth the review's eye,** all in `c/RD1/notes-c.md`:
- S02-VP-13's `every store` as a named rule (the Saudi Central Bank's authority);
- S02-VP-19's `every store` as business model;
- the WooPayments account country keyed as `the store's country` throughout;
- test 2's "particular law" counted only where a regulator and its rule are named.

**What comes next changed order.** The register is drafted first (`briefs/D-register.md`), so that the Yemen row and the scenario walk test a handful of decisions, not 142 founder items. Agents draft steps 2 to 4, and the coordinator checks each (`frame.md`, "How it runs").
