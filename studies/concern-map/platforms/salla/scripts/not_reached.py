# Write not-reached.tsv: salla.com pages needed for the concern map, taken verbatim from the held sitemaps.
# Usage: python3 -I not_reached.py
import os, re, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import OBS, OUT

TESTED = "403 (bot challenge page 'Just a moment...'), requested 2026-10-10T23:40:57Z"
UNTESTED = "not requested: salla.com answers 403 with a bot challenge from this session (tested on https://salla.com/terms)"

NEED = [
    ("/terms", "SA-C-170 terms of use; SA-C-230 legal entities; SA-C-110/111 holding money; SA-C-232 restricted activity; SA-C-233 data",
     "The entity that contracts with the merchant in this market (name, registration number, country); governing law and courts; whether Salla collects and holds sale proceeds, and on whose behalf; payout holds, reserves and set-off; suspension and restricted activities; liability split between Salla, merchant and partners."),
    ("/policies/terms", "SA-C-170 terms of use; SA-C-230 legal entities",
     "Whether this is the same document as /terms or a different one; contracting entity and date of the version; anything on payments, holds and termination."),
    ("/privacy", "SA-C-171 Salla privacy policy; SA-C-233 where data lives; SA-C-066 customer data",
     "Where store, customer and payment data are stored and processed (country, cloud provider); cross-border transfers; Salla's role (controller or processor) for merchants' customer data; sub-processors and partners that receive data; retention."),
    ("/policies/privacy", "SA-C-171 Salla privacy policy; SA-C-233 where data lives",
     "Same as /privacy; whether the two pages differ."),
    ("/policies/selling-policies", "SA-C-172 selling policy; SA-C-232 restricted activity and screening; SA-C-111 payouts",
     "The selling policy merchants accept when activating e-payments: prohibited products and activities, sanctions or screening wording, chargebacks and disputes, holds on funds, the party that processes payments."),
    ("/policies/nd96", "SA-C-180 policy at /policies/nd96",
     "The title and subject of this policy, its date, and which concern it governs."),
    ("/policies/publising-app-maker", "SA-C-174 App Maker publishing policy; SA-C-094 store mobile app",
     "Who publishes the store app in Apple and Google stores (Salla or the merchant's developer account), who is responsible for the app's content, and fees."),
    ("/policies/اتفاقية-استخدام-التسويق-بالعمولة", "SA-C-173 affiliate programme terms; SA-C-072 store affiliates",
     "The contracting entity, how commissions are paid and taxed, and whether this differs from the partners.salla.com affiliate agreement."),
    ("/اتفاقية-استخدام-التسويق-بالعمولة", "SA-C-173 affiliate programme terms",
     "Same as the /policies/ version; whether the two pages differ."),
    ("/payments", "SA-C-110 Salla Payments; SA-C-114 processor and licence; SA-C-111 payouts; SA-C-113 fees; SA-C-164 settlement currency",
     "Who processes or acquires card and mada payments for Salla Payments and under which licence or bank partner; fees; payout timing; currencies accepted and settled; which methods are offered in this market."),
    ("/sallacapital1", "SA-C-128 financing",
     "Who provides the financing (Salla, a fund, a bank), its licence, the contract, and how repayments are taken from sales."),
    ("/tamara", "SA-C-118 buy now, pay later",
     "Salla's arrangement with Tamara: who contracts with the merchant, fees, and who bears credit risk."),
    ("/shipping", "SA-C-140 Salla shipping labels; SA-C-115 COD via Salla labels; SA-C-235 partner failure",
     "Carriers per market, who contracts with the carriers, COD collection and remittance, and what happens when a carrier fails or is unavailable."),
    ("/salla-crossborder", "SA-C-146 international shipping; SA-C-162 customs duties; SA-C-163 currencies",
     "Who pays customs duties and taxes on cross-border orders, which currencies buyers pay in and how conversion rates are set."),
    ("/uae-quiqup", "SA-C-140 shipping in the UAE; SA-C-167 markets served",
     "The delivery partner offered to UAE stores and who contracts with it."),
    ("/mrsool", "SA-C-139 carrier integrations",
     "The delivery partner arrangement and who contracts with it."),
    ("/gcc-ecommerce", "SA-C-167 markets served; SA-C-230 legal entities",
     "Which GCC countries Salla serves now, whether Salla has an entity in each, and what differs per country (payments, shipping, tax)."),
    ("/faq", "SA-C-167 markets served; SA-C-110 Salla Payments",
     "Answers to 'Can I use Salla outside Saudi Arabia?' and to the payment methods question, which the held plans page shows only as headings."),
    ("/sallapoint", "SA-C-095 Salla Point",
     "Card acceptance at the point of sale: who processes in-person payments and under which licence."),
    ("/mahally", "SA-C-096 Mahally",
     "Fees or commission Mahally charges, who is the seller of record, and who handles payment and returns."),
    ("/strategic-partner", "SA-C-235 partners",
     "Salla's named strategic partners and their roles."),
]


def sitemap_urls():
    out = []
    for sm in ("sitemap_ar-SA.xml", "sitemap_en-SA.xml", "sitemap_ar-AE.xml", "sitemap_en-AE.xml"):
        for l in open(os.path.join(OBS, "salla.com", sm), encoding="utf-8"):
            m = re.search(r"<loc>(https://salla\.com/[^<]*)</loc>", l)
            if m:
                out.append((sm, m.group(1)))
    return out


rows = []
urls = sitemap_urls()
for path, needed, what in NEED:
    found = False
    for sm, u in urls:
        p = urllib.parse.unquote(urllib.parse.urlparse(u).path)
        p2 = re.sub(r"^/(en-sa|ar-ae|en-ae)(?=/|$)", "", p) or "/"
        if p2 == path:
            found = True
            st = TESTED if u == "https://salla.com/terms" else UNTESTED
            rows.append((u, st, needed + f" (listed in held salla.com/{sm})", what))
    if not found:
        print("not in sitemaps:", path)
# pages named in Salla's held llms-full.txt but absent from the sitemaps
for u, needed, what in (
    ("https://salla.com/uae", "SA-C-167 markets served; SA-C-230 legal entities (named in held salla.com/llms-full.txt)",
     "What Salla offers UAE merchants, which entity serves them, and UAE-specific payments, shipping and tax."),
    ("https://salla.com/uae/store-checklist", "SA-C-006 verification; SA-C-231 licences (named in held salla.com/llms-full.txt)",
     "Licences and documents a UAE store needs, and which are Salla's requirements versus the authorities'."),
):
    rows.append((u, UNTESTED, needed, what))
rows.append(("https://salla.sa/", "403 (bot challenge page 'Just a moment...'), requested 2026-10-10T23:40:58Z",
             "SA-C-230 legal entities (salla.sa is named as Salla's Arabic site in held salla.com/ai-info)",
             "No specific page is needed beyond the salla.com pages above; listed because the host refuses this session."))
seen = set()
with open(os.path.join(OUT, "not-reached.tsv"), "w", encoding="utf-8") as f:
    f.write("url\tstatus\tneeded_for\twhat_to_look_for\n")
    for r in rows:
        if r[0] in seen:
            continue
        seen.add(r[0])
        f.write("\t".join(x.replace("\t", " ").replace("\n", " ") for x in r) + "\n")
print("rows", len(seen))
