# Brief: S-02, cause, coexistence and what follows (step 1, phase C)

This is `PLAN.md` Stage 4, subject S-02. You are one agent with one task: one part of one root decision. The message that started you names the root decision and its variation points that make your part. Other agents work on other parts, in the same folder, writing through the same tool.

**Read only this brief and, in `studies/subjects/S-02/`:**
- `bullets.tsv`, the questions phase A asked of each platform;
- your points' rows, printed by `method/point_view.py`;
- once, what defines a market on each platform: S02-VP-26's keys as RD2's part wrote them (`analysis_edit.py studies/subjects/S-02 RD2 show S02-VP-26`), or its rows where that part hasn't run;
- the statements, gaps and absences those rows name, printed by id;
- the platforms' terms, from your root decision's slice;
- your root decision's phase C files, `c/<root decision>/answers.tsv` and `points.tsv`, through the tool's `show`, only for the points your message names.

Don't read `notes*.md` files, any `note` column, the platforms' own folders, or `variants.tsv` whole. What this brief takes from other files, it quotes.

**Printing.** Never read a file whole. Print what you need:

```
python3 -I method/point_view.py studies/subjects/S-02 <RD> <vp_id> [<vp_id> ...] [--platform <p>] [--full]
python3 -I method/point_view.py studies/subjects/S-02 --records <id>,<id>
python3 -I method/subject_slice.py studies/subjects/S-02 --print <RD> --what terms --platform <p>
python3 -I method/subject_slice.py studies/subjects/S-02 --print <RD> --bullet <b> --platform <p> | grep -i <word>
```

- **`point_view.py`** prints each platform's rows for a point, in the three groups below. For each row:
  - its form;
  - its excerpt and evidence;
  - each statement with its kind, scope and release marker;
  - the statements under (h) that condition them;
  - for a `gap` row, what the gap asks; for an `absent` row, what is absent.
- **`--platform`** prints one platform's rows, for a large point; **`--full`** prints rows' evidence whole.
- **`--records`** prints statements, gaps and absences whole by id, from any bullet, (h) among them, each with its kind.
- **The slice printer with `grep`** finds a platform's other statements by their words, such as those that name a law.

## The subject

> What fills "a market": which settings bind per market, and who sets each?

**Its three root decisions** (`PLAN.md`, section 6, step 1):
- **RD1, the store's own country:** what fills a store's country; who sets, checks and changes it; what binds to it; and the countries a platform serves.
- **RD2, the markets a store sells into:** what defines one, how many a store can hold, and who creates them.
- **RD3, what binds per market, and who sets it:** which settings take a value per market, which hold for the whole store, and which the platform sets and which the seller.

**Step 0 is done.** The subject is about the product: it asks what Sharrwah's data model holds. Don't repeat it.

**What S-02 decides, and what it leaves to other subjects** (`frame.md`). S-02 decides where a value is held and who sets it, for every kind of setting, currency and payment methods among them. The value itself, and what a party does with it, belong to the subject that covers it:
- the company that sells to the buyer or contracts with the merchant, merchants of record among them: S-03;
- payment methods' values, and the providers that process or convert payments: S-04;
- taxes: S-05;
- which countries Sharrwah serves: S-07;
- currency's values: S-09;
- delivery and carriers: S-10.

**Then, for each point of your part,** apply the test form's steps 3 to 5 below. They are `PLAN.md`'s, section 6, as the pilot applied them. What this brief adds for S-02 is marked *(the coordinator's own, 27 October 2026)*; S-02's method report lists each, and the founder sees them in S-02's report. What the pilot added keeps its own mark.

## What phase B gives you

Each variation point asks one question of one X, from one bullet. For each point, each platform has rows in one of four forms:
- **answer rows,** one per distinct answer;
- **a `gap`:** a question the platform's evidence doesn't answer, which may stand beside answer rows;
- **`absent`:** absent from a complete list the platform publishes;
- **`not covered`:** nothing recorded.

## The unit: each answer of a point

*(The coordinator's own, 27 October 2026, after the dry run of this brief.)*
- **Why.** Compared as whole sets, every point's platforms differed, so every point came out `vendor choice`. A platform holds refinements beside its main answer, and each refinement made the sets unequal. Mill's methods compare one phenomenon at a time. So phase C compares the platforms on each answer of a point, one at a time: whether each platform gives it.
- **Keys.** First give each answer row of the point a **key**: the answer it gives, in the vocabulary below. One platform's rows that give the same key are one answer. A row whose excerpt and statements give two answers takes both keys.

| Question | Keys |
| --- | --- |
| `what "X" takes its value per` (f) | `a market the store sells into`, `the buyer's country`, `the store's own country`, `the whole store`: the four phrases phase B's evidence names |
| `who sets`, `who checks`, `who changes`, `who creates`, `who changes or removes` | `the seller` (the merchant, "you", the account's owner); `the platform` (its own name, products and company, and the defaults its code sets); `the buyer`; `a staff permission or role`, whatever the platform calls it; `no one`; or a third party by its own name, such as `Stripe` |
| `what must hold before "X" changes` (b) | the condition, in the platform's words |
| `what decides "X"` (c) | `every store`; `the store's country` (as a field or record holds it, such as the store's address or location); `the merchant's country` (where the merchant is, resides or is domiciled, and the one country a site, page or section is tied to); `the business's registered country`; `a business entity`; `the billing address`; or the platform's own word for another decider |
| `what fills "X"` (a) | the field or record, in the platform's words: the store's address, its billing address, a business entity, the account, a country field |
| `what countries fill "X"`, `what countries are kept out of "X"` (d) | each country, or a group the platform names, such as the Gulf states |
| `what defines "X"` (e) | `a country` (one per market); `several countries` (a market of more than one country, or a group of them such as the Gulf states); `a region` (a state or province within a country); `a city`; `a group of customers` (segments or tags); `a company` (a business buyer or its locations); `a location` (a retail location or point of sale); `a channel` (a sales channel or marketplace); `a storefront` (what it serves, such as a region or a brand, goes in `note`); `a default market` (one the platform makes for the store, such as a domestic or primary market); `a market within a market` (a submarket); `no market` |
| `what limits "X"` (e) | `a number of markets per store, set by plan`; `a number of markets per store, the same on every plan`; `no limit on the number of markets`; `markets of some kinds only on some plans`; `one country per market`; `a country in one market only`; `a number of <things> per market`, naming the things, such as catalogs, languages or domains. The numbers and plans go in `note` |

Where a row gives an answer the vocabulary doesn't hold, its key is the platform's own words. Where the platform doesn't say what its term means, `cause_reading` says so. A key in two platforms' own words is the same only by the rule for "same", below. Write the keys with the tool's `keys`. Every answer row takes at least one key.
- **A row that answers another question than its point's** (listed under "Rows phase B left for you to weigh") is keyed by what it says. Where a decision for the founder follows, the item goes to the subject that owns that question.

- **What each platform does on each key.** The tool works it out from the keys, as one of four:
  - `gives`: an answer row of the platform's takes the key;
  - `lacks`: an `absent` row of the platform's excludes the key. Say which key with `--absent`;
  - `open`: the platform has only `gap` or `not covered` rows for the point; or a `gap` row of its asks for this key's answer. Say which key with `--open`;
  - `not stated`: the platform has answer rows, none takes the key, and nothing makes it open.

  `lacks` and `not stated` both count as not giving the key, so two platforms that don't give it agree. A gap blocks only the keys it asks for, and only where its platform's answer could change the cause: the tool tries both ways and says so. A gap whose scope doesn't overlap the scope compared (below) blocks nothing. A gap can't be marked open on a key its platform gives.
- **A platform that gives a key and lacks it** contradicts itself: an answer row gives it, and an `absent` row excludes it. The tool says so. Weigh the two in `cause_reading`, and say which you follow and why.

## The references, in three groups

- **Saudi:** Salla and Zid, which serve the Saudi market first.
- **Global:** Shopify and BigCommerce, independent of each other.
- **Self-hosted:** WooCommerce, software the merchant runs.

## Step 3: cause, for each key

Go down this list and take the first tag that applies to the key *(the order is the pilot's coordinator's own)*. The tool proposes the mechanical tags (1, 4, 5, 6 and 7); you check them, and tests 2 and 3, which need reading.

1. **`no difference`** *(the pilot's coordinator's own)*: every platform gives the key.
   - *(The pilot's coordinator's own, 17 October 2026:)* a variant that names a party only to say it has no part names no one filling X.
2. **`market, named rule`:** a statement names a law, or a regulator's rule, as the reason why a platform gives the key, or doesn't, where the platforms differ on it.
   - *(The pilot's coordinator's own:)* it names a particular law, or a particular regulator with its rule. Generic wording such as "applicable law" or "a regulatory authority" doesn't count.
   - It may be any statement of the subject: one of the key's rows, a statement under (h) that conditions them, or another statement of the platform that you find by its words. Cite it.
3. **`maturity`:** every statement that gives the key on a platform that differs carries a release marker in `marker`, such as beta, early access, preview or sunset; cite them, and the tool checks their markers. A marker on one of several statements doesn't decide it *(the coordinator's own, 27 October 2026, from the pilot's problems)*.
4. **`business model`:** WooCommerce differs from the four hosted platforms on the key, the four agree, and a WooCommerce statement says what it does or doesn't provide *(the pilot's coordinator's own)*. The statement may be one of the point's rows' or one you find in the slice. Without one, this test doesn't apply.
   - *(The coordinator's own, 27 October 2026:)* also, under `what limits "X"`, where the key is a limit the platforms' statements, or the statements under (h) that condition them, tie to their plans or fees, such as `a number of markets per store, set by plan`. This needs no WooCommerce statement.
5. **`market, pattern`:** Salla and Zid agree on the key, Shopify and BigCommerce agree on it, and the two pairs differ.
6. **`vendor choice`:** Salla and Zid differ on the key, or Shopify and BigCommerce do.
7. **`unknown`:** none of the above can be shown, such as when a test needs a platform that is `open` on the key. Name the rows that leave it open in `blocked_by`.

**Rules for comparing:**
- **Same.** Two answers are the same when they use the same words, or a platform's own translation of them in `terms.tsv`, or name the same party or identifier. The same words that `terms.tsv` defines differently on two platforms, such as Shopify's "Designated Country" and WooCommerce's "Designated Countries", aren't the same. *(The pilot's coordinator's own:)* the merchant, the buyer and the platform itself are each one party on every platform, and any other party is the same only by name.
- **`a market the store sells into`** gives the same key on two platforms where it names what each one's rows under S02-VP-26, what defines a market, name for it *(the coordinator's own, 27 October 2026)*. A row may name as its market something those rows don't name for its platform, such as a sales channel, a point of sale, or a channel's target countries. Its key is then that thing, in the vocabulary of (e), and `cause_reading` says so.
- **Like with like.** Compare declarations (`stated`, `official page`, `shipped`) with declarations, and `observed` with `observed`, as Q1's 12 October rule does. A comparison resting on a declaration set against an observation is `unknown`, with why. The pilot's rulings on kinds hold *(the pilot's coordinator's own, 25 and 26 October 2026)*:
  - a platform's documentation about its own policies is `stated`;
  - only terms, pricing and legal pages, and agreements they incorporate, are `official page`;
  - an API's schema as its own introspection answers it is `shipped`.

  `--records` prints each statement's kind. Like with like compares the statements that give a key on two platforms. A platform that doesn't state a key has no statement to compare, so it counts as not giving the key, whatever the kinds of the others' statements.
- **Scopes** *(the pilot's coordinator's own)*. Compare rows whose scopes overlap: the same country, or general. Record the scopes you compared in `scopes_compared`.
  - *(The coordinator's own, 27 October 2026, from the pilot's problems:)* a scope that names a plan, a feature, a store or a business type, but no country, region or site, is general for this test.
  - *(The coordinator's own, 27 October 2026:)* for `no difference`, the platforms may give the key in scopes that don't overlap. Record each in `scopes_compared`.
- **Absence** counts only from an `absent` row, which rests on a complete list. Absence ids (`S02-XX-N…`) may be cited wherever statements are.
- **A cause is a reading.** Write it as one sentence beginning "Reading:", for every key but one with `no difference`. It never becomes a platform statement.

## Step 4: coexistence, for each point

*(The pilot's coordinator's own, 25 October 2026:)* letters are read per root decision. The decision's register entry says which binding its recommendation takes, and the platforms' letters are its evidence. So give each point its letters, in its point row.

Give each platform the letter for how it binds its answers to the point. Where its statements show more than one way, give each letter, joined by `+`, and cite each in `coexistence_basis` *(the pilot's coordinator's own, 17 October 2026)*. `D` and `unknown` stand alone.
- `A`: its answers coexist in one store. Examples: a default for the whole store beside a value per market; a value per market that the buyer's country adjusts; the seller beside a staff permission;
- `B`: one answer per store, market or plan, chosen by configuration, such as a plan that decides whether markets exist at all;
- `C`: set on each product or catalog item, so one store holds several;
- `D`: the platform gives only one answer. Cite a statement saying it can't be another, or an `absent` row. A platform with an open gap on the point can't be `D`;
- `unknown` *(the pilot's coordinator's own)*: the statements don't show which.

*(The coordinator's own, 27 October 2026:)*
- under (a) to (d), give `B` where a statement shows one answer per store, chosen by a record of the store's, such as one contracting party per billing address. Where an answer is a rule the platform's terms fix, give `unknown` unless a statement shows how answers bind;
- under `what limits "X"`, give every platform `unknown`: limits don't bind as answers do.

**Generality.** When one answer is a restricted form of another, and the general one can reach it by configuration, name the general one's rows in `general_variant`, and the statement that shows it can reach the other in `general_basis`. For example, a value per market is general, and `the whole store` its restricted form, where a statement shows that a store can hold one market for all its buyers.

## Step 5: what follows

**For each key,** list every rule that applies, in exactly the words of the right-hand column, separated by `;`:

| Result for the key | What follows |
| --- | --- |
| `no difference` | a commonality, carried as the references carry it |
| `market, named rule` or `market, pattern` | a variation point bound per market |
| `vendor choice` or `business model`, expensive to change | a decision for the founder, on a recommendation |
| `vendor choice` or `business model`, cheap to change | left to the build |
| `maturity` or `unknown`, expensive to change | kept open as a variation point until evidence settles it |
| `maturity` or `unknown`, cheap to change *(the pilot's coordinator's own)* | left to the build |

*(The coordinator's own, 27 October 2026:)* the market rows of the pilot's table bind "D with a market cause". Read for one key at a time, a market cause binds the key per market. Under (d) and (e), whose keys are about markets and countries themselves, that would be circular. There, a market cause follows as vendor choice does, and `cause_reading` names the cause.

**For each point,** list in its point row each letter's rule that applies. A letter's rule applies when at least one platform has that letter *(the pilot's coordinator's own)*:

| Letter | What follows |
| --- | --- |
| A | the platform carries all the variants at once |
| B | a variation point behind one interface, bound per market, store or plan |
| C | bound per product |

If none applies, write `none applies`.

**Expensive to change** means that getting it wrong would mean changing money flows, the legal structure, the data model or partner contracts after launch. Judge it for each key, and say why in `expensive_because`, or write `cheap:` with why. *(The coordinator's own, 27 October 2026, from `frame.md`: S-02 is expensive because every per-market binding hangs on it.)*
- **Where a value is held** is the data model, so expensive: the keys of `what fills`, `what decides`, `what defines`, and `a market the store sells into` under `what "X" takes its value per`. `the buyer's country`, `the store's own country` and `the whole store` are expensive where they decide what is stored. They are cheap where they only pick a default or a display: say which.
- **Who sets, checks, creates or changes it:** judge by what the key's party does with X. Moving money, holding funds, or acting under a contract with the merchant, such as converting or processing payments, is expensive. Naming, displaying or translating is cheap, and so is a screen or a permission.
- **`what limits "X"`:** a number, whether the platform fixes it or a plan sets it, is cheap, since Sharrwah sets its own. A rule on what a market may hold is expensive.
- **`what must hold before "X" changes`** is expensive where the condition touches money or the legal structure, such as a balance to be cleared; elsewhere, cheap.

**Founder items.** Where "a decision for the founder" follows, write the founder's question in `founder_item`. The coordinator writes the recommendation, not you.
- **Under `what defines "X"`,** the keys are options of one decision. Every key there that takes a founder item takes the same one: "What may define a market in Sharrwah?" The coordinator writes it once.
- **A key whose value belongs to another subject** (the list under "The subject") is that subject's. Write the founder's question beginning with the subject's id, such as "S-04: does a payment provider convert the buyer's currency?". The coordinator moves it there.
- **Dependencies** *(the coordinator's own, 27 October 2026, from the pilot's register: founder items aren't independent decisions)*. In `depends_on`, name the points whose own founder items, once answered, would settle this one, and say why in `note`. This is a reading. The likely ones:
  - a `who sets` point depends on its twin, the point of the same kind of setting that asks `what "X" takes its value per`;
  - a key `a market the store sells into` depends on S02-VP-26, what defines a market;
  - a point under (c) depends on S02-VP-01, what fills the store's country.

## Rows phase B left for you to weigh

Phase B's parts marked these as readings, and the coordinator lists them for you *(the coordinator's own, 27 October 2026)*. Each is a row as phase B wrote it. Give it its key by the rules above, and say in `cause_reading` where the reading changes a cause.
- **Markets that are channels, locations or marketplaces:**
  - WooCommerce's Point of Sale, Google's channel visibility, and the store's allowed countries (S02-WC-278), read under (f) as "a market";
  - Zid's sales channel (S02-V-791), and its marketplaces (S02-V-443);
  - Salla Point (S02-V-433).
- **Zid's Region & Language popup** (S02-ZD-187). RD2 reads it as market selection, the buyer switching region. RD3's rows read the country and city it sets as the buyer's country (S02-V-764, S02-V-772, S02-V-781, S02-V-1090), and the buyer as who sets the language (S02-V-1089).
- **Rows whose statements say more or less than their excerpt:** S02-V-099, about any store's seller; S02-V-169, which mixes a general scope with Zid Pay Kuwait's; S02-V-783, per product and per region at once.
- **Rows that may give one answer twice:** S02-V-049 and S02-V-260 (BigCommerce); S02-V-012 and S02-V-013 (Salla); S02-V-100 and S02-V-101 (Shopify).
- **Rows that may answer another question than their point's:**
  - S02-V-757, S02-V-758 and S02-V-814: who converts amounts, not who sets the currency;
  - S02-V-1078: a gateway read as a payment method;
  - S02-V-102: Shopify Payments' contract, not the contracting party;
  - S02-V-785 and S02-V-786: limits on cash on delivery.
- **Rows resting on code read closely:** S02-V-895, minified code; S02-V-840, a provider's configuration.
- **Rows that sit beside an absence they seem to contradict:** S02-V-409 and S02-SH-N03; S02-V-455 and S02-BC-N01.
- **Privacy law read as `every store`** (S02-V-218, S02-V-219).

## Rules

- **Every reading, key and letter cites** the `stmt_ids` or `variant_id`s it rests on.
- **No inference beyond the reading,** anywhere, including notes. No ranking of platforms, and nothing about what Sharrwah should do beyond the rule tables.
- **Depth by risk** (`PLAN.md`, Stage 4). A key every platform gives takes a light check: confirm it from the rows, cite one statement per platform, and go on.
- **Stop and report** if a point can't be analysed from these files. Name what is missing.
- **Write as you go:** each point's keys, answers and point row as soon as they are done.
- **Size.** Keep count of your tool calls. Write a point's answers in one `batch`. At about 100 calls, finish the point in hand, write its rows, run the check, and stop, saying which points are left. A fresh agent continues from your rows.

## Output, in `studies/subjects/S-02/c/<root decision>/`

**Write everything with `method/analysis_edit.py`,** which holds a lock on the folder while it writes:

```
python3 -I method/analysis_edit.py studies/subjects/S-02 <RD> keys <vp_id> --row <variant_id>=<key>[;<key>] ... [--open <variant_id>=<key>] [--absent <variant_id>=<key>]
python3 -I method/analysis_edit.py studies/subjects/S-02 <RD> answer <vp_id> '<key>' --cause '<tag>' --cause-basis '<ids>' --scopes '<...>' --reading 'Reading: ...' --blocked-by '<ids>' --follows '<phrases>' --expensive '<...>' --founder-item '<...>' --depends-on '<vp_ids>' --note '<...>'
python3 -I method/analysis_edit.py studies/subjects/S-02 <RD> point <vp_id> --coexistence 'salla=A; zid=B; shopify=A+B; bigcommerce=D; woocommerce=unknown' --coexistence-basis '<ids>' --general '<variant_ids>' --general-basis '<ids>' --follows '<phrases>' --note '<...>'
python3 -I method/analysis_edit.py studies/subjects/S-02 <RD> show <vp_id>
python3 -I method/analysis_edit.py studies/subjects/S-02 <RD> check <vp_id> ...
python3 -I method/analysis_edit.py studies/subjects/S-02 <RD> notes '<your part>' '<text>'
python3 -I method/analysis_edit.py studies/subjects/S-02 <RD> batch <file>
```

- **`keys`** writes the point's keys and prints, for each key, what each platform does on it (`gives`, `lacks`, `open`, `not stated`), with the cause the mechanical tests give. It replaces the point's keys whole, so give every row's keys each time. The point's answer rows whose key no longer exists are dropped.
- **`answer`** writes one key's row, filling what each platform does from the keys. Give every field the row needs each time. A row's `cause` may differ from the tool's proposal only by tests 2 and 3, or by a reading you write in `cause_reading`.
- **`point`** writes the point's row.
- **`show`** prints the point's keys, its answer rows and its point row.
- **`check`** checks the rows of the points named, and names each answer row, key or point row that is missing.
- **`notes`** appends your text to `notes-c.md` under a heading for your part.
- **`batch`** runs a file of commands, one per line, each as it would follow `<RD>` (such as `answer S02-VP-41 'the whole store' --cause ...`), and says which lines failed. Keep the file in your scratch folder.

It refuses:
- a tag outside step 3;
- a phrase outside the rule tables;
- an id that is neither a statement, gap or absence of the subject, nor a row of a point;
- a coexistence entry it can't read, or a platform with no entry or two;
- `D` with no basis, or for a platform that gives two keys or more;
- `none applies` beside a rule;
- `bound per product` without a `C`, or a `C` without it;
- a founder decision with an empty `founder_item`, or with `cheap:`;
- `no difference` for a key some platform doesn't give;
- `maturity` citing a statement with no release marker;
- a `blocked_by` row that is an answer or `absent`;
- a `depends_on` that is no point, or the point itself.

| File | Columns |
| --- | --- |
| `answers.tsv` | `vp_id` · `key` · `rows` (the variant_ids that give it) · `gives` · `lacks` · `open` · `not_stated` (platforms) · `cause` · `cause_basis` · `scopes_compared` · `cause_reading` · `blocked_by` · `follows` · `expensive_because` · `founder_item` · `depends_on` · `note` |
| `points.tsv` | `vp_id` · `keys` (each row's keys, and the gaps and absences marked) · `coexistence` · `coexistence_basis` · `general_variant` · `general_basis` · `follows` · `note` |
| `notes-c.md` | Under a heading per part: each key whose cause is `unknown`, with why; each point a `blocked_by` row would change, with the row and what it would need to show; problems with the method. |

**Before you finish,** run `check` on your points. It should list no problem and nothing missing.

**Report:**
- your points, and for each key its cause and what follows;
- the founder items, with what each depends on, and those that belong to another subject;
- the keys a `blocked_by` row holds open;
- your count of tool calls;
- problems with the brief or the tools.
