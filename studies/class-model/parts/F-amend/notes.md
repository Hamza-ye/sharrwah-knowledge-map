# F-amend: capabilities made from the held pass

Written by the agent of `briefs/M-amend.md`, 31 October 2026, from the coordinator's decisions in `held/new.tsv` (N14, N15) and the facts, places and proposed definitions in `held/new-proposals.tsv` and `.md`. The part holds two capabilities and their ten cells. No concern lands here: the capabilities come from the held pass, not from the concern map. It has every file `E-amend` has; `derived.tsv` and `derived-qualities.tsv` are the checker's.

## The held pass's new capabilities (31 October)

**How the cells were made.** As in `C-amend`: each capability's terms were searched over the five platforms' statements in one run of `class_slice.py search`, in English and, for Salla and Zid, in Arabic. Every hit was read, and each cell's reading names its hits by key. `searched` is a plain `;`-separated list, so that the checker re-runs every term. A term read only in domain F's concerns ('transfer', 'نقل', 'تحويل', WooCommerce's 'updates') says so in brackets. All ten cells are `none-held`: no platform's concern-map statement holds either thing. The held pass names both, Shopify's App versions in sixteen lines and Salla's Transfer Requests in ten. `held_amend.py` adds those lines later, as each of those two cells' readings says.

**CM-APP-013, App versions** (N14; parent CM-APP-001).
- **Places of its own:** the Dev Dashboard's item Versions on an app's page (observed-sh@e38dc17e3:structures/shopify/dev-dashboard-nav/app-431413264385/items.jsonl line 9, SH-23:46), and the Partner Dashboard's route /:orgId/apps/:appId/versions (partners-dashboard-routes line 70, SH-86:100).
- **The definition** rests on the held lines: 'This command creates an app version, which is a snapshot of your app configuration and all extensions' (SH-98:52), and configuration that 'can be easily rolled back' (SH-57:3).
- **Homonyms:**
  - not CM-API-006, the platform's versions of its API (Shopify's SH-S-0690, Salla's SA-S-0207), nor Salla's theme versions (theme-versions-management and its siblings, CM-SFR-001's and CM-SFR-003's);
  - not CM-APP-010, settings held per store, nor CM-APP-004's app trials (Salla's 'نسخة تجريبية', SA-S-1570, SA-S-1571);
  - not WooCommerce's extension updates that a connected store receives (CM-APP-011's and CM-APP-012's), which are the merchant's side, not a version the platform keeps for the developer.
- **Shopify's statements on deployment, not cited:**
  - the access scopes omitted 'on initial deployment' and added 'In later deployments' (SH-S-6262, SH-S-6263);
  - the extensions' size limit enforced 'at deployment' (SH-S-7495, SH-S-7496);
  - 'the same app that deployed the function' (SH-S-6204).

  None of them names a version or says what a deployment keeps. The tie between deploying and a version is the held pass's statement (SH-98:52), not the concern map's, so citing them here would join on the held line's word. A case for the coordinator, below.
- **Parent:** apps. Both Shopify dashboards put Versions on an app's own page.

**CM-PTN-011, App ownership transfer** (N15; parent CM-PTN-001).
- **Places of its own:** the portal admin's route /admin/applications/transfer-requests (observed-sa@b0bd0b163:structures/salla/portal-app-routes/prod/items.jsonl line 128, SA-34:90), and its menu item Transfer Requests / طلبات نقل (portal-menu-definitions line 11, SA-43:3), in the admin's menu, gated by the admin permission manage-app-requests.
- **What it is:** the FAQ's 'Can I transfer my App ownership to another Partner?', 'Yes you can, by using App ownership transfer feature' (SA-39:93). The definition says no more than that: a partner transfers an app it owns to another partner, by a request kept in the platform's own portal admin. That the other partner accepts it isn't stated in what the held lines quote.
- **Homonyms:** inventory transfers (CM-INV-006; Shopify's read_inventory_transfers), a domain's transfer (Salla, CM-SFR-008), and the App Maker's app moved to the merchant's own accounts on Apple's and Google's stores (SA-S-5035, CM-CHN-006's, the store's own mobile app).
- **Parent:** the partner programme, by the coordinator's decision. CM-PTN-002, the partner account, is the alternative.

## The checker's flags, read (`check_class_part.py`, 31 October)

The last run printed "0 problems, 9 flags for the reviewer". All nine are none-held cells whose searched terms match statements, and none changes a cell:
- **CM-APP-013,** cells lines 2 to 6.
  - Every matched statement is named by key in its cell's reading, as another sense, except thirteen of Shopify's access-scope statements. They name shopify.app.toml or Shopify CLI as the place where an app declares its scopes, and say nothing of a version: SH-S-5923, SH-S-5932, SH-S-5959, SH-S-6141, SH-S-6151, SH-S-6152, SH-S-6190, SH-S-6207, SH-S-6224, SH-S-6240, SH-S-6242, SH-S-6257 and SH-S-6290, under SH-C-158 and the concerns that share them.
  - 'version' matches 'conversion' on every platform, and إصدار, نسخة and نسخ match issuing, copies and trials.
- **CM-PTN-011,** cells lines 7, 8, 9 and 11. The hits are data transfers, a domain's transfer, the App Maker's app moved to the merchant's store accounts, bank transfers, payouts, a non-transferable licence, SFTP and BigCommerce's category Data Transfer/Migration Services. Each is named in its cell.

**Gaps.** No cell cites a statement, so no Q1 gap bears on one.

## Cases not settled

1. **Shopify's deployments as app versions.** SH-S-6262, SH-S-6263, SH-S-7495, SH-S-7496 and SH-S-6204 aren't cited, since none names a version. What would settle it: the coordinator's reading of whether a deployment is this capability's thing, on the held pass's SH-98:52. If it is, they become Shopify's `shows` evidence here.
2. **Whether the receiving partner accepts a transfer.** Not stated in the held lines' quoted text; the locale's 'A request to transfer App ownership has been sent.' (SA-34's notes) shows only a request. The definition leaves acceptance out.
