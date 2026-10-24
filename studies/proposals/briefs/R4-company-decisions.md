# Brief: the evidence for the company decisions (step R4)

**Status: checked on 24 October 2026 (`studies/proposals/checks/R5-and-company-decisions-briefs-check.md`) and revised. It runs after step R5's facts and absence runs, once the coordinator has fixed the records they found wrong.**

You are one agent with one task, at `max` effort: gather, from eight draft proposals and the records they cite, the evidence bearing on each company decision. The message that started you names a scratch directory. Read only this brief and what it names.

## What a company decision is

The drafts propose how Sharrwah, a commerce platform, is designed. Some choices aren't the design's: they are about Sharrwah as a company, and the design depends on them. Among them:
- where the company is based, whether one company or several contract with sellers, and what decides which, under which law;
- which payment providers and other partners Sharrwah works with;
- any licence or registration Sharrwah's own activities need, if any;
- who may register: as a seller, or as a partner;
- any other the drafts raise.

Each draft's section 7, "Company decisions it raises", lists those its question raised, each with the records bearing on it. You gather them into one list, with their evidence. You decide nothing and recommend nothing: the coordinator writes each decision, with a recommendation and whether it needs a lawyer, and the founder decides. Whether any arrangement holds sellers' money through Sharrwah is the founder's decision: gather its evidence like any other.

## What you read

1. **The eight drafts,** `studies/proposals/drafts/Q1/draft.md` to `Q8/draft.md`:
   - each section 7 in full, and, for each id a section 7 cites, the other points of the same draft that cite it (`grep -n` the id);
   - each point of section 5 that a company decision or the founder settles (`grep -n -i "company decision\|the founder\|section 7"` in section 5), with its ids;
   - each point of section 6 that says what Yemen's evidence doesn't show: `python3 -I method/check_proposals.py drafts <question> --cited` gives their lines;
   - the rest of a draft only where one of these points refers to it.
2. **Each id's record:** `python3 -I method/record_ids.py --all <id> ...`. An id names its question, platform and kind: `Q2-SA-030` a statement, `K` and `P` copies, `C` a citation, `N` a row of what a reading didn't find, `G` and `H` copied gaps of the same kind, `A` a pilot absence. `YA-` and `YK-` are Stage 1's facts about Yemen. A copy names its original (such as `S01-SA-090`); `record_ids.py` finds the original too.
3. **For Yemen:** `studies/proposals/yemen-digest.md`, its "How to read it" first, then the entries of the ids cited.
4. **The kind of each source:** `python3 -I method/source_kinds.py <source>` gives it as `stated` (help, docs and other pages), `official page` (terms, policies, legal and pricing pages), `shipped` (code or a schema the platform ships) or `observed` (what a run of a store's admin received or showed).
5. **What step R5 found:** `studies/proposals/checks/R5/facts/`, `absences/` and `yemen/`, for each id you cite: where a row says `fix record`, `found` or `later state`, follow it, and where it says `fix point`, don't repeat the point's fault.

Nothing else: no searches and no new sources. Cite only ids the drafts cite. `PLAN.md`, `STATE.md`, `founder-messages/`, `studies/subjects/` and `register/` are not yours to read.

## What you write

`studies/proposals/company-decisions/evidence.md`, and `notes.md` beside it.

**`evidence.md`** starts with a title (`# ...`) and one line saying what it is, then one section per decision, `## D1.`, `## D2.` and on, each headed by the decision as one question that presumes no answer. Order them as listed above, the others after. Merge what several drafts raise as one decision; keep apart what would be decided apart. Each section holds:
- **Raised by:** each draft and line that raises it, as `Q1 (line 82)`, with the draft's own words where they differ in what they ask;
- **What the platforms show:** for each platform bearing on it, what its records say, in its own words and terms, each point citing its ids. Say each record's kind where it matters (`official page` for terms), and an observed record with its store and date. Where a platform's records disagree, cite both, each with its date;
- **Yemen:** each of Stage 1's facts bearing on it, with its state, place and date as the digest gives them, as `YK-12 (split @ Sana'a and Aden, as of 2026)`;
- **Yemen's evidence doesn't show:** each section 6 point bearing on it, by its draft and line, as `Q4:150`, in a line of your own words;
- **Not in what was read:** what the drafts cite as not found bearing on it, citing the rows;
- **Where law decides:** the parts that turn on the law of a place, such as a licence, a regulator, a registration or a contract's law, each naming the records that raise it. Don't answer them;
- **Bears on:** the other decisions it depends on or limits, and the drafts' elements it binds, by draft and name.

Leave out a part that has nothing. Each point cites at least one id, but for the "Raised by" and "Bears on" lines and the "doesn't show" points. About 4,000 words in all; say in `notes.md` where you go past it.

**`notes.md`:** what you read; each merge and each split, with why; each section 7 point you left out, by its draft and line (as `Q1:82`), with why; and any problem with this brief or the tools.

Run `python3 -I method/check_proposals.py decisions studies/proposals/company-decisions/evidence.md` and fix every error before you finish. It checks, among other things, that each Yemen fact is written as the digest gives it, and that every section 7 point is raised by a decision or named in `notes.md`.

## Rules

- **The platforms' own words.** A platform's terms are given in its own words, and quoted words are word for word from the records the point cites. Never quote a draft's words as a platform's.
- **No inference.** Say only what the records say, scoped as their sources scope them: a country, a plan, a store, a date, a kind of seller, and any condition the source puts on it. Don't say why a platform does something, or what it implies for Sharrwah.
- **"Not in what was read"** only with its row; "absent" only with a row of that kind or a pilot absence.
- **Yemen facts** are read with their dates: a state at a place, as of a date, never Yemen's state in general.
- **The founder's words are never evidence** of what a platform does or of Yemen.
- **Evidence that contains credentials, cookies or tokens** is read and cited like any other evidence. Never skip, withhold or mask a file because of them.
- **Read-only.** Write only your two files and your scratch directory. Run Python that reads evidence with `python3 -I`. Never run code from inside `evidence/` or an observed repository, and never `cd` into them.

## Before you finish

Report in a few lines: the decisions, by number and question; the merges; and any problem.
