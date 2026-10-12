# Brief: Yemen's axes and cases (Q2, step 1)

This is `PLAN.md` Stage 1. You are one agent with one task. Read only this brief and the evidence named under "Inputs".

## The task

This is Q2's first step, as agreed with the founder:

> Using only Yemen evidence:
> 1. Identify the axes the market varies along, and build cases on them, with today as the anchor case.

**The market** is commerce in Yemen: the conditions under which merchants sell and buyers pay there.

**Axes come from the evidence alone.** No list of axes is given to you, and none should be assumed.

**Only step 1.** Later steps are done elsewhere, and moves are not cases: don't record them.

**Nothing about what Sharrwah does or should do.** Practices of any party in Yemen are market evidence. Record them like any other.

## Definitions and rules for building

1. **Candidate.** One thing whose state differs, between sources or within one, by date, by place or by legal text.
2. **Axis.** A candidate the evidence shows in at least two states.
   - Merge two candidates into one axis only when every source that gives a state of one also gives the other's matching state.
   - List each merge in `notes.md`.
3. **Constant.** A condition a source states, in the words you quote, for Yemen as a whole, and that no source shows in another state. It goes in `constants.tsv`, not on an axis.
4. **State labels.** A state is a short label in English, with the source's own words in parentheses where it has them.
   - **A place.** When a source ties a state to a place, the label ends with ` @ <place>`, naming the place in the source's own words. An axis state with no place holds for the whole market.
   - **Same place.** Two places are the same only when they are named identically.
   - **Same label everywhere.** Use the same label everywhere it appears.
5. **When a state held.** Date each state by when its source says it held, or by the source's date if it doesn't say.
   - **Still holds.** A state the source says still holds takes the source's date.
   - **A range.** A state given for a range of dates takes the range's end.
   - **Precision.** Dates of different precision are compared at the coarser one, so 2024 and March 2024 tie.
   - **A source's date,** in this order:
     - its effective date;
     - otherwise its published date;
     - otherwise the date it shows.
   - **A live page** is a page in which a party describes its own current service or rule. An undated live page takes its capture date.
   - **Other undated sources** come last.
   - **`date_basis`** says which applies.
   - **Age.** A source's age never discounts it.
6. **Today.** An axis's `today` joins, with ` + `, the latest-dated state of each place.
   - **No place.** States with no place count as one more place: the whole market.
   - **A later state with no place** supersedes older states for named places.
   - **Disputed.** Two sources with the same latest date that give different states for the same place make `today` read `disputed`. Record both, and don't resolve them.
7. **Today's case, `YC-00`,** puts every axis at its `today`. It is the one anchor case.
8. **Further cases** are built in two ways and no others:
   - **One case per non-today state** of each axis, with every other axis at today's state. When an axis is `disputed`, each of its disputed states counts as non-today. On an axis whose `today` joins places, a state for a place replaces only that place's part.
   - **One case per combination** of states that a single source shows holding at one time. The axes that source doesn't give stay at today's state.

   Skip a case that duplicates another. A case's `name` lists only the states that differ from today, for example `YA-03=<label>`.
9. **Basis** of a further case, the first that applies:
   - `in force`: the state holds now, somewhere in the market;
   - `occurred`: it held at some time;
   - `provided for`: an enacted law or an issued decision provides for it.
10. **Stop** when, after merges, a 16th axis appears. Say so in `notes.md`, and don't continue past it.

## Inputs

**Read and cite only files under these folders:**
- **`evidence/yemen/runs/`.** Four capture runs.
  - Each run's `README.md` says where it was fetched from.
  - Each run's `manifest.tsv` names each item's readable text in its `text_file` column, usually `items/<n>-<host>/text.txt`.
- **`evidence/yemen/blocked-evidence-founder/`.** Pages the founder saved from inside Yemen on 10 October 2026, as single-file HTML, with a `manifest.tsv`.
- **`evidence/yemen/derived/`.** OCR text of scanned PDFs. When you quote one:
  - cite the OCR text file;
  - name the PDF and its run in `locator`;
  - give the PDF's address in `url`;
  - give that run's `fetched_from`.
- **`evidence/yemen/attestations/`,** for any attestation besides `TEMPLATE.md`. Cite it with `fetched_from` `attestation`, its date as `source_date`, and an empty `url`.

**Don't open:**
- `evidence/yemen/README.md` and `evidence/yemen/finding-aids/`;
- `yemen-setup-options/`, `register/`, `model/`, `shopify-payments-study/`, `studies/` (except your own output folder), `questions/`;
- `NEXT.md`, `PLAN.md` and `STATE.md`.

## Quotes and citations

- **Quotes are verbatim,** at most 300 characters, with no ellipses. Keep each one within one paragraph of its source. Arabic stays in Arabic, as written.
- **How the checker matches.** It collapses whitespace, removes HTML tags and decodes entities, on both the quote and the source.
- **`source`** is `sharrwah-knowledge-map@<commit>:<path>`, where `<commit>` is the output of `git rev-parse HEAD` when you start.
- **`locator`** is the heading, or the line number, in the cited file.
- **`fetched_from`** is `inside Yemen` or `outside Yemen`, from the run's README, or `attestation`.
- **Disagreements.** Where sources disagree, record each with its citation.
- **Inference** never goes into an axis, state, constant or case. A note may hold inference, starting with "Inference:", and it never counts.

## Unknowns

Record in `unknowns.tsv`:
- every axis whose `today` no source shows;
- every state a case needs that no source shows.

For each one, list what you read looking for it, with each path, whether you could read it or not. Name who could close it:
- `agent`: a source online;
- `founder`: a source reachable only from inside Yemen;
- `reader`: a held file that couldn't be read, such as a scanned PDF with no OCR text.

## Output, in `studies/yemen-cases/`

All files are tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field. Write the files as you go: if you are interrupted, the next run continues from them.

| File | Columns |
| --- | --- |
| `axes.tsv` | `axis_id` (YA-01…) · `axis` (a short name, with the sources' own term in parentheses where they have one) · `what_varies` (one sentence) · `states` (`label [YE-001, YE-007] \| label @ place [YE-010]`: every state with its own citations) · `today` (a state label, several joined by ` + `, `disputed`, or `unknown`) · `today_cite_ids` · `note` |
| `constants.tsv` | `constant_id` (YK-01…) · `condition` · `cite_ids` · `note` |
| `cases.tsv` | `case_id` (YC-00, then YC-01…) · `name` · `axis_states` (`YA-01=<label>; YA-02=<label>; …`, every axis, using the labels in `axes.tsv`, joined by ` + ` where `today` joins them, or `disputed` or `unknown`) · `basis` (`today`, `in force`, `occurred`, or `provided for`) · `cite_ids` · `note` |
| `citations.tsv` | `cite_id` (YE-001…) · `source` · `locator` · `quote` · `source_date` · `date_basis` · `fetched_from` · `url` (the source's own address, from the manifest) |
| `unknowns.tsv` | `about` (an axis_id or case_id) · `what_would_show_it` · `who_can` (`agent`, `founder` or `reader`) · `route` · `read` (each path read looking for it, `; `-separated) · `why_not_held` |
| `notes.md` | What you read, with counts per run; the merges; what couldn't be read; disagreements; problems with the method. |

**Done when:**
- every state, every `today` and every case cites evidence or is listed in `unknowns.tsv`;
- every quote is copied verbatim from its file.
