# Brief: S-02, variation points and variants (step 1, phase B)

This is `PLAN.md` Stage 4, subject S-02. You are one agent with one task: one part of one root decision. The message that started you names both: the root decision, the bullets you place, and the platforms whose statements you place. Other agents work on the other parts, one after another for the same root decision, each continuing from the files the last one wrote.

**Read only this brief and, in `studies/subjects/S-02/`:**
- `bullets.tsv`, the questions phase A asked of each platform, and `b/ranges.tsv`, your root decision's ids and cap;
- your root decision's slice, `slices/<root decision>/`, cut from the five platforms' phase A files by `method/subject_slice.py`, printed in parts (below):
  - `statements.tsv`: every statement under one of your root decision's bullets, with its `platform`, its `kind` (by rule) and its `source` (its first citation's);
  - `gaps.tsv` and `absences.tsv`: those under your root decision's bullets, with their platform, and an absence's kind;
  - `terms.tsv`: every platform's terms;
- your root decision's own folder, `b/<root decision>/`, where earlier parts wrote;
- in the second pass, each platform's `a2.tsv` and `absence-audit.tsv`, and the slices as the coordinator cuts them again.

Don't read the platforms' own folders (but for the second pass's two files), `notes.md` files, `recorded.tsv` files, or any `note` column. The slices hold no notes.

**Reading the slice in parts.** Never read a slice whole. Print what you need:

```
python3 -I method/subject_slice.py studies/subjects/S-02 --print <RD> --bullet <b> --platform <p>
python3 -I method/subject_slice.py studies/subjects/S-02 --print <RD> --ids <id>,<id>
python3 -I method/subject_slice.py studies/subjects/S-02 --print <RD> --what gaps|absences|terms --platform <p>
```

## The subject

> What fills "a market": which settings bind per market, and who sets each?

**Its three root decisions** (`PLAN.md`, section 6, step 1):
- **RD1, the store's own country:** what fills a store's country; who sets, checks and changes it; what binds to it; and the countries a platform serves.
- **RD2, the markets a store sells into:** what defines one, how many a store can hold, and who creates them.
- **RD3, what binds per market, and who sets it:** which settings take a value per market, which hold for the whole store, and which the platform sets and which the seller.

Phase A collected what each platform states under eight bullets. Each belongs to a root decision, as `bullets.tsv` says:
- **(a)** to **(d)**, RD1: what fills the store's own country; who sets, checks or changes it; what the platform binds to it; the countries the platform serves;
- **(e)**, RD2: what defines a market a store sells into, how many it can hold, and who creates one;
- **(f)**, RD3: a setting that takes its value per market, whether the store's own country (as in (a)) or a market it sells into (as in (e)), or per buyer's country; and who sets that value;
- **(g)**, RD2 and RD3: that a setting holds for the whole store (RD3's), or that the platform has no market of the kind in (e) (RD2's);
- **(h):** where, or for whom, what a statement under (a) to (f) describes is offered.

Statements under (h) are conditions, not variants: a variant rests on at least one statement under (a) to (g). A later step reads the conditions.

**Your task:** split your root decision into the facets that can change it, as variation points, and place your part's statements under them as variants. Don't judge the variants, and don't give causes; a later phase does that.

## Rules

0. **Same.** In these rules, two things are the same when they use the same words, or a platform's own translation of them in `terms.tsv`, or name the same party or identifier. Quote what shows it. Two platforms agree on a variation point when their sets of answers are the same.
   - **Without the platform's translation,** `answers` may rest on your translation of the platform's words. Quote them, and mark the translation as yours in `basis_evidence`.
1. **The questions.** A bullet asks more than one thing, and each thing is its own kind of variation point, with its own form of question. X is always quoted from a statement.

   | Bullet | Questions, each its own variation point | What a variant names |
   | --- | --- | --- |
   | (a) | `what fills "X"`, X the store's own country, location or address | the field or record that holds it: the store's address, its billing address, a business entity, the account |
   | (b) | `who sets "X"`; `who checks "X"`; `who changes "X"`; `what must hold before "X" changes`, X the store's country as in (a) | the party, or the condition |
   | (c) | `what decides "X"`, X a thing the platform binds, such as a contracting party, documents or a payment service | what decides it: the store's country, its location, its billing address, the business's registered country, a business entity |
   | (d) | `what countries fill "X"`, X the platform's words for where it serves merchants; `what holds "X"`, how it holds them | the countries, or what holds the list: a sign-up field, a terms clause, a feature's countries |
   | (e) | `what defines "X"`, X a market a store sells into; `what limits "X"`, how many a store can hold; `who creates "X"`, and who changes or removes it | a country, region, city, group of customers, location, channel or storefront; the limit; the party |
   | (f) | `what "X" takes its value per`; `who sets "X"`, X a setting | the store's own country, a market the store sells into, the buyer's country, or the whole store (from (g)); the platform or the seller |

2. **Candidates.** Each statement under one of your part's bullets that answers one of that bullet's questions gives one candidate per question it answers, with its X quoted from it.
   - **The role test** applies to X itself: X must be the thing the question names, in the root decision's sense. A country a buyer ships to is not the store's own country; a setting of the platform's own account is not a store's setting. "Market", "country" and "region" name different things on different platforms.
   - **A candidate whose X passes the role test is a facet** of its root decision (`PLAN.md`, Stage 4). One that matches no other raises its own variation point.
   - A statement under your bullets that answers none of their questions, or whose X fails the role test, goes in `notes-b.md` by its id, with the reason in a few words.
3. **Variation points.** Candidates from different statements under the same question are one variation point when their X matches on one of the bases in rule 5.
   - Each variation point keeps its bullet. Its question takes that question's form from rule 1, with X in double quotes, quoted from one of the statements in `raised_by`.
   - `x_words` lists each raising platform's own words for X.
   - **Merging.** Two variation points of the same question, answered by exactly the same statements, are merged. List each merge in `notes-b.md`.
   - **Earlier parts.** Read your root decision's `variation-points.tsv` before you start, and place your statements under its points first. Raise a new one only where none matches. For a point you raise, give a row for every platform, the earlier parts' platforms too: print their statements under that bullet and place what answers it.
4. **Variants.** For each variation point and each platform, give one row per distinct answer the platform gives, with its own `variant_id`. An answer's `variant` excerpt names the who or what that fills X. Two answers are distinct when their excerpts name a different who or what. A row takes one of four forms:
   - **an answer:** `variant` is an excerpt of one of its statements, verbatim;
   - **`absent`:** the platform's absences show it absent from a complete list, under the variation point's bullet, with those `absence_ids`. Its `kind` is the absence's kind;
   - **`gap`:** the platform's gaps under the same bullet cover it, with those `gap_ids`;
   - **`not covered`:** the platform has none of these. These rows go back to that platform for gap-closing (phase A2). List them in `notes-b.md`.

   **(g).** A statement that a setting holds for the whole store is the platform's variant, "the whole store", under each of RD3's `what "X" takes its value per` points it applies to. A statement that the platform has no market of the kind in (e) is its variant under each of RD2's points it applies to. Either takes the basis `answers` alone.
5. **Matching.** Compare each statement with a statement in the variation point's `raised_by` from another platform, where there is one. Record every basis that holds, with the words that show it in `basis_evidence`:
   - `term`: the same term, including a platform's own translation from `terms.tsv`. It fails when the two platforms' definitions in `terms.tsv` differ.
   - `identifiers`: the same key, scope, topic, field or entitlement, as the statement itself states it, not as its `identifier` column's heading gives it;
   - `definition`: the same definition, with both quoted;
   - `answers`: the statement says who or what fills the variation point's X, in words that name the same X.
     - `answers` rests on what the statement says, not on shared words. Its own words must name what fills X in X's role, as rule 2's role test says. `basis_evidence` quotes those words and says which role they name. The role test holds whatever a variant's basis, since shared words can be homonyms.
     - A variant whose words name only what is kept out of X's role is not an answer variant. It goes in the variation point's `note`, with its statement's id. If no other variant of the platform answers, the platform's answer is a `gap` with its gaps under that bullet, or, if it has none, `not covered` (the pilot's ruling of 25 October 2026, on its review's finding 36).

   A statement goes under a variation point only if at least one basis holds. When it only partly matches, split the variation point rather than force the match.

   **Lists.** Statements that share a `source` and an `identifier` may be runs of one list, split because the source holds the items apart. Read them together.
6. **Kind and scope.**
   - `kind` is copied from the slice's `kind` for each statement of the variant. If they differ, list each, `;`-separated.
   - `scope` is as the statements give it. If they differ, list each scope with its `stmt_ids`, `;`-separated.
7. **Every statement is placed or noted.** Each statement of your part, under each of your part's bullets it carries, is in a variant of one of your root decision's variation points, or in `notes-b.md` by its id with its reason (rule 2). The checker lists the rest.
8. **No inference,** no ranking and no causes, anywhere, including notes.
9. **Write as you go.** Write each variation point and variant to the files as soon as it is placed. If you are stopped, your files must hold everything done so far, and the next run continues from them.
10. **Stop and report** past your root decision's cap of variation points in `b/ranges.tsv`, listing in `notes-b.md` the statements not yet placed.

## Second pass, after phases A2 and A3

When the coordinator says phases A2 and A3 are done, the slices are cut again, so that they hold the statements A2 added. Read each platform's `a2.tsv` and `absence-audit.tsv`, and print the statements they name from the slice by id. Revisit every row that was `gap`, `absent` or `not covered`, and each arrangement A2 was given. Recheck, under rule 5, any row you compared with a statement of its own platform. The second pass adds no variation point and splits none. A statement that fits no existing variation point is listed in `notes-b.md`. For each row revisited:
- replace it with variants from the statements A2 added, under the rules above;
- or make it `absent`, with A2's `absence_ids`;
- or keep it as `gap`, with A2's `gap_ids`.

Record what changed in `notes-b.md`.

## Output, in `studies/subjects/S-02/b/<root decision>/`

All files are tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field. Use only your root decision's ids in `b/ranges.tsv`, continuing from the last one in your folder.

| File | Columns |
| --- | --- |
| `variation-points.tsv` | `vp_id` (S02-VP-NN) · `bullet` (one of your root decision's bullets from `a` to `f`) · `question` · `x_words` · `raised_by` (stmt_ids) · `note` |
| `variants.tsv` | `variant_id` (S02-V-NNN) · `vp_id` · `platform` (`shopify`, `salla`, `woocommerce`, `zid` or `bigcommerce`) · `variant` (an excerpt, `absent`, `gap` or `not covered`) · `stmt_ids` · `basis` (every basis that holds, `;`-separated) · `basis_evidence` · `kind` · `scope` · `gap_ids` · `absence_ids` · `note` |
| `notes-b.md` | Statements noted by id, with their reasons; merges; partial overlaps that were split; `not covered` rows; problems with the method. |

**Before you finish,** check your files on a copy that holds only your own root decision's folder:
1. Copy `studies/subjects/S-02` to `<your scratch folder>/S-02`, then remove from the copy every folder in `b/` but your own.
2. Run `python3 -I method/merge_slices.py <that folder>/S-02 b`. It refuses ids outside your range, a bullet outside your root decision, or more variation points than your cap.
3. Run `python3 -I method/check_subject.py <that folder>/S-02 <an output folder> $(ls -d evidence/product-class/runs/*)` from the repository's root.
4. Fix, in your own folder, every line of level `error` on your ids. Its `review` line for your root decision, and `unplaced.tsv` in the output folder, list your root decision's statements neither in a variant nor noted: those of your part's bullets and platforms are yours to place or note; the rest belong to other parts.
