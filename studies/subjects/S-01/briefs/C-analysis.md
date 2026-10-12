# Brief: S-01, cause, coexistence and what follows (pilot, step 1, phase C)

This is `PLAN.md` Stage 2, the pilot. You are one agent with one task.

**Read only this brief and, in `studies/subjects/S-01/`:**
- `variation-points.tsv` and `variants.tsv`;
- each platform's `statements.tsv`, `terms.tsv` and `absences.tsv`, for the platforms' own words.

Don't read `notes*.md` files or any `note` column.

## The subject

> Who holds the merchant's funds between the buyer's payment and the merchant's payout?

**Step 0, once, in `notes-c.md`.** Is the subject about the product, the market context, or the company? Say why. Company questions go to the founder.

**Then, for each variation point,** apply the test form's steps 3 to 5 below. They were agreed with the founder on 12 October 2026. Where this brief adds to them, the addition is marked *(the coordinator's own)*: it is recorded in `PLAN.md` section 11, and the founder sees it at G1.

## The references, in three groups

- **Saudi:** Salla and Zid, which serve the Saudi market first.
- **Global:** Shopify and BigCommerce, independent of each other.
- **Self-hosted:** WooCommerce, software the merchant runs.

## Step 3: cause

Go down this list and take the first tag that applies *(the order is the coordinator's own)*. Compare by Mill's methods of agreement and difference.

1. `no difference` *(the coordinator's own)*: no variant is `gap`, `not covered` or `absent`; at least two platforms answer; and every `variant` excerpt names the same who or what.
2. `market, named rule`: a cited statement names a law or a regulator's rule as the reason for, or the condition of, a variant that differs from the others.
3. `maturity`: a variant that differs from the others has a statement carrying a release marker, recorded in `marker`.
4. `business model` *(this test is the coordinator's own)*: WooCommerce differs from the four hosted platforms, which agree among themselves, and a cited WooCommerce statement says what it does or doesn't provide.
5. `market, pattern`: Salla and Zid agree with each other, and differ from Shopify and from BigCommerce.
6. `vendor choice`: Salla and Zid differ from each other, or Shopify and BigCommerce do.
7. `unknown`: none of the above can be shown, including when a needed variant is `gap` or `not covered`.

**Rules for comparing:**
- **Same, agree, differ.** Two things are the same when they use the same words, or a platform's own translation of them in `terms.tsv`, or name the same party or identifier. Two platforms agree on a variation point when their sets of answers are the same; otherwise they differ.
- **Like with like.** Compare declarations (`stated`, `official page`, `shipped`) with declarations, and `observed` with `observed`, as Q1's 12 October rule does. A cause resting on a declaration set against an observation is `unknown`, with why.
- **Scopes** *(the coordinator's own)*. Compare variants whose scopes overlap: the same country, or general. Record the scopes compared in `scopes_compared`.
- **Absence** counts only from an `absent` variant, which rests on a complete list. A `gap` is not absence. Absence ids (`S01-XX-N…`) may be cited wherever statements are.
- **A cause is a reading.** Write it as one sentence beginning "Reading:". It never becomes a platform statement.

## Step 4: coexistence

Give one letter for each platform, by how the platform binds its variants:
- `A`: they coexist in one store;
- `B`: one per store, market or plan, set by configuration;
- `C`: one per product, so one store can hold several;
- `D`: the platform offers only one. Cite either a statement saying so or an `absent` variant.
- `unknown` *(the coordinator's own)*: the statements don't show which.

**Generality.** When one variant is a restricted form of another, and the general one can reach it by configuration, name the general one's `variant_id`.

## Step 5: what follows by rule

List every rule below that applies, each in exactly the words of the right-hand column, separated by `;`. If none applies, write `none applies`. A letter's row applies when at least one platform has that letter *(the coordinator's own)*.

| Result | What follows |
| --- | --- |
| no difference *(the coordinator's own)* | a commonality, carried as the references carry it |
| A | the platform carries all the variants at once |
| B | a variation point behind one interface, bound per market, store or plan |
| C | bound per product |
| D with a market cause | a variation point bound per market |
| vendor choice or business model, expensive to change | a decision for the founder, on a recommendation |
| vendor choice or business model, cheap to change | left to the build |
| maturity or unknown, expensive to change | kept open as a variation point until evidence settles it |
| maturity or unknown, cheap to change *(the coordinator's own)* | left to the build |

**Expensive to change** means that getting it wrong would mean changing money flows, the legal structure, the data model or partner contracts after launch. Say which applies in `expensive_because`, or `cheap` with why.

**Founder items.** When "a decision for the founder" applies, write the founder's question in `founder_item`. The coordinator writes the recommendation, not you.

## Rules

- **Every reading and letter cites** the `stmt_ids` or `variant_id`s it rests on.
- **No inference beyond the reading,** anywhere, including notes. No ranking of platforms, and nothing about what Sharrwah should do beyond the rule table.
- **Stop and report** if a variation point can't be analysed from these files. Name what is missing.

## Output, in `studies/subjects/S-01/`

The `.tsv` file is tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field.

| File | Columns |
| --- | --- |
| `analysis.tsv` | `vp_id` · `cause` · `cause_basis` (stmt_ids) · `scopes_compared` · `cause_reading` · `coexistence` (`shopify=B; salla=D; …`, one letter per platform) · `coexistence_basis` (stmt_ids) · `general_variant` (a variant_id, or empty) · `follows` · `expensive_because` · `founder_item` · `note` |
| `notes-c.md` | Step 0; every cause recorded as `unknown`, with why; problems with the method. |
