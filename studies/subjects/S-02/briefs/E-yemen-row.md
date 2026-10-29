# Brief: S-02, the Yemen row (step 2)

This is `PLAN.md` Stage 4, subject S-02, its section 6, step 6: the Yemen row, after the analysis. You are one agent with one task. The coordinator checks your rows, and an agent that made none of it reviews them.

**Read only:**
- this brief;
- `PLAN.md`, section 1 (the guard on the first market) and section 6, step 6;
- `founder-decisions.tsv`, its row of 28 October (Sharrwah's markets: Yemen is one of them, and its circumstances may change);
- `studies/subjects/S-02/register.tsv` and `decisions.md`: the decisions and their options;
- Stage 1's records in `studies/yemen-cases/`: `axes.tsv`, `constants.tsv`, `cases.tsv`, `citations.tsv`, `unknowns.tsv` and `corrections.md`. Query them with short scripts, not whole;
- the sources Stage 1's citations name, to check a fact's quote.

## The task

For each founder decision in `register.tsv`, and each option its `alternatives` lists, say what the option needs in Yemen today, and whether that exists:
- **What it needs:** a party, a provider, a partner, a licence, a way to pay, or a condition of the market, such as a currency or an area where the conditions differ. Only what the option itself needs: an option that needs nothing particular in any market needs nothing in Yemen.
- **Whether it exists:** `yes`, `no` or `unknown`, from Stage 1's records:
  - each fact cited by its ids (`YA`, `YK`, `YC`, `YE`), read with its date and with `corrections.md`;
  - each fact checked against its source's quote before you use it;
  - a fact with an exclusion such as "only" read as two facts;
  - a fact the records don't hold is `unknown`, and says what would show it. Nothing is inferred.
- **Changing conditions:** Q2's cases (`cases.tsv`) only where an option depends on a condition that changes, and then the cases where it does.

## Rules

- **Yemen is one market among the founder's.** The row says whether each option can be set up in Yemen today. It never becomes a reason for a recommendation, and it never adds a design need that only Yemen shows. Such a need is a product gap, written without Yemen's name (`PLAN.md` section 6, step 5), and goes in `product_gap`.
- **No decision.** Say what each option needs and what exists, not which option to take.

## Output, in `studies/subjects/S-02/`

- `yemen-row.tsv`: tab-separated, with a header row and no quoting. Columns: `decision_id` · `option` · `needs` · `exists` (`yes`, `no`, `unknown`) · `evidence` (the Stage 1 ids) · `as_of` (each fact's date) · `what_would_show_it` (for `unknown`) · `product_gap` · `note`.
- Your notes in `notes-yemen-row.md`: facts that were hard to read, and problems with the brief or the records.

**Size:** about 50 requests. At about 80, write what you have and stop, saying which decisions are left.

**Report:** per decision, what each option needs in Yemen and whether it exists, in a line; the product gaps; problems.
