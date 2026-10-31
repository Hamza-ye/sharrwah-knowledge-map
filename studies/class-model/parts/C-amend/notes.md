# C-amend: capabilities made from the held pass

Written by the agent of `briefs/M-amend.md`, 31 October 2026, from the coordinator's decisions in `held/new.tsv` (N05, N06, N10, N11) and the facts, places and proposed definitions in `held/new-proposals.tsv` and `.md`. The part holds four capabilities and their twenty cells. No concern lands here: the capabilities come from the held pass, not from the concern map. It has every file `E-amend` has; `derived.tsv` and `derived-qualities.tsv` are the checker's.

## The held pass's new capabilities (31 October)

**How the cells were made.** Each capability's terms were searched over the five platforms' statements in one run of `class_slice.py search`, in English and, for Salla and Zid, in Arabic. Every hit was read. Each cell's reading names its hits by key and says why each is cited or not; the cells that hold statements cite them in `evidence.tsv`. A platform whose held lines name the thing gets its cell from the concern map's statements only, and its reading says that `held_amend.py` adds those lines later: Zid and Salla on CM-SHP-024, Zid and Shopify on CM-CHK-011, and Shopify on CM-CHK-012 and CM-PAY-033. `searched` is a plain `;`-separated list (B-extent: "Lists are `;`-separated"), not `E-amend`'s 'en: … | ar: …', so that the checker re-runs every term. A term read only in some concerns says so in brackets.

**CM-SHP-024, Shipment received by another person** (N05; parent CM-SHP-001).
- **Place of its own:** Zid's plan policy `orders_and_products_specifications.shipment_receipt_by_different_consignee` (other-product-class@0d79b794f:zid/structures/store-plan-policies/items.jsonl line 340, ZD-11:122). Salla's is one switch of its invoice settings, which shows the delegated recipient, المستلم المفوض, in place of the order's owner (SA-26:146, SA-27:17). A switch isn't a place of its own.
- **The join:** Zid and Salla, a reading: the same thing, as SA-26 already read it. How a delegate is assigned isn't stated. Not gifting (CM-LOY-006): nothing says the other person isn't the buyer's agent.
- **Cells:** all five `none-held`. The nearest hit is Salla's webhook topic order.customer.updated, 'تحديث بيانات مستلم الطلب' / 'Order Customer Updated' (SA-C-040/boundary/SA-S-1585, CM-ORD-001's). It isn't cited: its English name makes the order's recipient the customer, and it doesn't say someone else receives.
- **Parent:** the coordinator's decision. Zid keeps the policy under Orders and products properties, and Salla its switch in the invoice settings, so neither grouping is shipping's. CM-CHK-009, an option at checkout, is the alternative.

**CM-CHK-011, Order limits** (N06; parent CM-CHK-002).
- **Place of its own:** Zid's two plan policies `min_limit_for_order` and `max_limit_for_order`, 'Enable minimum order limit' and 'Enable maximum order limit' (store-plan-policies lines 338 and 339, ZD-11:120, ZD-11:121).
- **The definition:** a minimum or a maximum an order must meet, on its value or on its quantities, so that Zid's limit, whose unit isn't stated, and Shopify's quantity rules both fit. The join is a reading on role.
- **Shopify's cell** (`statements`): the setting Add-to-cart limit, core (SH-C-046/decides/SH-S-7483, SH-S-7484), its reason, shows (SH-C-046/reason/SH-S-7489), and the uncited help-center section SH-I-2113, shows. It is the proposals' lead (held/new-proposals.md, 'Leads'). The three statements are also cited on CM-CHK-002 (C-anchor), whose name holds 'Add-to-cart limit'. This part can't change C-anchor; whether CM-CHK-002 keeps them, and the term, now that its child holds the limit, is the coordinator's. Both capabilities are in one tree, so the checker doesn't flag it.
- **Not cited:** the App Store category Order limit apps (SH-I-1816, CM-CHK-005's, shows). Q1's U-084 says the output doesn't define what those apps limit, and the same words on Salla are a daily count of orders (CM-ORD-010). Citing it would rest on the word, as `E-amend` declined to join Custom URLs.
- **Salla's cell** (`statements`): the plan line تخصيص خيارات المتجر, 'تخصيص الطلبات (حد أدنى، أوقات استقبال، تفعيل الكوبونات، إعادة الطلب)' (SA-C-002/decides/SA-S-2097, plan سلة بلس), core. It is a reading: the minimum is one of the plan's customizations of orders, and its unit isn't stated. SA-C-002 is domain A, with D under `also`, not C (the checker's flag). The statement is cited because no Salla statement of a domain C concern names an order's minimum. The same plan line supports core on CM-ACC-006 (A) and CM-MKT-023 (D), each for another of its customizations. With this cell it supports core in three domains, which the merge will flag.
- **The other cells:** Zid, WooCommerce and BigCommerce are `none-held`; Zid's held lines are added later. Not this capability: CM-ORD-010's daily order limit, CM-CHK-005's app-written validation, and the payment methods' ceilings (Salla's 1000 SAR for cash on delivery, Zid's COD Limit, MIS pay's minimum for instalments).

**CM-CHK-012, Tipping** (N10; parent CM-CHK-001).
- **Places of its own:** the checkout settings' anchor Tipping (observed-sh@e38dc17e3:structures/shopify/admin-router/items.jsonl line 358, SH-10:78), and the POS app's settings item Tips and its page (pos-settings lines 52 and 191, SH-96:31, SH-96:59).
- **Shopify's cell** (`statements`, shows only): the uncited help-center section SH-I-2109, 'Setting up tipping options for online orders', placed in SH-C-047, the proposals' lead. Its derived placement is `not-stated` until `held_amend.py` adds the held lines, thirteen of them core.
- **The other four cells:** `none-held`. The only hits are WooCommerce's `desc_tip` attribute and Shopify's '10 Tips' post.

**CM-PAY-033, 3D Secure** (N11; parent CM-PAY-001).
- **Place of its own:** Shopify's plan feature 'Fraud protection and 3D Secure checkout' (pricing-page-data line 85, SH-75:185).
- **Shopify's cell** (`statements`): the uncited webhook topic `subscription_billing_attempts/challenged`, 'as per 3D Secure' (SH-C-186/boundary/SH-S-6071), core, a reading. SH-C-186 is domain B, with C under `also`, so it may support a cell here.
- **BigCommerce's cell** (`statements`): BC-C-022/reason/BC-S-0130, core, a reading, the proposals' lead. It stays cited core on CM-PAY-022 (saved payment methods), for the stored payment instrument.
- **Salla's, Zid's and WooCommerce's cells:** `none-held`. Their hits are sign-in codes, tax-invoicing codes and fraud protection.
- **The changelog digest:** its C46.4 placed Shopify's 3D Secure, then a setting inside Shopify Payments with no place of its own, on CM-PAY-002 core and on CM-PAY-009 core (held/rules/merchant-changelog.md; held/shopify/notes-SH-46.md, entry SH-E-747ee5be). Those lines aren't N11's, so `held_amend.py` won't bring them here. Whether they move is the coordinator's.

## The checker's flags, read (`check_class_part.py`, 31 October)

The last run printed "0 problems, 12 flags for the reviewer". None changes a cell:
- **evidence line 6,** SA-C-002/decides/SA-S-2097, a statement of a domain A concern: cited on CM-CHK-011's Salla cell, as above.
- **evidence, BC-C-022/reason/BC-S-0130, cited by CM-PAY-022 and CM-PAY-033 in two trees.** They aren't one capability, nor parent and child. The statement names two things, the stored payment instrument (CM-PAY-022's) and 3D Secure-enabled cards (this capability's).
- **cells line 17, CM-PAY-033 Shopify: core rests only on a boundary statement.** The webhook topic states that the financial institution challenges the billing attempt as per 3D Secure, and that Shopify reports it. That is the platform's own processing of the charge, a reading. The held pass's plan feature (SH-75:185, core) adds a statement that isn't a boundary one.
- **The nine none-held flags,** cells lines 2, 3, 5 (CM-SHP-024), 9, 10, 11 (CM-CHK-011), 14 (CM-CHK-012), 18 and 20 (CM-PAY-033). Every statement they match is named by key in its cell's reading, as another sense: recipients of services, notices, payments received and cash on delivery; payment, payout, wallet and request limits; the settings' `desc_tip` attribute; sign-in and invoicing codes and fraud protection. Two Salla plan lines, SA-S-2144 and SA-S-1970, match only because their JSON text holds the next plan line, a fraud-protection one.

**Gaps.** The cells' derived gaps don't change what any cell claims: SA-C-002's responsible and reason (page not read), SH-C-046's responsible (stated only in general terms), and SH-C-047's and SH-C-186's reason (searched, not found).

## Cases not settled

1. **CM-CHK-002 and the Add-to-cart limit.** Its three statements are now cited on CM-CHK-011 as well, and CM-CHK-002's name holds the term. Whether the parent keeps them is the coordinator's.
2. **Salla's SA-S-2097.** It is core in three domains now (A, D and C), and its حد أدنى is read as an order's minimum. What would settle it: Salla's store-options page, with the minimum's field and unit.
3. **Order limit apps (SH-I-1816).** It isn't cited here, since U-084 is open: what those apps limit isn't defined.
4. **Shopify's C46.4 lines on CM-PAY-002 and CM-PAY-009.** Whether they move to CM-PAY-033.
5. **BigCommerce's 3D Secure.** BC-S-0130 doesn't say who authenticates the card. Its core here rests on the platform's own API naming 3D Secure-enabled cards, a reading.
6. **Zid's order limit unit** (N06's open case 2) still isn't stated. The definition holds value or quantity either way.
