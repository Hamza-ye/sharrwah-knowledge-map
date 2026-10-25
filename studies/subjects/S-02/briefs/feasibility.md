You are testing whether one capability map can be built from two commerce platforms' own machine-readable structures. This is a read-only feasibility test, timeboxed to about an hour of work. Work only from this brief and the files it names.

## Rules
- Never `cd` into, or run code from inside, /home/user/observed-sh or /home/user/observed-sa. Read their files by absolute path, and run Python only with `python3 -I`, with scripts kept outside those folders.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence. Never skip or mask it.
- Write only the one output file named below. Commit nothing.

## The sources
- **Shopify:** `/home/user/observed-sh/`. Read `README.md` and `structures/README.md` first. `structures/REGISTER.tsv` lists every structure. The ones to start from are under `structures/shopify/`:
  - the admin navigation (`admin-main-nav`, `admin-settings-nav`, `admin-route-titles-en`, `admin-router`);
  - the permission tree and roles (`admin-permission-tree`, `admin-roles`, `admin-role-permissions`, `admin-assignable-permissions`);
  - the webhook topics (`admin-webhook-topics`);
  - the admin GraphQL schema (`admin-graphql-schema`, `admin-graphql-reference-nav`).
- **Salla:** `/home/user/observed-sa/`. Read `README.md` and `docs/READING.md` first. The structures to start from are under `structures/salla/`:
  - the dashboard navigation (`dashboard-nav`, `dashboard-main-navigation`, `dashboard-settings-menu`, and the `dashboard-menu-*` files);
  - the staff roles and permissions (`dashboard-staff-roles`, `staff-permission-groups`);
  - the events (`dashboard-webhook-events`, `docs-event-lists`);
  - the data schemas (`docs-dataschemas`) and the API operations (`docs-operations`).
- **The areas:** `/home/user/sharrwah-knowledge-map/studies/proposals/areas/areas.tsv`, 34 areas. Its `platform_area_ids` column shows how each area was drawn from the platforms' own groupings.

## The question
Can each of the 34 areas be filled, from these structures, with four things for each platform?
- **capabilities:** navigation nodes, API resource types or operations;
- **roles:** the permissions that gate them;
- **interactions:** the events or webhook topics they emit;
- **a key** that joins the two platforms' entries, or else the reason a hand mapping is needed.

## How
1. Survey the structures' formats: what each file holds, how big it is, and whether it carries ids, names or paths that could serve as keys.
2. Sample five areas: A-01 (accounts, stores and staff), A-04 (products and inventory), A-09 (orders), A-11 (how buyers pay) and A-24 (apps). For each, list what each platform's structures give under the four headings above, with file paths and a few example entries. Then judge whether a join is mechanical (shared names or a crosswalk), partly mechanical, or manual.
3. From the sample, estimate the effort to fill all 34 areas. Say which structures carry most of the value, and which add little.

## Output
Write `/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/s02-feasibility.md`. Include:
- the survey;
- the five sample areas, with paths;
- your judgement: feasible, partly feasible, or not, and why;
- what a full map would take, in hours of agent work;
- the risks, such as structures that are stale, partial or ambiguous.

State facts with their file paths. Mark your own estimates as estimates.

Then reply in at most 12 lines.
