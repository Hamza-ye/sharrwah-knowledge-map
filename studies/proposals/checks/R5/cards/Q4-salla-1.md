# Cards: Q4 on salla

15 records cited by `studies/proposals/drafts/Q4/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - All five let a seller take orders that the buyer pays outside the platform. They match on role (basis 4), each in its own words, all in stated pages: with a Shopify manual payment method the seller "can arrange to receive their payment in a way that works best for them"; with Salla's bank transfer "يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك"; Zid shows the merchant's bank account at payment "لتمكين العملاء من الدفع عن طريق التحويل البنكي"; with WooCommerce's direct bank transfer "the payment process is manual and happens outside your WooCommerce powered store"; BigCommerce's offline payment methods "do not require a credit card or a traditional payment gateway". Q4-SH-K1737, Q4-SA-P0099, Q4-ZD-K0124, Q4-WC-002, Q4-BC-P0114
- **section 1, line 8:** - WooCommerce and BigCommerce share the term offline payment method (basis 1), and Salla and Zid the terms التحويل البنكي and الدفع عند الاستلام (basis 1), all in stated pages. Q4-WC-002, Q4-BC-P0114, Q4-SA-P0098, Q4-ZD-K0098
- **section 1, line 9:** - Cash on delivery collected by the seller's own carrier keeps the money out of Salla: with a carrier outside Salla's shipping labels "لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة", and the amounts are settled "مباشرة بين التاجر وشركة الشحن". WooCommerce's cash on delivery "lets you take payments at the time of delivery", BigCommerce's lets customers "pay you with cash", and Shopify lists it among the common types of manual payments (role, basis 4, all stated). Q4-SA-P0091, Q4-SA-P0092, Q4-WC-004, Q4-BC-P0117, Q4-SH-003
- **section 1, line 10:** - Orders the seller creates take such payments too (role, basis 4, all stated): a Salla manual order takes bank transfer with the receipt uploaded, or cash on delivery with its commission; Zid's تفعيل الدفع اليدوي lets the merchant "إنشاء وتنفيذ الطلبات دون الحاجة إلى وجود عملية دفع إلكترونية فعلية"; BigCommerce's manual orders "can reference an offline payment such as cash or check". Q4-SA-007, Q4-ZD-001, Q4-BC-020
- **section 1, line 11:** - In their terms (official pages), Shopify tells the seller any contract of sale is "directly and only between you and the customer"; Salla's agreement says "ليس هناك أي علاقة لمنصة سلة بطريقة الدفع عند الاستلام", and lets Salla require that payments be made directly between merchant and consumer through their own bank accounts; Zid says it is "ليست طرفاً في العلاقة بين المستهلك والتاجر", which names no one in the role. Q4-SH-K1491, Q4-SA-P0080, Q4-SA-P0081, Q4-ZD-029
- **section 1, line 15:** - No one term covers all five. Shopify says manual payment methods, with cash on delivery, money orders and bank transfers as common types; WooCommerce says offline payment method; BigCommerce's offline payment methods are Bank deposit, Cash on delivery, Check, Money order and Pay in store; Salla and Zid name each method, as التحويل البنكي and الدفع عند الاستلام. Q4-SH-003, Q4-WC-002, Q4-BC-006, Q4-SA-P0099, Q4-SA-P0098, Q4-ZD-K0098
- **section 1, line 23:** - **Proof of payment.** In Salla's dashboard text (recorded session, 12 October 2026) the merchant picks the bank receipt image on the order (اختر صورة الإيصال البنكي), and one storefront's checkout (store.rasasi.com.sa, 9 October 2026) asked the buyer to "Upload your bank transfer receipt". How a merchant reviews a receipt and confirms the payment, and whether Salla takes part, was not in what was read. Q4-SA-015, Q4-SA-074, Q4-SA-N02
- **section 1, line 25:** - WooCommerce, BigCommerce and Salla carry payment in the one order status (role, basis 4). WooCommerce sets cash-on-delivery orders to Processing "until payment is collected", though Processing means "Payment has been received (paid)"; BigCommerce places offline-paid orders in Awaiting Payment (both stated). Salla's dashboard text (recorded session, 12 October 2026) shows قيد المراجعة on the confirmation page "عند الدفع عبر التحويل البنكي أو الدفع عند الاستلام", and its help offers to set cash-on-delivery orders to تم التنفيذ at once, "لتجنب إشكالية سوء فهم العميل لحالة" that status. Q4-WC-015, Q4-WC-019, Q4-BC-P0115, Q4-SA-018, Q4-SA-045
- **section 1, line 26:** - **Time to pay** (role, basis 4, all stated). Salla's merchant can turn off the bank-transfer مهلة الدفع, so that the customer must transfer and attach the receipt on completing the order; WooCommerce's Hold Stock "automatically cancels eligible Pending payment orders created through checkout after the configured time limit"; Shopify lets the seller add payment terms, after which an unpaid order becomes Overdue. Q4-SA-047, Q4-WC-039, Q4-SH-014
- **section 1, line 28:** - **Refunds.** WooCommerce and BigCommerce record a refund that the seller makes outside them (role, basis 4, both stated): a WooCommerce order can reach Refunded "without the customer’s funds having been returned"; recording an offline refund in BigCommerce is "an optional manual process". When a refund can't go through Salla, the merchant transfers the amount to the customer's bank account or adds it to the customer's wallet in the store. Q4-WC-026, Q4-BC-018, Q4-SA-009
- **section 1, line 30:** - For a bank-transfer order, Salla takes a Salla label's cost from the merchant's balance, not from the order, and asks for a top-up when it is short; Zid takes a return label's cost from محفظة زد. Q4-SA-013, Q4-ZD-K0581
- **section 1, line 31:** - **Reports.** Zid's analytics give "نسب استخدام طرق الدفع في متجرك", and Salla's dashboard text (recorded session, 12 October 2026) the distribution of payments by payment method: a match on role (basis 4) across stated and observed sources. With WooCommerce's default Date Paid, "orders without a paid date are excluded". Q4-ZD-022, Q4-SA-049, Q4-WC-032
- **section 1, line 38:** - **By plan.** Salla offers bank transfer and cash on delivery on its basic plan, where "طرق الدفع الإلكترونية فهي متاحة ضمن الباقات المدفوعة فقط" (stated); Zid's plan comparison (shipped) offers Bank Transfer Payment on all four plans. Q4-SA-P0099, Q4-SA-P0068, Q4-ZD-K0126
- **section 1, line 46:** - Who collects and holds those amounts before payout was not in what was read. Salla's usage agreement (6 October 2026) says "ليس هناك أي علاقة لمنصة سلة بطريقة الدفع عند الاستلام", while its help (7 October 2026) describes the dues reaching the store's account: records that may disagree. The proposal rests on the help for the flow, and on neither for who holds the money. Q4-SA-G0117, Q4-SA-P0080, Q4-SA-P0038
- **section 2, line 56:** - Built-in kinds, each off until the seller turns it on: **bank transfer to the seller**; **cash on delivery**, collected by the seller's courier or carrier; **payment at pickup**, at the seller's branch or store; and a **seller-named method** with the seller's own name. They draw on BigCommerce's five offline methods, Pay in store among them, Salla's and Zid's bank transfer and cash on delivery, and Shopify's custom manual payment method. Q4-BC-006, Q4-SA-P0099, Q4-SA-P0098, Q4-ZD-K0098, Q4-SH-007
- **section 2, line 58:** - The same methods serve orders the seller creates, the payment being recorded as the order is made, as Salla's manual orders, Zid's تفعيل الدفع اليدوي and BigCommerce's manual orders allow. Q4-SA-007, Q4-ZD-001, Q4-BC-020
- **section 2, line 66:** - It draws on Shopify's and Zid's separate payment status, Shopify's Overdue after payment terms, and Salla's قيد المراجعة for bank-transfer and cash-on-delivery orders. Q4-SH-014, Q4-SA-018
- **section 2, line 67:** - Why: rule 3, as the data model is expensive to change after launch. A cash-on-delivery order is delivered before it is paid; one status for both puts WooCommerce's in Processing, which means paid, and led Salla to offer a setting so customers don't misread تم التنفيذ. Q4-WC-015, Q4-WC-019, Q4-SA-045
- **section 2, line 70:** - Proof: the buyer, at checkout or later, or the seller can attach a receipt; the order then awaits review until the seller confirms, and Sharrwah doesn't judge the proof. It draws on Salla's receipt upload; how Salla's merchant reviews a receipt was not in what was read, so the confirming step is Sharrwah's own proposal. Q4-SA-015, Q4-SA-074, Q4-SA-N02
- **section 2, line 75:** - **Payment window**: per method, an optional time for the buyer to pay after ordering; when it ends, the order shows overdue or is cancelled with its stock released, as the seller chooses. Rule 3 puts only the due date in the data model now and leaves the rest to the build. Q4-SA-047, Q4-WC-039, Q4-SH-014
- **section 2, line 77:** - **Refund record**: a refund of a seller-collected payment is made by the seller outside Sharrwah (to the buyer's bank account, in cash, or as credit in the store where it offers one) and entered on the order: amount, route, date and who entered it. Sharrwah's screens would say the refund was recorded, not that it was sent. Q4-BC-018, Q4-SA-009
- **section 2, line 86:** - Alternative not taken: taking such a charge, such as a label's cost, from a balance the seller tops up, as Salla and Zid do. A prepaid balance would hold sellers' money through Sharrwah, so it is left to the founder's decision under the guard. Q4-SA-013, Q4-ZD-K0581
- **section 2, line 87:** - **Payment reports**: reports would count seller-collected orders by method and by the amount and date recorded. Rule 3 leaves them to the build; they need only the **Payment record**. Q4-SA-049, Q4-ZD-022, Q4-WC-032
- **section 2, line 94:** - **Cash on delivery** collected by the seller's own courier or carrier, settled between them as on Salla, needs none of this and doesn't wait for the decision. Q4-SA-P0092
- **section 3, line 104:** - **Set per plan:** whether a store gets the methods, which conditions it may set, and any **Seller-collected order charge**: Salla offers bank transfer on its basic plan, Zid's restrictions start at its growth plan, and BigCommerce's fee applies on self-serve plans. Q4-SA-P0099, Q4-ZD-K0357, Q4-BC-012
- **section 3, line 107:** - **Set per order:** payment and refund entries, proof and a due date. Q4-SA-015, Q4-SH-014
- **section 3, line 113:** - **Set by the buyer:** the method chosen, and any proof attached. Q4-SA-074
- **section 7, line 156:** - Sharrwah's position in sales paid outside it: will its agreement say the sale is between seller and buyer only, and that Sharrwah has no part in cash on delivery or bank transfer, as Shopify's, Salla's and Zid's terms say of themselves? Q4-SH-K1491, Q4-SA-P0080, Q4-ZD-029
- **section 7, line 157:** - May Sharrwah require that payments be made directly between seller and buyer, as Salla's agreement lets Salla require? Q4-SA-P0081

## The cards

### Q4-SA-P0099

**Cited at:** section 1, line 7; section 1, line 15; section 1, line 38; section 2, line 56; section 3, line 104

**Record** (`studies/proposals/records/Q4/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-098
- bullet: a;end-payment
- placement: boundary
- identifier: ❓ ما هي طرق الدفع المتاحة في باقة بيسك؟
- statement: في باقة بيسك يمكنك تفعيل خيار التحويل البنكي، حيث يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك.
- scope: باقة بيسك
- cite_ids: S01-SA-C109
- from: new

**Citation S01-SA-C109:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 874 (article dcrwxldslve7spa8eqdgii8g, تفعيل طرق الدفع في المتجر), paragraph 49 | 2026-08-31 | kind: stated | quote check: found
- quote: في باقة بيسك يمكنك تفعيل خيار التحويل البنكي، حيث يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ي حسب الدولة ونوع المنتج لضمان عمليات دفع آمنة ومتوافقة مع السياسات المعتمدة. لمزيد من التفاصيل حول حدود معاملات الدفع الإلكتروني - خيار تحديد السوق في حال تم تفعيل ميزة الأسواق المتعددة ، ستظهر أيقونة اختيار السوق في صفحة طرق الدفع، حيث تتيح لك اختيار السوق الذي ترغب في إدارة إعداداته، والتنقل بسهولة بين الأسواق المختلفة المرتبطة بمتجرك. لمزيد من التفاصيل حول تفعيل وإدارة الأسواق المتعددة. الأسئلة الشائعة ❓ ما هي طرق الدفع المتاحة في باقة بيسك؟ ⟪في باقة بيسك يمكنك تفعيل خيار التحويل البنكي، حيث يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك.⟫ كما يمكنك تفعيل الدفع عند الاستلام ليتم تحصيل المبلغ عبر شركة الشحن أو من خلال مندوبك الخاص. أما طرق الدفع الإلكترونية فهي متاحة ضمن الباقات المدفوعة فقط. ❓من يمكنه استخدام ميزة عرض رسالة التبرع؟ التجار الذين يستخدمون مدفوعات سلة فقط. ❓ كيف يمكنني تفعيل طرق الدفع في متجري؟ من صفحة (طرق الدفع)، اختر وسيلة الدفع المناسبة واضغط (تفعيل) ثم أكمل بياناتها. ❓هل تكون ميزة عرض رسالة التبرع مفعّلة تلقائياً؟ نعم، تكون مفعّلة تلقائياً لجميع المتاجر التي تعم…

### Q4-SA-P0098

**Cited at:** section 1, line 8; section 1, line 15; section 2, line 56

**Record** (`studies/proposals/records/Q4/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-097
- bullet: a
- placement: boundary
- identifier: ❓ ما هي طرق الدفع المتاحة في باقة بيسك؟
- statement: كما يمكنك تفعيل الدفع عند الاستلام ليتم تحصيل المبلغ عبر شركة الشحن أو من خلال مندوبك الخاص.
- scope: باقة بيسك
- cite_ids: S01-SA-C108
- from: new

**Citation S01-SA-C108:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 874 (article dcrwxldslve7spa8eqdgii8g, تفعيل طرق الدفع في المتجر), paragraph 50 | 2026-08-31 | kind: stated | quote check: found
- quote: كما يمكنك تفعيل الدفع عند الاستلام ليتم تحصيل المبلغ عبر شركة الشحن أو من خلال مندوبك الخاص.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …لدفع الإلكتروني - خيار تحديد السوق في حال تم تفعيل ميزة الأسواق المتعددة ، ستظهر أيقونة اختيار السوق في صفحة طرق الدفع، حيث تتيح لك اختيار السوق الذي ترغب في إدارة إعداداته، والتنقل بسهولة بين الأسواق المختلفة المرتبطة بمتجرك. لمزيد من التفاصيل حول تفعيل وإدارة الأسواق المتعددة. الأسئلة الشائعة ❓ ما هي طرق الدفع المتاحة في باقة بيسك؟ في باقة بيسك يمكنك تفعيل خيار التحويل البنكي، حيث يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك. ⟪كما يمكنك تفعيل الدفع عند الاستلام ليتم تحصيل المبلغ عبر شركة الشحن أو من خلال مندوبك الخاص.⟫ أما طرق الدفع الإلكترونية فهي متاحة ضمن الباقات المدفوعة فقط. ❓من يمكنه استخدام ميزة عرض رسالة التبرع؟ التجار الذين يستخدمون مدفوعات سلة فقط. ❓ كيف يمكنني تفعيل طرق الدفع في متجري؟ من صفحة (طرق الدفع)، اختر وسيلة الدفع المناسبة واضغط (تفعيل) ثم أكمل بياناتها. ❓هل تكون ميزة عرض رسالة التبرع مفعّلة تلقائياً؟ نعم، تكون مفعّلة تلقائياً لجميع المتاجر التي تعمل عبر مدفوعات سلة، باستثناء تجار سبيشل. ❓في أي حالات لا تظهر رسالة التبرع؟ لا تظهر رسالة التب…

### Q4-SA-P0091

**Cited at:** section 1, line 9

**Record** (`studies/proposals/records/Q4/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-090
- bullet: d
- placement: responsible
- identifier: الأسئلة الشائعة
- statement: لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة.
- scope: شركة شحن خارج نطاق بوليصات سلة
- cite_ids: S01-SA-C095
- from: index:SA-C-116:SA-S-0120
- note: Answer to 'هل تقوم سلة بتحصيل مبالغ الدفع عند الاستلام عند استخدام شركة شحن خارج نطاق بوليصات سلة؟'.

**Citation S01-SA-C095:** `https://help.salla.sa/article/تفعيل-وإدارة-الدفع-عند-الاستلام-مع-بوليصات-سلة/koda8pykc6pdhylg7zb2iu0g` | الأسئلة الشائعة (line 786 of the rendered text) | 2026-08-31 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235130Z-q1-salla-sources/items/027-help.salla.sa/text.txt` (fetched 2026-10-10T23:51:44Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/023-help.salla.sa/text.txt` (fetched 2026-10-12T10:49:59Z, captured)
- quote: لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة.
- title: تفعيل الدفع عند الاستلام وإدارته | مركز المساعدة - سلة
- the page opens: تفعيل الدفع عند الاستلام وإدارته مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل حل…
- in context: …يد عن الرسوم في محفظتك كربح لك. - في حال إضافة رسوم أقل من رسوم الشركة لتحفيز عملاءك على الشراء سيتم خصم المبلغ الذي يزيد عن الرسوم من رصيدك. الأسئلة الشائعة ❓ما هي شركات الشحن التي تدعم الدفع عند الاستلام من بوليصات سلة؟ الشركات الداعمة للدفع عند الاستلام من بوليصات سلة هي: 1- أرامكس 2- جي اند تي اكسبريس | J&T 3- أي مكان 4- سمسا 5- ريد بوكس 6- شيبا | shipa ❓ هل تقوم سلة بتحصيل مبالغ الدفع عند الاستلام عند استخدام شركة شحن خارج نطاق بوليصات سلة؟ ⟪لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة.⟫ تتم تسوية مبالغ الدفع عند الاستلام مباشرة بين التاجر وشركة الشحن وفقاً للاتفاق المبرم بين الطرفين. ❓ما هي أيام تحويل رصيد الدفع عند الاستلام الناتج من بوليصات سلة للتاجر؟ الأيام المحددة لتحويل رصيد الدفع عند الاستلام من الشركات التي تدعم الدفع عند الاستلام في بوليصات سلة إلى التاجر هي: يومي الأحد والأربعاء لجميع شركات الشحن ضمن بوليصات سلة. تُصدر الفاتورة بمبالغ الطلبات التي استلمها العميل وتكون حالتها (تم التوصيل) أو (تم الشحن)، وتشمل الطلبات ا…

### Q4-SA-P0092

**Cited at:** section 1, line 9; section 2, line 94

**Record** (`studies/proposals/records/Q4/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-091
- bullet: a;b;d
- placement: responsible
- identifier: الأسئلة الشائعة
- statement: تتم تسوية مبالغ الدفع عند الاستلام مباشرة بين التاجر وشركة الشحن وفقاً للاتفاق المبرم بين الطرفين.
- scope: شركة شحن خارج نطاق بوليصات سلة
- cite_ids: S01-SA-C096
- from: index:SA-C-116:SA-S-0121
- note: Same answer as the preceding statement. About 200 carrier articles (old articles sections) each answer ما هي آلية تسوية المبالغ؟ with that carrier's schedule; not recorded one by one (see notes.md).

**Citation S01-SA-C096:** `https://help.salla.sa/article/تفعيل-وإدارة-الدفع-عند-الاستلام-مع-بوليصات-سلة/koda8pykc6pdhylg7zb2iu0g` | الأسئلة الشائعة (line 788 of the rendered text) | 2026-08-31 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235130Z-q1-salla-sources/items/027-help.salla.sa/text.txt` (fetched 2026-10-10T23:51:44Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/023-help.salla.sa/text.txt` (fetched 2026-10-12T10:49:59Z, captured)
- quote: تتم تسوية مبالغ الدفع عند الاستلام مباشرة بين التاجر وشركة الشحن وفقاً للاتفاق المبرم بين الطرفين.
- title: تفعيل الدفع عند الاستلام وإدارته | مركز المساعدة - سلة
- the page opens: تفعيل الدفع عند الاستلام وإدارته مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل حل…
- in context: …رسوم الشركة لتحفيز عملاءك على الشراء سيتم خصم المبلغ الذي يزيد عن الرسوم من رصيدك. الأسئلة الشائعة ❓ما هي شركات الشحن التي تدعم الدفع عند الاستلام من بوليصات سلة؟ الشركات الداعمة للدفع عند الاستلام من بوليصات سلة هي: 1- أرامكس 2- جي اند تي اكسبريس | J&T 3- أي مكان 4- سمسا 5- ريد بوكس 6- شيبا | shipa ❓ هل تقوم سلة بتحصيل مبالغ الدفع عند الاستلام عند استخدام شركة شحن خارج نطاق بوليصات سلة؟ لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة. ⟪تتم تسوية مبالغ الدفع عند الاستلام مباشرة بين التاجر وشركة الشحن وفقاً للاتفاق المبرم بين الطرفين.⟫ ❓ما هي أيام تحويل رصيد الدفع عند الاستلام الناتج من بوليصات سلة للتاجر؟ الأيام المحددة لتحويل رصيد الدفع عند الاستلام من الشركات التي تدعم الدفع عند الاستلام في بوليصات سلة إلى التاجر هي: يومي الأحد والأربعاء لجميع شركات الشحن ضمن بوليصات سلة. تُصدر الفاتورة بمبالغ الطلبات التي استلمها العميل وتكون حالتها (تم التوصيل) أو (تم الشحن)، وتشمل الطلبات المنجزة خلال الأسبوع السابق. يرجى ملاحظة أن وصول المبلغ إلى حسابك البنكي قد يستغرق وقتاً إضافياً حسب…

### Q4-SA-007

**Cited at:** section 1, line 10; section 2, line 58

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-007
- bears_on: 1;3
- identifier: الخطوة الثالثة. تحديد طريقة الدفع
- statement: لدى العميل عدة طرق لدفع قيمة الطلب، وهي: 1- تحويل بنكي ، اختر البنك وارفع ايصال الدفع. 2- دفع عند الاستلام، حدد عمولة الدفع عند الاستلام. 3- وسائل دفع أخرى كالبطاقة الإئتمانية أو وسائل الدفع الآجل.
- scope: إنشاء طلب جديد يدوياً
- cite_ids: Q4-SA-C012;Q4-SA-C013;Q4-SA-C014;Q4-SA-C015
- from: held

**Citation Q4-SA-C012:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 210 (article dsw3leig1h4jocdmnengiw8s, إنشاء طلب جديد يدوياً) | 2026-03-14 | kind: stated | quote check: found
- quote: لدى العميل عدة طرق لدفع قيمة الطلب، وهي:
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …تج خاص 1- اضغط (+ منتج خاص). 2- أدخل بيانات بطاقة المنتج الخاص ثم اضغط (إضافة). يمكنك تعديل بيانات المنتج الخاص بالضغط عليه. الخطوة الثانية. تحديد العميل ابحث عن اسم العميل (في حال كان الطلب لعميل سابق) أو اضغط (+إضافة عميل جديد) في حال كان الطلب لعميل جديد، ثم ادخل بيانات العميل، واضغط (حفظ). لإرسال الطلب إلى شخص آخر فعّل خيار (ارسال الطلب لشخص آخر) وأدخل اسم المستلم وبريده الإلكتروني ورقم جواله، ثم اضغط (حفظ). الخطوة الثالثة. تحديد طريقة الدفع ⟪لدى العميل عدة طرق لدفع قيمة الطلب، وهي:⟫ 1- تحويل بنكي ، اختر البنك وارفع ايصال الدفع. 2- دفع عند الاستلام، حدد عمولة الدفع عند الاستلام. 3- وسائل دفع أخرى كالبطاقة الإئتمانية أو وسائل الدفع الآجل. سيظهر قسم طريقة الدفع في الطلب بالشكل: الخطوة الرابعة. تحديد طريقة شحن الطلب حدد فيما إذا كان الطلب يحتاج إلى شحن أم لا. الحالة1- الطلب لا يحتاج شحن عندما تكون منتجات المتجر عبارة عن منتجات رقمية أو بطاقات رقمية أو استشارات فهي منتجات لا تحتاج إلى شحن. الحالة2- الطلب يحتاج شحن وتوصيل حدد هل …

**Citation Q4-SA-C013:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 210 (article dsw3leig1h4jocdmnengiw8s, إنشاء طلب جديد يدوياً) | 2026-03-14 | kind: stated | quote check: found
- quote: 1- تحويل بنكي ، اختر البنك وارفع ايصال الدفع.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ات بطاقة المنتج الخاص ثم اضغط (إضافة). يمكنك تعديل بيانات المنتج الخاص بالضغط عليه. الخطوة الثانية. تحديد العميل ابحث عن اسم العميل (في حال كان الطلب لعميل سابق) أو اضغط (+إضافة عميل جديد) في حال كان الطلب لعميل جديد، ثم ادخل بيانات العميل، واضغط (حفظ). لإرسال الطلب إلى شخص آخر فعّل خيار (ارسال الطلب لشخص آخر) وأدخل اسم المستلم وبريده الإلكتروني ورقم جواله، ثم اضغط (حفظ). الخطوة الثالثة. تحديد طريقة الدفع لدى العميل عدة طرق لدفع قيمة الطلب، وهي: ⟪1- تحويل بنكي ، اختر البنك وارفع ايصال الدفع.⟫ 2- دفع عند الاستلام، حدد عمولة الدفع عند الاستلام. 3- وسائل دفع أخرى كالبطاقة الإئتمانية أو وسائل الدفع الآجل. سيظهر قسم طريقة الدفع في الطلب بالشكل: الخطوة الرابعة. تحديد طريقة شحن الطلب حدد فيما إذا كان الطلب يحتاج إلى شحن أم لا. الحالة1- الطلب لا يحتاج شحن عندما تكون منتجات المتجر عبارة عن منتجات رقمية أو بطاقات رقمية أو استشارات فهي منتجات لا تحتاج إلى شحن. الحالة2- الطلب يحتاج شحن وتوصيل حدد هل الشحن مجاني أم مدفوع، ثم حدد شركة الشحن واضغط …

**Citation Q4-SA-C014:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 210 (article dsw3leig1h4jocdmnengiw8s, إنشاء طلب جديد يدوياً) | 2026-03-14 | kind: stated | quote check: found
- quote: 2- دفع عند الاستلام، حدد عمولة الدفع عند الاستلام.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …عديل بيانات المنتج الخاص بالضغط عليه. الخطوة الثانية. تحديد العميل ابحث عن اسم العميل (في حال كان الطلب لعميل سابق) أو اضغط (+إضافة عميل جديد) في حال كان الطلب لعميل جديد، ثم ادخل بيانات العميل، واضغط (حفظ). لإرسال الطلب إلى شخص آخر فعّل خيار (ارسال الطلب لشخص آخر) وأدخل اسم المستلم وبريده الإلكتروني ورقم جواله، ثم اضغط (حفظ). الخطوة الثالثة. تحديد طريقة الدفع لدى العميل عدة طرق لدفع قيمة الطلب، وهي: 1- تحويل بنكي ، اختر البنك وارفع ايصال الدفع. ⟪2- دفع عند الاستلام، حدد عمولة الدفع عند الاستلام.⟫ 3- وسائل دفع أخرى كالبطاقة الإئتمانية أو وسائل الدفع الآجل. سيظهر قسم طريقة الدفع في الطلب بالشكل: الخطوة الرابعة. تحديد طريقة شحن الطلب حدد فيما إذا كان الطلب يحتاج إلى شحن أم لا. الحالة1- الطلب لا يحتاج شحن عندما تكون منتجات المتجر عبارة عن منتجات رقمية أو بطاقات رقمية أو استشارات فهي منتجات لا تحتاج إلى شحن. الحالة2- الطلب يحتاج شحن وتوصيل حدد هل الشحن مجاني أم مدفوع، ثم حدد شركة الشحن واضغط (حفظ). 💡ملاحظة: عند كتابة العنوان الوطني، ستظهر قائ…

**Citation Q4-SA-C015:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 210 (article dsw3leig1h4jocdmnengiw8s, إنشاء طلب جديد يدوياً) | 2026-03-14 | kind: stated | quote check: found
- quote: 3- وسائل دفع أخرى كالبطاقة الإئتمانية أو وسائل الدفع الآجل.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ة. تحديد العميل ابحث عن اسم العميل (في حال كان الطلب لعميل سابق) أو اضغط (+إضافة عميل جديد) في حال كان الطلب لعميل جديد، ثم ادخل بيانات العميل، واضغط (حفظ). لإرسال الطلب إلى شخص آخر فعّل خيار (ارسال الطلب لشخص آخر) وأدخل اسم المستلم وبريده الإلكتروني ورقم جواله، ثم اضغط (حفظ). الخطوة الثالثة. تحديد طريقة الدفع لدى العميل عدة طرق لدفع قيمة الطلب، وهي: 1- تحويل بنكي ، اختر البنك وارفع ايصال الدفع. 2- دفع عند الاستلام، حدد عمولة الدفع عند الاستلام. ⟪3- وسائل دفع أخرى كالبطاقة الإئتمانية أو وسائل الدفع الآجل.⟫ سيظهر قسم طريقة الدفع في الطلب بالشكل: الخطوة الرابعة. تحديد طريقة شحن الطلب حدد فيما إذا كان الطلب يحتاج إلى شحن أم لا. الحالة1- الطلب لا يحتاج شحن عندما تكون منتجات المتجر عبارة عن منتجات رقمية أو بطاقات رقمية أو استشارات فهي منتجات لا تحتاج إلى شحن. الحالة2- الطلب يحتاج شحن وتوصيل حدد هل الشحن مجاني أم مدفوع، ثم حدد شركة الشحن واضغط (حفظ). 💡ملاحظة: عند كتابة العنوان الوطني، ستظهر قائمة بالخيارات المطابقة، وبمجرد اختيار العنوان يتم تعبئة جميع …

### Q4-SA-P0080

**Cited at:** section 1, line 11; section 1, line 46; section 7, line 156

**Record** (`studies/proposals/records/Q4/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-079
- bullet: b;d
- placement: responsible
- identifier: المادة الثامنة – خدمات الدفع والسداد للمتاجر في منصة سلّة
- statement: ليس هناك أي علاقة لمنصة سلة بطريقة الدفع عند الاستلام، فطريقة الدفع هذه تخضع للعلاقة فيما بين المستهلك والتاجر ومزود الخدمة.
- cite_ids: S01-SA-C083
- from: new

**Citation S01-SA-C083:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 85 (المادة الثامنة – خدمات الدفع والسداد للمتاجر في منصة سلّة) | 2026-10-06 | kind: official page | quote check: found
- quote: ليس هناك أي علاقة لمنصة سلة بطريقة الدفع عند الاستلام، فطريقة الدفع هذه تخضع للعلاقة فيما بين المستهلك والتاجر ومزود الخدمة.
- in context: …ت التي ينضمون إليها أو البوليصات التي يستخدمونها. تحتفظ منصة سلّة بحقها في إضافة أو زيادة أو خفض أو خصم أي رسوم أو نفقات بموجب قواعد وأحكام اتفاقية الاستخدام، على أي من المستخدمين أياً كان سبب تسجيلهم. المادة الثامنة - خدمات الدفع والسداد للمتاجر في منصة سلّة: توفّر منصة سلة عبر شركائها نظام الدفع والسداد في منصة سلّة فيمكن أن يتم عبر الانترنت كلياً من خلال خيارات الدفع المتوفرة على منصة سلّة أو من خلال أي طريقة دفع توفرها منصة سلّة من حين لآخر. ⟪ليس هناك أي علاقة لمنصة سلة بطريقة الدفع عند الاستلام، فطريقة الدفع هذه تخضع للعلاقة فيما بين المستهلك والتاجر ومزود الخدمة.⟫ يجوز أن تشترط منصة سلة في أي وقت وأي حالٍ من الأحوال أن تتم عمليات الدفع مباشرةً بين التاجر والمستهلك، وعبر حساباتهم البنكية الخاصة بهم، وليس هناك أي علاقة حينئذٍ لمنصة سلة. إن توفير منصة سلّة لخدمة الدفع عبر الانترنت عن طريق المنصة هو بغرض التسهيل والمحافظة على حقوق التجار والمتاجر. يلتزم التاجر بتحديد سعر الخدمة أو البضاعة التي يقوم بعرضها في متجره وفقاً للقيمة السوقية المتعارف عليها، ولا علاقة لمنصة سلّة بأي حال من الأحوال بسوء تقدير تكلفة ال…

### Q4-SA-P0081

**Cited at:** section 1, line 11; section 7, line 157

**Record** (`studies/proposals/records/Q4/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-080
- bullet: a;d
- placement: decides
- identifier: المادة الثامنة – خدمات الدفع والسداد للمتاجر في منصة سلّة
- statement: يجوز أن تشترط منصة سلة في أي وقت وأي حالٍ من الأحوال أن تتم عمليات الدفع مباشرةً بين التاجر والمستهلك، وعبر حساباتهم البنكية الخاصة بهم، وليس هناك أي علاقة حينئذٍ لمنصة سلة.
- cite_ids: S01-SA-C084
- from: new

**Citation S01-SA-C084:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 86 (المادة الثامنة – خدمات الدفع والسداد للمتاجر في منصة سلّة) | 2026-10-06 | kind: official page | quote check: found
- quote: يجوز أن تشترط منصة سلة في أي وقت وأي حالٍ من الأحوال أن تتم عمليات الدفع مباشرةً بين التاجر والمستهلك، وعبر حساباتهم البنكية الخاصة بهم، وليس هناك أي علاقة حينئذٍ لمنصة سلة.
- in context: …ب قواعد وأحكام اتفاقية الاستخدام، على أي من المستخدمين أياً كان سبب تسجيلهم. المادة الثامنة - خدمات الدفع والسداد للمتاجر في منصة سلّة: توفّر منصة سلة عبر شركائها نظام الدفع والسداد في منصة سلّة فيمكن أن يتم عبر الانترنت كلياً من خلال خيارات الدفع المتوفرة على منصة سلّة أو من خلال أي طريقة دفع توفرها منصة سلّة من حين لآخر. ليس هناك أي علاقة لمنصة سلة بطريقة الدفع عند الاستلام، فطريقة الدفع هذه تخضع للعلاقة فيما بين المستهلك والتاجر ومزود الخدمة. ⟪يجوز أن تشترط منصة سلة في أي وقت وأي حالٍ من الأحوال أن تتم عمليات الدفع مباشرةً بين التاجر والمستهلك، وعبر حساباتهم البنكية الخاصة بهم، وليس هناك أي علاقة حينئذٍ لمنصة سلة.⟫ إن توفير منصة سلّة لخدمة الدفع عبر الانترنت عن طريق المنصة هو بغرض التسهيل والمحافظة على حقوق التجار والمتاجر. يلتزم التاجر بتحديد سعر الخدمة أو البضاعة التي يقوم بعرضها في متجره وفقاً للقيمة السوقية المتعارف عليها، ولا علاقة لمنصة سلّة بأي حال من الأحوال بسوء تقدير تكلفة المنتجات أو الخدمات المعروضة في المتاجر على منصة سلة، حيث إن تقديرها بالشكل المتعارف عليه تجارياً هو التزاماً واقع على عاتق التاجر. يلتزم التاجر بتوفير فواتير وسندات قبض وسندات…

### Q4-SA-015

**Cited at:** section 1, line 23; section 2, line 70; section 3, line 107

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-015
- bears_on: 1;3
- identifier: payment.receipt_img_desc
- statement: اختر صورة الإيصال البنكي
- cite_ids: Q4-SA-C032
- from: held

**Citation Q4-SA-C032:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/orders.json` | key "payment.receipt_img_desc" | 2026-10-12 | kind: observed | quote check: found
- quote: "receipt_img_desc":"اختر صورة الإيصال البنكي"
- in context: …قي عن 1.","amount_placeholder":"أدخل المبلغ","details":"تفاصيل الدفع","first_part_received":"تم استلام الدفعة الأولى من العميل","first_part_title":"الدفعة الأولى","receipt_browse":"أو تصفَّح من جهازك","receipt_drag_drop":"اسحب وأفلت الملف هنا","receipt_upload_label":"إرفاق إثبات الدفع","second_part_title":"الدفعة الثانية"},"partially_paid":"مدفوع جزئيًا","pending_desc":"يمكنك إرسال رابط الدفع للعميل من إجراءات الطلب.","pending_label":"غير مدفوع",⟪"receipt_img_desc":"اختر صورة الإيصال البنكي"⟫,"refund_amount":"إرجاع فارق المبلغ للعميل","refund_amount_desc":"فارق المبلغ الناتج عن تعديل الطلب: {{amount}}","refund_amount_label":"أعد فارق المبلغ للعميل","refund_exceed_limit":"تم تجاوز الحد الأقصى لمبلغ الاسترجاع.","refund_expired":"انتهت المهلة المسموح بها للاسترجاع وفقًا لشروط المدفوعات السعودية.","refund_limit_hint":"لا يمكن استرجاع مبلغ يتجاوز قيمة المنتجات المسترجعة.","refund_method":"تحديد طريقة الاسترجاع","refund_points.cashback":"ر…

### Q4-SA-074

**Cited at:** section 1, line 23; section 2, line 70; section 3, line 113

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-074
- bears_on: 1;3
- identifier: Storefront checkout, Payment: Bank transfer details
- statement: Bank transfer details Upload your bank transfer receipt and enter the sender's name so we can verify your payment. [x] Give me 24 hours Confirm payment Sender account holder name [Test Order] Upload your transfer receipt.
- scope: store مرحبا بكم في متجر الرصاصي للعطور الرسمي (store.rasasi.com.sa), observed 2026-10-09
- cite_ids: Q4-SA-C109
- from: held

**Citation Q4-SA-C109:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261009T112238Z-journey-storefront-account-order-en/steps/039.text.txt` | step 39 (https://store.rasasi.com.sa/en/checkout/[hidden field]?lang=en&&has_apple_pay=true) | 2026-10-09 | kind: observed | quote check: found
- step 39: Upload your transfer receipt: the test image (it says no money was sent) | https://store.rasasi.com.sa/en/checkout/[hidden field]?lang=en&&has_apple_pay=true | "Shipping & delivery - مرحبا بكم في متجر الرصاصي للعطور الرسمي" | 2026-10-09T11:47:21.938Z
- the step's files: `observed-sa@4ca2e896a:raw/runs/20261009T112238Z-journey-storefront-account-order-en/steps/039.aria.yaml`, `observed-sa@4ca2e896a:raw/runs/20261009T112238Z-journey-storefront-account-order-en/steps/039.text.txt`
- quote: Bank transfer details Upload your bank transfer receipt and enter the sender's name so we can verify your payment. [x] Give me 24 hours
- in context: …y address RHOD6998 - Test order - no money sent - please cancel - Saudi Arabia - Riyadh - حي العليا - King Fahd Branch Road,6998 Edit Carrier أرامكس, من 2 - 4 يوم عمل ربما تزيد بسبب قهري Additional Information and Preferences Edit Payment Bank transfer Bank transfer Select bank account ساب - RUKN ALRASASI TRADING ONE PERSON COMPANY Account holder RUKN ALRASASI TRADING ONE PERSON COMPANY Account number 011-717170-002 IBAN SA4645000000011717170002 ⟪Bank transfer details Upload your bank transfer receipt and enter the sender's name so we can verify your payment. [x] Give me 24 hours⟫ Confirm payment Sender account holder name [Test Order] Upload your transfer receipt. [ ] Business purchase For businesses or organizations: Enter your company name, tax ID, and commercial registration for your invoice. Confirm payment مع كل طلب لك نصيب من الخير سنتبرع بجزء من قيمة طلبك لجمعية ركن الحوار

### Q4-SA-018

**Cited at:** section 1, line 25; section 2, line 66

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-018
- bears_on: 3
- identifier: settings.complete_customization.form.under_review_desc (under_review_label: قيد المراجعة)
- statement: عند الدفع عبر التحويل البنكي أو الدفع عند الاستلام، أو عند الدفع الإلكتروني دون تفعيل خيار "تعيين حالة 'تم التنفيذ' عند الطلب بالدفع الإلكتروني".
- scope: صفحة تأكيد الطلب
- cite_ids: Q4-SA-C037;Q4-SA-C036
- from: held

**Citation Q4-SA-C037:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/orders.json` | key "settings.complete_customization.form.under_review_desc" | 2026-10-12 | kind: observed | quote check: found
- quote: "under_review_desc":"عند الدفع عبر التحويل البنكي أو الدفع عند الاستلام، أو عند الدفع الإلكتروني دون تفعيل خيار
- in context: … بعد إتمام الطلب.","form":{"completed":"تم التنفيذ","completed_desc":"عند الدفع الإلكتروني مع تفعيل خيار \"تعيين حالة 'تم التنفيذ' عند الطلب بالدفع الإلكتروني\".","completed_label":"تم التنفيذ","hero_title_placeholder":"العنوان الرئيسي","messages_label":"رسائل ما بعد إتمام الطلب","messages_label_desc":"أضف رسائل مُخصَّصة تظهر للعميل بناءً على حالة الطلب.","pending_payment_desc":"عند طلب العميل مهلة للدفع.","pending_payment_label":"بانتظار الدفع",⟪"under_review_desc":"عند الدفع عبر التحويل البنكي أو الدفع عند الاستلام، أو عند الدفع الإلكتروني دون تفعيل خيار⟫ \"تعيين حالة 'تم التنفيذ' عند الطلب بالدفع الإلكتروني\".","under_review_label":"قيد المراجعة"},"label":"صفحة تأكيد الطلب"},"digital_products_notify":{"desc":"حدِّد قنوات إرسال محتوى المنتجات الرقمية بعد شرائها لعملائك.","form":{"digital_code_email":"البريد الإلكتروني","digital_code_sms":"رسالة نصية (SMS)","placeholder":"اختر القنوات المناسبة"},"label":"إرسال محتوى المنتجات الرقمية"},"disable_bank_transfer_payment_period":{"desc":"سيتوجب على العم…

**Citation Q4-SA-C036:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/orders.json` | key "settings.complete_customization.form.under_review_label" | 2026-10-12 | kind: observed | quote check: found
- quote: "under_review_label":"قيد المراجعة"
- in context: …ted_label":"تم التنفيذ","hero_title_placeholder":"العنوان الرئيسي","messages_label":"رسائل ما بعد إتمام الطلب","messages_label_desc":"أضف رسائل مُخصَّصة تظهر للعميل بناءً على حالة الطلب.","pending_payment_desc":"عند طلب العميل مهلة للدفع.","pending_payment_label":"بانتظار الدفع","under_review_desc":"عند الدفع عبر التحويل البنكي أو الدفع عند الاستلام، أو عند الدفع الإلكتروني دون تفعيل خيار \"تعيين حالة 'تم التنفيذ' عند الطلب بالدفع الإلكتروني\".",⟪"under_review_label":"قيد المراجعة"⟫},"label":"صفحة تأكيد الطلب"},"digital_products_notify":{"desc":"حدِّد قنوات إرسال محتوى المنتجات الرقمية بعد شرائها لعملائك.","form":{"digital_code_email":"البريد الإلكتروني","digital_code_sms":"رسالة نصية (SMS)","placeholder":"اختر القنوات المناسبة"},"label":"إرسال محتوى المنتجات الرقمية"},"disable_bank_transfer_payment_period":{"desc":"سيتوجب على العميل إتمام التحويل البنكي وإرفاق الإيصال لإتمام الطلب.","label":"تعطيل مهلة الدفع عند التحويل ال…

### Q4-SA-045

**Cited at:** section 1, line 25; section 2, line 67

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-045
- bears_on: 3
- identifier: تخصيص متى يتم تحويل الطلب إلى تمّ التنفيذ
- statement: تخصيص متى يتم تحويل الطلب إلى تمّ التنفيذ؛ لتجنب إشكالية سوء فهم العميل لحالة "تم التنفيذ" في خيارات مثل الدفع عند الاستلام أو في طلبات بعض المنتجات مثل منتج حسب الطلب.
- cite_ids: Q4-SA-C075
- from: held

**Citation Q4-SA-C075:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 758 (article v5jrh4oz46bfkh8u0dnnlk8v, تخصيص إعدادات الطلبات) | 2026-09-01 | kind: stated | quote check: found
- quote: تخصيص متى يتم تحويل الطلب إلى تمّ التنفيذ؛ لتجنب إشكالية سوء فهم العميل لحالة "تم التنفيذ" في خيارات مثل الدفع عند الاستلام أو في طلبات بعض المنتجات مثل منتج حسب الطلب.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …يث حالة الطلب باستيراد ملف إكسل وتتضمن المراحل التالية: تصدير الطلبات إلى ملف إكسل، ثمَّ تعديل حالة الطلبات حسب المطلوب، ثمَّ حفظ الملف، ثمَّ رفع ملف الإكسل بالضغط على استيراد. 12. تقليص الطلبات غير الجادة والمرتجعات خطوات إعداد الإقرار قبل الشراء لتقليص الطلبات غير الجادة والمرتجعات. 13. استعادة الطلبات والمنتجات المحذوفة طريقة استعادة المنتجات والطلبات التي تم حذفها في ال30 يومًا الماضية من متجرك. 14. تخصيص متى يُحول الطلب إلى تم التنفيذ خطوات ⟪تخصيص متى يتم تحويل الطلب إلى تمّ التنفيذ؛ لتجنب إشكالية سوء فهم العميل لحالة "تم التنفيذ" في خيارات مثل الدفع عند الاستلام أو في طلبات بعض المنتجات مثل منتج حسب الطلب.⟫ 15. إكمال الطلب للسلات المتروكة إكمال الطلب للسلات المتروكة من تفاصيل الطلب. 16. إضافة خدمة حسب الطلب ويُقصد بخدمة حسب الطلب: جميع المنتجات أو الخدمات التي لا يمكن تسعيرها بشكل مباشر، ويتم تحديد السعر النهائي لها بعد مفاوضات مع العميل. 17. إدارة استرجاع الطلبات طريقة إرجاع طلب بالكامل مع إرجاع قيمة الطلب أو جزء منها للعميل، وكذلك كيفية التعديل على الطلب المسترجع من ناحية الأسعار أو الكمية بزيادتها أو إنقاصها. 18. إدارة بوليصات الشحن كيفية استخدا…

### Q4-SA-047

**Cited at:** section 1, line 26; section 2, line 75

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-047
- bears_on: 3;4
- identifier: 8- تعطيل مهلة الدفع في التحويل البنكي
- statement: عند تعطيل المهملة سيتوجب على العميل إجراء التحويل البنكي مباشرة وإرفاق إيصال الدفع عند إكمال الطلب.
- cite_ids: Q4-SA-C077
- from: held

**Citation Q4-SA-C077:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 758 (article v5jrh4oz46bfkh8u0dnnlk8v, تخصيص إعدادات الطلبات) | 2026-09-01 | kind: stated | quote check: found
- quote: عند تعطيل المهملة سيتوجب على العميل إجراء التحويل البنكي مباشرة وإرفاق إيصال الدفع عند إكمال الطلب.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …زون تلقائياً بناء على حالة الطلب 1. من صفحة إعدادات الطلبات، اضغط ( إعادة المخزون تلقائياً بناء على حالة الطلب). 2. عيّن خيار إعادة المخزون تلقائياً بناء على حالة الطلب. 7- تنبيه الحد الأعلى لوزن الطلب يتيح لك هذا الخيار تحديد الحد الأعلى لوزن الطلبات. وعند تجاوزه، سيظهر تنبيه للتاجر في صفحة الطلب. وأيضا سيظهر تنبيه أثناء تغيير حالة مجموعة طلبات إلى تم التنفيذ، مع توضيح أرقام الطلبات التي تجاوزن الحد الأعلى. 8- تعطيل مهلة الدفع في التحويل البنكي ⟪عند تعطيل المهملة سيتوجب على العميل إجراء التحويل البنكي مباشرة وإرفاق إيصال الدفع عند إكمال الطلب.⟫ 9- عرض مؤشر الشحن يظهر للعميل شريط يدل على أن شحن الطلب مجاني. بالشكل: 10- تفعيل إعادة الطلب يمكنك توفير الوقت بشكل كبير لعملائك في إعادة طلب المنتجات. بدلاً من العودة إلى صفحة المنتجات وتسجيل الدخول والبحث عن المنتجات التي يرغبون في تكرار طلبها مرة أخرى ، يمكن للعملاء الآن إعادة طلب المنتجات بالكامل بنقرة واحدة فقط. 🎯 تنبع أهمية ميزة إعادة الطلب من تمكين العملاء من الاستمرار في الشراء دون إضاعة الوقت والجهود. سيظهر للعميل زر إعاد الطلب في أسفل …

### Q4-SA-009

**Cited at:** section 1, line 28; section 2, line 77

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-009
- bears_on: 3
- identifier: ❓ ماذا أفعل إذا لم تتوفر شروط الإرجاع؟
- statement: في حال تعذر إرجاع المبلغ من خلال سلة، يمكنك استخدام إحدى الطرق التالية: تحويل المبلغ مباشرة إلى الحساب البنكي للعميل بعد الحصول على رقم الآيبان الخاص به. إضافة المبلغ إلى محفظة العميل داخل المتجر ليتمكن من استخدامه في عمليات شراء لاحقة.
- cite_ids: Q4-SA-C021;Q4-SA-C022;Q4-SA-C023
- from: held

**Citation Q4-SA-C021:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 60 (article lwd3jzhb0qs7v51b50rcc50a, إدارة استرجاع الطلبات) | 2026-09-03 | kind: stated | quote check: found
- quote: في حال تعذر إرجاع المبلغ من خلال سلة، يمكنك استخدام إحدى الطرق التالية:
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ا يوجد حد زمني مماثل، ويمكن تنفيذ الإرجاع وفق سياسات بوابة الدفع. ❓هل ظهور حالة "الاسترجاع قيد المعالجة" في إيصال الاسترجاع يعني أن المبلغ وصل للعميل؟ ليس بالضرورة. ظهور حالة "الاسترجاع قيد المعالجة" يعني أن طلب الاسترجاع تم تنفيذه وإرساله للمعالجة، ولكن قد يستغرق وصول المبلغ إلى العميل وقتًا إضافيًا، وذلك حسب بوابة الدفع وطريقة الدفع المستخدمة. يمكنك متابعة حالة الاسترجاع من تفاصيل الطلب حتى تكتمل العملية. ❓ ماذا أفعل إذا لم تتوفر شروط الإرجاع؟ ⟪في حال تعذر إرجاع المبلغ من خلال سلة، يمكنك استخدام إحدى الطرق التالية:⟫ تحويل المبلغ مباشرة إلى الحساب البنكي للعميل بعد الحصول على رقم الآيبان الخاص به. إضافة المبلغ إلى محفظة العميل داخل المتجر ليتمكن من استخدامه في عمليات شراء لاحقة. خدمات مساندة: يمكنك تحسين تجربة استرجاع الطلبات باستخدام تطبيق ريتيرن بلس أو تطبيق يم الذي يقدم حلولاً فعّالة لإدارة الطلبات المرتجعة وتنظيمها بسهولة. يساعد التطبيق في تتبع المرتجعات بشكل دقيق، مما يساهم في تسريع العملية وتحسين رضا العملاء. ldhl8u3zmgwdqcspg7fkvadc https://help.salla…

**Citation Q4-SA-C022:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 60 (article lwd3jzhb0qs7v51b50rcc50a, إدارة استرجاع الطلبات) | 2026-09-03 | kind: stated | quote check: found
- quote: تحويل المبلغ مباشرة إلى الحساب البنكي للعميل بعد الحصول على رقم الآيبان الخاص به.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ور حالة "الاسترجاع قيد المعالجة" في إيصال الاسترجاع يعني أن المبلغ وصل للعميل؟ ليس بالضرورة. ظهور حالة "الاسترجاع قيد المعالجة" يعني أن طلب الاسترجاع تم تنفيذه وإرساله للمعالجة، ولكن قد يستغرق وصول المبلغ إلى العميل وقتًا إضافيًا، وذلك حسب بوابة الدفع وطريقة الدفع المستخدمة. يمكنك متابعة حالة الاسترجاع من تفاصيل الطلب حتى تكتمل العملية. ❓ ماذا أفعل إذا لم تتوفر شروط الإرجاع؟ في حال تعذر إرجاع المبلغ من خلال سلة، يمكنك استخدام إحدى الطرق التالية: ⟪تحويل المبلغ مباشرة إلى الحساب البنكي للعميل بعد الحصول على رقم الآيبان الخاص به.⟫ إضافة المبلغ إلى محفظة العميل داخل المتجر ليتمكن من استخدامه في عمليات شراء لاحقة. خدمات مساندة: يمكنك تحسين تجربة استرجاع الطلبات باستخدام تطبيق ريتيرن بلس أو تطبيق يم الذي يقدم حلولاً فعّالة لإدارة الطلبات المرتجعة وتنظيمها بسهولة. يساعد التطبيق في تتبع المرتجعات بشكل دقيق، مما يساهم في تسريع العملية وتحسين رضا العملاء. ldhl8u3zmgwdqcspg7fkvadc https://help.salla.sa/article/%D8%A5%D8%AF%D8%A7%D8%B1%D8%A9-%D8%A7%D9%84%D8%A7%D8%B4%D8%AA%D8%B1%D8…

**Citation Q4-SA-C023:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 60 (article lwd3jzhb0qs7v51b50rcc50a, إدارة استرجاع الطلبات) | 2026-09-03 | kind: stated | quote check: found
- quote: إضافة المبلغ إلى محفظة العميل داخل المتجر ليتمكن من استخدامه في عمليات شراء لاحقة.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: … بالضرورة. ظهور حالة "الاسترجاع قيد المعالجة" يعني أن طلب الاسترجاع تم تنفيذه وإرساله للمعالجة، ولكن قد يستغرق وصول المبلغ إلى العميل وقتًا إضافيًا، وذلك حسب بوابة الدفع وطريقة الدفع المستخدمة. يمكنك متابعة حالة الاسترجاع من تفاصيل الطلب حتى تكتمل العملية. ❓ ماذا أفعل إذا لم تتوفر شروط الإرجاع؟ في حال تعذر إرجاع المبلغ من خلال سلة، يمكنك استخدام إحدى الطرق التالية: تحويل المبلغ مباشرة إلى الحساب البنكي للعميل بعد الحصول على رقم الآيبان الخاص به. ⟪إضافة المبلغ إلى محفظة العميل داخل المتجر ليتمكن من استخدامه في عمليات شراء لاحقة.⟫ خدمات مساندة: يمكنك تحسين تجربة استرجاع الطلبات باستخدام تطبيق ريتيرن بلس أو تطبيق يم الذي يقدم حلولاً فعّالة لإدارة الطلبات المرتجعة وتنظيمها بسهولة. يساعد التطبيق في تتبع المرتجعات بشكل دقيق، مما يساهم في تسريع العملية وتحسين رضا العملاء. ldhl8u3zmgwdqcspg7fkvadc https://help.salla.sa/article/%D8%A5%D8%AF%D8%A7%D8%B1%D8%A9-%D8%A7%D9%84%D8%A7%D8%B4%D8%AA%D8%B1%D8%A7%D9%83-%D9%81%D9%8A-%D8%A8%D8%A7%D9%82%D8%A7%D8%AA-%D8%B3%D9%84%D8%A9-%D8%B9%D8%…

### Q4-SA-013

**Cited at:** section 1, line 30; section 2, line 86

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-013
- bears_on: 3
- identifier: ❓كيف سيتم التعامل بخصوص البوليصات مع الحوالة البنيكة؟
- statement: في هذه الحالة لن تُخصم بوليصة من رسوم الطلب، و سيتم الخصم من الرصيد في حال كان هناك رصيد متوفر لدى التاجر، أو ستظهر للتاجر رسالة تفيد بضرورة شحن الرصيد في حال رصيده لا يكفي المبلغ المطلوب.
- scope: بوليصات سلة
- cite_ids: Q4-SA-C027
- from: held

**Citation Q4-SA-C027:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 83 (article mdke7ybzpze7jnsiiloylga2, إدارة بوليصات الشحن) | 2026-09-01 | kind: stated | quote check: found
- quote: في هذه الحالة لن تُخصم بوليصة من رسوم الطلب، و سيتم الخصم من الرصيد في حال كان هناك رصيد متوفر لدى التاجر، أو ستظهر للتاجر رسالة تفيد بضرورة شحن الرصيد في حال رصيده لا يكفي المبلغ المطلوب.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …حفظة والفواتير ❓ما الإجراء المتبع إذا كان رصيد محفظة متجري أقل من قيمة البوليصة؟ من صفحة الطلب، وعند ضغط (إصدار البوليصة). ❓كيف سيتم التعامل مع الرسوم الجمركية والرسوم الاضافية للشحن الدولي مع DHL ؟ ستتم التسوية من خلال رصيد المحفظة. ❓أين ستظهر حركة البوليصات، بالمحفظة أم بأرشيف البوليصات؟ ستظهر حركة البوليصات في المحفظة وفي البوليصات. - في المحفظة كمبلغ مالي. - في ارشيف البوليصات سجل تفصيلي. ❓كيف سيتم التعامل بخصوص البوليصات مع الحوالة البنيكة؟ ⟪في هذه الحالة لن تُخصم بوليصة من رسوم الطلب، و سيتم الخصم من الرصيد في حال كان هناك رصيد متوفر لدى التاجر، أو ستظهر للتاجر رسالة تفيد بضرورة شحن الرصيد في حال رصيده لا يكفي المبلغ المطلوب.⟫ ❓هل تدعم البوليصات في حالة الدفع عند الاستلام؟ الشركات التي تدعم الدفع عند الاستلام من بوليصات سلة هي: أي مكان أرامكس J&T لمزيد من لتفاصيل حول تفعيل وإدارة الدفع عند الاستلام مع بوليصات سلة ❓كيف سنتعامل مع الشحن الشحن المجاني، وفي حالة قيمة الشحن أقل أو أكثر من قيمة الشحن المعتمدة في الشركة؟ على سبيل المثال: في حال الشحن مع DHL تساوي 30 ريال، والتاجر زاد أو نقص من تبويب التسعيرة الخاص بالشركة، كيف سيتم تغطية الفرق أو التعامل معه؟ ستتم التعامل وت…

### Q4-SA-049

**Cited at:** section 1, line 31; section 2, line 87

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-049
- bears_on: 3
- identifier: payment_methods_description (payment_methods: طرق الدفع المستخدمة)
- statement: يوضِّح توزيع المدفوعات حسب طريقة الدفع في الفترة الزمنية المحددة.
- cite_ids: Q4-SA-C079;Q4-SA-C080
- from: held

**Citation Q4-SA-C079:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/reportsv2.json` | key "payment_methods_description" | 2026-10-12 | kind: observed | quote check: found
- quote: يوضِّح توزيع المدفوعات حسب طريقة الدفع في الفترة الزمنية المحددة.
- in context: ….","payment_fees":"رسوم الدفع الإلكتروني","payment_fees_description":"الرسوم التي يفرضها مزوِّدو خدمات الدفع مقابل معالجة عمليات الدفع الإلكتروني (مثل: رسوم البطاقات الائتمانية) خلال الفترة المحددة.","payment_fees_formula":"رسوم الدفع الإلكتروني = إجمالي رسوم الدفع الإلكتروني / إجمالي الطلبات","payment_fees_title":"رسوم الدفع الإلكتروني","payment_method_cost":"رسوم طرق الدفع","payment_methods":"طرق الدفع المستخدمة","payment_methods_description":"⟪يوضِّح توزيع المدفوعات حسب طريقة الدفع في الفترة الزمنية المحددة.⟫","payment_methods_formula":"طرق الدفع = إجمالي طرق الدفع / إجمالي الطلبات","payments":"المدفوعات","payments_reports":"تقارير المدفوعات","percentage_of_abandoned_carts_from_addition_to_cart":"نسبة السلات المتروكة من إجمالي الإضافة للسلة","percentage_of_orders_requested_from_bank":"نسبة الطلبات المطالبة من البنك","performance":"الأداء","performance_description":"الأداء هو الأداء المتاح للمستخدمين.","performance_formula":"الأداء = إجمالي الأداء / إ…

**Citation Q4-SA-C080:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/reportsv2.json` | key "payment_methods" | 2026-10-12 | kind: observed | quote check: found
- quote: "payment_methods":"طرق الدفع المستخدمة"
- in context: …n":"تمثِّل نسب قبول المدفوعات لكل وسيلة دفع خلال الفترة الزمنية المحددة.","payment_fees":"رسوم الدفع الإلكتروني","payment_fees_description":"الرسوم التي يفرضها مزوِّدو خدمات الدفع مقابل معالجة عمليات الدفع الإلكتروني (مثل: رسوم البطاقات الائتمانية) خلال الفترة المحددة.","payment_fees_formula":"رسوم الدفع الإلكتروني = إجمالي رسوم الدفع الإلكتروني / إجمالي الطلبات","payment_fees_title":"رسوم الدفع الإلكتروني","payment_method_cost":"رسوم طرق الدفع",⟪"payment_methods":"طرق الدفع المستخدمة"⟫,"payment_methods_description":"يوضِّح توزيع المدفوعات حسب طريقة الدفع في الفترة الزمنية المحددة.","payment_methods_formula":"طرق الدفع = إجمالي طرق الدفع / إجمالي الطلبات","payments":"المدفوعات","payments_reports":"تقارير المدفوعات","percentage_of_abandoned_carts_from_addition_to_cart":"نسبة السلات المتروكة من إجمالي الإضافة للسلة","percentage_of_orders_requested_from_bank":"نسبة الطلبات المطالبة من البنك","performance":"الأداء","performance_des…
