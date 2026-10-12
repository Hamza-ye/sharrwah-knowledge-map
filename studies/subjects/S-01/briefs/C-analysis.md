# Brief: S-01, cause, coexistence and what follows (pilot, step 1, phase C)

This is `PLAN.md` Stage 2, the pilot. You are one agent with one task.

**Read only this brief and:**
- `studies/subjects/S-01/variation-points.tsv` and `variants.tsv`;
- the five platforms' phase A outputs in `studies/subjects/S-01/<platform>/`, for the statements' own words.

## The subject

> Who holds the merchant's funds between the buyer's payment and the merchant's payout?

**Your task:** for each variation point, apply the test form's steps 3 to 5, as they stand below. They were agreed with the founder on 12 October 2026.

**Step 0 first.** Say once, in `notes-c.md`, whether the subject is about the product, the market context, or the company, and why.

## The references

- **Salla and Zid** serve the Saudi market first.
- **Shopify and BigCommerce** are global platforms, independent of each other.
- **WooCommerce** is self-hosted software.

## The test form, steps 3 to 5

**3. Cause,** found by comparing the references with Mill's methods of agreement and difference. Choose one tag:
- `market, named rule`: a cited statement names the law, regulator or rule;
- `market, pattern`: Salla and Zid agree with each other and differ from Shopify and BigCommerce;
- `vendor choice`: platforms in the same market differ;
- `maturity`: only from the platform's own release markers, such as beta, new or sunset;
- `business model`: follows from how the platform earns or what it holds;
- `unknown`.

**Absence.** Absence counts only from a complete list the platform publishes. A `gap` or `not covered` variant is not absence. When a cause would rest on one, the cause is `unknown`.

**Comparing like with like.** Compare variants of the same kind: `observed` with `observed`, `stated` with `stated`, and so on. A cause that rests on comparing different kinds is `unknown`, with the reason.

**A cause is a reading.** Write it as one sentence beginning "Reading:". It never becomes a platform statement.

**4. Coexistence,** by how the variant is bound. When platforms differ, give it per platform:
- `A`: the variants coexist in one store;
- `B`: one per store, market or plan, set by configuration;
- `C`: one per product, so one store can hold several;
- `D`: mutually exclusive, so a platform offers only one.

**Generality.** When one variant is a restricted form of another, and the general one can reach it by configuration, name the general one.

**5. What follows by rule.** Take the first rule that applies:

| Result | What follows |
| --- | --- |
| A | the platform carries all the variants at once |
| B | a variation point behind one interface, bound per market, store or plan |
| C | bound per product |
| D with a market cause | a variation point bound per market |
| vendor choice or business model, expensive to change | a decision for the founder, on a recommendation |
| vendor choice or business model, cheap to change | left to the build |
| maturity or unknown, expensive to change | kept open as a variation point until evidence settles it |

**Expensive to change** means that getting it wrong would mean changing money flows, the legal structure, the data model or partner contracts after launch. Say which of these applies.

## Rules

- **Every reading cites** the `stmt_ids` it rests on.
- **No inference beyond the reading itself.** No ranking of platforms, and nothing about what Sharrwah should do beyond the rule table.
- **Stop and report** if a variation point can't be analysed without information outside these files. Name what is missing.

## Output, in `studies/subjects/S-01/`

The `.tsv` file is tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field.

| File | Columns |
| --- | --- |
| `analysis.tsv` | `vp_id` · `cause` · `cause_basis` (stmt_ids) · `cause_reading` · `coexistence` (`A`–`D`, or per platform as `shopify=B; salla=D`) · `coexistence_basis` (stmt_ids) · `general_variant` · `follows` · `expensive_because` · `founder_item` (the question for the founder, when the rule gives one) · `note` |
| `notes-c.md` | Step 0; every cause recorded as `unknown`, with why; problems with the method. |
