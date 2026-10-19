# Brief: one question's draft proposal (step R4)

**Status: draft, 19 October 2026. It is checked before it runs.**

You are one agent with one task: the draft proposal for one question. The message that started you names the question and a scratch directory. Your folder is `studies/proposals/drafts/<question>/`. You run at `max` effort.

## What the draft is for

- **Sharrwah** is a commerce platform for sellers. It is to be built once and set up for each country it serves. Yemen is the first country it serves, not its design target.
- **Five platforms** were read for your question: Shopify, Salla, WooCommerce, Zid and BigCommerce. Some were read in depth; the others were checked only for what differs from the in-depth ones or goes beyond them.
- **Your draft** says how the five handle the question, and proposes Sharrwah's model for it, from their evidence: enough to start the design of Sharrwah's first build.
- **The coordinator** finishes the proposal from your draft, and owns its recommendation. The founder accepts or changes it. Your draft decides nothing.

## Read only

1. **Your question:** its section in `studies/proposals/questions-for-agents.md`. Its sentences are numbered in square brackets. Use those numbers.
2. **Which platforms were read in depth,** and why: your question's rows in `studies/proposals/areas/depth.tsv`.
3. **The five accounts:** `studies/proposals/records/<question>/<platform>/account.md`. Read the in-depth ones first, in `depth.tsv`'s order, then the checks.
   - Each account says what its platform shows for the question, in its own terms, and each point ends with the ids it rests on.
   - A check's points carry labels. "the same" and "differs" name the in-depth points they match, and the basis; "goes beyond" matches none; "not in what was read" is an in-depth point the check's reading didn't show.
4. **The records behind the accounts,** by id only: `python3 -I method/record_ids.py <id> [<id> ...]` prints each id's row and the quotes it rests on, with each source and its date. Look up what your proposal will rest on, and wherever an account point is unclear.
   - From each platform's `notes.md`, read only its lists of account points not checked, and of copies found wrong or out of date.
5. **The areas list:** in `studies/proposals/areas/areas.md`, the areas whose questions include yours (for Q8, every area). They show what each platform files where, in its own names.
   - `studies/proposals/areas/areas.tsv` holds the founder's mark for each area in its `mark` column, where there is one. With no `mark` column, no area is marked yet.
6. **Yemen's evidence:** `studies/proposals/yemen-digest.md`, read whole once, and Stage 1's rows by id with `record_ids.py`.
7. **For Q5 only,** the pilot's files in `studies/subjects/S-01/`: in `entry.md`, its Decisions 1 to 13 and its last section, "What this entry rests on, and what would change it"; `variation-points.tsv`; and in `method-report.md`, the list "Still open after the re-check".
8. **For Q7 only,** in the same `entry.md`, Decision 14's section.

Read nothing else: not the platforms' own pages or files, other questions' records, `PLAN.md`, `STATE.md`, `founder-messages/`, `founder-decisions.tsv`, `studies/proposals/questions.md`, or `register/`. This brief gives you the founder's decisions you need.

## The founder's decisions that bind the draft

- **The guard.** No arrangement that holds sellers' money through Sharrwah goes live anywhere without the founder's decision, whether Sharrwah itself holds it or a payment company holds it in an account opened through Sharrwah.
  - It limits only what goes live. It neither requires the design to provide for either arrangement nor rules one out.
  - Where your proposal provides for one, say so, and that it goes live only by the founder's decision.
- **The pilot's Decisions 1 to 14 are deferred.** They stay open and bind nothing, not even for one country. Q5's draft frames Decisions 1 to 13 again, and Q7's draft Decision 14, from the question's records (section 8 below).
- **The areas' marks.** An area marked `won't do` is outside Sharrwah: propose nothing for it, though its evidence may still show how the platforms handle your question. `must do`, or no mark, means the area is in.

## Order of work

1. Read your question, its `depth.tsv` rows, and the five accounts.
2. In your scratch directory, for each sentence: what each platform shows, which points match across platforms and on which basis, and where they differ.
3. Choose what your proposal will rest on, look up those ids, and read their quotes and dates.
4. Read the areas list for your question's areas, with their marks.
5. Read the Yemen digest whole. List the facts that bear on what you propose, and look up those you will use.
6. For Q5 and Q7, read the pilot's pieces above.
7. Write `draft.md` and `notes.md`, run the checker, and fix what it reports.

## `draft.md`

Headed `# <question>: <its title>, a draft proposal`, with these sections, in this order:

### 1. How the platforms handle it

- One subsection for each of the question's sentences, headed by its number, as `### [2]`. Two sentences answered together share one heading, as `### [1] [2]`.
- For each sentence: what each platform does, in its own terms; where platforms match, and on which basis (below); where one differs or goes beyond the others; and where a platform's reading didn't show it.
- **A point a check lists as not checked** says so: "not checked on Zid". It cites the ids of the platforms that show it.
- Keep it to what the proposal needs. The accounts hold the rest, and the coordinator reads them too.

### 2. Proposed: names, structure and behaviour

- Each element Sharrwah would have: its proposed name in **bold** and in English, what it is, and how it behaves.
- For each: the platforms' things it draws on, with their ids; what it takes from each, where it combines them; and why, by the rules under "Proposing" below.
- Where the platforms differ on it, the alternative not taken, and why.

### 3. What can plug in, what is set per what, and who sets it

- What can plug in: providers, apps, methods or anything else the evidence shows plugging in.
- What is set per what: per store, per country, per plan, per product, or whatever level the evidence supports, with no level fixed in advance.
- Who sets each: the seller, Sharrwah, a provider, or another party the evidence names.

### 4. Parts, in the order they can be built

- The parts the design divides into, each with what it needs built before it.
- A part needs no id where it only builds on elements of sections 2 and 3: name them instead.

### 5. What the design must keep open

- What the records don't settle and would be expensive to change later, and what depends on a company decision or on the founder: what the design must keep open for each, and what would settle it.

### 6. Yemen: what its evidence allows, forbids or doesn't show

- For each element of sections 2 and 3 that Yemen's evidence bears on: whether it allows it, forbids it, or doesn't show it, at which places, and as of which dates (below).

### 7. Company decisions it raises

- Each company decision the question's evidence raises: where the company is based, which providers and partners Sharrwah works with, any licence, who may register, or any other. For each: the question in one line, and the ids bearing on it. Don't recommend: the coordinator does.

### 8. The pilot's decisions (Q5 and Q7 only)

- Q5: Decisions 1 to 13. Q7: Decision 14. For each:
  - the question in one line, from the entry;
  - what your question's records show for it, cited by their ids. The pilot's statements are among Q5's copies, as `P` ids, and are cited by those ids, never by the entry;
  - whether sections 2 to 5 settle it, keep it open, or leave it to the founder or a company decision;
  - how the pilot's open findings bear on it, where they do.
- The entry is the coordinator's earlier framing, which the founder deferred. Its questions and options may frame yours. Its recommendations bind nothing, and nothing in it is evidence.

## Rules

### Citing

Everything your draft cites gets checked after you: each fact against its source; each not-found or absent row by a fresh search and an audit; each Yemen fact against its quotes; and each "Yemen's evidence doesn't show" by a search and an audit. So cite what your proposal rests on, and only that.

- **Every point ends with the ids it rests on,** as the accounts' points do. A point is a list item or a paragraph. There are two exceptions: a part in section 4 that only builds on elements of sections 2 and 3, and a point in section 6 that says only what Yemen's evidence doesn't show.
- **Cite the one or two ids that show a point best,** not every id an account gives for it.
- **How much to cite,** in distinct ids:
  - the platforms' statements, copies and citations: at most about 45 (Q5, about 70);
  - not-found rows, copied gaps and pilot absences: at most about 7 (Q5, about 10);
  - Stage 1's ids: at most about 8 (Q5, about 12).

  Past these, the checker warns. Say in `notes.md` why you needed more.
- **Cite a not-found row or copied gap** only where your proposal rests on a platform not showing something. Otherwise leave the point out.
- **"Absent"** only where an `absent` not-found row or a pilot absence (`A` id) says so. Anything else a reading didn't show is "not in what was read".
- **Records that disagree:** cite both, each with its date, and say which, if either, the proposal rests on.
- **Areas** (`A-01` and so on) may be named. They are the coordinator's grouping, never evidence of what a platform does.

### The platforms' own words

- **Name each platform's things in its own words,** as its records give them.
- **Quotation marks and backticks** are kept for the platforms' and Stage 1's own words, copied exactly from a record the point cites. The checker finds each in the cited records.
- **Arabic** appears only as the platforms' or Stage 1's own words, copied exactly from a record the point cites. The checker checks it the same way.
- **Your own words** for what a platform does are plain descriptions, never another platform's term.
- **Sharrwah's proposed names** are in bold, never in quotation marks.

### Comparing platforms

Two platforms' things match only on one of these bases, each shown in the platforms' own words:
1. the same term, used by both for what the question's sentence asks about, a platform's own translation counting as its term;
2. the same identifier, such as a key, scope, topic or entitlement;
3. the same definition, both quoted;
4. the same role in what the question asks, each by its own words.

Name the basis where you say two platforms match. A word both use for different things is no basis. A partial overlap is recorded as such.
- **One party on every platform:** the merchant, the buyer, and the platform itself, which includes its own name, its payment product and its company. Salla naming Salla and Zid naming Zid name the same party. Any other party, such as Stripe, is the same only by name.
- **"No part":** a statement that a party has no part names no one filling the role, but shows that this party isn't in its platform's set.
- **Like with like:** compare what platforms declare (their docs, help, terms, pricing pages or shipped code) with what others declare, and what was observed in a store with what was observed. `python3 -I method/source_kinds.py <source>` gives a source's kind. Where a comparison mixes them, say so.

### Proposing

The proposal follows these rules, and says which one each choice rests on:
1. **Built once, set up for each country it serves** (product line engineering: Pohl, Böckle & van der Linden 2005). What differs between countries is set up, not built apart.
2. **Hide what is likely to change** (Parnas 1972). Each choice likely to change sits behind its own part, so that changing it doesn't change the rest.
3. **Effort follows risk** (Fairbanks 2010; Boehm 1988). Decide now what would be expensive to change after launch: money flows, legal structure, the data model, and partner contracts. Leave the rest to the build, with one line each.
4. **The last responsible moment** (Poppendieck & Poppendieck 2003). Where the records don't settle a choice that is expensive to change, keep it open, and say what the design must keep open for it (section 5).

- **No level or setter is fixed in advance.** Where each thing is set, and who sets it, come from what the platforms show. Where they differ, say which you follow and why.
- **Don't rank the platforms.** Say what each does, and which you follow and why, by the rules above.

### Money

- **The flow ends** at the payout to the merchant's own bank account.
- **A wallet is in the flow** when its own words say it holds the merchant's sales proceeds before that payout. Where the wallet itself is the answer, the statement must say so. One whose words say only that it holds top-ups for the platform's services is outside it.
- **A time, condition, fee or deduction** acting on an in-flow wallet's funds counts like any other.
- **The guard** above applies wherever your proposal touches sellers' money.

### Yemen

- **Each Yemen fact you use** cites its axis or constant id, with the part you use (the state and its place) and its date, as "YA-01 (YER 533 @ Sana'a, as of 2026-10-08)".
- **Stage 1's rules for reading a state,** in the digest, hold: a condition's states are alternatives; a state's place is the scope its source gives it; only a state whose source says it holds in all of Yemen supersedes states at other places; a proposed state is never today; each part of today is read with its date.
- **The frame:** the merchant sells in the Yemeni market. A platform's condition naming only countries or regions is checked against that.
- **"Allows", "forbids" and "doesn't show"** each name the places and dates they hold for. Where no fact bears, write "Yemen's evidence doesn't show", with what would show it. Never infer.
- **Other countries** wait until the founder decides to enter them. Propose nothing particular to a country other than Yemen, beyond what the design keeps open for any country.

### Law

- **Quotes only.** A platform's terms show what that platform requires of its sellers, never what any law requires of Sharrwah.
- Sharrwah's own legal position is a company decision, for the founder with a lawyer. Raise it in section 7.

### No inference

- Say nothing about what a platform does beyond what its records show.
- Each proposal is marked as Sharrwah's proposed design, never as what a platform does.
- Notes record what you read, what the records don't show, and problems: never inference.

### Length

- About 5,000 words, not counting ids (Q5, about 7,000). Section 1 takes at most about half.

## Files, in your folder

- **`draft.md`,** as above.
- **`notes.md`:**
  - what you read: the accounts, the ids you looked up, the areas, the digest, and for Q5 and Q7 the pilot's pieces;
  - under "What the records don't show": each thing your proposal needed and no record gives, with what would show it;
  - anything past the citing limits, and why;
  - problems with this brief or the tools.

Write working copies in your scratch directory, never in the repository.

## Before you finish

Run `python3 -I method/check_proposals.py drafts <question>`, and fix every error. It checks:
- the sections, in order, and section 1's subsections for the question's sentences;
- that every point cites an id, but for the two exceptions under "Citing", and that each id exists among your question's records, Stage 1's files, the pilot's variation points or the areas;
- that each quoted word, each word in backticks and each run of Arabic is found in a record the point cites;
- that "absent" rests on an absent row or a pilot absence;
- the citing limits and the length, as warnings.

Then report in a few lines: the ids cited, by kind; the length; what the checker reports; and anything in this brief or the tools that got in your way.
