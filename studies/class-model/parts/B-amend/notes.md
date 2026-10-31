# B-amend: concerns moved into domain B after its parts ran

Written by the coordinator, 30 October 2026.

## ZD-C-089, Zid's Bundle Offers (الحزم التسويقية)

- **Why it moved.** `D-zid` batch 1 found that Zid's own statements describe a product bundle, "Bundle multiple products into one package" (ZD-S-0928), "not ordinary discounts" (ZD-S-1033), and that domain D has no bundle capability. `B-zid` already cites all seven of its statements in CM-SEL-006, Product bundles, six as `core` or `shows` evidence of Zid's cell. Landing it in D would have put the same statements in two domains. scope.tsv now gives it domain B, with D under `also`.
- **The landing.** CM-SEL-006, by the term bundle, clean. No cell or evidence is written: Zid's cell for CM-SEL-006 is `B-zid`'s, and it already cites the concern.
- **What it leaves.** Zid's API path for bundle offers sits under discounts (/discounts/bundle-offers, ZD-S-0106), and its API group under Marketing (ZD-S-0026). Both are cited in CM-SEL-006 by `B-zid`. A reviewer may weigh whether Zid's grouping under marketing makes the bundle a marketing offer as well; the model follows the statements that say what it is.

## The held pass's new capabilities (31 October)

Written by the agent of `briefs/M-amend.md`, 31 October 2026, from the coordinator's decision in `held/new.tsv` (N16) and the facts and proposed definition in `held/new-proposals.tsv` and `.md`. The section above, its landing and its files' other rows are the coordinator's, kept as they were. This section adds one capability, its five cells and one evidence row. No concern lands for it: it comes from the held pass, not from the concern map.

**CM-CAT-016, Product certificates** (N16; parent CM-CAT-001).
- **Place of its own:** Salla's route /products/certificates and its navigation item Product certificates (شهادات المنتج) in Products (observed-sa@b0bd0b163:structures/salla/dashboard-nav-segments/prod/items.jsonl line 142, SA-22:76). It is gated by the staff permission products_management (SA-30:42), and its plan gate is the feature product-certificates on plans plus, pro and special (observed-sa@b0bd0b163:derived/plan-gates.tsv line 92, SA-32:105). An admin route, B-extent's first kind.
- **The definition holds only what the route and its page's title say.** The page is titled 'Certificate templates', and what a certificate is, or what it certifies, isn't stated (SA-22's notes). So nothing can be joined to it by what it does. The other platforms' cells say the definition isn't stated, as B-extent asks for a capability its own platform names but never defines.
- **Parent:** the product catalog, by Salla's grouping: the route sits under Products and is gated by products_management.
- **Salla's cell** (`statements`): the released feature flag product-certificates (SA-C-020/decides/SA-S-3473, plans plus, pro and special), core, uncited until now. A released flag supports core, with its plans as its scope (the dry run's rulings). The held pass's three lines are added later by `held_amend.py`.
- **The other four cells:** `none-held`. The searches were by the word, certificate, in English and, for Zid, Arabic (شهادة and its plurals, قالب, معتمد, موثق). Each finds only other certificates: the store's SSL and business platform certificates, PCI DSS, Zid's VAT and IBAN certificates, BigCommerce's gift certificates and Tier 1 certifications, and Shopify's Plus Certified apps.
- **`searched`** is a plain `;`-separated list, not `E-amend`'s 'en: … | ar: …', so that the checker re-runs every term.

**The checker's flags, read** (`check_class_part.py`, 31 October). The last run printed "0 problems, 4 flags for the reviewer". All four are none-held cells whose searched terms match statements, cells lines 2 (Shopify), 4 (WooCommerce), 5 (Zid) and 6 (BigCommerce). Every statement they match is named by key in its cell's reading as another certificate or another sense of the word, and none changes a cell. Salla's cell shows the gaps on SA-C-020's responsible and reason (page not read), which don't change what it claims.

**Case not settled.** What a product certificate is. What would settle it: the certificate templates page with a template opened (held/new-proposals.md, open case 9).
