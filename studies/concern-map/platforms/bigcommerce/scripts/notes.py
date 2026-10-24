# Fill notes_template.md with counts from final/ and write final/notes.md.
import csv, collections, os
B = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/bigcommerce"
F = B + "/final/"
def rd(n):
    with open(F + n, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
inv, con, cit, st, gp, nr = (rd(x) for x in ("inventory.tsv", "concerns.tsv", "citations.tsv", "statements.tsv", "gaps.tsv", "not-reached.tsv"))
where = {
    "api-resources": "Developer docs index (`developer/llms.txt`), API reference pages; GraphQL API Overview; Beta groups in the index's API Docs section",
    "webhook-topics": "Webhook Events, Channel Webhooks, Inventory and location events, B2B Edition Webhooks",
    "access-scopes": "API Accounts page, OAuth scopes tables",
    "settings": "Settings V3 API reference, \"Available settings and configuration\"",
    "plan-features": "Pricing page, Compare plans tables (raw HTML)",
    "legal-agreements": "MSA, Incorporated Terms list, and footer links (Website Terms of Use, Legal Archives)",
    "other:product-lines": "Product page, All Features",
    "other:app-marketplace-categories": "Apps & Integrations page, All Categories",
    "other:embedded-payment-providers": "Pricing page, Embedded Payment Provider List",
    "other:contracting-entities": "MSA, Contracting Entity table",
    "other:subprocessors": "Third-Party Subprocessors page",
}
cnt = collections.Counter(r["list"] for r in inv)
oos = collections.Counter(r["list"] for r in inv if not r["concern_ids"])
lists = "\n".join(f"| `{k}` | {where[k]} | {v}" + (f" ({oos[k]} out of scope)" if oos[k] else "") + " |" for k, v in cnt.most_common())
P = ["where", "decides", "responsible", "boundary", "reason"]
cs, cg = collections.defaultdict(set), collections.defaultdict(set)
for r in st: cs[r["placement"]].add(r["concern_id"])
for r in gp: cg[r["placement"]].add(r["concern_id"])
cells = "\n".join(f"| {p} | {len(cs[p])} | {len(cg[p] - cs[p])} | {sum(1 for r in st if r['placement'] == p)} |" for p in P)
extra = sum(1 for r in gp if r["concern_id"] in cs[r["placement"]])
kinds = ", ".join(f"{k} {v}" for k, v in collections.Counter(r["gap_kind"] for r in gp).most_common())
who = ", ".join(f"{k} {v}" for k, v in collections.Counter(r["who_can"] for r in gp).most_common())
t = open(B + "/scripts/notes_template.md", encoding="utf-8").read()
for k, v in dict(INV=len(inv), CON=len(con), CIT=len(cit), ST=len(st), GP=len(gp), NR=len(nr), LISTS=lists, CELLS=cells,
                 EXTRA_GAPS=extra, KINDS=kinds, WHO=who).items():
    t = t.replace("{" + k + "}", str(v))
runs = [open(B + "/capture/" + x).read().strip() for x in ("RUN1", "RUN2")]
t += "\n## Capture and check\n\n"
t += f"- **Captures:** the cited web pages were captured with `method/capture/run.sh` (CAPTURE_LANG `en,ar;q=0.8`) in two runs: `{os.path.basename(runs[0])}` (120 URLs) and `{os.path.basename(runs[1])}` (23 URLs added after the guide pages were read). Both runs are under `q1n/bigcommerce/capture/`. All 143 URLs were captured; the 16 commerce.com pages were captured through the browser.\n"
t += "- **Checker:** `method/check_concern_map.py` was run on `check/run/bigcommerce` (a symlink to `final/`) with both capture runs. It reported no issues. All citation quotes were found: most exactly, the rest in the \"markup removed\" form, which drops markdown pipes, backticks and links.\n"
t += "- **Working copies:** every working-copy fetch is logged in `fetched/log.tsv`, along with the debugging requests made to diagnose the Help Center. One stray request went to `0.0.0.32` when a count line was read as a URL; the proxy refused it.\n"
open(F + "notes.md", "w", encoding="utf-8").write(t)
print("notes.md written:", len(t), "chars")
