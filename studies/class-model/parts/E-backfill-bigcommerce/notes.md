# E-backfill-bigcommerce: notes

The back-fill after `E-bigcommerce`, which added two capabilities to domain E: CM-SFR-014, sites and routes of a headless storefront channel (under CM-SFR-011), and CM-CHN-007, several storefronts in one store, BigCommerce's Multi-Storefront (under CM-CHN-001). This part writes their cells for Shopify, Salla, WooCommerce and Zid: eight cells. It adds no capability and lands no concern. Besides `cells.tsv`, `evidence.tsv` and `notes.md` it writes `qualities.tsv`, for the one limit its cited statement gives.

`candidates --domain E --platform P --areas SFR,CHN` gave leads on BigCommerce's terms (Sites; Sites & Routes; store_sites; MSF; Multi-Storefront; Storefronts). They settled no cell alone, so each cell was searched for the thing itself, in English and, for Salla and Zid, in Arabic, singular and plural, with and without ال. The terms are in each cell's `searched`.
- **CM-SFR-014:** a headless storefront's site, its domain and its routes, registered with the platform.
- **CM-CHN-007:** more than one storefront run from one store's catalogue, orders and admin. Kept apart from domain A's CM-ACC-003 (several stores under one owner) and from CM-MKS-001 (Markets: a version of the store for the buyers of a place).

## The cells

| cap | Shopify | Salla | WooCommerce | Zid |
|---|---|---|---|---|
| CM-SFR-014 | none-held | none-held | none-held | none-held |
| CM-CHN-007 | statements (core, a reading) | none-held | none-held | none-held |

### CM-SFR-014: none-held on all four

- **Shopify.** No statement names a headless storefront's site, domain or routes. "Deploy your Hydrogen app to Oxygen, Shopify's global edge hosting platform" (SH-C-139/where/SH-S-0710) is hosting of the headless app, cited in CM-SFR-011; it doesn't say what site or domain the storefront is served at, or that its routes are registered with Shopify, so it isn't cited here (a reading). The domain statements are the store's domains (SH-C-033, CM-SFR-008) and Markets' local domains and web presences (SH-C-106, SH-C-110, SH-C-111, SH-S-7061, SH-S-7458), domain E's CM-MKS area, and none names a headless storefront.
- **Salla and Zid.** Neither has a cell in CM-SFR-011 (headless and custom storefronts); both are none-held there. Their hits are موقع as a website or a place, Shipping Routes (Salla, domain C), flags whose names are all they state, and the store's own domain.
- **WooCommerce.** The Store API's own REST routes (WC-S-0081, cited in CM-SFR-012) are an API's routes, not a storefront's site or page routes, a reading. "Sites" in its statements are WordPress installations using Woo.
- For every platform but BigCommerce, what a site and a route are isn't stated: BigCommerce's statement (BC-S-0231) gives the API group, not a definition, as CM-SFR-014's note says.

### CM-CHN-007: Shopify held, the others none-held

- **Shopify, core, a reading.** The plan row "Build headless storefronts" gives 1 on Basic, Grow and Advanced and 25 on Plus (SH-C-139/decides/SH-S-7056). This part reads the number as how many headless storefronts the store's plan includes: up to 25 storefronts of one store on Plus. That is the same shape as BigCommerce's plan line Multi-storefront, which gives added storefronts and a maximum per plan (BC-S-0228). It is a join on role, a reading: BigCommerce's term is Multi-Storefront; Shopify's statement names only headless storefronts and a count. The statement doesn't say the storefronts share the store's catalogue, orders and admin; that they belong to one store rests on the plan table being a store's plan. If the reviewer reads the number otherwise, the cell becomes `none-held` with the terms searched: MSF; Multi-Storefront; Multi-storefront; Storefronts; multiple storefronts; multi-storefront; multistore; multi-store; additional storefront; another storefront; more than one storefront; several storefronts; storefront per. The quality "Headless storefronts per plan" repeats E-anchor's on CM-SFR-011, since the limit bears on both.
- Not cited for Shopify: the Headless channel's scope lines (SH-S-6152, SH-S-6157, SH-S-6159, SH-S-6162), which name one channel; Agentic Storefronts (SH-C-140, domain F), selling through channels operated by Shopify or partners; the app category Storefronts - Other (SH-I-1939); and storefronts in general (SH-S-0305). Shopify's organization and its stores (CM-ACC-003) and Markets (CM-MKS-001) are kept apart.
- **Salla.** The released flag multi-stores (SA-C-003/decides/SA-S-3085) is several stores linked to one account: `scope.tsv` gives SA-C-003 domain A, and A-anchor cites it in CM-ACC-003. Kept apart.
- **WooCommerce.** WordPress multisite and its network (network-orders, WC-S-0089; Blueprint's network-wide settings, WC-S-5448, WC-S-5450, cited in CM-MIG-006) are several sites; no statement says they share one store's catalogue or orders, so they are not read as several storefronts of one store. Kept apart, a reading.
- **Zid.** "Orders can be created either by the customers from the storefronts or by the merchants from their dashboard" (ZD-S-0906, domain C) is read as the storefronts of the stores the API serves, in general terms, not several storefronts of one store.

## The checker's flags

- **SH-C-139/decides/SH-S-7056 is cited by CM-CHN-007 and CM-SFR-011, in two trees.** Yes. The row is a count of headless storefronts: what a headless storefront is belongs to CM-SFR-011, and that a store has 25 of them belongs to CM-CHN-007, a reading. Neither is the other's parent in the model (CM-SFR-011 is under no parent; CM-CHN-007 is under CM-CHN-001). By the convention on strained fits, E-anchor's landing of SH-C-139 in CM-SFR-011 now has a statement cited in another tree, so it would be `strained`; this part lands nothing, and leaves that to the coordinator. This also bears on CM-CHN-007's note, which says the coordinator may prefer area SFR for it: placed under CM-SFR-011 or beside it, the two cells would sit in one tree.
- **cells.tsv lines 2 to 5 and 7 to 9, none-held with matches.** Each cell's reading names its hits and why each isn't the capability. On Shopify's CM-SFR-014, the 88 matches are mostly domain, url and route statements: the store's domains (SH-C-033, CM-SFR-008), Markets' domains and web presences (SH-C-106, SH-C-110, SH-C-111), the Headless and Hydrogen admin routes (SH-S-5134, SH-S-5135, cited in CM-SFR-011), payment sessions, the lifecycle of a Shopify Function (SH-S-0683) and app categories; none names a headless storefront's site or routes.

## Problems

- The candidates use BigCommerce's terms only, in English, so on Salla and Zid they found one statement each. The cells rest on the searches above.
- Gap: no statement held on Shopify, Salla, WooCommerce or Zid defines a site or route of a headless storefront; and BigCommerce's own BC-C-040/decides is `page not read`.

## The coordinator's decisions (30 October)

- **SH-C-139 is `strained`** in CM-SFR-011, since its plan row SH-S-7056 is cited here in CM-CHN-007.
- **CM-CHN-007 stays under CM-CHN-001.** BigCommerce, the platform that gives it a place, runs its storefronts as channels (convention 6); a headless storefront on Shopify is one of the store's channels too. The reading that SH-S-7056 counts storefronts of one store is a join on role, for the final review.

