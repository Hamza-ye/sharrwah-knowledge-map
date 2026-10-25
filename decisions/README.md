# Decisions

This folder holds the work's decisions (`METHOD.md` section 4):
- **`subjects.tsv`:** the backlog, one row per subject;
- **`D-<nnn>-<short-name>.md`:** one decision record each, numbered in the order they are opened.

`method/decision_status.py` lists both by status. With `--guard`, it runs the market guard (`METHOD.md` section 3a).

## The backlog

| Column | What it holds |
| --- | --- |
| `id`, `subject` | The subject: one decision area, small enough to finish in about a day |
| `milestone` | The milestone that closes it, M0 to M8, or "set at S-02" for the areas whose order the spine sets |
| `areas` | The ids it covers from the 34 areas (`studies/proposals/areas/areas.tsv`). Each area belongs to one subject. |
| `km_areas` | The Knowledge Map areas whose questions it takes by default (`register/km-questions.tsv`). Each area belongs to one subject. |
| `covers` | Other questions it takes: Knowledge Map ids (`KM-…`) outside its own areas, the pilot's decisions, drafts, and the founder's restored decisions |
| `door` | One-way if it holds a founder decision, two-way otherwise |
| `risk` | H, M or L: the cost of getting it wrong |
| `needed_by` | When it is needed, in the Knowledge Map's terms: `spine`, `model`, `launch` or `later` |
| `arc42` | The architecture description's sections it fills |
| `status` | `open`, `in progress`, `waiting on the founder` or `closed` |
| `budget_m` | Its budget in millions of agent tokens, set at framing |
| `notes` | One line |

## A decision record

A record is never edited once it is accepted. A new record supersedes it, and both link to each other (`METHOD.md` section 10). The form is MADR 4's short form, with the fields `METHOD.md` section 4 adds:

```
---
id: D-001
title: the question, in plain words
subject: S-01
status: proposed            # proposed, accepted, deferred, under review, or superseded by D-nnn
door: one-way               # one-way: the founder's; two-way: engineering's
integrity: 3                # 1, 2 or 3 (METHOD.md section 6)
outcome: Built              # Built, Configured, Chosen or Context (METHOD.md section 3a)
varies_by: —                # for Configured or Chosen: what it varies by (market, plan, merchant)
risks: W-07                 # ids in risks.tsv
evidence: YK-131            # the ids it rests on
depends_on: —               # records whose outcomes it takes as given while they are not yet accepted (METHOD.md section 10)
trigger: —                  # for a deferred record: what reopens it
date: 2026-10-24
---

# The question, in plain words

## Context and problem statement

## Terms

The words this record relies on, each defined in the glossary (`architecture/12-glossary.md`) from the sources named there.

| Term | What this record relies on it to cover | Sources |
| --- | --- | --- |
| payment method | … | `observed-sh/…`; `observed-sa/…` |

## Scope

**Decides:**
- …

**Takes as given:**
- … (an accepted record, a founder decision in `founder-decisions.tsv`, or a record named in `depends_on`)

**Leaves open:**
- … — S-07. Carried: why every outcome S-07 could reach fits this record unchanged (or "Not carried: …", and the record stays proposed until S-07 decides)

## Decision drivers

## Considered options

## Decision outcome

Chosen option: "…", because …

## Consequences

## The guard

How the outcome passes `METHOD.md` section 3a: its type, what it varies by, and why no market's facts shape it.

## Evidence

The sources by id, each outside source with its type in the Knowledge Map's codes, for example "E031 (DECL)", and what that type can't tell where the record leans on it (`register/README.md`, "The source types").

## Confirmation

How we will know it works: the scenarios it must pass, and when it is reviewed.

**Gaps:** what isn't known that bears on the decision, the work that would close each gap, and when it is needed.
```

**What the guard reads.** For a record whose outcome is Built:
- the "Decision outcome" and "Consequences" sections must name no market;
- its evidence must not come only from one market's Context ids.

**Terms and Scope** (`METHOD.md` sections 4, 6 and 10; amendment 2). A record decides nothing outside its Scope, and uses each term only as far as its Terms row says. `method/decision_status.py` checks that:
- every record has both sections;
- each term in the Terms table is a heading in the glossary, and each row names its sources;
- each item under **Leaves open** names a subject in `subjects.tsv` (`S-nn`);
- each record in `depends_on` exists, and a record is not accepted before the records it depends on;
- each item under **Leaves open** says "Carried:" or "Not carried:", and an accepted record has no item "Not carried" (`METHOD.md` section 6's acceptance rule).

The checks of meaning are not a script's: at the record's level, each term is checked against the paths it cites, and each Scope item against what the record decides.

**Source types** (`METHOD.md` section 5: "Each source is weighed by the Knowledge Map's source types"). Each outside source a record cites, such as Shopify's engineering sources (`E001` to `E040`), has its type in the Evidence section: what it is good for, what it can't tell, and how far to trust it. A platform declaration (DECL) says what a platform intends, not that it behaves so; an engineering blog or talk (LIT) is one company's account. `method/decision_status.py` flags an outside source in the `evidence` field whose type the Evidence section doesn't give. The checker at levels 2 and 3 checks the type and how the record weighs it.

**The evidence standard** (`METHOD.md` section 6; amendment 3). Every claim in a record is a fact, with its source; an interpretation, marked as one (for example "*The coordinator's reading:* …"); or an assumption, marked as one, with what would confirm or refute it. A decision is not a claim: it needs reasons, not a source.
