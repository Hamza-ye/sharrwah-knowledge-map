# SH-104: the scope picker's API labels, placed by script

**What the batch is.** 62 entries of Shopify's `dev-dashboard-scopes`: the labels the Dev Dashboard's scope picker lists under each resource heading, naming the API that grants its scopes ('Admin API; parent: Orders'). `method/held_scope_apis.py --cut` took them out of SH-24, whose agent placed the headings.

**The rule.** A label takes its heading's lines (SH-23's R23.10; the Editions digest's E157), the API its term. One heading entry can stand for the heading under several APIs, since the structure makes one entry per distinct text, so a label takes the heading's lines whose reading names its own API's item (SH-24's R24.1); a heading whose lines name no API gives every label all its lines.

## The coordinator's check (31 October 2026, the script's batch)

- **The checker passes** on all 62 entries, once SH-23 and SH-24 were checked.
- **The routing:** SH-24 found that 7 of its headings, and 4 of SH-23's, stand for headings under two or three APIs. Its lines name each API's item; SH-23's four (Companies, Customer, Draft Orders, Checkouts) read only the Admin API's, so the check added their other items' lines to SH-23, by the model's placements of those scopes (SH-S-5913, SH-S-5926, SH-S-5914, SH-S-6164), and named the Storefront API's Checkouts and the Customer Account API's Draft Orders on their one line each, which the checker allows once per capability.
- **Cost:** the script, no agent.
