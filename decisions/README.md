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
trigger: —                  # for a deferred record: what reopens it
date: 2026-10-24
---

# The question, in plain words

## Context and problem statement

## Decision drivers

## Considered options

## Decision outcome

Chosen option: "…", because …

## Consequences

## The guard

How the outcome passes `METHOD.md` section 3a: its type, what it varies by, and why no market's facts shape it.

## Confirmation

How we will know it works: the scenarios it must pass, and when it is reviewed.
```

**What the guard reads.** For a record whose outcome is Built:
- the "Decision outcome" and "Consequences" sections must name no market;
- its evidence must not come only from one market's Context ids.
