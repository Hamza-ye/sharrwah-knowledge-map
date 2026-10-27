# Brief: S-02, variation points and variants (step 1, phase B)

This is `PLAN.md` Stage 4, subject S-02. You are one agent with one task: one part of one root decision. The message that started you names both: the root decision, the bullets you place, and the platforms whose statements you place, in their order, with the parts before and after yours. A part is some of a root decision's bullets, for all of the platforms or some of them. Other agents work on the other parts, one after another for the same root decision, each continuing from the files the last one wrote.

**Read only this brief and, in `studies/subjects/S-02/`:**
- `bullets.tsv`, the questions phase A asked of each platform, and `b/ranges.tsv`, your root decision's ids and cap;
- your root decision's slice, `slices/<root decision>/`, cut from the five platforms' phase A files by `method/subject_slice.py`, printed in parts (below):
  - `statements.tsv`: every statement under one of your root decision's bullets, with its `platform`, its `kind` (by rule) and its `source` (its first citation's);
  - `gaps.tsv` and `absences.tsv`: those under your root decision's bullets, with their platform, and an absence's kind;
  - `terms.tsv`: every platform's terms;
- your root decision's own folder, `b/<root decision>/`, where earlier parts wrote;
- in the second pass: your root decision's work list, `b/second-pass/<root decision>/worklist.tsv`; each platform's `a2.tsv` and `absence-audit.tsv`; the slices as the coordinator cuts them again; and the usage of `method/variants_edit.py`, at the top of the file.

Don't read the platforms' own folders (but for the second pass's two files), their `notes.md` or `recorded.tsv` files, or any `note` column of phase A's files. The slices hold no notes.

**Reading the slice in parts.** Never read a slice whole. Print what you need:

```
python3 -I method/subject_slice.py studies/subjects/S-02 --print <RD> --bullet <b> --platform <p>
python3 -I method/subject_slice.py studies/subjects/S-02 --print <RD> --ids <id>,<id>
python3 -I method/subject_slice.py studies/subjects/S-02 --print <RD> --what gaps|absences|terms --platform <p>
```

A statement's columns are `platform`, `kind`, `source`, `stmt_id`, `bullet`, `placement`, `identifier`, `statement`, `scope` and `marker`. To scan many, print only those you need, such as `| cut -f1,4,5,7,8`. To find statements by their words, use `grep` on the printed rows. Read your root decision's `variants.tsv` the same way, by variation point or platform (`awk -F'\t' '$2=="S02-VP-03"'`), never whole.

## The subject

> What fills "a market": which settings bind per market, and who sets each?

**Its three root decisions** (`PLAN.md`, section 6, step 1):
- **RD1, the store's own country:** what fills a store's country; who sets, checks and changes it; what binds to it; and the countries a platform serves.
- **RD2, the markets a store sells into:** what defines one, how many a store can hold, and who creates them.
- **RD3, what binds per market, and who sets it:** which settings take a value per market, which hold for the whole store, and which the platform sets and which the seller.

Phase A collected what each platform states under eight bullets. Each belongs to a root decision, as `bullets.tsv` says:
- **(a)** to **(d)**, RD1: what fills the store's own country; who sets, checks or changes it; what the platform binds to it; the countries the platform serves, or doesn't;
- **(e)**, RD2: what defines a market a store sells into, how many it can hold, and who creates one;
- **(f)**, RD3: a setting that takes its value per market, whether the store's own country (as in (a)) or a market it sells into (as in (e)), or per buyer's country; and who sets that value;
- **(g)**, RD2 and RD3: that a setting holds for the whole store (RD3's), or that the platform has no market of the kind in (e) (RD2's);
- **(h):** where, or for whom, what a statement under (a) to (f) describes is offered.

Statements under (h) are conditions, not variants: a variant rests on at least one statement under (a) to (g). A later step reads the conditions.

**Your task:** split your root decision into the facets that can change it, as variation points, and place your part's statements under them as variants. Don't judge the variants, and don't give causes; a later phase does that.

## Rules

0. **Same.** In these rules, two words or terms are the same when they are the same words, or a platform's own translation of them in `terms.tsv`, or name the same party or identifier. Quote what shows it.
   - **Without the platform's translation,** you may rest on your own translation of the platform's words. Quote them, and mark the translation as yours in `basis_evidence`.
   - **Two platforms agree** on a variation point when their sets of answers are the same.
1. **The questions.** A bullet asks more than one thing, and each thing is its own kind of variation point, with its own form of question. X is the thing the question asks about, and its role is fixed by the question:

   | Bullet | Questions, each its own variation point | X's role | What a variant names |
   | --- | --- | --- | --- |
   | (a) | `what fills "X"` | the store's own country (below) | the field or record that holds it: the store's address, its billing address, a business entity, the account, a field such as `store_country` |
   | (b) | `who sets "X"`; `who checks "X"`; `who changes "X"`; `what must hold before "X" changes` | the store's own country, as in (a) | the party, or the condition |
   | (c) | `what decides "X"` | a thing the platform binds, of one of the kinds below | what decides it: the store's own country as a field or record holds it, the merchant's residence, the business's registered country, a business entity |
   | (d) | `what countries fill "X"`; `what countries are kept out of "X"` | where the platform serves merchants, in its words | a list of countries, as the platform states or shows it |
   | (e) | `what defines "X"`; `what limits "X"`: how many a store can hold, and the rules on what one may hold; `who creates "X"`; `who changes or removes "X"` | a market a store sells into | a country, region, city, group of customers, location, channel or storefront; the limit or the rule; the party |
   | (f) | `what "X" takes its value per`; `who sets "X"` | a setting of the store, of one of the kinds below | what its value is taken per; the party that sets it: the seller, the platform, the buyer, or a third party the statement names, such as a provider or an app |

   **The store's own country** is the country, address or jurisdiction the platform holds as where the store, or its merchant, is based, registered or resident. It includes what the platform calls the store's country, location or country of operation, the merchant's country of residence, and the country of the merchant's tax registration, unless the statement or the platform's own term ties that registration to a market the store sells into. It isn't:
   - a place the store ships from, sells at, or keeps stock in, such as a pickup point, a branch, a warehouse or a shipping origin. The statement's own words decide: a location they say orders ship from, or stock is kept in, is one of these, whatever the platform calls it;
   - a buyer's country;
   - where the platform hosts the store.

   **A market a store sells into** is what the platform defines for a store to sell to. It isn't the store's own country.

   **The kinds of thing bound, under (c),** from (c)'s own words in `bullets.tsv`. Each kind is one X:
   - the contracting party: the platform's company the merchant contracts with;
   - the terms: which terms apply, and the law and courts that govern them;
   - documents and checks: what the merchant provides to verify the store or the business;
   - the platform's own payment service: whether and how the store can use it;
   - other payment providers: which ones the store can use, and the payment methods it can offer through them, such as cash on delivery or a bank transfer;
   - payouts: where, how and in what currency the merchant is paid;
   - the platform's fees: its plans, their prices, and the currency they are billed in;
   - taxes on the platform's fees;
   - the store's taxes: how its own sales are taxed, from its country;
   - other features and services of the platform that the store can use, such as shipping services;
   - the store's defaults: what the platform sets from the store's country, such as its currency, language or units;
   - the store's data: where it is held, and the privacy law that applies.

   **The kinds of setting, under (f),** from the platforms' own groupings of a market's settings: Shopify's market page (S02-SH-413, S02-SH-316), Salla's sections for a market (S02-SA-024, and the identifiers `القسم 1` to `القسم 8`), and BigCommerce's channel-specific settings (S02-BC-098). A setting of the store is one whose value the seller or the platform sets for the store; a setting of the platform's own account isn't. Each kind is one X:
   - currency: the currencies a buyer sees and pays in, the default among them, and how amounts are converted;
   - language: the languages offered, the default among them, and translated content;
   - domain: the domain, subdomain, subfolder or URL;
   - products: which products are offered, and in what order;
   - prices: product prices, price lists and adjustments;
   - discounts and offers, with gift cards, gifting, store credit, loyalty and affiliates;
   - storefront design: the theme, its settings and its content, the store's app, and what search engines are shown;
   - checkout and customer accounts: checkout's settings and the rules an order must pass, and sign-in and registration;
   - taxes and duties;
   - shipping: zones, rates, options and carriers;
   - payment methods offered to buyers, cash on delivery among them;
   - who sells to the buyer: the business entity, or the merchant of record;
   - returns and cancellations;
   - locations: the branches, warehouses and pickup points that fulfil orders, and how stock is taken from them;
   - contact information shown to buyers;
   - the buyer's address: its fields, format and validation;
   - messages to buyers, such as notifications and the sender's name;
   - staff access: what staff may manage;
   - market selection: how a buyer's market is chosen, suggested, switched or restricted, a backup market among them;
   - privacy and consent: cookie consent, and the privacy settings shown to buyers;
   - store status: whether the store is open or in maintenance.

   **Kinds, under (c) and (f).** A default and the options it is chosen from are one kind, such as a store's default currency and the currencies it supports. A thing that sets two kinds at once, such as a catalog that sets both which products are offered and their prices, goes under both. A thing or setting that fits none of the kinds raises a new kind: name it in `x_words`, and list it in `notes-b.md`.
2. **Candidates.** Each statement under one of your part's bullets that answers one of that bullet's questions gives one candidate per question and per X it answers, with its X quoted from it. A statement that names several settings, such as design, prices and currency, gives a candidate for each.
   - **The role test** applies to X itself: X must be in the question's role, as rule 1 gives it. "Market", "country" and "region" name different things on different platforms, so the test rests on what the statement says X is, not on its words. A feature flag or key whose words, identifier and scope say "country" without saying whose fails the test.
   - **A candidate whose X passes the role test is a facet** of its root decision (`PLAN.md`, Stage 4).
   - **Noted, not placed.** A statement under one of your bullets that answers none of that bullet's questions, or whose X fails the role test, is noted in `notes-b.md`, with the reason in a few words. Write each on its own line, starting with its id and that bullet: `- S02-SA-011 (b): reason`, or `- S02-SA-011 (c, d): reason` for two bullets. Only lines that start this way count as notes, so write ids elsewhere in `notes-b.md` without a bullet in brackets after them. A statement under two of your bullets is noted, or placed, under each.
3. **Variation points.**
   - **X matches by its role.** Candidates under the same question are one variation point when their X is the same in that question's role, whatever each platform calls it:
     - **(a), (b), (d) and (e):** each question has one X in its role, so all candidates of one question make one variation point;
     - **(c) and (f):** candidates are one variation point when their X is of the same kind, from rule 1's lists.
     - Two variation points never share a question and a kind.
   - **The question.** Each variation point keeps its bullet. Its question takes that question's form from rule 1. X is in double quotes, quoted from a statement in `raised_by`, in words that name X itself, not a variant.
   - **`x_words`** gives each platform's own words for X, as the platforms' rows come in. Under (c) and (f) it starts with the kind's name, then ` | ` before each platform's words, such as `the platform's fees | shopify: billing currency | zid: الرسوم`.
   - **`raised_by`** names the statements a point was raised from. A statement is placed only by a variant row, so a statement in `raised_by` has its own row too.
   - **Earlier parts.** Read your root decision's `variation-points.tsv` before you start, and place your statements under its points first. Raise a new one only where none matches.
   - **Every platform has a row** under each variation point (rule 4). Give the rows of your part's platforms, in the order your message gives them.
   - **For a point you raise, give the rows of the platforms placed before it too:** those that earlier parts covered under the same bullet, and those placed earlier in your own part. Each placed its statements under every question and X they answer, and raised a point where none matched. So find their rows by search, not by reading their statements whole:
     1. Print those platforms' statements under that bullet with only their `stmt_id` and `identifier` (`| cut -f1,4,7`), and read those whose identifier names X or its kind.
     2. Search their statements under that bullet, and `notes-b.md`, for X's words in each language, the platforms' translations in `terms.tsv`, your own translations, X's identifiers, and the other platforms' words in the point's `x_words`.
     3. Read what the searches find, and place what answers.
     4. Otherwise, their row is `gap` or `not covered`, as rule 4 says.
     5. Log the words you searched for in `notes-b.md`, under the point's id.
   - **Later parts.** The platforms a later part covers under that bullet are left to it.
4. **Variants.** For each variation point and each platform, give one row per distinct answer the platform gives, with its own `variant_id`.
   - **One answer.** An answer's `variant` excerpt names the who or what that fills X. Two answers are distinct when their excerpts name a different who or what:
     - in (a), each field or record is one answer;
     - in (d), each list of countries, as the platform states it, is one answer: a statement, or the runs of one list read together (rule 5, Lists). Two statements that name the same countries are one answer;
     - the same answer stated in two languages, by the platform's own translation, is one answer;
     - one answer from several statements is one row, with all of them in `stmt_ids`;
     - under (c), things of one kind with the same decider are one answer, such as several payment providers each offered by the merchant's country. Which country gets which stays in the statements and their scope;
     - under (c), a statement that a thing is offered to every store, whatever its country, answers with its excerpt, and `basis_evidence` names `every store`. So does a statement whose own words apply the thing to all stores, merchants, plans, subscriptions or fees, where neither it nor its `scope` names a country, a site or a region;
     - under (c), an answer names what decides X from rule 1's table, or `every store`. A statement whose decider is something else, such as a payment method, where a transfer goes or a carrier, answers nothing: name it in the point's `note`, and note the statement (rule 2). A statement that names no decider, and isn't `every store`, is noted too.
   - **Its form.** A row takes one of four forms:
     - **an answer:** `variant` is an excerpt of one of its statements, verbatim;
     - **`absent`:** the platform's absences show it absent from a complete list, under the variation point's bullet, with those `absence_ids`. Its `kind` is the absence's kind;
     - **`gap`:** one of the platform's gaps under the same bullet asks, in its `what_is_missing`, for this point's answer. Give those `gap_ids`. A `gap` row may stand beside the platform's answer rows, where its gap asks for an answer they don't give;
     - **`not covered`:** the platform has none of these. These rows go back to that platform for gap-closing (phase A2). List them in `notes-b.md`.
   - **What a value is taken per.** Under (f)'s `what "X" takes its value per`, `basis_evidence` names what the setting's value differs by, as the statement shows it, in one of four phrases: `the store's own country`, `a market the store sells into`, `the buyer's country`, or `the whole store`.
     - A value that is the same for every buyer is `the whole store`. One that differs by the buyer's country is `the buyer's country`, even where the store switches the difference on once.
     - A market that takes the store's value until the seller changes it takes its value per `a market the store sells into`.
   - **Who sets, changes or checks it.**
     - Under `who sets "X"` and `who changes "X"`, a control in the store's admin means the seller sets or changes it. "Automatically", "by default" or "on your behalf" means the platform does, unless the statement names another party.
     - Under `who checks "X"`, a check of a field or record that holds the store's own country, as (a)'s answers name them, is a check of X: its address, its business entity, or the business's registration.
     - A staff permission or role that the statement says gates it, or the account's owner, is its own answer, beside the seller's.
     - A party that requires a value without setting it, such as a regulator, isn't who sets it.
     - An answer may be that no one can, in the statement's words, such as "it cannot be changed later".
     - In a platform's code, a value or default the code sets is the platform's. A filter or hook alone names no party. A party the code's words name, such as developers, is its own answer.
   - **(g).**
     - **A statement that a setting holds for the whole store** is the platform's answer under each of RD3's `what "X" takes its value per` points it applies to. Its `variant` is an excerpt of it, and its `basis_evidence` names `the whole store`. Where no such point's X is of its setting's kind, it raises one. Where it also names who sets that setting, it answers the setting's `who sets "X"` point too.
     - **A statement that the platform has no market of the kind in (e)** is its answer under each of RD2's points it applies to. Its `variant` is an excerpt of it, and its `basis_evidence` names `no market`. Where no RD2 point exists yet, it raises `what defines "X"`, with X the platform's words for the market it lacks.
     - **Basis.** A row resting only on such statements takes the basis `answers` alone. A row that also holds other statements lists every basis that holds (rule 5), `answers` among them, so that one answer stays one row.
     - **The other half.** A statement under (g) in your root decision's slice that holds the other decision's half is noted, as rule 2 says.
5. **Matching.** Compare each statement with a statement in the variation point's `raised_by` from another platform, where there is one. Record every basis that holds, with the words that show it in `basis_evidence`. Where `raised_by` holds no other platform's statement yet, the basis is `answers`.
   - `term`: the same term, including a platform's own translation from `terms.tsv`. It fails when the two platforms' definitions in `terms.tsv` differ.
   - `identifiers`: the same key, scope, topic, field or entitlement, as the statement itself states it, not as its `identifier` column's heading gives it;
   - `definition`: the same definition, with both quoted;
   - `answers`: the statement says who or what fills the variation point's X, in X's role.
     - `answers` rests on what the statement says, not on shared words. Its own words must name what fills X in X's role, as rule 2's role test says. `basis_evidence` quotes those words and says which role they name. The role test holds whatever a variant's basis, since shared words can be homonyms.
     - Where a statement's own words don't name its X, or what fills it, its `identifier` or `scope` may, as phase A recorded them from the source, under any bullet. `basis_evidence` then quotes it.
     - A variant whose words name only what is kept out of X's role is not an answer variant. It goes in the variation point's `note`, with its statement's id, and its statement is noted in `notes-b.md` (rule 2). If no other variant of the platform answers, the platform's row is `gap` or `not covered`, as rule 4 says (the pilot's ruling of 25 October 2026, on its review's finding 36).

   A statement goes under a variation point only if at least one basis holds. `basis_evidence` quotes the words that show it from the statements that show it best; it needn't quote every statement in `stmt_ids`.

   **Lists.** Statements that share a `source` and an `identifier` may be runs of one list, split because the source holds the items apart. Read them together.
6. **Kind and scope.**
   - `kind` is copied from the slice's `kind` for each statement of the variant. If they differ, list each, `;`-separated.
   - `scope` is as the statements give it. If they differ, list each scope with its `stmt_ids`, `;`-separated, and leave out the statements without one.
7. **Every statement is placed or noted.** Each statement of your part, under each of your part's bullets it carries, is in one of these places:
   - a variant of a variation point of that bullet, or, for a statement under (g), of a point rule 4 places it under;
   - or `notes-b.md`, as its id followed by that bullet, with its reason (rule 2).

   The checker lists the rest.
8. **No inference,** no ranking and no causes, anywhere, including notes.
9. **Write as you go.** Write to the files at the latest after each platform's statements under each bullet, and more often for a platform with many. If you are stopped, your files must hold everything done so far, and the next run continues from them.
10. **Stop and report** past your root decision's cap of variation points in `b/ranges.tsv`. Report the variation points under each question, and why each is its own. Don't note the statements not yet placed: the checker lists them. The coordinator decides before the next part runs.

## Second pass, after phases A2 and A3

When the coordinator says phases A2 and A3 are done, the slices are cut again to hold what they added, and each root decision gets a work list. The second pass places what was added, under the variation points the first pass raised.

**Your work list** is `b/second-pass/<root decision>/worklist.tsv`, written by `method/second_pass_list.py`. Your message names your part's rows in it. Its columns are `task`, `id`, `platform`, `bullet`, `vp_id` and `why`. Do the tasks in the list's order, revisits first. Don't read the slices whole: print the statements a task names by id, 10 to 15 at a time, with only the columns you need (`--print <RD> --ids ... | cut -f1,2,4,5,7,8,9`). An id the printer doesn't print, it names on its standard error: that statement is under none of your root decision's bullets, so leave it. The tasks:
- **`revisit`:** a row that was `gap`, `absent` or `not covered`, under the point in `vp_id`, which gap-closing worked. `why` first names its **leads**: the statements gap-closing found for the point, under the point's bullet. This task places or notes each lead under that bullet: under this point, or under another of the bullet's points that it answers, or in `notes-b.md` (rule 2). `why` then names the statements under your decision's other bullets, which have their own tasks, and those outside your slice, which you leave. Last, it names the gaps and absences gap-closing left for the point. Replace the row:
  - **with an answer row for each distinct answer** the leads give (rule 4): the first keeps the row's `variant_id` (`replace`), and the others take new ids (`add`);
  - **or, where every answer the leads give is one the platform's rows already hold,** join the leads to those rows (`join`), and `remove` the old row;
  - **or with `absent`,** giving the absences `why` names;
  - **or with `gap`,** giving only the gaps `why` names. A gap `why` doesn't name was settled by gap-closing, and goes. A `gap` row may stand beside answers (rule 4).

  A `not covered` row never stands beside another row of its platform under the same point.
- **`place`:** a statement neither in a variant nor noted, under the `bullet` given. Place it under your root decision's variation points, by the rules above, or note it, as rule 2 says. Each platform's `a2.tsv` names, by point, the statements gap-closing found for it, and `absence-audit.tsv` those the audit recorded for a claim: read them as leads to a point, not as its answer.
- **`reread`:** a statement an earlier part noted under a rule widened since. `why` names the part and the rule. Place it, or leave it noted; its earlier note stays as it is either way.
- **`note`:** a statement not to place. Note it, under its bullet, with the reason `why` gives, in its words.

The second pass adds no variation point and splits none. A statement that fits none is noted, with that reason. Recheck, under rule 5, any row you compared with a statement of its own platform.

**Writing.** Make every change to `variants.tsv`, and to `x_words`, with `method/variants_edit.py studies/subjects/S-02 <root decision> <command>`:
- `rows <vp_id> [<platform>]` prints a point's question, `x_words` and rows;
- `join <variant_id> --stmts <ids> [--evidence <words>]` adds statements to an answer row, and takes its `kind` and `scope` again from all its statements (rule 6);
- `add <vp_id> <platform>` and `replace <variant_id>` write an answer (`--variant <excerpt> --stmts <ids> --basis <bases> --evidence <words>`), a `--gap` with `--gaps`, or an `--absent` with `--absences`; `add` gives the next free id of your range;
- `remove <variant_id>`;
- `done <task> <id> <bullet> <outcome>` records, in a few words, the outcome of each `revisit`, `reread` and `note` task, as soon as it is done;
- `xwords <vp_id> <platform> <words>` adds a platform's words for X.

It refuses an excerpt that isn't in its statements, a statement outside your slice, and a basis outside rule 5's four. Change no row a task doesn't lead you to. Write `notes-b.md` yourself, appending under a heading "Second pass, <your part>": the statements you note, in rule 2's form; the rows you replaced or removed, and what took their place; the rereads you placed; and the words you searched for.

**Write as you go:** each revisit as soon as it is done, and every 15 to 20 other tasks.

**Before you finish,** check as the Output section says, and run `python3 -I method/second_pass_list.py studies/subjects/S-02 --check`, which only reads. In the checker's `unplaced.tsv`, your part's `place` rows and your revisits' leads should be gone. In `--check`'s list, your part's revisit, reread and note tasks should be gone. The checker's `review` lines on quotes found only in a page's source are the coordinator's.

## Output, in `studies/subjects/S-02/b/<root decision>/`

All files are tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field. Use only your root decision's ids in `b/ranges.tsv`, continuing from the last one in your folder.

| File | Columns |
| --- | --- |
| `variation-points.tsv` | `vp_id` (S02-VP-NN) · `bullet` (one of your root decision's bullets from `a` to `f`) · `question` · `x_words` · `raised_by` (stmt_ids) · `note` |
| `variants.tsv` | `variant_id` (S02-V-NNN, or S02-V-NNNN past 999) · `vp_id` · `platform` (`shopify`, `salla`, `woocommerce`, `zid` or `bigcommerce`) · `variant` (an excerpt, `absent`, `gap` or `not covered`) · `stmt_ids` · `basis` (every basis that holds, `;`-separated) · `basis_evidence` · `kind` · `scope` · `gap_ids` · `absence_ids` · `note` |
| `notes-b.md` | Statements noted by id and bullet, with their reasons; new kinds; the searches for earlier platforms' rows; `not covered` rows; problems with the method. |

**Before you finish,** check your files on a copy that holds only your own root decision's folder:
1. Copy `studies/subjects/S-02` to `<your scratch folder>/S-02`, then remove from the copy every folder in `b/` but your own.
2. Run `python3 -I method/merge_slices.py <that folder>/S-02 b`. It refuses ids outside your range, a bullet outside your root decision, or more variation points than your cap.
3. Run `python3 -I method/check_subject.py <that folder>/S-02 <an output folder> $(ls -d evidence/product-class/runs/*)` from the repository's root. It checks every quote of phase A too, and takes several minutes: give it a timeout of fifteen minutes.
4. Fix, in your own folder, every line of level `error` on your ids, except `no row for this variation point and platform` for a platform a later part covers under that bullet.
5. `unplaced.tsv` in the output folder lists the statements, by root decision, bullet and platform, that are neither in a variant nor noted. Read your root decision's rows (its first column). Those of your part's bullets and platforms are yours to place or note; the rest belong to other parts. A statement it lists that your slice doesn't hold was added after the slices were cut, by phase A3 running beside you: leave it for the second pass.
