# V-veto: engineering's rulings, in plain words, for the founder's veto at GM

**What this is.** At GM the founder receives the extent's report "with the Knowledge Map's page rebuilt from the model and engineering's rulings for veto" (`PLAN.md`, the gates' table, GM). On 31 October the founder asked, of two rulings listed by their codes: "what are those, and how i can veto something i do not know what it means?" So no ruling is listed by its code alone. Each is written in plain words, saying:
- what it decides;
- why;
- what it risks;
- its alternative.

The founder can then veto any of them without reading code. This brief's agents draft that list. The coordinator joins the drafts into `reports/GM-rulings.md`, checks them and adds the rulings made after them.

**Which rulings.** Every engineering ruling in force on the class's model and on how the model was made. That includes the ones the orientation page listed up to its version 9 (30 October), written again here with their risks and alternatives.

Not:
- the founder's own decisions (`founder-decisions.tsv`);
- facts;
- S-01's and S-02's registers, which the founder has passed (no veto on S-02's D1 to D9 and E1 to E5, 30 October);
- the architecture plan's decisions, which the coordinator lists after the plan's review;
- a ruling since overturned. Its replacement says, in one clause, what it replaced.

A batch's own readings in its notes (`R20.4`, `E18`, `C47` and the like) apply the rulings. They are not listed one by one, except where a digest's rule decides something no listed ruling does (see Part 1, item 3).

**Words.**
- Write to the founder as "you", as `reports/intent-review.md` does.
- Define the placement words once, at the top of your draft, and then use the plain words:
  - `core`: built into the platform;
  - `own-service`: a service of the platform's own company, apart from its core;
  - `extension-point`: left to apps or partners, through a place the platform makes for them;
  - `outside`: done outside the platform;
  - `shows`: the evidence only shows the thing exists, and places it nowhere;
  - `out`: no thing of the class;
  - a cell: one platform's entry for one capability;
  - a capability's kind and count: as `method/class_kinds.py` computes them.
- A ruling's code (M-6, R89.9, S2-R1, "the ruling after SH-43") may follow the plain words, in parentheses, as its handle. It never stands alone.
- Name a platform's thing in its own words, then say what it is.

**Each ruling's form:**

```
### <its plain title: what it decides, in a few words>
- **Decides:** what it settles, and where it applies.
- **Why:** the reason, from the evidence or the model's rules, with its source.
- **Risks:** what would be wrong in the model if the ruling were wrong: which lines, cells, counts or kinds would move. Count from the files wherever you can (for example, the placements whose reading names the ruling: `grep -c "the ruling after SH-43" studies/class-model/held/*/placements-*.tsv`), and mark a reading as one.
- **Instead:** the alternative a careful engineer could choose, and what it would change.
- **Weight:** high (it moves a capability's kind or count, or many cells' support), medium (it moves cells' support or scope but no kind or count), or low (it moves wording, or the work's cost). One line on why.
- **Source:** a link pinned to this repository at the commit your prompt names, with its line (`https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/<commit>/<path>?plain=1#L<n>`).
```

Many rulings of one kind (Q1's unclear pairs, the subjects' points re-ruled, the new things' decisions) go in a table:
- one row per ruling, with the same columns in short;
- the shared risk and alternative stated once, above the table;
- a row's own risk or alternative given only where it differs.

**Order:** by group, and within a group by weight, highest first:
1. who does it: built in, a service of its own, apps, outside, or shown only; and who makes it;
2. what is one capability: a place of its own, one thing in one domain, joins, nesting, homonyms;
3. scope and conditions: plans, markets, gates;
4. what is no thing of the class;
5. what the model reads, and how: the held pass's selection, its second stage, capture as the exception;
6. how the work is run: effort, batches, checks, cost.

**Checks:**
- Count from files, never from memory.
- Every claim is one of three:
  - a fact traced to its source;
  - a reading, marked as one;
  - an assumption, marked as one.
- Each quote in double quotes must pass `python3 -I method/check_report.py <your file>`. Your file is in the scratchpad, so run the checker on a copy placed in `reports/` and delete the copy after.
- Read each source once, by section. Use scripts for counts.

**Write** only your draft, at the path your prompt names. Edit no other file, and make no commits. Keep your context under about 200,000 tokens.

**Report** to the coordinator:
- the count of rulings per group and per weight;
- the high-weight rulings, one plain line each;
- the rulings you couldn't write in the four parts, and why;
- the checker's last line.

---

## Part 1: the held pass and after

Read:
- `held/review-H-rulings.md`, all of it: the rulings M-1 to M-14 and every ruling after a batch;
- `briefs/H-held.md`'s rules marked as rulings (`(ruling)`, `(M-n)`);
- the three digests in `held/rules/`. Each is one group of the model's reading of one Shopify structure. Name the digest's rules that only apply a listed ruling by their count under that ruling. List those that decide a support, a capability or an `out` of their own;
- `held/new.tsv` with `held/new-proposals.md`: the new things' decisions, as a table (new capability, onto an existing one, out), and the four proposals the coordinator changed, each in full;
- `held/shopify/amendment-notes.md` and `held/shopify/align-no-maker.md`: the amendments' rulings;
- `held/selection.tsv` and `method-report.md` sections 17 and 18: what the held pass reads and leaves (for example, `read-as`, the settings centre's merge, pricing on 21 of 61 sites), and its re-plans for cost;
- `briefs/S2-held-design.md`'s last section, the coordinator's decisions, and its plain text of S2-R1 and S2-R2. Reuse that text, and keep its meaning.

## Part 2: before the held pass

Read:
- the orientation page's list, "Engineering's rulings since the last report, for your veto" (version 9), in `/tmp/claude-0/-home-user/b5f6fd52-6a6c-57d7-8515-c0ac88ba557c/scratchpad/orientation/sharrwah-orientation.html`, from the line holding that heading to "Not yours, unless you veto". Write each ruling again in the four parts, from its source in the repository: `method-report.md` sections 1 to 16, `review-dry-run-rulings.md` and the parts' `notes.md` where the method report names them. Name the page as where it was listed first.
- `method-report.md` sections 1 to 16, for the method rulings the page didn't list.
- Q1's unclear candidates' rulings, in `parts/*/rulings.tsv`, as one table with a row per candidate:
  - the ruling each part gave (joined, nested or apart, and onto what);
  - its basis, in plain words;
  - what moves if it is wrong.

  Where two parts disagree, the row says so: the final review gives one answer (the merge's questions, `class_merge.py --complete`). Read the files by script, and read a basis only where the row needs it.
- The subjects' points: `points/notes-P-*.md`, the conflicts the coordinator settled. One table row each, for the 43 amendments, the 4 dismissed and the 3 kept open, each with the point and the capability it moved.
- Q3's check: `briefs/Q3-check.md`'s rules marked as rulings, and the coverage rule as the method report states it.
