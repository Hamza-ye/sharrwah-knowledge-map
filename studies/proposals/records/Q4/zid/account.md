# Q4 on Zid, against Shopify and Salla

## [1]

- **differs** (term): "تفعيل الدفع اليدوي": orders without electronic payment, from الطلبات > إنشاء طلب يدوي > معلومات الدفع. Against Shopify [1]: Q4-SH-001, Q4-SH-002, Q4-SH-K1737; Salla [1]: Q4-SA-007, Q4-SA-K0504. Q4-ZD-001, Q4-ZD-002
- **differs** (term): التحويل البنكي ("Bank Transfer Payment"): every plan. Against Salla [1]: Q4-SA-P0099, Q4-SA-P0068. Q4-ZD-K0126, Q4-ZD-P0142, Q4-ZD-P0150
- **differs** (role): bank accounts under إدارة طرق الدفع > الحسابات البنكية, each shown or hidden at payment. Against Salla [1]: Q4-SA-P0100 ("The bank account added"), Q4-SA-003 ("The merchant adds it"); Shopify [1]: Q4-SH-K1735 ("A seller picks"); Shopify [3]: Q4-SH-006. Q4-ZD-K0124, Q4-ZD-P0075, Q4-ZD-004, Q4-ZD-005
- **differs** (term): الدفع عند الاستلام ("Cash on Delivery"): every plan, set per carrier under لوحة التحكم > اللوجستيات; "Advanced Payment Methods" excludes starter. Against Salla [1]: Q4-SA-P0098, Q4-SA-K1530. Q4-ZD-K0113, Q4-ZD-K0110, Q4-ZD-K0111, Q4-ZD-K0097, Q4-ZD-P0074
- **differs** (role): the Terms make the merchant responsible for خدمة الدفع عند التوصيل, "خدمة مقدمة من طرف ثالث", and for bank transfer, under the bank's terms. Against Salla [1]: Q4-SA-P0080, Q4-SA-P0081. Q4-ZD-030, Q4-ZD-P0073, Q4-ZD-K0114, Q4-ZD-P0076, Q4-ZD-K0127, Q4-ZD-K0128
- **differs** (role): Zid "ليست طرفاً في العلاقة بين المستهلك والتاجر". Against Shopify [1]: Q4-SH-K1491, Q4-SH-K1492 ("Shopify's terms say"). Q4-ZD-029
- **differs** (role): بوابات الدفع الأُخرى (Paymob, amwal pay, Tap) stop when Zid Pay is activated. Against Salla [1]: Q4-SA-K1639, Q4-SA-K1656, Q4-SA-K1636. Q4-ZD-K0084, Q4-ZD-K0085, Q4-ZD-K0086, Q4-ZD-K0087, Q4-ZD-K0094, Q4-ZD-K0088
- **not in what was read:** who collects COD with the merchant's own carrier or courier. Against Salla [1]: Q4-SA-P0091 ("When the carrier is outside"), Q4-SA-P0199. Q4-ZD-N01
- **differs** (role): a زد كاشير session ends with cash and credit sales entered. Against Salla [3]: Q4-SA-042 ("Salla Point reports show"). Q4-ZD-033
- **not in what was read:** cashier payments through intermediaries. Against Salla [1]: Q4-SA-034, Q4-SA-035; Salla [3]: Q4-SA-036. Q4-ZD-N14
- **not in what was read:** the merchant's own PayPal or stc pay. Against Salla [1]: Q4-SA-K1626, Q4-SA-K1627. Q4-ZD-N15
- **not in what was read:** such payments in the merchant wallet. Against Salla [1]: Q4-SA-A0002. Q4-ZD-N16

## [2]

- **differs** (term): the help centre lists "الدفع عند الاستلام مع شركات التوصيل. التحويل البنكي."; also "الدفع اليدوي". Against Shopify [2]: Q4-SH-003, Q4-SH-004; Salla [2]: Q4-SA-K1604 ("The names in the dashboard"). Q4-ZD-K0098, Q4-ZD-001
- **differs** (role): codes `zid_bank_transfer` (Bank Transfer), `bank_transfer`, `zid_cod` (Cash on Delivery); webhook conditions `Cash On Delivery`, `Bank Transfer`. Against Salla [1]: Q4-SA-K1608 ("Bank transfer is a feature flag"); Salla [2]: Q4-SA-050. Q4-ZD-018, Q4-ZD-020, Q4-ZD-021, Q4-ZD-K0115, Q4-ZD-025
- **differs** (role): `zid_cop`: "Cash on Pickup". Against Salla [1]: Q4-SA-048. Q4-ZD-019
- **differs** (role): `pos-cash`; the payment methods API omits POS methods. Against Salla [1]: Q4-SA-031 ("Salla Point"). Q4-ZD-018, Q4-ZD-K0101
- **differs** (identifier): payment options may hold built-in `bank`. Against Salla [1]: Q4-SA-K1608 ("Bank transfer is a feature flag"). Q4-ZD-040
- **differs** (role): plan comparison lines for these methods. Against Salla [2]: Q4-SA-K1605 ("The plan feature lists"). Q4-ZD-K0126, Q4-ZD-K0113, Q4-ZD-K0118, Q4-ZD-K0097
- **not in what was read:** a method the merchant names. Against Shopify [2]: Q4-SH-007; Shopify [1]: Q4-SH-045. Q4-ZD-N07

## [3]

### حالة الطلب وحالة الدفع

- **differs** (role): invoices can show "مدفوع أو غير مدفوع"; `payment_status` pending, paid, failed, refunded; `unpaid` covers pending, refunded, voided. Against Shopify [3]: Q4-SH-K1736 ("Orders that use"), Q4-SH-018 ("Unpaid covers"). Q4-ZD-012, Q4-ZD-016, Q4-ZD-K0209
- **differs** (role): 6 statuses; carriers set جاري التوصيل and مكتمل; `order_status` has nine values. Against Salla [3]: Q4-SA-011. Q4-ZD-013, Q4-ZD-014, Q4-ZD-K0578, Q4-ZD-015
- **differs** (role): paid orders can move to مكتمل automatically. Against Salla [3]: Q4-SA-019. Q4-ZD-003
- **differs** (role): `cod_confirmed`. Against Salla [3]: Q4-SA-060 ("The order API's payment object"). Q4-ZD-017
- **goes beyond:** bank transfer can be paused. Q4-ZD-007
- **not in what was read:** what the customer sees while payment is awaited. Against Shopify [3]: Q4-SH-020; Salla [3]: Q4-SA-018. Q4-ZD-N08
- **not in what was read:** a transfer time limit. Against Salla [3]: Q4-SA-017. Q4-ZD-N10
- **not in what was read:** payment due dates or terms. Against Shopify [3]: Q4-SH-014. Q4-ZD-N09

### Payment Status

- **differs** (role): "Payment Status", "Bulk Payment Status Update"; `order.payment_status.update`. Against Shopify [3]: Q4-SH-005 ("After the seller receives"); Shopify [2]: Q4-SH-035 ("In the Admin API"). Q4-ZD-K0207, Q4-ZD-K0208, Q4-ZD-K0206
- **not in what was read:** an API call setting `payment_status` to paid. Against Shopify [3]: Q4-SH-039 ("`orderMarkAsPaid` creates"). Q4-ZD-N04
- **not in what was read:** partial payment. Against Shopify [3]: Q4-SH-035 ("`orderCreateManualPayment` records"), Q4-SH-021. Q4-ZD-N06
- **not in what was read:** an order field for the bank account or transfer receipt. Against Salla [3]: Q4-SA-015, Q4-SA-059. Q4-ZD-N05

### طرق الاسترداد

- **differs** (role): "طرق الاسترداد تعتمد على طريقة الدفع الأساسية للطلب"; credit notes follow cancelling when payment is "حوالة بنكية مؤكدة"; Reverse Orders has "Upload bank transfer receipt". Against Salla [3]: Q4-SA-008 ("Refund through Salla"); Shopify [3]: Q4-SH-K1492 ("The terms place refunds"). Q4-ZD-K0582, Q4-ZD-010, Q4-ZD-011, Q4-ZD-K0430
- **differs** (term): returns set the order to قيد الاسترجاع; the customer wallet returns amounts without refund invoices. Against Salla [3]: Q4-SA-010 ("Setting قيد الاسترجاع"), Q4-SA-009 ("Refund through Salla"). Q4-ZD-036, Q4-ZD-038
- **differs** (role): selling and invoicing need a زد كاشير session. Against Salla [3]: Q4-SA-032. Q4-ZD-034
- **goes beyond:** customer wallet balance doesn't cover COD fees. Q4-ZD-039

### الرسوم

- **differs** (role): a separate COD fee is deducted before transfer; some carriers add 10 SAR. Against Salla [3]: Q4-SA-P0059 ("With the merchant's own carrier"). Q4-ZD-K0119, Q4-ZD-P0125
- **differs** (role): labels and shipping fees come from the Zid wallet. Against Salla [3]: Q4-SA-013. Q4-ZD-K0581, Q4-ZD-K0328
- **goes beyond:** each API payment method carries `fees`. Q4-ZD-024
- **not in what was read:** a Zid fee on bank-transfer or manual orders. Against Shopify [3]: Q4-SH-K1740; Salla [3]: Q4-SA-K0051. Q4-ZD-N02

### التحليلات

- **differs** (role): analytics: "نسب استخدام طرق الدفع في متجرك"; total sales exclude cancelled orders; reports on some plans. Against Salla [3]: Q4-SA-049 ("Reports show"), Q4-SA-K0582 ("Statuses included"); Shopify [3]: Q4-SH-033. Q4-ZD-022, Q4-ZD-023, Q4-ZD-K0616
- **differs** (role): session reports in زد كاشير; `pos.analytics`. Against Salla [3]: Q4-SA-042 ("Salla Point reports show"). Q4-ZD-035, Q4-ZD-037
- **not in what was read:** COD orders or fees in reports. Against Salla [3]: Q4-SA-052, Q4-SA-051 ("Reports show"). Q4-ZD-N18
- **not in what was read:** shipping reports on COD collected. Against Salla [3]: Q4-SA-064, Q4-SA-065. Q4-ZD-N19
- **not in what was read:** amounts recorded in another currency. Against Shopify [3]: Q4-SH-026. Q4-ZD-N17
- **not in what was read:** deleting an order. Against Shopify [3]: Q4-SH-030. Q4-ZD-N11
- **not in what was read:** filtering orders by payment method. Against Salla [3]: Q4-SA-002. Q4-ZD-N12

## [4]

- **differs** (term): قيود الدفع (growth and up) conditions include cart value, location and cancelled orders, against "طلبات الدفع عند الاستلام الوهمية". Against Salla [4]: Q4-SA-055 ("Payment restrictions"), Q4-SA-022 ("Cash on delivery terms"), Q4-SA-020. Q4-ZD-K0356, Q4-ZD-K0357, Q4-ZD-K0358, Q4-ZD-K0359, Q4-ZD-026, Q4-ZD-027
- **differs** (role): "Block Cash on Delivery": growth and pro. Against Salla [4]: Q4-SA-055. Q4-ZD-K0112
- **differs** (role): COD per carrier area; none with Redbox and Parcels. Against Salla [4]: Q4-SA-K1591 ("Cash on delivery terms"). Q4-ZD-008, Q4-ZD-031, Q4-ZD-032
- **differs** (role): the IBAN must start with SA or AE. Against Salla [4]: Q4-SA-054. Q4-ZD-006, Q4-ZD-005
- **differs** (role): COD totals are converted between currencies. Against Shopify [4]: Q4-SH-K1739. Q4-ZD-028
- **differs** (role): `edit.store.orders`, `third_create_order`. Against Shopify [4]: Q4-SH-042 ("The API's"). Q4-ZD-K0420, Q4-ZD-K0425
- **goes beyond:** both can be offered to guest buyers. Q4-ZD-009
- **not in what was read:** test mode. Against Shopify [4]: Q4-SH-028. Q4-ZD-N13
- **not in what was read:** API error codes. Against Shopify [4]: Q4-SH-043 ("The API's"). Q4-ZD-N20

## [5]

- **differs** (role): with زد شب, Zid collects COD for the merchant and pays the wallet twice a month after fees; carriers owe the merchant nothing directly. Against Salla [5]: Q4-SA-P0041 ("The flow"); Shopify [5]: Q4-SH-045. Q4-ZD-K0122, Q4-ZD-P0070, Q4-ZD-K0117, Q4-ZD-K0121, Q4-ZD-P0072, Q4-ZD-K0123, Q4-ZD-P0071, Q4-ZD-K0118
- **differs** (role): COD up to 3750 SAR locally; none internationally or for instant service. Against Salla [5]: Q4-SA-062 ("With Salla shipping labels"). Q4-ZD-K0120, Q4-ZD-P0126, Q4-ZD-P0127, Q4-ZD-P0129, Q4-ZD-P0128
- **goes beyond:** Zid is "وسيطاً تقنياً" for shipping. Q4-ZD-K0335
- **not in what was read:** a view of COD not yet in the wallet. Against Salla [5]: Q4-SA-P0038 ("The wallet has"). Q4-ZD-N03
