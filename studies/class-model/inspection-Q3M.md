# Inspection of the brief for checking Q3's candidate misses against what is held (30 October 2026)

**What this is:** an inspection, before it runs, of `briefs/Q3-misses.md` with `method/q3_misses.py` (`misses` and `check`), as `PLAN.md`, section 3 asks. The inspector wrote neither, and changed no file except this one.

**What was read, and at which commits:**
- The brief and the checker are read at `ffbfe34b`. Neither changed up to `1d213be6`, while this inspection ran.
- In the same time, `PLAN.md` gained the held pass and an omission review (`9e59d2ef`), and `class_slice.py` the held pass's entries (`9d1369d3`). Both are read where they bear on this brief (Q3M-18, Q3M-19).
- The evidence is read at observed-sh `19a5f6435`, observed-sa `b0bd0b163`, other-product-class `0d79b794f`, and WooCommerce's release 11.2.1.
- The checker's tests ran on a scratch copy of `studies/class-model` (`CLASS_MODEL_DIR`), with fixtures that cite real held files.

Severity: **must fix** means an agent following the brief would write wrong lines. **Should fix** means the output would be less consistent, harder to check or act on, or more expensive than it needs to be. **Note** is for the record.

**What holds:**
- The brief carries out the founder's decision of 30 October in its order (the guides, then search) and in its list, with one narrowing (Q3M-12).
- `misses` prints every candidate miss that Q3's check names (Q3M-25).
- Of 42 variants with one fault each, the checker refused 29, among them every fault this inspection was asked to try (Q3M-16).
- Each tool works on a real term:
  - `corpus_search.py`, on Shopify, Salla and Zid, in English and Arabic;
  - `held_index.py`, `quote_check.py --text` and `schema_type.py`;
  - `class_slice.py` (`search`, `caps`, `key`, `outscope`), `q3.py where` and `land_points.py cell`.

---

## Must fix

**Q3M-1. The pages this repository holds can't be cited, so an agent will record them as not held.**
- *Found:*
  - The brief allows three kinds of source (lines 64 to 67): a held file in an evidence repository, a fetch archive's record, and WooCommerce's release.
  - The checker accepts only `https?://`, `observed-sh|observed-sa|other-product-class@<commit>:` or `woocommerce-11.2.1:` (`q3_misses.py` line 104). It loads no capture run: `quote_check.Sources(ROOTS, [])` (line 128).
  - Both search tools the brief names list this repository's own captures:
    - `corpus_search.py zid "التحويل البنكي" --max 3` listed 8 documents under "capture runs", such as `sharrwah-knowledge-map@ffbfe34b…:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/088-help.zid.sa/text.txt` (`https://help.zid.sa/bank-accounts/`).
    - `held_index.py https://woocommerce.com/document/woocommerce-shipping/` answered only `readable: sharrwah-knowledge-map:evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/048-woocommerce.com/text.txt (capture, 200)`.
    - `corpus_search.py` also reads the founder's saves: 23 BigCommerce files in `evidence/product-class/blocked-evidence-founder/bigcommerce/`.
  - Zid's own gap register sends its readers here: "Zid's other surfaces: help.zid.sa, docs.zid.sa, zid.sa, the app and theme markets, the mobile apps | not captured here; sharrwah-knowledge-map holds some of their pages (`evidence/product-class/`)" (`other-product-class@0d79b794f:zid/GAPS.md` line 18). `held-vs-read.md` says the concern map read "the public pages of Zid, BigCommerce and WooCommerce, captured in this repository".
  - On the scratch copy, the Zid page above was refused both ways:
    - cited as `corpus_search.py` prints it, with "source is a captured page's address, or <repository>@<commit>:<path> (woocommerce-11.2.1:<path> for the release)";
    - cited by its address, with "the quote is not found in https://help.zid.sa/bank-accounts/ (unresolved; not captured)".

    `quote_check.py` itself found the same quote both ways: by the path, and by the address when the capture run's folder is passed.
  - So no citation of these pages can pass. An agent who finds a Zid, BigCommerce or WooCommerce help or docs page here can only drop it. It then writes `held: no`, with a capture request for a page already held. `PLAN.md`, section 6, routes that as "page not read", for an agent, not as a capture.
- *Fix:*
  - In `q3_misses.py`:
    - line 104: accept `sharrwah-knowledge-map@<commit>:evidence/product-class/` (`ROOTS` already maps the repository);
    - drop `https?://` from the pattern, since nothing loads a capture run and an address can never resolve. Or load `evidence/product-class/runs/*` at line 128 and keep addresses.
  - In the brief:
    - add to "Read only": "this repository's captures of the platforms' public pages, `evidence/product-class/runs/*/`, and the founder's saves, `evidence/product-class/blocked-evidence-founder/<platform>/`, which `corpus_search.py` and `held_index.py` list";
    - add to `source`: "a page this repository holds, as `sharrwah-knowledge-map@<commit>:<path>`, with the path as `corpus_search.py` prints it".

**Q3M-2. `held_index.py` says "not held" for what other-product-class holds, and "not readable" for an archive held in parts.**
- *Found:*
  - It reads only observed-sa, observed-sh and this repository's capture runs (`held_index.py` line 76: `for repo in ("observed-sa", "observed-sh")`).
    - `held_index.py "https://dashboard.zid.sa/locales/ar/orders.json?2269948e"` printed `not held`. Yet `corpus_search.py zid "إيصال التحويل" …` found that address held at `other-product-class@0d79b794f…:zid/raw/runs/20261028T144617Z-dashboard-locales/fetch.warc.gz@666254`.
    - For `https://www.commerce.com/terms/`, it listed only this repository's capture of 12 October. It missed other-product-class's fetch run `20261029T024622Z-legal-pricing-docs`, whose `fetch.cdx` holds the address with status 200.
  - It counts an archive as in git only where `fetch.warc.gz` is (line 92). An archive over 100 MB is held in parts, `fetch-00000.warc.gz` and on (observed-sh's `README.md`, "Layout").
    - For the return-rules page, it printed `not readable: observed-sh@19a5f643:raw/runs/20261016T213535Z-help-en-ar-html-md/fetch.warc.gz@22399639 (cdx-only, 200)`.
    - Yet `git ls-files` shows that run's `fetch-00000.warc.gz` and `fetch-00001.warc.gz`, and its `fetch.cdx` puts the record in `fetch-00000.warc.gz`.
    - `quote_check.py` found "Return rules apply to fulfilled items" at `…/fetch-00000.warc.gz`, offset 22399639. It refused the location `held_index.py` printed: "git show 19a5f6435:…/fetch.warc.gz failed".
  - The brief says to use it "for an address you expect" (line 31) on all five platforms. On the three platforms that other-product-class holds, its "not held" can be false, as it was for Zid above.
- *Fix:*
  - In `held_index.py`:
    - read other-product-class's platform folders as it reads the observed repositories: `raw/runs/*/fetch.cdx`, the structures' `meta.json`, the steps in `actions.jsonl`, and `answers.jsonl`;
    - count a cut archive's parts as in git, and locate each record at the part `fetch.cdx` names.
  - Until then, add to the brief's tools: "`held_index.py` reads observed-sh, observed-sa and this repository's captures only. For Zid, BigCommerce and WooCommerce, use `corpus_search.py`, or grep the platform folder's `raw/runs/*/fetch.cdx` and `answers.jsonl`. A `cdx-only` location is readable where its run holds `fetch-NNNNN.warc.gz` parts, at the part `fetch.cdx` names."

**Q3M-3. A thing of several parts gets one `held`, and the part not held gets no capture.**
- *Found:*
  - Several misses name several things (`q3_misses.py` lines 20 to 32):
    - M-04 names five: "the admin's own language, right-to-left layout, numerals, date formats and mixed-direction text";
    - M-07 names four: "the return window, return fees, restocking fees, final sale";
    - M-01, M-02 and M-08 name two each.
  - `held` is `yes` or `no` for the whole line (the brief, line 78), and `capture` is "for `no` only" (line 83). The checker refuses a capture on a held line: "capture is for a miss not held" (tested).
  - Suppose Shopify holds the return window but not a return fee. One agent writes `yes` and another `no`. The part not held gets no capture, so the coordinator has nothing to write a handoff from. The same holds where only a title or a list entry is held, which step 3 ranks below the page (line 34).
- *Fix:*
  - In `MISSES`, give each miss its parts where the thing is several. Alternatives, such as "a delivery date or time slot", stay one part.
  - Add a column `parts` after `held`: each part as `<part>: yes` or `<part>: no`, `;`-separated.
  - `held` is then:
    - `yes` where every part is held;
    - `part` where some are;
    - `no` where none is.
  - `capture` is required for `part` and `no`, naming the run for the parts not held.
  - The checker tests that `parts` names each of the miss's parts once.

**Q3M-4. `held` has no value for three cases the plan names: absent from a complete list, held but not readable, and can't tell.**
- *Found:*
  - **Absent from a complete list.** `PLAN.md`, section 6, the test form, step 2: "Absence counts only from a complete list the platform publishes, such as an enumerated schema or a full plan table. Otherwise it is a gap."
    - The repositories hold lists that may be such (a reading): Zid's `store-plan-policies` ("every policy key, whether it is enabled") and BigCommerce's `plan-comparison` (each platform's `structures/REGISTER.tsv`).
    - A platform may also state that it doesn't do the thing.
    - The brief has no line for either. With `yes`, the checker demands a capability for a thing the platform doesn't do (`q3_misses.py` line 176). With `no`, it demands a capture of something already settled (line 159).
  - **Held but not readable.** Section 6, Evidence: "if it is held but not readable, the reader is extended".
    - `held_index.py`'s header names the case: "cdx-only   an index line whose archive is not in git: held, but not readable from the repository".
    - observed-sa has 68 fetch runs with a `fetch.cdx`, and 63 with their archive in git.
    - observed-sh's traces and screenshots are not committed (its `README.md`, "What is in git").

    An agent would write `no` with a capture, asking for a new run where the plan extends the reader.
  - **Can't tell.** The rules say "Where you can't tell, say what would settle it" (line 103), but `held` has no `unclear`. One string shows the problem: Zid's dashboard has `details.viewTransferReceipt`, "عرض إيصال التحويل", in its orders strings (`other-product-class@0d79b794f:zid/structures/dashboard-locales/items.jsonl` line 23232). It may or may not be M-13's thing (a reading). One agent will write `yes`, another `no`.
- *Fix:* add to `held`:
  - `absent`: a complete list the platform publishes leaves the thing out, or the platform says it doesn't do it. The list or the statement is cited, `capture` is empty, and `capability` is the miss's (Q3M-5);
  - `unreadable`: held only in a form the tools can't read. `capture` names the file and where it is held (the mirror, a trace), so the reader is extended rather than a new run made;
  - `unclear`: a statement may be the thing, but its words don't settle it. `capture` says what would settle it.

  Test each in the checker.

**Q3M-5. `capability` is written per line but decided across the miss, and the checker passes a `new` with no place.**
- *Found:*
  - Step 5 decides `new` across the platforms: "Where no capability is its thing and some platform gives it a place of its own, write `new`" (the brief, line 37). But the column is per line, and its one rule is per line: "`none` only where it isn't held and no capability is its thing" (line 81).
  - Take M-07, with a place on Shopify only. An agent may write `new` on Shopify's line, and on Salla's line (not held) `new`, `none` or the capability that contains it. All three pass: on the scratch copy, one miss with `new`, `CM-RET-003` and `none` on three of its lines printed "0 problems".
  - A capability that is the thing and one that only contains it are both written as a cap_id. In the first case, Q3's `partly` turns out covered. In the second, the thing is a feature, or detail. The coordinator can't tell the two apart.
  - The baseline fixture had `new` on M-07's Shopify line and `place` `none` on every line of M-07. The checker printed "35 of 35 lines, 4 statements, 4 citations; 0 problems", against step 5.
- *Fix:*
  - In the brief: "`capability` is the miss's, the same on all five of its lines, written after all five are read. It is:
    - the cap_id whose thing it is;
    - `new`, where at least one of its lines names a place;
    - otherwise, the cap_id of the capability whose thing contains it.

    A column `as` says which: `its thing`, `new` or `feature`. `none` only where nothing is held on any platform, and no capability contains it."
  - In `q3_misses.py`, test that every line of a miss has the same `capability` and `as`, and that a `new` has a place on at least one of them.

**Q3M-6. The "place of its own" test adds a clause to B-extent's rule that settles M-01 before the run, and two of its kinds are undefined.**
- *Found:*
  - B-extent's rule: "where at least one platform gives it a place of its own: an admin section or route, an API group, a plan line, or an app category. A single feature flag isn't enough." (`B-extent.md` line 131; the dry run's ruling 2, `review-dry-run-rulings.md` line 40.)
  - The brief applies it "by B-extent's rule", then adds: "A single feature flag, or a setting on a page, isn't one" (line 35). Neither source has the second half.
  - The clause decides a case ahead of the evidence:
    - Shopify's router gives tipping an anchor of the Checkout settings route: `checkout-settings:index`, section Checkout, its anchors including "Tipping -> tipping" (`observed-sh@19a5f6435:structures/shopify/admin-router/items.jsonl` line 358). Its route titles name it: `checkout-settings:index:tipping:title`, "Tipping" (`admin-route-titles-en/items.jsonl` line 130).
    - Read as "a setting on a page", tipping is a feature of CM-CHK-001 before anyone reads it. Read as "an admin section", it has a place of its own, and is `new` unless a capability is its thing.
    - Return rules, by contrast, have routes of their own: `setting:legal:cancel_return_policy_update`, path `legal/cancel-return-rules/:id` (held pass entry SH-E-00907).
  - "Admin section" and "API group" are not defined, so two agents will read them differently:
    - one will take a router's section as an admin section, another a titled part of a page;
    - one will take a GraphQL object such as `ReturnPoliciesReturnRules` as an API group (the brief's own example points to the schema, Q3M-8), another a group of the API's own reference.

    A reading: most of batch A's misses (tipping, test mode, the admin's language, scheduled delivery, packages) sit in exactly these borderline places.
- *Fix:*
  - Quote B-extent's rule as it stands, and drop "or a setting on a page".
  - If the coordinator holds that a part of a settings page isn't a place of its own, that changes the convention for every part. Make the change in `B-extent.md` and the dry run's rulings, marked as the coordinator's, and say how an anchor counts.
  - Define each kind by the platform's own organization, for instance:
    - an admin route: an entry of the platform's route manifest, with its own path (Shopify's `admin-router`, Salla's `dashboard-app-routes`, Zid's `dashboard-route-manifest`);
    - an admin section: a section that the manifest or the admin's navigation names;
    - an API group: a group that the API's own reference names, not one type, field, mutation or enum value;
    - a plan line: a row of a plan table;
    - an app category: a category of the platform's app store.

**Q3M-7. "`none: <why>` (a paid plan, … a country)" contradicts the plan and the handoffs, which route both as capture requests.**
- *Found:*
  - Step 6: "Where no run can, write `none: <why>` (a paid plan, a document, a country)" (line 39).
  - `PLAN.md`, section 6:
    - line 362: a capture request names "a journey from the repository's own catalog, a held paid store, or a store set up for it";
    - line 364: "only what no run can capture goes to the founder".
  - `handoffs/README.md`:
    - line 11: "A request may need the founder, for something only the founder can give: a payment, a phone, a store on a paid plan. It says so under **Needs**";
    - H-005 is such a request, for a store on Salla's Special plan;
    - H-006 ran with "a new Shopify account located in the United States" (line 30), so a country can be a run too.
  - An agent following line 39 writes `none` for these. The coordinator would then take to the founder what is a capture request.
- *Fix:* replace line 39's last two sentences with:
  - "Where a run could capture it with something only the founder can give (a payment, a store on a paid plan, a phone, an account in another country), name the run and add `needs: <what>` (`handoffs/README.md`, Needs).
  - `none: <why>` only where no run can capture it at all, such as a document only the platform holds, or what only a real verification would show.
  - That a page exists that would hold it is an assumption: say so."

## Should fix

**Q3M-8. The brief's example pre-answers M-07 on Shopify, and points to the schema as its place.**
- *Found:*
  - Line 3: "Shopify's return rules, for one, are held in its Help Center and its admin API schema, and the concern map has no statement on them."
  - It is true. Both hold them:
    - `observed-sh@19a5f6435:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/fulfillment/managing-orders/returns/return-rules.md`;
    - `schema_type.py … ReturnPoliciesReturnRules`: "Return Rules that apply to returns under a return policy profile."
  - But it is batch A's own line (M-07 on Shopify), stated without a citation. It names the schema, not the routes, and the routes are what step 4 turns on (Q3M-6). A reading: an agent may stop at the two places named.
- *Fix:* use an example outside the 13 misses. Or keep this one, cited, and add: "M-07 is batch A's to check. This names two of the places that hold it, not its place of its own."

**Q3M-9. `misses` prints Q3's rests as they stand, and three of them say "none held" of pages observed-sh holds.**
- *Found:* in the output of `q3_misses.py misses --batch A`:
  - M-05: "Shopify's Help Center on local delivery settings, and Salla's and Zid's help pages on delivery and shipping settings, none held". Held: `…/md/en/manual/fulfillment/setup/delivery-methods/local-delivery.md`.
  - M-06: "Shopify's Help Center on shipping packages in its shipping settings, and the label-buying screens of Salla and Zid, none held". Held: `…/md/en/manual/fulfillment/setup/packaging/setting-up-packages.md` and `packages-and-weights.md`.
  - M-07: "Shopify's Help Center on return rules and self-serve returns, and Salla's and Zid's returns settings, none held". Held: `…/managing-orders/returns/return-rules.md` and `self-serve-returns/setup.md`.

  Q3's batches read the concern map only (the brief, line 3), so "none held" there means that the concern map holds none. Printed as it stands, it reads as a fact about the repositories, and it steers a run toward `no` (a reading).
- *Fix:*
  - In `cmd_misses`, print each rest under the label "Q3's batch, from the concern map only: its 'none held' and 'not held' are what this check tests".
  - In the brief, after line 7, add: "A rest's 'held', 'not held' and 'none held' are about the concern map, not the repositories."

**Q3M-10. Four misses are worded narrower or wider than their rows.**
- *Found:* `q3_misses.py` lines 20 to 32, against the rests that `misses` prints:
  - **M-02** takes a design aim into the thing: "kept out of the store's balances and reports". It comes from `pay:PAY-36`, which asks how outcomes can be simulated "without blocking live sales or mixing test money into balances and reports", which is Sharrwah's aim. A test mode whose statements don't say how it stays apart from the reports would then read as not the thing (a reading).
  - **M-11** narrows the rest's "a buyer's refusal at delivery as a way to contest" to "a buyer refusing a cash-on-delivery order at the door", and drops "as a way to contest". `pay:PAY-30` asks about every channel a buyer can use to contest. A refused prepaid delivery falls outside the wording.
  - **M-01** says "at checkout", while `pay:PAY-02` asks about a tip as an event that changes what a buyer owes. Shopify's POS tips are held: `…/manual/sell-in-person/shopify-pos/tips.md`, and the POS setting "Collect tips" (held pass entry SH-E-06185). One agent will count them, another won't.
  - **M-09** drops the rest's "for merchants", and adds "editions", Shopify's own word for its releases.
- *Fix:*
  - M-02: "a payment test mode in a store: test orders and simulated payment outcomes, and what the platform says of how they stay apart from live orders, balances and reports".
  - M-11: "a buyer refusing a delivery at the door, as a way to contest a payment, whatever the payment method: the shipment's return and what is charged".
  - M-01: say whether in-person tips are part of the thing.
  - M-09: "each platform's dated record of what it added, changed or removed, for merchants and for developers: changelogs and release notes".

**Q3M-11. `capability` has no value for a held thing that isn't a capability.**
- *Found:*
  - The checker refuses `none` on a held line (`q3_misses.py` line 176).
  - M-09's records are held:
    - WooCommerce's release carries its changelog: `woocommerce-11.2.1:readme.txt` line 171, "== Changelog ==", and line 173, "= 11.2.1 2026-10-09 =";
    - Shopify's are captured: `shopify/dev-changelog` in observed-sh's `structures/REGISTER.tsv`, and `merchant-changelog/changelog.shopify.com@home` (held pass entry SH-E-05557).
  - The model's `CM-API-006` is "API versioning and change log: the platform's versions of its API, when it adds one, and its record of changes". It covers the API's record only.
  - A record of what changed for merchants is a source for `km:EVO-01`'s "where is the class heading". It may not be "something a store or the platform can have or not have" (B-extent line 58), a reading. An agent must still write a cap_id or `new`.
- *Fix:* add `not a capability` to `capability`: a thing held that isn't something a store or the platform can have or not have (B-extent, "Build capabilities"), with why in `reading`. The checker accepts it on a held line.

**Q3M-12. The guides: `index/` is narrowed against the founder's decision, the catalogs step 6 needs are left out, and nothing says what to read whole.**
- *Found:*
  - The founder's decision names `index/` whole: "README.md, docs/READING.md, docs/GAPS.md, docs/OPERATING.md, index/, structures/README.md and structures/REGISTER.tsv" (`founder-decisions.tsv`, last row). For observed-sh and observed-sa, the brief narrows it to "`index/` (`runs.tsv`, `run-notes.tsv`, `instruments.json`)" (line 11).
  - That leaves out `index/ledger-summary.tsv` and `index/ledger/`:
    - observed-sh's `README.md`, under "Starting points", names them right after `structures/REGISTER.tsv`, for "What exists and why some things don't";
    - observed-sh's ledger holds `journey-unit.tsv`, `admin-route.tsv` and `sitemap--help-shopify-sitemaps.tsv`;
    - observed-sa's holds `journey-unit.tsv`, `settings-field.tsv` and `feature.tsv`.
  - Step 6 asks for "a journey … from the repository's own catalog" (line 39). The catalogs are `index/ledger/journey-unit.tsv` and observed-sh's `derived/journey-catalog.jsonl` (its `docs/READING.md`, "Indexes"). Neither is on the list.
  - observed-sa has no `index/instruments.json`.
  - The files the brief lists come to 1,650,105 characters:
    - 1,163,329 of them are the two observed repositories' `runs.tsv` and `run-notes.tsv`;
    - 228,966 are their registers.

    The brief says to read a long document "never whole" (line 108), but not which guide is long. Two agents will read different amounts, and record different things in `guides`.
- *Fix:* replace lines 11 and 24 to 30 with:
  - "Once, at the start, read these whole (about 132,000 characters): each observed repository's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `docs/OPERATING.md` and `structures/README.md`; other-product-class's `README.md` and `docs/OPERATING.md`; and each platform folder's `README.md` and `GAPS.md`.
  - For each miss, grep these with its terms in each language: `structures/REGISTER.tsv`, `index/runs.tsv`, `index/run-notes.tsv`, `index/ledger-summary.tsv` and `index/ledger/*.tsv` (journey units, routes, sitemaps), `index/instruments.json` where it exists, and observed-sh's `derived/journey-catalog.jsonl`.
  - `guides` records, for the line, the rows that bear on it: structure ids, run ids, ledger rows, and the `GAPS.md` row."

**Q3M-13. A "searched, not found" isn't recorded at a commit.**
- *Found:*
  - `PLAN.md`, section 6 (line 365): "A 'searched, not found' lists what it read, at a commit."
  - `searched` asks for "the tool, the terms and the platform" (line 31), and `guides` for what was read (line 30). Neither asks for a commit.
  - The checker tests only that each is non-empty: `guides` = `-` passed (tested).
- *Fix:* end `guides` and `searched` with the commits read: `observed-sh@<c>`, `observed-sa@<c>`, `other-product-class@<c>`, `sharrwah-knowledge-map@<c>` for its captures, and `woocommerce-11.2.1`. Or, if the commits are fixed for the run (Q3M-26), put them once at the top of the notes.

**Q3M-14. A search costs more than the brief says.**
- *Found:*
  - Measured:

    | Search | Time | Output |
    | --- | --- | --- |
    | `corpus_search.py shopify "return rules" "return rule" --max 6`, run twice | 1 min 52 s and 1 min 54 s | 480 lines, 78,879 characters |
    | Salla, three Arabic terms, `--max 5` | 56 s | 29,873 characters |
    | Shopify with `--runs-only` | 0.8 s | 60,638 characters |

  - `--max` caps the detailed listings, then prints every address past the cap, one per line (`corpus_search.py` line 28: "every address past the cap follows, one line each").
  - The brief says: "A search takes seconds to a minute. Keep its output short with `--max`" (line 107).
  - With 7 misses and several terms and languages, a batch's Shopify searches alone can add over a million characters to its context (an assumption on the number of searches).
- *Fix:*
  - "Search each miss once per platform and language, with all its terms in one call: any term matches.
  - Write the output to a file in your scratchpad. Read its first 80 lines and its last line, and grep the rest."

  Or add an option to `corpus_search.py` that leaves out the addresses past the cap.

**Q3M-15. `capture` doesn't carry what a handoff needs.**
- *Found:*
  - `handoffs/README.md` (line 13 on) says every request names:
    - the repository and the instrument;
    - what to capture, step by step, and where to stop;
    - what is already held;
    - why;
    - what the founder must give;
    - when it is done.
  - `capture` asks only for "the run" (line 39):
    - the repository goes without saying for Shopify and Salla, but not for the three platforms in other-product-class, where handoffs now go too (H-009);
    - nothing asks for the instrument, the addresses or screens, where to stop, or what is needed.
- *Fix:* "`capture`: `<repository>; <instrument, from index/instruments.json>; <the run: a journey unit by its ledger id, a fetch of named addresses, or the GAPS.md row, quoted>; stop at <…>; needs: <what, or nothing>`." The line's statements and `guides` give what is already held. The miss and its Q3 rows give why.

**Q3M-16. What the checker lets through.**
- *Found:*
  - I built a baseline that passes: 35 lines, and 4 statements on Shopify and WooCommerce. Its citations are a Help Center page, a fetch archive's record, the schema's introspection record and a release file.
  - I then made 42 variants, each with one fault. The checker refused 29 (listed under "What I ran"), among them:
    - a quote not in its source;
    - a statement outside its quote;
    - a held line with no statement;
    - a place naming another row's statement, on the same platform or another;
    - a wrong id range;
    - a missing platform.

    Two of the 29 are this repository's captures, which it should accept (Q3M-1).
  - It passed the other 13 with "0 problems":
    - one is a statement that the platform doesn't do the thing, recorded as held, which no checker can see (Q3M-4);
    - the other 12 are in the table below, with the baseline's own `new` that has no place.

    | Fault | Against (the brief's line, unless named) |
    | --- | --- |
    | `place` empty | line 80: `none`, or a kind |
    | `place` naming a `decides` statement | line 35, "the statement that shows it"; a place is `where`, "the place the platform gives it" (line 51) |
    | `new` with no place on any line of the miss | line 37 (Q3M-5) |
    | one miss with `new`, a cap_id and `none` on three lines | Q3M-5 |
    | Salla's statement citing Shopify's citation, `Q3-SH-C100` | the checker's own "this platform's citations". `cites` is one dict across the platforms (`q3_misses.py` line 93), so this passes for a platform read after Shopify, and the reverse was refused |
    | a Salla citation whose source is observed-sh | the platform's repository |
    | a citation that no statement names | none stated |
    | a citation at an older commit of observed-sh, `efb896be8` | line 65: "at the repository's current commit" |
    | locator `line 999` | line 68. `quote_check.py` reads a locator only for an archive (its line 10) |
    | `capture` = `none` | line 39: `none: <why>` |
    | a field in double quotes | line 72: no quoting |
    | `guides` = `-` | line 30 |
    | `statement` = "final sale", two words of its quote | line 57: "a sentence or the shortest whole part that says it" (a judgement; a minimum length would catch the worst) |

  - Two of its messages mislead:
    - for a bad source it suggests "a captured page's address", which can never pass (Q3M-1);
    - for corpus_search's `<path>@<offset>` pasted as a source, it prints a git error rather than the rule.
- *Fix,* in `cmd_check`:
  - refuse an empty `place`;
  - require a place's statement to have the placement `where`;
  - test the miss's `capability` and `new` as Q3M-5 says;
  - keep citations per platform, and look a statement's `cite_ids` up there only;
  - require a citation's repository to be the platform's: observed-sh for Shopify, observed-sa for Salla, and for the others `other-product-class@…:<platform>/`, `woocommerce-11.2.1:` or this repository's captures of the platform's hosts;
  - require every citation to be named by a statement;
  - require the commit to be the repository's `HEAD`, or one the coordinator's message names;
  - for a file, require the quote's first words within a few lines of `line N`;
  - require `none` in `capture` to be followed by `: <why>`;
  - refuse a field with `"`;
  - for a source ending in `@<digits>`, say: "the offset goes in `locator`".

**Q3M-17. The source form for a fetch archive doesn't fit an archive held in parts, and the release's path isn't anchored.**
- *Found:*
  - Line 66 gives "`<repository>@<commit>:<path to fetch.warc.gz>`".
    - An archive over 100 MB is held in parts, and `fetch.cdx` names each record's part.
    - So a citation must name the part. `quote_check.py` found the quote at `…/20261016T213535Z-help-en-ar-html-md/fetch-00000.warc.gz`, offset 22399639, and refused `…/fetch.warc.gz` at that offset (Q3M-2).
  - Line 67 gives `woocommerce-11.2.1:<path>`, but not what the path is relative to.
    - It is relative to `/home/user/woocommerce-release/11.2.1/woocommerce` (the checker's `ROOTS`), not to the folder line 13 names.
    - `woocommerce-11.2.1:woocommerce/includes/…` was refused (tested).
- *Fix:*
  - Line 66: "a record of a fetch archive, as `<repository>@<commit>:<the archive's file, as fetch.cdx or corpus_search.py names it: fetch.warc.gz, or its part fetch-NNNNN.warc.gz>`, with the record's offset as the locator. `corpus_search.py` prints `<path>@<offset>`: split it."
  - Line 67: "`woocommerce-11.2.1:<path>`, the path inside `/home/user/woocommerce-release/11.2.1/woocommerce/`, as `corpus_search.py` prints it."

**Q3M-18. The model can't cite what this check writes.**
- *Found:*
  - `q3_misses.py`'s header says these statements are what "only the coordinator's amendments from Q3's check cite in the model".
  - `class_slice.citable()` reads the concern map's statements, the subjects' (`S01-SA-104`) and the held pass's entries (`ZD-E-00001`), the last added at `9d1369d3`.
  - `check_class_part.py`'s `plat()` (line 52) resolves `XX-C-`, `XX-I-`, `XX-E-` and `S\d\d-XX-\d+`. Run on four ids, it returned `None` for `Q3-SH-100`, and a platform for `SH-E-00907`, `S01-SA-104` and `SH-C-058/where/SH-S-7098`.
  - So an amendment's cell that cites a Q3 statement would be refused as "not a statement key" (line 373; a reading of the code, not run on a part).
- *Fix:* before the amendments, do for `q3/statements/` what `9d1369d3` did for the held pass:
  - extend `class_slice.citable()` and `subject_citations()` to `q3/statements/*/<platform>/statements.tsv` and `citations.tsv`;
  - extend `plat()` to `Q3-XX-\d+`.

**Q3M-19. The held pass now reads the same evidence, and this brief can't name what is already citable.**
- *Found:*
  - `PLAN.md`, Stage 4A (line 221, added at `9e59d2ef`) runs a held pass. It reads "route manifests, settings, navigation, plans, permissions, catalogs and changelogs … entry by entry", and places them on the model. Its entries are listed with ids, in `held/<platform>/entries.tsv`.
  - Among them are items that bear on the misses (a reading):
    - SH-E-00907, the return rules' route `setting:legal:cancel_return_policy_update` (M-07);
    - SH-E-06185, the POS setting "Collect tips" (M-01);
    - SH-E-05557, a merchant changelog entry (M-09, batch B).
  - The brief doesn't mention the held pass. `statements` takes only the batch's own Q3 ids (the checker: "is not a statement of statements/A/"), so an agent must quote an entry again, under a second id. It can't name a concern-map key either, where `class_slice.py search` (step 2) finds one that Q3's batch missed.
  - One item then has two ids, and the held pass and this check may place it differently: a feature of CM-CHK-001 against `new` (a reading).
- *Fix:*
  - Decide the order of the two, and say it in the brief:
    - if this check runs first, its `new` capabilities and features go to the held pass as leads;
    - if the held pass runs first, this check reads only what its entries don't hold.
  - Either way, let `statements` also name existing ids, a concern-map key or a held pass entry, which the checker resolves through `class_slice.citable()`. Add to the brief: "Where `class_slice.py search`, or a grep of `studies/class-model/held/<platform>/entries.tsv`, finds the item, name its id. Write a Q3 statement only for what neither holds."

**Q3M-20. A `new` capability and its cells need more than a line gives.**
- *Found:*
  - The coordinator amends through `<domain>-amend` parts, "each with every platform's cells" (`Q3-check.md` line 102).
  - Each cell needs evidence rows with `supports`: `core`, `own-service`, `extension-point`, `outside` or `shows` (`B-extent.md` lines 113 to 118).
  - A new capability needs a name in every platform's terms, an area and a parent (`B-extent.md` lines 62 to 66 and 140).
  - A line gives a cap_id or `new`, statements with Q1's placements, and a reading. The notes ask only for "a capability, a feature of one, or detail" (line 87).
- *Fix:*
  - Add `supports` to `misses-<batch>.tsv`: a reading, by B-extent's values, `;`-separated.
  - For `new`, the notes give its proposed name in every platform's terms, its `area`, its `parent`, and the capabilities it touches.

## Notes

- **Q3M-21.** Step 5's "`q3.py where` on a statement of the same page" (line 36) can't be done with the tools named. No tool finds the concern map's statements by their page:
  - `class_slice.py key` prints a statement's id, identifier and text, not its source (`key SH-C-058/where/SH-S-7098`);
  - `search` matches the identifier and the statement only (`class_slice.py` line 315).

  Say instead: "search the concern map with the page's title, and run `q3.py where` on what it finds".
- **Q3M-22.** `quote_check.py --text` and `class_slice.py outscope` behave in ways the brief doesn't say:
  - `quote_check.py --text SOURCE` (line 17) needs the record's offset for a fetch archive ("not readable: a fetch archive is cited with its record's offset as the locator");
  - for a captured page by its address, it needs the capture run's folder ("not readable: not captured" without it);
  - `class_slice.py outscope` prints nothing at all when nothing matches (Salla, "استرجاع; returns"), so a search that finds nothing leaves no line to record.
- **Q3M-23.** `identifier`, "the page's title, or the API's name" (line 56), doesn't say what to write for an item of a structure: a route's id, a locale key, a plan's key. Add "or the item's own id".
- **Q3M-24.** Ids run from 100 to 199 per platform in batch A (line 48). Batch A's Shopify lines (7 misses) may need nearly that many statements (an assumption). Say what to do past 199, or widen the ranges.
- **Q3M-25.** `MISSES` names all 15 rows that Q3's check marks as a candidate miss, in `result` or `rest`, and no others:
  - 4 are `partly / candidate miss: held`, and 11 `partly / candidate miss: not held`, across the 13 misses;
  - Q3's check has no `unclear` row. Over `q3/check-*.tsv`: 163 covered, 63 beyond the class, and 19 partly / beyond the class.
- **Q3M-26.** The two batches don't collide: their ids run in separate ranges, and each writes its own files. The evidence repositories' `HEAD`s should stay fixed while they run: a new commit rebuilds `corpus_search.py`'s caches (minutes), and leaves citations at two commits. The coordinator's message could name the commits.
- **Q3M-27.** `corpus_search.py`'s WooCommerce corpora (line 69) don't include the six `items.jsonl` of `woocommerce/structures/`. But each comes from saved answers, which it does read: `payments-providers/meta.json` names run `20261029T023051Z-country-change-en`. A citation would then go to the answer file.
- **Q3M-28.** The brief keeps the plan's rules (lines 94 to 103):
  - every claim is one of three;
  - the founder's words are never evidence;
  - credentials are read and cited;
  - the evidence repositories are read-only;
  - `python3 -I`;
  - no commits.

---

## What I ran

All from `/home/user/sharrwah-knowledge-map`, with `python3 -I`. The tests that write ran on a copy of `studies/class-model/` at `/tmp/claude-0/-home-user-sharrwah-knowledge-map/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/cm`, with `CLASS_MODEL_DIR` set.

**The checker:**
- `method/q3_misses.py misses --batch A` and `--batch B`.
- `method/q3_misses.py check --batch A`:
  - on the empty copy: "0 of 35 lines …; 36 problems";
  - on a baseline: "35 of 35 lines, 4 statements, 4 citations; 0 problems";
  - on 42 one-fault variants. The generator is `/tmp/claude-0/-home-user-sharrwah-knowledge-map/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/fixtures/gen.py`, and its results are in `/tmp/claude-0/-home-user-sharrwah-knowledge-map/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/fixture-results.txt`.
- The 29 variants it refused:
  - a quote not in its source;
  - a statement outside its quote, and a statement paraphrasing it;
  - a held line with no statement;
  - a place naming another row's statement, on the same platform and on another;
  - a stmt_id and cite_id out of range;
  - a wrong prefix;
  - a missing platform;
  - a place of an unknown kind;
  - Shopify's statement citing Salla's citation;
  - a fake commit;
  - a captured page's address;
  - this repository's capture, by path and by address;
  - `path@offset` as a source;
  - the release's path with its folder;
  - `held` = `partly`;
  - a held line with `capability` `none`;
  - an unknown cap_id;
  - a capture on a held line, and none on a line not held;
  - statements on a line not held;
  - statement ids separated by commas;
  - an eleventh field;
  - batch B's miss;
  - a duplicate line;
  - a statement of another miss;
  - an unknown placement.
- The 13 it passed are in Q3M-16.

**The search tools:**
- `method/corpus_search.py`:
  - `shopify "return rules" "return rule" --max 6` (twice);
  - `shopify "return rules" --runs-only --max 5`;
  - `zid "إيصال التحويل" "إثبات التحويل" "صورة التحويل" "إيصال الدفع" --max 5`;
  - `zid "التحويل البنكي" --max 3`;
  - `salla "سياسة الاسترجاع" "مدة الاسترجاع" "رسوم الاسترجاع" --max 5`.
- `method/held_index.py`, on Shopify's return-rules page, `help.zid.sa`, a BigCommerce docs address, a WooCommerce docs page, `www.commerce.com/terms/` and a Zid dashboard locale file.

**The quote and schema tools:**
- `method/quote_check.py`, on 11 quotes:
  - a Help Center file;
  - the same page's record in a fetch archive;
  - two quotes from the schema's introspection record;
  - a Zid locale line;
  - a release file;
  - a captured Zid page, by address with and without its run, and by path;
  - a record in a part of a split archive, and the same record under the archive's whole name.
- `method/quote_check.py --text`, on a Help Center file, an archive with and without its offset, and a captured page's address with and without its run.
- `method/schema_type.py …/admin-graphql-schema/2026-10 ReturnPoliciesReturnRules`.

**The model's tools:**
- `method/class_slice.py`: `search --platform shopify --terms "tipping; tip"`, `caps --terms "return; refund; returns"`, `key` on a statement and an inventory id, and `outscope` on Salla and Shopify.
- `method/q3.py where SH-I-2109 SH-C-041/boundary/SH-S-2538`, and `method/land_points.py cell CM-RET-003 shopify`.
- `check_class_part.plat()` on four ids.

**The repositories and the check's files:**
- `ls` and `wc -c` of every guide the brief lists, in all three repositories.
- Greps of observed-sh's `admin-router` and `admin-route-titles-en` items, its Help Center files and `structures/REGISTER.tsv`, each `GAPS.md`, and `held/<platform>/entries.tsv`.
- A count of observed-sa's fetch runs whose archive is in git.
- A comparison of `MISSES` with `q3/check-*.tsv`.

## What I didn't check

- I settled no miss. The evidence quoted here shows what the brief's steps will meet, not the result of any line.
- I built no fixtures for batch B. The checker's code is the same for both batches.
- I didn't read `briefs/H-held.md`, `STATE.md` or `held-vs-read.md` beyond its first lines. The held pass enters this inspection only through `PLAN.md`, Stage 4A, and `class_slice.py`, which the brief names.
- I didn't verify that the lists named in Q3M-4 are complete lists in the plan's sense.
- Q3M-18's refusal is a reading of `check_class_part.py`. I ran `plat()`, not a part with a Q3 key.
- The cost in Q3M-14 is measured on six searches. The total per batch is an assumption.

---

## The coordinator's response (30 October 2026, about 16:00 UTC)

**The order (Q3M-19):** the held pass runs first. Q3's 13 candidate misses are then checked in its second stage, which reads the held pages for the cells that still hold nothing. So one brief, one statement scheme and one checker serve both, and the second stage cites the held pass's entries by their ids where they hold the thing. `briefs/Q3-misses.md` doesn't run: it is marked superseded, and the second stage's brief takes each finding below.

**Done now, since the held pass or every later reading needs them:**
- **Q3M-2:** `held_index.py` reads other-product-class's platform folders: fetch archives, structures' `meta.json`, steps and saved answers. It reads an archive held in parts at the part `fetch.cdx` names. Tested on the three addresses this inspection gives:
  - Shopify's return rules are now readable at `fetch-00000.warc.gz@22399639`;
  - Zid's locale file is held in `zid/raw/runs/20261028T144617Z-dashboard-locales`;
  - `www.commerce.com/terms/` is held in BigCommerce's `20261029T024622Z-legal-pricing-docs` and `contracting-entities`.
- **Q3M-6:** B-extent's rule is quoted as it stands, with no clause added. What each kind of place of its own is, by the platform's own self-description, becomes the coordinator's convention, in `B-extent.md`'s "Conventions from the dry run". It counts an anchor that a route manifest names, with its own title and path, as an admin section. The held pass's brief takes it before it runs.
- **Q3M-10:** the four misses are reworded to their rows (`q3_misses.py`, `MISSES`). M-01 takes in-person tips in, since `pay:PAY-02` asks about a tip as a change to what a buyer owes, in any channel.
- **Q3M-14:** `corpus_search.py --brief` prints, past the cap, a count per corpus instead of every address. A Zid search came to 1,670 characters in 17 seconds.

**Taken into the second stage's brief and checker:**
- **Q3M-1:** this repository's captures and the founder's saves, as `sharrwah-knowledge-map@<commit>:<path>`, with the capture runs loaded.
- **Q3M-3:** a thing's parts, each held or not, with `held` as `yes`, `part` or `no`, and a capture for the parts not held.
- **Q3M-4:** `absent`, cited to the complete list or the platform's own statement; `unreadable`; `unclear`.
- **Q3M-5:** the miss's capability decided once across its lines, with `as`: its thing, new or feature.
- **Q3M-7:** a capture that needs the founder is a request with `needs`. `none: <why>` only where no run can capture it.
- **Q3M-8:** no example drawn from the misses.
- **Q3M-9:** the rests printed as the concern map's only.
- **Q3M-11:** `not a capability`.
- **Q3M-12:** the guides read whole once, about 132,000 characters, and the rest grepped. `index/` whole, with the ledgers and the journey catalog.
- **Q3M-13:** the commits fixed for the run and named in its message.
- **Q3M-15:** a capture names the repository, the instrument, the run, where to stop and what is needed.
- **Q3M-16:** each test this inspection lists.
- **Q3M-17:** an archive's part, and the release's path inside `/home/user/woocommerce-release/11.2.1/woocommerce/`.
- **Q3M-18:** the second stage's statements made citable by the model's tools before any amendment.
- **Q3M-20:** `supports` in each line. For `new`, the notes give its name in every platform's terms, its area and its parent. The coordinator makes it with every platform's cells.
- **Notes:**
  - Q3M-21 and Q3M-23 are taken in the wording;
  - Q3M-22 and Q3M-27 are written into the tools' notes;
  - Q3M-24: ids get four digits;
  - Q3M-25, Q3M-26 and Q3M-28 are for the record.

