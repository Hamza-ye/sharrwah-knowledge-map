# Q4 on Zid: sorted against Shopify and Salla

## [1]

- **differs** (term): "تفعيل الدفع اليدوي" creates orders with no electronic payment, from الطلبات > إنشاء طلب يدوي > معلومات الدفع. Against Shopify [1]: Q4-SH-001, Q4-SH-002, Q4-SH-K1737; Salla [1]: Q4-SA-007, Q4-SA-K0504. Q4-ZD-001, Q4-ZD-002
- **differs** (term): التحويل البنكي ("Bank Transfer Payment") is marked for every plan, starter included. Against Salla [1]: Q4-SA-P0099, Q4-SA-P0068. Q4-ZD-K0126, Q4-ZD-P0142, Q4-ZD-P0150
- **differs** (role): bank accounts are added under إدارة طرق الدفع > الحسابات البنكية, several at once, each shown or hidden on the payment page; banks are Saudi or Gulf. Against Salla [1]: Q4-SA-P0100 ("The bank account added"), Q4-SA-003 ("The merchant adds it"); Shopify [1]: Q4-SH-K1735 ("A seller picks"). Q4-ZD-K0124, Q4-ZD-P0075, Q4-ZD-004, Q4-ZD-005
- **differs** (term): الدفع عند الاستلام ("Cash on Delivery") is marked for every plan and set per carrier under لوحة التحكم > اللوجستيات; "Advanced Payment Methods", naming COD, excludes starter. Against Salla [1]: Q4-SA-P0098, Q4-SA-K1530. Q4-ZD-K0113, Q4-ZD-K0110, Q4-ZD-K0111, Q4-ZD-K0097, Q4-ZD-P0074
- **differs** (role): the Terms activate خدمة الدفع عند التوصيل on request and make the merchant responsible for it, "نظراً لكونها خدمة مقدمة من طرف ثالث", and for bank transfer services, under the bank's terms. Against Salla [1]: Q4-SA-P0080, Q4-SA-P0081. Q4-ZD-030, Q4-ZD-P0073, Q4-ZD-K0114, Q4-ZD-P0076, Q4-ZD-K0127, Q4-ZD-K0128
- **differs** (role): the Terms say Zid "ليست طرفاً في العلاقة بين المستهلك والتاجر". Against Shopify [1]: Q4-SH-K1491, Q4-SH-K1492 ("Shopify's terms say"). Q4-ZD-029
- **differs** (role): other gateways (Paymob, amwal pay, Tap) are reached under المدفوعات > بوابات الدفع الأُخرى; activating Zid Pay disables them. Against Salla [1]: Q4-SA-K1639, Q4-SA-K1656, Q4-SA-K1636. Q4-ZD-K0084, Q4-ZD-K0085, Q4-ZD-K0086, Q4-ZD-K0087, Q4-ZD-K0094, Q4-ZD-K0088
- **not in what was read:** who collects cash-on-delivery amounts when the merchant ships through its own carrier contract or its own courier. Against Salla [1]: Q4-SA-P0091 ("When the carrier is outside"), Q4-SA-P0199. Q4-ZD-N01

## [2]

- **differs** (term): the help centre lists "الدفع عند الاستلام مع شركات التوصيل. التحويل البنكي."; orders without electronic payment use "الدفع اليدوي". Against Shopify [2]: Q4-SH-003, Q4-SH-004; Salla [2]: Q4-SA-K1604 ("The names in the dashboard"). Q4-ZD-K0098, Q4-ZD-001
- **differs** (role): order payment codes include `zid_bank_transfer` (Bank Transfer), `bank_transfer` and `zid_cod` (Cash on Delivery); webhook conditions take `Cash On Delivery` and `Bank Transfer`. Against Salla [1]: Q4-SA-K1608 ("Bank transfer is a feature flag"); Salla [2]: Q4-SA-050. Q4-ZD-018, Q4-ZD-020, Q4-ZD-021, Q4-ZD-K0115, Q4-ZD-025
- **differs** (role): a payment code `zid_cop` is named "Cash on Pickup". Against Salla [1]: Q4-SA-048. Q4-ZD-019
- **differs** (role): `pos-cash` is a code; the payment methods API omits POS methods. Against Salla [1]: Q4-SA-031 ("Salla Point"). Q4-ZD-018, Q4-ZD-K0101
- **differs** (role): the plan comparison lists Bank Transfer Payment, Cash on Delivery, Cash on Delivery Collection and Advanced Payment Methods. Against Salla [2]: Q4-SA-K1605 ("The plan feature lists"). Q4-ZD-K0126, Q4-ZD-K0113, Q4-ZD-K0118, Q4-ZD-K0097
- **not in what was read:** a payment method the merchant creates and names. Against Shopify [2]: Q4-SH-007. Q4-ZD-N07

## [3]

### حالة الطلب وحالة الدفع

- **differs** (role): the invoice can show "مدفوع أو غير مدفوع"; `payment_status` lists pending, paid, failed, refunded; the webhook's `unpaid` covers pending, refunded, voided. Against Shopify [3]: Q4-SH-K1736 ("Orders that use"), Q4-SH-018 ("Unpaid covers"). Q4-ZD-012, Q4-ZD-016, Q4-ZD-K0209
- **differs** (role): 6 order statuses; the carrier sets جاري التوصيل and مكتمل; `order_status` takes nine values. Against Salla [3]: Q4-SA-011. Q4-ZD-013, Q4-ZD-014, Q4-ZD-K0578, Q4-ZD-015
- **differs** (role): paid orders can be set to move to مكتمل automatically. Against Salla [3]: Q4-SA-019. Q4-ZD-003
- **differs** (role): `cod_confirmed` says whether a COD order is confirmed. Against Salla [3]: Q4-SA-060 ("The order API's payment object"). Q4-ZD-017
- **goes beyond:** bank transfer can be paused, keeping the account data. Q4-ZD-007
- **not in what was read:** what the customer is shown or sent while such an order awaits payment. Against Shopify [3]: Q4-SH-020; Salla [3]: Q4-SA-018. Q4-ZD-N08
- **not in what was read:** a time limit for the customer's bank transfer. Against Salla [3]: Q4-SA-017. Q4-ZD-N10
- **not in what was read:** payment due dates or terms. Against Shopify [3]: Q4-SH-014. Q4-ZD-N09

### Payment Status

- **differs** (role): "Payment Status" and "Bulk Payment Status Update" are on every plan; `order.payment_status.update` fires on `paid` or `unpaid`. Against Shopify [3]: Q4-SH-005 ("After the seller receives"); Shopify [2]: Q4-SH-035 ("In the Admin API"). Q4-ZD-K0207, Q4-ZD-K0208, Q4-ZD-K0206
- **not in what was read:** an API operation that records a payment or sets `payment_status` to paid. Against Shopify [3]: Q4-SH-039 ("`orderMarkAsPaid` creates"). Q4-ZD-N04
- **not in what was read:** recording part of an order's amount as paid. Against Shopify [3]: Q4-SH-035 ("`orderCreateManualPayment` records"), Q4-SH-021. Q4-ZD-N06
- **not in what was read:** an order field for the store bank account or the customer's transfer receipt. Against Salla [3]: Q4-SA-015, Q4-SA-059. Q4-ZD-N05

### طرق الاسترداد

- **differs** (role): "طرق الاسترداد تعتمد على طريقة الدفع الأساسية للطلب"; a credit note obliges the merchant to refund; notices follow cancelling or editing when payment is "حوالة بنكية مؤكدة" or electronic; Reverse Orders has "Upload bank transfer receipt". Against Salla [3]: Q4-SA-008 ("Refund through Salla"); Shopify [3]: Q4-SH-K1492 ("The terms place refunds"). Q4-ZD-K0582, Q4-ZD-010, Q4-ZD-011, Q4-ZD-K0430

### الرسوم

- **differs** (role): Zid deducts a separate COD fee before transfer to the wallet; some carriers charge 10 SAR extra. Against Salla [3]: Q4-SA-P0059 ("With the merchant's own carrier"). Q4-ZD-K0119, Q4-ZD-P0125
- **differs** (role): return labels and direct shipping fees are taken from the Zid wallet. Against Salla [3]: Q4-SA-013. Q4-ZD-K0581, Q4-ZD-K0328
- **goes beyond:** each API payment method carries `fees`. Q4-ZD-024
- **not in what was read:** a Zid fee on bank-transfer or manual-payment orders. Against Shopify [3]: Q4-SH-K1740; Salla [3]: Q4-SA-K0051. Q4-ZD-N02

### التحليلات

- **differs** (role): analytics show "نسب استخدام طرق الدفع في متجرك"; total sales exclude only cancelled orders; reports are for some plans. Against Salla [3]: Q4-SA-049 ("Reports show"), Q4-SA-K0582 ("Statuses included"); Shopify [3]: Q4-SH-033. Q4-ZD-022, Q4-ZD-023, Q4-ZD-K0616
- **not in what was read:** deleting an order. Against Shopify [3]: Q4-SH-030. Q4-ZD-N11
- **not in what was read:** filtering orders by payment method. Against Salla [3]: Q4-SA-002. Q4-ZD-N12

## [4]

- **differs** (term): قيود الدفع (growth and higher plans) conditions include cart value, location and a customer's cancelled orders, against "طلبات الدفع عند الاستلام الوهمية"; an example hides bank transfer at 100 to 300 SAR. Against Salla [4]: Q4-SA-055 ("Payment restrictions"), Q4-SA-022 ("Cash on delivery terms"), Q4-SA-020. Q4-ZD-K0356, Q4-ZD-K0357, Q4-ZD-K0358, Q4-ZD-K0359, Q4-ZD-026, Q4-ZD-027
- **differs** (role): "Block Cash on Delivery" is marked for growth and pro. Against Salla [4]: Q4-SA-055. Q4-ZD-K0112
- **differs** (role): COD is set per carrier area; not with Redbox and Parcels. Against Salla [4]: Q4-SA-K1591 ("Cash on delivery terms"). Q4-ZD-008, Q4-ZD-031, Q4-ZD-032
- **differs** (role): the IBAN must start with SA or AE. Against Salla [4]: Q4-SA-054. Q4-ZD-006, Q4-ZD-005
- **differs** (role): for COD, partners convert totals when currencies differ. Against Shopify [4]: Q4-SH-K1739. Q4-ZD-028
- **differs** (role): `edit.store.orders` (staff) and `third_create_order` (drafts). Against Shopify [4]: Q4-SH-042 ("The API's"). Q4-ZD-K0420, Q4-ZD-K0425
- **goes beyond:** bank transfer and COD can be offered to guest buyers. Q4-ZD-009
- **not in what was read:** testing these methods without a real order. Against Shopify [4]: Q4-SH-028. Q4-ZD-N13

## [5]

- **differs** (role): with زد شب, Zid collects COD on the merchant's behalf and pays the wallet twice a month after fees (an FAQ: two working weeks); the merchant is owed nothing directly by carriers; a short wallet is covered from COD dues. Against Salla [5]: Q4-SA-P0041 ("The flow"); Shopify [5]: Q4-SH-045. Q4-ZD-K0122, Q4-ZD-P0070, Q4-ZD-K0117, Q4-ZD-K0121, Q4-ZD-P0072, Q4-ZD-K0123, Q4-ZD-P0071, Q4-ZD-K0118
- **differs** (role): local COD up to $1000 (3750 SAR); none for international or instant service; smart lockers online only. Against Salla [5]: Q4-SA-062 ("With Salla shipping labels"). Q4-ZD-K0120, Q4-ZD-P0126, Q4-ZD-P0127, Q4-ZD-P0129, Q4-ZD-P0128
- **goes beyond:** Zid calls itself "وسيطاً تقنياً" for shipping, not a carrier. Q4-ZD-K0335
- **not in what was read:** a view of COD amounts collected and not yet in the wallet. Against Salla [5]: Q4-SA-P0038 ("The wallet has"). Q4-ZD-N03
