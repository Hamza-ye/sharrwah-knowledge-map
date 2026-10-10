# Shopify engineering evidence

Copies of the engineering sources on how Shopify built payments in relation to the rest of its platform. They cover architecture talks, engineering blog posts, developer docs on the payments contract, and three open-source repositories. They support the payment seam study (`studies/payment-seam/`). The rules in `evidence/yemen/README.md` apply here too: runs are never edited, each run states where it was fetched from, and sources dated before 2023 are historical.

That date rule matters most here. The detailed write-ups of Shopify's internal payment architecture date from 2019–2022. They show how Shopify was built then. The 2023–2026 sources cover adjacent topics: the PCI DSS v4 checkout, inventory reservations, the Universal Commerce Protocol, the Packwerk retrospective, and the current provider contract.

| Folder | What it holds |
| --- | --- |
| `finding-aids/20261010-shopify-engineering-sources.tsv` | The search agent's list of 40 sources, E001–E040, with dates and what each covers. Not evidence. |
| `runs/20261010T083026Z-engineering-sources/` | The 37 web sources (E001–E037), fetched raw and through a browser from outside Yemen on 10 October 2026. All 37 were captured. By date: 14 are from before 2023, 5 from 2023–2024, 9 from 2025–2026, and 9 are undated live pages. |
| `runs/20261010T083203Z-repositories/` | Three repositories pinned at a commit (E038–E040): Shopify/packwerk, Shopify/semian and activemerchant/active_merchant. See below for what was kept. |

## What was kept from each repository

- **Every repository:** its README, licence, changelog and full file list.
- **Packwerk:** also its usage and violation guides.
- **Active Merchant:** also the gateway base class and response class, plus the list of its 252 gateway adapters.

Commits and dates are in `repos.tsv`.
