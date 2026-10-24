# Reviews every candidate in candidates.tsv (Q1 Salla re-pass, 11 October 2026).
# list-entry candidates: rules per list, with the explicit drops below; first-run candidates: one decision each.
# Writes work/reviewed.tsv (kept and moved statements) and final/review-log.tsv (every move and drop).
# Usage: python3 -I review.py
import sys, os, re, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

cand = rd(f"{SP}/candidates.tsv")
cit = {r["cite_id"]: r for r in rd(f"{FIRST}/citations.tsv")}
inv = rd(f"{FIRST}/inventory.tsv")
inv_by_cite = collections.defaultdict(list)
for r in inv:
    inv_by_cite[r["cite_id"]].append(r)

NAV_SOURCES = ("dashboard-settings-menu", "dashboard-main-navigation", "partners-portal-navigation", "dashboard-translations/en/settings.json")

# ---------- list-entry: explicit drops (concern, cite) -> reason ----------
LE_DROP = {}
def le_drop(cids, cites, reason):
    for c in cids.split():
        for s in cites.split():
            LE_DROP[(c, s)] = reason
le_drop("SA-C-234 SA-C-203", "SA-S-1005", "The entry is the Merchant API docs page 'Support'; it names no API resource, event or scope of this concern.")
le_drop("SA-C-203", "SA-S-1096 SA-S-1097 SA-S-1099", "A Partners Agent Kit docs section (Getting Started, Setup, Support) is a guide, not the kit's interface.")
le_drop("SA-C-203", "SA-S-1101 SA-S-1102 SA-S-1103", "A Salla Apps Playbook docs section is a guide, not an API, event or extension target.")
le_drop("SA-C-203", "SA-S-1108", "The Salla CLI docs section 'Additional Resources' (upgrade, troubleshooting) is a guide, not a command group.")
le_drop("SA-C-197", "SA-S-1091", "The Embedded SDK docs section 'Resources' (support, common examples) is a guide, not a module or endpoint.")
le_drop("SA-C-090", "SA-S-1119 SA-S-1132 SA-S-1133 SA-S-1134 SA-S-1135 SA-S-1136 SA-S-1137",
        "A Twilight Engine docs section that is a guide (architecture overview, getting started, review, file structure, Twig, change log), not a template surface a theme implements.")
le_drop("SA-C-190 SA-C-192", "SA-S-1157", "The docs navbar entry names the Merchant API as a whole; the entry itself doesn't name this concern.")
le_drop("SA-C-194 SA-C-199", "SA-S-1170", "The docs navbar entry names the App API as a whole; the entry itself doesn't name this concern.")
le_drop("SA-C-194", " ".join(f"SA-S-{n}" for n in list(range(1188, 1206)) + list(range(1221, 1231)) + [1184]),
        "An App Store category or app type names a subdivision of the App Store; it doesn't say where the App Store itself lives.")
le_drop("SA-C-200", "SA-S-1716", "The settings key names WhatsApp verification for customer login; it doesn't name communication apps.")
le_drop("SA-C-026", "SA-S-1730", "The settings key names market selection; it doesn't name branches or warehouses.")
le_drop("SA-C-115", "SA-S-1876", "The navigation link names the Wallet page; it doesn't say cash on delivery is there.")
le_drop("SA-C-112", "SA-S-1881", "The navigation link names Store Verification; it doesn't name the bank account for receiving dues.")
le_drop("SA-C-200", " ".join(c["cite_ids"] for c in cand if c["identifier"] == "whatsapp_chat_browse"),
        "The permission names WhatsApp chat browsing; it doesn't name communication apps.")
le_drop("SA-C-020 SA-C-040 SA-C-140 SA-C-110 SA-C-073 SA-C-096 SA-C-033 SA-C-160 SA-C-161",
        " ".join(f"SA-S-{n}" for n in list(range(2155, 2164)) + list(range(2174, 2179))),
        "A row of the plans page's comparison table; the held text has the row's title but not which plans have it, so it states no availability.")
le_drop("SA-C-194", "SA-S-2188", "The Special plan heading names integrations with programs and tools; it doesn't name the App Store.")
le_drop("SA-C-234", "SA-S-2197", "The Special plan heading claims platform stability; it states no availability or control.")
le_drop("SA-C-194", "SA-S-2098 SA-S-2147", "The plan line names integrations with outside services (Google Analytics, Zapier); it doesn't name the App Store.")

def le_placement(c):
    """Rules per list (task brief): a list entry answers where/boundary only when its list is a location or
    boundary structure, and decides only when the item itself states availability or control."""
    note = c["note"]
    if note == "list other:order-statuses":
        return "move:boundary", "The order statuses are the Merchant API's answer for the store (GET /admin/v2/orders/statuses); each is a record that API resource returns, not a location."
    return "keep", ""

def plan_scope(cite_id):
    loc = cit[cite_id]["locator"]
    src = cit[cite_id]["source"]
    m = re.search(r"\(plan ([^)]+)\)", loc)
    if m:
        return "plan: " + m.group(1)
    if "com-specialplan" in src:
        return "plan: سلة سبيشل"
    return ""

STAFF_GROUP = {}
for l in open(f"{OSA}/structures/salla/staff-permission-groups/demo@en/items.jsonl", encoding="utf-8"):
    g = json.loads(l)
    for p in g.get("permissions", []):
        STAFF_GROUP[p["name"]] = g["label"]
PARTNER_GROUP = {}
for l in open(f"{OSA}/structures/salla/portal-stores-access-requests-permissions/partner@en/items.jsonl", encoding="utf-8"):
    g = json.loads(l)
    for p in g.get("permissions", []):
        PARTNER_GROUP[p["key"]] = g["name"]["ar"] + " / " + g["name"]["en"]

# ---------- first-run: one decision per candidate, by its order in candidates.tsv ----------
# idx|action|scope|reason (log; for keep: none)|note (statement)
D = r"""
006|drop||The quote is a price-unit label ('SAR / yearly'); the plan and price are on other lines.|
007|drop||The quote is a price-unit label ('AED / yearly'); the plan and price are on other lines.|
008|drop||A row of the plans page's comparison table; the held text doesn't show which plans have it.|
009|drop||A row of the plans page's comparison table; the held text doesn't show which plans have it.|
010|drop||The quote is the question line only; the answer 'بدون عمولة منصة' is on other lines.|
012|drop||It says what the store balance is used for; it doesn't place it. Kept under boundary.|
013|drop||It says what the store balance is used for; it states no condition or value. Kept under boundary.|
014|keep|||
015|keep|||
016|keep|||Item of the list introduced by 'قد يحصل فشل في سحب رصيد محفظة لأحد الأسباب التالية:'.
017|keep|||Item of the list introduced by 'قد يتأخر تحويل المبلغ إلى حسابك البنكي في الحالات التالية:'.
019|keep|||It states what the store balance pays for: the plan's renewal, purchases from Salla's store and shipping labels.
020|keep|||
021|keep|الإمارات (article: إنشاء متجر جديد خارج السعودية - الإمارات)||
022|keep|السعودية (article: توثيق متجرك الجديد في السعودية)||
023|keep|الإمارات (article: توثيق متجرك في الإمارات)||
024|keep|الكويت (article: توثيق متجرك في الكويت)||
025|keep|السعودية (article: توثيق متجرك الجديد في السعودية)||
026|move:decides|الإمارات (article: إنشاء متجر جديد خارج السعودية - الإمارات)|It tells the merchant to set the store's legal entity, which determines the licences needed; that is who decides, and it states no legal responsibility.|
027|keep|السعودية (article: توثيق متجرك الجديد في السعودية)||
028|drop||Salla's team reviewing the request is a decision step, kept under decides; it names no API, event or contract.|
029|keep|الإمارات (article: توثيق متجرك في الإمارات)||
030|keep|||
031|keep|السعودية (article: توثيق متجرك الجديد في السعودية)||Under the heading 'لماذا يجب توثيق متجرك؟'.
032|keep|||
042|drop||The clause makes partners responsible for the content they provide; applying it to access to a merchant's store would be inference. Written as a gap.|
057|drop||The settings key names market selection, not branches or warehouses.|
079|keep|||
080|keep|||
090|keep|||The operation names the Customer Wallet as an application on apps.salla.sa that must be installed.
096|move:decides|the answering store (merchant@en)|A feature flag states the feature's value for the store; it doesn't say where the concern lives.|
097|move:decides|the answering store (merchant@en)|A feature flag states the feature's value for the store; it doesn't say where the concern lives.|
098|keep|||
099|keep|الأفراد المواطنين أو المقيمين في المملكة||
100|keep|||
101|drop||Already kept under decides; it names no API, event or contract.|
102|move:responsible|التطبيقات المنشورة في متجر تطبيقات سلة|A clause of the App Store terms stating an obligation of published apps; that is what the terms state, not an API or event.|
109|keep|||
120|keep|||
121|keep|||
124|drop||An event-list item is an event, already kept under boundary; it doesn't say where the concern lives.|
125|keep|||
127|keep|||
128|keep|||
130|keep|||
132|keep|||
133|drop||The quoted status line (line 22) names the Merchant APIs component, not Mahally.|
138|keep|||A component of Salla's status page at status.salla.sa.
139|keep|||
140|keep|الإمارات||Answer to 'ما طرق الدفع المتاحة عبر مدفوعات سلة في الإمارات؟'.
141|keep|الكويت||Answer to 'ماهي طرق الدفع المتاحة عبر مدفوعات سلة في الكويت؟'.
142|keep|الإمارات (article: تفعيل مدفوعات سلة في الإمارات)||Under 'متطلبات تفعيل مدفوعات سلة'.
143|keep|الإمارات (article: تفعيل مدفوعات سلة في الإمارات)||Under 'متطلبات تفعيل مدفوعات سلة'.
144|keep|||
145|keep|||
146|keep|الإمارات (article: تفعيل مدفوعات سلة في الإمارات)||Under 'متطلبات تفعيل مدفوعات سلة'.
147|keep|الإمارات (article: تفعيل مدفوعات سلة في الإمارات)||
148|keep|الكويت (article: تفعيل طرق الدفع في المتجر - الكويت)||Under 'متطلبات تفعيل مدفوعات سلة'.
149|keep|الكويت||
150|keep|الإمارات (article: تفعيل مدفوعات سلة في الإمارات)||
151|keep|||
152|move:decides||Accepting the selling policy is a step that activation requires, so it answers who decides; it names no API or event.|A step of 'خطوات تفعيل المدفوعات الإلكترونية'.
153|move:responsible|الإمارات (article: تحويلات مدفوعات سلة والتسويات في الإمارات)|It names the contract that governs settlement, which is what the terms state; it names no API or event.|The contract's parties are not stated.
154|keep|||
155|drop||The step is the merchant choosing the transfer cycle, kept under decides; it doesn't place the concern.|
156|keep|||
157|keep|||
158|keep|||
159|keep|الإمارات||
160|keep|الكويت||
161|keep|باقة بلس||From the older article (المقالة الجديدة - إدارة طرق الدفع وتفعيل المدفوعات الإلكترونية); a newer article lets the merchant choose the cycle.
162|keep|باقة برو||From the older article; see SA-S-0078 for the newer wording.
163|keep|باقة سلة سبيشل||From the older article; see SA-S-0078 for the newer wording.
164|keep|سلة سبيشل||
165|keep|الكويت||The same page also says 'بحد أدنى للتحويل دينار كويتي واحد' (SA-S-0086); recorded, not resolved.
166|keep|المتاجر الرقمية||
167|keep|||
168|keep|||
169|keep|الإمارات||
170|move:responsible|الإمارات (article: تحويلات مدفوعات سلة والتسويات في الإمارات)|It names the contract that governs settlement, which is what the terms state; it names no API or event.|The contract's parties are not stated.
171|move:responsible|الكويت (article: تحويلات مدفوعات سلة والتسويات في الكويت)|It names the contract that governs settlement, which is what the terms state; it names no API or event.|The contract's parties are not stated.
172|move:decides||It defines the transfer cycle as what sets when payments are transferred, which answers who decides; it names no API or event.|
173|keep|||
174|keep|||
175|keep|||
176|keep|الإمارات||
177|keep|الكويت||
178|keep|الكويت||
179|keep|||
180|keep|الإمارات||
181|drop||The Payments API group lists payment methods and the banks shown for bank transfer; it doesn't name the bank account for receiving dues.|
182|drop||It explains how to use the fees calculator; it doesn't place the concern.|
183|keep|الإمارات||
184|keep|سلة سبيشل||Description under the heading 'رسوم مرنة لبوابة الدفع'.
185|keep|||
186|move:boundary||It states what the shopping-experience fee covers (card and address saving, Apple Pay quick checkout, fraud protection), which is how the fee meets those services; it sets no value.|
187|move:responsible|الإمارات|It names the contract under which fees are calculated, which is what the terms state; it names no API or event.|The contract's parties are not stated.
188|drop||It explains how to use the fees calculator; it names no API, event or contract.|
189|drop||The VAT on fees is kept under decides; it names no API, event or contract.|
190|move:responsible|الإمارات|It names the contract that governs settlement, the only Salla statement on the party behind settlement; it names no API or event.|The contract's parties are not stated, so who processes or acquires is still not shown.
191|move:responsible|الكويت|It names the contract that governs settlement, the only Salla statement on the party behind settlement; it names no API or event.|The contract's parties are not stated, so who processes or acquires is still not shown.
192|drop||The transfer days are a value, kept under decides; it doesn't place the concern.|
193|drop||The quote is the list's lead-in only; a new statement quotes the list itself.|
194|keep|||
195|keep|||
196|keep|||
197|keep|||
198|keep|الإمارات||Under the heading 'عبر بوليصات سلة المخفضة' (cash on delivery).
200|keep|||
201|keep|||
202|move:responsible||It states that Salla does not take on collecting cash-on-delivery amounts here, which is a statement of Salla's role; it doesn't place the concern.|Answer to 'هل تقوم سلة بتحصيل مبالغ الدفع عند الاستلام عند استخدام شركة شحن خارج نطاق بوليصات سلة؟'.
203|drop||Kept under responsible and decides; it doesn't place the concern.|
204|keep|الإمارات||
205|keep|||
206|keep|الإمارات||
207|keep|||Answer to 'هل تقوم سلة بتحصيل مبالغ الدفع عند الاستلام عند استخدام شركة شحن خارج نطاق بوليصات سلة؟'.
208|drop||Kept under where and decides; it names no API or event.|
209|keep|الإمارات||
210|keep|||
211|drop||It states how the account is used; it states no condition or value.|
212|keep|||
213|drop||A plan line answers who decides and is kept there from the plan list.|
214|keep|||The list of deferred-payment methods follows the quote on the page.
215|drop||An answer listing the methods available in a market is kept under decides; it doesn't place the concern.|
216|drop||An answer listing the methods available in a market is kept under decides; it doesn't place the concern.|
217|keep|الإمارات||Answer to 'ما خيارات «اشترِ الآن وادفع لاحقًا» المتاحة؟'.
218|keep|الكويت||Answer to 'ماهي خيارات (اشترِ الآن وادفع لاحقًا) المتاحة؟'. The same page's table lists 'ديما، تالي'; recorded, not resolved.
219|move:boundary||It says the merchant services team helps open a Tabby or Tamara account for the store, which is how the concern meets the providers; it sets no value.|
220|keep|||Dashboard text shown when applying for an account with a provider; {{name}} is the provider's name.
221|keep|الإمارات||
222|keep|||
223|keep|الإمارات||
224|keep|||
225|keep|الإمارات||
226|drop||Kept under where and decides; it names no API or event.|
227|move:decides|الإمارات|An answer on whether a method is available states availability, which is who decides; it names no API or event.|Answer to 'هل PayPal متاح؟'.
228|keep|||
229|keep|||
230|drop||Kept under boundary; it states no condition or value.|
231|keep|||
232|keep|||
233|keep|||Salla's own words on who collects the payments when a gateway is connected; the merchant's contract with the gateway is not quoted.
234|keep|||
235|drop||Kept under where.|
237|keep|||
238|keep|||
239|keep|||
240|move:decides||A precondition for a refund is a condition, which answers who decides.|
241|move:boundary||An API operation is how the concern meets the rest; the operation doesn't place the concern.|
242|drop||Kept under decides (the same quote).|
243|drop||It states what the endpoint does, kept under boundary; it states no condition.|
244|keep|||
245|drop||It describes what the feature does; it doesn't place it. The docs navbar entry 'Recurring Payments API' is kept under where.|
246|keep|||
247|keep|||The key charity_payments.description is the payments namespace's text for charity stores.
248|keep|||
249|keep|||
250|keep|||
251|keep|||
252|move:responsible||It names the agreement the merchant approves (اتفاقية الوكالة بالاستثمار), which is what the terms state; it names no API or event.|
253|keep|||
254|keep|||
255|drop||A plan line answers who decides and is kept there from the plan list.|
256|drop||The quote is the list's lead-in only; a new statement quotes the list itself.|
257|drop||The sentence is about cash on delivery through the labels, kept under SA-C-115.|
259|keep|||
260|keep|||
261|keep|الإمارات||
262|move:boundary|الإمارات|It says cash-on-delivery amounts are followed through the carrier activated under an outside contract, which is how the concern meets the carrier; it sets no value.|
264|keep|||
266|keep|||
268|keep|||
270|keep|||
271|keep|||
272|keep|||
273|keep|||
274|keep|المملكة العربية السعودية||
275|keep|||
276|drop||It states who pays the fee, kept under decides; it states no legal responsibility.|
278|keep|||
279|keep|||
280|keep|||
283|keep|||
284|keep|||
285|keep|||
286|keep|||
288|move:decides||The merchant's settings decide whether the tax number and taxes show on invoices and the storefront.|
289|keep|||
290|keep|||The feature registry gives zatca the type 'app' and an app_id.
291|keep|المملكة العربية السعودية||
292|keep|باقة برو وسبيشل||Answer to whether the ZATCA link is available on all plans.
293|move:boundary||A statement that the platform works with ZATCA e-invoicing is how the concern meets the authority; it sets no value.|
294|keep|||
295|keep|||
296|keep|||
298|move:reason||It is a reason Salla states; it is not a boundary.|The reason given for tip 4, 'استخدم IOSS عند البيع لدول الاتحاد الأوروبي'.
299|keep|||
300|keep|||
301|keep|||
302|keep|||
303|keep|||Description of the automatic option of the markets product-price setting.
305|drop||A plan line answers who decides and is kept there from the plan list.|
306|move:decides||A statement of how many currencies the platform supports states a value; it names no API or event.|The plan list says '+33' currencies (SA-S-1970); recorded, not resolved.
307|drop||Kept under decides (the same quote).|
308|keep|||
309|keep|الإمارات||
310|keep|الكويت||
311|drop||Kept under decides; it names no API or event.|
312|drop||Kept under decides; it names no API or event.|
313|keep|||
314|keep|أي دولة أو منطقة من دول الخليج||
315|keep|||
316|keep|باقة سبيشل||
317|keep|||
318|drop||The settings key is a loyalty-program page; it states nothing about how markets meet the rest.|
319|keep|||
320|keep|||Salla's statement of its own primary markets.
321|keep|countries: AE, SA, KW, QA, OM, BH||
322|drop||The quote is the label 'Available in' only; the markets are on other lines.|
323|move:decides||The store's country determines the documents required, which is who decides; it names no API or event.|
324|keep|||
325|keep|||The usage policy is accepted at sign-up.
326|move:responsible|متجر تطبيقات سلة|A clause of the App Store terms stating an obligation; that is what the terms state.|
327|keep|||The selling policy is accepted when e-payments are activated.
328|keep|||
329|keep|||
330|keep|||
331|move:responsible||The forum for disputes is what the terms state about legal responsibility; it is not an API or event.|
332|keep|||
333|keep|||The capture account's own app record; cited only to show that the record carries a contract.
334|keep|||The capture account's own app record.
335|keep|الإمارات||
336|keep|الكويت||
337|move:decides|الإمارات|What the contract governs (settlement and transfer) is what sets those values; it names no API or event.|
338|drop||Kept under decides (the same quote).|
340|move:boundary||OAuth 2.0 is the method at the boundary; it doesn't place the concern.|
341|keep|||
342|drop||The clause covers the use of apps in general; applying it to app authorization would be inference. Written as a gap.|
343|keep|||
344|drop||The scope entry is kept under boundary from the scope list; it doesn't place the concern.|
345|keep|||
346|keep|||
348|drop||The webhook event is kept under boundary from the event list; it doesn't place the concern.|
349|drop||The docs navbar entry names the App API as a whole; it doesn't name app events.|
350|keep|||
351|drop||The quoted status line (line 22) names the Merchant APIs component, not the App Store.|
352|keep|||
353|keep|||
354|keep|||The joining policy covers every partner track, app developers included (المادة الأولى).
355|keep|||
356|keep|||
357|move:responsible||The forum for disputes is what the terms state about legal responsibility; it is not an API or event.|
358|keep|||
359|keep|||
360|keep|||
361|keep|||
362|keep|||
363|keep|||
364|keep|||
365|keep|||
366|drop||The payout filter's status options name statuses; they state no API, event or contract.|
367|keep|||Reason stated in the clause: 'مقابل خدمات الاستضافة والتكامل'.
368|drop||It describes what App Functions are; the statement that Salla manages them is kept under where.|
369|keep|||
370|keep|||
371|keep|||
372|keep|||
373|keep|||
374|keep|||
375|keep|||
376|keep|||
377|keep|||
378|keep|||
379|drop||Kept under decides (the same quote).|
380|keep|||
381|keep|||
382|keep|||
383|keep|||
384|keep|||
385|keep|||
386|move:decides||A consequence of exceeding limits is a limit, which answers who decides.|
387|keep|||
388|drop||Kept under boundary and reason.|
389|keep|||
390|keep|||
391|keep|||
392|keep|||
393|keep|||
394|drop||The clause is about the content partners provide; a new statement quotes the clause on the partner's account.|
395|move:decides||A condition for being a partner is an eligibility condition, which answers who decides.|
397|keep|||
398|keep|||
400|keep|||
401|keep|||The joining policy covers affiliates and influencers as partners (المادة الأولى).
403|keep|||
404|keep|||
405|keep|||
406|keep|||One of the measures listed under المادة (14) 6: 'يحق لسلة اتخاذ الإجراءات التنظيمية أو التشغيلية المناسبة عند مخالفة السياسات'.
407|keep|||
411|keep|||
412|keep|||
413|keep|||
414|keep|||
415|keep|||
416|keep|||
417|keep|||
418|keep|||
419|drop||Kept under responsible; it names no API or event.|
420|drop||Kept under responsible; it names no API or event.|
421|drop||It names the payment services contract but not its parties, so it shows no entity.|
422|move:responsible||A statement of the platform's nationality is a legal-entity statement; it names no API or event.|
423|keep|||
424|keep|الإمارات||
425|keep|||
426|drop||A general clause on complying with Saudi law; it doesn't speak of licences or regulated activity.|
427|drop||A general clause on complying with laws; it doesn't speak of licences or regulated activity.|
428|keep|||
429|move:decides|الإمارات (article: إنشاء متجر جديد خارج السعودية - الإمارات)|It tells the merchant to set the store's legal entity, which determines the licences needed; that is who decides.|
430|drop||Kept under decides (the same quote).|
431|drop||Kept under reason (the same quote).|
432|move:decides||A condition for being accepted as a partner is an eligibility condition, which answers who decides.|
433|keep|السعودية (article: توثيق متجرك الجديد في السعودية)||
434|keep|||
435|keep|||
436|keep|||
437|keep|||
438|keep|||
439|keep|||
440|keep|السعودية (article: توثيق متجرك الجديد في السعودية)||
441|move:decides|الكويت|A requirement of verification is a condition, which answers who decides.|
442|drop||Kept under decides (the same quote).|
443|move:boundary||TLS on the REST APIs is how the APIs meet the rest; it doesn't place the concern.|
444|keep|||A line of Salla's status page at status.salla.sa.
445|keep|||
446|drop||Kept under boundary (the same quote); it states no condition.|
447|keep|||
448|drop||A blurb under 'Service Status'; it names no API, event or location.|
449|drop||A second status line; the status page is kept under where.|
450|drop||The clause is about sharing store data to register with a provider; it says nothing about a partner being unavailable.|
451|keep|العمولات في برنامج التسويق بالعمولة (privacy-affiliate-plans)||
452|keep|||
453|keep|||
454|drop||The status line names Salla's own component; it names no partner.|
"""
DEC = {}
for line in D.strip().splitlines():
    parts = line.split("|")
    idx, action, scope, reason, note = parts[0], parts[1], parts[2], parts[3], parts[4] if len(parts) > 4 else ""
    DEC[int(idx)] = (action, scope, reason, note)

def fr_pattern(c):
    s = c["structure"]
    if c["placement"] == "where" and "docs-sidebar/" in s and re.match(r"line \d+$", c["identifier"]):
        return ("keep", "", "", "")
    if c["placement"] == "boundary" and any(k in s for k in NAV_SOURCES):
        return ("move:where", "", "A settings or navigation entry is an admin section and route, which answers where; it is not an API, event or scope.", "")
    return None

def ident_for(c):
    cid = c["cite_ids"]
    loc = cit[cid]["locator"]
    if c["join"] == "list-entry":
        return c["identifier"]
    if inv_by_cite.get(cid):
        return inv_by_cite[cid][0]["entry"]
    loc = re.sub(r"\s*\(line \d+ of the (rendered text|markdown)\)", "", loc)
    loc = re.sub(r"\s*\(sequence diagram\)", "", loc)
    return loc.strip()

out, log = [], []
seen = set()
fr_i = 0
pending = []
for c in cand:
    key0 = (c["concern_id"], c["placement"], c["cite_ids"])
    if c["join"] == "list-entry":
        if (c["concern_id"], c["cite_ids"]) in LE_DROP:
            log.append({**c, "action": "drop", "reason": LE_DROP[(c["concern_id"], c["cite_ids"])]})
            continue
        action, reason = le_placement(c)
        scope, note = c["scope"], ""
        if c["note"] == "list plan-features":
            scope = plan_scope(c["cite_ids"])
            note = "Plan line."
        elif c["note"] == "list other:dashboard-features":
            if not scope:
                scope = "the answering store (merchant@en)"
                note = "Feature flag with no plans or countries; enabled and released are the answering store's values."
            else:
                note = "Feature flag; plans and countries as the registry states them; enabled and released are the answering store's values (merchant@en)."
        elif c["note"] == "list other:staff-permissions":
            note = "Staff permission, group " + STAFF_GROUP.get(c["identifier"], "?") + "."
        elif c["note"] == "list other:partner-access-permissions":
            note = "Permission a partner can request on a merchant's store, group " + PARTNER_GROUP.get(c["identifier"], "?") + "."
        elif c["note"] == "list other:order-statuses":
            scope = "the answering store (merchant@ar)"
        elif c["note"] == "list access-scopes" and c["identifier"] == "metadata":
            note = "The docs' access lines tie this scope to the concern's operations (metadata.read / metadata.read_write)."
        else:
            note = c["note"].replace("list ", "List: ")
    else:
        fr_i += 1
        dec = DEC.get(fr_i) or fr_pattern(c)
        if dec is None:
            sys.exit(f"no decision for first-run candidate {fr_i}: {key0}")
        action, scope, reason, note = dec
        if action == "drop":
            log.append({**c, "action": "drop", "reason": reason})
            continue
    newp = c["placement"]
    if action.startswith("move:"):
        newp = action.split(":")[1]
    key = (c["concern_id"], newp, c["cite_ids"])
    if key in seen:
        log.append({**c, "action": "drop", "reason": (reason + " " if action.startswith("move:") else "") + f"The same citation is already kept under {newp} for this concern."})
        continue
    if action.startswith("move:"):
        log.append({**c, "action": f"move to {newp}", "reason": reason})
    seen.add(key)
    out.append({"concern_id": c["concern_id"], "placement": newp, "structure": c["structure"], "identifier": ident_for(c),
                "statement": c["statement"], "scope": scope, "cite_ids": c["cite_ids"], "note": note, "origin": c["join"]})

# a move into a placement can collide with a list-entry candidate that comes later in the file: drop the later one
assert fr_i == 454, fr_i
wr(f"{SP}/work/reviewed.tsv", ST_COLS + ["origin"], out)
LOG_COLS = ["concern_id", "placement", "statement_start", "cite_ids", "action", "reason"]
wr(f"{SP}/final/review-log.tsv", LOG_COLS,
   [{"concern_id": r["concern_id"], "placement": r["placement"], "statement_start": r["statement"][:80],
     "cite_ids": r["cite_ids"], "action": r["action"], "reason": r["reason"]} for r in log])
print("kept", len(out), "log", len(log), collections.Counter(r["action"].split(" ")[0] for r in log))
print(collections.Counter((r["origin"], r["placement"]) for r in out))
