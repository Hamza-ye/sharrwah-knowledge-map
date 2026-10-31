# Brief: S-02, designs beyond the references, for D8 and D9

This is `PLAN.md` section 6, "Options beyond the references": "Where a recommendation needs more than the references show, established designs and engineering writing are read for that decision. Each is weighed by its kind of source." S-02's register recommends two options that no reference shows. You read what established designs and engineering writing say on those two questions. You are one agent with one task. You decide nothing, and the coordinator checks your rows.

**Read only:**
- this brief;
- `PLAN.md`, section 6: "Options beyond the references" and "Evidence";
- in `studies/subjects/S-02/register.tsv`, the rows S02-D8, S02-D9, S02-D7, S02-E2 and S02-M6, and in `decisions.md`, the section "Needs no reference meets";
- `method/capture/README.md`, for how a page is captured;
- the sources you find, as you capture them.

Leave out every `notes*.md` file and every `note` column.

## The two questions

- **D8, a seller's area within a country:** how do established designs name and key on an area below the country? What does a rule keyed on such an area need, and what happens when the area changes? For example:
  - standard codes for a country's subdivisions;
  - the hierarchies of places that tax, address or localisation data use.
- **D9, two currency areas under one currency code:** how do established designs identify a currency in money records? Is a currency's code enough, or do they hold a currency as a record that carries its code? What does the standard for currency codes do when one currency's units differ in value? For example:
  - the currency-code standard's own rules for when a new code is given;
  - the money pattern of engineering writing, an amount with its currency;
  - how payment or ledger systems document the currency an amount carries.

## The task

1. **Find the sources.** Prefer, in this order:
   - a standard, or its maintenance body's page;
   - an established engineering book or pattern catalogue;
   - a platform's or provider's own documentation;
   - a company's engineering blog, which is that company's own account.

   At most six sources per question. A source you can't fetch is noted, not guessed.
2. **Capture each page** with the capture tools, into one run: `evidence/designs/runs/<UTC time>-s02-designs/`. Add a short `README.md` to the run, saying what it holds and why. Cite each quote by the captured file's path and line.
3. **Record each source in a row:**
   - what it shows on the question, quoted word for word;
   - its kind;
   - which option of the decision it bears on;
   - a reading, marked as one, of whether it supports the option, weakens it, or bears on neither.

## Rules

- **No decision.** Say what each source shows, not which option to take.
- **No market's facts.** No market's facts, and no market's name, as a reason.
- **Word for word.** Quotes are copied exactly. A reading is marked as one.
- **Your own files only.** Make no commits; the coordinator commits. Run Python with `python3 -I`.

## Output, in `studies/subjects/S-02/`

- `designs.tsv`: tab-separated, with a header row and no quoting. Columns: `decision_id` · `source` (title, and its address) · `kind` · `quote` · `locator` (the captured file's path and line) · `bears_on` (an option letter of the decision's `alternatives`) · `reading` · `note`.
- `notes-designs.md`: what you searched, what you couldn't fetch, and problems with the brief.

**Size:** about 40 requests. At about 60, write what you have and stop.

**Report:** per question, each source in a line, with its kind and what it shows for each option; then problems.
