# Inspection of the held pass's review brief: `briefs/H-review.md` (30 October 2026)

**What this is:** an inspection, before it runs, of the brief for the review of the held pass's dry run, `studies/class-model/briefs/H-review.md`. `PLAN.md`, section 3: "Before a brief runs, a separate agent reads it for anything that presupposes the answer".
- **What the review does:** it checks every placement line of BC-1 and ZD-1 against its source and the rules of `briefs/H-held.md`. Its findings set the other 68 batches' effort and the brief's changes.
- **Who inspected:** the inspector wrote none of the brief, made neither batch, and changed no file except this one.
- **Where the commands ran:** from the repository's root at `1827f4a5`. Every line number below is at that commit unless a finding names another.
- **The branch moved to `cab5e806` while the inspection ran:**
  - `33946dbc` committed ZD-1's `placements-ZD-1.tsv` and `notes-ZD-1.md`. This inspection reads them as examples, with BC-1's (`ff50bbee`);
  - `41c14c05` added a line to `evidence-map.md` on Zid's page index, which E-2 reads;
  - `0dd24c1f` and `cab5e806` changed `method/check_surface.py` and `method/held_vs_read.py`, which the review doesn't use;
  - nothing the review reads changed: `git diff --stat 1827f4a5 HEAD` prints nothing for the briefs, `held_entries.py`, `held_amend.py`, `class_slice.py`, `land_points.py`, `merged/` and BC-1's files.
- **The evidence:** read at other-product-class `0d79b79`, the commit `entries.tsv` names (`0d79b794f`), through its guides first: `README.md`, `zid/README.md`, `bigcommerce/structures/REGISTER.tsv`, and Zid's `index/`.
- **The batches' costs:** from the session's agent records, counted with `method/count_tokens.py`: `/root/.claude/projects/-home-user-sharrwah-knowledge-map/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/subagents/agent-a66aac536eba1b04d.*` for BC-1, and `agent-adb25b370ae8819f0.*` for ZD-1. They are facts about this session, not evidence of what a platform does.

**Severity:**
- **Must fix:** a reviewer following the brief would give wrong or unsupported verdicts. Or the coordinator couldn't use the review's output to correct the two batches, fix `H-held.md`, or set the other batches' effort.
- **Should fix:** the output would be less consistent, harder to check, or more expensive than it needs to be.
- **Note:** for the record.

**In short:** 7 must fix, 8 should fix, 6 notes.
- **The stance:**
  - the brief leaves out section 3's rule that a review tries to refute and reports counter-evidence, not agreement (V-1);
  - its three cases carry the BC-1 agent's own readings, the third asserts what the review must decide, and ZD-1's cases are missing (V-2);
  - it judges `supports` by H-held.md's restatement where B-extent.md's own definitions differ (V-3).
- **What it may read:**
  - "the file and locator `entries.tsv` gives" is a line of the structure's `items.jsonl`, which is the build's input. The bytes behind most of both batches' readings are outside "Read only". Four of the six BC-1 checks I tried need them (E-1);
  - nothing checks what never became an entry. The plans' prices in BigCommerce's plan table are one example (E-2).
- **What it gives the coordinator:**
  - its verdicts can't say that a line is missing, that a filler or a reading is wrong, or what a `new` should be (O-1);
  - no row says why a miss happened or what it changes, so the founder's rule on effort can't be applied from it. And the two batches hold 8 of the pass's 144 structures, with no `out`, no `outside`, no flag and no permission list (O-2).
- **Its size:** about 787,000 characters to read once, about 225,000 tokens (an assumption), past the project's cap before any search. Both batch agents passed the cap: their last requests held 257,452 and 297,153 tokens (K-1).

---

## Part 1. What the brief presupposes, and the standard it sets

### Must fix

**V-1. The review isn't told to refute, and its first verdict is `agree`.**
- *Found:*
  - **The plan's rule:** `PLAN.md`, section 3, line 80: "A review tries to refute what it reviews, claim by claim, and reports counter-evidence and missing evidence, not agreement." Line 81: "A review also looks for what an entry never cites".
  - **The brief:**
    - it cites section 3 only as "after a brief runs, a separate agent reviews the result against its sources" (line 3);
    - its verdicts begin with `agree` (line 23);
    - nothing asks for the alternative a line was tested against.
  - **Where a refutation would start:** two placements differ from how the model's own cell reads a statement of the same kind (facts, `land_points.py cell` at `1827f4a5`; "the same kind" is a reading):
    - CM-PAY-011's BigCommerce cell reads "more than 65 pre-integrated online payment solutions" (BC-C-026/where/BC-S-0150) as `core`. BC-1 places 44 of the gateways' rows on it as `shows`: lines 38 to 61, but not 43 and 53, and lines 70 to 91;
    - CM-CHN-004's BigCommerce cell is `own-service`, on Feedonomics Holdings, LLC's contracting row (BC-C-067/responsible/BC-S-0366). BC-1 places the Feedonomics cards as `extension-point` (lines 2 to 9 and 14 to 21).
  - **Why it matters, a reading:** with 318 lines and `agree` first, a reviewer can pass a line without testing it. A review that passes lines it never tested undercounts the misses the effort decision rests on (O-2).
- *Fix:* add before "For each line, give a verdict" (line 22):

  > **Try to refute each line** (`PLAN.md`, section 3). Name the strongest other placement the entry and its sources allow, including the one the cell's own reading of the same kind of statement gives (`land_points.py cell`), and test the line against it. Report counter-evidence and missing evidence, not agreement. A line the test doesn't overturn `stands`, and its `why` names the alternative tested and why it fails. Look also for what the line leaves out: another capability the entry is, or a thing it states that no line places.

  Then replace `agree` (line 23) with `stands`.

**V-2. The three cases carry one agent's readings, the third asserts what the review must decide, and ZD-1's cases are missing.**
- *Found:* the brief names three cases "from the agents' notes" (lines 35 to 38), all of them BC-1's. Each is worded as BC-1's agent framed it.
  - **"a help page that lists third parties' providers, where the help-page rule meets the `outside` rule":**
    - **The rule may not apply.** H-held.md's help-page rule covers "a help page's title, a changelog post, or a FAQ" (line 58). The gateways are rows of four tables in a help article. Whether the rule applies to a row is the question, and the case assumes it does.
    - **It offers two values where there are more:**
      - BC-1's notes name a third, `core`: "the article calls them 'BigCommerce gateway integrations'" (`notes-BC-1.md`, line 25);
      - B-extent.md's `extension-point` covers "a provider interface" (line 116);
      - the model's own cell for these gateways, CM-PAY-011, holds `core`, `outside`, `shows` and `extension-point` readings (V-1).
    - **The article's words around the tables** (facts at other-product-class `0d79b79`, `bigcommerce/raw/runs/20261029T024758Z-help-center-en/steps/001.text.txt`):
      - "Processing payments through BigCommerce gateway integrations on the Embedded Payment Provider listdo not incur Open Payment Provider fees" (line 77);
      - "the following app payment processors are also Embedded Payment Providers" (line 111).
    - **The lines at stake:** BC-1's lines 38 to 96, 59 of its 175, are the article's rows. 51 of them are on CM-PAY-011: 44 `shows` and 7 `extension-point`.
  - **"a card in the platform's own channel catalog, where a third party is the venue or the provider":**
    - **The axis is the agent's own.** Venue against provider is the axis BC-1's agent chose: "I used `core` where the third party is only the venue (a marketplace) and `extension-point` where it is named as the provider" (notes, line 99).
    - **B-extent.md asks something else.** Its `core` asks who does it: "the platform itself does it for the merchant" (line 114).
    - **Whether a venue is a slot filler at all is open.** A filler is "a third party or a law a statement names as doing the capability or setting its terms" (line 150). BC-1 records Google, Meta, Microsoft, Pinterest, TikTok, Amazon, Walmart and eBay as fillers on lines 2 to 27, and the plan line's channels on lines 103 and 104. CM-CHN-004's cell names the same ad channels for a plan line and records none, because they "are in its identifier only, not in its words".
    - **The lines at stake:** BC-1's lines 2 to 27, and the fillers on lines 103 and 104.
  - **"an entry naming one of the platform's group companies as a provider":**
    - **The case states both conditions of `own-service` as given.** The two conditions are that the entry names the platform's company, or one of its group, and that it names that company as the maker or provider of a separate product (B-extent.md, line 115).
    - **The contracting entities.** They name "Commerce Entity: Commerce.com US, Inc., a Texas corporation in the United States" and its like, with "Services: Ecommerce Platform, Extensions, and certain Professional Services" (`bigcommerce/structures/contracting-entities/items.jsonl`, lines 1 to 5). Whether that names a provider of a separate product is the review's question.
    - **Feedonomics:**
      - BC-1's agent found that "no entry names Feedonomics as a company of Commerce's group" (notes, line 36);
      - the model's CM-CHN-004 cell says "no statement held says in words that Feedonomics Holdings is of BigCommerce's group, a gap".
    - **So the case asserts a group membership the evidence doesn't state.** That runs against the brief's own rule, "Never decide a maker, a third party or a placement from what you know of the platform" (line 49).
  - **ZD-1's cases are missing.** The brief was committed at `1827f4a5`, before ZD-1's notes (`33946dbc`). They name:
    - containers placed by their children's thing: 11 entries (`notes-ZD-1.md`, lines 45 to 58);
    - pages with a release badge, `new` or `beta` (line 70);
    - pages listed only under a store condition, and their `scope` (line 108);
    - what an agent may read to clarify an entry (line 106);
    - an access request by the platform's own team, against S7 (line 68);
    - and, in its placements, two pages at an app's address named with the platform's brand, "Zid Ads" and "Zid Voice", placed `extension-point` (lines 13 and 14).
- *Fix:* replace lines 35 to 38 with:

  > - **Where H-held.md left the agents unsure or let them read a rule two ways,** with a fix in words the coordinator can paste. Rule on each case from the entries and their sources, weighing every value B-extent.md allows, and find others. The agents' notes name these:
  >   - BC-1's payment-gateways rows (lines 38 to 96): which `supports` each takes, from the rows and the article around them, and whether H-held.md's rule for a help page's title applies to a row of a table in one;
  >   - BC-1's channel cards (lines 2 to 27): who each card and its source show doing the work (the platform, a named third party, or no one), and so which `supports` each takes, and which of the parties it names are fillers;
  >   - the entries that name a company (BC-1's contracting entities, lines 28 to 37; the Feedonomics cards, lines 2 to 9 and 14 to 21): whether any names the platform's company, or a company of its group, as the maker or provider of a separate product, by its own words and its source's only;
  >   - ZD-1's containers (Analytics, Settings, Store, Marketing, Logistics, Payments, Channels, Apps, Online store, Communications, Whatsapp), its pages with a release badge, its pages listed only under a store condition, its pages at an app's address named with the platform's brand (Zid Ads, Zid Voice), and its access requests by the platform's own team;
  >   - every other item of both notes' "couldn't tell" and "Problems".

**V-3. The verdicts follow H-held.md's restatement of the model's rules where B-extent.md's own definitions differ.**
- *Found:*
  - **Which rules the brief names.** Check 3 judges `supports` "by B-extent's 'Cells and evidence' and its conventions, as H-held.md restates them" (line 19). H-held.md itself says the values are B-extent.md's, "exactly as 'Cells and evidence' and its conventions define them", and then restates them "In particular" (H-held.md, line 51).
  - **The restatement leaves out the defining clause of three values:**

    | Value | B-extent.md (lines 114 to 116) | H-held.md (lines 52 to 55) | Dry-run lines it bears on |
    | --- | --- | --- | --- |
    | `core` | "the platform itself does it for the merchant. The statement names its own admin section, setting, route or built-in behaviour, a plan line that includes it…" | "the platform's own admin place, setting, route, plan line or staff permission…" | BC-1's Buy Buttons, Amazon, Walmart and eBay cards (lines 22, 24 to 26). Their notes say "Who builds these connections isn't stated" (line 37) |
    | `extension-point` | "the statement shows third parties doing it through something the platform provides…" | "an app's page, an app store's category, an extension target or a provider interface" | BC-1's tax services (lines 169, 170, 172 to 176); ZD-1's Zid Ads and Zid Voice (lines 13, 14) |
    | `own-service` | "…Without a statement naming the company, place the cell by what its statements show, and note the missing maker statement as a gap" | that sentence is absent | the Feedonomics cards; Zid Ads and Zid Voice |

  - **The help-page rule.** H-held.md's help-page rule (line 58) has no counterpart in B-extent.md, whose rule on a title is "its words as a whole decide" (line 145).
  - **Why it matters, a reading:**
    - about 95 of the 318 lines turn on these clauses: BC-1's lines 2 to 27, 38 to 96 and 169 to 176, and ZD-1's 13 and 14;
    - a verdict by the restatement and one by B-extent.md can differ on them;
    - `held_amend.py` writes each placement as evidence in the model's cells, where B-extent.md's meaning governs.
- *Fix:* replace the first words of check 3 (line 19) with:

  > **`supports`,** by B-extent.md's "Cells and evidence" and its conventions, which H-held.md's rule 4 says govern. Where H-held.md's restatement reads differently, the verdict follows B-extent.md, and the difference is a fix to H-held.md, with the lines it touches. The restatement leaves out B-extent.md's "the platform itself does it for the merchant" for `core`; "the statement shows third parties doing it through something the platform provides" for `extension-point`; and, for `own-service`, "Without a statement naming the company, place the cell by what its statements show, and note the missing maker statement as a gap".

### Should fix

**V-4. "Your review decides" hands the reviewer the coordinator's decision.**
- *Found:*
  - **The brief:** "Your review decides how the other 68 batches run, at what effort and with what changes to the brief" (line 3).
  - **The plan:** `PLAN.md`, section 3, line 80: "The coordinator checks each finding against its evidence before applying it."
  - **The founder's decision of 30 October** (`founder-decisions.tsv`, line 32) is on "What effort the agents run at, where the coordinator sets it", and says: "Whether a level misses is judged by the quality and completeness of its results."
  - **A reading:** the review supplies those results. The decision is the coordinator's.
- *Fix:* replace that sentence with:

  > Your findings are the evidence from which the coordinator corrects the two batches, fixes H-held.md and its checker, and sets the other batches' effort (the founder, 30 October: by the quality and completeness of their results). The coordinator checks each finding against its evidence before applying it (`PLAN.md`, section 3).

---

## Part 2. What the review may read

### Must fix

**E-1. "The source" stops at the structure's items, so most of the agents' readings can't be checked, and some would be judged wrong.**
- *Found:*
  - **What the brief allows.** Under "Read only" (line 5), the brief allows "each entry's source, at the file and locator `entries.tsv` gives" (line 9). For every entry of both batches, that is a line of the structure's `items.jsonl`, such as `other-product-class@0d79b794f:bigcommerce/structures/channel-catalog/items.jsonl`, `line 1`.
  - **Why the item isn't enough:**
    - `show` renders each entry from that item, so comparing the two tests only the build;
    - the repository's guide puts the bytes elsewhere: "`meta.json` (source, shape as observed, counts), `source.*` (the bytes as received) and `items.jsonl` (one item per line, as the source states it)" (other-product-class `README.md`, line 27). Its ledger is "joined to the run steps that hold it" (line 31).
  - **Where the known disagreements are:** beyond the item, where the agents read:
    - H-held.md's two known cases: the settings list's step (line 34) and the plan table's `source.html` (line 35);
    - BC-1's notes on four structures (lines 82 to 94);
    - ZD-1's notes on the page index (lines 72 to 87).
  - **Tried on BC-1's lines, and on ZD-1's.** Each fact is at other-product-class `0d79b79`:

    | Line | Placement | What checks it | In the item? |
    | --- | --- | --- | --- |
    | BC-1 14 to 21, the "Ads and social" cards | `extension-point`, filler Feedonomics | each card's Learn more link, `support.bigcommerce.com/s/article/Feedonomics-for-<channel>`: `bigcommerce/raw/runs/20261029T023811Z-channels-en/steps/002.frame-0.aria.yaml`, lines 93 to 118 | No. `channel-catalog/items.jsonl`, lines 9 to 13, hold region, position, name, description and action; `grep -c "Feedonomics-for"` on it gives 0. A reviewer held to the item would find the filler unsupported |
    | BC-1 43, Amazon Pay on CM-PAY-012 | `shows` | "leading digital wallets such as Amazon Pay, Apple Pay, and Google Pay": the article's `001.text.txt`, line 74 | No, and not in `payment-gateways/source.html` either: it holds the tables only (27,484 bytes; `grep -c "digital wallets"` gives 0) |
    | BC-1 169 to 176, tax services | `extension-point` | "Install" beside each service, and "An automated solution for sales tax calculation, integrated with BigCommerce.": `bigcommerce/raw/runs/20261029T012951Z-store-settings-en/steps/045.text.txt` | No. `tax-services/items.jsonl` holds the JSON answer |
    | BC-1 2 to 27, `scope` left empty | | the store the catalog shows: "trial store w5pamplexj, default country Oman, currency OMR" (`channel-catalog/meta.json`, `source.store`); "the help article states the list follows the store's country and currency" (the register's channel-catalog row) | No. `show --meta` prints only the descriptive keys: `structure`, `surface`, `shape`, `counts`, `items` |
    | BC-1 135, `new:Display` | `core` | `class_slice.py caps --terms "display settings; display; breadcrumbs; product display"`: CM-ANL-006, CM-INV-010, CM-SFR-005, CM-TAX-001 | Yes, with the model's tools |
    | BC-1 116, Surcharge rate on CM-PLN-003 | `core` | `land_points.py cell CM-PLN-003 bigcommerce`: "plan line Open Payment Provider Fee: 2.0%, 1.0%, 0.6%, 0.0% with contract, by plan" (BC-C-026/decides/BC-S-0152) | Yes, with the model's tools |
    | ZD-1 110, Bank accounts on CM-PAY-030 | `core` | "These bank accounts will appear as payment methods for customers on your store.": `zid/raw/runs/20261028T160128Z-dashboard-routes-rest-en/steps/097.text.txt`, line 36, reached through `zid/index/ledger/dashboard-routes.tsv` | No |
    | ZD-1 125, an access request on CM-STF-005 | `core` | "Zid technical team would like to access your account to provide support…": `zid/structures/dashboard-locales/items.jsonl`, namespace `access-request`. The selection marks that structure `read: no` | No |
    | ZD-1 13 and 14, Zid Ads and Zid Voice | `extension-point` | in `zid/structures/dashboard-page-index/source.js`: `zidAdsPage` with pageKey `apps.${a}` and path `apps/${a}/embedded`, and `zidVoicePage` with the badge `new` | Partly. `source.js` sits beside the items, but the brief names only the locator |

  - **How much rests on such files:** ZD-1's readings and notes cite 75 run steps, and four of its lines rest on the locales.
- *Fix:* replace line 9 with:

  > - the entries, through `python3 -I method/held_entries.py show --platform <p> --batch <b> --candidates`, and `--meta`;
  > - **each entry's sources, at other-product-class `0d79b794f`** (the commit `entries.tsv` names), through its guides first. That is the item at the file and locator `entries.tsv` gives; the file the structure's `meta.json` names under `source` (`held_as`, `answer`), with the rest of that `meta.json`; and the `source.*` file beside `items.jsonl`. Where the rendering, the item and the source differ, the source governs;
  > - what the agents read to clarify an entry, so that each reading resting on it can be checked:
  >   - the platform folder's `index/`, with Zid's `index/ledger/dashboard-routes.tsv` and the run steps it names;
  >   - the run steps the notes and readings cite;
  >   - `zid/structures/dashboard-locales/items.jsonl`, which the selection marks `read: no`.
  >
  >   For each reading that rests on a file beyond the entry's item, say whether H-held.md allows it (its rule 1, line 33, names only the item), as a fix to H-held.md.

**E-2. Nothing checks what the batches never placed.**
- *Found:*
  - **What the brief checks.** Check 1 asks whether each entry is what its source says (line 14). No check asks whether every thing a structure's source states became an entry. Yet the founder's decision judges a level "by the quality and completeness of its results" (`founder-decisions.tsv`, line 32).
  - **What a source states and no entry holds** (facts at other-product-class `0d79b79`):
    - **Zid's page index:**
      - `source.js` holds 137 `pageKey` literals, 136 of them distinct, and `items.jsonl` holds 119. The 18 without an item are those ZD-1's notes list (lines 74 to 81);
      - the route manifest's items carry no title (`dashboard-route-manifest/meta.json`, `counts.keys`: id, path, the `has…` flags, module, imports, css, parentId, index). So those 18 pages' English and Arabic titles reach no entry;
      - the evidence map's line added at `41c14c05` reads that "the model loses nothing", because each page's route is in the manifest. The review can test that reading.
    - **BigCommerce's plans' prices:**
      - `plan-comparison/meta.json` holds `prices_above_the_table`: "Core $39 monthly or $29/mo billed annually; Growth $105 or $79; Scale $399 or $299; Performance by quote". The plan page's step holds them too (`bigcommerce/raw/runs/20261029T015915Z-plan-upgrade-en/steps/004.text.txt`, lines 16 to 38);
      - no BigCommerce entry holds "$39" or "$29": `grep -c` on `held/bigcommerce/entries.tsv` gives 0;
      - the concern map holds no BigCommerce statement with them either: `class_slice.py search --platform bigcommerce --terms "$39; $29/mo; $105; billed annually"` finds 0 statements;
      - H-held.md sends agents to `meta.json`'s descriptive keys, and to the rest "only where an entry needs it" (line 21). `show --meta` doesn't print this key, and no entry needs it. So BC-1 couldn't place the prices: a miss caused by the brief, not by effort (a reading).
    - **The channel catalog's "Create more storefronts with paid plan"** (step `002.frame-0.aria.yaml`, line 62): no entry holds it. BC-1's notes name it (line 86).
- *Fix:* add to "Then, across both batches" (line 32):

  > - **What the batches never placed.** For each of the eight structures, compare its items with its sources (the files E-1 names). List each thing a source states that no entry holds, with its place in the source, and say whether it would change a cell. ZD-1's notes name 18 pages of the page index, and the plan table's `meta.json` holds the plans' prices. For each, say whether the agent, the brief, the selection or the build left it out.

### Should fix

**E-3. The review doesn't read what the agents were told to read.**
- *Found:*
  - **What H-held.md sends the agents to:**
    - the evidence map (line 16);
    - their platform's guides, and its `REGISTER.tsv` rows (lines 17 to 20);
    - `show --meta` (line 21);
    - `held/selection.tsv`: "why each structure is read, its `placement` and its `note`" (line 22).

    The review's "Read only" list (lines 5 to 10) names none of them.
  - **The plan:** `PLAN.md`, section 6, line 364: "Every agent that reads evidence starts from it, by structure, before any search." The evidence map's section "What the tools read, and what they miss" holds the known faults the review will meet, such as the settings list's addresses.
  - **The selection's reasons:** the agents read them. For BigCommerce's `channel-catalog`, `payment-gateways` and `tax-services`, they read "what the platform connects" (`held/selection.tsv`). Without reading them, the review can't tell whether a miss came from those words (O-2's `cause` `brief`).
- *Fix:* add to "Read only this brief and":

  > - what the agents were told to read, to judge whether a miss is the brief's:
  >   - the evidence map (`studies/class-model/evidence-map.md`), first, by structure (`PLAN.md`, section 6);
  >   - `held/selection.tsv`'s rows for the eight structures;
  >   - the platforms' `structures/REGISTER.tsv` rows for them.

---

## Part 3. What the output gives the coordinator

### Must fix

**O-1. The verdicts can't say what the coordinator needs to correct a line.**
- *Found:* the verdicts are `agree`, `wrong capability`, `wrong supports`, `should be new`, `should not be new`, `should be out`, `missing: <column>` and `can't tell` (lines 22 to 28), one per line (lines 57 to 62). They can't say:
  - **that a line is missing:**
    - an entry that is also another capability's. H-held.md's rule 2 asks for it: "write two lines with the same `entry_id`" (line 37);
    - a thing an entry states that no line places. Examples: "Physical dimension settings" in BC-1's Website section (entry 109; notes, line 48), and "certain Professional Services" in the contracting rows (notes, line 42). `PLAN.md`, section 3, asks a review to look for what was never cited (line 81);
  - **that a column holds a wrong value:**
    - check 4 asks whether the four columns are right (line 20), but only `missing` can answer it;
    - BC-1 records venues as fillers (lines 2 to 27, 103 and 104), and V-2 asks whether a venue is a filler at all;
    - `held_amend.py` writes each filler into the part's `slot-fillers.tsv`. What fills a slot is `world` (`PLAN.md`, Stage 4A, "The kind and the count"), so a wrong filler moves what the coordinator computes;
  - **what a `new` should be instead:** `should not be new` names no cap_id. The coordinator's `held/new.tsv` needs "the capability it is, an existing one, or out" (H-held.md, line 115);
  - **that a reading is wrong:** `held_amend.py` writes each line's `reading` into the evidence row's `why` (line 74). A reading that misstates its source goes into the model;
  - **that an entry misrenders its source:** a build fault, which the coordinator must fix before 68 more batches run;
  - **two verdicts on one line,** or **a group whose entries differ:** ZD-1 groups 20 entries on six lines (92, 126, 129, 136, 141 and 143), one of them six entries long.

  And `missing: <column>` doesn't give the missing value.
- *Fix:* replace lines 22 to 28 with:

  > For each line, one row per verdict. A line with two problems takes two rows, and a group whose entries need different verdicts takes a row per entry. Each verdict carries the value it calls for:
  > - `stands` (V-1);
  > - `wrong capability: <cap_id>`;
  > - `wrong supports: <value>`;
  > - `should be new: new:<name>`; `should not be new: <cap_id>` or `should not be new: out`; `should be out`;
  > - `missing line: <cap_id or new:name> <supports>`: the entry is also another capability's, or states a thing no line places;
  > - `missing <column>: <value>` or `wrong <column>: <value>`, for `scope`, `terms`, `filler` and `quality`;
  > - `wrong reading: <what the source says>`: `held_amend.py` writes the reading into the model's evidence;
  > - `entry differs from source: <how>`;
  > - `can't tell: <what would settle it>`.

**O-2. The output can't support the founder's rule on effort, and the dry run holds few of the pass's kinds.**
- *Found:*
  - **The rule.** The founder, 30 October (`founder-decisions.tsv`, line 32): "Where `high` or `xhigh` consistently misses important details for a type of task, evidence review above all, that type runs at `xhigh` or `max`. Whether a level misses is judged by the quality and completeness of its results."
  - **What the rule needs, per type of task:** which misses are important, whether they recur, and whether a higher level would have caught them.
    - The brief asks the last question across both batches (line 39). But no row says why a miss happened or what it changes, so the coordinator can check the effort judgement line by line only by redoing the review.
    - "Important" is undefined.
  - **The kinds it names aren't the batches' kinds.** The brief asks for misses "by kind of entry (a route, a page, a plan line, a permission, a gateway, a channel, a flag)" (line 34). The two batches hold no permission list and no flag:
    - BC-1's 175 lines: 81 `core`, 34 `extension-point`, 5 `own-service`, 51 `shows` and 4 `new`;
    - ZD-1's 143 lines: 140 `core`, 2 `extension-point` and 1 `new`;
    - no line of either is `out` or `outside`. The counts are from the `placement` and `supports` columns of both files, with `sort | uniq -c`.
  - **The dry run holds 8 of the pass's 144 structures.** That is the number the 70 batches hold (`held/batches.tsv`, column `structures`: Salla 64, Shopify 58, WooCommerce 10, Zid 6, BigCommerce 6).
    - The pass's other kinds aren't in the dry run: Shopify's and Salla's staff and partner permissions (the S7 rule); Salla's `dashboard-features` and Zid's flags; API scopes and webhook topics; extension targets and app categories; Flow's tasks; Zid's plan policies; WooCommerce's release code; and Salla's Arabic-only lists.
    - A reading: the review can set the effort for the kinds the dry run holds, and nothing for the others.
  - **A miss's cause can be other than effort.**
    - Both agents ran at `high` (the session's agent records: `"effort":"high"`).
    - Both passed the project's cap. Their last requests held 257,452 and 297,153 tokens, against "about 200,000" (`STATE.md`, line 153).
    - A reading: a miss that grows toward a batch's end points to the batch's size, not to effort. Only the line's position can show that.
- *Fix:*
  - Add to the TSV, after `verdict`:
    - `cause`, for every verdict but `stands`, one of:
      - `care`: the brief and the evidence named settle it, and the line misses it;
      - `brief`: H-held.md doesn't settle it, or reads two ways (name the rule);
      - `evidence`: the entry and its sources don't settle it;
      - `tool`: the rendering, the leads or the checker misled (name which);
    - `effect`: what the correction changes once `held_amend.py` writes it, one of:
      - `count`: a cell gains or loses `core` or `own-service`;
      - `kind`: a cell gains or loses `extension-point` or `outside`;
      - `capability`: a capability made or not made, or the entry moved to another;
      - `filler`: a slot filler added or removed;
      - `column`: scope, terms, quality or reading only;
    - `in_leads`: `yes` or `no`, whether the right cap_id is among the entry's leads, or `-` for `new` and `out`.
  - Replace "the effort judgement" (line 67) and line 76 with:

    > - the misses by `cause` and `effect`: per batch, per structure, per rule of H-held.md, and per third of each batch's lines, each with the lines it rests on;
    > - which effects you take as the "important details" of the founder's decision of 30 October, and why;
    > - what the dry run doesn't hold, and so sets nothing for. Of the 144 structures the 70 batches hold, BC-1 and ZD-1 hold 8. No line is `out` or `outside`, and neither batch holds a flag or a list of staff or partner permissions;
    > - your judgement, per kind of entry the dry run holds: `high`, `xhigh` or `max`, with the misses it rests on.

### Should fix

**O-3. Check 4 asks for "the entry's own words" where H-held.md doesn't.**
- *Found:*
  - **The brief:** check 4 asks of `scope`, `terms`, `filler` and `quality`, "are they in the entry's own words" (line 20).
  - **H-held.md's rule 5 (lines 60 to 63) asks it differently of each:**
    - `scope`: "in its words";
    - `terms`: each "found in the entry's text";
    - `filler`: "a third party or a law the entry names", with no rule on its wording;
    - `quality`: "<what>: <value in its words>".
  - **An example:** BC-1's line 28 records the filler "the law of New York (Governing Law)" for "Governing Law: New York". Check 4 would count it a miss, though H-held.md allows it.
  - **Why it matters, a reading:** false misses inflate the count O-2 rests on.
- *Fix:* replace check 4 with:

  > **`scope`, `terms`, `filler` and `quality`,** by H-held.md's rule 5: `scope` in the entry's words; each term found in its text; a filler, a third party or a law the entry names as doing it or setting its terms; a quality's value in its words. Is anything the entry states missing?

**O-4. The notes' claims go unreviewed, though the coordinator will act on them.**
- *Found:* the review checks placement lines only (line 12). The notes are half of each batch's output (H-held.md, lines 97 to 101), and some of their claims would change the model or the build:
  - BC-1's differences with the model's cells (notes, lines 67 to 80):
    - CM-CHN-007's "max. 3" storefronts, against the table's 4 to 15;
    - CM-INV-005's "Custom", against "Up to 50";
    - CM-PAY-001's missing payments page;
  - ZD-1's reading that CM-PAY-030's cell takes the bank accounts page for the payouts page (notes, line 64);
  - ZD-1's 18 dropped pages (E-2), and both batches' structures whose items and source disagree;
  - each new thing's searched terms, its proposed domain, area and parent, and its names.
- *Fix:* add to "Then, across both batches":

  > - **The notes' claims.** Check each claim of both notes against its source: each new thing's searched terms and proposed place, each "couldn't tell", each difference from the model's cells, and each structure whose items and source disagree. List each with a verdict and why.

**O-5. A fix to H-held.md may depart from B-extent.md again, or be a method ruling no one announces.**
- *Found:*
  - **No limit on the fixes.** The brief asks for fixes "in words the coordinator can paste" (line 35), and doesn't say they must stay within B-extent.md's rules. The held pass's inspection found that H-held.md's first restatement had departed from them (`inspection-H.md`, B-1).
  - **B-extent.md doesn't settle every case either.** Some of the cases in V-2 are open there too, such as whether a venue is a slot filler.
  - **The plan's rule on method rulings:** `PLAN.md`, section 3, line 55: "Each method ruling is listed in one plain line at the next report".
  - **No ask for checker tests.** A recurring miss that a script could catch belongs in `held_entries.py check`, which every batch runs (H-held.md, line 103). The brief doesn't ask for that.
- *Fix:* add to the ambiguities item:

  > Each fix stays within B-extent.md's rules. Where B-extent.md doesn't settle a case either, say so: it is a method ruling for the coordinator, listed at the next report (`PLAN.md`, section 3). For each recurring miss, say whether a test in `held_entries.py check` would catch it, and which test.

**O-6. The rows aren't pinned to the files and commits they judge.**
- *Found:*
  - **Line numbers drift.** Rows are keyed by "the placement file's line number" (line 59), and the brief pins no commit. ZD-1's files were committed after the brief (`33946dbc`), and corrections will shift lines.
  - **The model and the evidence aren't pinned either.** `STATE.md` (line 173) says a correction request for BigCommerce's settings list "is due" from the founder's local agent, and it would change the items.
  - **The counts:** the lines are 318 (BC-1 175, ZD-1 143). They carry 332 placements of 300 entries, since ZD-1 groups entries on six lines.
  - **The format:** the brief has no rule against a tab or a newline inside a field.
- *Fix:* add to "Output":

  > Read the placements and notes at their commits (BC-1 at `ff50bbee`, ZD-1 at `33946dbc`), the model at `1827f4a5`, and other-product-class at `0d79b794f`. Give each of the 318 lines at least one row, keyed by `batch`, `line`, `entry_id` and the line's `cap_id`, so that a row still finds its line after a correction. No tab or newline inside a field.

---

## Part 4. Size, cost and the review's own effort

### Should fix

**K-1. One agent reviewing both batches passes the project's cap on reading alone.**
- *Found:*
  - **What the review reads once,** measured at `1827f4a5` and other-product-class `0d79b79`, in characters:

    | What | Characters |
    | --- | --- |
    | `show --candidates`, BC-1 and ZD-1 | 63,942 + 46,381 |
    | the placements | 55,876 + 31,623 |
    | the notes | 14,993 + 11,878 |
    | this brief, H-held.md, and B-extent.md's two sections (lines 109 to 154) | 4,826 + 12,063 + 7,168 |
    | one `land_points.py cell` per capability placed and platform: 68 for BigCommerce, 91 for Zid | 138,859 + 196,894 |
    | BC-1's sources: the settings step; the plan table; the article's text, not its 849,339-byte `001.html`; the channel step; the tax answer and steps 43 to 45; the terms grid | 70,488 |
    | ZD-1's sources: the page index's `source.js`, and the 75 run steps its readings and notes cite | 36,136 + 95,977 |
    | **In all** | **about 787,000** |

  - **In tokens:** about 225,000, at 3.5 characters a token. That is an assumption: the held pass inspection's ratio for Latin text, and Arabic runs denser. The figure comes before any `caps` search (one or two per line), any cell of an alternative, and the 318 rows the review writes.
  - **The batches, measured** with `count_tokens.py` on the session's records:
    - BC-1: 51 requests and 7.9 million tokens, its context growing from 49,347 to 257,452;
    - ZD-1: 76 requests and 13.8 million, its context growing from 49,373 to 297,153.
  - **The cap:** "parts small enough that no context passes about 200,000 tokens" (`STATE.md`, line 153).
  - **The review's cost.** These are assumptions from those runs:
    - one agent reading what both batch agents read would run about 127 requests, its context growing from about 50,000 to about 500,000: about 35 million tokens;
    - five parts of about 65 lines would each peak near 140,000 tokens, at about 2.5 million each: about 12 million in all, and a last part for the cross-batch sections;
    - the review reads more per line than the agents did (E-1), so both figures are low (a reading).
  - **No "how to work" section.** The brief has none, while H-held.md has one (line 82).
- *Fix:*
  - Run the review in parts, each by a fresh agent, each writing its own `review-dry-run-<part>.tsv`:
    - BC-1 lines 2 to 37 (the channel catalog and the contracting entities);
    - BC-1 lines 38 to 96 (the payment gateways);
    - BC-1 lines 97 to 176 (the plan table, the settings list and the tax services);
    - ZD-1 lines 2 to 62 (the page index);
    - ZD-1 lines 63 to 144 (the page index and the route manifest).
  - A last part, or the coordinator, joins the rows and writes `review-dry-run.md`'s cross-batch sections from them and from the parts' notes.
  - Add:

    > ## How to work, keeping your context small
    > - Read each structure's sources once, before its lines.
    > - Read each cell once, for the capability placed and for each alternative you test. Keep what it holds in a line of your notes.
    > - Print your entries 20 to 30 at a time, with `show --from --to --candidates`. Read your placement lines with `sed -n`, never the whole file.
    > - Never print `001.html` of the help-center run: its text is in `001.text.txt`.
    > - Write rows as you go.

**K-2. The brief states no effort for the review itself.**
- *Found:*
  - **The founder's decision:** the founder, 30 October (`founder-decisions.tsv`, line 32): "No agent runs at `medium` or `low` for reading evidence, reviewing, or making an engineering judgement: `high`, `xhigh` or `max`."
  - **The briefs:** H-held.md states its level (line 29). This brief states none.
  - **What the reviewer isn't told:**
    - both batches ran at `high` (the session's agent records), and the brief doesn't say so, though it asks whether `high` missed (line 39);
    - the held pass's inspection ran at `max` (the same records, "Inspect the held pass brief").
  - **A reading:** a review run at the batches' own level can't show what a closer reading finds.
- *Fix:* add after "Read only":

  > **Effort:** `max`, or `xhigh` at least. The batches ran at `high`, and this review measures what a closer reading finds (the founder, 30 October).

---

## Part 5. Notes

**N-1. The branch moved while this inspection ran** (see the header). The commits after `1827f4a5` change nothing the review reads. `41c14c05`'s line in the evidence map bears on E-2.

**N-2. What the dry run measures for the whole pass, beside the review.**
- *Found:*
  - the two batches cost 21.7 million tokens for 300 entries: about 72,000 an entry;
  - their contexts grew by about 1,400 tokens an entry for BC-1, (257,452 − 49,347) / 147, and about 1,600 for ZD-1, (297,153 − 49,373) / 153;
  - the 70 batches' median size is 169 entries, and the largest is 390 (ZD-5; `held/batches.tsv`);
  - `PLAN.md`, line 642, puts the held pass and the omission review at "about 80 to 180 million agent tokens in all, an assumption to be measured on the first batches".
- *What those rates give, all assumptions:*
  - at `high`, the pass's 14,879 entries would cost about 1.1 billion tokens;
  - a 390-entry batch would end near 680,000 tokens of context;
  - batches of about 95 to 105 entries would stay under the cap;
  - any level above `high` would cost more.
- The coordinator can set the projection beside the effort decision. Past a quarter over the budget, it goes to the founder (`PLAN.md`, Stage 4A and section 8).

**N-3. `held_amend.py` clips each reading at 160 characters** (line 74, `clip(r['reading'], 160)`). 123 of BC-1's 175 readings are longer, and 43 of ZD-1's 143. A reading's later part doesn't reach the evidence row, and neither does a correction made to that part.

**N-4. The leads, as the agents saw them and as they are now.**
- *Found:*
  - **The leads changed twice while the batches ran:**
    - at `ff50bbee` (16:24:17 UTC), to whole words only;
    - at `1827f4a5` (16:25:09), dropping the terms that more than two capabilities share.
  - **The batches ran across both changes:** both began at 16:10:17. BC-1's last request was at 16:24:01, and ZD-1's at 16:25:46.
- *Measured:* how often each agent's cap_id is among the entry's leads:

  | Leads | BC-1 (171 placements on a capability) | ZD-1 (156) |
  | --- | --- | --- |
  | `show --candidates` now | 81 | 68 |
  | the script as it stood when the batches began (`dc1e6414`, run from a scratch copy) | 84 | 67 |

  In both versions, 46 of ZD-1's placements have no lead at all.
- The brief should say which leads it measures. By these figures, the choice changes the count little.

**N-5. The output's name.** `held/review-dry-run.tsv` and `.md` share their name with the extent's own dry-run review files (`studies/class-model/review-dry-run-cells.md`, `-structure.md` and `-rulings.md`). B-extent.md cites those as "the dry run's review" (line 130). A name such as `held/review-H.tsv` keeps the two apart.

**N-6. What the brief gets right,** as `PLAN.md` requires:
- every claim is one of the three kinds (lines 44 to 47);
- the founder's words are never evidence (line 48);
- no maker, third party or placement is decided from what one knows of the platform (line 49);
- the evidence is read-only, and Python runs with `-I` (lines 51 and 52);
- the source governs where it and the rendering differ (line 14);
- the reviewer made neither batch;
- `can't tell` names what would settle it;
- the leads are measured, not assumed.

---

## What I ran

All from `/home/user/sharrwah-knowledge-map`, with `python3 -I`, at `1827f4a5` and then at the commits the header names. Scratch files went to the scratchpad only.
1. **The brief and its inputs:**
   - `H-review.md` and `H-held.md`;
   - `B-extent.md`'s "Cells and evidence" and "Conventions from the dry run";
   - `inspection-H.md`, with the coordinator's response;
   - `PLAN.md`'s sections 3 and 6, and Stage 4A;
   - `founder-decisions.tsv`'s rows of 30 October.
2. **Both batches:**
   - `placements-BC-1.tsv`, `notes-BC-1.md`, `placements-ZD-1.tsv` and `notes-ZD-1.md`;
   - `held_entries.py show --candidates` and `--meta` for both;
   - `held_entries.py check` for both, which printed "147 of 147 entries placed; 0 problems" and "153 of 153 entries placed; 0 problems";
   - counts by `placement` and `supports`, with `sort | uniq -c`.
3. **Lines tried against their sources** (E-1's table), with the model's tools:
   - `class_slice.py caps`, `search` and `key`;
   - `land_points.py cell` for CM-PAY-011, CM-APP-011, CM-CHN-004, CM-PLN-003 and CM-PLN-001 on BigCommerce.
4. **The sources, at other-product-class `0d79b79`, through its guides:**
   - `README.md`, `zid/README.md` and `bigcommerce/structures/REGISTER.tsv`;
   - the six BigCommerce structures' `meta.json` files and items;
   - the steps of runs `20261029T023811Z-channels-en` (step 2), `20261029T024758Z-help-center-en` (step 1), `20261029T012951Z-store-settings-en` (steps 2 and 43 to 45) and `20261029T015915Z-plan-upgrade-en` (step 4);
   - Zid's `dashboard-page-index/source.js` against its items, by script: 137 `pageKey` literals, 119 items, 18 without one;
   - Zid's ledger, the run steps `rest-en#97` and `#195`, and the locales' `access-request` namespace.
5. **The sizes:**
   - `wc -c` on everything K-1 lists;
   - `land_points.py cell` for every capability each batch places.
6. **The costs:**
   - `method/count_tokens.py` on the two batch agents' transcripts, with each request's context size from their `usage`;
   - each agent's `effort`, from its record.
7. **The leads:** each placed cap_id against its entry's leads, with the current script and with `held_entries.py` at `dc1e6414`. The old script ran from a scratch copy whose `studies/` pointed to the repository's; `show` writes nothing.

## What I didn't check

- I placed no entry and judged no placement. The cases above are where a verdict turns, not verdicts.
- I tried six BC-1 lines and three ZD-1 lines against their sources. I didn't read every source.
- I measured the cells of the capabilities placed, but not the cells of the alternatives a refutation would test, nor the `caps` searches. K-1's totals are low for that reason.
- The cost figures in K-1 and N-2 are assumptions from two measured runs, scaled as the method report's square law suggests. None was measured on a review.
- I named the other 68 batches' structures from `batches.tsv`, without reading them.

---

## The coordinator's response (30 October 2026, about 17:20 UTC)

Every finding is taken. The coordinator checked V-1's two cells, V-3's clauses and E-2's prices against the files first, and each holds. The brief (`briefs/H-review.md`) is rewritten:
- **Part 1, the stance:**
  - **V-1:** each line is refuted against the strongest other placement, the cell's own reading of the same kind of statement among them, and `agree` is now `stands`, which names the alternative tested.
  - **V-2:** the cases are worded as questions, per part, with every value B-extent.md allows. ZD-1's cases are added: its containers, release badges, store conditions, Zid Ads and Zid Voice, access requests, bank accounts page and Customer Referrals.
  - **V-3:** B-extent.md governs `supports`, and the brief quotes the three clauses H-held.md's restatement leaves out. A difference is a fix to H-held.md.
  - **V-4:** the review's findings are the evidence the coordinator decides from.
- **Part 2, what it reads:**
  - **E-1:** the sources are the item, the file `meta.json` names, the rest of `meta.json` and the `source.*` file. It also reads what the agents read to clarify an entry: `index/`, the run steps cited, and Zid's locales. Whether H-held.md allows those reads is a question for its fixes.
  - **E-2:** each part lists what its structures' sources state and no entry holds. R4 tests the evidence map's reading of the 18 dropped pages, and R3 the plans' prices.
    - A scan of every `meta.json` in the three repositories found two other keys that hold what a platform states and no entry holds: BigCommerce's plan prices, and Zid's store role list (one role, "Store Owner") in `store-permissions/meta.json`.
    - After the review, a selection rule makes both entries: the prices go to BC-1's corrections, and the role to ZD-4 before it runs. The other non-descriptive keys hold provenance (copies, runs read, instruments).
  - **E-3:** the review reads the evidence map, the selection's rows and the register's rows, as the agents did.
- **Part 3, the output:**
  - **O-1:** the verdicts now name a missing line, a wrong column, a wrong reading, an entry that differs from its source, and what a `new` should be. A group takes a row per entry where its entries differ.
  - **O-2:** each verdict but `stands` has a `cause` and an `effect`, and each line `in_leads`. R6 counts the misses by batch, structure, rule and third of the batch. It also names which effects are the important details, and what the dry run doesn't hold.
  - **O-3:** check 4 follows H-held.md's rule 5.
  - **O-4:** each part checks its notes' claims.
  - **O-5:** each fix stays within B-extent.md, or is named as a method ruling, and each recurring miss names the checker test that would catch it.
  - **O-6:** the inputs are pinned, rows are keyed by batch, line, entry and cap_id, and no field holds a tab or newline.
- **Part 4, its size:**
  - **K-1:** five parts, each by a fresh agent, and R6 joins them. The brief has a "How to work" section.
  - **K-2:** the parts run at `max`. The review measures what a closer reading finds, and a review at the batches' own level couldn't.
- **Part 5, the notes:**
  - **N-2:** the projection goes to the founder after the review, with the measured context growth and a re-plan to cost less (`PLAN.md`, section 8).
  - **N-3:** fixed. `held_amend.py` keeps each placement's whole reading in the evidence row.
  - **N-4:** `in_leads` is measured on the leads as they print at `99d429ad`. That version, after this inspection, skips an identifier many entries share (every Zid route had led to CM-PAY-003 by `$storeId`) and shows each lead's cell.
  - **N-5:** the output is named `held/review-H*`.
  - **N-1** and **N-6:** noted.
