# M-amend: the held pass's new capabilities, made in amendment parts

**What this is.** The coordinator has decided the held pass's new things in `studies/class-model/held/new.tsv`. Sixteen are new capabilities: each row's reading says 'a new capability, made in `<domain>-amend` with each platform's cells'. This brief's agent makes the capabilities its prompt names in their domain's amendment part, as `parts/E-amend/` made BigCommerce's three (30 October). `method/held_amend.py` later turns the held pass's lines into each cell's evidence; this part gives each capability its row, and each platform its cell from the concern map's statements.

**Read, in this order:**
1. `briefs/B-extent.md`: what a capability is, its place of its own, the supports, and how a cell reads.
2. `parts/E-amend/`, every file, and its `notes.md`: the form to follow, row by row.
3. `held/new.tsv` (the decisions) and `held/new-proposals.tsv` and `.md` (each group's facts, places of its own, proposed definition and open cases): the definition is the coordinator's to word, from these.
4. `merged/capabilities.tsv` and `merged/cells.tsv`, for the area's other capabilities, the parent, and how their cells and readings are written.
5. `python3 -I method/class_slice.py --help`, and its `search` over each platform's statements, in English and, for Salla and Zid, in Arabic.

**Do, for each capability your prompt names:**
1. **Its row** in the part's `capabilities.tsv`: the decided `cap_id`, its area, the capability in the model's form (what it is; then each platform's own names for it, in their words), its parent, and a note: made by the coordinator from the held pass (`held/new.tsv`, 31 October), its place of its own cited, and the joins across platforms marked as readings where they are.
2. **A cell for each of the five platforms** in the part's `cells.tsv`, as `E-amend`'s are: search each platform's statements for the thing; where statements hold it, `held` is `statements`, with their terms and a reading, and the statements' rows in `evidence.tsv` as `E-amend` writes them; where none does, `held` is `none-held`, with the terms searched in `searched` (Arabic too for Salla and Zid). A platform whose held lines name the thing still gets its cell here: `held_amend.py` adds those lines later, so say so in the reading.
3. **Its notes** in the part's `notes.md`: a section 'The held pass's new capabilities (31 October)', each capability's grounds, and the checker's flags read.
4. A part that doesn't exist yet (`A-amend`, `C-amend`, `F-amend`) is made with every file `E-amend` has, each with its header row.

**Then:** run `python3 -I method/check_class_part.py <part>` on each part you wrote, and fix what it finds, until it prints no problem or only flags you read in the notes. Don't edit any other part, the merged files, `held/` or the placements. Don't run `held_amend.py` or `class_merge.py`. Make no commits. Keep your context under about 200,000 tokens: search a capability's five platforms in one script.

**Report** to the coordinator: each capability's row as written, its cells (`statements` or `none-held`, per platform), the checker's last line for each part, and the cases you couldn't settle.
