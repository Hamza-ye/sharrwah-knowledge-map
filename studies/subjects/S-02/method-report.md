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
| RD1-2: (b), all five platforms | 128 | 44 | 8.3 | 2.9 | 4 | 39 |
| RD3-2: (f) and (g), Salla | 133 | 65 | 15.8 | 2.0 | 7 more (44) | 75 |

**What RD1-1 taught:**
- **One point per question held:** the five platforms' answers to "what fills the store's own country" fell under one variation point, as 30 fields and records and one gap, and the countries served and kept out under one each.
- **The brief changed during the run,** and the coordinator's message named only one change. The agent found the others and applied them. A message to a running agent now lists every change.
- **Two rules were narrower than needed,** and were widened: a statement's identifier or scope may name what fills X under any bullet, not only (c) and (f); and a `gap` row may stand beside a platform's answers. Six statements the part noted under the narrower rule are read again in the second pass: S02-SH-259, S02-SH-260, S02-SH-396, S02-SA-249, S02-ZD-148 and S02-ZD-149.

**The absence audit's brief, re-checked** (the inspector resumed, 9 requests): ready to run. The first search for Zid's gap S02-ZD-G01 now matches 31 documents, against 128, all listed with snippets, the field the gap names among them. All 159 help-page passages Zid's citations quote fall inside the article text the search now reads. Zid's 11 claims are split between two agents run one after the other, by topic, so that each keeps its shared sources: the store's country, its checks, the contracting party and payments; then the countries served, and markets.

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
