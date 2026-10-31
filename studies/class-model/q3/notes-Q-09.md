# Q3's check, batch Q-09: notes

Rows: km:SRF-01 to SRF-05, MIG-01 to MIG-03, EVO-01 to EVO-03, WLD-01 to WLD-05, INT-01 to INT-05 (21). The checker's last line: `21 of 21 rows placed; 0 problems`.

**Count by result:** covered 5, partly 7, beyond the class 9, candidate miss: held 0, candidate miss: not held 0 as a whole row (2 as a `rest`), unclear 0.
- covered (5): SRF-01, SRF-02, SRF-03, MIG-01, MIG-02
- partly (7): SRF-04, WLD-01, WLD-02, WLD-04 and INT-03, each with the rest beyond the class; EVO-01 and EVO-02, with the rest not held
- beyond the class (9): SRF-05, MIG-03, EVO-03, WLD-03, WLD-05, INT-01, INT-02, INT-04, INT-05

## Rows that were hard to place, and why

- **SRF-01 (the workspace's shape).** No capability is "the admin's navigation". A reading: the workspace's shape is the arrangement of the capabilities, not a capability of its own. The admin-navigation inventories land in each area's capabilities (Shopify's SH-I-0743 Orders in CM-ORD-001; WooCommerce's WC-I-0040 Home and WC-I-0044 Settings in CM-ONB-004), and Q1 left the containers out on purpose (`outscope`: Shopify's Home SH-I-0742 and Settings SH-I-0772, "container for the settings pages"; Salla's group headings such as SA-I-0771). Settings are CM-ACC-006, Home is CM-ANL-003. On admin search, Salla's settings search (SA-S-2087) is cited in CM-ACC-006@salla, and each list's search sits in its area (Salla's order_search, customer_search). No statement holds Shopify's admin-wide search (searched: admin search, global search, search the admin, command palette, Shopify admin navigation). I placed the row as covered, with the navigation tree as detail.
- **SRF-04 (UI conventions).** Bulk actions are capabilities' cells (CM-CUS-003, CM-CAT-001@shopify, CM-ORD-003@salla and @zid). The save bar, unsaved changes, validation, empty states and confirmations aren't a capability, and nothing is held for them. I placed them as Sharrwah's own admin design, `engineering:detail`, rather than as a miss. A reading: they are how an admin is built, not something the class does for a merchant.
- **SRF-05 (how each platform organises its offering).** I placed it as `plan`: the model's extent is itself this reconciliation (PLAN.md Stage 4A: Shopify's and Salla's grouping as the anchor, the others mapped onto it, from inventories of every self-description the row names), and the rebuilt Knowledge Map page shows it (founder-decisions 2026-10-30 GM).
- **EVO-01 and EVO-02 (change over time).** The model is the class at one capture. What a cell's statements already show is placed as covered: the API change logs (CM-API-006), experimental features (CM-EVO-001), and release states cited in cells (WooCommerce is_experimental, Blueprint (beta), Shopify's betas on admin routes, Salla's released and unreleased flags, BigCommerce's closed betas). What has changed, and how long a capability has been established, needs dated evidence. I placed that rest as `candidate miss: not held` because the material can be captured: the platforms' change records. A reading: it isn't a missing capability the way other misses are, since the thing missing is evidence over time, beside CM-API-006's API change log. The coordinator may prefer to route it as a capture request only, with no amendment to the model.
- **EVO-03 (earlier stages as a guide to sequencing).** I placed it as engineering's, since ordering is ordinary engineering (the founder's intent of 29 October) and the architecture plan orders areas by dependency. Marked `wrong party`: as worded, it asks the platforms' history to settle a sequence that engineering sets.
- **MIG-03.** Which merchants come first is the founder's. From which platforms a first market's merchants come is a market's fact that no subject covers. What the importers carry is `engineering:detail`. Because of that, its `when` is "at the area's build", which raises `wrong time` against `launch`.
- **WLD-05 (merchants' complaints).** No review or forum page is held, and complaints aren't a capability. I placed it as `subject:none`, from public sources only, since the founder rules out merchant interviews. Its `when` is `unclear` because `subject:none` gives no time.
- **INT-02 and INT-05.** I marked both `wrong party`: each asks for a decision that a decision in force already settles. For INT-02 it is what parity means (the intent of 29 October). For INT-05 it is whether resource limits rule out architecture choices (the scope decision of 28 October, the intent of 29 October).

## Candidate misses, with what was searched

No held miss. Two not-held rests:
- **EVO-01, rest:** each platform's own record of what it added, changed or removed, by area, with dates. Searched in English: changelog, change log, release notes, deprecated, deprecation, sunset, beta, developer preview, unstable, experimental, new feature. Searched in Arabic for Salla and Zid: جديد, تجريبي. `outscope` for beta, deprecat, changelog, release: only Shopify's legal section 9.10 Beta Services (SH-I-2418, left out by Q1). Salla's Change Log link is held (SA-S-1167, in CM-API-006@salla), but not its content. Material that would settle it: captures of Shopify's changelog and Editions pages, Salla's Change Log page, and Zid's and BigCommerce's developer changelogs. Also WooCommerce's release changelog, an assumption: that the held release 11.2.1 carries one; I didn't open it.
- **EVO-02, rest:** how long a capability has been established. Same searches and same material.

Subjects that no subject covers, for Stage 3's list (`subject:none`):
- MIG-03: the platforms a market's merchants sell on today.
- WLD-01: each market's e-commerce and consumer-protection law (disclosures, withdrawal and cooling-off, the platform's own duties).
- WLD-04: SMS and WhatsApp providers, and maps and address providers, per market.
- WLD-05: merchants' complaints in Sharrwah's markets, from public reviews and forums.

## Problems with the brief or the evidence

- None that stopped a row.
- The brief's `who_answers` for the founder lists "whether Sharrwah's own company runs a service". MIG-02's Salla migration service is placed own-service (CM-MIG-005@salla), and a migration service isn't on the founder's named list. I kept MIG-02 with the model alone, since it asks how the platforms help.
- The `beyond the class` categories don't name "the platforms' history" (EVO-01 to EVO-03). I placed it as described above.
