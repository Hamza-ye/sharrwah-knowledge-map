# Inspection of the brief `P-points.md` and its script, before it runs

**What this is.** `PLAN.md`, section 3: "Before a brief runs, a separate agent reads it for anything that presupposes the answer (inspection: Fagan 1976)." I made none of what I inspect: `studies/class-model/briefs/P-points.md` (58 lines) and `method/land_points.py` (472 lines), on `claude/vibrant-meitner-oh70v4`, 30 October 2026.

**The state I tested against.**
- I began at commit `81d7d898`, with C's anchor batch 11 being written in the working tree.
- HEAD moved to `f2293a5e` while I worked: C's anchor is now complete, with 89 capabilities.
- The brief, the script and the subjects' files are the same at both commits.
- I re-ran the sizes, the lead ranking, the count of `open` leads and the baseline check at `f2293a5e`, with the same results. The figures below are from it.
- Domain C still isn't merged. The script reads it from `C-anchor` and `C-woocommerce`, with no Zid or BigCommerce part yet, so C's capabilities and cells cited below aren't final.

**What I read:**
- the brief and the script;
- `PLAN.md`, sections 3 and 6, and Stage 4A, including line 219, "The subjects' points";
- `founder-decisions.tsv`, whole, with the rows of 25, 26, 29 and 30 October (lines 12–22 and 26–31), and the founder's message of 30 October that its line 30 cites;
- `architecture/plan.md`, sections 1, 3 and 4;
- the two subjects' `variation-points.tsv`, `variants.tsv`, `register.tsv`, and `analysis.tsv` or `answers.tsv`, a few rows at a time;
- the model, through `class_slice.py` (`model`, `caps`) and `q3.py` (`where`, `slice`);
- for the reason `point`, `R-extent.md` and `review_select.py`;
- the code of `class_slice.py`, `class_kinds.py` and `class_merge.py` where `land_points.py` relies on it.

I didn't read the parts' notes or the earlier inspections.

**Severity:**
- `must fix`: fix it before the brief runs;
- `optional`: worth doing, but it doesn't block the run.

Facts cite a file and line, or a command and its output. Readings are marked as readings. Each fix is a proposal, for the coordinator to decide.

## Summary

**8 must fix, 12 optional.**

The must-fix findings:
1. **M1.** The status routes each conflict before its evidence is weighed. Its `to the founder` rule sends questions of fact about a platform to the founder.
2. **M2.** `count` doesn't use the model's own placement rule, and it overlaps `placement`. With several capabilities, the brief doesn't say which cell a platform is compared with.
3. **M3.** S-02 has 30 "who sets" questions. Because `placement` names "the merchant", a seller setting a platform's own setting reads as a conflict.
4. **M4.** The `page` route floods the leads from files that hold many concerns. It can push the capability the question names out of `show`'s view.
5. **M5.** No command the brief names prints a cell's full reading or the statements behind its placements. Step 5 and `basis` need both.
6. **M6.** `show` alone is about 64k to 109k tokens a batch. With the rest of the reading, S-02's batches approach or pass 200k.
7. **M7.** Nothing records what happened to each conflict, so neither the final review nor the architecture can read the outcome.
8. **M8.** `check` passes rows the brief forbids: an empty route, `none` beside a capability, a second conflict type it never checks, and any text as a basis.

## Must fix

### M1. The status routes each conflict before its evidence is weighed, and sends questions of fact to the founder

**The rule.**
- The brief tells the drafter not to weigh the sides: "Don't decide which side is right: the coordinator reads both" (P-points.md:27).
- It then has the drafter route each conflict by the point's register rows (:28–31):
  - `to the founder`, "where a conflict touches a founder's own decision: a register row whose status says the founder settled or decided it ... or a decision in `founder-decisions.tsv`";
  - `reopened`, "for every other conflict".
- "Touches" isn't defined. A reading: in some sense, any conflict on S-01 touches Decision 1 (`founder-decisions.tsv`:16) or the guard (:8).

**How far it reaches.** In S-01, 11 of the 23 points are named only by the founder's rows, so the rule makes every conflict found on them `to the founder`, whatever its substance:
- VP-01 (D1, D1.1, E1, E2) and VP-11 (D1.3, D7);
- VP-02 (D2), VP-03 (D3), VP-04 (D4), VP-06 (D5), VP-09 (D6);
- VP-10 (D12), VP-15 (D8), VP-20 (D10) and VP-21 (D11).

I computed this with the script's own register map, over `register.tsv`'s statuses.

**A worked case: S01-VP-01, "who or what fills 'holds the funds'".**
- `show`'s second lead is CM-PAY-004, "Processing, acquiring and holding funds behind the platform's payment service". Its Salla cell is `not-stated` (`class_slice.py model --domain C --areas PAY`; `parts/C-anchor/derived.tsv`:54).
- S-01's S01-V-016 (`variants.tsv`:16, 13 statements) reads "يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها": the e-payments balance holds the store's sales dues before they are transferred.
- S-01's analysis reads: "Salla and Zid both name the platform itself as the holder" (`analysis.tsv`:2).
- Landed on CM-PAY-004, the brief makes this a `count` conflict. Because every row naming VP-01 is the founder's, it also makes it `to the founder`.
- What the conflict is about is whether Salla's cell in CM-PAY-004 should be `core`. That is what Salla does, and it is the class's model. PLAN.md:57–58 and :64 put both among what is "Not the founder's to settle".
- A reading: whichever way the cell is settled, Decision 1 stands, unless the evidence it rested on is overturned.

**What the plan says.**
- PLAN.md:219: a founder's decision "isn't reopened by engineering: the conflict comes to the founder with its evidence".
- PLAN.md:53: "Nothing reaches the founder without a decision attached". Each item comes with its evidence, its options and a recommendation.
- A reading: the plan sends the founder the conflict that would reopen a founder's decision. Correcting a cell reopens none, so the brief's rule is wider than the plan's sentence.

**One status can't carry two routes.**
- S01-VP-19 is named by S01-D1.2 and S01-D9, which are the founder's (`register.tsv`:11, :20), and by S01-E3, which is "proposed, engineering" (:37).
- S02-VP-27 is named by four kinds of row:
  - S02-D5, engineering's;
  - S02-M4, moved;
  - S02-M9, moved to the founder's plans and prices (:30);
  - S02-F6, follows by rule (:36).

**`check` doesn't test the status against the register.** Both of these fixtures pass with exit 0:
- S01-VP-05, named only by its follows-by-rule row, given `to the founder`;
- S01-VP-01, named only by the founder's rows, given `reopened`.

**Fix.**
- **The drafter records; it doesn't route.** For each conflict, it names the rows the conflict bears on:
  - `rows: <ids, with S-02's keys>` for the register rows whose answer rests on the side the conflict questions;
  - `rows: model` where only the cells are in question.

  It also says, as a reading, which side the statements bear out, or what would settle it. The drafter's status is `landed` or `conflict`.
- **"After the batches" states the order.** The coordinator settles the fact first: that is engineering's (PLAN.md, section 3). Then:
  - where a cell is wrong, an amend part corrects it;
  - where the subject's evidence is wrong under an engineering row, the row is ruled again and listed for veto;
  - where the subject's evidence is wrong under a founder's row, it goes to the founder, with options and a recommendation.

  Each conflict is routed on its own.
- **`check`:** each `rows:` id must be one that the point's register names. `review_select.py`:179 must keep selecting every drafted conflict under the new words.

### M2. `count` isn't the model's placement rule, and it overlaps `placement`

**The two types overlap.**
- `count`: the subject shows the platform doing the thing itself "where the landing capability's cell on that platform is not `core` or `own-service`: ... or only `extension-point`, `outside` or `shows`" (P-points.md:22).
- `placement`: "One says the platform itself, the other a third party or the merchant" (:23).
- A subject that shows the platform itself, against an `outside` or `extension-point` cell, is both. The brief doesn't say which type applies.

**`count`'s test isn't the model's.**
- The brief counts the platform's "own admin, setting, API or terms" and "its company's own service".
- The model places `core` and `own-service` by its conventions. The final review states them for the same question (R-extent.md:21, :24):
  - `core`: "its own API for its own feature (C1), a released flag (C6), a staff permission (S7)";
  - `own-service`: "a statement name[s] the company as the maker or provider (... C5 ...). A brand in a product's name doesn't".
- A platform's terms aren't among them.

**The `open` capabilities show the effect.**
- CM-ACC-002, "The merchant agreement's contracting party and governing law", is `open: unplaced`, with all five cells `not-stated` (`merged/kinds.tsv`:3; `class_kinds.py`:10–13, convention 12).
- Its Shopify cell holds the Terms of Service's statements, each one `shows` (`merged/evidence.tsv`:19–20, SH-C-002/decides/SH-S-0001 and the rows after it; `merged/cells.tsv`:9).
- S02-VP-08, "what decides 'Shopify Contracting Party'", reads Shopify's terms (S02-SH-C001: https://www.shopify.com/legal/terms, "13. Shopify Contracting Party and Forum").
- A reading: landed there, the brief's test makes a `count` conflict on every platform whose terms S-02 holds, against a placement the model makes on purpose.
- Five points have an `open` capability like this in their top three leads: S01-VP-21, S02-VP-02, S02-VP-03, S02-VP-08 and S02-VP-09.

**Several capabilities: the brief doesn't say which cell to compare.**
- P-points.md:17 lands a point on several capabilities "where the platforms answer it in different capabilities".
- But :21–22 compare with "the landing capability's cell", which is one cell.
- S01-VP-01's Salla answer is in CM-PAY-005, where Salla is `core` (`parts/C-anchor/derived.tsv`:56; its evidence cites SA-C-111/boundary/SA-S-0076 as `core`, `parts/C-anchor/evidence.tsv`:464). CM-PAY-004's Salla cell is `not-stated`. Depending on which cell is read, this is a `count` conflict or no conflict.
- `check`'s `lead:` lines test the first capability only (land_points.py:447–452).

**Fix.**
- Define both types by the model's conventions, by reference: C1, C5 with its maker evidence, C6, S7, and convention 12. Don't restate them more loosely. Say that a platform's own terms stating a thing don't place it `core`.
- Make the two types exclusive:
  - `count`: the subject's statements meet those conventions for `core` or `own-service`, and the cell is placed otherwise or holds nothing;
  - `placement`: the cell is `core` or `own-service`, and the subject shows a third party, the merchant acting outside the platform, or a confirmed absence.
- Compare each platform with the cell of the capability it answers in. `check` should print a platform's `lead:` only where none of the point's capabilities holds its statements.

### M3. S-02's "who sets" questions read as placement conflicts

**The evidence.**
- 30 of S-02's 75 questions ask who sets, changes, creates or checks a value (26 of them "who sets"; `variation-points.tsv`, VP-04 to VP-06, VP-28, VP-29 and VP-42 to VP-92). That question is about who configures a setting. A cell's placement is about who provides the capability.
- `placement` sets "the merchant" against "the platform itself" (P-points.md:23), and the brief's paragraph on grain covers only markets (:21).
- **A worked case: S02-VP-42, "who sets 'currency'".**
  - S-02's answers: 'the seller' and 'the platform' on all five; 'the buyer' on BigCommerce and WooCommerce; 'the enabled payment gateway' and 'partners' on Zid; 'Stripe' on BigCommerce (`answers.tsv`:163–168).
  - Its top lead, CM-MKS-006, is `core` on Salla, Zid and BigCommerce.
  - A reading: by the brief's words, 'the seller' against `core` is a placement conflict, and the same holds on most of these points.
  - A reading: by the same words, S02-V-814, "Stripe detects the shopper's currency, handles the FX conversion" (`variants.tsv`:618), conflicts with CM-MKS-006's BigCommerce `core`. Yet CM-MKS-007, currency conversion, already holds BigCommerce as `core;outside`.
- S-02's own register leaves to the build, as cheap to change, "who besides the seller sets each setting (the platform, a staff role, an app, a developer or the buyer)" (S02-F10, `register.tsv`:40).

**Fix.**
- Say that the seller, a staff member or the buyer setting the platform's own setting is the platform's `core`, and never a conflict.
- For a "who sets" point, compare a third party (Stripe, a gateway, partners, an app) only with the capability whose thing it does: for VP-42's Stripe, CM-MKS-007. There it differs only as M2's `placement` defines a difference.

### M4. The `page` route floods the leads from files that hold many concerns

**How the route works.**
- Take a statement read on a page, at a locator the concern map doesn't cite. It gives a lead to every concern the concern map cites anywhere on that page (land_points.py:126–132, 199–200).
- Each of those concerns counts 1 per statement (:224–226; the weights are at :286–287 and :352–353).
- `show` adds at most two term leads after the top five (:356).

**Pages that are whole corpora.** Counting a statement once for each variant that cites it:
- S-02's Salla statements hit observed-sa's `dashboard-translations/en/settings.json`, which holds 33 concerns, 56 times. At observed-sa@4ca2e89, that is one file of 2,034 keys for the whole settings centre.
- They hit `docs-operations/md-openapi/items.jsonl`, the docs' whole OpenAPI set, 52 times.
- Shopify's shopify.com/legal/terms holds 64 concerns (20 hits).
- Zid's JS bundle `zid.sa/_next/static/chunks/2501-f29c20b24ab64821.js` holds 35 concerns (10 hits).

**How often it decides the ranking.** By the script's own scoring:
- for 13 of the 98 points, the top lead rests on the page route alone;
- 155 of the top-five slots are page-only.

**A worked case: S02-VP-61, "what 'local payment methods' takes its value per".**
- `leads` ranks first CM-LOY-001 (store credit and customer wallet), then CM-TAX-001, CM-MKS-001, CM-PAY-020, CM-PAY-031 and CM-APP-010. Each rests on `page SA5` to `SA7` alone.
- Checked by hand:
  - S02-SA-096 and S02-SA-097 (`salla/statements.tsv`:97–98) are settings.json's keys `payments/payment-restrictions#type.country-ip-address` and `#type.scopes` ("Markets").
  - What makes CM-LOY-001 a lead is SA-C-063's statements on the same file's keys `coupons/cashback-eligibility`, `wallet/max-credit-usage` and `wallet/gift-card`.
- Neither of the two capabilities that hold the point's own terms is among `show`'s seven leads (`class_slice.py caps --terms "payment restrictions;payment-restrictions;قيود الدفع;local payment methods"`):
  - CM-PAY-017, "Local payment methods", which is the question's own words;
  - CM-PAY-019, "Payment method rules", which holds "payment restrictions" and "قيود الدفع", S-02's Salla and Zid terms.
- A reading: CM-MKS-001 (Markets) also heads the page-only leads of S02-VP-18, S02-VP-69 and S02-VP-70. With the noise favouring it, a drafter may land "what X takes its value per" on Markets rather than on X.

**Fix.**
- Weight a page hit by 1 over the number of concerns the page holds. Or drop the route where a page holds more than about three concerns, and for collection files (`.json`, `.jsonl`, a JS bundle).
- For each page lead, print the page and its number of concerns.
- Rank term leads with the others by score, rather than capping them at two.
- Say in the brief that a `page` can be a whole corpus.

### M5. No named command prints a cell's full reading or the statements behind its placements

**The evidence.**
- P-points.md:42 sends the drafter to `class_slice.py model --domain <D> --areas <AREA>` "where a cell's clipped reading doesn't settle it". But `model` prints `held`, the terms clipped at 120 characters and the placements: no reading (class_slice.py:382–409; `model --domain C --areas PAY`).
- `q3.py slice` prints no reading either. `q3.py where` goes from a statement to its cells, not from a cell to its statements.
- `show` clips each reading at 220 characters (land_points.py:366). 910 of the 949 cells with statements have a longer reading (median 606 characters; 90th percentile 1,029).
- Step 5 asks the drafter to "Name the subject's statement ids and the cell" and "both sides' statements" (P-points.md:22–23). The cell's side is its evidence rows, which no named command lists.
- `basis` is "the concern map's keys a cell cites" (:18). `point_leads` collects a basis for each lead (land_points.py:209, 223, 226), but neither `show` nor `leads` prints it. For `cited`, it keeps the citation id, not the key (:223).
- A reading: a drafter will either load `cells.tsv` or `evidence.tsv` whole, or write conflicts without the model's side.

**Fix.**
- Add a `cell CAP PLATFORM` command that prints the cell's whole reading, its placements and, for each placement, its evidence keys with their `why`.
- Have `show` print each lead's basis as full keys.

### M6. `show` alone is a third to a half of a drafter's context

**`show --points <the batch>` at the brief's defaults:**

| batch | points | characters (of them Arabic) | tokens, estimated |
| --- | --- | --- | --- |
| P-1 | 23 | 205,298 (12,883) | 64k–75k |
| P-2 | 23 | 303,326 (7,959) | 90k–105k |
| P-3 | 26 | 315,715 (7,622) | 93k–109k |
| P-4 | 26 | 284,500 (5,532) | 83k–98k |

**How I estimated it.** The token figures are an assumption, because no tokenizer is available here:
- 3.0 to 3.5 Latin characters a token for this id-dense text, and 1.2 to 1.5 for Arabic;
- a second proxy, one token per punctuation mark and per five letters, gives 64k, 94k, 97k and 86k;
- the largest single point is S02-VP-27, at about 5.6k.

**The rest of a drafter's reading:**
- `founder-decisions.tsv`, whole: 21,561 characters, about 6–7k;
- the brief and `--help`: about 3–4k;
- each model slice: 2–8k (C's PAY area is 21,203 characters, about 7–8k);
- each `key` and each subject row;
- its own rows and notes;
- the session's own prompt.

An assumption on these puts P-3 at roughly 160k to 215k by its end.

**Fix.**
- Halve P-2, P-3 and P-4 into batches of 11 to 13 points, keeping each "what X takes its value per" with its "who sets X". Or run `show` at `--width 140 --top 4` (P-3: 220,120 characters, about 65k–76k).
- Say that each point's `show` is read once.

### M7. Nothing records what happened to each conflict

**The evidence.**
- "After the batches" (P-points.md:56–58) names what follows: rulings ruled again, amend parts, the founder at GM. It records none of it, and the file's fields (land_points.py:50) have no place for it.
- `review_select.py`:175–182 selects points by `status != landed`, once, after the last merge. Its `coordinator` reason reads only the parts' files and `scope.tsv` (:140–161). If the coordinator dismisses a conflict and rewrites the row as `landed`, it is reviewed only if the seeded tenth happens to draw it.
- The review asks: "Is each conflict real, of the type given, with the status its rules give?" (R-extent.md:35). But it runs after the amend parts, so a conflict resolved by amending a cell no longer shows in the cells it reads.
- The architecture reads what varies from the subjects' registers (`architecture/plan.md`:36), and an area waits for the subjects that cover its open questions (:90, :97). It needs each point's state after its conflict is settled, and no file holds that.

**Fix.**
- Add an `outcome` field. It is empty in the drafts. The coordinator writes it, marked "(the coordinator)", as one of:
  - `model amended: <part>/<file> <row>`;
  - `re-ruled: <row>, listed for veto`;
  - `carried to <subject>`;
  - `to the founder: <item>`;
  - `dismissed: <why>`.
- The drafted conflict and status stay as written.
- `check` takes a flag that, once the coordinator's pass is done, requires an outcome for every conflict.
- `review_select.py` selects every drafted conflict, whatever its outcome, and every row the coordinator marked.

### M8. `check` passes rows the brief forbids

**The evidence.** I wrote fixtures in the scratchpad and pointed the unchanged script at them through `CLASS_MODEL_DIR`. Each of these passes with exit 0:
- an empty `route`. P-points.md:18 requires the routes, but land_points.py:424–426 check only the routes that are present;
- `CM-PAY-004;none`, `none;none`, and a capability listed twice (:418–423, :445);
- `count:` with nothing after the colon;
- `count: a; bogus: b` and `count: a|bogus: b`, whose second type is never checked: :437–440 split only on ` | `;
- `nonsense` as the `basis`. :427–428 check only that it isn't empty.

The opposite error also occurs: a `none` point whose conflict is `premise: ... | structure: ...` is refused, because :445 needs `structure` to come first.

**Fix:**
- require a route wherever `cap_ids` isn't `none`;
- allow `none` only on its own;
- require each capability to appear once;
- require text after each type's colon;
- split conflicts on `|` with or without spaces, and look for `structure` in any part;
- require each basis item to be one of:
  - a key that a cell of one of the point's capabilities cites;
  - `concern:<id>`, for a concern landed in one of them;
  - `term:<t>`, with `t` among the point's `x_words`;
- require each route to be backed by a basis item of its form.

## Optional

### O1. `cited` resolves through a citation, not the statement, and hides the concern's landing

**The evidence.**
- land_points.py:72–74 key each cell's evidence by the last part of its key, which is the statement's first citation, and drop the concern.
- Where a cell cites that citation, :220–226 take `cited` and skip the concern's own landing (the `elif`).
- On Shopify, 599 of the 2,085 first citations are shared by more than one statement.
- Of 984 `cited` hits on the two subjects' statements:
  - 125 reach a capability only through another concern's statement on the same citation;
  - 103 hide the concern's own landing. For example, S01-SH-099 comes from `index:SH-C-110:SH-S-0566`. SH-C-110 lands in CM-MKS-003, but the lead shows CM-PAY-004 only.
- So the brief's description of the route, "a cell cites the concern map's statement the subject's statement comes from" (P-points.md:10), holds for most hits, not all.

**Fix.** Key the evidence by concern and citation where the trace knows the concern, and count the concern route beside `cited`.

### O2. Most of the subjects' Shopify and Salla help statements don't trace, and `show` hides it

**Shopify.**
- S-02's variants use 901 Shopify statements, and 74 of them trace.
- 483 of the 820 that don't trace cite observed-sh's copies of help pages, such as `structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets.md`. The concern map cites the same pages as https://help.shopify.com/en/manual/....
- If `norm_source` (land_points.py:96–103) read those copies as their URLs, 124 would trace.

**Salla.**
- The subjects cite Salla's help as observed-sa's `help-articles/<lang>/texts.jsonl`. The concern map cites it as https://help.salla.sa/article/<slug>/<id>.
- The subjects' locator names the article. For example, S02-SA-C096 reads "line 1074 (article wv9wyqrnhwpm6m2rp3cmg653, ...)".
- 111 of S-01's 181 such citations, and 186 of S-02's 396, name an article the concern map cites.

**`show` hides it.** It prints only the total traced (land_points.py:357). S02-VP-69, for example, traces 25 of its 91 statements, and none of Shopify's 42.

**Fix.**
- Map both kinds of copy to the concern map's sources: the help path for Shopify, the article id for Salla.
- Print the statements traced for each platform.
- Tell the drafter to search (`caps`, `search`) for a platform with nothing traced.

### O3. `show` hides variants beyond eight per platform

**The evidence.**
- `--variants 8` caps each platform's list (land_points.py:344, :349).
- P-1 hides 116 of its 614 variants, across 24 point-and-platform pairs; S01-VP-04 has 15 on Shopify. P-2 hides 30, and P-3 and P-4 hide none.
- The brief compares "platform by platform, what the subject's variants ... say" (P-points.md:21). But it sends the drafter to `variants.tsv` only "where the view leaves a variant in doubt" (:12).

**Fix.** Run P-1 at `--variants 20`, since it is the smallest batch. Or require every variant to be read before a `none`.

### O4. The status rule doesn't name three kinds of register row

**The evidence.**
- S02-M9 is "moved to the founder's plans and prices" (`register.tsv`:30), and `founder-decisions.tsv`:30 says it "comes to me with plans". It is neither "a row moved to another subject" (`reopened`) nor a row "the founder settled or decided" (P-points.md:30–31).
- The "follows by rule" rows (S-01's nine, and S-02's F1 to F10) fall under "every other conflict" without being named.
- A moved row's question is open in the subject it moved to.

**Fix.** Name each kind:
- M9's conflict goes to the founder with plans, not at GM;
- a follows-by-rule row is re-applied by the coordinator;
- a moved row's conflict is carried to its subject as an input, and not ruled again now.

### O5. `premise` names only universal or negative claims

**The evidence.**
- P-points.md:25 limits it to "(what every platform does, or that no reference does a thing)".
- S02-M9's recommendation rests on "as the class shows" (`register.tsv`:30), a claim that some platform does a thing.
- S02-F7 rests on "Carried as all five carry it" (:37).

**Fix.** Make `premise` cover any claim about what the references do or show.

### O6. The brief gives no way to mark a point that cuts across every area

**The evidence.**
- S02-VP-41, "what 'currency' takes its value per", is named by S02-D9 (`register.tsv`:21). D9 is the architecture plan's worked example of keeping room. Its step is taken with the cross-cutting decisions, because every amount refers to a currency record (`architecture/plan.md`, section 4, and section 3, item 3).
- The plan also says "S-09's currency of records bind[s] every area that holds ... an amount" (:97).
- Yet S02-VP-41's leads are all MKS capabilities.
- "The main one first. Add others where the point's thing spans capabilities" (P-points.md:17) lets one drafter list one capability and another list thirty.
- The brief says the architecture reads the landing "to see which capabilities vary by market and why" (:7), but the output carries neither the cause nor the binding time. The architecture plan's variation points name their binding time (section 4).

**Fix.**
- Add a `reach` field: `capability`, or `cross-cutting: <architecture plan, section 3, item>`, with the main capability still named.
- Say that the cause and the binding time come from the subject's analysis, by `vp_id`.

### O7. The subjects' slot fillers aren't compared with the model's

**The evidence.**
- `architecture/plan.md`:37 takes what fills a slot from "The model's slot fillers; each subject's evidence".
- `merged/slot-fillers.tsv` holds 162 rows.
- S-01's variants name fillers: Global-e (S01-V-001), Stripe, Adyen, and Tabby and Tamara under S01-VP-22.
- The brief compares only cells.

**Fix.** For a point landed on a slot, or on a capability with `outside` cells, list in the notes the fillers the subject names that `slot-fillers.tsv` lacks. Each is a lead, not a conflict.

### O8. `check` crashes on three malformed files instead of reporting them

**The evidence:**
- a row of 6 fields: `AttributeError: 'NoneType' object has no attribute 'strip'` (land_points.py:429);
- a header with `cap_id` in place of `cap_ids`: `KeyError: 'cap_ids'` (:418);
- a UTF-8 byte-order mark: `KeyError: 'subject'` (:402).

**Fix:**
- report short rows and skip them;
- stop on a wrong header, with its problem line;
- open the file as `utf-8-sig`.

### O9. Batches and subjects are hard-coded

**The evidence.**
- `SUBJECTS` and `BATCHES` are hard-coded (land_points.py:46, :48), and the patterns use `S0\d` (:168, :188).
- The docstring says the full check covers "every point of each subject landed once across them" (:22). But :403–407 check only the points inside the batches' ranges. Today those ranges cover all 98 points.
- PLAN.md:219: "Each later subject's points land as it ends."

**Fix.** Compute the batches from the subjects' files, check that every point of every subject is in a batch, and match `S\d\d`.

### O10. For a domain not yet merged, the parts are read in name order

**The evidence.**
- land_points.py:77–88 read a domain's parts in `sorted()` name order. So an `amend` part comes before `anchor`, and backfills come before mappings.
- `class_merge.py` orders parts by `PART_ORDER`, with amend last (class_slice.py:58).
- For a merged domain, the script reads `merged/` alone. D-amend's landing of WC-C-047 in CM-CUS-009 (7cf14483) is newer than the merge (765de7c2), so the script doesn't see it until the next merge.

This is harmless once C is merged and the merge is redone.

**Fix.** Use `PART_ORDER`, and warn when a merged domain has a part newer than `merged/`.

### O11. The term route drops S-02's head term

**The evidence.**
- land_points.py:234–236 skip any part of `x_words` without "platform:".
- In 64 of S-02's 75 points, the first part has no platform. For S02-VP-61, that part is "payment methods offered to buyers".
- A term with an annotation keeps a stray quote: `Currency" (table column)`, in S01-VP-23.

**Fix.** Take the head term too, and strip the annotations.

### O12. A point landed on `none` goes to the review's share 4

**The evidence.** In `review_select.py`:51–55, `share_of("none")` matches no area and defaults to `"4"`, the share for E to G. So an S-01 payments point with no capability would go to that share's reviewer.

**Fix.** Assign such a point by the domain of its leads.

## What I tested, and how

My scratch tools are in `/tmp/claude-0/-home-user-sharrwah-knowledge-map/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/tools/`. Each imports `land_points.py` unchanged and uses its own functions and scoring. I wrote nothing in the repository except this file, and made no commits.

**Commands I ran:**
- `land_points.py`: `--help` and `batches`;
- `show` on every batch's points, at the defaults and at `--width 140 --top 4` for P-3;
- `leads` on S01-VP-01 and on S02-VP-01, VP-02, VP-03, VP-08, VP-09, VP-41, VP-43, VP-61 and VP-85;
- `class_slice.py model` for C PAY, E MKS and A ACC, and `caps`;
- `q3.py where` and `q3.py slice --area ACC`.

**Leads I checked by hand:**
- S01-SA-004 leads to CM-PAY-005. The lead holds: that cell cites the same statement, SA-C-111/boundary/SA-S-0076, as `core`, and it is the point's thing.
- S01-SA-026 leads to CM-PLN-006. That cell cites SA-C-005/boundary/SA-S-0091 as `shows`: the citation is real, but the thing is a different one.
- S02-VP-61's page leads, against the statements on both sides and against settings.json at observed-sa@4ca2e89 (M4).

**What I measured, through the script's functions:**
- each statement's trace, and the untraced statements by cause (O2);
- the pages each statement hits, by their number of concerns (M4);
- the top five leads of every point (M4, M2);
- `cited` against `concern` (O1);
- the copied statements;
- the sizes of `show` and of the other inputs (M6);
- the variants `show` hides (O3).

**What holds:**
- **Copied statements are traced soundly.** S-02 has 122 of them. 106 trace the same through S-01 as through their own citations. The other 16 add neighbouring citations of the same concern. The redirection loses none.
- **Register lists:** `show` and `check` compute them the same way (land_points.py:166–170, :320, :431).
- **Batches:** all 98 points fall in exactly one batch, and S-02's pairs stay together.
- **The brief's account of the statuses matches the evidence:**
  - S-01's founder's, standing, kept and proposed rows, in `register.tsv`;
  - S-02's D1 to D9 and E1 to E5, "engineering's ruling ... no veto";
  - `founder-decisions.tsv`:16–17, :19–20 and :30.
- **The founder's words of 30 October** (`founder-messages/2026-10-30-before-gm.md`:11) are carried faithfully.

**`check`: the baseline.** In a fixture directory, I linked `merged/` and `parts/` read-only and set `CLASS_MODEL_DIR` to it. The baseline lands all 98 points on their top lead, with questions and registers as the script computes them. It prints "# 98 points in P-1, P-2, P-3, P-4, 0 problems", with 93 `lead:` lines. 48 of those come from C's missing Zid and BigCommerce cells.

**`check`: 42 changes to P-1.** Each ran in its own fixture directory, with `check --batch P-1`:
- **24 caught**, as they should be:
  - a missing point, and a duplicate;
  - a register out of order, one row short, or joined by `, `;
  - `none` with `landed`, and `none` with a `count` conflict;
  - an unknown capability, and `None` written as a capability;
  - a bad type, a type without its colon, and `None` written as the conflict;
  - a conflict with `landed`; `none` with `reopened` or `to the founder`; a status outside the three;
  - a bad route, an empty basis, an empty reading;
  - a question changed by one space;
  - a wrong subject, and another batch's point;
  - rows of 11 and of 9 fields.
- **4 accepted, rightly:** `none` with a `structure` conflict and `reopened`; CRLF line ends; a blank last line; a field starting with a quote.
- **1 refused, wrongly:** `premise` before `structure` on a `none` point.
- **10 passed, wrongly:**
  - `none` beside a capability, `none;none`, and a capability listed twice;
  - `count:` with nothing after the colon;
  - two conflicts joined by `;`, or by `|` without spaces;
  - `to the founder` on S01-VP-05, and `reopened` on S01-VP-01;
  - an empty route;
  - a nonsense basis.
- **3 crashed:** a 6-field row, a wrong header, and a byte-order mark.

**What I couldn't test:**
- **Domain C merged.** C-zid, C-bigcommerce and C's backfills haven't run, so C's leads, cells and `lead:` lines will change. The worked cases of M1 and M2 rest on C's cells and should be read again after the merge. The page and `cited` noise rates should be measured again then.
- **Token counts.** They are estimates; no tokenizer is available here.
- **A drafter's run on a batch, the coordinator's pass, and the amend parts.** None exists yet.
- **`review_select.py` on real points files.** None exists yet, so I read its code instead.
