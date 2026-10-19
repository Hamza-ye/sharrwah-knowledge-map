# Brief: one question's draft proposal (step R4)

**Status: revised after its check (`studies/proposals/checks/R4-drafting-brief-check.md`), and for the founder's decisions of 19 October 2026: no marks on the areas list, and citing counts that are a guide, not a limit.**

You are one agent with one task: the draft proposal for one question. The message that started you names the question and a scratch directory. Your folder is `studies/proposals/drafts/<question>/`. You run at `max` effort.

## What the draft is for

- **Sharrwah** is a commerce platform for sellers. It is to be built once and set up for each place it serves. What a place is, and the level at which things differ between places, come from the evidence. Yemen is the first place it serves, not its design target.
- **Five platforms** were read for your question: Shopify, Salla, WooCommerce, Zid and BigCommerce. Some were read in depth; the others were checked only for what differs from the in-depth ones or goes beyond them.
- **Your draft** says how the five handle the question, and proposes Sharrwah's model for it, from their evidence: enough to start the design of Sharrwah's first build.
- **The coordinator** finishes the proposal from your draft, and owns its recommendation. The founder accepts or changes it. Your draft decides nothing.

## Read only

1. **Your question:** its section in `studies/proposals/questions-for-agents.md`. Its sentences are numbered in square brackets. Use those numbers.
2. **Which platforms were read in depth:** your question's rows in `studies/proposals/areas/depth.tsv`.
3. **The five accounts:** `studies/proposals/records/<question>/<platform>/account.md`. Read the in-depth ones first, in `depth.tsv`'s order, then the checks.
   - Each account says what its platform shows for the question, in its own terms, and each point ends with the ids it rests on.
   - A check's points carry labels. "the same" and "differs" name the in-depth points they match, and the basis; "goes beyond" matches none; "not in what was read" is an in-depth point the check's reading didn't show.
4. **The records behind the accounts,** by id: `python3 -I method/record_ids.py <id> [<id> ...]` prints each id's row and the quotes it rests on, with each source and its date. Look up what your proposal will rest on, and wherever an account point is unclear.
   - From each platform's `notes.md`, read only its lists of account points not checked, and of copies found wrong or out of date.
   - For Q5 and Q7, to find a pilot statement no account cites, search your question's `copied-view.tsv` files with `grep -F` for a term, and read only the lines it prints.
5. **The areas list:** in `studies/proposals/areas/areas.md`, the areas whose questions include yours (for Q8, every area). They show what each platform files where, in its own names.
6. **Yemen's evidence:** `studies/proposals/yemen-digest.md`, read whole once, after you have written sections 1 to 5, and Stage 1's rows by id with `record_ids.py`.
7. **For Q5 and Q7 only,** the pilot's variation points named under section 8 below: in `studies/subjects/S-01/variation-points.tsv`, only their `vp_id`, `question` and `x_words` columns.

**Earlier words, not evidence.** `depth.tsv`'s reasons, the text of `areas.md`, and the copies' working fields that `record_ids.py` prints, such as `placement`, `bullet` and `conditions`, are the coordinator's or earlier runs' words. They are never evidence, and never the basis for a level or a setter.

Read nothing else: not the platforms' own pages or files, other questions' records, `PLAN.md`, `STATE.md`, `founder-messages/`, `founder-decisions.tsv`, `studies/proposals/questions.md`, `register/`, or anything else in `studies/subjects/`. This brief gives you the founder's decisions you need.

## The founder's decisions that bind the draft

- **The guard.** No arrangement that holds sellers' money through Sharrwah goes live anywhere without the founder's decision, whether Sharrwah itself holds it or a payment company holds it in an account opened through Sharrwah.
  - It limits only what goes live. It neither requires the design to provide for either arrangement nor rules one out.
  - Where your proposal provides for one, say so, and that it goes live only by the founder's decision.
- **The pilot's Decisions 1 to 14 are deferred.** They stay open and bind nothing, not even for one place. Q5's draft frames Decisions 1 to 13 again, and Q7's draft Decision 14, from the question's records (section 8 below).
- **The areas list.** The founder marked no area: all 34 areas are in Sharrwah. When each part is built is decided in the design, not in your draft.

## Order of work

1. Read your question, its `depth.tsv` rows, and the five accounts.
2. In your scratch directory, for each sentence: what each platform shows, which points match across platforms and on which basis, and where they differ.
3. Choose what your proposal will rest on, look up those ids, and read their quotes and dates.
4. Read the areas list for your question's areas.
5. Write sections 1 to 5, and 7.
6. Read the Yemen digest whole, once. List the facts that bear on the elements of sections 2 and 3, look up those you will use, and write section 6. Where a fact changes what the design must keep open, add it to section 5.
7. For Q5 and Q7, read the decisions under section 8 and their variation points, and write section 8.
8. Write `notes.md`, run the checker, and fix what it reports.

## `draft.md`

Write the headings exactly as these, with the title at level 1, the sections at level 2, and section 1's subsections at level 3:

```
# <question>: <its title>, a draft proposal
## 1. How the platforms handle it
### [1]
## 2. Proposed: names, structure and behaviour
## 3. What can plug in, what is set per what, and who sets it
## 4. Parts, in the order they can be built
## 5. What the design must keep open
## 6. Yemen: what its evidence allows, forbids or doesn't show
## 7. Company decisions it raises
## 8. The pilot's decisions
```

Section 8 is for Q5 and Q7 only. Each list item is a point of its own, and a sub-item too.

**1. How the platforms handle it.**
- One subsection for each of the question's sentences, in order, headed by its number, as `### [2]`. Two adjacent sentences answered together share one heading, as `### [1] [2]`.
- For each sentence: what each platform does, in its own terms; where platforms match, and on which basis (below); and where one differs or goes beyond the others.
- Where your proposal rests on a platform's reading not showing something, say so, citing its not-found row or copied gap.
- A point a check lists as not checked says so, as "not checked on Zid", and cites the ids of the platforms that show it.
- Keep it to what the proposal needs. The accounts hold the rest, and the coordinator reads them too.

**2. Proposed: names, structure and behaviour.**
- Each element Sharrwah would have: its proposed name in **bold** and in English, what it is, and how it behaves. The element's own line ends with its ids, not only its sub-items.
- For each: the platforms' things it draws on, with their ids; what it takes from each, where it combines them; and why, by the rules under "Proposing" below.
- Where the platforms differ on it, the alternative not taken, and why.

**3. What can plug in, what is set per what, and who sets it.**
- What can plug in: providers, apps, methods or anything else the evidence shows plugging in.
- What is set per what: the level at which each thing is set, as the evidence supports it, with no level fixed in advance.
- Who sets each: the seller, Sharrwah, a provider, or another party the evidence names.

**4. Parts, in the order they can be built.**
- The parts the design divides into, each with what it needs built before it.
- A part needs no id where it only builds on elements of sections 2 and 3: name them, in bold, instead.

**5. What the design must keep open.**
- What the records don't settle and would be expensive to change later, and what depends on a company decision or on the founder: what the design must keep open for each, and what would settle it.

**6. Yemen: what its evidence allows, forbids or doesn't show.**
- For each element of sections 2 and 3 that a Yemen fact bears on: whether the fact allows it or forbids it, at which places and as of which dates, citing the fact (below).
- Write "Yemen's evidence doesn't show" only where an element's set-up for Yemen depends on a fact the digest doesn't give, with what would show it.

**7. Company decisions it raises.**
- Each company decision the question's evidence raises: where the company is based, which providers and partners Sharrwah works with, any licence, who may register, or any other. For each: the question in one line, and the ids bearing on it. Don't recommend: the coordinator does.

**8. The pilot's decisions** (Q5 and Q7 only).
- **The decisions,** each with its variation point:
  - Q5: 1, who holds the merchant's funds (S01-VP-01); 2, who settles the funds to the merchant (S01-VP-02); 3, who sends payouts to the merchant's bank account (S01-VP-03); 4, who collects the buyer's payment (S01-VP-04); 5, whether the platform acts as the merchant's agent (S01-VP-06); 6, who deducts fees, refunds and other amounts owed (S01-VP-09); 7, which accounts a merchant holds (S01-VP-11); 8, payout timing (S01-VP-15); 9, deducted before payout, or billed apart (S01-VP-19); 10, funds held when the service ends (S01-VP-20); 11, when funds go back to the buyers (S01-VP-21); 12, a security interest over the merchant's funds (S01-VP-10); 13, when the merchant is paid under installments (S01-VP-22).
  - Q7: 14, the currency in which a merchant's funds are held, if anywhere, and paid out (S01-VP-23).
- **For each decision:**
  - the question in one line, in your own neutral words: who or what fills the role, and at what level, presuming no holder and no level;
  - what your question's records show for it, cited by their ids. The pilot's statements are among your question's copies, as `P` ids;
  - whether sections 2 to 5 answer it, keep it open, or leave it to the founder or a company decision.

  Each of these points cites the decision's variation point, and the second its records too.
- **Two open findings of the pilot's review** bear on these:
  - a statement that names only what doesn't fill a role names no one filling it (the "no part" rule below). One of the pilot's earlier readings of Zid on currency rests on such a statement: Zid's list of currencies that can't be withdrawn from its wallet. Rest no reading on such a statement;
  - whether WooCommerce's policy pages count among its terms is open. Where your draft rests on one, say so.
- Earlier framings of these decisions, and the recommendations made on them, are the coordinator's. They reach the proposal when the coordinator finishes it, not your draft.

## Rules

### Citing

Everything your draft cites gets checked after you: each fact against its source; each not-found or absent row by a fresh search and an audit; each Yemen fact against its quotes; and each "Yemen's evidence doesn't show" by a search and an audit. So cite what your proposal needs, and nothing it doesn't rest on.

- **Every point ends with the ids it rests on,** as the accounts' points do. A point is a list item or a paragraph. The exceptions: a part in section 4 that only builds on bold elements of sections 2 and 3; a point in section 6 that says only what Yemen's evidence doesn't show; and in section 8, a decision's variation point counts as an id.
- **Cite the one or two ids that show a point best,** not every id an account gives for it.
- **How much to cite: a guide, not a limit** (the founder's decision of 19 October 2026). A draft usually needs about:
  - the platforms' statements, copies and citations: 40 distinct ids (Q5, 60);
  - not-found rows, copied gaps and pilot absences: 7 (Q5, 10);
  - Yemen facts, each an axis or constant at one place: 8 (Q5, 12);
  - "Yemen's evidence doesn't show": 2 (Q5, 3).

  Cite what your proposal needs, past these where it needs more. The checker counts them as notes. Say in `notes.md` where you went past them, and for what.
- **Not found.** Cite a not-found row or copied gap only where your proposal rests on a platform's reading not showing something. A point that says a reading didn't show something always cites one. Otherwise leave the point out.
- **"Absent"** only where an `absent` not-found row or a pilot absence (`A` id) says so. Anything else a reading didn't show is "not in what was read".
- **Records that disagree:** cite both, each with its date, and say which, if either, the proposal rests on.
- **A copy found wrong or out of date** in a platform's `notes.md`: rest no point on it. Cite the statement that corrects it, or both, as records that disagree.
- **Areas** (`A-01` and so on) may be named. They are the coordinator's grouping, never evidence of what a platform does.
- **Never cite** the pilot's entry, its variants (`S01-V-` ids), its statements by their pilot ids, or any file under `studies/subjects/`, `register/` or `founder-messages/`. The checker rejects them.

### The platforms' own words

- **Name each platform's things in its own words,** as its records give them.
- **Quotation marks and backticks,** double, single or angled, go only around words that stand together in a record the point cites, copied exactly, with no ellipsis. The checker finds each in the cited records. Ids are never quoted.
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
- **Like with like:** compare within one kind of source, as `python3 -I method/source_kinds.py <source>` gives it: observed, shipped, stated or official page. Where a comparison mixes kinds, name them.

### Proposing

The proposal follows these rules, and says which one each choice rests on:
1. **Built once, set up for each place it serves** (product line engineering: Pohl, Böckle & van der Linden 2005). What differs between places is set up, not built apart.
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

- **Each Yemen fact you use** cites its axis or constant id, followed in brackets by the part you use (the state and its place) and its date, such as YA-01 (YER 533 @ Sana'a, as of 2026-10-08).
- **Stage 1's rules for reading a state,** in the digest, hold: a condition's states are alternatives; a state's place is the scope its source gives it; only a state whose source says it holds in all of Yemen supersedes states at other places; a proposed state is never today; each part of today is read with its date.
- **The frame:** the merchant sells in the Yemeni market. A platform's condition naming only countries or regions is checked against that.
- **"Allows" and "forbids"** each name the places and dates they hold for. "Doesn't show" is written as section 6 says. Never infer.
- **Places other than Yemen** wait until the founder decides to enter them. Propose nothing particular to one of them, beyond what the design keeps open for any place.

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
  - what you read: the accounts, the ids you looked up, the areas, the digest, and for Q5 and Q7 the variation points;
  - under "What the records don't show": each thing your proposal needed and no record gives, with what would show it;
  - where you cited past the guide's counts, and for what;
  - problems with this brief or the tools.

Write working copies in your scratch directory, never in the repository.

## Before you finish

Run `python3 -I method/check_proposals.py drafts <question>`, and fix every error. It checks:
- the sections, in order, written as above, and section 1's subsections for the question's sentences;
- that every point cites an id, but for the exceptions under "Citing"; that each id exists among your question's records, Stage 1's files, the pilot's variation points or the areas; that no id is another question's; and that nothing the rules above forbid is cited;
- that each quoted word, each word in backticks and each run of Arabic is found in a platform's or Stage 1's record the point cites;
- that a point saying a reading didn't show something cites its not-found row or copied gap, and that "absent" rests on an absent row or a pilot absence;
- as warnings: each Yemen fact's date, and the length; as notes: the counts past the citing guide.

Then report in a few lines: the ids cited, by kind; the length; what the checker reports; and anything in this brief or the tools that got in your way.
