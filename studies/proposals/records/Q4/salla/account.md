# Q4 on Salla: orders whose payment does not pass through Salla

## [1]

### Bank transfer (التحويل البنكي)

- On the basic plan (باقة بيسك) the merchant can turn on bank transfer, "حيث يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك"; electronic payment methods are only on paid plans. Q4-SA-P0099, Q4-SA-P0068
- The bank account added under payment methods (طرق الدفع) is used to receive customers' bank transfers and is shown to them at checkout. Q4-SA-P0100, Q4-SA-K1603, Q4-SA-021 (bank_transfer.empty.description: "أضف حسابًا بنكيًا لمتجرك لاستقبال الحوالات البنكية من عملائك.")
- The merchant adds it from the payment methods page, section التحويل البنكي, giving bank name, account holder, account number, IBAN and, optionally, an alternate identifier for SARIE (نظام الحوالات السريع), whose details then show on the checkout page. More than one account can be added. Q4-SA-003, Q4-SA-004, Q4-SA-006, Q4-SA-001
- Bank transfer is a feature flag (`bank`) enabled with no plan list, and a payment method key (`bank`) in the order data. Q4-SA-K1608, Q4-SA-050, Q4-SA-061
- In one store (real-merchant, `merchant_type` KSA), observed on 12 October 2026, the payment methods page listed under Other payment methods مكافآت الراجحي and الدفع عند الاستلام (`cod`, `"is_active": false`), and under Bank transfer one bank account of the store, Al Rajhi Bank. Q4-SA-067, Q4-SA-068, Q4-SA-069
- In one storefront's checkout (store.rasasi.com.sa), observed on 9 October 2026, bank transfer showed the store's account and asked: "Upload your bank transfer receipt and enter the sender's name so we can verify your payment.", with a "Give me 24 hours" option. Q4-SA-074

### Cash on delivery through the merchant's own carrier or courier

- On the basic plan the merchant can turn on cash on delivery, "ليتم تحصيل المبلغ عبر شركة الشحن أو من خلال مندوبك الخاص". Q4-SA-P0098, Q4-SA-K1530
- When the carrier is outside Salla shipping labels, "لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة", and the amounts are settled directly between merchant and carrier under their own agreement. Q4-SA-P0091, Q4-SA-P0092, Q4-SA-K1600, Q4-SA-K1598
- A merchant's own courier (مندوب) can offer cash on delivery where it collects amounts at delivery; settlement methods vary with each carrier's policy. Q4-SA-P0199, Q4-SA-P0202
- Branch pickup (الاستلام من الفرع) can be offered with cash on delivery and a cash-on-delivery fee. Q4-SA-048

### The usage agreement

- Article 8 of the usage agreement: Salla has no relation to the cash-on-delivery method, which is governed by the relation between consumer, merchant and service provider; and Salla may require at any time that payments be made directly between merchant and consumer through their own bank accounts, "وليس هناك أي علاقة حينئذٍ لمنصة سلة". Q4-SA-P0080, Q4-SA-P0081

### Orders created by the merchant, and Salla Point

- A manual order (إنشاء طلب جديد يدوياً) takes one of: bank transfer with the bank chosen and the receipt uploaded, cash on delivery with its commission, or other methods. Q4-SA-007, Q4-SA-K0504
- Salla Point (سلة بوينت), the point-of-sale product, takes cash (الدفع نقداً: "استلم المدفوعات مباشرة من العميل بشكل نقدي.") and lists bank transfer and cash among its methods; cash and payment link are available at once, card needs an application. Q4-SA-031, Q4-SA-038, Q4-SA-033, Q4-SA-039, Q4-SA-K1402
- Salla Point has custom payment methods (طرق الدفع المخصصة) "لتسجيل المدفوعات عبر الوسطاء (مثل جاهز، مرسول، هنقرستيشن)", for delivery apps or indirect payment sources. Q4-SA-034, Q4-SA-035

### Gateways and wallets the merchant connects

- With an external gateway, payments are collected through it instead of Salla Payments, using credentials from the merchant's own gateway account. Q4-SA-K1639, Q4-SA-K1656, Q4-SA-K1636
- PayPal is connected by entering the merchant's account details; stc pay can be connected directly or through Salla's gateway, and moving to the gateway cannot be undone. Q4-SA-K1626, Q4-SA-K1627
- Payments through Tabby, Tamara, Mokafaa Al Rajhi, PayPal, an external gateway or bank transfer have no tab in the wallet, whose tabs are store balance, electronic payments and cash-on-delivery payments. Q4-SA-A0002

## [2]

- The names in the dashboard and help: التحويل البنكي / تحويل بنكي (key `bank`), حوالة بنكية, الدفع عند الاستلام / دفع عند الاستلام (key `cod`, "Cash on delivery"), and in Salla Point الدفع نقداً / نقدًا, whose permission `salla_point_cod_orders` is named الطلبات النقدية in one source and طلبات الدفع عند الاستلام in another. Q4-SA-K1604, Q4-SA-K1579, Q4-SA-050, Q4-SA-054, Q4-SA-031, Q4-SA-038, Q4-SA-041, Q4-SA-K1426
- The plan feature lists file التحويل البنكي, نظام المدفوعات الفورية عبر سريع and الدفع عند الاستلام under the payment group. Q4-SA-K1604, Q4-SA-K1605, Q4-SA-K1580
- On a bank transfer order of the real-merchant store, the order's refund action names the method `"payment_method_label": "حوالة بنكية"`. Q4-SA-071

## [3]

### Recording the payment

- Orders can be filtered by payment method on the orders page. Q4-SA-002
- In the order, the merchant picks the bank receipt image (اختر صورة الإيصال البنكي), and for partial payments attaches proof of payment (إرفاق إثبات الدفع). Q4-SA-015, Q4-SA-016, Q4-SA-K0563
- The order API's payment object carries `store_bank_id`, `receipt_image_path` ("The URL link of the receipt image") and `cash_on_delivery` with its amount; a sample order payload shows `"payment_method": "bank"` with a `receipt_image` and status `under_review`. Q4-SA-059, Q4-SA-060, Q4-SA-061, Q4-SA-K0577
- Not found: how a merchant reviews a customer's bank transfer receipt and confirms the payment, and whether Salla takes part. Q4-SA-N02
- On a bank transfer order of the real-merchant store (order 24438069, created from the dashboard), observed on 12 October 2026, the order data held `"payment_method": "bank"` and a `receipt_image`, and the order page showed "Payment transferred" with "Al Rajhi Bank Bank transfer". Q4-SA-070, Q4-SA-072
- Its order activity showed محمد المغربي and AJEX changing the status, three times to بإنتظار المراجعة, then to تم الشحن and تم التوصيل. Q4-SA-073

### Order status

- The nine basic statuses are محذوف، بانتظار المراجعة، بانتظار الدفع، قيد التنفيذ، تم التنفيذ، ملغي، مسترجع، قيد الاسترجاع، طلب عرض سعر. Q4-SA-011, Q4-SA-K0598, Q4-SA-K0599
- The order confirmation page shows قيد المراجعة "عند الدفع عبر التحويل البنكي أو الدفع عند الاستلام" or electronic payment without auto-completion. Q4-SA-018
- The merchant can set an order to تم التنفيذ automatically when it is placed with cash on delivery, excluding product types; this is offered to avoid customers misreading "تم التنفيذ" for cash on delivery. Q4-SA-019, Q4-SA-045, Q4-SA-046
- Turning off the bank transfer payment period (تعطيل مهلة الدفع عند التحويل البنكي) requires the customer to transfer and attach the receipt to complete the order. Q4-SA-017, Q4-SA-047
- A confirmation message can be sent when an order paid on delivery is received. Q4-SA-063
- In Salla Point, a cash order is confirmed and then registered to send the invoice. Q4-SA-032

### Refunds

- Refund through Salla needs the payment method to be mada, Visa, Apple Pay or Tamara, with enough balance in the payments balance; otherwise the merchant can transfer the amount to the customer's bank account using their IBAN, or add it to the customer's wallet in the store. Q4-SA-008, Q4-SA-009
- Setting قيد الاسترجاع does not return the amount; bank transfer is not supported for automatic cashback refund, which goes to the customer wallet. Q4-SA-010, Q4-SA-053
- The same bank transfer order's refund action held `"has_refund_amount": false` and `"can_refund_to_wallet": true`. Q4-SA-071
- Salla Point reports show cash refunded from the drawer and drawer difference. Q4-SA-042, Q4-SA-043, Q4-SA-044

### Fees

- For bank transfer orders, the shipping label is not deducted from the order amount but from the merchant's balance, which must be topped up if short. Q4-SA-013
- With the merchant's own carrier, the merchant enters the cash-on-delivery commission agreed in its contract with the carrier; the merchant can raise or lower the COD fee from what the carrier charges. Q4-SA-P0059, Q4-SA-K1593, Q4-SA-K1588
- "بدون عمولة منصة على مبيعاتك" appears in the plan lines of سلة سبيشل. Q4-SA-K0051
- Not found: whether Salla charges any fee of its own on bank-transfer orders, or on cash on delivery through the merchant's own carrier. Q4-SA-N01

### Reports

- Reports show the distribution of payments by payment method, orders by type including الدفع عند الاستلام, and total costs that include cash-on-delivery fees. Q4-SA-049, Q4-SA-052, Q4-SA-051
- Shipping reports count confirmed cash-on-delivery orders and the share of COD shipments delivered and collected. Q4-SA-064, Q4-SA-065
- Statuses included in reports are set by the merchant (order-report-statuses, on plus, pro and special). Q4-SA-K0582, Q4-SA-K2501
- Salla Point custom payment methods are recorded in reports, and deleting one leaves past orders and reports unchanged. Q4-SA-036, Q4-SA-037

## [4]

- Bank transfer, cash on delivery and STC pay are currently for stores in Saudi Arabia only, and SARIE identifiers are for Saudi stores only; the dashboard says bank transfer is not available for some countries. Q4-SA-054, Q4-SA-005, Q4-SA-P0101
- Cash on delivery terms (شروط الدفع عند الاستلام): minimum and maximum order value, maximum cart weight, excluded categories and products, and hiding COD from customers banned in other Salla stores; the option must also be enabled in the carrier's settings. Q4-SA-022, Q4-SA-026, Q4-SA-027, Q4-SA-028, Q4-SA-029, Q4-SA-030, Q4-SA-066, Q4-SA-K1584, Q4-SA-K1591
- One cash-on-delivery order per customer per day can be set (تقييد طلبات الدفع عند الاستلام للعميل الواحد). Q4-SA-020
- Payment restrictions (قيود الدفع) can hide cash on delivery by cart value, customer group, category or market. Q4-SA-055, Q4-SA-056, Q4-SA-057, Q4-SA-058, Q4-SA-K1664
- A shipping label can be cancelled through support only if the order was paid electronically, not on delivery. Q4-SA-012
- In Salla Point, cash and the direct link remain available when the card subscription has lapsed. Q4-SA-040
- Not found: any limit on the amount of a bank-transfer order other than restrictions the merchant sets. Q4-SA-N03
- In the real-merchant store, observed on 12 October 2026, the cash on delivery settings excluded two categories (الأشمغة, منتجات دولية), and one order's data answered `"is_available": false` with ".خدمة الدفع عند الاستلام غير متاحة للتصنيفات في السلة". Q4-SA-075, Q4-SA-076

## [5]

- With Salla shipping labels, cash on delivery is offered for orders from SAR 20 to SAR 1,000, through the carriers listed (one article names Aymakan, Aramex and J&T; another adds SMSA, Redbox and Shipa); in the UAE the method is "coming soon". Q4-SA-062, Q4-SA-K1585, Q4-SA-K1586, Q4-SA-014, Q4-SA-P0095, Q4-SA-K1589
- The flow: the customer pays cash on delivery and the carrier transfers the amount to Salla; Salla transfers cash-on-delivery dues to the merchant's bank account on a schedule according to the plan, on Sundays and Wednesdays for label carriers. Q4-SA-P0041, Q4-SA-P0042, Q4-SA-P0039, Q4-SA-P0093, Q4-SA-K1587
- The wallet has a cash-on-delivery payments tab (المدفوعات عند الاستلام) showing dues from orders paid on delivery that will be transferred to the bank account, totals before fees and tax, and fees that include the carrier's COD fee and the purchase-experience fee. Q4-SA-P0038, Q4-SA-023, Q4-SA-024, Q4-SA-025, Q4-SA-K1590
- The real-merchant store's cash on delivery wallet page, observed on 12 October 2026, showed: "Customer pays on delivery", "The carrier transfers the payment to Salla", "Your dues are transferred to your bank account ending in 1444", and payouts "every Sunday and Wednesday". Q4-SA-078
- The Aramex card under Salla shipping labels in the demo store, observed on 9 October 2026, answered its question هل يتوفر الدفع عند الاستلام؟ with "نعم بوليصات سلة تدعم الدفع عن الإستلام". Q4-SA-077
- In the UAE and Kuwait, cash-on-delivery tracking is not in the wallet; the merchant follows amounts through the carrier activated under an external contract or its own courier. Q4-SA-K1602, Q4-SA-P0150
- The order API's `cash_on_delivery` object carries the amount for cash on delivery. Q4-SA-060
- Still open: who collects and holds cash-on-delivery amounts collected through Salla shipping labels before payout. Q4-SA-G0117, Q4-SA-H0008
