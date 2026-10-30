# The class's model: what each run taught

**What this file is:** the lessons of each run of Stage 4A, the class's model, about running the agents and planning the work (`PLAN.md`, Stage 4: "Each run's lessons"). Costs are agent tokens, counted by `method/count_tokens.py` over each agent's transcript.

## 1. The brief's inspections (30 October, 23:53 to 00:46 UTC)

- **The inspection** of `briefs/B-extent.md` (19.8 million, 95 requests) found 19 problems, 13 of them must fix. As written, the dry run would have produced wrong rows: a WooCommerce part with no domain to stay within, false "nothing held" cells from coarse concerns, placements with no test, rows no checker could test.
- **The re-inspection** of the rewrite and its two new scripts (21.7 million, 46 requests) resolved 17 of the 19 and found 16 new problems. Seven were checker faults that would have let wrong rows pass a part's own check. The inspector found them by running the scripts on fixtures it built, and on faulty copies of those.
- **Lesson:** an inspector that runs the scripts finds what reading the brief can't. Ask for it in every inspection of a brief that comes with scripts.
- **Lesson:** most new problems came from the fixes, as inspection A found before (`inspection-A.md`, "The coordinator's disposition"). A re-inspection after a large rewrite is worth its cost. A fix the inspector specified exactly can be applied, then tested on the inspector's own fixtures, without a third round.

## 2. The scope part (01:00 to 01:09 UTC)

- **3.8 million, 27 requests,** for all 652 concerns. One agent read compact output (each concern's name, terms, `where` identifiers and Q1 matches) and wrote the file platform by platform.
- **Lesson:** a judgment over many small items costs little when the script prints only what the judgment needs. The scope part recorded an area in nearly every reason, which lets domain C be split by area without another run.

## 3. The review brief's inspection (01:10 to 01:30 UTC)

- **9.1 million, 60 requests:** 15 findings, 10 must fix. Two reached beyond the review:
  - Arabic search: a broken plural isn't a substring, and ة against ه missed matches. The search now reads ة as ه and ى as ي, and the briefs ask for singular and plural.
  - `own-service` on a brand-named product: a brand in a product's name doesn't name its maker.

  Both were sent to the running `B-anchor` by message, and it applied them.

## 4. B-anchor (01:07 to 01:46 UTC)

- **33.9 million, 122 requests,** for 22 concerns (Shopify 11, Salla 11): 25 capabilities, 50 cells, 220 evidence rows; its own check passed with 7 flags for the reviewer.
- **Where the cost went.** The context grew from about 86,000 tokens to 516,000. By quarter of its requests:

  | Quarter | Requests | Tokens | Mean context |
  | --- | --- | --- | --- |
  | 1 | 30 | 2.9 million | 96,000 |
  | 2 | 31 | 6.5 million | 210,000 |
  | 3 | 30 | 9.9 million | 331,000 |
  | 4 | 31 | 14.3 million | 462,000 |

  The last quarter cost five times the first, for the same number of requests.
- **Lesson,** as in S-02 (`studies/subjects/S-02/method-report.md`): a part's cost grows with the square of its length, since every request re-reads the whole context. So a part is cut small enough that its context stays under about 250,000 tokens: one area per part where a domain is large, and a fresh agent that continues from the files when a part runs long. By this part's own first half (9.4 million for 61 requests), two fresh agents doing half each would have cost about 19 million together, not 34.
- **What it read as `shows`:** Shopify's tags and taxonomy shown only through Shopify's own API scopes, where the brief counts the platform's "own API for its own feature" as `core`. This is one of the dry run review's checks.
