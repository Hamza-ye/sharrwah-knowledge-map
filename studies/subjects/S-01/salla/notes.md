# S-01, phase A: salla (SA)

Subject: who holds the merchant's funds between the buyer's payment and the merchant's payout.

## What I read

**Q1 index**, `studies/concern-map/platforms/salla/`: `concerns.tsv`, `statements.tsv`, `gaps.tsv`, `citations.tsv`. I read in full the statements and gaps of SA-C-005, 006, 095, 096, 098, 110 to 128, 140, 164, 167, 170, 172, 177, 230, 231, 235 and 304, and the concern list.

**Held**, observed-sa at `4ca2e896a729215f422a137a364e7e9488610ba3` (the working tree was clean at that commit):

- `structures/salla/com-policies/terms/text.txt` (salla.com/terms, all 623 lines; the agreement text appears twice on the page, the first copy is cited), `com-policies/payments/text.txt`, `com-policies/shipping/text.txt`, `com-policies/policies-selling/text.txt`.
- `structures/salla/partners-legal/apps-policy`, `privacy`, `themes-policy` (`text.txt`): searched for amounts, transfers and settlements. They concern partners' dues, not the merchant's sales money.
- `structures/salla/help-articles/ar/texts.jsonl` and `en/texts.jsonl`, with `items.jsonl` for titles and `last_update_at`: the whole corpus searched by pattern (balances, transfer cycle, payouts, settlement, contract, licence, central bank, withholding, countries, COD, BNPL, gateways). Read in full: دورة تحويل المدفوعات الإلكترونية (ar, en), تحويلات مدفوعات سلة والتسويات في الإمارات (ar, en), … في الكويت (ar, en), تفعيل المدفوعات الإلكترونية (ar, en), صفحة المحفظة, - محفظة المتجر, -دورة تحويل المدفوعات الإلكترونية, إعداد الحساب البنكي واسترداد رصيد متجرك, إعداد الحساب البنكي ونظام الحوالات السريع, إدارة الطلبات المشتبه بها, تفعيل وإدارة الدفع عند الاستلام مع بوليصات سلة, تفعيل طرق الدفع في المتجر (Saudi), تفعيل مدفوعات سلة في الإمارات, تفعيل طرق الدفع في المتجر - الكويت. Read in part (money-flow paragraphs): the Tabby, Tamara and Madfu articles, the UAE Tabby and Tamara articles, طريقة تفعيل خدمات التقسيط, PayPal, stc pay, مكافأة الراجحي, the charity-store articles (PayTabs, Moyasar, Apple Pay), إدارة استرجاع الطلبات, the Salla Point articles, the Mahally articles, أسئلة شائعة حول توثيق المتجر (both), مركز الإعدادات الموحد, - تعيين إعدادات الفوترة في المتجر, the five English Salla Capital articles.
- `structures/salla/dashboard-translations/ar/payments.json` and `en/payments.json` (all keys), `apps.json`, `orders.json`, `shipping.json`; the other Arabic namespaces searched for balance, transfer, withholding and deduction wording.
- `structures/salla/kyc-schema/demo@en/source.json` (the store verification form).
- `structures/salla/docs-operations/md-openapi/items.jsonl` (settlements and transactions operations).
- `structures/salla/dashboard-features/merchant@en/items.jsonl` (payment, wallet, COD and financing flags).
- `structures/salla/merchant-plans/merchant@ar`, `com-plans`, `com-specialplan` (ar-sa, en-sa, ar-ae).
- Fetch-archive records read with `method/warc_text.py`: `raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz@8607584` (salla.com/payments, text and raw) and `@28743756` (salla.com/en-sa/terms).

**Live**, read 2026-10-12: https://docs.salla.dev/1973350f0.md (Settlements; same descriptions as the held operations).

## What I couldn't read

- The answers to the four FAQ questions on salla.com/payments, among them «متى يتم تحويل المدفوعات من لوحة تحكم متجري إلى حسابي البنكي؟». They are collapsed: they are not in the held text, and the archived record holds the questions without the answers. salla.com is not among the live sources the brief allows for salla.
- The text and parties of عقد خدمات الدفع (payment services agreement). The UAE and Kuwait payout articles name it as signed during store verification; no held file carries it. `kyc-schema/demo@en` holds the verification form (owner, documents, bank account, review) with no contract text.
- No Arabic Salla Capital article is held. The five English articles describe eligibility, application and tracking, not the deduction from sales; the deduction is stated in the dashboard's `capital.*` text, which is cited.
- The English usage agreement (salla.com/en-sa/terms) is held only in fetch archives (`20261005T235211Z-com-en-scheme@4672139`, `20261006T030341Z-com-toplevel@28743756`). I read the second. It carries the platform's English for terms recorded here, for example "returning any pending amounts in electronic payments to consumers", "Saudi Central Bank", "the payment and settlement system". I did not cite it: see the first problem below.

## Not recorded one by one

About 200 carrier articles (120 in the Arabic section مقالات قديمة, 78 in the English section Older articles, 2 current) each answer «ما هي آلية تسوية المبالغ؟» or a similar question with that carrier's own settlement schedule. Recording each would pass the 150-statement cap. The general statements are recorded instead: Salla does not collect COD amounts for carriers outside بوليصات سلة, and those amounts are settled directly between the merchant and the carrier under their agreement (from SA-S-0120 and SA-S-0121).

## Problems with the method or the brief

- The checker reads a local source with `git show <commit>:<path>` and does not open gzipped fetch archives, so a quote cited to `raw/runs/.../fetch.warc.gz` is reported "not found". The brief asks for archive records to be cited by archive path and offset. I cited nothing from archives; the English translations that exist only in the archived English terms are therefore not in `terms.tsv`.
- The usage agreement names only سياسة الخصوصية وسرية المعلومات as a further policy binding the merchant. The selling policy (سياسة البيع) is accepted when e-payments are activated (help articles), and عقد خدمات الدفع is named in help articles; the usage agreement names neither. The selling policy page is Salla's own and lists prohibited products and services only.
- Some held statements disagree with each other. Each is recorded with a note and not resolved: the Kuwait minimum payout (KWD 1, and "لا يوجد حد أدنى للتحويل" on the same page); moving amounts from رصيد المدفوعات الإلكترونية to رصيد المتجر (allowed in تفعيل المدفوعات الإلكترونية, not allowed in the older - محفظة المتجر); when a suspicious order's amount reaches the e-payments balance (on completion by the merchant, or recorded before confirmation).
- Statements copied from the index keep their index citations: several are help.salla.sa pages read rendered on 2026-10-10 and cited by live URL, which wait for the coordinator's capture. The same articles are held in `help-articles` at the brief's commit; new statements from them cite the held copy.
- Statements from articles in the help centre's مقالات قديمة section carry a note saying so.
