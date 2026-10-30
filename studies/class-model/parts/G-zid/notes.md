# G-zid: notes

**What this part is.** Domain G's mapping part for Zid, onto the model so far: G-anchor, G-woocommerce and G-backfill-woocommerce (13 capabilities: CM-MIG-001 to 006, CM-OPS-001 to 005, CM-EVO-001, CM-SRF-001). `scope.tsv` gives Zid one concern of domain G, ZD-C-044 (Export requests / طلبات التصدير), and no concern of another domain names G under `also`.

**What it holds.** No new capability, 1 landing, 13 cells (one per capability, Zid's), 10 evidence rows, no quality, no slot filler, no ruling (Zid has no unclear candidates). Every statement of ZD-C-044 is cited, and its one placed inventory entry (ZD-I-0132). Each row below is a reading unless it quotes a statement.

## How I cut, and why

- **ZD-C-044 lands in CM-MIG-004 (Export log), joined on role, strained.** The concern's own place is a settings page, Export requests (طلبات التصدير): "يمكنك الوصول الى طلبات التصديرات من خلال : لوحة التجكم > الضغط على أيقونة الاعدادات . بعد ذلك الضغط على خانة طلبات التصدير" (ZD-C-044/where/ZD-S-0803), listed under General in the new dashboard's settings (ZD-I-0132). On it, "عند طلب أي ملف مُصدّر، ستتمكن من تحميله مباشرة في متصفحك" (ZD-C-044/decides/ZD-S-0804). So it is a page of its own for the store's requested exports, apart from where an export is started. Salla's Export log (سجل التصدير) is also a page of its own for the store's exports, in its logs list, with its own permission (SA-C-027/where/SA-S-1890; SA-C-010/decides/SA-S-2423). I read them as the same role. Neither the name nor a definition joins them, and Salla doesn't say what its log records.
- **Why not CM-MIG-001.** CM-MIG-001 is the mechanism of import and export. Zid's concern is about the page where requested exports are collected and downloaded, not about importing or about the objects exported. Its boundary statement, the Merchant API Products > Product Export (ZD-C-044/boundary/ZD-S-0018), is Zid's own export API, so I cite it in CM-MIG-001. That puts the concern's statements in two trees (CM-MIG-004 has no parent), which makes the fit strained. The reviewer may instead land the concern in CM-MIG-001, the coarser capability, as the anchor did with SA-C-027, and keep ZD-S-0803 to ZD-S-0805 in CM-MIG-004.
- **The password protection of exported files** (ZD-S-0804, with its reason ZD-S-0805) is one option of the Export requests page, not a place of its own. It stays in CM-MIG-004's cell, and no capability is added for it.
- **No new capability.** Zid's one concern fits the model, so the model's union doesn't grow, and no back-fill is needed after this part.

## Cells

- **CM-MIG-001, statements.** `core`: the Product Export API (ZD-S-0018); and four plan lines Q1 placed in other domains' concerns, which no statement covers (C2): Import Products and Export Products (ZD-I-0229, ZD-I-0250, in ZD-C-083, products, B), Bulk Export Orders (ZD-I-0263, in ZD-C-080, orders, C) and Export Customer Data (ZD-I-0345, in ZD-C-091, customers, D). The capability names products, customers and orders as its objects, and these lines are Zid's only evidence of import and of exports of orders and customers. That is why the cell cites them, as the anchor cited Shopify's export permissions placed in other concerns. The concern map gives these plan lines no plan, so which plans hold them isn't stated.
- **CM-MIG-005, statements, `shows` only.** The one Zid statement of a move from another platform is the reason given on the URL redirects page: "عند انتقالك إلى زد من منصة أخرى، قد تحتاج لإضافة عدد كبير من عمليات إعادة التوجيه دفعة واحدة" (ZD-C-102/reason/ZD-S-0968, domain E). It names no service, app or section for the move, so who carries it out isn't stated. Shopify's cell is `shows` too, and Salla's is `own-service`.
- **The other ten cells are `none-held`.** Each lists its searched terms in English and Arabic, with the Arabic singular and plural, with and without ال.

## Joins

- **On role:** ZD-C-044 in CM-MIG-004 (above). Its keys are ZD-C-044/where/ZD-S-0803 and ZD-C-044/decides/ZD-S-0804 for Zid, and SA-C-027/where/SA-S-1890 and SA-C-010/decides/SA-S-2423 for Salla.
- No join by terms, identifier, definition or match. Zid was never matched by Q1.

## Homonyms kept apart

- **Mobile app (تطبيق الجوال).** CM-SRF-001 is the app for managing the store (Salla's تطبيق إدارة المتجر, WooCommerce mobile app). Zid holds two other mobile apps, both domain E, and neither is cited:
  - the store's own customer-facing app, تطبيق الجوال (ZD-C-116: ZD-S-1006, ZD-S-0500, ZD-S-1084, ZD-S-1087). In ZD-S-1084, تطبيق التاجر means the merchant's store app, which the Anaqeed team (عناقيد) publishes;
  - Zid's POS app, تطبيق الكاشير للجوال والتابلت (ZD-C-108: ZD-S-0979, ZD-S-0978).
- **Template (قالب).** The storefront's design templates (ZD-C-113/decides/ZD-S-1001; ZD-I-0328, ZD-I-0333, domain E) are not CM-MIG-003's export templates.
- **سجل / log.** Zid's records of features (Inventory Management Logs, ZD-I-0244, ZD-I-0251) and the commercial register (السجل التجاري, ZD-S-0738, ZD-S-0759, ZD-S-0755) are neither CM-OPS-005's logger entries nor CM-MIG-004's export log. CM-MIG-004's Zid cell rests on Export requests, which isn't named a log (see the role join).
- **Status / health (حالة).** The health states of webhook endpoints (ZD-C-072, F) and the statuses of payments and orders (ZD-C-028; ZD-I-0264 and others) are not CM-OPS-004's store status.
- **Infrastructure provider.** Google Cloud "acts solely as an infrastructure provider and processor" (ZD-C-042/responsible/ZD-S-0798, domain A) for Zid's AI data processing. It isn't the store's hosting (CM-OPS-003), so it isn't cited and isn't a slot filler here.
- **Pilot.** "Limited pilot" (ZD-C-112/decides/ZD-S-1069, C) is the scope of one feature, not CM-EVO-001's feature settings.

## Strained fits

- **ZD-C-044 in CM-MIG-004.** It is joined on role with a Salla page whose content isn't stated, and its boundary statement ZD-S-0018 is cited in CM-MIG-001, another tree. See "How I cut".

## What the checker flagged, and answers

- **Five evidence rows cite statements of concerns outside G that don't name G under `also`:**
  - ZD-I-0229, ZD-I-0250 (ZD-C-083, B), ZD-I-0263 (ZD-C-080, C) and ZD-I-0345 (ZD-C-091, D), in CM-MIG-001. They are the cell's only evidence of import and of exports of the objects the capability names (see "Cells"). B-zid already cites ZD-I-0229 and ZD-I-0250 as `core` in CM-CAT-001 (catalog), so the merge will flag a statement that supports `core` in two domains. The reviewer should decide which domain keeps them. Following the anchor, which took the product import routes into G, the import and export lines read as G's mechanism; B-zid reads them as product-management plan lines.
  - ZD-C-102/reason/ZD-S-0968 (E), in CM-MIG-005, `shows` only: Zid's only statement of a move from another platform.
- **Eight `none-held` cells have matching statements.** I read the hits, and each is another thing:
  - CM-EVO-001's 194 hits are plan lines, for the terms features, المزايا and مزايا. Examples are the plan cards' "All features of … package, plus:" (ZD-S-0361, ZD-S-0370) and Zid Agent's wallet "المزايا المختلفة" (ZD-S-0713). The one other hit is Limited pilot.
  - CM-MIG-003's hits are design templates.
  - CM-OPS-001's hits are Zid Pay's liability terms (ZD-S-0594), activating Zid Pay disabling another gateway (ZD-S-0608, the term تعطل), and product availability (ZD-C-085, ZD-C-087).
  - CM-OPS-002's one hit is an app's partner-managed setup (ZD-S-0877).
  - CM-OPS-003's hits are Google Cloud for AI processing and the OAuth server URL.
  - CM-OPS-004's hits are the term status in payments, orders and webhooks, and الكاش in الكاشير (POS).
  - CM-OPS-005's hits are سجل in the commercial register (ZD-S-0730, ZD-S-0738, ZD-S-0755, ZD-S-0759, ZD-S-0763) and log in blog and login (ZD-C-093; ZD-S-0613 and others).
  - CM-SRF-001's hits are the App Market's apps (ZD-C-070, ZD-C-071, ZD-C-074), the store's own app (ZD-C-116), the POS app (ZD-C-108) and service partners (ZD-S-1080).

## Gaps and problems

- **ZD-C-044/responsible is stated only in general terms** (Q1's gap). Who answers for exports isn't stated.
- **Neither the Export requests page nor Salla's Export log is defined**: what each lists, how long its files are kept, and whether it records imports. The join on role rests on their being separate pages for exports.
- **ZD-S-0018 and ZD-I-0018 are the same Product Export API entry.** Q1 places the statement in ZD-C-044 and the inventory entry in ZD-C-083 (B). I cite only the statement.
- **Zid's plan lines for import and export carry no plan** in the concern map's inventory entries, so their scope isn't stated.
