# Build the inventory entries from Zid's own lists, each with a source URL and a verbatim quote showing it.
import json, os, re, sys, csv
Z = sys.argv[1]; F = os.path.join(Z, "fetched")
sys.path.insert(0, os.path.join(Z, "scripts"))
out = []
def add(lst, entry, url, quote, locator, key):
    out.append(dict(list=lst, entry=entry, url=url, quote=quote, locator=locator, key=key))

# 1. API reference groups (docs.zid.sa navigation as listed in llms.txt, API Docs section)
sec = None; seen = {}
for line in open(os.path.join(F, "docs-llms.txt"), encoding="utf-8"):
    if line.startswith("## "): sec = line[3:].strip(); continue
    m = re.match(r"^- (.*?)\[([^\]]*)\]\((https://docs\.zid\.sa/[^)]*\.md)\)", line)
    if not m or sec != "API Docs": continue
    crumb = m.group(1).strip()
    if crumb in seen: continue
    seen[crumb] = 1
    q = f"{crumb} [{m.group(2)}]({m.group(3)})"
    add("api-resources", crumb, "https://docs.zid.sa/llms.txt", q, "## API Docs, first page listed under this group", "api:" + crumb)

# 2. Webhook events
wh = open(os.path.join(F, "docs", "webhooks.md"), encoding="utf-8").read()
for m in re.finditer(r"^\| ([a-z_.]+)( \[\(Supports `conditions`\)\]\(#event-conditions\))? \| ([^|]+?) \|", wh, re.M):
    q = f"{m.group(1)}{m.group(2) or ''} | {m.group(3).strip()}"
    add("webhook-topics", m.group(1), "https://docs.zid.sa/webhooks.md", q, "# Merchant Events tables", "wh:" + m.group(1))
ev = open(os.path.join(F, "docs", "events-878234m0.md"), encoding="utf-8").read()
for m in re.finditer(r"^\| `(app\.market\.[a-z_.]+)` \| ([^|]+?) \|", ev, re.M):
    add("webhook-topics", m.group(1), "https://docs.zid.sa/events-878234m0.md", f"`{m.group(1)}` | {m.group(2).strip()}", "## App Subscription Events table", "wh:" + m.group(1))
pw = open(os.path.join(F, "docs", "overview-1341008m0.md"), encoding="utf-8").read()
mq = re.search(r"Types:<br>“merchant_linked”,<br>“payment_paid”,<br>“refund_status_changed”", pw)
for t in ("merchant_linked", "payment_paid", "refund_status_changed"):
    add("webhook-topics", t, "https://docs.zid.sa/overview-1341008m0.md", mq.group(0), "Request Model, type", "wh:" + t)

# 3. Scopes (first page that names each)
for line in open(os.path.join(F, "docs", "scopes.tsv"), encoding="utf-8"):
    s, slug, raw = line.rstrip("\n").split("\t")
    if slug.startswith("docs/"):
        url = "https://docs.zid.sa/" + slug[5:]
        q = "Ensure you include the `embedded_apps_tokens_write` scope in your initial OAuth request."
        loc = "Step 1"
    else:
        url = f"https://docs.zid.sa/{slug}.md"
        # the accordion line that names the scope
        m = re.search(r"(`\s*" + re.escape(s) + r"\s*`[^<]*)", raw)
        q = re.sub(r"\s+", " ", m.group(1)).strip()
        q = q[:160]
        loc = "Scopes accordion"
    add("access-scopes", s, url, q, loc, "scope:" + s)

# 4. Settings sections (help centre category الإعدادات)
import zverify
cat = open(os.path.join(F, "help", "cat1.html"), encoding="utf-8").read()
txt = zverify.html_text(cat)
lines = [x for x in (re.sub(r"\s+", " ", l).strip() for l in txt.split("\n")) if x]
sub = None
start = lines.index("اضبط إعدادات متجرك وحسابك في زد وصلاحيات فريق العمل.") if "اضبط إعدادات متجرك وحسابك في زد وصلاحيات فريق العمل." in lines else 0
for i, l in enumerate(lines[start:], start):
    m = re.match(r"^(عام|التواصل|المتجر) جميع المقالات \((\d+)\)$", l)
    if m: sub = m.group(1); continue
    if l.startswith("تواصل معنا"): break
    if sub and l and i + 1 < len(lines) and lines[i + 1].startswith("آخر تحديث"):
        add("settings", f"{sub} › {l}", "https://help.zid.sa/category/%d8%a7%d9%84%d8%a5%d8%b9%d8%af%d8%a7%d8%af%d8%a7%d8%aa/", l, f"الإعدادات › {sub}", "set:" + l)

# 5. Help centre: Zid products and services categories (منتجات وخدمات زد)
c5 = zverify.html_text(open(os.path.join(F, "help", "cat5.html"), encoding="utf-8").read())
l5 = [re.sub(r"\s+", " ", l).strip() for l in c5.split("\n")]
i0 = l5.index("منتجات وخدمات زد ✨"); parent = None; seen5 = set()
for l in l5[i0 + 1:]:
    if l in ("Articles", "المقالات") and parent in ("زد نمو", "تطبيق الجوال") and parent not in seen5:
        pass
    if l.endswith(" -->"):
        parent = l[:-4].strip()
        add("other:help-centre-zid-products", parent, "https://help.zid.sa/category/zid-pay/", "منتجات وخدمات زد ✨", "sidebar منتجات وخدمات زد", "hp:" + parent)
        continue
    if l in ("-->", "", "Articles", "المقالات"): continue
    if l.startswith("تعرّف على إستقبال"): break
    if parent and (parent, l) not in seen5:
        seen5.add((parent, l))
        add("other:help-centre-zid-products", f"{parent} › {l}", "https://help.zid.sa/category/zid-pay/", l, f"sidebar منتجات وخدمات زد › {parent}", "hps:" + parent + "›" + l)

# 6. Plan features: compare table (pricing JS chunk) and plan cards (pricing page)
chunk = open(os.path.join(F, "js", "2501-f29c20b24ab64821.js"), encoding="utf-8").read()
for g in re.finditer(r'\{group:\{ar:"([^"]*)",en:"([^"]*)"\},features:\[', chunk):
    start = g.end(); depth, i = 1, start
    while depth and i < len(chunk):
        if chunk[i] == "[": depth += 1
        elif chunk[i] == "]": depth -= 1
        i += 1
    for f in re.finditer(r'\{name:\{ar:"([^"]*)",en:"([^"]*)"\},description:\{ar:"[^"]*",en:"[^"]*"\},plans:\{[^}]*\}\}', chunk[start:i - 1]):
        add("plan-features", f"{g.group(2)} / {g.group(1)} › {f.group(2)} / {f.group(1)}", "https://zid.sa/_next/static/chunks/2501-f29c20b24ab64821.js",
            f'name:{{ar:"{f.group(1)}",en:"{f.group(2)}"}}', f'compare-plans group {g.group(2)}', "plan:" + g.group(2) + "›" + f.group(2))
rsc = open(os.path.join(F, "txt", "en_pricing.rsc.txt"), encoding="utf-8").read()
for m in re.finditer(r'"pricingPlan_id":\{"id":"([^"]+)"', rsc):
    seg = rsc[m.start(): m.start() + 20000]
    nxt = seg.find('"pricingPlan_id"', 20)
    if nxt > 0: seg = seg[:nxt]
    en = re.findall(r'"packageName":"([^"]*)"', seg)[1]
    for f in re.finditer(r'\{"name":"([^"]*)","groupSubtitle":[^,]*,"languages_id":\{"name":"en"\}\}', seg):
        add("other:plan-cards", f"{en} › {f.group(1)}", "https://zid.sa/en/pricing/", f.group(1), f"plan card {en}", "card:" + en + "›" + f.group(1))

# 7. Legal agreements
legal = [("terms-conditions", "Terms & Conditions / الشروط والأحكام"), ("privacy-policy", "Privacy Policy / سياسة الخصوصية"),
         ("zidpay-terms-conditions-sa", "Zid Pay Terms and Conditions (Saudi Arabia) / شروط وأحكام زد باي"),
         ("zidpay-terms-conditions-kw", "Terms and Conditions for Zed Pay – Kuwait"),
         ("domestic-shipping-terms", "Domestic Shipping terms"), ("global-shipping-terms", "Global Shipping terms"),
         ("logistics-t-and-cs", "Logistics terms and conditions")]
for slug, name in legal:
    add("legal-agreements", name, "https://zid.sa/sitemap.xml", f"<loc>https://zid.sa/en/legal/{slug}</loc>", "sitemap.xml /legal/ entries", "legal:" + slug)
add("legal-agreements", "Zid Stores' Customer Complaints / شكاوي عملاء متاجر زد", "https://zid.sa/en/legal/terms-conditions/", "Zid Stores' Customer Complaints", "footer", "legal:complaints")
for h, q in [("خدمة وكيل زد (Zid Agent)", "خدمة وكيل زد (Zid Agent) آلية التنفيذ وحدود المسؤولية"),
             ("شركات الخدمات اللوجستية الطرف الثالث على متجر زد للتطبيقات (ZAM)", "شركات الخدمات اللوجستية الطرف الثالث على متجر زد للتطبيقات (ZAM)"),
             ("زد شب", "زد شب ما هي خدمة الشحن المباشر؟"), ("سوق تطبيقات زد", "سوق تطبيقات زد التعريفات"),
             ("سوق ثيمات زد", "سوق ثيمات زد التعريفات"), ("زد كاشير", "زد كاشير التعريفات"),
             ("محفظة زد", "محفظة زد ما هي محفظة التاجر في زد؟"), ("خدمة المميزات الإضافية VAS", "خدمة المميزات الإضافية VAS آلية التنفيذ وحدود المسؤولية"),
             ("مزيد", "مزيد تحكم هذه الشروط والأحكام"), ("زد باي", "زد باي زد باي هي خدمة تمكن التاجر"), ("تمويل زد", "تمويل زد التعريفات")]:
    add("legal-agreements", f"الشروط والأحكام › {h}", "https://zid.sa/ar/legal/terms-conditions/", q, "section heading", "legalsec:" + h)
add("legal-agreements", "Zid App Activation & OAuth Policy", "https://docs.zid.sa/zid-app-activation-oauth-policy-2422816m0.md", "# Zid App Activation & OAuth Policy", "title", "legal:oauth-policy")
for n in ("App Partner terms", "Theme Partner terms", "Theme commercial policy"):
    add("legal-agreements", n, "https://zid.sa/en/partners/developers/blog/partner-payouts/", n, "footer Terms & policies", "legal:" + n)

# 8. App Market categories (public categories endpoint used by apps.zid.sa)
cats = json.load(open(os.path.join(F, "apps", "categories.json"), encoding="utf-8"))
for c in cats["categories"]["apps_by_category"]:
    add("other:app-market-categories", c["name"], "https://api.zid.sa/v1/market/public/categories", f'"id":{c["id"]},"parent_id":null,"name":"{c["name"]}"', "categories.apps_by_category", "appcat:" + str(c["id"]))
    for s in c["subcategories"]:
        add("other:app-market-categories", f'{c["name"]} › {s["name"]}', "https://api.zid.sa/v1/market/public/categories", f'"id":{s["id"]},"parent_id":{c["id"]},"name":"{s["name"]}"', "subcategories", "appcat:" + str(s["id"]))

# 9. Zid's product lines (zid.sa header Solutions menu)
nav = [("E-store", "Turn Your Idea into a Thriving E-Store"), ("POS (Point of Sales)", "Manage your Branches From One Dashboard"),
       ("Payments", "Receive and Manage Payments with Ease"), ("Shipping", "Smart Shipping Solutions"),
       ("Inventory Management", "Streamline and track your inventory effortlessly"), ("Zid Voice", "Recover abandoned carts with a voice agent"),
       ("Apps", "400+ Apps For Your Business Growth"), ("Themes", "Customize Your Store, Your Way."),
       ("Mazeed Marketplace", "Double Your Sales and Get More Orders"), ("Financing", "Flexible Funding For Your Business Growth"),
       ("Marketing Tools", "Turn Your Store into a Customer Magnet"), ("Marketplaces", "Sold on Amazon and Trendyol and Jahez"),
       ("ZID Assurance", "Boost your customers' trust and increase purchase rates"), ("Whatsapp", "Whatsapp")]
for n, d in nav:
    q = n + d if n != "Whatsapp" else "Whatsapp\nPricing"
    add("other:product-lines", n, "https://zid.sa/en/solutions/payments/", q, "header menu Solutions", "pl:" + n)

# 10. Countries (zid.sa/llms.txt, "Other countries")
for name, slug in [("Egypt", "egypt"), ("UAE", "uae"), ("Kuwait", "kuwait"), ("Oman", "oman"), ("Syria", "syria")]:
    add("other:countries", name, "https://zid.sa/llms.txt", f"- [{name}](https://zid.sa/en/{slug}/)", "## Other countries", "country:" + name)

# 11. Staff permissions (docs.zid.sa User Roles and Permissions, List of Available Permissions)
ur = open(os.path.join(F, "docs", "-user-roles-and-permissions-604944m0.md"), encoding="utf-8").read()
for m in re.finditer(r"^\| `([a-z.]+)`\s*\| ([^|]+?)\s*\| ([^|]+?)\s*\|$", ur, re.M):
    q = f"`{m.group(1)}` | {m.group(2)} | {m.group(3)}"
    add("other:staff-permissions", f"{m.group(1)} ({m.group(2)} / {m.group(3)})", "https://docs.zid.sa/-user-roles-and-permissions-604944m0.md", q, "List of Available Permissions", "perm:" + m.group(1))

# 12. App types (docs.zid.sa Overview, "App Types"): the extension points an app can take
ov = "https://docs.zid.sa/zid-apps-overview.md"
for grp, name, q in [("Subscription Apps", "Public apps", "**Public apps:** Apps designed for wider use and are listed in Zid App Market."),
                     ("Subscription Apps", "Private apps", "**Private apps:** Apps intended for specific stores only."),
                     ("Shipping apps", "Shipping and fulfillment company", "**Shipping and fulfillment company:** Apps that connect merchants with companies that handle both shipping and fulfillment."),
                     ("Shipping apps", "Shipping company only", "**Shipping company only:** Apps that are focused only on the shipping aspect.")]:
    add("extension-points", f"{grp} › {name}", ov, q, "# App Types", "apptype:" + name)

for i, e in enumerate(out, 1):
    e["inv_id"] = f"ZD-I-{i:04d}"
json.dump(out, open(os.path.join(F, "inventory.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(out), Counter(e["list"] for e in out))
