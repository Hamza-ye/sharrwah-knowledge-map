# Brief: S-02, cause, coexistence and what follows (step 1, phase C)

This is `PLAN.md` Stage 4, subject S-02. You are one agent with one task: one part of one root decision. The message that started you names both: the root decision and its variation points that make your part. Other agents work on the other parts, each on its own points, in the same folder.

**Read only this brief and, in `studies/subjects/S-02/`:**
- `bullets.tsv`, the questions phase A asked of each platform;
- your points' rows, printed by `method/point_view.py`;
- the statements those rows cite, printed by id;
- the platforms' terms, from your root decision's slice;
- in `c/<root decision>/analysis.tsv`, only the rows of points your message names.

Don't read `notes*.md` files, any `note` column, the platforms' own folders, or `variants.tsv` whole.

**Printing.** Never read a file whole. Print what you need:

```
python3 -I method/point_view.py studies/subjects/S-02 <RD> <vp_id> [<vp_id> ...]
python3 -I method/point_view.py studies/subjects/S-02 --stmts <id>,<id>
python3 -I method/subject_slice.py studies/subjects/S-02 --print <RD> --what terms --platform <p>
```

**What `point_view.py` prints.** For each point, it prints each platform's rows in the three groups below. For each row:
- its form;
- the answer its evidence names;
- its kind;
- its statements' scopes and release markers;
- the statements under (h) that condition them. A statement under (h) says where, or for whom, what it conditions is offered: plans, features, countries, business types.

It then prints each platform's set of answers, and the answers two or more platforms share.

The `answer` it prints is the tool's own reading of the row's `basis_evidence`. Check it against the evidence, and never cite it. `--stmts` prints statements whole, from any bullet, (h) among them.

## The subject

> What fills "a market": which settings bind per market, and who sets each?

**Its three root decisions** (`PLAN.md`, section 6, step 1):
- **RD1, the store's own country:** what fills a store's country; who sets, checks and changes it; what binds to it; and the countries a platform serves.
- **RD2, the markets a store sells into:** what defines one, how many a store can hold, and who creates them.
- **RD3, what binds per market, and who sets it:** which settings take a value per market, which hold for the whole store, and which the platform sets and which the seller.

**Step 0 is done.** The subject is about the product: it asks what Sharrwah's data model holds (`frame.md`). Don't repeat it.

**Then, for each point of your part,** apply the test form's steps 3 to 5 below. They are `PLAN.md`'s, section 6, as the pilot applied them (`studies/subjects/S-01/briefs/C-analysis.md`).
- What this brief adds for S-02 is marked *(the coordinator's own, 27 October 2026)*. It is listed in S-02's method report, and the founder sees it in S-02's report.
- What the pilot added keeps its own mark.

## What phase B gives you

Each variation point asks one question of one X, from one bullet. For each point, each platform has rows in one of four forms:
- **answer rows,** one per distinct answer;
- **a `gap`:** the platform's gap asks for an answer its rows don't give. It may stand beside answer rows;
- **`absent`:** absent from a complete list the platform publishes;
- **`not covered`:** nothing recorded.

**The answers, by the point's question** (phase B's rule 1, `briefs/B-variation-points.md`):

| Question | What an answer names |
| --- | --- |
| `what fills "X"` (a) | the field or record that holds the store's own country |
| `who sets "X"`, `who checks "X"`, `who changes "X"` (b); `who creates "X"`, `who changes or removes "X"` (e); `who sets "X"` (f) | a party: the seller; the platform; the buyer; a staff permission or role, or the account's owner; a third party the statement names; or no one |
| `what must hold before "X" changes` (b) | a condition |
| `what decides "X"` (c) | what decides it: the store's own country as a field or record holds it; the merchant's residence; the business's registered country; a business entity; the country a site, page or section is tied to; or `every store` |
| `what countries fill "X"`, `what countries are kept out of "X"` (d) | a list of countries |
| `what defines "X"` (e) | a country, region, city, group of customers, location, channel or storefront, or `no market` |
| `what limits "X"` (e) | a limit or a rule, such as how many markets a plan allows |
| `what "X" takes its value per` (f) | one of four: `the store's own country`, `a market the store sells into`, `the buyer's country`, `the whole store` |

## The references, in three groups

- **Saudi:** Salla and Zid, which serve the Saudi market first.
- **Global:** Shopify and BigCommerce, independent of each other.
- **Self-hosted:** WooCommerce, software the merchant runs.

## Step 3: cause

Go down this list and take the first tag that applies *(the order is the pilot's coordinator's own)*. Compare by Mill's methods of agreement and difference.

1. `no difference` *(the pilot's coordinator's own)*: no row of the point is `gap`, `not covered` or `absent`; at least two platforms answer; and every platform's set of answers is the same.
   - *(The pilot's coordinator's own, 17 October 2026:)* a variant that names a party only to say it has no part names no one filling X, whatever bullet phase A gave its statement.
2. `market, named rule`: a cited statement names a law, or a regulator's rule, as the reason for, or the condition of, a variant that differs from the others.
   - *(The pilot's coordinator's own:)* it names a particular law, or a particular regulator with its rule. Generic wording such as "applicable law" or "a regulatory authority" doesn't count.
   - Any statement of the subject may be that statement, one under (h) or one phase B noted among them.
3. `maturity`: a variant that differs from the others carries a release marker in `marker`, such as beta, early access, preview or sunset.
   - *(The coordinator's own, 27 October 2026, from the pilot's problems:)* every statement the variant rests on carries the marker. A marker on one of several statements doesn't decide the cause.
4. `business model`, either of two tests:
   - *(the pilot's coordinator's own:)* WooCommerce differs from the four hosted platforms, which agree among themselves, and a cited WooCommerce statement says what it does or doesn't provide;
   - *(the coordinator's own, 27 October 2026:)* under `what limits "X"`, the limits that differ are ones the platforms' statements, or the statements under (h) that condition them, tie to their plans or fees, such as how many markets each plan allows.
5. `market, pattern`: Salla and Zid agree with each other, and differ from Shopify and from BigCommerce.
6. `vendor choice`: Salla and Zid differ from each other, or Shopify and BigCommerce do.
7. `unknown`: none of the above can be shown, including when a comparison needs a row that is `gap` or `not covered`.

**Rules for comparing:**
- **Same, agree, differ.** Two answers are the same when they use the same words, or a platform's own translation of them in `terms.tsv`, or name the same party or identifier. Two platforms agree on a point when their sets of answers are the same; otherwise they differ. A platform's two rows that name the same who or what are one answer in its set.
- **Parties** *(the pilot's coordinator's own)*. The merchant, the buyer and the platform itself are each one party on every platform. The platform itself includes its own name, its own products, its own company, and the defaults its code sets. Any other party, such as Stripe or a payment gateway, is the same only by name.
  - *(The coordinator's own, 27 October 2026:)* a staff permission or role is one answer on every platform, whatever the platform calls it: the seller's staff, acting as the seller allows. So is no one.
- **Answers of S-02's own forms** *(the coordinator's own, 27 October 2026)*:
  - **Under `what "X" takes its value per`,** each of the four phrases is one answer on every platform.
  - **`a market the store sells into`** is the same answer on two platforms where it names what each one's rows under S02-VP-26 (what defines a market) name for it. A row may name as its market something those rows don't name for its platform, such as a sales channel, a point of sale, or a channel's target countries. Compare that row as the thing it names, and say so in `cause_reading`.
  - **Under `what decides "X"`,** each decider is one answer, and so is `every store`. A site, page or section that the platform ties to one country answers as that country, the merchant's.
  - **Under `what fills "X"`,** two fields or records are the same by the rule above: the same words, translation or identifier. Each platform's own field is otherwise its own answer.
- **Like with like.** Compare declarations (`stated`, `official page`, `shipped`) with declarations, and `observed` with `observed`, as Q1's 12 October rule does. A cause resting on a declaration set against an observation is `unknown`, with why. The pilot's rulings on kinds hold (`studies/subjects/S-01/briefs/C-analysis.md`): a platform's documentation about its own policies is `stated`, and kinds follow `method/source_kinds.py`.
- **Scopes** *(the pilot's coordinator's own)*. Compare variants whose scopes overlap: the same country, or general. Record the scopes you compared in `scopes_compared`.
  - *(The coordinator's own, 27 October 2026, from the pilot's problems:)* a scope that names a plan, a feature, a store or a business type, but no country, region or site, is general for this test.
- **Absence** counts only from an `absent` row, which rests on a complete list. A `gap` is not absence. Absence ids (`S02-XX-N…`) may be cited wherever statements are.
- **Gaps** *(the coordinator's own, 27 October 2026)*.
  - A `gap` or `not covered` row leaves its platform's set open. So it blocks a test that needs that platform to agree with another, or to differ from it.
  - Name every row that blocks a test you would otherwise have applied in `blocked_by`, with the test in `cause_reading`. The coordinator reads `blocked_by` to see which open questions could change a cause.
  - A platform still differs where its own statements exclude an answer another platform gives, such as "only one currency per store". Cite that statement.
- **Shared answers** *(the coordinator's own, 27 October 2026, from the pilot's problems: strict set equality hides what platforms share)*. In `shared`, name each answer that two or more platforms give, with those platforms, whatever the cause. Start from the tool's `shared` line, and correct it where your comparison differs.
- **A cause is a reading.** Write it as one sentence beginning "Reading:". It never becomes a platform statement.

## Step 4: coexistence

From Stage 4, a subject's letters are read per root decision *(the pilot's coordinator's own, 25 October 2026)*: the decision's register entry says which binding its recommendation takes, and the platforms' letters are its evidence. So give each point its letters, as below.

Give each platform the letter for how it binds its variants. Where its statements show more than one way, give each letter, joined by `+`, as `shopify=A+B`, and cite each letter's statements in `coexistence_basis` *(the pilot's coordinator's own, 17 October 2026)*. `D` and `unknown` stand alone. The letters:
- `A`: the variants coexist in one store;
- `B`: one per store, market or plan, set by configuration;
- `C`: one per product, so one store can hold several;
- `D`: the platform offers only one. Cite either a statement saying so or an `absent` row;
- `unknown` *(the pilot's coordinator's own)*: the statements don't show which.

*(The coordinator's own, 27 October 2026.)* In S-02, a point's variants are its answers, so the letters read:
- `A`: the platform holds several answers at once in one store. Examples: a default for the whole store beside a value per market; a value per market that the buyer's country adjusts; the seller beside a staff permission.
- `B`: one answer per store, market or plan, chosen by configuration, such as a plan that decides whether markets exist at all.
- `C`: set on each product or catalog item, so one store holds several, such as which markets a product is offered in.
- `D`: the platform gives only one answer, and a statement says it can't be another, or an `absent` row shows it.

**Generality.** When one variant is a restricted form of another, and the general one can reach it by configuration, name the general one in `general_variant`. Several ids may go there, `;`-separated *(the coordinator's own, 27 October 2026, from the pilot's problems)*.
- *(The coordinator's own:)* for example, a value per market is general, and `the whole store` its restricted form, where a statement shows that a store can hold one market for all its buyers. Cite it.

## Step 5: what follows by rule

List every rule below that applies, each in exactly the words of the right-hand column, separated by `;`. If none applies, write `none applies`. A letter's row applies when at least one platform has that letter *(the pilot's coordinator's own)*.

| Result | What follows |
| --- | --- |
| no difference *(the pilot's coordinator's own)* | a commonality, carried as the references carry it |
| A | the platform carries all the variants at once |
| B | a variation point behind one interface, bound per market, store or plan |
| C | bound per product |
| D with a market cause | a variation point bound per market |
| vendor choice or business model, expensive to change | a decision for the founder, on a recommendation |
| vendor choice or business model, cheap to change | left to the build |
| maturity or unknown, expensive to change | kept open as a variation point until evidence settles it |
| maturity or unknown, cheap to change *(the pilot's coordinator's own)* | left to the build |

**Expensive to change** means that getting it wrong would mean changing money flows, the legal structure, the data model or partner contracts after launch. Say which applies in `expensive_because`, or `cheap:` with why.

*(The coordinator's own, 27 October 2026, from `frame.md`: S-02 is expensive because every per-market binding hangs on it.)* By the point's question:
- **Where a value is held** is the data model, so expensive. These questions are `what fills`, `what decides`, `what defines` and `what "X" takes its value per`.
- **Who sets, checks, creates or changes it** is expensive only where X is a money flow, the legal structure or a partner contract. That is: the contracting party; the terms; documents and checks; payments and their providers; payouts; the platform's fees and their taxes; who sells to the buyer. Elsewhere it is cheap, a screen or a permission. Say which.
- **`what limits "X"`** is cheap where the limit is a number the configuration sets, and expensive where it is a rule on what a market may hold.
- **`what must hold before "X" changes`** is expensive where the condition touches money or the legal structure, such as a balance to be cleared; elsewhere, cheap.
- **Under (d),** which countries Sharrwah serves is the founder's question in S-07, not this subject's (`frame.md`, "Where it meets other subjects"). Compare the lists as usual. Where a decision for the founder follows, write in `founder_item`: "S-07: which countries Sharrwah serves".

**Founder items.** When "a decision for the founder" applies, write the founder's question in `founder_item`. The coordinator writes the recommendation, not you.

*(The coordinator's own, 27 October 2026, from the pilot's register: founder items aren't independent decisions.)* In `depends_on`, name the points whose own founder item, once answered, would settle this one. This is a reading, so say why in `note`. The likely ones:
- a `who sets "X"` point depends on its twin, `what "X" takes its value per`, with the same X;
- a point whose answers include `a market the store sells into` depends on S02-VP-26, what defines a market;
- a point under (c) depends on S02-VP-01, what fills the store's country.

## Rows phase B left for you to weigh

Phase B's parts marked these as readings, and the coordinator listed them for you *(the coordinator's own, 27 October 2026)*. Each is a row as phase B wrote it. Compare it by the rules above, and say in `cause_reading` where the reading changes the cause.
- **WooCommerce's channels as markets.** Rows under (f) cite Point of Sale, Google's channel visibility, and the store's allowed countries (S02-WC-278) as "a market". RD2's rows under S02-VP-26 define WooCommerce's market by its selling locations. Phase B noted S02-WC-359, Google's target countries, as not a market.
- **Zid's sales channel as a market** (S02-V-791).
- **The city and country a buyer picks in Zid's Region & Language popup,** read under (f) as the buyer's country.
- **Privacy law read as `every store`** (S02-V-218, S02-V-219).
- **Rows that may give one answer twice:** S02-V-049 and S02-V-260 (BigCommerce), and S02-V-012 and S02-V-013 (Salla).
- **S02-V-099:** its excerpt names "Stores with multiple languages enabled", while its statements are about any store's seller. Read its statements, not only its excerpt.

## Rules

- **Every reading and letter cites** the `stmt_ids` or `variant_id`s it rests on.
- **No inference beyond the reading,** anywhere, including notes. No ranking of platforms, and nothing about what Sharrwah should do beyond the rule table.
- **Depth by risk** (`PLAN.md`, Stage 4). Where every platform answers and agrees, check it lightly: confirm the sets from the rows, cite one statement per platform, and go on.
- **Stop and report** if a point can't be analysed from these files. Name what is missing.
- **Write as you go:** each point's row as soon as it is done.
- **Size.** Keep count of your tool calls. At about 100, finish the point in hand, write its row, run the check, and stop, saying which points are left. A fresh agent continues from your rows.

## Output, in `studies/subjects/S-02/c/<root decision>/`

**Write each row with `method/analysis_edit.py`:**

```
python3 -I method/analysis_edit.py studies/subjects/S-02 <RD> set <vp_id> --cause '<tag>' --cause-basis '<ids>' --scopes '<...>' --reading 'Reading: ...' --shared '<...>' --blocked-by '<ids>' --coexistence 'salla=A; zid=B; shopify=A+B; bigcommerce=D; woocommerce=unknown' --coexistence-basis '<ids>' --general '<ids>' --follows '<phrases>' --expensive '<...>' --founder-item '<...>' --depends-on '<vp_ids>' --note '<...>'
```

- `set` writes the point's whole row each time, so give it every field the row needs.
- It refuses:
  - an unknown tag;
  - a coexistence entry it can't read, or one missing for a platform;
  - a phrase not in the rule table;
  - an id that is neither a statement of the subject nor a row of the point;
  - a `blocked_by` row that is an answer.
- `show <vp_id>` prints a row you wrote.
- `check` checks your rows, and lists the points of the root decision that have none.

| File | Columns |
| --- | --- |
| `analysis.tsv` | `vp_id` · `cause` · `cause_basis` (stmt_ids) · `scopes_compared` · `cause_reading` · `shared` · `blocked_by` (variant_ids) · `coexistence` (one letter or `+`-joined letters per platform) · `coexistence_basis` (stmt_ids or variant_ids) · `general_variant` (variant_ids, or empty) · `follows` · `expensive_because` · `founder_item` · `depends_on` (vp_ids) · `note` |
| `notes-c.md` | Appended under a heading "<your part>": every cause recorded as `unknown`, with why; the points whose cause a `blocked_by` row would change, with the row and what it would need to show; problems with the method. |

**Before you finish,** run `python3 -I method/analysis_edit.py studies/subjects/S-02 <RD> check <your vp_ids>`. It should list no problem and no point of yours without a row.

**Report:** your points, by cause and by what follows; the founder items, with what each depends on; the points a `blocked_by` row holds open; your count of tool calls; and problems with the brief or the tools.
